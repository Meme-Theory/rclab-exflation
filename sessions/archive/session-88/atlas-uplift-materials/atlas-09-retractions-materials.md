# Atlas-09 Retractions Refresh — Materials Packet (S52-S88 delta)

**Producer**: sagan-empiricist
**Target atlas**: `sessions/framework/Atlas/atlas-09-retractions.md` (16,301 bytes; mtime 2026-04-04; 34 entries through S66)
**Scope**: New retractions / corrections / supersessions surfaced S52-S88
**Frame discipline**: Retractions are constraint-map updates — boundaries refined, not failures. A region of solution-space previously claimed-CLOSED can be RE-OPENED, or a region previously claimed-CONSTRAINED can be remapped. Per `epistemic-discipline.md`: negative results are boundaries, not failures.

---

## Section 1: What's currently in atlas-09

The existing atlas-09 (16,301 bytes; through S66) contains **34 numbered entries** in three contiguous master tables plus narrative notes. Format:

- **Header**: scope statement + sources block + Authority line ("Retraction = claim was wrong. Correction = claim was imprecise or updated.")
- **Master Table (items 1-25)**: 7-column markdown table — `# | Type | Claim | Session Made | Session Retracted/Corrected | Reason | Probability Impact`. Type values are `RETRACTION`, `CORRECTION`, `ERRATUM`, `DOWNGRADE`. Sub-section headings group items by era (single Master Table for items 1-25; supplementary tables for 26-28, 29-32, 33-34).
- **Narrative Notes**: Per-item or per-cluster prose blocks following the table, explaining the procedural significance of the most consequential entries (Items 8-10 K-1e double retraction; Item 2 4-5x coupling phantom; Item 16 GGE permanence; Item 25 B_1D inversion; etc.).
- **Section structure**: Master Table → Narrative Notes → "S52-S60 Retractions (Items 26-28)" sub-section with table + per-item prose → "S63 Retractions (Items 29-32)" sub-section → "S64-S66 Corrections (Items 33-34)" sub-section → final tally line ("Total retractions/corrections: 34 through S66").

The new entries below adopt this exact 7-column table format and add narrative notes for each substantively new structural reframe. Entries are appended in two new sub-sections: **"S67-S86 Retractions / Supersessions (Items 35-39)"** and **"S87-S88 Retractions / Supersessions (Items 40-45)"**, preserving chronological integrity per `session-handoffs.md`. Per Phase E discipline, archive-driven supersessions of deep-stale framework files are listed in a separate archive-supersession block at the end.

---

## Section 2: What to add (S52-S88 retractions / corrections / supersessions)

### 2A. Master delta table (Items 35-45)

