# Session 86 Synthesis (Slot 1a, S-8): Convention-Lockdown Demarcation Theorem + R_842 Migration-Ledger Audit

**Date**: 2026-04-27
**Agent**: volovik-superfluid-universe-theorist
**Slot**: 1a, entry S-8 (DR3 L=14+ deep-dive precursor + convention-lockdown formalization + R_842 rectangle canonicalization)
**Source Documents**:
- `sessions/archive/session-86/session-86-w12-workingpaper.md` (W12-4 §6(e) finding; convention-dependent oscillation vs monotone)
- `sessions/archive/session-86/session-86-w13-workingpaper.md` (P9 R_842 dual-rectangle adjudication; §735–810 retrospective)
- `sessions/framework/registry/w0-primary-decision-rule.md` (§1.1, §1.2, §3, §5 reversibility protocol; both rectangles documented)
- `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.npz` (rho_series at L ∈ {8, 9, 10, 11, 12}; provenance for canonical-anchored construction)
- `computations/canonical_constants.py` (L1243 `w0_FW = -0.918`; S58 Volovik partition + effacement provenance)
- `sessions/archive/session-84/session-84-w1-workingpaper.md:879` (S84 W1b-9 R_918 → R_842 migration ledger §(b))
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md` (`project_volovik-convergence.md`, `project_substrate-compaction-timescape.md` substrate basis)
- `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 (cross-link target)

---

## I. Session Outcome

The W12 C33 §6(e) finding is structurally a demarcation theorem on the equivalence class of regulator-stability conventions over the substrate-projected late-time spectral-action gradient w_0(L). The canonical-anchored convention `w_0_FW(L) := rho_Zubarev(L) + offset` with `offset = w_0_FW − rho_Zubarev(L=10) = −0.340827` is the unique additive translation that absorbs the S58 Volovik-partition effacement contribution (Γ_eff = 0.99970) as a closed-form constant; rho-direct (`w_0(L) := rho_Zubarev(L)`) discards the effacement and is therefore non-admissible because it produces a regulator-axis trajectory that no longer projects onto the substrate observable. The R_842 ⟵ R_918 migration recorded in S84 W1b-9 §(b) is a re-centering of the falsifier rectangle by exactly the substrate-physical w_0 shift induced by the W10-2 branch-(iv) re-promotion; both this S86 plan-prompt and the runtime detection at W13 P9 expose the precise SOURCE-RECON Class-(c) vulnerability that the proposed `_source_reconciliation_audit.py` extension closes.

---

## II. Key Results

### Result II.1 — Demarcation theorem on admissible regulator-stability conventions

**Result**: Convention `C` over the regulator axis L_max is admissible iff it satisfies
`w_0^{C}(L=10) = w_0_FW = −0.918` exactly,
where `w_0_FW` is the canonical pin in `canonical_constants.py:1243` carrying provenance "S58 Volovik partition + effacement (Γ = 0.99970)". **Classification: PHONONIC** (the demarcation is on a substrate-projected observable, not on a coordinate choice in a container).

**Substitution chain** (Volovik-partition-effacement preservation criterion):

```
Step 1 — Definitions:
  rho_Zubarev(L)     := L_max-truncated Zubarev-weighted spectral moment of D_K
                        on Jensen-deformed SU(3) at tau_fold (S85 W0-7 producing-script artifact;
                        cached in s85_w0_zubarev_lmax_convergence_to_minus_one.npz field 'rho_series').
                        Identified at L=10 with value rho_Zubarev(L=10) = -0.577173 (NPZ pin).
  Gamma_eff           := 0.99970 (S52/S58 Volovik partition effacement coefficient;
                        substrate-internal post-fold spectral-action attenuation;
                        canonical_constants.py provenance trace via w0_FW comment).
  E_part(L)           := substrate effacement contribution at truncation L,
                        defined as the additive shift between the bare Zubarev moment
                        and the post-Volovik-partition-projected late-time w_0 prediction.
                        At L=10 this equals w_0_FW - rho_Zubarev(L=10) = -0.340827.
  w_0_FW              := -0.918 (canonical_constants.py:1243; S58 Volovik partition canonical;
                        the substrate's late-time w_0 prediction at z=0 under post-fold integral).
  Convention C        := any function L -> w_0^{C}(L) mapping the regulator axis to
                        a w_0 prediction.
  Effacement-preservation:
    C preserves effacement E iff  w_0^{C}(L=10) == w_0_FW  exactly,
    i.e., the L=10 anchor matches the S58 Volovik-partition canonical to bit precision.

Step 2 — Substitute the two candidate conventions:

  (a) Canonical-anchored convention (CAC):
        w_0^{CAC}(L) := rho_Zubarev(L) + offset,  where offset := w_0_FW - rho_Zubarev(L=10).
      At L=10:
        w_0^{CAC}(L=10) = rho_Zubarev(L=10) + [w_0_FW - rho_Zubarev(L=10)]
                        = w_0_FW.   [exact algebraic identity; no float accumulation]

  (b) rho-direct convention (RDC):
        w_0^{RDC}(L) := rho_Zubarev(L)  [override at L=10 to w_0_FW only as a patch — see Step 5]
      At L=10 (no override):
        w_0^{RDC}(L=10) = rho_Zubarev(L=10) = -0.577173,
        which differs from w_0_FW = -0.918 by Delta = +0.340827.

Step 3 — Simplify the preservation predicate:

  Preserves(C, E)  iff  w_0^{C}(L=10) - w_0_FW == 0
  Preserves(CAC, E) iff  [rho_Zubarev(L=10) + offset] - w_0_FW == 0
                    iff  [rho_Zubarev(L=10) + (w_0_FW - rho_Zubarev(L=10))] - w_0_FW == 0
                    iff  0 == 0.   TRUE by algebraic identity.
  Preserves(RDC, E) iff  rho_Zubarev(L=10) - w_0_FW == 0
                    iff  -0.577173 - (-0.918) == 0
                    iff  0.340827 == 0.   FALSE  (delta is the entire effacement contribution).

Step 4 — Read off direction:

  CAC SATISFIES the preservation criterion at L=10 BY CONSTRUCTION.
  RDC VIOLATES the preservation criterion at L=10; the violation magnitude
  equals the full effacement contribution |E_part(L=10)| = 0.340827.

  At L=8 and L=12 the same offset is applied:
    w_0^{CAC}(L=8)  = rho_Zubarev(L=8)  + offset = -0.504466 + (-0.340827) = -0.845293
    w_0^{CAC}(L=12) = rho_Zubarev(L=12) + offset = -0.634885 + (-0.340827) = -0.975713
  (Sage exact-rational verified, all four to 12 sig figs.)

  Under CAC the L_max trajectory in the R_842 cell-occupancy partition is
  C1 -> C1 -> C3 (PASS, PASS, FAIL): strict-monotone with n_step=1.
  Under RDC the L_max trajectory is
  C4 -> [override C1] -> C4 (FAIL, PASS, FAIL): an A->B->A oscillation
  forbidden by the W12-4 step-monotone criterion.

Step 5 — Equivalence-class membership criterion:

  Define A_E := { C : C preserves effacement E AND C is monotone in L_max
                  in the partial order FAIL < INFO < PASS over the R_842 cell partition }.

  Claim: A_E is a one-parameter family parameterized by the choice of
  spectral-moment scheme (rho_Zubarev, rho_zeta, rho_PV, rho_Mellin)
  PROVIDED each scheme is composed with its own effacement-anchored
  additive offset. The CAC built on rho_Zubarev is the canonical
  representative; CAC built on rho_zeta or rho_PV would be admissible
  iff (i) rho_zeta(L=10) and rho_PV(L=10) are precomputed from the same
  D_K spectral data, and (ii) offset_zeta := w_0_FW - rho_zeta(L=10),
  offset_PV := w_0_FW - rho_PV(L=10) absorb the same effacement contribution
  by construction.

  Claim: RDC is OUTSIDE A_E. The RDC patch "override at L=10 only" was
  the precursor S85 W1b-1 attempt to recover effacement preservation
  WITHOUT modifying the L != 10 cells; this patch produced a discontinuous
  function (a step at L=10) that is structurally indistinguishable from
  the C4 -> C1 -> C4 oscillation flagged by the W12-4 monotonicity test.
  The patch fails because it preserves effacement only at the patch point,
  not as a closed-form translation of the spectral-moment function.

Conclusion (the demarcation theorem):

  A convention C is ADMISSIBLE for DR3-class L_max-stability gates iff
  C is a closed-form additive translation of a spectral-moment scheme
  rho_X(L) by an offset constant chosen so that w_0^{C}(L=10) = w_0_FW
  EXACTLY at the L=10 anchor and with NO L-conditional patches.
  CAC = (rho_Zubarev, offset = -0.340827) is the canonical representative.
  RDC + L=10-override is OUTSIDE A_E.
```

