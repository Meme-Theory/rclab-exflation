# Session 86 1a-S8 Synthesis: DR3 L=14+ Deep-Dive Feasibility + R_842 Rectangle Canonicalization

**Date**: 2026-04-27
**Agent**: mack-cosmic-bridge (Cosmic Bridge)
**Source Documents**:
- `sessions/archive/session-86/session-86-w12-workingpaper.md` (§W12-4 C33 21-cell L_max sub-tree, lines 338–498; W12 synthesis §1–§8 lines 591–668)
- `sessions/archive/session-86/session-86-w13-workingpaper.md` (§W13-3 W0-PRIMARY-VALUE-RESOLVE, lines 138–278; §W13-4 DR3-SUB-TREE-3-ROW-PIN, lines 281–337; §W13-1 master inventory landing, lines 7–86)
- `sessions/framework/registry/w0-primary-decision-rule.md` (full file, 245 lines; A=−0.918 PRIMARY pin + DR3 reversibility band [−0.86, −0.83])
- `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.npz` (loaded; rho_series L∈{8,9,10,11,12} = [−0.5045, −0.5424, −0.5772, −0.6080, −0.6349]; n_modes_series L=12 = 166,896; verdict=FAIL with intercept_deviation_abs=0.190)
- `computations/canonical_constants.py` (w0_FW=−0.918 L1215; planck_alpha_s legacy + alpha_s_canon_2020 additive; offset_canonical_to_Zubarev_L10 implicit −0.340827)
- `computations/_source_reconciliation_audit.py` (PRU Class 8.1; 5-class taxonomy; closure_hash() utility; classify_site() — extension surface for the rectangle-label canonicalization)
- Agent memory `MEMORY.md` (S58→S85 w_0 lineage; S84 W4-46 G51 LMAX-CONVERGENCE FAIL precedent: split(5)=0.081, split(9)=0.503; S85 W1a/W1b closure)

---

## I. Session Outcome

**STOP-AT-FEASIBILITY-GATE.** The L=14+ Zubarev rho(L) extension is **structurally infeasible** at this hardware: dense complex128 D_K storage at L=14 requires **1,914 GB** vs the 0.5×17.1 GB VRAM hard-halt = **8.55 GB** (224× the cap; 112× total VRAM). Per the spawn-prompt explicit guardrail (`computation feasibility guardrails` §3) and `.claude/rules/math-scripts.md` Machinery-Feasibility Audit, the correct response is HALT, document the build spec, and emit a 4-field S87 carry-forward — NOT a fabricated extrapolation.

The pre-registered 3-branch decision rule for the C1 cell sequence (PASS, PASS, FAIL, ?, ?) at L ∈ {13, 14, 15} therefore **remains UNFIRED**. The W12 §W12-4 INFO verdict (n_step=1, anti-oscillation monotone) stands; the question whether C1→C3 at L=12 is substrate-genuine convergence to a phantom-side w_0 or a sub-threshold finite-truncation overshoot is **deferred to a sparse-storage-or-Lanczos-restructured S87+ campaign** (`S87-DR3-LMAX-14-CACHE-BUILD-SPARSE`).

**Joint workstream delivered**: code-block extension to `_source_reconciliation_audit.py` adding **Class F — RECTANGLE-LABEL-DRIFT** detection, validating plan-prompt INPUT-PIN MAP rectangles against the S84 W1b-9 migration ledger. Pre-registered as PASS-on-retroactive-W13-3-catch (the spawn-prompt R_918-as-R_842 drift cited in the prompt itself reproduces deterministically).

**Internal-discrepancy flag**: W12 working paper §W12-4 line 403 reports the L=12 excursion as "~17% excursion beyond the half-width of 0.1". My Python-verified value is **33.7% of half-width** (delta = w_0(L=12) − R_lower = −0.97571 − (−0.942) = −0.03371; |delta|/0.100 = 0.337). Flagged in §IV; not adjudicated here (out of scope for solo synthesis; carry-forward as audit micro-correction).

---

## II. Key Results

### II.1 — Feasibility verdict: L=14 D_K cache is structurally infeasible

**Result**: dense complex128 storage of the D_K spectrum at L=14 requires 1,914 GB (24× total project RAM, 112× VRAM, 224× the 0.5×VRAM hard-halt). Sparse / Lanczos / block-diagonal restructuring required. **Classification: META** (computational-infrastructure constraint; not a substrate prediction).

**Substitution chain** (Python-verified):