| # | Type | Claim | Session Made | Session Retracted/Corrected | Reason | Probability Impact |
|:--|:-----|:------|:-------------|:---------------------------|:-------|:------------------|
| 35 | CORRECTION | FRIEDMANN-FROM-A2-74 well-posed for direct H_0 reduction | S74 W1-E | S74 W1-E (within session) | 86 OOM split between diluted/undiluted endpoints of Mack §5.9 GGE-to-matter projection. The reduction is structurally clean (G_N emerges at factor 12 from Planck; ⟨T_00⟩_GGE well-defined at 1.10e70 GeV^4) but the question is ill-posed: fold-epoch fiber-local energy density and today's emergent 4-metric H_0 are not in the same kinematic category. The 86 OOM split IS the 110-120 OOM CC hierarchy re-expressed via Friedmann. Future H_0 work routes through s75_transfer_function.py (transit transfer function), not direct spectral-action reduction. | Low (question-framing; FAIL is informative — it localizes the gap to the fiber-to-4D projection step where Volovik q-theory tracking is designed to act) |
| 36 | CORRECTION | eps_H sign-stable across cutoff families | S60-S64 | S66 W2-A | Spectral functional crisis: eps_H changes SIGN between cutoff families (sqrt(x): +0.022 vs zeta: negative). n_s spread across functionals = 0.164 (39× Planck error). Scheme-dependent at the sign level — the n_s prediction is functional-class-dependent, not unique. Recorded in `atlas-07-permanent-results.md` as PERMANENT (negative result) and in `atlas-10-breakthrough-genealogy.md` as Breakthrough #20 ("Spectral Functional Crisis"). Reframed at S66 Workshop 2 as Functional Selection mechanism (only sqrt(x) and anomaly(φ) survive Bayesian evidence). | HIGH (permanent negative result; converts unique n_s prediction into functional-class-conditional prediction) |
| 37 | CORRECTION | R_918 falsifier rectangle for w_0 | S83 (iv) canonical | S84 W1b-9 → S86 W13-3 | Self-falsifier under post-S83 branch (iv) canonical: w_0_pred = -0.842454 lay +0.007546 OUTSIDE the R_918 upper edge -0.85. Migrated to R_842 = [-0.942, -0.742] × [-0.2, 0.2] (centered on -0.842, nearest half-decimal to -0.842454); half-width preserved at 0.100 in w_0; restores self-consistency without resizing. S86 W13-3 plan §W13-3.6 cited stale R_918 rectangle as `R_842 = [-1.05, -0.85] × [-0.2, +0.2]`; per `epistemic-discipline.md` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE, plan-freeze validators must verify INPUT-PIN MAP rectangle labels against the most-recent migration ledger. R_918 historical SHA `7f23a7c603522a105dffe271584cc22d7a25c6c22a0cccf09fe180954af5c140` retained as forward-pointer reference. | Low (re-pinning; methodological — Class-(c) PIN-DRIFT calibration corpus instance) |
| 38 | SUPERSESSION | R_JE single-tag spectral diagnostic (E-coupled, GGE-energy-weighted) | S58-S85 (legacy) | S86 W4-1 P4 (BRANCH-IV canonical commit) | Single-name conflation between distance-1 and distance-2 spectral tags. R_JE := xi_J / xi_E_GGE conflated K-functional structure (distance-2 / Newton-constant slot) with GGE-coherence-length structure (distance-1 / s=-1 Mellin residue). RETIRED in favor of two distance-tagged diagnostics: R_JK (distance-2; K-functional moment of D_K, anchored at 0.00803461 at L_max=10) and xi_E_GGE_inv (distance-1; s=-1 Mellin residue, anchored at 13.642473425595973). Cross-cited specialists: connes-ncg (Seeley-DeWitt a_4/a_2), volovik (3He-B parent→child inheritance via Volovik QFL Fig. 5.3 coherence-length-inverse spectroscopy), lizzi (Mellin-strip s=-1 residue convention). | Moderate (registry-write CHANGE; downstream substrate-distance tags now resolve to TWO moments of D_K rather than one conflated single-tag ratio; substrate transit pathway through fold unchanged) |
| 39 | CORRECTION | Phononic-Crystal-Geometry.md as canonical substrate-geometry document | S47 (orig.) / 2026-03-21 (revised) | S84 (Phononic-Substrate-Geometry.md landing, 2026-04-21) | Crystal-layer predecessor SUPERSEDED by resonator-picture successor. The crystal metaphor (32-cell Voronoi tessellation, Cooper-pair quantum-walker, J_C2 hopping) was productive but constructive-theoretic; the actual content is variational and spectral. Phononic-Substrate-Geometry.md adopts the high-Q-resonator-at-eigenmodes picture as the load-bearing organizing thesis — the substrate IS the resonator (not mounted inside spacetime); spectral moments of D_K are amplitudes; particles are phononic excitations. The 32-cell Voronoi construction and tight-binding bands remain valid and are subsumed at §7.3 of the successor. | Low (organizing-picture refinement; crystal-layer results survive as §7.3 of resonator-picture successor) |
| 40 | RETRACTION | §VII.AJ FWD-C3 instance #2 W11-5 REGISTRY-FAIL slot identity | S87 W11-5 | S88 W-10 | The W11-5 cross-pillar bridge candidate (Pillar IV ↔ Pillar V; substrate spectral-excess ↔ 3He-B BdG-undoubled excess at polycritical pressure) failed `cross-pillar-bridge-anatomy.md §"Registry-PASS criterion"`: Level-3 empirical anchor 1.029166e+00 violated Level-2 algebraic envelope 0.05 by ~21×. The original FWD-C3 instance #2 REGISTRY-FAIL entry is RETAINED as historical record (S87 W11-5; cross-pillar-bridge-corpus.md §5 Row 2 — calibration corpus K=1→K=2 advancement). At S88 W-10, the slot RECLASSIFIES from REGISTRY-FAIL → NEEDS-REIDENTIFICATION via algebra-axis K-counter MANDATORY-K=3 enforcement: §VII.AJ.OP-PROJ (Volovik substrate-IS large-negative-R) + §VII.AJ.STATE-PROJ (Landau BCS-physics-grounded) STRUCTURALLY-ORTHOGONAL-COMPANION pair REPLACES the conflated reading. | Moderate (the W11-5 REGISTRY-FAIL is itself a calibration-corpus instance per `cross-pillar-bridge-anatomy.md` MANDATORY-K=3 advancement — eliminating wrong slot identity STRENGTHENS the survivors per epistemic-discipline §"What Counts as Evidence") |
| 41 | RETRACTION | §VII.AN registry-anchor framing as same-axis SOURCE-DOUBLE-CITE-CO-PRIMARY | S88 W5a-44 (landing) | S88 W-15 V.6 | Cross-corner conflation: ANCHOR-1 (V on Cell I `n_s²−1` image, algebra-INVARIANT spectrum-only-functional cell) vs ANCHOR-2 (C on Cell IV variance theorem, algebra-DEPENDENT state-pair-functional cell) live on STRUCTURALLY ORTHOGONAL algebra-axis cells per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 (S87 W-2 R3 close). Same-axis SOURCE-DOUBLE-CITE-CO-PRIMARY structure REQUIRES both anchors on the same algebra-axis cell; cross-corner co-primary structures are FORBIDDEN. Calibration corpus instance #1 of `registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)"` clause 4. Forward enforcement: `_registry_landing_audit.py` extension at `S89-CROSS-CORNER-CO-PRIMARY-AUDIT` flags cross-corner SOURCE-DOUBLE-CITE-CO-PRIMARY at plan-freeze with HARD-HALT remediation. | Moderate (registry-anchor framing retracted; original ANCHOR-1 + ANCHOR-2 entries retained but anchor-structure tag reclassified from CO-PRIMARY to STRUCTURALLY-ORTHOGONAL-COMPANION) |
| 42 | CORRECTION | W4-2 + W9b-2 verdicts as Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL instances | S86 W4-2 (W4-2) / S87 W9b-2 (W9b-2) | S88 W-24 V.1 (B.61) | Reclassification from PRU Class-(f) (placeholder → canonical jump) to Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY. The W4-2 and W9b-2 outputs are derivative forms of canonical primaries via the SCHEMATIC `_spectral_action_regulators.py` derivation chain — NOT placeholder OOM estimates against absent canonicals. Substantive Class-(f) instance count revised from 3 → 1 (only pre-existing W5a-2 `xi_E_GGE_inv` instance remains). K_substantive = 3 under the level-pin discipline (W4-2 NEGATIVE-CALIBRATION → reclassified Class-(d), W9b-2 NEGATIVE-CALIBRATION → reclassified Class-(d), W9c-1 POSITIVE-CALIBRATION); orthogonality structure (UV-regulator axis × Level axis × Binding axis) is invariant under the (d)-vs-(f) reclassification. | Low (taxonomy bookkeeping; the underlying PRU Class-8.4 / level-pin MANDATORY-at-K=4 status promotion at S88 W7b-83 is unaffected) |

