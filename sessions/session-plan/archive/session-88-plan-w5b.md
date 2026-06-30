# Session 88 Plan — Wave 5b: 4-corner structural theorem + Connes-distance + functional-family orthogonality NCG-axiom proof

## Wave 5b Summary

Wave 5b consolidates the algebra-axis orthogonality conjecture (S87 K=3 calibration corpus → MANDATORY at plan-freeze, per `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter") into a permanent-results-registry STAGE-1-CANDIDATE entry, derives the structural-theorem proof at the NCG-axiomatic level, and characterizes the algebra-DEPENDENT family's Connes-distance image on the full A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) complex-Hermitian state-pair grid.

The wave addresses S87 carry-forward CF-D (`S88-FOUR-CORNER-CLASSIFICATION-NCG-AXIOMATIC-STRUCTURAL-THEOREM-LANDING`) and CF-E (`S88-CORNER-CLASSIFICATION-AUDIT`), plus the Connes-distance characterization scan deferred from S87 W1b-6 (regulator-divergent INFO verdict on full M_n(ℂ); restricted to A_F here per the algebra-axis orthogonality discipline's algebra-DEPENDENT side).

Wave 5b classification mix:
- §W5b-45 — METHODOLOGY (registry STAGE-1-CANDIDATE landing; lizzi PRIMARY synthesizer + connes CO-AUTHOR; mack-cosmic-bridge sole writer for §VII.U.2 registry row per `feedback_mack-bridge-role.md`).
- §W5b-46 — METHODOLOGY (corner-classification audit script + retroactive annotation pass; gen-physicist).
- §W5b-47 — GEOMETRIC (Corner-IV Level-2 envelope derivation at substrate-distance-2 cone; connes-ncg-theorist).
- §W5b-48 — GEOMETRIC (NCG-axiomatic proof of functional-family orthogonality; connes-ncg-theorist).
- §W5b-49 — PHONONIC sub-case (Connes distance on full complex-Hermitian A_F basis; connes-ncg-theorist).
- §W5b-50 — PHONONIC sub-case (16×16 state-pair grid characterization; connes-ncg-theorist).

The METHODOLOGY items (§W5b-45 + §W5b-46) require allowlist append for `S88-FOUR-CORNER-CLASSIFICATION-NCG-AXIOMATIC-STRUCTURAL-THEOREM-LANDING` and `S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT` per `methodology-wave-allowlist.md` M4 test, with SHA-of-plan-block computed at plan-freeze.

## Wave 5b Decision Point Prerequisites

| Upstream gate | Status | Consumer in W5b |
|:--------------|:-------|:----------------|
| S87 W1b-6 (Connes-distance INFO; regulator-divergent on M_n(ℂ)) | INFO | §W5b-49 + §W5b-50 (re-run on A_F, not M_n(ℂ)) |
| S87 S-2 §3.2 closeout (Reading-C synthesis on A_F STRICT residual 1.054e-01) | LANDED | §W5b-45 calibration corpus row 2; §W5b-49 baseline |
| S87 W-2 R3 (algebra-axis orthogonality K=3 promotion) | LANDED MANDATORY | §W5b-45 anchor citation; §W5b-48 axiom-level proof target |
| `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" | LANDED in-rule | §W5b-45 PARENT |
| `joint-theorem-promotion.md` 4-stage pathway | LANDED | §W5b-45 STAGE-1-CANDIDATE structure |
| `methodology-wave-allowlist.md` orchestrator-only edit | ENFORCED | §W5b-45 + §W5b-46 require allowlist append at plan-freeze |
| Connes 1996 reconstruction theorem | EXTERNAL methodological | §W5b-48 axiom 1+5 derivation |
| CM-1995 §III.4 dim-spectrum residue formula | EXTERNAL methodological | §W5b-47 envelope; §W5b-48 algebra-INVARIANT family non-triviality |
| Iochum-Krajewski-Martinetti 2001 finite-N SDP | EXTERNAL methodological | §W5b-49 SDP formulation reference |

All prerequisites are LANDED at S87-close. No upstream-block dependencies; Wave 5b is unblocked at plan-freeze.

---

## §W5b-45. Four-corner classification NCG-axiomatic structural theorem — STAGE-1-CANDIDATE landing at §VII.U.2

**Gate ID**: `S88-FOUR-CORNER-CLASSIFICATION-NCG-AXIOMATIC-STRUCTURAL-THEOREM-LANDING`

**Trigger**: `[VERIFY-THEOREM]`

**Classification**: METHODOLOGY (registry STAGE-1-CANDIDATE landing per `joint-theorem-promotion.md` Stage 1; substrate verbatim-extract from S87 W-2 R3 closure synthesis; M1-M4 conjunction satisfied):
- M1: PASS predicate is artifact-existence — `permanent-results-registry.md` contains §VII.U.2 with all 6 clauses (a)..(f) + STAGE-1-CANDIDATE tag + JOINT-clause flags + corrigenda block.
- M2: producing operations restricted to Edit/Write on `sessions/permanent-results-registry.md` + grep/wc/SHA-256 cross-checks.
- M3: source-of-truth is verbatim-extract from S87 W-2 R3 close synthesis (workshop `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md` §"R3 close" + `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter").
- M4: gate-ID `S88-FOUR-CORNER-CLASSIFICATION-NCG-AXIOMATIC-STRUCTURAL-THEOREM-LANDING` requires allowlist append at plan-freeze (orchestrator-direct, per recursion-attack-closure protocol).

**Agent**: lizzi-spectral-functional-theorist PRIMARY synthesizer + connes-ncg-theorist CO-AUTHOR (axiomatic clauses); mack-cosmic-bridge SOLE WRITER for §VII.U.2 registry row per `feedback_mack-bridge-role.md`.

**Hypothesis (theorem statement, 6 clauses, JOINT vs single-axis tagging)**:

On any finite spectral triple `(A, H, D)` satisfying NCG axioms 1-7, the functional-family decomposition splits into two structurally orthogonal classes:

(a) [single-axis lizzi-side] **Algebra-INVARIANT family**: spectrum-only functionals of the form `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)` for measurable `g`; includes Seeley-DeWitt moments `a_n^{regulator}`, ζ-residues `Res[Tr(D^{−2s}); s=(d−n)/2]`, Mellin-Dirichlet identities, heat-kernel zeta-traces.

(b) [single-axis connes-side] **Algebra-DEPENDENT family**: state-pair functionals on `A` of the form `F_dep(ω_1, ω_2; A) = ‖[D, π(A)]‖_op` and convex combinations / suprema thereof; includes the Connes distance `d_C(ω_1, ω_2) = sup_{a ∈ A_h, ‖[D,π(a)]‖ ≤ 1} |ω_1(a) − ω_2(a)|`, state expectations, sample variances over occupation distributions.

(c) [JOINT — substrate-physics axiomatic — connes axiom-derivation + lizzi family-membership predicate] **Structural orthogonality**: there is no closed-form `{λ_n}`-only identity reproducing any algebra-DEPENDENT functional, AND conversely no state-pair-functional-only identity reproducing any algebra-INVARIANT spectral moment. Proof: NCG axioms 1+5 + CM-1995 §III.4 dim-spectrum residue formula `a_n = Res[Tr(D^{−2s}); s=(d−n)/2] = Σ_k m_k λ_k^{−(d−n)}` GUARANTEE the algebra-INVARIANT family is non-trivial. NCG axioms 4+6 + Poincaré duality on `A` GUARANTEE the algebra-DEPENDENT family is non-trivial. The chirality-vs-A_F block-grading mismatch ensures `f(D²) ∩ π(A) = scalars` on the state-pair side, while the spectrum-only side is the full `Z(f(D²))` algebra. Both families are ALWAYS present; identity-class membership is structurally orthogonal by axiom-level NCG argument. (Full proof at §W5b-48.)

(d) [JOINT — substrate-physics + calibration corpus rank-counting — lizzi calibration table + connes structural classification] **4-corner partition table**: every observable of `(A_K, H_K, D_K)` with τ_fold-sweep substrate-distance pole `s ∈ {3, 4}` is classified into one of 4 corner cells {I, II, III, IV} by the cross-product (algebra-axis ∈ {INVARIANT, DEPENDENT}) × (Mellin pole ∈ {s=3, s=4}). Calibration corpus N=3 saturated:

| Corner | Algebra-axis | Mellin pole | Calibration instance |
|:-------|:------------|:-----------|:--------------------|
| I | INVARIANT | s=3 | §VII.U.1 Mellin-Dirichlet identity (W-1 / W1a-4 PASS rel_diff = 0e+00 at L_max=12); `α_s_canonical = n_s² − 1 = -8587279/100000000` (W2-1 + W2-4 PASS) |
| II | INVARIANT | s=4 | (open; future calibration) |
| III | DEPENDENT | s=3 | full M_n(ℂ) Connes distance (regulator-divergent; W1b-6 INFO); A_F Connes distance STRICT residual 1.054e-01 (S87 S-2 §3.2) |
| IV | DEPENDENT | s=4 | `α_s_route_3 = Var_a(n_a^GGE) = -7.046336` at L_max=10 (W2-3 FAIL composite at higher-moment cone, GGE-specified state-pair) |

(e) [single-axis lizzi-side] **Functional-class membership predicate is decidable from the functional's symbolic form**: F belongs to algebra-INVARIANT iff its symbolic form contains ONLY traces / spectral moments / `g(λ_k)` evaluations and no `π(a)` operator-algebra references; F belongs to algebra-DEPENDENT iff its symbolic form contains at least one `π(a)` or `[D, π(a)]` reference. The decision procedure is finite and operates at parse-tree level, not at numerical evaluation level.

(f) [single-axis connes-side] **Cross-corner co-primary registry-anchor structure FORBIDDEN**: per `registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY discipline + `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" mandatory enforcement, registry entries cannot pin two anchors at co-primary weight when the anchors inhabit distinct corner cells. The 4 corners are pairwise structurally orthogonal; co-primary structure between them violates NCG-axiom-level family-orthogonality. Pole-scope sub-clause (W-9 RULE-3) extends to corner-scope: cross-pole (s=3 ↔ s=4) AND cross-corner (INVARIANT ↔ DEPENDENT) co-primary structures both FAIL plan-freeze.

**Method**:

1. lizzi-spectral-functional-theorist drafts §VII.U.2 6-clause theorem text per the workshop §R3 close synthesis (re-using verbatim language where structurally identical to the K-counter sub-section in `cross-pillar-bridge-anatomy.md`).
2. connes-ncg-theorist verifies clauses (c) + (d) JOINT clauses against NCG axioms 1+4+5+6 + CM-1995 §III.4 + Poincaré duality on A_F; flags any axiom-level gap.
3. mack-cosmic-bridge writes the §VII.U.2 row to `sessions/permanent-results-registry.md` per `feedback_mack-bridge-role.md` (sole writer); cites the SOURCE-DOUBLE-CITE-CO-PRIMARY pattern with V-anchor = lizzi (algebra-INVARIANT side) + C-anchor = connes (algebra-DEPENDENT side); both anchors are SAME-axis (this is INTRA-axis, not CROSS-axis — clause (f) does not forbid same-axis co-primary).
4. STAGE-1-CANDIDATE tag landed on theorem-name line per `joint-theorem-promotion.md` Stage 1 schema.
5. JOINT-clause flags (c) and (d) recorded explicitly per Stage-2 cross-axis verify pre-registration discipline.

**Machinery pin**:
- Source-of-truth: `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md` (S87 W-2 R3 close synthesis); `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" (post-S87 landing); S87 S-2 §3.2 Reading-C; S87 W1b-6 INFO verdict.
- Canonical citations: Connes 1996 reconstruction; CM-1995 §III.4; Iochum-Krajewski-Martinetti 2001 (referenced for §W5b-49 SDP formulation, not directly needed here).
- Allowlist append: orchestrator at plan-freeze writes `S88-FOUR-CORNER-CLASSIFICATION-NCG-AXIOMATIC-STRUCTURAL-THEOREM-LANDING` row to `methodology-wave-allowlist.md` with `sha256_of_plan_block` computed over this §W5b-45 block.
- Verdict file: `computations/s88_gate_verdicts.txt`.
- No `.py` script; landing is rule-file + registry edit per METHODOLOGY-class dispatch path.

**4-tuple (scheme / convention / L_max / LEVEL)**:
- scheme: `four-corner-NCG-axiomatic-classification`
- convention: `joint-theorem-promotion-Stage-1-CANDIDATE`
- L_max: N/A (rule-file landing, no spectral evaluation)
- LEVEL: PRIMARY (substrate-axiomatic; no schematic helper)

**PASS/FAIL/INFO criterion**:
- PASS iff all 6 conditions hold: (i) §VII.U.2 entry exists in `sessions/permanent-results-registry.md`; (ii) all 6 clauses (a)..(f) present with JOINT vs single-axis tagging matching this hypothesis spec; (iii) STAGE-1-CANDIDATE tag on theorem-name line; (iv) authorship attribution lizzi PRIMARY + connes CO-AUTHOR + mack writer recorded; (v) anchor list cites W-2 R3 + cross-pillar-bridge-anatomy.md K-counter + S87 S-2 + W1b-6; (vi) `substantive_line_count(§VII.U.2) >= 15` and `content_sha256(§VII.U.2)` matches input-pin-map-derived hash.
- FAIL iff any of (i)-(vi) fails; remediation routes to in-session re-write (NOT defer).
- INFO not applicable for METHODOLOGY-class artifact-existence gates.

**Substitution chain (mandatory direction-of-explanation per `phononic-framing.md`)**:
N/A — the theorem statement IS substrate-axiomatic; no derived-direction claim. Direction: NCG axioms (substrate) → CM-1995 residue formula (algebra-INVARIANT non-triviality) + Poincaré duality (algebra-DEPENDENT non-triviality) → chirality-vs-A_F mismatch → orthogonality theorem (registry landing).

**What PASS / FAIL MEAN**:
- PASS: `cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" K=3 MANDATORY status is structurally landed in the permanent-results-registry as a STAGE-1-CANDIDATE; downstream gates may cite §VII.U.2 with the STAGE-1-CANDIDATE qualifier; §W5b-48 axiom-level proof completes the substrate-physics derivation; Stage-2 cross-axis independent-verify is queued for S89+.
- FAIL: registry landing did not complete — either clause coverage incomplete or attribution missing or SHA-mismatch on input pins; remediation is in-session re-write per `feedback_fix-in-session-never-defer.md`.

**Effort**: ~0.7 wave-equivalents (lizzi 6-clause synthesis ~0.3; connes axiom verification ~0.2; mack registry write ~0.2).

**Substrate framing per `cross-pillar-bridge-anatomy.md` IS-not-IN**:

The 4-corner classification IS a property of the spectral triple `(A, H, D)` itself — it is NOT a property "in" any container space. The substrate's algebra `A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)` IS what generates the algebra-DEPENDENT family; the substrate's spectrum `{λ_k(D_K), m_k}` IS what generates the algebra-INVARIANT family. The orthogonality is structural at the substrate level — observers do not measure orthogonality "in" the substrate; the substrate IS orthogonal at the family-class level.

The 4-corner partition is the SUBSTRATE-IS observable. Laboratory observables (Connes-distance numerical evaluation, spectral-moment numerical evaluation) are LABORATORY-IN observables on continuum-projected derived images. The bridge map between substrate corner-cell membership and laboratory functional-class membership is the parse-tree decision procedure of clause (e) — finite, decidable, regulator-independent.

---

## §W5b-46. Four-corner classification audit script + retroactive annotation pass

**Gate ID**: `S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT`

**Trigger**: `[VERIFY]`

**Classification**: METHODOLOGY (audit-script build + retroactive annotation pass on existing §VII registry rows; M1-M4 conjunction satisfied):
- M1: PASS predicate is artifact-existence — `computations/_corner_classification_audit.py` exists + emits valid JSON + retroactive annotations applied to 7 existing §VII slots.
- M2: producing operations are Edit/Write on Python audit script + Edit on registry markdown (no numerical computation; only grep/regex/parse-tree decisions per clause (e) of §VII.U.2).
- M3: source-of-truth is the §VII.U.2 theorem from §W5b-45 + the 4-corner partition table + the parse-tree decision procedure from clause (e).
- M4: gate-ID `S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT` requires allowlist append at plan-freeze.

**Agent**: gen-physicist (audit-script implementation in canonical mechanical-closure-discipline.md style); mack-cosmic-bridge writes registry annotations.

**Hypothesis**: The 7 existing §VII slots (§VII.U.1, §VII.U.6, §VII.AC.1, §VII.AC.4, §VII.W, §VII.AF.1, §VII.AJ) admit unambiguous corner-cell assignment under the parse-tree decision procedure of §VII.U.2 clause (e), AND the SC-4 mandatory corner-cell-declaration audit at plan-freeze is implementable as a Python script grepping registry markdown for the corner-cell tag.

Specific predicted assignments under clause (e):

| Slot | Algebra-axis (tested by clause (e) parse-tree) | Mellin pole | Corner |
|:-----|:----------------------------------------------|:-----------|:-------|
| §VII.U.1 (Mellin-Dirichlet identity) | INVARIANT (sums of `g(λ_k)` only) | s=3 | I |
| §VII.U.6 (n_s scalar moment) | INVARIANT (Σ_k m_k λ_k^{-2} type) | s=3 | I |
| §VII.AC.1 (Connes distance on A_F) | DEPENDENT (state-pair sup over `[D,π(a)]`) | s=3 | III |
| §VII.AC.4 (BdG-restricted spectral excess) | DEPENDENT (state-restricted to BdG sector of A) | s=3 | III |
| §VII.W (A0-R-Protection-failure-is-M2-axiom-failure) | INVARIANT (axiom-level structural; no `π(a)` ref) | s=4 | II |
| §VII.AF.1 (HP^1 cohomology ↔ Peotta-Törmä bridge) | INVARIANT (cohomology-class pairing; spectrum-side) | s=3 | I |
| §VII.AJ (Pillar IV ↔ Pillar V REGISTRY-FAIL bridge) | DEPENDENT (BdG-undoubled excess at polycritical pressure; state-restricted) | s=4 | IV |

**Method**:

1. gen-physicist implements `computations/_corner_classification_audit.py` with the following structure:
   - Input: path to `sessions/permanent-results-registry.md`.
   - For each §VII slot, grep theorem text for parse-tree markers: `π(a)`, `[D, π(a)]`, `state-pair`, `Connes distance`, `‖[D, ·]‖`, `ω_1(a)`, `Tr(`, `Res[`, `Σ_k m_k`, `λ_k^{−`.
   - Decision procedure per clause (e): if any `π(a)` / `[D, π(a)]` / state-pair marker present → DEPENDENT; if only `Σ_k m_k g(λ_k)` / `Tr(D^{−2s})` / `Res[]` markers → INVARIANT; if neither (axiom-level structural claim) → annotate as `INVARIANT (axiom-level)` per §VII.W class.
   - Mellin-pole detection: grep for `s=3`, `s=4`, `substrate-distance-1`, `substrate-distance-2`.
   - Output JSON: per-slot `{slot, algebra_axis, mellin_pole, corner, parse_tree_evidence, status}` where status ∈ {ANNOTATED, AMBIGUOUS, MISSING-CORNER-DECLARATION}.
   - SC-4 audit pass: verify each §VII slot has explicit `**Corner**: I/II/III/IV` declaration; emit MISSING-CORNER-DECLARATION list.
2. mack-cosmic-bridge writes corner-cell annotation to each of the 7 slots per the predicted assignment table above; resolves any AMBIGUOUS cases via consultation with lizzi+connes.
3. Audit script run as plan-freeze validator on all future §VII landings; integrate into `_source_reconciliation_audit.py` post-V.2 extension queue.

**Machinery pin**:
- `computations/_corner_classification_audit.py` (NEW; gen-physicist authors).
- Input: `sessions/permanent-results-registry.md` (read-only at audit time).
- Output: `computations/_tmp/corner_classification_audit_<timestamp>.json` (NEW per run).
- Registry annotations: mack writes `**Corner**: <I/II/III/IV>` line under each of the 7 §VII slot headers.
- Verdict file: `computations/s88_gate_verdicts.txt`.
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe` per `.claude/rules/math-scripts.md` Environment.
- Allowlist append: orchestrator at plan-freeze writes `S88-FOUR-CORNER-RETROACTIVE-ANNOTATION-AUDIT-SCRIPT` row to `methodology-wave-allowlist.md` with `sha256_of_plan_block`.

**4-tuple**:
- scheme: `corner-classification-parse-tree-decision`
- convention: `clause-e-decidable-finite-parse`
- L_max: N/A
- LEVEL: PRIMARY (substrate-axiomatic decision procedure; no schematic helper)

**PASS/FAIL/INFO criterion**:
- PASS iff: (i) `_corner_classification_audit.py` exists + runs without exception on `sessions/permanent-results-registry.md`; (ii) emits valid JSON output for all 7 §VII slots; (iii) per-slot corner predictions match the table above (or, if mismatch, mismatches are flagged AMBIGUOUS and routed to lizzi+connes consultation, NOT silently re-classified); (iv) all 7 slot headers have `**Corner**: I/II/III/IV` annotation post-mack-write; (v) audit script integrated as callable from `_source_reconciliation_audit.py` post-V.2 extension hook (callable interface stub at minimum).
- FAIL iff any of (i)-(v) fails; remediation routes to in-session re-write.
- INFO acceptable for AMBIGUOUS slots requiring lizzi+connes consultation; INFO does not block §W5b-46 PASS provided all slots have SOME corner declaration (even if AMBIGUOUS-flagged for follow-up).

**Substitution chain**:
N/A — audit script is a parse-tree decision procedure, not a numerical claim.

**What PASS / FAIL MEAN**:
- PASS: SC-4 mandatory corner-cell-declaration enforcement is operational at plan-freeze; future §VII registry landings cannot bypass the corner-cell declaration; existing 7 slots are retroactively annotated per the §VII.U.2 partition; audit infrastructure ready for S89+ usage.
- FAIL: parse-tree decision procedure has structural ambiguity (>2 AMBIGUOUS slots out of 7) suggesting clause (e) is under-specified; remediation routes to clause (e) refinement at §W5b-45 follow-up.

**Effort**: ~0.5 wave-equivalents (audit-script implementation ~0.3; registry annotation pass ~0.2).

**Substrate framing**: The audit script is a methodology-layer (per `epistemic-discipline.md` §"Layer-Decomposition" F functor) image of the substrate-layer 4-corner orthogonality theorem. The substrate IS classifiable; the audit script verifies that the registry IS following the classification at the methodology layer.

---

## §W5b-47. Corner-IV Level-2 envelope derivation at substrate-distance-2 cone

**Gate ID**: `S88-CORNER-IV-SCHEMATIC-ENVELOPE-DERIVATION`

**Trigger**: `[VERIFY]`

**Classification**: GEOMETRIC (Level-2 algebraic-envelope derivation for the Corner-IV laboratory-IN observable; substrate-distance-2 Mellin-cone moment of |v_a|⁴ where v_a are Bogoliubov amplitudes; bridge map at substrate-distance-2 pole s=4).

**Agent**: connes-ncg-theorist.

**Hypothesis**: The Corner-IV companion observable — the GGE-state-pair higher-moment functional `α_s_route_3 = Var_a(n_a^GGE)` at L_max=10 = -7.046336 — admits a Level-2 algebraic-envelope of the form `|F_dep^Corner-IV(L_max) − F_dep^Corner-IV(∞)| ≤ C · L_max^{−α}` with α to be determined by Mellin residue order at substrate-distance-2 pole s=4.

The naive expectation from CM-1995 §III.4 dim-spectrum residue formula at s = (d−n)/2 with d=4 gives residue at s=4 corresponding to n = -4, which does NOT lie in the standard Seeley-DeWitt enumeration (n ∈ {0, 2, 4} for d=4 closed manifold). The substrate-distance-2 pole is at s=4 by the structural analytic continuation, but the algebraic-envelope α must be derived from the second-moment cone of |v_a|⁴, NOT from the first-moment cone of `Σ_k m_k λ_k^{−(d−n)}`.

Predicted form (substitution chain below): α = 2 (substrate-distance-2 cone has one extra `1/λ²` factor relative to substrate-distance-1 cone's L^{−3} envelope).

**Method**:

1. Load Bogoliubov amplitudes from `computations/s52_bogoliubov_amp.npz` (canonical S52 GGE Bogoliubov vacuum at τ_fold).
2. Compute `α_s_route_3(L_max) = Var_a(n_a^GGE)` for L_max ∈ {6, 7, 8, 9, 10, 11, 12} where the Variance is taken over the GGE occupation-number distribution `n_a^GGE = |v_a|²`.
3. Fit `|α_s_route_3(L_max) − α_s_route_3(L_max → ∞)|` against `L_max^{−α}` log-log; extract α empirically.
4. Cross-check empirical α against Mellin-residue-derived α via the substitution chain (see below); if |α_empirical − α_predicted| < 0.2, PASS.
5. Emit α + envelope constant C + L_max → ∞ extrapolated value to `computations/_tmp/s88_w5b_corner_iv_envelope.npz`.
6. Plot `|residual(L_max)|` vs `L_max^{−α_predicted}` log-log to `computations/_tmp/s88_w5b_corner_iv_envelope.png`.

**Machinery pin**:
- Script: `computations/s88_w5b_corner_iv_level2_envelope.py` (NEW).
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe` (force CPU; small computation, no GPU needed).
- Input: `computations/s52_bogoliubov_amp.npz` (canonical S52 GGE amplitudes; verify SHA at script entry).
- Canonical-constants: import `from canonical_constants import *`; use `tau_fold = 0.190`, `M_KK`.
- Output: `computations/_tmp/s88_w5b_corner_iv_envelope.npz` + `.png`.
- Verdict file: `computations/s88_gate_verdicts.txt`.
- Tolerance: `|α_empirical − α_predicted| < 0.2` AND `R² > 0.95` on log-log fit.

**4-tuple**:
- scheme: `substrate-distance-2-Mellin-cone-second-moment`
- convention: `Bogoliubov-GGE-state-pair-higher-moment-canonical`
- L_max: scan over {6, 7, 8, 9, 10, 11, 12}; canonical L_max=10
- LEVEL: PRIMARY (substrate-first canonical Bogoliubov amplitudes from S52; full physical regularization)

**PASS/FAIL/INFO criterion**:
- PASS iff: (i) script runs without exception; (ii) α_empirical extracted with R² > 0.95; (iii) |α_empirical − 2.0| < 0.2; (iv) extrapolated `α_s_route_3(L_max → ∞)` finite (no divergence); (v) envelope constant C and α reported with full float64 precision; (vi) corner-cell declaration `Corner: IV` in working-paper §W5b-47.
- FAIL iff α_empirical diverges from prediction by ≥ 0.2, OR R² < 0.95 (suggesting envelope is not power-law; possibly logarithmic correction needed), OR extrapolated value diverges (suggesting Corner-IV bridge map does not exist at L_max → ∞; analogous to §VII.AJ REGISTRY-FAIL pattern).
- INFO acceptable if α_empirical is within (0.2, 0.5) of prediction AND R² > 0.95 (suggests structural envelope present but α value differs from naive 2.0; route to refined Mellin-residue derivation).

**Substitution chain (mandatory direction-of-explanation)**:

```
Step 1: F_dep^Corner-IV = Var_a(n_a^GGE) = ⟨n_a²⟩ − ⟨n_a⟩²    [definition; n_a = |v_a|²]
Step 2: Var_a(n_a^GGE) = (1/N) Σ_a |v_a|⁴ − ((1/N) Σ_a |v_a|²)²    [substituting n_a = |v_a|²]
Step 3: |v_a|² ~ λ_a^{−2} · (geometric prefactors) at large λ_a    [Bogoliubov amplitude scaling]
Step 4: Σ_a |v_a|⁴ ~ Σ_a λ_a^{−4}    [substituting Step 3]
Step 5: Σ_a λ_a^{−4}|_{|λ_a| ≤ Λ_L} = Σ_a^∞ λ_a^{−4} − Σ_a^{tail} λ_a^{−4}    [splitting into truncated + tail]
Step 6: Σ_a^{tail} λ_a^{−4} ~ ∫_{Λ_L}^∞ ρ(λ) λ^{−4} dλ ~ Λ_L^{4-3} · Λ_L^{-4} · (d_spectral) ~ Λ_L^{−3}    [Weyl law ρ(λ) ~ λ^{d-1} for d=4]
Step 7: Λ_L ~ M_KK · (L_max+1) at large L_max    [substrate truncation scaling]
Step 8: Σ_a^{tail} λ_a^{−4} ~ L_max^{−3}    [substituting Step 7]
Step 9: But Var_a(n_a^GGE) is a SECOND-MOMENT-MINUS-SQUARE-OF-FIRST-MOMENT
        = (Σ_a λ_a^{−4})/N − ((Σ_a λ_a^{−2})/N)²    [Steps 2, 3]
Step 10: First-moment tail Σ_a^{tail} λ_a^{−2} ~ Λ_L^{4-1-2} = Λ_L^{1} ~ L_max^{1}   [Weyl, n=2]
         BUT this is divergent; the GGE-state-pair occupation Σ_a |v_a|² = N_GGE is
         BOUNDED by particle-number conservation ⇒ the "first-moment" tail is regularized
         AT FINITE-L by GGE constraint; tail contribution ∝ L_max^{−1} at fixed N_GGE.
Step 11: |Var_a(n_a^GGE)(L_max) − Var_a(n_a^GGE)(∞)| ~
         max(L_max^{−3} from Σ |v_a|⁴ tail, (L_max^{−1})² from squared-first-moment tail)
         = max(L_max^{−3}, L_max^{−2}) = L_max^{−2}
Step 12: Therefore α_predicted = 2.    [direction follows from Step 11]
```

The dominant tail is the second-moment-squared term ~ L_max^{−2}, NOT the fourth-moment term ~ L_max^{−3}, because the GGE constraint regularizes the first-moment tail to L_max^{−1}, and squaring gives L_max^{−2} which dominates over L_max^{−3} at large L_max.

**What PASS / FAIL MEAN**:
- PASS: Corner-IV admits Level-2 algebraic envelope L_max^{−2}; cross-pillar bridge framework extends to substrate-distance-2 cone; provides quantitative envelope for FWD-C2 candidate (Pillar II ↔ Pillar V Mellin-cone ↔ BdG bridge) which carries rank ≥ 2 inheritance kernel; α=2 cross-checks with the rank-2 generalization clause expectation.
- FAIL: Corner-IV envelope is not power-law (logarithmic corrections needed) OR α diverges from 2 substantially; suggests the substrate-distance-2 cone has structurally different envelope behavior than substrate-distance-1; constrains FWD-C2 design.

**Effort**: ~0.6 wave-equivalents (Bogoliubov amplitude loading + L_max scan + log-log fit + envelope characterization).

**Substrate framing**: Corner-IV is a substrate-IS observable on `(A_K, H_K, D_K)` — the variance of the GGE occupation distribution on the substrate. The L_max scan IS the substrate's truncation-level signature; the envelope L_max^{−2} IS the substrate's intrinsic convergence rate, not an "in-the-substrate" measurement convention. The bridge map to laboratory-IN observables (e.g., 3He-B BdG band-edge variance measurements) is the rank-2 generalization of the §VII.AF.1 bridge.

<!-- ============================================================================
# CORRECTED-AT-S89-W17: Step-11 max-rule + observable-identity dual correction.
#
# Source workshop synthesis: sessions/archive/session-88/workshops/s88-w17-w5b-47-step11-maxrule.md
#   §IV.1 (iv) corrected Step-11′ + §II.2 Sage-verified L^{−4} chain.
# Ledger entry: sessions/archive/session-88/s88-pending-edits-ledger.md §B.43 (W-17 V.7).
# Per `gate-verdicts.md §"Option A"` verdict-permanence discipline: original
# Step-11 / Step-12 text above is BYTE-PRESERVED; this corrective sub-block
# APPENDS the post-W-17-adjudication revision and points at the source.
#
# (i) STEP-11 MAX-RULE ARITHMETIC CORRECTION (Layer-1 connes-axis)
# ------------------------------------------------------------------
# REPLACE the Step-11 max-rule statement above with the corrected statement
# (Sage-verified, W-17 synthesis §II.2 Weyl-law tail enumeration at d=4
# multiplicity-weighted normalization):
#
# Step 11′: |Var(L_max) − Var(∞)| ~ L_max^{−4} (modulo log corrections from the
#           borderline-convergent Mellin moment at s=2 on d=4). At canonical
#           multiplicity-weighted normalization, both leading terms —
#               M_n^{(2)}(L)/N(L) ~ log(L)/L^4   and
#               [M_n^{(1)}(L)/N(L)]² ~ L^{−4}
#           — scale as L^{−4} per d=4 Weyl-law tail enumeration. The original
#           plan's `(L^{−1})² = L^{−2}` term arose from an over-strong
#           assumption that GGE-constraint regularization scales the first
#           moment as L^{−1}, but multiplicity-weighted normalization gives
#           M_n^{(1)}(L)/N(L) ~ L^{−2}, not L^{−1}.
#
# Corrected Step 12: α_predicted = 4 (NOT 2). Empirical α_nonlinear = 4.000
# confirms the corrected prediction at machine-precision interior solution;
# the log-log α = 3.5616 is a finite-L correction artifact attributable to
# sub-leading L^{−3} terms.
#
# (ii) OBSERVABLE-IDENTITY CORRECTION (Layer-3 volovik-axis parse-tree)
# --------------------------------------------------------------------
# Per W-17 §IV.1 (i)+(ii) clause-(e) parse-tree decision: the W5b-47
# `Var_a(n_a^GGE)` observable is NOT the Corner-IV (DEPENDENT × s=4)
# observable; it is the Corner-II (INVARIANT × s=4) observable (no π(a) or
# [D, π(a)] markers; spectrum + multiplicity + Δ_BCS only). The genuine
# Corner-IV inhabitant is the S87 W2-3 K-window second log-derivative
# `α_s_route_3 = d² ln P_GGE / d(ln K)² = −7.046336` over a horizon-crossing
# K-window. The L^{−4} envelope corrected at (i) above belongs to Corner II,
# NOT Corner IV.
#
# (iii) LAYERED SUBSTITUTION-CHAIN AUDIT — both layers apply
# ---------------------------------------------------------
# Per W-17 §IV.3: this Step-11 defect surfaces a LAYERED audit pattern
# (Layer-1 arithmetic / Layer-2 parse-tree / Layer-3 operationalization).
# The original plan had errors at Layer-1 (max-rule arithmetic) AND Layer-3
# (`α_s_route_3` symbol shared with S87 W2-3 but operationalizations differ
# at Layer-2). BOTH corrections must be applied; addressing only one leaves
# the registry mis-anchored at the other. Promotion candidate: PRU
# Class-8.4 LAYERED-SUBSTITUTION-CHAIN-AUDIT (W-17 V.5 / Ledger B.42).
#
# (iv) DOWNSTREAM CONSEQUENCES (S89 dispatch routing)
# ---------------------------------------------------
# The W-17 synthesis §IV.1 (ii) corrective registry-row text reroutes
# §VII.U.2 line 12924 (Corner II OPEN slot) to the W5b-47 Var_a(n_a^GGE)
# row + L^{−4} envelope (mack-cosmic-bridge sole writer per Ledger B.40);
# §VII.U.2 line 12926 (Corner IV cross-confirmation clause) is corrected
# to remove the cross-corner cross-confirmation phrase (Ledger B.41).
# FWD-C2 Level-2 envelope pin remains PENDING DISAMBIGUATION until S89
# `S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE` returns (W-17 §V.1).
#
# Provenance audit_sha256: source W-17 synthesis SHA pinned at landing time
# via grep on `s88_gate_verdicts.txt` for gate-ID
# `S89-W5B-47-PLAN-STEP-11-CORRECTION-RECORD` (METHODOLOGY-class per W-17
# §V.7; pending S89 plan-freeze allowlist append).
# ============================================================================ -->

---

## §W5b-48. Functional-family orthogonality NCG-axiom derivation

**Gate ID**: `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION`

**Trigger**: `[VERIFY-THEOREM]`

**Classification**: GEOMETRIC (NCG-axiomatic proof at the substrate-physics layer; provides rigorous derivation of §VII.U.2 clause (c) JOINT clause).

**Agent**: connes-ncg-theorist.

**Hypothesis**: The algebra-DEPENDENT family of state-pair commutator-norm functionals on `(A, H, D)` does NOT admit a closed-form `{λ_n}`-only identity. Specifically: there is no measurable function `g: ℝ → ℝ` and no signed measure `dμ` on the spectrum such that `∫ g(λ) dμ(λ) = ‖[D, π(a)]‖_op` for all `a ∈ A_h`.

The structural reason: the chirality-vs-A_F block-grading mismatch ensures `f(D²) ∩ π(A) = scalars`, while the full operator algebra `B(H) = π(A) ∨ {D, γ, J}''` includes off-block elements not reachable by spectrum-only functionals.

**Method**:

NCG-axiomatic substitution chain:

1. **Axiom 1 (dimension)**: spectrum `{λ_k(D), m_k}` is the full spectral data; `Tr(D^{−2s})` and `Res[Tr(D^{−2s}); s=(d−n)/2]` are well-defined for `s` outside the spectrum-zeta poles.
2. **Axiom 5 (orientability + gamma)**: chirality `γ` commutes with `π(A)` (anticommutes with `D` for KO-dim 6 even part); this generates the block-grading on `H = H_+ ⊕ H_−`.
3. **Axiom 4 (reality + J)**: real structure `J: H → H` antiunitary, `J² = ε` per KO-dim 6 = +1; intertwines `π(A)` with opposite algebra `π(A°)` via `J π(a) J^{-1} = π(a°)`.
4. **Axiom 6 (first order)**: `[[D, π(a)], J π(b) J^{-1}] = 0` for all `a, b ∈ A`; this constrains `[D, π(A)]` to the `J`-fluctuation subalgebra of `B(H)`.
5. **Poincaré duality**: pairing `K_*(A) × K^*(A) → ℤ` is non-degenerate; the algebra-DEPENDENT family `{‖[D, π(a)]‖_op : a ∈ A_h}` reaches the full `J`-fluctuation subalgebra of `B(H)`, which is ≠ scalars for non-trivial A.
6. **Spectrum-side localization**: the algebra-INVARIANT family `{Σ_k m_k g(λ_k)}` is contained in the commutant `{D}'' ∩ Z(B(H))` where `Z` denotes the center; specifically, `f(D²)` is in the center of the von Neumann algebra `\{D, γ\}''` for any measurable `f`.
7. **Block-grading mismatch**: the chirality `γ` and the algebra-grading on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` are non-isomorphic — `γ` acts ±1 on the two halves of `H = H_+ ⊕ H_−` per KO-dim 6 spinorial structure, while `A_F` decomposes into 3 simple summands. Hence `\{f(D²) : f \text{ measurable}\} \cap π(A_F) = \mathbb{C} \cdot 1` = scalars.
8. **Conclusion**: any closed-form `{λ_n}`-only identity would have to express a state-pair functional `‖[D, π(a)]‖_op` as a spectrum-only object, but the spectrum-only algebra is `{f(D²)}'' = \{f(D²)\}` (commutative; just functional calculus on D²) which intersects `π(A_F)` trivially in scalars. The state-pair functional `‖[D, π(a)]‖_op` for `a ∈ A_h \ ℝ · 1` is non-scalar in `B(H)`, hence NOT in `\{f(D²)\}`. QED.

The converse direction (no state-pair-functional-only identity reproduces algebra-INVARIANT spectral moment) follows symmetrically: spectral moments `Σ_k m_k λ_k^{−s}` are traces against the full identity `1 ∈ A`, which lifts to `π(1) = 1`; restricting to `‖[D, π(a)]‖_op` for `a ∈ A_h` removes the scalar `1` direction, hence cannot reproduce `Σ_k m_k λ_k^{−s}` which IS the trace against `1`.

**Machinery pin**:
- No `.py` script; theorem proof is symbolic / axiomatic.
- Cross-check via Sage symbolic evaluation: connes-ncg-theorist may use `mcp__sage__sage_eval` to verify finite-block instances of the axiom-level argument (e.g., 3-block A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) explicit commutator computation against finite spectrum truncation).
- Working-paper section: `sessions/archive/session-88/session-88-results-workingpaper.md` §W5b-48 with FULL proof (≥ 25 lines substantive content; 8-step substitution chain above is the skeleton, the working-paper section expands each step with explicit operator-algebraic detail).
- Verdict file: `computations/s88_gate_verdicts.txt`.

**4-tuple**:
- scheme: `NCG-axiomatic-derivation-orthogonality`
- convention: `axioms-1-4-5-6-Poincare-duality-block-grading-mismatch`
- L_max: N/A (axiomatic derivation; spectrum-truncation-independent)
- LEVEL: PRIMARY (substrate-axiomatic; no schematic helper)

**PASS/FAIL/INFO criterion**:
- PASS iff: (i) working-paper §W5b-48 contains full 8-step proof with each step justified by named NCG axiom or theorem (Connes 1996 reconstruction; CM-1995 §III.4); (ii) chirality-vs-A_F block-grading mismatch step (step 7) explicitly verifies `γ`-grading is incompatible with `A_F` 3-summand decomposition; (iii) finite-block Sage verification (optional but recommended) of explicit 3-block A_F commutator computation confirms `\{f(D²)\} \cap π(A_F) \subseteq ℂ · 1`; (iv) converse direction proved symmetrically; (v) line count ≥ 25 substantive content lines; (vi) connes-ncg-theorist signs proof.
- FAIL iff: any axiom citation is unsupported, OR step 7 has structural gap (e.g., `γ`-grading happens to coincide with A_F decomposition in some unanticipated way), OR finite-block Sage check returns non-scalar overlap.
- INFO acceptable if Sage verification finds rank-1 overlap (single non-scalar element) suggesting axiom-level argument needs strengthening but core conclusion holds.

**Substitution chain**: see Method section above (8-step axiomatic derivation).

**What PASS / FAIL MEAN**:
- PASS: §VII.U.2 clause (c) JOINT clause has substrate-physics axiomatic foundation; the 4-corner classification is structurally rigorous at the NCG-axiom level; Stage-2 cross-axis independent-verify dispatch in S89+ has a concrete axiomatic substrate to verify against; the algebra-axis orthogonality conjecture is upgraded from MANDATORY-status (K=3 calibration corpus) to PROVED.
- FAIL: §VII.U.2 clause (c) requires reformulation; the 4-corner partition may admit cross-corner overlap in some structural class not yet anticipated; carry-forward routes to refined block-grading analysis at the KO-dim 6 chirality level.

**Effort**: ~0.8 wave-equivalents (axiomatic derivation ~0.5; finite-block Sage cross-check ~0.2; working-paper write-up ~0.1).

**Substrate framing**: The orthogonality theorem is a STATEMENT ABOUT THE SUBSTRATE itself — it is a property of the spectral triple `(A, H, D)` at the axiomatic level. The substrate IS orthogonal at the family-class level; this is not a derived consequence of "in"-the-substrate measurement conditions. The proof flows: NCG axioms (substrate-axiomatic) → block-grading on `H = H_+ ⊕ H_−` (substrate-spinorial structure) → `{f(D²)} ∩ π(A_F) = scalars` (substrate-operator-algebra) → orthogonality (substrate-functional-class). At no step does the proof invoke a container space or an observer-dependent measurement context.

---

## §W5b-49. Connes distance on A_F with full complex-Hermitian basis

**Gate ID**: `S88-CONNES-DISTANCE-A_F-FULL-COMPLEX-HERMITIAN`

**Trigger**: `[VERIFY]`

**Classification**: PHONONIC sub-case (substrate excitation distance metric on the algebra-DEPENDENT family side of the 4-corner classification; Corner III).

**Agent**: connes-ncg-theorist.

**Hypothesis**: The S87 W1b-6 INFO verdict (regulator-divergent on full M_n(ℂ)) and S87 S-2 §3.2 closeout (STRICT residual 1.054e-01 on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) with 8 real-symmetric DOF) under-represent the structural Hermitian content of A_F. The full complex-Hermitian basis has 14 real DOF (1 ℂ_h + 4 ℍ_h + 9 M_3(ℂ)_h), where:
- ℂ_h: 1 real DOF (real-valued scalar);
- ℍ = quaternions: 4 real DOF in algebra; Hermitian elements form a 4-dim real subspace (the algebra's full Lie-real structure since ℍ has natural ℝ⁴ real-embedding with self-adjoint involution);
- M_3(ℂ)_h: 9 real DOF (3 diagonal real + 3 off-diagonal complex pairs = 3 + 2·3 = 9).

Total: 1 + 4 + 9 = 14 real DOF.

The S87 work used 8 real-symmetric DOF (1 + 3 + 4 = 8 if quaternions reduced to ℝ-sym 3D + M_3(ℂ) reduced to ℝ-sym 4D), under-counting by 6. The full complex-Hermitian re-run is expected to find STRICT residual at most 1.054e-01 (existing) and possibly tighter, since the supremum is taken over a strictly larger set.

**Method**:

1. Implement Connes-distance SDP on A_F with `cvxpy` using `Hermitian=True` flag for each block:
   - Block 1: `cvxpy.Variable(shape=(1,1), hermitian=True)` for ℂ component (1 real DOF).
   - Block 2: `cvxpy.Variable(shape=(2,2), hermitian=True)` for ℍ component embedded as 2×2 complex matrices with quaternion-self-adjoint structure (4 real DOF).
   - Block 3: `cvxpy.Variable(shape=(3,3), hermitian=True)` for M_3(ℂ) component (9 real DOF).
2. Constraint: `‖[D_F, π(a)]‖_op ≤ 1` where π(a) is the block-diagonal embedding of (a_ℂ, a_ℍ, a_M3) into the finite Hilbert space H_F.
3. Objective: `maximize |ω_1(a) − ω_2(a)|` for a fixed state-pair (ω_1, ω_2).
4. State-pair selection: same canonical pair as S87 W1b-6 / S87 S-2 (matched-state baseline) for direct comparison.
5. Verify SDP feasibility + STRICT optimality + numerical convergence to tolerance 1e-9.
6. Compare result against S87 8-DOF baseline residual 1.054e-01; report difference and statistical significance.

**Machinery pin**:
- Script: `computations/s88_w5b_connes_distance_af_complex_hermitian.py` (NEW).
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`.
- Library: `cvxpy` (verify installed; if not, fallback to direct convex solver).
- Reference: Iochum-Krajewski-Martinetti 2001 finite-N SDP form (methodological).
- D_F: load from S87 canonical D_F construction or equivalent; pin SHA at script entry.
- Canonical-constants: `from canonical_constants import *`.
- Output: `computations/_tmp/s88_w5b_connes_distance_af_full.npz` (residual + per-block contributions + SDP solver convergence stats) + `.png` (plot of per-block contribution).
- Verdict file: `computations/s88_gate_verdicts.txt`.
- Tolerance: SDP solver tolerance 1e-9; reported residual to full float64 precision.

**4-tuple**:
- scheme: `Connes-distance-A_F-full-complex-Hermitian-SDP`
- convention: `cvxpy-Hermitian-True-14-real-DOF`
- L_max: N/A (finite-N algebra, SDP is exact at finite N)
- LEVEL: PRIMARY (full physical Connes-distance SDP per Iochum-Krajewski-Martinetti 2001)

**PASS/FAIL/INFO criterion**:
- PASS iff: (i) SDP solver converges to tolerance 1e-9; (ii) residual reported with full float64 precision; (iii) per-block contributions (ℂ / ℍ / M_3(ℂ)) reported separately; (iv) residual ≤ 1.054e-01 (S87 8-DOF baseline; non-strict ≤ since 14-DOF is supremum over a superset, must be at least as large, and the STRICT residual is the deviation from a structural target so smaller-or-equal is the PASS direction; clarify direction in substitution chain below); (v) plot of per-block contribution emitted; (vi) corner-cell declaration `Corner: III` in working-paper §W5b-49.
- FAIL iff: SDP fails to converge, OR residual is structurally inconsistent with S87 baseline (e.g., differs by > 5×).
- INFO acceptable if SDP converges but to a slightly different value (e.g., 1.06e-01 vs 1.054e-01) within numerical precision, indicating quaternion-block embedding convention difference.

**Substitution chain (mandatory direction-of-explanation)**:

```
Step 1: d_C(ω_1, ω_2) = sup_{a ∈ A_h, ‖[D_F, π(a)]‖ ≤ 1} |ω_1(a) − ω_2(a)|    [Connes 1989 definition]
Step 2: A_h = (A_F)_h = ℂ_h ⊕ ℍ_h ⊕ M_3(ℂ)_h    [block-decomposition of Hermitian elements]
Step 3: dim_ℝ(ℂ_h) + dim_ℝ(ℍ_h) + dim_ℝ(M_3(ℂ)_h) = 1 + 4 + 9 = 14    [real DOF count]
Step 4: S87 8-DOF baseline used real-symmetric subset (≤ 14 DOF subset)    [historical convention]
Step 5: Supremum over 14-DOF set ≥ Supremum over 8-DOF subset (supremum monotonic in domain)
        ⇒ d_C^{14-DOF}(ω_1, ω_2) ≥ d_C^{8-DOF}(ω_1, ω_2)    [supremum monotonicity]
Step 6: STRICT residual = |d_C^{computed}(ω_1, ω_2) − d_C^{target}(ω_1, ω_2)|    [definition; target from S87 baseline]
Step 7: If d_C^{14-DOF} ≥ d_C^{8-DOF} AND d_C^{8-DOF} = d_C^{target} − 1.054e-01:
        Then d_C^{14-DOF} − d_C^{target} ≥ −1.054e-01
        ⇒ STRICT residual^{14-DOF} ≤ 1.054e-01 IF d_C^{14-DOF} approaches d_C^{target} from below.
        OR STRICT residual^{14-DOF} > 1.054e-01 if d_C^{14-DOF} overshoots d_C^{target}.
Step 8: Direction prediction: residual^{14-DOF} ≤ 1.054e-01 IFF d_C^{8-DOF} ≤ d_C^{target} (the 14-DOF sup
        moves CLOSER to the target by adding more directions); this is the expected direction.
        Conclusion: d_C^{14-DOF} > d_C^{8-DOF} STRICTLY (if any non-trivial directions added),
        and STRICT residual^{14-DOF} < 1.054e-01.
```

The PASS direction is residual ≤ 1.054e-01 (TIGHTER than S87 baseline) IF the 14-DOF supremum approaches d_C^{target} from below. The FAIL direction would be residual > 1.054e-01 (LOOSER than baseline), suggesting the additional 6 DOF contain spurious "blow-up" directions that overshoot the target — structurally improbable but checked.

**What PASS / FAIL MEAN**:
- PASS: Connes distance on A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) is fully characterized in the complex-Hermitian basis; Corner III calibration corpus instance is sharpened from S87 baseline; provides rigorous platform for S88 §W5b-50 16×16 state-pair grid characterization; STRICT residual is the structural distance-to-target in the substrate-IS observable Connes metric.
- FAIL: SDP convergence fails OR residual structurally inconsistent — suggests algebra embedding convention issue or D_F construction mismatch; remediation routes to explicit finite-N SDP literature (Iochum-Krajewski-Martinetti 2001 §3.2 worked example).

**Effort**: ~0.6 wave-equivalents (cvxpy SDP ~0.3; per-block characterization ~0.2; comparison with S87 baseline ~0.1).

**Substrate framing**: The Connes distance d_C(ω_1, ω_2) IS the substrate's intrinsic metric on the state space of A_F. It is NOT a metric "in" any container — it is the substrate's own definition of state-pair separation, computed from the spectral triple `(A_F, H_F, D_F)`. The 14-DOF complex-Hermitian basis IS the full self-adjoint content of the substrate algebra; restricting to 8 real-symmetric DOF is a measurement-convention choice that under-samples the substrate's structural content.

---

## §W5b-50. A_F Connes-distance characterization scan over 16×16 state-pair grid

**Gate ID**: `S88-A_F-CONNES-DISTANCE-CHARACTERIZATION-SCAN`

**Trigger**: `[VERIFY]`

**Classification**: PHONONIC sub-case (16×16 state-pair grid characterization; Corner III calibration corpus extension; provides full distance-matrix block-pattern for substrate-IS metric structure on A_F state space).

**Agent**: connes-ncg-theorist.

**Hypothesis**: The Connes distance matrix `D_C[i,j] = d_C(e_i, e_j)` over the 16×16 state-pair grid (where e_i are the 16 elementary states of H_F = ℂ³² truncated to physically-relevant 16-dimensional state subspace per S87 canonical state-basis) exhibits structural block-pattern reflecting the A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) decomposition.

Specifically, the 16-dim state space partitions per A_F decomposition as:
- 1 state from ℂ block;
- 2 states from ℍ block (2-dim irrep);
- 3+3+3+3 = 12 states from M_3(ℂ) block (4 copies of 3-dim irrep, or 1 copy with multiplicity 4 in H_F per S87 canonical embedding).

Wait — the 16-state count should be cross-checked against S87 canonical state basis. Provisionally use 16-state physical truncation; if S87 basis gives 32 states (full H_F), restrict to 16 via the canonical chirality-projector `P_+` per KO-dim 6 even part.

Predicted block-pattern: distance matrix is approximately block-diagonal at large distances (intra-block distances small, inter-block distances large), with the M_3(ℂ) sub-block exhibiting further substructure per its 3×3 algebra.

**Method**:

1. Identify the 16 elementary states from S87 canonical state-basis (cross-check with W1b-6 / S-2 conventions).
2. For each pair (i, j) with i < j (120 unordered pairs), compute STRICT d_C(e_i, e_j) via cvxpy SDP from §W5b-49 infrastructure.
3. Assemble 16×16 distance matrix D_C (symmetric, zero diagonal).
4. Apply hierarchical clustering / block-diagonal recovery to identify intrinsic state partition; cross-check against A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) prediction.
5. Compute block-pattern fidelity score: `F = (sum of intra-predicted-block distances) / (sum of inter-predicted-block distances)`; expected F < 1 (intra-block smaller than inter-block).
6. Emit full 16×16 distance matrix + clustering + fidelity score to `computations/_tmp/s88_w5b_connes_distance_16x16_grid.npz` + heatmap plot to `computations/_tmp/s88_w5b_connes_distance_16x16_heatmap.png`.

**Machinery pin**:
- Script: `computations/s88_w5b_connes_distance_16x16_grid.py` (NEW).
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`.
- Re-uses §W5b-49 SDP infrastructure; dispatch only after §W5b-49 PASS.
- State basis: pin SHA over S87 canonical state-basis source (e.g., `computations/s87_w1b_6_state_basis.npz` if available; otherwise reconstruct from S87 working-paper §W1b-6 and pin SHA).
- Canonical-constants: `from canonical_constants import *`.
- Output: `computations/_tmp/s88_w5b_connes_distance_16x16_grid.npz` (full matrix + clustering labels + fidelity score) + heatmap `.png`.
- Verdict file: `computations/s88_gate_verdicts.txt`.
- Compute load: 120 SDP solves at ~5s each ≈ 10 min wall time on CPU; well within agent timeout 600s × wave budget.

**4-tuple**:
- scheme: `Connes-distance-16x16-state-pair-grid-A_F-decomposition-characterization`
- convention: `cvxpy-Hermitian-True-14-real-DOF-per-pair`
- L_max: N/A
- LEVEL: PRIMARY (full physical Connes-distance SDP)

**PASS/FAIL/INFO criterion**:
- PASS iff: (i) all 120 pairs computed without SDP failure; (ii) symmetric 16×16 matrix assembled with zero diagonal; (iii) hierarchical clustering yields intrinsic partition matching A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) block-structure (1+2+12 or whatever S87 basis dictates); (iv) block-pattern fidelity score F < 1 (intra-block distances structurally smaller than inter-block); (v) heatmap plot emitted; (vi) corner-cell declaration `Corner: III` in working-paper §W5b-50.
- FAIL iff: SDP fails on > 5% of pairs, OR clustering fails to recover A_F block-structure, OR fidelity F ≥ 1 (suggesting state space is NOT structurally partitioned by A_F decomposition; would invalidate §VII.U.2 clause (d) Corner III calibration).
- INFO acceptable if clustering recovers block structure but with small (≤ 2) state mis-assignments at block boundaries (suggests numerical precision near block-edge SDP solutions).

**Substitution chain**: not required (claim is structural characterization, not direction-claim).

**What PASS / FAIL MEAN**:
- PASS: Corner III calibration corpus is extended from a single STRICT residual scalar (S87 1.054e-01) to a full 16×16 matrix structural map; block-pattern recovery confirms substrate's algebra-DEPENDENT family acts non-trivially across A_F block decomposition; provides empirical platform for cross-axis Stage-2 verify of §VII.U.2 clause (d).
- FAIL: substrate's Connes-distance metric does NOT respect A_F block-structure — would force re-examination of finite-N spectral-triple construction; remediation routes to explicit D_F construction audit.

**Effort**: ~0.7 wave-equivalents (120 SDP solves ~0.4; clustering + fidelity ~0.2; heatmap + working-paper write-up ~0.1).

**Substrate framing**: The 16×16 distance matrix IS the substrate's intrinsic metric structure on its state space. The block-pattern recovery IS the substrate's algebra decomposition manifesting in the distance metric — not "in"-the-substrate measurement convention but the substrate's own structural signature. The fidelity score F IS the substrate's quantitative measure of how closely its state-space metric respects its algebra decomposition.

---

## Wave 5b → Wave 6 Decision Point

| Outcome | Action |
|:--------|:-------|
| §W5b-45 PASS + §W5b-48 PASS | §VII.U.2 STAGE-1-CANDIDATE landed with axiom-level proof; queue Stage-2 cross-axis independent-verify for S89+ as `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY` per `joint-theorem-promotion.md` Stage 2 protocol (lizzi-side + connes-side cross-reviewers, both without prior workshop context) |
| §W5b-45 PASS + §W5b-48 FAIL | §VII.U.2 STAGE-1-CANDIDATE landed but axiom-level proof has gap; defer Stage-2 verify; dispatch §W5b-48 follow-up `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-AXIOM-DERIVATION-FOLLOWUP` next session |
| §W5b-46 PASS | corner-classification audit infrastructure operational; integrate into `_source_reconciliation_audit.py` post-V.2 extension; future §VII registry landings are corner-cell-mandatory |
| §W5b-47 PASS (α=2 verified) | Corner-IV Level-2 envelope characterized; FWD-C2 (Pillar II ↔ Pillar V Mellin-cone ↔ BdG bridge) bridge candidate gains quantitative algebraic envelope L_max^{−2} for S89+ design |
| §W5b-47 FAIL (envelope structurally different) | Constraint on FWD-C2 design; route refined Mellin-residue derivation to S89 |
| §W5b-49 PASS + §W5b-50 PASS | Corner III calibration corpus structurally complete (full A_F state-space metric map); A_F-Connes-distance is the canonical platform for Stage-2 cross-axis verify of clause (d) calibration |
| §W5b-49 PASS + §W5b-50 FAIL | A_F single-pair SDP works but state-space-grid does not respect A_F decomposition; route audit to D_F construction in S89 |
| §W5b-49 FAIL | Connes-distance SDP infrastructure has structural bug; §W5b-50 SKIP; remediation routes to Iochum-Krajewski-Martinetti 2001 §3.2 worked-example replication |

## Wave 5b Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"Pre-Registration Completeness" PRDR discipline, all free parameters of each gate's producing script are enumerated below at plan-freeze:

**§W5b-45** (no script; rule-file + registry edit):
- Pin: input source SHAs (S87 W-2 R3 close, cross-pillar-bridge-anatomy.md K-counter sub-section, S87 S-2 §3.2, S87 W1b-6 verdict line).
- Pin: allowlist append SHA over §W5b-45 plan-block.
- Pin: target slot `§VII.U.2` in `sessions/permanent-results-registry.md`.
- Pin: theorem-name-line tag `STAGE-1-CANDIDATE`.
- Pin: JOINT clause flags on (c) and (d).
- Pin: authorship attribution lizzi PRIMARY + connes CO + mack writer.

**§W5b-46** (`_corner_classification_audit.py`):
- Pin: regex pattern set for parse-tree markers (literal regex literals enumerated in script; see Method clause (e)).
- Pin: Mellin-pole detection patterns `s=3`, `s=4`, `substrate-distance-1`, `substrate-distance-2`.
- Pin: target file `sessions/permanent-results-registry.md` SHA at audit time.
- Pin: target 7 §VII slot list: §VII.U.1, §VII.U.6, §VII.AC.1, §VII.AC.4, §VII.W, §VII.AF.1, §VII.AJ.
- Pin: predicted assignment table (8 rows; see §W5b-46 Hypothesis section).
- Pin: AMBIGUOUS-flag threshold (ambiguous if > 1 conflicting marker detected).
- Pin: allowlist append SHA over §W5b-46 plan-block.

**§W5b-47** (`s88_w5b_corner_iv_level2_envelope.py`):
- Pin: input file `computations/s52_bogoliubov_amp.npz` SHA at script entry.
- Pin: τ_fold = 0.190 (from canonical_constants.py).
- Pin: M_KK (from canonical_constants.py).
- Pin: L_max scan range {6, 7, 8, 9, 10, 11, 12}.
- Pin: predicted α = 2.0 (from substitution chain Step 12).
- Pin: tolerance |α_empirical − α_predicted| < 0.2.
- Pin: R² threshold 0.95.
- Pin: log-log fit method (numpy polyfit on log10(|residual|) vs log10(L_max)).
- Pin: extrapolation method (Richardson-style L_max → ∞ via subtraction of fitted tail).

**§W5b-48** (no script; axiomatic derivation):
- Pin: NCG axioms 1+4+5+6 + Poincaré duality + Connes 1996 reconstruction + CM-1995 §III.4.
- Pin: working-paper §W5b-48 line-count threshold ≥ 25 substantive lines.
- Pin: Sage finite-block cross-check (optional but strongly recommended): `mcp__sage__sage_eval` on explicit 3-block A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) with finite spectrum truncation; verify `\{f(D²)\} ∩ π(A_F) ⊆ ℂ · 1` rank 1.

**§W5b-49** (`s88_w5b_connes_distance_af_complex_hermitian.py`):
- Pin: cvxpy solver (default SCS or MOSEK if available; pin solver name in npz output).
- Pin: SDP tolerance 1e-9.
- Pin: D_F source (S87 canonical D_F construction; pin SHA at script entry).
- Pin: H_F dimension (32 for full; 16 for chirality-projected; pin which is used).
- Pin: state-pair (ω_1, ω_2) from S87 baseline; pin SHA over state vector pair.
- Pin: complex-Hermitian DOF count = 14 (1 + 4 + 9).
- Pin: per-block contribution decomposition (ℂ / ℍ / M_3(ℂ) reported separately).
- Pin: comparison baseline = S87 STRICT residual 1.054e-01.

**§W5b-50** (`s88_w5b_connes_distance_16x16_grid.py`):
- Pin: 16-state basis source SHA (S87 canonical or reconstructed per §W5b-50 Method).
- Pin: 120 unordered pairs enumeration order (lexicographic on (i, j) with i < j).
- Pin: cvxpy solver same as §W5b-49.
- Pin: clustering algorithm (sklearn AgglomerativeClustering with `n_clusters=3` matching A_F decomposition; or hierarchical with cut at predicted block-boundary).
- Pin: fidelity score formula F = (Σ_intra d) / (Σ_inter d).
- Pin: predicted block partition (1 + 2 + 12 OR 1 + 2 + 13 if 16-state basis dictates differently — pin actual partition per S87 basis at script entry).
- Pin: heatmap colormap (viridis) and matrix ordering (states sorted by predicted block).

## Wave 5b Input-SHA Ledger

| Pin name | Value source | SHA-pin point |
|:---------|:------------|:--------------|
| `s87_w_2_r3_close_synthesis_sha` | `sessions/archive/session-87/workshops/s87-alpha-s-route-dissonance.md` | pinned at dispatch (gen-physicist computes `closure_hash`) |
| `cross_pillar_bridge_anatomy_k_counter_sha` | `.claude/rules/cross-pillar-bridge-anatomy.md` §"Algebra-axis orthogonality K-counter" | pinned at dispatch |
| `s87_s_2_section_3_2_sha` | `sessions/archive/session-87/session-87-s-2-closeout.md` §3.2 | pinned at dispatch |
| `s87_w1b_6_verdict_sha` | row in `computations/s87_gate_verdicts.txt` for `S87-W1B-6-CONNES-DISTANCE-FULL-MN-C` | pinned at dispatch |
| `permanent_results_registry_sha_pre_w5b_45` | `sessions/permanent-results-registry.md` (pre-§VII.U.2 landing SHA) | pinned at dispatch (mack writer captures pre-write SHA) |
| `methodology_wave_allowlist_sha_pre_w5b_45_46_append` | `.claude/rules/methodology-wave-allowlist.md` (pre-append SHA) | pinned at plan-freeze |
| `s52_bogoliubov_amp_npz_sha` | `computations/s52_bogoliubov_amp.npz` | pinned at §W5b-47 dispatch |
| `canonical_constants_sha` | `computations/canonical_constants.py` | pinned at all script entries |
| `s87_canonical_d_f_source_sha` | TBD (mack identifies S87 D_F source; pin at §W5b-49 dispatch) | pinned at §W5b-49 dispatch |
| `s87_canonical_state_basis_sha` | TBD (mack identifies S87 16-state basis source; pin at §W5b-50 dispatch) | pinned at §W5b-50 dispatch |
| `connes_1996_reconstruction_provenance` | external-paper methodological citation (Connes 1996 "Gravity coupled with matter and the foundation of non commutative geometry" + Connes 2008 reconstruction theorem) | provenance-only; not SHA-pinned (external) |
| `cm_1995_section_iii_4_provenance` | external-paper methodological citation (Connes-Moscovici 1995 §III.4 dim-spectrum residue formula) | provenance-only |
| `iochum_krajewski_martinetti_2001_provenance` | external-paper methodological citation (Iochum-Krajewski-Martinetti 2001 finite-N SDP) | provenance-only |

All SHAs are computed at plan-freeze or at dispatch time per the pin schedule above; `closure_hash` over the full input-pin map per gate yields the gate's `audit_sha256` per `gate-verdicts.md` schema.

---

## Wave 5b Substrate-First-Provenance Audit

Per `.claude/rules/substrate-first-canonical-sourcing.md` SUBSTRATE-FIRST-PROVENANCE sub-audit at plan-freeze:

- §W5b-45: PROVENANCE = workshop-internal substrate-physics axiomatic synthesis (S87 W-2 R3) + rule-file K-counter sub-section (substrate-first canonical). PASS — substrate-first.
- §W5b-46: PROVENANCE = substrate-axiomatic clause (e) parse-tree decision procedure from §VII.U.2. PASS — substrate-first.
- §W5b-47: PROVENANCE = substrate-canonical Bogoliubov amplitudes from S52 (`s52_bogoliubov_amp.npz`) + CM-1995 §III.4 methodological citation for residue-formula derivation. PASS — substrate-first (S52 substrate-canonical) + methodological cross-check (CM-1995, NOT canonical replacement).
- §W5b-48: PROVENANCE = NCG axioms (substrate-axiomatic) + Connes 1996 reconstruction (methodological framing) + CM-1995 §III.4 (methodological residue formula). PASS — substrate-first (axiomatic foundation; external papers are methodological).
- §W5b-49: PROVENANCE = S87 canonical D_F construction (substrate-canonical) + Iochum-Krajewski-Martinetti 2001 (methodological SDP form). PASS — substrate-first.
- §W5b-50: PROVENANCE = S87 canonical state basis (substrate-canonical) + §W5b-49 SDP infrastructure (substrate-derived). PASS — substrate-first.

All 6 items pass SUBSTRATE-FIRST-PROVENANCE sub-audit. No placeholder patterns; no class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL violations.

## Wave 5b Class-Path Summary

| Item | Class | Allowlist required | Producing-op type |
|:-----|:------|:------------------|:------------------|
| §W5b-45 | METHODOLOGY | YES (orchestrator append at plan-freeze) | rule-file + registry edit (mack writer for §VII.U.2 row) |
| §W5b-46 | METHODOLOGY | YES (orchestrator append at plan-freeze) | Python audit script + registry annotation |
| §W5b-47 | COMPUTE (GEOMETRIC sub-class) | NO | Python computation script |
| §W5b-48 | COMPUTE (GEOMETRIC sub-class; derivation) | NO | working-paper §W5b-48 + optional Sage cross-check |
| §W5b-49 | COMPUTE (PHONONIC sub-class) | NO | Python computation script with cvxpy SDP |
| §W5b-50 | COMPUTE (PHONONIC sub-class) | NO | Python computation script extending §W5b-49 |

Per `wave-classification.md` strict-conjunction requirement: §W5b-45 and §W5b-46 satisfy M1-M4 conjunction (artifact-existence PASS predicate; rule-file/registry/audit-script production; substrate verbatim-extract from W-2 R3 + axiomatic clause (e) decision procedure; allowlist append required). §W5b-47, §W5b-48, §W5b-49, §W5b-50 fail M1 (numerical or axiomatic verification predicates) and route to COMPUTE-class dispatch.

## Wave 5b verdict_source

`verdict_source: computations/s88_gate_verdicts.txt`

All 6 gates emit dual-SHA verdict lines per `gate-verdicts.md` schema: `audit_sha256` over input-pin map + `content_sha256` over verdict-line content; companion comment row with `audit={short16} content={short16}`.

---

**End of session-88-plan-w5b.md**