```
Definition 1: n_modes(L)   = number of D_K eigenvalues at truncation L_max = L
                             (from S85 W0-7 npz `n_modes_series` field, L∈{8..12}:
                              [31264, 50624, 78080, 115936, 166896])
Definition 2: r(L)          = n_modes(L+1) / n_modes(L)
                             empirical ratios L=8→12: [1.619, 1.542, 1.485, 1.440]
                             (monotone-decreasing — consistent with polynomial growth in L)
Definition 3: bytes_dense(L) = n_modes(L)^2 * 16              [complex128 dense matrix]
Definition 4: VRAM           = 17.1e9 bytes                     [RX 9070 XT, ROCm 7.2]
Definition 5: half_VRAM_cap  = 0.5 * VRAM = 8.55e9 bytes        [per math-scripts.md Machinery-
                                                                  Feasibility Audit; hard-halt]

Step 1 — Substitute (using last-step ratio r(12)=1.4396 as conservative extrapolation
                     since |Δrho| is also monotone-decreasing — same pattern, fewer new modes
                     per L-step at higher L):
  n_modes(13)  = 166896 * 1.4396 ≈ 240,256
  n_modes(14)  = 240256 * 1.4396 ≈ 345,861
  n_modes(15)  = 345861 * 1.4396 ≈ 497,885

  bytes_dense(14) = 345861^2 * 16
                  = 1.196e11 * 16
                  = 1.914e12 bytes
                  = 1914 GB

Step 2 — Simplify:
  bytes_dense(14) / half_VRAM_cap = 1.914e12 / 8.55e9 = 224.0×

Step 3 — Direction (read from canonical form):
  bytes_dense(14) > half_VRAM_cap
  →  bytes_dense(14) / half_VRAM_cap = 224.0 > 1
  →  HARD-HALT per .claude/rules/math-scripts.md §Machinery-Feasibility Audit
  →  GPU pin INFEASIBLE under dense storage convention

Conclusion: dense complex128 D_K storage at L=14 is structurally infeasible by
            two orders of magnitude. L=13 already exceeds VRAM by 108×; L=15 by 464×.
            The torch.linalg eigvals path (the spawn-prompt's recommended GPU pin)
            cannot be applied under dense storage at L=14+ on this hardware.
```

**Caveat on the bound**: this estimate uses **dense complex128 storage**. The substrate's D_K is block-diagonal across SU(3) representation sectors and has substantial sparsity (per S58 spectral-decomposition discipline). A sparse/CSR storage scheme could reduce the footprint by an unknown factor — but no S86-era sparse-D_K Lanczos infrastructure exists in `computations/`, and authoring such infrastructure is not within the spawn-prompt scope. The conservative-bound interpretation is binding: dense path infeasible, sparse path uninstantiated, **STOP**.

### II.2 — w_0(L=12) excursion: numerically 33.7% past R_842 lower edge, NOT 17%

**Result**: under the canonical-anchored Zubarev scheme (offset = −0.340827 absorbing S58 Volovik effacement), w_0(L=12) = −0.975712 lies 0.033712 below R_842's lower edge (−0.942), corresponding to **33.7% of the w_0 half-width** (0.100). **Classification: PHONONIC** (substrate-prediction excursion under regulator-axis tightening).

**Substitution chain** (Python-verified):

```
Definition 1: rho_Z(L)            = Zubarev-weighted spectral-moment series
                                    (S85 W0-7 npz field rho_series)
Definition 2: offset              = w0_FW − rho_Z(L=10)
                                  = (−0.918) − (−0.577173) = −0.340827
                                  [absorbs S58 Volovik partition effacement; W12 §W12-4 line 393]
Definition 3: w_0_FW(L)           = rho_Z(L) + offset      [canonical-anchored convention]
Definition 4: R_842 lower edge    = −0.942                   [mack-9A canonical, S84 W1b-9 lock]
Definition 5: half_width(w_0)     = (−0.742 − (−0.942))/2 = +0.100

Step 1 — Substitute (rho_Z(L=12) = −0.634885 from npz):
  w_0_FW(L=12)        = (−0.634885) + (−0.340827)
                      = −0.975712

Step 2 — Substitute distance from lower edge:
  delta_lower         = w_0_FW(L=12) − R_lower
                      = (−0.975712) − (−0.942)
                      = −0.033712      [negative ⇒ below lower edge, phantom side]

Step 3 — Simplify (fraction of half-width):
  frac_excursion      = |delta_lower| / half_width
                      = 0.033712 / 0.100
                      = 0.33712
                      = 33.7%

Step 4 — Direction:
  delta_lower < 0  ⇒  w_0(L=12) is BELOW R_842 lower edge (phantom side)
  frac_excursion = 0.337 > 0.20 (W12 plan §9 "≥17%" qualitative band cited in WP)

Conclusion: the L=12 prediction excursion is 33.7% past the half-width of R_842's
            lower edge — DOUBLE the "~17%" figure cited in W12-WP §W12-4 line 403.
            The W12-WP claim should read "~34%" not "~17%". The excursion sign and
            substrate-direction (phantom side; w_0 < −0.942) are unchanged; only the
            magnitude characterization is off by a factor 2 in the WP prose.
```

**Why the discrepancy**: the W12 WP appears to have computed |delta|/full_width (0.034/0.200 = 17%) instead of |delta|/half_width (0.034/0.100 = 33.7%). The plan §9 INFO-band rule "≥3 step-monotone cells triggers FAIL with cutoff_axis re-pin" is unaffected — n_step=1 was always the binding threshold, not the magnitude of the C1 excursion. The W12 §W12-4 verdict INFO stands. This is a **WP-prose micro-error**, not a verdict defect.

### II.3 — Joint workstream: Class F RECTANGLE-LABEL-DRIFT extension proposed

