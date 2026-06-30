# Session 97 Wave 6 — Canonical-constants promotion & registry hygiene (Results Working Paper)

**Session**: 97 | **Wave**: W6 | **Plan**: session-97-plan-w6.md | **Theme**: Canonical-constants promotion & registry hygiene (METHODOLOGY-class) — Step-2 `update_constant` provenance promotions (four pins) + a verdict-file companion-comment annotation-hygiene decision.

## Gate Sections

### §W6-1. S97-W6-1-OMDM-RHOVAC-PINS (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S97-W6-1-OMDM-RHOVAC-PINS`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (canonical-pin provenance completeness + per-pin source-keying; the two promoted quantities span a lab-IN datum and a substrate-first prediction-ratio, the gate is the keying decision + PROVENANCE existence, not a substrate-physics compute)
**Agent**: `gen-physicist`
**Hypothesis**: The two W8-5 register/gate-sourced reproducer headlines (`Ω_DM h²=0.1200`, `ρ_vac/ρ_obs=1.032`) promote to `canonical_constants.py` with non-empty PROVENANCE AND each correctly source-keyed (Ω_DM h² → OBSERVATIONAL-ANCHOR; ρ_vac/ρ_obs → FRAMEWORK-PREDICTION per DILUTION-CC-66), so a future one-command reproducer resolves them RESOLVED-CANONICAL.
**Plan reference**: `sessions/session-plan/session-97-plan-w6.md` §W6-1 (+ `## ORCHESTRATOR PLAN-FREEZE RECONCILIATION` for the two w1-routed pins).

**Scope note (4-pin §W6-1 invariant; this gate promotes 2)**: the plan §W6-1 ORCHESTRATOR-RECONCILIATION folded two FURTHER w1-routed substrate-internal pins (`x_fold`, `Omega_BA_fold`) into the §W6-1 enumeration. Those were **already promoted to canonical in S97 W1** (fix-in-session): `x_fold=85.7928` via `S97-W1-XTODAY` PASS; `Omega_BA_fold=2.241353` via `S97-W1-OMEGA-PROFILE` PASS. They are therefore OUT of this gate's promotion scope and are **NOT re-added** (`update_constant` refuses overwrite; re-adding would be a duplicate). This gate's verifier CROSS-CHECKS (read-only) that both already resolve as canonical — confirming the four-pin §W6-1 invariant holds (**2 promoted here + 2 already-canonical-from-W1**). No technical debt: the w1↔w6 cross-wave routing is closed in-session.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
- `computations/session-97/s97_w6_omdm_rhovac_pins.py` (25,325 B) — script; must_contain greps PASS: `from canonical_constants import` ✓, `append_verdict` ✓.
- `computations/session-97/s97_w6_omdm_rhovac_pins.npz` (6,756 B) — records the two `(name, value, keying)` tuples, the per-pin resolves/keyed/tag_present/dilution_cite_ok/cross_note_ok booleans, the W1-already-canonical cross-check (`x_fold`, `Omega_BA_fold`), and the dual-SHA inputs + pinmap.
- `computations/session-97/s97_w6_omdm_rhovac_pins.png` (40,985 B) — optional (plan `optional:true`) 2-row provenance-resolution + source-keying status panel (2 promoted + 2 W1-already-canonical).
- Verdict line in `computations/session-97/s97_gate_verdicts.txt` (line 86) — matches `^S97-W6-1-OMDM-RHOVAC-PINS:.* audit_sha256=[a-f0-9]{64}` (exactly one canonical line); `audit_sha256=4ec12df8cacf48948216091f252daaac4ad41d3cc151288bf56cbcdabe4a387a`, `content_sha256=652d9c9607f981147f33c27e5ff67c697a22e7361670685694bac9e8d380088d` (both full 64-hex; unique across the S97 verdict file — sig_5 uniqueness preserved), dual-SHA companion row at line 87.
- This WP §W6-1 — Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit + the `OBSERVATIONAL-ANCHOR` / `FRAMEWORK-PREDICTION` / `DILUTION-CC-66` content tokens.