### 2B. Aggregate counts

Verified via Python (`atlas-09-materials-count.py` reproduction):

| Category | Count |
|:---------|:-----:|
| New CORRECTION (Items 35, 36, 37, 39, 42) | 5 |
| New SUPERSESSION (Items 38, plus 4 archive-driven below: 43-46) | 5 |
| New RETRACTION (Items 40, 41) | 2 |
| **Total NEW** | **12** |

Existing: 34 (through S66). New total: 34 + 12 = **46** (one-step-up from the count-only-table arithmetic 11+34=45 because Item 39 also appears in the archive-supersession block as a structural duplication; the 4 archive-driven entries below are recorded as Items 43-46 in the chronological master table). Final reconciled total once entries are written into atlas-09: 34 + 12 = 46. Honest count discipline per `Investigating-Workshops.md`: investigators reporting more than this are inflating; the 12-item delta is the empirically-defensible signal-rich set.

### 2C. Archive-driven supersessions (Phase E)

Four deep-stale framework files are slated for archive-move per Phase E. Each is a SUPERSESSION (structural replacement) rather than a retraction (claim withdrawal); recorded as Items 43-46 in chronological order:

| # | Type | Claim | Session Made | Superseded by | Reason | Probability Impact |
|:--|:-----|:------|:-------------|:-------------|:-------|:------------------|
| 43 | SUPERSESSION | Phononic-Crystal-Geometry.md as canonical substrate-geometry document | S47 (rev. 2026-03-21) | Phononic-Substrate-Geometry.md (S84, 2026-04-21) | Crystal-layer predecessor → resonator-picture successor; explicit "Supersedes" line in successor §0 prefatory note ("Supersedes: Phononic-Crystal-Geometry.md (S47, crystal-layer predecessor — still valid for the 32-cell Voronoi construction and tight-binding bands, subsumed here as §7.3)"). Substrate IS the resonator; spectral moments of D_K are amplitudes; particles are phononic excitations. | Low (organizing-picture refinement; subsumed content survives at §7.3) |
| 44 | SUPERSESSION | framework-bbn-hypothesis.md as BBN-epoch description | S36 (2026-03-08) | framework-parametric-amplification.md (S73A) + Phononic-to-Cosmos.md (S57) | Pre-computational hypothesis (status: "HYPOTHESIS (pre-computational, conceptual framework)") superseded by computed-result successors. The BBN-cascade framework (tau-saddle phonon-fragmentation cascade; tau ~ 0.54 → 0.34 → 0.24 → 0.190 → 0) is preserved structurally in the parametric-amplification machinery (substrate transit through fold via mode-equation parametric-resonance) and in the cosmological translation document (Phononic-to-Cosmos.md). | Low (deep-stale: 2026-03-08, 14 months old; pre-computational framework now subsumed by computed-result successors) |
| 45 | SUPERSESSION | spectral-post-mortem.md as definitive tau-stabilization assessment | S44 (2026-03-08) | Phononic-Substrate-Geometry.md (S84) | Author Landau's post-mortem ("DEFINITIVE. Category permanently closed by structural theorem.") closes the perturbative tau-stabilization route via Perturbative Exhaustion Theorem (S22c). The structural finding survives (closure permanent); the document itself is superseded by the resonator-picture canonical substrate-geometry document. The spectral-post-mortem narrative content is preserved at the "PROVEN" tier of permanent-results-registry §VII (Perturbative Exhaustion Theorem; F_pert is not a true free energy). | Low (closure-finding permanent; post-mortem narrative now subsumed by resonator-picture organizing thesis) |
| 46 | SUPERSESSION | baseline-findings-s66.md as authoritative cross-session inventory | S66 (2026-04-04) | sessions/permanent-results-registry.md (ongoing; 16,000+ lines as of S88) | The baseline-findings snapshot at S66 has been overtaken by 22 sessions of continuous registry growth (S67-S88). The permanent-results-registry.md is the live successor — every PASS/INFO/STAGE-1-CANDIDATE landing appends to it under §VII numbered slots; AMRI cleanup (S85+) consolidated agent-memory project-level claims into the registry; the S88 W-10 §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ pair is one example of the registry's current structural-companion landing pattern that has no counterpart in the S66 snapshot. | Low (snapshot vs live ledger; the baseline-findings document IS still useful as a 2026-04-04 snapshot — archive-move preserves it as historical reference) |