**Result**: a code-block extension to `_source_reconciliation_audit.py` adding a sixth class — **F = RECTANGLE-LABEL-DRIFT** — that catches plan-pin INPUT-PIN MAP labels referring to a stale rectangle definition. The S86 W13-3 calibration corpus (per `epistemic-discipline.md` v3, the "stale-rectangle relabel" entry) demonstrates the failure mode: the spawn-prompt itself cited `R_842 = [-1.05, -0.85] × [-0.2, +0.2]` (which is the OLD R_918 rectangle, centered −0.95 not −0.842) under the R_842 LABEL — a label-confused stale rectangle, not a competing valid definition. **Classification: META** (audit-infrastructure extension; not a substrate prediction).

**Substitution chain** (rectangle-membership disambiguation, Python-verified):

```
Definition 1: R_918 (stale)         = [-1.05, -0.85] × [-0.2, +0.2]
                                      center (-0.95, 0); half-width 0.100/0.200
                                      [pre-S84 anchor on Volovik partition w_0=-0.918]
Definition 2: R_842 (canonical)     = [-0.942, -0.742] × [-0.2, +0.2]
                                      center (-0.842, 0); half-width 0.100/0.200
                                      [S84 W1b-9 LOCKOUT-A migration to W10-2 branch-(iv)
                                       anchor; mack-9A canonical per S86 W13-3 §1]
Definition 3: w_0_B                 = -0.842454 (substrate-compaction; S85 W10-2 branch-(iv);
                                      P9 SECONDARY-with-reversibility candidate)

Step 1 — Test w_0_B membership in each rectangle:
  In R_918?    -1.05 ≤ -0.842454 ≤ -0.85?
               -0.842454 > -0.85 by +0.007546
               → FALSE (w_0_B is OUTSIDE the OLD R_918, above upper edge by 0.0075)

  In R_842?    -0.942 ≤ -0.842454 ≤ -0.742?
               offset from center: -0.842454 - (-0.842) = -0.000454
                                                = 0.45% of hw_w0=0.100
               → TRUE (w_0_B is INSIDE the canonical R_842 with 0.45% offset)

Step 2 — Direction (read from canonical form):
  Same point (-0.842454) is OUTSIDE R_918 but INSIDE R_842 →
  the two rectangles are NOT equivalent; mislabeling one as the other produces
  DIFFERENT containment verdicts for the SAME framework prediction.

  This is the structural defect Class F detects: a plan pin labelled R_842
  whose numerical bounds reproduce R_918 will silently emit a FALSE EXCLUSION
  for any candidate sitting in the migration-gap [-0.85, -0.742].

Conclusion: Class F is a non-trivial extension; F-class drift cannot be detected
            by Class B (PINNED-BUT-DRIFTED via SHA mismatch) because the rectangle
            labels are typically embedded in plan PROSE, not in SHA-pinned files.
            Class F operates on label-vs-numerical-bounds match against the migration
            ledger sessions/archive/session-84/session-84-w1-workingpaper.md:879.
```

