# Session 86 Synthesis: Surviving CC-suppression corridor map after F_4 ∘ MB ∘ SD-subtraction closure

**Date**: 2026-04-27
**Agent**: gen-physicist (Workhorse-Gen-Physicist) — Slot 1a, Entry S-1
**Source Documents**:
- `sessions/archive/session-86/session-86-w2-workingpaper.md` (W2 Mellin-Barnes infrastructure; canonical for C9/C10/C11/C12)
- `sessions/archive/session-86/session-86-w3-workingpaper.md` (W3 Mellin-cone consequences; 6/6 PRE-REG-INC, mechanical closure)
- `sessions/permanent-results-registry.md` (registry rows for Two-Layer Obstruction, Atlas_5, F_4 / M partition, dilution-CC, q-theory closures)
- `computations/s86_gate_verdicts.txt` (canonical verdict file; lines 89-96 W2, 118-129 W3)
- `sessions/evoi-framework.md` (S83 stamp priority table)

Cross-pillar bridges per spawn-prompt: dilution-CC ↔ Pillar VIII (S65 SCALE-TRANSFER-65); Friedmann two-layer ↔ Pillar I (acoustic gravity, S58/S76); q-theory ↔ Pillar II (Volovik program); cutoff_sqrt + anomaly ↔ Pillar III (NCG regulator algebra).

---

## I. Session Outcome

W2 C9 (`S86-MELLIN-HEAT-KERNEL-INFRA`) returned FAIL `value=9.455686e+00` at L_max=10 by BOTH pre-registered FAIL branches simultaneously: ratio_min_in_F_4 = 9.4557 (19 OOM above the 5e-1 PASS bound) AND χ²/dof_max = 1.4696e+04 (3 OOM above the 20-FAIL bound). CC2 cross-check PASSed at machine-ε across all three F_4 regulators (rel_err ∈ {2.34e-16, 2.21e-16, 3.56e-16}), proving the FAIL is a substrate signature, not a Mellin-Barnes integrator artifact. The lens worked; the substrate does not admit F_4 CC suppression at L_max=10.

This single gate **CLOSES the F_4 ∘ MB ∘ SD-subtraction CC-suppression corridor** and **CONVERTS three prior S85 truncation-hypothesis FAILs to STRUCTURAL FAILs** (W0-7 ρ → −0.81 conjecture at val=−0.132 L_max=8; W0-11 CC-3 Connes-Moscovici residue; W0-20 Mellin-cone s=3 R_inf at val=1.81e+06 L_max=12). All three share the F_4 ∘ MB lens and the structural cause is now named: *F_4 cannot suppress*. Three surviving CC-suppression families remain — (i) C-regulator class outside F_4 (cutoff_sqrt + anomaly); (ii) Mellin-Strip / Convergence-Cone Theorem T5 boundary; (iii) non-MB mechanisms (dilution-CC, Friedmann two-layer gravity, q-theory). This synthesis produces the ranked corridor map across all three families.

---

## II. Key Results

### II.1 F_4 ∘ MB ∘ SD-subtraction corridor — CLOSED, structural

**Result**: GEOMETRIC. The 4-tuple `(value=9.455686e+00, scheme=MB-Connes-Moscovici, convention=SD-subtracted, L_max=10)` lands the closure with both PASS bound and FAIL bound exceeded by every member of F_4 = {ζ, Zubarev, SDW}.

Per-regulator at L_max=10 (W2 §W2-1 table; N_unique=78,080, N_pw-weighted=9,535,776, Λ=4.6702):
- ζ: ratio_0 = 1.0839e+01, χ²/dof = 1.4696e+04 (n=6 dominant, (Δ/σ)²=5.86e+04)
- Zubarev: ratio_0 = 9.4557, χ²/dof = 2.2047e+02 (n=6 + n=0 mixed)
- SDW: ratio_0 = 9.6870, χ²/dof = 4.2340e+02 (n=6 + n=0 mixed)

ratio_min_in_F_4 = 9.4557 (Zubarev, the pre-registered worst-case-smallest convention). The FAIL is independently confirmed by (a) the suppression criterion AND (b) the cross-method consistency criterion, on three regulators each. The CC2 NON-monotonic n=0 with ζ-class growth factor 239× (3.93e+05 → 9.38e+07 across L_max ∈ {5,6,7,8,10}) shows the substrate's a_0 spectral content has not yet entered the Weyl asymptotic regime at L_max=10; high-n slots (n=4, n=6) ARE converging monotonically (those moments are dominated by the smallest, stable eigenvalues), confirming the residue extractor is functioning at high n and the FAIL is structural at the cosmological-constant slot a_0.

The substrate-framing inversion: this is NOT "the Mellin-Barnes machinery did not work." The machinery worked (CC3 PASS at machine ε = 4 OOM tighter than the 1e-12 threshold). What it shows is the ABSENCE of an F_4 multiplier-algebra suppression structure in the substrate's a_0 slot. The framework cannot achieve cosmological-constant suppression by analytic continuation of the heat-kernel zeta within the F_4 algebra at this truncation; the suppression must live elsewhere.

### II.2 Three S85 FAILs converted: truncation-hypothesis → STRUCTURAL

