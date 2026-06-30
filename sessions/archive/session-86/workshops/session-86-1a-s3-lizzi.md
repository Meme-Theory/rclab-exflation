# Session 86 Synthesis: Substrate-First Canonical-Sourcing Rule Promotion

**Date**: 2026-04-27
**Agent**: lizzi-spectral-functional-theorist (lizzi)
**Slot**: S86 W1a Slot 1a, entry S-3
**Source Documents**:
- `sessions/archive/session-86/session-86-w0c-workingpaper.md` §W0c-3 (lines 328-483)
- `sessions/archive/session-86/session-86-w4-workingpaper.md` §W4-2 (lines 121-298)
- `sessions/archive/session-86/session-86-w5a-workingpaper.md` §W5a-1 + §10 substitution chain (lines 53-100)
- `.claude/rules/phononic-framing.md` (Substrate Picture + IS Space, Not IN Space mandate)
- `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" (PRU-extension Class 8.1, 5-class taxonomy + 4-band severity calibration)
- `.claude/agent-memory/lizzi-spectral-functional-theorist/MEMORY.md`

---

## I. Session Outcome

Three independent S86 witnesses surfaced the same plan-authorship pathology: **canonical sourcing of substrate quantities was assigned to external-paper provenance (vdd §VI, Connes-Chamseddine §2.2-2.3, placeholder analytic estimates) where the substrate's own first-principles computation is the structural canonical**. The fixes (W0c-3 reroute to S83 W2-G24; W4-2 SCHEMATIC-vs-physical disclosure; W5a-2 substitution-chain correction post-hoc) were per-witness reactive. A permanent rule promotes the substrate-first canonical-sourcing discipline to a forward-looking pre-flight audit, extending `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" with a sixth class — **(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — and a HARD-HALT severity at D_max ≥ 3.0 (as observed at W5a-2 with measured D_max = 3.13).

The rule operates at the **canonical-sourcing axis**, complementary to but distinct from `phononic-framing.md`'s **explanation-direction axis**. Where phononic-framing prevents container-thinking in narrative ("particles created IN curved spacetime" → "fiber spectrum reorganizes"), substrate-first canonical-sourcing prevents container-thinking in numerical provenance ("xi_E_GGE_inv ≈ O(10⁻²) per analytic placeholder" → "xi_E_GGE_inv = 13.642473 from 59.8 · Δ_BCS / K_base substrate computation").

---

## II. Key Results

### Witness #1 — W0c-3 §(b): vdd §VI does not exist

**Result**: The plan §W0c-3 hypothesis cited "vdd §VI extraction at L_max=2" as the canonical source for `nonflat_T_correction_L2`. The companion script `s86_w0c_extract_vdd_T_correction.py` globbed all 14 vdd papers in `researchers/Van-den-Dungen/`; **zero §VI / Section VI headings were found**. The 14 papers use named sections (Abstract, Key Arguments and Derivations, Key Results, Impact and Legacy, Connection to Phonon-Exflation Framework). Routing was redirected to the substrate-first canonical: S83 W2-G24 PASS, where Cartan-flatness at tau_fold yields `correction_P1_T = 0.0` to machine epsilon (`R|_{Cartan⁴} = 0`; abelian Cartan ⇒ Γ on C×C = 0).

**Classification**: GEOMETRIC (substrate Cartan-subbundle flatness is a property of the spectral triple itself, not of an excitation; pin lives on the fabric).

The W0c-3 verdict landed PASS by handling the redirection in-script. The pathology is upstream: the **plan-author** drafted external-paper provenance in the first place. The plan-time SOURCE-RECON sub-audit per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" did not catch the redirection because the audit triggers on PIN-name resolution (was the pin populated?), not on PIN-source-existence (does the cited canonical actually contain the heading?). A new audit class is required — call it **(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — with detection logic that globs the cited external source for the cited heading, and routes to substrate computation if absent.

### Witness #2 — W4-2 line 503: SCHEMATIC analogs disclosed at FAIL time

**Result**: `_spectral_action_regulators.py` helpers (zeta_a_n, mellin_a_n, heat_kernel_a_n, hard_cutoff_a_n, pauli_villars_a_n) are **schematic analogs of Connes-Chamseddine 1996 §2.2-2.3 Mellin multipliers, not the full physical regularizations**. The W4-2 K-invariance gate FAILed at max_pair_ratio = 9.240e-01 (target ≤ 1e-2). The agent's honesty disclosure at line 503 — "the K-invariance breakdown holds for these schematic forms; a live-physical-regularization re-run is a separate question" — preserves epistemic integrity but flags the structural issue: the gate's verifier rubric was **applied against a schematic regulator atlas without the rubric pre-registering the SCHEMATIC-vs-physical level**.

