# Session-X Plan — Wave 8: SU(3) Jensen Crystal-Geometry Visualization (script + figures + ARCHIVE source) — COMPREHENSIVE EXPANSION

**Date**: 2026-05-25
**Author**: baptista-spacetime-analyst (per-wave planner; session-x fanout swarm)
**Owner agent**: baptista-spacetime-analyst (SU(3)/Jensen geometry; Riemannian-submersion fiber-base decomposition; judges geometric correctness AND executes the GPU-venv rerun in the document's authorial voice)
**Plan source**: `sessions/session-plan/session-x-context.md` §0 (PRIMARY MODE — expansion), §1, §2, §4 (gate architecture), §5 (survey directive), §6 (governing rules), §7 "W8" seed
**Working paper**: `sessions/session-x/session-x-w8-workingpaper.md`

> **THIS FILE OVERWRITES the prior mis-scoped W8 plan** (which was RECONCILE → UPDATE+RERUN → ARCHIVE-SCRUTINY, a validation-primary skeleton whose G2 did not mandate ADDING figures). Per the session-x scope correction (context §0): **EXPANSION is the job; VALIDATION is the embedded QA sub-layer.** A verify-only plan FAILS. This plan's center of mass is G2 (`WX-W8-2`): bring the depicted geometry to current (S93-era) understanding, ADD figures for post-S47 geometric results that warrant visualization, regenerate via the GPU venv, AND comprehensively migrate the archived source doc forward.

## Wave 8 Summary

W8 comprehensively brings ONE artifact-triple — the visualization script `sessions/framework/Phononic-crystal-geometry_viz.py` (36,290 B), its 7 output figures `Phononic-Crystal-Geometry-Vis-{1..7}.png`, and its archived source document `sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md` (25,581 B) — to a current whole-project view of **SU(3) Jensen crystal geometry**, integrating ~46 sessions of geometric results (S47 source → S93). The script imports 16 names from `canonical_constants` (`tau_fold, c_fabric, c_Gold, J_C2, J_su2, J_u1, N_cells, E_cond, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3, N_e_classical, xi_BCS, L_over_xi, Delta_0_GL`) and depicts a 32-cell Voronoi tessellation of SU(3) plus a 6-branch tight-binding band structure. The S47-era visualization predates the entire post-S47 geometric program: the 4-stratum bottom-20 partition-stability theorem (S87/S88 §VII.AJ), the spectral-moment R-family + R-monotonicity (S64/S73B/S74), the curvature-invariant `R_protected_fold` (S74), the spectral-dimension flow vs CDT (S92), and the §VII cross-pillar bridge geometry (S86/S89). Per context §5, the comprehensive pass is an **aggregate KB-mining survey** (`search_knowledge → trace_entity → get_constant → list_entities`), NOT a linear session read.

W8's gate skeleton is the context-§4 `SURVEY → EXPAND → VERIFY` architecture, specialized for the viz artifact:

- **`WX-W8-1` AGGREGATE-DOMAIN-SURVEY (AUDIT)** — the comprehensiveness ENGINE. Map the SU(3) Jensen crystal-geometry DOMAIN against the whole KB: the 16 constants' current state AND post-S47 geometric results warranting NEW figures. Output: a state-of-domain map + a GAP analysis (KB-cited), incl. dead-import / stale-import / provenance-gap findings.
- **`WX-W8-2` EXPANSION/UPDATE+RERUN (VERIFY; REAL numerical output)** — the DELIVERABLE. Bring the script + depicted geometry to current understanding, ADD figures for the post-S47 results G1 deems warranted (≥ 3 new figures from the candidate slate), fix the QA-layer drifts, then re-execute via the GPU venv → regenerate the existing PNGs AND emit the new ones.
- **`WX-W8-3` ARCHIVE-MIGRATION (AUDIT)** — comprehensively migrate the archived source doc's still-live content forward (resolve the §7.3-pointer issue D6), decide re-sourcing, flag orphaned content.

This wave **splits** into a script+geometry+rerun sub-wave (W8a = `WX-W8-1` + `WX-W8-2`) and an archive-migration sub-wave (W8b = `WX-W8-3`), per the context §7 W8 seed split directive.

### Planner aggregate light-recon (2026-05-25, KB-verified at plan-freeze; the FULL survey + expansion is the executor's gated work)

**(A) QA-LAYER drift exemplars** — pre-identified discrepancies the G1 survey enumerates and G2 fixes ALONG THE WAY (these are the QA sub-layer, NOT the deliverable):

| # | Locus | Finding | KB query | Candidate verdict |
|:-:|:------|:--------|:---------|:------------------|
| D1 | script line 528 `tau_bump = 0.2015`; vis5 title "Speed Bump at tau = 0.2015" | `tau_fold = 0.19` canonical (S12/S42, **NOT superseded**); `0.2015` is the BCS speed-bump location (archive §6, S53 W3-7), **structurally DISTINCT** from the transit fold. vis5 already co-plots both (green dotted = fold 0.19 via imported `tau_fold`; gold dashed = bump 0.2015 hardcoded). | `get_constant("tau_fold")` → 0.19, Superseded=False | CURRENT-WITH-DISAMBIGUATION (do NOT find-replace 0.2015→0.19; context §2 cautionary quartet) |
| D2 | script line 185 Vis-1 label `J_{u(1)} = 0.038`; in-script comment + archive line 53/311 `J_u1 = 0.029` | SCRIPT label string matches canonical; the ARCHIVE doc table (§1, §9) is STALE at 0.029. Note: script `import` pulls `J_u1=0.038`, so the Vis-1/Vis-7 plotted `J_C2/J_u1` ratio uses 0.038 — but the legend label literal and archive prose say 0.029. | `get_constant("J_u1")` → 0.038, no PROVENANCE | script value CURRENT; archive STALE (→ W8-3 migration) |
| D3 | script line 76-77 `BRANCHES['Higgs-2']['omega0']=1.456`, `['Higgs-3']['omega0']=10.37` (hardcoded); imported `omega_H2`, `omega_H3` NEVER consumed | `omega_H2 = 1.41`, `omega_H3 = 11.465` canonical; the `BRANCHES` dict hardcodes 1.456 / 10.37 and the imported `omega_H2/omega_H3` are **dead imports**. Decide: are 1.456/10.37 distinct band-centers (S52 GL extrapolation) vs canonical 1.41/11.465 (later refinement)? | `get_constant("omega_H2")`→1.41; `get_constant("omega_H3")`→11.465 | STALE-OR-DISAMBIGUATE: reconcile BRANCHES to canonical OR document the distinct-provenance |
| D4 | script `gap_freqs` dict (lines 253-258) reads imported `omega_L1=0.138`, `omega_L2=0.192`; archive §9 lists `omega_L1=0.070`, `omega_L2=0.107` (S48 LEGGETT-MODE-48, 3-band) | **Naming collision**: the imported `omega_L1/L2` (0.138/0.192) are the S52 GL Leggett-band Γ-point gaps; the archive §9 `omega_L1/L2` (0.070/0.107) are the S48 3-band Leggett frequencies — a DIFFERENT quantity sharing a symbol. KB confirms both: `omega_L2 = 0.137398` (S52 dispersion) vs `omega_L0 = 0.070-0.138` (S56 model-dependent). | `get_constant("omega_L1")`→0.138; archive §9 cross-read | DISAMBIGUATE (two distinct Leggett observables; tag each by provenance) |
| D5 | `Delta_0_GL` imported (line 21); never referenced in script body | dead import; canonical note: "GL order parameter amplitude, NOT the BCS excitation gap". | `get_constant("Delta_0_GL")`→0.7704, Superseded=False | CURRENT value, UNUSED-IMPORT (hygiene) |
| D6 | live successor doc `Phononic-Substrate-Geometry.md` header: "Supersedes Phononic-Crystal-Geometry.md ... subsumed as §7.3"; that §7.3 actual title = "R-Protection as K-Pairing Class" | pointer mismatch: the supersession claim points at §7.3, but §7.3 carries a spectral-functional theorem, not the 32-cell / tight-binding crystal content. The crystal geometry may be ORPHANED in the migration. | `Grep("§7.3"|"7\\.3", Phononic-Substrate-Geometry.md)` | ARCHIVE-MIGRATION finding: supersession-target mis-pointed OR crystal content orphaned (→ W8-3) |
| D7 | 8 of 16 imports (`c_fabric, c_Gold, J_C2, J_su2, J_u1, L_over_xi, N_e_classical, omega_H2, omega_H3`) return "No PROVENANCE entry" | values EXIST and are correct, but lack `canonical_constants.py` PROVENANCE dict entries → `substrate-first-canonical-sourcing.md` flag. | `get_constant(...)` each | CURRENT value, PROVENANCE-GAP (advisory; note in G1, do not block) |
| D8 | R sign convention | archive §1/§9 `R(fold) = +2.018` (Koszul sectional-curvature magnitude); S61 `R_K(fold) = −2.018` (signed scalar); S53 `R_K(0) = 4.0` (bi-invariant max). Three sign/normalization conventions for the same fold curvature. | `search_knowledge("R fold 2.018 Jensen")` | DISAMBIGUATE (pin the convention used in any new curvature figure) |

**(B) EXPANSION candidate slate** — post-S47 geometric results warranting NEW figures (the DELIVERABLE; G1 confirms each via KB, G2 adds ≥ 3 of these as figures Vis-8…Vis-N):

| Cand | Post-S47 geometric result | KB citation | Why it warrants a figure |
|:----:|:--------------------------|:------------|:-------------------------|
| **E1** | **4-stratum bottom-20 partition stability** (N₁,N₂,N₃,N₄) = **(2,4,8,6)** at τ_fold=0.190, with τ-asymmetric breakdown: δ_τ,crit-neg = −0.0750 (anticrossing-swap → (4,2,8,6)), δ_τ,crit-pos = +0.175 (stratum-coalescence); 2.33× neg/pos asymmetry | §VII.AJ.partition-stability (atlas-07; S87 W11-2 `STABILITY-4`; S88 W2-6); `S87-VII-AJ-PARTITION-STABILITY-LANDING` PASS; Friedrich-Bär saturation theorem | A NEW geometric portrait: the Peter-Weyl bottom-20 spectrum as a 4-stratum bar/partition figure + the τ-asymmetric breakdown geometry (a moduli-deformation Level-2 substrate-IS observable). This is the single biggest post-S47 geometry result the figures never depicted. |
| **E2** | **Spectral-moment R-family + R-monotonicity**: `R_protected_fold = 1.1287 = a_0·a_4/a_2²` at τ_fold; dR/dτ ≥ 0 (R-monotonicity, S64 W1-A, closes CC Path C); the R-family {R₁,R₂,R₃} dimensionless ratios | `R_protected_fold` (S73B/S74, R-PROTECTED, Superseded=False); R-monotonicity theorem (constraint-mega-matrix S64); `s74_r_family_stability` | A NEW figure: the spectral-action moment landscape a_n(τ) and the protected dimensionless ratio R₁(τ) across the Jensen line — connects the crystal's curvature anatomy (§7 of the archive) to the spectral action, which the S47 figures omit entirely. |
| **E3** | **Spectral-dimension flow** d_s(σ) = −2 d ln P(σ)/d ln σ on the Jensen-deformed SU(3) Dirac spectrum, P(σ)=Σ dim(p,q)Σ_i e^{−σλ_i²}; fold window σ_*≈1.4005 M_KK⁻²; UV d_s→8, IR flow vs CDT 4→2 | S92 ad-hoc `s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md`; `d_s(σ) = −2 dlnP/dlnσ`; same-functional-different-scale fair-comparison rule | A NEW figure: d_s(σ) heat-trace flow — directly visualizes the internal geometry's dimensional flow, a flagship S92 cross-framework (CDT/asymptotic-safety) result with NO prior figure. |
| **E4** | **§VII cross-pillar bridge geometry**: R_universal = ⟨[φ_g^sym],[Ch(P₀(τ_fold))]⟩ (Hochschild cocycle × Chern character); R_canonical = 7.3250 (cocycle-norm ratio φ_67/φ_88); the SU(3) finite spectral triple (A_K, H_K, D_K) | §VII.W (first cross-pillar bridge); `s86-hp1-cohomology-quantum-metric-bridge`; `s89-w2-r-canonical-observable-identity` (R_canonical=7.324974) | A NEW figure: the bridge-geometry anatomy (substrate-IS Hochschild pairing → HKR → laboratory-IN quantum-metric trace), the framework's flagship S86-S93 geometric program, absent from the S47 crystal picture. |

The depicted **core geometry is structurally CURRENT** and must be PRESERVED (expansion is additive): 32-cell Voronoi (`N_cells = 32`, Superseded=False, S42 `GIANT-VORONOI`); 6 tight-binding branches + the `A_latt = C³²` lattice spectral triple (S53); `c_fabric/c_Gold = 229.5` (S53 P5 PERMANENT, `proven_1157`); `N_pair = 1` (S53 PERMANENT). The Jensen block scaling `(L₁,L₂,L₃) = (e^{2τ}, e^{−2τ}, e^{τ})` with volume identity `(2,−2,1)·(1,3,4) = 0` is exact to machine epsilon (archive §1; S12/S53 P6; Sage-verified at plan-freeze) — the geometric ratio one substitution chain pins. The `c_fabric/c_Gold = 229.479` → 2.718 acoustic e-folds (d=3+1, exp 1/2) is the second chain; the 8D BLV exponent (1/7·ln(229.48) = 0.777) is the archive §8.2 open question that the expansion should fold in as a current-state caveat.

## Wave 8 Decision Point Prerequisites

**NONE.** W8 is independent of W1–W7 (each wave comprehensively expands a distinct document against the KB; no cross-wave verdict gates any W8 item). The only session-level dependency is downstream: W9 (`gen-physicist` cross-document closeout) consumes the W8 verdicts. No upstream prereq → no mechanical-closure path is anticipated for W8 at dispatch per `.claude/rules/mechanical-closure-discipline.md`. The executor's FIRST action per gate is the KB-mining query set (context §5), recorded in the WP **MCP Pre-Compute Audit** block (mandatory per `workingpaper.md` Rule 3).

---

## §W8-1. WX-W8-1 — AGGREGATE-DOMAIN-SURVEY (SU(3) Jensen crystal-geometry domain vs whole KB)

```yaml
# ---- Identity (4 fields) ----
gate_id: "WX-W8-1-AGGREGATE-DOMAIN-SURVEY"
schema_version: "R3"
trigger: "[AUDIT]"
classification: "GEOMETRIC"
agent_type: "baptista-spacetime-analyst"
hypothesis: >
  The SU(3) Jensen crystal-geometry DOMAIN, surveyed across the whole knowledge base (S47→S93),
  contains substantially MORE current geometric content than the S47-era visualization depicts:
  (a) each of the 16 canonical_constants names imported by Phononic-crystal-geometry_viz.py
  resolves to a current value with a CURRENT/STALE/SUPERSEDED/DEAD-IMPORT/PROVENANCE-GAP verdict, AND
  (b) the GAP between what the project now knows about SU(3) Jensen geometry and what the script/figures
  cover is enumerable as a KB-cited candidate slate of post-S47 geometric results (4-stratum partition
  stability, R-family/R-monotonicity, spectral-dimension flow, cross-pillar bridge geometry, and any
  further results the survey finds) — each gap row with its KB citation and a one-line "where it belongs
  as a figure / script section."

method:
  description: >
    Aggregate WHOLE-DOMAIN KB survey (context §5), NOT a claim-by-claim audit. THREE passes:
    (1) CONSTANT-STATE pass — for each of the 16 imported names run get_constant(name): record value,
        Superseded flag, PROVENANCE presence, and compare to the value the script DISPLAYS/HARDCODES
        (Vis-1 J_u1 label=0.038; BRANCHES Higgs-2=1.456 / Higgs-3=10.37 vs imported omega_H2/omega_H3;
        gap_freqs omega_L1=0.138/omega_L2=0.192 vs archive-§9 0.070/0.107; in-script EJ_EC=0.818, Gi=0.506,
        N_e_total=2.8913, THRESHOLD=3.1, GAP=0.21, N_e_sound=0.5*ln(c_ratio)). Classify each import:
        CURRENT / STALE / SUPERSEDED / DEAD-IMPORT (imported-but-unconsumed) / PROVENANCE-GAP.
    (2) DEPICTED-GEOMETRY pass — search_knowledge + trace_entity to confirm the CURRENT status of every
        depicted structure: 32-cell Voronoi (|W(SU(3))|=6 / Z_3 / torus-tessellation origin), 6 tight-binding
        branches (1 Goldstone + 2 Leggett + 3 Higgs), the J_C2:J_su2:J_u1 = 4:3:1 bond hierarchy, the
        c_fabric/c_Gold=229.5 acoustic hierarchy + 2.89 e-fold budget, N_pair=1, the Mott regime, the
        BCS speed bump, the curvature anatomy (archive §7). Each → latest non-superseded canonical /
        permanent theorem / closed mechanism, with the entity cited.
    (3) DOMAIN-GAP pass (the heavy, comprehensiveness pass) — sweep the SU(3) Jensen geometry DOMAIN for
        post-S47 results the figures NEVER depicted. Required query families (expect tens of queries):
          search_knowledge("4-stratum partition stability bottom-20 cardinality (2,4,8,6)")
          search_knowledge("R-monotonicity dR/dtau spectral moment a_2 a_4 R_protected_fold")
          search_knowledge("spectral dimension flow d_s diffusion CDT Jensen SU(3)")
          search_knowledge("cross-pillar bridge Hochschild Chern character quantum metric SU(3)")
          search_knowledge("Peter-Weyl block-diagonal D_K eigenvalue spectrum tau_fold")
          search_knowledge("Jensen TT-deformation moduli stability anticrossing stratum")
          trace_entity("curvature anatomy"); trace_entity("partition stability"); trace_entity("R-monotonicity")
          list_entities("theorems"); list_entities("closed"); list_entities("gates")  # filter to geometry domain
          get_constant("R_protected_fold"); get_constant("tau_fold"); plus any new constants the survey surfaces
    OUTPUT: (a) state-of-domain map (constant-state table + depicted-geometry status table); (b) GAP ANALYSIS —
    a candidate slate of post-S47 geometric results to ADD as figures, each row {result, KB entity/citation,
    where-it-belongs (Vis-N / script section)}, plus the dead-import/stale/provenance-gap ledger from passes
    (1)-(2). The closure script formalizes the dual-SHA verdict over the survey + gap artifacts + canonical
    snapshot; the survey + gap analysis is the agent's KB-mining by hand, recorded in the WP.
  producing_script: "computations/session-x/sx_w8_aggregate_domain_survey.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator — domain-coverage + gap set
operator:
  type: "set"
  form: >
    PASS iff (constant_state_verdict(name) ∈ {CURRENT,STALE,SUPERSEDED,DEAD-IMPORT,PROVENANCE-GAP} ∀ 16 names)
    AND (depicted_geometry_status enumerated for all core structures w/ KB entity)
    AND (gap_slate = {post-S47 geometric results NOT covered} enumerated, |gap_slate| ≥ 4, each row KB-cited).
    Coverage-by-enumeration: the survey covers the domain's pertinent entity classes (constants, theorems,
    closed, gates, sessions) AND the gap analysis is enumerated with citations.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    16/16 imported constants assigned a state-verdict with KB query; ALL core depicted structures
    assigned a CURRENT/STALE/SUPERSEDED status with cited entity; gap_slate non-empty with ≥ 4
    KB-cited candidate post-S47 figures (the E1-E4 slate is the floor, not the ceiling — the survey
    finds the rest). FAIL if the survey only re-checks the script's existing claims (no gap_slate).
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (context §4 R3 mapping: G1 → type:set domain-coverage + gap set)"

# (4) reachable_rationals — synthesis/survey gate, no figure output
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — aggregate-domain-survey gate (no numerical figure output; the survey + gap analysis is the deliverable)"

# (5) machinery_pin_map — KB tools + entity classes + the 16 constant names + snapshot paths
machinery_pin_map:
  # 16 imported constant names surveyed (the script's import list):
  constants_surveyed: "[tau_fold, c_fabric, c_Gold, J_C2, J_su2, J_u1, N_cells, E_cond, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3, N_e_classical, xi_BCS, L_over_xi, Delta_0_GL]"
  kb_tools: "[mcp__knowledge__get_constant, search_knowledge, trace_entity, list_entities, query_entity]"
  entity_classes_surveyed: "[constants, theorems, closed, gates, sessions, open]"
  domain_scope_definition: "SU(3) Jensen crystal geometry: left-invariant metric blocks (e^{2tau},e^{-2tau},e^{tau}) on su(3)=u(1)+su(2)+C^2; 32-cell Voronoi tessellation; Peter-Weyl D_K spectrum; tight-binding bands; curvature anatomy; spectral-action moments; cross-pillar bridge geometry"
  gap_row_taxonomy: "{result, KB_entity_or_citation, where_it_belongs (Vis-N | script-section | archive-section)}"
  constant_state_taxonomy: "{CURRENT, STALE, SUPERSEDED, DEAD-IMPORT, PROVENANCE-GAP}"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py"
  script_path: "sessions/framework/Phononic-crystal-geometry_viz.py"
  archive_doc_path: "sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md"
  document_sha: "<computed-at-runtime>"
  N_eval: "N/A — survey gate"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A — set-membership verdict, not numerical comparison"
  scheme: "aggregate-domain-survey"
  convention: "KB-cited-gap-enumeration"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — no numerical compute in survey gate"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["sx_w8_aggregate_domain_survey.py", "canonical_constants_snapshot", "state_of_domain_map", "gap_analysis", "kb_query_manifest", "document_pre_sha"]
  content_sha256_inputs: ["state_of_domain_map", "gap_analysis"]

# (7) substitution_chain — Jensen volume-preservation identity + c-ratio (both retained in the survey)
substitution_chain:
  required: true
  content: |
    The survey RETAINS two directional/ratio claims from the depicted geometry; both must carry the chain
    per math-scripts.md §"Double-Check Logic Before Compute".

    CHAIN 1 — Jensen volume preservation (the geometric ratio underpinning "the manifold changes shape, not size"):
      Definition 1: Jensen metric block scales (archive §1; S12): L_1 = e^{2*tau} (u(1), 1 dir),
                    L_2 = e^{-2*tau} (su(2), 3 dirs), L_3 = e^{tau} (C^2 coset, 4 dirs).
      Definition 2: det(g_tau) = L_1^{m1} * L_2^{m2} * L_3^{m3} with multiplicities (m1,m2,m3) = (1,3,4).
      Substitute:   det(g_tau) = (e^{2tau})^1 * (e^{-2tau})^3 * (e^{tau})^4 = e^{(2*1 + (-2)*3 + 1*4)*tau}.
      Simplify:     exponent = (2,-2,1) . (1,3,4) = 2 - 6 + 4 = 0.    [Sage-verified at plan-freeze: = 0 exact]
                    det(g_tau) = e^{0*tau} = e^0 = 1.
      Canonical form: det(g_tau) = 1 for all tau.
      Direction:    volume is tau-INDEPENDENT (constant, not increasing/decreasing).
      Conclusion:   the internal manifold changes SHAPE at fixed VOLUME — exflation is geometric shape change,
                    not KK volume transfer (archive §6 "Jensen Volume Preservation"). The survey verifies this
                    claim is CURRENT (S12/S53 P6, machine-epsilon; PROVEN "Volume-preserving TT", registry).

    CHAIN 2 — sound-speed hierarchy → acoustic e-folds (the central acoustic fact; survey verifies CURRENT + flags 8D caveat):
      Definition 1: c_fabric = 209.97368021 M_KK (canonical_constants; spectral-action gradient, S42).
      Definition 2: c_Gold   = 0.915 M_KK (canonical_constants; Goldstone band group velocity, S52).
      Definition 3: N_e^sound = (1/2) * ln(c_fabric / c_Gold)   [3+1D BLV exponent, archive §6; S53 W0-1].
      Substitute:   c_fabric / c_Gold = 209.97368021 / 0.915 = 229.479...    [Sage-verified: 229.479431923497]
      Simplify:     N_e^sound = (1/2) * ln(229.479) = (1/2) * 5.435813 = 2.7179...
      Canonical form: N_e^sound(d=3+1) = 2.718 e-folds; total N_e = 2.718 + 0.1734 (geom) = 2.891.
      Direction:    the substrate vibrates 229x FASTER than the pair hops (ratio >> 1).
      Conclusion:   2.718 acoustic e-folds (dominant over the 0.173 geometric ceiling by 15.7x). The survey
                    flags the §8.2 OPEN caveat: the 8D BLV exponent 1/7 gives (1/7)*ln(229.48) = 0.777
                    [Sage-verified], so the d-dependence of the conformal exponent is an unresolved current-state
                    nuance the expansion must fold in (NOT silently retain the 3+1D number as settled).

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  viz_script:
    path: "sessions/framework/Phononic-crystal-geometry_viz.py"
    sha256: "<computed-at-runtime>"
  archive_doc:
    path: "sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md"
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w8_aggregate_domain_survey.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w8_aggregate_domain_survey.npz"
    artifact_kind: "data"
    optional: true                       # survey gate: gap/state artifacts live in the WP; npz optional
  plot:
    path: "computations/session-x/sx_w8_aggregate_domain_survey.png"
    artifact_kind: "plot"
    optional: true                       # no figure output from the survey gate
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W8-1-AGGREGATE-DOMAIN-SURVEY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w8-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W8-1. WX-W8-1-AGGREGATE-DOMAIN-SURVEY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The SU(3) Jensen crystal-geometry domain is comprehensively mapped: 16/16 imports state-verdicted,
  all core depicted structures status-tagged with KB entities, AND a ≥4-row KB-cited gap slate of
  post-S47 geometric results enumerated for figure-addition in G2. The comprehensiveness engine has run.
FAIL_meaning: >
  The survey only re-checked the script's existing claims (no gap slate) OR left imports/structures
  unverified. This is the context-§4 G1 failure signature ("FAILED if it only audits existing claims").
INFO_meaning: >
  Survey complete but a gap row is UNVERIFIABLE (KB entity ambiguous) OR a constant's state is
  genuinely ambiguous (e.g., the omega_L1/L2 naming collision needs a convention decision in G2).

# ---- Effort + framing ----
effort:
  files_created: ["computations/session-x/sx_w8_aggregate_domain_survey.py", "computations/session-x/sx_w8_aggregate_domain_survey.npz (optional)"]
  estimated_time: "0.5 day (the heavy KB-mining survey + gap enumeration is the bulk; closure script is mechanical)"

substrate_framing: |
  GEOMETRIC gate. The survey maps the substrate's geometry — D_K eigenvalues on Jensen-deformed SU(3),
  their Peter-Weyl decomposition, the curvature anatomy, the spectral-action moments — against the whole
  KB. Direction of explanation per phononic-framing.md: the substrate IS the spectral triple (A_K, H_K, D_K);
  the 32-cell tessellation and the tight-binding bands are how the substrate's spectral weight organizes,
  NOT structures IN a container. The gap slate (4-stratum partition, R-family, d_s flow, bridge geometry)
  is the post-S47 deepening of that same substrate geometry — additive synthesis, not a new container.
```

---

## §W8-2. WX-W8-2 — COMPREHENSIVE-EXPANSION + UPDATE + RERUN (script to current geometry; ADD figures; regenerate via GPU venv)

```yaml
# ---- Identity (4 fields) ----
gate_id: "WX-W8-2-COMPREHENSIVE-EXPANSION-UPDATE-RERUN"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "GEOMETRIC"
agent_type: "baptista-spacetime-analyst"
hypothesis: >
  After comprehensively expanding Phononic-crystal-geometry_viz.py to integrate the G1 gap — bringing the
  depicted 32-cell Voronoi + tight-binding geometry to current (S93-era) understanding, fixing every
  QA-layer drift (D1-D8), AND adding ≥ 3 NEW figures (Vis-8…Vis-N) for post-S47 geometric results from the
  G1 candidate slate (E1 4-stratum partition stability; E2 R-family/R-monotonicity; E3 spectral-dimension
  flow; E4 cross-pillar bridge geometry) — the script re-executes cleanly through the GPU venv and emits
  ALL figures (the original set, brought current, PLUS the new ones), with every material G1 gap row
  integrated OR explicitly scoped-out with a one-line reason.

method:
  description: >
    The DELIVERABLE gate (context §4 G2). FOUR steps:
    (1) EXPAND the depicted geometry to current understanding: bring the existing 7 figures' annotations,
        constants, and captions to the current canonical (consume the imported omega_H2/omega_H3 instead of
        the hardcoded BRANCHES literals OR document the distinct-provenance per D3; disambiguate the
        omega_L1/L2 naming collision per D4; pin the R sign convention per D8; co-plot the d=8 BLV exponent
        caveat in the e-fold figure per §8.2). PRESERVE the structurally-current core (32-cell Voronoi,
        N_pair=1, 229.5 hierarchy) and the authorial voice.
    (2) ADD ≥ 3 NEW figures for the G1-confirmed post-S47 geometric results. Default mapping (G1 may refine):
          Vis-8  = E1 4-stratum bottom-20 partition (2,4,8,6) at tau_fold + tau-asymmetric breakdown geometry
                   (delta_neg=-0.0750 anticrossing-swap, delta_pos=+0.175 stratum-coalescence).
          Vis-9  = E2 spectral-moment landscape a_n(tau) + protected ratio R_1(tau) = a_0*a_4/a_2^2 (R_protected_fold=1.1287)
                   with the R-monotonicity dR/dtau >= 0 annotation.
          Vis-10 = E3 spectral-dimension flow d_s(sigma) = -2 dlnP/dlnsigma on the Jensen D_K spectrum
                   (UV d_s->8, fold window sigma_*≈1.4005), vs the CDT 4->2 reference (same-functional-different-scale
                   fair-comparison per phononic-framing.md AH-PF-1).
          (Vis-11 = E4 cross-pillar bridge-geometry anatomy — ADD if G1 deems it figure-warranted within effort.)
        New-figure data: use the GPU venv torch.linalg for any D_K spectrum recomputation (Peter-Weyl
        block-diagonal, fits in VRAM per math-scripts.md D_K block-diagonality pre-check); cite the source
        canonical values (partition cardinality (2,4,8,6); R_protected_fold; d_s functional) from the KB —
        do NOT re-derive closed results, VISUALIZE them (substrate-first sourcing).
    (3) RE-EXECUTE the script through the GPU venv:
          "phonon-exflation-sim/.venv312/Scripts/python.exe" sessions/framework/Phononic-crystal-geometry_viz.py
        Verify it runs to completion and writes Phononic-Crystal-Geometry-Vis-{1..N}.png (N = 7 + #new).
    (4) The closure script (computations/session-x/sx_w8_expansion_update_rerun.py) records the dual-SHA
        verdict over the pre/post script SHA + the regenerated+new PNG set + the integrated/scoped-out gap
        ledger; it loads canonical_constants, asserts the post-script imports resolve, asserts every promised
        PNG exists on disk with non-zero size, and append_verdict's. The intellectual work (the expansion
        writing + new-figure design) is the agent's, recorded in the WP + the expanded script itself.
  producing_script: "computations/session-x/sx_w8_expansion_update_rerun.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator — gap-integration set: integrated ∪ scoped-out = all material gaps; AND all promised PNGs exist
operator:
  type: "set"
  form: >
    PASS iff (integrated_gaps ∪ scoped_out_gaps = G1_material_gap_slate)
    AND (#new_figures >= 3 from {E1,E2,E3,E4})
    AND (∀ promised PNG p: exists(p) ∧ size(p) > 0)
    AND (script re-executes via GPU venv with exit 0)
    AND (every QA-layer drift D1-D8 resolved: fixed | disambiguated | scoped-out-with-reason).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    Every material G1 gap row integrated OR scoped-out (one-line reason); >= 3 NEW figures added and emitted;
    all (7 + #new) PNGs present on disk with size > 0; script exit code 0 under the GPU venv. A cosmetic /
    minimal edit (e.g., only fixing D2 and re-running with no new figures) FAILS this gate (context §4 G2:
    "a cosmetic/minimal edit FAILS this gate").
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (gap-integration set) + artifact-existence (PNG outputs) — context §4 R3 mapping G2 → type:set gap-integration"

# (4) reachable_rationals — REAL figure output (the W8 RERUN exception per context §4 + §7 W8 seed)
reachable_rationals:
  includes_integer_mesh: true
  mesh_density: "<#figures>"             # = 7 (regenerated current) + #new (>= 3) = >= 10 publication figures; pin the exact integer at expansion-freeze

# (5) machinery_pin_map — 16 constant names + script path + venv python + new-figure data params
machinery_pin_map:
  constants_consumed: "[tau_fold, c_fabric, c_Gold, J_C2, J_su2, J_u1, N_cells, E_cond, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3, N_e_classical, xi_BCS, L_over_xi, Delta_0_GL]"
  new_figure_canonical_inputs: "[partition_cardinality=(2,4,8,6), delta_tau_crit_neg=-0.0750, delta_tau_crit_pos=+0.175, R_protected_fold=1.1287, d_s_fold_window_sigma=1.4005, R_canonical_bridge=7.3250]"
  script_path: "sessions/framework/Phononic-crystal-geometry_viz.py"
  GPU_path: "phonon-exflation-sim/.venv312/Scripts/python.exe"   # PINNED venv python per computation-environment.md (W8 RERUN exception)
  torch_linalg_for_DK: "true — Peter-Weyl block-diagonal D_K eigvals on GPU (torch.linalg.eigvals; fits VRAM per math-scripts.md D_K block-diagonality pre-check)"
  png_naming: "Phononic-Crystal-Geometry-Vis-{n}.png"
  png_count_expected: "<7 + #new; pin exact integer at expansion-freeze>"
  matplotlib_backend: "Agg (non-interactive; per script line 26)"
  figure_dpi: "200 (per script rcParams)"
  N_eval: "N/A — figure regeneration, not a numerical scan"
  L_max: "10 (D_K spectrum truncation for any new spectral figure; per master cache; or 6 for partition cardinality per S87 W11-2 Casimir-bound)"
  scan_range: "tau in [0.01, 0.35] for R-family/curvature figures (archive vis5 range); sigma in [1e-2, 1e2] for d_s flow"
  step_size: "500 points (matching script K/tau linspace density) or adaptive for d_s log-grid"
  tolerance: "PNG existence + size > 0 (artifact-existence); script exit 0"
  scheme: "comprehensive-expansion-update-rerun"
  convention: "additive-synthesis-preserve-voice; substrate-first new-figure sourcing"
  random_seed: "42 (existing Vis-1 RandomState; preserve for reproducibility of the BCC node layout)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["sx_w8_expansion_update_rerun.py", "canonical_constants_snapshot", "viz_script_pre_sha", "gap_integration_ledger", "new_figure_canonical_inputs", "g1_gap_slate"]
  content_sha256_inputs: ["viz_script_post_sha", "png_manifest (names + sizes)"]

# (7) substitution_chain — the two retained ratio claims, now carried into the EXPANDED script's figures
substitution_chain:
  required: true
  content: |
    The expanded script RETAINS and now figure-annotates the same two directional/ratio claims; both carry
    the chain (identical to W8-1 CHAIN 1 + CHAIN 2; re-stated here because the EXPANSION is where the values
    get re-plotted, so the direction read-off must be re-verified against the post-edit annotations).

    CHAIN 1 — Jensen volume preservation (vis annotations + any new curvature figure):
      Definition 1: L_1=e^{2tau} (u(1)), L_2=e^{-2tau} (su(2)), L_3=e^{tau} (C^2); mults (1,3,4).
      Substitute:   det(g_tau) = e^{(2,-2,1).(1,3,4) * tau} = e^{(2-6+4)*tau} = e^{0} = 1.   [Sage: exponent = 0 exact]
      Direction:    volume tau-INDEPENDENT.
      Conclusion:   shape-change-at-fixed-volume; any new curvature figure (E2) MUST preserve this (the a_n(tau)
                    landscape varies while det g = 1 — the spectral moments move, the volume does not).

    CHAIN 2 — c_fabric/c_Gold ratio → e-fold annotation (vis3 + vis6, brought current with the 8D caveat):
      Definition 1: c_fabric = 209.97368021 (canonical); c_Gold = 0.915 (canonical).
      Substitute:   ratio = 209.97368021 / 0.915 = 229.479.   [Sage: 229.479431923497]
      Simplify:     N_e^sound(3+1) = 0.5*ln(229.479) = 2.718; N_e^sound(8D) = (1/7)*ln(229.479) = 0.777.  [Sage-verified both]
      Direction:    ratio >> 1 (substrate faster than pair); but the e-fold COUNT direction depends on the BLV
                    exponent (1/2 vs 1/7) — the d=8 value is 3.5x SMALLER than the 3+1D value.
      Conclusion:   vis3/vis6 must annotate BOTH the 3+1D (2.718) and the 8D-caveat (0.777) values; the prior
                    figures showed only the 3+1D number as if settled (archive §8.2 flags this OPEN). Bringing
                    the figure current = showing the exponent ambiguity, not silently retaining 2.718.

# (8) input_files
input_files:
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"
  viz_script:
    path: "sessions/framework/Phononic-crystal-geometry_viz.py"
    sha256: "<computed-at-runtime>"
  archive_doc:
    path: "sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md"
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w8_expansion_update_rerun.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w8_expansion_update_rerun.npz"
    artifact_kind: "data"
    optional: true                       # closure script records png manifest; npz optional
  plot:
    # The PRIMARY figure outputs live at the script's own OUT_DIR (sessions/framework/), NOT computations/session-x/.
    # These are the regenerated + new PNGs — NON-OPTIONAL per context §7 W8 seed ("the PNG outputs are optional: false").
    path: "sessions/framework/Phononic-Crystal-Geometry-Vis-8.png"
    artifact_kind: "plot"
    optional: false                      # the FIRST new figure is mandatory; the closure script verifies all (7 + #new)
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W8-2-COMPREHENSIVE-EXPANSION-UPDATE-RERUN:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w8-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W8-2. WX-W8-2-COMPREHENSIVE-EXPANSION-UPDATE-RERUN"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The visualization is comprehensively expanded to current SU(3) Jensen geometry: all material G1 gaps
  integrated/scoped, >= 3 new figures (post-S47 results) added and emitted alongside the regenerated current
  originals, every QA drift fixed/disambiguated, script exits 0 under the GPU venv. The figures now read as
  a current (S93-era) comprehensive depiction of the crystal geometry.
FAIL_meaning: >
  Cosmetic/minimal edit (no new figures, or < 3) OR a promised PNG missing/zero-size OR script crash under
  the GPU venv OR a material gap silently dropped (neither integrated nor scoped-out). Closes the corridor
  "the S47 figures can be brought current by drift-fixing alone" — they cannot; expansion is required.
INFO_meaning: >
  Expansion landed with >= 3 new figures but one candidate (e.g., E4 bridge geometry) was scoped-out with a
  documented reason (effort/figure-warrant), OR a new-figure data recomputation hit a regime caveat (e.g.,
  d_s flow window sensitivity) recorded as a figure annotation.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w8_expansion_update_rerun.py"
    - "sessions/framework/Phononic-crystal-geometry_viz.py (EXPANDED in place — script edit, not new file)"
    - "sessions/framework/Phononic-Crystal-Geometry-Vis-{1..7}.png (regenerated current)"
    - "sessions/framework/Phononic-Crystal-Geometry-Vis-{8..N}.png (NEW: >= 3 post-S47-result figures)"
  estimated_time: "1.0-1.5 days (the figure-design + expansion writing for >= 3 new geometric figures + bringing 7 current is the bulk; rerun + closure is fast)"

substrate_framing: |
  GEOMETRIC gate with REAL figure output. The expansion deepens the depiction of the substrate's geometry.
  Direction per phononic-framing.md: D_K eigenvalues on Jensen-deformed SU(3) -> Peter-Weyl decomposition ->
  the bottom-20 4-stratum partition (E1) / the spectral-action moments a_n(tau) (E2) / the spectral-dimension
  flow d_s(sigma) (E3) / the cross-pillar bridge pairing (E4). Every new figure VISUALIZES a closed/permanent
  substrate-IS result (the cardinality vector, R_protected_fold, the d_s functional, R_canonical) — substrate-
  first sourcing: visualize what the KB already proved, do NOT re-derive. The core S47 crystal picture
  (32-cell Voronoi, N_pair=1, 229.5 hierarchy) is the substrate's spectral-weight organization, preserved and
  brought current; the new figures are the post-S47 deepening of that SAME geometry, additive in the doc's voice.
```

---

## §W8-3. WX-W8-3 — ARCHIVE-MIGRATION (comprehensively migrate the archived source doc's live content forward)

```yaml
# ---- Identity (4 fields) ----
gate_id: "WX-W8-3-ARCHIVE-MIGRATION"
schema_version: "R3"
trigger: "[AUDIT]"
classification: "GEOMETRIC"
agent_type: "baptista-spacetime-analyst"
hypothesis: >
  The archived source document ARCHIVE/Phononic-Crystal-Geometry.md (S47/S53, superseded mid-S86 by
  Phononic-Substrate-Geometry.md) contains STILL-LIVE crystal-geometry content that the supersession did
  NOT fully migrate forward: the §7.3-pointer (D6) is a mis-pointed supersession target (live doc §7.3 =
  "R-Protection as K-Pairing Class", NOT the 32-cell/tight-binding content), and several archive sections
  (the curvature anatomy §7, the 32-cell tessellation §1, the Mott regime §5, the acoustic-cosmology §6,
  the open-questions §8) are either orphaned, partially migrated, or superseded — each assignable a
  MIGRATE-FORWARD / ALREADY-MIGRATED / ORPHANED / SUPERSEDED / RE-SOURCE verdict with a destination.

method:
  description: >
    AUDIT gate over the archived doc, resolving its migration status comprehensively (context §7 W8 seed:
    "comprehensively migrate the archived source doc forward (resolve the §7.3-pointer issue)"). FOUR steps:
    (1) RESOLVE D6 — Grep Phononic-Substrate-Geometry.md for the §7.3 reference and its actual §7.3 title;
        confirm the supersession header's "subsumed as §7.3" claim against the live §7.3 content. Determine
        whether the 32-cell/tight-binding crystal content is (a) migrated elsewhere in the live doc, (b)
        orphaned (no live home), or (c) intentionally dropped (superseded framing per the archive header
        "crystal IN a container" -> "substrate IS the spectral triple").
    (2) SECTION-BY-SECTION migration ledger — for each archive section (§1 crystal picture, §2 quantum walker,
        §3 sound-speed hierarchy, §4 band structure, §5 Mott regime, §6 acoustic cosmology, §7 curvature anatomy,
        §8 open questions, §9 key-numbers, §10 portrait): assign {MIGRATE-FORWARD (live content with no current
        home -> name destination doc/section), ALREADY-MIGRATED (cite live location), ORPHANED (live but homeless),
        SUPERSEDED (framing replaced; cite the replacement), RE-SOURCE (value drift -> cite canonical)}. Use
        search_knowledge/trace_entity + Grep on the live successor doc.
    (3) DECIDE re-sourcing — the archive §9 key-numbers table has the stale J_u1=0.029 (D2), the omega_L1/L2
        naming collision (D4), and the R-sign convention (D8); recommend the canonical re-sourcing for each
        (this informs both the live successor doc AND the expanded viz script's annotations from W8-2).
    (4) The closure script records the dual-SHA verdict over the migration ledger + the D6 resolution; the
        section-by-section migration analysis is the agent's by-hand work, recorded in the WP. NOTE: this gate
        does NOT bulk-edit the archived doc (it is ARCHIVED); it produces the migration ledger + destination
        recommendations. Any live-content migration INTO the successor doc is the W2 owner's (tesla-resonance)
        domain — W8-3 emits the recommendation, flags orphans, and cross-references W2.
  producing_script: "computations/session-x/sx_w8_archive_migration.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator — migration-status set: every archive section assigned a status; PASS = full coverage
operator:
  type: "set"
  form: >
    PASS iff (∀ archive section s ∈ {§1..§10}: migration_status(s) ∈
              {MIGRATE-FORWARD, ALREADY-MIGRATED, ORPHANED, SUPERSEDED, RE-SOURCE} with destination/citation)
    AND (D6 §7.3-pointer resolved: live-§7.3-title confirmed ∧ crystal-content-disposition determined)
    AND (re-sourcing recommended for each stale-value section §9 drift).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    10/10 archive sections status-tagged with destination/citation; D6 resolved (live §7.3 title confirmed +
    crystal-content disposition: migrated-elsewhere | orphaned | intentionally-superseded); re-sourcing pinned
    for the §9 stale values (J_u1, omega_L1/L2, R-sign). FAIL if the §7.3 pointer is left unresolved or any
    section is un-triaged.
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (migration-status set over the 10 archive sections) — context §4 R3 mapping G3 → type:set"

# (4) reachable_rationals — synthesis/audit gate
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — archive-migration audit gate (the migration ledger + D6 resolution is the deliverable; no figure output)"

# (5) machinery_pin_map
machinery_pin_map:
  archive_sections: "[§1 crystal picture, §2 quantum walker, §3 sound-speed, §4 band structure, §5 Mott, §6 acoustic cosmology, §7 curvature anatomy, §8 open questions, §9 key numbers, §10 portrait]"
  migration_status_taxonomy: "{MIGRATE-FORWARD, ALREADY-MIGRATED, ORPHANED, SUPERSEDED, RE-SOURCE}"
  successor_doc: "sessions/framework/Phononic-Substrate-Geometry.md"
  d6_resolution_tools: "[Grep on successor doc for §7.3, search_knowledge, trace_entity]"
  re_source_targets: "[J_u1 (0.029->0.038), omega_L1/L2 naming-collision (0.070/0.107 S48 vs 0.138/0.192 S52), R-sign (+2.018 Koszul vs -2.018 signed vs 4.0 bi-invariant)]"
  archive_doc_path: "sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py"
  cross_reference_wave: "W2 (tesla-resonance owns Phononic-Substrate-Geometry.md; live-content migration INTO successor is W2's domain)"
  N_eval: "N/A — audit gate"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A — set-membership verdict"
  scheme: "archive-migration-audit"
  convention: "section-status-enumeration"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — no numerical compute"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["sx_w8_archive_migration.py", "archive_doc_sha", "successor_doc_sha", "migration_ledger", "d6_resolution", "canonical_constants_snapshot"]
  content_sha256_inputs: ["migration_ledger", "d6_resolution"]

# (7) substitution_chain — re-sourcing the stale §9 values (the J_u1 + R-sign disambiguation)
substitution_chain:
  required: true
  content: |
    The archive §9 key-numbers table carries the QA-layer drifts; the migration ledger's RE-SOURCE rows
    pin the canonical, which requires the directional/value chain per math-scripts.md.

    CHAIN — J_u1 re-sourcing (archive §1/§9 = 0.029; canonical = 0.038):
      Definition 1: J_u1 = u(1)-direction Josephson coupling (overlap integral of D_K eigenstates between
                    adjacent Voronoi cells along the u(1) generator), archive §1.
      Definition 2: canonical_constants J_u1 = 0.038 (get_constant, no PROVENANCE entry, not superseded).
      Substitute:   archive value 0.029 vs canonical 0.038.
      Simplify:     ratio J_C2/J_u1: archive-table form = 0.933/0.029 = 32.2; canonical form = 0.933/0.038 = 24.6.
      Direction:    the canonical J_u1 (0.038) gives a SMALLER J_C2:J_u1 ratio (24.6 vs 32.2) — the u(1) bond is
                    stronger than the archive states.
      Conclusion:   RE-SOURCE the archive §9 J_u1 to 0.038; the "32:1 ratio" prose in archive §1 ("the 32:1 ratio
                    between J_C2 and J_u1") is itself stale (true ratio ~24.6:1 on canonical). The viz script
                    Vis-1 annotation box (line 211 J_C2/J_u1:.1f) already uses imported 0.038 -> displays ~24.6,
                    so the SCRIPT is current and the ARCHIVE prose is the stale locus. Flag for W2 migration.

    NOTE on R-sign (no single-direction claim — a convention pin, documented not "directional"):
      archive §1/§9 R(fold) = +2.018 is the magnitude of the Koszul sectional-curvature scalar; S61
      R_K(fold) = -2.018 is the signed scalar in the (mostly-plus) convention; S53 R_K(0) = 4.0 is the
      bi-invariant maximum. The migration ledger RE-SOURCE row pins ONE convention (recommend the signed
      S61 form for any forward curvature figure/section, with the magnitude noted) — NOT a directional claim,
      so no >/< read-off; the disambiguation is a convention declaration.

# (8) input_files
input_files:
  archive_doc:
    path: "sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md"
    sha256: "<computed-at-runtime>"
  successor_doc:
    path: "sessions/framework/Phononic-Substrate-Geometry.md"
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
    path: "computations/session-x/sx_w8_archive_migration.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w8_archive_migration.npz"
    artifact_kind: "data"
    optional: true                       # audit gate: migration ledger lives in WP; npz optional
  plot:
    path: "computations/session-x/sx_w8_archive_migration.png"
    artifact_kind: "plot"
    optional: true                       # no figure output from the migration audit
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W8-3-ARCHIVE-MIGRATION:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w8-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W8-3. WX-W8-3-ARCHIVE-MIGRATION"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The archived source doc is comprehensively triaged: 10/10 sections status-tagged with destinations, the
  D6 §7.3-pointer resolved (live §7.3 title confirmed + crystal-content disposition), and the §9 stale values
  re-sourced to canonical. Live content has a forward home (or is documented orphaned/superseded); the
  migration recommendation is ready for the W2 successor-doc owner.
FAIL_meaning: >
  The §7.3 pointer left unresolved OR a section un-triaged OR a stale §9 value un-re-sourced. Closes the
  corridor "the archive supersession was complete" — D6 shows it was not (the supersession target is mis-pointed).
INFO_meaning: >
  Migration ledger complete but a section's disposition is genuinely ambiguous (e.g., the curvature anatomy §7
  is partially migrated to the live doc's §7.3 K-pairing content AND partially orphaned), recorded as a split
  status with both citations.

# ---- Effort + framing ----
effort:
  files_created: ["computations/session-x/sx_w8_archive_migration.py", "computations/session-x/sx_w8_archive_migration.npz (optional)"]
  estimated_time: "0.5 day (the section-by-section migration triage + D6 Grep resolution + re-sourcing is the bulk; closure is mechanical)"

substrate_framing: |
  GEOMETRIC gate. The archive documents the substrate's crystal geometry under the pre-S86 "crystal IN a
  container" framing; the supersession to Phononic-Substrate-Geometry.md is precisely the phononic-framing.md
  IS-not-IN correction ("substrate IS the spectral triple, not a crystal IN a container"). The migration ledger
  preserves the substrate-IS geometric content (curvature anatomy, partition structure, the protected chain
  q_7^2 = K(u(1),C^2) = 1/16) while shedding the container framing. Direction: the migrated content must read
  FROM the substrate (D_K spectrum, Peter-Weyl, curvature invariants) TOWARD emergent physics — the archive's
  §7 protected-invariant theorems (K(u(1),su(2))=0, K(u(1),C^2)=1/16, Ric(u(1))=1/4) are live substrate-IS
  structural results that MUST migrate forward (not be lost in the supersession).
```

---

## Wave 8 → Wave 9 Decision Point

W9 (`gen-physicist` cross-document closeout) consumes the W8 verdicts as one of the 8 expanded-document inputs to its SHARED-CONSTANT-MATRIX + COVERAGE-CONSISTENCY sweep. Branching:

| W8 outcome | W9 consequence |
|:-----------|:---------------|
| `WX-W8-2` PASS (script expanded + ≥3 new figures emitted) | W9 SHARED-CONSTANT-MATRIX includes the W8 viz among the cross-document constant-consistency check: the 16 imports' values (esp. tau_fold=0.19, c_fabric/c_Gold, J-couplings, the new-figure canonical inputs R_protected_fold/(2,4,8,6)/d_s) must agree with the values cited in W1/W2/W3/W4 prose. W9 verifies the expanded figures' annotations match the expanded prose docs. |
| `WX-W8-2` INFO (one candidate scoped-out) | W9 notes the scoped-out figure (e.g., E4 bridge geometry) as a coverage gap; cross-checks whether W2 (`Phononic-Substrate-Geometry.md`, which owns the bridge geometry domain) covers it instead — coverage may be satisfied at the document-set level even if not in the viz. |
| `WX-W8-2` FAIL (cosmetic edit / PNG missing / crash) | W9 flags the W8 viz as NOT brought current; the coverage-consistency sweep records the SU(3) Jensen geometry visualization domain as incomplete; routes a re-dispatch recommendation to next session. |
| `WX-W8-3` MIGRATE-FORWARD/ORPHANED rows | W9 cross-checks that any archive content flagged MIGRATE-FORWARD lands in (or is referenced by) the W2 successor doc `Phononic-Substrate-Geometry.md`; ORPHANED rows become a documented coverage gap for the document set. |

No W8 gate gates another W8 gate's dispatch (W8-1 → W8-2 is a logical dependency — the expansion consumes the survey's gap slate — but both honestly close per their own thresholds; if W8-1 returns FAIL/INFO, W8-2 proceeds using the partial gap slate + the planner light-recon slate E1-E4 as the floor, documenting the degraded input).