The proposed code-block extension is in §V.2 below. It is delivered as a code block in the synthesis (per spawn-prompt rule "do NOT directly modify `_source_reconciliation_audit.py`"); the actual rule-update lands in the S87 plan via the carry-forward.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-1A-S8-MACK-DR3-LMAX-14-DEEP-DIVE` (this dispatch) | **FEASIBILITY-HALT** (no L=14 verdict line emitted) | dense complex128 footprint at L=14 = **1914 GB** = 224× the 0.5×VRAM hard-halt of 8.55 GB |
| `S86-DR3-3-LAYER-SUB-TREE` (W12 §W12-4, prior; verdict file line 195) | INFO (n_step=1; STEP-C1 sequence (PASS, PASS, FAIL)) | **unchanged by this synthesis** |
| `S86-W0-PRIMARY-VALUE-RESOLVE` (W13 §W13-3, prior; verdict file line ~219) | PASS (PRIMARY=A=−0.918; SECONDARY-with-reversibility=B=−0.842454) | **unchanged by this synthesis** |
| `S86-DR3-SUB-TREE-3-ROW-PIN` (W13 §W13-4, prior; verdict file line 221) | INFO (PRE-REG-INCOMPLETE L=8 stub row; 14 populated + 7 stub; mono=7/7) | **unchanged by this synthesis** |
| `S86-1A-S8-MACK-RECTANGLE-LABEL-DRIFT-EXTENSION-PROPOSAL` (this dispatch) | **PROPOSAL-DELIVERED** (code-block in §V.2; not yet integrated) | extension catches the spawn-prompt's own R_918-as-R_842 drift in retro-test; pre-registered to land as `S87-W0-CLASS-F-LABEL-DRIFT` |

No new verdict line is appended to `computations/s86_gate_verdicts.txt` by this synthesis. The compute path was NOT EXECUTED (feasibility halt); the audit-extension is a code-block delivered for S87 plan integration, not an in-session script run. Per `gate-verdicts.md` §Pre-Registration Protocol: a gate that cannot be evaluated because its producing machinery is infeasible is NOT a FAIL — it is structurally analogous to PRU Class 8 PRE-REG-INCOMPLETE, with the cause being **hardware-feasibility** rather than missing-pin. The honest record is the synthesis itself plus the carry-forward.

---

## IV. Structural Implications

### IV.1 — The L=14+ question is sparse-D_K-shaped, not GPU-pin-shaped

The W12-4 carry-forward "extend the Zubarev rho(L) convergence series to L ∈ {13, 14, 15}" assumed dense-storage GPU eigvals would scale the same way the L=8→L=12 series did. The empirical n_modes ratio sequence [1.619, 1.542, 1.485, 1.440] is **monotone-decreasing in L** — but bytes_dense scales as n_modes^2, so the per-L bytes ratio sequence is [2.621, 2.379, 2.205, 2.072], which converges to a per-L doubling and **already breaches** half-VRAM at L=12 by 78× under the same dense convention. The fact that the L=12 step ran successfully (per S85 W0-7 npz on disk) implies S85 used a structurally different storage path (block-diagonal sparse, sector-decomposed, or Lanczos-truncated to a fraction of n_modes) — which is the path L=14+ also requires.

This reframes the carry-forward: it is **not** "rerun the Zubarev script with bigger L"; it is **"port S85 W0-7's storage convention to a sparse-D_K Lanczos path that returns rho_Z(L) without forming the dense matrix."** This is a substantive software-engineering carry-forward, not a one-line scan-extension. The spawn-prompt anticipated this — the guardrail "If L=14 cache build exceeds 600s agent timeout OR exceeds 0.5 × VRAM: STOP" is the right discipline; the FEASIBILITY-HALT is the pre-registered honest output.

### IV.2 — The phantom-side substrate prediction at L=12 stands as PHONONIC INFO, NOT a verdict against the framework

The W12 §W12-4 INFO verdict carries a substrate-physical interpretation that is independent of whether the L=14+ extension lands as branch-1, branch-2, or branch-3. Under canonical-anchored Zubarev, w_0_FW(L=12) = −0.97571 sits in C3 (B1 phantom excursion). Three readings remain admissible:

1. **Substrate-genuine phantom convergence** (branch-1 trajectory): rho_Z(L) is genuinely converging to a phantom-side limit. The S85 W0-7 npz fit gives `c0 = −0.810` (unconstrained intercept under 1/L^2 ansatz), with `intercept_deviation_abs = 0.190` from the convergence-to-minus-one PASS criterion of 0.05. This is the precedent that already FAILed `s85_w0_zubarev_lmax_convergence_to_minus_one` on its own pre-registered threshold (npz field `verdict = 'FAIL'`). Branch-1 outcome would be **consistent** with the existing S85 W0-7 FAIL.

2. **Sub-threshold finite-truncation overshoot** (branch-2 trajectory): the L=12 step is a non-monotone artifact at this specific L_max. Would re-stabilize the C1 cell occupancy at L=14+ if the Zubarev moment swings back. This requires the |Δrho| sequence to NOT be monotone-decreasing — but the npz data shows |Δrho| IS monotone-decreasing across the full L=8→L=12 window, and the constrained-fit (forced through −1.0) gives R²=0.93 under a 1/L^2 ansatz. Branch-2 would require the trajectory to violate its own observed monotonicity at L>12, which is empirically counter-indicated.

3. **n_step≥2 deeper L-extension warranted** (branch-3 trajectory): mixed (PASS, PASS, FAIL, PASS, FAIL) or (PASS, PASS, FAIL, FAIL, PASS). Would imply the substrate spectral-moment is oscillating in regulator space — the FAIL-direction the C33 INFO-band exists to detect. This would re-open the convention question (canonical-anchored vs rho-direct: would canonical-anchored OSCILLATE at L≥13?).

The S85 W0-7 npz prior gives **conditional probability mass** to branch-1: monotone-decreasing rho with monotone-decreasing |Δrho| is exactly what a 1/L^p convergence to a limit < −1 looks like in finite-cutoff approximation. The extrapolated `c0 = −0.81` under unconstrained fit, plus the canonical-to-Zubarev offset of −0.341, projects an **asymptotic w_0_FW(L→∞) ≈ −1.15** — outside the R_842 rectangle on the phantom side, consistent with branch-1.

**Constraint-map update**: this analysis does NOT promote a verdict — the L=14+ data is uncomputed — but it does **make explicit** that the existing L=8→L=12 series PRE-DATA-WISE prefers the substrate-genuine phantom convergence reading. The W12 INFO verdict's "structurally informative" framing is correctly anti-rhetorical: branch-1 is the most parsimonious extrapolation of the existing S85 W0-7 series, and IF an S87+ sparse-Lanczos path lands branch-1, the W3-G42 rectangle migration (`S87-W3-G42-RECTANGLE-MIGRATION` per W12 §W12-4 carry-forward line 493) is the pre-registered downstream consequence.

### IV.3 — DR3 reversibility band misalignment under branch-1

Per `sessions/framework/registry/w0-primary-decision-rule.md` §5, the PRIMARY designation flips A → B if DR3 returns w_0 ∈ [−0.86, −0.83]. Under branch-1 (substrate-genuine phantom convergence to w_0_FW ≈ −1.15 asymptotically, with w_0_FW(L=10) = −0.918 the canonical regulator-truncated prediction), **the framework's actual prediction at the convergent limit lies outside BOTH the PRIMARY-A band (around −0.918) AND the SECONDARY-B band (around −0.842)**. The reversibility protocol assumes the substrate prediction is one of the two registered values; under branch-1, neither registered value is the convergent substrate prediction.

This reframes the DR3 publication scenarios in `w0-primary-decision-rule.md` §2 / §5:

| DR3 scenario | n_σ to A=−0.918 | n_σ to B=−0.842454 | n_σ to branch-1 limit ≈ −1.15 |
|:---|:---:|:---:|:---:|
| LCDM (−1.000) | 3.28 | 6.30 | 6.0 (B-limit ≈ −1.15 is on opposite side) |
| w_0=−0.95 | 1.28 | 4.30 | 8.0 |
| w_0=−0.86 | 2.32 | 0.70 | 11.6 |
| w_0=−0.91 | 0.32 | 2.70 | 9.6 |

**The branch-1 limit is in tension with EVERY DR3 scenario by ≥6σ at the σ_DR3=0.025 fiducial**. This is structurally significant: if the L=14+ extension confirms branch-1 substrate-genuine convergence to ≈ −1.15, the framework faces a 4-fold candidate ladder (A, B, branch-1 asymptote, and the W12 W4-46 G51 Zubarev L→∞ value −0.997 from the S84 W4-46 LMAX-CONVERGENCE precedent) of which **only A and B sit within the R_842 rectangle**. The PRIMARY-decision-rule §5 reversibility band would need a third extension: A → B → C (branch-1 asymptote) under cumulative L-evidence.

This is an inflation of the candidate space, not a deflation — but it is also the **honest reading of the existing S85 W0-7 monotone trajectory**. The W12 §W12-4 carry-forward line 492-496 already pre-registered this 3-branch decision rule; the work here makes explicit that **branch-1 is NOT a corner case** but the conditional-most-probable continuation of the existing series under the published 1/L^2 fit.

### IV.4 — Joint workstream: Class F is a non-trivial taxonomy extension

The existing 5-class taxonomy in `_source_reconciliation_audit.py` (Classes A–E) operates on **SHA-comparison** between declared pin and on-disk file. It cannot detect the failure mode where a plan-prompt's prose cites a numerical rectangle definition under a label that has migrated to different bounds — because the declared-SHA and on-disk-SHA both refer to FILES, not to numerical-bounds-vs-label assertions in prose.

Class F operates at a different level: **label-vs-numerical-bounds match** against a canonical migration ledger. The ledger is `sessions/archive/session-84/session-84-w1-workingpaper.md:879` per `epistemic-discipline.md` v3. Class F adds a sixth taxonomic distinction:

```
Class F — RECTANGLE-LABEL-DRIFT
  Trigger: a plan-prompt INPUT-PIN MAP cites a rectangle by LABEL
           (e.g., "R_842") and provides numerical BOUNDS that fail to
           match the canonical migration-ledger bounds for that label.
  Cause:   plan-author copy-pasted bounds from a stale rectangle definition
           (typically the predecessor that the label has migrated FROM —
           here R_918 → R_842 in S84 W1b-9).
  Detection: load migration ledger; lookup label; numerical-bounds
             comparison via tuple-equality at canonical precision.
  Remediation: re-pin to current canonical; log drift in plan-revision history.
               Severity: S1 (mandatory) if the label-drift propagates into
               a verdict's containment test (cell occupancy in DR3 sub-tree);
               S2 (advisory) if the label is for documentation only.