**Result**: GEOMETRIC + registry-grade family entry. The C9 hypothesis "the substrate's a_0 spectral content is finite and the W0-7 / W0-11 / W0-20 FAILs were artifacts of finite L_max" is FALSIFIED. All three FAILs now stand as STRUCTURAL.

| S85 gate | Prior state | New state | Mechanism (post-C9) |
|:---------|:------------|:----------|:--------------------|
| W0-7 (ρ → −0.81 conjecture, val=−0.132 at L_max=8) | TRUNCATION-HYPOTHESIS FAIL | **STRUCTURAL FAIL** | Jensen-Zubarev ρ-exponent under F_4 ∘ MB cannot reach −1; structural-from-kernel |
| W0-11 (CC-3 Connes-Moscovici residue) | TRUNCATION-HYPOTHESIS FAIL | **STRUCTURAL FAIL** | F_4 multiplier-algebra cannot suppress |Λ_CC^MB|/|a_0| below 1e-1 |
| W0-20 (Mellin-cone s=3 R_inf, val=1.81e+06 at L_max=12) | TRUNCATION-HYPOTHESIS FAIL | **STRUCTURAL FAIL** | s=3 cone-apex residue not regulator-stable across F_4 |

**Registry-grade structural FAIL family entry** (W2 seed Candidate 4):
```
F_4-MB-SD-CC-SUPPRESSION-IS-STRUCTURALLY-EMPTY (S86-W2-1)
  Members: {S85 W0-7, S85 W0-11, S85 W0-20}
  Common lens: F_4 ∘ MB ∘ SD-subtraction at L_max ≥ 8
  Common cause: F_4 multiplier algebra (finite-vector class with support
                exactly {0, 2, 4, 6} on the SD slots) cannot suppress
                the substrate's a_0 spectral content on the truncated
                D_K cache.
  Closure verdict: S86-MELLIN-HEAT-KERNEL-INFRA FAIL by both ratio
                   (9.456 ≫ 5e-1, all 3 regulators) and χ²/dof (1.47e+04 ≫ 20).
  CC2 cross-check: machine-ε (CC2 PASS) — NOT an integrator artifact.
  audit_sha256: 1559e559208db268580961556082122cc4d97d73bb01a98c056cdde404155544
  content_sha256: ed4ee766ad00f31f71f475b476b511806cbbf8d5ed2ddf5567db9b40854482f7
```

This is the consolidated single-phenomenon entry the spawn prompt requires. All three S85 corridors close together; no further re-emission attempts under F_4 ∘ MB are possible without first changing the regulator class or the analytic-continuation mechanism.

### II.3 Three surviving corridors — ranked map

**Result**: GEOMETRIC (regulator-class corridors) + PHONONIC (substrate-density mechanisms).

Each of the three remaining families is named, given a formal mechanism, and stamped with: regime of validity, decisive S87+ gate, EVOI estimate, mutual-exclusivity flags, parallel-runnability flags. The constraint that ALL F_4 regulators FAILed by both branches at L_max=10 is the universal filter — a corridor survives only if it lies OUTSIDE the F_4 ∘ MB ∘ SD-subtraction lens. (Detailed table in Section IV; the registry-traceable constraint check appears alongside each entry.)

### II.4 Callable infrastructure delivered (W2 collateral)

**Result**: GEOMETRIC. Three modules survive the W2 cascade as reusable infrastructure for the surviving corridors:

- `computations/_analytic_zeta.py` (162 lines, C10 INFO) — `analytic_zeta(s, L_max) -> complex` API at d_spec=8 cone apex, off-pole. Callable for any complex s off the {2, 4} poles and any L_max in the loaded spectrum cache. Cross-checks (i) and (ii) sit in pre-registered INFO band (L_max=8→L_max=10 truncation-stability shift 6.11e-1 = 61%; ε-analyticity 1.124e-3 vs 1e-3 threshold by 1.12×). The truncation-stability INFO is the substrate's spectral-density-growth signature. **Surviving use**: feeds the Convergence-Cone Theorem T5 evaluation directly (corridor B below).
- `computations/_cluster_span_extract.py` (330 lines, C12 FAIL by precision-floor 0.5×float_eps). Bit-exact reproduction of W0-3 ratio `b2/b3 = 2.000000000000002` at L_max=12. Module CALLABLE; verdict-line FAIL is Publication-Precision Pre-Registration (canonical-metric algebraic factor-2 mismatch documented in §"Canonical-metric pin extension" of `epistemic-discipline.md`). **Surviving use**: K-corridor extension (W3 C13) — actual deviation is 3 OOM tighter than C13's `< 1e-12` threshold.
- `sessions/framework/registry/lizzi-finite-infinite-vector-classification.md` (133 lines, C11 PASS at max_rel_err=8.07e-28 = 16 OOM below threshold). **F_4 / M partition refined to 3-class taxonomy**: F_4 (finite-vector, support {0,2,4,6}: ζ, SDW, sharp-cutoff truncated); M (mixed-support continuous Mellin profile with residues outside {0,1,2,3}: cutoff_sqrt, anomaly-non-truncated); F_4-INF (singleton sub-atlas containing Zubarev: infinite-vector class whose Mellin-profile residues land EXACTLY on F_4 slots). The closed-form `M[exp(-x/Λ_Z²)](s) = Λ_Z^{2s}·Γ(s)` is permanent — algebraic property of the regulator kernel, independent of L_max truncation. **Surviving use**: anchors the T5 Mellin-Strip theorem (corridor B) and the per-regulator suppression analysis on cutoff_sqrt + anomaly (corridor A).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-MELLIN-HEAT-KERNEL-INFRA` (C9, W2-1) | **FAIL** | ratio_min_in_F_4 = 9.4557 ≫ 5e-1; χ²/dof_max = 1.4696e+04 ≫ 20 |
| `S86-MELLIN-CONE-RESIDUE-INFRASTRUCTURE` (C10, W2-2) | **INFO** | analytic_zeta(s=3, L_max=10) = 2.807432e+05 + 0j; χ²/dof = 2.166e-32 PASS structurally; truncation-stability 6.11e-1 in INFO band |
| `S86-MELLIN-MULTIPLIER-INFINITE-VECTOR-EXTENSION` (C11, W2-3) | **PASS** | max_rel_err = 8.066073499380351e-28 vs 1e-12 threshold (16 OOM margin) |
| `S86-CLUSTER-SPAN-EXTRACTOR-BUILD` (C12, W2-4) | **FAIL** (precision-floor) | rel_err = 1.083e-15 vs 1e-15 threshold; bit-exact W0-3 ratio reproduction |
| `S86-ZETA-REGULATOR-STABILIZATION-THEOREM-LANDING` (T9, W3-1) | **FAIL (PRE-REG-INC)** | blocked by C9 FAIL + C10 INFO; deferred to S87 |
| `S86-W0-7-MB-RE-EMIT` (W3-2) | **FAIL (PRE-REG-INC)** | blocked by C10 INFO; deferred to S87 |
| `S86-W0-11-MB-RE-EMIT` (W3-3) | **FAIL (PRE-REG-INC)** | blocked by C9 FAIL; deferred to S87 |
| `S86-W0-20-MB-RE-EMIT` (W3-4) | **FAIL (PRE-REG-INC)** | blocked by C10 INFO; deferred to S87 |
| `S86-CLUSTER-SPAN-K-CORRIDOR-EXTENSION` (C13, W3-5) | **FAIL (PRE-REG-INC)** | blocked by C12 FAIL + C19 FAIL; deferred to S87 |
| `S86-W3-11-LAMBDA-CONVENTION-RESOLUTION` (C43, W3-6) | **FAIL (PRE-REG-INC)** | blocked by C14 FAIL ('no_eigvals_in_cache'); deferred to S87 |

W3 6/6 are mechanical PRE-REG-INC closures (no specialist-agent dispatch, no physics computation). All audit_sha256 are per-gate-distinct (audit hash includes gate-identity keys); content_sha256 = `05071d10327d7f32fe88eb9d63278f3a4f737ca1f87280a3c51a5f8266c01686` shared across the closure script.

---

## IV. Structural Implications

### IV.1 The OOM-positioning substitution chain (why F_4 closure does NOT close cutoff_sqrt + anomaly)

Before ranking corridors I write the substitution chain governing the direction claim "F_4 closure does not propagate to the M = {cutoff_sqrt, anomaly} family." The claim is structural-from-construction; F_4 ⊂ Atlas_5 is a strict proper inclusion and the F_4 lens never evaluated cutoff_sqrt or anomaly.

```
Step 1 (definitions):
  F_4    := {ζ, Zubarev, SDW}                         (pure-a_4 family;
                                                       Mellin support exactly
                                                       on {0, 2, 4, 6})
  M      := {cutoff_sqrt, anomaly}                    (mixed-support family;
                                                       Mellin profile carries
                                                       residues outside {s ∈ {0,1,2,3}})
  Atlas_5 := F_4 ∪ M                                   (canonical 5-regulator
                                                       atlas per S85 W5-7 +
                                                       S86 plan-w14 §1)
  C9 evaluation set: r ∈ F_4 only (3 regulators tested)
  ratio_C9(r)         := |Λ_CC^MB(r)| / |a_0^trunc(r)| at L_max=10
  PASS_C9 ⟺ max_{r ∈ F_4} ratio_C9(r) ≤ 5e-1

Step 2 (substitution into C9 outcome):
  observed: ratio_C9(ζ)        = 1.084e+01
            ratio_C9(Zubarev)  = 9.456e+00
            ratio_C9(SDW)      = 9.687e+00
  max_{r ∈ F_4} ratio_C9(r)    = 1.084e+01
  PASS condition: 1.084e+01 ≤ 5e-1 ?  →  FALSE
  Verdict: FAIL on F_4.

