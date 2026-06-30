# Session-X Plan — Wave 1: Comprehensive Aggregate Expansion of `Phononic-framework-hypothesis.md`

**Date**: 2026-05-25
**Author**: tesla-resonance (per-wave planner = executor; author-specialist for this document)
**Owner agent**: `tesla-resonance` (the document carries the Tesla-Resonance / Workhorse-Resonance voice)
**Plan source**: `sessions/session-plan/session-x-context.md` §0 (PRIMARY MODE), §1, §2, §4 (gate architecture), §5 (heavy survey), §7 W1 domain seed
**Working paper**: `sessions/session-x/session-x-w1-workingpaper.md`
**Target document**: `sessions/framework/Phononic-framework-hypothesis.md` (57,340 bytes; rev post-S53; ~40 sessions S53→S93 to integrate)

> **Scope correction (this plan overwrites a prior validation-scoped W1 plan).** The earlier file at
> this path was organized around "drift targets" — a VALIDATION-primary framing. Per
> `session-x-context.md §0`, **EXPANSION is the deliverable; validation is the embedded QA sub-layer
> (gate G3).** A plan that merely reconciles existing claims has FAILED the assignment. This plan is
> expansion-primary: the center of mass is G2 (integrate ~40 sessions of in-domain results the
> document was never written to include). The drift fixes the prior planner identified (the tau
> quartet, the sin²θ_W form) are folded in as QA *along the way*, not as the point.

---

## Wave 1 Summary

This wave **comprehensively expands `Phononic-framework-hypothesis.md` to a current (S93-era) view of the WHOLE PROJECT** within its domain — the foundational resonance hypothesis: the self-tuning cavity, the Cayley-Dickson division-algebra ladder, the inside-out inversion, the transit paradigm, and emergent Lorentz violation. The document is a post-S53 snapshot (12 sections, ending with the tight-binding reframe and BLV acoustic cosmology). The ~40 sessions S53→S93 that bear on the resonance hypothesis were never folded in.

The three gates implement the context's `SURVEY → EXPAND → VERIFY` architecture:

- **WX-W1-1 (AUDIT)** — the comprehensiveness engine: map the resonance-hypothesis DOMAIN across all ~93 sessions in the knowledge base, then enumerate the GAP between what the project knows in-domain and what the document covers, each gap row KB-cited with a "where it belongs."
- **WX-W1-2 (VERIFY)** — the deliverable: substantially expand the document to integrate the gap (new sections + deepened sections + new mechanisms/theorems/bridges/constants/paradigm shifts), in the resonance-hypothesis authorial voice; disambiguate the tau quartet and adjudicate+reconcile the sin²θ_W form as QA.
- **WX-W1-3 (VERIFY)** — QA over the expanded document: every claim current, IS-not-IN framed, provenance-traced, and `a_n^{regulator}`-tagged where applicable.

**Carry-forward source**: none (bespoke aggregate-expansion session per `session-x-context.md`; not a prior-session reviewer carry-forward).

**Planner domain-survey result (pre-blueprint, this plan)**: a substantial knowledge-base sweep (≈30 `search_knowledge` / `trace_entity` / `list_entities` / `get_constant` / `query_entity` queries + `Glob`) pre-identified the major gap areas the document is missing, seeding G1's scope and G2's section blueprint. The ten major gap areas + the tau quartet + the sin²θ_W reconciliation are enumerated in §"G2 expansion blueprint" below with KB citations. This is the BLUEPRINT, not the execution — the executor's G1 survey finds the remainder and the executor's G2 writes it.

---

## Wave 1 Decision Point Prerequisites

**None.** W1 is independent — it consumes only the target document, `computations/_shared/canonical_constants.py`, and `tools/knowledge.db` (all present at dispatch). No upstream verdict from S-prior or from another session-x wave gates any W1 item. W1's three gates are internally sequential (G1 → G2 → G3): G2 consumes G1's gap-analysis artifact; G3 consumes G2's expanded document. If G1's gap artifact is absent at G2 dispatch, G2 honestly closes per `.claude/rules/mechanical-closure-discipline.md` (PRE-REG-INC blocked by WX-W1-1); likewise G3 on G2. The expanded document feeds the W9 cross-document closeout (see "Wave 1 → Wave 9 Decision Point").

---

## §W1-1. WX-W1-1 — AGGREGATE-DOMAIN-SURVEY