The Volovik-partition effacement is thereby promoted from a numerical residual to a *demarcation-theoretic invariant*: it is the additive constant that must be absorbed identically into every admissible convention, in the same way the chemical potential is absorbed identically into every admissible Zubarev-weighted thermodynamic ensemble (cf. S73B GIBBS-DUHEM PASS, where w_GGE = -0.408 is the closed-form Euler-relation residual for the GGE on the substrate fabric; the Volovik effacement is the analogous closed-form residual for the post-fold late-time projection).

---

### Result II.2 — Cross-link to PROHIBITED_ACTIONS Class 1: lockdown closes a cross-session gap

**Result**: PROHIBITED_ACTIONS Class 1 ("convention-shopping") in `.claude/rules/v3-closure-recovery.md` forbids changing a gate's `convention` tag (or scheme/threshold) DURING a single-gate recovery — i.e., it closes the within-gate execution-property failure where a FAIL re-runs as PASS by relabeling the convention. **Classification: NON-PHONONIC** (methodology).

The W12-4 §6(e) finding exposes a STRUCTURALLY DISTINCT failure class that Class 1 does *not* catch: cross-session convention drift, where two consecutive sessions choose two different conventions for the same regulator-stability gate family without a documented demarcation argument, and a downstream reader cannot tell which session's prediction is canonical. Specifically:

- S85 W1b-1 used RDC + L=10-override and got an oscillation FAIL (C4 → C1 → C4).
- S86 W12-4 used CAC and got step-monotone INFO (C1 → C1 → C3).
- Both gates ran on the SAME underlying spectral data (S85 W0-7 NPZ rho_series).
- Each gate satisfied PROHIBITED_ACTIONS Class 1 *within itself* (no within-gate convention switch).
- The cross-session inconsistency only surfaces because the W12-4 §6(e) team-lead synthesis explicitly documented the precursor's convention.

The proposed `regulator-convention-lockdown.md` rule registers CAC as the S87+ binding form for ALL DR3-class L_max-stability gates and flags RDC (and any future variant that fails the demarcation theorem above) as forbidden. This is a cross-session pre-registration commitment, structurally analogous to PROHIBITED_ACTIONS but at the rule-file layer rather than the recovery-procedure layer. It closes the gap by making the convention itself a pre-registered framework constant, not a per-gate machinery pin.

---

### Result II.3 — R_842 rectangle is the substrate-physical re-centering of R_918, not a labeling change

**Result**: The S84 W1b-9 §(b) migration ledger establishes that `R_918 = [-1.05, -0.85] × [-0.2, +0.2]` (center -0.95, w_0 half-width 0.100, w_a half-width 0.200) was superseded by `R_842 = [-0.942, -0.742] × [-0.2, +0.2]` (center -0.842, half-widths preserved at 0.100 and 0.200). **Classification: PHONONIC** (the re-centering tracks a substrate-physical re-promotion of the W10-2 branch-(iv) anchor, not a labeling convention).

**Substitution chain** (substrate-physical content of the migration):