(METHODOLOGY-class: PASS predicate is artifact-existence-with-content, verified by content presence / regex match, NEVER by line/byte counts.)

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`; queries executed BEFORE the promotion):
- `get_constant('Omega_DM_h2')` → **not found** (ABSENT — eligible to promote; no clobber).
- `get_constant('rho_vac_over_rho_obs')` → **not found** (ABSENT — eligible to promote).
- `get_constant('Omega_DM_obs')` → **0.264** (EXISTS — the Planck density PARAMETER Ω_DM; the new pin must be named distinctly `Omega_DM_h2` and carry the cross-note so the physical density Ω·h² is NOT conflated with this dimensionless parameter).
- `get_constant('x_fold')` → **85.7928** (already canonical, gate `S97-W1-XTODAY`) — OUT of scope, NOT re-added.
- `get_constant('Omega_BA_fold')` → **2.241353** (already canonical, gate `S97-W1-OMEGA-PROFILE`) — OUT of scope, NOT re-added.
- `search_knowledge('DILUTION-CC-66 Volovik tracking vacuum rho_vac')` → confirms DILUTION-CC-66 PROVEN S66 (`rho_vac/rho_obs = 1.032`, Volovik Paper 25 §V / Paper 35; closes 114-OOM CC gap to 0.01 OOM; CC_OOM=115.5); **C10** (Atlas-04) `rho_vac ~ M_Pl² H²` is **ASSUMED-PARTIALLY-PROVEN** — substrate-first source chain for the FRAMEWORK-PREDICTION keying verified.
- `search_knowledge('LEGGETT-MOMENT Omega_DM h2 0.1200 dark matter density')` → confirms S70 LEGGETT-MOMENT (PROVEN, `Ω_DM h²=0.1200`, 0.6% from Planck 2018). The 0.1200 coincides with the Planck-observed datum; per `substrate-first-canonical-sourcing.md §(i)` the pin is keyed as the lab-IN **OBSERVATIONAL-ANCHOR** (the external comparison target), distinct from the framework's own LEGGETT-MOMENT prediction — keying it as a substrate prediction would invert the explanation direction.

PRE-CLOSED status: **NOT pre-closed** — the two `canonical_constants.py` pins were genuinely ABSENT at plan-freeze (the gate's deliverable is the Step-2 promotion + the per-pin source-keying decision per `math-scripts.md §"Canonical Write-Order"`).

**Verdict**: **PASS** — both promoted pins resolve via `get_constant` with non-empty PROVENANCE, each correctly source-keyed (`Ω_DM h²` OBSERVATIONAL-ANCHOR with the `Omega_DM_obs=0.264` cross-note; `ρ_vac/ρ_obs` FRAMEWORK-PREDICTION citing gate `DILUTION-CC-66` with the C10 ASSUMED-PARTIALLY-PROVEN conditionality carried), values transcribe verbatim, and the W1-already-canonical cross-check confirms `x_fold`/`Omega_BA_fold` resolve. Script verifier `resolve_and_keyed=2/2`. **Solution-space meaning**: the W8-5 "two non-direct-pin headlines" gap is CLOSED — a future one-command reproducer resolves both as RESOLVED-CANONICAL, and the canonical ledger now carries the correct substrate-first-vs-observational provenance distinction (no observational datum masquerading as a substrate prediction, and vice versa).

**Results**:

Two `update_constant` Step-2 promotions (canonical-write-order Step-2 leg; the two values transcribed VERBATIM from existing register/gate sources, NOT recomputed), followed by a PROVENANCE `note`-field enrichment Edit (mirroring the S96 W7-2 exemplar `s96_hyg_canonical_pins.py`), then the two-phase verification+closure script:

1. **`Omega_DM_h2 = 0.1200`** → keyed **OBSERVATIONAL-ANCHOR** (Planck-observed physical DM density Ω_DM h²; lab-IN datum; cross-check anchor only per `substrate-first-canonical-sourcing.md §(i)`; NOT a substrate prediction even though the framework Leggett-channel value LEGGETT-MOMENT-70 coincides at 0.6%). PROVENANCE `note` carries the cross-note **DISTINCT from `Omega_DM_obs=0.264`** (the Planck density PARAMETER Ω_DM at `canonical_constants.py:539`) — physical density Ω·h² vs dimensionless density parameter; the two are NOT to be conflated. Landed in `canonical_constants.py` SECTION E (assignment L656 + PROVENANCE dict L1746). Verifier: `prov_nonempty=True, tag_present=True, cross_note_ok=True`, value `0.12` (match).
2. **`rho_vac_over_rho_obs = 1.032`** → keyed **FRAMEWORK-PREDICTION** (substrate-first; gate `DILUTION-CC-66`/S66 Scenario B — Volovik tracking-vacuum `rho_vac ~ M_Pl² H²`, Volovik Paper 25 §V / Paper 35 — closes the 114-OOM CC gap to 0.01 OOM, CC_OOM=115.5). PROVENANCE `note` carries the substrate-IS chain (D_K eigenvalues → a₀ Seeley-DeWitt zeroth moment → ρ_vac → ρ_vac/ρ_obs) AND the **C10 (Atlas-04) `rho_vac ~ M_Pl² H²` ASSUMED-PARTIALLY-PROVEN** conditionality so the pin does not overstate its register status. `gate` field = `DILUTION-CC-66`. Landed in SECTION E (assignment L657 + PROVENANCE dict L1749). Verifier: `prov_nonempty=True, tag_present=True, dilution_cite_ok=True`, value `1.032` (match).

**Per-pin verdict predicate** (the gate's set-membership operator): for each promoted pin, `get_constant(name)` resolves AND PROVENANCE carries session + source + the correct keying tag (searched across the PROVENANCE `note`/`source`/`comment`/`gate` fields, so the discriminator is robust to which field the tool/Edit wrote it into); for `rho_vac/ρ_obs` additionally the DILUTION-CC-66 cite; for `Ω_DM h²` additionally the `Omega_DM_obs=0.264` cross-note. All four conjuncts PASS for both pins.

**Write-order declaration** (`math-scripts.md §"Canonical Write-Order"`): this gate is the **Step-2 leg ONLY** — no NEW framework-prediction VALUE is produced (both values are transcribed from existing register/gate sources), so the full (1)verdict→(2)canonical→(3)inventory write-order short-circuits: Step-1 verdict-file emission = this gate's own dual-SHA verdict line (documents the promotion event); Step-2 = the two `update_constant` calls (the actual promotion). **Step-3 (falsifier-master-inventory row) is N/A** — neither pin is a NEW falsifier prediction (Ω_DM h² is an observational anchor already tracked; ρ_vac/ρ_obs is the DILUTION-CC-66 result already inventory-anchored at `framework-cc-oom.md` Door 12 / `falsifier-watchlist`). NO `mack-cosmic-bridge` inventory write triggered.

**Dual-SHA closure** (METHODOLOGY-class per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"`): `content_sha256 = sha256(bytes(script)) = 652d9c96…088d` (the F-image of the numerical PASS-predicate eigenvalue, over the script — here the rule/registry/module DIFF carrier); `audit_sha256 = sha256(bytes(script) ‖ bytes(canonical_constants.py) ‖ pinmap_json) = 4ec12df8…387a` (over the input-pin map of source documents). The `canonical_constants.py` bytes are included in `audit_sha256` precisely because the gate's deliverable IS the post-mutation module state; the verification script ran AFTER the orchestrator's two `update_constant` mutations + the `note`-enrichment Edit, so the module was in its FINAL state when the SHA was taken (the W7-2 "mutate → verify → SHA" two-phase pattern). `[AUDIT]` trigger — non-directional, so **no schema-v2 3-tuple row**.