```yaml
# ---- Identity (4 fields) ----
gate_id: "WX-W1-1-AGGREGATE-DOMAIN-SURVEY"
schema_version: "R3"
trigger: "[AUDIT]"
classification: "PHONONIC"
agent_type: "tesla-resonance"
hypothesis: "The phonon-exflation knowledge base contains a substantial body of S54→S93 results in the resonance-hypothesis domain (self-tuning cavity, division-algebra ladder, inside-out inversion, transit paradigm, emergent Lorentz violation) that `Phononic-framework-hypothesis.md` (a post-S53 snapshot) does not cover; this gate maps that domain and enumerates the gap with citations."

method:
  description: >
    Sweep the knowledge base broadly across the resonance-hypothesis DOMAIN (NOT the document's
    existing claims). For each domain topic, query the pertinent entity classes across all ~93
    sessions: search_knowledge(broad domain topics — tens of queries), trace_entity(each major
    in-domain mechanism / theorem / observable), list_entities(theorems|closed|gates|open),
    get_constant(each constant the domain touches; check the Superseded flag), query_entity(drill
    into specifics). Produce TWO artifacts: (a) a current whole-project STATE-OF-DOMAIN MAP, and
    (b) a GAP ANALYSIS table — everything the project knows in-domain that the document does NOT
    yet cover (new-since-S53 OR never-covered), each row carrying its KB citation and a one-line
    "where it belongs in the document." The query manifest is recorded in the WP MCP Pre-Compute
    Audit block (mandatory per workingpaper.md Rule 3). A gap row without a KB citation is
    "imagined" per the derivative-output discipline and is INADMISSIBLE.
  producing_script: "computations/session-x/sx_w1_aggregate_domain_survey.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set"
  form: >
    PASS-set membership: { domain_entity_classes_swept } ⊇ { theorems, closed, gates, open,
    constants, sessions } over the resonance-hypothesis domain  AND  |gap_rows_with_citation| ≥ 1
    per domain topic with a non-empty "where it belongs" field. The gate maps the survey-coverage +
    gap set; it is NOT a numerical comparison.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    (i) The survey sweeps the resonance-hypothesis domain across ALL pertinent entity classes
    (theorems ∧ closed ∧ gates ∧ open ∧ constants ∧ sessions), with the query manifest recorded;
    AND (ii) the GAP ANALYSIS is enumerated as a table in which EVERY row carries a KB citation
    (gate ID / theorem / closed-mechanism / canonical_constants entry / session file + line) AND a
    one-line "where it belongs in the document." FAILS if the output only re-checks the document's
    existing claims (a claim-by-claim audit) rather than mapping the domain and the gap.
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (domain entity-class sweep + gap-row citation count); no numerical threshold"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — synthesis/survey gate (no numerical comparison; PASS is set-coverage + gap-enumeration-with-citations)"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A — survey gate (no numerical evaluation; closure script computes SHAs over survey + gap artifacts only)"
  L_max: "N/A — survey gate (the document's substrate results are reported at their native L_max, e.g. L_max=10 for the 155,984 D_K eigenvalues; the survey does not recompute spectra)"
  scan_range: "N/A — survey gate (the survey range is the session axis S1→S93, swept via knowledge.db, not a numerical scan)"
  step_size: "N/A — survey gate"
  tolerance: "N/A — survey gate (PASS is set-coverage + citation-completeness, not a tolerance band)"
  scheme: "AGGREGATE-DOMAIN-SURVEY"
  convention: "domain-coverage-by-enumeration-plus-gap-citation"
  random_seed: "N/A — deterministic (KB queries + SHA over fixed inputs)"
  GPU_path: "N/A — survey gate (no linear algebra; closure script is SHA + verdict on CPU)"
  kb_tools_surveyed: "[search_knowledge, trace_entity, list_entities, get_constant, query_entity, list_constants]"
  entity_classes_surveyed: "[theorems, closed, gates, open, constants, sessions, researchers]"
  domain_scope: >
    The resonance-hypothesis domain = the foundational framework hypothesis. Topics to sweep
    (non-exhaustive; survey finds the rest): self-tuning cavity / self-consistency map; Cayley-Dickson
    division-algebra ladder (R→C→H→O→S, J_3(O), F_4⊃SU(3)×SU(3), Aut(O)=G_2); inside-out inversion
    (eigenvalues-as-frequencies, BLV acoustic metric); emergent Lorentz violation / Debye cutoff;
    transit paradigm (instanton gas, GGE relic, Ordered Veil, integrability); the 27 TT drums /
    Lichnerowicz; block-diagonal theorem; structural-monotonicity / trace theorem; tight-binding
    crystalline cavity (N_pair=1); acoustic cosmology / exflation-not-inflation; frequency hierarchy;
    the P-1..P-10 predictions; cross-pillar bridge program (§VII.*); LQG/CDT cross-framework;
    DILUTION-CC; spectral-functional maturation; observational program (A_s, n_s, α_s, Ω_DM, m_H,
    w_0, r, f_NL, N_eff); the tau quartet; sin²θ_W.
  gap_row_taxonomy: >
    Each gap row is tagged one of: NEW-SINCE-S53 (a result that postdates the document's authorship)
    OR NEVER-COVERED (a result the document omits regardless of date) OR DRIFTED (a retained claim
    whose value/status the project has since superseded — the QA-layer subset). Each row carries:
    {gap statement, KB citation, tag, where-it-belongs}.

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["state_of_domain_map", "gap_analysis"]

# (7) substitution_chain
substitution_chain:
  required: false
  content: |
    N/A — this gate makes no sign/direction/ratio claim. It enumerates a domain-coverage set and a
    gap set. (Any directional claim that SURFACES in the gap analysis — e.g. g1/g2 = e^{-2τ}
    direction, the sin²θ_W form, the sound-speed-hierarchy → e-folds map — is carried forward to
    WX-W1-2, where the substitution chain is mandatory before that claim is written into the
    expanded document.)

# (8) input_files
input_files:
  target_document:
    path: "sessions/framework/Phononic-framework-hypothesis.md"
    sha256: "<computed-at-runtime>"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w1_aggregate_domain_survey.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w1_aggregate_domain_survey.npz"
    artifact_kind: "data"
    optional: true   # survey artifacts are the state-of-domain map + gap table (markdown in WP); npz optional (may store the kb_query_manifest + SHA pins)
  plot:
    path: "computations/session-x/sx_w1_aggregate_domain_survey.png"
    artifact_kind: "plot"
    optional: true   # survey gate has no figure
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W1-1-AGGREGATE-DOMAIN-SURVEY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w1-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W1-1. WX-W1-1-AGGREGATE-DOMAIN-SURVEY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric (3 fields) ----
PASS_meaning: >
  The resonance-hypothesis domain has been swept across the pertinent entity classes and the gap
  between project knowledge and document coverage is enumerated with citations. The solution-space
  meaning: the expansion target (G2) is now BOUNDED — the set of material gaps is known and citation-
  backed, so G2 can integrate-or-scope every one of them. This gate licenses a COMPREHENSIVE (not
  cosmetic) expansion.
FAIL_meaning: >
  The survey did not map the domain (e.g. it only re-checked the document's existing sentences) OR
  the gap analysis has rows without KB citations. Solution-space meaning: the expansion target is
  unbounded/imagined — G2 cannot proceed comprehensively because the gap set is not established. The
  fix is to re-run the domain sweep with the entity-class coverage + per-row citation discipline.
INFO_meaning: >
  Partial coverage — the domain was swept but one or more pertinent entity classes were not reached
  (e.g. open-channels surveyed but closed-mechanisms not), OR a minority of gap rows lack citations.
  Solution-space meaning: G2 may proceed on the cited subset while the uncited rows route to a
  same-wave re-query before they are written into the document.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w1_aggregate_domain_survey.py"
    - "computations/session-x/sx_w1_aggregate_domain_survey.npz"
    - "sessions/session-x/session-x-w1-workingpaper.md (§W1-1 section + state-of-domain map + gap table)"
  estimated_time: "heavy — this is the comprehensiveness engine; expect tens of KB queries, not a handful (per session-x-context.md §5)"

substrate_framing: |
  PHONONIC. The domain is the substrate's own resonance structure: the eigenvalue spectrum of D_K on
  Jensen-deformed SU(3) IS the set of vibrational modes; particles, couplings, and cosmology are
  spectral moments of that one operator. The survey maps how the project's understanding of THAT
  structure has matured S54→S93 — the cross-pillar bridges (substrate-IS observables bridged to
  laboratory-IN observables), the transit paradigm (the fold IS the physics), the spectral-functional
  maturation, the LQG/CDT cross-framework placement. The direction of explanation is preserved: from
  D_K eigenvalues → spectral moments → emergent physics. No container-thinking — the survey catalogues
  what the substrate IS at S93, not what lives "inside" a pre-existing spacetime.
```