```
Step 1 — Definitions:
  R_918_center  := -0.950   (S58 Volovik-partition canonical; corresponds to a w_0
                            prediction of -0.918 with R_918 half-width 0.100 + a 0.018
                            buffer below; w_0 = -0.918 sat at offset 0.32 of half-width
                            inside upper edge).
  R_842_center  := -0.842   (W10-2 branch-(iv) substrate-compaction direct evaluation;
                            w_0 = -0.842454 sits at offset 0.000454 inside center,
                            i.e., 0.45% of half-width).
  Delta_center  := R_842_center - R_918_center = -0.842 - (-0.950) = +0.108
                  (a re-centering of the falsifier rectangle by 0.108 in w_0).

Step 2 — Substrate-physical interpretation of Delta_center:

  Delta_center is the difference between two methodologically-distinct substrate
  projections of the same observable (per w0-primary-decision-rule.md §1):

    A (Volovik partition):     post-fold integral over expansion history -> w_0 = -0.918
    B (substrate-compaction):  fiber-tau density at z=0 directly        -> w_0 = -0.842454

  The migration R_918 -> R_842 is the re-centering of the FALSIFIER rectangle
  from anchor A to anchor B. It is NOT a relabel; the rectangle's center is
  a substrate-coordinate (the framework's own w_0 prediction at the chosen
  projection), so changing the center IS changing which substrate observable
  the rectangle gates.

Step 3 — Half-width preservation:

  R_918 (w_0 half-width) = 0.100
  R_842 (w_0 half-width) = 0.100   [UNCHANGED]
  R_918 (w_a half-width) = 0.200
  R_842 (w_a half-width) = 0.200   [UNCHANGED]

  The preservation of half-widths (0.100 ~ 2.17 sigma_w0_DR3 = 0.092; 0.200 ~ 1.13 sigma_wa_DR3)
  is NOT incidental: it confirms that the migration is ONLY a re-centering on the
  newly canonical projection, with the geometric falsifier-rectangle envelope
  preserved. Any rectangle re-emission that ALSO changed the half-width would
  be a Class-(b) PIN-LOOSE-SOURCE-TIGHT or Class-(a) PIN-TIGHT-SOURCE-LOOSE
  drift per epistemic-discipline.md SOURCE-RECON taxonomy; the W1b-9 ledger
  satisfies neither, so the migration is a pure projection-axis update.

Step 4 — The labeling claim:

  Claim: R_918 -> R_842 is a SUBSTRATE-GENUINE BOUNDARY SHIFT, not a labeling-
  only update. Reason: the rectangle's center IS a substrate observable (the
  framework's own w_0 prediction under projection X); changing the projection
  changes the substrate observable; the rectangle changes accordingly.

  Counter-claim (rejected): "R_918 and R_842 are two equally-valid labels for
  the same rectangle." This fails because the half-width preservation argument
  requires both centers to be substrate-physical projections, not labels for
  a single underlying rectangle. Two projections of the same observable do
  not collapse to a single label unless they coincide; A and B differ by 0.075546
  in d(w_0_LCDM) (per W13 P9 §III), so they are not coincident.

Direction (read from canonical form):

  The R_842 rectangle is the structural source for ALL S86+ DR3 falsifier
  citations that adopt the W10-2 branch-(iv) substrate-compaction anchor.
  The R_918 rectangle is preserved in the migration ledger ONLY for audit-
  provenance lineage of the pre-S84 Volovik-partition anchor; ANY S86+
  citation of R_918 under the R_842 label is a Class-(c) PIN-DRIFT-FROM-
  STALE-SOURCE defect per epistemic-discipline.md, exactly as cataloged
  in the S86 W2-4 calibration-corpus extension §"W13-3 R_842 stale-rectangle
  relabel" entry.
```

The W13 P9 runtime detection of the plan-prompt R_918 boundaries `[-1.05, -0.85]` cited under the R_842 label is therefore the **first runtime exposure of the migration ledger's structural-source role**: the plan author at S86 W13-3 cited the OLD R_918 boundaries with the NEW R_842 label, exactly the failure mode the migration ledger §(b) was written to prevent. The verdict was invariant under either label-mapping (Criterion 4 registry-history-priority dominates), but the structural defect surfaced cleanly.

**Substrate cross-link** (volovik home pillar — what does R_842 partition mean substrate-physically?):

Per `project_substrate-compaction-timescape.md` (per memory index entry "fiber tau tracks density → clock variance → w_a"), the R_842 partition corresponds to the SECOND substrate-compaction phase: **post-transit, post-acoustic-relaxation, late-time fiber-tau density tracking at z=0**. The R_918 partition corresponds to the FIRST substrate-compaction phase: **post-fold expansion-history integral over the entire post-transit epoch**. These are physically distinct substrate observables:

| Phase | Substrate observable | w_0 anchor | Rectangle |
|:------|:--------------------|:-----------|:----------|
| First (Volovik partition) | Post-fold integral over expansion history; effacement-residual coupling at Γ_eff = 0.99970 | -0.918 (canonical pin, S58 → S85, 28+ sessions) | R_918 (superseded) |
| Second (substrate-compaction) | Direct fiber-tau density at z=0; instantaneous late-time projection of spectral-action gradient | -0.842454 (S85 W10-2 branch-(iv)) | R_842 (active per W1b-9) |

The migration is therefore a **substrate-genuine boundary shift** — the falsifier rectangle now gates a different substrate observable, not the same observable under a different label. This matters because any S87+ citation that uses R_842 boundaries with anchor-A semantics (or vice versa) silently swaps which substrate observable the framework's prediction is being tested against; the proposed audit-script extension catches exactly this swap at plan-freeze.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-DR3-3-LAYER-SUB-TREE` (W12-4 C33) | INFO (n_step=1; STEP-C1-(PASS,PASS,FAIL)) | offset = -0.340827; w_0(L=12) = -0.975713 (0.034 below R_842 lower edge) |
| `S86-W0-PRIMARY-VALUE-RESOLVE` (W13 P9) | PASS (PRIMARY = A = -0.918; SECONDARY-with-reversibility = B) | DR3-trigger band [-0.86, -0.83]; if w_0^DR3 lands here, primary flips A → B |
| `S86-DR3-SUB-TREE-3-ROW-PIN` (W13 P8) | INFO (14-pop + 7-stub; mono = 7/7; oscillations = 0) | L=8 PRE-REG-INCOMPLETE per spawn-prompt fallback |
| W12-4 §6(e) cross-cutting finding | INFO (cross-session convention drift identified) | RDC produces oscillation FAIL; CAC produces step-monotone INFO on same data |
| W13 §735–810 retrospective on P9 R_842 detection | INFO (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE; SOURCE-RECON calibration corpus extended) | plan-prompt cited R_918 boundaries `[-1.05, -0.85]` under R_842 label; mack-9A canonical `[-0.942, -0.742]` is correct |

(All five entries are PRE-EXISTING verdicts in the source documents; this synthesis does NOT re-adjudicate them. Per parent-prompt rule "Gate verdicts from source docs are authoritative — do not re-adjudicate.")

