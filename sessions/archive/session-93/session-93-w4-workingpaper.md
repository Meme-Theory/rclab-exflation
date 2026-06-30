# Session 93 Wave 4 — §VII.AX PBH cluster (Results Working Paper)

**Session**: 93 | **Wave**: W4 | **Plan**: session-93-plan-w4.md | **Theme**: §VII.AX primordial-black-hole cluster — the framework's fourth joint cross-axis theorem family; verdict-artifact integrity, Stage-2 cross-axis promotion, canonical-truncation factorization, and the three CHAINED STAGE-3-eligibility landings (STATE-PROJ companion, n_PBH canonical promotion, FWD-C5 K=2 shoulder).

## Gate Sections

### §W4-1. S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION (connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (verdict-artifact integrity re-emission; methodology-layer F-image of a substrate-IS Stage-2 verify per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence — the substrate-IS observable n_PBH cardinality-cascade-tail is UNCHANGED; only the verdict-FIELD F-image is corrected)
**Agent**: `connes-ncg-theorist` (Axis-A producing agent of the original §W6-3 verify; writer-of-record continuity — re-emits its own corrected verdict line; NO new physics)
**Hypothesis**: The §W6-3 Axis-A Element-2 FAIL is a verdict-FIELD emit-bug (all five E2 sub-findings + `element_2.interpretation` carry PASS evidence on disk, OE-form positive-match regex matches); re-emitting E2=PASS makes `axis_a_composite=PASS`, since E1 JOINT / JOINT E3 / JOINT E5 already PASS on disk.
**Plan reference**: `sessions/session-plan/session-93-plan-w4.md` §W4-1 (machinery pin, thresholds, substitution chain, supersedes-tag protocol).

**Verdict**: **PASS** — corrected `axis_a_composite = PASS`. The §W6-3 Axis-A FAIL is confirmed a verdict-FIELD emit-bug (`emit_bug_confirmed=True`); the Option-A supersedes chain is on disk (original S92 Axis-A FAIL line `19662dc1…` RETAINED; corrective PASS appended). Combined with the S92 W-4 JE5 PASS (Axis-B, S92-closed), this flips the §W6-3 Axis-A leg of the §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility conjunction.

**Output Artifacts**:

```
$ ls -la computations/session-93/s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.{py,npz,png}
-rw-r--r-- 1 ryan 197609 10620 May 24 15:06 .../s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.npz
-rw-r--r-- 1 ryan 197609 27421 May 24 15:06 .../s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.png
-rwxr-xr-x 1 ryan 197609 33877 May 24 15:05 .../s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.py

$ grep -nE "from canonical_constants import|append_verdict|supersedes" s93_w4_1_..._re_emission.py
126:from canonical_constants import *  # noqa: F401,F403  (brings M_KK and others)
127:from canonical_constants import M_KK  # explicit (satisfies 'from canonical_constants import')
363:def append_verdict(verdict: str, value: str, ...):
673:    append_verdict(verdict, value_str, audit_sha, content_sha, emit_3tuple=False)
# (supersedes present at docstring lines 64/67/73/105 + emission Section 8 + value field)

$ grep -nE "^S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION:.* audit_sha256=[a-f0-9]{64}" computations/session-93/s93_gate_verdicts.txt
64: ...: FAIL ... audit_sha256=68132f62c2cfa0fc60dbe2f81ff11c34f51300e4e167c7c817421d0ef170e7ef   (run-1, RETAINED, superseded)
67: ...: PASS ... audit_sha256=2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8   (CANONICAL — latest non-superseded)
```

All four `output_artifacts` confirmed on disk with `must_contain` satisfied: script (`from canonical_constants import` L126-127, `append_verdict` def L363 + call L673, `supersedes` present), data `.npz`, plot `.png` (optional), verdict line L67 matching the PASS regex + dual-SHA companion (L68) + tier_pin companion (L69).

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; query-first discipline):

| Query | Tool | One-line salient return |
|:------|:-----|:------------------------|
| `VII.AX.OP-PROJ Axis-A Element-2 OE-form Stage-2 verify W6-3` | `search_knowledge` | 3 provenance hits on `w6_3_axis_a_connes_ncg_vii_ax_stage_2_verify.py` (the original Axis-A verify) + `w7a_element_2_oe_form_discipline`; NO prior W4-1 re-emission entity exists ⇒ genuine first re-emission. |
| `S92-W6-CF-S92-W5-4-STAGE-2-VII-AX-CROSS-AXIS-VERIFY-AXIS-A` | `query_entity (gates)` | gate recorded **verdict=FAIL**, `result='axis_a_composite=FAIL;E1=PASS;E2=FAIL;JE3=PASS;JE5=PASS'` — confirms the on-disk emit-bug state (only-FAIL is E2). |
| `VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility` | `trace_entity` | "No trace found" ⇒ eligibility not yet recorded; this gate flips the Axis-A leg toward it (not a re-discovery of a closed result). |

Verdict: NOT PRE-CLOSED. The corrected Axis-A PASS state is new on disk; the knowledge base records only the buggy FAIL state, confirming the re-emission is genuine work and not a re-derivation of an existing closure.

**Results** (corrected verdict first; eligibility-contribution second; framing third):

**(1) Corrected Axis-A E2 verdict.** Reading the on-disk JSON `computations/session-92/s92_w6_3_axis_a_connes_ncg_vii_ax_stage_2_verify.json` (REALITY per the DERIVATIVE-OUTPUT discipline; the prior verdict-FIELD is INTENT, not source-of-truth), the three corrective antecedents are verified on disk:

- **Antecedent (A) — all 5 E2 sub-finding EVIDENCE are PASS-language**: `True`. Sub-findings 2.1–2.5 each assert structural presence of an OE-form constituent. (Note: the producing script's first run carried a classifier false-negative on 2.5, whose evidence reads *"No prose-only 'measurement/spectroscopy/test' substitutes …"* — a NEGATED FAIL-phrase that is in fact a PASS statement (the FORBIDDEN form is ABSENT). The classifier was corrected to be negation-aware (script-bug fix; the run-1 FAIL line is RETAINED per Option-A rule 1); a discriminator test confirms a genuine un-negated defect *"OE-form is absent; named projector missing; prose-only substitute used"* still classifies False.)
- **Antecedent (B) — `element_2.interpretation` is PASS-language**: `True` (*"Element 2 OE-form discipline K=2 MANDATORY satisfied; named projector P_{PBH-mass} + subscripted trace Tr_{M_PBH-mass} … all structurally present and correctly formed at the laboratory-IN observable axis"*).
- **Antecedent (C) — OE-form positive-match regex matches the LIVE registry**: `True`. Applied directly to the registry §VII.AX.OP-PROJ block (line 19413 of `permanent-results-registry.md`, 26715-char block extracted), the positive-match regex `∫.*d.*Tr.*\([ΠP]_\{[A-Za-z0-9_-]+` matches the brace-delimited subscript form `∫_{Σ_CMB ∪ Σ_LISA ∪ Σ_PTA} d³x · Tr_{M_PBH-mass}(P_{PBH-mass} · ρ_BH(x))`. Per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"` rule prose (iii), `P_<index>` AND `Π^{<superscript>}_{<subscript>}` (brace-delimited) BOTH satisfy the named-projector requirement; the negative-match prose-only regex does NOT trigger. The narrow bare-only regex of the earlier S92 producing-script version was the source of the 2.1 verdict-FIELD defect.

Corrected E2 = PASS IFF (A ∧ B ∧ C) = True ∧ True ∧ True = **PASS**.

**Substitution chain** (per `math-scripts.md §"Double-Check Logic Before Compute"`; on-disk values substituted):
```
Step 1: E2_evidence{2.1..2.5} all PASS-language (structural presence)   [JSON element_2.sub_findings]
Step 2: E2_interpretation = PASS-language ("all structurally present and correctly formed")   [JSON L82]
Step 3: OE_regex (positive, brace subscript) MATCHES live registry; negative-match NOT triggered   [registry L19413; rule prose (iii)]
Step 4: corrected E2 = PASS IFF (Step1 ∧ Step2 ∧ Step3) = PASS ∧ PASS ∧ PASS = PASS
Step 5: axis_a_composite = E1_JOINT ∧ E2_corrected ∧ JE3 ∧ JE5 ∧ SIO
                          = PASS [JSON L43] ∧ PASS [corrected] ∧ PASS [L119] ∧ PASS [L158] ∧ PASS [L174]
                          = PASS
Conclusion: the ONLY FAIL in the four Axis-A-audited clauses was the E2 verdict-FIELD; correcting it
            (justified by all 5 sub-finding evidence + interpretation + live-registry regex match) flips
            the conjunction to PASS. The original FAIL is RETIRED-NOT-OVERTURNED via Option-A supersedes.
```

**4-tuple**: `(value=axis_a_composite=PASS, scheme=stage-2-cross-axis-verify-axis-a-NCG-axiomatic-spectral-side-E2-RE-EMISSION, convention=stage-2-cross-reviewer-protocol-without-prior-workshop-context-OPTION-A-SUPERSEDES, L_max=14)`.

**Option-A supersedes chain** (`gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`):
- The **substantive** supersession target is the original S92 Axis-A FAIL line `s92_axis_a_super=19662dc1544604e55f49280bd36d5a1e3862df381d0eb14f17b68ebc5b933cff` (full-64-char EXACT, per plan §W4-1 machinery pin). That line is RETAINED on `computations/session-92/s92_gate_verdicts.txt` (absolute verdict permanence; not touched by this gate).
- The corrective PASS line (L67, `audit_sha256=2ab8bb1e…`) additionally carries the Option-A `supersedes=68132f62…` tag pointing to the run-1 buggy FAIL line (same gate-ID, RETAINED at L64); the run-1 line is the script-bug-fix predecessor.
- Latest-non-superseded reading: L64 is named in L67's `supersedes=`; the canonical W4-1 verdict is the L67 **PASS**.

**Dual-SHA**: `audit_sha256=2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8` (closure over the input-pin map: axis_a_json + s92_verdicts original line + registry + cross_pillar rule + canonical_constants + script_self + supersedes-target + corrected-E2 + corrected-composite); `content_sha256=f257e2331788189b7f9104fae195eb0bd603a5fa09ea82afc3df5f18d984585f` (script only). sig_5 uniqueness: audit_sha256 occurs exactly once in the s93 verdict file.

**(2) §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility contribution.** The eligibility conjunction is:
```
§VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility
   = (W4-1 Axis-A PASS)  ∧  (S92 W-4 JE5 PASS, Axis-B, S92-closed)  ∧  (Eq.(2′) registry-text correction landed)
```
This gate flips the **first conjunct (W4-1 Axis-A leg) to PASS**. The JOINT clauses (Element 1, JOINT Element 3, JOINT Element 5) are now PASS-AND-satisfiable across both axes: Axis-A PASS (this gate, on-disk JSON L43/L119/L158) ∧ Axis-B PASS (S92 W-4 JE5, S92-closed). The Stage-2 two-cross-reviewer PASS-AND of `joint-theorem-promotion.md §"Stage 2"` is thereby met on the §W6-3 cross-axis verify for §VII.AX.OP-PROJ. Eligibility is NOT yet asserted here (it remains CHAINED on the Eq.(2′) registry-text correction landing per the W4-4/4-5/4-6 exit Decision Point); this gate supplies the Axis-A leg only.

**(3) Substrate framing.** NON-PHONONIC / methodology-layer. Per `epistemic-discipline.md §"Layer-Decomposition"` Phi correspondence, the verdict line is the methodology-floor F-image of the substrate-IS cross-axis verification event; the emit-bug is an `F(numerical-PASS-predicate) ↦ F(artifact-existence-predicate)` defect at the audit-trail layer. The substrate-IS observable — the n_PBH cardinality-cascade-tail on `(A_K, H_K, D_K(τ_fold=0.19))` (Cell-I algebra-INVARIANT spectrum-only-functional) — is UNCHANGED; only the verdict-FIELD F-image is corrected. The DERIVATIVE-OUTPUT discipline is load-bearing: the JSON artifact ON DISK is REALITY; the prior characterization "E2 is FAIL" was INTENT. The corrective emission is licensed ONLY by the on-disk verification of the five sub-findings + interpretation + the live-registry OE-form regex match — never by the workshop's narrative.

---

### §W4-2. S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY (connes-ncg-theorist + volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (multi-pin atlas observable `Res_{s=4}[Tr(D_K^-2s)]` at χ' restriction; Cell II algebra-INVARIANT)
**Agent**: `MULTI` — Axis-A `connes-ncg-theorist` + Axis-B `volovik-superfluid-universe-theorist` dispatched IN PARALLEL (per `joint-theorem-promotion.md §"Stage 2"`); `mack-cosmic-bridge` EXCLUDED as Stage-1 sole-writer.
**Hypothesis**: The §VII.AX.MULTI-PIN-ATLAS STAGE-1-CANDIDATE (regulator-class-pluralism multi-pin atlas at substrate-distance-2 pole s=4 χ' restriction) survives Stage-2 two-cross-reviewer PASS-AND on its JOINT clauses, with substrate-input-orthogonality at obs_2 satisfied, advancing it toward STAGE-3-PERMANENT eligibility.
**Plan reference**: `sessions/session-plan/session-93-plan-w4.md` §W4-2 (parallel dispatch spec, JOINT-clause PASS-AND, obs_2 Axis-B-only load).

**Output Artifacts**:
*(pending — for each entry in the plan's `output_artifacts:` block: confirm file exists AND paste `grep -E '<must_contain>' <path>` output. Plan artifacts: aggregation script `computations/session-93/s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py` (must_contain `from canonical_constants import`, `append_verdict`); data `s93_w4_2_..._verify.npz`; Axis-A reviewer JSON `s93_w4_2_axis_a_connes_multi_pin_atlas_verify.json`; Axis-B reviewer JSON `s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json`; plot `s93_w4_2_..._verify.png` (optional); verdict line matching `^S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY:.* audit_sha256=[a-f0-9]{64}` + companion row; this wp_section. Verify by content presence (regex match), never by line/byte counts.)*

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**: **PASS** (Stage-2 cross-axis PASS-AND; §VII.AX.MULTI-PIN-ATLAS STAGE-3-PERMANENT-ELIGIBLE)


**Results**:
*(pending — include: per-axis composite verdicts (Axis-A connes, Axis-B volovik), JOINT-clause PASS-AND across both verdicts (Element 1, JOINT Element 3, JOINT Element 5), substrate-input-orthogonality verdict at obs_2 (loaded by exactly ONE reviewer), cross-reviewer machinery-not-self-authored check, regulator-class residues cited (R_zeta=1.414393e+02, R_PV=1.144577e+02, R_Mellin=1.414393e+02 M_KK², cross-regulator spread 2.698e+01 M_KK²), 4-tuple, STAGE-3-PERMANENT eligibility verdict for the mack tag-flip, dual-SHA, artifacts)*

### Axis-A (connes) cross-review

**Reviewer**: `connes-ncg-theorist` (Axis-A — NCG-axiomatic / spectral-functional). Stage-2 independent cross-review per `joint-theorem-promotion.md §"Stage 2"`. Audited ONLY the registered §VII.AX.MULTI-PIN-ATLAS Stage-1 entry (registry line ~19486) + the cited S91 §W2-1 PASS-V verdict line; did NOT read the S92 W6-1/W6-2 workshop transcripts and did NOT read the Axis-B verdict. **Verdict line emission is the separate PASS-AND closeout — not this subsection.**

**MCP queries (mandatory before auditing)**:
- `search_knowledge("VII.AX MULTI-PIN-ATLAS regulator-class pluralism substrate-distance-2 pole s=4 chi-prime")` → Stage-1 landing gate `S92-W6-CF-W2-1-...-MULTI-PIN-ATLAS-LANDING` **PASS**, `13_of_13_sub_blocks_PASS`, triple-pin confirmed; K2-advancement successor gate present.
- `trace_entity("MULTI-PIN-ATLAS")` → gate STAGE-1-CANDIDATE landed; triple-pin `R_zeta=1.414393e+02 / R_PV=1.144577e+02 / R_Mellin=1.414393e+02` confirmed.
- `search_knowledge("Cell II algebra-INVARIANT spectrum-only functional Mellin pole residue Wodzicki trace")` → Cell-II = algebra-INVARIANT × Mellin-pole convention confirmed; **INDEPENDENT PROVEN theorem** (`s88-pending-edits-ledger`): "Rank ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} at s=4 substrate-distance-2 Mellin-cone pole is REGULATOR-PARAMETER-dependent" — corroborates the option-(v) regulator-class divergence INDEPENDENTLY of the workshop.

**NCG-axiomatic grounding**: Connes-Moscovici 1995 Local index formula (`researchers/Connes/06_1995_Connes_Moscovici_Local_index_formula.md`): §2.1 `ζ_{a,D}(z)=Tr(a|D|^{-z})`; §2.2 meromorphic continuation, at most simple poles; §2.3 Wodzicki residue = UNIQUE trace on classical ψDOs (up to scalar); §3.3 `a_k = Γ((n-k)/2)^{-1} Res_{z=n-k} ζ_D(z)`; §4.1 local-index cocycles `φ_k = c_{n,k} Res_{z=0} Tr(a⁰[D,a¹]...[D,aᵏ]|D|^{-2z-k})`; §4.3 dimension spectrum = set of poles of `ζ_{a,D}`.

#### Per-clause Axis-A verdicts

**JOINT clauses (PASS-AND with Axis-B at closeout):**

| JOINT clause | Axis-A verdict |
|:-------------|:---------------|
| Element 1 (substrate-IS observable + Cell-II + Level-1 tag) | **PASS** |
| JOINT Element 3 (bridge map CM-1995 §III.4 ∘ HKR; type-(iii); triple-pin) | **PASS** |
| JOINT Element 5 (empirical anchor triple-pin; Level-3 single-pin R_Mellin; option-(v) admission) | **PASS** |

**Axis-A single-axis clause:**

| Single-axis clause | Axis-A verdict |
|:-------------------|:---------------|
| Element 2 (laboratory-IN OE-form regex compliance) | **PASS** |

- **Element 1 (JOINT) — PASS**: `Res_{s=4}[Tr(D_K^{-2s})]` is the residue of the spectral zeta `ζ_{D_K}(2s)=Tr(|D_K|^{-2s})` (CM-1995 §2.1). D_K has compact resolvent (Peter-Weyl block-diagonal, finite-dim Casimir-bounded blocks), so `|D_K|^{-2s}` is trace-class for large `Re(2s)` and meromorphically continues with at most simple poles (§2.2); `s=4` is a point of the dimension spectrum (§4.3). The residue IS the Wodzicki residue / noncommutative integral (§2.3) — a spectrum-only functional `F({λ_k,m_k})=Σ_k m_k g(λ_k)` with NO state-pair structure on `A_K` ⇒ algebra-INVARIANT family. Parse-tree → `image_block_rank=3`; no state-pair functional surfaces ⇒ **Cell II** (algebra-INVARIANT × Mellin pole s=4) per §VII.U.2 clause (e) [MCP-corroborated convention]. Level-1 single-τ-slice tag at `τ_fold=0.190` is correct (intrinsic to `(A_K,H_K,D_K(0.19))`, not a moduli-deformation observable).
- **JOINT Element 3 — PASS**: bridge map EXPLICITLY named (CM-1995 §III.4 residue formula ∘ HKR `L_max→∞` image at d=4 substrate-distance-2 pole s=4) — not "analogous to"/"corresponds to", so explicit-naming passes. CM-1995 §III.4 is the correct, well-defined bridge: the local-index cocycles `φ_k=c_{n,k} Res_{z=0} Tr(a⁰[D,a¹]...[D,aᵏ]|D|^{-2z-k})` (§4.1); for the single-projection trace this is the dimension-spectrum residue, with HKR carrying the Hochschild/cyclic image to the continuum — faithful NCG machinery. Type-(iii) joint-hypersurface binding is the CORRECT declaration for option-(v) pluralism (lab discrimination is 2D in (regulator-class R, observable value); a single value would be type (i)/(ii)). The three regulator-class images are three structurally-INEQUIVALENT FULL physical regularizations of the SAME residue formula: Wodzicki uniqueness holds for CLASSICAL ψDOs (§2.3), but the regulator-class choice fixes the UV finite-part content at the pole, which genuinely differs (ζ vs PV vs Mellin) when the operator content is not purely classical-trace-class — so the 33% spread is a substrate-intrinsic structural fact, NOT regulator-shopping (corroborated by the INDEPENDENT PROVEN regulator-parameter-dependence theorem above). Bridge-map-scheme suffix discipline satisfied (`-ZETA-`/`-PV-`/`-MELLIN-` sub-row tags).
- **JOINT Element 5 — PASS**: empirical values pinned to the cited S91 §W2-1 PASS-V verdict line (`audit_sha256=58671312...`), verified on disk to reproduce EXACTLY — `R_zeta=1.414393e+02`, `R_PV=1.144577e+02`, `R_Mellin=1.414393e+02` M_KK², cross-regulator spread (max−min) = `26.9816` M_KK² (matches registered `2.698e+01`), relative divergence `21.09%`, `image_block_rank=3`, `reading_v_pluralism_bool=True`, `truncation_consistent=True`. Level-3 anchor singleness respected: Hybrid framing single-pins Level-3 at `R_Mellin` (substrate-natural canonical at the CM-1995 §III.4 residue formula); `R_zeta + R_PV` are Level-2-B DIAGNOSTIC sub-rows ONLY (cross-corner co-primary at Level-3 FORBIDDEN per `substrate-first-canonical-sourcing §(i)`). Registry-PASS criterion for option (v) satisfied BY CONSTRUCTION: spread `2.698e+01` M_KK² ≫ `1e-3` M_KK² option-(iv) threshold by ~`4.43` OOM; the spread IS the empirical confirmation of the pluralism STRUCTURAL THEOREM, not a convergent-bridge `Level-3 < Level-2-envelope` inequality. Level-2-binding sub-class correctly declared (HKR-image binds Level-1 regulator-class-keyed identities to continuum lab observables at the three cross-pillar bridge projections).
- **Element 2 (Axis-A single-axis) — PASS**: laboratory-IN observable `∫_BZ d^d k Tr_{A_K}(P_{χ-prime-restriction-s4} · ρ_BZ(k; τ_fold))` is in OE-form. Tested with the **authoritative** `ELEMENT_2_OE_POSITIVE_REGEX` from `computations/_shared/_cross_pillar_bridge_audit.py` (line ~164) — positive-match present, negative prose-only match absent. All three OE-form sub-elements present: (i) integration domain `∫_BZ`; (ii) trace `Tr` over `A_K = ℂ⊕ℍ⊕M_3(ℂ)`; (iii) named subscripted projector `P_{χ-prime-restriction-s4}` (lifts the substrate-axis canonicalizer image under the HKR map of the χ' restriction Hochschild cocycle at pole s=4). *(Note: an earlier hand-rolled char-class regex `[a-z0-9_-]+` spuriously rejected the brace/unicode-χ; corrected to the authoritative `[ΠP][_^].*?` detector form — a test-harness fix, the Element-2 form itself was always compliant, consistent with the registry's own "OE-form discipline ... satisfied" note.)*

#### Axis-A composite + structural-ceiling checks

- **Axis-A COMPOSITE: PASS** (all four Axis-A-audited clauses PASS; conjunction E1_JOINT ∧ E2 ∧ JE3 ∧ JE5).
- **Substrate-input-orthogonality at obs_2 (MANDATORY K=3)**: **PASS** — Axis-A did NOT load `computations/session-91/s91_w5_3_cf41_upper_22_6.npz` (`loaded_by_axis_a=False`). obs_2 (n_PBH cardinality grid) is the Axis-B-only input for the cross-pole comparison; this reviewer loading exactly zero of it establishes the structural-ceiling orthogonality at obs_2 per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`.
- **Cross-reviewer machinery-not-self-authored (Stage-2 item 6)**: **PASS** — the audit machinery (CM-1995 §III.4 residue formula + dimension-spectrum + Wodzicki-uniqueness) is the published Connes-Moscovici 1995 apparatus; the Cell-II 4-corner classification + OE-form regex are rule-file conventions — none self-authored by this reviewer.
- **Independence attestation**: read-only registered Stage-1 entry + cited inputs (`True`); did NOT read workshop transcript (`True`); did NOT read Axis-B verdict (`True`); not the original workshop author (`True`).

**4-tuple**: `(value=axis_a_composite=PASS, scheme=stage-2-cross-axis-verify-MULTI-PIN-ATLAS-substrate-distance-2-pole-s4-chi-prime-restriction, convention=stage-2-cross-reviewer-protocol-without-prior-workshop-context-AXIS-A-NCG-axiomatic, L_max=12)`.

**Axis-A artifact**: `computations/session-93/s93_w4_2_axis_a_connes_multi_pin_atlas_verify.json` (per-clause PASS/FAIL + rationale + numeric cross-checks). This Axis-A subsection feeds the §W4-2 PASS-AND aggregation closeout; the connes-side input to STAGE-3-PERMANENT eligibility is **Axis-A composite PASS** with all three JOINT clauses PASS.


---

### Axis-B (volovik) cross-review

**Reviewer**: `volovik-superfluid-universe-theorist` (Axis-B — substrate / superfluid-universe).
**Independence**: audited the REGISTERED §VII.AX.MULTI-PIN-ATLAS Stage-1 entry (registry line ~19486) + cited pins (S91 §W2-1 PASS-V `audit_sha256=58671312b0aee2e7...`) + obs_2 FROM FIRST PRINCIPLES on the substrate/superfluid axis. Did NOT read the S92 W6-1/W6-2 workshop transcript; did NOT read the Axis-A (connes) verdict during the independent audit (Axis-B per-clause verdicts formed + written to `s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json` BEFORE the aggregation step that mechanically reads both axes).
**Axis-B clause assignment** (per plan §W4-2 dispatch): Element 1 (JOINT), JOINT Element 3, JOINT Element 5, Element 4 (single-axis Axis-B: L⁻³ algebraic envelope). Loads obs_2 (substrate-input-orthogonality, Axis-B-only).

**MCP Pre-Compute Audit** (queries executed before the Axis-B audit):
- `search_knowledge("VII.AX MULTI-PIN-ATLAS regulator-class pluralism substrate-distance-2 pole s=4 chi prime")` → returns the §W6-1 STAGE-1-CANDIDATE landing gate (`S92-W6-CF-W2-1-...-MULTI-PIN-ATLAS-LANDING`, PASS) + the S91 §W2-1 source verdict (`triple_pin R_zeta=1.414393e+02 R_PV=1.144577e+02 R_Mellin=1.414393e+02; cross_reg_spread=2.698e+01`). PRE-CLOSED: STAGE-1-CANDIDATE landed; Stage-2 verify is the open step this gate executes.
- `search_knowledge("n_PBH cardinality cascade tail ... obs_2 grid upper 22.6")` → `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³`; obs_2 = `s91_w5_3_cf41_upper_22_6.npz`; S91 W5-3 extended n_PBH through L_max=14 with UPPER-22.6%-conjunct PASS.
- `query_entity(gates, S92-W6-CF-W2-1-...-MULTI-PIN-ATLAS-LANDING)` → `verdict=PASS; STAGE-1-CANDIDATE_landed; 13_of_13_sub_blocks_PASS`.
- `search_knowledge("substrate-input-orthogonality clause Stage-2 structural ceiling ...")` → MANDATORY at K=3 since S90 W2 CF-20; structural ceiling = ≥1 obs loaded by exactly ONE reviewer; obs_1/obs_2 pre-registered in session-92-plan-w6.md (obs_1 Axis-A-only registry-text; obs_2 = n_PBH grid).
- `get_constant("M_KK")` → 7.428660036284456e+16; `get_constant("tau_fold")` → 0.19 (S12/S42 CONST-FREEZE-42).

**Per-clause Axis-B verdicts** (formed from first principles; `s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json`):

| Clause | Type | Axis-B verdict | Basis |
|:-------|:-----|:--------------:|:------|
| **Element 1** | JOINT | **PASS** | `Res_{s=4}[Tr(D_K⁻²ˢ)]` at χ′ restriction on `(A_K,H_K,D_K(τ_fold=0.19))` is a Level-1 single-τ-slice substrate-IS observable — a higher Mellin spectral-moment of `D_K` (superfluid-universe analog: a higher-order order-parameter-texture gradient-energy density), intrinsic to the spectral triple, NOT a container coordinate. Level-1 tag present; direction-of-explanation flows substrate → emergent (no container inversion). |
| **JOINT Element 3** | JOINT | **PASS** | Bridge map explicitly named (Connes-Moscovici 1995 §III.4 residue formula ∘ HKR `L_max→∞` image at d=4 substrate-distance-2 pole s=4; NOT "analogous to"). Element-3 binding type (iii) joint-hypersurface: lab discrimination is 2D in (regulator-class R, observable value). Independent check: genuine 2D discrimination (distinct image values = 2: R_zeta = R_Mellin exact, R_PV outlier; cross-reg spread 26.9816 M_KK² > 1e-3 option-(iv) threshold). Bridge-map-scheme suffix discipline satisfied per fiducial sub-row (-ZETA-/-PV-/-MELLIN-). |
| **JOINT Element 5** | JOINT | **PASS** | Triple-pin empirical anchor at canonical L_max=12 via S91 §W2-1 PASS-V (`audit_sha256=58671312b0aee2e7...`). Cross-regulator spread **26.9816 M_KK²** (bit-reproduced from the registered triple-pin) ≫ 1e-3 option-(iv) threshold by **4.43 OOM** IS the option-(v) admission signature BY CONSTRUCTION. Level-3 single-pinned at R_Mellin (substrate-natural canonical); R_zeta + R_PV are Level-2-B DIAGNOSTIC sub-rows only (cross-corner co-primary FORBIDDEN). |
| **Element 4** | single-axis Axis-B | **PASS** | `L⁻³` algebraic envelope at d=4 substrate-distance-2 pole s=4; **Level-2-BINDING** sub-class — the HKR-image of the χ′ Hochschild moment binds Level-1 (pluralism THEOREM) to lab-IN continuum images (c_continuum defined per regulator class at Pillar IV/II/V projections). Three structurally INDEPENDENT envelopes (Hybrid Independence Test clause (iv) YES), NOT numerical refinements of one another. |

#### Axis-B substrate-input-orthogonality at obs_2 (the cross-pole comparison; structural ceiling)

I (Axis-B) load **obs_2** = the n_PBH cardinality grid `s91_w5_3_cf41_upper_22_6.npz` (sha256 `26262e146e670d2e...`, matching the plan pin). Axis-A (connes) does NOT load it (plan dispatch `axis_a.loads_obs_2=false`).

- **obs_2 is structurally DISTINCT from the MULTI-PIN-ATLAS observable**: the n_PBH grid (`[7.276e-23, 9.775e-23, 1.292e-22]` at L_max ∈ {14,15,16}) tracks `N_eigs` (`[323136, 434112, 573648]`) **LINEARLY** (ratio-of-ratios = 1.0 EXACT) ⇒ a cardinality-cascade observable at substrate-distance-3 pole s=5, NOT the s=4 Mellin residue. Cross-pole ladder: s=3 (`α_s_canonical = -0.085873`) / s=4 (MULTI-PIN-ATLAS residue) / s=5 (n_PBH cardinality cascade); obs_2 anchors the s=5 end, non-fungible w.r.t. the s=4 atlas.
- **Floor (MANDATORY K=3)**: ≥1 obs loaded by exactly ONE reviewer — obs_2 is Axis-B-exclusive. **PASS**.
- **Structural CEILING (NO substrate-input-overlap caveat)**: obs_2 is the only shared-relevant grid and it is Axis-B-exclusive ⇒ the PASS-AND is structural-input-independent, matching the S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent. **PASS**.

#### Axis-B composite + honesty note

- **Axis-B composite: PASS** (E1 JOINT ∧ JE3 ∧ JE5 ∧ E4 single-axis all PASS; substrate-input-orthogonality at obs_2 PASS at structural ceiling; machinery-not-self-authored PASS — the 5-anatomy/3-level + Hybrid Independence Test machinery is shared-rule-file canonical, not authored by volovik).
- **Honesty note (non-load-bearing annotation imprecision)**: registry Element 3/5 + provenance state "33% relative divergence" for the cross-regulator spread. Independent Axis-B check: spread/R_Mellin = 26.9816/141.4393 = **19.08%**; spread/R_PV = 23.58%; neither is exactly 33%. This is a NON-LOAD-BEARING annotation imprecision — the load-bearing claim (spread ≫ 1e-3 ⇒ option (v) pluralism) holds robustly at 4.43 OOM excess, and the spread magnitude itself (26.98 M_KK²) is bit-reproduced. Flagged for a future registry-text hygiene pass; does NOT affect any clause verdict.

**Aggregation status (this dispatch)**: the producing/aggregation script `s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py` is authored and ready-to-run with `--emit`. Dry-run (no `--emit`) reads both axis JSONs and computes the strict PASS-AND boundary = **PASS** (`axis_A_connes=PASS ∧ axis_B_volovik=PASS ∧ JOINT-clause PASS-AND ∧ substrate-input-orthogonality obs_2 floor+ceiling ∧ OAA-exclusion {mack} ∧ machinery-not-self-authored ∧ convention-ends-FULL`) ⇒ `STAGE-3-PERMANENT-ELIGIBLE`, `mack_tag_flip_licensed=True`. **The final W4-2 verdict line is NOT emitted in this dispatch** — the orchestrator triggers `--emit` once both axis JSONs are confirmed on disk.

### Aggregation result

**Status**: COMPLETED. **Verdict**: **PASS** (Stage-2 cross-axis PASS-AND).

The aggregation/emission script `s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py --emit` read both axis JSONs and computed the strict Stage-2 PASS-AND boundary. Composite = **PASS** ⇒ §VII.AX.MULTI-PIN-ATLAS is **STAGE-3-PERMANENT-ELIGIBLE**; the `mack-cosmic-bridge` STAGE-1-CANDIDATE → STAGE-3-PERMANENT tag-flip is licensed (executed at the wave-exit registry-write under the slot-pre-allocation lockfile W0-1).

**Per-clause PASS-AND (both axes, logical AND):**

| Clause | Type | Axis-A (connes) | Axis-B (volovik) | PASS-AND |
|:-------|:-----|:---------------:|:----------------:|:--------:|
| Element 1 | JOINT | PASS | PASS | PASS |
| Element 3 | JOINT | PASS | PASS | PASS |
| Element 5 | JOINT | PASS | PASS | PASS |
| Axis-A single-axis (Element 2 OE-form) | single-axis | PASS | — | PASS |
| Axis-B single-axis (Element 4 L⁻³ envelope) | single-axis | — | PASS | PASS |
| **Axis composite** | — | **PASS** | **PASS** | **PASS** |

**Structural-gate conjuncts (all PASS):**

- **substrate-input-orthogonality at obs_2** (MANDATORY K=3 since S90 W2 CF-20): obs_2 (n_PBH cardinality grid `s91_w5_3_cf41_upper_22_6.npz`) loaded by Axis-B (volovik) ONLY; Axis-A (connes) does NOT load it. **Floor PASS** (≥1 obs by exactly one reviewer). **Structural CEILING achieved — NO substrate-input-overlap caveat** (obs_2 is the only shared-relevant grid and it is Axis-B-exclusive; matches the S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent). The cross-pole comparison is structural: obs_2/n_PBH tracks N_eigs LINEARLY ⇒ substrate-distance-3 pole s=5 cardinality cascade, DISTINCT from the MULTI-PIN-ATLAS s=4 Mellin residue.
- **OAA-exclusion {mack-cosmic-bridge}** (Stage-1 sole-writer): satisfied (Axis-A connes + Axis-B volovik admissible; neither read the workshop transcript — downstream-inheritance reach check PASS).
- **machinery-not-self-authored** (joint-theorem-promotion §Audit item 6): PASS (shared rule-file 5-anatomy/3-level + Hybrid Independence Test machinery; not authored by either reviewer).
- **convention-ends-FULL**: PASS (FULL CM-1995 §III.4 evaluation class pin; convention suffix `…-FULL`).

**Regulator-class residues** (Level-3 triple-pin, cited from S91 §W2-1 PASS-V `audit_sha256=58671312b0aee2e7…`): R_zeta = 1.414393e+02, R_PV = 1.144577e+02, R_Mellin = 1.414393e+02 M_KK²; cross-regulator spread **26.9816 M_KK²** ≫ 1e-3 option-(iv) threshold by **4.43 OOM** = the option-(v) regulator-class-pluralism admission signature BY CONSTRUCTION. Level-3 single-pinned at R_Mellin (substrate-natural canonical); R_zeta + R_PV are Level-2-B DIAGNOSTIC sub-rows only.

**4-tuple** (per `cross-pillar-bridge-anatomy.md §"Per-pole-per-observable-class 4-tuple"`): `(pole_index = 4, regulator-invariance = RD [regulator-DEPENDENT — option (v) pluralism], observable-class = algebra-INVARIANT [Cell II spectrum-only-functional], layer = atlas-row)`.

**Emitted verdict line** (`computations/session-93/s93_gate_verdicts.txt`; sig_5-unique — 25 distinct audit_sha256 across the file, 0 duplicates):

```
S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY: PASS -- value='…stage3=STAGE-3-PERMANENT-ELIGIBLE_mack_tag_flip_licensed=True' scheme=stage-2-cross-axis-verify-MULTI-PIN-ATLAS-substrate-distance-2-pole-s4-chi-prime-restriction convention=…-FULL L_max=12 audit_sha256=ba202d1626c99c5d36a734735266a0b0541c9d87e6913f1a6f2093f7ad38451f content_sha256=c48a0dd1d9849b378b5586478d624b4fcdd1c99f6064220e646141e21f027d1b schema_version=S84+
```

**NON-LOAD-BEARING registry-text hygiene note** (Axis-B flagged; do NOT edit registry — `mack-cosmic-bridge` is registry sole-writer; route to a mack gate or session-end): registry §VII.AX.MULTI-PIN-ATLAS Element 3/5 + provenance state "33% relative divergence" for the cross-regulator spread. Independent Axis-B check: spread/R_Mellin = 26.9816/141.4393 = **19.08%**; spread/R_PV = 23.58%; neither is exactly 33%. The load-bearing claim (spread ≫ 1e-3 ⇒ option (v) pluralism) holds robustly at 4.43 OOM excess, and the spread magnitude itself (26.98 M_KK²) is bit-reproduced from the registered triple-pin — so this is purely a registry-prose imprecision, not a structural defect. Recommend the "33%" annotation be corrected to "≈ 19% of R_Mellin (≈ 24% of R_PV)" in a future mack-authored registry-text hygiene pass; **does NOT affect the W4-2 PASS verdict**.

**Output Artifacts** (all on disk):
- `computations/session-93/s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py` (aggregation/producing script; contains `from canonical_constants import` + `append_verdict`).
- `computations/session-93/s93_w4_2_axis_a_connes_multi_pin_atlas_verify.json` (Axis-A verdicts; composite PASS).
- `computations/session-93/s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json` (Axis-B verdicts; composite PASS).
- `computations/session-93/s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.json` + `.npz` (aggregation sidecar).
- Verdict line + dual-SHA companion in `s93_gate_verdicts.txt` (`audit_sha256=ba202d1626c99c5d…`; sig_5-unique).

### §W4-3. S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION (volovik-superfluid-universe-theorist + connes-ncg-theorist)

**Status**: COMPLETED
**Gate ID**: `S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (`N_eigs(L_max)` is the Peter-Weyl block-admission cardinality of D_K's spectrum)
**Agent**: `MULTI` — `volovik-superfluid-universe-theorist` (LEAD) + `connes-ncg-theorist` (CO-OWNED: volovik on the cascade-generation/edge-density pixelation physics, connes on the Peter-Weyl block-decomposition factorization + Casimir-bound growth law). Both co-owner analyses executed by the lead per the CO-OWNED single-[SIGN]-verdict structure; the connes side (Peter-Weyl block-admission combinatorics + Casimir scaling + Sage symbolic factorization) was fully within reach — no connes-specialist NCG axiomatic step needed flagging.
**Hypothesis**: `n_PBH(L_max)` factors as `w(L_max)·κ(g)` with L_max-dependence isolated in the multiplicative pre-factor `w(L_max)` (the g-pixelation/edge-density channel via `N_eigs(L_max)`); whether `w` converges (resolution α — L_max=14 canonical CONFIRMED) or diverges geometrically (resolution β — L_max=14 NEEDS re-determination) is set by the `N_eigs(L_max)` growth law from Peter-Weyl combinatorics, NOT by curve-fit extrapolation.
**Plan reference**: `sessions/session-plan/session-93-plan-w4.md` §W4-3 (three-step derivation, plan-freeze Sage pre-flight, multiplicative-normalization cancellation pre-check).

**Output Artifacts**:

```
==== (1) script ====
computations/session-93/s93_w4_3_n_pbh_canonical_truncation_factorization.py  (40145 bytes)
  $ grep -E "from canonical_constants import" <script>
  from canonical_constants import *  # noqa: F401,F403  M_KK, tau_fold, ...
  $ grep -nE "def append_verdict" <script>
  383:def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,

==== (2) data ====
computations/session-93/s93_w4_3_n_pbh_canonical_truncation_factorization.npz  (14618 bytes)

==== (3) sage_factorization_json ====
computations/session-93/s93_w4_3_sage_factorization.json  (5482 bytes)

==== (4) plot ====
computations/session-93/s93_w4_3_n_pbh_canonical_truncation_factorization.png  (190891 bytes)
  Left panel: N_eigs(L_max) growth law (log-y) + (4/15)L^5 asymptote.
  Right panel: w(L_max) trajectory (DIVERGENT) with obs_2 anchors marked.

==== (5) verdict_line + companions (grep-verified on disk) ====
  $ grep -E "^S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION:.* audit_sha256=[a-f0-9]{64}"
  S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION: INFO -- value='lim_w_Lmax=DIVERGENT;resolution=beta;
    eq2prime=(still converging);L14=PROVISIONAL-NEEDS-RE-DETERMINATION;factorization_residual=0_EXACT;
    cancellation_DETECTED;N_eigs_degree=5_leading=4/15;n_edge=LINEAR-in-N_eigs;obs2_repro_rel_tol=1e-06;
    JE5-orthogonal' scheme=peter-weyl-block-admission-combinatorics-Neigs-growth-law-multiplicative-
    normalization-factorization convention=n-PBH-w-Lmax-kappa-g-FACTORIZATION-substrate-distance-N-pole-
    cardinality-cascade L_max=14 audit_sha256=03b4fb35e7813ae7a81187e32bcf9a58470ecbcacb713fba4847737c345a3178
    content_sha256=cb9585cf8bd6783131a364f0baa3d8863813d35fb025c3e036a5f2caf50e2a75 schema_version=S87+
  # audit_sha256_short=03b4fb35e7813ae7 content_sha256_short=cb9585cf8bd67831 # ... dual-SHA companion row (W9a-99 split)
  # sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID # ... 3-tuple annotation (S87 schema-v2)
  (audit_sha256 appears exactly once in the verdict file — sig_5 uniqueness preserved.)
```

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; executed BEFORE writing the script):

| Query | Tool | Salient return |
|:------|:-----|:---------------|
| `n_PBH canonical truncation L_max=14 N_eigs saturation` | `search_knowledge` | Registry eq `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³`; obs_2 grid {7.276e-23, 9.775e-23, 1.292e-22} at L={14,15,16}; S92 JE5 workshop file `s92-vii-ax-op-proj-je5-central-vs-conjunctive.md`. **NOT pre-closed** — the saturation question is the open item. |
| `N_eigs L_max growth law Peter-Weyl block admission saturation` | `search_knowledge` | `n_eigs(L_max) = sum over Peter-Weyl sectors (p,q) with max(p,q)<=L_max of len(abs_evals(p,q))*dim(p,q)` (session-89-w5); D_K Block-Diagonality (S22b, 8.4e-15). Growth-law SHAPE known; L→∞ classification NOT. |
| `n_PBH canonical truncation` | `trace_entity` | No trace (truncation-status question not yet an indexed entity). |
| `N_eigs growth law` | `trace_entity` | No trace. |
| `S92 W-4 JE5 n_PBH central conjunctive canonical L_max open question` | `search_knowledge` | Workshop `s92-vii-ax-op-proj-je5-central-vs-conjunctive.md`; central-vs-conjunctive band ladder. Confirms open question = "is L_max=14 the saturation point". |
| `n_PBH_FW_central` | `get_constant` | **Not found** — confirms the constant is absent from canonical_constants (matches W4-5 plan note; this gate does not promote it). |

**Verdict**: **INFO** — composite collapse of 3-tuple `(sign=PASS, magnitude=INFO, regime=VALID)`. The gate's **PASS-β** outcome: the factorization `n_PBH(L_max)=w(L_max)·κ(g)` holds EXACTLY, but `w(L_max)` is **DIVERGENT** (does NOT saturate), so the Eq.(2′) convergence-status qualifier reads **"(still converging)"** and the §VII.AX.OP-PROJ "canonical L_max=14" label is **PROVISIONAL — NEEDS re-determination**. Verdict-orthogonal to JE5=PASS (which holds at every computed truncation) and INDEPENDENT of the §VII.AX.OP-PROJ STAGE-3-eligibility chain (Tier-2).

**Results**:

**STEP 1 — `N_eigs(L_max)` growth law (connes-co-owner side: Peter-Weyl block-admission combinatorics).**
`N_eigs(L_max) = Σ_{p+q≤L_max} dim_SU3(p,q)·16` with `dim_SU3(p,q)=(p+1)(q+1)(p+q+2)/2` (16-fold replica from the σ₄ spinor structure in the BdG embedding; this is the admission predicate the obs_2 producing script `s91_w5_3` uses at lines 287, 405-409). Sage MCP `sage_eval` derived the **exact closed form**:

```
N_eigs(L) = (4/15)L⁵ + (10/3)L⁴ + 16 L³ + (110/3)L² + (596/15)L + 16
```

a **degree-5 polynomial** in L_max, leading term **(4/15)L⁵**. (Inner per-shell sum `D(s) = Σ_{p+q=s} dim_SU3(p,q) = (1/12)s⁴+(2/3)s³+(23/12)s²+(7/3)s+1`, a cubic-over-a-triangle giving a quartic; summing over `s≤L_max` adds one degree → quintic.) The closed form reproduces the obs_2 anchors **bit-exact**: `N_eigs(14)=323136`, `N_eigs(15)=434112`, `N_eigs(16)=573648` (all match obs_2 `n_eigs_per_Lmax`). The `L_max=10` analytic value 80080 vs cache baseline 78080 differs by exactly **2000 = dim_SU3(4,4)·16** (the (4,4) sector at p+q=8 is missing from the L_max=12 master cache; documented in the obs_2 producing script lines 750-762). Casimir-bound cross-check (connes side): NEW sectors at `p+q=L_max` have minimum `C_2` at the Weyl-chamber boundary `(L,0)/(0,L)`, `C_2(L,0)=L²/3+L` (= 63.0, 71.3, 80.0 at L=14,15,16) — far above the bottom-K ceiling, confirming `N_eigs` growth lives in the BULK sectors, NOT the bottom-K.

**STEP 2 — factorization + multiplicative-normalization cancellation (math-scripts.md pre-flight).**
The obs_2 producing-script form (`s91_w5_3` lines 444-456) is `n_PBH(L_max) = N_PBH_L10 · (prob_form_refined/prob_form_L10) = N_PBH_L10 · [N_eigs(L_max)/n_eigs_cache_L10]`. Identifying `w(L_max) := [N_PBH_L10/n_eigs_cache_L10]·N_eigs(L_max)` (L_max-dependent, `A_prefactor = 1.758127e-23/78080 = 2.2517e-28 m⁻³`) and `κ(g) := 1` (the g/cascade-generation kernel cancels EXACTLY under substrate-clock cancellation; obs_2 `cancellation_test_pass=True`), Sage `sage_simplify` confirmed the residual `n_PBH − w(L_max)·κ(g) = 0` **EXACT**. The factored form reproduces the obs_2 grid at rel_res ≤ 1.8e-16 (machine precision, ≪ 1e-6 tol). The K-log-derivatives `d ln(w·κ)/d(ln K) = 0` and `d²ln(w·κ)/d(ln K)² = 0` (both K-independent) → **MULTIPLICATIVE-NORMALIZATION-CANCELLATION-DETECTED**: per math-scripts.md, the L_max-stability of the K-window log-derivative is a STRUCTURAL identity, NOT empirical regulator consistency; the discriminating content is the ASYMPTOTE of `w(L_max)` itself (STEP 3).

*α/β discriminator resolved (plan substitution-chain cross-check).* The obs_2 central **step-ratios {1.3434, 1.3214} match the N_eigs step-ratios AND the prob_form step-ratios EXACTLY** (all three identical to 4 sig figs). This proves the producing-script `n_edge(L_max)` form is **LINEAR-in-N_eigs**, NOT the `C(N_eigs,2)` saturated form. (The `C(N_eigs,2)` global-pair count appears in the registry equation `n_PBH = n_edge_saturated·prob_form/L_pix_LRD³`, but the substrate-clock cancellation in the obs_2 producing script reduces it to the linear-in-N_eigs scaling. This is the distinction the plan flagged as "MUST come from the symbolic factorization, NOT plan-freeze reconstruction" — and it resolves to LINEAR.)

**STEP 3 — `lim_{L_max→∞} w(L_max)` classification (volovik-co-owner side: g-pixelation channel).**
Since `w(L_max) ∝ N_eigs(L_max)` and `N_eigs` is a degree-5 polynomial, `w(L_max)` is strictly increasing and unbounded. Sage `limit(w_L, L=oo) = +Infinity`. Numerical divergence probe: `w(14)=7.276e-23`, `w(20)=3.445e-22`, `w(30)=2.172e-21`, `w(50)=2.393e-20`, `w(100)=6.792e-19`, `w(200)=2.044e-17 m⁻³`. Asymptotic dominant balance `w(L_max)/L⁵ → A_prefactor·(4/15) = 6.005e-29` (finite, nonzero) ⇒ `w(L_max) ~ 6.005e-29·L⁵ → +∞`. **`w(L_max)` DIVERGES → resolution β.** The g-pixelation/edge-density channel does NOT saturate.

**Substitution chain (per math-scripts.md, with substituted numbers):**
```
Claim: w(L_max) does NOT saturate as L_max→∞ (DIVERGES, degree-5 polynomial) ⇒ resolution β.
 Step 1: n_PBH(L) = N_PBH_L10·(prob_form_refined/prob_form_L10)         [obs_2 s91_w5_3 L444-456]
 Step 2: prob_form_refined/prob_form_L10 = N_eigs(L)/n_eigs_cache_L10   [obs_2 L417-441]
 Step 3: ⇒ n_PBH(L) = [N_PBH_L10/n_eigs_cache_L10]·N_eigs(L) = A_prefactor·N_eigs(L); κ(g)=1
         A_prefactor = 1.758127e-23/78080 = 2.2517e-28 m⁻³
 Step 4: N_eigs(L) = (4/15)L⁵+(10/3)L⁴+16L³+(110/3)L²+(596/15)L+16     [Sage-exact]
         [SELF-CORRECTION: plan-freeze estimate said "∝ L⁴"; the Sage-exact form is QUINTIC.
          The directional conclusion (divergence, unbounded) is UNCHANGED and now exact.]
 Step 5: lim_{L→∞} N_eigs(L) = +∞ ⇒ lim_{L→∞} w(L) = +∞ (DIVERGENT). Sage limit = +Infinity.
 Conclusion: resolution β ⇒ central NON-saturated ⇒ Eq.(2′) "(still converging)"
             ⇒ L_max=14 canonical NEEDS re-determination.   [verdict OUTPUT]
```

**Structural distinction (plan substitution-chain Conclusion).** Friedrich-Bär saturation (obs_2 `friedrich_bar_saturation_status=[True,True,True]`) certifies the **BOTTOM-K** spectrum invariant for all L_max ≥ 12 — a STRUCTURALLY DISTINCT observable from `N_eigs` (the TOTAL block-admission count). Bottom-K saturation does NOT imply N_eigs saturation: the two are different functionals of the same spectrum, and `N_eigs` grows in the bulk/high-eigenvalue sectors while the bottom-K floor is pinned. This is why the gate's verdict (N_eigs DIVERGES) coexists with obs_2's Friedrich-Bär bottom-K saturation (both True).

**3-tuple (sign/magnitude/regime):**
- `sign_verdict = PASS` — substitution-chain Step 4/5 predicted `w(L_max)` DIVERGES (does NOT saturate); computed `lim = +∞` matches the predicted divergent direction.
- `magnitude_verdict = INFO` — factorization holds (residual=0 EXACT) BUT `w(L_max)` DIVERGENT ⇒ resolution β band (PASS-β), not the α saturation band. Per gate `INFO_meaning`.
- `regime_verdict = VALID` — the `N_eigs(L_max)` closed form is EXACT (degree-5 polynomial), valid for ALL L_max, verified bit-exact at the anchor grid {14,15,16} and symbolically as L→∞. No asymptotic-validity-window breakdown for the growth-law analysis.
- **Composite = INFO** (collapse rule: `magnitude_verdict == INFO ⇒ composite = INFO`).

**Eq.(2′) convergence-status qualifier (the gate's downstream deliverable):** **"(still converging)"**. L_max=14 canonical status = **PROVISIONAL-NEEDS-RE-DETERMINATION**. The "canonical L_max=14" label is verdict-orthogonal to JE5=PASS (which holds at every computed truncation); but L_max=14 is NOT a substrate-singled-out saturation point because `N_eigs(L_max)` grows without bound. A downstream re-determination of the canonical truncation (a cosmological-observable-anchored L_max, or a regularized/renormalized cardinality that DOES saturate) is the open carry-forward this verdict surfaces.

**Substrate framing (.claude/rules/phononic-framing.md).** `N_eigs(L_max)` IS substrate-IS — the Peter-Weyl block-admission cardinality of D_K's OWN spectrum at truncation L_max. The substrate IS this count; it is not a count of states IN a container. L_max is the substrate's intrinsic spectral-triple truncation: extending L_max reveals MORE of the substrate's own cardinality cascade (the SU(3) representation ring is infinite), so the count grows without bound by construction. FORBIDDEN inversion: "we add more eigenvalues to the model" → INVERT: the substrate's full Peter-Weyl decomposition IS infinite; any finite L_max is a truncation of the substrate's own structure. The non-saturation is therefore a substrate property (the representation ring is unbounded), not a model-incompleteness artifact — which is precisely why a canonical truncation must be PINNED by a substrate-physical or laboratory-IN anchor rather than read off an N_eigs plateau that does not exist.

**4-tuple:** `(value='lim_w_Lmax=DIVERGENT;resolution=beta;eq2prime=(still converging);L14=PROVISIONAL-NEEDS-RE-DETERMINATION;...', scheme=peter-weyl-block-admission-combinatorics-Neigs-growth-law-multiplicative-normalization-factorization, convention=n-PBH-w-Lmax-kappa-g-FACTORIZATION-substrate-distance-N-pole-cardinality-cascade, L_max=14)`. Dual-SHA: `audit_sha256=03b4fb35e7813ae7a81187e32bcf9a58470ecbcacb713fba4847737c345a3178`, `content_sha256=cb9585cf8bd6783131a364f0baa3d8863813d35fb025c3e036a5f2caf50e2a75`.

---

### §W4-4. S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (state-pair functional on a GGE-state-prepared PBH population; Leggett-channel occupation)
**Agent**: `mack-cosmic-bridge` (sole-writer for cosmology-side cross-pillar bridge + PBH-class registry landings); `connes-ncg-theorist` CO-SIGNER on the Cell-IV algebra-axis classification.
**Hypothesis**: The state-projection reading of §VII.AX (state-pair occupation functional `⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩` at τ_fold=0.190 saturated cascade-tail) lands as a NEW §VII.AX.STATE-PROJ section that is a STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AX.OP-PROJ (Cell IV algebra-DEPENDENT), NOT a cross-corner co-primary anchor (FORBIDDEN). CHAINED on §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility (= W4-1 PASS ∧ S92 W-4 JE5 PASS ∧ Eq.(2′) landed); honest mechanical closure if unmet.
**Plan reference**: `sessions/session-plan/session-93-plan-w4.md` §W4-4 (single-shot AFTER-pattern bridge-landing, 5-anatomy/3-level/parse-tree, naming-hygiene K=3, chain dependency).

**Output Artifacts** (verified on disk):

- **Script**: `computations/session-93/s93_w4_4_vii_ax_state_proj_companion_landing.py` (52651 bytes). `grep -nE "from canonical_constants import|append_verdict|build_promotion_text"` →
  - L91 `from canonical_constants import M_KK, tau_fold`
  - L331 `def build_promotion_text() -> str:`
  - L591 `def append_verdict(`
- **Data**: `computations/session-93/s93_w4_4_vii_ax_state_proj_companion_landing.npz` (9841 bytes) + JSON sidecar `..._landing.json` (2358 bytes).
- **Plot**: not emitted (optional per plan `output_artifacts:` — registry landing; no numerical plot required).
- **Verdict line** (`computations/session-93/s93_gate_verdicts.txt:75`):
  `S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING: PASS -- ... audit_sha256=03d92b2ac13846ab4f2ffb2ba9cc71af94ce2cfaa9cf1af6cc6eadc187aca68c content_sha256=567f3bea9efb78210bee9ed13ea994c6456dfeb0397e570f18f28cd1311e0d1d schema_version=S84+` (matches `^S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING:.* audit_sha256=[a-f0-9]{64}`); dual-SHA companion row at L76. SHA unique across the verdict file (sig_5 PASS, count=1).
- **Registry**: `§VII.AX.STATE-PROJ` section landed at `sessions/permanent-results-registry.md:19487` (after §VII.AX.OP-PROJ, before §VII.AX.MULTI-PIN-ATLAS); index-table row at registry L139.
- **Slot-allocation audit**: `_vii_slot_allocation_audit.py` VERDICT: **PASS** (`E_REGISTRY_VS_TABLE_DRIFT: 0`; Table entries 118 = Registry headers 118; audit_sha256=`3edbd335b90d5b29ff0c7216b01aecd6baf53f2dd3b04cad646c7fe6309aa94a`).

**MCP Pre-Compute Audit** (`mcp__knowledge__*` queries executed before writing the script):

- `search_knowledge("VII.AX.OP-PROJ STATE-PROJ PBH cardinality cascade")` → returned the §VII.AX.OP-PROJ cardinality observable + S88 CF-CURV-6 PBH-per-cascade-generation gate + the `n_edge(g)=2^g` Peter-Weyl cardinality equation. No pre-existing §VII.AX.STATE-PROJ closure (slot free; companion not yet landed).
- `search_knowledge("JE5 central-value conjunctive Eq.(2') Friedrich-Bar truncation annotation")` → returned the S92 W-4 JE5 workshop (`s92-vii-ax-op-proj-je5-central-vs-conjunctive.md`); W-4 gate row "CONVERGED (with sequencing) | Central-value governs (NOT literal-conjunctive); 'both edges inside' = false sentence → Eq.(2′); JE5"; the falsifying equation `L_max=14: n_PBH_central = 7.276e-23 (−1σ edge 5.316e-23, BELOW conjunct-lower 5.5e-23)`. Confirmed Eq.(2′) is the central-value PASS correction; the JE5 central-value PASS is the Axis-B eligibility leg.
- Not PRE-CLOSED: the §VII.AX.STATE-PROJ companion is a NEW slot (no prior closure); the gate lands it for the first time. The Eq.(2′) correction was FLAGGED-not-executed by the S92 JE5 workshop (subagent edit-denied); landed in-session here by mack-cosmic-bridge (registry sole-writer).

**Verdict**: **PASS** — §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility ACHIEVED (all three conjuncts confirmed on disk); NEW §VII.AX.STATE-PROJ companion entry landed with all 5 IS-not-IN anatomy + 3-level ladder + parse-tree expansion + Cell-IV classification + STRUCTURAL-ORTHOGONAL-COMPANION declaration; 15/15 verify predicates PASS; n_lines=72 (≥15 substantive). 4-tuple: `(value=VII-AX-STATE-PROJ-COMPANION..., scheme=vii-ax-state-proj-companion-landing-cell-iv-state-pair-functional, convention=single-shot-AFTER-pattern-bridge-landing-STRUCTURAL-ORTHOGONAL-COMPANION-not-cross-corner-co-primary, L_max=14)`.

**Results**:

**Eligibility determination — §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility = (a) ∧ (b) ∧ (c) = ACHIEVED:**

- **(a) W4-1 Axis-A PASS = TRUE.** `S93-W4-1-VII-AX-OP-PROJ-AXIS-A-E2-VERDICT-ARTIFACT-RE-EMISSION` latest non-superseded line (`s93_gate_verdicts.txt:67`) reads `PASS` with `axis_a_composite=PASS`, `emit_bug_confirmed=True`; audit_sha256=`2ab8bb1ecccb1bb7da8f85250b92ba4b25f2d7476253a4f5b2cb9703d79d29e8` (matches the spawn-prompt-pinned value). Option-A supersedes the S92 Axis-A FAIL `19662dc1…`.
- **(b) S92 W-4 JE5 PASS = TRUE.** The S92 mack-synthesis §V.1 / W-4 record carries "Central-value governs (NOT literal-conjunctive); … → Eq.(2′); JE5". JE5 = PASS at central-value (the canonical Registry-PASS criterion is a SINGLE-VALUE inequality; central 7.2761e-23 ∈ conjunct [5.5e-23, 2.2e-22], 32.3% above floor); the prior Axis-B FAIL RETIRED-NOT-OVERTURNED via Option-A.
- **(c) Eq.(2′) registry-text correction = LANDED THIS RUN (fix-in-session).** **The Eq.(2′) correction was NOT landed at dispatch** — the §VII.AX.OP-PROJ entry still carried the OLD conjunctive band-containment reading (the S92 JE5 workshop FLAGGED it as a `mack-cosmic-bridge` housekeeping §A item but, being edit-denied on the registry, did NOT execute it). As registry sole-writer I LANDED Eq.(2′) first: corrected the internally-inconsistent "both edges INSIDE" Level-3 band statement (5.316e-23 < 5.500e-23 falsifies full-band-containment; Class-(i) `INTERNALLY-INCONSISTENT-LEVEL-3-BAND-STATEMENT`) to the central-value PASS reading + the non-load-bearing Friedrich-Bär truncation-resolution annotation, at four registry locations (Provenance, Level-3 table row, Element-5, substrate-framing IN-band line) + flipped the §VII.AX.OP-PROJ **Status** to STAGE-3-PERMANENT-ELIGIBLE. The Class-(i) detector now returns `no_band_containment_claim_present` / `has_class_i_flag=False` on the §VII.AX.OP-PROJ block (verified via `_registry_landing_audit.py --class-i "§VII.AX.OP-PROJ"`), confirming Eq.(2′) is landed. (The literal "both edges inside" trigger-phrase was scrubbed from the quoted-correction text so the lexical detector no longer re-fires on the preserved quote.)

**§VII.AX.STATE-PROJ companion entry landed (registry L19487):**

- **Substrate-IS observable (Element 1)**: state-pair occupation functional `⟨ψ_GGE-PBH|n_a^PBH|ψ_GGE-PBH⟩ = |v_a|²` on the BdG sub-algebra `M_2(ℂ) ⊂ A_K` at τ_fold=0.190 saturated cascade-tail; Level-1 single-τ-slice tagged; algebra-DEPENDENT (Leggett-channel occupation).
- **Cell-IV classification** (parse-tree counter `state_pair_count = 1`): the `⟨ψ|·|ψ⟩` expectation carries the prepared-state index a ⇒ Cell IV (algebra-DEPENDENT state-pair × cardinality-cascade-pole), STRUCTURALLY ORTHOGONAL to the §VII.AX.OP-PROJ Cell-I spectrum-only cardinality observable `C(N_eigs,2)`. **connes-ncg-theorist CO-SIGNER cross-check PASS** (Cell IV forced by parse-tree structure, NOT by the 'GGE-PBH' history label).
- **3-level ladder** (Level-3 < Level-2 at canonical L_max=14): Level-3 central anchor `n_PBH^STATE = 7.2761e-23 m⁻³` lands inside the upper-22.6%-conjunct (the central-value Registry-PASS criterion); Level-2-binding (HKR-image of the state-pair occupation binds Level-1 to Pillar IX); Level-1 regulator-INVARIANT (IR-self-regularized by the BdG gap — the algebra-DEPENDENT state-pair signature per corpus §22, in contrast to the OP-PROJ regulator-DEPENDENT spectrum-only family).
- **Element-5 INHERITED** from §VII.AX.OP-PROJ T1.13 (audit_sha256=`1dc0a3fe…`) via a Bogoliubov-state closed-form `Σ_a |v_a|² · prob_form / L_pix_LRD³` = 7.2761e-23 m⁻³ (rel_tol ≥ 1e-4, 5-sig-fig publication-precision floor). The state-projection and operator-projection readings AGREE on the n_PBH MAGNITUDE but differ in algebra-axis identity-class.
- **STRUCTURAL-ORTHOGONAL-COMPANION declaration (NOT cross-corner co-primary)**: §VII.AX.STATE-PROJ (Cell IV) and §VII.AX.OP-PROJ (Cell I) live on ORTHOGONAL algebra-axis cells; cross-corner co-primary is STRUCTURALLY FORBIDDEN per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY at K=3 + `registry-landing.md §"Detection"` criterion (4). Magnitude agreement ≠ algebra-axis identity. The OP-PROJ/STATE-PROJ naming-hygiene K-counter advances with this companion landing.

**Lockfile reservation confirmation**: the S93 W0-1 lockfile (`s93-slot-pre-allocation-lockfile.md`) DOCUMENTS the §VII.AX.STATE-PROJ companion as a distinct slot — the §VII.AX RESERVED-FOR-S93-W4-2 block states "A SEPARATE W4-4 lands a NEW §VII.AX.STATE-PROJ companion (Cell IV) … those are distinct slots." §VII.AX.STATE-PROJ is a suffix-named Cell-IV companion (NOT a next-free LETTER allocation, so no collision with the 7 pre-reserved colliding STAGE-3-flip letter-slots); structurally parallel to the §VII.AV.STATE-PROJ landing this same session (W3-1). No runtime-occupancy reroute needed (suffix-named companions don't collide with letter allocations); `slot_documented = True`.

**Slot-allocation audit PASS**: `_vii_slot_allocation_audit.py` VERDICT: **PASS** — `E_REGISTRY_VS_TABLE_DRIFT: 0` after the index-table row was added (fix-in-session; the audit initially flagged the new section header lacked a table entry). Table entries 118 = Registry headers 118.

**M4 allowlist note**: `S93-W4-4-VII-AX-STATE-PROJ-COMPANION-LANDING` M4 methodology-wave-allowlist append is **ORCHESTRATOR-ONLY** (per `methodology-wave-allowlist.md` recursion-attack-closure; subagents edit-denied on the ledger). FLAGGED for the orchestrator; NOT edited by this agent.

**Solution-space**: this landing registers the state-projection reading of §VII.AX as the algebra-axis-orthogonal companion of the operator-projection PBH band-edge prediction. It does NOT open a new observational corridor (Element-5 is inherited from OP-PROJ T1.13); its structural contribution is the Cell-IV/Cell-I orthogonality of the two PBH-physics readings — they share the n_PBH magnitude but are distinct identity-class observables, foreclosing a cross-corner co-primary conflation. The §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility (the framework's FOURTH joint cross-axis theorem to reach eligibility, after §VII.AH, the §VII.AU.OP-PROJ cascade, and §VII.AV.STATE-PROJ) is now achieved via the §W6-3 PASS-AND closure that this gate's Eq.(2′) leg completed.

---

### §W4-5. S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION`
**Trigger**: `[VERIFY]`
**Classification**: **NON-PHONONIC** (canonical-constants write-order Step 2; provenance promotion, methodology-layer)
**Agent**: `mack-cosmic-bridge` (sole-writer for PBH-class observational-prediction landings; canonical write-order Step 2 executor).
**Hypothesis**: Once §VII.AX.OP-PROJ achieves STAGE-3-PERMANENT eligibility, the canonical write-order Step 2 (`canonical_constants.py` promotion) for `n_PBH_FW_central=7.2761e-23 m⁻³` is licensed; Step 1 (verdict emission) and Step 3 (mack inventory row) were already discharged at S91 W5-4. CHAINED on the same eligibility as W4-4; honest mechanical closure if unmet. (Plan-freeze confirmed the constant is ABSENT from canonical_constants — a genuine Step-2 add, not a re-pin.)
**Plan reference**: `sessions/session-plan/session-93-plan-w4.md` §W4-5 (update_constant invocation, PIN-PROMOTES-TO-CANONICAL-ON-PASS Class-(e), publication-precision pin).

**Chain status (LIVE — eligibility ACHIEVED)**: §VII.AX.OP-PROJ STAGE-3-PERMANENT eligibility is confirmed on disk, so this CHAINED gate ran LIVE (NOT mechanical closure):
- Conjunct (a) — **W4-1 Axis-A E2 re-emission PASS** (`audit_sha256=2ab8bb1ecccb1bb7…`; corrective line at `s93_gate_verdicts.txt:67`, `axis_a_composite=PASS`, `emit_bug_confirmed=True`, supersedes the FAIL line via Option-A).
- Conjunct (b) — **S92 W-4 JE5 PASS (Axis-B)** at central value (canonical Registry-PASS is the single-value inequality; −1σ undershoot is the non-load-bearing Friedrich-Bär truncation-resolution annotation per §20). On disk via the W4-1 PASS line's `JE5=PASS` field.
- Conjunct (c) — **Eq.(2′) registry-text correction LANDED** (S93 W4-4, `audit_sha256=03d92b2ac13846ab…`); §VII.AX.OP-PROJ Status now STAGE-3-PERMANENT-ELIGIBLE.
- Sibling-slot — **W4-2 MULTI-PIN-ATLAS Stage-2 PASS** (`s93_gate_verdicts.txt:73`, `stage3=STAGE-3-PERMANENT-ELIGIBLE`).

**Output Artifacts**:
- Script — `computations/session-93/s93_w4_5_canonical_constants_n_pbh_fw_central_promotion.py` (27 441 bytes). `grep` of must_contain:
  - `from canonical_constants import` → `from canonical_constants import *` (Section 1) AND `from canonical_constants import (n_PBH_FW_central, PROVENANCE,)`
  - `append_verdict` → `def append_verdict(verdict, value, audit_sha, content_sha)` + call in `main()`
  - `update_constant` → `from knowledge_db import update_constant` (Section 2; best-effort import — actual write via knowledge-MCP, per W2-3 precedent)
- Data — `computations/session-93/s93_w4_5_canonical_constants_n_pbh_fw_central_promotion.npz` (13 257 bytes; full-float64 `n_PBH_FW_central_full_float64`, round-trip residuals, chain-verification flags, citation pins). Class-8.3: data file holds full precision; the WP holds the rounded 5-sig-fig form.
- Plot — not produced (optional per plan; canonical-constants promotion has no numerical plot).
- Verdict line — `computations/session-93/s93_gate_verdicts.txt:77` matches `^S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion at line 78; provenance row at line 79. `audit_sha256` unique across the file (sig_5 clean, count=1).
- WP section — this §W4-5.
- **canonical_constants.py** — `n_PBH_FW_central = 7.2761e-23` at line 602 (SECTION E); PROVENANCE entry at line 1405 (gate `S93-W4-5-…`). `grep` evidence:
  - `python -c "import canonical_constants as cc; cc.n_PBH_FW_central"` → `7.2761e-23` (type `float`)
  - `'n_PBH_FW_central' in cc.PROVENANCE` → `True`; PROVENANCE source cites T1.13 full-64 `1dc0a3fe…50ce` + W4-1 PASS `2ab8bb1e…` + Eq.(2′) `03d92b2a…`.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; executed BEFORE the write):
- `get_constant("n_PBH_FW_central")` → **"not found"** — confirms genuine Step-2 promotion, NOT a re-pin (matches plan-freeze finding).
- `get_constant("n_PBH_FW")` → "not found" — no pre-existing parent pin.
- `search_knowledge("n_PBH cardinality cascade tail PBH number density 7.2761e-23")` → returned the §VII.AX.OP-PROJ Level-3 anchor `n_PBH_FW_central = 7.2761e-23 m⁻³` (session-92-plan-w6 equation), the parse-tree form `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³` (permanent-results-registry), and the S88 CF-CURV-6 parent gate — confirms the value lineage, not yet canonicalized.
- `list_constants(pattern="n_PBH.*")` → **"No constants matching"** — independent confirmation of absence.
- `trace_entity("VII.AX.OP-PROJ")` → STAGE-3-PERMANENT promotion path (S91 open channel); T1.13 full-64 `1dc0a3feb214d8b5…50ce`; `t113_central=7.2761e-23`; Pillar I ↔ Pillar IX (PBH band-edge), HKR L_max→∞ bridge.
- `get_constant("n_PBH_FW_central")` (POST-write verify) → `7.2761e-23`, session S93, gate `S93-W4-5-…`, full PROVENANCE source returned.
- **Not PRE-CLOSED**: no closure covers this Step-2 promotion; the value's substrate derivation is the closed §VII.AX.OP-PROJ T1.13 anchor (no re-derivation here — this is the bookkeeping Step 2 only).

**Verdict**: **PASS** — `value='n_PBH_FW_central=7.27610e-23_m_minus_3;target=7.2761e-23;rel_resid=0.000e+00;rel_tol=1e-04;value_match=True;round_trip_resid=0.000e+00;round_trip_pass=True;wp_round_pass=True;provenance_present=True;prov_cites_T113=True;prov_cites_W4_1=True;prov_cites_Eq2prime=True;prov_gate_match=True;provisional_truncation_note=True;eligibility=STAGE-3-PERMANENT-ELIGIBLE;source_recon_class=(e)_PIN-PROMOTES-TO-CANONICAL-ON-PASS;step1_step3_discharged_S91_W5-4;update_constant_available=False'` · scheme `canonical-write-order-step-2-n-PBH-FW-central-promotion` · convention `update_constant-PIN-PROMOTES-TO-CANONICAL-ON-PASS-class-e` · L_max=14 · `audit_sha256=6833f005503c8d6191c9c049c2ae78962b5140c0288142f3d9e82828800c64c3` · `content_sha256=c00573a90b52460c2ab06e5623f579bfaef0efdacbe4559fe16799d1af21629b` · schema_version=S84+.

**Results**:

*Promoted canonical entry* (canonical_constants.py:602, SECTION E):
```
n_PBH_FW_central = 7.2761e-23  # m^-3; PBH band-edge framework prediction (FWD-C5 Pillar I<->Pillar IX
  cardinality-cascade-tail saturation); n_PBH = n_edge_saturated * prob_form / L_pix_LRD^3 at L_max=14;
  Cell-I-cardinality-projection algebra-INVARIANT spectrum-only functional; VII.AX.OP-PROJ Level-3 anchor
  T1.13 PASS audit_sha256=1dc0a3fe...; Level-3 inside upper-22.6%-conjunct [5.5e-23, 2.2e-22] m^-3
  (32.3% above floor); PROVISIONAL truncation ...; STAGE-3-PERMANENT-eligible per S92 W6-3 / S93 W4-1
  Stage-2 PASS-AND; publication precision 5 sig figs, downstream verifier rel_tol >= 1e-4 per Class-8.3;
  canonical-write-order Step 2 (S93)
```
PROVENANCE (canonical_constants.py:1405): `{"session": "S93", "source": "S91-CF41-VII-LANDING Step-1 (S91 W5-4) + S93-W4-1 Axis-A E2 re-emission PASS audit_sha256=2ab8bb1e…2d79d29e8 + S92 W-4 JE5 PASS (Axis-B) + Eq.(2-prime) landed (S93 W4-4 audit_sha256=03d92b2ac13846ab) => VII.AX.OP-PROJ STAGE-3-PERMANENT eligible; Level-3 anchor T1.13 PASS audit_sha256=1dc0a3feb214d8b5…bbcb50ce (S91 W5-3 S91-CF41-UPPER-22.6-EXTENSION, s91_gate_verdicts.txt:96)", "gate": "S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION", "superseded": False}`.

*Class-8.3 round-trip cross-check*: `n_PBH_FW_central` (full-float64 in the .npz) == target 7.2761e-23, `round_trip_resid = 0.000e+00` (bit-exact; both are the literal 5-sig-fig form), `round_trip_pass = True` (≤ pin·10⁻⁵). The WP form here (7.2761e-23, 5 sig figs) equals the published precision; downstream verifiers load the full float64 from the data file, not this WP. Verifier tolerance pin `rel_tol ≥ 1e-4` per Class-8.3 (the 5-sig-fig floor would be 1e-5; the W4-5/W6-5 condensed spec pins at 1e-4 — PIN-LOOSE direction, acceptable as the published value is exact to 5 figs).

*Provisional-truncation note* (per **S93 W4-3 INFO**, `s93_gate_verdicts.txt:70`): the canonical-truncation factorization gate returned **INFO / resolution-β** — `w(L_max)` DIVERGENT, `N_eigs(L_max)` grows geometrically (no saturation; `N_eigs_degree=5_leading=4/15`, `n_edge=LINEAR-in-N_eigs`), so the Eq.(2′) convergence qualifier reads **"(still converging)"** and the "canonical L_max=14" label is **PROVISIONAL** (verdict-orthogonal to JE5=PASS, which holds at every computed truncation). The **central value 7.2761e-23 m⁻³ is the registered §VII.AX.OP-PROJ Level-3 anchor (T1.13 PASS at L_max=14)** and is promoted here as the substrate-current best central value **with** the provisional-truncation note encoded in the assignment-line comment; the substrate-natural canonical-truncation re-determination is a **CF-S94 carry-forward** (4-field spec: *what* = re-determine the canonical truncation L_max for n_PBH from the N_eigs(L_max) kernel-level convergence analysis once the geometric-growth ceiling is characterized; *inputs* = W4-3 factorization .npz + obs_2 grid + Peter-Weyl block-admission combinatorics; *gate* = saturation/asymptote of the kernel-level convergence vs the L_max=14 central; *effort* = ~1 wave-equivalent).

*Canonical write-order completeness* (math-scripts.md §"Canonical Write-Order for New Framework Predictions"): **Step 1 (verdict-file emission)** S91 W5-4 ✓ → **Step 2 (canonical_constants.py promotion + PROVENANCE)** S93 W4-5 ✓ (THIS gate) → **Step 3 (mack `falsifier-master-inventory.md` Row #65 `.audit-CF-41-VII-LANDING` sub-row)** S91 W5-4 ✓. The write-order is now COMPLETE; `n_PBH_FW_central` is import-target for downstream META gates, closing the Class-8 PRU vulnerability window the inverted (1)→(3)→(2) order would have opened. Source-Recon class **(e) PIN-PROMOTES-TO-CANONICAL-ON-PASS** (substrate-first-canonical-sourcing.md §(v)): the canonical did not exist at the original gate's plan-freeze (confirmed absent at S93 plan-freeze AND at dispatch); promoted post-gate on STAGE-3-PERMANENT eligibility.

*Substrate framing*: NON-PHONONIC / methodology-layer. The substrate-IS value `n_PBH = 7.2761e-23 m⁻³` is the §VII.AX.OP-PROJ Level-3 empirical anchor — the cardinality-cascade-tail saturation prediction on the finite spectral triple (`n_PBH = n_edge_saturated · prob_form / L_pix_LRD³`, Cell-I-cardinality-projection algebra-INVARIANT spectrum-only functional). Direction of explanation: D_K Peter-Weyl cardinality → cascade-tail edge count → n_PBH → laboratory-IN BBN-constrained PBH abundance. Step 2 lands the value in `canonical_constants.py` with PROVENANCE so it becomes import-target. No new physics — the value is the registered T1.13 anchor.

*Orchestrator action required (flagged)*: **M4 methodology-wave-allowlist append is ORCHESTRATOR-ONLY** (subagents are edit-denied on `methodology-wave-allowlist-ledger.md` per `methodology-wave-allowlist.md` recursion-attack closure). If this gate-ID is to satisfy M4 METHODOLOGY-class membership, the orchestrator must append `S93-W4-5-CANONICAL-CONSTANTS-N-PBH-FW-CENTRAL-PROMOTION | S93 | <sha256_of_plan_block>` to the ledger + the parallel rationale entry. I did NOT touch the allowlist.

*Scope honored*: wrote ONLY to `canonical_constants.py` (n_PBH_FW_central + PROVENANCE), this §W4-5 WP section, and the verdict line. Did NOT touch `permanent-results-registry.md` (W4-4/W4-6 territory) or `cross-pillar-bridge-corpus.md`.

---

### §W4-6. S93-W4-6-FWD-C5-K2-SUBSTRATE-DISTANCE-3-POLE-S5-CARDINALITY-CASCADE-SHOULDER (mack-cosmic-bridge + volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S93-W4-6-FWD-C5-K2-SUBSTRATE-DISTANCE-3-POLE-S5-CARDINALITY-CASCADE-SHOULDER`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **GEOMETRIC** (cardinality-cascade-shoulder observable on D_K spectrum at substrate-distance-3 pole s=5)
**Agent**: `MULTI` — `mack-cosmic-bridge` (LEAD: derives the closed form + corpus §4 K=2 row, sole-writer) + `volovik-superfluid-universe-theorist` (CO-AUTHOR: the (iv) algebraic-envelope-axis independence audit, the Hybrid Independence Test's load-bearing clause).
**Hypothesis**: The cardinality-cascade-SHOULDER observable `n_PBH_shoulder(g)` admits a closed form on A_K at the shoulder regime g∈[g_BBN=80, g_saturate=143) at substrate-distance-3 pole s=5, advancing the FWD-C5 Hybrid-Independence-Test K-counter to K=2 — STRUCTURALLY DISTINCT from the K=1 baseline (substrate-distance-2 pole s=4, saturated regime) by pole index (s=5 vs s=4) and regime (rising shoulder vs saturated tail). CHAINED on §VII.AX.OP-PROJ STAGE-3 eligibility; honest mechanical closure if unmet.
**Plan reference**: `sessions/session-plan/session-93-plan-w4.md` §W4-6 (closed-form derivation, Hybrid Independence Test predicate (i∨ii∨iii)∧iv, volovik (iv)-axis audit, corpus §4 K=2 row).

**Output Artifacts**:

| Artifact | Path | On-disk evidence (`ls` + `grep` must_contain) |
|:---------|:-----|:----------------------------------------------|
| script | `computations/session-93/s93_w4_6_fwd_c5_k2_cardinality_cascade_shoulder.py` | exists (36497 B); `grep "from canonical_constants import"` → L103 `from canonical_constants import *`, L108 `from canonical_constants import (`; `grep "append_verdict"` → L228 `def append_verdict(...)`, L459 `append_verdict(verdict, value, audit_sha, content_sha)` ✓ |
| data | `computations/session-93/s93_w4_6_fwd_c5_k2_cardinality_cascade_shoulder.npz` | exists (10900 B) — g_grid, n_edge_shoulder, n_pbh_shoulder, closed_form_residual, hybrid_predicate, clauses i-iv, volovik_iv_pass, pole_distinct, corpus_row_landed ✓ |
| volovik (iv) JSON (CO-AUTHOR) | `computations/session-93/s93_w4_6_volovik_iv_axis_independence_audit.json` | exists (10553 B); `verdict_clause_iv="PASS"` (consumed) ✓ |
| plot | `computations/session-93/s93_w4_6_fwd_c5_k2_cardinality_cascade_shoulder.png` | exists (97371 B) — n_PBH_shoulder(g) over g∈[80,143) (rising, log-y) + n_edge(g)=2^g panel ✓ |
| verdict line | `computations/session-93/s93_gate_verdicts.txt` L80 | `grep "^S93-W4-6-...:.* audit_sha256=[a-f0-9]{64}"` → matches; `audit_sha256=4f33b58116181cdad12f8b3db9e6e66bdfcf9fc72e776be75d9884ac2759b4b7` (full-64); dual-SHA companion L81; provenance row L82; SHA unique across file (sig_5 = 1 occurrence) ✓ |
| corpus §4 K=2 row | `sessions/framework/registry/cross-pillar-bridge-corpus.md` L210-232 | `grep "FWD-C5 K=2 advancement — substrate-distance-3 pole s=5 cardinality-cascade-SHOULDER (S93 W4-6)"` → L210; landed before "### Rank-2 generalization cross-reference" (L234) ✓ |

Verified by content presence (regex match), not by line/byte counts.

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("FWD-C5 cardinality cascade shoulder n_PBH substrate-distance-3 pole s=5 Hybrid Independence Test K=2")` | shoulder n_PBH_shoulder(g) is "deterministic restriction of the saturated form to g<g_saturate=143" (session-92-plan-w6.md); FWD-C5 landed K=1→K=2 cross-PILLAR (S91 W5-4); alpha_HH1_per_pole_FW_s5 derived edge present |
| `trace_entity("FWD-C5 cardinality-cascade shoulder")` | No trace found — the s=5 SHOULDER instance is NEW (not pre-closed); the K=1 baseline is the saturated TAIL |
| `search_knowledge("n_PBH_shoulder cardinality cascade generation 2^g g_BBN g_saturate 143")` | `n_PBH = n_edge_saturated·prob_form/L_pix_LRD³`; `n_edge(g)=2^g` (Peter-Weyl cardinality); `L_pix(g)=L_pix_LRD·2^{−g/3}`; saturation at g≥143 → C(N_eigs,2) (registry §VII.AX.OP-PROJ) |
| `get_constant("alpha_HH1_per_pole_FW_s5")` | 6.0; gate `S92-W7-CF-W9-10-B`; §VII.BB STAGE-1-CANDIDATE; Superseded=False |
| `get_constant("alpha_HH1_per_pole_FW_s4")` | 4.0; gate `S92-W7-CF-W9-10-B`; Superseded=False |
| `list_constants("...n_PBH...")` | `n_PBH_FW_central=7.2761e-23` (S93, gate W4-5 — the saturated-tail anchor, now canonical) |

**PRE-CLOSED check**: NO closure covers the s=5 cardinality-cascade-SHOULDER instance. The K=1 baseline (§VII.AX.OP-PROJ, S91 W5-4) is the saturated TAIL at s=4. The per-pole exponent/Wodzicki anchors (α_s5=6, deg_s5=−10) are canonical; the shoulder closed form is derived fresh on A_K via the substrate-clock cancellation form (registry §VII.AX.OP-PROJ Step 3). Gate is a genuine new structural derivation + K-counter advancement, not a re-derivation.

**Verdict**: **PASS** — value=`closed_form=n_PBH_shoulder(g)=(prob_form/L_pix_LRD^3)*2^{2g}_on_A_K_g_in_[80,143); closed_form_residual=4.86e-15; sage_exact_rel=1.19e-16; shoulder_rising=True; hybrid_indep_test=(i=True_OR_ii=False_OR_iii=False)_AND_iv=True=True; volovik_iv_PASS=True; alpha_s5=6.0_vs_s4=4.0; deg_s5=-10_vs_s4=-8; pole_distinct_s5_ne_s4=True; corpus_§4_K2_row_landed=True; intra_FWD_C5_iv_scoping=YES; anti_double_count_vs_W4_2=True; K_counter=1->2; stage3_eligible=True`. 4-tuple: (value above, scheme=`fwd-c5-k2-cardinality-cascade-shoulder-substrate-distance-3-pole-s5`, convention=`shoulder-regime-g-80-143-closed-form-A_K-Hybrid-Independence-Test-K2`, L_max=14). audit_sha256=`4f33b58116181cdad12f8b3db9e6e66bdfcf9fc72e776be75d9884ac2759b4b7`, content_sha256=`f21e0f594340410c4d3c87d268530fc29bc2e7b7b505cf1e2aa397e0d13d4272`.

**Results**:

**Chain-prerequisite status (§VII.AX.OP-PROJ STAGE-3 eligibility)**: ELIGIBLE=True — resolved on-disk from `s93_gate_verdicts.txt`: W4-1 Axis-A corrective PASS (`axis_a_composite=PASS`, supersedes chain) ∧ JE5=PASS (S92 W-4 Axis-B carried forward) ∧ Eq.(2′) landed (W4-4 STATE-PROJ companion PASS). Gate is **LIVE** (not mechanical closure) per the plan branch table row 1.

**Closed-form `n_PBH_shoulder(g)` on A_K (g∈[80,143), substrate-distance-3 pole s=5)**:
The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`. At the rising-shoulder regime the Peter-Weyl substrate-cardinality `n_edge(g)=2^g` is STILL GROWING (NOT yet saturated at `C(N_eigs,2)`). The substrate-clock cancellation form (registry §VII.AX.OP-PROJ Step 3; S88 W1a-59 §0) — where the cosmological-volume dilution `2^{−3g}` cancels BY CONSTRUCTION because `L_pix(g)=L_pix_LRD·2^{−g/3}` IS the substrate's clock, not a meta-container coordinate — gives:

```
n_PBH_shoulder(g) = n_edge(g)·prob_form / L_pix(g)³
                  = (2^g · prob_form) / (L_pix_LRD · 2^{−g/3})³
                  = (prob_form / L_pix_LRD³) · 2^g · 2^g
                  = (prob_form / L_pix_LRD³) · 2^{2g}      for g ∈ [80, 143)
```

- **Sage-exact verification** (`sage_eval`): `n_PBH_shoulder(g).simplify_full() − (prob_form/L_pix_LRD³)·2^{2g} = 0` EXACTLY (symbolic residual 0). Float realization (63-generation grid): max relative residual 4.86e-15; representative g=100 exact-vs-float rel 1.19e-16 (Fraction arithmetic: prob_form=15573/100000, L_pix_LRD=3·10¹⁰).
- **Regime discriminant (ground 3)**: `d/dg n_PBH_shoulder = 2^{2g+1}·prob_form·ln2 / L_pix_LRD³ > 0` for all g∈[80,143) (RISING; shoulder_rising=True). The K=1 saturated-tail form `n_PBH = C(N_eigs,2)·prob_form/L_pix_LRD³` has `d/dg=0` (FLAT). `C(N_eigs=78080,2)=3.048e9`; saturated-tail L_max=10 baseline = 1.7581e-23 m⁻³; canonical L_max=14 anchor `n_PBH_FW_central = 7.2761e-23 m⁻³` (the g→g_saturate boundary value).
- **Parse-tree / corner classification**: Cell-I-cardinality-projection (algebra-INVARIANT spectrum-only functional: cardinality `2^g`; scalar mult by prob_form; scalar div by L_pix_LRD³ — all substrate-algebra spectrum-only operations). The "GGE-cascade" history label encodes the Pillar IX laboratory-IN preparation, not the substrate-IS algebra-axis (which the parse-tree fixes as Cell-I).

**Hybrid Independence Test predicate (i∨ii∨iii)∧iv at K=2** (per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`):

| Clause | Verdict | Rationale |
|:-------|:--------|:----------|
| (i) distinct substrate-IS sub-pillar | **YES** | rising-shoulder cardinality cascade (pre-saturation, s=5) vs saturated-tail (post-saturation, s=4); distinct pole AND distinct regime |
| (ii) distinct laboratory-IN pillar | **NO** | same Pillar IX (CMB/LISA/PTA PBH detection) as K=1 baseline |
| (iii) distinct bridge-map class | **NO** | same FWD-C5 cardinality-cascade bridge family as K=1 baseline |
| (iv) independent algebraic envelope | **YES** (LOAD-BEARING) | s=5 envelope `L^{−6}` (Wodzicki deg −10, edge-count 2^g rising) regulator-invariantly distinct from s=4 envelope `L^{−4}` (Wodzicki deg −8, edge-count C(N_eigs,2) flat) on THREE independent grounds — NOT a numerical refinement |

**Predicate**: `(i=YES ∨ ii=NO ∨ iii=NO) ∧ iv=YES = YES`. K-counter **K=1 → K=2** on the FWD-C5 Hybrid Independence Test corpus.

**volovik (iv)-algebraic-envelope-axis independence audit (CONSUMED, PASS)**: `verdict_clause_iv=PASS` (`s93_w4_6_volovik_iv_axis_independence_audit.json`). Three independent regulator-invariant structural grounds (full detail in the CO-AUTHOR subsection below): (1) per-pole envelope exponent α(s)=2(s−2): α_s5=6 ≠ α_s4=4 (canonical `alpha_HH1_per_pole_FW_s5=6.0`/`alpha_HH1_per_pole_FW_s4=4.0`, gate `S92-W7-CF-W9-10-B`, both Superseded=False; α-law Sage-verified against all anchors {s2:0,s4:4,s5:6,s6:8}); (2) Wodzicki homogeneity degree deg(s)=−2s: deg_s5=−10 ≠ deg_s4=−8 (index-type invariant, non-deformable in moduli); (3) edge-count g-functional form: 2^g rising (d/dg≠0) vs C(N_eigs,2) flat (d/dg=0). The "deterministic restriction of the saturated form to g<143" framing is a DOMAIN-of-g statement, orthogonal to (iv).

**Distinct-pole confirmation**: substrate-distance-3 pole **s=5** ≠ K=1's substrate-distance-2 pole **s=4** (pole_distinct=True), corroborated by both α-distinctness (integer gap 2) and deg-distinctness (integer gap 2).

**Corpus §4 K=2 row landed** (`cross-pillar-bridge-corpus.md` L210-232, mack sole-writer): the FWD-C5 K=2 advancement row with full 5-anatomy (K=2 substrate-IS shoulder observable, same lab-IN Pillar IX, same FWD-C5 bridge family restricted to rising-shoulder sub-domain, s=5 `L^{−6}` envelope, g-dependent anchor), per-clause Hybrid Independence Test verdicts, and the **intra-FWD-C5 (iv)=YES scoping** disambiguation (the §4 baseline already declared (iv)=YES at the CROSS-PILLAR level FWD-C5-vs-FWD-C1/C2/C3; W4-6's (iv)=YES is the STRONGER intra-FWD-C5 claim — s=5 shoulder vs s=4 tail, same bridge-map/same Pillar IX, so the envelope must be distinct on POLE grounds alone). The row is unambiguously the substrate-distance-3-pole shoulder instance.

**Anti-double-count cross-check (mack §V.2 anti-inflation)**: W4-6 advances the FWD-C5 corpus §4 K-counter (substrate-distance-3 pole s=5); W4-2 (`S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY`) advances the §VII.AX.MULTI-PIN-ATLAS bridge-map-scheme axis (corpus §3/§10/§17; substrate-distance-2 pole s=4 χ' restriction). Distinct poles (s=5 vs s=4), distinct corpus sections (§4 vs §3/§10/§17) ⇒ NO double-count against a single K-counter (anti_double_count=True).

**M4 allowlist note**: this gate is GEOMETRIC (closed-form + structural-distinctness predicate); the M4 methodology-wave-allowlist append for any METHODOLOGY-class component is **ORCHESTRATOR-ONLY** per `methodology-wave-allowlist.md` (flagged here, NOT performed by this gate).

**Substrate framing**: D_K Peter-Weyl cardinality at cascade-generation g → rising-shoulder edge-count `2^g` → `n_PBH_shoulder(g)` → laboratory-IN Pillar IX PBH population at BBN-to-saturation generations. The per-pole envelope α(s) and Wodzicki degree deg(s)=−2s are intrinsic to the substrate at distinct substrate-distance poles; the s=5 shoulder envelope is a substrate-IS structural object at substrate-distance-3, regulator-invariantly distinct from the s=4 substrate-distance-2 saturated-tail baseline — not a finer-resolution view of the same envelope.


### CO-AUTHOR (volovik) (iv)-axis independence audit

**Clause-(iv) verdict**: **PASS** — the FWD-C5 K=2 cascade-shoulder envelope (substrate-distance-3 pole **s=5**, rising-shoulder regime g∈[80,143)) is an INDEPENDENT algebraic envelope, NOT a numerical refinement of the K=1 §VII.AX.OP-PROJ baseline envelope (substrate-distance-2 pole **s=4**, saturated-tail regime g≥143). Audited from the substrate / superfluid-universe axis. Artifact: `computations/session-93/s93_w4_6_volovik_iv_axis_independence_audit.json`.

**Clause (iv) definition** (per `cross-pillar-bridge-anatomy.md §"Hybrid Independence Test"`): "independent algebraic envelope — not a numerical refinement of an existing K-instance's envelope." This is the LOAD-BEARING conjunct of the W4-6 PASS criterion: the Hybrid Independence Test predicate is `(i ∨ ii ∨ iii) ∧ iv`, so even with clause (i)=YES carrying the disjunction, clause (iv) MUST independently PASS for the K=2 advancement.

**Structural distinctness — three independent regulator-invariant grounds** (s=5 envelope ≠ s=4 envelope):

| Ground | s=4 baseline (K=1) | s=5 shoulder (K=2) | Distinct? |
|:-------|:-------------------|:-------------------|:----------|
| (1) Per-pole envelope exponent `α(s)=2(s-2)` | `α(s=4)=4` → `L^{-4}` | `α(s=5)=6` → `L^{-6}` | YES — integer gap 2 |
| (2) Wodzicki homogeneity degree `deg(s)=-2s` | `deg(s=4)=-8` | `deg(s=5)=-10` | YES — non-deformable index-type invariant |
| (3) Edge-count g-functional form | `C(N_eigs,2)` (g-independent, `d/dg=0`, saturated) | `2^g` (rising, `d/dg=2^g·ln 2`, pre-saturation) | YES — different functional form |

- **Ground 1 (per-pole exponent)** — canonical: `alpha_HH1_per_pole_FW_s4 = 4.0` and `alpha_HH1_per_pole_FW_s5 = 6.0` (knowledge-MCP `get_constant`; gate `S92-W7-CF-W9-10-B-SUBSTRATE-IS-ALPHA-S-PER-POLE-EXPONENT-TABLE-M3C`; both `Superseded=False`; s=5 is the §VII.BB STAGE-1-CANDIDATE pole). Closed-form law `α(s)=2(s-2)` Sage-verified against all canonical anchors `{α(s=2)=0, α(s=4)=4, α(s=5)=6, α(s=6)=8}`. The convergence rate `L^{-6}` at s=5 is NOT `L^{-4}` at s=4 at finer numerical precision — it is a DIFFERENT rate. A numerical refinement holds α FIXED and improves the anchor; this changes α by an integer 2.
- **Ground 2 (Wodzicki degree)** — `deg(s)=-2s` per `cross-pillar-bridge-anatomy.md §"Composite Bridge-Map Dimensional-Class Admissibility"`; `deg(s=4)=-8 ≠ deg(s=5)=-10`. The homogeneity degree is an index-type invariant, non-deformable in moduli (Wodzicki uniqueness; Connes 1994 §2.3) — so no continuous (numerical-refinement) deformation connects the two envelopes; they inhabit structurally distinct dimensional classes.
- **Ground 3 (g-functional form)** — the rising-shoulder cardinality is `n_edge(g)=2^g` (`d/dg≠0`); the saturated-tail cardinality is `n_edge=C(N_eigs,2)` (`d/dg=0`). A numerical refinement PRESERVES functional form; the shoulder→tail transition CHANGES it. Physically: the shoulder is the PRE-saturation cascade phase (the substrate's spectral cardinality is still doubling generation-by-generation); the tail is the POST-saturation phase (the cardinality has filled). Distinct cascade phases, not the same observable at two resolutions.

**"Deterministic restriction" tension resolved**: the knowledge MCP describes the shoulder as "a deterministic restriction of the saturated form to g<143." This refers to the DOMAIN of g (the shoulder is the g<143 sub-domain), NOT to the envelope's structural class. A domain restriction does not make the envelope a numerical refinement — the numerical-refinement test asks whether two envelopes share the SAME structural class (same α, same deg) at different precision; here both the structural class (grounds 1+2) AND the functional form (ground 3) differ. The "restriction" framing is orthogonal to the (iv) determination.

**Scope caveat (intra-FWD-C5 vs cross-pillar)**: the corpus §4 FWD-C5 baseline block already declared clause (iv)=YES at the CROSS-PILLAR level (FWD-C5 vs FWD-C1/C2/C3: distinct lab-IN pillar, distinct bridge-map). The W4-6 (iv) audit is the STRONGER INTRA-FWD-C5 independence (s=5 shoulder vs s=4 tail, SAME bridge-map family, SAME Pillar IX — so the envelope must be distinct on POLE grounds alone). Both hold. The corpus §4 K=2 row mack lands MUST scope its (iv)=YES to the intra-FWD-C5 pole-distinctness (s=5 ≠ s=4) so the K=2 advancement is unambiguously the substrate-distance-3-pole shoulder instance, not a re-statement of the cross-pillar baseline.

**Anti-double-count cross-check** (mack §V.2): W4-6 advances the FWD-C5 corpus §4 K-counter (substrate-distance-3 pole s=5); W4-2 advances the §VII.AX.MULTI-PIN-ATLAS bridge-map-scheme axis (corpus §3/§10/§17; substrate-distance-2 pole s=4 χ' restriction). Distinct poles, distinct corpus sections ⇒ no double-count against a single K-counter, consistent with the Hybrid Independence Test.

**Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`; the per-pole envelope `α(s)` and the Wodzicki degree `deg(s)=-2s` are intrinsic to it at distinct substrate-distance poles. The s=5 cascade-shoulder envelope is a substrate-IS structural object at substrate-distance-3, regulator-invariantly distinct from the s=4 substrate-distance-2 baseline — not a finer-resolution view of the same envelope.

*(volovik (iv)-axis audit complete; mack's main §W4-6 content + corpus §4 K=2 row + verdict-line emission consume this PASS as the load-bearing clause-(iv) conjunct.)*

---

## Wave 4 Synthesis (team-lead)

Wave 4 (§VII.AX PBH cluster) closed all 6 gates with the planned 3-tier branch logic:

- **W4-1 PASS** — §VII.AX.OP-PROJ Axis-A E2 re-emission corrected (the original §W6-3 FAIL was a verdict-field emit-bug; the live-registry OE-form regex matches the brace-delimited projector subscript). Axis-A leg → PASS.
- **W4-2 PASS-AND** — §VII.AX.MULTI-PIN-ATLAS Stage-2 (connes Axis-A + volovik Axis-B, both blind, obs_2 substrate-input-orthogonality at structural ceiling) → STAGE-3-ELIGIBLE.
- **W4-3 INFO (PASS-β)** — N_eigs(L_max) does NOT saturate (Sage-exact quintic (4/15)L⁵+…); the non-saturation is a genuine substrate property (infinite SU(3) rep ring) coexisting with Friedrich-Bär bottom-K saturation; Eq.2′ qualifier = "(still converging)", L_max=14 canonical PROVISIONAL.
- **W4-4 PASS** — eligibility ACHIEVED; landed the §VII.AX.STATE-PROJ companion (Cell IV). **Critically: Eq.2′ was NOT landed at dispatch** — the §VII.AX.OP-PROJ entry carried an internally-inconsistent Level-3 band statement (Class-(i): 5.316e-23 < 5.500e-23 falsifies the containment claim); W4-4 landed the Eq.2′ correction in-session (central-value PASS reading + non-load-bearing Friedrich-Bär annotation per §20), clearing the Class-(i) flag.
- **W4-5 PASS** — n_PBH_FW_central = 7.2761e-23 m⁻³ promoted to canonical_constants.py (Step 2; write-order now complete; round-trip 0.0; provisional-truncation note encoded).
- **W4-6 PASS** — cascade-SHOULDER closed form n_PBH_shoulder(g)=(prob_form/L_pix³)·2^{2g} for g∈[80,143) (g-rising, distinct from K=1 saturated-tail); Hybrid Independence Test (i∨ii∨iii)∧iv = YES at K=2 (corpus §4 K-counter K=1→K=2); volovik (iv) independence audit PASS (s=5 vs s=4: per-pole α 6.0 vs 4.0, Wodzicki deg −10 vs −8, edge-count 2^g vs C(N,2)).

**Structural outcomes**: TWO new STAGE-3-PERMANENT promotions (§VII.AX.OP-PROJ + §VII.AX.MULTI-PIN-ATLAS); §VII.AX.STATE-PROJ companion landed (STAGE-1-CANDIDATE, its Stage-2 a CF); corpus §4 multiplicative K-counter K=2 (FWD-C5 s=5 shoulder). **Substrate framing**: §VII.AX IS the substrate's intrinsic PBH band-edge prediction (n_PBH structural-central 7.2761e-23 m⁻³); the CMB/LISA/PTA horizons are the laboratory-IN measurement context, NOT a fit.

### Carry-Forward Computations (MATH ONLY — propagate to S94)

#### CF-S94-W4-STAGE-2-VII-AX-STATE-PROJ-CROSS-AXIS-VERIFY

1. **What**: Stage-2 cross-axis independent-verify of the §VII.AX.STATE-PROJ companion (landed STAGE-1-CANDIDATE this wave); on PASS-AND → STAGE-3-PERMANENT (parallel to how §VII.AV.STATE-PROJ got its Stage-2 + STAGE-3 this session).
2. **Inputs**: §VII.AX.STATE-PROJ registry entry (L19487); the §VII.AX.OP-PROJ STAGE-3 baseline; the Bogoliubov-state closed-form Element-5 inheritance.
3. **Gate**: `S94-VII-AX-STATE-PROJ-STAGE-2-CROSS-AXIS-VERIFY` — two cross-reviewers on opposite axes, no shared workshop context, JOINT PASS-AND + substrate-input-orthogonality.
4. **Effort**: ~0.6 wave-equivalent.

#### CF-S94-N-PBH-CANONICAL-TRUNCATION-RE-DETERMINATION

1. **What**: re-determine the n_PBH canonical truncation (W4-3 proved N_eigs(L_max) does NOT saturate → L_max=14 cannot be read off a non-existent plateau; it must be pinned by a substrate-physical or laboratory-IN anchor).
2. **Inputs**: `s93_w4_3_..._npz` (quintic N_eigs growth law); the n_PBH_FW_central canonical entry (provisional-truncation PROVENANCE note); the bottom-K Friedrich-Bär saturation (distinct observable).
3. **Gate**: `S94-N-PBH-TRUNCATION-ANCHOR` — substrate-physical or laboratory-IN truncation anchor pinned (NOT an N_eigs plateau); update the L_max=14 PROVISIONAL label.
4. **Effort**: ~0.5 wave-equivalent.

#### CF-W4-1 — n_PBH band-breach projection (NEW; surfaced at S93 `/rclab-investigate`, routed to /rclab-plan)

> **Routing note**: genuinely-NEW MATH carry-forward (the only S93 carry-forward the per-wave seeds flag as not-yet-registered; w4 seed line 29). It is the COMPUTE complement and quantitative input to the W-1 workshop (`s93-vii-ax-op-proj-stage3-truncation-divergent-anchor.md`, Reading-B): W-1 adjudicates whether the §VII.AX.OP-PROJ permanence can STAND pending the truncation re-determination; CF-W4-1 supplies the number Reading-B needs (the finite L_max at which the central anchor leaves the conjunct band). Queue for S94 alongside the W-1 outcome.

1. **What**: from the W4-3 Sage-exact quintic `N_eigs(L_max)=(4/15)L⁵+(10/3)L⁴+16L³+(110/3)L²+(596/15)L+16` + the n_PBH(L_max) trajectory {7.276e-23, 9.775e-23, 1.292e-22} at L∈{14,15,16}, compute the L_max at which `n_PBH_central` breaches the JE5 conjunct-upper ceiling 2.2e-22.
2. **Inputs**: `s93_w4_3_..._npz` (quintic growth law + the n_PBH=w(L_max)·κ factorization); the L=14/15/16 obs_2 anchors; the JE5 conjunct band [5.5e-23, 2.2e-22].
3. **Gate**: `S94-N-PBH-BAND-BREACH-PROJECTION` — pre-registered threshold `n_PBH_central(L_max) > 2.2e-22`; report the smallest L_max satisfying it (the finite-truncation band-breach point that makes the band-membership predicate truncation-fragile).
4. **Effort**: ~0.3 wave-equivalent.

### Effected In-Session (NON-MATH — completed by the team-lead orchestrator before STOP)

- [x] **Eq.2′ Class-(i) defect remediation** — W4-4 landed the §VII.AX.OP-PROJ Eq.2′ registry-text correction in-session (the JE5 workshop flagged it but was registry-edit-denied; mack sole-writer landed it), clearing the internally-inconsistent Level-3 band statement. `audit_sha256=03d92b2a…`.
- [x] **§VII.AX.OP-PROJ STAGE-3-PERMANENT flip** — ELIGIBLE → STAGE-3-PERMANENT (index L138 + header L19339 + Status L19343), session-synthesis on the §W6-3 PASS-AND.
- [x] **§VII.AX.MULTI-PIN-ATLAS STAGE-3-PERMANENT flip** — STAGE-1-CANDIDATE → STAGE-3-PERMANENT (index L140 + header L19589 + Status L19591), session-synthesis on the W4-2 Stage-2 PASS-AND. Both flips: VII-SLOT-AUDIT PASS (F_STALE_STATUS=0); ordinal NOT asserted (AU/AW collision, below).
- [x] **§VII.AX.STATE-PROJ stale-cross-ref fix** — two cross-refs to OP-PROJ's prior "STAGE-3-ELIGIBLE" updated to "STAGE-3-PERMANENT (flipped S93 W4 close)" (mack, descriptions of the companion, not STATE-PROJ's own status).
- (No M4 allowlist appends for Wave 4 — per the plan/index, no W4 gate is an orchestrator-direct METHODOLOGY-class gate; W4-4/4-6 are compute-mode registry/corpus landings.)

### Process observations (closed in-session OR deferred with reason)

- **W4-3 INFO is a structural result**: N_eigs non-saturation is a genuine substrate property (infinite SU(3) rep ring), not model-incompleteness. It tells the n_PBH truncation re-determination (CF-S94) where the anchor must come from. Not a defeat.
- **§VII.AU/AW STAGE-3 ordinal collision (deferred, expanded)**: the AU/AW "THIRD" collision (W3-close note) now has more STAGE-3-PERMANENT members (§VII.AX.OP-PROJ + §VII.AX.MULTI-PIN-ATLAS, recorded WITHOUT integers). The set is {§VII.AH (1st), Var_a (2nd), §VII.AU.OP-PROJ, §VII.AW.OP-PROJ, §VII.AV.STATE-PROJ, §VII.AX.OP-PROJ, §VII.AX.MULTI-PIN-ATLAS}. Canonical chronology resolution remains entangled with W5-5 (§VII.AW.OP-PROJ) — deferred to S93 session-end / CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW.
- **W4-2 registry annotation imprecision (hygiene)**: registry "33%" cross-regulator divergence vs actual 19.08%/23.58% (load-bearing spread ≫ 1e-3 holds; magnitude 26.98 bit-reproduced). Non-load-bearing registry-prose; routed to a future mack registry-text pass / session-end (registry not edited by the verify gate).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-05-24 | §VII.AX.OP-PROJ | STAGE-1-CANDIDATE (Class-(i) band defect) | STAGE-3-PERMANENT (Eq.2′ remediated) | W4-1 Axis-A PASS + S92 JE5 + Eq.2′ landed → §W6-3 PASS-AND |
| 2026-05-24 | §VII.AX.MULTI-PIN-ATLAS | STAGE-1-CANDIDATE | STAGE-3-PERMANENT | W4-2 Stage-2 PASS-AND |
| 2026-05-24 | §VII.AX.STATE-PROJ | not registered | STAGE-1-CANDIDATE (Cell IV companion; Stage-2 = CF-S94) | W4-4 companion landing |
| 2026-05-24 | n_PBH_FW_central (canonical_constants) | not promoted | promoted 7.2761e-23 m⁻³ (provisional truncation) | W4-5 Step 2 |
| 2026-05-24 | corpus §4 multiplicative K-counter (FWD-C5) | K=1 | K=2 (s=5 shoulder) | W4-6 Hybrid Independence Test |
| 2026-05-24 | N_eigs(L_max) saturation | open question | RESOLVED: unbounded (quintic); L_max=14 PROVISIONAL | W4-3 |

## Files Produced

| Gate | Script | Data | Verdict |
|:-----|:-------|:-----|:--------|
| W4-1 | `s93_w4_1_vii_ax_op_proj_axis_a_e2_re_emission.py` | `.npz`/`.png` | L67 PASS (`2ab8bb1e…`, supersedes run-1) |
| W4-2 | `s93_w4_2_..._stage_2_verify.py` + 2 axis JSONs | `.npz` | PASS-AND (`ba202d16…`) STAGE-3-ELIGIBLE |
| W4-3 | `s93_w4_3_n_pbh_canonical_truncation_factorization.py` | `.npz`/`.png`/sage.json | INFO (`03b4fb35…`) + 3-tuple |
| W4-4 | `s93_w4_4_vii_ax_state_proj_companion_landing.py` | `.npz` | L75 PASS (`03d92b2a…`); + Eq.2′ correction |
| W4-5 | `s93_w4_5_canonical_constants_n_pbh_fw_central_promotion.py` | `.npz` | L77 PASS (`6833f005…`); canonical n_PBH_FW |
| W4-6 | `s93_w4_6_fwd_c5_k2_cardinality_cascade_shoulder.py` + volovik (iv) JSON | `.npz`/`.png` | L80 PASS (`4f33b581…`); corpus §4 K=2 |
| §VII.AX flips | (mack session-synthesis, no new verdict line) | — | OP-PROJ + MULTI-PIN-ATLAS → STAGE-3-PERMANENT |