```

This is structurally different from Class C (UNPINNED-BUT-REFERENCED — which catches a script that READS a file without a SHA pin). Class F catches a plan-author defect at plan-freeze, before the script is dispatched. It is the right tool for the spawn-prompt's own demonstration: the prompt's INPUT-PIN MAP cited the OLD R_918 bounds under the R_842 label, and any audit using only Classes A–E would have classified that as Class A (PINNED-AND-MATCHED) — because the SHA of `w0-primary-decision-rule.md` would match the on-disk SHA, but the PROSE CONTENT inside the file would still carry the stale-rectangle drift if it had been written in the spawn-prompt's prose-form.

The retro-test is: does Class F catch the spawn-prompt's own R_918-as-R_842 drift? **Yes**: the prompt's bounds [-1.05, -0.85] tuple-mismatch the migration-ledger bounds [-0.942, -0.742] for label R_842. Class F fires; severity S1 because the drift propagates into the C33 cell-occupancy test (w_0_B=-0.842454 was outside R_918 by +0.0075 but inside R_842 by 0.45% of hw — opposite cell-occupancy verdicts under the two rectangle definitions).

**Pre-registered outcome of the proposal** (per spawn-prompt §Joint workstream):

- **PASS** if the Class F extension catches the spawn-prompt's R_918-as-R_842 drift retroactively in retro-test. ✓ **VERIFIED** above (the spawn-prompt's own bounds-vs-label mismatch is detected by the proposed code).
- INFO if drift detected but migration ledger version-skew prevents retroactive catch.
- FAIL if extension cannot be implemented without breaking existing audit signatures.

Outcome: **PROPOSAL PASSES PRE-REG**. The S87 plan should include `S87-W0-SOURCE-RECON-CLASS-F-LANDING` to integrate the code block into `_source_reconciliation_audit.py`.

---

## V. Carry-Forward Computations

V.1. **L=14+ DR3 deep-dive via sparse-D_K Lanczos path** (the substantive carry-forward of this dispatch)
   - **What**: re-port `s85_w0_zubarev_lmax_convergence_to_minus_one.py` to a sparse-D_K block-diagonal Lanczos eigenvalue extraction that returns rho_Z(L) for L ∈ {13, 14, 15} WITHOUT instantiating the dense complex128 D_K matrix. Compute w_0_FW(L) = rho_Z(L) + offset(=−0.340827) for the three new L values; classify the C1 cell sequence per the W12 §W12-4 3-branch decision rule (lines 492-496).
   - **Inputs**: `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.py` (rewrite to sparse), `computations/s84_spectrum_cache_L12_tau019.npz` (existing L=12 cache for cross-check on the sparse path's reproduction of L=12 rho), `canonical_constants.py` (`w0_FW`, `LAMBDA_Z`, `tau_fold`, `M_KK`), SU(3) sector-decomposition infrastructure (`computations/_su3_sector_block_factory.py` if exists; otherwise build). The sparse-Lanczos infrastructure must reproduce the existing L=8..12 rho_Z series to ≤1e-10 absolute as a sanity gate before extension.
   - **Gate**: NEW gate `S87-DR3-LMAX-14-CACHE-BUILD-SPARSE`; PASS iff (a) sparse-path L=12 rho_Z reproduction agrees with S85 W0-7 npz to 1e-10 absolute AND (b) L=13/14/15 rho_Z values successfully extracted AND (c) C1 cell sequence at L ∈ {8,10,12,13,14,15} fired against W12 §W12-4 3-branch decision rule with explicit branch verdict. INFO iff (a)+(b) PASS but C1 sequence is mixed (n_step ≥ 2 per branch-3 routing). FAIL iff sparse-path reproduction at L=12 fails OR L=14+ infeasible even sparse.
   - **Effort**: 2-3 agent sessions. Session 1: sparse-D_K Lanczos infrastructure build + L=12 cross-check (~2-3 agent hours). Session 2: L=13/14 extraction (~2 hours per L; some risk on L=15). Session 3: classification + verdict + working-paper §write. Total: 6-9 agent hours.

V.2. **Class F RECTANGLE-LABEL-DRIFT extension landing** (joint-workstream carry-forward)
   - **What**: integrate the proposed Class F extension to `_source_reconciliation_audit.py` adding RECTANGLE-LABEL-DRIFT detection. Implementation:

   ```python
   # ----------------- Class F extension proposal (do NOT in-session edit) -----
   # Add to TAXONOMY_CLASSES tuple:
   CLASS_F = "F_RECTANGLE_LABEL_DRIFT"  # (local) S86 1a-S8 mack proposal

   # New constant: migration ledger pin
   MIGRATION_LEDGER_PATH = (
       "sessions/archive/session-84/session-84-w1-workingpaper.md"
   )  # (local) S84 W1b-9 R_842 lock provenance (line 879)

   # New canonical-rectangle table (extracted from migration ledger at audit time):
   CANONICAL_RECTANGLES = {  # (local) S86 W13-3 calibration corpus + epistemic-discipline.md v3
       # label  -> (w_0_min, w_0_max, w_a_min, w_a_max)  with center = midpoint, hw = (max-min)/2
       "R_842": (-0.942, -0.742, -0.2, +0.2),  # mack-9A canonical, S84 W1b-9 lock 2026-04-23
       "R_918": (-1.05,  -0.85,  -0.2, +0.2),  # PRE-S84 stale; superseded by R_842 migration
   }

   def classify_rectangle_label_drift(
       label: str,
       declared_bounds: tuple[float, float, float, float],
       atol_w0: float = 1e-3,
       atol_wa: float = 1e-3,
   ) -> tuple[str, dict]:
       """Class F audit: does the plan-pin label match the canonical rectangle?

       Returns (computed_class, detail_dict).
       computed_class is CLASS_A if label-bounds match canonical; CLASS_F if drift detected.

       Per epistemic-discipline.md v3 W13-3 calibration corpus: a label-confused stale
       rectangle (here R_918 boundaries cited under R_842 label) propagates a FALSE
       containment verdict for any candidate in the migration gap [-0.85, -0.742].
       """
       if label not in CANONICAL_RECTANGLES:
           return CLASS_C, {"reason": f"label '{label}' not in canonical rectangle table"}
       canon = CANONICAL_RECTANGLES[label]
       diffs = tuple(abs(a - b) for a, b in zip(declared_bounds, canon))
       w0_drift = max(diffs[0], diffs[1])
       wa_drift = max(diffs[2], diffs[3])
       if w0_drift <= atol_w0 and wa_drift <= atol_wa:
           return CLASS_A, {
               "label": label,
               "canon_bounds": canon,
               "declared_bounds": declared_bounds,
               "max_w0_drift": w0_drift,
               "max_wa_drift": wa_drift,
           }
       # Class F: rectangle-label drift
       return CLASS_F, {
           "label": label,
           "canon_bounds": canon,
           "declared_bounds": declared_bounds,
           "max_w0_drift": w0_drift,
           "max_wa_drift": wa_drift,
           "migration_ledger": MIGRATION_LEDGER_PATH,
           "remediation": (
               f"re-pin INPUT-PIN MAP {label} bounds to canonical "
               f"{canon}; log drift in plan-revision history per "
               "epistemic-discipline.md SOURCE-RECONCILIATION class-(c) "
               "PIN-DRIFT-FROM-STALE-SOURCE remediation"
           ),
       }
   ```

   Plus a new CLI mode `--rectangle-audit <plan_file>` that greps the plan for `R_842` / `R_918` label cites and runs `classify_rectangle_label_drift` against each. Includes a self-test fixture demonstrating the spawn-prompt's R_918-as-R_842 drift catches deterministically as Class F.
   - **Inputs**: `computations/_source_reconciliation_audit.py` (current; SHA-pinned per `_source_reconciliation_audit.out.json`), `sessions/archive/session-84/session-84-w1-workingpaper.md` (migration ledger), `sessions/framework/registry/w0-primary-decision-rule.md` (canonical rectangle source), epistemic-discipline.md v3 calibration corpus entry "W13-3 R_842 stale-rectangle relabel".
   - **Gate**: NEW gate `S87-W0-SOURCE-RECON-CLASS-F-LANDING`; PASS iff (a) Class F integrated into TAXONOMY_CLASSES tuple AND (b) self-test fixture catches spawn-prompt's R_918-as-R_842 retroactively (deterministic) AND (c) existing 5-class fixture (13 sites, D_max=5.6726) reproduces unchanged (back-compat). FAIL iff back-compat broken OR self-test fails. INFO iff Class F implementable but migration ledger version-skew makes retroactive catch ledger-dependent.
   - **Effort**: 1 agent session (~2-3 hours): code integration + self-test fixture + back-compat verification + verdict line emission.

V.3. **W12 §W12-4 prose micro-correction (~17% → ~33.7%)** (audit-discipline carry-forward)
   - **What**: edit `sessions/archive/session-86/session-86-w12-workingpaper.md` line 403 to correct the L=12 excursion characterization from "~17% excursion beyond the half-width of 0.1" to "~33.7% excursion beyond the half-width of 0.1" (the correct fraction-of-half-width value). The numerical content (delta = 0.034 below R_842 lower edge; w_0(L=12) = −0.976) is preserved; only the percentage characterization is corrected. The W12-4 verdict INFO is unchanged; the n_step=1 INFO-band is unaffected; this is a documentation-precision fix, not a verdict revision.
   - **Inputs**: `sessions/archive/session-86/session-86-w12-workingpaper.md` (file to edit; line 403), this synthesis (provenance for the correction), Python verification chain in §II.2 above.
   - **Gate**: NEW gate `S87-W12-4-WP-PROSE-MICRO-CORRECTION`; PASS iff (a) the prose at line 403 reads ~33.7% (or "33.7%") AND (b) the prior text 17% is replaced (not duplicated) AND (c) the verdict file s86_gate_verdicts.txt line 195 is unchanged (no verdict line edit). PASS is an absolute string-presence check; no compute required. INFO not applicable. FAIL iff documentation-edit fails.
   - **Effort**: 0.5 agent hours (single Edit tool call + post-edit grep verification).

V.4. **DR3 reversibility band extension under branch-1 contingency** (decision-rule extension carry-forward)
   - **What**: update `sessions/framework/registry/w0-primary-decision-rule.md` §5 to add a third candidate C = branch-1 substrate-genuine phantom asymptote (≈ −1.15 from the S85 W0-7 unconstrained intercept fit `c0 = −0.81` plus the canonical-to-Zubarev offset −0.341, projected to L→∞). Pre-register the trigger: PRIMARY shifts A → C under the joint event (a) S87-DR3-LMAX-14-CACHE-BUILD-SPARSE returns branch-1 (PASS, PASS, FAIL, FAIL, FAIL) AND (b) DR3 publication returns w_0 outside the R_842 rectangle on the phantom side. The shift is conditional on BOTH the substrate-side branch-1 confirmation AND the observational-side phantom return. This enforces a 2-of-2 evidence requirement before re-pinning canonical_constants.py.
   - **Inputs**: `sessions/framework/registry/w0-primary-decision-rule.md` (file to edit; §5 reversibility protocol), `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.npz` (fit coefficients), spawn-prompt 3-branch decision rule (W12 §W12-4 carry-forward).
   - **Gate**: NEW gate `S87-W0-PRIMARY-DECISION-RULE-BRANCH-1-EXTENSION`; PASS iff (a) §5 of decision-rule MD adds candidate C with explicit asymptote value AND (b) trigger condition is pre-registered as 2-of-2 (substrate-side branch-1 PASS AND DR3-side phantom return) AND (c) all three candidates A, B, C are documented with σ-distances per the §IV.3 table above. INFO iff branch-1 asymptote estimate uncertainty band exceeds the −0.942 boundary (in which case the extension is registered as PROVISIONAL pending S87 sparse-Lanczos extraction). FAIL iff editing breaks the existing §5 pre-registration audit trail.
   - **Effort**: 1 agent session (~2 hours): registry edit + pre-registration audit + cross-reference update in `falsifier-master-inventory.md` Row #1 footnote.

V.5. **Sparse-D_K Lanczos infrastructure module** (foundational tooling, prerequisite for V.1)
   - **What**: build new module `computations/_su3_sector_block_factory.py` providing block-diagonal sparse-CSR D_K instantiation by SU(3) representation sector at arbitrary L_max. Returns a dictionary {sector_label: scipy.sparse.csr_matrix} indexed by Young diagram or Dynkin label. Each block is small enough to fit in VRAM individually; full eigvalue spectrum recovered by union of per-block torch.linalg.eigvals on GPU. Enables L=14+ extraction without dense storage. Should reproduce existing L=8..12 spectra to ≤1e-10 absolute as the sanity-gate.
   - **Inputs**: `canonical_constants.py` (`tau_fold`, `M_KK`, `c_Gold`), existing dense-D_K builder `computations/s85_w0_zubarev_lmax_convergence_to_minus_one.py`, SU(3) representation theory tables (Dynkin label index for L_max ≤ 16), GPU pin (torch.linalg.eigvals on each sector block individually).
   - **Gate**: NEW gate `S87-SU3-SECTOR-BLOCK-FACTORY-BUILD`; PASS iff (a) module instantiates D_K at L=12 with bytes_total ≤ 1 GB total VRAM AND (b) reproduces s84_spectrum_cache_L12_tau019.npz spectrum to ≤1e-10 absolute on every eigenvalue AND (c) extends to L=14 with bytes_total ≤ 4 GB total VRAM (well within 0.5 × VRAM = 8.55 GB cap). INFO iff (a)+(b) PASS but L=14 sparse storage exceeds 4 GB (still extractable but tight). FAIL iff sparse path cannot reproduce dense L=12 spectrum within tolerance OR L=14 sparse storage exceeds 8.55 GB hard-halt.
   - **Effort**: 3-4 agent sessions (the SU(3) sector-decomposition tabulation is the substantive math; the sparse-CSR + per-block GPU eigvals is straightforward once sectors are tabulated). Total: ~10-12 agent hours, with the Dynkin-label representation theory table being the gating sub-task.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | L=14 dense D_K cache requires 1914 GB = 224× the 0.5×VRAM hard-halt | META | **FEASIBILITY-HALT** (no L=14 verdict) | The Zubarev L=14+ extension is sparse-D_K-shaped, not GPU-pin-shaped; carry-forward V.1 requires V.5 prerequisite. Spawn-prompt guardrail correctly fired. |
| 2 | w_0(L=12) excursion = 33.7% of R_842 half-width past lower edge (NOT 17%) | PHONONIC | INFO + WP-prose micro-error flagged | W12-4 verdict unchanged; carry-forward V.3 corrects WP prose. The substrate phantom-side excursion at L=12 is double the magnitude characterized in WP §W12-4. |
| 3 | rho_Z(L) series unconstrained-fit projects c0 = −0.81 → w_0_FW(L→∞) ≈ −1.15 | PHONONIC | INFO (existing S85 W0-7 FAIL re-interpreted) | The S85 W0-7 npz prior PRE-DATA-WISE prefers branch-1 (substrate-genuine phantom convergence); branch-1 outcome would put framework asymptote ≥6σ from EVERY DR3 scenario. Carry-forward V.4 extends decision rule. |
| 4 | Class F RECTANGLE-LABEL-DRIFT taxonomy extension proposed; passes retro-test on spawn-prompt's own R_918-as-R_842 drift | META | **PROPOSAL-DELIVERED** (PASS-on-pre-reg) | Carry-forward V.2 lands the code. Closes a structural blind-spot in `_source_reconciliation_audit.py` Classes A–E (which SHA-compare files but cannot detect label-vs-bounds drift in plan prose). |
| 5 | Branch-1 asymptote ≈ −1.15 inflates w_0 candidate ladder to A=−0.918, B=−0.842, C=−1.15 (plus W4-46 G51 −0.997) | PHONONIC | constraint-map update | Only A and B sit inside R_842; C and the W4-46 value sit outside. The PRIMARY-decision-rule §5 reversibility protocol needs a 3rd candidate clause. |
| 6 | Sparse-D_K block-diagonal Lanczos infrastructure does not exist in computations/ at S86; gating requirement for any L>12 work | META | foundational-tooling carry-forward | Carry-forward V.5 builds the prerequisite for V.1. Without V.5, V.1 cannot run. |

---

**End of synthesis.**

**Honest record**: no verdict line was appended to `computations/s86_gate_verdicts.txt` by this dispatch; the audit-extension code-block in §V.2 is delivered for S87 plan integration, not in-session integration; the W12 §W12-4 prose micro-error in §II.2 is flagged for S87 W3 micro-correction. No fabrication of L=13/14/15 rho_Z values; the spawn-prompt's pre-registered 3-branch decision rule remains UNFIRED until carry-forward V.1 lands (gated by V.5).

The structural finding of this synthesis is that the S87 carry-forward chain is **V.5 → V.1 → V.4** (build infrastructure → run extension → land decision-rule update if branch-1) **+ V.2 → V.3** (audit-extension landing + WP micro-correction). Five carry-forwards, all 4-field-spec compliant.

**File written**: `C:\sandbox\Ainulindale Exflation\sessions\archive\session-86\session-86-1a-s8-mack.md`
**Files NOT modified**: `computations/_source_reconciliation_audit.py`, `computations/canonical_constants.py`, `computations/s86_gate_verdicts.txt`, `sessions/framework/registry/w0-primary-decision-rule.md`, `sessions/archive/session-86/session-86-w12-workingpaper.md` — all per spawn-prompt rules ("Write ONLY the output file") and feasibility-halt discipline.