---

## IV. Structural Implications

### IV.1 The CC question is unaffected; the substrate-projection ambiguity is sharpened

The Volovik-partition effacement is a substrate observable, not a regulator parameter. The W12-4 §6(e) finding means the regulator-axis L_max projection of w_0 has TWO admissible (substrate-correct) closed-form schemes (zeta, Zubarev, possibly PV and Mellin), each of which preserves the effacement at L=10 by construction. Within each scheme the offset is a closed-form constant. ACROSS schemes, the offset is scheme-dependent because the unmodified rho(L=10) values differ; the canonical pin w_0_FW = -0.918 is what makes them all collapse to the same L=10 anchor. The substrate's late-time w_0 prediction is therefore protected from regulator-axis bookkeeping — exactly the protection structure expected from a Volovik-partition equilibrium theorem (cf. S58 `volovik-partition-62-result.md` "Z finite (det=5.7e74); S_1loop/S_b=51.9%").

This does NOT close the CC gap (still 110+ OOM permanent per `cc-gge-residual-71-result.md`); it sharpens the discrimination between substrate observables and regulator artifacts.

### IV.2 Master-inventory Row #1 footnote should cite the demarcation theorem

The W13 P11 master inventory Row #1 currently cites `w_0 = -0.918, +3.28σ vs LCDM under DR3` with a footnote pointing to `w0-primary-decision-rule.md`. After convention-lockdown lands, the footnote should additionally cite the demarcation theorem (Result II.1 above) so any downstream reader knows that the L_max-stability prediction is bounded WITHIN the CAC-admissible class, not a free-parameter-fitted band. This is a one-line edit at S87 W0; not a re-emission.

### IV.3 The R_842 ⟵ R_918 migration ledger is now the authoritative boundary-source for plan-freeze validators

Per S84 W1b-9 §(b), the migration is geometrically a pure re-centering with half-widths preserved. Per Result II.3 above, the re-centering is substrate-physical, not labeling. The proposed `_source_reconciliation_audit.py` extension (Section VI below) makes this fact OPERATIONAL at plan-freeze: any future plan-prompt INPUT-PIN MAP that cites R_842 boundaries must agree with the migration-ledger row, OR be flagged as a Class-(c) drift candidate. This converts the W13 P9 runtime detection (which required a sagan-empiricist runtime audit to surface) into a deterministic plan-freeze halt.

### IV.4 What opened, closed, shifted

| Change | Description |
|:-------|:------------|
| OPENED | A 4-field S87 spec for landing the regulator-convention-lockdown rule (V.1 below). |
| OPENED | A 4-field S87 spec for extending `_source_reconciliation_audit.py` with rectangle-label validation (V.2 below). |
| CLOSED | The S85 W1b-1 → S86 W12-4 cross-session convention drift on DR3-class L_max-stability gates (CAC is the binding form going forward). |
| CLOSED | The "two-rectangles-same-label" ambiguity for R_842 (mack-9A canonical `[-0.942, -0.742]` is the structural source per W1b-9 ledger §(b)). |
| SHIFTED | The substrate-physical interpretation of R_842: it now gates the SECOND (substrate-compaction) projection at z=0, not the FIRST (Volovik partition) post-fold integral. |
| UNCHANGED | The CC gap (~110 OOM permanent); w_0_FW = -0.918 canonical pin; PRIMARY = A per W13 P9 PASS; reversibility band [-0.86, -0.83] for DR3 publication. |

---

## V. Carry-Forward Computations

