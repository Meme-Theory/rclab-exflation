# Session 86 Plan — Wave W7: Substrate-mechanism gates (CC residue + branch-c)

**Owner**: `gen-physicist` (multi-solo coordination across 3 specialists per gate)
**Output verdict file**: `computations/s86_gate_verdicts.txt`
**Script prefix convention**: `computations/s86_w7_<slug>.py`
**Item count**: 2 (C1, C4)

---

## §0. Wave W7 Summary

Wave W7 executes the two substrate-mechanism gates flagged by the S85 closeout as
requiring multi-solo coordination — neither item lives within a single specialist's
sole jurisdiction, so the wave is gen-physicist-owned at the planner/orchestrator
level, with one designated runtime specialist per gate plus two cross-cited
companion specialists.

- **C1** `S86-JOINT-CC-RESIDUE-COMPUTE` — Joint CC residue across the
  phonon-first / transit / landau sectors. Source: gen-physicist 9A §4.1
  (1A 3-solo from S85). The three sectors each closed their own CC-residue
  derivation in S85; W7-1 extracts the joint (3-sector consensus / weighted)
  residue and tests cross-sector agreement.

- **C4** `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` — Branch-c phonon
  mechanism-specific 10× ABSOLUTE ratio across the 3B 3-solo specialists
  (volovik / landau / kaku). Source: gen-physicist 9A §4.8 (3B 3-solo).
  Tests whether the branch-c phonon mechanism is observably distinct from
  its sibling mechanism candidates.