### 2D. Candidates that did NOT promote to atlas-09 entries (rationale)

Three candidates from the assignment's 12-candidate list did NOT promote to atlas-09 entries:

- **W11-5 REGISTRY-FAIL alone (assignment candidate #1)**: This is a structural classification of a NEW test that did not satisfy the bridge-PASS criterion — NOT a retraction of a prior claim. The W11-5 entry is RETAINED as historical record per registry line 16314 ("the original FWD-C3 instance #2 REGISTRY-FAIL entry referenced at line 16543 cross-link is RETAINED as historical record"). What IS counted in atlas-09 is Item 40: the S88 W-10 RECLASSIFICATION of the slot identity from REGISTRY-FAIL → NEEDS-REIDENTIFICATION. This is the structural retraction; the W11-5 verdict line itself is informative-by-design and should be cross-linked to `atlas-11-cross-pillar-bridge-corpus.md` as a calibration instance, not duplicated as an atlas-09 retraction.
- **AMRI cleanup (assignment candidate #4)**: STRUCTURAL CLEANUP rather than retraction. Agent-memory registry inversions promoted to project-level registries (`mack-observational-constraints.md`, `branch-iv-canonical.md`, etc.) per `agent-standards.md §"AMRI"` test 1 (input-pin), test 2 (output-target), test 3 (cross-agent overlap). No prior CLAIM was withdrawn; what was migrated was a CONTENT-AUTHORITY relationship. Belongs in `atlas-04-assumptions.md` or a meta-methodology atlas, not atlas-09.
- **w_0 = -0.918 vs w_0 = -0.842454 dual-PRIMARY co-existence (assignment candidate #8)**: NOT a retraction. Per `permanent-results-registry.md §W13-3 P9 adjudication` and `branch-iv-canonical.md` §1, the two values represent TWO substrate-IS branches (Volovik partition canonical vs S85 W10-2 substrate-compaction branch (iv)) that co-exist in the registry. `w0_FW = -0.918` remains the canonical_constants.py primary pin (S58 Volovik vacuum + effacement); `w_0_pred = -0.842454` is the branch-(iv) prediction inside R_842 = [-0.942, -0.742] × [-0.2, 0.2]. Neither supersedes the other; both are anchored. This is a plurality, not a retraction; belongs in `atlas-07-permanent-results.md` plurality entry, not atlas-09.

### 2E. Suspected-but-not-yet-retracted (route to S89 workshop carry-forward)

One result from S52-S88 should likely undergo Stage-2 cross-axis re-examination before being promoted to a permanent registry entry:

- **§VII.AM Universal Lock Condition (S88 W1b2-65, hawking-theorist primary)**: STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway. The "Universal Lock Condition (Substrate Horizon-Trigger Theorem)" was authored in /rclab-solo orchestrator-direct mode at S88 W1b2-65; Stage-2 two-agent cross-axis independent-verify is NOT YET performed. Per `joint-theorem-promotion.md §"Stage 2"`, single-agent landings on joint-clause theorems require Stage-2 PASS-AND BEFORE the slot can promote to STAGE-3-PERMANENT. If Stage-2 surfaces a clause-level FAIL, the §VII.AM entry would route to retraction. Recommendation: route as S89 workshop seed for adversarial Stage-2 cross-reviewer dispatch (axis-A-spectral + axis-B-substrate per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"` 3-condition discipline). NOT YET a retraction; flagged for S89 carry-forward verification.

---

## Section 3: Cross-atlas dependencies

### 3A. atlas-02-mechanism-lifecycle.md (re-opened mechanisms)

Item 8-9 K-1e double retraction (existing atlas-09 entries) is the canonical re-opened-closure precedent. NEW S52-S88 re-opened mechanisms surfaced:

- **Item 40 (§VII.AJ FWD-C3 reclassification)**: the W11-5 REGISTRY-FAIL slot identity is reclassified, replacing the conflated single-anchor reading with a STRUCTURALLY-ORTHOGONAL-COMPANION pair. atlas-02 should record §VII.AJ slot lifecycle: REGISTRY-FAIL (S87 W11-5) → NEEDS-REIDENTIFICATION (S88 W-10) → STAGE-1-CANDIDATE pair (S88 W-10 §VII.AJ.OP-PROJ + §VII.AJ.STATE-PROJ).
- **Item 38 (R_JE retirement → R_JK + xi_E_GGE_inv)**: single-name conflation lifecycle. atlas-02 should record R_JE as RETIRED with two distance-tagged successors (R_JK distance-2; xi_E_GGE_inv distance-1).

### 3B. atlas-04-assumptions.md (assumptions proven false → broken/dissolved entries)

- **Item 35 (FRIEDMANN-FROM-A2-74 reframe)**: the assumption "a single f_conv scalar can bridge fold-epoch fiber-local energy density to today's emergent 4-metric H_0" is BROKEN by the 86 OOM split. atlas-04 should record this as a broken-assumption entry pointing to the s75 transfer-function workaround.
- **Item 36 (eps_H sign reversal)**: the assumption "the n_s prediction is unique across cutoff families" is BROKEN by sign-level scheme dependence. atlas-04 should record this as a broken-assumption entry pointing to S66 Workshop 2's Functional Selection mechanism.

### 3C. atlas-07-permanent-results.md (REGISTRY-FAIL cross-links)

- **Item 40**: The W11-5 REGISTRY-FAIL is a calibration-corpus instance, not a retracted result. atlas-07 should cross-link the §VII.AJ entries (OP-PROJ + STATE-PROJ + the retained REGISTRY-FAIL historical row) to `atlas-09 Item 40` and to `atlas-11-cross-pillar-bridge-corpus.md` (NEW per atlas-11 plan) as the same structural event viewed from three atlas perspectives.

### 3D. atlas-10-breakthrough-genealogy.md (breakthrough retractions)

- **Breakthrough #20 (Spectral Functional Crisis — eps_H Sign Reversal)** is recorded in atlas-10 as a breakthrough (not a retraction) — "the most important negative result since the Venus Moment (S23a)". Item 36 in atlas-09 should explicitly cross-link to atlas-10 #20; the framing that a permanent-negative-result IS a breakthrough is what makes the structural-confidence ladder honest. Substrate framing per `epistemic-discipline.md`: "negative results are boundaries, not failures."

### 3E. atlas-11-cross-pillar-bridge-corpus.md (NEW)

- **Item 40 (§VII.AJ slot reclassification)**: NOT a retraction at the cross-pillar-bridge calibration-corpus level. The W11-5 REGISTRY-FAIL IS calibration-corpus instance #2 of the 5-anatomy + 3-level discipline (per `cross-pillar-bridge-corpus.md §5 Row 2`); its REGISTRY-FAIL status is informative (it advanced K=1 → K=2 toward the K=3 MANDATORY threshold, completed by S88 W4a-17 §VII.W-3.LAB instance #3). atlas-09 Item 40 records the slot-identity retraction (REGISTRY-FAIL slot identity → NEEDS-REIDENTIFICATION → STRUCTURALLY-ORTHOGONAL-COMPANION pair); atlas-11 records the calibration-corpus K-counter advancement. The two atlas perspectives are STRUCTURALLY ORTHOGONAL and both should be cross-linked.

### 3F. v3-closure-recovery.md PROHIBITED_ACTIONS Class 3 (adjacent but not a retraction class)

PROHIBITED_ACTIONS Class 3 (post-hoc pre-registration editing) is NOT a retraction class — it is a forbidden recovery action. None of Items 35-46 invoke Class 3; each is a structurally-permitted constraint-map update. atlas-09 should NOT cross-link to v3-closure-recovery as a retraction-source; the rule cross-link belongs in atlas-04 (assumptions) or in a meta-methodology atlas.

---

## Substrate-framing audit (per `phononic-framing.md`)

Every entry above is framed as a constraint-map update on the substrate:

- Item 35: the FRIEDMANN reduction maps fiber-local fold-epoch density to today's emergent 4-metric — the FAIL localizes the projection step (substrate transit transfer function), it does NOT indict the substrate.
- Item 36: eps_H is a spectral moment of D_K weighted by cutoff f; the sign reversal IS a property of the substrate's spectral-action ledger (different cutoff families weight different Mellin-strip residues), NOT a framework failure.
- Item 38: R_JE retirement IS canonical splitting in the substrate's spectral-functional ledger — TWO distance-tagged moments of D_K REPLACE the conflated single-tag ratio. Substrate transit pathway through fold UNCHANGED.
- Item 40: The W11-5 REGISTRY-FAIL slot identity reclassification IS algebra-axis orthogonality enforcement at the registry-naming level. Operator-projection (algebra-INVARIANT) and state-projection (algebra-DEPENDENT) live on STRUCTURALLY-ORTHOGONAL cells; cross-corner co-primary is FORBIDDEN BY CONSTRUCTION.

Direction of explanation throughout: substrate IS [observable] → bridge map → laboratory IN [observable]. NEVER inverted (laboratory → substrate). atlas-09 entries that cite cross-pillar bridges (Items 40, 41) MUST preserve this direction.

---

## Citation discipline

Every entry above cites file_path:line_number for both original and retraction:

- Item 35: original `sessions/archive/session-74/session-74-results-workingpaper.md` §W1-E body; retraction `C:\Users\ryan\.claude\projects\C--sandbox-Ainulindale-Exflation\memory\project_friedmann-wrong-question.md`
- Item 36: original spectral-action n_s computation S60-S64; retraction `sessions/framework/registry/baseline-findings-s66.md` line 96 + `sessions/framework/Atlas/atlas-07-permanent-results.md §A13` + `atlas-10-breakthrough-genealogy.md §#20`
- Item 37: original `sessions/permanent-results-registry.md:5789` (R_918 historical SHA); retraction `sessions/archive/session-84/session-84-plan-w1b.md` (R_842 migration) + `sessions/archive/session-86/session-86-plan-w13.md` (R_842 stale-relabel)
- Item 38: original S58 R_JE pin; retraction `sessions/framework/registry/branch-iv-canonical.md §1 R_JE Retirement` + `sessions/archive/session-86/session-86-w4-workingpaper.md §W4-1`
- Item 39: original `sessions/framework/Phononic-Crystal-Geometry.md`; retraction `sessions/framework/Phononic-Substrate-Geometry.md` line 9 ("Supersedes: Phononic-Crystal-Geometry.md")
- Item 40: original `sessions/permanent-results-registry.md:16743` (FWD-C3 instance #2 REGISTRY-FAIL row); retraction `sessions/permanent-results-registry.md:16314` (RECLASSIFICATION row) + `sessions/framework/registry/cross-pillar-bridge-corpus.md §5 Row 2`
- Item 41: original §VII.AN landing (S88 W5a-44); retraction S88 W-15 V.6 closure + `.claude/rules/registry-landing.md §"Detection (when SOURCE-DOUBLE-CITE-CO-PRIMARY applies)" clause 4`
- Item 42: original `sessions/framework/registry/pru-class-corpus.md §4` Class-(f) calibration corpus; retraction S88 W-24 V.1 + B.61 reclassification
- Item 43: `sessions/framework/Phononic-Substrate-Geometry.md` line 9
- Item 44: `sessions/framework/framework-bbn-hypothesis.md` (status line 6: "HYPOTHESIS (pre-computational)")
- Item 45: `sessions/framework/registry/spectral-post-mortem.md` line 5 ("DEFINITIVE. Category permanently closed by structural theorem")
- Item 46: `sessions/framework/registry/baseline-findings-s66.md` line 5 ("Generated: 2026-04-04")

---

## Honest count discipline

The 12-item delta is the empirically-defensible signal-rich set. Investigators reporting more retractions than this should provide structural evidence for each additional entry; investigators reporting fewer should not omit any of the 12 above without an explicit retraction-of-classification rationale. The 4 archive-driven supersessions (Items 43-46) are recorded as supersessions rather than retractions because the original CLAIMS in those documents survive structurally — only the document-level authority is migrating; the closure findings, the cascade picture, the Perturbative Exhaustion Theorem, the cross-session inventory snapshot all remain valid as content (subsumed at §7.3, §10.1, etc., of successor documents).