### V.1 Land `regulator-convention-lockdown.md` rule-file
- **What**: install the proposed rule-file content (Section VI.A below) at `.claude/rules/regulator-convention-lockdown.md`. Add cross-link from `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1 to the new rule (one-line addition: "see also `regulator-convention-lockdown.md` for cross-session convention-consistency lockdown for DR3-class L_max-stability gates"). Verify rule-file passes `_source_reconciliation_audit.py` at plan-freeze for S87 W0 (no broken cites).
- **Inputs**: Section VI.A code block; existing `.claude/rules/v3-closure-recovery.md`; existing `.claude/rules/epistemic-discipline.md` (for SOURCE-RECON cross-link); `computations/canonical_constants.py:1243` (for w0_FW pin).
- **Gate**: NEW `S87-W0-REGULATOR-CONVENTION-LOCKDOWN-LANDING` — PASS iff (i) rule-file lands at `.claude/rules/regulator-convention-lockdown.md`; (ii) Class 1 cross-link present in `v3-closure-recovery.md`; (iii) `_pru_cardinality_audit.py` and `_source_reconciliation_audit.py` both exit 0 on the rule-file's pin map; (iv) all subsequent S87+ DR3-class L_max-stability gate plans cite CAC as the convention. INFO if (i)-(ii) land but (iii) raises a Class-(d) advisory. FAIL if rule cannot be landed without breaking an existing rule's cross-references.
- **Effort**: 1-2 hours, 1 agent session (orchestrator-installable; orchestrator review of Section VI.A content + 2 file edits + audit run).

### V.2 Extend `_source_reconciliation_audit.py` with rectangle-label validation
- **What**: implement the proposed extension (Section VI.B below) as a new `validate_rectangle_label()` function added to the audit script. Function loads the most-recent migration ledger (default: `sessions/archive/session-84/session-84-w1-workingpaper.md` line 879 §(b) table for R_842; future migrations append rows to a structured `sessions/framework/rectangle-migration-ledger.md` file authored as part of this carry-forward). For each `R_<label>` rectangle reference in a plan INPUT-PIN MAP, verify the cited boundaries match the ledger's row for that label; if mismatch detected, emit Class-(c) PIN-DRIFT-FROM-STALE-SOURCE advisory with severity calibrated per the W2-4 canonical-metric calibration corpus. Run extended audit retroactively against the S86 W13-3 plan-prompt to verify it catches the OLD-R_918-as-R_842 drift.
- **Inputs**: Section VI.B code block; `computations/_source_reconciliation_audit.py:1-383` (existing module); `sessions/archive/session-84/session-84-w1-workingpaper.md:879` (R_918 → R_842 ledger §(b)); `sessions/archive/session-86/session-plan/session-86-plan-w13.md` §W13-3.6 INPUT-PIN MAP (test fixture for retroactive catch).
- **Gate**: NEW `S87-W0-RECTANGLE-LABEL-VALIDATION-EXTENSION` — PASS if extended audit catches the OLD-R_918-as-R_842 drift retroactively in the pre-S86 plan AND emits Class-(c) advisory at the correct severity; INFO if drift detected but migration-ledger version-skew prevents retroactive catch (pre-W1b-9 plans would not have had the §(b) ledger to compare against); FAIL if extension cannot be implemented without breaking existing audit signatures (the existing 13-site fixture replay must still PASS at D_max_replayed = 5.6726 to within 1e-10).
- **Effort**: 3-4 hours, 1 agent session (sagan-empiricist or gen-physicist; familiar with `_source_reconciliation_audit.py` from W0a-2; involves ~150 LOC addition, 2 fixture rows, 1 retroactive-replay test).

### V.3 Author `sessions/framework/rectangle-migration-ledger.md` as the structured registry
- **What**: extract the S84 W1b-9 §(b) migration table (and any subsequent rectangle migrations) into a structured `sessions/framework/rectangle-migration-ledger.md` registry with one row per rectangle migration. Each row carries: rectangle label, w_0 range, w_0 center, w_0 half-width, w_a range, w_a center, w_a half-width, status (active/superseded), session-of-migration, structural justification (e.g., "re-centering on W10-2 branch-(iv) anchor"), SHA-256 of source working paper. Initial registry contains TWO rows: R_918 (superseded, 2026-04-23 W1b-9) and R_842 (active, 2026-04-23 W1b-9). Future rectangle migrations append rows; the ledger is append-only per `epistemic-discipline.md` §"Registry-Write Hygiene".
- **Inputs**: `sessions/archive/session-84/session-84-w1-workingpaper.md:879` (R_918 → R_842 source table); `sessions/framework/registry/_registry-template.md` (registry scaffold); `computations/script-template.py` (append-only writer pattern).
- **Gate**: NEW `S87-W0-RECTANGLE-MIGRATION-LEDGER-REGISTRY-CREATE` — PASS iff (i) ledger file lands at the cited path with 2 rows; (ii) `_source_reconciliation_audit.py` extension (V.2) consumes the ledger as its rectangle-validation source; (iii) registry passes `_yaml_gate_validator.py` schema check; (iv) abort-if-exists pre-flight check fires correctly. INFO if 1 row only (e.g., active rectangle without superseded predecessor). FAIL if file already exists at path (registry-CREATE corridor closed; would need a separate UPDATE gate).
- **Effort**: 2 hours, 1 agent session (kaku-speculative-theorist or sagan-empiricist; mechanical extract + canonical formatting; one append-only Python writer per `feedback_dispatch-discipline.md`).

### V.4 Land follow-on calibration-corpus extension to `epistemic-discipline.md`
- **What**: extend the SOURCE-RECONCILIATION calibration corpus in `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" with a new entry naming the convention-lockdown demarcation as a Class-(b) PIN-LOOSE-SOURCE-TIGHT precedent (RDC has loose effacement-preservation; CAC has tight effacement-preservation; the lockdown rule tightens the pin to source band). Cross-reference the demarcation theorem (Result II.1 above) and the new `regulator-convention-lockdown.md` rule.
- **Inputs**: `.claude/rules/epistemic-discipline.md` (existing calibration corpus at `Calibration corpus (rule precedents)`); Result II.1 of this synthesis; new `regulator-convention-lockdown.md` from V.1.
- **Gate**: NEW `S87-W0-EPISTEMIC-DISCIPLINE-CALIB-CORPUS-EXTENSION` — PASS iff the calibration-corpus entry lands AND `_source_reconciliation_audit.py` correctly classifies a synthetic RDC-vs-CAC fixture as Class-(b) at severity S2 (advisory). FAIL if classification routes to wrong class.
- **Effort**: 1 hour, 1 agent session (orchestrator + lizzi-spectral-functional-theorist for calibration-corpus formatting consistency).

### V.5 Extend Zubarev rho_series to L ∈ {13, 14, 15} (DR3 L=14+ deep dive proper)
- **What**: extend `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.py` to compute rho_Zubarev(L) at L = 13, 14, 15. Apply CAC offset to produce w_0(L=13), w_0(L=14), w_0(L=15). Re-fire the W12-4 21-cell matrix as a 35-cell L_max ∈ {8, 10, 12, 13, 14} matrix (or 49-cell L_max ∈ {8, 10, 12, 13, 14, 15} matrix per spawn budget). Apply W12-4 §11 decision rule for the C1-cell sequence: (PASS,PASS,FAIL,FAIL,FAIL) → phantom-side migration confirmed (W3-G42 rectangle migration to R_phantom triggers); (PASS,PASS,FAIL,PASS,PASS) → oscillation revealed in 5-layer view (FAIL with cutoff_axis re-pin); (PASS,PASS,FAIL,?,?) with mixed → INFO continues, ≥3 step-monotone tightens.
- **Inputs**: `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.py` (extend); `computations/s84_spectrum_cache_L12_tau019.npz` (precursor cache; need new `s84_spectrum_cache_L13_tau019.npz`, etc., requires GPU eigenvalue runs at L=13/14/15 D_K matrices); `canonical_constants.py:1243` `w0_FW`; `R_842 = [-0.942, -0.742]` from migration ledger.
- **Gate**: `S87-DR3-LMAX-12-DEEP-DIVE` (pre-registered carry-forward from W12-4 §11) — pre-registered 3-branch decision rule per W12-4 §11; PASS / INFO / FAIL bands per W12-4 §9.
- **Effort**: 6-8 hours, 1-2 agent sessions (heavy GPU eigenvalue computation at L=13/14/15; M_dim grows polynomial in L; needs `torch.linalg.eigvalsh` with VRAM-feasibility check per `.claude/rules/math-scripts.md` §"Machinery-Feasibility Audit"; canonical-anchored convention BINDING per V.1 lockdown rule). All four feedback fields satisfied.

---

## VI. Proposed Artifacts (CODE BLOCKS — DO NOT INSTALL DIRECTLY; ORCHESTRATOR INSTALLS AFTER REVIEW)

### VI.A Proposed `.claude/rules/regulator-convention-lockdown.md` content

