# Session 86 Plan — Wave W4: BRANCH-IV / SECTOR-2 / cutoff_sqrt adjudication

**Owner**: `transit-dynamics-theorist`
**Wave size**: 3 items (P4, P5, C28)
**Effort estimate (combined)**: 6-8 hours; P4 + P5 ~2-3 hours each; C28 4-6 hours (extends from S85 workshop file)
**Theme**: Settle 2B path-(c) commit (BRANCH-IV) + 2A SECTOR-2 split (Mellin-kernel K-invariant) + W-4 cutoff_sqrt closure. The wave anchors the substrate's BRANCH-IV transit pathway through the van-Hove fold, lifts SECTOR-2's substrate-distance-1 pin, and converts the S85 workshop verdict into a registry-canonical adjudication outcome.

**Substrate-framing reminder for whole wave**: BRANCH-IV is the substrate's transit pathway through the van-Hove fold at τ_fold = 0.190; the eigenvalue spectrum of D_K reorganizes at the fold and the GGE relic is the substrate's residual coherence pattern. R_JK and ξ_E_GGE^{−1} are spectral diagnostics OF the substrate (functionals on the D_K spectrum), not external probes. The Mellin-kernel pole structure at pivot is a GEOMETRIC property of the regulator class. The cutoff_sqrt adjudication decides regulator-atlas cardinality — i.e., whether the substrate's spectral-action moments admit one structural family or two. State each gate IS-language (the substrate IS the spectral content; the regulator atlas IS the way the spectral content is summed), not IN-language (no objects "live in" a pre-existing regulator space).

---

## §0. Wave W4 Summary

| # | Gate ID | Type | Trigger | Owner subagent | Effort |
|:--|:--------|:-----|:--------|:---------------|:-------|
| W4-1 | `S86-BRANCH-IV-FORMULATION-COMMIT` (P4) | PHONONIC | [VERIFY] | `transit-dynamics-theorist` (primary) + `volovik-superfluid-universe-theorist` (cross-cite for ξ_E_GGE^{−1} 3He-B parent → child inheritance) | 1 wave (~2-3h) |
| W4-2 | `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT` (P5) | GEOMETRIC | [VERIFY-THEOREM] | `lizzi-spectral-functional-theorist` (primary; Mellin-kernel pole structure is regulator-class geometry) + `connes-ncg-theorist` (cross-cite, NCG sourcing of Mellin-kernel residue at pivot) | 1 wave (~2-3h) |
| W4-3 | `S86-W-4-CUTOFF-SQRT-ADJUDICATION` (C28, running into S86) | META | [AUDIT] | `connes-ncg-theorist` (primary, R3 closer of S85 workshop) + `lizzi-spectral-functional-theorist` (cross-cite, R2 emergence + 3-gate refinement) | 4-6h |

**S87+ deferral note**: C45 (`S86-SIXTH-REGULATOR-SYNTHESIS`, lizzi S-7 §V.9) is conditional on C28 closing; partition manifest §2 already defers C45 to S87 unless C28 verdict is STRUCTURALLY-EXCLUDED. The S85 workshop converged on REQUIRES-S86-GATE (joint 3-gate adjudication at GATE A L_max-finiteness + GATE B kernel-admissibility + GATE C S82-applicability), so C45 stays S87-deferred per the workshop pre-commitment unless C28's S86 instantiation flips outcome.

---

## §0.5. Wave W4 Decision-Point Prerequisites

**MUST PRECEDE W4 (hard upstream pins)**:

| Prereq wave | Prereq item | Why W4 needs it |
|:------------|:------------|:----------------|
| W0a | R3 `S86-CUTOFF-AXIS-YAML-PIN` (`cutoff_axis: spectral \| coherence \| both` field on every gate block invoking a cutoff) | C28's "regulator atlas membership" question and P5's "Mellin-kernel pole at pivot" both invoke the cutoff axis. Without R3 the gate block is PRU-vulnerable (Class 8) and W4 verdict lines would float at execution time per the S78 W1-B / W2-C / W3-L pattern flagged in `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness. |
| W0b | R8 `S86-PRR-THREE-LAYER-ADJUDICATION` (methodology entry generalizing three-layer parameter / experimental-Fisher / substrate-marginalized framework) | C28's joint 3-gate outcome rule is itself a three-layer adjudication artifact (combinatorial / admissibility / kernel-routing per S85 lizzi R3). R8 entry must exist BEFORE C28 writes `sessions/framework/registry/cutoff-sqrt-adjudication.md` so the registry write inherits the canonical methodology vocabulary. |

**W4 → DOWNSTREAM (W4 outputs gate later waves)**:

| W4 item | Downstream wave | Downstream item | Reason for hard dependency |
|:--------|:----------------|:----------------|:---------------------------|
| P4 (`ξ_E_GGE^{−1}` distance-1 spectral diagnostic landed) | W5a | P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` | gen-physicist 9A §3.6: Sector-1 ξ²(0) IC sources from ξ_E_GGE^{−1} pin. P3 cannot integrate (ε, η, α_s, ξ²) ODE from N=0 fold IC until ξ²(0) is sourced from a registry-pinned diagnostic. |
| C28 (cutoff_sqrt verdict captured) | W6 (C2 perturbative-immunization umbrella corollaries beyond C-η/C-θ); W15 (potential C45 S87 trigger) | atlas-cardinality decision; if STRUCTURALLY-EXCLUDED: S86-S87 adjudication contracts to 4-regulator F_4 ∪ {anomaly}; if GENUINELY-PHYSICAL: 5-regulator atlas with two physical sub-families becomes structural TWO-CLASS THEOREM stronger than S67 FRUSTRATION-TRIANGLE; if REQUIRES-S86-GATE (S85 converged outcome): defer to S86 numerical gate executions of GATE A + GATE B + GATE C. |

**Independence within wave**: P4 and P5 independent at plan-write and at compute time (different specialists, different framework files, different canonical-constants entries); C28 independent of both at compute time but classified META at the wave level because its outcome cascades to atlas cardinality.

---

## §I. Carry-Forward Items Mapping (3 rows)

| W4 # | Carry-forward source | Verbatim source citation | Wave assignment |
|:-----|:---------------------|:-------------------------|:-----------------|
| W4-1 (P4) | partition §1 W4 item 1; context file §2.2 row P4 | gen-physicist 9A §4.6 + lizzi 9A §2.2 | "Retire R_JE; land both R_JK (K-functional, distance-2 tag) AND ξ_E_GGE^{−1} (s=−1 spectral diagnostic, distance-1 tag) per 2B path-(c) commit" |
| W4-2 (P5) | partition §1 W4 item 2; context file §2.2 row P5 | gen-physicist 9A §4.5b | "Substrate Mellin-kernel pole structure at pivot independent of SR flow; pin K-invariant as substrate-distance-1 quantity" |
| W4-3 (C28) | partition §1 W4 item 3; context file §2.6 row C28 | gen-physicist S-7 §V.22 + lizzi S-7 §IV.3 (CF V.2 + V.3 pre-registered) | "Complete connes × lizzi 3-round workshop on cutoff_sqrt status; outcome decides whether atlas is 4-regulator or 5-regulator with two physical sub-families" — S85 workshop file `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` confirms converged R3 outcome = REQUIRES-S86-GATE with 3-gate joint adjudication |

All three items appear in exactly one wave; no overlap with other W-prefixed waves. The 3-row count is verified against partition §3 wave-sum row: `W4: P4, P5, C28 = 3`.

---

## §W4-1. S86-BRANCH-IV-FORMULATION-COMMIT (P4)

### 1. Gate ID
`S86-BRANCH-IV-FORMULATION-COMMIT`

### 2. Trigger
`[VERIFY]` — the commit is a registry-write operation that must be quantitatively verified via Python before commit: every promised file edit (3 distinct edits) must exist with non-stub content; every promised canonical-constants entry (2 NEW: `R_JK`, `xi_E_GGE_inv`) must register WITH provenance; the verification script must read both targets back and confirm presence + value + source-cite.

### 3. Classification
`PHONONIC` — BRANCH-IV is the substrate's transit pathway through the van-Hove fold (τ_fold = 0.190). R_JK is the K-functional (distance-2 tag) computed from D_K spectral moments. ξ_E_GGE^{−1} is the s=−1 spectral diagnostic at distance-1 — a functional on the GGE relic spectrum that is intrinsic to substrate excitations, not an external probe. Per `.claude/rules/phononic-framing.md`: the GGE relic IS the substrate's post-transit residual coherence pattern (the substrate IS spectral content; ξ_E_GGE^{−1} IS one moment of that content).

