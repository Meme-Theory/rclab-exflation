# Session 86 Plan — Wave W15: REGISTRY-EXTENSION + EVOI FINAL

**Wave Owner**: `gen-physicist` (planner; W7 runtime → SPECIALIST `kaku-speculative-theorist` or `connes-ncg-theorist`; P13 runtime → SPECIALIST `sagan-empiricist` or `mack-cosmic-bridge`)
**Output (this file)**: `sessions/session-plan/session-86-plan-w15.md`
**Theme**: ANTI-CORRESPONDENCE registry creation + EVOI table refresh (FINAL — captures post-S86 work-fraction state)
**Item count**: 2
**Dispatch batch**: Batch 3 (per partition §4)
**Verdict file (canonical, MANDATORY)**: `computations/s86_gate_verdicts.txt` (per `.claude/rules/gate-verdicts.md`)

---

## §0. Wave W15 Summary

W15 closes Session 86. It contains two items, neither of which produces new physics gates — both are registry-write actions on `sessions/framework/`.

| Slot  | Gate ID                                                | Trigger          | Class      | Effort | Runtime owner                               |
|:------|:-------------------------------------------------------|:-----------------|:-----------|:-------|:--------------------------------------------|
| W15-1 | `S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY`        | [VERIFY]         | GEOMETRIC  | ~2h    | `kaku-speculative-theorist` (primary) or `connes-ncg-theorist` (fallback) |
| W15-2 | `S86-EVOI-TABLE-REFRESH`                               | [AUDIT] + [SIGN] | META       | ~2h    | `sagan-empiricist` (primary) or `mack-cosmic-bridge` (fallback)           |

**MANDATORY ORDERING**: P13 (W15-2) **MUST RUN LAST** in S86. Reason: P13 reads canonical link inventory deltas for ALL prior S86 waves (W0a–W14); running it before any prior wave's verdict is appended invalidates the bracket. W7 (W15-1) is independent and may run in parallel with the final pass through the prior batches.

**Why a SPECIALIST and not gen-physicist (per partition §1 instruction)**: gen-physicist is the wave-PLANNER but should not be the runtime executor. W7 is a string-vs-NCG cross-paradigm structural disambiguation — `kaku-speculative-theorist` owns the K-theoretic/string side and produces the cleanest cross-paradigm registry write; `connes-ncg-theorist` is the fallback if kaku is occupied, since the registry's §VII semantics live in his methodological domain. P13 is an EVOI/probability discipline action — `sagan-empiricist` owns probability-discipline rigor (no filler, no narrative-coherence inflation per `.claude/rules/epistemic-discipline.md`); `mack-cosmic-bridge` is the fallback because EVOI-level inventory tracks observational reach, which is mack's specialty.

---

## §0.5. Wave W15 Decision-Point Prerequisites