**C10 capstone-hygiene routing note (session-close)**: the `ρ_vac/ρ_obs` promotion touches a `canonical_constants.py` value the capstone §6.3/§7 may cite and carries the C10 ASSUMED-PARTIALLY-PROVEN conditionality. The verdict is **PASS** (not INFO): the conditionality is CARRIED in the pin's PROVENANCE comment (not deferred), so the keying is complete. The C10 register-status reconciliation (capstone-hygiene 5-question gate Q3: any capstone prose tag on ρ_vac/ρ_obs must equal its C10 register status) is a SEPARATE session-close routing item for the orchestrator's `session-97-housekeeping.md §A/§B` — NOT a keying gap in this gate, and NOT a carry-forward compute (it is a prose-tag reconciliation, not a substrate recompute).

---

### §W6-2. S97-W6-2-PETROV-ANNOTATION (gen-physicist)

**Status**: COMPLETED
**Gate ID**: `S97-W6-2-PETROV-ANNOTATION`
**Trigger**: `[AUDIT]`
**Classification**: **GEOMETRIC** (the underlying observable is the τ→∞ Petrov/CMPP type of the 12D Jensen product metric — a fiber-geometry property of the fabric; the gate is a verdict-file companion-comment consistency decision, NOT a re-derivation)
**Agent**: `gen-physicist` (orchestrator-direct candidate per `mechanical-closure-discipline.md`)
**Hypothesis**: The `S96-GEOM-TAUINF-PETROV` dual-SHA companion-comment boilerplate ("dynamic Type G PERSIST to tau->inf") is stale relative to the authoritative canonical value-field (`dyn_window=tau<=6(6/12)`, `dynamic_resolvable=I`); a session-close annotation-hygiene resolution restores comment/value consistency WITHOUT recompute (verdict permanence).
**Plan reference**: `sessions/session-plan/session-97-plan-w6.md` §W6-2.

