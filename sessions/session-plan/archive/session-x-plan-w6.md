# Session-X Plan — Wave 6: Cross-Workshop Synthesis / The 32×32 Operator Read Three Ways (Comprehensive Aggregate Expansion)

**Date**: 2026-05-25
**Author**: phonon-first-cosmologist (generated per /rclab-plan per-wave swarm; scope-corrected to expansion-primary)
**Owner agent**: `phonon-first-cosmologist` (planner AND executor — the document's author-specialist; the cross-domain pattern detector who wrote the S53 synthesis)
**Plan source**: `sessions/session-plan/session-x-context.md` §0, §1, §2, §4, §5, §6, §7 (W6 seed)
**Working paper**: `sessions/session-x/session-x-w6-workingpaper.md`
**Target document**: `sessions/framework/Phononic-Investigation.md` (21,077 bytes; authored 2026-03-21 by Phonon-First Cosmologist as the S53 cross-workshop synthesis; ~40 sessions of project evolution to integrate, S53→S93)

---

## Wave 6 Summary

**PRIMARY MODE — EXPANSION, not validation.** This wave comprehensively brings
`Phononic-Investigation.md` from its S53 authorship state to a current (S93-era) whole-project view of
the framework's **cross-workshop synthesis domain**: the central thesis that *the 32×32 hopping matrix
(equivalently the finite Dirac operator `D_K(τ)` on the 32-cell Voronoi tessellation of (SU(3),
g_Jensen)) is simultaneously the vacuum functional, the shell-correction generator, and the causal
structure — one spectrum read three ways*, plus the **five cross-workshop isomorphisms** the synthesis
identified. The document was written at the END of S53 as a forward-looking pattern-detection report:
it pre-registered a 13-gate S54 program, posed four open questions, and proposed five structural
isomorphisms as conjectures. In the ~40 sessions since, every one of those gates ran, every one of those
open questions was answered (sometimes by dissolving the question), and the isomorphisms either hardened
into permanent cross-pillar theorems, were carried into the mature §VII bridge program, or were
superseded. The document has NEVER integrated any of that. The deliverable (G2) is a substantially
expanded / largely-rewritten synthesis that reads as if authored TODAY with full knowledge of S54→S93.

The DOMAIN this wave surveys and expands: every result bearing on **cross-domain pattern detection /
cross-pillar isomorphism / the unification of the eight pillars through the single `D_K` eigenvalue
problem** — specifically (a) the **S54 consolidated-program gates** (ED-SWEEP-54, SA-LATT-OCC-54,
CONNES-LATT-54 / BURES-CONNES-LATTICE-54, GEODESIC-DEVIATION-54, GUTZWILLER-SU3-54, SCALE-FACTOR-54,
Q-RAYCHAUDHURI-54, FIRAS-GGE-54 + the 5 carry-forward gates) and their full S54→S93 fates; (b) the **five
isomorphisms** (Strutinsky=O'Neill=saddle-point; Connes=Bures=Fisher; volume-preservation=CC-free=topological-rigidity;
the taxonomy-trap; Gutzwiller-Selberg stabilization↔dimensional-reduction) and their promotion/supersession;
(c) the **four open questions** and their resolutions; (d) **NEW cross-domain isomorphisms established
S54→S93** that the S53 doc could not have seen (the §VII cross-pillar bridge program, BCS-as-universal-ancestor,
the SU(1,1) three-way identity, the six-layer causal structure, the LQG/CDT cross-framework comparisons).
Reconstructed from the knowledge base (NOT read linearly).

**VALIDATION is the embedded QA layer (G3), not the deliverable.** The drift-fixes below get corrected
*along the way*; they are necessary but are NOT the point. A reconcile-only pass FAILS this wave (this
plan OVERWRITES a prior mis-scoped reconcile-only plan at the same path).

### Carry-forward / scope source

This is a bespoke aggregate-expansion session (`session-x`), not a sequential compute session. The
"carry-forward" is the entire S54→S93 cross-workshop-synthesis domain enumerated against the document's
coverage (the G1 gap analysis IS the carry-forward source). The §7 W6 seed plus the G1 survey define scope.

### What the G1 survey already surfaced (planner pre-survey; the executor extends this)

The planner ran ~22 KB queries at plan-freeze (manifest reproduced in the G1 WP block + the Input-SHA
Ledger). The single most important finding: **the document's entire forward-looking apparatus — the 13-gate
S54 program, the four open questions, and the five conjectural isomorphisms — has been RESOLVED.** The
document currently reads as a prospectus for a session that happened forty sessions ago. Major gaps (each
with a provisional "where it belongs"), tagged by the gap taxonomy:

| # | Gap (KB-cited) | Tag | Where it belongs |
|:--|:---------------|:----|:-----------------|
| GAP-1 | **S54 program — ALL 8 decisive/high-value gates RAN in S54 then migrated INFO** at S81 batch-canonical-hygiene (`no-run-no-gate` convention). `s54_ed_sweep`, `s54_gutzwiller_su3` (→ `T3-BATCH-S54-GUTZWILLER-SU3` INFO), `s54_bures_connes` (→ `T3-BATCH-S54-BURES-CONNES` INFO / `BURES-CONNES-54` INFO S54), `s54_geodesic_deviation` (→ `T3-BATCH-S54-GEODESIC-DEVIATION` INFO / `DEVIATION-54`), `s54_q_raychaudhuri` (→ `RAYCHAUDHURI-54`), `s54_firas_gge` (→ `GGE-54` / `T3-BATCH-S54-FIRAS-GGE` INFO), `SCALE-FACTOR-54` (PASS in S54 table; `a(τ)` with `q(τ)` −0.97→+0.81 per S54 QA-Hawking). The §IV "Converged S54 Program" must be rewritten from a forward prospectus into a RETROSPECTIVE: each gate annotated with its S54 outcome + where the thread actually resolved downstream. | NEW-SINCE-AUTHORSHIP | §IV (rewrite prospectus → retrospective with per-gate outcomes) |
| GAP-2 | **Isomorphism 1 (Strutinsky=O'Neill=saddle-point) → PERMANENT cross-pillar theorem.** Registry/memory: "Strutinsky-NCG = O'Neill A-tensor: smooth-base + oscillating-fiber decomposition." Quantitatively grounded S57 (`E_GS(fold)=−23.509 = E_smooth+δE_shell+E_pair = −23.468+(−0.041)`) and S62 (`δE_shell = E_exact−E_smooth = −8.857`). The **gradient ratio in the O'Neill/Strutinsky decomposition is 0.71 at the fold** (memory), DISTINCT from the **BCS-vs-geometric gradient ratio 1.30** (PROVEN S53, the speed-bump). Two different ratios — disambiguate, do NOT overwrite the 1.30. | DRIFTED-CLAIM + NEW | Isomorphism 1 (upgrade conjecture → PERMANENT theorem; disambiguate the two ratios) |
| GAP-3 | **The product-submersion O'Neill tensors VANISH: A = T = 0 exactly** for M⁴×SU(3) (S73a Mack-VdD; verified S61 `A-TENSOR-61` to 0.47%; `a_2(D_total)=a_0(D_M)a_2(D_K)+a_2(D_M)a_0(D_K)` with cross-terms bounded by A,T → 0). This is a critical clarification of Isomorphism 1/3: the *product* A-tensor (M⁴ × fiber) is zero; the Strutinsky=O'Neill content lives in the *fiber-internal* Jensen-deformation decomposition (smooth base curvature + oscillating internal correction WITHIN SU(3)), not in the product submersion. The S53 doc conflated these. | NEW-SINCE-AUTHORSHIP | Isomorphism 1 + Isomorphism 3 (the A=T=0 clarification) |
| GAP-4 | **Open Question #2 (does E_0(τ) have a minimum?) → RESOLVED: NO, and the question was mis-framed.** `τ=0.2015` is a local MAXIMUM (PROVEN S53, the speed-bump); CC Path C "R(τ) monotone by AM-GM, no CC minimum along Jensen" (S64 W1-A); the framework's stabilization is the **first-order transit / instanton paradigm** ("Transit τ=0→fold = first-order phase transition", PROVEN S37-38), NOT a potential-well minimum. The DNP instability + Perturbative Exhaustion + clock constraint (permanent results) closed the moduli-well route. This is the framework's "Friedmann wrong question" paradigm: the S53 doc made the E_0 minimum its central decisive question; the project's answer is that the minimum does not exist and was never the right test. | NEW-SINCE-AUTHORSHIP (paradigm shift) | §V Open Question #2 → resolved; §VI paradigm-shift paragraph; §IV ED-SWEEP retrospective |
| GAP-5 | **Open Question #4 (the 115-OOM CC gap) → CLOSED by DILUTION-CC-66.** Volovik tracking vacuum `ρ_vac ~ M_Pl²·H²` (Paper 25 §V; Paper 35) closes the 114-OOM gap to **0.01 OOM** at ratio 1.032 (Scenario B); `CC_OOM=115.5`. The S53 doc's framing ("Strutinsky explains WHY the smooth functional is wrong but does not give the right answer") is half-correct: the Strutinsky/saddle-point reframe is the *structural* diagnosis, and DILUTION-CC is the *quantitative* closure (a DIFFERENT spectral moment — a_0 self-tunes via H²-tracking, distinct from the a_2 shell correction). The two are complementary, not competing. | NEW-SINCE-AUTHORSHIP (resolution) | §V Open Question #4 → resolved; §VI |
| GAP-6 | **Open Question #3 (Bures-Connes / Martinetti-Mercati) → carried into the A_F finite-spectral-triple program.** S87 `CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` (INFO, value 0.980, L_max=12, substrate-state-pair-canonical); S88 `CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE` (PASS, d_C finite on A_F, L10=L12=2.386138). The Connes distance migrated from the 32-cell lattice (S46 `DISTANCE-46`, S54 lattice/continuum) to the canonical A_F = ℂ⊕ℍ⊕M_3(ℂ) finite triple, where it is now an algebra-DEPENDENT state-pair functional in the **algebra-axis orthogonality K-counter** program (Corner II). The Martinetti-Mercati proportionality is instantiated as the finite-spectrum-identity conjecture. The continuum Connes distance "grows only modestly" while the lattice distance "grows exponentially (tracks 1/J_{C²})" (S55-4) — the disambiguation the doc lacks. | NEW-SINCE-AUTHORSHIP | §V Open Question #3 → carried-into-A_F section; Isomorphism 2 update |
| GAP-7 | **Open Question #1 (mass-variation sign) → addressed via S56/S58 mass_variation + S61 A-TENSOR.** `s56_mass_variation` (VARIATION-56, consumes `s54_tb_hamiltonian.npz`), `s58_mass_variation` (VARIATION-58), `s39_geodesic_mass` (GEOD-39). With the product O'Neill A=T=0 (GAP-3), the geometric mass-variation channel is NOT the expansion driver; the framework's expansion mechanism reframed entirely (see GAP-4 — transit, not a metric-mediated mass-variation). The PI-fabric prediction (DM from dispersion, DE from monotonic mixing) is the mature successor. | NEW-SINCE-AUTHORSHIP | §V Open Question #1 → addressed/superseded section |
| GAP-8 | **Isomorphism 5 (Gutzwiller-Selberg: stabilization↔dimensional-reduction) → the d_s spectral-dimension arc, culminating S92 vs CDT.** S53 `d_s=1.65`; S44 `spectral_dim_band` (BAND-44/DIMFLOW-44, "Lifshitz anomalous dimension `eta_eff=3.77`"); S61 `spectral_dimension_pair` (PAIR-61/PHONON-3); S63 `spectral_dimension` (DIMENSION-63); **S92 ad-hoc workshop `s92-adhoc-spectral-dimension-ds-flow-vs-cdt.md` (kk + landau, CONVERGED)**: `d_s(σ)=−2 d ln P/d ln σ`, the σ→0 Weyl asymptotic vs the windowed `d_s(σ_*)` at the fold are DISTINCT functionals, the impedance product `Z = ρ_E·v_g = const` (Sage-exact across the family `γ_E=1−1/n ∈ [1/2,1)`), and the fair "same-functional-same-scale" comparison to CDT. Memory: **z=2 EXACT from phonon bands; S57 z=3.68 RETRACTED** (finite-size + wrong d_s). This is now a permanent cross-pillar directive (`cross-pillar-bridge-corpus.md §24`; mirrored to `phononic-framing.md` + `cross-pillar-bridge-anatomy.md`). | NEW-SINCE-AUTHORSHIP (Isomorphism 5 hardened to directive) | Isomorphism 5 (rewrite with the d_s arc + z=2 + CDT directive); new §"Spectral dimension flow vs CDT" |
| GAP-9 | **Isomorphism 4 (taxonomy trap) → matured into the eight-pillar "fabric" / Ordered Veil framing + the algebra-axis orthogonality K-counter.** The S53 observation "any single-pillar label is a projection that discards information from the other seven" became (a) the THE ORDERED VEIL paradigm (GGE relic never thermalizes — integrable, not chaotic; permanent), and (b) the formal **algebra-axis orthogonality conjecture** (S87+, MANDATORY at K=3): spectrum-only functionals (algebra-INVARIANT) and state-pair functionals (algebra-DEPENDENT) are STRUCTURALLY ORTHOGONAL — the rigorous statement of "different projections cannot be conflated." | NEW-SINCE-AUTHORSHIP | Isomorphism 4 (upgrade observation → Ordered Veil + algebra-axis-orthogonality formalization) |
| GAP-10 | **The §VII cross-pillar bridge program (S82→S93) is the mature successor to "five isomorphisms".** The S53 doc identified 5 isomorphisms informally; the project built a formal apparatus: the **5-anatomy** (substrate-IS observable / laboratory-IN observable / bridge map / algebraic envelope / empirical anchor) + the **3-level structural-confidence ladder** (Level-1 cohomology-class identity / Level-2 L^{−α} envelope / Level-3 empirical anchor), with the joint-theorem 4-stage promotion pathway (Stage-0 workshop → Stage-1 candidate → Stage-2 two-axis independent verify → Stage-3 permanent). §VII.AH was the FIRST cross-axis joint theorem to reach STAGE-3-PERMANENT. This is the modern formal home of "cross-domain isomorphism." | NEW-SINCE-AUTHORSHIP | new §"From five isomorphisms to the §VII bridge program"; §VII Closing |
| GAP-11 | **NEW cross-domain isomorphism: BCS-Hamiltonian-as-universal-ancestor (S72).** Six predictions from ONE algebraic object across five pillars; CC dilution (χ_vac>0 from BCS concavity) and laminar flow (Re_GGE=0 from integrability) are logically independent, sharing the BCS Hamiltonian as common ancestor. This is a NEW isomorphism the S53 doc could not have stated — and it is the *deepest* version of "one operator, many faces". | NEW-SINCE-AUTHORSHIP | new §"New isomorphisms S54→S93" (Isomorphism 6) |
| GAP-12 | **NEW cross-domain isomorphism: the SU(1,1) three-way identity.** BCS squeeze (Pillar IV) + cosmological Bogoliubov (Pillar I) + Josephson phase (Pillar V) are the SAME SU(1,1) group element; `S_compound = S_spatial · S_BCS` by SU(1,1) multiplication (S70). Plus `R_BG = 1/cosh(2r)` (S93 W8-6 PASS) — the narrow-path pre/post-fold bridge-coefficient ratio = reciprocal SU(1,1) squeeze weight. | NEW-SINCE-AUTHORSHIP | new §"New isomorphisms S54→S93" (Isomorphism 7) |
| GAP-13 | **NEW: the six-layer causal structure (S70) + TWO sonic horizons.** Entry sonic horizon (τ~0.22, a_2 geometric, kinematic) + exit sonic horizon (τ~0.16, a_4 BCS condensation), white-hole interior between; the six-layer encoding maps the spectral-moment hierarchy a_0→a_2→a_4→a_6. This is the matured causal-hierarchy reading of the S53 "causal structure" face of `D_K`. | NEW-SINCE-AUTHORSHIP | §VI causal-architecture paragraph; the "causal structure" face of the central thesis |
| GAP-14 | **NEW: LQG/CDT cross-framework workshops (S92).** The S53 Closing invoked CDT (Paper 28, d_s→2 in UV), Strutinsky (1967), NCG (Paper 10) as "three communities, three decades, same discovery." The project then ran ACTUAL cross-framework comparisons (S92 LQG×phonon-first narrow-path workshop; S92 d_s-flow-vs-CDT) — these belong in the Closing, upgrading the rhetorical "three communities" into landed cross-framework verdicts (γ does not admit cutoff running per Paper 03 §VII; Regime II structural failure is substrate-likely). | NEW-SINCE-AUTHORSHIP | §VII Closing (upgrade rhetoric → landed cross-framework results) |
| GAP-15 | **DRIFT: τ quartet + canonical pins.** Doc carries `τ=0.2015` (speed-bump maximum) as if it were the fold; canonical `tau_fold=0.19` (S12/S42 CONST-FREEZE-42). The quartet 0.2015 (speed-bump max) / 0.190 (canonical fold) / 0.193878 (S59 N_pair=4 ED fold) / 0.15 (τ_0 epoch) are DISTINCT — disambiguate, do NOT overwrite. `c_Gold=0.915` confirmed canonical. `Gi=0.506` (Ginzburg ratio, Mott regime) confirmed. | DRIFTED-CLAIM | every τ mention + a τ-disambiguation callout |
| GAP-16 | **NEW: N_pair scaling fate.** The S53 doc's carry-forward gate #9 (pair-pair scattering at N_pair=2, the Mott-superfluid boundary) ran: `NPAIR2-CC-55`; S58 `THERM-ORDER-59` N_pair=3/4 ED at `tau_fold=0.193878`; pair-transfer `S_+(N) ~ (N+1)(1−N/16)/2` bosonic, <1% (PERMANENT). The N_pair=1 → N_pair>1 question the doc left open is closed. | NEW-SINCE-AUTHORSHIP | §IV carry-forward retrospective (#9) |

The executor's G1 gate extends this table to full domain coverage (expect the survey to find more — e.g.,
the S38 GGE permanence / KAM ε=0.037 quantitative update, the SA-LATT-OCC-54 → S57 occupied-spectral-action
landing, the Q-RAYCHAUDHURI-54 → S54 QA-Hawking conformal-time `η=∫dτ/a(τ)` result, the FIRAS-GGE-54
observability fate vs the current frozen-arrow falsifier program, and whether any S54-program gate has a
modern §VII registry slot).

---

## Wave 6 Decision Point Prerequisites

**None.** Wave 6 is independent (no upstream S{N-1} or intra-session prerequisite). It surveys the
knowledge base and expands one curated framework document. It does NOT consume any other Session-X wave's
output. (The only dependent wave is W9, which verifies all 8 expanded docs are mutually consistent — W9
consumes W6's OUTPUT, not the reverse.) Internally, the three gates are sequenced: G2 consumes the G1 gap
analysis; G3 reads the G2-expanded document. If a cited input file is missing at dispatch time, the gate
honestly closes per `.claude/rules/mechanical-closure-discipline.md` (`value='upstream_<reason>'`); all
three input files (the document, `canonical_constants.py`, `tools/knowledge.db`) are verified present at
plan-freeze.

### Split (per context §7 W6 + spawn directive): W6a §§I–II, W6b §III

The expansion is internally split into two halves so the executor can pace the comprehensive rewrite. Both
halves are produced under the SAME three gates (the split is an organizational discipline inside G2/G3, not
separate gate-IDs):

- **W6a** = §I (The Single Deepest Finding — the "one operator read three ways" central thesis) + §II (The
  Three Workshops Compared). The central-thesis face is updated with the six-layer causal structure (GAP-13),
  the A=T=0 product-submersion clarification (GAP-3), and the §VII-bridge-program maturation (GAP-10). The
  three-workshop comparison table is annotated with each workshop's downstream fate.
- **W6b** = §III (Cross-Workshop Isomorphisms — the five isomorphisms). Each of the five is updated to its
  S54→S93 status (PERMANENT theorem / carried-into-A_F / hardened-to-directive / matured-to-Ordered-Veil),
  and a NEW subsection adds Isomorphisms 6–7 (BCS-ancestor, SU(1,1) three-way) + the §VII-bridge-program
  framing. §IV (S54 program → retrospective), §V (four open questions → resolutions), §VI (Framework After
  S53 → Framework After S93), and §VII (Closing → landed cross-framework results) are covered across BOTH
  halves under the same gates.

The G1 gap analysis and the G3 reconciliation cover BOTH halves; G2 produces BOTH halves and the verdict's
`value=` field reports the per-half integration counts (W6a, W6b).

---

## §W6-1. WX-W6-1-AGGREGATE-DOMAIN-SURVEY

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W6-1-AGGREGATE-DOMAIN-SURVEY"
schema_version: "R3"
trigger: "[AUDIT]"
classification: "GEOMETRIC"
agent_type: "phonon-first-cosmologist"
hypothesis: "The cross-workshop-synthesis domain across all ~93 sessions — the central 'one operator read three ways' thesis, the S54 consolidated-program gates, the five cross-workshop isomorphisms, the four open questions, and the cross-pillar-bridge apparatus that succeeded them — can be mapped against the document's coverage, and the GAP (results the project knows but the document does not cover: each S54 gate's fate, each isomorphism's promotion/supersession, each open question's resolution, and NEW cross-domain isomorphisms established S54→S93) can be enumerated with KB citations across the pertinent entity classes (theorems / closed / gates / sessions / open / constants / equations / provenance)."

method:
  description: >
    Sweep the knowledge base BROADLY for the document's domain across S54->S93. The domain is cross-domain
    pattern detection / cross-pillar isomorphism / the unification of the eight pillars through the single
    D_K eigenvalue problem. Four survey axes, each a trace+search sweep:
      (A) S54-program-gate FATE axis: trace_entity each of {ED-SWEEP-54, SA-LATT-OCC-54, CONNES-LATT-54,
          BURES-CONNES-LATTICE-54, GEODESIC-DEVIATION-54, GUTZWILLER-SU3-54, SCALE-FACTOR-54,
          Q-RAYCHAUDHURI-54, FIRAS-GGE-54} + the 5 carry-forward gates (N_pair=2, modulus-fluctuation,
          tight-binding, integrability-breaking, full-modulus-dynamics). Record S54 outcome AND where the
          thread resolved downstream (S55-S93).
      (B) ISOMORPHISM FATE axis: trace_entity / search_knowledge each of the five {Strutinsky=O'Neill=saddle,
          Connes=Bures=Fisher, volume-preservation=CC-free=topological, taxonomy-trap, Gutzwiller-Selberg}.
          Classify each as PERMANENT-THEOREM / CARRIED-INTO-PROGRAM / HARDENED-TO-DIRECTIVE /
          MATURED-TO-PARADIGM / SUPERSEDED, with the promoting session + gate cited.
      (C) OPEN-QUESTION RESOLUTION axis: for each of the four S53 open questions (mass-variation sign,
          E_0-minimum existence, Bures-Connes relationship, 115-OOM CC gap), find the resolving result
          (gate / theorem / closed mechanism) and whether it CONFIRMED, REFUTED, or DISSOLVED the question.
      (D) NEW-ISOMORPHISM axis: search_knowledge for cross-domain connections established S54->S93 that the
          S53 doc could NOT have stated (BCS-as-universal-ancestor S72; SU(1,1) three-way identity S70/S93;
          six-layer causal structure S70; the §VII cross-pillar bridge program 5-anatomy+3-level S82-S93;
          LQG/CDT cross-framework workshops S92). These are the gap that makes the expansion COMPREHENSIVE,
          not merely current.
    Produce (a) a current whole-project STATE-OF-DOMAIN MAP organized by the four axes and (b) a GAP ANALYSIS
    -- every domain result the document does NOT yet cover, each row with its KB citation and a one-line
    "where it belongs in the document." This gate is FAILED if it only re-checks the document's existing
    claims (the document's existing claims are S53-frozen; re-checking them is the QA sub-layer, NOT the
    domain survey).
  producing_script: "computations/session-x/sx_w6_domain_survey.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator -- set-coverage of the domain + gap enumeration
operator:
  type: "set"
  form: >
    PASS iff (entity_classes_surveyed superset-of {theorems, closed, gates, sessions, open, constants,
    equations, provenance}) AND (survey_axes_covered == {A:S54-gate-fate, B:isomorphism-fate,
    C:open-question-resolution, D:new-isomorphism}) AND (|gap_rows| > 0 with every gap_row carrying a
    KB citation + a where-it-belongs tag) AND (every one of the 9 S54 decisive/high-value gates has a
    fate recorded) AND (every one of the 5 isomorphisms has a fate classification) AND (every one of the
    4 open questions has a resolution classification). The survey is a SET-COVERAGE predicate over the
    domain's entity classes AND the four survey axes, NOT a numerical threshold.

# (2) strict_PASS_boundary -- domain classes + axes surveyed + gap enumerated with citations
strict_PASS_boundary:
  value: "entity_classes_surveyed == 8 (all of {theorems, closed, gates, sessions, open, constants, equations, provenance}) AND survey_axes_covered == 4 (A,B,C,D) AND gap_rows >= 16 (the planner pre-survey floor; executor extends) AND every gap_row has (kb_citation != '' AND where_belongs != '' AND gap_tag in {NEW-SINCE-AUTHORSHIP, NEVER-COVERED, DRIFTED-CLAIM, PARADIGM-SHIFT}) AND s54_gate_fate_table covers all 9 decisive/high-value gates AND isomorphism_fate_table covers all 5 isomorphisms AND open_question_resolution_table covers all 4 questions"
  direction: ">="

# (3) boundary_reachable_analytically -- coverage-by-enumeration
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (the domain's pertinent entity classes + the four survey axes are a finite enumerable set; the gap is the set-difference between project-knowledge-in-domain and document-coverage; the S54-gate / isomorphism / open-question fate tables are finite closed enumerations of size 9, 5, 4 respectively)"

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
  domain_scope_definition: "cross-domain pattern detection / cross-pillar isomorphism / the unification of the eight pillars (acoustic-analogue / superfluid-cosmology / NCG-spectral-action / flat-band-BCS / Josephson-arrays / topological-solitons / spectral-dimension / KK-geometry) through the single finite Dirac operator D_K(tau) on the 32-cell Voronoi tessellation of (SU(3), g_Jensen); the 'one operator read three ways' (vacuum functional / shell-correction generator / causal structure); the S54 consolidated-program gates; the five cross-workshop isomorphisms; the four open questions; the §VII cross-pillar bridge apparatus (5-anatomy + 3-level + joint-theorem promotion) that formalized 'cross-domain isomorphism'"
  survey_axes: "[A: S54-program-gate FATE (9 decisive/high-value + 5 carry-forward), B: isomorphism FATE (5), C: open-question RESOLUTION (4), D: NEW-isomorphism (S54->S93 connections the S53 doc could not state)]"
  gap_taxonomy: "[NEW-SINCE-AUTHORSHIP (S54+ result not in doc), NEVER-COVERED (pre-S53 domain result the doc omitted), DRIFTED-CLAIM (doc claim superseded/disambiguation-needed, e.g. tau quartet / gradient-ratio conflation), PARADIGM-SHIFT (a result that dissolves rather than answers an S53 open question, e.g. E_0-minimum -> first-order-transit)]"
  s54_gate_enumeration: "{ED-SWEEP-54, SA-LATT-OCC-54, CONNES-LATT-54, BURES-CONNES-LATTICE-54, GEODESIC-DEVIATION-54, GUTZWILLER-SU3-54, SCALE-FACTOR-54, Q-RAYCHAUDHURI-54, FIRAS-GGE-54} (decisive+high-value, n=9) + {NPAIR2 pair-pair scattering, modulus-fluctuation delta_tau(K), 32-cell tight-binding, integrability-breaking corrections, full-modulus-dynamics BCS-speed-bump} (carry-forward, n=5)"
  isomorphism_enumeration: "{1: Strutinsky=O'Neill=saddle-point, 2: Connes=Bures=Fisher, 3: volume-preservation=CC-free=topological-rigidity, 4: taxonomy-trap-universal, 5: Gutzwiller-Selberg stabilization<->dimensional-reduction}"
  open_question_enumeration: "{1: mass-variation expansion sign, 2: does E_0(tau) have a minimum, 3: Bures-Connes relationship, 4: the 115-OOM CC gap}"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (plan-freeze snapshot; gate re-pins <computed-at-runtime>)"
  document_sha_prefreeze: "Phononic-Investigation.md @ SHA256 ad44e519410a840ebc4a24d9620a755b2586351f468fb03f687c24b6c90d80b7 (plan-freeze; gate re-pins <computed-at-runtime>)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]
  # NOTE: G1 does not modify the document; "document_post" == "document_pre" for this gate's content hash.
  # The content_sha256 pins the survey/gap artifact set the gate produces (state_of_domain_map + the four
  # axis fate-tables + gap_analysis written into the WP), which IS the gate's deliverable.

# (7) substitution_chain -- not required for the survey gate itself (no directional claim)
substitution_chain:
  required: false
  content: |
    G1 is a set-coverage + enumeration gate; it asserts no sign/direction/ratio claim. The directional /
    ratio claims it SURFACES (the gradient ratio 0.71-vs-1.30 disambiguation; the q(tau) -0.97->+0.81
    deceleration sign from SCALE-FACTOR-54; the Z = rho_E * v_g impedance product) are pre-registered for
    the G2 gate's substitution_chain, where they are written or retained. (See section W6-2 substitution_chain.)

# (8) input_files
input_files:
  document:
    path: "sessions/framework/Phononic-Investigation.md"
    sha256: "<computed-at-runtime>"   # plan-freeze: ad44e519410a840ebc4a24d9620a755b2586351f468fb03f687c24b6c90d80b7
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # plan-freeze: 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"   # ~80 MB; rebuilt by /weave --update; dynamic

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w6_domain_survey.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w6_domain_survey.npz"
    artifact_kind: "data"
    optional: true   # survey artifact set is recorded in the WP; npz optional (may store the gap-row + fate tables)
  plot:
    path: "computations/session-x/sx_w6_domain_survey.png"
    artifact_kind: "plot"
    optional: true   # no plot required for a survey gate
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W6-1-AGGREGATE-DOMAIN-SURVEY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-1. WX-W6-1-AGGREGATE-DOMAIN-SURVEY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"   # the KB query manifest lives here (context section 5 mandatory)
      - "State-of-Domain Map"
      - "Gap Analysis"
      - "S54 Program Gate-Fate Table"
      - "Isomorphism Fate Table"
      - "Open-Question Resolution Table"

# ---- Verdict rubric ----
PASS_meaning: >
  The cross-workshop-synthesis domain has been swept across all 8 pertinent entity classes AND the four
  survey axes (S54-gate-fate, isomorphism-fate, open-question-resolution, new-isomorphism); the gap between
  project-knowledge-in-domain and document-coverage is enumerated with >= 16 cited gap rows (planner floor;
  executor extends), each with a where-it-belongs tag and a gap tag; the S54 gate-fate table covers all 9
  decisive/high-value gates, the isomorphism-fate table covers all 5 isomorphisms, the open-question table
  covers all 4 questions. The comprehensiveness ENGINE has run -- G2 has a complete, cited integration
  target. Solution-space: the expansion's scope is now bounded and provenance-traced.
FAIL_meaning: >
  The survey only re-checked the document's existing (S53-frozen) claims (validation, not domain survey),
  OR the gap analysis lacks KB citations / where-it-belongs tags, OR an entity class or survey axis was
  skipped, OR any S54 gate / isomorphism / open question lacks a recorded fate. This means the
  comprehensiveness engine did not run; G2 would expand against an imagined rather than KB-grounded gap.
INFO_meaning: >
  Domain swept across all axes and gaps enumerated, but a pertinent entity class returned ZERO domain hits
  (e.g., no in-domain 'open' entities survived to S93 because all four S53 open questions resolved) -- a
  genuine emptiness recorded honestly, not a coverage failure. The gate fires INFO and documents the empty
  class with its (null) query, so G2 knows that region is truly clear (the four open questions are all
  resolved is itself a finding).

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w6_domain_survey.py"
    - "computations/session-x/sx_w6_domain_survey.npz (optional -- gap-row + fate tables)"
    - "sessions/session-x/session-x-w6-workingpaper.md (section W6-1)"
  estimated_time: "0.4-0.6 day (heavy KB sweep -- tens of queries across 8 entity classes x 4 survey axes, S54->S93; tracing 9 S54 gates + 5 isomorphisms + 4 open questions to their fates)"

substrate_framing: |
  GEOMETRIC. The domain is the cross-pillar unification thesis: that the finite Dirac operator D_K(tau) on
  the 32-cell Voronoi tessellation of (SU(3), g_Jensen) is ONE spectrum whose eigenvalues simultaneously set
  the Connes distances (metric/vacuum face), their occupation-weighted partial sums (Strutinsky shell
  correction / stabilization face), and their return-probability asymptotics (spectral dimension / causal
  face). The survey maps what the project now knows about how these three faces are algebraically coupled
  and how the five S53 isomorphisms (each a claim that two pillars share one formal structure) fared. The
  direction of explanation flows FROM D_K eigenvalues TOWARD the emergent physics of each pillar -- never
  the reverse. The 'taxonomy trap' (no single-pillar label captures the system) is itself the substrate-IS
  statement: the substrate IS the intersection of the eight projections, not any one of them. The survey
  verifies the domain still respects this and finds where the project formalized it (algebra-axis
  orthogonality; the §VII bridge anatomy).
```

---

## §W6-2. WX-W6-2-COMPREHENSIVE-EXPANSION

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W6-2-COMPREHENSIVE-EXPANSION"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "GEOMETRIC"
agent_type: "phonon-first-cosmologist"
hypothesis: "The cross-workshop-synthesis domain gap enumerated in G1 can be integrated into Phononic-Investigation.md -- rewriting the S54 program from a forward prospectus into a retrospective with each gate's fate, upgrading the five isomorphisms to their S54->S93 status (Strutinsky=O'Neill -> PERMANENT theorem; Connes=Bures=Fisher -> carried into the A_F finite-triple program; taxonomy-trap -> Ordered Veil + algebra-axis orthogonality; Gutzwiller-Selberg -> the d_s arc / z=2 / CDT directive), resolving the four open questions (E_0-minimum DISSOLVED into the first-order-transit paradigm; 115-OOM CC CLOSED by DILUTION-CC-66; Bures-Connes carried into A_F; mass-variation-sign superseded by the transit reframe), adding NEW isomorphisms (BCS-as-universal-ancestor; SU(1,1) three-way; six-layer causal structure; the §VII bridge program), and disambiguating the tau quartet and the 0.71-vs-1.30 gradient ratios -- in the cross-domain-pattern-detector authorial voice, such that the document reads as a current (S93) comprehensive synthesis. A minimal/cosmetic edit FAILS."

method:
  description: >
    THE DELIVERABLE. Substantially expand / rewrite Phononic-Investigation.md to integrate every material
    gap row from G1. The S53 doc is a forward-looking prospectus written at the END of S53; the rewrite
    converts it into a retrospective-AND-current synthesis. Concretely (W6a + W6b split):
      W6a (§I central thesis + §II three-workshop comparison):
        - §I (The Single Deepest Finding): KEEP the central insight (the 32x32 matrix = vacuum functional +
          shell-correction generator + causal structure, one spectrum read three ways) -- it is CONFIRMED and
          is the document's enduring contribution. DEEPEN it: the 'causal structure' face is now the
          SIX-LAYER causal architecture (GAP-13) with TWO sonic horizons (entry tau~0.22 a_2-kinematic; exit
          tau~0.16 a_4-BCS-condensation), the spectral-moment hierarchy a_0->a_2->a_4->a_6. Add the A=T=0
          product-submersion clarification (GAP-3): the three faces are coupled through the FIBER-INTERNAL
          Jensen decomposition, not the product submersion (whose O'Neill tensors vanish). Note that the
          'three faces are algebraically coupled' claim is now realized as 'D_K encodes metric, stabilization,
          AND causality through one eigenvalue problem' (a permanent cross-pillar bridge core).
        - §II (Three Workshops Compared): KEEP the comparison table; ADD a fate column / annotation to each
          row recording where that workshop's central result resolved (BLV-dead -> confirmed permanent, the
          condensate-free Connes route carried into A_F; Strutinsky-NCG -> PERMANENT theorem S57/S62;
          remnant-CC -> DILUTION-CC closure S66). Restate the cross-workshop architecture with the modern
          §VII-bridge framing.
      W6b (§III five isomorphisms + §IV-VII):
        - §III Isomorphism 1 (Strutinsky=O'Neill=saddle): UPGRADE from conjecture to PERMANENT cross-pillar
          theorem. Cite S57 (E_GS(fold)=-23.509 = E_smooth+delta_E_shell+E_pair) and S62 (delta_E_shell=-8.857).
          DISAMBIGUATE the two gradient ratios: 0.71 (smooth-vs-oscillating in the O'Neill/Strutinsky
          decomposition at the fold) vs 1.30 (BCS-condensation-vs-geometric-potential, the speed-bump, PROVEN
          S53). Add the A=T=0 clarification (the *product* O'Neill A-tensor vanishes; the Strutinsky=O'Neill
          content is the fiber-internal decomposition).
        - §III Isomorphism 2 (Connes=Bures=Fisher): UPDATE -- the Connes distance migrated from the 32-cell
          lattice to the canonical A_F = C+H+M_3(C) finite triple (S87 finite-spectrum-identity conjecture
          INFO 0.980; S88 subalgebra-restriction PASS d_C=2.386138). The Martinetti-Mercati proportionality
          is instantiated as the finite-spectrum-identity conjecture. Disambiguate lattice (exponential,
          tracks 1/J_{C^2}) vs continuum (modest growth) Connes distance (S55-4). Note Connes distance is now
          an algebra-DEPENDENT state-pair functional (Corner II) in the algebra-axis orthogonality program.
        - §III Isomorphism 3 (volume-preservation=CC-free=topological): UPDATE -- det(g)=const matured into
          the H2 theorem (tracelessness / volume-preserving TT, permanent); CC-free emergence confirmed via
          DILUTION-CC (a_0 self-tuning). Reconcile with the A=T=0 product-submersion result.
        - §III Isomorphism 4 (taxonomy trap): UPGRADE -- matured into (a) THE ORDERED VEIL paradigm (GGE never
          thermalizes; integrable not chaotic; KAM epsilon=0.037; permanent) and (b) the algebra-axis
          orthogonality K-counter (S87+, MANDATORY at K=3) -- the rigorous statement that single-pillar
          projections (spectrum-only algebra-INVARIANT vs state-pair algebra-DEPENDENT) cannot be conflated.
        - §III Isomorphism 5 (Gutzwiller-Selberg): REWRITE with the d_s arc: S53 d_s=1.65 -> S44 eta_eff=3.77
          Lifshitz -> S61/S63 -> S92 d_s-flow-vs-CDT (z=2 EXACT; S57 z=3.68 RETRACTED; impedance product
          Z = rho_E * v_g = const; sigma->0 Weyl asymptotic vs windowed d_s(sigma_*) DISTINCT; fair
          same-functional-same-scale CDT comparison). This is now a permanent cross-pillar directive.
        - NEW §III subsection "Isomorphisms established S54->S93": Isomorphism 6 (BCS-Hamiltonian-as-universal-
          ancestor, S72 -- 6 predictions from 1 algebraic object across 5 pillars), Isomorphism 7 (SU(1,1)
          three-way: BCS squeeze + cosmological Bogoliubov + Josephson phase, S70/S93; R_BG=1/cosh(2r)).
        - NEW §"From five isomorphisms to the §VII bridge program": the project formalized 'cross-domain
          isomorphism' into the 5-anatomy + 3-level ladder + joint-theorem 4-stage promotion (S82-S93); §VII.AH
          first STAGE-3-PERMANENT cross-axis joint theorem. This is the modern home of the S53 informal
          isomorphisms.
        - §IV (Converged S54 Program): REWRITE from prospectus into RETROSPECTIVE. Each of the 9 decisive/
          high-value gates annotated with its S54 outcome (ran -> migrated INFO at S81; SCALE-FACTOR-54 PASS)
          and where the thread resolved downstream. The 5 carry-forward gates likewise (N_pair=2 -> NPAIR2-CC-55,
          THERM-ORDER-59 N_pair=3/4; pair-transfer S_+(N) bosonic <1% permanent).
        - §V (What Remains Unresolved): REWRITE -- all four open questions RESOLVED. OQ#2 (E_0 minimum)
          DISSOLVED: tau=0.2015 is a MAXIMUM, stabilization is first-order transit / instanton, not a well
          (the framework's 'Friedmann wrong question'). OQ#4 (CC) CLOSED by DILUTION-CC-66 (0.01 OOM, ratio
          1.032). OQ#3 (Bures-Connes) carried into A_F. OQ#1 (mass-variation sign) superseded by the transit
          reframe + A=T=0. Retitle the section or split into "Resolved since S53" + any genuinely-still-open.
        - §VI (The Framework After S53): UPDATE to "The Framework After S93" -- fold in the paradigm shifts
          (transit not equilibrium; instanton not well; Ordered Veil; six-layer causal structure), the
          DILUTION-CC closure, the §VII bridge program, current canonical pins.
        - §VII (Closing): UPGRADE the rhetorical "three communities, three decades, same discovery" into the
          LANDED cross-framework results: the S92 LQG x phonon-first narrow-path workshop + the S92
          d_s-flow-vs-CDT comparison (gamma does not admit cutoff running; fair same-functional comparison).
      Across BOTH halves: disambiguate the tau quartet (0.2015 speed-bump-max / 0.190 canonical fold /
      0.193878 S59 ED fold / 0.15 tau_0) with a tau-disambiguation callout; refresh c_Gold=0.915, Gi=0.506.
    Drift-fixing happens here as the QA layer (every retained claim brought current). Substitution chains
    (per math-scripts.md) are written for the gradient-ratio disambiguation, the q(tau) deceleration sign,
    and the impedance product.
  producing_script: "computations/session-x/sx_w6_comprehensive_expansion.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator -- set: gap-integration (integrated union scoped-out = all G1 gaps)
operator:
  type: "set"
  form: >
    PASS iff (integrated_gaps union scoped_out_gaps == all_G1_material_gaps) AND (scoped_out_gaps each carry
    a one-line reason) AND (document_post is a substantial expansion: §IV rewritten prospectus->retrospective,
    all 5 isomorphisms updated to S54->S93 status, all 4 open questions resolved, NEW isomorphisms 6-7 + the
    §VII-bridge-program section added, tau quartet + gradient-ratio disambiguated) AND (no isomorphism left at
    conjecture status without its S93 fate). The predicate is set-equality (every G1 gap is accounted for)
    PLUS a substantiveness predicate (expansion, not cosmetic edit).

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "for every material gap row g in G1: (g in integrated) XOR (g in scoped_out with reason); AND (count of integrated gaps / count of material gaps) reported per-half (W6a, W6b) in verdict value=; AND document_post substantially larger and restructured (new sections present for: NEW isomorphisms 6-7, the §VII-bridge-program section, the spectral-dimension/CDT directive; §IV converted to retrospective; §V all-four-resolved); AND each of the 5 isomorphisms carries a fate tag in {PERMANENT-THEOREM, CARRIED-INTO-A_F, HARDENED-TO-DIRECTIVE, MATURED-TO-PARADIGM}; AND each of the 4 open questions carries a resolution tag in {RESOLVED, CLOSED, CARRIED, DISSOLVED}; AND the tau-quartet AND the 0.71-vs-1.30 gradient-ratio disambiguations both present"
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (gap set from G1 is finite; integrated union scoped-out = gap set is a decidable set-equality over the G1 enumeration; the 5-isomorphism and 4-open-question fate-tagging are finite closed checks)"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A -- synthesis/expansion gate (prose synthesis + fate-table integration, not a numerical scan)"

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
  GPU_path: "N/A -- prose/synthesis authoring + SHA; no linear algebra"
  half_split: "W6a={§I central thesis (one-operator-three-ways + six-layer causal + A=T=0 clarification), §II three-workshop comparison + fate annotations}; W6b={§III five isomorphisms updated + NEW isomorphisms 6-7 + §VII-bridge-program section, §IV prospectus->retrospective, §V four-open-questions resolved, §VI Framework-After-S93, §VII Closing landed cross-framework}"
  isomorphism_fate_tags: "[PERMANENT-THEOREM (iso 1), CARRIED-INTO-A_F (iso 2), HARDENED-TO-DIRECTIVE (iso 5), MATURED-TO-PARADIGM (iso 3 -> H2/CC-free, iso 4 -> Ordered-Veil/algebra-axis-orthogonality)]"
  open_question_resolution_tags: "[OQ1 mass-variation-sign -> SUPERSEDED-BY-TRANSIT-REFRAME, OQ2 E_0-minimum -> DISSOLVED (first-order-transit), OQ3 Bures-Connes -> CARRIED-INTO-A_F, OQ4 115-OOM-CC -> CLOSED (DILUTION-CC-66)]"
  tau_disambiguation_pin: "tau=0.2015 (speed-bump local MAXIMUM, S53) != tau_fold=0.190 (canonical, S12/S42 CONST-FREEZE-42) != tau_fold=0.193878 (S59 N_pair=4 ED) != tau_0~0.15 (epoch). c_Gold=0.915 (canonical). Gi=0.506 (Ginzburg ratio, Mott regime). Do NOT collapse the quartet."
  gradient_ratio_disambiguation_pin: "ratio 0.71 = smooth-vs-oscillating gradient in the O'Neill/Strutinsky decomposition at the fold (memory); ratio 1.30 = |dE_cond/dV_KK| BCS-condensation-vs-geometric-potential = the speed-bump (PROVEN S53, Phononic-framework-hypothesis.md). DISTINCT quantities; the doc's '1.30' in Isomorphism-1 context must be split."
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (plan-freeze; gate re-pins <computed-at-runtime>)"
  document_sha_prefreeze: "Phononic-Investigation.md @ SHA256 ad44e519410a840ebc4a24d9620a755b2586351f468fb03f687c24b6c90d80b7 (plan-freeze; gate re-pins <computed-at-runtime>; gate re-reads the G1-recorded gap_analysis as its integration target)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_pre", "state_of_domain_map", "gap_analysis", "canonical_constants_snapshot", "kb_query_manifest"]
  content_sha256_inputs: ["document_post"]
  # The content_sha256 pins the EXPANDED document (document_post), which is the gate's deliverable. The
  # audit_sha256 pins the inputs that bound the expansion (the pre-document + the G1 survey/gap artifacts +
  # the canonical snapshot + the KB query manifest) so the expansion is provenance-traced to the survey.

# (7) substitution_chain -- REQUIRED (the expansion writes/retains directional + ratio claims)
substitution_chain:
  required: true
  content: |
    Three directional/ratio claims are written or retained in the expansion; each gets an explicit chain per
    math-scripts.md §"Double-Check Logic Before Compute" in the WP G2 section.

    CLAIM A -- "the two gradient ratios are DISTINCT (0.71 != 1.30) and measure different things":
      Step 1: ratio_Strutinsky := |dF_smooth/dtau| / |d(delta_F_shell)/dtau| at tau_fold   [O'Neill/Strutinsky decomposition; memory + S57/S62 landings]
      Step 2: ratio_BCS := |dE_cond/dV_KK| at the fold                                      [BCS-condensation vs geometric potential; PROVEN S53, Phononic-framework-hypothesis.md]
      Step 3: numerator of ratio_Strutinsky is the SMOOTH spectral-action gradient (monotone, dS/dtau=+58,673 sign-positive); numerator of ratio_BCS is the pairing-energy gradient (a DIFFERENT spectral object, the condensation energy)   [definitions are over different functionals]
      Step 4: the two ratios share neither numerator nor denominator; they are gradients of distinct
              decompositions (smooth-vs-oscillating energy WITHIN the spectral action vs condensation-vs-geometry
              ACROSS two potentials)
      Step 5: ratio_Strutinsky = 0.71 (oscillating < smooth at fold) and ratio_BCS = 1.30 (condensation >
              geometric at fold) are therefore both correct and NON-INTERCHANGEABLE
      Conclusion: the document MUST report both with their distinct definitions; collapsing them (the S53
              doc's implicit conflation) is the drift. [direction: both ratios retained, disambiguated]

    CLAIM B -- "SCALE-FACTOR-54 gives DECELERATION post-fold (q transitions from negative to positive)":
      Step 1: q(tau) := -a*a''/(a')^2, the deceleration parameter   [definition; a(tau) = mean Connes distance, SCALE-FACTOR-54]
      Step 2: S54 QA-Hawking recorded q(tau) running from -0.97 (quasi-de Sitter, accelerating) to +0.81 (decelerating)   [S54 QA-Hawking workshop, conformal time eta=int dtau/a(tau)]
      Step 3: sign(q) flips - to + across the transit   [from the recorded endpoints -0.97 < 0 < +0.81]
      Step 4: q<0 => acceleration (early/near-fold); q>0 => deceleration (late)   [sign convention read-off]
      Conclusion: the Connes-route effective scale factor accelerates near the fold then decelerates -- the
              expansion is NOT eternal de Sitter; retain with the recorded endpoints. [direction: q sign flip - -> +]

    CLAIM C -- "the impedance product Z = rho_E * v_g is CONSTANT across the d_s family":
      Step 1: rho_E(E) := (1/(pi n)) A^{-1/n} (E-E_0)^{-(1-1/n)}   [energy-axis DOS, S92 d_s-vs-CDT eq]
      Step 2: v_g(E) := n A^{1/n} (E-E_0)^{(1-1/n)}                 [group velocity, same workshop]
      Step 3: Z = rho_E * v_g = (1/(pi n)) A^{-1/n} (E-E_0)^{-(1-1/n)} * n A^{1/n} (E-E_0)^{(1-1/n)}   [product]
      Step 4: simplify: the n cancels, A^{-1/n} A^{1/n}=1, (E-E_0)^{-(1-1/n)} (E-E_0)^{(1-1/n)}=1  =>  Z = 1/pi
      Conclusion: Z is E-INDEPENDENT (= 1/pi, const) for the whole family gamma_E = 1-1/n in [1/2,1); the
              impedance is a CONSISTENCY CHECK (Z=const), not a lock -- retain per the S92 directive. [direction: Z constant]

# (8) input_files
input_files:
  document:
    path: "sessions/framework/Phononic-Investigation.md"
    sha256: "<computed-at-runtime>"   # plan-freeze: ad44e519410a840ebc4a24d9620a755b2586351f468fb03f687c24b6c90d80b7
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # plan-freeze: 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"   # ~80 MB; rebuilt by /weave --update; dynamic
  g1_gap_analysis:
    path: "sessions/session-x/session-x-w6-workingpaper.md"
    sha256: "<computed-at-runtime>"   # the G1 section's gap_analysis + fate tables are the integration target

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w6_comprehensive_expansion.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w6_comprehensive_expansion.npz"
    artifact_kind: "data"
    optional: true   # the expanded document IS the deliverable; npz optional (may store integrated/scoped gap-row ledger)
  plot:
    path: "computations/session-x/sx_w6_comprehensive_expansion.png"
    artifact_kind: "plot"
    optional: true   # no plot for a synthesis-expansion gate
  expanded_document:
    path: "sessions/framework/Phononic-Investigation.md"
    artifact_kind: "expanded_document"
    must_contain:
      - "S93"                                    # the document now references the current era
      - "DILUTION-CC"                            # GAP-5 integrated
      - "z = 2"                                  # GAP-8 spectral-dimension z=2 integrated (or "z=2")
      - "Ordered Veil"                           # GAP-9 taxonomy-trap -> Ordered Veil integrated
      - "algebra-axis orthogonality"             # GAP-9 formalization integrated
      - "SU(1,1)"                                # GAP-12 new isomorphism integrated
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W6-2-COMPREHENSIVE-EXPANSION:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-2. WX-W6-2-COMPREHENSIVE-EXPANSION"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
      - "Gap Integration Ledger"                 # integrated XOR scoped-out, per gap row
      - "Substitution Chain"                     # the three directional/ratio chains (A, B, C)

# ---- Verdict rubric ----
PASS_meaning: >
  Every material gap row from G1 is integrated into the document OR explicitly scoped-out with a one-line
  reason; the document is substantially expanded and restructured (§IV converted prospectus->retrospective,
  all 5 isomorphisms tagged to their S54->S93 fate, all 4 open questions resolved/closed/carried/dissolved,
  NEW isomorphisms 6-7 + the §VII-bridge-program section added, the spectral-dimension/CDT directive folded
  in); the tau quartet and the two gradient ratios are disambiguated; the synthesis reads as a current (S93)
  comprehensive cross-domain-pattern-detection document in the author's voice. Solution-space: the document
  now reflects the whole project's current cross-pillar-unification understanding.
FAIL_meaning: >
  The edit is cosmetic/minimal (drift-fixes only, no domain expansion), OR a material gap row is neither
  integrated nor scoped-out, OR an isomorphism is left at conjecture status without its S93 fate, OR an open
  question is left "open" when the project resolved it, OR the NEW isomorphisms / §VII-bridge section are
  absent. This means the deliverable (a comprehensive S93 synthesis) was not produced -- the wave reduced to
  the QA sub-layer it was explicitly told is NOT the task.
INFO_meaning: >
  The expansion is substantial and the document is current, but a specific gap row was scoped-out for a
  defensible reason (e.g., a domain result belongs more naturally in a sibling phononic* document -- the
  six-layer causal detail in Phononic-C-Causality, the full CC closure in Phononic-to-Cosmos -- and is
  cross-referenced rather than duplicated). The scope-out is recorded with its reason in the Gap Integration
  Ledger; cross-document coverage is W9's concern.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w6_comprehensive_expansion.py"
    - "computations/session-x/sx_w6_comprehensive_expansion.npz (optional -- gap-integration ledger)"
    - "sessions/framework/Phononic-Investigation.md (EXPANDED in place -- the deliverable)"
    - "sessions/session-x/session-x-w6-workingpaper.md (section W6-2)"
  estimated_time: "1.0-1.4 day (the full-wave comprehensive rewrite: §IV prospectus->retrospective, 5 isomorphisms updated + 2 new, 4 open questions resolved, §VI/§VII brought to S93, all in authorial voice)"

substrate_framing: |
  GEOMETRIC. The expansion keeps and deepens the document's enduring thesis -- one finite Dirac operator
  D_K(tau) on the 32-cell Voronoi tessellation of (SU(3), g_Jensen), read three ways (metric / stabilization
  / causal) -- and brings it to the project's current understanding: the three faces are now known to be one
  bridge core (D_K encodes metric, stabilization, AND causality through one eigenvalue problem); the causal
  face is the six-layer architecture with two sonic horizons (a_2-kinematic entry, a_4-condensation exit);
  the stabilization face's E_0-minimum question DISSOLVED into the first-order-transit paradigm (no well --
  the substrate complexifies through a phase transition, it does not roll into a potential minimum); the
  five informal isomorphisms became permanent theorems (Strutinsky=O'Neill), carried structures (Connes
  distance on A_F), directives (d_s/z=2/CDT), and paradigms (Ordered Veil + algebra-axis orthogonality). The
  direction of explanation flows FROM D_K eigenvalues TOWARD the emergent physics; the rewrite restores this
  wherever the S53 prose drifted toward container-thinking. Every retained number is brought to its canonical
  pin (tau quartet, c_Gold, Gi, the two gradient ratios).
```

---

## §W6-3. WX-W6-3-RECONCILE-VERIFY

```yaml
# ---- Identity (6 fields) ----
gate_id: "WX-W6-3-RECONCILE-VERIFY"
schema_version: "R3"
trigger: "[VERIFY]"
classification: "GEOMETRIC"
agent_type: "phonon-first-cosmologist"
hypothesis: "Every claim in the EXPANDED Phononic-Investigation.md (retained + newly added) is current (no stale claim), framing-compliant (substrate-IS direction per phononic-framing.md -- isomorphisms framed as the substrate's structural identities, not GR/QFT explaining the substrate), provenance-traced (each S54-gate fate / isomorphism status / open-question resolution / canonical pin cited to a theorem / closed mechanism / gate / canonical_constants entry), and a_n^{regulator}-tagged where a Seeley-DeWitt coefficient is cited; the stale/unframed/untraced set is EMPTY."

method:
  description: >
    QA OVER THE EXPANDED DOCUMENT (the embedded validation layer). Re-read the G2-expanded
    Phononic-Investigation.md end-to-end and verify three predicate families, building the
    stale/unframed/untraced SET (PASS = empty):
      (1) CURRENCY: no claim contradicts a current canonical value or a post-S53 supersession. Specifically
          check: tau quartet not collapsed (0.2015 != 0.190 != 0.193878 != 0.15); c_Gold=0.915, Gi=0.506
          current; the two gradient ratios (0.71, 1.30) both present and distinctly defined; E_0=MAXIMUM not
          minimum (OQ2 dissolved); CC CLOSED (DILUTION-CC-66, 0.01 OOM); d_s reading current (z=2, NOT the
          retracted z=3.68; sigma->0 Weyl asymptotic vs windowed d_s(sigma_*) distinct). Each S54 gate's
          fate matches the KB (migrated INFO / PASS / downstream-resolved). Each isomorphism's fate tag
          matches the KB.
      (2) FRAMING (IS-not-IN per phononic-framing.md): each isomorphism is framed as the SUBSTRATE'S
          structural identity (the substrate IS the intersection of the eight projections), NOT as GR / QFT /
          thermodynamics governing the substrate. The 'one operator read three ways' must flow D_K eigenvalues
          -> spectral moments -> emergent physics. Flag any container-thinking sentence (e.g., 'the area
          theorem implies', 'Einstein's equations govern', 'fields ON the compact space K', 'space expands').
          The taxonomy-trap framing must read substrate-IS (single-pillar label = projection that discards the
          other seven), not 'the system is hard to classify'.
      (3) PROVENANCE: each fate / status / resolution / pin is traced -- a permanent theorem (registry),
          closed mechanism (DILUTION-CC-66), gate verdict (with gate-ID), or canonical_constants entry. A gap
          row's integration without a KB citation is "imagined" per the derivative-output discipline. Any
          Seeley-DeWitt a_n citation carries a regulator tag (a_n^{zeta} / a_n^{Pauli-Villars} / a_n^{Mellin}
          / a_n^{lattice} / a_n^{cutoff}) per regulator-pin-discipline.md.
    Emit the stale/unframed/untraced SET. PASS iff empty.
  producing_script: "computations/session-x/sx_w6_reconcile_verify.py"

# ---- PRDR Checklist (8 items) ----

# (1) operator -- set: the stale/unframed/untraced set, PASS = empty
operator:
  type: "set"
  form: >
    PASS iff (stale_claims union unframed_claims union untraced_claims union untagged_a_n == empty_set). The
    predicate is set-emptiness over the EXPANDED document's claims across three independent QA families
    (currency, IS-not-IN framing, provenance) plus the a_n regulator-tag check.

# (2) strict_PASS_boundary
strict_PASS_boundary:
  value: "|stale_claims| == 0 AND |unframed_claims| == 0 AND |untraced_claims| == 0 AND |untagged_a_n_citations| == 0, evaluated over the document_post produced by W6-2; AND the tau-quartet not collapsed; AND the d_s reading is z=2 (NOT z=3.68); AND OQ2 reads E_0-MAXIMUM/transit (NOT open minimum question); AND OQ4 reads CC-CLOSED (DILUTION-CC-66)"
  direction: "="

# (3) boundary_reachable_analytically
boundary_reachable_analytically:
  bool: true
  proof_ref: "coverage-by-enumeration (the document's claim set is finite and enumerable; the stale/unframed/untraced set is a decidable subset under the three QA predicate families + the a_n-tag regex)"

# (4) reachable_rationals
reachable_rationals:
  includes_integer_mesh: false
  mesh_density: "N/A -- synthesis/QA gate (claim-by-claim verification, not a numerical scan)"

# (5) machinery_pin_map
machinery_pin_map:
  N_eval: "N/A -- QA gate (no numerical evaluation; the stale/unframed/untraced count is a coverage observable)"
  L_max: "N/A"
  scan_range: "N/A"
  step_size: "N/A"
  tolerance: "N/A -- set-emptiness predicate, not a numerical comparison"
  scheme: "reconcile-verify-v1"
  convention: "stale-unframed-untraced-set-emptiness"
  random_seed: "N/A -- deterministic"
  GPU_path: "N/A -- claim verification + SHA; no linear algebra"
  qa_predicate_families: "[currency (no claim contradicts current canonical / post-S53 supersession), framing (IS-not-IN per phononic-framing.md: isomorphisms = substrate structural identities, not GR/QFT governing the substrate), provenance (each fate/status/resolution/pin cited to theorem/closed/gate/canonical_constants)]"
  a_n_regulator_tag_set: "[a_n^{zeta}, a_n^{Pauli-Villars}, a_n^{Mellin}, a_n^{lattice}, a_n^{cutoff}] per regulator-pin-discipline.md; bare a_n FORBIDDEN in any NEW Seeley-DeWitt citation"
  container_thinking_flag_set: "['area theorem implies', 'Einstein equations govern', 'fields on the compact space', 'space expands', 'particles created in curved spacetime', 'summing over geometries'] per phononic-framing.md error-pattern table"
  currency_checklist: "[tau-quartet-not-collapsed, c_Gold=0.915, Gi=0.506, gradient-ratios-0.71-and-1.30-distinct, E_0-MAXIMUM-not-minimum, CC-CLOSED-DILUTION-CC-66, d_s-z=2-not-z=3.68, sigma->0-Weyl-vs-windowed-d_s-distinct, each-S54-gate-fate-matches-KB, each-isomorphism-fate-matches-KB]"
  canonical_constants_snapshot: "computations/_shared/canonical_constants.py @ SHA256 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17 (plan-freeze; gate re-pins <computed-at-runtime>)"
  document_sha_postexpansion: "Phononic-Investigation.md @ SHA256 <computed-at-runtime> (reads the W6-2 document_post; NOT the plan-freeze pre-document)"

# (6) audit_discriminators
audit_discriminators:
  audit_sha256_inputs: ["document_post", "currency_checklist", "framing_checklist", "provenance_checklist", "canonical_constants_snapshot"]
  content_sha256_inputs: ["stale_unframed_untraced_set"]
  # G3 reads the EXPANDED document (document_post from W6-2) and produces the stale/unframed/untraced SET as
  # its content deliverable. The audit_sha256 pins the document-under-review + the three QA checklists + the
  # canonical snapshot.

# (7) substitution_chain -- not required for the QA gate itself; it VERIFIES the chains W6-2 wrote
substitution_chain:
  required: false
  content: |
    G3 asserts no new sign/direction/ratio claim; it VERIFIES that the directional/ratio claims W6-2 retained
    or wrote (the gradient-ratio disambiguation, the q(tau) deceleration sign, the Z = rho_E * v_g impedance
    product) each carry a complete substitution chain per math-scripts.md and that the read-off direction in
    the expanded document matches the chain's conclusion. A retained directional claim WITHOUT a chain, or
    with a chain whose conclusion contradicts the document's read-off, is added to the stale/unframed set.

# (8) input_files
input_files:
  document:
    path: "sessions/framework/Phononic-Investigation.md"
    sha256: "<computed-at-runtime>"   # the W6-2-EXPANDED document (document_post), NOT the plan-freeze pre-document
  canonical_constants:
    path: "computations/_shared/canonical_constants.py"
    sha256: "<computed-at-runtime>"   # plan-freeze: 30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17
  knowledge_db:
    path: "tools/knowledge.db"
    sha256: "<computed-at-runtime>"   # ~80 MB; dynamic; for provenance re-verification of cited fates

# ---- Output artifacts ----
output_artifacts:
  script:
    path: "computations/session-x/sx_w6_reconcile_verify.py"
    artifact_kind: "script"
    must_contain:
      - "from canonical_constants import"
      - "append_verdict"
  data:
    path: "computations/session-x/sx_w6_reconcile_verify.npz"
    artifact_kind: "data"
    optional: true   # the stale/unframed/untraced set is recorded in the WP; npz optional (may store the per-claim ledger)
  plot:
    path: "computations/session-x/sx_w6_reconcile_verify.png"
    artifact_kind: "plot"
    optional: true   # no plot for a QA gate
  verdict_line:
    path: "computations/session-x/sx_gate_verdicts.txt"
    artifact_kind: "verdict_line"
    must_contain: "^WX-W6-3-RECONCILE-VERIFY:.* audit_sha256=[a-f0-9]{64}"
    companion_row_required: true
    schema_v2_3tuple_required: false
  wp_section:
    path: "sessions/session-x/session-x-w6-workingpaper.md"
    artifact_kind: "wp_section"
    section_anchor: "### §W6-3. WX-W6-3-RECONCILE-VERIFY"
    must_contain:
      - "\\*\\*Status\\*\\*:.*COMPLETED"
      - "\\*\\*Verdict\\*\\*:.*(PASS|FAIL|INFO)"
      - "\\*\\*Output Artifacts\\*\\*"
      - "\\*\\*MCP Pre-Compute Audit\\*\\*"
      - "Currency Check"
      - "Framing Check"
      - "Provenance Check"

# ---- Verdict rubric ----
PASS_meaning: >
  The expanded document carries zero stale claims (all currency checks pass: tau quartet intact, gradient
  ratios distinct, E_0 maximum/transit, CC closed, d_s z=2), zero unframed claims (every isomorphism reads
  substrate-IS, no container-thinking sentence), zero untraced claims (every fate/status/resolution/pin is
  KB-cited), and zero bare a_n citations. The expanded synthesis is current, framing-compliant, and
  provenance-traced. Solution-space: the document is a clean, authoritative S93 cross-pillar-synthesis
  artifact ready for the W9 cross-document consistency sweep.
FAIL_meaning: >
  The stale/unframed/untraced set is non-empty: some claim contradicts a current canonical value (e.g., tau
  quartet collapsed, d_s still at z=3.68, E_0 still framed as an open minimum question), OR a sentence
  inverts the substrate-IS direction (GR/QFT explaining the substrate), OR a fate/resolution lacks a KB
  citation, OR a Seeley-DeWitt a_n is cited bare. The QA layer caught a defect; route it to a W6-2 fix
  (in-session per fix-in-session-never-defer.md), then re-run G3.
INFO_meaning: >
  The document is current, framed, and traced, but a borderline framing call was made (e.g., a heritage
  citation to CDT/Strutinsky/NCG as conceptual framing -- admissible per substrate-first-canonical-sourcing
  §(i) -- vs a canonical replacement). The call is documented in the Framing Check with its rationale so W9
  can confirm cross-document consistency of the framing convention.

# ---- Effort + framing ----
effort:
  files_created:
    - "computations/session-x/sx_w6_reconcile_verify.py"
    - "computations/session-x/sx_w6_reconcile_verify.npz (optional -- per-claim QA ledger)"
    - "sessions/session-x/session-x-w6-workingpaper.md (section W6-3)"
  estimated_time: "0.4-0.6 day (claim-by-claim QA over the expanded synthesis across three predicate families + the a_n-tag sweep)"

substrate_framing: |
  GEOMETRIC. The QA gate enforces the substrate-IS direction over the whole expanded synthesis: the five (now
  seven) isomorphisms must each read as the substrate's OWN structural identity -- two pillars sharing one
  formal structure because the substrate IS that structure, not because an external theory (GR, QFT,
  thermodynamics) imposes it. The taxonomy-trap, in particular, is the cleanest substrate-IS statement in the
  document (the substrate IS the intersection of the eight pillar projections; any single-pillar label
  discards information from the other seven) and must not drift into "the system is hard to classify"
  (container-thinking, as if the system sat IN a classification space). The currency check binds every
  retained number to its D_K-eigenvalue-derived canonical pin; the provenance check binds every fate to a
  landed gate / theorem / closed mechanism. The direction of explanation -- D_K eigenvalues -> spectral
  moments -> emergent physics -> the isomorphism -- is the gate's central invariant.
```

---

## Wave 6 → Wave 9 Decision Point

Wave 6 produces the EXPANDED `Phononic-Investigation.md` plus its three verdict lines. **W9
(cross-document consistency + coverage closeout) consumes W6's OUTPUT**, not the reverse. The branching W9
reads from W6:

- **All three W6 gates PASS** → the expanded `Phononic-Investigation.md` enters the W9 SHARED-CONSTANT-MATRIX
  gate (cross-check the τ quartet, `c_Gold=0.915`, `Gi=0.506`, `CC_OOM=115.5`, `tau_fold=0.19`, `z=2`, and the
  DILUTION-CC closure against the other 7 expanded docs — esp. `Phononic-to-Cosmos` (CC closure, W3),
  `Phononic-C-Causality` (six-layer causal structure, two sonic horizons, W4), and
  `Phononic-framework-hypothesis` (gradient ratio 1.30, the five-isomorphism framing, W1)) and the
  COVERAGE-CONSISTENCY gate (the five-isomorphism / §VII-bridge framing must be coherent across docs).
- **W6-2 FAIL (cosmetic edit / unintegrated gap)** → re-dispatch W6-2 with the specific unintegrated gap rows
  named (the G1 gap analysis is the integration target; fix in-session per `fix-in-session-never-defer.md`).
  Do NOT advance to W9 with an under-expanded document.
- **W6-3 FAIL (stale/unframed/untraced claim)** → fix the named claim in `Phononic-Investigation.md`
  in-session (per `fix-in-session-never-defer.md`), re-run W6-2's content SHA + W6-3. The verdict file
  retains both lines per absolute verdict permanence (Option A `supersedes` tag if a corrective W6-3 line is
  emitted).
- **W6-2 INFO (gap scoped-out to a sibling doc)** → record the scope-out + cross-reference in the Gap
  Integration Ledger; flag it for W9 so the cross-document coverage sweep confirms the scoped-out content
  lives in its sibling doc (e.g., the full six-layer causal detail in `Phononic-C-Causality`; the full CC
  closure apparatus in `Phononic-to-Cosmos`). W6 owns the cross-pillar-SYNTHESIS framing of these results;
  the sibling docs own the domain detail — W9 confirms the division is clean and the cross-references resolve.

The cross-pillar isomorphisms this wave touches (Strutinsky=O'Neill, Connes=Bures=Fisher, the d_s/CDT
directive, BCS-as-ancestor, SU(1,1) three-way) are registered cross-pillar bridge content — W9 verifies they
are framed identically (5-anatomy + 3-level where a registry slot exists) in `Phononic-Investigation` and in
the sibling docs that also cite them.

---

## Wave 6 Machinery-Enumeration Pin

Aggregate of all three gate `machinery_pin_map` entries (per `epistemic-discipline.md §"Pre-Registration
Completeness"` PRDR; read by `_yaml_gate_validator.py` for sig_4 of the v3 closure ladder).

| Gate | scheme | convention | survey/QA scope | GPU_path | random_seed |
|:-----|:-------|:-----------|:----------------|:---------|:------------|
| WX-W6-1 (SURVEY) | `aggregate-domain-survey-v1` | `kb-cited-gap-enumeration` | 8 entity classes × 4 survey axes (S54-gate-fate / isomorphism-fate / open-question-resolution / new-isomorphism); 9 S54 gates + 5 isomorphisms + 4 open questions enumerated | N/A (KB reads + SHA) | N/A — deterministic |
| WX-W6-2 (EXPAND) | `comprehensive-expansion-v1` | `gap-integrated-or-scoped` | W6a (§I–II) + W6b (§III–VII); isomorphism fate-tags + open-question resolution-tags; τ-quartet + gradient-ratio disambiguation pins | N/A (prose/synthesis authoring + SHA) | N/A — deterministic |
| WX-W6-3 (VERIFY) | `reconcile-verify-v1` | `stale-unframed-untraced-set-emptiness` | 3 QA predicate families (currency / framing / provenance) + a_n regulator-tag sweep + container-thinking flag set | N/A (claim verification + SHA) | N/A — deterministic |

**Shared pins** (all three gates):
- `canonical_constants.py` snapshot @ SHA256 `30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17` (plan-freeze; each gate re-pins `<computed-at-runtime>`).
- `tools/knowledge.db` (~80 MB; dynamic, rebuilt by `/weave --update`; `<computed-at-runtime>`).
- Verdict file: `computations/session-x/sx_gate_verdicts.txt` (canonical path per `gate-verdicts.md`).
- Closure script per gate: `computations/session-x/sx_w6_{slug}.py` — loads doc + canonical snapshot + survey/gap artifacts, computes dual SHA, `append_verdict`. The closure script is MECHANICAL (SHA + verdict); the intellectual work (the survey, the gap analysis, the comprehensive expansion) is the executor's, recorded in the WP + the survey/gap artifacts + the expanded document itself.
- No GPU / no linear algebra in any W6 gate (`GPU_path: N/A` uniformly); these are synthesis/survey/QA gates. No random seed (deterministic KB reads + prose). No `N_eval` / `L_max` / `scan_range` / `step_size` / `tolerance` (set-coverage / set-equality / set-emptiness predicates, not numerical comparisons).

**Canonical-pin disambiguation table** (the QA layer pins these; G3 verifies them present + distinct):

| Symbol | Value | Meaning | Provenance | Do NOT confuse with |
|:-------|:------|:--------|:-----------|:--------------------|
| `tau` (speed-bump) | 0.2015 | local MAXIMUM of E_0 / the speed-bump | PROVEN S53 (Phononic-framework-hypothesis.md) | the fold |
| `tau_fold` | 0.190 | canonical van Hove fold | S12/S42 CONST-FREEZE-42 | the speed-bump max |
| `tau_fold` (S59 ED) | 0.193878 | N_pair=4 exact-diagonalization fold | S59 THERM-ORDER-59 | the canonical 0.190 |
| `tau_0` | ~0.15 | late-time epoch | framework epoch | the fold |
| `c_Gold` | 0.915 M_KK | Goldstone band velocity | canonical | — |
| `Gi` | 0.506 | Ginzburg ratio (Mott regime) | P3 permanent | — |
| ratio_Strutinsky | 0.71 | smooth-vs-oscillating gradient (O'Neill/Strutinsky decomp at fold) | memory / S57/S62 | ratio_BCS |
| ratio_BCS | 1.30 | \|dE_cond/dV_KK\| (condensation-vs-geometric, the speed-bump) | PROVEN S53 | ratio_Strutinsky |
| `CC_OOM` | 115.5 | CC order-of-magnitude gap (now CLOSED) | S66 DILUTION-CC-66 (0.01 OOM, ratio 1.032) | "unresolved" |
| `z` (dynamical exponent) | 2 (EXACT) | phonon-band dynamical exponent | memory (S57 z=3.68 RETRACTED) | z=3.68 |

---

## Wave 6 Input-SHA Ledger

Every input file the three W6 gates consume, with expected SHA-256 per `gate-verdicts.md`. Static files
have precomputed plan-freeze hashes; dynamic inputs are `<computed-at-runtime>`. Cross-checked at plan-freeze
by `_plan_upstream_pin_validator.py`.

| Input file | Consumed by | Plan-freeze SHA-256 | Runtime pin |
|:-----------|:-----------|:--------------------|:------------|
| `sessions/framework/Phononic-Investigation.md` | G1 (pre), G2 (pre → expands), G3 (post) | `ad44e519410a840ebc4a24d9620a755b2586351f468fb03f687c24b6c90d80b7` | `<computed-at-runtime>` (G3 reads the G2-expanded `document_post`) |
| `computations/_shared/canonical_constants.py` | G1, G2, G3 | `30b33df33bba087d55abef1b628abd33b850f52e61ddec7d013ca0b311ea8a17` | `<computed-at-runtime>` |
| `tools/knowledge.db` | G1 (survey), G3 (provenance re-verify) | dynamic (~80 MB; rebuilt by `/weave --update`) | `<computed-at-runtime>` |
| `sessions/session-x/session-x-w6-workingpaper.md` (G1 gap_analysis) | G2 (integration target) | dynamic (produced by G1) | `<computed-at-runtime>` |

**Plan-freeze input-existence verification** (per `mechanical-closure-discipline.md`): the two static inputs
(`Phononic-Investigation.md`, `canonical_constants.py`) are verified present at the SHAs above at plan-freeze
(2026-05-25). `tools/knowledge.db` is present (queried live during the planner pre-survey — 22 queries across
search_knowledge / trace_entity / get_constant / query_entity). The G1 WP section is produced by G1 itself
(G2's dependency on it is intra-wave sequential, not an upstream-session prerequisite). No input is blocked;
no gate is expected to mechanically close. If at dispatch time any input is absent, the affected gate
honestly closes per `mechanical-closure-discipline.md` (`value='upstream_<reason>'`, FAIL/PRE-REG-INC,
never PASS).

**KB query manifest (planner pre-survey, reproduced in the G1 WP MCP Pre-Compute Audit block; executor
extends)**: `trace_entity(ED-SWEEP-54)`, `trace_entity(Strutinsky O'Neill)`, `trace_entity(Connes distance
Bures metric)`, `trace_entity(spectral dimension flow)`, `trace_entity(GUTZWILLER-SU3)`,
`trace_entity(DILUTION-CC-66)`, `trace_entity(CORRECTION-74 A-tensor O'Neill)`, `search_knowledge(Strutinsky
shell correction O'Neill A-tensor)`, `search_knowledge(Connes Bures Fisher Martinetti Mercati)`,
`search_knowledge(32 cell Voronoi tight-binding pair band ED E_0 minimum fold)`, `search_knowledge(spectral
dimension d_s z=2 CDT return probability)`, `search_knowledge(z=2 Lifshitz retracted z=3.68)`,
`search_knowledge(O'Neill A-tensor geodesic deviation mass variation sign)`, `search_knowledge(SCALE-FACTOR-54
Connes scale factor)`, `search_knowledge(quantum Raychaudhuri FIRAS GGE suppression)`, `search_knowledge(Bures
Connes proportional Martinetti Mercati A_F finite triple S87 S88)`, `search_knowledge(BCS Hamiltonian universal
ancestor SU(1,1) squeeze five pillars)`, `search_knowledge(gradient ratio shell correction 0.71 1.30 dS/dtau)`,
`search_knowledge(E_0 minimum maximum tau fold first-order transit instanton)`, `get_constant(tau_fold)`,
`get_constant(c_Gold)`, `query_entity(sessions, 54)`, `query_entity(sessions, 92)`.

---

**End of Session-X Plan — Wave 6 (cross-workshop synthesis / the 32×32 operator read three ways).** The
deliverable is a comprehensively EXPANDED `Phononic-Investigation.md` that reads as a current (S93)
cross-pillar-unification synthesis; validation (G3) is the embedded QA layer. Owner: `phonon-first-cosmologist`
(the document's author-specialist). Independent wave (no upstream prerequisite); W9 consumes its output.
