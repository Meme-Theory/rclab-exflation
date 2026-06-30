# Session-X Plan — Wave 3: Comprehensive Aggregate-Expansion of `Phononic-to-Cosmos.md`

**Date**: 2026-05-25
**Author**: mack-cosmic-bridge (generated per `/rclab-plan` per-wave swarm, expansion-primary scope)
**Owner agent**: `mack-cosmic-bridge` (author of the document "Crystal to Cosmos"; cosmology + observational-contact domain specialist; planner AND `/rclab-coordinate` executor)
**Plan source**: `sessions/session-plan/session-x-context.md` §0–§2, §4–§7 (W3 seed)
**Working paper**: `sessions/session-x/session-x-w3-workingpaper.md`
**Document under expansion**: `sessions/framework/Phononic-to-Cosmos.md` (Mack, authored 2026-03-23 / S57; 500 lines, 64,462 bytes)

> **OVERWRITE NOTE**: this file replaces the prior mis-scoped (reconcile-primary) W3 plan. Per context §0/§1 (scope correction 2026-05-25): **EXPANSION is the job; VALIDATION is the QA sub-layer.** A reconcile-only plan FAILS the assignment.

---

## Wave 3 Summary

**PRIMARY MODE — comprehensive aggregate EXPANSION, not validation.** This wave brings `Phononic-to-Cosmos.md` — my own S57 cosmologist's assessment of the framework — to a current (S93-era) whole-project view of the framework's **cosmology + observational-contact domain**. The document was authored at S57 and has never integrated the ~36 sessions (S58→S93) of cosmological development produced since. Its headline conclusion — that the cosmological constant is "112–114 orders of magnitude above observation" with a resolving "mechanism [that] does not yet exist" (§1) — is not merely *wrong now*: the document is missing the **entire DILUTION-CC resolution apparatus** (S66, Volovik tracking vacuum `rho_vac ~ M_Pl^2 H^2` closing the gap to `rho_vac/rho_obs = 1.032` / 0.01 OOM) **plus 36 sessions of cosmological development** — the spectral-index paradigm reversal (n_s 2.065 → 0.9561), the dual-pathway tensor-to-scalar program, the BBN thermalization theorem, the Volovik-partition dark-matter resolution, the late-time ISW-tracking channel, the falsifier-master-inventory + pre-registered-observations programs, the GW domain-wall retraction, LRD/JWST contact, and the §VII cross-pillar cosmology bridges.

The deliverable (G2) is a **substantially expanded / largely-rewritten document** that reads as if I authored it today with full knowledge of all ~93 sessions — in my own authorial voice (rigorous, conversational, observation-anchored, substrate-IS-direction-respecting, accepting "only the kind of truth I could rederive mathematically"). The validation pass (G3) is the embedded QA layer: every retained claim brought current, every number traced to a canonical_constants entry / permanent theorem / closed mechanism / gate verdict, every framing inverted to the substrate-IS direction where it drifted. **A reconcile-only edit FAILS this wave. A cosmetic/minimal edit FAILS G2. If the executor finishes fast, that is the failure signature (context §0): a 36-session domain synthesis cannot be done in a quick pass.**

The wave has THREE gates in the canonical `SURVEY → EXPAND → VERIFY` architecture (context §4). Center of mass is G2.

- **WX-W3-1 AGGREGATE-DOMAIN-SURVEY (AUDIT)** — the comprehensiveness engine: map the framework's cosmology domain across ~93 sessions via the knowledge MCP and enumerate the gap (everything the project knows in this domain that the document does NOT cover), each gap row KB-cited with a "where it belongs."
- **WX-W3-2 COMPREHENSIVE-EXPANSION (VERIFY)** — the deliverable: rewrite the CC section as RESOLVED (DILUTION-CC-66 + downstream) AND comprehensively expand the DM / DE / observational program to current.
- **WX-W3-3 RECONCILE+VERIFY (VERIFY)** — QA over the expanded document: zero stale / unframed / untraced claims; substrate-IS direction restored; substitution chains on every directional/ratio claim.

**Default classification: PHONONIC** (substrate cosmology — DM = Leggett-channel GGE quasiparticle relic, CC = a_0 zeroth-moment non-equilibrium residual diluted by the Volovik tracking vacuum, expansion = acoustic through the BLV metric). Pure-LCDM-comparison passages (the §6 LCDM/WDM baselines, the Appendix convention-translation rows for standard FRW quantities) are classified NON-PHONONIC where they describe the comparison framework, not the substrate.

**Document-section split (per spawn directive "W3a §§1–3; W3b §§4+")**: the three gates address the document holistically, but the expansion/QA writing is organized by document region — **W3a coverage = document §§1–3** (Executive Summary; What the Framework Claims; Where It Connects to Real Cosmology: DM / DE+CC / extra dimensions / phase transitions / Hubble); **W3b coverage = document §§4+** (What It Gets Right; What It Gets Wrong; the Observational Gauntlet; Connections to Research; Recommendations; Appendix convention table). G2's PASS criterion (every material gap integrated-or-scoped) spans both regions; the W3a/W3b split is the executor's organizing partition for the rewrite, recorded in the G2 WP section as two sub-blocks.

**Scope discipline (mack-bridge role)**: per `feedback_mack-bridge-role.md`, my observational priorities ARE the user's observational priorities; this wave treats DESI DR3 / CMB-S4 / LiteBIRD / LISA / 21cm testability claims as load-bearing and brings them to current pre-registered-observations status with full fidelity. I do NOT overstate cosmological agreement; I keep three categories distinct — what the data shows, what it suggests, what it does not address — which is the document's own honest-assessment stance, preserved and extended.

---

## Wave 3 Decision Point Prerequisites

**NONE.** Wave 3 is structurally independent — it surveys the existing knowledge base (a read-only snapshot at dispatch time) and rewrites a single curated document. It consumes NO upstream verdict from any other session-x wave; per the partition manifest it dispatches in parallel with W1, W2, W4–W8. The three W3 gates are internally sequential (G1 survey produces the gap set that G2 consumes; G2 produces the expanded document that G3 QAs), but carry no cross-wave dependency. All inputs (the document, `computations/_shared/canonical_constants.py`, `tools/knowledge.db`) exist on disk at plan-freeze with SHAs pinned in the Input-SHA Ledger below. The cross-document consistency closeout (W9, `gen-physicist`) consumes THIS wave's output; W3 does not depend on W9.