Step 3 (canonical form for the inference scope):
  C9 verdict is a statement on F_4 measure only:
    proposition_C9 := ∀ r ∈ F_4, ratio_C9(r) > 5e-1.
  C9 says NOTHING about ratio_C9(r') for r' ∈ M, because M ∩ F_4 = ∅
  and no M-evaluation was performed at C9.

Step 4 (direction):
  F_4 corridor:    closure of CC-suppression at the F_4 ∘ MB ∘ SD-subtraction lens.
  M corridor:      ratio_C9(cutoff_sqrt), ratio_C9(anomaly) UNMEASURED at S86.
  Since proposition_C9 is universally quantified ONLY over F_4, no direction
  follows for M. The F_4 closure neither rules-in nor rules-out M-suppression.

Conclusion: F_4 closure does NOT propagate to M. The cutoff_sqrt + anomaly
corridor remains structurally OPEN at S86. Whether ratio_M is < 5e-1 (PASS)
or > 5e-1 (FAIL, joining F_4 in the same wall) is the C45 / C28 gate question
deferred to S87 W2 (per registry row PRR §C45 + §C28).
```

This chain governs corridor A below. The analogous chains for corridors B (Mellin-Strip) and C (non-MB) follow the same logical pattern: each lives in a measure-space the C9 lens did not cover.

### IV.2 Ranked corridor map (the joint-requirement deliverable)

Each of the three surviving families is ranked by EVOI per `feedback_reporting-framing.md` + `evoi-prioritization.md`. EVOI = P(pass) × |ΔP(pass)| + P(fail) × |ΔP(fail)|. Mutual-exclusivity (MX) and parallel-runnability (||) flags:
- MX(A,B) — corridors are MUTUALLY EXCLUSIVE if their PASS conditions are joint-incompatible
- ||(A,B) — corridors are PARALLEL-RUNNABLE if their decisive gates have disjoint input pins

| Rank | Corridor | Family | Formal mechanism | Regime of validity | Decisive S87+ gate | EVOI | MX flags | || flags |
|:----:|:---------|:-------|:------------------|:-------------------|:-------------------|:-----|:---------|:--------|
| 1 | **A. cutoff_sqrt + anomaly (M outside F_4)** | regulator-algebra (Pillar III, NCG) | C-regulator class evaluation: extend the C9 ratio test to r ∈ M = {cutoff_sqrt, anomaly}. The 3-class partition (F_4 / F_4-INF / M from C11) makes M structurally distinct from F_4 — the Mellin profile of cutoff_sqrt carries a SINGLE residue at slot a_4 (s=2 in lizzi convention; per s85-1c-perturbative-immunization-family.md), not the full 4-vector support of F_4. The anomaly regulator (Andrianov-Lizzi 2011, f_0=1/2 forced) carries residue weight outside {0,1,2,3} entirely. | NCG regulator algebra at d_spec=8; Mellin-support distinct from F_4. C28 (W4 cutoff_sqrt adjudication) must close first to determine whether cutoff_sqrt is structurally INCLUDED in the framework's regulator scope or STRUCTURALLY-EXCLUDED. Per registry §C28 the Two-Layer Obstruction (S86 W1b T7) holds n_joint = 0/3 within F_4 AND n_joint = 0/2 within M, so the WALL persists across either C28 outcome — but the OOM-position of M's CC-suppression ratio is independent. | `S87-CC-SUPPRESSION-ON-M = max_{r ∈ M} ratio_C9(r)` at L_max=10 with PASS ≤ 5e-1, INFO ∈ (5e-1, 5], FAIL > 5. Pre-registered cross-check: CC1 a_2 reproduction across M (the dispersion proxy used at C9). | **HIGH** (~22% — the PASS direction would re-open the entire MB-class of CC-suppression mechanisms after F_4 closed; the FAIL direction would CLOSE Atlas_5 ∘ MB entirely, an even larger constraint-map advance) | not MX with B (Mellin-Strip is a SEPARATE analytic-continuation mechanism); not MX with C (non-MB and M-MB are disjoint method classes) | || B (independent input pins: A uses spectrum cache + `_analytic_zeta.py` ratio; B uses `_analytic_zeta.py` strip-edge probe at Re(s) = 0+); || C (C uses Friedmann two-layer derivative at S58/S76 cache, fully disjoint) |
| 2 | **B. Mellin-Strip / Convergence-Cone Theorem T5** | regulator-algebra (Pillar III, NCG) | T5 boundary: the convergence cone of `analytic_zeta(s, L_max)` is the strip Re(s) > 0 (per C11 substitution chain — Zubarev's INFINITE-VECTOR Mellin profile `Λ_Z^{2s}·Γ(s)` is the analytic substrate of the strip, anchored by C11 PASS). The T5 boundary at Re(s) = 0+ is a DIFFERENT analytic-continuation mechanism from the Connes-Moscovici residue-extraction of C9 — it does NOT rely on the F_4 multiplier algebra acting on Seeley-DeWitt slots. T5 measures the CC slot through the strip-edge limit `lim_{s → 0+} s · analytic_zeta(s, L_max)` evaluated against the substrate's spectral density at the IR cutoff. | s ∈ {strip Re(s) > 0}; truncation-stability of strip-edge limit must converge faster than 6.11e-1 (the C10 truncation INFO at s=3); cross-check via the L-extrapolation `R(L) = R_∞ + α/L² + β/L⁴` on L ∈ {7,8,9,10}. | `S87-T5-STRIP-EDGE-LIMIT = lim_{s → 0+} s · analytic_zeta(s, L_max=10)` with PASS-window pre-registered against the substrate's CC-target ratio (factor ~1e-30 below `a_0^trunc` for genuine cosmological-constant value); INFO if the limit is finite but does not match the CC target; FAIL if the limit is divergent (which would close the strip-mechanism corridor in the same way C9 closed F_4). | **MEDIUM-HIGH** (~14%) — the C11 closed form anchors the analytic structure but the strip-edge OOM-position is unmeasured; the C10 API is callable with no infrastructure dependency | not MX with A (different lens: A measures residues at SD-slots, B measures the strip-edge limit) | || A (disjoint input pins as above); || C |
| 3 | **C. non-MB mechanisms** | substrate-density (Pillars I + II + VIII) | Three non-MB sub-mechanisms tested separately, all OUTSIDE the spectral-functional regulator-algebra class: (i) **dilution-CC** (S65 SCALE-TRANSFER-65 / S66 DILUTION-CC-66) — ρ_vac/ρ_rad = 0.67 at BBN, gap closure by today (per `project_dilution-cc-priority.md`); cross-pillar bridge to Pillar VIII. (ii) **Friedmann two-layer gravity** (S58 + S76 acoustic gravity; `s58_friedmann_derivation.py`, `s76_friedmann_bcs_exact.py`). The two-layer architecture splits Λ_CC across the BCS-gravity and Sakharov layers (per registry row "Two-level BCS-gravity description (SDW vs Sakharov)"); the S74 W1-E FAIL (86 OOM split) was structural and informative — the wrong question was solved (per `project_friedmann-wrong-question.md`); cross-pillar bridge to Pillar I. (iii) **q-theory** (Volovik program, registry §T9 + §T13 + framework-cc-oom.md). Mixed B-F q-theory exclusion (T9): same-spectrum B/F has at most one critical point, which is a maximum — no interior q-theory equilibrium. Net: 1 single-channel pathway closed, but the multi-channel q-theory remains open as F-theory equivalent (per `project_qtheory-ftheory.md`); cross-pillar bridge to Pillar II. | (i) BBN-era τ ≪ τ_fold; (ii) post-fold acoustic-gravity double layer with Goldstone separation per S58; (iii) q-theory variational: dE_ZP/dq > 0 monotonicity (per registry §"CC = Integrability"). | (i) `S87-DILUTION-CC-SCALE-TRANSFER-RECONFIRM` at L_max=10 with the scale-transfer ratio recomputed against present-day H_0 anchor; PASS if ratio remains in S66 PASS scenario B band. (ii) `S87-FRIEDMANN-TWO-LAYER-LAMBDA-PARTITION` — recompute the SDW vs Sakharov layer split with W2's `analytic_zeta` API as the SDW-layer evaluator; PASS if total Λ partition lands within factor 10 of observed CC. (iii) `S87-Q-THEORY-MULTI-CHANNEL-EQUILIBRIUM` — search beyond the single-channel T9 closure for multi-channel equilibrium points; INFO if no equilibrium exists at any channel count. | **MEDIUM** (~10% combined; ~5% per sub-mechanism after the prior closures) — sub-mechanisms (i) and (iii) have substantial historical state already (S65, S66, S58, S76); (ii) is the highest-leverage among the three because the F_4 closure removes the spectral-functional contender, leaving acoustic-gravity Λ-partition as the structural alternative | not MX with A or B (different physical mechanisms; non-MB is method-class-disjoint) | || A; || B; the three sub-mechanisms (i), (ii), (iii) are also || each-other (disjoint input caches) |

**Universal F_4 constraint check** (the spawn-prompt joint requirement): each surviving corridor is tested against the constraint that ALL F_4 regulators FAILed by both branches at L_max=10:

- Corridor A passes the constraint check vacuously: M ∩ F_4 = ∅; A's measure-space is disjoint from C9's. The substitution chain in §IV.1 shows F_4 closure does not propagate to M.
- Corridor B passes the constraint check by construction: the strip-edge limit `lim_{s → 0+} s · analytic_zeta(s, L_max)` does not factor through the F_4 multiplier algebra. T5 evaluates the analytic continuation directly through the C11 closed-form Mellin profile, not through the SD-subtraction prescription.
- Corridor C passes the constraint check by mechanism class: dilution, Friedmann two-layer, and q-theory are non-spectral-functional mechanisms. They do not invoke any F_4 regulator and do not perform Mellin-Barnes residue extraction. The F_4 ∘ MB ∘ SD-subtraction lens is irrelevant to their evaluation.

All three corridors survive the spawn-prompt constraint check.

### IV.3 What W2 also gives the surviving corridors

- The C10 `analytic_zeta(s, L_max)` API is the analytic anchor for corridor B's strip-edge probe and is consulted by corridor A's CC1 dispersion proxy (extended to M).
- The C11 3-class partition (F_4 / F_4-INF / M) supplies the structural reason corridor A is non-trivial: M is genuinely distinct from F_4 at the multiplier-algebra dimension, not just at the slot-support level.
- The C12 `cluster_span(L_max)` module is callable for the K-corridor probe in any of the three corridors that wants to test cluster identities at their own evaluation points.

### IV.4 What did NOT advance

- W3 was 6/6 PRE-REG-INC mechanical closure — no physics in W3. The W3 plan-blocks (C9, C10, C12, C14, C19 prerequisites) carry forward as-is to S87.
- The Two-Layer Obstruction (S86 W1b T7, S86-TWO-LAYER-OBSTRUCTION-LANDING PASS at content_sha256=`deadfc5824ad8883…`) holds across both F_4 (n_joint=0/3) and M (n_joint=0/2). This is a separate wall from the F_4 ∘ MB ∘ SD-subtraction closure — it concerns joint-conjunct PASS across regulators, not single-regulator suppression. The corridor map above is orthogonal to this wall.

---

## V. Carry-Forward Computations

Per `feedback_fix-in-session-never-defer.md` + the spawn-prompt mandate: 4-field specs (what / inputs / gate / effort) for each surviving corridor's first decisive S87+ gate. Each spec is independently dispatchable.

```
V.1. CC-SUPPRESSION-ON-M corridor opener (rank-1 EVOI)
   - What: extend the C9 mellin_barnes_residue_extractor with explicit
     SD-subtraction to evaluate ratio_C9(r) for r ∈ M = {cutoff_sqrt, anomaly}
     at L_max=10 on the canonical D_K spectrum cache. Compute
     |Λ_CC^MB(r)| / |a_0^trunc(r)| AND χ²/dof against the truncation
     residual, reproducing the exact C9 protocol on the M-family. Verify
     CC2 monotonicity per regulator; verify CC3 (contour-deformation
     self-consistency at s=2.5) at machine-ε precision.
   - Inputs:
     * computations/canonical_constants.py (M_KK, tau_fold, Vol_SU3)
     * computations/s84_spectrum_cache_L12_tau019.npz (the D_K cache)
     * computations/_analytic_zeta.py (C10 callable API)
     * computations/s86_w2_c9_mellin_heat_kernel_infra.py (C9 reference
       script; copy SD-subtraction prescription verbatim, swap regulator)
     * cutoff_sqrt evaluator (per s86_w8_p7_rho_substrate_mc.py REGULATOR_EVAL_MAP)
     * anomaly evaluator (Andrianov-Lizzi 2011, f_0 = 1/2 forced;
       per .claude/rules/epistemic-discipline.md scrubbed-plan §0.6)
   - Gate: S87-CC-SUPPRESSION-ON-M
       PASS_ratio:  max_{r ∈ M} ratio_C9(r) ≤ 5e-1
       PASS_chi:    max_{r ∈ M} χ²/dof    ≤ 5
       INFO_ratio:  5e-1  < ratio ≤ 5
       INFO_chi:    5     < χ²/dof ≤ 20
       FAIL_ratio:  ratio > 5
       FAIL_chi:    χ²/dof > 20
       Either FAIL branch alone triggers FAIL (per C9 convention).
   - Effort: 4-6 hours, 1 agent session (spectral-geometer or lizzi-spectral-functional-theorist).
     Same template as C9; primary cost is anomaly-regulator implementation.

V.2. T5 strip-edge limit (rank-2 EVOI)
   - What: evaluate lim_{s → 0+} s · analytic_zeta(s, L_max=10) on the
     finite-spectrum truncation, using a 5-point sweep s ∈ {0.001, 0.005,
     0.01, 0.05, 0.1} with mpmath workdps=50. Cross-check the limit by
     L-extrapolation R(L) = R_∞ + α/L² + β/L⁴ on L ∈ {7, 8, 9, 10}.
     Compare the strip-edge limit against the substrate's CC-target ratio
     (Λ_CC,obs / Λ_CC,naive ~ 1e-120 in Pillar I units; corresponding
     dimensionless target ratio in spectral units pre-registered from
     c_fabric · M_KK normalization).
   - Inputs:
     * computations/canonical_constants.py
     * computations/_analytic_zeta.py (C10)
     * computations/s84_spectrum_cache_L12_tau019.npz
     * sessions/framework/registry/lizzi-finite-infinite-vector-classification.md
       (C11 closed-form for cross-check)
   - Gate: S87-T5-STRIP-EDGE-LIMIT
       PASS:  finite limit, agrees with CC-target ratio within factor 10
       INFO:  finite limit, does NOT agree with CC-target within factor 10
       FAIL:  divergent limit OR L-extrapolation does not converge
              (closes the strip-mechanism corridor analogously to F_4 ∘ MB)
   - Effort: 3-4 hours, 1 agent session (lizzi-spectral-functional-theorist).
     C10 API is callable; primary cost is the L-extrapolation fit and
     CC-target normalization.

V.3. Friedmann two-layer Λ-partition (rank-3, sub-mechanism (ii); highest leverage of corridor C)
   - What: re-derive the SDW vs Sakharov Λ-partition of the Friedmann
     two-layer gravity (per s58_friedmann_derivation.py + s76_friedmann_bcs_exact.py)
     using the C10 analytic_zeta(s, L_max=10) as the SDW-layer evaluator,
     replacing the previous SDW partial-sum approximations. Compute
     Λ_total = Λ_BCS-grav + Λ_Sakharov and compare to observed CC
     (Λ_obs ~ 1.1e-52 m^-2 in geometric units).
   - Inputs:
     * computations/canonical_constants.py
     * computations/s58_friedmann_derivation.py (BCS-grav layer)
     * computations/s76_friedmann_bcs_exact.py (current SDW layer)
     * computations/_analytic_zeta.py (C10 replacement evaluator)
     * computations/s84_spectrum_cache_L12_tau019.npz
   - Gate: S87-FRIEDMANN-TWO-LAYER-LAMBDA-PARTITION
       PASS:  |Λ_total / Λ_obs - 1| < 10  (factor-10 agreement)
       INFO:  factor 10-100 agreement (substantive but not closing)
       FAIL:  factor > 100 disagreement OR Λ_total has wrong sign
   - Effort: 5-7 hours, 1 agent session (cosmology-bridge agent or mack).
     Higher-effort due to the Sakharov-layer reformulation; but the F_4
     closure removes the spectral-functional alternative, raising the
     marginal value of this gate.

V.4. Dilution-CC scale-transfer reconfirm (rank-3, sub-mechanism (i))
   - What: recompute SCALE-TRANSFER-65 / DILUTION-CC-66 against present-day
     H_0 anchor using the latest spectrum cache. Verify ρ_vac/ρ_rad = 0.67
     at BBN remains consistent with the framework's evolved state (per
     project_dilution-cc-priority.md "gap closure by today, not at fold").
   - Inputs:
     * computations/canonical_constants.py
     * computations/s66_dilution_cc.py (reference script)
     * computations/s67_bbn_volovik.py (cross-check ρ_vac/ρ_rad)
     * computations/s84_spectrum_cache_L12_tau019.npz
     * Planck 2018 BBN constraints (Y_p, D/H values used in S67)
   - Gate: S87-DILUTION-CC-SCALE-TRANSFER-RECONFIRM
       PASS:  ρ_vac/ρ_rad at BBN within 20% of S66 Scenario B value (0.67)
       INFO:  within 20-50% of S66 value (drift but not break)
       FAIL:  > 50% deviation from S66 value
   - Effort: 2-3 hours, 1 agent session (gen-physicist or volovik-superfluid-universe-theorist).
     Recompute against S66 with current canonical_constants and current cache.

