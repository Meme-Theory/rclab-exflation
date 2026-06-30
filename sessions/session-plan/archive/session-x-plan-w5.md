# Session-X Plan — Wave 5: Conformal/Causal Diagrammatics (Comprehensive Aggregate Expansion)

**Date**: 2026-05-25
**Author**: schwarzschild-penrose-geometer (generated per /rclab-plan per-wave swarm; scope-corrected to expansion-primary)
**Owner agent**: `schwarzschild-penrose-geometer` (planner AND executor — the document's author-specialist)
**Plan source**: `sessions/session-plan/session-x-context.md` §0–§2, §4–§7 (W5 seed)
**Working paper**: `sessions/session-x/session-x-w5-workingpaper.md`
**Target document**: `sessions/framework/Phononic-Penrose-Diagrams.md` (58,219 bytes; authored 2026-03-21, post-S53; ~40 sessions of project evolution to integrate, S53→S93)

---

## Wave 5 Summary

**PRIMARY MODE — EXPANSION, not validation.** This wave comprehensively brings
`Phononic-Penrose-Diagrams.md` from its S53 authorship state to a current (S93-era) whole-project
view of the framework's **conformal/causal diagrammatics domain**. The document currently catalogs 9
S53-era diagrams (A–I) plus an *append-only* S85 W6-6 extension (Diagrams J–N) that was bolted on
without integrating it into the synthesis, the open-question list, or the diagram interrelations. In
between and after, ~40 sessions produced causal-structure, acoustic-metric, Petrov/CMPP, bi-metric,
spectral-dimension, and cosmological-history results that the document has NEVER folded in. The
deliverable (G2) is a substantially expanded / largely-rewritten document that reads as if authored
today with full knowledge of S54→S93.

The DOMAIN this wave surveys and expands: every result bearing on the framework's
**conformal compactification, causal structure, horizons, singularity theorems, Penrose/conformal
diagrams, acoustic vs geometric causal cones, Petrov/CMPP classification, Weyl-curvature-hypothesis
structure, and cosmological-history conformal diagrams** — across all ~93 sessions, reconstructed
from the knowledge base (NOT read linearly).

**VALIDATION is the embedded QA layer (G3), not the deliverable.** The drift-fixes below get
corrected *along the way*; they are necessary but are NOT the point. A reconcile-only pass FAILS this
wave (this plan OVERWRITES a prior mis-scoped reconcile-only plan).

### Carry-forward / scope source

This is a bespoke aggregate-expansion session (`session-x`), not a sequential compute session. The
"carry-forward" is the entire S54→S93 diagrammatics domain enumerated against the document's coverage
(the G1 gap analysis IS the carry-forward source). The §7 W5 seed plus the G1 survey define scope.

### What the G1 survey already surfaced (planner pre-survey; the executor extends this)

The planner ran ~20 KB queries at plan-freeze (manifest in the Input-SHA Ledger + reproduced in the
G1 WP block). Major gaps the document is MISSING (each with a provisional "where it belongs"):

| # | Gap (KB-cited) | Where it belongs |
|:--|:---------------|:-----------------|
| GAP-1 | **EoS quartet**: doc's `w=0.202` is the kinetic/transit-era *stiff* value; the late-time DE EoS is `w0_FW=-0.918` (Volovik partition, canonical, S58/S66), with `w_0_B=-0.842454` (substrate-compaction, S85 W10-2) and the S49 multi-T GGE band `[-0.43,-0.59]`. The `0.202` and `-0.918` are DISTINCT quantities (kinetic-modulus vs partition late-time) — disambiguate, do NOT overwrite. | Diagrams A, B, E, H + a new EoS-disambiguation callout |
| GAP-2 | **tau~0.22 vs tau_fold=0.19**: `tau_fold=0.19` is canonical (van Hove fold = dump = extremal horizon); `tau~0.22` is the post-fold physical-universe epoch. DISTINCT — the §0 disambiguation target (analog of the tau quartet). | Overview + Diagrams A, B, G + Zone table |
| GAP-3 | **Bi-metric Kasparov decoupling** (T3 permanent, S63/S66 VdD-Hawking): scalars see the acoustic metric (with white hole), tensors see the gravitational metric (no white hole); `U_total = 1_M ⊗ U_K ⟹ β_T=0` exactly at linear order; `r_s = c_s · r_H`. | Diagram C (two cones → two metrics for two field sectors); Diagram H; new sub-diagram |
| GAP-4 | **S55 dynamic-transit conformal diagram** (DIAGRAM-55): conformal diagram shows viable cosmology WITHOUT a static fixed point — directly bears on Diagrams A/B/E. | New diagram or Diagram B/E deepening |
| GAP-5 | **S69 conformal-factor transit** (W4-F CONFORMAL-FACTOR-TRANSIT-69, FACTOR-69, TRANSIT-69) — Penrose-diagram SHAPE from the conformal factor; ANOM-69/EPSH-69 conformal anomaly. sp-authored. | New diagram + Diagram A/B refinement |
| GAP-6 | **S70 Penrose sequence** (SEQUENCE-70) + **S71 causal moment map** (MAP-71, consumes s70_penrose_sequence.npz) — a time-ordered Penrose sequence and a causal-structure moment map; both post-date the doc. | New diagram(s) |
| GAP-7 | **S76 CMPP-TYPE-GGE-TRANSIT** (TRANSIT-76, W3-H, sp-authored) — Petrov classification of the GGE *during* transit (distinct from static/dynamic in Diagram A). | Diagram A/F deepening |
| GAP-8 | **S84 W8B-95 CMPP-PETROV-TYPE-INVARIANCE** (PASS, `D/D/D/D/D/D/D/D/G/G/G/G/G/G/G/G/8`) + **S85 W6-2 dense 171-pt grid** — the static-D/dynamic-G invariance is now a *permanent* result across 8+ tau points and a 171-point grid. The doc's Diagram M append references this but does not integrate the invariance theorem. | Diagram A/F + synthesis point 6 |
| GAP-9 | **DILUTION-CC (S66)** closes the 114-OOM CC gap to 0.01 OOM; `CC_OOM=115.5`. Bears on the cosmological-history diagrams (E, H) and the "vacuum energy = a_0 moment" framing. | Diagrams E/H epoch annotations + synthesis |
| GAP-10 | **Spectral-dimension flow vs CDT** (S92 ad-hoc workshop): `d_s(σ) = −2 d ln P/d ln σ`; the σ→0 Weyl asymptotic (=8 on SU(3)) vs the windowed `d_s(σ_*)` at the fold are DISTINCT functionals; impedance product `Z = ρ_E·v_g`; fair same-functional-same-scale comparison to CDT. This is the **current answer to the doc's Open Question #7**. | Open Question #7 → resolved section |
| GAP-11 | **Mach disambiguation**: the doc/MEMORY carry THREE distinct Mach-type velocities — transit Mach 13.75 (`Mach_max`, modulus-space transit/sound), the 12D transit velocity `v_transit=26.5 M_KK` (Diagram A/B), and the acoustic-analog `Mach_max=54.3` (MEMORY analog). Disambiguate. | Diagrams A, B, C + a velocity-glossary callout |
| GAP-12 | **r tensor-to-scalar**: doc cites the framework as decelerating FRW; current values are `r=3.86e-10` (S44 permanent) and the S63/S64 second-order scalar→tensor conversion `r^{(2)}~0.033` (TENSOR-SCALAR-64 PASS). Bears on Diagram E/H observational annotations. | Diagram E/H + synthesis |
| GAP-13 | **S77 overshoot turnaround** (tau=1.614, CMPP D-static / G-dynamic, `S77-C5-HESSIAN-OVERSHOOT` 35/35 negative): Diagram N captures the slice but the overshoot is not integrated into Diagram B's modulus-space zones or the censorship picture. | Diagram B/G integration |
| GAP-14 | **Reheating temperature** (S77 `T_RH=1.70e15 GeV`, `N_decay=63.4`; S74 alternative `T_rh=1.374e10 GeV`): the doc's Diagram E cosmological history needs the modulus-decay reheating epoch + its disambiguation (two pathways). | Diagram E |

The executor's G1 gate extends this table to full domain coverage (expect the survey to find more —
e.g., S47/S48 retracted analog-horizon history, S58/S61 acoustic-metric refinements, the
Akama-Diakonov emergent-metric open channel CF19, S93 substrate-mode-localization emergent-3-slices).