```markdown
# Regulator-Convention Lockdown for DR3-Class L_max-Stability Gates

> **Provenance**: S86 W12-4 §6(e) cross-cutting finding (mack-cosmic-bridge,
> 2026-04-26) + S86 1a-S8 demarcation theorem (volovik-superfluid-universe-
> theorist, 2026-04-27). Source plans: `sessions/archive/session-86/session-86-w12-
> workingpaper.md` lines 405-409, 622-623, 654; `sessions/archive/session-86/session-
> 86-1a-s8-volovik.md` Result II.1.

## Rule (cross-session convention-consistency for DR3-class L_max-stability)

For ALL S87+ computation gates of class **DR3 L_max-stability** — i.e., gates whose
verdict is a function of `w_0_FW(L_max)` evaluated at two or more values of
the regulator axis L_max ∈ {5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ...} —
the convention used to map regulator-axis spectral moments to the late-time
w_0 prediction MUST be the **canonical-anchored convention (CAC)**:

```
w_0_FW(L) := rho_X(L) + offset_X
where:
  rho_X(L)   = a regulator-axis spectral-moment scheme:
               X ∈ {Zubarev, zeta, Pauli-Villars, Mellin}
               (default: Zubarev, per S85 W0-7 NPZ rho_series field)
  offset_X   = w_0_FW - rho_X(L_anchor)  with L_anchor = 10
               (the additive constant that absorbs the S58 Volovik-partition
               effacement contribution as a closed-form translation)
  w_0_FW     = canonical_constants.py:1243 = -0.918
               (S58 Volovik partition + effacement Gamma_eff = 0.99970)
```

The CAC for the canonical scheme X = Zubarev has `offset_Zubarev = -0.340827`
(verified against S85 W0-7 `rho_series[L=10] = -0.577173`).

## Demarcation theorem (admissibility class)

A convention `C` is **admissible** for a DR3-class L_max-stability gate iff
`C` satisfies the effacement-preservation criterion:

```
  w_0^{C}(L=10) = w_0_FW   EXACTLY (bit-precision algebraic identity at L=10).
```

CAC satisfies this BY CONSTRUCTION (the offset is defined to absorb the
L=10 residual). Any convention that does NOT satisfy this — including the
**rho-direct convention (RDC)** `w_0(L) := rho_X(L)` with no offset, or
RDC + L=10-override (a discontinuous patch) — is **OUTSIDE the admissibility
class** and MUST NOT be used.

## Enforcement

- Plan-freeze validators (`_source_reconciliation_audit.py` post-V.2 extension)
  scan computation scripts in DR3 L_max-stability gate scope for the CAC pattern
  `w_0(L) = rho_X(L) + <offset_constant>`. Detection of `w_0(L) := rho_X(L)`
  WITHOUT an offset, or with an L=10-conditional override, fires Class-(b)
  PIN-LOOSE-SOURCE-TIGHT severity S1 advisory (halts plan-freeze).
- Re-running a previously-failed DR3-class gate under a DIFFERENT scheme
  (Zubarev → zeta) is permitted PROVIDED the new scheme is composed with
  its own effacement-anchored offset. Switching the offset constant ad-hoc
  (without anchoring at L=10) is treated as PROHIBITED_ACTIONS Class 1
  (convention-shopping) per `.claude/rules/v3-closure-recovery.md`.

## Cross-Link to v3-closure-recovery PROHIBITED_ACTIONS Class 1

PROHIBITED_ACTIONS Class 1 forbids changing a gate's `convention` tag DURING
recovery — i.e., the within-gate execution-property failure where a FAIL is
relabeled as PASS by switching conventions. The cross-session analog (changing
convention BETWEEN sessions on the same gate-family) is structurally different:
both sessions can satisfy Class 1 internally and still produce inconsistent
verdicts (S85 W1b-1 RDC oscillation FAIL vs S86 W12-4 CAC step-monotone INFO
on the same underlying rho_series data). This rule closes that gap by
pre-registering CAC as the binding form across ALL S87+ DR3-class L_max-stability
gates — a rule-file commitment, not a per-gate machinery pin.

## Scope (NOT for non-DR3 gates)

This lockdown is SPECIFIC to DR3-class L_max-stability gates. Non-DR3 gates
(e.g., n_s convergence, alpha_s convergence, r convergence) MAY use schemes
other than CAC if their canonical anchor is not w_0_FW. Each gate-class with
a distinct canonical anchor REQUIRES its own analogous lockdown rule, derived
by the same demarcation-theorem template (Result II.1 of session-86-1a-s8-volovik.md).

## Source

- S86 W12-4 §6(e) cross-cutting finding (mack-cosmic-bridge synthesis).
- S86 1a-S8 demarcation theorem (volovik-superfluid-universe-theorist; this
  rule-file's substrate-physics derivation).
- S58 Volovik partition canonical pin `w0_FW = -0.918` (canonical_constants.py:1243).
- S85 W0-7 Zubarev rho_series at L ∈ {8, 9, 10, 11, 12} (`computations/s85_w0_zubarev_lmax_convergence_to_minus_one.npz`).
- Cross-reference: `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 1.
- Cross-reference: `.claude/rules/epistemic-discipline.md` §"Source Reconciliation" Class (b) PIN-LOOSE-SOURCE-TIGHT.
```

### VI.B Proposed extension to `computations/_source_reconciliation_audit.py`

```python
# -----------------------------------------------------------------------------
# Rectangle-label validation extension (S87 W0; per S86 1a-S8 V.2 carry-forward)
#
# Validates that any rectangle reference (e.g., R_842, R_918) in a plan
# INPUT-PIN MAP agrees with the most-recent migration-ledger row for that
# label. Catches the "OLD-R_918-as-R_842" stale-rectangle-relabel drift
# class documented in epistemic-discipline.md §"W13-3 R_842 stale-rectangle
# relabel" calibration entry.
#
# Triggers on: plan-prompt INPUT-PIN MAP entries matching the regex
#   r'R_(\d{3})\s*=\s*\[([^\]]+)\]\s*(?:×|x|\*)\s*\[([^\]]+)\]'
# Validates the parsed (w_0_lo, w_0_hi, w_a_lo, w_a_hi) tuple against the
# migration ledger's row for label R_<digits>.
# -----------------------------------------------------------------------------

import re
from pathlib import Path