---

## §W1-2. WX-W1-2 — COMPREHENSIVE-EXPANSION

```yaml
# ---- Identity (4 fields) ----
gate_id: "WX-W1-2-COMPREHENSIVE-EXPANSION"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "tesla-resonance"
hypothesis: "`Phononic-framework-hypothesis.md` can be substantially expanded so that it reads as a current (S93-era) comprehensive synthesis of the resonance hypothesis — integrating every material gap from WX-W1-1 (new sections + deepened sections + new mechanisms/theorems/bridges/constants/paradigm shifts) in the document's authorial voice — with the tau quartet disambiguated and the sin²θ_W form adjudicated and reconciled to canonical as the embedded QA layer."

method:
  description: >
    THE DELIVERABLE. Substantially expand / largely-rewrite `Phononic-framework-hypothesis.md` to
    integrate the WX-W1-1 gap analysis. Add new sections for post-S53 results, deepen existing
    sections to current understanding, fold in new mechanisms / theorems / cross-pillar bridges /
    canonical constants / paradigm shifts, and restructure where the current view demands it — IN the
    resonance-hypothesis authorial voice (cavity / drums / standing-wave register; preserve the
    existing §-numbered structure as the spine, extend it). Drift-fixing is the QA layer woven
    through: every retained claim is brought current, the tau quartet (0.190 / 0.2015 / 0.15 /
    0.2117 / 0.2994) is disambiguated WITHOUT overwriting (they are DISTINCT quantities), and the
    §1 sin²θ_W form is ADJUDICATED (see substitution chain Claim A — the un-normalized
    e^{-4τ}/(1+e^{-4τ}) form vs the factor-3 trace-normalized 3/(3+e^{4τ}) form is a genuine open
    question, NOT a settled overwrite; adjudicate from the evidence chain, do not assume). The
    producing/closure script computes the dual SHA over document_pre + survey/gap artifacts (audit)
    and document_post (content) and appends the verdict line; the EXPANSION WRITING itself is the
    executor's intellectual work, recorded in the expanded document + the WP §W1-2 section. A
    cosmetic / minimal edit FAILS this gate.
  producing_script: "computations/session-x/sx_w1_comprehensive_expansion.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set"
  form: >
    Gap-integration partition: { integrated_gap_rows } ∪ { scoped_out_gap_rows } = { all_gap_rows
    from WX-W1-1 }, with each scoped_out row carrying a one-line reason. PASS requires the partition
    to COVER every material gap row (integrated OR explicitly scoped-out — no silently-dropped rows)
    AND a substantive (non-cosmetic) document delta.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    EVERY material gap row from WX-W1-1 is either INTEGRATED into the expanded document OR explicitly
    SCOPED-OUT with a one-line reason; the document now reads as a current (S93) comprehensive
    synthesis (new sections present for the major post-S53 gap areas — cross-pillar bridges, transit/
    causality, spectral-functional maturation, LQG/CDT, DILUTION-CC, GGE-permanence arc, the division-
    algebra theorem + modular-flow tick formalization, the observational program — AND existing
    sections deepened to current values); the tau quartet is disambiguated (all five quantities
    present and distinguished, none overwritten); the sin²θ_W form is adjudicated and reconciled. The
    delta is SUBSTANTIVE: the expansion adds material content, not formatting. A cosmetic/minimal
    edit (only reconciling a few numbers, or touching < the major gap areas) FAILS.
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (gap-row integration partition: integrated ∪ scoped-out = all WX-W1-1 gaps); substantive-delta check is content-pattern, not numerical"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — synthesis/expansion gate (PASS is gap-integration coverage + substantive-delta, not a numerical comparison)"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A — expansion gate (no numerical evaluation; the closure script computes SHAs + verdict; the expansion is prose synthesis)"
  L_max: "N/A — expansion gate (substrate results are cited at their native L_max — e.g. 155,984 D_K eigenvalues at L_max=10; the expansion does not recompute spectra, it integrates published verdicts)"
  scan_range: "N/A — expansion gate"
  step_size: "N/A — expansion gate"
  tolerance: "N/A — expansion gate (PASS is gap-coverage + substantive-delta; any numerical value written in is cited verbatim from canonical_constants / a gate verdict, not recomputed under a tolerance)"
  scheme: "COMPREHENSIVE-EXPANSION"
  convention: "gap-integration-coverage-plus-substantive-delta; substrate-IS framing per phononic-framing.md"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — expansion gate (closure script is SHA + verdict on CPU; no linear algebra)"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ <computed-at-runtime>"
  document_pre_sha: "<computed-at-runtime>"
  expansion_blueprint_source: "WX-W1-1 gap analysis (this wave) + the §'G2 expansion blueprint' section of this plan (the ten gap areas + tau quartet + sin²θ_W adjudication, KB-cited)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    MANDATORY for every directional/ratio claim added or retained in the expanded document (per
    math-scripts.md §"Double-Check Logic Before Compute"). The executor writes the chain in the WP
    §W1-2 for each such claim BEFORE writing it into the document. The load-bearing instances:

    --- Claim A: sin²θ_W form ADJUDICATION (un-normalized vs trace-normalized) ---
    Definition 1: g_1/g_2 = e^{-2τ_0}   [Jensen metric components, eq 3.71; atlas-07 PROVEN; S17a]
    Definition 2 (un-normalized Weinberg): sin²θ_W = g_1² / (g_1² + g_2²)
    Substitute:   sin²θ_W = (g_1/g_2)² / ((g_1/g_2)² + 1) = e^{-4τ_0}/(e^{-4τ_0}+1) ≡ 1/(1+e^{+4τ_0})
                  [the doc §10 form ≡ doc §1 form — algebraically identical]
    Definition 2' (SU(2)/U(1) trace-normalized, candidate canonical):
                  sin²θ_W = (3/5)g_1² / ((3/5)g_1² + g_2²) → factor-3 family 3/(3+e^{4τ}) form
                  [flagged by the prior W1 planner: session-76-baptista-kk-workshop K1.9;
                   session-55-framework-update Eq.17]
    Direction/adjudication: at τ_0=0.2994 the un-normalized form gives ≈0.2319 (matches the measured
                  Weinberg angle); the factor-3 form gives a different value. The two forms are NOT
                  algebraically identical — they differ by the SU(2)/U(1) hypercharge trace
                  normalization. This is a GENUINE OPEN ADJUDICATION, not a settled overwrite. The
                  executor MUST adjudicate which form is the current canonical from the evidence chain
                  (trace_entity("sin2_theta_W"); get_constant("sin2_thetaW_fold"); atlas-07; the S55/
                  S72/S76 sources), write the substitution chain for BOTH, and annotate the
                  supersession explicitly in the document. The retained part — g_1/g_2 = e^{-2τ}
                  (atlas-07 PROVEN, S17a) — is CURRENT regardless.
    Conclusion:   adopt the adjudicated canonical form; state τ_0=0.2994 as the experimental
                  constraint (not a fold prediction); if the factor-3 form is canonical, reconcile
                  BOTH §1 and §10 to it and document the normalization.

    --- Claim B: g_1/g_2 = e^{-2τ} direction (retained) ---
    Definition:   g_τ = 3·diag(e^{+2τ}×3, e^{-2τ}×4, e^{+τ}×1); the U(1)_Y / SU(2)_L normalizations
                  inherit the e^{+2τ}/e^{-2τ} scaling of their fiber directions [atlas-07; S17a].
    Simplify:     g_1/g_2 = e^{-2τ}
    Direction:    τ > 0 ⇒ g_1/g_2 < 1; monotone decreasing in τ.
    Conclusion:   the retained §1/§10 claim holds; cite as PROVEN structural identity (S17a).

    --- Claim C: sound-speed hierarchy → acoustic e-folds (retained, deepened; keep the
        sound-speed PIECE distinct from the TOTAL — the prior planner flagged 2.72 vs 2.92) ---
    Definition:   N_e^acoustic = N_e^geom + (1/2)ln(ρ_f/ρ_i) − (1/2)ln(c_sf/c_si)  [BLV acoustic
                  metric, S53 W0-1, exact to 4.4e-15; Permanent Resonance Results].
    Substitute:   density term cancels (P_exc=1.000); c_fabric/c_Gold = 229.5 (c_fabric=209.97 M_KK,
                  c_Gold=0.915 M_KK) ⇒ sound-speed PIECE = (1/2)ln(229.48) = 2.7179.
    Direction:    larger sound-speed hierarchy ⇒ more acoustic e-folds. The TOTAL = geometric(0.1734)
                  + sound-speed(2.7179) + GPE(0.069) ≈ 2.92.
    Conclusion:   the 229× hierarchy IS the dominant (93%) acoustic-expansion contribution; in the
                  document keep "2.7179 = sound-speed piece" DISTINCT from "≈2.92 = total" (do NOT
                  conflate); cross-check the c_fabric / c_Gold pins at expansion time.

    (Any additional directional claim surfaced by the gap analysis — structural-monotonicity
    dS/dτ > 0, the Chebyshev tilt theorem sign, the four-speed hierarchy ordering c_mod > c_BLV >
    c_BA > c_L — gets its own substitution chain in the WP before it is written into the document.)

# (8) input_files
input_files:
  target_document:
    path: "sessions/framework/Phononic-framework-hypothesis.md"
    sha256: "<computed-at-runtime>"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  gap_analysis_artifact:
    path: "sessions/session-x/session-x-w1-workingpaper.md (WX-W1-1 gap table) + computations/session-x/sx_w1_aggregate_domain_survey.npz"
    sha256: "<computed-at-runtime>"
  connes_addendum:
    path: "sessions/framework/Collabs/tesla-framework-hypothesis-connes-addendum.md"
    sha256: "<computed-at-runtime>"
  lqg_comparison:
    path: "sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w1_comprehensive_expansion.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w1_comprehensive_expansion.npz"
    artifact_kind: "data"
    optional: true   # the deliverable is the expanded .md; npz optional (may store document_pre/post SHA pins + gap-integration ledger)
  plot:
    path: "computations/session-x/sx_w1_comprehensive_expansion.png"
    artifact_kind: "plot"
    optional: true   # expansion gate has no figure
  expanded_document:
    path: "sessions/framework/Phononic-framework-hypothesis.md"
    artifact_kind: "document"
    optional: false   # THE DELIVERABLE — substantially expanded in place
    must_contain:
      - "tau_fold"           # tau quartet disambiguation present
      - "0.2015"             # static-V_KK maximum retained + distinguished
      - "cross-pillar"       # cross-pillar bridge program integrated
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W1-2-COMPREHENSIVE-EXPANSION:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w1-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W1-2. WX-W1-2-COMPREHENSIVE-EXPANSION"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric (3 fields) ----
PASS_meaning: >
  The document is now a comprehensive S93-era synthesis of the resonance hypothesis: every material
  gap row is integrated or explicitly scoped-out, the major post-S53 areas have new/deepened sections,
  the tau quartet is disambiguated, and the sin²θ_W form is adjudicated and reconciled. Solution-space
  meaning: the foundational-hypothesis document is current and coherent with the rest of the framework
  — it can be cited as the authoritative resonance-hypothesis statement at S93 and it feeds the W9
  cross-document closeout cleanly.
FAIL_meaning: >
  The expansion is cosmetic/minimal (only a few numbers reconciled, or fewer than the major gap areas
  touched) OR one or more material gap rows were silently dropped (neither integrated nor scoped-out).
  Solution-space meaning: the document remains stale — it does NOT yet read as a current synthesis, and
  W9 would inherit an incomplete document. The fix is to integrate the missing gap rows.
INFO_meaning: >
  Substantive expansion landed, but a minority of gap rows are scoped-out for a reason that warrants
  next-session attention (e.g. a result whose integration depends on an open computation), OR the
  sin²θ_W adjudication is left open with both forms documented pending a dedicated normalization gate.
  Solution-space meaning: the document is materially current; the scoped-out rows / open adjudication
  are documented carry-forwards rather than silent omissions.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w1_comprehensive_expansion.py"
    - "computations/session-x/sx_w1_comprehensive_expansion.npz"
    - "sessions/framework/Phononic-framework-hypothesis.md (substantially expanded IN PLACE)"
    - "sessions/session-x/session-x-w1-workingpaper.md (§W1-2 section + gap-integration ledger + substitution chains)"
  estimated_time: "heavy — a full wave of effort (user directive: 'treat each document as a full wave of effort'); a ~40-session domain synthesis cannot be done in a quick pass"

substrate_framing: |
  PHONONIC. The expansion writes the substrate's S93-era resonance structure into the foundational
  document, preserving the IS-not-IN direction throughout (phononic-framing.md). New content flows
  from D_K eigenvalues → spectral moments → emergent physics: the cross-pillar bridges are written as
  substrate-IS observables bridged (HKR / K-theory) to laboratory-IN observables, NOT as the substrate
  living inside a lab; the transit paradigm is written as the fold (a property of the spectral action)
  BEING the physics, not as an event inside a pre-existing spacetime; the LQG/CDT comparison is written
  as two substrates (spin networks vs the spectral triple) placed side by side, with the framework's
  geometry emergent from the a_2 moment — never explaining the substrate via GR. The division-algebra
  ladder is deepened with the S88 Wedderburn-Artin theorem + the connes-addendum modular-flow tick
  formalization, both substrate-internal (the algebra that defines the cavity determines its modes).
  LCDM vocabulary stays excluded (exflation not inflation; a_0 not "vacuum energy"; Leggett inter-band
  coherence not "dark-matter particle"). The cavity still rings — now at S93 resolution.
```