**Verdict**: **INFO** (resolution **(b)** — value-field-governs note). INFO is the honest pre-registered token for resolution (b) per the plan's `INFO_meaning`: the four stale companion rows are LEFT byte-for-byte and explicitly flagged retained-historical, governed-by the value-field — NOT made literally consistent (that would be resolution (a) → PASS). The gate's deliverable is the DECISION + its application; both resolutions are acceptable, and the verdict token records WHICH was chosen. `[AUDIT]` trigger → no schema-v2 3-tuple row.

**Resolution chosen: (b) value-field-governs note.** A single explicit `value-field governs` NOTE was APPENDED to `computations/session-96/s96_gate_verdicts.txt`, directly under the canonical PASS line's block (after its schema-v2 3-tuple row, before the next gate `S96-OBS-OMEGAGW-GGE-VS-ZN`). The note (i) names `audit_sha256=8f49af075339ccac65f14478b944d57720033de4892e27ed0d785a739c761074` as the canonical (latest non-superseded) line whose `value=` field GOVERNS (supersession chain `f260302b → 4789decf → ec803215 → 8f49af07`); (ii) states the authoritative window `dyn_window=tau<=6(6/12)` + `dynamic_resolvable=I` (asymptotic dynamic resolves to Type-I below float64) + `static_tauinf=Type-D-all-12`; (iii) flags the "dynamic Type G PERSIST to tau->inf" prose in the four companion rows as RETAINED-HISTORICAL pre-supersession boilerplate (correct as-emitted in the early chain, before the W5-3 methodology §6 regime-of-validity correction discovered the `r_dyn` float64-detectability floor at τ≈5–6); (iv) records that **verdict permanence** is preserved — the note is APPENDED; the canonical `value=`/`audit_sha256`/`content_sha256` lines, all four companion rows, and the schema-v2 3-tuple row are UNCHANGED byte-for-byte. **Why (b) over (a)**: resolution (b) touches the verdict file in exactly ONE place (lower-risk against absolute verdict permanence than editing four historical companion rows under (a)), and honestly preserves the Option-A supersession story rather than overwriting it.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML; METHODOLOGY-class — verified by content presence, NEVER by line/byte counts):

- **annotation edit** `computations/session-96/s96_gate_verdicts.txt` — the appended `value-field governs` note. `grep -c "S97-W6-2-PETROV-ANNOTATION value-field-governs"` → **1**. Canonical PASS line UNCHANGED: `grep -cE "^S96-GEOM-TAUINF-PETROV: PASS.*audit_sha256=8f49af075339ccac65f14478b944d57720033de4892e27ed0d785a739c761074"` → **1**. ✓ (verdict permanence preserved.)
- **script** `computations/session-97/s97_w6_petrov_annotation.py` — EXISTS. `grep -c "from canonical_constants import"` → **1**; `grep -c "append_verdict"` → **2** (def + call). ✓
- **data** `computations/session-97/s97_w6_petrov_annotation.npz` — EXISTS (optional:true); records `{resolution_chosen=b, verdict_token=INFO, canonical_line_audit_sha, authoritative_window, companion_rows_touched=0, governs_note_appended=True, verdict_permanence_preserved=True, dual-SHA inputs}`. ✓
- **plot** `computations/session-97/s97_w6_petrov_annotation.png` — NOT emitted (optional:true; no numerical plot for an annotation decision — the npz + this WP carry the evidence; a missing plot is NOT a stub-flag per the gate-block). ✓
- **verdict line** `computations/session-97/s97_gate_verdicts.txt` — line 88, matches `^S97-W6-2-PETROV-ANNOTATION:.* audit_sha256=[a-f0-9]{64}`. `audit_sha256=cbcbbd112a1ec518c4517d4591d56244518f173af04338047f3ad8bcf1e72aff`, `content_sha256=61427ffb30622910290ad38f096736f7f4b0da950d96ba085fbec0cd364cc01d`. Canonical line + dual-SHA companion row (line 89) present; NO schema-v2 3-tuple ([AUDIT] trigger). Exactly 1 canonical line; full-64 audit SHA unique in the file (sig_5 clean). ✓