### 4. Agent type assignment + rationale
**Primary runtime agent**: `transit-dynamics-theorist` (BRANCH-IV is the substrate transit pathway through the fold; this is the specialist's home domain — Bogoliubov coefficients, mode equations in time-dependent backgrounds, GGE formation post-quench). Per partition §1 W4 owner assignment, the wave is owned by `transit-dynamics-theorist`. The planner-runtime separation is honored: the planner is also `transit-dynamics-theorist` but the runtime agent is a fresh dispatch (different conversation; not the planner instance).

**Cross-cite specialist**: `volovik-superfluid-universe-theorist` — required for the ξ_E_GGE^{−1} provenance row in canonical_constants.py: 3He-B parent → fabric child inheritance (per `project_3heb-inheritance.md` user-memory). The s=−1 spectral diagnostic on the GGE relic in the substrate has its observational template in 3He-B coherence-length spectroscopy. Cross-cite in the canonical_constants.py docstring; not a separate dispatch.

**NOT gen-physicist** per the partition manifest constraint that wave-specific specialists succeed where gen-physicist breadth-coordinator stalls on dense waves (S84 lesson).

### 5. Hypothesis (one sentence)
The BRANCH-IV path-(c) 2B commit canonicalizes the substrate transit pathway with R_JE retired in favor of two distance-tagged spectral diagnostics: R_JK (K-functional at distance-2) and ξ_E_GGE^{−1} (s=−1 GGE coherence-length inverse at distance-1).

### 6. Method — COMPLETE dispatch prompt

```
You are the runtime `transit-dynamics-theorist` agent dispatched for S86-W4-1
gate `S86-BRANCH-IV-FORMULATION-COMMIT` (P4). This is a [VERIFY] commit-write
gate. Your job is to land 2B path-(c) BRANCH-IV in the framework registry +
canonical constants module + write a verification script that reads the
landings back and emits a verdict line.

PRE-COMPUTE QUERIES (mandatory per CLAUDE.md "Knowledge MCP — MANDATORY"):
  mcp__knowledge__search_knowledge("BRANCH-IV R_JE R_JK xi_E_GGE")
  mcp__knowledge__search_knowledge("3HeB inheritance distance-1 distance-2")
  mcp__knowledge__list_constants("xi_|R_J")    # check if either exists already
  mcp__knowledge__trace_entity("BRANCH-IV-FORMULATION")
Confirm: (a) no prior canonical entry exists for R_JK or xi_E_GGE_inv (would
indicate name collision); (b) R_JE retirement is consistent with W3-3 / W3-4 /
W3-5 PASSes from S85 (cite SHA from computations/s85_gate_verdicts.txt).

STEP 1 — Verify framework file existence + create if absent:
  Path: `sessions/framework/registry/branch-iv-canonical.md`
  If absent, create with header: "# BRANCH-IV Canonical Formulation (S86 P4 commit)"
  + sections: "## R_JE Retirement", "## R_JK (K-functional, distance-2)",
              "## ξ_E_GGE^{−1} (s=−1 spectral diagnostic, distance-1)",
              "## Provenance + cross-cite ledger"
  If present, append a new section "## S86 P4 Commit (2B path-(c))" preserving
  prior content; do NOT overwrite.

STEP 2 — Write the three substantive sections:

  (a) R_JE Retirement note. Cite W3-3, W3-4, W3-5 PASSes from S85
      (audit_sha256 from `computations/s85_gate_verdicts.txt`,
      look for `W3-3:`, `W3-4:`, `W3-5:` prefixed verdict lines; record
      first 16 hex chars + filename + line number for each).
      Substrate language: R_JE was the prior single-distance-tag formulation;
      the 2B path-(c) audit (gen-physicist 9A §4.6 + lizzi 9A §2.2) showed
      single-name conflation between distance-1 and distance-2 tags. Two
      tags REPLACE the one — this IS canonical splitting in the substrate
      spectral-functional ledger.

  (b) R_JK landing as distance-2 K-functional. Formula:
      R_JK[D_K] := Tr_F( χ_K(D_K) · D_K^{-2} ) where χ_K is the K-functional
      character associated with the corridor at K = K_corridor (per W12-2
      8-K-atom disambiguation R5 from W0a). Distance-2 tag = the operator
      enters the spectral-action ledger at the second moment a_2 (Newton's
      constant slot). Cite gen-physicist 9A §4.6 substitution chain.

  (c) ξ_E_GGE^{−1} landing as distance-1 s=−1 spectral diagnostic. Formula:
      ξ_E_GGE^{−1} := lim_{s → −1} ζ_{D_K^{(GGE)}}(s) where D_K^{(GGE)} is
      the post-fold GGE-restricted Dirac operator (D_K projected to the
      59.8-pair Parker production sector per S38 GGE permanence theorem).
      Distance-1 tag = appears at first non-trivial Mellin-strip residue
      below s=0. Provenance: 3He-B coherence-length-inverse template
      (Volovik QFL fig. 5.3) — parent→child inheritance per
      `project_3heb-inheritance.md`.

STEP 3 — canonical_constants.py registration:
  from canonical_constants import *      # confirm import works
  Append two NEW canonical entries (use `update_constant` MCP first to ensure
  no collision):

  R_JK = <numerical value to be computed in STEP 4>     # K-functional at K_corridor
  # Provenance: S86-W4-1 P4; gen-physicist 9A §4.6; substrate distance-2 tag
  xi_E_GGE_inv = <numerical value to be computed in STEP 4>   # s=-1 spectral diagnostic
  # Provenance: S86-W4-1 P4; lizzi 9A §2.2; 3He-B parent inheritance per
  # project_3heb-inheritance.md; substrate distance-1 tag

STEP 4 — Write `computations/s86_w4_p4_branch_iv_commit.py`:
  from canonical_constants import *
  Compute R_JK from D_K spectral cache at L_max=10 (load from existing cache
  `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz`, verify SHA against
  knowledge MCP `get_constant('M_KK')` provenance chain).

  GPU PATH MANDATORY (per `feedback_compute-environment.md` + CLAUDE.md
  math-scripts.md): the D_K spectral cache load + Mellin functional eval is
  155984 x 155984 effective dimension; use:
       import torch
       D_K_eigs = torch.from_numpy(np.load(cache_path)['eigenvalues']).to('cuda')
  with explicit `torch.linalg.eigh` if a re-diagonalization is needed
  (it should not be — load cached eigenvalues). For Mellin-strip residue
  extraction at s=−1, use `torch.special.gammaln` for Γ(s) at s=−1+ε
  with analytic continuation per the Mellin-Barnes residue convention.

  CPU FALLBACK (if torch.cuda unavailable):
       import os
       os.environ.setdefault('OMP_NUM_THREADS', '8')
       import numpy as np   # only AFTER thread cap

  Verification block (first 20 lines of stdout per `.claude/rules/gate-verdicts.md`):
    log SHA-256 of:
      - branch-iv-canonical.md (after edits)
      - canonical_constants.py (after edits)
      - computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz
      - computations/s85_gate_verdicts.txt (for W3-3/4/5 cite SHAs)
      - canonical_constants.py M_KK + tau_fold + Vol_SU3 import line SHAs

  Computation:
    R_JK_value = compute_K_functional(D_K_eigs, K_corridor=K_corridor)
    xi_E_GGE_inv_value = compute_s_minus_1_residue(D_K_eigs_GGE_projected)

  Then update canonical_constants.py via the update_constant MCP with
  provenance lines; re-import to verify load.

STEP 5 — Cross-checks (5 mandatory; PASS iff all 5):
  CC-1: R_JK has units of M_KK^{-2} (Newton-constant slot). Verify by
        dimensional analysis trace + numerical rescaling under M_KK →
        2·M_KK; ratio must equal 1/4 (factor M_KK^{-2}).
  CC-2: xi_E_GGE_inv has units of M_KK (inverse coherence length).
        Verify by M_KK rescaling; ratio must equal 2 (factor M_KK^{+1}).
  CC-3: branch-iv-canonical.md contains the substring "R_JE retired" AND
        "R_JK" AND "xi_E_GGE_inv" (verify via grep tool, NOT eyeball).
  CC-4: canonical_constants.py contains BOTH `R_JK = ` and
        `xi_E_GGE_inv = ` lines + provenance comment.
  CC-5: Re-import `from canonical_constants import *` succeeds; both
        names accessible in module namespace; values match what was
        written.

STEP 6 — Verdict line append to `computations/s86_gate_verdicts.txt`
   (canonical path per `.claude/rules/gate-verdicts.md`):

  S86-BRANCH-IV-FORMULATION-COMMIT|PASS|R_JE_retired+R_JK_landed+xi_E_GGE_inv_landed|branch-iv-canonical|2B-path-c|N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
  # audit_sha256_short=<16-hex>

  PASS iff all 5 CC pass + all 3 file edits present + both canonical entries
  registered with provenance.
  FAIL iff any element absent (R_JE not retired in branch-iv-canonical.md,
  OR R_JK formula absent, OR xi_E_GGE_inv formula absent, OR canonical
  registration missing, OR re-import fails).

  Exit code 0 regardless (per `.claude/rules/math-scripts.md` §Exit Codes).
```

### 7. Machinery pin (PRDR — every free parameter pinned)

| Pin | Value | Source / SHA |
|:----|:------|:-------------|
| Framework file path | `sessions/framework/registry/branch-iv-canonical.md` | partition §1 W4 P4 + this plan |
| Canonical constants file path | `computations/canonical_constants.py` | EXISTS 86,443 B at 2026-04-24 per context §0 |
| Verification script path | `computations/s86_w4_p4_branch_iv_commit.py` | per script-prefix convention §6.5 |
| `R_JK` canonical name | `R_JK` (NOT `R_JE`, NOT `R_JK_corridor`) | gen-physicist 9A §4.6 |
| `xi_E_GGE_inv` canonical name | `xi_E_GGE_inv` (Python-identifier-safe form of ξ_E_GGE^{−1}) | lizzi 9A §2.2 |
| K_corridor source | `K_corridor` from R5 K-disambiguation (W0a) — distinct from K_base, K_R5, K_crit, K_substrate, K_R3, K_FIRAS, K_pivot | W0a R5; partition §1 W0a |
| D_K cache | `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` | precomputed; SHA pin via `<computed-at-runtime>` first-line stdout |
| L_max | 10 (canonical for spectral-action moments) | framework canonical |
| Mellin convention | Connes-Chamseddine spectral-action convention; analytic-continuation past s=−1 | per S82 + S83 Mellin-cone conventions |
| GPU path | `torch.cuda` if available, `torch.linalg.eigh` for any re-diagonalization | per `feedback_compute-environment.md` |
| CPU fallback | `OMP_NUM_THREADS=8` set BEFORE numpy import | per `.claude/rules/math-scripts.md` |
| Source-cite SHAs (W3-3/W3-4/W3-5 PASSes) | `<computed-at-runtime>` from `computations/s85_gate_verdicts.txt` | input pin map |

`schema_version: R3` (per W0a R3 cutoff_axis YAML pin requirement; not strictly applicable — this gate has no cutoff axis).

### 8. Expected output 4-tuple
`(value="R_JE_retired+R_JK_landed+xi_E_GGE_inv_landed", scheme="branch-iv-canonical", convention="2B-path-c", L_max="N/A")`

`L_max="N/A"` because P4 is a registry-write commit, not a spectral-truncation-sensitive computation. R_JK and xi_E_GGE_inv themselves carry L_max=10 as their computed-value pin; the COMMIT does not have an L_max axis.

### 9. PASS/FAIL/INFO thresholds

- **PASS** (RATIO + ABSOLUTE + EXISTENCE composite):
  - R_JE retired in `branch-iv-canonical.md` (grep substring "R_JE retired" returns ≥1 match)
  - R_JK landed with formula in `branch-iv-canonical.md` (grep substring "R_JK" returns ≥1 match in formula context)
  - ξ_E_GGE^{−1} landed with formula in `branch-iv-canonical.md` (grep substring "xi_E_GGE" returns ≥1 match in formula context)
  - `R_JK = <value>` line present in `canonical_constants.py` with provenance comment
  - `xi_E_GGE_inv = <value>` line present in `canonical_constants.py` with provenance comment
  - `from canonical_constants import *` re-import succeeds; both names accessible
  - All 5 CC PASS (units, M_KK rescaling, file-grep, canonical registration, re-import)
- **FAIL**: any element absent. The gate is COMMIT-class — no quantitative tolerance band; either the registry write happened or it did not.
- **INFO**: NOT applicable — commit gates are PASS/FAIL only. (If the runtime agent encounters mid-task PRU defect — e.g., R_JK formula source ambiguous between two competing 9A §4.6 sub-formulations — emit `PRE-REG-INCOMPLETE` per `.claude/rules/gate-verdicts.md` last paragraph and terminate without commit; orchestrator escalates to user.)

### 10. Substitution chain
P4 carries no sign / direction / threshold claim. The COMMIT is a CHANGE operation (retire → land), not a magnitude claim. The substitution chain requirement of `.claude/rules/math-scripts.md` §Double-Check Logic Before Compute is NOT triggered for this gate. (CC-1 + CC-2 dimensional-analysis traces are themselves substitution chains executed inside the verification script; they verify dimensions, not directions.)

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: BRANCH-IV pathway anchored as the canonical S86+ formulation with two distance-tagged diagnostics replacing R_JE's single-tag. **HARD UNLOCK**: W5a P3 `S86-SECTOR-1-SR-FLOW-Z-FACTOR` becomes runnable (its ξ²(0) IC sources from ξ_E_GGE^{−1} per partition §3 sequencing row "W4 (P4) → W5 (P3 SECTOR-1 ξ²(0) IC)"). The single-name-conflation methodology entry from W0b R7 receives its 2B-path-(c) witness row.

- **FAIL**: BRANCH-IV remains in S85 ambiguous state; W5a P3 cannot dispatch (orchestrator must sub-wave a P4-rescue dispatch). Constraint-map status: the registry retains R_JE single-tag formulation, which has been audited as conflated (single-name-conflation methodology entry from W0b R7 lists 2B SECTOR-split as one of 4 witnesses); W4 FAIL leaves that witness row hanging. The 2B path-(c) commit was selected over path-(a) (retain R_JE) and path-(b) (split R_JE into R_JE_1 + R_JE_2 without re-tagging) because it canonicalizes the distance-class taxonomy used downstream by P5 + P3.

- **PRE-REG-INCOMPLETE**: trigger an S86-W4-supplementary sub-wave to pin R_JK formula source if 9A §4.6 admits multiple readings; do NOT commit a guessed formula.

### 12. Effort estimate
~2-3 hours: 30 min knowledge MCP queries + framework file inspection; 60-90 min substantive section writing + canonical_constants.py edits; 30 min script writing + 5 CC implementation; 15 min verdict-line append + post-dispatch verification per `.claude/rules/agent-standards.md` §Completion Verification.

### 13. Substrate-framing reminder (per `.claude/rules/phononic-framing.md`)
**MANDATORY in every section of branch-iv-canonical.md**: BRANCH-IV is the substrate's transit pathway through the van-Hove fold (τ_fold = 0.190); the eigenvalue spectrum of D_K reorganizes at the fold; R_JK and ξ_E_GGE^{−1} are spectral functionals OF the substrate (moments of D_K), not external probes IN spacetime. Use IS-not-IN language: "R_JK IS the K-functional moment of D_K at distance-2", NOT "R_JK lives in the K-corridor of substrate space". The GGE relic IS the substrate's residual coherence pattern post-fold, not an excitation IN a vacuum. 3He-B is a parent → child inheritance for the ξ_E_GGE^{−1} template, not an analogy (per `project_3heb-inheritance.md`).

---

## §W4-2. S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT (P5)

### 1. Gate ID
`S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT`

### 2. Trigger
`[VERIFY-THEOREM]` — the substrate Mellin-kernel pole at pivot is independent of SR (slow-roll) flow is a STRUCTURAL claim about the regulator-class Mellin-kernel residue. Per `.claude/rules/gate-verdicts.md` §1 trigger taxonomy, [VERIFY-THEOREM] requires proof + counterexample probe. The probe is computed across all 5 atlas members; the theorem is the K-invariant at substrate-distance-1.

### 3. Classification
`GEOMETRIC` — the Mellin-kernel pole structure is a property of the regulator class (the way the spectral content is summed), not a property of the substrate's excitations. Per `.claude/rules/phononic-framing.md`: "GEOMETRIC concerns the spectral triple structure, D_K eigenvalues, Jensen deformation, fiber topology — the fabric itself rather than its excitations". The K-invariant pin is a substrate-distance-1 quantity = first-moment Mellin residue = property of the spectral triple.

### 4. Agent type assignment + rationale
**Primary runtime agent**: `lizzi-spectral-functional-theorist` — Mellin-kernel pole structure is the lizzi-track home domain (Mellin Strip / Convergence Cone Theorem from S85-W0-S6, ZETA-NOT-PHYSICAL-75, S82 W2-3 + W2-5 Mellin-cone work). This is the domain expert. The transit-dynamics-theorist (wave owner) coordinates the dispatch but the runtime agent is `lizzi-spectral-functional-theorist`.

**Cross-cite specialist**: `connes-ncg-theorist` — the Mellin-kernel pole at s=3 in d_spec=8 NCG is the Connes-Chamseddine convention; cross-cite via the Mellin-multiplier infinite-vector formalism (cf. C11 in W2). Cross-cite in the script's SHA-source provenance list; not a separate dispatch.

**NOT gen-physicist** per partition manifest specialist-routing rule.

### 5. Hypothesis (one sentence)
The substrate Mellin-kernel pole structure at the CMB pivot is invariant across the 5-regulator atlas (or 4-regulator if C28 closes STRUCTURALLY-EXCLUDED): the pole locations of M[K_substrate](s) at s=3 in d_spec=8 NCG agree across {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} within a tolerance of RATIO ≤ 1e-3 OR ABSOLUTE ≤ 1e-6, establishing K_substrate as a substrate-distance-1 invariant (regulator-independent first-moment Mellin residue).

### 6. Method — COMPLETE dispatch prompt

```
You are the runtime `lizzi-spectral-functional-theorist` agent dispatched
for S86-W4-2 gate `S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT` (P5). This is a
[VERIFY-THEOREM] structural-claim gate. Your job is to extract the
Mellin-kernel pole locations at s=3 in d_spec=8 NCG across the 5-regulator
atlas at the CMB pivot, verify the K-invariant pin (substrate-distance-1
quantity), and emit a verdict line.

PRE-COMPUTE QUERIES (mandatory per CLAUDE.md "Knowledge MCP — MANDATORY"):
  mcp__knowledge__search_knowledge("Mellin kernel pole pivot regulator")
  mcp__knowledge__search_knowledge("K-invariant substrate distance-1")
  mcp__knowledge__trace_entity("ZETA-NOT-PHYSICAL-75")
  mcp__knowledge__trace_entity("Mellin Strip Convergence Cone Theorem")
  mcp__knowledge__list_constants("K_|tau_fold|M_KK")
Confirm: (a) ZETA-NOT-PHYSICAL-75 is the closed mechanism that established
the K-invariant as substrate-distance-1 in S82 W2-3; (b) the Mellin-cone
infrastructure may not yet be live (W2 plans C9 + C10 for Mellin-cone build).
If C9/C10 not yet PASS at compute time, P5 falls back to direct heat-kernel
truncation per S85 W2-5 convention.

SUBSTITUTION CHAIN (REQUIRED per `.claude/rules/math-scripts.md` §Double-
Check Logic — this gate makes a substrate-distance-1 invariance claim):

  Definition 1 — K-invariant at substrate-distance-1:
    K_substrate(s, regulator R) := Res_{s=3} M[K(τ; R)](s)
    where K(τ; R) is the regulator-R-tagged heat kernel on D_K^2 evaluated
    at τ = τ_pivot, M is the Mellin transform, and Res_{s=3} extracts the
    s=3 pole residue (= first non-trivial Seeley-DeWitt coefficient slot in
    d_spec=8 NCG, per Connes-Chamseddine 1996).
    Distance-1 tag: pole at s=3 corresponds to the FIRST non-trivial Mellin
    residue in d_spec=8 (s = d_spec/2 - 1 = 3); higher-distance tags are at
    s = d_spec/2 - n for n ≥ 2.

  Definition 2 — pivot τ:
    τ_pivot := τ value at which the CMB pivot mode k_pivot = 0.05 Mpc^{-1}
    is sampled. Per S77 N-PIVOT-MAP (canonical_constants.py), this is the
    substrate τ-coordinate corresponding to N_pivot = 3.12 e-folds before
    the fold. Use canonical_constants.tau_pivot if registered; else compute
    from canonical_constants.tau_fold = 0.190 minus the substrate-N translation.

  Definition 3 — 5-regulator atlas:
    A_5 := {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}
    per context §1.5 (W12-4 atlas: F_4 ∪ M = {ζ, Zubarev, SDW} ∪ {cutoff_sqrt,
    anomaly}). Note: if C28 (W4-3) closes STRUCTURALLY-EXCLUDED, the atlas
    contracts to A_4 = F_4 ∪ {anomaly}. P5 runs on whichever atlas is live
    at compute time; if C28 closes simultaneously and disagrees, re-emit P5
    under the post-C28 atlas.

  Step 1 (substitute):
    For each R in A_5:
      pole_R := K_substrate(s=3, R) = Res_{s=3} M[K(τ_pivot; R)](s)

  Step 2 (substitute SR-flow independence):
    Let dε/dN, dη/dN be the SR-flow parameters at τ_pivot. The K-invariance
    claim is:
      ∂(pole_R) / ∂(ε, η) |_{τ_pivot} = 0   for all R in A_5.
    This is the substrate-distance-1 invariance: K_substrate is determined
    by the Mellin-residue structure of the regulator-tagged heat kernel,
    not by the inflaton-SR trajectory.

  Step 3 (simplify to canonical form):
    pole_R = Res_{s=3} M[K(τ_pivot; R)](s)
           = (Seeley-DeWitt a_2 coefficient at τ_pivot under regulator R)
           × (regulator-R Mellin-multiplier residue at s=3)
    The first factor is COMMON to all R (substrate property); the second is
    R-specific. Theorem claim: the second factor evaluates to the SAME
    numerical value across A_5 (modulo a R-specific sign convention pinned
    via P14 a_n regulator-pin discipline + R3 cutoff_axis YAML pin).

  Step 4 (read direction):
    K-invariant ⇔ |pole_R - pole_R'| / |pole_R| ≤ 1e-3 (RATIO) OR
                  |pole_R - pole_R'|         ≤ 1e-6 (ABSOLUTE)
    for all pairs (R, R') in A_5. The PASS direction is "all pairs satisfy
    the tolerance" (substrate-distance-1 invariance HOLDS); FAIL direction is
    "at least one pair violates" (substrate-distance-1 invariance BROKEN);
    INFO direction is "1 of 5 atlas members deviates within band 1e-3 to
    1e-2" (intermediate; flagged for sub-wave audit).

WRITE script `computations/s86_w4_p5_sector_2_k_invariant.py`:

  from canonical_constants import *
  # imports tau_fold, M_KK, tau_pivot (if registered), K-disambiguated
  # K_corridor, K_pivot, K_R3 etc per W0a R5

  PRE-EXISTING infrastructure check (prerequisite for Mellin-cone path):
    try:
        from analytic_zeta import analytic_zeta   # from W2 C10 if landed
        mellin_cone_live = True
    except ImportError:
        mellin_cone_live = False    # fall back to direct heat-kernel
                                    # truncation per S85 W2-5

  GPU PATH MANDATORY for the Mellin-kernel evaluation (per
  `feedback_compute-environment.md` + CLAUDE.md): D_K cache load is
  155984 dim; Mellin transform of K(τ; R) at high precision needs:
       import torch
       K_tau_pivot = torch.from_numpy(...).to('cuda')
       # Mellin via FFT-quadrature on log-tau grid; use torch.fft.fft on GPU
       # for the Mellin-Plancherel evaluation
  CPU FALLBACK:
       import os
       os.environ.setdefault('OMP_NUM_THREADS', '8')
       import numpy as np

  Verification block (first 20 lines stdout per `.claude/rules/gate-verdicts.md`):
    log SHA-256 of:
      - computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz (D_K eigenvalues)
      - canonical_constants.py (tau_pivot, tau_fold, K_corridor entries)
      - computations/s85_gate_verdicts.txt (W2-3, W2-5, ZETA-NOT-PHYSICAL-75
        provenance)
      - regulator-tagged Mellin multiplier source (Connes-Chamseddine 1996
        appendix; W11-3 NCG-Structural-Exclusion META-THEOREM cite)

  Computation:
    poles = {}
    for R in ['zeta', 'zubarev', 'SDW', 'cutoff_sqrt', 'anomaly']:
        K_tau_R = build_regulator_tagged_kernel(D_K_eigs, tau_pivot, R)
        poles[R] = mellin_residue_s3(K_tau_R, regulator=R)

    Tolerance check (Step 4 above):
      max_pair_ratio = max over (R, R'): |poles[R] - poles[R']| / |poles[R]|
      max_pair_abs   = max over (R, R'): |poles[R] - poles[R']|
      pass_ratio    = max_pair_ratio <= 1e-3
      pass_abs      = max_pair_abs   <= 1e-6
      pass_overall  = pass_ratio OR pass_abs

    INFO band: 1 of 5 atlas members deviates with max_pair_ratio in
               [1e-3, 1e-2]; flagged for sub-wave audit.
    FAIL: max_pair_ratio > 1e-2 or > 1e-6 absolute when ratio undefined.

  COUNTEREXAMPLE PROBE (per [VERIFY-THEOREM] trigger requirement):
    Test SR-flow independence by perturbing dε/dN -> dε/dN + δ at τ_pivot
    and re-extracting poles[R]; verify ∂(pole_R)/∂ε ≈ 0 within 1e-4
    (numerical differentiation tolerance). PROBE-FAIL if any pole_R
    shows non-zero derivative.

CROSS-CHECKS (6 mandatory):
  CC-1: pole_R has units of M_KK^2 (a_2 slot). M_KK rescaling test.
  CC-2: K_substrate at s=3 reproduces Connes-Chamseddine 1996
        appendix coefficient for ζ (literature anchor; tolerance 1e-4).
  CC-3: Counterexample probe ∂(pole_R)/∂ε ≈ 0 at all 5 R (or 4 R if
        post-C28 contraction).
  CC-4: cutoff_sqrt entry consistency with S85 W4 workshop verdict
        (REQUIRES-S86-GATE per workshop file `s85-w4-cutoff-sqrt-status.md`
        line 895/1153/1184); P5 either TREATS cutoff_sqrt as in-atlas
        (default; awaits C28 outcome) and reports its pole_R; OR if
        C28 has co-completed STRUCTURALLY-EXCLUDED, drop cutoff_sqrt and
        re-run on A_4.
  CC-5: SHA-pin all input files + canonical_constants imports; closure
        SHA computed from input-pin map (NOT hardcoded) per
        `.claude/rules/gate-verdicts.md`.
  CC-6: schema_version: R3 stamped in plan-block (per W0a R3 cutoff_axis
        YAML pin requirement; this gate INVOKES cutoff axis via cutoff_sqrt
        regulator → MUST have cutoff_axis: spectral|coherence|both pinned).

VERDICT line append to `computations/s86_gate_verdicts.txt`:

  S86-SECTOR-2-MELLIN-KERNEL-K-INVARIANT|PASS|max_pair_ratio=<v>;max_pair_abs=<v>|Mellin-kernel|substrate-distance-1|10|content_sha256:<64-hex>|audit_sha256:<64-hex>
  # audit_sha256_short=<16-hex>

  PASS: max_pair_ratio ≤ 1e-3 OR max_pair_abs ≤ 1e-6 + counterexample
        probe ≈ 0 + 6 CC PASS.
  INFO: 1 of 5 (or 1 of 4) atlas members deviates with
        max_pair_ratio in [1e-3, 1e-2]; record which R and how much.
  FAIL: max_pair_ratio > 1e-2 OR counterexample probe non-zero.

  Exit code 0 regardless.
```

### 7. Machinery pin (PRDR — every free parameter pinned)

| Pin | Value | Source / SHA |
|:----|:------|:-------------|
| Script path | `computations/s86_w4_p5_sector_2_k_invariant.py` | per script-prefix convention §6.5 |
| 5-regulator atlas | {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} | context §1.5; W12-4 empirical 5-regulator atlas |
| Atlas contraction (conditional) | drop cutoff_sqrt → A_4 if C28 co-completes STRUCTURALLY-EXCLUDED | C28 verdict; planner pre-registers conditional fallback |
| L_max | 10 (canonical) | framework canonical |
| Pivot τ | `tau_pivot` (canonical_constants.py if registered; else derived from `tau_fold = 0.190 − N_pivot translation` per S77 N-PIVOT-MAP) | S77 N-PIVOT-MAP; canonical_constants.py |
| d_spec | 8 (NCG dimension) | Connes-Chamseddine convention |
| Pole-extraction scheme | Mellin-Barnes residue at s=3; analytic_zeta API if W2 C10 landed, else direct heat-kernel truncation per S85 W2-5 | conditional on W2 status at compute time |
| Tolerance — RATIO | 1e-3 | S82 + S83 Mellin-cone convention |
| Tolerance — ABSOLUTE | 1e-6 | S82 + S83 Mellin-cone convention |
| Tolerance — INFO band (RATIO) | [1e-3, 1e-2] | per `.claude/rules/gate-verdicts.md` INFO clause |
| Counterexample-probe δε | 1e-4 (numerical differentiation step) | standard finite-difference convention |
| GPU path | `torch.cuda` for Mellin-Plancherel evaluation; `torch.linalg`/`torch.fft.fft` | per `feedback_compute-environment.md` |
| CPU fallback | `OMP_NUM_THREADS=8` BEFORE numpy import | per `.claude/rules/math-scripts.md` |
| `cutoff_axis` YAML field | `cutoff_axis: both` (P5 invokes both spectral cutoff [ζ, Zubarev, SDW] and coherence cutoff [cutoff_sqrt, anomaly]) | W0a R3 |
| `schema_version` | `R3` | W0a R3 + C21 R3 lift |
| Random seed | None — deterministic computation; explicitly pin `np.random.seed(0)` and `torch.manual_seed(0)` for any stochastic Mellin-quadrature fallback | PRDR completeness |
| Input pin map | D_K cache SHA + canonical_constants.py SHA + s85_gate_verdicts.txt SHA + Connes-Chamseddine 1996 appendix SHA (literature) | `<computed-at-runtime>` first 20 lines stdout |

### 8. Expected output 4-tuple
`(value="max_pair_ratio=<v>;max_pair_abs=<v>", scheme="Mellin-kernel", convention="substrate-distance-1", L_max=10)`

### 9. PASS/FAIL/INFO thresholds

- **PASS**: `max_pair_ratio ≤ 1e-3 OR max_pair_abs ≤ 1e-6` across all (R, R') pairs in atlas; counterexample probe ∂(pole_R)/∂ε ≈ 0 within 1e-4 at all R; all 6 CC PASS. Tolerance rule: RATIO is primary; ABSOLUTE is fallback when RATIO undefined (e.g., one pole_R = 0). MIXED tolerance per `.claude/rules/gate-verdicts.md` is the conjunction of RATIO-pass with ABSOLUTE-pass when both are well-defined.
- **FAIL**: `max_pair_ratio > 1e-2` (definitively breaks substrate-distance-1 invariance) OR counterexample probe shows non-zero ∂(pole_R)/∂ε > 1e-4 at any R OR any CC fails.
- **INFO**: `max_pair_ratio in [1e-3, 1e-2]` with exactly 1 of 5 (or 1 of 4) atlas members responsible for the deviation; record which R and how much; flag for sub-wave audit. (Per `feedback_arbitrary-gates.md` INFO usage — this is a structured pre-registered band, not an arbitrary round-number cutoff.)

### 10. Substitution chain
**REQUIRED per `.claude/rules/math-scripts.md` §Double-Check Logic Before Compute** — the gate makes a substrate-distance-1 invariance claim with a tolerance threshold. Full chain:

```
Definition 1 (K-invariant at substrate-distance-1):
  K_substrate(s, R) := Res_{s=3} M[K(τ_pivot; R)](s)
  where M is Mellin transform, K is regulator-R-tagged heat kernel,
  s=3 is the first non-trivial Mellin residue in d_spec=8 NCG.

Definition 2 (5-regulator atlas):
  A_5 := {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}
  per context §1.5 W12-4 partition F_4 ∪ M.

Step 1 (substitute):
  For each R, pole_R := K_substrate(s=3, R)
  For each (R, R') pair, deviation := |pole_R - pole_R'|.

Step 2 (substitute the invariance claim):
  Theorem: ∀ (R, R'), deviation / |pole_R| ≤ 1e-3 OR deviation ≤ 1e-6.

Step 3 (simplify to canonical form):
  pole_R = (a_2(τ_pivot)) × (M_R(s=3))
  where a_2(τ_pivot) is the substrate Seeley-DeWitt coefficient
  (R-independent) and M_R(s=3) is the regulator-R Mellin-multiplier
  residue at s=3.
  Therefore deviation = a_2(τ_pivot) × |M_R(s=3) - M_{R'}(s=3)|.
  Invariance ⇔ M_R(s=3) is R-independent at s=3.

Step 4 (direction):
  M_R(s=3) is R-independent (PASS direction)
    ⇔ K_substrate IS a substrate-distance-1 invariant.
  M_R(s=3) is R-dependent at s=3 (FAIL direction)
    ⇔ K-invariant pin BROKEN; substrate-distance-1 tag invalid for K.
  Conclusion: PASS direction = "regulator-class Mellin residue at s=3
  is universal" — this is the substrate-distance-1 invariance theorem
  claim. Verified numerically across A_5 (or A_4 post-C28).
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: SECTOR-2 pin established as substrate-distance-1 K-invariant; **completes the 2A SECTOR split**: SECTOR-1 = SR-flow Z-factor (W5a P3 territory), SECTOR-2 = Mellin-kernel-K-invariant (this gate). The single-name-conflation methodology entry from W0b R7 receives its 2A SECTOR-split witness row. Constraint-map gain: substrate-distance-1 invariance is now a registry-canonical structural claim with a Python-verified counterexample probe.

- **FAIL**: substrate-distance-1 invariance BROKEN; the K-invariant pin is REJECTED; SECTOR-2 cannot be canonicalized as a single substrate-distance tag — must be split into per-regulator distance tags (SECTOR-2-ζ, SECTOR-2-Zubarev, etc.) at the registry level. This cascades to W6 (perturbative-immunization corollaries C-α/β/γ assume regulator-class universality at distance-1) and to W5a P3 (which sources its IC from substrate-distance-1 quantities — if K-invariance fails, P3's IC inherits per-regulator splitting). Constraint-map gain: SECTOR-split is finer than 2A predicted; new corridor of regulator-specific substrate-distance taxonomy opens.

- **INFO**: 1 atlas member responsible for deviation — record which (most likely candidate per S85 W12-4 is `cutoff_sqrt` if C28 lands GENUINELY-PHYSICAL or REQUIRES-S86-GATE; or `anomaly` if M-class regulators behave differently from F_4-class). Flag the deviating R for sub-wave audit; the K-invariant pin remains LOOSE on the full atlas but STRICT on F_4 (echoes T6 W5-6 HP^1 R-protected-LOOSE/STRICT split landed in W1b).

### 12. Effort estimate
~2-3 hours: 30 min knowledge MCP queries + Mellin-cone infrastructure status check (W2 C9/C10); 60-90 min script writing + 5-regulator pole extraction + counterexample probe; 30 min CC implementation + verification block; 15 min verdict-line append + post-dispatch verification.

### 13. Substrate-framing reminder (per `.claude/rules/phononic-framing.md`)
The Mellin-kernel pole at s=3 IS a property of how the substrate's spectral content is summed — the regulator class IS the summation prescription, the Mellin residue IS one moment of the resulting spectral-action functional. The K-invariant pin asserts that this moment is regulator-independent at substrate-distance-1 — meaning the substrate's first non-trivial spectral-action contribution is intrinsic to D_K, not to the regulator. State the result IS-language: "K_substrate IS the substrate-distance-1 invariant moment of the Mellin-kernel residue at the CMB pivot τ"; NOT "K_substrate is a cutoff-independent quantity living in regulator space". Cross-cite the Mellin Strip / Convergence Cone Theorem (T5, W1b) and ZETA-NOT-PHYSICAL-75 (S82 closed mechanism) — both are upstream substrate-distance-1 anchors.

---

## §W4-3. S86-W-4-CUTOFF-SQRT-ADJUDICATION (C28)

### 1. Gate ID
`S86-W-4-CUTOFF-SQRT-ADJUDICATION`

### 2. Trigger
`[AUDIT]` — the gate captures a workshop adjudication outcome (the S85 connes × lizzi 3-round workshop on cutoff_sqrt status). Per `.claude/rules/gate-verdicts.md` §1, [AUDIT] is "factor-counting / OOM-estimate that must be reproducible". The audit here is the workshop's verdict-classification reproducibility: the runtime agent re-reads the workshop file, extracts the converged R3 verdict, and writes the framework-canonical adjudication file. The VALUE recorded is the verdict classification (one of three pre-registered outcomes); the AUDIT is reproducible because the workshop file is SHA-pinned at S85 close.

### 3. Classification
`META` — regulator-class adjudication outcome decides atlas cardinality. Per `.claude/rules/phononic-framing.md` taxonomy: this is neither PHONONIC (no substrate excitation) nor GEOMETRIC (no spectral-triple structure being computed) nor PARTICLE (no quantum number) — it is META, classifying the framework's regulator-atlas cardinality. The decision cascades to atlas-cardinality dependent gates (W6 immunization corollaries, S87 C45 sixth-regulator-synthesis).

### 4. Agent type assignment + rationale
**Primary runtime agent**: `connes-ncg-theorist` — connes was the R3 closer of the S85 workshop (per workshop file lines 1280+, R3 connes follow-up converges on the gate); the S86 runtime agent should be the same specialist who carried the R3 substitution chain. The connes-ncg-theorist is also the canonical owner of cutoff_AL2010 admissibility derivation (the GENUINELY-PHYSICAL steelman in the workshop).

**Cross-cite specialist**: `lizzi-spectral-functional-theorist` — lizzi was the R2 emergence agent + R3 ratifier of the 3-gate refinement (workshop file lines 1043, 1056, 1153, 1184). The 3-gate joint outcome rule (GATE A L_max-finiteness master + GATE B kernel-admissibility + GATE C S82-applicability) is co-owned by connes (R3 acceptance) and lizzi (R2 refinement). Cross-cite via the script's SHA-source provenance + a co-author line in the framework file.

**NOT gen-physicist** unless the runtime fails: per partition §1 W4 natural-split-candidates note, "C28 may need a gen-physicist rescue if connes×lizzi adjudication is unfinished and needs orchestrator-level commit". Default is connes-ncg-theorist primary.

### 5. Hypothesis (one sentence)
The S85 connes × lizzi 3-round cutoff_sqrt workshop converged on the verdict REQUIRES-S86-GATE with a 3-gate joint adjudication (GATE A L_max-finiteness master gate, GATE B kernel-admissibility conditional refinement, GATE C residual S82-applicability check); C28 captures that verdict in `sessions/framework/registry/cutoff-sqrt-adjudication.md` with the atlas-cardinality cascade documented (REQUIRES-S86-GATE means atlas remains at 5 members with cutoff_sqrt PENDING-EVENT until S86 numerical gate executions of GATES A + B + C resolve).

### 6. Method — COMPLETE dispatch prompt

```
You are the runtime `connes-ncg-theorist` agent dispatched for S86-W4-3
gate `S86-W-4-CUTOFF-SQRT-ADJUDICATION` (C28). This is an [AUDIT]
workshop-closure-capture gate. Your job is to extract the converged R3
verdict from the S85 connes × lizzi 3-round workshop on cutoff_sqrt status,
classify the outcome into one of three pre-registered classes, write the
framework-canonical adjudication file, and emit a verdict line.

PRE-COMPUTE QUERIES (mandatory per CLAUDE.md "Knowledge MCP — MANDATORY"):
  mcp__knowledge__search_knowledge("cutoff_sqrt regulator atlas STRUCTURALLY-EXCLUDED")
  mcp__knowledge__search_knowledge("cutoff_AL2010 kernel admissibility")
  mcp__knowledge__trace_entity("ZETA-NOT-PHYSICAL-75")
  mcp__knowledge__trace_entity("Regulator-Family Boundary Theorem")
  mcp__knowledge__list_entities("closed")    # check closure ledger
Confirm: (a) cutoff_AL2010 admissibility status is OPEN at S85 close; (b)
the 3-gate refinement is the converged adjudication apparatus; (c) C45
S86-SIXTH-REGULATOR-SYNTHESIS is conditional on C28 outcome (per partition
§2 deferral row).

STEP 1 — Read the workshop file:
  Path: `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md`
  File size: 1916 lines. SHA-pin at workshop-file load time (first 20 lines
  stdout per `.claude/rules/gate-verdicts.md`).

  EXTRACT verbatim from the file:
    (i)   Round 3 connes closing verdict (workshop file ~lines 1280-1340)
    (ii)  Round 2 lizzi emergence E1-L (~line 1153) "REQUIRES-S86-GATE is
          the converged W4 verdict, with the technical landscape now sharply
          asymmetric"
    (iii) Round 2 lizzi E2-L (~line 1056-1065) 3-gate joint outcome rule
          with master-gate refinement
    (iv)  Round 2 lizzi E3-L (~line 1255-1269) combinatorial vs admissibility
          taxonomy LAYER 1 / LAYER 2 separation
    (v)   Round 3 connes E1-L acceptance (~line 1329) "ACCEPTED IN FULL"
    (vi)  Joint outcome rule pre-commit (~line 911-927, 1222)
    (vii) Workshop-file content_sha256 (compute via Python hashlib at load
          time; record as input pin)

STEP 2 — Classify the verdict into one of three pre-registered outcomes:

  Pre-registered outcomes (per gen-physicist S-7 §V.22 + lizzi S-7 §IV.3):
    {STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL, REQUIRES-S86-GATE}

  Decision rule (substitution chain — REQUIRED per `.claude/rules/math-
  scripts.md` §Double-Check Logic Before Compute):

    Definition: workshop-converged outcome := the verdict that BOTH connes
                R3 and lizzi R2 endorse without retraction.

    Substitution: from workshop file:
      lizzi R2 E1-L (line 1153): "REQUIRES-S86-GATE is the converged W4
        verdict, with the technical landscape now sharply asymmetric."
      connes R3 (line 1329): "(c) E1-L: REQUIRES-S86-GATE as the workshop's
        converged W4 verdict: ACCEPTED IN FULL."

    Simplify: BOTH agents endorsed REQUIRES-S86-GATE without retraction in
              R3.

    Direction: workshop-converged outcome = REQUIRES-S86-GATE.

  Therefore the C28 verdict classification is REQUIRES-S86-GATE.

  IF the runtime audit re-reads the workshop and finds the convergence claim
  ambiguous or contradicted (e.g., connes R3 retracts the acceptance, or
  lizzi R2 E1-L is conditional on unmet criteria), then:
    - Classification = the SAME three options, picked per the substitution
      chain at re-read time.
    - If no clear convergence is read off, emit FAIL (workshop file
      unparseable or contradicted) — do NOT guess.

STEP 3 — Document the 3-gate joint adjudication apparatus:

  From workshop file lines 911-927 (R2-A-E2 connes pre-commit) + 1056-1065
  (R2-B lizzi master-gate refinement) + 1184 (R2 lizzi closing) + 1329
  (R3 connes acceptance):

    GATE A (master gate; expected to FAIL pure cutoff_AL2010):
      L_max-finiteness check on the cutoff_AL2010 admissibility derivation.
      PASS iff the derivation yields a finite, well-defined regulator at
      L_max → ∞; FAIL if divergent. Per workshop R2 D1 (connes), pure
      cutoff_AL2010 is EXPECTED to fail this gate due to the L_max-divergence
      attack.

    GATE B (kernel-admissibility conditional refinement):
      Whether the kernel admits f_0 != 0 under broadened CM-2008 §1.143.
      PASS iff a kernel admissibility extension covers the a_0 slot; FAIL
      otherwise. Per workshop R2 lizzi E2-L: GATE B is necessary-but-not-
      sufficient (because even if a_0 is sourced by {dim, fin} alone, the
      COUPLING into S_b at the Λ^4 slot still requires GATE A).

    GATE C (residual S82-applicability check):
      Whether S82 W2-3 + W2-5 disjoint-corridor + reg-violation results
      apply to the cutoff_AL2010 admissibility branch. PASS iff S82
      results extend to cutoff_AL2010; FAIL otherwise.

    Joint outcome rule (refined L_lizzi from workshop line 1056-1065):
      If GATE A PASSES + GATE B PASSES + GATE C PASSES: GENUINELY-PHYSICAL
        (atlas REMAINS 5-regulator with cutoff_sqrt promoted to canonical).
      If GATE A FAILS regardless of B/C: STRUCTURALLY-EXCLUDED (atlas
        contracts to 4-regulator F_4 ∪ {anomaly}; cutoff_sqrt removed).
      If GATE A PASSES + (GATE B FAILS OR GATE C FAILS): REQUIRES-S87-GATE
        (atlas pre-status PENDING; defer to S87).

  PRE-REGISTRATION OF S86 NUMERICAL GATES A + B + C (because C28 verdict =
  REQUIRES-S86-GATE per workshop convergence):
    - Pre-register GATE A as `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS`
      (placeholder for S86+ wave dispatch; not part of W4)
    - Pre-register GATE B as `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY`
    - Pre-register GATE C as `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY`
    - Each gate pre-registered with PASS/FAIL/INFO thresholds + machinery
      pin per PRDR; these enter S86+ as new W-prefixed items.

STEP 4 — Write `sessions/framework/registry/cutoff-sqrt-adjudication.md`:

  Header: "# Cutoff_sqrt Adjudication (S86 C28 verdict landing)"

  Sections:
    ## §1. Workshop convergence (S85 W4)
       (verbatim quotes from connes R3 + lizzi R2 + lines 911/1056/1153/
        1184/1329; cite workshop_sha)

    ## §2. Verdict classification: REQUIRES-S86-GATE
       (substitution chain from STEP 2; binding pre-registration)

    ## §3. 3-gate joint adjudication apparatus
       ### §3.1 GATE A (L_max-finiteness master)
       ### §3.2 GATE B (kernel-admissibility conditional refinement)
       ### §3.3 GATE C (S82-applicability residual check)
       ### §3.4 Joint outcome rule (refined L_lizzi)

    ## §4. Atlas-cardinality cascade
       Current atlas: A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}.
       Post-S86 (conditional on GATES A+B+C):
         - A_5 retained if GENUINELY-PHYSICAL (GATES A+B+C all PASS)
         - A_4 = {ζ, Zubarev, SDW, anomaly} if STRUCTURALLY-EXCLUDED
           (GATE A FAILS) — collapses W5 frustration to 4-regulator
         - A_5 PENDING if REQUIRES-S87-GATE — atlas stays at 5 with
           cutoff_sqrt PENDING-EVENT classification

    ## §5. Downstream cascade
       - W6 perturbative-immunization corollaries (C2 umbrella + C-α/β/γ):
         atlas-cardinality dependent — re-run under PASS-resolved atlas
         when GATES A+B+C close.
       - C45 S87 SIXTH-REGULATOR-SYNTHESIS: only meaningful if atlas
         contracts (STRUCTURALLY-EXCLUDED) or remains 5-with-PENDING
         (REQUIRES-S87-GATE); deferred to S87 per partition §2.
       - W4-2 P5 K-invariant: P5 runs on whichever atlas is live at
         compute time; if C28 resolves STRUCTURALLY-EXCLUDED before P5
         dispatches, P5 runs on A_4.

    ## §6. Provenance + cross-cite ledger
       - workshop_sha (S85 file)
       - connes-ncg-theorist (R3 verdict closer)
       - lizzi-spectral-functional-theorist (R2 emergence + 3-gate refinement)
       - C45 S87 deferral row from partition §2
       - R8 PRR three-layer adjudication methodology entry from W0b

STEP 5 — Write `computations/s86_w4_c28_cutoff_sqrt_adjudication.py`:

  from canonical_constants import *

  Verification block (first 20 lines stdout):
    log SHA-256 of:
      - sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md
      - sessions/framework/registry/cutoff-sqrt-adjudication.md (after write)
      - sessions/permanent-results-registry.md (for cross-cite to existing
        ZETA-NOT-PHYSICAL-75 + W11-3 NCG-Structural-Exclusion META-THEOREM)

  No GPU required — this is a parse + classify + write operation.
  Set OMP_NUM_THREADS=8 for any incidental numpy use.

  Computation:
    workshop_text = read_workshop_file()
    convergence = parse_convergence_block(workshop_text)
       # extracts connes R3 closing + lizzi R2 E1-L lines verbatim
    verdict_class = classify(convergence)
       # one of {STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL, REQUIRES-S86-GATE}
       # per substitution chain in STEP 2

    if verdict_class == "REQUIRES-S86-GATE":
        gates_pre_registered = pre_register_3_gates(workshop_text)
        # writes the GATE A + B + C pre-registrations to the framework file

    write_framework_file(verdict_class, gates_pre_registered)
    cross_check_5(verdict_class, framework_file_path)

CROSS-CHECKS (5 mandatory):
  CC-1: workshop file SHA matches expected (first-load SHA pin).
  CC-2: classification ∈ {STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL,
        REQUIRES-S86-GATE} (no other value permitted).
  CC-3: framework file contains the substring "REQUIRES-S86-GATE" (or
        whichever verdict was selected) AND all 3 GATE pre-registrations
        (if REQUIRES-S86-GATE).
  CC-4: framework file substring "atlas cardinality" appears with the
        per-outcome cascade documented (4-regulator vs 5-regulator vs
        5-PENDING).
  CC-5: cross-cite to W0b R8 PRR three-layer adjudication methodology
        entry present (this gate INHERITS the methodology vocabulary
        from R8).

VERDICT line append to `computations/s86_gate_verdicts.txt`:

  S86-W-4-CUTOFF-SQRT-ADJUDICATION|INFO|REQUIRES-S86-GATE|connes×lizzi-workshop|3-round-closeout|N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
  # audit_sha256_short=<16-hex>

  Verdict mapping:
    classification = STRUCTURALLY-EXCLUDED → PASS (atlas contracts
                     definitively; structural closure)
    classification = GENUINELY-PHYSICAL    → PASS (atlas confirmed;
                     5-regulator with two physical sub-families becomes
                     structural TWO-CLASS THEOREM)
    classification = REQUIRES-S86-GATE     → INFO (deferred to subsequent
                     wave; 3 GATES A+B+C pre-registered)
    workshop file unparseable / contradicted → FAIL (do NOT guess)

  Exit code 0 regardless.
```

### 7. Machinery pin (PRDR — every free parameter pinned)

| Pin | Value | Source / SHA |
|:----|:------|:-------------|
| Workshop file path | `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` | partition §1 W4 + this plan |
| Workshop file SHA | `<computed-at-runtime>` first 20 lines stdout | input pin map |
| Framework file path (output) | `sessions/framework/registry/cutoff-sqrt-adjudication.md` | this plan |
| Verification script path | `computations/s86_w4_c28_cutoff_sqrt_adjudication.py` | per script-prefix convention §6.5 |
| Verdict-classification scheme | enum {STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL, REQUIRES-S86-GATE} | gen-physicist S-7 §V.22 + lizzi S-7 §IV.3 |
| Convergence-detection rule | "BOTH connes R3 and lizzi R2 endorse without retraction" | substitution chain in STEP 2 |
| Atlas-cardinality outcome map | STRUCTURALLY-EXCLUDED → A_4; GENUINELY-PHYSICAL → A_5; REQUIRES-S86-GATE → A_5 PENDING | this plan |
| 3-gate pre-registration (conditional on REQUIRES-S86-GATE) | GATE A L_max-finiteness, GATE B kernel-admissibility, GATE C S82-applicability | workshop file lines 911-927, 1056-1065, 1184, 1329 |
| Source-cite SHAs | s85-w4-cutoff-sqrt-status.md SHA + permanent-results-registry.md SHA + W0b R8 entry SHA (when R8 lands) | input pin map |
| GPU path | NONE (parse + classify + write) | not applicable |
| CPU thread cap | `OMP_NUM_THREADS=8` for any incidental numpy use | per `.claude/rules/math-scripts.md` |
| `cutoff_axis` YAML field | `cutoff_axis: coherence` (cutoff_sqrt + anomaly are coherence-class regulators per S-1 F_4/M partition) | W0a R3 |
| `schema_version` | `R3` | W0a R3 |
| Random seed | None (deterministic parse + classify) | PRDR completeness |

### 8. Expected output 4-tuple
`(value="REQUIRES-S86-GATE" [or whichever verdict reads off], scheme="connes×lizzi-workshop", convention="3-round-closeout", L_max="N/A")`

`L_max="N/A"` because C28 is a workshop-closure-capture gate, not a spectral computation; the underlying GATES A + B + C carry their own L_max pins when they dispatch in subsequent waves.

### 9. PASS/FAIL/INFO thresholds

- **PASS**: classification is STRUCTURALLY-EXCLUDED (atlas contracts to A_4; structural closure achieved) OR GENUINELY-PHYSICAL (atlas confirmed at A_5 with two physical sub-families = structural TWO-CLASS THEOREM stronger than S67 FRUSTRATION-TRIANGLE). Atlas-cardinality outcome documented in cutoff-sqrt-adjudication.md per cascade table.
- **INFO**: classification is REQUIRES-S86-GATE (deferred to subsequent wave for GATES A + B + C numerical execution); 3 gates pre-registered with full PRDR machinery pin specs in the framework file. Per `feedback_arbitrary-gates.md` INFO is the correct verdict — REQUIRES-S86-GATE is a structured pre-registered outcome, not a methodological failure.
- **FAIL**: workshop file unparseable (file missing, mid-file truncation, contradiction between connes R3 and lizzi R2 that prevents convergence-detection); do NOT guess the classification — flag as FAIL and escalate to user via Stage-3 trigger per `.claude/rules/v3-closure-recovery.md`.

**Expected verdict** per S85 workshop-file convergence (lines 1153 + 1329): **INFO with classification REQUIRES-S86-GATE**. The PASS expectation (STRUCTURALLY-EXCLUDED or GENUINELY-PHYSICAL) is RULED OUT by the workshop's converged refusal to commit either steelman: GENUINELY-PHYSICAL retreated to a modified-coupling Q6-C reframe lizzi did NOT defend in R2; STRUCTURALLY-EXCLUDED retreated from kernel-admissibility (S82 W2-5 reg-violation, retracted) to L_max-finiteness (D1, expected to FAIL pure cutoff_AL2010). Both retreats name sharp pre-registered numerical questions; neither closes definitively in the workshop. Therefore C28's expected outcome is INFO/REQUIRES-S86-GATE.

### 10. Substitution chain
**REQUIRED per `.claude/rules/math-scripts.md` §Double-Check Logic Before Compute** — the gate makes a classification claim that picks one of three pre-registered outcomes. Full chain (also in dispatch prompt STEP 2):

```
Definition (workshop-converged outcome):
  workshop-converged outcome := the verdict that BOTH connes R3 and lizzi R2
                                endorse without retraction.

Substitution (from workshop file `s85-w4-cutoff-sqrt-status.md`):
  lizzi R2 E1-L (line 1153):
    "REQUIRES-S86-GATE is the converged W4 verdict, with the technical
     landscape now sharply asymmetric."
  connes R3 (line 1329 (c) E1-L):
    "REQUIRES-S86-GATE as the workshop's converged W4 verdict: ACCEPTED IN
     FULL."

Simplify:
  BOTH agents endorsed REQUIRES-S86-GATE.
  No retractions present in workshop file post-line-1329.
  Therefore workshop-converged outcome = REQUIRES-S86-GATE.

Direction:
  Verdict classification = REQUIRES-S86-GATE.
  C28 outcome = INFO (per threshold table; REQUIRES-S86-GATE → INFO).
  Atlas cardinality cascade = A_5 PENDING with cutoff_sqrt PENDING-EVENT
                              status; 3 GATES A + B + C pre-registered for
                              S86+ dispatch.
  Conclusion: C28 lands INFO with REQUIRES-S86-GATE classification.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS (STRUCTURALLY-EXCLUDED)**: atlas reduces to 4-regulator F_4 ∪ {anomaly}; cutoff_sqrt removed from regulator atlas; W5 frustration collapses to 4-regulator (every W5 result that was a 5-atlas-membership-FAIL becomes a PASS or vacuous on the contracted atlas, per workshop file C3 substitution chains). C45 S87 SIXTH-REGULATOR-SYNTHESIS becomes meaningful (build composite r_mix = α·zeta + β·{remaining regulator}). The S67 FRUSTRATION-TRIANGLE retains its 3-bit information content; W5 retains its 2-class regulator-distinction (F_4 vs {anomaly}). Constraint-map gain: definitive structural closure of one regulator-class corridor.

- **PASS (GENUINELY-PHYSICAL)**: atlas remains 5-regulator with cutoff_sqrt promoted to canonical second physical sub-family. W5 results constitute a structural TWO-CLASS THEOREM (F_4 = a_4-pure ∪ {cutoff_sqrt, anomaly} = mixed-support) STRONGER than S67 FRUSTRATION-TRIANGLE's 3-bit closure. Per workshop file lines 372 + 922-927 + 1184 + 1252: this would require the modified-coupling Q6-C reframe to succeed, which lizzi explicitly did NOT defend in R2. So this outcome is RULED OUT at S85 close; would require a sub-wave defending Q6-C to revive. Constraint-map gain: structural promotion of regulator-class taxonomy.

- **INFO (REQUIRES-S86-GATE)**: atlas stays at 5 with cutoff_sqrt PENDING-EVENT; 3 GATES A + B + C pre-registered for subsequent-wave numerical dispatch. **EXPECTED outcome per S85 workshop convergence**. Constraint-map gain: structured deferral with explicit numerical pre-registration; no information loss; future S86+ waves dispatch GATES A + B + C with full PRDR machinery pins. C45 S87 stays deferred (per partition §2). W6 corollaries run on full A_5; if GATE A subsequently FAILS, W6 results re-emit on A_4.

- **FAIL (workshop unparseable)**: requires user intervention via Stage-3 trigger per v3-closure-recovery.md (workshop file is the SOLE input; if it cannot be parsed, the gate cannot be evaluated). Constraint-map status: C28 left OPEN; downstream waves W6 + S87 C45 inherit the open status. Should be impossible at compute time given the S85 workshop file exists at 1916 lines with a clear R3 convergence section.

### 12. Effort estimate
4-6 hours per partition §1 W4: 60-90 min knowledge MCP queries + workshop file read + convergence extraction; 90-120 min substitution-chain documentation + 3-gate pre-registration writing; 60-90 min framework file write + script + 5 CC; 30-45 min verdict-line append + post-dispatch verification. The longer end (6h) accounts for the 3-gate pre-registration's PRDR machinery-pin specs needing to be written at full plan-grade (not stub) so that subsequent S86+ wave-planners can dispatch GATES A + B + C without re-deriving the pin specs.

### 13. Substrate-framing reminder (per `.claude/rules/phononic-framing.md`)
The cutoff_sqrt regulator IS one of the 5 prescriptions for summing the substrate's spectral content into a finite spectral-action functional. The atlas-cardinality decision IS a statement about how many distinct structural prescriptions the substrate's spectral content admits — NOT a statement about how many "layers" or "containers" the substrate has. The 3 GATES A + B + C are tests OF the cutoff_sqrt prescription's structural admissibility within Connes-Chamseddine 2010 axioms — not tests of an external cutoff scale IN the substrate. State the result IS-language: "the regulator atlas IS the set of admissible Mellin-summation prescriptions on the substrate spectral content"; NOT "the regulator atlas is a list of cutoffs imposed on substrate space". Cross-cite the Mellin Strip / Convergence Cone Theorem (T5, W1b), the Regulator-Family Boundary Theorem (lizzi S-1), and the NCG-Structural-Exclusion META-THEOREM (W11-3 + T2).

---

## §X. Wave W4 → Downstream Decision Point

### §X.1 P4 → W5a P3 HARD DEPENDENCY

Per partition §3 sequencing row "W4 (P4 ξ_E_GGE^{−1} pin) → W5 (P3 SECTOR-1 ξ²(0) IC)" + gen-physicist 9A §3.6 ("Sector-1 ξ²(0) IC sources from ξ_E_GGE^{−1} pin"):

P4 PASS unlocks W5a P3 dispatch. The W5a wave-planner reads the canonical_constants.py xi_E_GGE_inv entry as the source of P3's ξ²(0) initial condition. If P4 FAILs or stays PRE-REG-INCOMPLETE, W5a must defer P3 to a sub-wave or escalate to user. The W5a planner explicitly CITES this dependency per partition §1 W5a "HARD DEPENDENCY: P4 ξ_E_GGE^{−1} pin from W4 must land first".

Implication for orchestrator at compute time: dispatch W4-1 P4 BEFORE dispatching W5a P3. If both waves go to dispatch in parallel batches, the orchestrator stages W5a P3 dispatch until W4-1 P4 verdict line lands in `computations/s86_gate_verdicts.txt`.

### §X.2 P5 → W6 perturbative-immunization corollaries

P5's K-invariant pin establishes substrate-distance-1 invariance of the Mellin-kernel residue. W6 C2 + C40 + C42 perturbative-immunization corollaries assume regulator-class universality at substrate-distance-1; if P5 FAILs, those corollaries inherit a per-regulator splitting that breaks the §VII.S immunization family's flat structure. W6 planner cites P5 status in its dispatch prompts.

### §X.3 C28 → atlas-cardinality decision affects C45 S87 sixth-regulator-synthesis

Per partition §2 deferral row C45: "only meaningful after C28 W-4 cutoff_sqrt closes — wait for S86 W4 verdict". C28's expected INFO/REQUIRES-S86-GATE outcome KEEPS C45 deferred to S87 (the sixth-regulator-synthesis is only meaningful after the 5-vs-4-vs-5-PENDING atlas decision lands; with REQUIRES-S86-GATE the atlas stays at 5-PENDING and C45 has no floor to extend).

If C28 unexpectedly lands STRUCTURALLY-EXCLUDED, C45 PROMOTES from S87 deferral to an S86 late-wave (W15 or similar) candidate.

### §X.4 C28 → W6 perturbative-immunization corollaries (atlas-cardinality dependent)

C2 umbrella + C-α/β/γ corollaries in W6 run over the atlas; the atlas-cardinality decision from C28 cascades into the corollary-test scheme. With REQUIRES-S86-GATE outcome, W6 corollaries run on full A_5 with cutoff_sqrt PENDING-EVENT noted; subsequent GATE A FAIL would trigger re-emission on A_4. W6 planner must cite C28 status in its dispatch prompts (which it does NOT, by partition §1 W6 sequencing — but this plan flags the atlas-cardinality dependency for the orchestrator).

---

## §0.10. Wave W4 Machinery-Enumeration Pin (PRDR — closes Class-8 PRU vulnerability)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate-relevant machinery parameter is enumerated below. Failure to pin any parameter creates execution-time freedom that manifests as multi-iteration verdict-log floatation. PRDR (Pre-Registration Dry-Run) was performed at plan-write time by static analysis of the dispatch prompts in §W4-1 / §W4-2 / §W4-3.

### W4-1 (P4) machinery enumeration

| Parameter | Pin value | Pinned where |
|:----------|:----------|:-------------|
| Framework file path | `sessions/framework/registry/branch-iv-canonical.md` | §W4-1 STEP 1 |
| Canonical constants file | `computations/canonical_constants.py` | §W4-1 STEP 3 |
| Verification script path | `computations/s86_w4_p4_branch_iv_commit.py` | §W4-1 STEP 4 |
| `R_JK` canonical name | `R_JK` (lower-snake variants explicitly forbidden) | §W4-1 §6 + §7 |
| `xi_E_GGE_inv` canonical name | `xi_E_GGE_inv` | §W4-1 §6 + §7 |
| K_corridor source | W0a R5 K-disambiguation `K_corridor` (distinct from 7 other K-keys) | §W4-1 §7 |
| D_K cache | `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` | §W4-1 §6 STEP 4 |
| L_max | 10 (selects L=10 slice from npz `L_max=[8,10,12]` grid via `.tolist().index(10)`; runtime canonical-path rescue per gate-verdicts.md) | §W4-1 §7 |
| Mellin convention | Connes-Chamseddine analytic-continuation past s=−1 | §W4-1 §7 |
| GPU path | `torch.cuda` + `torch.linalg.eigh` for eigenvalue ops | §W4-1 §6 STEP 4 |
| CPU fallback | `OMP_NUM_THREADS=8` BEFORE numpy import | §W4-1 §7 |
| Source-cite SHAs (W3-3/W3-4/W3-5) | `<computed-at-runtime>` from s85_gate_verdicts.txt | §W4-1 §7 |
| Output file paths | `branch-iv-canonical.md` (edits), `canonical_constants.py` (edits), `s86_w4_p4_branch_iv_commit.py` (new) | §W4-1 §6 |
| Random seed | N/A (deterministic commit) | §W4-1 §7 |
| Cross-checks | 5 mandatory (CC-1 .. CC-5 in §W4-1 §6 STEP 5) | §W4-1 §6 |
| Verdict-line schema | `S86-BRANCH-IV-FORMULATION-COMMIT|PASS|...|content_sha256:|audit_sha256:` per `.claude/rules/gate-verdicts.md` W9a-99 dual-SHA template | §W4-1 §6 STEP 6 |

PRDR confirmation: every free parameter pinned. D_PRU = 0.

### W4-2 (P5) machinery enumeration

| Parameter | Pin value | Pinned where |
|:----------|:----------|:-------------|
| Script path | `computations/s86_w4_p5_sector_2_k_invariant.py` | §W4-2 §6 |
| 5-regulator atlas | {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} | §W4-2 §7 |
| Atlas contraction (conditional) | A_4 if C28 STRUCTURALLY-EXCLUDED at compute time | §W4-2 §7 |
| L_max | 10 | §W4-2 §7 |
| Pivot τ | `tau_pivot` from canonical_constants.py (or derived from `tau_fold = 0.190` minus N_pivot translation per S77) | §W4-2 §7 |
| d_spec | 8 | §W4-2 §7 |
| Pole-extraction scheme | Mellin-Barnes residue at s=3; analytic_zeta API if W2 C10 landed, else direct heat-kernel truncation per S85 W2-5 | §W4-2 §7 |
| Tolerance — RATIO | 1e-3 | §W4-2 §7 + §9 |
| Tolerance — ABSOLUTE | 1e-6 | §W4-2 §7 + §9 |
| Tolerance — INFO band | RATIO ∈ [1e-3, 1e-2] | §W4-2 §9 |
| Counterexample-probe δε | 1e-4 | §W4-2 §7 |
| GPU path | `torch.cuda` + `torch.linalg`/`torch.fft.fft` for Mellin-Plancherel | §W4-2 §6 |
| CPU fallback | `OMP_NUM_THREADS=8` BEFORE numpy import | §W4-2 §7 |
| `cutoff_axis` YAML | `both` (P5 invokes both spectral and coherence cutoffs) | §W4-2 §7 |
| `schema_version` | `R3` | §W4-2 §7 |
| Random seed | `np.random.seed(0)` + `torch.manual_seed(0)` for any stochastic Mellin-quadrature fallback | §W4-2 §7 |
| Input pin map | D_K cache SHA + canonical_constants SHA + s85_gate_verdicts SHA + Connes-Chamseddine 1996 appendix SHA | §W4-2 §7 |
| Cross-checks | 6 mandatory (CC-1 .. CC-6 in §W4-2 §6) | §W4-2 §6 |
| Verdict-line schema | per W9a-99 dual-SHA template | §W4-2 §6 |

PRDR confirmation: every free parameter pinned. D_PRU = 0.

### W4-3 (C28) machinery enumeration

| Parameter | Pin value | Pinned where |
|:----------|:----------|:-------------|
| Workshop file path | `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` | §W4-3 §7 |
| Workshop file SHA | `<computed-at-runtime>` first 20 lines stdout | §W4-3 §7 |
| Framework file path (output) | `sessions/framework/registry/cutoff-sqrt-adjudication.md` | §W4-3 §7 |
| Verification script path | `computations/s86_w4_c28_cutoff_sqrt_adjudication.py` | §W4-3 §6 |
| Verdict-classification scheme | enum {STRUCTURALLY-EXCLUDED, GENUINELY-PHYSICAL, REQUIRES-S86-GATE} | §W4-3 §7 |
| Convergence-detection rule | "BOTH connes R3 and lizzi R2 endorse without retraction" | §W4-3 §6 STEP 2 + §10 |
| Atlas-cardinality outcome map | STRUCTURALLY-EXCLUDED→A_4; GENUINELY-PHYSICAL→A_5; REQUIRES-S86-GATE→A_5 PENDING | §W4-3 §7 |
| 3-gate pre-registration (conditional) | GATE A L_max-finiteness, GATE B kernel-admissibility, GATE C S82-applicability | §W4-3 §6 STEP 3 + §7 |
| GPU path | NONE (parse + classify + write) | §W4-3 §7 |
| CPU thread cap | `OMP_NUM_THREADS=8` for incidental numpy use | §W4-3 §7 |
| `cutoff_axis` YAML | `coherence` (cutoff_sqrt + anomaly are coherence-class regulators per S-1 F_4/M partition) | §W4-3 §7 |
| `schema_version` | `R3` | §W4-3 §7 |
| Random seed | None (deterministic parse + classify) | §W4-3 §7 |
| Cross-checks | 5 mandatory (CC-1 .. CC-5 in §W4-3 §6) | §W4-3 §6 |
| Verdict-line schema | per W9a-99 dual-SHA template | §W4-3 §6 |

PRDR confirmation: every free parameter pinned. D_PRU = 0.

**Wave-level PRDR verification**: D_PRU_wave = 0 (sum over 3 gates). Run `computations/_pru_cardinality_audit.py --plan sessions/session-plan/session-86-plan-w4.md` post-write; expected exit 0 with D_PRU_raw = 0.

---

## §0.11. Wave W4 Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md` "Pre-Registration Protocol" item 1 + Class-8 PRU prevention, every input file is pinned by SHA-256. Static files get precomputed hashes (deferred to runtime since hash computation requires file read at script-execute time); dynamic inputs marked `<computed-at-runtime>`.

| File / source | SHA pin | Used by |
|:--------------|:--------|:--------|
| `sessions/framework/registry/branch-iv-canonical.md` | `<computed-at-runtime>` (file may not exist pre-W4-1) | W4-1 P4 |
| `computations/canonical_constants.py` (pre-edit) | `<computed-at-runtime>` | W4-1 P4 + W4-2 P5 (read-only) |
| `computations/canonical_constants.py` (post-edit) | `<computed-at-runtime>` | W4-1 P4 (write-target) |
| `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` | `<computed-at-runtime>` | W4-1 P4 + W4-2 P5 |
| `computations/s85_gate_verdicts.txt` (149 verdicts, 52,187 B per context §0) | `<computed-at-runtime>` | W4-1 P4 (W3-3/W3-4/W3-5 cite SHAs) + W4-2 P5 (W2-3/W2-5 cite SHAs) |
| `sessions/permanent-results-registry.md` (216,477 B per context §0) | `<computed-at-runtime>` | W4-3 C28 (cross-cite to ZETA-NOT-PHYSICAL-75 + W11-3 META-THEOREM) |
| `sessions/archive/session-85/workshops/s85-w4-cutoff-sqrt-status.md` (1916 lines) | `<computed-at-runtime>` | W4-3 C28 (sole input) |
| `sessions/framework/registry/cutoff-sqrt-adjudication.md` (output) | `<computed-at-runtime>` post-write | W4-3 C28 |
| Connes-Chamseddine 1996 appendix (literature anchor for Mellin-multiplier residue at s=3) | `<computed-at-runtime>` from local PDF if present; else cite by DOI | W4-2 P5 |
| W0a R3 cutoff_axis YAML pin clause (in `.claude/templates/pru-pre-registration-template.md` after W0a lands) | `<computed-at-runtime>` | W4-2 P5 + W4-3 C28 (cutoff_axis YAML stamp) |
| W0b R8 PRR three-layer adjudication methodology entry (in `sessions/permanent-results-registry.md` after W0b lands) | `<computed-at-runtime>` | W4-3 C28 (cross-cite) |
| W0a R5 K-disambiguation (8-key vocabulary in `_pru_*` classifier) | `<computed-at-runtime>` | W4-1 P4 (K_corridor source) + W4-2 P5 (K_corridor / K_pivot disambiguation) |

**Closure SHA computation rule** (per `.claude/rules/gate-verdicts.md` "audit_sha256"): `audit_sha256 = closure_hash(input_pin_map ∪ machinery_pin_map)` — computed from the union of the input-SHA ledger above + the machinery-enumeration pin §0.10 above. Scripts MUST compute this at runtime via `computations/_closure_hash.py` (or equivalent); HARDCODING the SHA is FORBIDDEN per `.claude/rules/v3-closure-recovery.md` §sig_5 PROHIBITED_ACTIONS clause 4.

---

## End of Wave W4 plan

3 gate blocks (P4 + P5 + C28) at full 13-field fidelity; 3 PRDR enumerations with D_PRU_wave = 0; downstream-decision-point cross-references to W5a + W6 + S87 C45; substrate-framing reminders applied per `.claude/rules/phononic-framing.md`; specialist agent assignments per partition §1 owner + cross-cite specialist; canonical paths per `.claude/rules/gate-verdicts.md` (verdict file `computations/s86_gate_verdicts.txt`); GPU pinning explicit per `feedback_compute-environment.md`.