---

## Wave 8 Machinery-Enumeration Pin

Aggregate of all three gate `machinery_pin_map` entries (per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR; this is what `_yaml_gate_validator.py` reads for sig_4 of the v3 closure ladder):

- **16 imported canonical constants** (surveyed in W8-1, consumed in W8-2, re-sourced in W8-3): `tau_fold` (0.19, S12/S42, not superseded), `c_fabric` (209.97368021, no PROVENANCE), `c_Gold` (0.915, no PROVENANCE), `J_C2` (0.933, no PROVENANCE), `J_su2` (0.059, no PROVENANCE), `J_u1` (0.038, no PROVENANCE — archive prose stale at 0.029), `N_cells` (32, S42, not superseded), `E_cond` (−0.13685, S36 ED-CONV-36), `omega_L1` (0.138, no PROVENANCE), `omega_L2` (0.192, no PROVENANCE), `omega_H1` (0.38, no PROVENANCE), `omega_H2` (1.41, no PROVENANCE — script hardcodes 1.456), `omega_H3` (11.465, no PROVENANCE — script hardcodes 10.37), `N_e_classical` (0.1734, no PROVENANCE), `xi_BCS` (0.8083, S37), `L_over_xi` (0.031, no PROVENANCE), `Delta_0_GL` (0.7704, S37, dead import).
- **New-figure canonical inputs** (W8-2; substrate-first sourced, visualize-don't-rederive): `partition_cardinality=(2,4,8,6)` (§VII.AJ, S87 W11-2), `delta_tau_crit_neg=−0.0750`, `delta_tau_crit_pos=+0.175` (§VII.AE, S88 W2-9), `R_protected_fold=1.1286545967627695` (S73B/S74, a_0·a_4/a_2²), `d_s_fold_window_sigma≈1.4005 M_KK⁻²` (S92 ad-hoc), `R_canonical_bridge=7.324974378387362` (S89 W2, Hochschild×Chern, optional E4).
- **Script path**: `sessions/framework/Phononic-crystal-geometry_viz.py` (the EXPANDED artifact; SHA pre/post pinned at runtime).
- **GPU venv python** (W8-2 RERUN only; PINNED per `computation-environment.md`): `phonon-exflation-sim/.venv312/Scripts/python.exe`. torch.linalg on the RX 9070 XT (17.1 GB VRAM) for any D_K Peter-Weyl block-diagonal eigvals (fits VRAM per `math-scripts.md` D_K block-diagonality pre-check); matplotlib Agg backend, DPI 200.
- **PNG outputs** (W8-2): `Phononic-Crystal-Geometry-Vis-{1..N}.png` at the script's `OUT_DIR = sessions/framework/`, N = 7 (regenerated current) + #new (≥ 3). NON-OPTIONAL per context §7 W8 seed.
- **Closure scripts** (all three gates; mechanical SHA + verdict): `computations/session-x/sx_w8_aggregate_domain_survey.py`, `computations/session-x/sx_w8_expansion_update_rerun.py`, `computations/session-x/sx_w8_archive_migration.py` — each imports `canonical_constants`, computes dual SHA, `append_verdict`s to `computations/session-x/sx_gate_verdicts.txt`.
- **KB tools** (all gates): `mcp__knowledge__{get_constant, search_knowledge, trace_entity, list_entities, query_entity}` over entity classes `{constants, theorems, closed, gates, sessions, open}`.
- **Random seed**: 42 (Vis-1 BCC node `RandomState(42)`; preserve for layout reproducibility). All other compute deterministic.

## Wave 8 Input-SHA Ledger

Every input file W8's gates consume, with expected SHA-256 per `.claude/rules/gate-verdicts.md` (cross-checked at plan-freeze by `computations/_shared/_plan_upstream_pin_validator.py`; dynamic inputs marked `<computed-at-runtime>` and verified at execution):

| Input file | Consumed by | SHA-256 |
|:-----------|:------------|:--------|
| `sessions/framework/Phononic-crystal-geometry_viz.py` | W8-1 (survey), W8-2 (expand in place; pre/post) | `<computed-at-runtime>` |
| `sessions/framework/ARCHIVE/Phononic-Crystal-Geometry.md` | W8-1, W8-3 | `<computed-at-runtime>` |
| `sessions/framework/Phononic-Substrate-Geometry.md` | W8-3 (D6 §7.3 resolution; successor doc) | `<computed-at-runtime>` |
| `computations/_shared/canonical_constants.py` | W8-1, W8-2, W8-3 (16 imports + new-figure inputs) | `<computed-at-runtime>` |
| `tools/knowledge.db` | W8-1, W8-2, W8-3 (KB survey) | `<computed-at-runtime>` |

All input SHAs are `<computed-at-runtime>`: the script and successor doc are live framework files (the script is edited in-place by W8-2; the canonical_constants module is shared and may update between plan-freeze and execution; the knowledge.db is rebuilt by `/weave --update`). The closure scripts log each input's SHA in the first 20 lines of stdout and emit the closure hash per `gate-verdicts.md §"During computation"`.

---

**End of session-x W8 plan (EXPANSION-PRIMARY).** Deliverable: a comprehensively expanded SU(3) Jensen crystal-geometry visualization — the depicted geometry brought to current (S93-era) understanding, ≥ 3 NEW figures added for post-S47 geometric results (4-stratum partition stability, spectral-moment R-family, spectral-dimension flow, optional bridge geometry), regenerated through the GPU venv — plus a comprehensive archive-migration ledger resolving the §7.3-pointer and re-sourcing the stale values. Validation (the QA-layer drift fixes D1-D8) is embedded, not the point. Split: W8a = `WX-W8-1` + `WX-W8-2` (script + geometry + rerun); W8b = `WX-W8-3` (archive migration).