**Classification**: GEOMETRIC (regulator-class structure is a property of the spectral functional, not of substrate excitations; pin lives on the fabric's spectral-summation prescription).

The downstream cost is bounded — the FAIL verdict is correct under the schematic atlas, and the cascade to W5a P3 SR-flow Z-factor (also FAILed) is independent of the SCHEMATIC level. But the calibration corpus is now seeded: every SECTOR-2-class gate using `_spectral_action_regulators.py` should carry an explicit **PRIMARY (full physical regularization) vs SCHEMATIC (schematic analog)** declaration in its plan block, and the verdict line should encode the level (e.g., `convention=substrate-distance-1-SCHEMATIC` rather than the bare `substrate-distance-1`). The CC-2 PASS at rel_err = 1.7556e-16 (machine-epsilon match against Connes-Chamseddine literature anchor) confirms the schematic analogs are correctly implemented; the FAIL is structurally honest about regulator-class non-universality at the s=3 Mellin residue, not about the analog-vs-physical distinction.

### Witness #3 — W5a-2 §10: 3-OOM placeholder→canonical jump bypassed pre-compute audit

**Result**: The plan §10 substitution chain pre-registered the substrate-first source term in the SR-LO ε-flow ODE using a **placeholder** `xi_E_GGE_inv ≈ O(10⁻²)`. The W4 P4 PASS commit `S86-BRANCH-IV-FORMULATION-COMMIT` (audit `acc751101c8ca6ce`) pinned the canonical value at **xi_E_GGE_inv = 13.642473425595973** (M_KK units; substrate-natural anchor 59.8 · Δ_BCS / K_base; verified via `mcp__knowledge__.get_constant`). The mismatch:

**Substitution chain (D_max calculation, verified via Sage MCP)**:
- Step 1 (Definition): D_max ≡ |log₁₀(canonical) − log₁₀(placeholder)|.
- Step 2 (Substitute): D_max = |log₁₀(13.642473) − log₁₀(1.0e−2)| (taking the central O(10⁻²) representative; the plan literally writes `O(10⁻²)`, not a specific decade).
- Step 3 (Simplify): D_max = |1.13468 − (−2.0)| = **3.13468**.
- Step 4 (Direction): D_max = 3.135 ≥ 3.0 → **HARD-HALT band** per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" 4-band calibration ("D_max ≥ 3.0 → hard plan-freeze halt; manual review required").

The pre-compute audit did not fire because the placeholder `O(10⁻²)` is a textual approximation, not a numerical pin — the SOURCE-RECON sub-audit's `mcp__knowledge__.get_constant(name)` query requires a NAME, not a heuristic order-of-magnitude estimate. The placeholder evaded the cardinality test (PRU) and the value test (SOURCE-RECON) simultaneously.

**Substitution chain (effect at the gate, source-doc reproduction)**:
- Step 1 (Definition): (dε/dN)|substrate(0) = ε(0)·(2η(0) − 4ε(0) + 2·xi_E_GGE_inv).
- Step 2 (Substitute canonical): = 0.020·(0.010 − 0.080 + 2·13.642473) = 0.020·27.215 = **+0.5443**.
- Step 3 (Substitute placeholder): = 0.020·(0.010 − 0.080 + 2·0.01) = 0.020·(−0.050) = **−0.001**.
- Step 4 (Direction): the sign of (dε/dN)|substrate(0) flips between placeholder and canonical, AND the magnitude jumps by a factor of ~544×. Substrate/LCDM slope ratio at N=0 is **388.78** (verified via Sage), driving the SR-LO ODE into the nonlinear regime within N ≈ 0.13 e-folds, well before either pivot at N=3.12 or N=55.

**Classification**: PHONONIC (xi_E_GGE_inv is a substrate quasiparticle-pair anchor — 59.8 · Δ_BCS / K_base — directly tied to the GGE relic count and BCS gap; the placeholder vs canonical distinction is a matter of which substrate computation provides the pin).

The W5a-1 gate verdict (DOUBLE FAIL, both pivots) is **structurally correct** — the corridor SECTOR-1 SR-LO + substrate-first ξ²(0) is closed because the W4 P4 canonical IC drives the ODE out of the SR-LO linear-perturbation regime. The pathology is **the plan-author's reliance on a placeholder estimate** that survived plan-freeze without triggering pre-compute SOURCE-RECON. The §10 SIGN prediction (Z_ratio > 1) is confirmed; the §10 MAGNITUDE prediction is refuted by 2× and 92×, in the correct sign-direction but well past the linear-validity regime.

---

## III. Gate Verdicts (carried from source documents — not re-adjudicated per dispatch rule)

| Gate | Verdict | Decisive Number | Source |
|:-----|:--------|:----------------|:-------|
| S86-CANONICAL-ENTRY-CONSOLIDATION (W0c-3) | PASS | 5_entries_landed; vdd §VI absent in 14 papers; routed to S83 W2-G24 substrate canonical | W0c §W0c-3 line 357 |
| S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT (W4-2) | FAIL | max_pair_ratio = 9.240e-01 (target ≤ 1e-2); SCHEMATIC level disclosed at line 503 | W4 §W4-2 line 145 |
| S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55 (W5a-1) | FAIL | Z_ratio = 1.4353; \|Z_ratio−1\| = 0.435 ≫ 0.10 INFO ceiling | W5a §W5a-1 line 28 |
| S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312 (W5a-1) | FAIL | Z_ratio = 3.2976; \|Z_ratio−1\| = 2.298 ≫ 0.10 INFO ceiling | W5a §W5a-1 line 30 |

---

## IV. Structural Implications

### IV.1 — Three witnesses are not a coincidence; they are a class

The three witnesses span three distinct slot types:
- **W0c-3** is a META gate (canonical-constants registry consolidation); the canonical-source pathology surfaced at the writer (consolidation script's vdd-extractor companion).
- **W4-2** is a GEOMETRIC theorem-grade gate (substrate-distance-1 K-invariance test); the SCHEMATIC-vs-physical caveat surfaced at the agent's honesty disclosure at FAIL time, post-execution.
- **W5a-1** is a PHONONIC dynamics gate (SR-LO ODE integration); the placeholder-vs-canonical 3-OOM jump surfaced in the substitution-chain correction at line 53, post-execution, and is the structural root cause of the DOUBLE FAIL.

The shared pathology is **reliance on non-substrate canonical sources at plan-authorship**: external-paper sections (W0c-3), schematic library helpers (W4-2), or analytic placeholders (W5a-1). Each was a per-instance reactive fix. None was caught by the existing SOURCE-RECON sub-audit because SOURCE-RECON tests **pin-vs-canonical drift on values that are both numerically pinned**, not pin-vs-substrate-existence on values where one side is a placeholder, schematic, or missing reference.

### IV.2 — The audit class missing from `.claude/rules/epistemic-discipline.md` §"Source Reconciliation"

The current 5-class taxonomy:
- (a) PIN-TIGHT-SOURCE-LOOSE
- (b) PIN-LOOSE-SOURCE-TIGHT (FALSE-PASS direction)
- (c) PIN-DRIFT-FROM-STALE-SOURCE
- (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY
- (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS

**Missing**: (f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL. This class triggers when:
- the plan cites a NUMERICAL value as a pre-registered pin,
- the value is given as an order-of-magnitude estimate, schematic-library output, or paragraph reference to an external paper, AND
- a substrate-first canonical exists (or could be computed) for the same quantity but is NOT cited in the pin.

Severity calibration: the W5a-2 measured D_max = 3.13 OOM directly hits the existing 4-band calibration's HARD-HALT zone (D_max ≥ 3.0). For the new class (f), HARD-HALT severity is the default — placeholder-vs-substrate jumps are FALSE-PASS-direction in expectation (the placeholder is conservatively small or numerically null; the canonical is structurally large), and the W5a-1 case shows that the magnitude error can exceed the SR-LO linear-validity radius by hundreds of e-fold-equivalent slope amplification.

### IV.3 — Operationalizing `phononic-framing.md` "IS Space, Not IN Space" at the canonical-sourcing layer

`phononic-framing.md` operates at the **explanation-direction layer**: agents must invert "particles created IN curved spacetime" to "fiber spectrum reorganizes." The S86 witnesses show the same inversion is required at the **canonical-sourcing layer**: pins must source from the substrate's first-principles computation, not from external-paper provenance treated as authoritative. External papers are **methodological references** (cross-checks, anchors, conceptual framing); the substrate's own computation is the **canonical source**.

The mapping is:
- "particles created IN curved spacetime" (container-thinking, explanation) ↔ "xi_E_GGE_inv ≈ O(10⁻²) per analytic placeholder" (container-thinking, sourcing)
- "fiber spectrum reorganizes" (substrate-thinking, explanation) ↔ "xi_E_GGE_inv = 13.642473 from 59.8 · Δ_BCS / K_base substrate computation" (substrate-thinking, sourcing)

This is a STRUCTURAL theorem about where canonical authority lives, not a stylistic preference. The W0c-3 redirect demonstrates the substrate-first source is always available (S83 W2-G24 produced `correction_P1_T = 0.0` years before W0c-3's plan-author cited vdd §VI); the missing piece is the audit pattern that forces the substrate route at plan-freeze.

### IV.4 — Constraint-map updates

| Date | Mechanism / rule | Prior state | New state | Reason |
|:-----|:------|:------|:------|:------|
| 2026-04-27 | Substrate-first canonical-sourcing discipline | IMPLICIT (W0c-3 reactive handling) | EXPLICIT permanent rule (proposed at .claude/rules/substrate-first-canonical-sourcing.md) | Three independent S86 witnesses (W0c-3, W4-2, W5a-1) demonstrate plan-authorship pathology surviving SOURCE-RECON pre-flight |
| 2026-04-27 | SOURCE-RECON 5-class taxonomy | 5 classes (a)-(e) | 6 classes (a)-(f); class (f) adds HARD-HALT default severity | W5a-2 measured D_max=3.13 hits HARD-HALT band; class (f) is the structural address for placeholder-vs-substrate jumps |
| 2026-04-27 | Audit pipeline composition order | PRU → SOURCE-RECON → PRDR → execute → v3-recovery | PRU → SOURCE-RECON → SUBSTRATE-FIRST-PROVENANCE → PRDR → execute → v3-recovery | New sub-audit slot inserted between SOURCE-RECON (value test) and PRDR (machinery test); operates on pin-source-existence rather than pin-value-drift |

### IV.5 — Boundaries of the rule (what it does NOT do)

The rule applies to **canonical sourcing of pinned numerical quantities**. It does not apply to:
- Methodological cross-checks (CM-2008 cited as anchor for HP1_dim = 3 in W0c-3 entry #2 is correct usage; the substrate cross-check is S84 W10a-117).
- Conceptual framing references (citing Connes 1996 for Mellin-multiplier formalism is correct usage; the substrate computation is the spectral-action evaluation on D_K).
- Library helper-function disclosure (the W4-2 SCHEMATIC tag is not the structural problem; the missing pre-registration of the SCHEMATIC level in the gate's verifier rubric is).
- Secondary-derivation chains where the substrate primitive is many derivation-layers removed (those are class (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY, an existing class).

The rule applies precisely when a NUMERICAL pin is sourced from outside the substrate's first-principles computation, AND the substrate computation exists or could be performed.

---

## V. Carry-Forward Computations

**MANDATORY per `.claude/rules/feedback_fix-in-session-never-defer.md`**: every entry below has all four fields (What / Inputs / Gate / Effort).

### V.1. S87-SUBSTRATE-FIRST-PROVENANCE-AUDIT

- **What**: Build `computations/_substrate_first_provenance_audit.py` that, for every plan pin, (a) checks whether the cited canonical-source URL/path exists, (b) if cited as an external-paper section heading, globs the paper file for the heading and emits AUDIT-FAIL on absence, (c) if cited as an order-of-magnitude estimate or schematic-library output, queries `mcp__knowledge__.get_constant(name)` for the substrate-first canonical and emits CLASS-(f) HARD-HALT on D_max ≥ 3.0, (d) if cited correctly from substrate-first computation, emits PASS. Output: per-pin classification table {PASS, CLASS-(f)-HARD-HALT, ABSENT-EXTERNAL-HEADING, SCHEMATIC-UNDISCLOSED}; aggregate session-level signal `sig_6 = 0` if any pin returns non-PASS.
- **Inputs**: plan file (`sessions/session-plan/session-87-plan-*.md`); `mcp__knowledge__` MCP tools (get_constant, search_knowledge); glob over `researchers/*/`; `_pru_cardinality_audit.py` and `_source_reconciliation_audit.py` as composition-pattern templates.
- **Gate**: NEW gate `S87-SUBSTRATE-FIRST-PROVENANCE-AUDIT` with PASS = all pins classified PASS; FAIL = at least one pin returns CLASS-(f)-HARD-HALT, ABSENT-EXTERNAL-HEADING, or SCHEMATIC-UNDISCLOSED; INFO = pins flagged but plan author has logged explicit override with substrate-first justification. Threshold: PASS_REL_TOL n/a (categorical), 100% pin coverage required.
- **Effort**: 1 wave-equivalent (single agent session, ~3-4 hours). Script reuses `_source_reconciliation_audit.py` infrastructure; new logic is the heading-glob + placeholder-pattern detector. Self-tests modeled on `_recovery_controller.py --self-test` pattern (3 synthetic cases: (i) external-paper heading present → PASS; (ii) external-paper heading absent → ABSENT-EXTERNAL-HEADING; (iii) placeholder O(10⁻ⁿ) with substrate canonical D_max ≥ 3 → CLASS-(f)-HARD-HALT).

### V.2. S87-W5A-RESCALED-IC-RETRY (carry-forward from W5a-1, restated under new rule)

- **What**: Re-run the SR-LO Z-factor ODE with the canonical xi_E_GGE_inv = 13.642473 substituted at plan-freeze (not at post-hoc correction) AND with an IC rescaling that holds the substrate-first source term within the SR-LO linear-perturbation validity radius. The rescaling parameter γ ∈ (0, 1] is treated as a free parameter; PASS for any γ such that ε(N_pivot) < 0.5 across the integration window [0, 55].
- **Inputs**: `computations/s86_w5a_p3_sector_1_z_factor.npz` (W5a-1 data); canonical xi_E_GGE_inv from `mcp__knowledge__.get_constant` (NOT from a placeholder); SR-LO ODE machinery from `s86_w5a_p3_sector_1_sr_flow.py`; rescaling parameter scan γ ∈ {0.001, 0.01, 0.1, 1.0}.
- **Gate**: NEW gate `S87-SECTOR-1-SR-FLOW-RESCALED` with PASS band `|Z_ratio − 1| ≤ 0.05` for some γ ≤ 1; FAIL if no γ in the scan range satisfies the linear-validity criterion (i.e., the SR-LO + substrate-first IC corridor is closed even with rescaling).
- **Effort**: 0.5 wave-equivalents. Script reuses W5a-1 ODE machinery; new γ-scan adds the analysis cost. This carry-forward already existed in W5a's own §V; restating here under the new substrate-first rule because the rescaling itself is a substrate-first operation (the rescaling factor must come from a substrate computation, not from a tuning parameter).

### V.3. S87-W4-SCHEMATIC-vs-PHYSICAL-LEVEL-PRE-REGISTRATION

- **What**: Extend the plan-authorship template `.claude/templates/synthesis.md` and the gate-block schema in `.claude/templates/pru-pre-registration-template.md` to require an explicit **level pin** for any gate consuming `_spectral_action_regulators.py` or any other helper module whose docstring identifies it as a SCHEMATIC analog. Level pin values: PRIMARY (full physical regularization, e.g., a live Mellin-cone via `analytic_zeta`), SCHEMATIC (schematic analog with deterministic helper). Verdict line MUST encode the level in `convention=` (e.g., `convention=substrate-distance-1-SCHEMATIC` rather than bare `substrate-distance-1`).
- **Inputs**: `.claude/templates/pru-pre-registration-template.md`; `.claude/templates/synthesis.md`; `_spectral_action_regulators.py` docstring + W4-2 line 503 honesty disclosure.
- **Gate**: NEW gate `S87-LEVEL-PIN-RETROFIT` with PASS = template includes PRIMARY/SCHEMATIC pin field + audit script `_tier_pin_audit.py` greps gate blocks for level pin presence; FAIL = template lacks the field or audit detects unpinned gates. Threshold: 100% gate-block coverage in any S87+ plan.
- **Effort**: 0.25 wave-equivalents. Single template edit + small audit script. No physics computation; pure plan-authorship hardening.

### V.4. S87-PHONONIC-FRAMING-CANONICAL-SOURCING-CROSS-LINK

- **What**: Add a cross-link section to `.claude/rules/phononic-framing.md` identifying that the "IS Space, Not IN Space" mandate has TWO operational layers: (1) explanation-direction layer (existing; agents must invert container-thinking in narrative); (2) canonical-sourcing layer (new; pins must source from substrate-first computation). Cross-link to `.claude/rules/substrate-first-canonical-sourcing.md` (this synthesis's deliverable).
- **Inputs**: `.claude/rules/phononic-framing.md` (existing); `.claude/rules/substrate-first-canonical-sourcing.md` (this synthesis's proposed file).
- **Gate**: NEW gate `S87-FRAMING-RULE-CROSS-LINK` with PASS = both rule files cite each other; the explanation-direction layer and the canonical-sourcing layer are each documented with their own calibration corpus. Threshold: 2 mutual-citation edits, both files updated atomically.
- **Effort**: 0.1 wave-equivalents. Two file edits; no new computation.

### V.5. S87-PLACEHOLDER-PATTERN-DETECTOR-CALIBRATION

- **What**: Build a regex-based placeholder-pattern detector inside `_substrate_first_provenance_audit.py` that catches the W5a-2 pathology at plan-authorship time. Patterns to detect: `O\(10\^?-?\d+\)`, `≈ O\(`, `~ 10\^?-?\d+`, `placeholder`, `analytic estimate`, `rough estimate`, `order-of-magnitude`, `TBD`, `pending`. When any pattern fires inside a PIN value field (not in a comment), audit emits CLASS-(f) flag and queries the knowledge MCP for a canonical name match.
- **Inputs**: W5a-2 §10 substitution chain text as the calibration corpus (the literal phrase `xi_E_GGE_inv ≈ O(10⁻²)`); `mcp__knowledge__.search_knowledge` for canonical-name match resolution.
- **Gate**: NEW gate `S87-PLACEHOLDER-PATTERN-DETECTOR-VALIDATION` with PASS = synthetic test case using the W5a-2 placeholder text triggers CLASS-(f)-HARD-HALT and the canonical xi_E_GGE_inv is suggested as the substrate-first replacement; FAIL = either non-detection or wrong canonical suggestion.
- **Effort**: 0.25 wave-equivalents. Regex set + knowledge-MCP query wrapper; small synthetic-test harness.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:------|:------|:------|:------|
| 1 | W0c-3 vdd §VI absent in 14 papers; routed to S83 W2-G24 substrate canonical | GEOMETRIC | PASS (W0c-3) | Demonstrates substrate-first source always available; plan-author pathology was the citation, not the substrate |
| 2 | W4-2 SCHEMATIC analogs disclosed at line 503 | GEOMETRIC | FAIL (W4-2) | Level pre-registration missing from gate block; verdict structurally honest under schematic atlas |
| 3 | W5a-2 placeholder→canonical D_max = 3.135 (HARD-HALT band) | PHONONIC | FAIL (W5a-1 both pivots) | 388.78× substrate/LCDM slope ratio at N=0; SR-LO linear-validity exited within 0.13 e-folds |
| 4 | Three-witness convergence is structural, not coincidental | META | RULE-PROPOSED | New permanent rule at `.claude/rules/substrate-first-canonical-sourcing.md` |
| 5 | SOURCE-RECON taxonomy extended to 6 classes | META | RULE-PROPOSED | New class (f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL; HARD-HALT default at D_max ≥ 3.0 |

---

## VII. Proposed Rule-File Content (for orchestrator installation)

The following is the COMPLETE PROPOSED CONTENT for `.claude/rules/substrate-first-canonical-sourcing.md`. Per dispatch instructions, this synthesis does NOT directly create the rule file; the orchestrator will install it after review.

```markdown
# Substrate-First Canonical-Sourcing Discipline

> **Provenance**: S86 W1a Slot 1a entry S-3 (lizzi-spectral-functional-theorist, 2026-04-27).
> Three independent witnesses surfaced the same plan-authorship pathology — canonical sourcing of substrate quantities was assigned to external-paper provenance where the substrate's own first-principles computation is the structural canonical. Calibration corpus pinned at:
> - W0c-3 §(b) (vdd §VI absent in 14 papers; rerouted to S83 W2-G24 Cartan-flat R\|_{Cartan⁴} = 0)
> - W4-2 line 503 (SCHEMATIC `_spectral_action_regulators.py` helpers vs full Connes-Chamseddine 1996 §2.2-2.3 physical multipliers)
> - W5a-2 §10 (placeholder `xi_E_GGE_inv ≈ O(10⁻²)` vs canonical `xi_E_GGE_inv = 13.642473425595973` from W4 P4 commit; D_max = 3.13 OOM hits HARD-HALT band)

## Scope

This rule operates at the **canonical-sourcing axis** for every NUMERICAL pin in a computation script, working-paper section, plan-block PIN MAP, or canonical_constants.py provenance entry. It is complementary to but distinct from `phononic-framing.md`'s **explanation-direction axis**:

- `phononic-framing.md` operates at the explanation layer: agents must invert container-thinking in narrative ("particles created IN curved spacetime" → "fiber spectrum reorganizes").
- `substrate-first-canonical-sourcing.md` operates at the sourcing layer: pins must source from the substrate's first-principles computation, not from external-paper provenance treated as authoritative.

The two operate at the same epistemological depth (substrate is logically prior to emergent observables) but apply to disjoint artifact classes (narrative paragraphs vs numerical pin sources).

## (i) When external-paper provenance is methodological vs canonical

External-paper citations are **METHODOLOGICAL** (correct usage) when they serve as:
- Conceptual framing references (e.g., "the Connes-Chamseddine 1996 Mellin-multiplier formalism inspires the schematic helpers in `_spectral_action_regulators.py`")
- Cross-check anchors (e.g., "CM-2008 Table 2 confirms HP1_dim = 3, consistent with S84 W10a-117 R-protection rank-3 image")
- Heritage citations (e.g., "Volovik's superfluid universe analogy maps to the BEC acoustic white hole projection of substrate transit")
- Notational source for definitions (e.g., "Mukhanov-Sasaki gauge per Mukhanov 1985 §3")

External-paper citations are **CANONICAL** (FORBIDDEN — must reroute to substrate-first source) when they:
- Provide the NUMERICAL VALUE of a pin without the substrate-first computation having been performed (e.g., "xi_E_GGE_inv ≈ O(10⁻²) per analytic placeholder" — the substrate canonical 13.642473 from S86 W4 P4 must be cited instead)
- Cite a paper section heading as the source of a numerical extraction without verifying the heading exists (e.g., "vdd §VI extraction at L_max=2" when no vdd paper has §VI)
- Treat schematic library helper outputs as physical regularizations without disclosing the SCHEMATIC level (e.g., `_spectral_action_regulators.py.zeta_a_n(...)` cited as "the zeta-regulated Seeley-DeWitt coefficient" without SCHEMATIC disclosure)
- Use order-of-magnitude estimates as pinned values when the substrate canonical exists (e.g., placeholder vs. canonical xi_E_GGE_inv pathology)

The distinction is operational: a methodological citation supports the substrate-first computation; a canonical citation REPLACES it. Only the former is allowed.

## (ii) Audit pattern (glob external source for the heading; if absent, route to substrate computation)

For every plan pin (name = value) at plan-freeze, the SUBSTRATE-FIRST-PROVENANCE sub-audit:

1. Inspects the pin's PROVENANCE field. If the provenance cites `<external-paper-path> §<section-id>` or `<external-paper-path>:<line-range>`:
   - Glob the external-paper file for the cited section heading or line range.
   - If absent: emit AUDIT-FAIL `ABSENT-EXTERNAL-HEADING`; query `mcp__knowledge__.search_knowledge(name)` for the substrate-first canonical and recommend rerouting to the substrate source.
2. If the provenance cites a placeholder pattern (`O(10⁻ⁿ)`, `≈ ...`, `placeholder`, `TBD`, `pending`, `analytic estimate`):
   - Query `mcp__knowledge__.get_constant(name)` for the canonical value.
   - If a canonical exists with `D_max = |log₁₀(canonical) − log₁₀(placeholder_central)| ≥ 3.0`: emit AUDIT-FAIL `CLASS-(f) HARD-HALT`.
   - If a canonical exists with `1.0 ≤ D_max < 3.0`: emit `CLASS-(f) MANDATORY` (route to manual remediation).
   - If no canonical exists: emit `CLASS-(f) ADVISORY` (substrate computation required before plan-freeze).
3. If the provenance cites a schematic library helper (`_spectral_action_regulators.py`, `_phononic_helpers.py`, etc., where the docstring identifies the module as SCHEMATIC):
   - Verify the gate-block has an explicit level pin (PRIMARY = full physical; SCHEMATIC = schematic analog).
   - If level pin absent: emit AUDIT-FAIL `SCHEMATIC-UNDISCLOSED`.
   - If level pin = SCHEMATIC: verify the verdict-line `convention=` field encodes the SCHEMATIC suffix; AUDIT-PASS conditional on verdict-line emission.
4. If the provenance cites a substrate-first computation (a `computations/sN_*.py` script or `computations/sN_*.npz` data file from the framework's own computation): emit AUDIT-PASS.

The audit script is `computations/_substrate_first_provenance_audit.py` (proposed S87 carry-forward V.1; not yet implemented). It executes after `_source_reconciliation_audit.py` and before `_pru_cardinality_audit.py`'s PRDR machinery enumeration.

### Audit pipeline composition order (S87+)

```
PRU (cardinality pre-flight)
  → SOURCE-RECON (value drift on pinned-vs-pinned)
  → SUBSTRATE-FIRST-PROVENANCE (source-existence on pin-vs-substrate-canonical)
  → PRDR (machinery enumeration)
  → gate execution
  → v3-recovery audit
```

## (iii) Worked example — W0c-3 routing decision

The W0c-3 plan-author drafted entry #5 with provenance "vdd §VI extraction at L_max=2" for the canonical constant `nonflat_T_correction_L2`.

Pre-existing audit pipeline at S86: PRU passed (the pin name was present); SOURCE-RECON passed (the pin value `0.0` had no canonical to drift from — the constant was missing pre-W0c-3). The pathology evaded both audits.

Companion script `s86_w0c_extract_vdd_T_correction.py` performed the heading glob at runtime:
- Globbed `researchers/Van-den-Dungen/*.md` → 14 papers + AGENTS.md + index.md.
- Greps each paper for `^#+ .*VI` and `^#+ .*Section VI` headings → 0 matches across 14 papers.
- Identified that the 14 papers use named sections (Abstract, Key Arguments and Derivations, Key Results, Impact and Legacy, Connection to Phonon-Exflation Framework), not numbered Roman-numeral sections.

Routing decision: redirect to the substrate-first canonical source S83 W2-G24 (`computations/s83_w2_g24_nonflat_t_correction_l2.npz`, key `correction_P1_T = 0.0`, verdict PASS, reason: "Cartan subbundle is FLAT at tau_fold; abelian Cartan ⇒ Γ on C×C = 0 ⇒ R\|_{Cartan⁴} = 0 to machine epsilon. Non-flat T-correction is negligible.").

Outcome: W0c-3 verdict landed PASS by handling the redirection in-script. Per the new SUBSTRATE-FIRST-PROVENANCE sub-audit, the routing would have been forced at plan-freeze:
- Audit step 1 globs `researchers/Van-den-Dungen/*.md` for §VI; emits ABSENT-EXTERNAL-HEADING.
- Audit step 1 then queries `mcp__knowledge__.search_knowledge("nonflat_T_correction substrate first principles")` → top hit `s83_w2_g24_nonflat_t_correction_l2.npz`; recommends rerouting.
- Plan-author updates the PROVENANCE field to cite S83 W2-G24 directly; audit re-emits PASS.

Canonical lesson: **when an external-paper provenance citation cannot be verified by heading glob, the substrate-first canonical is the structural source, not the missing paper section**. The W0c-3 case is the canonical worked example for class (f) SOURCE-RECON detection.

## (iv) The W4-2 "SCHEMATIC vs full physical" level rule

For any computation script consuming a helper module whose docstring identifies it as a SCHEMATIC analog:

1. The plan gate-block MUST include a level pin field with one of two values:
   - **PRIMARY (full physical regularization)**: the helper is a faithful implementation of the underlying physical regularization (e.g., a live Mellin-cone evaluator via `analytic_zeta`, a full Pauli-Villars subtraction with mass-scale running).
   - **SCHEMATIC (schematic analog)**: the helper is a deterministic schematic that captures the structural form of the regularization but not the full physical content (e.g., `_spectral_action_regulators.py` per its own docstring).
2. The verdict line MUST encode the level in the `convention=` field (e.g., `convention=substrate-distance-1-SCHEMATIC` rather than bare `substrate-distance-1`).
3. The synthesis section for the gate MUST include an explicit cross-level disclosure paragraph (modeled on W4-2 line 503: "the K-invariance breakdown holds for these schematic forms; a live-physical-regularization re-run is a separate question").

Without (1)-(3), gate verdicts under SCHEMATIC helpers are structurally indistinguishable from gate verdicts under PRIMARY physical regularizations in downstream consumption (registry rows, knowledge-MCP indexing, cross-session synthesis), creating a LEVEL-conflation pathology analogous to the regulator-conflation pathology (`UV_REGULARIZATION_CONFLATION` per S75 ZETA-NOT-PHYSICAL-75 PASS).

The W4-2 case is the calibration corpus: the agent's honesty disclosure at line 503 PRESERVED epistemic integrity post-execution, but the structural fix is to PRE-REGISTER the level pin at plan-freeze, not to rely on agent honesty at FAIL time.

## (v) SOURCE-RECONCILIATION audit class (f) — PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL

Extension to `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" 5-class taxonomy:

**(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL** — the plan pin is given as a textual approximation, order-of-magnitude estimate, or placeholder string, AND a substrate-first canonical exists (or could be computed) for the same quantity.

Detection:
- Pattern set on the pin's VALUE field: `O\(10\^?-?\d+\)`, `≈ ...`, `~ 10\^?-?\d+`, `placeholder`, `TBD`, `pending`, `analytic estimate`, `rough estimate`, `order-of-magnitude`.
- Conjunction with substrate-canonical existence test: `mcp__knowledge__.get_constant(name)` returns a value, OR `mcp__knowledge__.search_knowledge(name)` returns a substrate-computation hit.

Severity (HARD-HALT default at D_max ≥ 3.0):
- D_max ≥ 3.0 → **HARD-HALT** (per W5a-2 measured D_max = 3.13; the placeholder-vs-substrate jump magnitude exceeded the SR-LO linear-validity radius and produced a 388.78× slope amplification).
- 1.0 ≤ D_max < 3.0 → **MANDATORY** (route to manual remediation; pre-registered canonical substitution before plan-freeze).
- 0.1 ≤ D_max < 1.0 → **ADVISORY** (substrate canonical recommended but not blocking).
- D_max < 0.1 → **NO-ACTION** (within S82-class-(d) absorbable band).

Remediation:
- (f) → query `mcp__knowledge__.get_constant(name)` for the canonical value; substitute into the plan PIN VALUE field; re-run SUBSTRATE-FIRST-PROVENANCE sub-audit; PASS on canonical substitution.

Calibration corpus precedents:
- **W5a-2 `xi_E_GGE_inv`** (S86 W5a-2 §10 substitution chain, lizzi 2026-04-27): placeholder `O(10⁻²)` vs canonical `13.642473425595973` from W4 P4 commit; D_max = 3.13; HARD-HALT band; substrate-first source is `sessions/framework/registry/branch-iv-canonical.md` §3 (formula source: lizzi 9A §2.2; substrate-natural anchor: 59.8 · Δ_BCS / K_base). First class-(f) instance; canonicalizes the placeholder-vs-substrate-canonical jump as the structural pathology this class addresses.

## Cross-link to `phononic-framing.md`

The "IS Space, Not IN Space" mandate operates at TWO operational layers:

1. **Explanation-direction layer** (existing; `phononic-framing.md` body): agents must invert container-thinking in narrative. Every explanation flows FROM substrate TOWARD emergent physics.
2. **Canonical-sourcing layer** (this rule; new): pins must source from substrate-first computation. External-paper provenance is methodological cross-check, never canonical replacement.

The two layers are complementary and non-overlapping. An agent who narrates substrate-first ("the fiber's eigenvalue spectrum reorganizes at the fold") but cites an external-paper placeholder for the numerical pin (`xi_E_GGE_inv ≈ O(10⁻²)`) violates the canonical-sourcing layer while honoring the explanation-direction layer. Both layers must be satisfied.

The structural reason: the substrate is logically prior at BOTH the conceptual level (where do explanations come from?) and the numerical level (where do pin values come from?). External papers are derived consequences, used as cross-checks. The substrate's own computation is canonical at both layers.

## Carry-Forward (S87)

- `S87-SUBSTRATE-FIRST-PROVENANCE-AUDIT`: implementation of `computations/_substrate_first_provenance_audit.py` (V.1 in this synthesis).
- `S87-PLACEHOLDER-PATTERN-DETECTOR-CALIBRATION`: regex set + knowledge-MCP query wrapper (V.5 in this synthesis).
- `S87-W4-SCHEMATIC-vs-PHYSICAL-LEVEL-PRE-REGISTRATION`: template hardening (V.3).
- `S87-PHONONIC-FRAMING-CANONICAL-SOURCING-CROSS-LINK`: mutual-citation edits in `phononic-framing.md` and this rule (V.4).
- `S87-W5A-RESCALED-IC-RETRY`: rerun under canonical xi_E_GGE_inv with rescaling scan (V.2).

## Source

S86 W1a Slot 1a entry S-3 (lizzi-spectral-functional-theorist solo synthesis, 2026-04-27).
Three witnesses calibration corpus: W0c-3 §(b), W4-2 line 503, W5a-2 §10.
SOURCE-RECONCILIATION extension target: `.claude/rules/epistemic-discipline.md` §"Source Reconciliation".
Cross-link target: `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space — Mandatory Reframe".
```

---

## VIII. Audit-Script Specification (companion to V.1; do not implement in this synthesis)

The companion to the rule file is the audit script `computations/_substrate_first_provenance_audit.py`. Specification (per dispatch instructions to produce the spec, not the script):

**Module signature**:
```python
def audit_plan_pin(
    pin_name: str,
    pin_value: str,            # raw text from plan PIN MAP value field
    pin_provenance: str,       # raw text from plan PIN MAP provenance field
    plan_file_path: Path,
) -> dict:
    """
    Returns: {
        "pin_name": str,
        "classification": str,  # one of: "PASS", "CLASS-(f)-HARD-HALT",
                                #         "CLASS-(f)-MANDATORY", "CLASS-(f)-ADVISORY",
                                #         "ABSENT-EXTERNAL-HEADING", "SCHEMATIC-UNDISCLOSED"
        "D_max": float | None,
        "substrate_canonical_suggestion": str | None,  # name of canonical to reroute to
        "remediation_text": str,                       # human-readable instructions
    }
    """
```

**Core detection logic** (3 sub-routines):

1. `_detect_placeholder_pattern(value: str) -> bool`: regex set `{O\(10\^?-?\d+\), ≈ ..., placeholder, TBD, pending, analytic estimate}`; returns True if any pattern matches.
2. `_glob_external_heading(provenance: str) -> tuple[bool, list[str]]`: parses provenance for `<path> §<section>` or `<path>:<line>`; globs the path and greps for the section/line; returns (heading_present, search_artifacts).
3. `_detect_schematic_helper(provenance: str) -> bool`: parses provenance for helper-module paths; reads each helper's docstring for `SCHEMATIC` marker; returns True if any helper is SCHEMATIC and gate-block lacks level pin.

**Composition with existing audits**:
- Runs AFTER `_source_reconciliation_audit.py` (which tests pin-vs-pinned drift).
- Runs BEFORE `_pru_cardinality_audit.py`'s PRDR machinery enumeration (which tests pin-presence cardinality).
- Aggregate session-level signal `sig_6 = 0` if any pin returns non-PASS; integrates with `v3-closure-recovery.md` Stage-1 remediation map (new sig_6 row).

**Self-tests** (3 synthetic cases per `_recovery_controller.py --self-test` pattern):
- (i) external-paper heading present (e.g., `researchers/Connes/Connes-1996.md §2.2`): PASS.
- (ii) external-paper heading absent (e.g., `researchers/Van-den-Dungen/vdd-paper-01.md §VI`): ABSENT-EXTERNAL-HEADING; suggest rerouting to substrate canonical.
- (iii) placeholder `xi_E_GGE_inv ≈ O(10⁻²)` with substrate canonical `13.642473`: CLASS-(f)-HARD-HALT (D_max = 3.13).

**Implementation effort**: 1 wave-equivalent (3-4 hours, 1 agent session per V.1 spec). Implementation queued for S87.

---

**End of synthesis.**