**MCP Pre-Compute Audit** (query-first per `.claude/rules/knowledge-index-usage.md`; executed BEFORE the resolution):

- `search_knowledge('Petrov CMPP type Jensen-product metric tau infinity classification 12D')` → **`w8b_cmpp_petrov_type_invariance`** (S84 provenance) + gate **`S84-W8B-95-CMPP-PETROV-TYPE-INVARIANCE`**: PASS, `value=D/D/D/D/D/D/D/D/G/G/G/G/G/G/G/G/8`, `convention=a2-reduction-4D`, `sha256=f2cf5c7c…` — the PERMANENT static-D / dynamic-G type-invariance baseline the S96 gate extends to τ→∞.
- Same query → theorem **A3 (Atlas-07)** "8D Petrov Classification of Jensen-Deformed SU(3) — Type D at τ=0 (Einstein), algebraically general at τ>0, stable multiplicity {3,4,1,2,4,3,…}". Confirms the static-D / dynamic-(algebraically-general) structure the canonical value-field encodes.
- `trace_entity('Petrov type Jensen-product metric')` → **No trace** (the τ→∞ extension is a session-level gate, not a named knowledge entity); the canonical state IS the S96 verdict-file line + the A3 theorem above.
- **Not PRE-CLOSED, and correctly so**: this gate does NOT re-derive the Petrov type (the S96-GEOM-TAUINF-PETROV gate already closed it: `static_tauinf=Type-D-all-12`, `dynamic_resolvable=Type-G` over τ≲6, asymptotic dynamic Type-I below float64). The MCP confirms the EXISTING classification the annotation governs; this gate is a verdict-file companion-comment consistency closure on top of it, per the plan's explicit "the GATE is the companion-comment consistency decision — NOT a re-derivation".

**Results**:

**1. The documented PROSE-vs-value-field inconsistency.** The S96-GEOM-TAUINF-PETROV block in `s96_gate_verdicts.txt` is a 4-line Option-A supersession chain: canonical line (audit `f260302b`, no `dyn_window`) → `4789decf` (`dyn_window=tau<=50(12/12)`, asymptotic dynamic D) → `ec803215` (`dyn_window=tau<=6(6/12)`, asymptotic `dynamic_resolvable=I`) → **canonical PASS `8f49af07`** (`dyn_window=tau<=6(6/12)`, `dynamic_resolvable=I`, `S84_continuation=(static=True,dynamic=True)`). All FOUR dual-SHA companion rows carry the identical pre-supersession prose "static Type D / **dynamic Type G PERSIST to tau->inf**", which conflicts with the canonical value-field's corrected window (dynamic resolvable only to τ≲6; asymptotic dynamic = Type-I below round-off). The W5 WP §W5-3 Results §6 (regime-of-validity correction) already disclosed this: the dynamic Type-G signal comes from the τ-fixed extrinsic-curvature cross-term `|K_diag|²≈704.64` while the fiber Weyl scale grows as ½e^{2τ}; the dimensionless ratio `r_dyn` sinks below float64-detectability at τ≈5–6, AND the modulus is censored from reaching τ→∞ (COSMIC-CENSORSHIP-49, barrier τ≈0.19 ≪ τ_NEC≈1.38), so "dynamic G persists to τ→∞" is physically counterfactual and numerically below round-off.

**2. The resolution applied (b).** The appended note makes the **value-field governs** relationship explicit at the verdict-file layer: the canonical value-field window (`dyn_window=tau<=6(6/12)`, `dynamic_resolvable=I`) is authoritative; the companion-row "dynamic Type G PERSIST to tau->inf" is retained-historical boilerplate. The note references the canonical line by **supersession-chain identity** (full audit_sha256=8f49af07…), NOT by the drifted S96-CF line numbers 123/128/131/134 (the verdict file has duplicate emission blocks). Pointer to the regime-artifact basis: W5 WP §W5-3 Results §6 + CF-W5-1.