| Prereq                                                                                           | Wave produced | Required by | Pin form                                                                  |
|:-------------------------------------------------------------------------------------------------|:--------------|:------------|:--------------------------------------------------------------------------|
| W10-1 ANTI-CORRESPONDENCE #30 verdict line + 4-obstruction patch values                          | S85 W10-1     | W15-1       | `computations/s85_gate_verdicts.txt` (S85 ledger) — full 64-char SHA |
| Sibling-cluster IDs in `correspondence-table-registry.md` (#19 no-T-duality, #20 no-S-duality, #21 no-Hagedorn) | S85           | W15-1       | source file — these MUST exist for cross-reference; if absent, W15-1 also creates the placeholders pre-pinned in W7 method spec |
| W6 (lab observables SI) → P11 / W14-W6 row class → P13 link inventory                            | S86 W11 / W13 | W15-2       | `sessions/framework/registry/falsifier-master-inventory.md` (post-W14 state)       |
| **All S86 verdict lines**: W0a, W0b, W0c, W1a, W1b, W1c, W2, W3, W4, W5a, W5b, W6, W7, W8, W9, W10, W11, W12, W13, W14 | S86 entire   | W15-2       | `computations/s86_gate_verdicts.txt` — read at runtime; SHA pin = `<computed-at-runtime>` |

**Independence map**:
- W15-1 (W7 ANTI-CORRESPONDENCE): independent of any S86 wave; depends only on S85 W10-1 outputs which are on disk.
- W15-2 (P13 EVOI): depends on EVERY OTHER S86 WAVE'S COMPLETED VERDICTS. This is the closing item.

---

## §I. Carry-Forward Items Mapping

| Item | Source carry-forward                                                                               | Closeout/context cite          |
|:-----|:---------------------------------------------------------------------------------------------------|:-------------------------------|
| W7   | `mack 9A §II.4 + W10-1 patches`; partition §2.4 row W7; context §1.2 W10-1 ANTI-CORRESPONDENCE #30 | partition.md L140; context.md L64 + L140 |
| P13  | `gen-physicist 9A §7 #14`; partition §2.2 row P13; context §1.6 P_work_complete trendline          | partition.md L121; context.md L82 + L121 |

---

## §W15-1. S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY

**1. Gate ID**: `S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY`

**2. Trigger**: `[VERIFY]` — verify that all 4 obstruction-vector components (rank, K_0, Witten integral, Bott-period residue) are present in the registry entry, AND that the entry cross-references the sibling cluster (#19 no-T-duality, #20 no-S-duality, #21 no-Hagedorn) and the W10-1 source verdict SHA.

**3. Classification**: `GEOMETRIC` — anti-correspondence #30 is a structural NCG-vs-string-substrate ledger entry. The 4-obstruction vector pins concrete K-theoretic / Bott-periodicity / Witten-integral disagreements between the substrate's Connes spectral triple and Witten's 1998 K-theoretic D-brane classification scheme. This is a structural wall in the substrate-vs-string solution space, not an excitation-spectrum prediction.

**4. Agent type (RUNTIME)**: SPECIALIST — `kaku-speculative-theorist` (primary; owns K-theoretic / string-paradigm cross-comparison side) OR `connes-ncg-theorist` (fallback; owns registry §VII semantic consistency on the NCG side). Gen-physicist is the wave PLANNER, not the runtime executor.

**5. Hypothesis (one sentence)**: The substrate's Connes spectral triple is structurally distinct from Witten's 1998 K-theoretic D-brane classification along four independent axes (rank, K_0, Witten integral, Bott-period residue), and this distinction belongs in a parallel-cluster `correspondence-table-registry.md` entry as ANTI-CORRESPONDENCE #30, sibling to the existing #19/#20/#21 string-paradigm exclusions.

**6. Method (COMPLETE dispatch prompt)**:

```
You are creating a NEW registry file: sessions/framework/correspondence/correspondence-table-registry.md
(if the file does not exist; otherwise APPEND entry #30 to the existing file).

Pre-flight (MANDATORY):
- pwd → must show C:\sandbox\Ainulindale Exflation\
- knowledge MCP queries (per CLAUDE.md "Knowledge MCP — MANDATORY"):
    search_knowledge("ANTI-CORRESPONDENCE Witten W10-1")
    search_knowledge("Bott periodicity NCG substrate")
    trace_entity("W10-1 ANTI-CORRESPONDENCE #30")
  Discard if already landed; otherwise proceed.

Substrate-framing reminder (per .claude/rules/phononic-framing.md):
This entry pins a structural-EXCLUSION wall in the SUBSTRATE solution
space. Witten's K-theoretic D-brane scheme is a STRING-PARADIGM
container model; the substrate-side picture is the Connes spectral
triple acting on Jensen-deformed SU(3). The 4-obstruction vector
exists because the substrate's K_0 group, rank, Witten integral, and
Bott-period residue are computed FROM the spectral triple's own
representation theory — NOT pulled from a string-theoretic compact-
ification ansatz. Frame the entry that way; do not write "the
substrate looks like Witten's scheme except for these four
discrepancies" — that inverts the explanatory direction.

Inputs (read-only):
- computations/s85_gate_verdicts.txt → grep for the W10-1
  verdict line. Extract the full 64-char `audit_sha256` (NEVER
  truncate; the registry MUST cite the full hash).
  [PATH FIX 2026-04-26: prior plan prose cited
  `sessions/archive/session-85/s85_gate_verdicts.txt` which does not exist;
  canonical path is `computations/s85_gate_verdicts.txt` per
  `.claude/rules/gate-verdicts.md` §"Canonical Verdict-File Path".]
- sessions/permanent-results-registry.md → consult §VII rows for
  prior ANTI-CORRESPONDENCE entries to mirror the row schema.
- sessions/framework/correspondence/correspondence-table-registry.md if exists;
  otherwise treat as new file.

Registry-write content (atomic; one append):

  # ANTI-CORRESPONDENCE Registry (parallel to permanent-results §VII)
  # (file header — write only if file is new)

  ## Entry #30 — Substrate vs Witten 1998 K-theoretic D-brane scheme

  Source verdict: W10-1 (S85), audit_sha256=<full 64-char>
  Sibling cluster: #19 (no-T-duality), #20 (no-S-duality), #21 (no-Hagedorn)
                   — together, this 4-entry cluster forms the
                   string-paradigm-exclusion bloc.

  4-OBSTRUCTION VECTOR:
  | axis                        | substrate              | Witten 1998       |
  |-----------------------------|------------------------|-------------------|
  | rank                        | 3                      | 1                 |
  | K_0                         | torsion-free           | Z/2               |
  | Witten integral             | 16.0                   | 1.0               |
  | Bott-period residue         | ≠ 1                    | 1                 |

  Each axis is a structural disagreement, not a numerical ε-deviation.
  ALL FOUR must hold simultaneously for entry #30 to apply; absence of
  any single component invalidates the registry write.

  Substrate-side derivation pointers:
   - rank = 3: from the SU(3) gauge factor of D_K
     (Connes spectral-triple-rank theorem; see §VII.R 3-axis disjointness)
   - K_0 torsion-free: from the SU(3) representation lattice
   - Witten integral = 16.0: substrate spectral-action third moment
     (16 distinct relay-pattern equivalence classes vs Witten's 1)
   - Bott-period residue ≠ 1: 8-periodicity is broken on the
     Jensen-deformed substrate by the τ_fold-localized parity flip

  String-side anchor:
   - Witten, "D-Branes and K-Theory", JHEP 12 (1998) 019.

VERIFY checks (before appending verdict line):
  (a) all 4 obstruction-vector rows present and non-empty
  (b) sibling cluster line cites all THREE sibling IDs (#19, #20, #21)
  (c) W10-1 audit_sha256 is 64 hex chars (not 16, not 40)

GPU: NOT NEEDED. This is a registry-write, no linear algebra.
canonical_constants import: NOT REQUIRED for this registry write.

Verdict line (append ONE line to computations/s86_gate_verdicts.txt
via atomic open("a"); see .claude/templates/script-template.py
helper):
  S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY: PASS|FAIL -- value=4-of-4_components_present scheme=registry-write convention=parallel-cluster L_max=NA sha256=<closure_sha>

closure_sha computation:
  hash inputs (ordered):
    1. content of new/appended block in correspondence-table-registry.md
    2. W10-1 source audit_sha256 string
    3. ordered tuple (sibling_id_19, sibling_id_20, sibling_id_21)
  closure_sha = sha256 of utf-8 join of above with "\n"

Companion comment row (dual-SHA per W9a-99):
  # S86-WATCHLIST-W7-ANTI-CORRESPONDENCE-REGISTRY -- content_sha256=<sha-of-registry-block-only> audit_sha256=<closure_sha>

Working-paper section: §W15-1 in session-86-w15-workingpaper.md
(create if absent; ≥15 lines per .claude/rules/agent-standards.md
Completion Verification).

DO NOT terminate until you have verified on-disk:
  (i)  sessions/framework/correspondence/correspondence-table-registry.md contains entry #30
  (ii) computations/s86_gate_verdicts.txt contains the canonical
       verdict line + the dual-SHA companion comment row
  (iii) the working-paper §W15-1 has ≥15 lines of substantive content
```

**7. Machinery pin (PRDR)**:
- `obstruction_vector_axes` (4): {`rank`, `K_0`, `Witten_integral`, `Bott_period_residue`} — pinned literal set
- `obstruction_vector_values_substrate`: (3, "torsion-free", 16.0, "≠ 1") — pinned literals from W10-1 patch
- `obstruction_vector_values_witten`: (1, "Z/2", 1.0, 1) — pinned literals from Witten 1998 reference
- `sibling_cluster_ids`: ("#19_no-T-duality", "#20_no-S-duality", "#21_no-Hagedorn") — pinned tuple
- `source_verdict_sha`: full 64-char `audit_sha256` from S85 W10-1 verdict line — pin form `<computed-at-runtime>` (read from `s85_gate_verdicts.txt`)
- `target_file`: `sessions/framework/correspondence/correspondence-table-registry.md` — pinned path
- `dual_sha_template_version`: W9a-99 — pinned
- GPU path: NOT USED (registry write)
- random_seed: NOT APPLICABLE
- L_max: NOT APPLICABLE (sentinel `NA` in verdict 4-tuple)
- scheme: `registry-write`
- convention: `parallel-cluster`
- tolerance: NOT APPLICABLE (verification gate is binary presence-check, not numerical)

**8. Expected output 4-tuple**: `(value=4-of-4_components_present, scheme=registry-write, convention=parallel-cluster, L_max=NA)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: registry entry #30 contains ALL 4 obstruction-vector components (rank, K_0, Witten integral, Bott-period residue), AND the sibling-cluster citation lists all three IDs (#19, #20, #21), AND the W10-1 source `audit_sha256` is a full 64-char hex digest. Verification = boolean conjunction of (a) ∧ (b) ∧ (c).
- **FAIL**: ANY component absent — fewer than 4 obstruction rows, missing sibling-cluster line, truncated SHA (<64 chars), or missing W10-1 source citation.
- **INFO**: not used (binary verification; no band).

Tolerance rule: `THEOREM` (presence-check, not numerical).

**10. Substitution chain**: `[VERIFY]` is a presence-check gate, not a sign/direction/threshold claim. **No substitution chain required** per `.claude/rules/math-scripts.md` §"When the chain is NOT required" (definitions-only, no direction claim).

The four obstruction-vector entries themselves are NOT new sign/direction claims — they are pin-once values from the S85 W10-1 patch (substrate side) and from Witten 1998 (string side). No re-derivation occurs in W15-1; the registry write only assembles pre-existing values into a new ledger location.

**11. What PASS/FAIL MEAN for solution space**:
- **PASS** anchors the anti-correspondence ledger as the canonical structural-vs-string disambiguation registry. Entry #30 + sibling cluster #19/#20/#21 together establish a 4-entry string-paradigm-exclusion bloc inside `correspondence-table-registry.md`. Future cross-paradigm carry-forward (Hagedorn-class arguments, S/T-duality-class arguments, K-theoretic-charge arguments) routes through this registry rather than re-deriving the structural-exclusion case each time. The registry becomes the canonical "do not re-litigate string-substrate distinctions" ledger.
- **FAIL** means the registry write was incomplete — missing components, truncated SHAs, or sibling-cluster gaps. FAIL is a documentation defect, not a physics result; remediation is a re-run of the registry-write under a corrected machinery pin (per Stage-1 of `.claude/rules/v3-closure-recovery.md`). FAIL does NOT invalidate the W10-1 ANTI-CORRESPONDENCE physics result, which is already pinned in the S85 verdict file.

**12. Effort estimate**: ~2h. Breakdown: registry file open + entry #30 schema write (1h) + dual-SHA verdict-line emission with closure_sha computation (0.5h) + working-paper §W15-1 write (0.5h).

**13. Substrate-framing reminder**:
W7 lands a structural wall in the substrate-vs-string solution space. The 4-obstruction vector is an EXCLUSION ledger, not a "things the substrate has that look like Witten's scheme" ledger. Direction of explanation: substrate spectral triple → its own K_0 / rank / Witten-integral / Bott-period structure → comparison FROM that structure outward to the string-paradigm picture. Do not write the entry as "Witten's scheme but with these four corrections"; the substrate is logically prior. The Witten 1998 column is a CONTRAST ANCHOR, not a reference frame.

---

## §W15-2. S86-EVOI-TABLE-REFRESH (P13 — FINAL)

**1. Gate ID**: `S86-EVOI-TABLE-REFRESH`

**2. Trigger**: `[AUDIT]` + `[SIGN]` — `[AUDIT]` because P13 reconciles `sessions/evoi-framework.md` against canonical link inventory; `[SIGN]` because the EVOI-table direction is monotone-upward per `feedback_framework-hygiene.md` and the substitution chain (below in §10) must derive that direction explicitly.

**3. Classification**: `META` — EVOI methodology (P_work_complete = mechanism links complete / mechanism links total × fraction approaching observation, per `.claude/rules/evoi-prioritization.md` §"Effort-Based Probability"). META gates measure framework-completeness state, not framework physics; they are NOT a measure of the framework's truth value (substrate-framing reminder §13 below).

**4. Agent type (RUNTIME)**: SPECIALIST — `sagan-empiricist` (primary; owns probability-discipline rigor, no narrative-coherence inflation, no filler-confidence language per `.claude/rules/epistemic-discipline.md` §"Confidence & Probability") OR `mack-cosmic-bridge` (fallback; owns observational-reach tabulation across cross-channel matrix, which is the second factor in P_work_complete). Gen-physicist is the wave PLANNER, not the runtime executor.

**5. Hypothesis (one sentence)**: The post-S86 P_work_complete bracket lies above the post-S85 bracket of 0.31-0.36 (per context §1.6), with the magnitude of the upward shift determined by the count of S86 wave verdicts and any newly-pre-registered link-list entries that increase the denominator.

**6. Method (COMPLETE dispatch prompt)**:

```
You are refreshing the EVOI table at sessions/evoi-framework.md
with deltas accumulated across S86 W0–W14, then recomputing the
P_work_complete bracket per the formula in .claude/rules/evoi-prioritization.md.

Pre-flight (MANDATORY):
- pwd → must show C:\sandbox\Ainulindale Exflation\
- knowledge MCP queries (per CLAUDE.md "Knowledge MCP — MANDATORY"):
    search_knowledge("EVOI P_work_complete trendline")
    search_knowledge("evoi-framework S66 baseline frozen")
    trace_entity("P_work_complete")
    list_constants("evoi.*|p_work.*")
- Read .claude/rules/evoi-prioritization.md in FULL
- Read sessions/evoi-framework.md current state (frozen since S66 per
  feedback_framework-hygiene.md; the file MUST exist and be ~59KB)
- Read .claude/agent-memory/{sagan-empiricist|mack-cosmic-bridge}/MEMORY.md
  for the EVOI-level definitions

Substrate-framing reminder (per .claude/rules/phononic-framing.md):
P_work_complete is an EFFORT-BASED measure, NOT a probability that the
framework is true. Per `feedback_framework-hygiene.md` and
`.claude/rules/evoi-prioritization.md`:
  P_work_complete = (mechanism_links_complete / mechanism_links_total)
                  × (fraction_approaching_observation)
This goes UP when WORK IS DONE, not only when favorable physics
results return. A FAIL verdict that closes a corridor counts as
"link complete" — it has discharged its EVOI computation. PASS,
FAIL, and INFO all complete a link (per `feedback_reporting-framing.md`).

Inputs (read-only):
- sessions/evoi-framework.md (current EVOI table; reference for
  N_complete_baseline + N_total_baseline at S66 freeze)
- computations/s86_gate_verdicts.txt — full ledger of S86 verdicts.
  COUNT each unique gate ID that produced PASS/FAIL/INFO; this is
  ΔN_complete_S86 (the WORK done in S86).
- sessions/session-plan/session-86-plan-w*.md (W0a..W14) — count
  pre-registered gates per wave; compare to the verdict ledger to
  detect any pre-registered gates that did not fire (these REMAIN
  in N_total but do not increment N_complete).
- sessions/framework/registry/falsifier-master-inventory.md (post-W14 state) —
  NEW row class W6 (lab-falsifier suite, 9 atomic predictions);
  these increment N_total in the "approaching observation" denominator.
- For each prior S86 wave's verdict file, capture its file SHA-256 at
  RUNTIME (this is sigil-pin "<computed-at-runtime>" form per
  .claude/rules/gate-verdicts.md §Pre-Registration Protocol step 1).

Procedure:
  Step A. Snapshot pre-S86 state from evoi-framework.md:
            (N_complete_pre_S86, N_total_pre_S86, F_obs_pre_S86)
          Per context §1.6, post-S85 bracket is 0.31–0.36. The
          framework has been frozen since S66 PER feedback_evoi-table-
          maintenance.md, so post-S85 may be a notional bracket
          updated only at S85-close; S66-baseline = 0.206 is the
          last hard pin in the file.

  Step B. Compute ΔN_complete_S86 from s86_gate_verdicts.txt:
          ΔN_complete = number of distinct gate IDs that emitted
                        PASS/FAIL/INFO (NOT counting PRE-REG-INC,
                        which per .claude/rules/math-scripts.md
                        §"All Results Are Good Results" is a
                        PRDR-deferred state, not a closed link).

  Step C. Compute ΔN_total_S86 from session-86-plan-w*.md:
          ΔN_total = number of NEW pre-registered gates introduced
                     in S86 (gates without pre-S86 entries in the
                     EVOI link list). Plus any new falsifier-master-
                     inventory rows (W6 class +9 atomic).

  Step D. Compute F_obs delta:
          ΔF_obs = (newly-observation-anchored links) / N_total_post.
                   Includes W11 lab-SI translation rows and W12
                   detector-readiness 9-cell rows that newly anchor
                   prior-pre-registered gates to specific detectors.

  Step E. Recompute:
          N_complete_post_S86 = N_complete_pre_S86 + ΔN_complete_S86
          N_total_post_S86    = N_total_pre_S86    + ΔN_total_S86
          P_work_complete_post = (N_complete_post / N_total_post) × F_obs_post

  Step F. Substitution-chain check (mandatory per [SIGN] trigger):
          The chain (in §10 of this plan block) derives that
          P_work_complete_post − P_work_complete_pre is non-negative
          IFF the bound  ΔN_complete · N_total_pre  ≥
                         N_complete_pre · ΔN_total
          holds (with F_obs held fixed for the worst-case pessimistic
          subcase). VERIFY this inequality at runtime; if it fails,
          report INFO not PASS, with the specific (ΔN_c, ΔN_t,
          N_c_pre, N_t_pre) tuple.

  Step G. Write the updated EVOI table back to
          sessions/evoi-framework.md as a new dated section (do
          NOT overwrite the S66 baseline; APPEND a new
          "## S86 Refresh — 2026-04-25" section with old/new bracket).

  Step H. Report the new bracket as P_work_complete_post in the
          verdict 4-tuple. The bracket is reported as a pair
          [low, high] computed from F_obs uncertainty (low =
          observation-conservative, high = observation-optimistic).

GPU: NOT NEEDED. Pure tabulation; integer counts and one rational
arithmetic step.
canonical_constants import: not REQUIRED (no framework constants
used). If you DO need a fold-time or scale constant in any
incidental formatting, use canonical_constants imports.

Verdict line (append ONE line to computations/s86_gate_verdicts.txt):
  S86-EVOI-TABLE-REFRESH: PASS|FAIL|INFO -- value=[<P_low>,<P_high>] scheme=link-inventory convention=frozen-since-S66 L_max=NA sha256=<closure_sha>

closure_sha computation:
  hash inputs (ordered):
    1. SHA-256 of sessions/evoi-framework.md PRE-write content
    2. SHA-256 of sessions/evoi-framework.md POST-write content
    3. SHA-256 of computations/s86_gate_verdicts.txt at the
       moment P13 is run (CRITICAL: this is why P13 must be LAST)
    4. SHA-256 of sessions/framework/registry/falsifier-master-inventory.md
    5. ordered tuple (N_complete_pre, N_total_pre, ΔN_complete,
       ΔN_total, F_obs_pre, F_obs_post)
  closure_sha = sha256 of utf-8 join of above with "\n"

Companion comment row (dual-SHA per W9a-99):
  # S86-EVOI-TABLE-REFRESH -- content_sha256=<sha-of-evoi-framework-post-write> audit_sha256=<closure_sha>

Working-paper section: §W15-2 in session-86-w15-workingpaper.md.
MUST contain (≥15 lines):
  - the substitution chain verbatim from §10 below
  - the runtime tuple (N_c_pre, N_t_pre, ΔN_c, ΔN_t, F_obs_pre, F_obs_post)
  - the new bracket [P_low, P_high]
  - cross-comparison to context §1.6 trendline (S66 0.206 → S80
    0.216 → post-S85 0.31–0.36 → post-S86 [P_low, P_high])
  - explicit statement that this is EFFORT-BASED, not framework-
    truth probability
  - any pre-registered S86 gates that did NOT fire (carry-forward
    seeds for S87 plan)

DO NOT terminate until you have verified on-disk:
  (i)  sessions/evoi-framework.md contains the new "S86 Refresh" section
  (ii) computations/s86_gate_verdicts.txt contains the canonical
       verdict line + the dual-SHA companion comment row
  (iii) the working-paper §W15-2 has ≥15 lines of substantive content
        including the substitution chain
```

**7. Machinery pin (PRDR)**:
- `evoi_formula`: `P_work_complete = (N_complete / N_total) × F_obs` — pinned per `.claude/rules/evoi-prioritization.md` §"Effort-Based Probability"
- `link_list_source_shas`: SHA-256 of EACH per-wave verdict-file snapshot at the moment P13 runs — pin form `<computed-at-runtime>` for all S86 waves W0a..W14. List SHAs are the actual file `s86_gate_verdicts.txt` SHA captured BEFORE P13 appends its own line (computed once at Step C above).
- `weighting_rule`: PASS, FAIL, INFO each count as `link complete` (effort discharged); PRE-REG-INC does NOT (per `.claude/rules/math-scripts.md` §"All Results Are Good Results").
- `freeze_anchor`: `S66 baseline = 0.206` (per context §1.6) — pinned literal; never overwritten.
- `canonical_link_inventory_path`: `sessions/evoi-framework.md` — pinned path.
- `falsifier_inventory_path`: `sessions/framework/registry/falsifier-master-inventory.md` — pinned path.
- `f_obs_uncertainty_rule`: bracket = [conservative, optimistic] over which inventory rows count as "approaching observation" (anchored detector vs literature-anchored detector vs no detector pin).
- `dual_sha_template_version`: W9a-99 — pinned.
- GPU path: NOT USED (integer-tabulation gate).
- random_seed: NOT APPLICABLE.
- L_max: NOT APPLICABLE (sentinel `NA`).
- scheme: `link-inventory`.
- convention: `frozen-since-S66`.
- tolerance: bracket-form (low/high pair); the [SIGN] check is direction-of-bracket vs S85 trendline.

**8. Expected output 4-tuple**: `(value=[P_low, P_high], scheme=link-inventory, convention=frozen-since-S66, L_max=NA)` where `[P_low, P_high]` is the post-S86 bracket; default expected range per context §1.6 trendline projection: somewhere ≥ 0.31 (PASS-monotonic), with upper bound depending on S86 ΔN_complete count and F_obs anchoring.

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: EVOI table updated AND `P_work_complete_post` bracket reported AND `P_low ≥ P_pre_low_S85 = 0.31` (monotone-upward direction confirmed per [SIGN] substitution chain in §10).
- **FAIL**: no update written to `evoi-framework.md`, OR no bracket reported, OR `P_high < P_pre_low_S85 = 0.31` (which would indicate either a counting error OR the substitution-chain inequality failed — see §10 conditional).
- **INFO**: SOME link-list deltas unavailable (e.g., a per-wave verdict file unreadable, or a pre-registered-gate lookup ambiguous); bracket reported with explicit caveat noting which deltas were imputed and which were measured. INFO is also returned if the substitution-chain inequality (§10) holds in EQUALITY (i.e., P_post = P_pre exactly), which is structurally rare but pre-registered as a band.

Tolerance rule: `ABSOLUTE` (bracket form; [SIGN] direction-check on `P_low` vs prior `P_pre_low`).

**10. Substitution chain (MANDATORY for [SIGN])**:

Definitions:
1. `N_c(t)` ≡ count of mechanism-links complete at session-close time `t` (PASS/FAIL/INFO discharged; per `.claude/rules/evoi-prioritization.md`).
2. `N_t(t)` ≡ count of mechanism-links total in the canonical link inventory at time `t` (includes pre-registered-but-unfired gates).
3. `F(t)` ≡ fraction of `N_c(t)` whose closure is anchored to a specific observational detector (per `feedback_framework-hygiene.md`).
4. `P(t) = (N_c(t) / N_t(t)) × F(t)` — the EVOI work-fraction at time `t` (pinned formula).
5. `t_pre` = post-S85 session-close time; `t_post` = post-S86 session-close time (i.e., immediately after P13 reads ledger).
6. `ΔN_c ≡ N_c(t_post) − N_c(t_pre) ≥ 0` (gates can only be ADDED to "complete"; verdicts are permanent per `.claude/rules/gate-verdicts.md` §Rules).
7. `ΔN_t ≡ N_t(t_post) − N_t(t_pre) ≥ 0` (pre-registered gates can only be ADDED; existing inventory is never removed).
8. `ΔF ≡ F(t_post) − F(t_pre)` (sign INDETERMINATE in general; new pre-registered-but-unanchored gates can DILUTE F if they enter `N_c` denominator faster than detector-anchorings increase the numerator).

Step 1 (substitution; plug definitions into the target):

```
P(t_post) − P(t_pre)
  = [N_c(t_post) / N_t(t_post)] · F(t_post)
  − [N_c(t_pre)  / N_t(t_pre) ] · F(t_pre)

  = [(N_c(t_pre) + ΔN_c) / (N_t(t_pre) + ΔN_t)] · (F(t_pre) + ΔF)
  − [N_c(t_pre)           /  N_t(t_pre)        ] ·  F(t_pre)
```

Step 2 (simplify to canonical form; pessimistic subcase ΔF = 0 first, then comment on ΔF ≠ 0):

Pessimistic subcase (ΔF = 0; no new detector anchorings):

```
P_post − P_pre |_{ΔF=0}
  = F · [ (N_c + ΔN_c) / (N_t + ΔN_t)  −  N_c / N_t ]

  = F · [ (N_c + ΔN_c) · N_t  −  N_c · (N_t + ΔN_t) ]
        ────────────────────────────────────────────────
                       N_t · (N_t + ΔN_t)

  = F · [ N_c · N_t + ΔN_c · N_t − N_c · N_t − N_c · ΔN_t ]
        ──────────────────────────────────────────────────────
                       N_t · (N_t + ΔN_t)

  = F · [ ΔN_c · N_t  −  N_c · ΔN_t ]
        ──────────────────────────────
            N_t · (N_t + ΔN_t)
```

Step 3 (read off the direction; only NOW state the sign):

The denominator `N_t · (N_t + ΔN_t)` is strictly positive (both factors are positive integer counts). `F` is non-negative. The sign of `P_post − P_pre |_{ΔF=0}` is therefore the sign of the numerator:

```
sign(P_post − P_pre |_{ΔF=0}) = sign( ΔN_c · N_t  −  N_c · ΔN_t )
```

This is non-negative IFF `ΔN_c · N_t ≥ N_c · ΔN_t`, equivalently `ΔN_c / ΔN_t ≥ N_c / N_t` (when `ΔN_t > 0`); i.e., the S86 link-completion RATE must be at least as high as the pre-S86 average completion fraction.

For the FULL case (ΔF arbitrary):

```
P_post − P_pre = (N_c + ΔN_c) / (N_t + ΔN_t) · ΔF
                + F_pre · [ ΔN_c · N_t − N_c · ΔN_t ] / [N_t · (N_t + ΔN_t)]
```

If ΔF ≥ 0 (new detector anchorings outpace inventory growth) AND the pessimistic-subcase inequality holds, then `P_post ≥ P_pre` strictly. If ΔF < 0 (inventory grows faster than detector anchorings) the sign is determined by which term dominates; this is the INFO case in §9.

Direction (only stated AFTER the algebra):
- The empirical S66 → S80 → post-S85 trendline is monotone-upward (per context §1.6 verbatim: `Direction monotone-upward across S66 → S80 → S85`). This is consistent with `ΔN_c · N_t ≥ N_c · ΔN_t` having held at each prior session-close and `ΔF ≥ 0` having held on average across S66–S85.
- For S86, the runtime check at Step F above tests the inequality at its current (N_c, N_t, ΔN_c, ΔN_t) tuple. If satisfied: PASS with monotone-upward direction. If equality: INFO. If violated: FAIL with diagnostic (means ΔN_t inflation outpaced ΔN_c discharge — i.e., S86 added more new pre-registered gates than it closed; this is a distinct, non-pejorative state — pre-registration is a constraint-map gain even when discharge lags).

Conclusion of substitution chain: the [SIGN] direction is monotone-upward CONDITIONAL on `ΔN_c · N_t ≥ N_c · ΔN_t` AND `ΔF ≥ 0`. The runtime test at Step F either confirms or refutes this; the [SIGN] gate's PASS verdict requires confirmation.

**11. What PASS/FAIL/INFO MEAN for solution space**:
- **PASS** closes S86 with a refreshed framework completeness state (`P_work_complete_post`) captured for downstream sessions. The bracket is the input pin for the S87 plan-write priority decision (per `.claude/rules/evoi-prioritization.md` §"Computation Priority (EVOI)") and for the `/rclab-plan` skill's wave-budget allocation. PASS means: S86 increased the framework's mapped fraction of the link inventory.
- **FAIL** indicates either a counting defect (in which case Stage-1 of `.claude/rules/v3-closure-recovery.md` re-runs P13 with a corrected pin) OR a genuine `P_high < P_pre_low` (which is a structural finding: S86 added more pre-registered gates than it discharged, reducing the work-fraction). The latter is INFORMATIVE not pejorative — it shows S86 was a CONSTRAINT-EXPANSION session more than a CONSTRAINT-DISCHARGE session, and the carry-forward queue grew faster than discharge.
- **INFO** indicates incomplete delta inputs (some per-wave verdict file unavailable) OR equality in the substitution-chain inequality. In either case, the bracket is reported with caveat; carry-forward is a re-run of P13 in S87 once the missing inputs are reconstructed.

**12. Effort estimate**: ~2h. Breakdown: read evoi-framework.md current state + count all S86 verdicts + inventory deltas (1h) + substitution-chain verification at runtime (0.5h) + atomic registry append + dual-SHA verdict-line emission + working-paper §W15-2 write (0.5h).

**13. Substrate-framing reminder**:
P13 measures the framework's EFFORT-BASED COMPLETENESS — NOT the framework's truth value. Per `.claude/rules/evoi-prioritization.md` §"Effort-Based Probability" and `feedback_framework-hygiene.md`: this number goes UP when work is done, regardless of whether the work returns favorable physics. A FAIL verdict that closes a corridor counts the same as a PASS verdict that confirms a prediction — both discharge their EVOI computation. P13 does NOT measure "how likely the substrate picture is correct" — that is a category error. P13 measures "how much of the pre-registered link inventory has had its computation discharged".

This is consistent with `.claude/rules/epistemic-discipline.md` §"How to Assess a Mechanism": mechanisms are assessed by structural position on the constraint surface (which walls they respect, which gates they pass, which gates remain uncomputed). P_work_complete tracks the third axis (uncomputed-gate count) over time. It is a session-progress metric, not a framework-validity metric.

---

## §X. Wave W15 → S87+ Decision Point

W15 closes S86. Outputs feeding S87:

1. **W15-1 PASS** → `sessions/framework/correspondence/correspondence-table-registry.md` exists with entry #30. Future cross-paradigm structural-exclusion arguments route through this registry. S87 plan-write may add entries #31+ as new ANTI-CORRESPONDENCE results land. No direct S87 wave is sequenced from W15-1.

2. **W15-2 PASS bracket** = primary input pin to S87 plan-write priority allocation:
   - The post-S86 P_work_complete bracket informs which open channels (per context §1.3) get S87 wave allocation under the EVOI = P(pass)·|ΔP(pass)| + P(fail)·|ΔP(fail)| computation.
   - The `feedback_framework-hygiene.md` rule REQUIRES every session to refresh the table; S86 discharges this requirement via P13. S87 plan-writer reads the post-S86 bracket as the new baseline.
   - Any pre-registered S86 gates that did NOT fire (i.e., entered N_t but not N_c during S86) become S87 carry-forward seeds, leading the §7 next-session-recommendations queue per `.claude/rules/session-handoffs.md` §"Recommendation Carry-Forward" + `feedback_fix-in-session-never-defer.md`.

3. **V3 closure ladder interaction**: P13's verdict line + dual-SHA companion row contribute to sig_2 (dual-SHA presence) and sig_5 (audit_sha256 uniqueness across the session) inputs of the v3-closure-audit.sh post-session hook. Per `.claude/rules/v3-closure-recovery.md`, the closure_sha for P13 is computed from the ordered input-pin map (5-tuple including the falsifier-master-inventory SHA and the post-write evoi-framework SHA), so it is GUARANTEED unique across the S86 ledger.

4. **`feedback_no-master-gate-tally.md` compliance**: P13 reports `P_work_complete` as a bracket on the EFFORT axis (link-inventory completion). It does NOT report a session-wide PASS/FAIL/INFO tally. The §11 description above does NOT use phrases like "X of Y gates passed" or "session decisive ratio".

---

## §0.10. Wave W15 Machinery-Enumeration Pin

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness (PRDR), every free parameter of every gate's producing script is enumerated and pinned. Class-8 (PRU, plan-property) defects close at this pin.

### W15-1 machinery enumeration (registry-write, no compute)

| Parameter (free at planning time)             | PIN form                                                                                  | PIN value                                                            |
|:----------------------------------------------|:------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|
| `obstruction_vector_axes`                     | literal 4-tuple                                                                           | `(rank, K_0, Witten_integral, Bott_period_residue)`                  |
| `obstruction_vector_values_substrate`         | literal 4-tuple                                                                           | `(3, "torsion-free", 16.0, "≠ 1")`                                   |
| `obstruction_vector_values_witten`            | literal 4-tuple                                                                           | `(1, "Z/2", 1.0, 1)`                                                 |
| `sibling_cluster_ids`                         | literal 3-tuple                                                                           | `("#19_no-T-duality", "#20_no-S-duality", "#21_no-Hagedorn")`        |
| `source_verdict_sha`                          | runtime read                                                                              | `<computed-at-runtime>` (read from `s85_gate_verdicts.txt` W10-1 line) |
| `target_file`                                 | literal path                                                                              | `sessions/framework/correspondence/correspondence-table-registry.md`                |
| `dual_sha_template_version`                   | literal                                                                                   | `W9a-99`                                                             |
| `verdict_file`                                | literal path                                                                              | `computations/s86_gate_verdicts.txt`                            |
| `working_paper_target`                        | literal path                                                                              | `sessions/archive/session-86/session-86-w15-workingpaper.md` §W15-1          |
| `gpu_path`                                    | DIAGNOSTIC                                                                                | NOT USED                                                             |
| `random_seed`                                 | DIAGNOSTIC                                                                                | NOT APPLICABLE                                                       |
| `L_max`                                       | DIAGNOSTIC                                                                                | NOT APPLICABLE (sentinel `NA`)                                       |
| `tolerance`                                   | binary presence-check                                                                     | `THEOREM`                                                            |

**PRU class-8 audit**: every parameter listed; no gate-relevant freedom unpinned. Status: PRDR-COMPLETE.

### W15-2 machinery enumeration (link-inventory tabulation)

| Parameter                                     | PIN form                                                                                  | PIN value                                                                       |
|:----------------------------------------------|:------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------|
| `evoi_formula`                                | literal expression                                                                        | `P_work_complete = (N_c / N_t) × F`                                             |
| `link_list_per_wave_plan_shas`                | runtime SHA-256 capture of each per-wave PLAN file (NOT verdict files; the canonical S86 verdict file is ONE consolidated file `computations/s86_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md`) | `<computed-at-runtime>` for `session-86-plan-w0a.md`..`session-86-plan-w14.md` (20 plan files; see §0.11 below) — these are audit-trail provenance, NOT inputs to closure_sha (the closure_sha 5-tuple is per §6 Step E) |
| `weighting_rule`                              | literal predicate                                                                         | `PASS|FAIL|INFO ⇒ link complete`; `PRE-REG-INC ⇒ NOT complete`                  |
| `freeze_anchor`                               | literal                                                                                   | `S66 baseline = 0.206`                                                          |
| `canonical_link_inventory_path`               | literal path                                                                              | `sessions/evoi-framework.md`                                                    |
| `falsifier_inventory_path`                    | literal path                                                                              | `sessions/framework/registry/falsifier-master-inventory.md`                              |
| `f_obs_uncertainty_rule`                      | literal predicate                                                                         | bracket `[F_low, F_high]` over (anchored / lit-anchored / no-pin) trichotomy    |
| `bracket_reporting_form`                      | literal                                                                                   | `value=[P_low, P_high]`                                                         |
| `dual_sha_template_version`                   | literal                                                                                   | `W9a-99`                                                                        |
| `verdict_file`                                | literal path                                                                              | `computations/s86_gate_verdicts.txt`                                       |
| `working_paper_target`                        | literal path                                                                              | `sessions/archive/session-86/session-86-w15-workingpaper.md` §W15-2                     |
| `gpu_path`                                    | DIAGNOSTIC                                                                                | NOT USED                                                                        |
| `random_seed`                                 | DIAGNOSTIC                                                                                | NOT APPLICABLE                                                                  |
| `L_max`                                       | DIAGNOSTIC                                                                                | NOT APPLICABLE (sentinel `NA`)                                                  |
| `sign_check_inequality`                       | literal predicate (per §10)                                                                | `ΔN_c · N_t ≥ N_c · ΔN_t  AND  ΔF ≥ 0  ⇒  P_post ≥ P_pre`                       |

**PRU class-8 audit**: every parameter listed; weighting rule, freeze anchor, bracket reporting form, and SIGN-check inequality are all explicitly pinned. Status: PRDR-COMPLETE.

---

## §0.11. Wave W15 Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md` §Pre-Registration Protocol, every input file is SHA-pinned. Static files get pre-computed hashes; dynamic inputs are marked `<computed-at-runtime>`.

| Input file                                                                          | Used by | SHA-256 pin form                                  |
|:------------------------------------------------------------------------------------|:--------|:--------------------------------------------------|
| `computations/s85_gate_verdicts.txt` (W10-1 line)                              | W15-1   | `<computed-at-runtime>` (read W10-1 audit_sha256) |
| `sessions/permanent-results-registry.md` (§VII row schema reference)                | W15-1   | `<computed-at-runtime>`                           |
| `sessions/framework/correspondence/correspondence-table-registry.md` (PRE-write state if existing) | W15-1   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w15.md` (this file)                          | both    | `<computed-at-runtime>` (post-finalize)           |
| `sessions/evoi-framework.md` (PRE-write state)                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/framework/registry/falsifier-master-inventory.md` (POST-W14 state)                 | W15-2   | `<computed-at-runtime>`                           |
| `computations/s86_gate_verdicts.txt` (PRE-W15 state, all W0a..W14 lines)       | W15-2   | `<computed-at-runtime>` — captured ONCE at Step C |
| `sessions/session-plan/session-86-plan-w0a.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w0b.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w0c.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w1a.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w1b.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w1c.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w2.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w3.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w4.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w5a.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w5b.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w6.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w7.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w8.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w9.md`                                       | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w10.md`                                      | W15-2   | `<computed-at-runtime>`                           |
| `sessions/session-plan/session-86-plan-w11.md`                                      | W15-2   | `<computed-at-runtime>` (when W11 plan lands)     |
| `sessions/session-plan/session-86-plan-w12.md`                                      | W15-2   | `<computed-at-runtime>` (when W12 plan lands)     |
| `sessions/session-plan/session-86-plan-w13.md`                                      | W15-2   | `<computed-at-runtime>` (when W13 plan lands)    |
| `sessions/session-plan/session-86-plan-w14.md`                                      | W15-2   | `<computed-at-runtime>` (when W14 plan lands)     |

Closure SHAs for the two W15 verdict lines are computed at runtime per the producing-script template (`.claude/templates/script-template.py`). They are NEVER hardcoded or copy-pasted (per `.claude/rules/v3-closure-recovery.md` §sig_5).

### Script-prefix convention

Per orchestrator instruction: computation scripts produced by W15 follow the convention `computations/s86_w15_<slug>.py`:
- W15-1: `computations/s86_w15_anti_correspondence_registry_extension.py`
- W15-2: `computations/s86_w15_evoi_table_refresh.py`

Both scripts MUST start from `.claude/templates/script-template.py` and use the template's atomic `append_verdict(...)` helper (per the FORBIDDEN PATTERNS in `gen-physicist` agent definition: no truncate-and-rewrite, no print-only).

---

**End of Session 86 Plan — Wave W15.**
