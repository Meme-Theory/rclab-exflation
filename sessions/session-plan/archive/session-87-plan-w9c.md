# Session 87 Plan — Sub-Wave 9c: c_sub Axiom-Side Cross-Review (connes-ncg)

**Owner**: `connes-ncg-theorist` (W-9 CF-3 attribution from S86; CF-56)
**Output verdict file**: `computations/s87_gate_verdicts.txt`
**Script prefix convention**: `computations/s87_w9c_<slug>.py`
**Item count**: 1 (CF-56)
**Cross-cite specialists**: `lizzi-spectral-functional-theorist` (cross-cite ONLY for proxy-source pin from W-9 §T-CR2.3 / lizzi A-T4.2 candidate; runtime dispatch is single-agent connes-ncg)

---

## Sub-Wave 9c Summary

Sub-Wave 9c executes the single W-9 CF-3 carry-forward `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` per `.claude/rules/epistemic-discipline.md` §"Verifier-Rubric Pre-Registration extension — Cross-Proxy Adjudication" (T1-19 / S86 W-9 RULE-2). This is an AXIOM-SIDE cross-review of S86 W5b §W5b-2 gate `S86-W5B-C16-CSUB-ADMISSIBILITY` which closed with INFO verdict (2/3 sub-tests PASS): atlas-membership PASS + τ-stationarity PASS + sign-reversal sub-test (c) FAIL at the τ-flow-trace proxy `c_sub_anomaly(τ) := d c_sub(τ)/dτ` (W5b workingpaper line 331). The C16 INFO admits TWO interpretive readings the workshop closed without adjudicating: (A) the literal τ-flow-trace FAIL stands → C16 confirmed INFO at L_max=10, OR (B) an algebraically-distinct anomaly-isolating proxy (lizzi A-T4.2 candidate: substrate-distance-2 WZW consistency residue at pole s=4) yields PASS → C16 promotes from INFO to ADMISSIBLE.

The cross-review's substrate-physics content is the CONFORMAL-ANOMALY isolation problem: the τ-flow-trace proxy `d c_sub(τ)/dτ` is a MIXED observable (it traces the full Mellin-moment derivative, including non-anomaly contributions like τ-dependence of the bare moment). The lizzi A-T4.2 candidate operationalizes a STRUCTURALLY DISTINCT proxy that isolates the conformal-anomaly contribution alone via the substrate-distance-2 WZW-consistency residue:

```
c_sub_anomaly_WZW(R) := Res[M_R(s) · anomaly_kernel; s=4] / Res[M_R(s); s=3]
```

where `M_R(s)` is the regulator-R-weighted Mellin transform of D_K^{≤10} and `anomaly_kernel` is the NCG-axiomatic conformal-anomaly kernel (a substrate-distance-2 pole isolator at s=4 versus the substrate-distance-1 normalization pole at s=3). The cross-review is **algebraically distinct** from the τ-flow-trace proxy — different operator (residue vs τ-derivative), different pole (s=4 vs τ-flow), different physical interpretation (WZW-consistency vs flow-trace). Both proxies are NCG-admissible; both target the conformal-anomaly contribution; the cross-review's task is to determine which proxy correctly isolates the substrate's actual conformal-anomaly content.

### One gate-item

- **§W9c-1 / CF-56** `S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` — Independent cross-reviewer (`connes-ncg-theorist`, NOT the original W5b lizzi authoring agent) operationalizes the lizzi A-T4.2 candidate substrate-distance-2 WZW-consistency residue proxy `c_sub_anomaly_WZW(R)` for the (C_H, C_epsH) parity-twin pair from the §VII.S sub-row family AND the broader 5-atlas regulator family. PASS = the WZW proxy yields a sign-reversal-CONSISTENT verdict across τ_fold (matching the canonical-constants ledger's expected sign-reversal direction); FAIL = the WZW proxy ALSO fails the sign-reversal test (the C16 INFO stands; both proxies agree that the sign-reversal sub-test FAILs); INFO = the WZW proxy is regime-marginal (Mellin-cone substrate-distance-2 convergence at s=4 is grazing the regulator's analytic boundary).

### Substrate-framing direction

The cross-review flows FROM the substrate (D_K^{≤10} eigenvalue spectrum + Mellin-moment residue structure at substrate-distance-1 and substrate-distance-2 poles) TOWARD the emergent observable (c_sub admissibility verdict). Both proxies (τ-flow-trace and WZW-consistency residue) are SUBSTRATE-IS quantities — they are spectral-moment functionals of D_K^{≤10}, not container observables evaluated "in" a regulator-bookkeeping space. Per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space": the regulator R does NOT contain the c_sub_anomaly observable; the regulator R IS a particular Mellin-cone weighting that selects a particular spectral-moment functional from the substrate. The cross-review's structural question is whether two distinct spectral-moment functionals (τ-flow-trace at substrate-distance-1 vs WZW-residue at substrate-distance-2) extract the SAME conformal-anomaly content from D_K, or whether one proxy is anomaly-blind while the other is anomaly-sensitive.

### Open-verdict framing (MANDATORY — Class-6-adjacent prohibition)