---

## §W1-3. WX-W1-3 — RECONCILE-AND-VERIFY

```yaml
# ---- Identity (4 fields) ----
gate_id: "WX-W1-3-RECONCILE-AND-VERIFY"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "tesla-resonance"
hypothesis: "After the WX-W1-2 expansion, the expanded `Phononic-framework-hypothesis.md` contains ZERO stale, unframed, or untraced claims: every claim (retained or newly added) is current, IS-not-IN framing-compliant, provenance-traced to a canonical_constants entry / permanent theorem / closed mechanism / gate verdict, and `a_n^{regulator}`-tagged wherever a Seeley-DeWitt coefficient is cited."

method:
  description: >
    QA sweep over the EXPANDED document (output of WX-W1-2). Build a claim ledger: for each claim,
    verify (i) CURRENT — the value/status matches the canonical_constants snapshot + the knowledge
    base (no superseded number, no pre-DILUTION-CC framing, no flatly-permanent GGE without the
    S39-retraction→S61-S66-re-establishment arc); (ii) FRAMED — the explanation direction is
    substrate-IS not container-IN per phononic-framing.md (no "fields on K", no "space expands", no
    "particles created in curved spacetime", no explaining substrate results via GR); (iii) TRACED —
    each numerical claim cites a canonical_constants entry / permanent-results theorem / closed
    mechanism / gate verdict; (iv) REGULATOR-TAGGED — every Seeley-DeWitt a_n citation carries an
    a_n^{regulator} tag per regulator-pin-discipline.md (ζ / Pauli-Villars / Mellin / lattice /
    cutoff). The PASS-set is the set { stale ∪ unframed ∪ untraced ∪ bare-a_n } over the expanded
    document; PASS = that set is EMPTY.
  producing_script: "computations/session-x/sx_w1_reconcile_and_verify.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator
operator:
  type: "set"
  form: >
    PASS iff |{ stale_claims } ∪ { unframed_claims } ∪ { untraced_claims } ∪ { bare_a_n_citations }|
    = 0 over the expanded document. The gate maps the residual-defect set; PASS = empty set.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "ZERO stale, unframed, untraced, or bare-a_n claims in the expanded document."
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (claim ledger: each row checked CURRENT ∧ FRAMED ∧ TRACED ∧ REGULATOR-TAGGED; PASS = empty defect set); no numerical threshold"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — QA/verification gate (PASS is an empty defect set, not a numerical comparison)"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A — QA gate (no numerical evaluation; the closure script audits the document text + cross-checks values against the canonical snapshot)"
  L_max: "N/A — QA gate (cited substrate values are verified at their native L_max as published; no recompute)"
  scan_range: "N/A — QA gate (the 'scan' is the claim ledger over the expanded document)"
  step_size: "N/A — QA gate"
  tolerance: >
    value-match tolerance for the CURRENT check: a numerical claim in the document matches its
    canonical_constants source within the source's published precision (per epistemic-discipline.md
    §"Publication-Precision Pre-Registration"; default rel_tol ≥ 1e-9 for presentation-precision
    values, looser where the canonical is published at fewer sig figs). Exact theorems / machine-ε
    results are matched verbatim.
  scheme: "RECONCILE-AND-VERIFY"
  convention: "four-axis claim audit: CURRENT ∧ FRAMED ∧ TRACED ∧ REGULATOR-TAGGED"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — QA gate (closure script is text audit + value cross-check + SHA on CPU)"
  framing_rule: ".claude/rules/phononic-framing.md (IS-not-IN; LCDM-vocabulary exclusion table)"
  provenance_rule: ".claude/rules/substrate-first-canonical-sourcing.md (no stale external-paper pin as canonical)"
  regulator_rule: ".claude/rules/regulator-pin-discipline.md (a_n^{regulator} tagging)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_post", "canonical_constants_snapshot", "claim_ledger", "kb_query_manifest"]
  content_sha256_inputs: ["claim_ledger"]

# (7) substitution_chain
substitution_chain:
  required: true
  content: |
    MANDATORY where the QA sweep itself re-verifies a directional/ratio claim retained in the
    document (per math-scripts.md §"Double-Check Logic Before Compute"). The QA gate re-checks each
    directional claim's chain that WX-W1-2 recorded (the sin²θ_W form adjudication, g_1/g_2 = e^{-2τ}
    direction, the sound-speed-hierarchy → e-folds map with the 2.7179-piece-vs-2.92-total split,
    structural-monotonicity dS/dτ > 0 sign, the four-speed hierarchy ordering c_mod > c_BLV > c_BA >
    c_L) and confirms the canonical-form direction matches what the document states. Any chain that
    does not reproduce the document's stated direction is a defect row (stale or mis-stated) and fails
    the gate until corrected.

# (8) input_files
input_files:
  expanded_document:
    path: "sessions/framework/Phononic-framework-hypothesis.md"
    sha256: "<computed-at-runtime>"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w1_reconcile_and_verify.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w1_reconcile_and_verify.npz"
    artifact_kind: "data"
    optional: true   # the QA artifact is the claim ledger (markdown in WP); npz optional (may store the defect set + value cross-check table)
  plot:
    path: "computations/session-x/sx_w1_reconcile_and_verify.png"
    artifact_kind: "plot"
    optional: true   # QA gate has no figure
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W1-3-RECONCILE-AND-VERIFY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w1-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W1-3. WX-W1-3-RECONCILE-AND-VERIFY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric (3 fields) ----
PASS_meaning: >
  The expanded document has zero stale/unframed/untraced/bare-a_n claims — every claim is current,
  substrate-IS framed, provenance-traced, and regulator-tagged. Solution-space meaning: the document
  is QA-clean and ready for the W9 cross-document consistency closeout; downstream citations of it
  inherit a fully-traced, current foundational-hypothesis statement.
FAIL_meaning: >
  The defect set is non-empty — at least one claim is stale (superseded value/framing), unframed
  (container-thinking), untraced (no canonical/theorem/gate citation), or carries a bare a_n. Solution-
  space meaning: the expansion has residual QA gaps; the named defect rows route to in-wave correction
  before W1 closes (per fix-in-session discipline).
INFO_meaning: >
  The document is substantially clean but a small number of claims carry a documented caveat (e.g. a
  value pinned to M_Pl_physical pending the M_Pl_spectral resolution, flagged not silently asserted; a
  cross-pillar bridge cited at STAGE-1-CANDIDATE with the qualifier present; the sin²θ_W normalization
  left as a documented open adjudication). Solution-space meaning: the residual items are disclosed
  caveats, not hidden defects.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w1_reconcile_and_verify.py"
    - "computations/session-x/sx_w1_reconcile_and_verify.npz"
    - "sessions/session-x/session-x-w1-workingpaper.md (§W1-3 section + claim ledger + value cross-check table)"
  estimated_time: "moderate — claim-ledger QA over the expanded document; lighter than G2 but not trivial (every claim cross-checked on four axes)"

substrate_framing: |
  PHONONIC. The QA gate enforces the substrate-IS discipline at the claim level: it is the guard that
  keeps the expanded document flowing FROM D_K eigenvalues → spectral moments → emergent physics, and
  catches any sentence that inverted to container-thinking during the expansion. It verifies that every
  number traces to the substrate's own ledger (canonical_constants / a permanent theorem / a closed
  mechanism / a gate verdict) rather than to an external-paper placeholder, and that every Seeley-DeWitt
  moment carries its regulator tag (the a_n value depends on the regulator — bare a_n silently consumes
  the calling context's regulator, a class-conflation the substrate forbids). PASS means the foundational
  document states the substrate as it IS at S93, with no drift and no container leakage.
```