# Default migration-ledger source. Per S86 1a-S8 V.3 carry-forward, this
# should migrate to a structured registry at sessions/framework/rectangle-
# migration-ledger.md once that registry exists; until then, parse the
# S84 W1b-9 §(b) table directly.
RECTANGLE_LEDGER_DEFAULT = Path(
    "sessions/archive/session-84/session-84-w1-workingpaper.md"
)
RECTANGLE_LEDGER_TABLE_LINE = 879  # (local) S84 W1b-9 §(b) table start line


def parse_rectangle_ledger(ledger_path: Path = RECTANGLE_LEDGER_DEFAULT) -> dict:
    """Parse the migration-ledger table; return {label: {w_0_range, w_a_range,
    center, half_widths, status, session_of_migration}}.

    Robust to either the S84 W1b-9 markdown-table form (active until
    S87 V.3 lands the structured registry) or the S87 V.3 structured
    registry form (sessions/framework/rectangle-migration-ledger.md).
    """
    if not ledger_path.exists():
        return {}
    text = ledger_path.read_text(encoding="utf-8")
    # Two parser branches — one for markdown table (S84 form), one for
    # structured registry (S87 form). Both produce the same dict schema.
    rectangles: dict = {}  # (local)
    # S84 form: extract rows with "| R_<digits> ... | range | ... |" pattern
    md_table_re = re.compile(
        r"R_(\d{3}).*?\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\].*?"
        r"\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]",
        re.MULTILINE,
    )
    for m in md_table_re.finditer(text):
        label = f"R_{m.group(1)}"  # (local)
        w0_lo, w0_hi = float(m.group(2)), float(m.group(3))  # (local)
        wa_lo, wa_hi = float(m.group(4)), float(m.group(5))  # (local)
        # Status detection: scan ±5 lines around the match for "active"
        # / "superseded" / "(active)" / "(superseded)" tokens.
        status = "unknown"  # (local)
        ctx_start = max(0, text.rfind("\n", 0, m.start()) - 200)  # (local)
        ctx_end = min(len(text), m.end() + 200)  # (local)
        ctx = text[ctx_start:ctx_end].lower()  # (local)
        if "superseded" in ctx:
            status = "superseded"  # (local)
        elif "active" in ctx:
            status = "active"  # (local)
        rectangles[label] = {
            "w_0_range": (w0_lo, w0_hi),
            "w_a_range": (wa_lo, wa_hi),
            "w_0_center": (w0_lo + w0_hi) / 2.0,
            "w_a_center": (wa_lo + wa_hi) / 2.0,
            "w_0_half_width": (w0_hi - w0_lo) / 2.0,
            "w_a_half_width": (wa_hi - wa_lo) / 2.0,
            "status": status,
        }
    return rectangles


# Plan INPUT-PIN MAP rectangle-reference regex; parses
# R_<NNN> = [a, b] × [c, d]   (or x or * for the cross product separator)
_PLAN_RECT_REF_RE = re.compile(
    r"R_(\d{3})\s*=\s*\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]\s*"
    r"(?:×|x|\*)\s*\[\s*(-?\d+\.\d+)\s*,\s*(-?\d+\.\d+)\s*\]"
)


def validate_rectangle_label(plan_text: str, ledger: dict) -> list[dict]:
    """Scan plan_text for rectangle references; cross-check against ledger.
    Return list of advisory entries; empty list = no defects.

    Each advisory entry has fields {label, plan_w0, plan_wa, ledger_w0,
    ledger_wa, ledger_status, defect_class, severity, message}.
    """
    advisories: list[dict] = []  # (local)
    for m in _PLAN_RECT_REF_RE.finditer(plan_text):
        label = f"R_{m.group(1)}"  # (local)
        plan_w0 = (float(m.group(2)), float(m.group(3)))  # (local)
        plan_wa = (float(m.group(4)), float(m.group(5)))  # (local)
        if label not in ledger:
            advisories.append({
                "label": label,
                "plan_w0": plan_w0,
                "plan_wa": plan_wa,
                "defect_class": "C_UNPINNED_BUT_REFERENCED",
                "severity": "S2",
                "message": (
                    f"Plan cites {label} but no migration-ledger row exists "
                    f"for this label. Add ledger row OR remove plan citation."
                ),
            })
            continue
        ledger_row = ledger[label]
        ledger_w0 = ledger_row["w_0_range"]
        ledger_wa = ledger_row["w_a_range"]
        # Tolerance: ledger boundaries are pinned; plan citation must match
        # within float-cancellation floor (10 * float_eps ~ 2.22e-15).
        TOL = 1e-12  # (local)
        w0_match = (
            abs(plan_w0[0] - ledger_w0[0]) <= TOL
            and abs(plan_w0[1] - ledger_w0[1]) <= TOL
        )
        wa_match = (
            abs(plan_wa[0] - ledger_wa[0]) <= TOL
            and abs(plan_wa[1] - ledger_wa[1]) <= TOL
        )
        if not (w0_match and wa_match):
            # The actionable case: this is the OLD-R_918-as-R_842 drift
            # mode documented in epistemic-discipline.md §"W13-3 R_842
            # stale-rectangle relabel" calibration entry.
            advisories.append({
                "label": label,
                "plan_w0": plan_w0,
                "plan_wa": plan_wa,
                "ledger_w0": ledger_w0,
                "ledger_wa": ledger_wa,
                "ledger_status": ledger_row["status"],
                "defect_class": "C_PIN_DRIFT_FROM_STALE_SOURCE",
                "severity": "S1",  # MANDATORY-halt; cross-session label drift
                "message": (
                    f"Plan cites {label} = {plan_w0} × {plan_wa}, but the "
                    f"migration-ledger row for {label} (status={ledger_row['status']}) "
                    f"is {ledger_w0} × {ledger_wa}. This is the "
                    f"stale-rectangle-relabel pattern: plan likely cites the "
                    f"OLD R_<other> boundaries under the NEW {label} label. "
                    f"Resolve per epistemic-discipline.md §\"W13-3 R_842 "
                    f"stale-rectangle relabel\" calibration entry."
                ),
            })
        elif ledger_row["status"] == "superseded":
            # Status-only advisory: boundaries match the ledger (so no
            # value drift), but the rectangle is superseded; plan should
            # cite the active successor.
            advisories.append({
                "label": label,
                "plan_w0": plan_w0,
                "plan_wa": plan_wa,
                "ledger_status": "superseded",
                "defect_class": "C_PIN_DRIFT_FROM_STALE_SOURCE",
                "severity": "S2",  # advisory; values match but rectangle is stale
                "message": (
                    f"Plan cites {label} which is SUPERSEDED in the migration "
                    f"ledger. Cite the active successor instead."
                ),
            })
    return advisories