**3. Verdict-permanence preservation (PROHIBITED_ACTIONS Class-3/4 guard).** The closure script ASSERTS — and verified TRUE — that the canonical PASS line (audit `8f49af07…`) is present unchanged with its content_sha (`978a2dd6…`) and value-field window, that the four stale companion-row heads (`f260302b`/`4789decf`/`ec803215`/`8f49af07`) are all still present, and that the governs-note is appended and well-formed (P1+P2=True, P3=True, P4=True ⇒ `resolution_b_applied=True`). The canonical `value=`/`audit_sha256`/`content_sha256` lines and the schema-v2 3-tuple row are UNCHANGED byte-for-byte. NO recompute, NO canonical-line edit — only one APPENDED comment line. **verdict permanence** is therefore preserved by construction.

**4. METHODOLOGY-class dual-SHA closure (separate S97 closure).** The S97 verdict line documents this annotation-hygiene decision as a closure DISTINCT from the S96 Petrov gate: `content_sha256` over the script bytes (`61427ffb…`); `audit_sha256` over `script‖s96_gate_verdicts.txt(post-resolution)‖pinmap_json` (`cbcbbd11…`) per `wave-classification.md §"Dual-SHA closure for METHODOLOGY-class"` (the edited verdict file is the F-image of the numerical PASS-predicate — the verdict-file analog of a rule-file diff; the S96 verdict-file-pin + W5 WP pin feed the pinmap). The canonical S96 Petrov line's OWN audit_sha256 (`8f49af07…`) is untouched. M4 satisfied: the gate-ID is on `methodology-wave-allowlist-ledger.md` (S97 row, `sha256_of_plan_block=efd8312e196c25d77edcee4c6ef3a8ef93b597a39c8a938061e137c8801b5d11`). Mechanical-closure honesty discipline (orchestrator-direct candidate, resolved gen-physicist-direct): the verdict line names the resolution (`resolution=(b)_value-field-governs`) AND this WP §W6-2 discloses it (Status/Verdict/which-resolution/substrate framing) — no task-complete-lie.

**5. Substrate framing (substrate-first, IS-not-IN).** GEOMETRIC. The τ→∞ Petrov/CMPP type is a **fiber-geometry property of the 12D Jensen-deformed product metric** `ds²=−dt²+a(t)²dx₃²+g_ab(τ)dyᵃdyᵇ` — NOT the algebraic type of a spacetime the fabric lives IN. The direction of explanation flows `D_K eigenvalues → Jensen fiber metric g_τ → 12D product lift → a₂-reduced emergent-4D Lorentzian metric → Petrov type`. The substrate IS Type-D static (the contracting SU(2) block carries divergent Weyl content → timelike i⁺; the expanding ℂ²/U(1) blocks carry convergent Weyl content → spacelike), with the transit-regime dynamic Type-G censored by COSMIC-CENSORSHIP-49. This gate does NOT re-derive any of that substrate physics — it brings the methodology-floor verdict-file ANNOTATION into F-consistency with the substrate-IS verdict (the layer-functor F: the comment is the methodology-floor image of the substrate-physics value-field per `epistemic-discipline.md §"Layer-Decomposition"`). The substrate physics is unchanged; only the annotation is reconciled.

---

## Wave 6 Synthesis (team-lead)

**Wave 6 — Canonical-constants promotion & hygiene (the deliberately-light final wave; both METHODOLOGY-class).** Both gates orchestrator-allowlist-licensed (W6-1 sha `6210658c…`, W6-2 sha `efd8312e…`); verdict file audit-clean (sig_5 verified across all 25 S97 canonical lines = 20 unique gates + 5 Option-A supersession-chain extras).