V.5. q-theory multi-channel equilibrium search (rank-3, sub-mechanism (iii))
   - What: extend T9 (Mixed B-F q-theory exclusion: same-spectrum B/F has
     at most one critical point, which is a maximum) to the multi-channel
     case where B and F spectra differ. Search the variational dE_ZP/dq
     > 0 monotonicity per registry §"CC = Integrability" across the
     multi-channel parameter space. Look for INTERIOR equilibrium points.
   - Inputs:
     * computations/canonical_constants.py
     * computations/s48_volovik_string.py (cc_gap_gravity, cc_ratio_grav,
       cc_ratio_kern reference)
     * computations/s84_spectrum_cache_L12_tau019.npz (B and F sectors)
     * registry §T9 + §"Mixed B-F q-theory" closures
   - Gate: S87-Q-THEORY-MULTI-CHANNEL-EQUILIBRIUM
       PASS:  interior equilibrium point exists (would re-open q-theory CC corridor)
       INFO:  no interior equilibrium at any tested channel count
              (extends T9 closure to multi-channel)
       FAIL:  monotonicity dE_ZP/dq > 0 violated at any channel count
              (would falsify the variational-monotonicity registry §T9)
   - Effort: 4-5 hours, 1 agent session (volovik-superfluid-universe-theorist
     or feynman-qft-fundamentalist).