Per `.claude/rules/epistemic-discipline.md` §"Cross-Proxy Adjudication" requirement (2): the verdict between (A) prior FAIL stands → C16 confirmed INFO at L_max=10 vs (B) cross-proxy yields PASS → C16 promotes from INFO to ADMISSIBLE MUST remain open and not pre-judged. This plan-block contains NO Class-6-adjacent ("iterate-until-PASS") framing. The dispatch prompt is symmetric across the two readings; the substitution chain Step 4 reads the direction off the canonical form WITHOUT pre-committing to either Track A (FAIL stands) or Track B (PASS via WZW); the PASS/FAIL/INFO threshold block is symmetric (PASS direction matches canonical-ledger expected sign-reversal; FAIL direction matches the τ-flow-trace proxy's negative-sign-both-sides finding; INFO is the regulator-regime-marginal band). Per `.claude/rules/v3-closure-recovery.md` PROHIBITED_ACTIONS Class 6: ANY mid-execution alteration of the WZW-proxy formula, the s=4 substrate-distance-2 pole pin, or the sign-reversal acceptance threshold to convert a FAIL into a PASS triggers a Stage-3 PROHIBITED_ACTIONS halt. The compute is ALLOWED to return either PASS or FAIL or INFO; the plan binds the dispatch to the pre-registered formulae and threshold band.

---

## Sub-Wave 9c Decision Point Prerequisites

W9c has TWO upstream sequencing constraints. Neither is a plan-write blocker (the W9c plan is written independently of these landings); each is checked at compute-dispatch time.

1. **S86 W5b §W5b-2 verdict line + working-paper section presence** — `S86-W5B-C16-CSUB-ADMISSIBILITY` verdict line MUST be in `computations/s86_gate_verdicts.txt` at compute time (it landed at S86-close per context §1.2; verified by grep at plan-freeze). The working-paper section `sessions/archive/session-86/session-86-w5b-workingpaper.md` §W5b-2 (lines 242-460) MUST be on disk for the τ-flow-trace proxy formula and the 3-sub-test classification (atlas-membership PASS, τ-stationarity PASS, sign-reversal FAIL). If absent at runtime, dispatch HALTS with `prereq_block=S86-W5B-C16-not-on-disk` per `.claude/rules/mechanical-closure-discipline.md` (the cross-review cannot proceed without the prior FAIL it is challenging).

2. **W-9 §T-CR2.3 lizzi A-T4.2 proxy specification (workshop wrap-up text)** — the WZW-consistency residue proxy formula `c_sub_anomaly_WZW(R)` was authored at S86 W-9 workshop §T-CR2.3 lines 1291-1334 by lizzi-spectral-functional-theorist. The proxy's pre-registration source MUST be on disk; the runtime dispatch reads the formula from the workshop file (or from the S87 STAGE-1 entry if CF-54 has landed the Joint F_2-Class Path-(c) Theorem with the WZW proxy as a clause-supporting anchor). Pin SHA late-bind from W-9 workshop file.

These are SEQUENCING constraints, not plan-write dependencies. The W9c plan freezes all per-gate machinery pins; the late-bind SHAs are documented in the Input-SHA Ledger below.

### Existing §VII slot-state at S86-close (for cross-review's registry-citation context)

- `§VII.S` — Perturbative-Ledger Immunization Family (relocated from §VII.Y at S86 W1a-1; sub-rows §VII.S.C-eta + §VII.S.C-theta) — OCCUPIED. The (C_H, C_epsH) parity-twin pair from §VII.S is the per-pair specialization the cross-review evaluates.
- `§VII.W` — Pillar III↔IV cross-pillar bridge theorem (S86 W-5; OCCUPIED). The cross-review does NOT route a registry edit to §VII.W; the cross-review's verdict is recorded ONLY in the verdict file + the working-paper section.
- This sub-wave does NOT land a new §VII slot. The cross-review's outcome modifies the C16 INFO classification (either confirmed INFO or promoted to ADMISSIBLE); the registry impact is at the FALSIFIER-INVENTORY level, not the §VII PERMANENT-RESULTS level. The W-9 carry-forward line CF-56 explicitly scoped this gate as a "cross-review" — i.e., a re-classification of an existing INFO outcome, not a new theorem-grade landing.

---

## §W9c-1. S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW (CF-56)

```yaml
gate_id: S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW
trigger: [VERIFY] [CROSS-PROXY-ADJUDICATION]
classification: GEOMETRIC
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
agent_type: connes-ncg-theorist
wave: W9c
effort_estimate: 1.0 wave (~10-14h)
provenance_carry_forward: CF-56 (W-9 CF-3 from compute-carryforward.md line 153)
rule_anchor_T1_19: .claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration extension — Cross-Proxy Adjudication"
```

### 1. Gate ID
`S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW` (carry-forward CF-56; compute-carryforward.md W-9 CF-3 attributing connes-ncg). Cross-proxy adjudication per `.claude/rules/epistemic-discipline.md` §"Verifier-Rubric Pre-Registration extension — Cross-Proxy Adjudication" (T1-19, S86 W-9 RULE-2).

### 2. Trigger
`[VERIFY]` (substitution chain mandatory per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute" — the cross-review makes a sign/direction claim about the conformal-anomaly contribution to c_sub under sheet-flip across τ_fold) + `[CROSS-PROXY-ADJUDICATION]` (the gate's PASS/FAIL/INFO outcome adjudicates between the τ-flow-trace prior-FAIL and the WZW-consistency-residue alternative-PASS readings; per T1-19 the proxy operationalization is rubric-pinned; per T1-19 (2) the verdict remains open and not pre-judged).

### 3. Classification
**GEOMETRIC**. Both proxies (τ-flow-trace `c_sub_anomaly(τ) := d c_sub(τ)/dτ` and WZW-consistency residue `c_sub_anomaly_WZW(R) := Res[M_R(s) · anomaly_kernel; s=4] / Res[M_R(s); s=3]`) are spectral-moment functionals of D_K^{≤10} on the Jensen-deformed SU(3) substrate at τ_fold = 0.190. The cross-review tests the substrate-canonical SHEET STRUCTURE of the Riemann cover at the van Hove fold (per S39 transit phase transition + S79 P1-2 W2-E sign-reversal closure rule cited in W5b workingpaper line 328). The conformal-anomaly contribution is a SUBSTRATE-IS quantity (it lives in the Mellin-cone residue structure of D_K, not in any regulator container); the cross-review's task is to confirm whether two distinct NCG-admissible spectral-moment functionals extract the same conformal-anomaly content, or whether the τ-flow-trace proxy is anomaly-blind while the WZW proxy is anomaly-sensitive.

### 4. Agent type
**Runtime primary**: `connes-ncg-theorist` (lead per W-9 CF-3 attribution; per T1-19 + `.claude/rules/joint-theorem-promotion.md` §"Two-Agent Independent-Verify (Stage 2 details)" the cross-reviewer MUST NOT be the original W5b authoring agent; the W5b §W5b-2 author was `lizzi-spectral-functional-theorist`, hence connes-ncg is the structurally-correct independent cross-reviewer).

**Cross-cited co-sign (NOT spawned as collab agent)**: `lizzi-spectral-functional-theorist` cross-cited ONLY at the proxy-source pin level (the lizzi A-T4.2 WZW-consistency residue proxy formula is read from W-9 workshop file via input-SHA pin; lizzi is NOT spawned as a collab agent). The runtime dispatch is single-agent (connes-ncg).

### 5. Hypothesis
The substrate-distance-2 WZW-consistency residue proxy `c_sub_anomaly_WZW(R)` (algebraically distinct from the substrate-distance-1 τ-flow-trace proxy `c_sub_anomaly(τ)`) is the structurally-correct conformal-anomaly isolator for D_K^{≤10} at τ_fold under the (C_H, C_epsH) parity-twin pair AND the broader 5-atlas regulator family. PASS = the WZW proxy yields a sign-reversal verdict CONSISTENT with the canonical-constants ledger's expected post-fold sheet-flip direction (positive c_sub_anomaly_WZW(R) on one side of τ_fold, negative on the other); FAIL = the WZW proxy ALSO fails the sign-reversal test (both proxies agree the sign-reversal sub-test (c) FAILs ⇒ C16 INFO stands across L_max=10 axiom-side cross-review); INFO = the WZW proxy is regime-marginal (Mellin-cone substrate-distance-2 convergence at s=4 grazes the regulator's analytic boundary, sign verdict undecidable at L_max=10).

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `connes-ncg-theorist`:

You are the AXIOM-SIDE INDEPENDENT CROSS-REVIEWER for the S86 W5b §W5b-2 gate
S86-W5B-C16-CSUB-ADMISSIBILITY which closed with INFO verdict (2/3 sub-tests PASS;
sign-reversal sub-test FAIL at the τ-flow-trace proxy). You operationalize an
ALTERNATIVE anomaly-isolating proxy (the lizzi A-T4.2 WZW-consistency residue
proxy at substrate-distance-2 pole s=4) per S87-W9c-1 (CF-56 from W-9 CF-3).

The cross-review's verdict adjudicates between:
  Track A — Prior FAIL stands → C16 confirmed INFO at L_max=10 axiom-side
            (the WZW proxy ALSO returns sign-reversal FAIL ⇒ both proxies agree
             the substrate-distance pole structure does NOT yield the canonical
             sign-reversal at τ_fold under the C_H + C_epsH parity-twin pair).
  Track B — Cross-proxy yields PASS → C16 promotes from INFO to ADMISSIBLE
            (the WZW proxy returns sign-reversal CONSISTENT with the canonical
             ledger's expected post-fold sheet-flip direction ⇒ the τ-flow-trace
             proxy was anomaly-blind; the substrate-distance-2 pole isolates the
             conformal-anomaly content the substrate-distance-1 trace missed).

Per `.claude/rules/epistemic-discipline.md` §"Cross-Proxy Adjudication" requirement
(2): the verdict is OPEN. Do NOT pre-commit to either Track A or Track B. The
substitution chain Step 4 reads the direction off the canonical form. The PASS/FAIL/INFO
threshold block is symmetric across the two readings. Per `.claude/rules/v3-closure-recovery.md`
PROHIBITED_ACTIONS Class 6: do NOT alter the WZW proxy formula, the s=4 pole pin,
or the sign-reversal acceptance threshold mid-execution to convert a FAIL into a PASS.

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch  # GPU path for D_K spectral evaluation if cache SHA mismatch
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. S86 W5b §W5b-2 working-paper section (τ-flow-trace proxy + 3-sub-test
     classification + INFO verdict context):
       `sessions/archive/session-86/session-86-w5b-workingpaper.md` (lines 242-460)
       SHA: <RUNTIME-LATE-BIND from S86 W5b workingpaper file>
  2. S86 W-9 workshop §T-CR2.3 (lizzi A-T4.2 WZW proxy formula source):
       `sessions/archive/session-86/session-86-w9-workshop.md` (lines 1291-1334)
       SHA: <RUNTIME-LATE-BIND from W-9 workshop file>
  3. S86 verdict file (S86-W5B-C16-CSUB-ADMISSIBILITY canonical line):
       `computations/s86_gate_verdicts.txt`
       SHA: <RUNTIME-LATE-BIND>
  4. D_K^{≤10} spectrum cache at τ_fold = 0.190:
       `computations/s84_spectrum_cache_L12_tau019.npz`
       SHA: <CANONICAL — read from S86 close>
  5. D_K^{≤10} spectrum cache at τ ∈ {τ_fold − δ_τ, τ_fold + δ_τ} for sign-reversal
     sheet-flip evaluation (δ_τ pin in machinery block):
       `computations/s84_spectrum_cache_L10_tau<value>.npz` (re-derived if absent)
       SHA: computed-at-runtime
  6. 5-atlas regulator definitions (canonical):
       `computations/_spectral_action_regulators.py` (SCHEMATIC-tagged per
       `.claude/rules/substrate-first-canonical-sourcing.md` §iv; SCHEMATIC declared
       in convention= field of verdict line)
       SHA: <CANONICAL>
  7. (C_H, C_epsH) parity-twin pair definition (§VII.S sub-rows §VII.S.C-eta +
     §VII.S.C-theta from S86 W1a-1 perturbative-ledger immunization landing):
       `sessions/permanent-results-registry.md` §VII.S
       SHA: <RUNTIME-LATE-BIND>
  8. NCG-axiomatic conformal-anomaly kernel definition (substrate-canonical):
       `sessions/archive/session-86/session-86-w9-workshop.md` §T-CR2.3 (anchor for
       anomaly_kernel(s) integrand, the substrate-distance-2 pole isolator)
       SHA: <RUNTIME-LATE-BIND from W-9 workshop file; same SHA as input #2>
  9. Canonical-constants ledger expected sign-reversal direction:
       `computations/canonical_constants.py` (substrate-canonical entries
       relevant to S79 P1-2 W2-E sign-reversal closure rule per W5b workingpaper
       line 328)
       SHA: <CANONICAL>

Computation steps:
  Step A. Pre-registration verification (substrate-first-provenance audit):
          - Verify the WZW proxy formula `c_sub_anomaly_WZW(R) := Res[M_R(s) ·
            anomaly_kernel(s); s=4] / Res[M_R(s); s=3]` is exactly as transcribed
            from W-9 workshop §T-CR2.3 (no mid-execution alteration).
          - Verify the s=4 substrate-distance-2 pole and the s=3 substrate-distance-1
            normalization pole are pinned per the W-9 workshop source (no scheme
            substitution).

  Step B. For each regulator R in the 5-atlas family {ζ, Pauli-Villars, Mellin,
          cutoff, lattice} AND specifically for the (C_H, C_epsH) parity-twin pair
          rows of §VII.S (per the W-11 calibration corpus extension cited in
          `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT" for
          η + GV joint probe context):
          - Construct M_R(s), the regulator-R-weighted Mellin transform of
            D_K^{≤10} at τ_fold = 0.190.
          - Compute Res[M_R(s) · anomaly_kernel(s); s=4] (substrate-distance-2
            residue).
          - Compute Res[M_R(s); s=3] (substrate-distance-1 normalization residue).
          - Compute c_sub_anomaly_WZW(R) := Res[M_R(s) · anomaly_kernel(s); s=4]
            / Res[M_R(s); s=3].

  Step C. Sign-reversal sheet-flip evaluation across τ_fold:
          - For each R, compute c_sub_anomaly_WZW(R; τ_fold − δ_τ) and
            c_sub_anomaly_WZW(R; τ_fold + δ_τ) at δ_τ = 0.005 (machinery pin).
          - Compute the sign-reversal predicate per regulator:
              sign_reversal_R := sign(c_sub_anomaly_WZW(R; τ_fold − δ_τ))
                              * sign(c_sub_anomaly_WZW(R; τ_fold + δ_τ))
          - sign_reversal_R = -1 ⇒ sheet-flip CONFIRMED for regulator R (sign of
            anomaly contribution flips across τ_fold, matching the canonical
            ledger's S79 P1-2 W2-E sign-reversal closure expectation).
          - sign_reversal_R = +1 ⇒ sheet-flip ABSENT for regulator R (same sign
            on both sides of τ_fold; the τ-flow-trace proxy's negative-sign-
            both-sides finding from W5b §W5b-2 sub-test (c) is reproduced).

  Step D. Cross-regulator aggregate:
          n_pass := |{R : sign_reversal_R = -1}|
          n_atlas := 5 (5-atlas full family)
          n_parity_twin_pass := |{R ∈ {C_H, C_epsH} : sign_reversal_R = -1}|

  Step E. Regime-of-validity check (Mellin-cone substrate-distance-2 convergence):
          For each R, verify M_R(s) is analytic in a neighborhood of s=4 at
          L_max=10 (the substrate-distance-2 pole at s=4 must be inside the
          regulator's convergence cone, NOT on its boundary):
            convergence_margin_R := |s=4 − boundary_R| / |s=4|
          regime_verdict per regulator:
            VALID  if convergence_margin_R ≥ 0.10 (≥10% inside the cone)
            MARGINAL if 0.05 ≤ convergence_margin_R < 0.10
            BREAKDOWN if convergence_margin_R < 0.05
          Aggregate regime_verdict for the gate:
            VALID if all 5 regulators VALID
            MARGINAL if 1-2 regulators MARGINAL (none BREAKDOWN)
            BREAKDOWN if any regulator BREAKDOWN OR ≥3 MARGINAL.

  Step F. Cross-check (functional-pluralism comparison with τ-flow-trace proxy):
          Re-evaluate the τ-flow-trace proxy `c_sub_anomaly(τ) := d c_sub(τ)/dτ`
          per the W5b §W5b-2 formula (cite the W5b workingpaper SHA from input #1
          for the formula source) on the SAME 5-atlas + (C_H, C_epsH) per-regulator
          set. Compare per-regulator:
            agree_R := (sign_reversal_R_WZW == sign_reversal_R_τflow)
          Report n_agree := |{R : agree_R = True}|.
          - n_agree = 5 ⇒ both proxies agree across the full atlas (the cross-review
            does NOT change the C16 outcome at the proxy-aggregate level; both
            proxies extract the same conformal-anomaly content).
          - n_agree < 5 ⇒ proxies DISAGREE on at least one regulator (the WZW proxy
            extracts different anomaly content than the τ-flow-trace proxy on
            those regulators; the cross-review provides direct evidence the two
            proxies are NOT algebraically equivalent at the substrate-physics level).

  Step G. Compute closure SHA: SHA-256 of the ordered input-pin map
          {w5b_workingpaper_sha, w9_workshop_sha, s86_verdict_sha, dk_spectrum_sha,
           dk_neighborhood_sha, atlas_def_sha, vii_s_pair_sha, anomaly_kernel_sha,
           canonical_constants_sha,
           s4_pole_pin=4, s3_pole_pin=3, delta_tau_pin=0.005,
           convergence_margin_threshold=0.10, sign_reversal_predicate=multiplicative,
           level_pin=SCHEMATIC-SCHEMATIC, regulator_atlas_pin=5-atlas + C_H + C_epsH}.

Decision rule (PASS/FAIL/INFO; composite collapse per gate-verdicts.md schema-v2):
  sign_verdict       = PASS if n_pass ≥ 3 AND n_parity_twin_pass = 2
                            (≥3 of 5 atlas regulators show sheet-flip AND BOTH
                             C_H and C_epsH show sheet-flip ⇒ canonical ledger's
                             expected sign-reversal direction is structurally
                             confirmed by the WZW proxy; cross-proxy yields
                             PASS reading);
                       FAIL if n_pass ≤ 1 AND n_parity_twin_pass ≤ 1
                            (≤1 of 5 atlas regulators show sheet-flip AND ≤1 of
                             the parity-twin pair shows sheet-flip ⇒ the WZW
                             proxy reproduces the τ-flow-trace proxy's negative
                             finding; cross-proxy CONFIRMS the C16 sign-reversal
                             FAIL; Track A reading is allocated);
                       N/A in the MIDDLE band (n_pass = 2 OR n_parity_twin_pass
                            mixed) — INFO outcome via magnitude_verdict.
  magnitude_verdict  = PASS if sign_verdict = PASS AND for each R with
                            sign_reversal_R = -1, |c_sub_anomaly_WZW(R; τ_fold −
                            δ_τ) − c_sub_anomaly_WZW(R; τ_fold + δ_τ)| /
                            max(|c_sub_anomaly_WZW(R; τ_fold ± δ_τ)|) ≥ 0.10
                            (sheet-flip magnitude is structurally significant,
                            not noise);
                       INFO if sheet-flip magnitudes are 0.01-0.10 (intermediate
                            band; structurally non-zero but small);
                       FAIL otherwise.
  regime_verdict     = per Step E aggregate.

Composite collapse (per `.claude/rules/gate-verdicts.md` S87+ schema-v2):
  if regime_verdict == BREAKDOWN: composite = FAIL
  elif sign_verdict == FAIL: composite = FAIL
  elif magnitude_verdict == FAIL and regime_verdict == VALID: composite = FAIL
  elif magnitude_verdict == FAIL and regime_verdict == MARGINAL: composite = INFO
  elif magnitude_verdict == INFO: composite = INFO
  elif sign_verdict == N/A: composite = INFO
  else: composite = PASS

Verdict line append (atomic, single open("a") write, per `.claude/rules/gate-verdicts.md`):
  S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW: <PASS|FAIL|INFO> -- \\
    value=<n_pass>/<n_atlas>+twin=<n_parity_twin_pass>/2 \\
    scheme=WZW-consistency-residue-substr-d-2 \\
    convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC \\
    L_max=10 sha256=<64-char closure>

Plus dual-SHA companion comment row:
  # audit_sha256_short=<16> content_sha256_short=<16> # \\
  # S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW dual-SHA companion row

Plus S87+ schema-v2 3-tuple annotation (REQUIRED for [VERIFY] trigger):
  # sign_verdict=<PASS|FAIL|N/A> magnitude_verdict=<PASS|INFO|FAIL> \\
  # regime_verdict=<VALID|MARGINAL|BREAKDOWN> # \\
  # S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW 3-tuple annotation (S87 schema-v2)

Plus cross-proxy adjudication record row (S87 introduction; pre-registered here):
  # n_agree_with_tau_flow_trace=<int>/5 track_allocation=<A|B|OPEN> # \\
  # S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW cross-proxy adjudication

Output file targets:
  computations/s87_w9c_csub_axiom_cross_review.py
  computations/s87_w9c_csub_axiom_cross_review.npz   (5-atlas + 2-twin
                                                             c_sub_anomaly_WZW(R)
                                                             values at τ_fold ± δ_τ
                                                             + sign_reversal_R per
                                                             regulator + n_agree
                                                             with τ-flow-trace)
  computations/s87_w9c_csub_axiom_cross_review.png   (per-regulator bar plot
                                                             of c_sub_anomaly_WZW(R)
                                                             at τ_fold − δ_τ vs
                                                             τ_fold + δ_τ; sign-
                                                             reversal indicator
                                                             per row)
  computations/s87_gate_verdicts.txt                  (canonical verdict
                                                             append; do NOT touch
                                                             other lines)

GPU path: torch.linalg.eigh on RX 9070 XT for D_K^{≤10} spectrum re-derivation at
τ_fold ± δ_τ if the cached spectrum file has SHA mismatch; otherwise CPU read of
caches with OMP_NUM_THREADS=8.

Working-paper section: append to `sessions/archive/session-87/session-87-w9c-workingpaper.md`
§W9c-1 with full structural content (≥15 substantive lines; do NOT stub). Include:
  (a) Open-verdict statement (Track A vs Track B ⇒ neither pre-judged)
  (b) Substitution chain reproducing the §10 substitution chain in this plan
  (c) Per-regulator c_sub_anomaly_WZW(R) values + sign_reversal_R verdict
  (d) Cross-check comparison with τ-flow-trace proxy (n_agree value)
  (e) Track allocation (A or B or OPEN) per the verdict outcome
  (f) Substrate-framing reminder (both proxies are SUBSTRATE-IS spectral-moment
      functionals; container-thinking direction is forbidden)
  (g) Rule-anchor citations: T1-19 (this gate's structural parent),
      regulator-pin-discipline §Class-(c) PIN-DRIFT extension (W-11 calibration
      precedent for the (C_H, C_epsH) parity-twin context),
      substrate-first-canonical-sourcing §iv (SCHEMATIC declaration for
      _spectral_action_regulators.py helpers).
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (canonical; matches S86 W5b §W5b-2 evaluation) |
| `scheme` | WZW-consistency-residue-substr-d-2 (substrate-distance-2 pole at s=4 with substrate-distance-1 normalization at s=3) |
| `convention` | cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC (SCHEMATIC tag per `.claude/rules/substrate-first-canonical-sourcing.md` §iv because `_spectral_action_regulators.py` is SCHEMATIC; live-physical-regulator re-run is a separate forward question) |
| `n_eval` | 7 (5-atlas {ζ, Pauli-Villars, Mellin, cutoff, lattice} + 2-parity-twin {C_H, C_epsH}) |
| `scan_range` | τ ∈ {τ_fold − δ_τ, τ_fold, τ_fold + δ_τ} (three-point sheet-flip across the van Hove fold) |
| `step_size` | δ_τ = 0.005 (matches W5b §W5b-2 τ-flow-trace proxy step) |
| `tolerance` | RATIO sheet-flip magnitude ≥ 0.10 for PASS magnitude_verdict; convergence_margin ≥ 0.10 for VALID regime_verdict |
| `random_seed` | None (deterministic Mellin-cone residue arithmetic) |
| `GPU path` | `torch.linalg.eigh` on RX 9070 XT for D_K^{≤10} spectrum re-derivation at τ_fold ± δ_τ if cache SHA mismatch; CPU read of caches with `OMP_NUM_THREADS=8` otherwise |
| `s4_pole_pin` | 4 (substrate-distance-2 conformal-anomaly residue pole) |
| `s3_pole_pin` | 3 (substrate-distance-1 normalization residue pole) |
| `delta_tau_pin` | 0.005 (sheet-flip step across τ_fold) |
| `convergence_margin_threshold` | 0.10 (regulator-by-regulator regime-of-validity at s=4) |
| `sign_reversal_predicate` | multiplicative (sign_reversal_R = sign(τ-) × sign(τ+); −1 ⇒ flip, +1 ⇒ no flip) |
| `n_pass_pass_threshold` | ≥3 of 5 atlas regulators with sheet-flip |
| `n_parity_twin_pass_threshold` | =2 of {C_H, C_epsH} with sheet-flip (BOTH must show flip for PASS) |
| `n_pass_fail_threshold` | ≤1 of 5 atlas regulators (Track A: prior FAIL stands) |
| `n_parity_twin_fail_threshold` | ≤1 of {C_H, C_epsH} (Track A: prior FAIL stands) |
| `level_pin` | SCHEMATIC (SCHEMATIC; `_spectral_action_regulators.py` per its docstring) |
| `regulator_atlas_pin` | 5-atlas + (C_H, C_epsH) per S86 §VII.S sub-rows |
| `regulator_pin_tag` | a_2^{Mellin} (substrate-distance-1 normalization) + a_4^{Mellin} (substrate-distance-2 anomaly residue) per `.claude/rules/regulator-pin-discipline.md` |
| `w5b_workingpaper_sha` | `<RUNTIME-LATE-BIND>` from S86 W5b workingpaper file |
| `w9_workshop_sha` | `<RUNTIME-LATE-BIND>` from S86 W-9 workshop file (proxy formula source + anomaly_kernel definition) |
| `s86_verdict_sha` | `<RUNTIME-LATE-BIND>` from S86 verdict file (S86-W5B-C16-CSUB-ADMISSIBILITY canonical line) |
| `vii_s_pair_sha` | `<RUNTIME-LATE-BIND>` from `permanent-results-registry.md` §VII.S |
| `dk_spectrum_sha` | `<CANONICAL>` (read from S86 close; `s84_spectrum_cache_L12_tau019.npz`) |
| `dk_neighborhood_sha` | computed-at-runtime (cached or re-derived for τ_fold ± δ_τ) |
| `atlas_def_sha` | `<CANONICAL>` (`_spectral_action_regulators.py`) |
| `anomaly_kernel_sha` | `<RUNTIME-LATE-BIND>` from W-9 workshop §T-CR2.3 (same SHA as `w9_workshop_sha`) |
| `canonical_constants_sha` | `<CANONICAL>` (`canonical_constants.py` at S87 plan-freeze) |

PRU Class-8 status:
- 8.0/8.1 (cardinality): every parameter pinned; all 27 entries above filled.
- 8.2 (verifier-rubric pre-registration): the cross-proxy adjudication's PASS pattern set is `{n_pass ≥ 3, n_parity_twin_pass = 2}` (CONJUNCTION; both threshold predicates required for PASS); FAIL pattern set is `{n_pass ≤ 1, n_parity_twin_pass ≤ 1}` (CONJUNCTION); INFO is the disjoint complement. No "or similar" / "or equivalent" tokens that could admit unintended sub-classifications. Calibration corpus pin (per T1-19 requirement (4)): the W5b §W5b-2 τ-flow-trace proxy's 3-sub-test classification (atlas-membership PASS at sub-test (a), τ-stationarity PASS at sub-test (b), sign-reversal FAIL at sub-test (c)) — the exemplar passing-vs-failing content snippet is the W5b §W5b-2 closure verdict line + W5b workingpaper §W5b-2 line 387 sub-test (c) classification. SHA pinned at runtime.
- 8.3 (publication-precision): n_pass + n_parity_twin_pass are integer counts (no precision-comparison floor); c_sub_anomaly_WZW(R) values published at full float64 in the .npz data file; working-paper section publishes 6-sig-fig presentation precision with the .npz file as full-precision source for any downstream verifier (per `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration").

### 8. Expected output 4-tuple
`(value=<n_pass>/<n_atlas>+twin=<n_parity_twin_pass>/2, scheme=WZW-consistency-residue-substr-d-2, convention=cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC, L_max=10)`

### 9. PASS / FAIL / INFO thresholds (with tolerance rule)

- **PASS (Track B allocation: cross-proxy yields PASS → C16 promotes from INFO to ADMISSIBLE)**:
  - `sign_verdict = PASS` (n_pass ≥ 3 of 5 atlas regulators show sheet-flip AND n_parity_twin_pass = 2 of {C_H, C_epsH} both show sheet-flip)
  - AND `magnitude_verdict = PASS` (sheet-flip magnitudes structurally significant ≥ 0.10 RATIO)
  - AND `regime_verdict = VALID` (all 5 atlas regulators inside s=4 convergence cone with margin ≥ 0.10)

- **INFO (open-verdict middle band; neither track decisively allocated)**:
  - `sign_verdict = N/A` (n_pass = 2 OR n_parity_twin_pass mixed) — ambiguous proxy aggregate
  - OR `regime_verdict = MARGINAL` AND `magnitude_verdict = PASS`
  - OR `magnitude_verdict = INFO` (sheet-flip magnitudes intermediate 0.01-0.10)

- **FAIL (Track A allocation: prior FAIL stands → C16 confirmed INFO at L_max=10 axiom-side cross-review)**:
  - `sign_verdict = FAIL` (n_pass ≤ 1 of 5 atlas regulators AND n_parity_twin_pass ≤ 1 of {C_H, C_epsH}) — both proxies agree the sign-reversal sub-test FAILs
  - OR `regime_verdict = BREAKDOWN` (any regulator BREAKDOWN OR ≥3 MARGINAL — the WZW proxy is regime-blind at L_max=10)
  - OR `magnitude_verdict = FAIL` AND `regime_verdict = VALID`

Tolerance-rule class: RATIO (per `.claude/rules/gate-verdicts.md`).

The threshold band is SYMMETRIC across Track A and Track B at the structural level (the gate is OPEN-VERDICT per T1-19 (2)): PASS pattern + FAIL pattern are pre-registered as CONJUNCTIONS of independent predicates (atlas-aggregate count + parity-twin pair count); the INFO middle band absorbs the disjoint complement (intermediate counts, regime-marginal, magnitude-intermediate) without favoring either track.

### 10. Substitution chain (MANDATORY — direction claim on cross-proxy sheet-flip)

```
Definition 1: M_R(s) := regulator-R-weighted Mellin transform of D_K^{≤10}
              [substrate-canonical Mellin-cone evaluator on the Jensen-deformed
               SU(3) substrate at L_max=10; 5-atlas regulator family per
               `.claude/rules/regulator-pin-discipline.md`]

Definition 2: anomaly_kernel(s) := substrate-distance-2 NCG-axiomatic conformal-
              anomaly kernel
              [per W-9 workshop §T-CR2.3 lines 1291-1334 (lizzi A-T4.2 anchor);
               isolates the conformal-anomaly contribution at the s=4 pole versus
               the substrate-distance-1 normalization at s=3]

Definition 3: c_sub_anomaly_WZW(R) := Res[M_R(s) · anomaly_kernel(s); s=4]
                                       / Res[M_R(s); s=3]
              [WZW-consistency residue proxy at substrate-distance-2; algebraically
               distinct from the τ-flow-trace proxy (different operator, different
               pole, different physical interpretation)]

Definition 4: c_sub_anomaly(τ) := d c_sub(τ)/dτ
              [τ-flow-trace proxy per W5b §W5b-2 line 331; substrate-distance-1
               trace of the τ-derivative of the Mellin moment; W5b sub-test (c)
               returned FAIL on this proxy under the negative-sign-both-sides
               finding]

Definition 5: sign_reversal_R := sign(c_sub_anomaly_WZW(R; τ_fold − δ_τ))
                                * sign(c_sub_anomaly_WZW(R; τ_fold + δ_τ))
              [sheet-flip predicate per regulator R; −1 ⇒ flip, +1 ⇒ no flip;
               canonical-ledger expectation per S79 P1-2 W2-E sign-reversal closure
               rule cited W5b workingpaper line 328: post-fold sheet structure
               flips the sign of the anomaly term]

Definition 6: n_pass := |{R ∈ 5-atlas : sign_reversal_R = -1}|
              n_parity_twin_pass := |{R ∈ {C_H, C_epsH} : sign_reversal_R = -1}|
              [aggregate predicates feeding the gate's sign_verdict]

Step 1 (substitute Definitions 1+2+3 into Definition 5):
  sign_reversal_R = sign(Res[M_R(s) · anomaly_kernel(s); s=4]
                         / Res[M_R(s); s=3]; τ_fold − δ_τ)
                  × sign(Res[M_R(s) · anomaly_kernel(s); s=4]
                         / Res[M_R(s); s=3]; τ_fold + δ_τ)

Step 2 (factor sign[denominator] into the numerator-only sheet-flip):
  Res[M_R(s); s=3] is the substrate-distance-1 normalization; per the regulator-
  pin-discipline normalization convention `_spectral_action_regulators.py` returns
  positive Mellin-Dirichlet weights at s=3 (substrate-natural normalization on
  D_K^{≤10}; matches the canonical normalization of M_KK + Vol_SU3 spectral-density).
  Therefore sign(Res[M_R(s); s=3]) = +1 throughout τ ∈ {τ_fold − δ_τ, τ_fold + δ_τ}
  (the substrate-distance-1 normalization residue does NOT flip across τ_fold;
  only the substrate-distance-2 anomaly residue can flip; this is the structural
  distinction between the two proxies).

  Hence:
    sign_reversal_R = sign(Res[M_R(s) · anomaly_kernel(s); s=4]; τ_fold − δ_τ)
                    × sign(Res[M_R(s) · anomaly_kernel(s); s=4]; τ_fold + δ_τ)

Step 3 (simplify under the canonical-ledger sheet-flip expectation):
  Per S79 P1-2 W2-E sign-reversal closure rule (W5b workingpaper line 328): for
  substrate-admissible regulators, the conformal-anomaly contribution to c_sub
  MUST flip sign across τ_fold because the post-fold sheet structure of the
  Riemann cover (eigenvalue-spectrum reorganization at the van Hove fold τ_fold
  = 0.190, S39 transit phase transition) flips the sign of the anomaly term in
  the spectral-action a_4 coefficient.
  ⇒ Canonical expectation: sign_reversal_R = -1 for all substrate-admissible R.
  ⇒ n_pass = 5 expected if WZW proxy correctly isolates the conformal anomaly.
  ⇒ n_parity_twin_pass = 2 expected (both C_H and C_epsH show sheet-flip) if
    the (C_H, C_epsH) parity-twin pair carries the same conformal-anomaly content
    via the WZW proxy as the broader 5-atlas family.

Step 4 (read direction from canonical form — OPEN-VERDICT NOT pre-judged):
  IF n_pass ≥ 3 AND n_parity_twin_pass = 2 (PASS pattern):
    The WZW proxy yields a sheet-flip verdict CONSISTENT with the canonical
    ledger's expected sign-reversal direction. Track B allocated. Reading: the
    τ-flow-trace proxy (substrate-distance-1, mixed observable) was anomaly-
    blind; the WZW proxy (substrate-distance-2, residue-isolated) extracts the
    conformal-anomaly content the τ-flow trace missed. C16 promotes from INFO
    to ADMISSIBLE. The substrate-distance-2 pole at s=4 is the structurally
    correct anomaly isolator.

  IF n_pass ≤ 1 AND n_parity_twin_pass ≤ 1 (FAIL pattern):
    The WZW proxy ALSO fails the sign-reversal test. Both proxies agree the
    substrate-pole structure does NOT yield the canonical sign-reversal at
    τ_fold under the (C_H, C_epsH) parity-twin pair AND the broader 5-atlas
    family. Track A allocated. Reading: the C16 INFO verdict stands across
    L_max=10 axiom-side cross-review; the canonical ledger's sign-reversal
    expectation is NOT structurally supported by either proxy at this regulator
    family; further axiom-side investigation requires either (i) a third
    algebraically-distinct proxy, (ii) higher L_max convergence, or (iii) a
    different parity-twin pair (e.g., other §VII.S sub-rows).

  IF middle band (n_pass = 2 OR n_parity_twin_pass mixed; INFO):
    Open verdict; neither track decisively allocated. Posteriors near priors.
    The cross-review's structural finding is that the WZW proxy is regulator-
    family-DEPENDENT in its sheet-flip behavior; cross-proxy adjudication
    requires further refinement.

  Direction claim established WITHOUT pre-judgment: the gate's PASS direction
  is structurally pinned to n_pass ≥ 3 AND n_parity_twin_pass = 2 (the canonical-
  ledger sign-reversal expectation); the FAIL direction is pinned to n_pass ≤ 1
  AND n_parity_twin_pass ≤ 1 (the τ-flow-trace negative-sign-both-sides finding
  reproduced); the INFO middle band is the structural complement (no convention-
  shopping or threshold-loosening permits a track allocation outside this
  pre-registered pattern set).
```

### 11. What PASS / FAIL / INFO means for solution space

- **PASS (Track B: C16 promotes from INFO to ADMISSIBLE)**:
  - Pins the WZW-consistency residue proxy at substrate-distance-2 (s=4 pole) as the structurally-correct conformal-anomaly isolator on D_K^{≤10}.
  - Establishes that the τ-flow-trace proxy at substrate-distance-1 (W5b §W5b-2) is ANOMALY-BLIND on the (C_H, C_epsH) parity-twin family AND the broader 5-atlas — its sub-test (c) FAIL is a feature of the proxy, not of the substrate.
  - C_sub admissibility for Path-C r=0.0117 (W5b §W5b-2 closure context) is RECONFIRMED at the axiom-side: c_sub is a stable substrate observable; sign-reversal predicate PASSES at the structurally-correct proxy.
  - Closes the §VII.S parity-twin-pair anomaly-detection ambiguity from the W-11 calibration corpus extension (regulator-pin-discipline §"Class-(c) PIN-DRIFT" extension).
  - Forward-looking: Path-C r-class admissibility has a structurally-consistent axiom-side anchor; downstream W-3 Path-H/Path-C multi-valued landing (CF-20) inherits a stronger Path-C admissibility pin.

- **INFO (open-verdict middle band)**:
  - The WZW proxy is REGULATOR-FAMILY-DEPENDENT in its sheet-flip behavior at L_max=10. Neither Track A nor Track B decisively allocated.
  - Cross-proxy adjudication is unresolved at S87; the C16 INFO at L_max=10 is not promoted but also not consolidated as confirmed FAIL.
  - Forward gate: re-run at L_max=12 OR test a third algebraically-distinct proxy (e.g., Cheeger-Simons secondary-class isolator at substrate-distance-3) to break the regulator-family dependence.

- **FAIL (Track A: C16 confirmed INFO at L_max=10 axiom-side; prior FAIL stands)**:
  - Pins the C16 INFO verdict as CONFIRMED at L_max=10 axiom-side cross-review. Both proxies (τ-flow-trace and WZW-consistency residue) agree the sign-reversal sub-test FAILs.
  - Forces a STRUCTURAL re-examination of the canonical-ledger sign-reversal expectation: either (i) the S79 P1-2 W2-E sign-reversal closure rule does NOT apply to the (C_H, C_epsH) parity-twin pair under the §VII.S sub-row context, OR (ii) higher L_max convergence is required to resolve the sheet-flip, OR (iii) the τ_fold = 0.190 anchor needs re-examination at L_max>10.
  - Path-C r=0.0117 admissibility (W5b §W5b-2 closure) inherits the FAIL: c_sub admissibility for Path-C remains conditional pending a third-proxy resolution.
  - Closes the WZW-residue-as-anomaly-isolator hypothesis at L_max=10 for this regulator family; forward gate is the third-proxy or higher-L_max route.
  - Per the W-11 calibration corpus extension (`.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT"): future joint-probe gates targeting conformal-anomaly detection MUST use proxies with structurally-distinct algebraic content; the τ-flow-trace + WZW-residue pair has now been shown to share the same finding under this pair.

### 12. Effort estimate
~10-14h (1.0 wave equivalent). Dominated by (i) Mellin-cone substrate-distance-2 residue evaluation at s=4 across 7 regulators × 3 τ-points = 21 residue evaluations, each O(155984) eigenvalue contributions for the Mellin-Dirichlet weight construction; (ii) cross-check with τ-flow-trace proxy on the same 7-regulator set (Step F) doubles the residue evaluation count to 42 across substrate-distance-1 + substrate-distance-2 poles; (iii) regime-of-validity convergence-margin computation per regulator at s=4 requires evaluating each regulator's analytic boundary in the complex s-plane (an additional 7 boundary-locator computations). GPU path on RX 9070 XT recommended for the residue batch (~2-4h wall-clock); CPU fallback is ~10-14h with `OMP_NUM_THREADS=8`.

### 13. Substrate-framing reminder

Both proxies (τ-flow-trace `c_sub_anomaly(τ) := d c_sub(τ)/dτ` and WZW-consistency residue `c_sub_anomaly_WZW(R) := Res[M_R(s) · anomaly_kernel(s); s=4] / Res[M_R(s); s=3]`) are SUBSTRATE-IS spectral-moment functionals of D_K^{≤10} on the Jensen-deformed SU(3) substrate. Per `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space": the regulator R does NOT contain the c_sub_anomaly observable; the regulator R IS a particular Mellin-cone weighting that selects a particular spectral-moment functional from the substrate. The substrate-distance-1 vs substrate-distance-2 pole distinction is NOT a "depth into" a regulator container — it is a structural feature of the Mellin-Dirichlet expansion of the substrate's own D_K^{≤10} spectrum. The conformal-anomaly content lives in the residue STRUCTURE of M_R(s) at the substrate-distance-2 pole s=4 (per the NCG-axiomatic anomaly kernel of W-9 §T-CR2.3); the sign-reversal predicate sign_reversal_R is a SUBSTRATE-IS sheet-flip observable, NOT a regulator-bookkeeping artifact.

The cross-review's structural question — does the substrate-distance-2 WZW residue extract the same conformal-anomaly content as the substrate-distance-1 τ-flow trace — is a SUBSTRATE-PHYSICS question about the structural relationship between two distinct Mellin-pole isolators on the SAME substrate. Container-thinking direction-inversions (treating the proxies as "looking into" the substrate from different "external angles") are forbidden — the proxies ARE spectral-moment functionals on D_K, not external probes.

The (C_H, C_epsH) parity-twin pair from §VII.S is the HP^1-cohomology-content-distinct corridor (per S86 W-5 §VII.P-v2 candidate; CF-34 lands the recast). The cross-review's evaluation on this pair is the AXIOM-SIDE specialization of the W-11 η + GV joint-probe finding (per `.claude/rules/regulator-pin-discipline.md` §"Class-(c) PIN-DRIFT" extension); the WZW residue at s=4 is an even-grading observable that complements the η + GV odd-grading observables of W-11. The cross-review extends the W-11 calibration corpus from the η + GV joint probe to the c_sub conformal-anomaly axis at substrate-distance-2.

```yaml
schema_version: R3
verdict_source: computations/s87_gate_verdicts.txt
```

---

## Sub-Wave 9c → next-sub-wave Decision Point

W9c is a single-gate sub-wave (1 of CF-56's 1.0 wave-equivalent). On W9c closure (verdict line on disk + working-paper section written + cross-proxy adjudication record row appended):

- If verdict = PASS (Track B) → C16 promotes from INFO to ADMISSIBLE. Downstream consumers:
  - Path-C r-class admissibility chain (W-3 Path-H/Path-C multi-valued landing CF-20 / W9 family) inherits a stronger Path-C admissibility pin.
  - W-9 Joint F_2-Class Path-(c) Theorem CF-54 STAGE-1 entry's anchor list strengthens (the WZW proxy joins the anchor evidence for Path-C admissibility).
  - The W-11 calibration corpus extension (regulator-pin-discipline §"Class-(c) PIN-DRIFT") gains a structural confirmation: substrate-distance-2 WZW residue is the structurally-correct anomaly isolator on (C_H, C_epsH).

- If verdict = INFO → C16 INFO stands at L_max=10; neither track allocated. Forward gate options:
  - L_max=12 re-run via S87+ extended-L gate
  - Third algebraically-distinct proxy (e.g., Cheeger-Simons secondary-class isolator at substrate-distance-3)
  - Different parity-twin pair (other §VII.S sub-rows) at L_max=10

- If verdict = FAIL (Track A) → C16 INFO confirmed at L_max=10 axiom-side; prior FAIL stands. Forward gate:
  - The S79 P1-2 W2-E sign-reversal closure rule's applicability to the (C_H, C_epsH) parity-twin pair becomes a separate sub-question (potentially a forward S88+ gate testing whether the sign-reversal expectation generalizes from the broader 5-atlas to the §VII.S parity-twin sub-row family).
  - Path-C r=0.0117 admissibility remains conditional pending third-proxy resolution.

**Cross-wave dependencies introduced by W9c outputs**:
- W9c verdict is an upstream pin for W3 Path-H/Path-C multi-valued landing (CF-20) — c_sub admissibility for Path-C is a clause-(c)-supporting anchor in the joint theorem.
- W9c verdict is an upstream pin for W-7 LAYER-1-2 retroactive audit (CF-45) at the LAYER-tag for c_sub citations — the LAYER-tagging reflects whether c_sub is structurally ADMISSIBLE (Track B) or INFO-deferred (Track A or middle band).
- W9c verdict is an upstream pin for W-11 η-GV regulator-INDEPENDENCE follow-up (CF-65) on (C_H, C_epsH) — the W9c WZW proxy is the even-grading complement to the W-11 odd-grading η + GV joint probe; PASS at W9c strengthens the W-11 odd-vs-even anomaly-decoding partition.

---

## Sub-Wave 9c Machinery-Enumeration Pin (§0.11 PRDR)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness" + `.claude/templates/pru-pre-registration-template.md`:

| Gate ID | N_eval | L_max | scan_range | step_size | tolerance | scheme | convention | random_seed | GPU path | regulator_pin |
|:--------|:-------|:------|:-----------|:----------|:----------|:-------|:-----------|:------------|:---------|:--------------|
| §W9c-1 (W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW) | 7 (5-atlas + C_H + C_epsH) × 3 (τ-points) = 21 residue evals | 10 | τ ∈ {τ_fold − 0.005, τ_fold, τ_fold + 0.005}; s ∈ {3, 4} | δ_τ = 0.005 | RATIO sheet-flip≥0.10; convergence_margin≥0.10 | WZW-consistency-residue-substr-d-2 | cross-proxy-adjudication-OPEN-VERDICT-SCHEMATIC | None | torch.linalg.eigh on RX 9070 XT (cache regen) / CPU OMP=8 (cache read) | a_2^{Mellin} (s=3 normalization) + a_4^{Mellin} (s=4 anomaly residue) |

PRU-class clearance:
- **Class 8.0 / 8.1 (cardinality)**: CLEARED. All 27 machinery parameters in §7 enumerated and pinned.
- **Class 8.2 (verifier-rubric pre-registration)**: CLEARED. PASS/FAIL pattern sets are CONJUNCTIONS of independent predicates (n_pass + n_parity_twin_pass thresholds); no "or similar" / "or equivalent" ambiguity admitting unintended sub-classifications. Calibration corpus pin: W5b §W5b-2 τ-flow-trace 3-sub-test classification (atlas-membership PASS, τ-stationarity PASS, sign-reversal FAIL at sub-test (c)) per W5b workingpaper §W5b-2 lines 387-394; SHA pinned at runtime.
- **Class 8.3 (publication-precision)**: CLEARED. Integer counts (n_pass, n_parity_twin_pass) carry no precision-comparison floor; per-regulator c_sub_anomaly_WZW(R) values published at full float64 in the .npz data file with 6-sig-fig presentation precision in the working-paper section; downstream verifiers load from the .npz file (full precision) per `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration".

SOURCE-RECONCILIATION audit anticipation:
- **Class (a) PIN-TIGHT-SOURCE-LOOSE**: N/A (no canonical pre-existing for c_sub_anomaly_WZW(R); the gate produces the value as a PIN-PROMOTES-TO-CANONICAL-ON-PASS Class (e) entry per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation").
- **Class (b) PIN-LOOSE-SOURCE-TIGHT**: N/A (no upstream tight canonical drift).
- **Class (c) PIN-DRIFT-FROM-STALE-SOURCE**: Cross-checked against the W5b §W5b-2 τ-flow-trace proxy formula source (W5b workingpaper line 331); the WZW proxy formula source (W-9 workshop §T-CR2.3 lines 1291-1334) is fresh at S87 plan-freeze (post-S86 close); no stale-source drift.
- **Class (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY**: τ_fold = 0.190 is the canonical primary; δ_τ = 0.005 is a derivative (3-pt finite-difference step); the chain is verified against canonical_constants.tau_fold = 0.190.
- **Class (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS**: c_sub_anomaly_WZW(R) per-regulator values become canonical_constants.py entries on PASS verdict (post-gate update_constant hook); provenance entry "promoted_from = S87-W5B-C16-AXIOM-SIDE-CSUB-CROSS-REVIEW" per `.claude/rules/epistemic-discipline.md` §"Source Reconciliation".
- **Class (f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL**: N/A (the WZW proxy formula is a substrate-first canonical from W-9 workshop; no placeholder OOM estimates; no `O(10^?)` patterns in any pin).

SUBSTRATE-FIRST-PROVENANCE audit anticipation: SCHEMATIC declaration in convention= field per `.claude/rules/substrate-first-canonical-sourcing.md` §iv; `_spectral_action_regulators.py` is SCHEMATIC per its docstring; the cross-review's outcome holds for these schematic forms; a live-physical-regulator re-run is a separate forward question (potential S88+ gate per the §iv discipline).

---

## Sub-Wave 9c Input-SHA Ledger

| Pin name | Source path | SHA pin schedule |
|:---------|:------------|:-----------------|
| `s86_w5b_workingpaper.md` §W5b-2 (lines 242-460) — τ-flow-trace proxy formula + 3-sub-test classification + INFO verdict context | `sessions/archive/session-86/session-86-w5b-workingpaper.md` | computed-at-runtime by §W9c-1 script |
| `s86_w9_workshop.md` §T-CR2.3 (lines 1291-1334) — lizzi A-T4.2 WZW proxy formula source + anomaly_kernel definition | `sessions/archive/session-86/session-86-w9-workshop.md` | computed-at-runtime by §W9c-1 script |
| `s86_gate_verdicts.txt` — `S86-W5B-C16-CSUB-ADMISSIBILITY` canonical verdict line (the prior INFO this gate cross-reviews) | `computations/s86_gate_verdicts.txt` | computed-at-runtime by §W9c-1 script (greps for the specific upstream verdict line) |
| `s84_spectrum_cache_L12_tau019.npz` — D_K^{≤10} spectrum at τ_fold = 0.190 | `computations/s84_spectrum_cache_L12_tau019.npz` | computed-at-runtime (file-SHA) by §W9c-1 |
| `s84_spectrum_cache_L10_tau<value>.npz` (×2) — D_K^{≤10} spectrum at τ_fold − 0.005 and τ_fold + 0.005 | `computations/s84_spectrum_cache_L10_tau0185.npz` + `computations/s84_spectrum_cache_L10_tau0195.npz` | computed-at-runtime by §W9c-1 (regenerate via torch.linalg.eigh on RX 9070 XT if cache absent) |
| `_spectral_action_regulators.py` — 5-atlas regulator definitions (SCHEMATIC-tagged) | `computations/_spectral_action_regulators.py` | computed-at-runtime by §W9c-1 |
| `permanent-results-registry.md` §VII.S — (C_H, C_epsH) parity-twin pair definition (sub-rows §VII.S.C-eta + §VII.S.C-theta) | `sessions/permanent-results-registry.md` | computed-at-runtime by §W9c-1 (greps for §VII.S sub-row pre-edit state) |
| `canonical_constants.py` — substrate-canonical constants (tau_fold = 0.190, M_KK, Vol_SU3, S79 P1-2 W2-E sign-reversal closure direction) | `computations/canonical_constants.py` | computed-at-runtime by §W9c-1 (the import target) |

All 8 input pins resolve to on-disk files at S86-close per context §0 "Files-on-disk verified at S87 plan-freeze (2026-04-27)" with one expected runtime-derivation (the τ_fold ± 0.005 spectrum caches, which regenerate via torch.linalg.eigh on RX 9070 XT if absent). The `_plan_upstream_pin_validator.py` post-write check verifies the 6 file-existence pins are non-zero size; HARD-HALT on any missing file other than the runtime-derived spectrum-cache pair.

Cross-cite-only pin (NOT a runtime input, registered for traceability):
- W-9 workshop wrap-up §"Workshop Verdict" — the open-verdict framing source per `.claude/rules/epistemic-discipline.md` §"Cross-Proxy Adjudication" requirement (2). Cited for plan-author traceability; not loaded by the runtime script.

---

**End of session-87-plan-w9c.md**