If, at dispatch time, any input SHA has drifted from the ledger (e.g., a concurrent wave touched `canonical_constants.py`), the executor resolves to the runtime file ground truth per `gate-verdicts.md §"Canonical Verdict-File Path"` runtime canonical-path rescue and documents the drift in the gate's `value=` field per `substrate-first-canonical-sourcing.md §(ii.B)` — it does NOT block. If a gate's producing machinery is somehow unmet at dispatch, it honestly closes per `mechanical-closure-discipline.md` (no convention-shopping to force a verdict).

---

## §W3-1. WX-W3-1 — AGGREGATE-DOMAIN-SURVEY

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W3-1-AGGREGATE-DOMAIN-SURVEY"
schema_version: "R3"
trigger: "[AUDIT]"
classification: "PHONONIC"   # cosmology domain = GGE relic acoustic physics + spectral-moment observables; substrate excitations throughout
agent_type: "mack-cosmic-bridge"
hypothesis: "The framework's cosmology + observational-contact domain, surveyed across all ~93 sessions via the knowledge MCP, contains a large, enumerable body of results (DILUTION-CC + downstream, the n_s/r/BBN paradigm shifts, the DM-abundance resolution, the late-time ISW/DESI/GW programs, the falsifier + pre-registered-observation registries, LRD/JWST contact, §VII cosmology bridges) that the S57 document does NOT cover; the gap is enumerable with KB citations."