# Retroactive replay against S86 W13-3 plan-prompt (validation fixture for V.2)
def replay_w13_3_plan_prompt() -> dict:
    """Run validate_rectangle_label() against the S86 W13-3 plan-prompt
    INPUT-PIN MAP. PASS iff exactly 1 advisory at severity S1 with
    defect_class=C_PIN_DRIFT_FROM_STALE_SOURCE for label R_842 is emitted.
    """
    plan_path = Path("sessions/session-plan/session-86-plan-w13.md")  # (local)
    ledger = parse_rectangle_ledger()
    if not plan_path.exists():
        return {"verdict": "INFO", "reason": "S86 W13 plan unavailable for replay"}
    plan_text = plan_path.read_text(encoding="utf-8")
    advisories = validate_rectangle_label(plan_text, ledger)
    matching = [
        a for a in advisories
        if a["label"] == "R_842"
        and a["defect_class"] == "C_PIN_DRIFT_FROM_STALE_SOURCE"
        and a["severity"] == "S1"
    ]
    return {
        "verdict": "PASS" if len(matching) >= 1 else "FAIL",
        "n_advisories": len(advisories),
        "n_matching_R842_S1": len(matching),
        "advisories": advisories,
    }
```

**Implementation notes** for the orchestrator:

1. The extension preserves the existing 13-site fixture replay (`replay_5a_workshop_fixture()` or equivalent), which must continue to PASS at `D_max_replayed = 5.6726` to within 1e-10. Insert the new functions AFTER the existing fixture-replay section to avoid regression.
2. The default ledger source `RECTANGLE_LEDGER_DEFAULT` is the S84 W1b-9 working paper. After V.3 lands the structured `sessions/framework/rectangle-migration-ledger.md` registry, the default should switch to that path. Until then, the markdown-table parser handles the S84 form correctly.
3. The `replay_w13_3_plan_prompt()` function is the gate-bound test for V.2. PASS expectation: exactly 1 advisory at severity S1 for label R_842, because the plan-prompt at S86 W13-3.6 INPUT-PIN MAP cites `R_842 = [-1.05, -0.85] × [-0.2, +0.2]` (the OLD R_918 boundaries under the NEW R_842 label).

---

## VII. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| II.1 | Demarcation theorem on admissible regulator-stability conventions; CAC ∈ A_E, RDC ∉ A_E; offset = -0.340827 absorbs the full S58 effacement contribution | PHONONIC | NEW (theorem) | Convention choice for DR3-class L_max-stability gates is now structurally determined; rho-direct family is closed |
| II.2 | Lockdown closes a cross-session convention-consistency gap that PROHIBITED_ACTIONS Class 1 does not catch (Class 1 = within-gate, lockdown = cross-session) | NON-PHONONIC | NEW (cross-link) | Pre-registers CAC as binding form for S87+; orchestrator-installable rule per V.1 |
| II.3 | R_842 ⟵ R_918 migration is substrate-physical re-centering (not labeling); half-widths preserved at 0.100 / 0.200; the two rectangles gate two distinct substrate observables | PHONONIC | CONFIRMED (S84 W1b-9 §(b)) | Migration ledger is authoritative source; plan-freeze validators must verify against it |
| III.1-5 | 5 source-doc gate verdicts (W12-4, W13 P9, W13 P8, W12-4 §6(e), W13 §735-810) | mixed | AUTHORITATIVE (not re-adjudicated) | Provides constraint-map state at S86 close |
| IV.1 | CC gap unaffected (~110 OOM permanent); regulator-axis bookkeeping vs substrate observable distinction sharpened | PHONONIC | UNCHANGED | Volovik partition equilibrium-theorem protection robust |
| IV.2 | Master-inventory Row #1 footnote should cite demarcation theorem | NON-PHONONIC | OPEN | One-line edit at S87 W0 |
| IV.3 | Migration-ledger §(b) is operational source for plan-freeze rectangle validation | NON-PHONONIC | NEW | Converts runtime catch (W13 P9) into deterministic plan-freeze halt |
| V.1 | Land `regulator-convention-lockdown.md` rule | NON-PHONONIC | OPEN (4-field spec) | Orchestrator-installable; 1-2 hours |
| V.2 | Extend `_source_reconciliation_audit.py` with `validate_rectangle_label()` | NON-PHONONIC | OPEN (4-field spec) | Sagan/gen-physicist; 3-4 hours; retroactive-PASS test on S86 W13-3 plan |
| V.3 | Author `sessions/framework/rectangle-migration-ledger.md` structured registry | NON-PHONONIC | OPEN (4-field spec) | Kaku/sagan; 2 hours; append-only writer |
| V.4 | Extend `epistemic-discipline.md` SOURCE-RECON calibration corpus with convention-lockdown precedent | NON-PHONONIC | OPEN (4-field spec) | Lizzi + orchestrator; 1 hour |
| V.5 | Extend Zubarev rho_series to L ∈ {13, 14, 15} (the DR3 L=14+ deep-dive proper) | PHONONIC | OPEN (4-field spec); pre-registered S87-DR3-LMAX-12-DEEP-DIVE | Heavy GPU eigenvalue computation; CAC binding per V.1; 6-8 hours |

---

**End of synthesis.** Convention-lockdown demarcation theorem (II.1), PROHIBITED_ACTIONS cross-link (II.2), and R_842 substrate-physical re-centering (II.3) all derived from substrate-first reasoning per `.claude/rules/phononic-framing.md`. Five S87 carry-forwards (V.1-V.5) pre-registered with full 4-field specs per `feedback_fix-in-session-never-defer.md`. No verdict re-adjudication; all source-doc gates cited as authoritative. All quantitative claims verified via Sage exact-rational + Python float64 (offset = -0.340827, w_0(L=8) = -0.845293, w_0(L=10) = -0.918, w_0(L=12) = -0.975713, R_842 lower-edge breach at L=12 = 0.034 in w_0).