---

## G2 expansion blueprint (the ten gap areas + tau quartet + sin²θ_W — KB-cited)

This is the BLUEPRINT the planner's domain survey produced to scope G1 and seed G2. The executor's WX-W1-1 survey finds the remainder; the executor's WX-W1-2 writes the integration. Each area is a major gap the document (post-S53) lacks; each row carries its KB anchor and a "where it belongs."

| # | Gap area (S54→S93) | KB anchor | Where it belongs in the document |
|:-:|:-------------------|:----------|:---------------------------------|
| 1 | **Modular-flow tick formalization** — the doc's §5 self-consistency map T IS Connes-Rovelli modular flow; the "tick equation" (τ_{n+1} = σ_1^{ω_τ}(τ_n)) is already written down | `sessions/framework/Collabs/tesla-framework-hypothesis-connes-addendum.md` (companion to THIS doc) | Deepen §5 (Self-Consistency Loop) + §2 (Division Algebra Ladder) — the tick is the modular automorphism iteration |
| 2 | **Cross-pillar bridge program (§VII.*)** — §VII.AH FIRST cross-axis joint theorem to STAGE-3-PERMANENT (S90 W2 CF-20); §VII.U.2 Corner-II Var_a; §VII.AW.OP-PROJ THIRD (S93 W5); 5-anatomy + 3-level ladder; algebra-axis orthogonality | `S90-VII-AH-STAGE-3-PERMANENT-PROMOTION` (PASS); `atlas-11-cross-pillar-bridge-corpus.md`; `.claude/rules/cross-pillar-bridge-anatomy.md`; session-93-w5-workingpaper | NEW major section (substrate-IS ↔ laboratory-IN bridges; the resonance structure made falsifiable) |
| 3 | **LQG/CDT cross-framework placement** — six shared commitments, decisive cosmogenesis divergence (LQC bounce vs τ_fold transit), spectral-dimension d_s flow vs CDT, five pre-registered workshops | `sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md` (S92); `sessions/archive/session-92/workshops/s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md` | Deepen P-3 (Spectral Dimension Flow) + NEW cross-framework section |
| 4 | **DILUTION-CC (S66)** — closes the 114-OOM CC gap to 0.01 OOM via Volovik tracking vacuum (ρ_vac/ρ_obs=1.032; CC_OOM=115.5); W11 wall | `S66-W1-A-DILUTION-CC`; `get_constant("CC_OOM")=115.5`; `atlas-10` #19; `constraint-mega-matrix` W11 | Deepen §7 / §9 (the CC framing is pre-resolution) + the observational program |
| 5 | **GGE-permanence arc** — S38 established → RETRACTED S39 (V_phys 13% non-separable) → RE-ESTABLISHED via integrability S61-S66 (R-G + BDI; t_therm~10^580); five-layer laminar protection (S72, Γ_eff~10^-72) | `atlas-07` E2/[NEW S39]; `THERM-61`; Permanent Resonance Results (S66 integrability closure, S72 laminar) | Correct §5A/§5B/§10 (the doc presents flatly permanent — write the retraction→re-establishment arc) |
| 6 | **Spectral-functional maturation (S66-75)** — JOINT-FALSIFICATION-67 (1/5 survives, f=√x sole CC survivor); f*(x)=0.912√x+0.088exp (FIT-72); non-perturbative (heat-kernel expansion does NOT exist for f*); Pomeranchuk reclassification S75 | `JOINT-FALSIFICATION-67` (PASS); `SPECTRAL-FUNCTIONAL-FIT-72`; Permanent Resonance Results (S72, S75) | NEW subsection under §10/§11 (the spectral action's fate after the trace theorem) |
| 7 | **Transit / causality (S70-S85)** — acoustic white hole CAUSAL DISCONNECT formalized (S85 W6); WKB structurally inapplicable to van Hove transit (S70 PERMANENT, sudden approx); Mach 13.75/54.73 | `S85-ACOUSTIC-WHITE-HOLE-CAUSAL-DISCONNECT-FORMAL`; Permanent Resonance Results (S70 Chirp-Penumbra) | Deepen §5B / §7 (the transit paradigm at S85 rigor) |
| 8 | **Observational program (S63-S75)** — A_s=1.58e-9 (75% Planck, decoherence sole regulator); n_s=0.9595/0.9649; Leggett-only DM Ω_DM h²=0.120 (0.6% Planck); m_H→127.5 GeV; α_s=n_s²−1 exact (6σ Planck, 73× short on coupling); w_0 band; r=0.033; f_NL=−0.313; N_eff=3.044 | Permanent Resonance Results §"Active observational matches"; `LEGGETT-MOMENT-70`; `falsifier-rigor-registry.md`; `framework-dm-properties.md` | Substantially expand §9 (Predictions) — the P-1..P-10 each get their S93 status; the prediction set is now a falsifier program |
| 9 | **Division-algebra ladder THEOREM (S88)** — `A0∧M2` iff each Wedderburn block is division-algebra (Frobenius rescue, n=1) OR matrix (n≥2); J_3(O)/F_4⊃SU(3)×SU(3)/Aut(O)=G_2 rigor | `S88-A0-M2-BACKWARD-RESCUE-CHARACTERIZATION-FOR-DIVISION-ALGEBRA-CLASS` (PASS); `sessions/session-plan/archive/session-88-plan-w4a.md`; connes-addendum | Deepen §2 (the ladder is no longer "speculation" — it has a Wedderburn-Artin theorem) |
| 10 | **tau_fold uniqueness PERMANENT (S85 W10-3)** — §VII.M.W10-3 van-Hove-cusp non-stationarity; tau_fold=0.190 canonical (CONST-FREEZE-42, NOT superseded) | `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` (PASS); `atlas-07` §VII.M.W10-3; `get_constant("tau_fold")=0.19` | Deepen P-1 (the fold is now a uniqueness theorem, not just a computed value) |

**tau quartet (DISTINCT — disambiguate, do NOT overwrite; the doc already begins this in P-1, finish it everywhere):**

- `tau_fold = 0.190` — canonical van Hove fold (CONST-FREEZE-42; §VII.M.W10-3 PERMANENT uniqueness theorem)
- `0.2015` — static-potential V_KK + E_cond LOCAL MAXIMUM (speed bump, S53 W3-7); a *consequence* of the fold, not the fold
- `0.15` — phi_paasch single-particle mass ratio m_{(3,0)}/m_{(0,0)} (S12)
- `0.2117` — Leggett-phi crossing ω_L2/ω_L1 = phi_paasch (S50)
- `0.2994` — Weinberg constraint from sin²θ_W = experiment (S17a; constraint, not a fold prediction)

**sin²θ_W form (QA — ADJUDICATE, do NOT blind-overwrite):** the doc §1 form `1/(1+e^{4τ_0})` ≡ §10 form `e^{-4τ}/(1+e^{-4τ})` (algebraically identical). The prior W1 planner flagged a candidate trace-normalized canonical `3/(3+e^{4τ})` (SU(2)/U(1) hypercharge normalization; session-76-baptista-kk-workshop K1.9; session-55-framework-update Eq.17) which is NOT algebraically identical to the un-normalized form. This is a genuine open adjudication (substitution chain Claim A in WX-W1-2): the executor adjudicates which form is current canonical from the evidence chain (`trace_entity`; `get_constant("sin2_thetaW_fold")` exists, S42; `sin2_thetaW_MSbar`, S72 WEINBERG-72; atlas-07 carries the un-normalized form with τ_0=0.2994 matching experiment), reconciles BOTH §1 and §10 to the adjudicated form, and documents the normalization. The retained `g_1/g_2 = e^{-2τ}` (atlas-07 PROVEN, S17a) is CURRENT regardless.

---

## Wave 1 → Wave 9 Decision Point

W1 feeds the W9 cross-document consistency + coverage closeout (the only dependent wave). The expanded `Phononic-framework-hypothesis.md` (output of WX-W1-2, QA-cleared by WX-W1-3) is one of the eight expanded documents W9 verifies for mutual consistency + comprehensiveness.

- **WX-W1-2 PASS + WX-W1-3 PASS** → the document enters W9's SHARED-CONSTANT-MATRIX with all values current and traced; W9 cross-checks the tau quartet, the sound-speed pins (c_fabric / c_Gold), A_s / n_s / α_s, the sin²θ_W form, and the cross-pillar bridge citations against the other seven documents.
- **WX-W1-2 PASS + WX-W1-3 INFO** → the document enters W9 with documented caveats (e.g. M_Pl_spectral-vs-physical on A_s; the sin²θ_W normalization adjudication); W9 records the caveat in the consistency matrix rather than flagging a contradiction.
- **WX-W1-2 FAIL or WX-W1-3 FAIL** → the document is NOT W9-ready; the failing gate's defect rows route to in-wave correction (fix-in-session per `feedback_fix-in-session-never-defer.md`) before W1 closes, OR — if a defect depends on a genuine future computation (e.g. a dedicated sin²θ_W normalization gate) — it is logged as a 4-field carry-forward into the next session's plan, NOT silently passed to W9.

W1 imposes no constraint on W2–W8 (those expand other documents independently). The only shared surface is the canonical-constants snapshot, which all waves read read-only.

---

## Wave 1 Machinery-Enumeration Pin

Aggregate of the three gates' `machinery_pin_map` entries (consumed by `_yaml_gate_validator.py` for sig_4 of the v3 closure ladder). All three are synthesis/QA gates: no numerical-threshold machinery (N_eval / L_max / scan_range / step_size / tolerance / random_seed / GPU_path are all `N/A` with the reason pinned per gate), so the PRDR cardinality is satisfied by the explicit-N/A-with-reason pattern (a survey/expansion gate has no free numerical parameter to leave unpinned).

| Gate | scheme | convention | tolerance | GPU_path | Non-N/A pins |
|:-----|:-------|:-----------|:----------|:---------|:-------------|
| WX-W1-1 | AGGREGATE-DOMAIN-SURVEY | domain-coverage-by-enumeration-plus-gap-citation | N/A (set-coverage + citation-completeness) | N/A | kb_tools_surveyed; entity_classes_surveyed; domain_scope; gap_row_taxonomy |
| WX-W1-2 | COMPREHENSIVE-EXPANSION | gap-integration-coverage-plus-substantive-delta; substrate-IS framing | N/A (gap-coverage + substantive-delta; written values cited verbatim from canonical) | N/A | canonical_constants_snapshot; document_pre_sha; expansion_blueprint_source |
| WX-W1-3 | RECONCILE-AND-VERIFY | four-axis claim audit: CURRENT ∧ FRAMED ∧ TRACED ∧ REGULATOR-TAGGED | value-match rel_tol ≥ 1e-9 (presentation precision; looser where canonical published at fewer sig figs); exact theorems matched verbatim | N/A | framing_rule; provenance_rule; regulator_rule |

All three carry `schema_version: "R3"`. The closure scripts (`sx_w1_*.py`) are mechanical (compute the dual SHA over the input-pin map + emit the verdict via the canonical `append_verdict` helper); the intellectual work (survey, gap analysis, expansion writing, claim ledger) is the executor's, recorded in the WP + the expanded document.

---

## Wave 1 Input-SHA Ledger

Every input file W1's gates consume, with expected SHA-256 (static files get precomputed hashes at plan-freeze; dynamic inputs marked `<computed-at-runtime>` and verified at execution per `gate-verdicts.md`). Cross-checked at plan-freeze by `computations/_shared/_plan_upstream_pin_validator.py`.

| File | Consumed by | SHA-256 |
|:-----|:-----------|:--------|
| `sessions/framework/Phononic-framework-hypothesis.md` (the target document, pre-expansion) | WX-W1-1, WX-W1-2 (pre); WX-W1-3 (post) | `<computed-at-runtime>` (mutated in place by WX-W1-2 — document_pre for W1-1/W1-2 audit-SHA, document_post for W1-3) |
| `computations/_shared/canonical_constants.py` | WX-W1-1, WX-W1-2, WX-W1-3 | `<computed-at-runtime>` |
| `tools/knowledge.db` | WX-W1-1, WX-W1-3 | `<computed-at-runtime>` |
| `sessions/framework/Collabs/tesla-framework-hypothesis-connes-addendum.md` | WX-W1-2 (modular-flow tick integration) | `<computed-at-runtime>` |
| `sessions/framework/correspondence/loop-quantum-gravity-phonon-exflation-comparison.md` | WX-W1-2 (LQG/CDT cross-framework integration) | `<computed-at-runtime>` |
| `sessions/session-x/session-x-w1-workingpaper.md` (WX-W1-1 gap table) | WX-W1-2 (gap-integration source) | `<computed-at-runtime>` (produced by WX-W1-1, consumed by WX-W1-2) |
| `computations/session-x/sx_w1_aggregate_domain_survey.npz` (if produced) | WX-W1-2 (kb_query_manifest + gap ledger) | `<computed-at-runtime>` |

**Note on dynamic SHAs**: all W1 inputs are `<computed-at-runtime>` because (a) the target document is mutated in place across the wave (its SHA is the discriminator between W1-1/W1-2 audit inputs and the W1-3 content input), and (b) `canonical_constants.py` + `knowledge.db` are live project state that may shift between plan-freeze and execution. The closure scripts capture the SHAs at execution time and pin them in the verdict line's audit_sha256 / content_sha256 per the dual-SHA discipline.