Both gates are PHONONIC: CC residue is a substrate-spectral quantity (the residue
of the spectral action's CC-channel pole at the Jensen-deformed fold); the
branch-c discriminator probes substrate-mechanism specificity (the identifiability
of one phononic excitation channel relative to its siblings). Both gates flow FROM
the substrate (D_K eigenvalues + spectral moments) TOWARD the emergent CC and
mechanism observables — no container-thinking direction-inversions permitted.

---

## §0.5. Wave W7 Decision-Point Prerequisites

W7 has TWO upstream plan-write dependencies that MUST be respected at compute
sequencing (plan-writing remains parallel per the partition manifest §4):

1. **W1a T2 §VII.R registry slot for CC-residue routing** — C1's "joint CC
   residue" lands at the §VII.R registry slot defined by the NCG-Meta-Theorem
   landing (T2 in W1a). The W7-1 verdict line cites the §VII.R routing key from
   T2's pinned registry-slot SHA. If T2 has not landed at compute time, W7-1
   degrades to INFO (verdict appended with `routing_pending=true`) rather than
   PASS/FAIL.

2. **W4 P4 BRANCH-IV commit clarifies branch-(iv) vs branch-c naming** — C4's
   "branch-c phonon mechanism" is the mechanism formally named in the W4 P4
   BRANCH-IV-FORMULATION-COMMIT (post-R_JE-retirement). The C4 dispatch prompt
   resolves "branch-c" against P4's pinned naming convention. If P4 has not
   landed at compute time, C4 degrades to INFO with `naming_pending=true` and
   defers the verdict to a P4-conditioned re-emission.

Both prerequisites are SEQUENCING constraints, not plan-write dependencies. This
plan file is written independently of T2 / P4; their pinned SHAs are referenced
as `<RUNTIME-LATE-BIND>` in the input-SHA ledger (§0.11).

---

## §I. Carry-Forward Items Mapping

| Wave §-id | Carry-forward source | S86 gate ID | Item class | Effort |
|:----------|:---------------------|:------------|:-----------|:-------|
| §W7-1     | gen-physicist 9A §4.1 (1A 3-solo) | `S86-JOINT-CC-RESIDUE-COMPUTE` | C1 | 2-4h |
| §W7-2     | gen-physicist 9A §4.8 (3B 3-solo) | `S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` | C4 | 2-4h |

Total wave effort: ~4-8h combined (depends on whether the 3-sector outputs from
S85 1A / 3B 3-solo runs can be re-used directly or must be re-computed under
canonical pin discipline).

---

## §W7-1. S86-JOINT-CC-RESIDUE-COMPUTE (C1)

### 1. Gate ID
`S86-JOINT-CC-RESIDUE-COMPUTE` (carry-forward: C1, source gen-physicist 9A §4.1)

### 2. Trigger
`[VERIFY]` — numerical agreement of the joint (3-sector consensus / weighted)
CC residue against pre-registered cross-sector consensus band. The substitution
chain is mandatory because the gate makes a direction claim about cross-sector
agreement.

### 3. Classification
**PHONONIC**. The CC residue is the residue of the spectral action's
CC-channel pole at the Jensen-deformed fold — a substrate-spectral quantity
derived from the D_K eigenvalue distribution via the heat-kernel /
Mellin-Barnes representation. The "joint" version aggregates across three
substrate sectors (phonon-first / transit / landau), each of which is a
distinct phononic excitation channel of the fabric.

### 4. Agent type
**Runtime primary**: `phonon-first-cosmologist` (the phonon-first sector is the
canonical CC-residue host; the other two sectors are sibling-checks). The
planner-level orchestration sits with `gen-physicist` because the gate spans
three solos that no single specialist owns.

**Cross-cited companions** (consulted via input-SHA pins from S85, NOT spawned
as collab agents):
- `transit-dynamics-theorist` (transit-sector CC residue input pin from S85
  1A solo run)
- `landau-condensed-matter-theorist` (landau-sector CC residue input pin from
  S85 1A solo run)

The runtime dispatch is single-agent (phonon-first-cosmologist) consuming three
sector-specific input artifacts; this is a SOLO compute, not a collab workshop.

### 5. Hypothesis
The CC residue, when computed across three substrate sectors (phonon-first /
transit / landau) and aggregated under a pre-registered consensus rule, yields
a single joint value that lies within a narrow cross-sector band, demonstrating
that CC-residue extraction is sector-method-invariant (a substrate-canonical
quantity, not an artifact of one sector's bookkeeping).

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `phonon-first-cosmologist`:

You are computing the joint CC residue across three substrate sectors per
S86-W7-1 (S86-JOINT-CC-RESIDUE-COMPUTE, carry-forward C1 from gen-physicist
9A §4.1).

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch  # GPU path for matrix-eigenvalue extraction
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')  # CPU fallback cap

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. Phonon-first sector CC residue from S85 1A solo:
     `sessions/archive/session-85/computations-artifacts/s85_w<X>_phonon_first_cc_residue.npz`
     SHA: <RUNTIME-LATE-BIND from S85 1A phonon-first solo verdict>
  2. Transit sector CC residue from S85 1A solo:
     `sessions/archive/session-85/computations-artifacts/s85_w<X>_transit_cc_residue.npz`
     SHA: <RUNTIME-LATE-BIND from S85 1A transit solo verdict>
  3. Landau sector CC residue from S85 1A solo:
     `sessions/archive/session-85/computations-artifacts/s85_w<X>_landau_cc_residue.npz`
     SHA: <RUNTIME-LATE-BIND from S85 1A landau solo verdict>
  4. Routing key for §VII.R registry slot (NCG-Meta-Theorem landing):
     `sessions/permanent-results-registry.md` §VII.R
     SHA: <RUNTIME-LATE-BIND from W1a T2>

Computation steps:
  Step A. Load each sector's CC residue r_i ∈ {r_phonon, r_transit, r_landau}
          along with its (scheme, convention, L_max, regulator) tag-tuple.
  Step B. Verify all three solos used the SAME L_max=10 and the SAME
          regulator family (Mellin / heat-kernel / spectral-action); if any
          sector deviates, abort and emit INFO with reason.
  Step C. Compute the three pre-registered combination rules:
            R_arith = (1/3) Σ r_i                   # arithmetic mean
            R_geom  = (Π r_i)^(1/3)                  # geometric mean
            R_wEVOI = Σ w_i · r_i, w_i = EVOI(sector_i) / Σ EVOI(sector_j)
                      with EVOI weights pinned in §0.10 (machinery).
  Step D. Compute pairwise RATIO disagreements:
            d_ij = |r_i - r_j| / max(|r_i|, |r_j|)  for (i,j) ∈ pairs
          and d_max = max_{i,j} d_ij.
  Step E. Cross-check: re-derive R_arith via independent pathway (pin the
          three sector residues into a separate computation utility
          `_cc_residue_consensus.py` if it exists; otherwise inline the
          consensus arithmetic AND verify R_arith = R_arith_inline to
          machine epsilon).
  Step F. Compute closure SHA: SHA-256 of the ordered input-pin map
          {r_phonon_sha, r_transit_sha, r_landau_sha, vii_R_routing_sha,
          combination_rule_pin, EVOI_weights_pin}.

Decision rule (PASS/FAIL/INFO):
  PASS if d_max ≤ 1e-2 (RATIO tolerance) AND all three combination rules
       agree to 1e-2 RATIO (R_arith ≈ R_geom ≈ R_wEVOI):
       joint CC residue is the CONSENSUS value (report all three; the
       canonical entry is R_wEVOI per §0.10 pin).
  INFO if 2 of 3 sectors agree to 1e-2 but the third deviates by > 1e-2
       (one-sector outlier; document which sector and the deviation
       magnitude; do NOT promote the consensus to canonical until the
       outlier is reconciled in S87+).
  FAIL if no two sectors agree to 1e-2 RATIO (no consensus exists; CC
       residue is sector-method-DEPENDENT, which closes the
       substrate-canonical interpretation).

Verdict line append (atomic, single open("a") write):
  S86-JOINT-CC-RESIDUE-COMPUTE: <PASS|FAIL|INFO> -- value=<R_wEVOI> \\
    scheme=<consensus|outlier|none> convention=<wEVOI> L_max=10 \\
    sha256=<64-char closure>

Plus dual-SHA companion comment row (per gate-verdicts.md):
  # content_sha256=<64-char> audit_sha256=<64-char>

Output file targets:
  computations/s86_w7_joint_cc_residue.py
  computations/s86_w7_joint_cc_residue.npz   (sector residues + combos)
  computations/s86_w7_joint_cc_residue.png   (3-bar comparison plot)
  computations/s86_gate_verdicts.txt         (canonical verdict append)

GPU path: torch.linalg for any matrix-eigenvalue extraction in the
3-sector CC residue cross-check (none of the inputs require it directly
since the residues are scalars; if the cross-check pipeline re-derives
any sector from raw D_K, route via torch.linalg on RX 9070 XT).
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (canonical) |
| `scheme` | per-sector CC residue scheme as recorded in each S85 1A solo verdict; combination scheme = `consensus` |
| `convention` | `wEVOI` for canonical entry; `arith` and `geom` reported as cross-checks |
| `n_eval` | 1 per sector (residue is a scalar) |
| `scan_range` | N/A (no scan; aggregation only) |
| `tolerance` | RATIO ≤ 1e-2 for cross-sector agreement; RATIO ≤ 1e-2 for cross-rule agreement |
| `random_seed` | None (deterministic aggregation) |
| `GPU path` | `torch.linalg` on RX 9070 XT if cross-check pipeline re-derives any sector from D_K; otherwise CPU with `OMP_NUM_THREADS=8` |
| `EVOI_weights` | w_phonon, w_transit, w_landau pinned at runtime from `sessions/evoi-framework.md` (frozen since S66; W15 P13 will refresh post-S86); pin SHA captured in closure |
| `combination_rule_pin` | three rules computed: arith / geom / wEVOI; canonical = wEVOI |
| `vii_R_routing_sha` | from W1a T2 (late-bind) |
| `input_solo_shas` | three sector SHAs from S85 1A 3-solo (late-bind) |

PRU Class-8 status: every parameter pinned EXCEPT the four `<RUNTIME-LATE-BIND>`
SHAs, which are runtime-resolvable (the source artifacts exist in S85 close).
This is acceptable per `.claude/rules/epistemic-discipline.md` §Pre-Registration
Completeness: late-bind input SHAs are NOT PRU Class-8 (which requires plan-time
unpinnable machinery); they are pinned-at-runtime per the dynamic-input convention.

### 8. Expected output 4-tuple
`(value=<R_wEVOI>, scheme=consensus|outlier|none, convention=wEVOI, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS**: `d_max ≤ 1e-2` (RATIO across 3 sectors) AND `|R_arith − R_geom|/|R_wEVOI| ≤ 1e-2` AND `|R_arith − R_wEVOI|/|R_wEVOI| ≤ 1e-2`.
- **INFO**: exactly 2 of 3 pairwise distances `d_ij ≤ 1e-2`, the third `d_ik > 1e-2` (one-sector outlier band, 1e-2 < d_ik ≤ 1e-1).
- **FAIL**: no pair satisfies `d_ij ≤ 1e-2`, OR any pair has `d_ij > 1e-1`.

Tolerance-rule class: RATIO (per `.claude/rules/gate-verdicts.md` PRDR
machinery enumeration).

### 10. Substitution chain (MANDATORY — consensus-band direction)

```
Definition 1: r_i = CC_residue(sector_i, L_max=10, scheme_i, convention_i)
              for i ∈ {phonon, transit, landau}, each from its S85 1A solo.

Definition 2: R_wEVOI = Σ_i w_i · r_i
              where w_i = EVOI(sector_i) / Σ_j EVOI(sector_j)
              and EVOI weights pinned from sessions/evoi-framework.md.

Definition 3: d_ij = |r_i − r_j| / max(|r_i|, |r_j|), pairwise RATIO distance.

Definition 4: PASS predicate
              P_pass = (max_{i,j} d_ij ≤ 1e-2)
                     AND (|R_arith − R_geom|/|R_wEVOI| ≤ 1e-2)
                     AND (|R_arith − R_wEVOI|/|R_wEVOI| ≤ 1e-2).

Step 1 (substitute the three solo residues into d_ij):
  d_phonon,transit = |r_phonon − r_transit| / max(|r_phonon|, |r_transit|)
  d_phonon,landau  = |r_phonon − r_landau|  / max(|r_phonon|, |r_landau|)
  d_transit,landau = |r_transit − r_landau| / max(|r_transit|, |r_landau|)

Step 2 (substitute into R_wEVOI):
  R_wEVOI = w_phonon · r_phonon + w_transit · r_transit + w_landau · r_landau
          = (Σ w_i · r_i) with w_i ≥ 0 and Σ w_i = 1.

Step 3 (simplify the consensus-band condition):
  If d_max ≤ 1e-2 then |r_i − r_j| ≤ 1e-2 · max(|r_i|, |r_j|) for all (i,j).
  Combining with R_wEVOI = convex combination (w_i ≥ 0, Σ w_i = 1):
    min(r_i) ≤ R_wEVOI ≤ max(r_i)
    => |R_wEVOI − r_i| ≤ max(r_j) − min(r_j) ≤ 1e-2 · max(|r_j|).
  Hence R_wEVOI ∈ [r_min, r_max], a band of RATIO width ≤ 1e-2.

Step 4 (read direction from canonical form):
  PASS ⟺ d_max ≤ 1e-2 (consensus tight) AND inter-rule agreement ≤ 1e-2.
  INFO ⟺ exactly one sector falls outside the 1e-2 band (outlier).
  FAIL ⟺ no consensus (sector-method-dependence of CC residue).

Conclusion: a PASS verdict directly establishes that the CC residue is a
substrate-canonical quantity (sector-method-invariant within 1% RATIO).
A FAIL closes the canonical interpretation: CC residue would then be a
sector-bookkeeping artifact, not a spectral observable.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: pins joint CC residue as substrate-canonical 3-sector consensus
  quantity, eligible for §VII.R registry landing as a Lizzi-track structural
  result. Routing key from W1a T2 §VII.R becomes the canonical SHA for the
  joint value. Closes the "is CC residue sector-method-dependent?" open
  question raised in S85 1A 3-solo synthesis. Strengthens the substrate-spectral
  derivation chain (D_K → spectral moments → CC channel residue → emergent
  observable).
- **INFO**: one-sector outlier flagged; canonical entry deferred. The outlier
  sector becomes an S87 carry-forward computation (re-derive that sector's CC
  residue under canonical L_max=10 + canonical regulator family). Not a
  framework-eliminating result; just an unfinished aggregation.
- **FAIL**: no sector-consensus exists. CC residue is sector-method-DEPENDENT,
  which closes the "CC residue as substrate-canonical observable" interpretation
  and forces the framework to treat CC-channel residue as a per-sector quantity
  with no joint reduction. Downstream gates that cite "the" CC residue (W12 P7
  CGWB-ρ Monte Carlo, W14 watchlist Row #7 ρ_AC) would need re-spec under
  per-sector residue maps.

### 12. Effort estimate
~2-4h runtime. Dominated by input-SHA pinning + cross-check pipeline
construction; the aggregation arithmetic itself is O(1). If S85 1A 3-solo
output artifacts must be re-computed under canonical pin discipline (e.g.,
one solo used a non-canonical L_max), add 2-4h per re-computed sector
(maximum +12h if all three sectors need re-derivation).

### 13. Substrate-framing reminder
CC residue is a **substrate-spectral quantity**: the residue of the spectral
action's CC-channel pole at the Jensen-deformed fold, derived from the D_K
eigenvalue distribution via heat-kernel / Mellin-Barnes. The three sectors
(phonon-first / transit / landau) are three substrate-bookkeeping schemes for
extracting the SAME underlying spectral quantity — NOT three different
physical processes. The joint value PASS confirms substrate-bookkeeping
invariance; FAIL confirms sector-bookkeeping dependence (NOT a sign that
"the CC is wrong" — only that "CC residue" is not the right canonical name
for a sector-invariant scalar). Direction of explanation: D_K eigenvalues →
spectral action moments → CC-channel residue → joint value. NEVER frame as
"the cosmological constant lives at the EW scale and the three sectors
measure it differently".

---

## §W7-2. S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE (C4)

### 1. Gate ID
`S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE` (carry-forward: C4, source
gen-physicist 9A §4.8)

### 2. Trigger
`[VERIFY]` — numerical agreement of the branch-c mechanism-specific 10×
ABSOLUTE ratio against the pre-registered 10× threshold. The substitution
chain is mandatory because the gate makes a direction claim about ratio
magnitude (≥ 10× ABSOLUTE).

### 3. Classification
**PHONONIC**. Branch-c is a phonon-mechanism candidate (post-W12-3
inverted-Josephson retraction; formal naming pinned at W4 P4
BRANCH-IV-FORMULATION-COMMIT). The discriminator probes
mechanism-specificity: whether branch-c's signature observable is
distinguishable from sibling phonon-mechanism candidates (volovik
superfluid-universe variant, landau condensed-matter variant, kaku
speculative variant). All three siblings are excitations of the SAME
substrate fabric; the question is whether their spectral / response
signatures differ by ≥10× ABSOLUTE on the chosen observable.

### 4. Agent type
**Runtime primary**: `volovik-superfluid-universe-theorist` (the volovik
sector originates the canonical branch-c naming via 3He-B inheritance per
the project's substrate-compaction lineage). The planner-level orchestration
sits with `gen-physicist` because the gate spans three sibling specialists.

**Cross-cited companions** (consulted via input-SHA pins from S85 3B 3-solo,
NOT spawned as collab agents):
- `landau-condensed-matter-theorist` (landau sibling-mechanism observable
  prediction from S85 3B solo)
- `kaku-speculative-theorist` (kaku sibling-mechanism observable prediction
  from S85 3B solo)

The runtime dispatch is single-agent (volovik-superfluid-universe-theorist)
consuming three sibling-specific input artifacts.

### 5. Hypothesis
The branch-c phonon mechanism produces a signature observable whose magnitude
exceeds the corresponding observable for each of its two sibling mechanisms
(landau, kaku) by a factor ≥ 10× ABSOLUTE, demonstrating that branch-c is
observably distinct (mechanism-specifically discriminable) and not a
re-bookkeeping of either sibling.

### 6. Method (complete dispatch prompt for runtime)

```
Dispatch prompt for `volovik-superfluid-universe-theorist`:

You are computing the branch-c phonon mechanism-specific discriminator per
S86-W7-2 (S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE, carry-forward C4
from gen-physicist 9A §4.8).

Required imports:
  from canonical_constants import *
  import numpy as np
  import torch  # GPU for any matrix work
  import hashlib
  import json
  import os
  os.environ.setdefault('OMP_NUM_THREADS', '8')

"Branch-c" definition resolution:
  Branch-c is the phonon mechanism formally named in the W4 P4
  BRANCH-IV-FORMULATION-COMMIT. The naming convention is:
    branch-(iv) = legacy umbrella from W12-3 inverted-Josephson retraction;
                  retired at W4 P4.
    branch-c    = the surviving phonon-channel mechanism after the retraction.
  Resolve the canonical name from W4 P4 verdict; SHA-pin the naming
  convention into the closure.

Inputs (load + SHA-pin in first 20 lines of stdout):
  1. Branch-c (volovik) signature observable from S85 3B solo:
     `sessions/archive/session-85/computations-artifacts/s85_w<X>_volovik_branchc_signature.npz`
     SHA: <RUNTIME-LATE-BIND from S85 3B volovik solo verdict>
  2. Landau sibling-mechanism observable from S85 3B solo:
     `sessions/archive/session-85/computations-artifacts/s85_w<X>_landau_sibling_signature.npz`
     SHA: <RUNTIME-LATE-BIND from S85 3B landau solo verdict>
  3. Kaku sibling-mechanism observable from S85 3B solo:
     `sessions/archive/session-85/computations-artifacts/s85_w<X>_kaku_sibling_signature.npz`
     SHA: <RUNTIME-LATE-BIND from S85 3B kaku solo verdict>
  4. W4 P4 BRANCH-IV-FORMULATION-COMMIT verdict for naming-convention SHA:
     `computations/s86_gate_verdicts.txt` line for S86-BRANCH-IV-...
     SHA: <RUNTIME-LATE-BIND from W4 P4>

Computation steps:
  Step A. Load each sibling's signature observable O_i ∈
          {O_volovik, O_landau, O_kaku} along with its (scheme, convention,
          L_max, observable_class) tag-tuple.
  Step B. Verify all three solos predict the SAME observable class (e.g.,
          all three predict an Ω_GW(f) at f_LISA = 3 mHz, OR all three
          predict an n_s deviation, OR all three predict a CGWB amplitude
          at the same f_pivot). If observable classes differ, abort and
          emit INFO with reason: "sibling observables not commensurable".
  Step C. Compute the two ABSOLUTE ratios (branch-c relative to each sibling):
            R_vL = |O_volovik| / |O_landau|          # branch-c vs landau
            R_vK = |O_volovik| / |O_kaku|             # branch-c vs kaku
          Use ABSOLUTE ratio (not RATIO-of-RATIOs) because the discriminator
          is a magnitude-dominance claim, not a relative-deviation claim.
  Step D. Compute the minimum dominance ratio:
            R_min = min(R_vL, R_vK).
          The PASS criterion fires on R_min ≥ 10 (branch-c dominates BOTH
          siblings by ≥ 10× ABSOLUTE).
  Step E. Cross-check (anti-cherrypick): also compute the inverse ratios
            R_Lv = |O_landau|  / |O_volovik|
            R_Kv = |O_kaku|    / |O_volovik|
          and verify R_Lv ≤ 0.1 AND R_Kv ≤ 0.1 (mechanical consistency of
          the dominance claim). If R_min ≥ 10 BUT either R_Lv > 0.1 or
          R_Kv > 0.1, abort with FAIL-CONSISTENCY (signals a per-observable
          arithmetic error in one of the input solos).
  Step F. Compute closure SHA: SHA-256 of the ordered input-pin map
          {volovik_sha, landau_sha, kaku_sha, branchc_naming_sha,
          observable_class_pin, ratio_basis_pin}.

Decision rule (PASS/FAIL/INFO):
  PASS if R_min ≥ 10 AND R_Lv ≤ 0.1 AND R_Kv ≤ 0.1: branch-c is observably
       discriminated from BOTH siblings by ≥ 10× ABSOLUTE.
  INFO if 5 ≤ R_min < 10 (intermediate dominance band; branch-c is
       distinguishable but does not meet the canonical 10× threshold;
       eligible for promotion if a sibling's observable is later refined
       downward).
  FAIL if R_min < 5: branch-c is NOT observably discriminated from at least
       one sibling at any reasonable ABSOLUTE threshold.

Verdict line append (atomic, single open("a") write):
  S86-BRANCH-C-MECHANISM-DISCRIMINATING-GATE: <PASS|FAIL|INFO> -- \\
    value=<R_min> scheme=ABSOLUTE-min-dominance \\
    convention=branch-c-vs-{landau,kaku} L_max=10 \\
    sha256=<64-char closure>

Plus dual-SHA companion comment row:
  # content_sha256=<64-char> audit_sha256=<64-char>

Output file targets:
  computations/s86_w7_branchc_discriminator.py
  computations/s86_w7_branchc_discriminator.npz   (3 observables + ratios)
  computations/s86_w7_branchc_discriminator.png   (3-bar magnitude plot)
  computations/s86_gate_verdicts.txt              (canonical verdict append)

GPU path: torch.linalg if any sibling observable requires re-derivation
from raw D_K spectral data (e.g., re-extracting an Ω_GW spectrum from
mode-by-mode Bogoliubov coefficients). Cap CPU threads at 8 if GPU
unavailable.
```

### 7. Machinery pin (PRDR — every free parameter)

| Parameter | Pin |
|:----------|:----|
| `L_max` | 10 (canonical) |
| `scheme` | per-sibling observable scheme as recorded in each S85 3B solo verdict; discriminator scheme = `ABSOLUTE-min-dominance` |
| `convention` | `branch-c-vs-{landau,kaku}` (volovik = canonical branch-c host) |
| `n_eval` | 1 per sibling observable (scalar magnitude per sibling) |
| `scan_range` | N/A (no scan; ratio-of-magnitudes only) |
| `tolerance` | ABSOLUTE: PASS at R_min ≥ 10; INFO at 5 ≤ R_min < 10; FAIL at R_min < 5 |
| `random_seed` | None (deterministic ratio) |
| `GPU path` | `torch.linalg` on RX 9070 XT for any re-derivation of a sibling observable from raw D_K; otherwise CPU with `OMP_NUM_THREADS=8` |
| `observable_class_pin` | the observable class chosen for the discriminator (Ω_GW @ f_LISA, n_s deviation, CGWB amplitude @ f_pivot, etc.) — pinned from the SHARED observable across the three S85 3B solos; if solos predict different classes, INFO with reason |
| `ratio_basis_pin` | `ABSOLUTE` (not RATIO-of-RATIOs) — pinned because the gate is a magnitude-dominance claim |
| `branchc_naming_sha` | from W4 P4 (late-bind) |
| `input_solo_shas` | three sibling SHAs from S85 3B 3-solo (late-bind) |

PRU Class-8 status: every parameter pinned EXCEPT the four `<RUNTIME-LATE-BIND>`
SHAs, which are runtime-resolvable from S85 3B + S86 W4 P4 outputs.

### 8. Expected output 4-tuple
`(value=<R_min>, scheme=ABSOLUTE-min-dominance, convention=branch-c-vs-{landau,kaku}, L_max=10)`

### 9. PASS/FAIL/INFO thresholds (with tolerance rule)

- **PASS**: `R_min ≥ 10` AND `R_Lv ≤ 0.1` AND `R_Kv ≤ 0.1`. Branch-c
  dominates BOTH sibling-mechanism observables by ≥ 10× ABSOLUTE.
- **INFO**: `5 ≤ R_min < 10`. Branch-c is distinguishable from both siblings
  but does not meet the canonical 10× ABSOLUTE threshold. Promotable if a
  sibling's observable is later refined downward (or if an updated
  observable-class measurement shifts one sibling's prediction).
- **FAIL**: `R_min < 5`, OR consistency check fails (`R_Lv > 0.1` while
  `R_min ≥ 10`, or symmetric for `R_Kv`). Branch-c is NOT observably
  discriminated from at least one sibling at any reasonable ABSOLUTE threshold.

Tolerance-rule class: ABSOLUTE (per the magnitude-dominance specification —
RATIO would mis-spec the gate by allowing both observables to scale together
without affecting the dominance ratio).

### 10. Substitution chain (MANDATORY — ratio-magnitude direction)

```
Definition 1: O_i = signature_observable(sibling_i, L_max=10, scheme_i,
              convention_i, observable_class_pin) for i ∈ {volovik (= branch-c),
              landau, kaku}, each from its S85 3B solo.

Definition 2: R_vL = |O_volovik| / |O_landau|     (branch-c over landau)
              R_vK = |O_volovik| / |O_kaku|        (branch-c over kaku)

Definition 3: R_min = min(R_vL, R_vK)              (worst-case dominance)

Definition 4: PASS predicate
              P_pass = (R_min ≥ 10)
                     AND (|O_landau|/|O_volovik| ≤ 0.1)   # consistency
                     AND (|O_kaku|  /|O_volovik| ≤ 0.1).  # consistency

Step 1 (substitute the three sibling magnitudes into R_vL, R_vK):
  R_vL = |O_volovik| / |O_landau|
  R_vK = |O_volovik| / |O_kaku|

Step 2 (substitute into R_min):
  R_min = min(|O_volovik|/|O_landau|, |O_volovik|/|O_kaku|)
        = |O_volovik| / max(|O_landau|, |O_kaku|)

Step 3 (simplify the consistency cross-check):
  If R_min ≥ 10, then |O_volovik| ≥ 10 · max(|O_landau|, |O_kaku|),
  hence |O_landau|/|O_volovik| ≤ 1/10 = 0.1 and
        |O_kaku|  /|O_volovik| ≤ 1/10 = 0.1
  identically. The consistency cross-check is REDUNDANT in exact arithmetic
  but catches per-solo input errors (a typo in one input file's magnitude
  field that breaks the inverse identity).

Step 4 (read direction from canonical form):
  PASS ⟺ |O_volovik| ≥ 10 · max(|O_landau|, |O_kaku|)
       (branch-c dominates BOTH siblings by ≥ 10× ABSOLUTE).
  INFO ⟺ 5 ≤ R_min < 10 (intermediate dominance band).
  FAIL ⟺ R_min < 5 (no observable discrimination at any reasonable
       ABSOLUTE threshold) OR consistency cross-check failure.

Conclusion: a PASS verdict directly establishes that branch-c is a
mechanism-specifically discriminable phonon channel (not a re-bookkeeping
of landau or kaku siblings). A FAIL closes the "branch-c as observably
distinct phonon mechanism" interpretation: branch-c would then be either
(a) observationally degenerate with one of its siblings, or (b)
sub-discriminator at the ABSOLUTE threshold and require a more sensitive
observable class to test.
```

### 11. What PASSES/FAILS MEAN for solution space

- **PASS**: confirms branch-c phonon mechanism is observably distinct from
  sibling mechanisms (landau, kaku) at the 10× ABSOLUTE threshold.
  Strengthens branch-c mechanism credibility within the substrate
  framework's mechanism inventory. Eligible for promotion to the
  `sessions/framework/registry/falsifier-master-inventory.md` watchlist (W14 W6
  NEW row class) as a discriminating prediction. Pins the W4 P4
  BRANCH-IV-FORMULATION-COMMIT naming convention as observationally
  load-bearing (not just bookkeeping).
- **INFO**: branch-c distinguishable but below the canonical 10× threshold.
  Carry-forward to S87 with a sharpened observable-class proposal
  (e.g., switch from Ω_GW @ f_LISA to Ω_GW @ f_LiteBIRD, where sibling
  predictions diverge more strongly). NOT a framework-eliminating result;
  intermediate-band finding.
- **FAIL**: branch-c is NOT observably discriminable from at least one
  sibling at the ABSOLUTE threshold. Closes the "branch-c as observably
  distinct mechanism" interpretation under the chosen observable class.
  The framework retains branch-c as a structural-bookkeeping entity (it
  may still be the correct mechanism), but it loses status as a
  near-term observational discriminator. Downstream watchlist entries
  citing branch-c-specific predictions (W13 P11 master-inventory; W14
  W6 NEW row class) need re-spec under sibling-degenerate framing.

### 12. Effort estimate
~2-4h runtime. Dominated by (a) input-SHA pinning across three sibling
solos + W4 P4 naming SHA, and (b) observable-class commensurability check
(verifying that all three solos predict the SAME observable). The
ratio-of-magnitudes arithmetic itself is O(1). If sibling solos predict
different observable classes (Step B abort path), the gate emits INFO and
the carry-forward is "re-run S85 3B solos under shared observable-class
pin" — cost is in S87, not in W7-2.

### 13. Substrate-framing reminder
Branch-c is a **phonon-mechanism candidate**: a relay-pattern excitation
channel of the substrate fabric, not a "particle in a container".
The discriminator probes substrate-mechanism specificity — whether
branch-c's spectral / response signature differs from sibling
mechanisms (volovik / landau / kaku variants of the SAME substrate).
All three siblings are excitations of the SAME substrate fabric (the
Jensen-deformed SU(3) spectral triple); the question is which spectral
moment / response coefficient acts as the canonical observable
fingerprint. PASS confirms substrate-mechanism specificity at the 10×
ABSOLUTE level; FAIL confirms observational degeneracy under the chosen
observable class. Direction of explanation: D_K eigenvalues → mechanism-
specific spectral moment → observable signature → ratio. NEVER frame as
"branch-c is a particle that interacts differently than landau-particles
in spacetime".

---

## §X. Wave W7 → Downstream Decision Point

W7 outputs feed three downstream wave / registry slots:

1. **C1 PASS** lands joint CC residue at the §VII.R registry slot defined by
   W1a T2 (NCG-Meta-Theorem landing). Routing key inherited from T2's
   pinned SHA. Joint value becomes a substrate-canonical Lizzi-track
   structural result citable by downstream gates that reference "the" CC
   residue (notably W12 P7 CGWB-ρ Monte Carlo and W14 W3 watchlist
   ρ_AC row).
2. **C1 INFO / FAIL** routes to S87 carry-forward as either (INFO)
   "re-derive outlier sector under canonical pin discipline" or (FAIL)
   "re-spec downstream gates that cite 'the' CC residue under per-sector
   residue maps".
3. **C4 PASS** strengthens branch-c phonon mechanism credibility within
   the substrate framework's mechanism inventory. Promotable to the
   `sessions/framework/registry/falsifier-master-inventory.md` watchlist as a
   discriminating prediction (W14 W6 NEW row class slot). Pins W4 P4
   BRANCH-IV-FORMULATION-COMMIT naming as observationally load-bearing.
4. **C4 INFO / FAIL** routes to S87 with either (INFO) "sharpen
   observable-class proposal so siblings diverge more strongly" or (FAIL)
   "re-spec branch-c-specific watchlist entries under sibling-degenerate
   framing".

W7 has NO same-session downstream wave dependency — it does not gate any
W8-W15 wave's plan-write or compute. It feeds REGISTRY and WATCHLIST slots
maintained in W13 / W14 / W15 (which read the verdict file independently
at compute time).

---

## §0.10. Wave W7 Machinery-Enumeration Pin

| Gate | Parameter | Pin | PRU class |
|:-----|:----------|:----|:----------|
| W7-1 (C1) | L_max | 10 | none (canonical) |
| W7-1 (C1) | scheme | per-sector + `consensus` aggregation | none (pinned) |
| W7-1 (C1) | convention | `wEVOI` canonical; `arith` + `geom` cross-checks | none (pinned) |
| W7-1 (C1) | tolerance | RATIO ≤ 1e-2 (pairwise) AND RATIO ≤ 1e-2 (cross-rule) | none (pinned) |
| W7-1 (C1) | EVOI weights | snapshot from `sessions/evoi-framework.md` at runtime; SHA captured in closure | none (runtime-pinned) |
| W7-1 (C1) | combination_rule_pin | `wEVOI` canonical (compute all three: arith / geom / wEVOI) | none (pinned) |
| W7-1 (C1) | GPU path | `torch.linalg` if cross-check re-derives any sector from D_K; CPU OMP=8 fallback | none (pinned) |
| W7-1 (C1) | random_seed | N/A (deterministic) | none (pinned) |
| W7-1 (C1) | input_solo_shas | three sector SHAs from S85 1A 3-solo | runtime-late-bind |
| W7-1 (C1) | vii_R_routing_sha | from W1a T2 §VII.R registry slot | runtime-late-bind |
| W7-2 (C4) | L_max | 10 | none (canonical) |
| W7-2 (C4) | scheme | per-sibling + `ABSOLUTE-min-dominance` | none (pinned) |
| W7-2 (C4) | convention | `branch-c-vs-{landau,kaku}` (volovik = canonical branch-c host) | none (pinned) |
| W7-2 (C4) | tolerance | ABSOLUTE: PASS R_min ≥ 10; INFO 5 ≤ R_min < 10; FAIL R_min < 5; consistency R_Lv ≤ 0.1 AND R_Kv ≤ 0.1 | none (pinned) |
| W7-2 (C4) | observable_class_pin | shared observable class across 3 siblings; INFO if not commensurable | none (pinned with abort-clause) |
| W7-2 (C4) | ratio_basis_pin | ABSOLUTE (not RATIO-of-RATIOs) | none (pinned) |
| W7-2 (C4) | GPU path | `torch.linalg` if any sibling re-derived from raw D_K; CPU OMP=8 fallback | none (pinned) |
| W7-2 (C4) | random_seed | N/A (deterministic) | none (pinned) |
| W7-2 (C4) | input_solo_shas | three sibling SHAs from S85 3B 3-solo | runtime-late-bind |
| W7-2 (C4) | branchc_naming_sha | from W4 P4 BRANCH-IV-FORMULATION-COMMIT | runtime-late-bind |

PRDR completeness check: every gate-relevant machinery parameter is pinned at
plan-time except for input SHAs (acceptable per the dynamic-input convention;
not PRU Class-8 since these are runtime-resolvable from existing artifacts,
not unpinnable plan-time freedoms). No PRU Class-8 vulnerability flagged.

---

## §0.11. Wave W7 Input-SHA Ledger

| Pin slot | Source | SHA at plan-write |
|:---------|:-------|:------------------|
| W7-1 phonon-first sector CC residue | S85 1A phonon-first solo verdict line | `<RUNTIME-LATE-BIND-S85-1A-phonon>` |
| W7-1 transit sector CC residue | S85 1A transit solo verdict line | `<RUNTIME-LATE-BIND-S85-1A-transit>` |
| W7-1 landau sector CC residue | S85 1A landau solo verdict line | `<RUNTIME-LATE-BIND-S85-1A-landau>` |
| W7-1 §VII.R routing key | W1a T2 NCG-Meta-Theorem landing | `<RUNTIME-LATE-BIND-W1a-T2-VII-R>` |
| W7-1 EVOI weights snapshot | `sessions/evoi-framework.md` at compute time | `<RUNTIME-SNAPSHOT-EVOI>` |
| W7-2 volovik branch-c signature | S85 3B volovik solo verdict line | `<RUNTIME-LATE-BIND-S85-3B-volovik>` |
| W7-2 landau sibling signature | S85 3B landau solo verdict line | `<RUNTIME-LATE-BIND-S85-3B-landau>` |
| W7-2 kaku sibling signature | S85 3B kaku solo verdict line | `<RUNTIME-LATE-BIND-S85-3B-kaku>` |
| W7-2 branch-c naming convention | W4 P4 BRANCH-IV-FORMULATION-COMMIT verdict | `<RUNTIME-LATE-BIND-W4-P4>` |
| W7-1 + W7-2 canonical_constants snapshot | `computations/canonical_constants.py` at compute time | `<RUNTIME-SNAPSHOT-canonical>` |

All `<RUNTIME-LATE-BIND-*>` slots resolve at compute time via grep-by-gate-ID
on the producing verdict file, then SHA-256 of the corresponding artifact
file. The closure SHA emitted by each W7 script is the SHA-256 of the
ordered concatenation of these resolved input SHAs plus the gate's
machinery pin map. No SHA is hardcoded; no SHA is copy-pasted from a prior
verdict line.

Plan-write-time validation: this ledger has 10 pin slots × 2 gates = 10
total runtime-late-bind / runtime-snapshot resolutions. No plan-time SHAs
(this wave depends on outputs from S85 + same-session W1a / W4, all of
which post-date this plan's authoring).

---

**End of Wave W7 plan.** Two gate blocks (W7-1 C1, W7-2 C4) at full 13-field
spec. Both PHONONIC. Both [VERIFY] trigger with mandatory substitution chain.
Runtime primary agents: `phonon-first-cosmologist` (W7-1) and
`volovik-superfluid-universe-theorist` (W7-2); planner-orchestration sits with
`gen-physicist` per the multi-solo coordination rule. Compute-sequencing
prerequisites: W1a T2 (CC-residue routing) and W4 P4 (branch-c naming) must
land before W7 verdicts can be promoted to canonical; otherwise the gates
degrade to INFO with `routing_pending` / `naming_pending` flags.