---

## Wave 5 Decision Point Prerequisites

**None.** Wave 5 is independent (no upstream S{N-1} or intra-session prerequisite). It surveys the
knowledge base and expands one curated framework document. It does NOT consume any other Session-X
wave's output. (The only dependent wave is W9, which verifies all 8 expanded docs are mutually
consistent — W9 consumes W5's OUTPUT, not the reverse.) Internally, the three gates are sequenced:
G2 consumes the G1 gap analysis; G3 reads the G2-expanded document. If a cited input file is missing
at dispatch time, the gate honestly closes per `.claude/rules/mechanical-closure-discipline.md`
(`value='upstream_<reason>'`); all three input files (the document, `canonical_constants.py`,
`tools/knowledge.db`) are verified present at plan-freeze.

### Split (per context §7 W5): W5a Diagrams A–C, W5b Diagrams D–I

The expansion is internally split into two diagram-family halves so the executor can pace the
comprehensive rewrite. Both halves are produced under the SAME three gates (the split is an
organizational discipline inside G2/G3, not separate gate-IDs): **W5a** = Diagrams A, B, C (the 12D
product spacetime, modulus-space conformal diagram, acoustic bi-metric) + the post-S53 conformal
diagrams that deepen them (S55, S69, S70, S71); **W5b** = Diagrams D–I (Mott lattice, GGE history,
Petrov/Weyl, censorship, complete history, novel/speculative) + the Diagram J–N append integrated +
the new spectral-dimension/CCC sections. The G1 gap analysis and the G3 reconciliation cover BOTH
halves; G2 produces BOTH halves and the verdict's `value=` field reports the per-half integration
counts.

---

## §W5-1. WX-W5-1-AGGREGATE-DOMAIN-SURVEY

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W5-1-AGGREGATE-DOMAIN-SURVEY"
schema_version: "R3"
trigger: "[AUDIT]"
classification: "GEOMETRIC"
agent_type: "schwarzschild-penrose-geometer"
hypothesis: "The conformal/causal diagrammatics domain across all ~93 sessions can be mapped against the document's coverage, and the GAP (results the project knows but the document does not cover) can be enumerated with KB citations across the pertinent entity classes (theorems / closed / gates / sessions / open / constants / equations / provenance)."

method:
  description: >
    Sweep the knowledge base BROADLY for the document's domain (conformal compactification, causal
    structure, horizons, singularity theorems, Penrose/conformal diagrams, acoustic vs geometric causal
    cones, Petrov/CMPP classification, Weyl-curvature-hypothesis structure, cosmological-history conformal
    diagrams) across S54->S93. Produce (a) a current whole-project STATE-OF-DOMAIN MAP and (b) a GAP
    ANALYSIS -- every domain result the document does NOT yet cover, each row with its KB citation and a
    one-line "where it belongs in the document." Plus a FIGURE-ASSET EXISTENCE CHECK: enumerate the 36
    existing figures/penrose/framework-{A..I*}.{tex,png,pdf} assets and confirm which diagrams have
    rendered assets vs ASCII-only, so G2 can flag any NEW diagram needing a TikZ stub via the
    /penrose-diagram skill. This gate is FAILED if it only re-checks the document's existing claims.
  producing_script: "computations/session-x/sx_w5_domain_survey.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator -- set-coverage of the domain + gap enumeration
operator:
  type: "set"
  form: >
    PASS iff (entity_classes_surveyed superset-of {theorems, closed, gates, sessions, open, constants,
    equations, provenance}) AND (|gap_rows| > 0 with every gap_row carrying a KB citation + a
    where-it-belongs tag) AND (figure_asset_existence_check enumerated for all 9 core diagrams A-I + 5
    append diagrams J-N). The survey is a SET-COVERAGE predicate over the domain's entity classes, NOT a
    numerical threshold.

# (2) strict_PASS_boundary -- domain classes surveyed + gap enumerated with citations
strict_PASS_boundary:
  value: "entity_classes_surveyed == 8 (all of {theorems, closed, gates, sessions, open, constants, equations, provenance}) AND gap_rows >= 14 (the planner pre-survey floor; executor extends) AND every gap_row has (kb_citation != '' AND where_belongs != '') AND figure_asset_check covers all 14 catalogued diagrams (A-N)"
  direction: ">="