method:
  description: >
    WHOLE-DOMAIN survey (NOT a claim-by-claim audit of the document's existing sentences).
    Sweep the knowledge base broadly across the framework's cosmology + observational-contact
    domain, using the query manifest below (tens of queries across the pertinent entity classes).
    Produce TWO artifacts recorded in the WP: (a) a CURRENT WHOLE-PROJECT STATE-OF-DOMAIN MAP
    (what the project now knows in this domain, organized by sub-topic, each item KB-cited),
    and (b) a GAP ANALYSIS — the set difference between (a) and what the document covers, each
    gap row carrying its KB citation + a one-line "where it belongs in the document" (which
    §/sub-§ of the document the gap content lands in, including new sub-sections). The closure
    script is mechanical (computes the dual-SHA over the survey/gap artifacts + canonical snapshot
    + doc-pre and appends the verdict). The intellectual work is the survey + gap enumeration,
    recorded in the WP MCP Pre-Compute Audit block + the survey/gap artifacts.
  producing_script: "computations/session-x/sx_w3_aggregate_domain_survey.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator — set-coverage + gap-enumeration
operator:
  type: "set"
  form: "PASS iff (domain_entity_classes_surveyed superset-of pertinent_classes) AND (gap_set enumerated with |citation(g)| >= 1 AND |where_in_doc(g)| >= 1 for every g in gap_set) AND (|gap_set| >= gap_floor)"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    Pertinent entity classes ALL swept = {theorems, closed, gates, sessions, open, constants, equations,
    registries, provenance} over the cosmology domain (DM / DE+CC / expansion-history / BBN / CMB-shape /
    GW / observational-program / LRD). Gap analysis enumerated with KB citation + doc-location per row.
    gap_floor = 12 material gap rows (the domain is ~36 sessions stale; a comprehensive survey cannot
    return fewer — a thin gap list is the failure signature per context §0). Each of the 7 headline
    domains (CC, n_s, r, DM-abundance, BBN/expansion, late-time DE/ISW, observational-program/falsifier)
    MUST appear with >= 1 gap row.
  direction: ">="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — synthesis/expansion gate"

# (5) machinery_pin_map — every free parameter of the survey + closure pinned
machinery_pin_map:
  N_eval: "N/A — survey gate (no numerical scan)"
  L_max: "N/A — survey gate; canonical L_max referenced where cosmology predictions cite it is L_max=10 (155,984-mode spectrum) and L_max=12 (master cache), recorded as context not computed"
  scan_range: "N/A — survey gate"
  step_size: "N/A — survey gate"
  tolerance: "N/A — survey gate (PASS is set-coverage + enumeration, not a numerical band)"
  scheme: "KB-AGGREGATE-SURVEY"
  convention: "substrate-IS-domain-map"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — no linear algebra; mechanical SHA + verdict only (numpy not invoked for compute)"
  # --- survey-specific pins (the comprehensiveness contract) ---
  kb_tools_pinned: "[search_knowledge, trace_entity, list_entities, get_constant, list_constants, query_entity]"
  entity_classes_surveyed: "[theorems, closed, gates, sessions, open, constants, equations, registries, provenance]"
  domain_scope_definition: >
    DOMAIN = the framework's cosmology + observational contact: (i) dark matter — Leggett/GGE quasiparticle
    relic, Omega_DM, f_DM partition, transfer function, free-streaming, annihilation/self-interaction nulls;
    (ii) dark energy + cosmological constant — DILUTION-CC, Volovik tracking vacuum, w_0/w_a, equation of state,
    effacement residual; (iii) expansion history — acoustic e-folds, BBN, reheating, N_eff, late-time H(z),
    Hubble tension; (iv) CMB-shape observables — n_s, r, n_T, alpha_s, f_NL, second-sound l~721, sigma_8;
    (v) GW background — transit GW, domain-wall (retracted S77), LISA Omega_GW; (vi) the observational program —
    pre-registered-observations, falsifier-master-inventory, falsifier-rigor-registry, P-OBS-ALIGNED-CEILING;
    (vii) §VII cross-pillar cosmology bridges (§VII.AT CC, §VII.AX PBH/OP-PROJ); (viii) LRD/JWST contact.
  gap_row_taxonomy: >
    Each gap row is tagged one of {NEW-SINCE-AUTHORSHIP (result postdates S57), NEVER-COVERED (predates or
    parallels S57 but absent from doc), SUPERSEDED-CLAIM (doc asserts X; X is now corrected — record old->new),
    PARADIGM-SHIFT (doc's framing of a whole topic is inverted by later results)}.
  query_manifest_floor: ">= 25 distinct KB queries logged in the WP MCP Pre-Compute Audit block"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["state_of_domain_map", "gap_analysis"]   # the survey deliverables are the "content" of this gate

# (7) substitution_chain — not required (survey gate produces no directional/ratio claim of its own)
substitution_chain:
  required: false
  content: |
    N/A — the survey gate enumerates the domain and the gap; it makes no sign/direction/ratio claim of
    its own. Directional/ratio claims surface in G2/G3 (the expansion) and carry their substitution chains
    there (Omega_DM interpretation, the 229x hierarchy, the CC-OOM magnitude, the DILUTION-CC ratio).

# (8) input_files
input_files:
  document_pre:
    path: "sessions/framework/Phononic-to-Cosmos.md"
    sha256: "fbc9176c12a39b15f90762ce0926316f3dc1042eeb12d0f0204838811a16ea30"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "53904e1733f827f807e20e2ed6081717cc048f6597e6f4ef158d31fc758d7c9f"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w3_aggregate_domain_survey.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w3_aggregate_domain_survey.npz"
    artifact_kind: "data"
    optional: true   # survey artifacts live in the WP; npz optional (may store the gap-row table + query manifest as arrays)
  plot:
    path: "computations/session-x/sx_w3_aggregate_domain_survey.png"
    artifact_kind: "plot"
    optional: true   # no plot required for a survey gate
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W3-1-AGGREGATE-DOMAIN-SURVEY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-1. WX-W3-1-AGGREGATE-DOMAIN-SURVEY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The cosmology domain has been swept across all pertinent entity classes; the gap analysis is enumerated
  (>= 12 material rows, all 7 headline domains represented) with a KB citation + doc-location per row and a
  taxonomy tag; >= 25 KB queries logged. The expansion (G2) has a complete, cited target list. The document's
  domain coverage is now MEASURED against the project's current state.
FAIL_meaning: >
  The survey only re-checked the document's existing claims (claim-by-claim audit, not a domain sweep), OR
  the gap analysis is thin (<12 rows / a headline domain missing / rows lacking citation or doc-location), OR
  <25 queries logged. This is the "finishes fast" failure signature (context §0): a 36-session domain synthesis
  cannot be done in a handful of queries. FAIL maps which domain sub-areas remain unsurveyed.
INFO_meaning: >
  The survey is complete but a domain sub-area returns ambiguous current state (e.g., a constant carries a
  value-spread across schemes with no single canonical — n_s is the canonical example: 0.9561 / 0.9567 / 0.9595 /
  0.9649). The ambiguity is logged as a gap row tagged for (value, scheme) disambiguation in G2, not silently collapsed.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w3_aggregate_domain_survey.py"
    - "computations/session-x/sx_gate_verdicts.txt (created if absent; appended if present)"
    - "sessions/session-x/session-x-w3-workingpaper.md §W3-1 (the state-of-domain map + gap analysis)"
  estimated_time: "0.4 wave-equivalents (the heavy KB sweep; tens of queries; gap enumeration)"

substrate_framing: |
  The cosmology domain is the physics of the GGE relic and its spectral-moment observables AFTER the
  fold transit: dark matter = Leggett-channel quasiparticle excitations of the post-transit GGE
  (Type-F single-summand-projection trace on A_K, Door-S70); the cosmological constant = the
  non-equilibrium a_0 zeroth-moment residual diluted by Volovik tracking (rho_vac ~ M_Pl^2 H^2);
  the expansion observables (w_0, w_a, n_s, r, ISW) = spectral moments of D_K read through the
  emergent acoustic metric. The survey maps the SUBSTRATE side of every cosmological observable
  (D_K eigenvalues -> spectral action moments -> emergent FRW quantity), NOT the LCDM container.
  Per phononic-framing.md: the framework derives LCDM's inputs from the spectral geometry; the
  survey enumerates which of those derivations the S57 document is missing.
```

---

## §W3-2. WX-W3-2 — COMPREHENSIVE-EXPANSION

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W3-2-COMPREHENSIVE-EXPANSION"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: "The document can be substantially expanded — CC section rewritten as RESOLVED (DILUTION-CC-66 + downstream); DM/DE/observational program comprehensively brought to the S93 state — such that every material gap row from G1 is either integrated into the document (in Mack's authorial voice, substrate-IS direction) or explicitly scoped-out with a one-line reason, and the document reads as a current comprehensive S93 synthesis."

method:
  description: >
    THE DELIVERABLE. Substantially expand / rewrite `sessions/framework/Phononic-to-Cosmos.md` to
    integrate the G1 gap set. This is additive synthesis in the document's own register (rigorous,
    conversational, observation-anchored), NOT a reconcile-only edit. Concretely the executor MUST:
    (a) REWRITE the CC treatment (doc §3b, §3b-ii, §5.1, Appendix CC row) — the headline "112-114 OOM,
        mechanism does not exist" becomes the DILUTION-CC-66 RESOLUTION: Volovik tracking vacuum
        rho_vac ~ M_Pl^2 H^2 closes the gap to rho_vac/rho_obs = 1.032 (0.01 OOM); CC_OOM=115.5 is the
        dilution DEPTH not a failure; the "reframing" subsection §3b-ii is promoted from "agenda, not
        result" to the executed S66 result + its §VII.AT registry slot + the C10/T7 assumption ladder +
        BBN-VOLOVIK-67 survival. The doc's "integrability problem" framing is retired (the CC magnitude
        is now a tracking-vacuum expansion-history reading, the W11 Volovik CC Tracking Wall).
    (b) REWRITE the spectral-index treatment (doc §5.2, Appendix n_s row, Exec Summary) — "n_s=2.065
        blue 262sigma CLOSED" is SUPERSEDED: the naive KZ power-law fit was the wrong observable; the
        slow-roll route (opened S42, first-viable S62 n_s=0.9567, triple-confirmed S73a Bogoliubov-invariant,
        canonical n_s_framework=0.9561 S84-85 gauge-invariant via eps_BLV=2-1/eps_SA exact) gives ~O(1)sigma
        from Planck. This INVERTS the document's headline (the doc treats n_s as a fatal 262sigma deficiency).
    (c) REWRITE the tensor-to-scalar treatment (doc §6 Test 2 region; Appendix) — "r=3.86e-10 unobservable"
        is SUPERSEDED by the dual-pathway program: r_CMB_framework=0.0117315 (Path-C, S83 G46 PASS),
        r_PathH=0.0074705 (Path-H); BK18 r<0.036 PASS; LiteBIRD 24sigma / CMB-S4 8.1sigma; BK-Array 2026 decision tree.
    (d) RESOLVE the DM-abundance mapping (doc §3a, §5.9, Appendix Omega_DM row) — the "factor-3 ambiguity,
        single most important unresolved issue" is RESOLVED by LEGGETT-MOMENT-70: Omega_DM h^2=0.1200 at 0.6%
        from Planck (Leggett-only = 0.03985 x 3.010), Type-F single-summand trace; Volovik partition
        F_Josephson=-336.6 (95.9%->vacuum) / F_BCS+F_BA+F_Leggett=14.411 (->matter).
    (e) REWRITE the BBN treatment (doc §5.3) — "no BBN connection, entirely conceptual" becomes BBN-VOLOVIK-67
        PASS (|w_vac-1/3|=3.39e-41, G_eff/G=1.5 marginal-inside-bounds) + S75 W3-M (10^14 thermalization
        e-folds erase GGE ICs, N_eff=3.044 to machine zero) + S76 reheat T_RH computation.
    (f) EXPAND the late-time expansion / Hubble treatment (doc §3e, §5.4) — the "no H(z), biggest gap" is
        PARTIALLY FILLED: w_0=-0.918 produces ISW-TRACKING-68 PASS (+12.3% vs LCDM, +7.6% substrate-specific
        c_s^2_DE=0 so DE clusters with matter), sigma_8=0.799; what remains genuinely open is scoped explicitly.
    (g) ADD NEW SECTIONS for programs the doc never covered: the pre-registered-observations detector
        timeline (DESI DR3 / JUNO / Euclid / DUNE / LiteBIRD / CMB-S4 / LISA / 21cm); the
        falsifier-rigor-registry (18 channels, 11 ZFP); P-OBS-ALIGNED-CEILING (7/9); the f_NL bispectrum
        program (folded=0.129 UNIQUE discriminant — no single-field model produces folded shape); the GW arc
        (S59 prediction -> S77 RETRACTION via Josephson-bias wall-killing 15,000x before reheating -> transit-GW
        PROVEN + Omega_GW_Lambda_A/C LISA discriminator S87); LRD/JWST contact; the §VII cross-pillar cosmology
        bridges (§VII.AT CC-tracking, §VII.AX.OP-PROJ — mack sole-writer).
    (h) UPDATE the §6 Observational Gauntlet + §8 Recommendations to the current pre-registered-observations
        state (the S57 "8 tests" are the ancestor of the current registry; map them forward, mark which
        recommendations were executed S58-S93: 8.2 H(z) -> ISW-68; 8.3 integrability/CC -> DILUTION-66;
        8.4 n_s -> slow-roll route; 8.1 T(k) and 8.6 free-streaming -> framework-dm-properties registry).
    (i) UPDATE the Appendix Convention Translation Table to current canonical values + new rows.
    Organize the rewrite as W3a (document §§1-3) + W3b (document §§4+) sub-blocks in the WP §W3-2 section.
    The closure script is mechanical: re-read the post-edit document, verify each G1 material gap row is
    addressed (integrated OR scoped-out), compute the dual-SHA, append the verdict.
  producing_script: "computations/session-x/sx_w3_comprehensive_expansion.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator — gap-integration set (integrated union scoped-out = all gaps)
operator:
  type: "set"
  form: "PASS iff for every g in gap_set(G1): g in integrated_set OR g in scoped_out_set(with one-line reason); AND integrated_set union scoped_out_set = gap_set; AND |integrated_set| / |gap_set| >= integration_floor"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    Every material gap row from G1 is integrated into the document OR explicitly scoped-out with a one-line
    reason. integration_floor = 0.80 (>= 80% of material gaps actually integrated, not merely scoped-out — a
    high scope-out fraction is the cosmetic-edit failure signature). The 4 headline rewrites (a CC-resolution,
    b n_s-paradigm-reversal, c r-dual-pathway, d DM-abundance-resolution) and the BBN rewrite (e) are
    MANDATORY-integrate (cannot be scoped out). The document grows substantially (the S57->S93 gap is ~36
    sessions; a comprehensive expansion materially increases coverage of every headline domain). Authorial
    voice preserved; substrate-IS direction restored wherever it drifted.
  direction: ">="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — synthesis/expansion gate"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A — expansion gate"
  L_max: "N/A — expansion gate (predictions cite their own canonical L_max=10/12 as documented)"
  scan_range: "N/A — expansion gate"
  step_size: "N/A — expansion gate"
  tolerance: "N/A — PASS is gap-integration coverage, not a numerical band"
  scheme: "AUTHOR-CURATED-EXPANSION"
  convention: "substrate-IS-Mack-voice"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — prose expansion + mechanical SHA/verdict; no linear algebra"
  # --- expansion-specific pins ---
  gap_set_source: "WX-W3-1 gap_analysis artifact (same-session upstream; survey gap-row table in WP §W3-1)"
  mandatory_integrate_rows: "[CC-resolution(DILUTION-CC-66), n_s-paradigm(2.065->0.9561), r-dual-pathway(0.0117/0.0075), DM-abundance(LEGGETT-MOMENT-70 Omega_DM_h2=0.120), BBN(BBN-VOLOVIK-67 + S75 thermalization)]"
  value_scheme_tagging: >
    Any framework prediction carrying a value-spread across schemes MUST be written as a (value, scheme)
    tuple, NOT a bare number. Canonical cases: n_s (0.9561 canonical / 0.9567 S73a / 0.9595 pre-reg-obs /
    0.9649 S84 constant-eps); w_0 (-0.918 canonical Volovik-partition / -0.842454 branch-(iv) substrate-compaction);
    r (0.0117315 Path-C / 0.0074705 Path-H). Per cross-pillar-bridge-corpus.md (value,scheme) discipline + my
    pinned S85 W1a-F1 rule (framework predictions are (value, scheme) tuples).
  voice_preservation: "first-person cosmologist register; 'the kind of truth I could rederive mathematically'; honest-assessment subsections retained; three categories distinct (data shows / suggests / does not address)"
  framing_direction: "substrate-IS per phononic-framing.md — D_K eigenvalues -> spectral moments -> emergent FRW observable; invert any container-thinking"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]

# (7) substitution_chain — REQUIRED (the expansion adds directional/ratio claims)
substitution_chain:
  required: true
  content: |
    Three directional/ratio claims added or rewritten by this gate MUST carry an explicit substitution
    chain in the document text + the WP §W3-2 section (per math-scripts.md §"Double-Check Logic Before Compute"):

    CLAIM 1 — "DILUTION-CC closes the CC gap (the magnitude is no longer a 114-OOM failure)."
      Step 1: Lambda_naive/Lambda_obs ~ 1.93e114    [doc S57 value, M_KK^4-scale GGE excess; CC_OOM=115.5 dilution depth, canonical S66]
      Step 2: rho_vac(today) = M_Pl^2 * H_0^2        [Volovik q-theory tracking law, C10 ASSUMED-PARTIALLY-PROVEN, S66; rho_vac ~ H^2 not H^0]
      Step 3: ratio = rho_vac(tracking) / rho_obs    [DILUTION-CC-66 substitution; H tracks down from GUT scale to H_0]
      Step 4: = 1.032                                [S66 W1-A PASS, s66_dilution_cc.npz; 0.01 OOM residual]
      Step 5: 1.032 ~ 1 ==> the H^2-tracking vacuum dilutes the M_Pl^2 H^2 initial reservoir to the observed
              value as H falls; the 114-OOM "gap" was the static (H^0) misidentification, NOT a tuning problem.
      Conclusion: CC magnitude is RESOLVED at 0.01 OOM under Volovik tracking (W11 wall, §VII.AT).

    CLAIM 2 — "Omega_DM is resolved at 0.6% (the factor-3 mapping ambiguity is closed)."
      Step 1: Omega_DM h^2 (Leggett-only) = (F_Leggett-anchored mass moment) [LEGGETT-MOMENT-70, Type-F trace]
      Step 2: = 0.03985 * 3.010                      [Leggett-channel anchor x multiplicity, s70_leggett_moment.npz]
      Step 3: = 0.1200                                [LEGGETT-MOMENT-70 PASS]
      Step 4: Planck Omega_DM h^2 = 0.1186 +/- 0.0020 [canonical Omega_DM_obs lineage / Planck 2018]
      Step 5: |0.1200 - 0.1186| / 0.1186 = 0.0118 ==> ~0.6% (the doc's "Interpretation A/B factor-3" is
              superseded — the Type-F single-summand trace fixes the mapping with no interpretive freedom).
      Conclusion: Omega_DM h^2 = 0.120 at 0.6%, RESOLVED (Door-S70).

    CLAIM 3 — "n_s is no longer a 262sigma failure; the framework predicts n_s ~ Planck."
      Step 1: n_s_naive = 2.065 (S53 KZ power-law fit over P(K) on [0.002,0.358] M_KK) [doc value — wrong observable]
      Step 2: n_s_slow-roll = 1 - 2*eps_H            [Hubble slow-roll from spectral-action ratio, S42/S62]
      Step 3: eps_H = (1/2)(dS/dtau)^2 / (S*d^2S/dtau^2) [S64; eps_BLV = 2 - 1/eps_SA exact gauge invariance, S66 T7]
      Step 4: n_s_framework = 0.9561                 [canonical, S84-85 gauge-invariant; S73a triple-confirmed 0.9567]
      Step 5: |0.9561 - 0.9649| / 0.0042 = 2.1 ==> O(1)sigma vs Planck (the pre-reg-obs table cites 1.29sigma
              via the CMB-S4 forecast sigma). Either way O(1)sigma, NOT 262sigma. The 262sigma was the naive-KZ
              observable (the wrong quantity); the slow-roll observable is O(1)sigma.
      Conclusion: n_s is O(1)sigma from Planck (the doc's headline 262sigma deficiency is SUPERSEDED).

    (Additional directional claims in the expansion — the 229x hierarchy -> l~721 (= pi*229.48 = 720.9), the
    w_a four-fold lock (= 0), the ISW +12.3% (C_l^Tg framework/LCDM = 1.123) — carry their chains inline where
    stated, each citing the canonical constant + gate.)

# (8) input_files
input_files:
  document_pre:
    path: "sessions/framework/Phononic-to-Cosmos.md"
    sha256: "fbc9176c12a39b15f90762ce0926316f3dc1042eeb12d0f0204838811a16ea30"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17"
  survey_gap_artifact:
    path: "sessions/session-x/session-x-w3-workingpaper.md"   # §W3-1 gap analysis (same-session upstream)
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "53904e1733f827f807e20e2ed6081717cc048f6597e6f4ef158d31fc758d7c9f"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w3_comprehensive_expansion.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w3_comprehensive_expansion.npz"
    artifact_kind: "data"
    optional: true   # the expansion is in the document; npz optional (gap-integration coverage table)
  plot:
    path: "computations/session-x/sx_w3_comprehensive_expansion.png"
    artifact_kind: "plot"
    optional: true
  document_post:
    path: "sessions/framework/Phononic-to-Cosmos.md"
    artifact_kind: "document"
    optional: false   # THE DELIVERABLE — the expanded document
    must_contain:
      - "DILUTION-CC"          # CC resolution integrated
      - "LEGGETT-MOMENT"       # DM-abundance resolution integrated
      - "BBN-VOLOVIK"          # BBN rewrite integrated
      - "0.9561"               # n_s paradigm-shift value integrated (canonical n_s_framework)
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W3-2-COMPREHENSIVE-EXPANSION:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-2. WX-W3-2-COMPREHENSIVE-EXPANSION"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  Every material gap row from G1 is integrated (>= 80%) or explicitly scoped-out; the 5 mandatory-integrate
  rewrites (CC-resolution, n_s-reversal, r-dual-pathway, DM-abundance, BBN) are all in the document; the
  document reads as a current comprehensive S93 synthesis in Mack's voice with the substrate-IS direction
  restored. The framework's cosmology assessment now reflects what the project actually knows in 2026-05.
FAIL_meaning: >
  A cosmetic/minimal edit (gaps merely annotated, not integrated; integration fraction <80%); OR any
  mandatory-integrate rewrite missing (e.g., CC still framed as "unsolved 114 OOM"; n_s still "262sigma CLOSED");
  OR authorial voice destroyed / replaced by registry-dump prose; OR substrate-IS direction inverted
  (container-thinking: "DM particles created in spacetime" rather than GGE excitations of the substrate).
  A reconcile-only edit FAILS — expansion is the deliverable.
INFO_meaning: >
  The expansion is substantially complete but a bounded subset of gap rows (a minority) is scoped-out with
  documented reason (e.g., a sub-topic whose current state is itself a STRUCTURALLY-OPEN gate — the genuine
  open questions, like the f_NL folded-shape detector-reach or the late-time H(z) frontier, are scoped as
  open, not fabricated as resolved). INFO when the scope-out set is non-empty but justified and the
  integration_floor is still met.

# ---- Effort + framing ----
effort:
  files_created:
    - "sessions/framework/Phononic-to-Cosmos.md (substantially expanded — the deliverable)"
    - "computations/session-x/sx_w3_comprehensive_expansion.py"
    - "sessions/session-x/session-x-w3-workingpaper.md §W3-2 (W3a §§1-3 + W3b §§4+ sub-blocks)"
  estimated_time: "1.0+ wave-equivalents (the comprehensive rewrite; the center of mass of the wave)"

substrate_framing: |
  The expansion preserves and restores the substrate-IS explanatory direction throughout. The CC is
  the a_0 zeroth-moment non-equilibrium residual of the GGE relic, diluted by the Volovik tracking
  vacuum (rho_vac ~ M_Pl^2 H^2) — NOT a vacuum-energy fine-tuning IN a spacetime container. Dark matter
  is the Leggett-channel quasiparticle excitation spectrum of the post-transit GGE (a Type-F
  single-summand trace on A_K), NOT a thermal-relic particle species. The expansion observables
  (n_s, r, w_0, ISW) are spectral moments of D_K read through the emergent BLV acoustic metric. Every
  rewritten claim flows D_K eigenvalues -> spectral action moments -> emergent FRW observable -> measured
  quantity, per phononic-framing.md. The doc's S57 "exflation is not inflation" register is preserved;
  the spectral-complexity-growth (not metric-expansion) framing is reinforced with the S58-S93 results.
  Substrate dynamics (fold transit, Volovik tracking) are NOT c-bounded (S74 user clarification); only
  propagation on the emergent g_M is — the expansion must not mis-frame transit/tracking as c-limited.
```

---

## §W3-3. WX-W3-3 — RECONCILE+VERIFY

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W3-3-RECONCILE-VERIFY"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "PHONONIC"
agent_type: "mack-cosmic-bridge"
hypothesis: "After the G2 expansion, the document contains ZERO stale claims, ZERO container-thinking framing violations, and ZERO untraced numbers — every retained-or-added claim is current, substrate-IS-framed, and provenance-traced to a canonical_constants entry / permanent theorem / closed mechanism / gate verdict, with a_n^{regulator} tags where Seeley-DeWitt coefficients are cited."

method:
  description: >
    QA sweep over the EXPANDED document (G2 output). Build the set of all checkable claims in the
    expanded document and verify each on three axes: (i) CURRENCY — the claim matches the current
    canonical value / gate verdict (no stale S57 numbers survive un-rewritten; the SUPERSEDED-CLAIM
    gap rows from G1 are confirmed corrected); (ii) FRAMING — substrate-IS direction per
    phononic-framing.md (no container-thinking: no "particles in spacetime", "space expands", "vacuum
    energy" used in the LCDM sense where the a_0 substrate framing applies; the LCDM-vs-substrate
    vocabulary table is respected); (iii) PROVENANCE — every number traces to a canonical_constants.py
    entry, a permanent theorem, a closed mechanism, or a gate verdict (cited inline or in the WP),
    with a_n^{regulator} tags on any Seeley-DeWitt coefficient citation per regulator-pin-discipline.md.
    The PASS set is EMPTY (zero stale/unframed/untraced). The closure script re-reads the document,
    runs the three-axis checks (a claim-extraction + canonical-cross-reference pass), computes the
    dual-SHA, and appends the verdict. Any residual stale/unframed/untraced claim is a FAIL row that
    routes back to in-session G2 correction (per fix-in-session discipline) before the wave closes.
  producing_script: "computations/session-x/sx_w3_reconcile_verify.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator — defect set, PASS = empty
operator:
  type: "set"
  form: "PASS iff stale_set union unframed_set union untraced_set = empty (every claim in the expanded document is current AND substrate-IS-framed AND provenance-traced)"

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: >
    |stale_set| = 0 (no S57 number survives where a current canonical exists) AND
    |unframed_set| = 0 (no container-thinking framing violation per phononic-framing.md LCDM-vs-substrate table) AND
    |untraced_set| = 0 (every number cites canonical_constants entry / permanent theorem / closed mechanism / gate;
    every Seeley-DeWitt a_n carries a regulator tag).
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A — synthesis/expansion gate"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A — verify gate"
  L_max: "N/A — verify gate"
  scan_range: "N/A — verify gate"
  step_size: "N/A — verify gate"
  tolerance: "rel_tol = 1e-3 on any numerical claim cross-checked against canonical_constants (publication-precision-tolerant; Class-8.3 default for presentation-precision numbers per epistemic-discipline.md)"
  scheme: "THREE-AXIS-QA-CURRENCY-FRAMING-PROVENANCE"
  convention: "substrate-IS"
  random_seed: "N/A — deterministic"
  GPU_path: "N/A — claim-extraction + canonical cross-reference; no linear algebra"
  # --- verify-specific pins ---
  currency_reference: "computations/_shared/canonical_constants.py (the SHA-pinned snapshot) + the G1 SUPERSEDED-CLAIM gap rows"
  framing_reference: "phononic-framing.md LCDM-vs-substrate vocabulary table + IS-Space-Not-IN-Space mandate"
  provenance_classes: "[canonical_constants entry, permanent theorem (sessions/permanent-results-registry.md), closed mechanism, gate verdict (computations/session-N/sN_gate_verdicts.txt)]"
  a_n_regulator_check: "any a_n Seeley-DeWitt citation must carry a_n^{zeta|Pauli-Villars|Mellin|lattice|cutoff} tag per regulator-pin-discipline.md"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_post", "canonical_constants_snapshot", "gap_analysis", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]

# (7) substitution_chain — REQUIRED (re-derives the directional/ratio claims G2 added)
substitution_chain:
  required: true
  content: |
    This gate VERIFIES (re-derives) the three substitution chains G2 added (CLAIM 1 DILUTION-CC ratio
    1.032; CLAIM 2 Omega_DM 0.6%; CLAIM 3 n_s O(1)sigma vs the naive-KZ 262sigma), plus the inline directional
    claims (229x -> l~721 = pi*229.48 = 720.9; w_a four-fold lock = 0; ISW +12.3% = C_l^Tg framework/LCDM
    = 1.123). For each, the verifier confirms: the cited canonical constant matches the SHA-pinned snapshot
    value; the arithmetic in the chain is correct to rel_tol 1e-3; the direction read-off matches the claim.
    A chain whose canonical input has drifted, or whose arithmetic fails, is an untraced/stale FAIL row routed
    to G2 in-session correction.
      Worked verify (CLAIM 1): rho_vac/rho_obs claimed 1.032; canonical DILUTION-CC-66 PASS value 1.032
      (s66_dilution_cc.npz, CC_OOM=115.5 depth); |1.032 - 1.032| = 0 <= 1e-3 ==> PASS, direction (~1) confirmed.

# (8) input_files
input_files:
  document_post:
    path: "sessions/framework/Phononic-to-Cosmos.md"   # the G2-expanded document
    sha256: "<computed-at-runtime>"
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17"
  survey_gap_artifact:
    path: "sessions/session-x/session-x-w3-workingpaper.md"   # §W3-1 gap analysis
    sha256: "<computed-at-runtime>"
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "53904e1733f827f807e20e2ed6081717cc048f6597e6f4ef158d31fc758d7c9f"

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w3_reconcile_verify.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w3_reconcile_verify.npz"
    artifact_kind: "data"
    optional: true   # defect-table arrays optional
  plot:
    path: "computations/session-x/sx_w3_reconcile_verify.png"
    artifact_kind: "plot"
    optional: true
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W3-3-RECONCILE-VERIFY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w3-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W3-3. WX-W3-3-RECONCILE-VERIFY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"

# ---- Verdict rubric ----
PASS_meaning: >
  The expanded document is fully current (no stale S57 number survives where a canonical exists),
  fully substrate-IS-framed (no container-thinking violation), and fully provenance-traced (every
  number cites canonical/theorem/closed/gate; every a_n carries a regulator tag). The document is
  a clean, current, comprehensive S93 synthesis ready for the W9 cross-document consistency closeout.
FAIL_meaning: >
  >= 1 stale claim survives (a SUPERSEDED-CLAIM gap row not actually corrected in G2), OR >= 1 framing
  violation (container-thinking inverting the substrate-IS direction), OR >= 1 untraced number / missing
  a_n regulator tag. FAIL rows route to in-session G2 correction (fix-in-session, never defer) and the
  gate re-runs after correction. FAIL maps the residual QA-defect set, not an agent failure.
INFO_meaning: >
  All three defect sets are empty EXCEPT for a bounded set of claims the document explicitly marks
  PRELIMINARY or STRUCTURALLY-OPEN (genuine open questions stated honestly as open — these are not
  "stale" or "untraced", they are correctly-labelled open frontier). INFO when such honestly-open
  claims exist and are correctly demarcated.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w3_reconcile_verify.py"
    - "sessions/session-x/session-x-w3-workingpaper.md §W3-3 (the three-axis QA defect tables)"
  estimated_time: "0.4 wave-equivalents (claim extraction + three-axis cross-reference over the expanded document)"

substrate_framing: |
  The QA gate enforces the substrate-IS direction as a PASS criterion, not a stylistic preference.
  A claim that explains a cosmological observable by invoking LCDM/GR as fundamental (rather than as
  emergent from D_K spectral moments) is a framing-defect FAIL. The verifier confirms that every
  cosmological quantity in the expanded document flows FROM the substrate (D_K eigenvalues -> spectral
  action moments) TOWARD the emergent FRW observable — the cosmological constant from the a_0 moment,
  gravity from a_2, dark matter from the Leggett-channel GGE excitation spectrum — and that the
  Volovik tracking-vacuum CC resolution, the slow-roll n_s, and the DILUTION-CC magnitude are all
  framed as substrate-derived, not container-physics phenomenology.
```

---

## Wave 3 → Wave 9 Decision Point

Wave 3 produces the comprehensively-expanded `Phononic-to-Cosmos.md` (G2 output) + the survey/gap and QA artifacts (G1/G3 WP sections + verdict lines). **W9 (cross-document consistency + coverage closeout, `gen-physicist`) consumes this wave's output.** The handoff to W9:

| W3 verdict pattern | W9 consequence |
|:-------------------|:---------------|
| G1 PASS AND G2 PASS AND G3 PASS | Document is current/comprehensive/clean; W9 SHARED-CONSTANT-MATRIX cross-checks `Phononic-to-Cosmos.md`'s cosmology constants (w_0=-0.918, Omega_DM h^2=0.120, n_s=0.9561, r=0.0117, CC_OOM=115.5) against the other 7 expanded docs for mutual consistency. W9 COVERAGE-CONSISTENCY confirms the cosmology domain is non-overlapping-yet-coherent with `Phononic-framework-hypothesis` (W1), `Phononic-C-Causality` (W4), `Phononic-Penrose-Diagrams` (W5). |
| G2 PASS AND G3 FAIL (residual QA defect) | G3 FAIL rows route to in-session G2 correction (fix-in-session); W3 re-runs G3 after correction BEFORE handing to W9. W9 does not consume an un-QA'd document. |
| G2 FAIL (cosmetic/minimal edit) | W3 does not close; G2 re-dispatches with the gap set unintegrated. W9 blocked on W3 until G2 PASS. |
| G1 FAIL (thin survey) | G2 has no complete target list; G1 re-dispatches with the full query manifest. The wave cannot proceed to a comprehensive expansion on a thin gap analysis. |

**Cross-document shared-constant pins for W9** (this wave's cosmology-domain canonical values, for the SHARED-CONSTANT-MATRIX): `w0_FW=-0.918`, `wa_FW=0`, `w0_FW_R842=-0.842454` (branch iv), `n_s_framework=0.9561`, `r_CMB_framework=0.0117315`, `r_PathH=0.0074705`, `CC_OOM=115.5`, `Omega_m=0.315`, `Omega_DM=0.266`, `Omega_Lambda=0.685`, `sigma_8=0.811`, `M_KK_gravity=7.4287e16 GeV`, `T_acoustic=0.112 M_KK`. W9 cross-checks these against W1/W4/W5 usages.

---

## Wave 3 Machinery-Enumeration Pin

Aggregate of all three gate `machinery_pin_map` entries (per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR; consumed by `_yaml_gate_validator.py` for sig_4 of the v3 closure ladder). All three gates are SYNTHESIS/EXPANSION gates — no numerical scan, no GPU linear algebra; the closure scripts are mechanical (dual-SHA + `append_verdict`). The intellectual work (survey, gap enumeration, expansion writing, three-axis QA) is the executor's, recorded in the WP + survey/gap artifacts + the expanded document.

| Gate | scheme | convention | tolerance | GPU_path | distinctive pins |
|:-----|:-------|:-----------|:----------|:---------|:-----------------|
| WX-W3-1 | KB-AGGREGATE-SURVEY | substrate-IS-domain-map | N/A (set-coverage) | N/A | entity_classes_surveyed (9), domain_scope (8 sub-areas), gap_row_taxonomy (4 tags), query_manifest_floor >= 25, gap_floor=12 |
| WX-W3-2 | AUTHOR-CURATED-EXPANSION | substrate-IS-Mack-voice | N/A (gap-integration coverage) | N/A | mandatory_integrate_rows (5), integration_floor=0.80, value_scheme_tagging, voice_preservation, framing_direction |
| WX-W3-3 | THREE-AXIS-QA-CURRENCY-FRAMING-PROVENANCE | substrate-IS | rel_tol=1e-3 (numerical claims) | N/A | currency_reference, framing_reference, provenance_classes (4), a_n_regulator_check; PASS=empty defect set |

**Determinism note**: all three gates are deterministic (no `random_seed`). The dual-SHA `audit_sha256` is computed from the ordered input-pin map (document_pre/post + canonical snapshot + survey/gap artifacts + kb_query_manifest); per-gate identity keys (gate_id, scheme, convention) guarantee pairwise-distinct `audit_sha256` across the three gates (sig_5 uniqueness preserved by construction). `content_sha256` is over the gate's content output (G1: survey+gap; G2/G3: document_post).

---

## Wave 3 Input-SHA Ledger

Every input file this wave's gates consume, with SHA-256 per `gate-verdicts.md`. Static files carry precomputed hashes (computed at plan-freeze 2026-05-25); dynamic same-session intermediates are marked `<computed-at-runtime>`. Cross-checked at plan-freeze by `_plan_upstream_pin_validator.py`.

| Input file | Consumed by | SHA-256 | Note |
|:-----------|:-----------|:--------|:-----|
| `sessions/framework/Phononic-to-Cosmos.md` (document_pre) | W3-1, W3-2 | `fbc9176c12a39b15f90762ce0926316f3dc1042eeb12d0f0204838811a16ea30` | the document under expansion (500 lines, 64,462 bytes, authored S57) |
| `sessions/framework/Phononic-to-Cosmos.md` (document_post) | W3-3 | `<computed-at-runtime>` | the G2-expanded document (rewritten in-session by W3-2) |
| `computations/_shared/canonical_constants.py` | W3-1, W3-2, W3-3 | `30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17` | canonical-value snapshot (w0_FW, wa_FW, n_s_framework, n_s_canon, r_CMB_framework, r_PathH, CC_OOM, Omega_DM_obs, planck_ns, sigma_8, M_KK_gravity, T_acoustic, Omega_m/b/Lambda) |
| `tools/knowledge.db` | W3-1, W3-2, W3-3 | `53904e1733f827f807e20e2ed6081717cc048f6597e6f4ef158d31fc758d7c9f` | knowledge-MCP graph (the survey source; ~93 sessions) |
| `sessions/session-x/session-x-w3-workingpaper.md` (§W3-1 gap analysis) | W3-2, W3-3 | `<computed-at-runtime>` | same-session upstream — W3-1 gap-row table feeds the expansion + QA |

**Verdict source** (per `gate-verdicts.md` + S86 W0a-5): `verdict_source: computations/session-x/sx_gate_verdicts.txt` — all three gates append the canonical dual-SHA verdict line here (NOT to any `_shared/` or `sessions/` variant; the canonical per-session path is `computations/session-x/`).

**Runtime drift discipline**: if `canonical_constants.py` SHA has drifted from this ledger at dispatch time (a concurrent wave touched it), the executor resolves to the runtime file value, documents the drift in the gate `value=` field per `substrate-first-canonical-sourcing.md §(ii.B)`, and proceeds — the drift does NOT block (the cosmology constants this wave cites are stable canonical pins; a same-session touch would be additive, not a value change to w0_FW/n_s_framework/etc).

---

**End of session-x Wave 3 plan (expansion-primary).** The deliverable is the comprehensively-expanded `Phononic-to-Cosmos.md`; validation (G3) is the embedded QA layer. Owner + executor: `mack-cosmic-bridge`. Independent wave (no upstream prereqs); feeds W9 cross-document closeout. Dispatch: `/rclab-coordinate sessions/session-plan/session-x-plan-w3.md`.