- **W6-1 S97-W6-1-OMDM-RHOVAC-PINS — PASS.** Two canonical pins promoted to SECTION E via the METHODOLOGY two-phase update_constant+verify pattern (S96 W7-2 precedent): `Omega_DM_h2=0.1200` keyed **OBSERVATIONAL-ANCHOR** (Planck lab-IN datum, cross-check only; cross-noted DISTINCT from the pre-existing `Omega_DM_obs=0.264` density parameter) and `rho_vac_over_rho_obs=1.032` keyed **FRAMEWORK-PREDICTION** (DILUTION-CC-66 substrate-first; C10 ASSUMED-PARTIALLY-PROVEN conditionality carried in the provenance). Scope honored: `x_fold`/`Omega_BA_fold` (already W1-promoted) verified present but NOT re-added; no σ₈ touched. The keying enforces the substrate-first direction — keying Ω_DM h² as a prediction would invert the explanation arrow (container-thinking).

- **W6-2 S97-W6-2-PETROV-ANNOTATION — INFO** (resolution (b), value-field-governs). The τ→∞ Petrov/CMPP-type annotation governs the existing classification (S84-W8B-95 PASS + Atlas-07 A3: static Type D, dynamic algebraically-general). The pre-supersession "dynamic Type G PERSIST to τ→∞" boilerplate is flagged retained-historical, GOVERNED by the canonical value-field (`dyn_window=τ≤6`, `dynamic_resolvable=I`) — touching the verdict file in exactly one place (lower-risk than editing 4 historical companion rows; preserves the Option-A supersession trail). The S96 canonical Petrov line + companions are byte-for-byte UNCHANGED (verdict permanence). Mechanical-closure honesty satisfied (verdict names resolution (b); WP discloses it).

**Capstone-hygiene 5-question gate (W6):** **Q1** (a(t)) — NO. **Q2** (§7 falsifier) — NO. **Q3** (status change) — the ρ_vac/ρ_obs pin carries the C10 ASSUMED-PARTIALLY-PROVEN conditionality, but C10 was already sharpened in-session (W2-2 Atlas-04 register update) and its §8.5 prose reconciliation is already routed to the session-close designated writer — the canonical pin is consistent with the Atlas C10 register; no new C10 action. **Q4/Q5** — NO.