# (3) boundary_reachable_analytically -- coverage-by-enumeration
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (the domain's pertinent entity classes are a finite enumerable set; the gap is the set-difference between project-knowledge-in-domain and document-coverage)"

# (4) reachable_rationals -- synthesis/expansion gate, no rational mesh
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A -- synthesis/expansion gate (survey + gap enumeration, not a numerical scan)"

# (5) machinery_pin_map -- survey tooling + scope, every parameter pinned
machinery_pin_map:
  N_eval: "N/A -- survey gate (no numerical evaluation; KB query count is a coverage observable, not a free numerical parameter)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A -- set-coverage predicate, not a numerical comparison"
  scheme: "aggregate-domain-survey-v1"
  convention: "kb-cited-gap-enumeration"
  random_seed: "N/A -- deterministic (KB queries are deterministic reads)"
  GPU_path: "N/A -- no linear algebra; KB reads + SHA only"
  kb_tools_surveyed: "[search_knowledge, trace_entity, list_entities, get_constant, query_entity, list_constants]"
  entity_classes_surveyed: "[theorems, closed, gates, sessions, open, constants, equations, provenance]"
  domain_scope_definition: "conformal compactification; causal structure (event/particle/apparent horizons); singularity theorems (Penrose 1965, trapped surfaces, geodesic incompleteness); Penrose & conformal diagrams; acoustic vs geometric causal cones (bi-metric); Petrov/CMPP algebraic classification; Weyl-curvature-hypothesis structure (|C|^2, Kretschmann K); cosmological-history conformal diagrams (epochs, EoS, e-folds, reheating)"
  gap_taxonomy: "[NEW-SINCE-AUTHORSHIP (S54+ result not in doc), NEVER-COVERED (pre-S53 domain result the doc omitted), DRIFTED-CLAIM (doc claim superseded/disambiguation-needed), APPEND-NOT-INTEGRATED (Diagram J-N bolted on but not woven into synthesis/open-questions)]"
  figure_asset_path_list: "figures/penrose/framework-A-12d-product.{tex,png,pdf}; framework-B-modulus-space.*; framework-C-acoustic-causality.*; framework-D-mott-lattice.*; framework-E-gge-history.*; framework-F-petrov-weyl.*; framework-G-censorship.*; framework-H-complete-history.*; framework-I1-white-hole-analogy.*; framework-I2-curvature-landscape.*; framework-I3-fock-space.*; framework-I4-wch-12d.*; (Diagrams J-N: ASCII/TikZ-stub only -- no rendered assets; flag for G2)"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (plan-freeze snapshot; gate re-pins <computed-at-runtime>)"
  document_sha_prefreeze: "Phononic-Penrose-Diagrams.md @ SHA256 d403d757b0680b012fdbd9ee78f69b5e63b55b2082958a2592ea07908a1e0ef7 (plan-freeze; gate re-pins <computed-at-runtime>)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]
  # NOTE: G1 does not modify the document; "document_post" == "document_pre" for this gate's content
  # hash. The content_sha256 pins the survey/gap artifact set the gate produces (state_of_domain_map +
  # gap_analysis written into the WP), which IS the gate's deliverable.

# (7) substitution_chain -- not required for the survey gate itself (no directional claim)
substitution_chain:
  required: false
  content: |
    G1 is a set-coverage + enumeration gate; it asserts no sign/direction/ratio claim. The directional
    claims it SURFACES (acoustic-cone narrowing, e-fold split, EoS-sign disambiguation) are pre-registered
    for the G2 gate's substitution_chain, where they are written or retained. (See section W5-2 substitution_chain.)

# (8) input_files
input_files:
  document:
    path: "sessions/framework/Phononic-Penrose-Diagrams.md"
    sha256: "<computed-at-runtime>"   # plan-freeze: d403d757b0680b012fdbd9ee78f69b5e63b55b2082958a2592ea07908a1e0ef7
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # plan-freeze: 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"   # 79.7 MB; rebuilt by /weave --update; dynamic

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w5_domain_survey.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w5_domain_survey.npz"
    artifact_kind: "data"
    optional: true   # survey artifact set is recorded in the WP; npz optional (may store gap-row table)
  plot:
    path: "computations/session-x/sx_w5_domain_survey.png"
    artifact_kind: "plot"
    optional: true   # no plot required for a survey gate
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W5-1-AGGREGATE-DOMAIN-SURVEY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w5-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W5-1. WX-W5-1-AGGREGATE-DOMAIN-SURVEY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"   # the KB query manifest lives here (context section 5 mandatory)
      - "State-of-Domain Map"
      - "Gap Analysis"
      - "Figure-Asset Existence Check"

# ---- Verdict rubric ----
PASS_meaning: >
  The conformal/causal diagrammatics domain has been swept across all 8 pertinent entity classes; the
  gap between project-knowledge-in-domain and document-coverage is enumerated with >= 14 cited gap rows
  (planner floor; executor extends), each with a where-it-belongs tag; the figure-asset existence check
  covers all 14 catalogued diagrams. The comprehensiveness ENGINE has run -- G2 has a complete, cited
  integration target. Solution-space: the expansion's scope is now bounded and provenance-traced.
FAIL_meaning: >
  The survey only re-checked the document's existing claims (validation, not domain survey), OR the gap
  analysis lacks KB citations / where-it-belongs tags, OR an entity class was skipped. This means the
  comprehensiveness engine did not run; G2 would expand against an imagined rather than KB-grounded gap.
INFO_meaning: >
  Domain swept and gaps enumerated, but a pertinent entity class returned ZERO domain hits (e.g., no
  in-domain 'open' entities) -- a genuine emptiness recorded honestly, not a coverage failure. The gate
  fires INFO and documents the empty class with its (null) query, so G2 knows that region is truly clear.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w5_domain_survey.py"
    - "computations/session-x/sx_w5_domain_survey.npz (optional -- gap-row table)"
    - "sessions/session-x/session-x-w5-workingpaper.md (section W5-1)"
  estimated_time: "0.4-0.6 day (heavy KB sweep -- tens of queries across 8 entity classes, S54->S93)"

substrate_framing: |
  GEOMETRIC. The domain is the conformal/causal structure of the spectral triple (A_K, H_K, D_K) and its
  product spacetime M^{3,1} x SU(3). The survey maps what the project now knows about how the substrate's
  eigenvalue geometry -> spectral-action moments (a_0/a_2/a_4) -> emergent 4D effective metric -> conformal
  boundary / causal cones / horizons / Petrov type. SU(3) is COMPACT and does NOT appear at conformal
  infinity; I^+/-, i^0, i^+/- are 4D constructs (this is the document's central structural invariant and the
  survey verifies the domain still respects it). The direction of explanation flows FROM D_K eigenvalues
  TOWARD the Penrose diagram -- never the reverse (no "GR governs the substrate" container-thinking).
```

---

## §W5-2. WX-W5-2-COMPREHENSIVE-EXPANSION

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W5-2-COMPREHENSIVE-EXPANSION"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "GEOMETRIC"
agent_type: "schwarzschild-penrose-geometer"
hypothesis: "The conformal/causal diagrammatics domain gap enumerated in G1 can be integrated into Phononic-Penrose-Diagrams.md -- adding diagrams/sections for post-S53 causal-structure results (S55/S69/S70/S71 conformal diagrams, S76 GGE-transit CMPP, S84/S85 CMPP invariance, bi-metric Kasparov split, spectral-dimension flow), deepening existing diagrams to current understanding, and disambiguating the tau~0.22 epoch and the w EoS -- in the geometer's authorial voice, such that the document reads as a current (S93) comprehensive synthesis. A minimal/cosmetic edit FAILS."

method:
  description: >
    THE DELIVERABLE. Substantially expand / rewrite Phononic-Penrose-Diagrams.md to integrate every
    material gap row from G1. Concretely (W5a + W5b split):
      W5a (Diagrams A-C):
        - Diagram A (12D product spacetime): integrate S76 CMPP-TYPE-GGE-TRANSIT (Petrov of GGE during
          transit) + S84 W8B-95 type-invariance theorem (D static / G dynamic, PERMANENT across 8+ tau,
          171-pt dense grid S85 W6-2) + S55 dynamic-transit-without-fixed-point conformal result. Restate
          the static-Type-D structural theorem with its current invariance status.
        - Diagram B (modulus-space conformal diagram): disambiguate tau~0.22 (post-fold physical epoch)
          vs tau_fold=0.19 (van Hove fold = dump = extremal horizon, kappa=0, T_H=0) explicitly; integrate
          the S77 overshoot turnaround (tau=1.614) into the zone structure; fold in S69 conformal-factor
          transit (Penrose-diagram shape) and the S70 Penrose-sequence / S71 causal-moment-map as
          modulus-space refinements; add the EoS-disambiguation callout (kinetic w=0.202 vs late-time
          w0_FW=-0.918 vs w_0_B=-0.842454 vs GGE band).
        - Diagram C (acoustic bi-metric): integrate the BI-METRIC KASPAROV DECOUPLING (T3 permanent,
          S63/S66 VdD-Hawking) -- the two cones are not just "different observers" but TWO METRICS for TWO
          FIELD SECTORS: scalars propagate in the acoustic metric (with white hole), tensors in the
          gravitational metric (no white hole), beta_T=0 exact at linear order, r_s = c_s*r_H. Add the
          velocity-glossary callout disambiguating the three Mach-type quantities (transit Mach 13.75;
          12D transit v=26.5 M_KK; acoustic-analog Mach 54.3). Refresh the second-sound CMB ladder (l ~ pi
          * c_fabric/c_Gold = 720.9) with current sound-speed pins.
      W5b (Diagrams D-I + appends + new sections):
        - Diagram E/H (cosmological history): integrate DILUTION-CC (S66, CC_OOM=115.5 -- the CC tension
          the framework now RESOLVES); add the reheating epoch (S77 T_RH=1.70e15 GeV / N_decay=63.4, with
          the S74 T_rh=1.37e10 GeV alternative disambiguated); add r tensor-to-scalar current values
          (r=3.86e-10 permanent; second-order r^{(2)}~0.033 S63/S64).
        - Diagram F (Petrov/Weyl): integrate the S84/S85 dense-grid CMPP invariance; restate the Weyl
          zero-crossings (0.895, 1.340) as Lambda^2 signature changes (not Petrov transitions) per current
          understanding.
        - Diagram G (censorship): integrate the S63 12D trapped-surface result (theta_int=0 identically;
          [T5] Volume-Preserving No-Trapping PERMANENT) and the overshoot into the censorship picture.
        - Integrate the Diagram J-N append INTO the synthesis + open-questions (currently bolted on);
          give J-N proper interrelation with A-I.
        - Resolve Open Question #7 (spectral dimension & conformal structure) using the S92 ad-hoc
          d_s-flow-vs-CDT workshop (sigma->0 Weyl asymptotic vs windowed d_s(sigma_*); impedance product;
          fair same-functional-same-scale comparison). Add a new section.
        - Update the synthesis (7 points) and open-questions list to S93 state; retire resolved questions.
    Drift-fixing happens here as the QA layer (every retained claim brought current). Every NEW diagram
    gets a TikZ stub via the .claude/skills/penrose-diagram/SKILL.md (full set of boundary labels
    {i+, i-, i0, I+, I-, horizons, singularities, shading}); ASCII sketches acceptable for conversational
    reasoning but the canonical output is skill-TikZ, saved to figures/penrose/<name>.tex where a new
    rendered diagram is warranted.
  producing_script: "computations/session-x/sx_w5_comprehensive_expansion.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator -- set: gap-integration (integrated union scoped-out = all G1 gaps)
operator:
  type: "set"
  form: >
    PASS iff (integrated_gaps union scoped_out_gaps == all_G1_material_gaps) AND (scoped_out_gaps each
    carry a one-line reason) AND (document_post is a substantial expansion: new sections for
    post-authorship results + deepened existing diagrams + tau~0.22 and w EoS disambiguated) AND (every NEW
    diagram carries the full boundary-label set + a skill-TikZ stub). The predicate is set-equality (every
    G1 gap is accounted for) PLUS a substantiveness predicate (expansion, not cosmetic edit).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "for every material gap row g in G1: (g in integrated) XOR (g in scoped_out with reason); AND (count of integrated gaps / count of material gaps) reported per-half (W5a, W5b) in verdict value=; AND document_post substantially larger and restructured (new sections present for GAP-3 bi-metric, GAP-10 spectral-dimension, GAP-13 overshoot integration); AND tau~0.22-vs-tau_fold AND w-EoS disambiguation callouts both present"
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (gap set from G1 is finite; integrated union scoped-out = gap set is a decidable set-equality over the G1 enumeration)"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A -- synthesis/expansion gate (prose + diagram integration, not a numerical scan)"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A -- expansion gate (no numerical evaluation; gap-integration count is a coverage observable)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A -- set-equality predicate, not a numerical comparison"
  scheme: "comprehensive-expansion-v1"
  convention: "gap-integrated-or-scoped"
  random_seed: "N/A -- deterministic"
  GPU_path: "N/A -- prose/diagram authoring + SHA; no linear algebra"
  diagram_split: "W5a={A,B,C + S55/S69/S70/S71 conformal-diagram integration}; W5b={D,E,F,G,H,I + J-N integrated + spectral-dimension section + bi-metric section}"
  tikz_skill_pin: ".claude/skills/penrose-diagram/SKILL.md (canonical TikZ preamble + snippet library + worked templates; full boundary-label set mandatory per output-standards.md)"
  new_diagram_asset_dir: "figures/penrose/<name>.tex (or sessions/session-x/figures/ if produced in-session); rendered PNG via figures/penrose/build.sh"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (plan-freeze; gate re-pins <computed-at-runtime>)"
  document_sha_prefreeze: "d403d757b0680b012fdbd9ee78f69b5e63b55b2082958a2592ea07908a1e0ef7 (plan-freeze)"
  gap_source: "WX-W5-1-AGGREGATE-DOMAIN-SURVEY gap_analysis (section W5-1 WP block); the integration target"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]
  # document_post is the EXPANDED document -- content_sha256 changes materially vs document_pre (the
  # substantiveness signal: a cosmetic edit leaves content_sha256 nearly degenerate vs pre).

# (7) substitution_chain -- REQUIRED (directional/ratio claims added or retained)
substitution_chain:
  required: true
  content: |
    Two directional claims are load-bearing in the expansion and MUST be written per
    math-scripts.md "Double-Check Logic Before Compute":

    CLAIM A -- Acoustic cone is NARROWER than the geometric cone (cone-opening ratio).
      Step 1: c_Gold = 0.915 M_KK            [canonical_constants get_constant c_Gold; Goldstone sound speed]
      Step 2: c_fabric = 209.97368021 M_KK   [canonical_constants get_constant c_fabric; substrate fabric speed]
      Step 3: cone_opening_acoustic / cone_opening_geom = arctan(c_Gold/c_fabric) / arctan(1)  [opening-angle defn]
      Step 4: Substitute and simplify
            = arctan(0.915/209.97) / arctan(1)
            = arctan(0.004358) / (pi/4)
            ~ 0.004358 / 0.785398        [small-angle: arctan(x) ~ x]
            ~ 0.005549                   [dimensionless ratio]
            => ratio of horizon DISTANCES c_fabric/c_Gold = 229.48  [reciprocal scale; the "229x narrower" figure]
      Step 5: c_Gold/c_fabric << 1 => acoustic cone opening << geometric => acoustic cone NARROWER  [direction]
      Conclusion: the acoustic null cone is ~229x narrower (in horizon distance) than the geometric cone;
                  the scalar sector (which sees the acoustic metric per the bi-metric split) is causally
                  confined relative to the substrate. [now justified]

    CLAIM B -- The e-fold split: the acoustic observer gains MORE e-folds than the geometric observer
    during transit (the document's central insight, retained + re-grounded).
      Step 1: a_acoustic = a_geom * sqrt(rho/c_s)   [BLV acoustic scale factor; Diagram C]
      Step 2: N_e = ln(a_final/a_initial)            [e-fold definition]
      Step 3: N_e^acou - N_e^geom = ln(sqrt(rho_f/c_s,f) / sqrt(rho_i/c_s,i))  [substitute; a_geom cancels in the ratio's geom part]
      Step 4: dominant term is the sound-speed transition c_fabric -> c_Gold (factor 229 drop in c_s)
            => Delta N_e (sound-speed) = +0.5*ln(c_fabric/c_Gold) ~ +0.5*ln(229.48) ~ +2.72  [the +2.72 acoustic e-folds]
            geometric gain (volume-preserving Jensen) ~ +0.17 e-folds  [EFOLD-MAPPING-52; det g_tau=const bounds a_geom]
      Step 5: 2.92 (=2.72+0.17 acoustic) > 0.17 (geom) => acoustic observer sees a UNIVERSE; geom barely moves  [direction]
      Conclusion: "the universe is what a phonon sees when the substrate barely moves" -- retained, now
                  grounded in the c_s-transition substitution chain + the bi-metric split (only the scalar
                  sector, on the acoustic metric, experiences this expansion). [now justified]

    Any FURTHER directional claim the executor retains or adds (e.g., the |C|^2/K DECREASING WCH claim,
    the Omega_k GROWS 2x anti-inflation claim) MUST carry its own substitution chain in the WP section W5-2 block.

# (8) input_files
input_files:
  document:
    path: "sessions/framework/Phononic-Penrose-Diagrams.md"
    sha256: "<computed-at-runtime>"   # plan-freeze: d403d757b0680b012fdbd9ee78f69b5e63b55b2082958a2592ea07908a1e0ef7
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # plan-freeze: 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17
  gap_analysis:
    path: "sessions/session-x/session-x-w5-workingpaper.md"   # the section W5-1 gap_analysis block (produced upstream this wave)
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w5_comprehensive_expansion.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w5_comprehensive_expansion.npz"
    artifact_kind: "data"
    optional: true   # the expanded document IS the deliverable; npz optional (may store gap-integration ledger)
  plot:
    path: "computations/session-x/sx_w5_comprehensive_expansion.png"
    artifact_kind: "plot"
    optional: true   # new diagrams render via figures/penrose/build.sh, not a gate .png
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W5-2-COMPREHENSIVE-EXPANSION:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  document_post:
    path: "sessions/framework/Phononic-Penrose-Diagrams.md"
    artifact_kind: "expanded_document"
    must_contain:
      # Substantiveness markers -- these MUST appear in the expanded document (each ties to a major gap):
      - "Kasparov"                 # GAP-3 bi-metric decoupling integrated
      - "spectral dimension"       # GAP-10 d_s-flow / Open Question #7 resolved
      - "1.614"                    # GAP-13 overshoot turnaround integrated into modulus-space zones
      - "DILUTION-CC"              # GAP-9 CC resolution integrated into cosmological history
      - "S93"                      # document re-dated/re-scoped to current era
    optional: false
  wp_section:
    path: "sessions/session-x/session-x-w5-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W5-2. WX-W5-2-COMPREHENSIVE-EXPANSION"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
      - "Gap Integration Ledger"        # per-gap: integrated / scoped-out (with reason)
      - "W5a"                            # Diagrams A-C half
      - "W5b"                            # Diagrams D-I half

# ---- Verdict rubric ----
PASS_meaning: >
  Every material G1 gap is integrated OR explicitly scoped-out with a one-line reason; the document now
  reads as a current (S93) comprehensive synthesis of the conformal/causal diagrammatics domain -- new
  sections for the bi-metric Kasparov split, the spectral-dimension/CDT resolution, and the J-N integration;
  deepened A-I; tau~0.22-vs-tau_fold and the w EoS disambiguated (NOT overwritten); every new diagram with
  full boundary labels + skill-TikZ. Solution-space: the document is now an authoritative current map of
  the framework's causal geometry.
FAIL_meaning: >
  A cosmetic/minimal edit (content_sha256 ~ document_pre), OR material gaps left neither integrated nor
  scoped, OR the tau/w disambiguations missing, OR a directional claim added/retained WITHOUT its
  substitution chain, OR a new diagram lacking the full boundary-label set. Solution-space: the expansion
  did not happen; the document remains stale.
INFO_meaning: >
  Substantial expansion landed, but >= 1 material gap is scoped-out as "belongs in a sibling document"
  (e.g., a pure-cosmology epoch detail that lives in Phononic-to-Cosmos.md W3, or a pure-CM correspondence
  that lives in Classification W7) with a cross-reference rather than duplicated here -- a legitimate scope
  boundary recorded honestly, flagged for the W9 cross-document consistency sweep.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w5_comprehensive_expansion.py"
    - "sessions/framework/Phononic-Penrose-Diagrams.md (SUBSTANTIALLY EXPANDED -- the deliverable)"
    - "sessions/session-x/session-x-w5-workingpaper.md (section W5-2)"
    - "figures/penrose/<new-diagram>.tex (any NEW rendered diagram warranted by the survey)"
  estimated_time: "1.0-1.5 day (the center of mass -- a full wave of comprehensive synthesis writing across two diagram-family halves)"

substrate_framing: |
  GEOMETRIC. The expansion preserves and re-grounds the IS-not-IN direction: D_K eigenvalue spectrum ->
  spectral-action moments (a_0 = cosmological/vacuum term DISTINCT from a_2 = Einstein-Hilbert/gravity) ->
  emergent 4D effective metric g_M (from a_2) -> conformal boundary + causal cones + Petrov type. SU(3) is
  compact (invisible at conformal infinity); the modulus tau is the substrate's INTRINSIC deformation
  parameter, NOT a coordinate in a meta-container (Level-2 moduli-deformation substrate-IS per
  phononic-framing.md). The bi-metric split is substrate-first: the acoustic metric is what the SCALAR
  excitation sector sees (a derived effective metric, not fundamental); the gravitational metric is the
  a_2-emergent one the TENSOR sector sees. "The universe is what a phonon sees" is the substrate statement
  of the acoustic-observer e-fold gain. No claim explains the substrate via GR -- GR (the a_2 Einstein-Hilbert
  action, the area theorem) is DERIVED from substrate spectral structure.
```

---

## §W5-3. WX-W5-3-RECONCILE-VERIFY

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W5-3-RECONCILE-VERIFY"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "GEOMETRIC"
agent_type: "schwarzschild-penrose-geometer"
hypothesis: "After the G2 expansion, the document contains ZERO stale / unframed / untraced claims: every claim (retained + newly added) is current against the S93 KB, framing-compliant (IS-not-IN per phononic-framing.md -- SU(3) compact and absent from conformal infinity; explanation flows D_K -> moments -> emergent physics), provenance-traced (canonical_constants entry / permanent theorem / closed mechanism / gate verdict), and a_n^{regulator}-tagged where a Seeley-DeWitt coefficient is cited, AND every claim that the substrate is IS-not-IN-space and that observables trace to CMPP/Petrov computations holds."

method:
  description: >
    QA sweep over the EXPANDED document (the G3 set, PASS = empty). For every claim:
      (1) CURRENCY: cross-check numerical values against canonical_constants.py / KB (no stale pin; the
          tau~0.22-vs-tau_fold=0.19 and w=0.202-vs-w0_FW=-0.918 disambiguations present and correct).
      (2) FRAMING: IS-not-IN compliance -- SU(3) compact, does NOT appear at conformal infinity; i+/-/i^0/I+/-
          are 4D constructs; the explanation direction flows FROM D_K eigenvalues TOWARD the Penrose
          diagram (no container-thinking, no "GR governs the substrate").
      (3) PROVENANCE: every claim traces to a canonical_constants entry, a permanent theorem
          (atlas-07-permanent-results), a closed mechanism, or a gate verdict -- every NEW causal-structure
          claim traces specifically to a CMPP/Petrov computation (S49/S50/S76/S84-W8B-95/S85-W6-2) or an
          acoustic/conformal gate (S53/S55/S63/S69/S70/S71/S85-W6).
      (4) a_n TAGGING: any Seeley-DeWitt coefficient citation (a_0, a_2, a_4 -- the doc's "vacuum energy =
          a_0", "gravity = a_2", "Yang-Mills = a_4") carries an explicit regulator tag a_n^{regulator} per
          regulator-pin-discipline.md.
    Build the stale/unframed/untraced SET; PASS iff the set is EMPTY.
  producing_script: "computations/session-x/sx_w5_reconcile_verify.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator -- set: stale union unframed union untraced, PASS = empty
operator:
  type: "set"
  form: >
    PASS iff (stale_claims union unframed_claims union untraced_claims union untagged_a_n_claims == empty).
    Each subset is a finite enumeration over the expanded document's claims; the union is the QA-defect
    set; PASS is the empty-set predicate.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "|stale_claims union unframed_claims union untraced_claims union untagged_a_n_claims| == 0; AND the two mandatory disambiguations (tau~0.22 vs tau_fold=0.19; w=0.202 vs w0_FW=-0.918) verified present and internally consistent; AND the substrate-IS invariant (SU(3) compact, absent from conformal infinity) restated and unviolated; AND every new causal-structure claim cites a CMPP/Petrov or acoustic/conformal gate"
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (claims in the expanded document are a finite enumerable set; the defect set is the union of four decidable per-claim predicates)"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A -- synthesis/expansion QA gate (claim-by-claim verification, not a numerical scan)"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A -- QA gate (no numerical evaluation; defect-set cardinality is a coverage observable)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A -- empty-set predicate, not a numerical comparison"
  scheme: "reconcile-verify-v1"
  convention: "stale-unframed-untraced-set-empty"
  random_seed: "N/A -- deterministic"
  GPU_path: "N/A -- claim verification + SHA; no linear algebra"
  qa_axes: "[currency (value vs canonical/KB), framing (IS-not-IN per phononic-framing.md), provenance (canonical_constants/theorem/closed/gate trace), a_n regulator tagging]"
  disambiguation_checks: "[tau~0.22 (post-fold epoch) != tau_fold=0.19 (van Hove fold/dump/extremal horizon); w=0.202 (kinetic/transit stiff) != w0_FW=-0.918 (late-time DE, canonical) != w_0_B=-0.842454 (S85)]"
  substrate_is_invariant: "SU(3) COMPACT; does NOT contribute to conformal boundary; i+/-/i^0/I+/- are 4D constructs; 12D Penrose diagram conformally identical to 4D with modified matter content (the document's central structural invariant -- MUST be restated and unviolated post-expansion)"
  cmpp_traceback_pins: "[CMPP-TRANSITION-49 (Lorentzian Type D, corrects Riemannian Type II artifact); A3/A4 atlas-07 (8D Petrov + Lorentzian CMPP Type D PERMANENT); S76 TRANSIT-76 (GGE-transit CMPP); S84-W8B-95 (type-invariance D/G); S85-W6-2 (dense-grid)]"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (plan-freeze; gate re-pins <computed-at-runtime>)"
  document_sha_expanded: "<computed-at-runtime>  # the G2 document_post; this gate reads the EXPANDED document"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]
  # Here "document_pre" for the audit hash is the G2-expanded document (G3's input); "document_post" is
  # the same document after any G3 in-place QA corrections (drift-fix touch-ups). If G3 finds zero
  # defects, document_post == its input (no corrective edit needed) and the gate PASSes clean.

# (7) substitution_chain -- verifies the chains G2 wrote (does not author new directional claims)
substitution_chain:
  required: true
  content: |
    G3 does not author NEW directional claims; it VERIFIES that every directional/ratio claim in the
    expanded document carries a valid substitution chain (per math-scripts.md). The verification predicate:
      Step 1: enumerate every claim containing {narrower, wider, increases, decreases, dominates,
              larger/smaller than, grows, suppresses} in the expanded document.
      Step 2: for each, confirm a substitution chain is present (in the document or its WP G2 block) with
              definitions cited to canonical sources.
      Step 3: spot-recompute the two load-bearing chains (acoustic-cone ratio 229.48 = c_fabric/c_Gold;
              acoustic e-fold gain +2.72 = 0.5*ln(c_fabric/c_Gold)) against canonical_constants pins.
      Step 4: any directional claim WITHOUT a chain => member of unframed_claims => G3 FAIL.
      Conclusion: the document's directional content is fully chain-justified, OR the defect set is non-empty.

# (8) input_files
input_files:
  document:
    path: "sessions/framework/Phononic-Penrose-Diagrams.md"   # the G2-EXPANDED document
    sha256: "<computed-at-runtime>"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # plan-freeze: 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w5_reconcile_verify.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w5_reconcile_verify.npz"
    artifact_kind: "data"
    optional: true   # defect-set table optional; recorded in WP
  plot:
    path: "computations/session-x/sx_w5_reconcile_verify.png"
    artifact_kind: "plot"
    optional: true
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W5-3-RECONCILE-VERIFY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w5-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W5-3. WX-W5-3-RECONCILE-VERIFY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
      - "Stale/Unframed/Untraced Set"   # the defect set (PASS = empty)
      - "Disambiguation Verification"   # tau~0.22 vs tau_fold; w EoS

# ---- Verdict rubric ----
PASS_meaning: >
  Zero stale/unframed/untraced/untagged claims in the expanded document; both mandatory disambiguations
  present and consistent; the SU(3)-compact-absent-from-conformal-infinity invariant restated and
  unviolated; every new causal-structure claim traces to a CMPP/Petrov or acoustic/conformal computation.
  Solution-space: the expanded document is QA-clean and citation-tight -- ready for the W9 cross-document
  consistency sweep.
FAIL_meaning: >
  >= 1 stale value (e.g., w=0.202 presented AS the late-time DE EoS; tau~0.22 conflated with tau_fold=0.19),
  OR a container-thinking violation (SU(3) treated as IN a spacetime; GR explaining the substrate), OR an
  untraced claim, OR an untagged Seeley-DeWitt coefficient, OR a directional claim missing its chain.
  Solution-space: the expansion introduced or retained defects; remediate before W9.
INFO_meaning: >
  Document is QA-clean except for >= 1 claim flagged DEFER-TO-SIBLING (a value whose canonical home is
  another Session-X document, e.g., a DESI-DR3 w_a pin that W3 Phononic-to-Cosmos owns) -- recorded with a
  cross-reference for the W9 shared-constant-matrix sweep rather than re-litigated here.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w5_reconcile_verify.py"
    - "sessions/session-x/session-x-w5-workingpaper.md (section W5-3)"
    - "sessions/framework/Phononic-Penrose-Diagrams.md (in-place QA touch-ups only, if defects found)"
  estimated_time: "0.4-0.5 day (claim-by-claim QA over the expanded document across four axes)"

substrate_framing: |
  GEOMETRIC. The QA gate enforces the IS-not-IN direction at the claim level: it FAILS any sentence that
  treats SU(3) as embedded in a pre-existing spacetime container, that explains a substrate result by
  invoking GR/black-hole physics rather than deriving GR from the a_2 spectral moment, or that presents the
  modulus tau as a coordinate in a meta-container rather than the substrate's intrinsic deformation
  parameter. Provenance tracing enforces substrate-first sourcing: every number is a spectral moment of D_K
  or a canonical pin derived from one, never an external-paper placeholder treated as canonical. The CMPP/
  Petrov traceback ensures the causal-structure claims rest on the Lorentzian-Type-D computation (which
  itself corrected the S49 Riemannian-Type-II artifact -- a worked example of substrate-first self-correction).
```

---

## Wave 5 → Wave 9 Decision Point

Wave 5 produces an **expanded `Phononic-Penrose-Diagrams.md`** and three verdict lines. It has no
intra-wave successor. Its OUTPUT feeds **W9** (cross-document consistency + coverage closeout over the
8 expanded docs, owner `gen-physicist`):

| W5 outcome | W9 consequence |
|:-----------|:---------------|
| G1 PASS, G2 PASS, G3 PASS | W9 SHARED-CONSTANT-MATRIX includes the expanded doc's pins (tau_fold=0.19, w0_FW=-0.918, CC_OOM=115.5, c_Gold/c_fabric, Mach_max=13.75, tau_overshoot=1.614) and cross-checks them against W1/W3/W4 (framework-hypothesis, to-cosmos, C-causality) for cross-document agreement; COVERAGE-CONSISTENCY confirms the diagrammatics domain is comprehensively covered with no orphan gap. |
| G2 INFO (gap scoped DEFER-TO-SIBLING) | W9 resolves the scope boundary: confirms the deferred content lands in its named sibling document (e.g., DESI/CC epoch detail in W3) and that the cross-reference is bidirectional. |
| G3 INFO (claim DEFER-TO-SIBLING) | W9 SHARED-CONSTANT-MATRIX adjudicates which document owns the deferred pin; the geometer doc cites, the owner doc canonicalizes. |
| Any G FAIL | W9 cannot certify cross-document consistency for the diagrammatics domain until W5 is remediated; W9 flags W5 as the blocking wave in its coverage report. |

**Action item (7-field, per output-standards.md) — the single carry-forward to W9:**

1. **What**: Provide the expanded `Phononic-Penrose-Diagrams.md` + its pin list (tau_fold, tau_overshoot, w0_FW, w_0_B, CC_OOM, c_Gold, c_fabric, Mach_max, T_acoustic, n_pairs) for the W9 shared-constant matrix and coverage-consistency sweep.
2. **Who**: `schwarzschild-penrose-geometer` (produces) → `gen-physicist` (consumes in W9).
3. **Input**: the three W5 verdict lines + the expanded document (document_post SHA) + the §W5-2 Gap Integration Ledger.
4. **Output**: W9 cross-document agreement verdict for the diagrammatics-domain pins + coverage confirmation.
5. **Format**: `sessions/session-x/session-x-w9-workingpaper.md` (W9 section); pins cross-checked against `computations/_shared/canonical_constants.py`.
6. **Deadline**: Session-X W9 (the dependent closeout wave).
7. **Depends on**:
   - WX-W5-2-COMPREHENSIVE-EXPANSION PASS (the expanded document; UPSTREAM GATE this wave).
   - WX-W5-3-RECONCILE-VERIFY PASS (QA-clean; UPSTREAM GATE this wave).
   - `computations/_shared/canonical_constants.py` @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (the pin source-of-truth).

---

## Wave 5 Machinery-Enumeration Pin

Aggregate of the three gates' `machinery_pin_map` entries (per `epistemic-discipline.md
§"Pre-Registration Completeness"` PRDR; consumed by `_yaml_gate_validator.py` for sig_4). All three
gates are synthesis/expansion gates — no numerical scan, no GPU, deterministic. The "machinery" being
pinned is the SURVEY SCOPE + INTEGRATION TARGET + QA AXES, not numerical solver parameters:

| Gate | scheme | convention | GPU_path | Pinned machinery (scope) |
|:-----|:-------|:-----------|:---------|:--------------------------|
| WX-W5-1 (survey) | aggregate-domain-survey-v1 | kb-cited-gap-enumeration | N/A | 6 KB tools × 8 entity classes; domain-scope definition; gap taxonomy (4 classes); figure-asset path list (14 diagrams) |
| WX-W5-2 (expansion) | comprehensive-expansion-v1 | gap-integrated-or-scoped | N/A | diagram split (W5a/W5b); TikZ skill pin; new-diagram asset dir; gap source = §W5-1 |
| WX-W5-3 (reconcile) | reconcile-verify-v1 | stale-unframed-untraced-set-empty | N/A | 4 QA axes; 2 disambiguation checks; substrate-IS invariant; CMPP traceback pins |

**Common pins (all three gates):**
- `canonical_constants.py` snapshot: SHA256 `30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17` (plan-freeze; each gate re-pins `<computed-at-runtime>`).
- `random_seed`: `N/A — deterministic` (KB reads, prose authoring, and SHA computation are deterministic).
- `tolerance`: `N/A` (set-coverage / set-equality / empty-set predicates, not numerical comparisons).
- `GPU_path`: `N/A` (no linear algebra; KB reads + prose authoring + SHA only).
- `audit_sha256_inputs`: `[document_pre, state_of_domain_map, gap_analysis, canonical_constants_snapshot, kb_query_manifest]`; `content_sha256_inputs`: `[document_post]` (per context §4 mapping).

**Closure-script note**: each gate's closure script `computations/session-x/sx_w5_{slug}.py` is
mechanical — it `from canonical_constants import *`, loads the document + canonical snapshot +
survey/gap artifacts, computes the dual SHA, and `append_verdict`s to
`computations/session-x/sx_gate_verdicts.txt`. The intellectual work (domain survey, gap analysis,
comprehensive expansion writing) is the executor's, recorded in the WP + the survey/gap artifacts +
the expanded document itself.

---

## Wave 5 Input-SHA Ledger

Every input file the wave's gates consume, with plan-freeze SHA-256 (per `gate-verdicts.md`).
Static files carry precomputed hashes; dynamic inputs marked `<computed-at-runtime>`. Cross-checked
at plan-freeze by `_plan_upstream_pin_validator.py`.

| Input file | Role | Plan-freeze SHA-256 | Runtime pin |
|:-----------|:-----|:--------------------|:------------|
| `sessions/framework/Phononic-Penrose-Diagrams.md` | the document (G1 reads; G2 reads+expands; G3 reads expanded) | `d403d757b0680b012fdbd9ee78f69b5e63b55b2082958a2592ea07908a1e0ef7` | `<computed-at-runtime>` (G2 changes it; G3 reads document_post) |
| `computations/_shared/canonical_constants.py` | canonical pin source-of-truth (all 3 gates) | `30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17` | `<computed-at-runtime>` |
| `tools/knowledge.db` | KB query target (G1 survey; G2/G3 trace-back) | `<computed-at-runtime>` (79,724,544 bytes; rebuilt by `/weave --update`; dynamic) | `<computed-at-runtime>` |
| `sessions/session-x/session-x-w5-workingpaper.md` (§W5-1 gap_analysis) | G2 integration target (produced upstream this wave by G1) | `<computed-at-runtime>` (created during G1) | `<computed-at-runtime>` |

**Plan-freeze verification (executed at planning):**
- Document present: YES (58,219 bytes; SHA `d403d757…`).
- canonical_constants.py present: YES (SHA `30b33df3…`).
- knowledge.db present: YES (79,724,544 bytes; SHA dynamic — rebuilt by `/weave --update`).
- `computations/session-x/` present: YES (verdict file `sx_gate_verdicts.txt` to be created at first append).
- Figure assets present: 36 files for Diagrams A–I (`framework-{A..I*}.{tex,png,pdf}`); Diagrams J–N are ASCII/TikZ-stub only (no rendered assets) — flagged for G2 (any newly-warranted rendered diagram gets a skill-TikZ source saved to `figures/penrose/<name>.tex`).

**KB query manifest (planner pre-survey — reproduced in §W5-1 WP MCP Pre-Compute Audit block; executor extends):**
- `search_knowledge`: "Penrose diagram conformal causal structure horizon"; "acoustic metric white hole sonic horizon supersonic"; "CMPP Petrov type D type G Weyl classification"; "singularity theorem trapped surface geodesic incompleteness censorship"; "transit Mach number sonic horizon entry exit S74 causality formalization"; "equation of state w post-transit GGE relic e-folds epoch reheating temperature"; "Weyl curvature hypothesis Kretschmann scalar conformal flatness arrow of time"; "conformal cyclic cosmology CCC conformal compactification infinity bifurcation regulator"; "spectral dimension flow d_s UV IR running dimensional reduction CDT"; "bi-metric scalar tensor two cones gravitational acoustic Volovik horizon split"; "second sound CMB multipole ladder Goldstone Leggett Higgs branch dispersion"; "overshoot turnaround tau 1.614 modulus evolution turning point reheating"; "c-compare skill propagation substrate dynamics classification".
- `trace_entity`: "Penrose sequence S70".
- `get_constant`: `tau_fold`(0.19, not superseded), `Mach_max`(13.75), `w0_FW`(-0.918), `CC_OOM`(115.5, S66), `c_Gold`(0.915), `c_fabric`(209.97368021), `v_transit`(not found — Diagram-A value 26.5 is WP-local), `c_BdG`(not found), `T_RH`(not found — S77 WP value 1.70e15 GeV), `tau_overshoot`(1.614), `G_mod`(not found — doc-local 5.0), `N_pair`(→ `n_pairs`=59.8), `T_acoustic`(0.112).

---

## Footer — Wave 5 Independence & Constraints

- **Prereqs**: NONE — Wave 5 is independent (surveys the KB + expands one curated document; consumes no
  other Session-X wave's output). The only dependency direction is W5 → W9 (W9 consumes W5's output).
- **Write scope**: this wave writes ONLY (a) the expanded `Phononic-Penrose-Diagrams.md` (G2 deliverable),
  (b) `sessions/session-x/session-x-w5-workingpaper.md` (the 3 gate sections), (c)
  `computations/session-x/sx_w5_{slug}.py` closure scripts + `sx_gate_verdicts.txt` appends, (d) any NEW
  `figures/penrose/<name>.tex` warranted by the survey. It does NOT edit any other framework document or
  any other Session-X wave's artifacts.
- **Curated-edit-by-author path**: this is the legitimate curated maintenance path (`feedback_framework-hygiene.md`
  + CLAUDE.md project-structure note) — the document's own author-specialist (the geometer) comprehensively
  revises it. NOT a bulk install-agent append to a curated root file.
- **Full fidelity**: no length targets; the deliverable is a comprehensively expanded document, verified by
  CONTENT (the must_contain markers + the gap-integration ledger), not by line/byte count
  (`feedback_max-effort-full-fidelity.md`).
- **Do not finish fast**: a domain-wide synthesis of ~40 sessions of conformal/causal-structure results
  cannot be done in a quick pass (context §0). The G1 survey is heavy (tens of KB queries); G2 is the
  center of mass (two diagram-family halves, comprehensive rewrite); G3 is the four-axis QA.
- **Scope correction note**: this plan file OVERWRITES a prior mis-scoped reconcile-only plan
  (`WX-W5-1-RECONCILE-PENROSE-DIAGRAM-CLAIMS` / RECONCILE→UPDATE→VERIFY). The current plan is
  expansion-primary (SURVEY→EXPAND→VERIFY) per context §0/§4; a reconcile-only pass FAILS the assignment.
```