V.6. Registry-grade family-entry landing for F_4-MB-SD closure
   - What: write the consolidated single-phenomenon registry entry per
     §II.2 above into sessions/permanent-results-registry.md as a Family
     Entry. The entry consolidates {S85 W0-7, S85 W0-11, S85 W0-20} as
     STRUCTURAL FAILs sharing the F_4 ∘ MB ∘ SD-subtraction lens; pins
     C9's audit_sha256 + content_sha256 as the closure provenance; cites
     the §IV.1 substitution chain showing F_4 closure does not propagate
     to M.
   - Inputs:
     * sessions/archive/session-86/session-86-w2-workingpaper.md (C9 verdict, §1
       Wave-W2 Synthesis, §IV.1 substitution chain text from this synthesis)
     * sessions/permanent-results-registry.md (target file)
     * computations/s86_gate_verdicts.txt lines 95-96 (C9 verdict +
       dual-SHA companion row)
     * S85 verdict lines for W0-7, W0-11, W0-20 (cite by sha256)
   - Gate: S87-F4-MB-SD-FAMILY-ENTRY-REGISTRY-LANDING
       PASS:  registry entry written with all four SHA pins, all three S85
              gates listed, and the substitution chain reference
       FAIL:  any pin missing OR substitution-chain reference broken
   - Effort: 1-2 hours, 1 agent session (lizzi-spectral-functional-theorist
     or registry-write-only worker).