**Effected In-Session (W6):**
- [x] Two METHODOLOGY-class allowlist rows appended (`S97-W6-1-OMDM-RHOVAC-PINS` sha `6210658c…`, `S97-W6-2-PETROV-ANNOTATION` sha `efd8312e…`) + paired rationales (orchestrator-only via helper; classification confirmed by the W6 plan M1–M3) — `methodology-wave-allowlist-ledger.md` + `methodology-wave-instances.md`.
- [x] Capstone-hygiene 5-question gate run (Q1–Q5; C10 conditionality consistent with the W2-2 Atlas sharpening + §8.5 designated-writer flag, no new action) — recorded `session-97-housekeeping.md §A`.
- [x] σ₈ channel-keyed canonical promotion recorded as CF-S98 (sub-keying ambiguity ⇒ carry-forward per `math-scripts.md §"Canonical Write-Order"`, NOT foldable into W6-1's pre-registered 2-pin scope) — WP CF below + `session-97-housekeeping.md §B`.
- [x] Housekeeping ledger finalized with W6 §A entries + W6-populated marker.
- [x] `/weave --update` flagged for session-close (the session's six add-only canonical promotions — `x_fold`, `Omega_BA_fold`, `Omega_GW_acoustic_peak`, `Omega_GW_acoustic_LISA_tail`, `Omega_DM_h2`, `rho_vac_over_rho_obs` — need the knowledge-index rebuild) — `session-97-housekeeping.md`.

## Carry-Forward Computations

> W6's two gates closed PASS/INFO with no future-compute residual of their own (6.1 PASS — both pins canonical; 6.2 INFO — annotation governed, closed). The C10 conditionality on ρ_vac/ρ_obs is NOT a new CF (it's consistent with the in-session W2-2 Atlas C10 sharpening + the already-routed §8.5 designated-writer prose flag). One hygiene carry-forward surfaced from W4-3 routes here (a canonical-promotion with a sub-keying decision, hence a CF rather than fix-in-session — mirrored to `session-97-housekeeping.md §B`):

### CF-S98-HK-SIGMA8-CHANNEL-KEYED-PINS — promote the two channel-keyed σ₈ values to canonical with provenance [Q2-hygiene]

> **Routing note**: Q2-class hygiene per `Investigating-Workshops.md §"Q2"`; surfaced by S97 W4-3 (f·σ8). Mirrored to `session-97-housekeeping.md §B`. NOT a workshop.
> **Why not §A (fix-in-session)**: sub-keying ambiguity — two distinct framework σ₈ channels exist (`SIGMA8-OZ-50`=0.799 S50 spectral-action/Goldstone-blind vs the S70/S96 a₂ growth-channel=0.79317), no `sigma_8_FW` canonical pin exists, and the canonical naming/keying convention for the two channels is a decision better pre-registered at S98 plan-freeze (per `math-scripts.md §"Canonical Write-Order"`: sub-keying ambiguity ⇒ carry-forward, not a single-value fix-in-session) than orchestrator-decided un-pre-registered now.

1. **What**: Promote both channel-keyed σ₈ values to `canonical_constants.py` SECTION E with channel-distinct provenance — `sigma8_OZ_50=0.799` (spectral-action / O-Z, S50; keyed to the existing SIGMA8-OZ-50 knowledge entity) and `sigma8_growth_a2=0.79317` (a₂ growth-channel, S70/S96). Pre-register the canonical naming + which (if either) is the headline σ₈, and a cross-note distinguishing the two channels (~0.7% apart, different spectral channels).
2. **Inputs**: SIGMA8-OZ-50 (S50, knowledge MCP); the S70/S96 a₂ growth-channel σ₈=0.79317; `computations/session-97/s97_fsigma8_forecast_refetch.npz` (W4-3, audit `a20043e7`); the existing `Omega_DM_obs`/`sigma8`-region SECTION-E pins for naming consistency.
3. **Gate**: `S98-HK-SIGMA8-CHANNEL-KEYED-PINS` — METHODOLOGY-class PASS = `get_constant('sigma8_OZ_50')` + `get_constant('sigma8_growth_a2')` both resolve with non-empty channel-distinct PROVENANCE + the cross-note (artifact-existence predicate; allowlist row at S98 plan-freeze).
4. **Effort**: < 0.1 wave.
5. **Depends on**: S97-W4-3 (the σ₈ disambiguation record — UPSTREAM).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:--|:--|:--|:--|:--|
| 2026-05-30 | `Omega_DM_h2` canonical pin (6.1) | absent from canonical_constants.py | canonical SECTION E, keyed OBSERVATIONAL-ANCHOR (lab-IN; DISTINCT from `Omega_DM_obs=0.264` density parameter) | W6-1 PASS |
| 2026-05-30 | `rho_vac_over_rho_obs` canonical pin (6.1) | absent from canonical_constants.py | canonical SECTION E, keyed FRAMEWORK-PREDICTION (DILUTION-CC-66; C10 ASSUMED-PARTIALLY-PROVEN conditionality carried) | W6-1 PASS |
| 2026-05-30 | Petrov τ→∞ dynamic-type annotation (6.2) | "dynamic Type G PERSIST to τ→∞" boilerplate (pre-supersession) | flagged retained-historical, GOVERNED by canonical value-field (`dyn_window=τ≤6`, `dynamic_resolvable=I`); S96 canonical lines byte-for-byte unchanged | W6-2 INFO (resolution (b)) |

## Files Produced

All paths under `computations/session-97/`. Verdicts in `s97_gate_verdicts.txt` (canonical).

| Gate | Verdict | Script | Data (.npz) | audit_sha256 (short) |
|:--|:--|:--|:--|:--|
| W6-1 S97-W6-1-OMDM-RHOVAC-PINS | PASS | `s97_w6_omdm_rhovac_pins.py` | `s97_w6_omdm_rhovac_pins.npz` (+`.png`) | `4ec12df8` |
| W6-2 S97-W6-2-PETROV-ANNOTATION | INFO | `s97_w6_petrov_annotation.py` | `s97_w6_petrov_annotation.npz` (no `.png`, optional) | `cbcbbd11` |

Canonical promotions (Step 2): `Omega_DM_h2=0.1200`, `rho_vac_over_rho_obs=1.032` (SECTION E). Registers touched (Effected-In-Session): `canonical_constants.py` (2 pins + PROVENANCE); `methodology-wave-allowlist-ledger.md` + `methodology-wave-instances.md` (2 rows); `computations/session-96/s96_gate_verdicts.txt` (W6-2 governs-note appended, S96 canonical lines untouched); `session-97-housekeeping.md` (W6 §A + §B). Helper: `computations/session-97/s97_w6_allowlist_append_helper.py`.