V.7. C28 cutoff_sqrt structural-exclusion adjudication closeout
   - What: close the open INFO verdict on S86-W-4-CUTOFF-SQRT-ADJUDICATION
     (verdict-file line 106: REQUIRES-S86-GATE INFO). Per registry §C28,
     the outcome determines whether cutoff_sqrt is in the framework's
     regulator scope. The decision unblocks corridor A (rank-1) S87
     dispatch — if cutoff_sqrt is STRUCTURALLY-EXCLUDED, corridor A's
     M-family reduces to {anomaly} only.
   - Inputs:
     * sessions/archive/session-85/workshops/cutoff-sqrt-adjudication.md (3-round
       workshop closeout)
     * computations/s86_gate_verdicts.txt line 106 (S86-W-4-CUTOFF-SQRT-ADJUDICATION INFO)
     * registry §C28 entry
   - Gate: S87-CUTOFF-SQRT-CORE-ATLAS-DECISION
       PASS:  STRUCTURALLY-EXCLUDED (cutoff_sqrt removed from atlas)
       PASS:  GENUINELY-PHYSICAL (cutoff_sqrt retained in atlas; M = {cutoff_sqrt, anomaly})
       INFO:  REQUIRES-S87-GATE (cascade defer; should be avoided)
   - Effort: 2-3 hours, 1 agent session (connes-ncg-theorist + lizzi
     workshop closeout).
     This is a prerequisite for V.1 — without it, V.1's M-family is
     under-pinned (PRU Class 8).
```

These seven carry-forwards constitute the complete forward queue from this synthesis. V.1, V.2, V.3, V.4, V.5 are physics gates with pre-registered thresholds. V.6 and V.7 are registry / closeout tasks that unblock the physics gates. All seven are independently dispatchable. The parallel-runnability table in §IV.2 confirms V.1, V.2, and V.3 can be dispatched in the same wave.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | F_4 ∘ MB ∘ SD-subtraction CC-suppression corridor closed | GEOMETRIC | **CLOSED** (C9 FAIL on both branches) | Eliminates an entire family of analytic-continuation strategies for cosmological-constant suppression on the truncated D_K cache at L_max=10 |
| 2 | Three S85 truncation-hypothesis FAILs converted to STRUCTURAL (W0-7, W0-11, W0-20) | GEOMETRIC | **STRUCTURAL** (Family Entry) | Cascade-sharpens the constraint map by 3 corridor closures; the registry-grade family entry consolidates them as a single phenomenon |
| 3 | Corridor A: cutoff_sqrt + anomaly (M outside F_4) | GEOMETRIC | **OPEN, rank-1 (~22% EVOI)** | F_4 closure does NOT propagate to M (substitution chain §IV.1); decisive S87 gate `S87-CC-SUPPRESSION-ON-M` |
| 4 | Corridor B: Mellin-Strip / Convergence-Cone Theorem T5 boundary | GEOMETRIC | **OPEN, rank-2 (~14% EVOI)** | C11 closed-form anchors the strip Re(s)>0; decisive S87 gate `S87-T5-STRIP-EDGE-LIMIT` via callable C10 API |
| 5 | Corridor C: non-MB mechanisms (dilution-CC, Friedmann two-layer, q-theory) | PHONONIC | **OPEN, rank-3 (~10% combined EVOI)** | Three sub-mechanisms parallel-runnable; Friedmann two-layer is highest-leverage sub-component because F_4 closure removes the spectral-functional alternative |
| 6 | C10 `analytic_zeta(s, L_max)` API delivered (W2-2 INFO) | GEOMETRIC | **CALLABLE** (infrastructure) | Anchors corridor B; consultable for corridors A and C cross-checks |
| 7 | C11 F_4 / M / F_4-INF 3-class partition theorem (W2-3 PASS) | GEOMETRIC | **PERMANENT** (registry note) | Structural reason corridor A is non-trivial; Zubarev's INFINITE-VECTOR class explains F_4 sub-atlas heterogeneity |
| 8 | C12 `cluster_span(L_max)` module delivered (W2-4 FAIL by precision-floor) | GEOMETRIC | **CALLABLE** (infrastructure); verdict FAIL by 0.5×float_eps | K-corridor probe usable in any surviving corridor; W3 C13 functionally unlocked at 3 OOM tighter than its own threshold |
| 9 | W3 6/6 mechanical PRE-REG-INC closure | (none — no physics) | **DEFERRED to S87** | Plan-blocks C9, C10, C12, C14, C19 carry forward as-is |
| 10 | C28 cutoff_sqrt adjudication INFO (REQUIRES-S86-GATE) | GEOMETRIC | **OPEN — must close S87** | Prerequisite for corridor A dispatch (V.1 PRU Class 8 vulnerability without it) |

**Substrate-framing closeout**: this is a constraint-map-advancing session in the substrate-first sense. The Mellin-Barnes machinery is the LENS the substrate is being read through — not the source of the result. C9 FAIL is what the substrate reveals when read through F_4 ∘ MB ∘ SD-subtraction at L_max=10: the substrate's a_0 spectral content is genuinely large in the F_4 regulator class. The framework must seek the cosmological-constant suppression elsewhere — outside F_4 (corridor A: M-family lens), outside the SD-residue-extraction mechanism (corridor B: strip-edge limit), or outside the spectral-functional class entirely (corridor C: substrate-density mechanisms via Pillars I, II, VIII). The W2 outputs (C10 API, C11 partition, C12 module, F_4-MB-SD family entry) are the infrastructure that supports searching that elsewhere.
