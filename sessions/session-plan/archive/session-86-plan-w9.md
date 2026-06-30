# Session 86 Plan — Wave W9: W2-2 instantiations + parity-extension + R-protection criterion

**Owner**: `gen-physicist` (planner only — runtime agents are specialists; see §0 below)
**Theme**: W2-2 mother-theorem predicted instantiations (§VII.P-prime + §VII.K-DUAL-q) + §VII.P-v2 parity refinement (HP^0-content-distinct corridors) + R-protection Mellin-moment criterion test (Level-2/3, defer-eligible).
**Item count**: 3 (C26, C24, C44).
**Verdict file (canonical)**: `computations/s86_gate_verdicts.txt` — every gate appends here using the atomic `open("a")` template, never elsewhere.

---

## §0. Wave W9 Summary

W9 closes the W2-2 mother-theorem registry by computing the two PREDICTED instantiations the mother-theorem entry left as forward-pointers (C26), refines §VII.P parity-blindness into the HP^0-content-distinct §VII.P-v2 plus an odd-parity sibling §VII.P' (C24), and tests the most ambitious 4-line proposal in lizzi S-1 §IV.5 — the Mellin-moment criterion for R-protection — against the S80 W0-9 184-entry empirical RATIO/ABSOLUTE/MIXED classification (C44).

**Subagent assignment** (per-gate, NOT gen-physicist at runtime):
- **C26** → `connes-ncg-theorist` (Spin(8) extension of SU(3); HP^k cohomology with k=3, rank=2; q-deformation of HP^even). Backup: `lizzi-spectral-functional-theorist` if Spin(8) representation theory bandwidth exhausted.
- **C24** → `connes-ncg-theorist` (HP^0 content + (C_H, C_epsH) twin-pair structure originate in NCG corridor classification). Cross-source includes lizzi S-7 §V.11 (odd-parity GV diagnostic).
- **C44** → `lizzi-spectral-functional-theorist` (lizzi S-1 §IV.5 originator; criterion is a Mellin-moment statement on the spectral-functional ledger).

**C44 defer-eligibility**: if W9 cumulative wall time exceeds 14h or C26+C24 spill above 11h combined, dispatch C44 in S87 W-aux instead. The defer rule fires on plan-time spend, not on PASS/FAIL outcome. Defer is registered as INFO-DEFER in the verdict file (not FAIL).

**Substrate framing reminder**: All three gates measure GEOMETRIC walls. C26 confirms two corollary-class instantiations of the substrate's HP^even Pontryagin structure. C24 sharpens which equivalence-class twins the substrate's spectral-triple permits in the §VII.P parity register. C44 tests whether the substrate's R-protection structure is captured by a 3-Mellin-moment criterion. Each is a property of the substrate's spectral-triple + HP-cohomology structure, NOT a property of fields living in a container spacetime.

---

## §0.5. Wave W9 Decision-Point Prerequisites

W9 has TWO upstream plan-write dependencies (the planners can write in parallel; the runtime agents enforce sequencing):

| Prerequisite | Source wave | What W9 reads | Reason |
|:-------------|:------------|:--------------|:-------|
| T2 `S86-VII-R-NCG-META-THEOREM-LANDING` (§VII.R registry slot) | W1a | NCG-Meta-Theorem registry SHA + 3-axis disjointness table + cross-pair note to §VII.S | C26 instantiations are corollary-class to the W2-2 mother-theorem; they MUST cite the §VII.R registry slot or the registry write is orphan-cited. C24 §VII.P-v2 refinement also routes through §VII.R parity-axis. |
| T10 `S86-FI-RD-PERMANENT-REGISTRY` (60-row composite atlas) | W1c | The 60-row M_lizzi composite atlas (FI/RD 18 + S82 42, M_connes conflict-checked) | C44 R-protection criterion is tested against the 184-entry W0-9 catalog (a substrate of the FI/RD M_connes composite); the M_lizzi conflict-check pin must land before C44 runs to ensure the empirical-classification baseline is itself coherent. |

**Compile-time enforcement at runtime** (not at plan-write): the C26/C24/C44 producing scripts read T2 and T10 closure-SHAs from `computations/s86_gate_verdicts.txt` as input pins. If those SHAs are absent at script invocation, the script raises `MissingUpstreamPinError` and exits 2 (script-broken, not FAIL).

---

## §I. Carry-Forward Items Mapping

| W9 gate | Source carry-forward | Source synthesis | §86-context.md row | Effort |
|:--------|:---------------------|:-----------------|:-------------------|:-------|
| C26 (W9-1) | `S86-W2-2-PREDICTED-INSTANTIATIONS` (2 sub-gates: §VII.P-prime + §VII.K-DUAL-q) | gen-physicist S-7 §V.20 | §2.4 row C26 | 6-8h total |
| C24 (W9-2) | `S86-VII-P-V2-PARITY-EXTENSION` | gen-physicist S-7 §V.18 + lizzi S-7 §V.11 | §2.4 row C24 | 4-5h MODERATE |
| C44 (W9-3) | `S86-R-PROTECTION-MELLIN-CRITERION` (Level-2/3, defer-eligible) | lizzi S-7 §V.12 | §2.4 row C44 | 8-12h HIGH |

W9 totals 18-25h combined. Combined with the 14h-or-bust defer rule on C44, the realistic in-S86 budget is C26 + C24 (10-13h) firm + C44 conditional.

---

## §W9-1. S86-W2-2-PREDICTED-INSTANTIATIONS (C26)

### 1. Gate ID
`S86-W2-2-PREDICTED-INSTANTIATIONS` (2 sub-gates: `C26.A = §VII.P-prime` and `C26.B = §VII.K-DUAL-q`)

### 2. Trigger
`[VERIFY-THEOREM]` — both sub-gates instantiate corollary-class theorems already pre-registered as predicted-instantiations in the S85 W2-2 mother-theorem entry. The trigger is theorem-grade equality / structural-class verification, not a sign-direction inference.

### 3. Classification
**GEOMETRIC** for both sub-gates. C26.A is HP^k cohomology with k=3, rank=2 on Spin(8)-extended SU(3) — pure spectral-triple structure, no substrate excitation. C26.B is HP^even bucket structure under q-deformation — a deformation property of the substrate's NCG cohomology ring.

### 4. Agent type
**Runtime agent**: `connes-ncg-theorist` (Spin(8)-extension representation theory + HP^even cohomology + q-deformation are NCG-track core; lizzi-spectral-functional-theorist holds the Mellin-axis backup but the primary structures here are HP-cohomological, not Mellin-functional). NOT gen-physicist at runtime.

### 5. Hypothesis (one sentence per sub-gate)
- **C26.A**: The W2-2 mother-theorem's predicted instantiation §VII.P-prime, namely "the HP^3 cohomology class (k=3, rank-2) of the Spin(8)-extended SU(3) spectral triple lifts the §VII.P parity-blindness wall to a strict structural exclusion at rank-2", evaluates to the predicted theorem-grade equality (or fails to instantiate, identifying the obstruction).
- **C26.B**: The W2-2 mother-theorem's predicted instantiation §VII.K-DUAL-q, namely "under q-deformation in the range q ∈ (0, 1), the HP^even cohomology of the deformed SU(3) spectral triple decomposes into exactly 4 buckets (HP^0, HP^2, HP^4, HP^6) with bucket boundaries q-independent up to O(1−q)^2", evaluates to the predicted 4-bucket decomposition with bucket-boundary stability inside the predicted q-band (or refutes one or both).

### 6. Method (complete dispatch prompt)

```
TASK: Compute the two predicted instantiations of the S85 W2-2 mother-theorem
that were pre-registered as forward-pointers in the W2-2 registry block.

ENVIRONMENT: phonon-exflation-sim/.venv312/Scripts/python.exe with
torch 2.9.1+rocm on RX 9070 XT. For all matrix ops with dim ≥ 100,
use `torch.linalg` on GPU (eigvals / SVD / matmul). For CPU fallback,
`os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE `import numpy`.

CANONICAL CONSTANTS: `from canonical_constants import *` at the top.
If you need M_KK, tau_fold, HP1_dim, FI_parity_exclusion, rank_exclusion
(C18 W0c additions), use the imported names. Do NOT hardcode.

UPSTREAM INPUT PINS:
  - T2 §VII.R NCG-Meta-Theorem registry slot SHA from
    computations/s86_gate_verdicts.txt (read at script start; raise
    MissingUpstreamPinError + exit 2 if absent).
  - W2-2 mother-theorem PASS verdict closure-SHA from S85 verdict file
    `computations/s85_gate_verdicts.txt` (read once, pin into the
    canonical-line input map for closure-SHA computation).
  - D_K spectral cache at L_max ∈ {10, 12} (path
    computations/cache/dk_spectrum_L{Lmax}.npz).

PRDR MACHINERY (every free parameter pinned; see §7 below for full list):
  L_max = 10 (primary), 12 (cross-check)
  scheme = "ncg-cohomological" (HP-cohomology canonical)
  convention = "HP^k-Pontryagin-rank-2-Spin8-extension" (C26.A)
             = "HP^even-q-deformed-4-bucket" (C26.B)
  q_range = [0.50, 0.95, step=0.05] (C26.B; 10 q-samples)
  tolerance = 1e-10 (theorem-grade equality)
             | 1e-3 (bucket-boundary stability under (1−q)^2)
  random_seed = 0 (deterministic; no Monte Carlo in HP-cohomology compute)
  GPU path = torch.linalg.eigvals / torch.linalg.svd for HP-cohomology
             differential operator + projection matrices (typically
             dim 200-1000 at L=10).

C26.A (§VII.P-prime) METHOD:
  Step 1: Construct the Spin(8)-extended SU(3) spectral triple by lifting
          the L=10 D_K through the standard Spin(8) ⊃ SU(3) embedding
          (use the rank-2 Casimir as the lift parameter). Cite Connes-
          Chamseddine 2007 §3 inner-fluctuation invariance (already a
          §VII.S.C-θ landed registry entry per W1c C41) for the lift well-
          definedness.
  Step 2: Compute the HP^3 cohomology of the lifted triple via the
          Hochschild-Pontryagin cochain complex. PASS-criterion
          equality is `dim HP^3(A_F^Spin8) - dim HP^3(A_F^SU3) == 1`
          (the Spin(8) extension adds exactly one rank-2 generator).
  Step 3: Project the §VII.P parity-blindness equivalence relation onto
          HP^3; verify the rank-2 generator is the obstruction class
          that lifts the parity-blindness wall to strict exclusion.

C26.B (§VII.K-DUAL-q) METHOD:
  Step 1: Construct the q-deformed SU(3)_q for q in q_range using the
          standard Drinfeld-Jimbo Hopf-algebra deformation. q=1 recovers
          the undeformed SU(3) baseline (use as null check).
  Step 2: For each q, compute HP^even(A_F^q) = HP^0 ⊕ HP^2 ⊕ HP^4 ⊕ HP^6.
          Bucket decomposition uses the parity-grading on the differential
          (HP^even is the kernel of the odd-degree differential).
  Step 3: Verify bucket count == 4 at every q-sample. Verify bucket
          boundary positions (the dimensions of each HP^{2k}) are stable
          under perturbation in q with deviation ≤ tolerance · (1−q)^2.

CROSS-CHECKS (mandatory, theorem-grade):
  - L=10 vs L=12 agreement: HP^3 dimension unchanged (both gates).
  - q=1 limit: HP^even decomposition reduces to undeformed 4-bucket.
  - C26.A equation `dim HP^3(A_F^Spin8) - dim HP^3(A_F^SU3) == 1` must
    be exactly equal (no tolerance — this is a dimension count of finite-
    dim vector spaces).

OUTPUT:
  - Script: computations/s86_w9_C26_w22_predicted_instantiations.py
  - Data: computations/s86_w9_C26_hp_cohomology.npz containing
          { 'hp3_dim_su3', 'hp3_dim_spin8', 'hp_even_buckets_q': dict,
            'bucket_boundary_dims_q': dict, 'rank2_obstruction_class': array,
            'q_range_used': array, 'L_max_primary': 10, 'L_max_cross': 12,
            'closure_sha256': str }
  - Plot: computations/s86_w9_C26_bucket_stability.png — 2-panel
          (left: HP^even bucket dim vs q; right: rank-2 obstruction class
          eigenvalue vs L_max).
  - Verdict line (atomic append via template helper) to
    computations/s86_gate_verdicts.txt — emit TWO lines, one per
    sub-gate (C26.A and C26.B), plus the dual-SHA companion comment row.
```

### 7. Machinery pin (PRDR — every free parameter pinned)
- `L_max`: 10 (primary), 12 (cross-check). Justified by S85 W0-3 / W0-16 / W2-2 stability at L=10.
- `scheme`: `"ncg-cohomological"` (HP-cohomology canonical, NOT Mellin-functional).
- `convention` (C26.A): `"HP^k-Pontryagin-rank-2-Spin8-extension"`.
- `convention` (C26.B): `"HP^even-q-deformed-4-bucket"`.
- `q_range`: `[0.50, 0.55, 0.60, ..., 0.95]` (10 samples). Lower bound 0.50 chosen so that the q-deformation is non-perturbative; upper bound 0.95 so that the deformation is mild enough that bucket-boundary stability is testable to O((1−q)^2) tolerance 1e-3.
- `q_step`: 0.05 (uniform).
- `tolerance` (theorem-grade equality): `1e-10` (matches W0-3 / W2-2 stability tolerance).
- `tolerance` (bucket-boundary stability): `1e-3 · (1−q)^2`.
- `random_seed`: 0 (deterministic; no Monte Carlo in HP-cohomology compute path).
- `GPU path`: `torch.linalg.eigvals` for HP-cohomology differential spectrum; `torch.linalg.svd` for projection matrices. CPU fallback: `OMP_NUM_THREADS=8` before `import numpy`.
- `rank_exclusion`: 3 (from C18 W0c canonical-entry; pinned not recomputed).
- `Spin(8) ⊃ SU(3) embedding`: standard branching rule; cite Connes-Chamseddine 2007 §3.

### 8. Expected output 4-tuple per sub-gate

C26.A: `(value=<dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3)>, scheme="ncg-cohomological", convention="HP^k-Pontryagin-rank-2-Spin8-extension", L_max=10)`
C26.B: `(value=<bucket_count for HP^even, single integer expected to be 4>, scheme="ncg-cohomological", convention="HP^even-q-deformed-4-bucket", L_max=10)`

Both with dual-SHA companion row: `content_sha256=<64-char>` (output `.npz` content hash) + `audit_sha256=<64-char>` (closure of input-pin map).

### 9. PASS / FAIL / INFO thresholds

**C26.A**:
- **PASS**: `dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3) == 1` exactly (theorem-grade integer equality), AND the rank-2 obstruction class projects non-trivially onto §VII.P parity-blindness equivalence. Tolerance rule: THEOREM (exact integer; no margin permitted).
- **FAIL**: integer difference ≠ 1 (any other value refutes the predicted instantiation — could be 0 [extension is parity-blind], 2 [extra generator], or negative [pathology]).
- **INFO**: dimension difference == 1 BUT the rank-2 generator does not project onto parity-blindness (instantiation is dimensionally correct but structurally orthogonal — the predicted lift mechanism fails).

**C26.B**:
- **PASS**: Exactly 4 buckets in HP^even at every q in q_range, AND bucket-boundary dimensions deviate by ≤ 1e-3 · (1−q)^2 from q=1 baseline. Tolerance rule: THEOREM for bucket count (exact integer 4) + ABSOLUTE for boundary stability (1e-3 · (1−q)^2).
- **FAIL**: bucket count ≠ 4 at any q-sample, OR boundary dimensions deviate by > 1e-3 · (1−q)^2.
- **INFO**: bucket count == 4 at all q but stability tolerance is exceeded marginally (within factor 2 of threshold) — flags candidate q-deformation regime where the bucket structure starts to break.

### 10. Substitution chain (theorem-grade dimension equality — MANDATORY for C26.A magnitude claim)

```
Definitions:
  A_F^SU3   = the §VII.P parity-blind algebra of the SU(3) spectral triple
              (with §VII.P parity-blindness equivalence relation R_P)
  A_F^Spin8 = the Spin(8)-extended algebra constructed via standard
              SU(3) ⊂ Spin(8) embedding (rank-2 Casimir lift)
  HP^k(A)   = k-th Hochschild-Pontryagin cohomology of A
  e_2       = the additional rank-2 Casimir generator from Spin(8)/SU(3)
              decomposition (a degree-3 cocycle in Hochschild)

Step 1 (definition of HP^3 dimension change under extension):
  dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3)
    = dim ker(d_3 : C^3(A_F^Spin8) → C^4(A_F^Spin8))
        − dim ker(d_3 : C^3(A_F^SU3) → C^4(A_F^SU3))
        − [dim image(d_2^Spin8) − dim image(d_2^SU3)]
  where d_k is the Hochschild differential at degree k.

Step 2 (substitute Spin(8) extension structure):
  By Connes-Chamseddine 2007 §3 inner-fluctuation invariance, the algebra
  extension A_F^SU3 → A_F^Spin8 adds exactly one rank-2 generator e_2 to
  C^3, and the d_2 image is unchanged (the extension is by an inner
  automorphism, not a new boundary). Therefore:
    dim ker(d_3^Spin8) − dim ker(d_3^SU3) = 1   [the extra generator e_2]
    dim image(d_2^Spin8) − dim image(d_2^SU3) = 0  [d_2 unchanged]

Step 3 (simplify):
  dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3) = 1 − 0 = 1.

Step 4 (direction):
  The integer equality is = 1 exactly; this is a theorem-grade dimension
  count of finite-dim cohomology spaces, no tolerance.
  The substrate's spectral-triple HP^3 cohomology gains exactly one
  generator under Spin(8) lift; the §VII.P parity-blindness wall is
  STRENGTHENED to strict exclusion at rank-2 IF AND ONLY IF this
  generator projects onto the parity-blindness equivalence — which
  is a separate (orthogonal) check pre-registered as the secondary
  PASS-criterion in §9.
```

### 10b. Substitution chain (C26.B bucket count — MANDATORY for predicted-instantiation magnitude)

```
Definitions:
  A_F^q     = q-deformed SU(3) Hopf algebra at deformation parameter
              q ∈ (0, 1) (Drinfeld-Jimbo)
  HP^even(A) = HP^0(A) ⊕ HP^2(A) ⊕ HP^4(A) ⊕ HP^6(A) (parity-graded)
  γ_parity  = parity grading operator (HP^k → (−1)^k · HP^k)

Step 1 (definition of HP^even bucket count):
  bucket_count(HP^even(A_F^q)) = #{ k : dim HP^k(A_F^q) > 0 AND k even }

Step 2 (substitute spectral-triple dim and parity grading):
  At L_max = 10, the rank-2 SU(3) HP^k cohomology is non-trivial for
  k ∈ {0, 2, 4, 6} and trivial for k ∈ {8, 10, 12, ...} (rank-2
  cohomological dimension bound). Even-degree restriction keeps
  k ∈ {0, 2, 4, 6}. q-deformation is a continuous deformation of the
  Hopf product; by rigidity of cohomological dimension under continuous
  deformation (Gerstenhaber-Schack 1986), dim HP^k(A_F^q) > 0 ⇔
  dim HP^k(A_F^1) > 0 for q in a neighborhood of 1, including q ≥ 0.50
  by direct computation.

Step 3 (simplify):
  bucket_count(HP^even(A_F^q)) = #{0, 2, 4, 6} = 4  for all q in q_range.

Step 4 (direction):
  Bucket count = 4 exactly (theorem-grade integer); bucket boundary
  dimensions (the dim HP^{2k}(A_F^q) values) deviate from q=1 baseline
  by O((1−q)^2) by Gerstenhaber-Schack rigidity, which is the predicted
  stability bound. The substrate's HP^even cohomology ring under
  q-deformation has a STABLE 4-bucket structure throughout q ∈ [0.50, 0.95].
```

### 11. What PASSES / FAILS MEAN for solution space
- **C26.A PASS** confirms the W2-2 mother-theorem's predicted §VII.P-prime instantiation: the §VII.P parity-blindness wall is structurally lifted to strict exclusion at rank-2 by the Spin(8) extension. The substrate's NCG corridor classification gains a strict-exclusion entry at HP^3.
- **C26.A FAIL** refutes the predicted lift mechanism. The §VII.P parity-blindness wall remains at the LOOSE (parity-blind) level. The mother-theorem's predicted instantiation list shrinks from 2 to 1, requiring registry-write retraction in S87.
- **C26.A INFO** indicates the dimension lift exists but is structurally orthogonal — a candidate alternative §VII.P-prime spec (PROBE rank-3 instead of rank-2) becomes the S87 follow-up.
- **C26.B PASS** confirms the W2-2 mother-theorem's predicted §VII.K-DUAL-q 4-bucket HP^even decomposition. The substrate's HP^even cohomology is q-deformation-stable across the predicted q-band, reinforcing the W2-2 registry's claim that the cohomology bucket structure is deformation-rigid.
- **C26.B FAIL** refutes the 4-bucket prediction. Either the bucket count is wrong (substrate's HP^even has different parity-grading structure than W2-2 predicted) or the bucket boundaries drift faster than O((1−q)^2) (deformation-rigidity claim refuted). Either FAIL forces W2-2 mother-theorem registry-write retraction in S87.
- **Both PASS** completes the W2-2 registry by landing the two predicted instantiations as concrete §VII.P-prime + §VII.K-DUAL-q theorem entries in `sessions/permanent-results-registry.md`.

### 12. Effort estimate
6-8h total (split as ≈3-4h C26.A Spin(8) extension + HP^3 cohomology compute; ≈3-4h C26.B q-deformation 10-sample sweep + bucket boundary stability check). GPU-bound at L=10/12 cohomology spectrum compute (matrix dim ≈ 200-1000).

### 13. Substrate-framing reminder
The substrate's spectral-triple HP^3 cohomology has property `dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3) = 1` under condition `extension via standard SU(3) ⊂ Spin(8) rank-2 Casimir lift`. The substrate's HP^even cohomology has property `4-bucket decomposition with O((1−q)^2) boundary stability` under condition `q ∈ [0.50, 0.95] Drinfeld-Jimbo deformation`. Neither result is about "fields in spacetime" — both are properties of the substrate's NCG cohomology ring itself.

---

## §W9-2. S86-VII-P-V2-PARITY-EXTENSION (C24)

### 1. Gate ID
`S86-VII-P-V2-PARITY-EXTENSION` (single composite gate; lands TWO new §VII registry entries: `§VII.P-v2` and the auxiliary `§VII.P'`)

### 2. Trigger
`[VERIFY-THEOREM]` — both parity-extension sub-results land theorem-grade equivalence-class refinements (twin-pair drop + odd-parity GV diagnostic) into the §VII.P registry family. The trigger is structural-class membership verification.

### 3. Classification
**GEOMETRIC**. The §VII.P parity-blindness wall is a property of the substrate's NCG corridor equivalence relation under R_P (parity equivalence); refining the equivalence to HP^0-content-distinct corridors (§VII.P-v2) and adding an odd-parity GV diagnostic (§VII.P') are pure structural refinements of that equivalence, not particle / phononic content.

### 4. Agent type
**Runtime agent**: `connes-ncg-theorist` (HP^0 content + (C_H, C_epsH) twin-pair structure originate in NCG corridor classification; §VII.P parity-blindness wall is an NCG-track theorem). Cross-source includes `lizzi-spectral-functional-theorist` for the odd-parity GV diagnostic from S84 §W10-115 (Lizzi-track Mellin/parity-cocycle output). The connes-ncg-theorist runs the gate; lizzi is the cross-reviewer for the odd-parity GV portion. NOT gen-physicist at runtime.

### 5. Hypothesis
The §VII.P parity-blindness wall (S85 W2-7 FAIL-with-refinement) admits a refinement to §VII.P-v2 by restricting the parity-equivalence relation R_P to HP^0-content-distinct corridors (which drops (C_H, C_epsH)-type twin pairs from the equivalence-class collapse) and is paired with an auxiliary §VII.P' that uses the odd-parity GV diagnostic landed in S84 §W10-115; both sub-statements land at theorem-grade equality + odd-parity-GV criterion respectively.

### 6. Method (complete dispatch prompt)

```
TASK: Land §VII.P-v2 (refined parity-blindness wall, HP^0-content-distinct
restriction) AND auxiliary §VII.P' (odd-parity GV diagnostic from S84
§W10-115) as TWO new entries in the §VII.P registry family. Both lands
require theorem-grade structural verification before registry write.

ENVIRONMENT: phonon-exflation-sim/.venv312/Scripts/python.exe with
torch 2.9.1+rocm. Matrix ops with dim ≥ 100 use torch.linalg on GPU.
CPU fallback: `os.environ.setdefault('OMP_NUM_THREADS', '8')` BEFORE
`import numpy`.

CANONICAL CONSTANTS: `from canonical_constants import *`. Required:
HP1_dim, FI_parity_exclusion (C18 W0c additions). Add `HP0_content_dim`
to canonical_constants.py FIRST if not present (with provenance =
"S82 W2-3 + S85 W2-7 §VII.P parity-blindness adjudication").

UPSTREAM INPUT PINS:
  - T2 §VII.R NCG-Meta-Theorem registry slot SHA from
    computations/s86_gate_verdicts.txt (raise + exit 2 if absent).
  - W2-7 §VII.P parity-blindness FAIL-with-refinement closure-SHA from
    computations/s85_gate_verdicts.txt.
  - S84 §W10-115 odd-parity GV diagnostic file at
    sessions/archive/session-84/computations-artifacts/s84_w10a_115_gv_explicit.npz
    (deleted in current branch per `git status`; if not present at
    runtime, attempt restoration from session-84-final.md narrative
    and raise FileNotFoundError otherwise; do NOT fall back to a
    re-derivation, as that would be a new gate).

PRDR MACHINERY (every free parameter pinned):
  L_max = 10 (primary)
  scheme = "ncg-corridor-equivalence" (HP^0-content-distinct refinement)
  convention (§VII.P-v2) = "HP^0-content-distinct-corridor-restriction"
  convention (§VII.P')   = "odd-parity-GV-diagnostic-S84-W10-115"
  twin_pair_class        = "(C_H, C_epsH)" (the two C-class equivalence
                           pairs explicitly dropped from R_P)
  tolerance (HP^0 content distinct) = THEOREM (exact integer dim equality)
  tolerance (odd-parity GV)         = THEOREM (cocycle non-vanishing
                                       at machine epsilon ≤ 1e-12)
  random_seed = 0
  GPU path = torch.linalg for HP^0 content dim compute + GV cocycle
             eigenvalue spectrum.

§VII.P-v2 METHOD:
  Step 1: Enumerate the §VII.P parity-equivalence classes from the
          S85 W2-7 catalog. Classify each class by its HP^0 content
          (the dim of HP^0 of the corridor's spectral-triple).
  Step 2: Restrict the equivalence relation R_P to "two corridors are
          R_P-equivalent ⇔ they have the same HP^0 content AND the
          same parity grading". Identify the dropped twin pairs:
          specifically the (C_H, C_epsH) pair, which under W2-7 R_P
          was equivalent (parity-blind) but under R_P|_{HP^0-distinct}
          is now distinguished (different HP^0 dim).
  Step 3: Verify: (a) the dropped twin pairs are exactly the (C_H,
          C_epsH)-type, (b) the refined R_P|_{HP^0-distinct} is still
          an equivalence (transitive, symmetric, reflexive), (c) the
          refined wall is non-empty (some corridors remain blocked).

§VII.P' METHOD:
  Step 1: Load the S84 §W10-115 odd-parity GV diagnostic from
          s84_w10a_115_gv_explicit.npz. The diagnostic is a cocycle
          ω_GV ∈ Z^odd(A_F) representing odd-parity equivalence
          obstruction.
  Step 2: Verify ω_GV does NOT vanish on the §VII.P-v2 surviving
          corridors (i.e., ω_GV is a non-trivial obstruction to
          additional equivalence beyond R_P|_{HP^0-distinct}).
  Step 3: Land §VII.P' as the auxiliary diagnostic: "the §VII.P-v2
          equivalence is sharpened to STRICT (no further refinement
          possible) by the non-vanishing of ω_GV on surviving
          corridors". PASS iff ω_GV non-vanishes at machine epsilon.

CROSS-CHECKS (mandatory):
  - L=10 vs L=8 agreement on HP^0 content classification.
  - (C_H, C_epsH) twin pair recovery: at L=10 these two corridors
    have HP^0 dims that differ by exactly 1 (or by some other
    structurally-determined integer; PASS iff the difference matches
    the dim-count predicted by the HP^0 cohomology of the C-class
    twin construction).
  - ω_GV cocycle dimension matches S84 §W10-115 (odd-parity dimension
    must agree to integer equality).

OUTPUT:
  - Script: computations/s86_w9_C24_vii_p_v2_parity_extension.py
  - Data: computations/s86_w9_C24_parity_extension.npz containing
          { 'r_p_v2_classes', 'dropped_twin_pairs',
            'hp0_content_per_corridor', 'omega_gv_eigenvalues',
            'omega_gv_non_vanishing': bool, 'L_max': 10,
            'closure_sha256': str }
  - Plot: computations/s86_w9_C24_class_collapse.png — 2-panel
          (left: §VII.P → §VII.P-v2 equivalence-class collapse diagram;
          right: ω_GV eigenvalue spectrum with non-vanishing band).
  - Verdict line (atomic append) to computations/s86_gate_verdicts.txt
    — emit ONE composite verdict for C24 (§VII.P-v2 + §VII.P' both
    land or neither lands), with dual-SHA companion comment row.
```

### 7. Machinery pin (PRDR)
- `L_max`: 10 (primary), 8 (cross-check for HP^0 content stability).
- `scheme`: `"ncg-corridor-equivalence"`.
- `convention` (§VII.P-v2): `"HP^0-content-distinct-corridor-restriction"`.
- `convention` (§VII.P'): `"odd-parity-GV-diagnostic-S84-W10-115"`.
- `twin_pair_class`: `"(C_H, C_epsH)"` (explicitly the two equivalence pairs dropped).
- `tolerance` (HP^0 content distinct): THEOREM (exact integer dim equality, no margin).
- `tolerance` (odd-parity GV non-vanishing): THEOREM at machine epsilon `1e-12`.
- `random_seed`: 0.
- `GPU path`: `torch.linalg.eigvalsh` for ω_GV cocycle spectrum (Hermitian); `torch.linalg.matrix_rank` for HP^0 content dim count.
- `S84 W10-115 input pin`: `sessions/archive/session-84/computations-artifacts/s84_w10a_115_gv_explicit.npz` (mandatory; see exception clause in Method §6).

### 8. Expected output 4-tuple
`(value=<tuple: ((C_H, C_epsH)_dropped: bool, omega_GV_non_vanishing: bool)>, scheme="ncg-corridor-equivalence", convention="HP^0-content-distinct + odd-parity-GV", L_max=10)` — with dual-SHA companion row.

### 9. PASS / FAIL / INFO thresholds
- **PASS**: BOTH (a) the (C_H, C_epsH)-type twin pairs are dropped from R_P|_{HP^0-distinct} (verified by exact integer HP^0-dim difference), AND (b) ω_GV does not vanish on any surviving §VII.P-v2 corridor (cocycle eigenvalue spectrum bounded away from 0 by ≥ 1e-12). Tolerance: THEOREM (integer + machine-ε).
- **FAIL**: either (a) twin pairs NOT dropped (HP^0-content-distinct restriction does NOT separate (C_H, C_epsH)), OR (b) ω_GV vanishes on at least one surviving corridor (auxiliary §VII.P' refutation).
- **INFO**: §VII.P-v2 lands but §VII.P' fails (or vice versa) — partial refinement; pre-registered fallback is a single-entry §VII.P-v2-only registry write with a §VII.P' deferred-to-S87 carry-forward.

### 10. Substitution chain — N/A by §VII.P-v2 alone
No new sign/direction/threshold claim; this is a structural-class refinement, not a quantitative direction inference. The "(C_H, C_epsH) dropped" claim is a discrete-class membership statement, not a sign claim. Per `.claude/rules/math-scripts.md`, definitional/classification statements without direction claims are exempt from the substitution-chain requirement.

### 11. What PASSES / FAILS MEAN for solution space
- **PASS** completes the S85 W2-7 §VII.P parity-blindness FAIL-with-refinement carry-forward. The substrate's parity-equivalence relation is refined to its HP^0-content-distinct restriction, the (C_H, C_epsH) twin pairs are now distinguished corridors (W2-7 FAIL closes into a §VII.P-v2 PASS), and the odd-parity GV diagnostic (§VII.P') confirms no further refinement is possible. Two new §VII registry entries land; §VII.P parity-family registry is structurally complete at S86 close.
- **FAIL** indicates §VII.P-v2 is NOT the correct refinement direction. Either HP^0 content does not separate (C_H, C_epsH) (the prediction in S85 W2-7 closeout is wrong) or the GV diagnostic vanishes (the §VII.P-v2 refinement is not strict, leaving more refinement room — registry write is deferred pending a stronger refinement candidate in S87+).
- **INFO** lands the §VII.P-v2 PASS half but defers §VII.P' to S87 with explicit carry-forward.

### 12. Effort estimate
4-5h MODERATE (≈2-3h §VII.P-v2 HP^0 content classification + twin-pair drop verification; ≈1-2h §VII.P' GV cocycle non-vanishing check on the loaded S84 W10-115 artifact). GPU-bound on the GV cocycle spectrum (small matrix, but eigenvalsh).

### 13. Substrate-framing reminder
The substrate's spectral-triple corridor equivalence has property `R_P|_{HP^0-distinct} drops (C_H, C_epsH)-type twin pairs` under condition `restriction of parity-equivalence to HP^0-content-distinct corridors`. The substrate's odd-parity cohomology has property `ω_GV does not vanish on §VII.P-v2 surviving corridors` under condition `odd-parity GV diagnostic from S84 W10-115`. Both are properties of the substrate's NCG corridor structure itself — refinements of the equivalence relation, not statements about fields living in a container.

---

## §W9-3. S86-R-PROTECTION-MELLIN-CRITERION (C44 — DEFER-ELIGIBLE)

### 1. Gate ID
`S86-R-PROTECTION-MELLIN-CRITERION` (single composite gate testing the lizzi S-1 §IV.5 criterion against 184-entry empirical classification)

### 2. Trigger
`[VERIFY-THEOREM]` — the gate evaluates a candidate criterion (proof or disproof) for R-protection on the 5-atlas via Mellin moments at orders n ∈ {0, 2, 6}. Trigger is theorem-grade (the criterion is either proven equivalent to empirical R-protection or refuted on counter-examples).

### 3. Classification
**GEOMETRIC**. R-protection is a property of the substrate's spectral-functional ledger under the 5-regulator atlas; the Mellin-moment criterion proposes a 3-moment characterization of which observables are R-protected. Both the criterion and the test target are GEOMETRIC structures of the substrate's spectral-functional ring.

### 4. Agent type
**Runtime agent**: `lizzi-spectral-functional-theorist` (lizzi S-1 §IV.5 originator; criterion is a Mellin-moment statement about the spectral-functional ledger; lizzi-track owns the Mellin-axis machinery). NOT gen-physicist at runtime.

### 5. Hypothesis
The criterion proposed in lizzi S-1 §IV.5 — "an observable O is R-protected on the 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} if and only if the Mellin moments `m_n^O = 0` for all n ∈ {0, 2, 6}" — agrees with the empirical R-protection classification of the S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED catalog at the ≥95% concordance threshold (PASS), or it disagrees on ≥20% of entries (FAIL, criterion refuted), or sits in the middle band (INFO, criterion partially valid with a structural-truncation correction needed).

### 6. Method (complete dispatch prompt)

```
TASK: Test the lizzi S-1 §IV.5 R-protection Mellin-moment criterion
against the S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED empirical
classification. Either prove the criterion (≥95% concordance) or
refute it (<80% concordance). PASS / INFO / FAIL banded outcome.

DEFER-ELIGIBILITY: this gate is Level-2/3, defer-eligible. If W9
cumulative wall time exceeds 14h (across C26 + C24 + setup), or
C26 + C24 spill above 11h combined, DEFER C44 to S87 W-aux instead
of dispatching. Defer fires on plan-time spend, NOT on outcome.
On defer, append an INFO-DEFER verdict line (see §9 below) instead
of running the script.

ENVIRONMENT: phonon-exflation-sim/.venv312/Scripts/python.exe with
torch 2.9.1+rocm. Mellin moment integrals are 1-D quadratures per
observable per moment order — for 184 observables × 3 moment orders
= 552 integrals, each ≈10^4 evaluations of the spectral density.
For batched evaluation, use torch tensor ops on GPU; for serial
evaluation, CPU with `OMP_NUM_THREADS=8` BEFORE `import numpy`.

CANONICAL CONSTANTS: `from canonical_constants import *`. Required:
M_KK, tau_fold, Vol_SU3, F_4 atlas pin (5-regulator atlas constants).

UPSTREAM INPUT PINS:
  - T10 `S86-FI-RD-PERMANENT-REGISTRY` 60-row composite atlas closure-SHA
    from computations/s86_gate_verdicts.txt (raise + exit 2 if
    absent — the empirical classification baseline must be conflict-
    checked first).
  - S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED classification artifact
    (path TBD; if at sessions/archive/session-80/computations-artifacts/s80_w09_*.npz
    or the W0-9 closeout structured CSV; agent identifies path at
    runtime via knowledge MCP `search_knowledge("W0-9 184-entry
    RATIO/ABSOLUTE/MIXED")` or `trace_entity("W0-9 R-protection
    classification")`).
  - lizzi S-1 §IV.5 criterion text (already canonical; extract verbatim
    statement into the script docstring).

PRDR MACHINERY (every free parameter pinned):
  L_max                 = 10 (primary), 8 (cross-check for moment stability)
  scheme                = "Mellin-moment-criterion-test"
  convention            = "criterion-vs-empirical" (criterion-classification
                          vs S80 W0-9 empirical-classification)
  moment_orders         = (0, 2, 6) (the 3 orders specified by lizzi S-1 §IV.5)
  moment_zero_tolerance = 1e-8 (absolute; m_n^O is "zero" iff |m_n^O| < 1e-8)
  concordance_PASS      = 0.95 (≥95% of 184 entries)
  concordance_INFO_low  = 0.80 (≥80% but <95% → INFO)
  atlas_regulators      = ("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")
                          [5-regulator atlas; pinned from C28 outcome —
                          if C28 lands STRUCTURALLY-EXCLUDED on cutoff_sqrt,
                          the atlas is 4-regulator; the criterion test
                          must run on the SAME atlas as the empirical
                          classification, so pin from S80 W0-9 baseline]
  random_seed           = 0
  GPU path              = torch tensor batching for 552 Mellin integrals
                          (184 observables × 3 orders); use torch.trapz
                          or torch.einsum over discretized spectral density.

METHOD:
  Step 1 (substitution-chain definition setup):
    For each of 184 observables O_i in the W0-9 catalog:
      Compute m_n^{O_i} = ∫_0^∞ t^{n-1} f_{O_i}(t) dt
      where f_{O_i}(t) is the spectral density of O_i sampled from
      the L_max=10 D_K cache, and the integral is the Mellin transform
      at order n ∈ {0, 2, 6}.
    Use the F_4 a_4-class regulator (zeta-canonical) for the spectral
    density, or batch over all 5 atlas regulators if the criterion is
    atlas-dependent (lizzi S-1 §IV.5 specifies: criterion is on the
    5-atlas, so test the conjunction `m_n^O = 0 ∀ n ∈ {0,2,6} ∀
    regulator ∈ atlas`).

  Step 2 (criterion classification):
    For each O_i:
      criterion_R_protected_i = (|m_0^{O_i}| < tol AND |m_2^{O_i}| < tol
                                 AND |m_6^{O_i}| < tol
                                 [for all atlas regulators])

  Step 3 (empirical classification load):
    Load S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED catalog. Map
    ABSOLUTE → R-protected, RATIO → R-protected (by definition of
    a ratio observable being scheme-invariant), MIXED → not R-protected
    (mixed-support means no scheme-independence under the W0-9 W11-3
    NCG-Structural-Exclusion META-THEOREM). The empirical_R_protected_i
    flag is read from the catalog directly. (NOTE: confirm this
    RATIO/ABSOLUTE → R-protected mapping with the W0-9 closeout text;
    if the catalog uses a different mapping, pin it from the catalog.)

  Step 4 (concordance compute):
    concordance = (1/184) · Σ_i [criterion_R_protected_i ==
                                   empirical_R_protected_i]
    The 184 individual agreements form a confusion matrix:
      TP = criterion R-protected AND empirical R-protected
      TN = criterion not AND empirical not
      FP = criterion R-protected AND empirical not
      FN = criterion not AND empirical R-protected
    concordance = (TP + TN) / 184.
    Per-class breakdown: report concordance separately for RATIO,
    ABSOLUTE, MIXED subsets.

  Step 5 (verdict assignment):
    PASS iff concordance ≥ 0.95.
    INFO iff 0.80 ≤ concordance < 0.95.
    FAIL iff concordance < 0.80.

  Step 6 (counter-example enumeration on FAIL or INFO):
    For each FP and FN observable, output the (O_i, m_0, m_2, m_6,
    empirical_class) tuple to a structured CSV. These are the
    counter-examples that refute (FAIL) or partially refute (INFO)
    the criterion.

CROSS-CHECKS (mandatory):
  - L=10 vs L=8 stability of concordance: |concordance(L=10)
    − concordance(L=8)| ≤ 0.05 (5% truncation tolerance).
  - 5-atlas vs single-regulator (zeta-only) sanity: if the criterion
    holds only on a single regulator but not on the full atlas, INFO
    instead of PASS (criterion is regulator-dependent, not 5-atlas-
    universal as lizzi S-1 §IV.5 claims).
  - Per-class concordance: report RATIO/ABSOLUTE/MIXED breakdowns
    separately. If MIXED-class concordance drops below 0.50 while
    RATIO+ABSOLUTE pass at ≥0.95, the criterion is class-restricted
    (an INFO outcome with refinement note).

OUTPUT:
  - Script: computations/s86_w9_C44_r_protection_mellin_criterion.py
  - Data: computations/s86_w9_C44_criterion_test.npz containing
          { 'm_0_per_observable', 'm_2_per_observable', 'm_6_per_observable',
            'criterion_classification', 'empirical_classification',
            'concordance_total', 'concordance_RATIO', 'concordance_ABSOLUTE',
            'concordance_MIXED', 'confusion_matrix', 'counterexample_list',
            'L_max_primary': 10, 'L_max_cross': 8, 'closure_sha256': str }
  - Plot: computations/s86_w9_C44_concordance.png — 3-panel
          (left: confusion matrix heatmap; center: per-class concordance
          bars; right: m_n^O scatter plot colored by empirical class).
  - Counter-example CSV: computations/s86_w9_C44_counterexamples.csv
    (FP + FN observables with full diagnostic).
  - Verdict line (atomic append) to computations/s86_gate_verdicts.txt
    with dual-SHA companion comment row.
```

### 7. Machinery pin (PRDR)
- `L_max`: 10 (primary), 8 (cross-check for truncation stability of moments).
- `scheme`: `"Mellin-moment-criterion-test"`.
- `convention`: `"criterion-vs-empirical"`.
- `moment_orders`: `(0, 2, 6)` (verbatim from lizzi S-1 §IV.5).
- `moment_zero_tolerance`: `1e-8` ABSOLUTE (a Mellin moment is "zero" iff `|m_n^O| < 1e-8`).
- `concordance_PASS`: `0.95` (≥95% of 184 entries agree).
- `concordance_INFO_low`: `0.80` (band 0.80 ≤ concordance < 0.95 → INFO).
- `atlas_regulators`: `("zeta", "Zubarev", "SDW", "cutoff_sqrt", "anomaly")`. Pinned from S80 W0-9 baseline atlas. If C28 W4 lands STRUCTURALLY-EXCLUDED on cutoff_sqrt before C44 runs, atlas drops to 4-regulator AND the empirical classification's atlas baseline must be re-checked (an additional sub-prerequisite if C28 closes early — see §0.5).
- `random_seed`: 0.
- `GPU path`: `torch.trapz` or `torch.einsum` for batched 552-integral Mellin moment compute; `torch.linalg` for spectral-density discretization.
- `RATIO/ABSOLUTE/MIXED → R-protected mapping`: pinned from S80 W0-9 closeout text (RATIO + ABSOLUTE → R-protected; MIXED → not R-protected). If the closeout uses a different mapping, the script REPORTS the mapping it adopts and the agent flags the discrepancy.

### 8. Expected output 4-tuple
`(value=<concordance ratio in [0.0, 1.0]>, scheme="Mellin-moment-criterion-test", convention="criterion-vs-empirical", L_max=10)` — with dual-SHA companion row.

### 9. PASS / FAIL / INFO thresholds
- **PASS**: concordance ≥ 0.95 across all 184 entries AND per-class concordance ≥ 0.85 in EVERY class (RATIO, ABSOLUTE, MIXED) AND L=10 vs L=8 stability ≤ 0.05. Tolerance: ABSOLUTE on concordance threshold; THEOREM on L_max stability tolerance.
- **FAIL**: concordance < 0.80 (criterion refuted on ≥20% of entries).
- **INFO**: 0.80 ≤ concordance < 0.95 (band) — criterion partially valid; counter-example CSV identifies the offending observables; structural-truncation correction or class-restriction note becomes S87 carry-forward.
- **INFO-DEFER**: gate is deferred per Level-2/3 budget rule (W9 wall time > 14h). Verdict line: `S86-R-PROTECTION-MELLIN-CRITERION: INFO -- value=DEFER scheme=Mellin-moment-criterion-test convention=criterion-vs-empirical L_max=N/A sha256=<closure-of-defer-pin-map>` (criterion test deferred to S87 W-aux).

### 10. Substitution chain — MANDATORY for the C44 criterion-direction claim

```
Definitions:
  O                   = an observable in the S80 W0-9 184-entry catalog
  f_O(t)              = spectral density of O sampled from L_max=10 D_K
                        cache (the Mellin transform integrand)
  m_n^O               = ∫_0^∞ t^{n-1} f_O(t) dt   [Mellin moment at order n]
  R-protected (lizzi  = m_n^O = 0 ∀ n ∈ {0, 2, 6} (across the 5-atlas)
   S-1 §IV.5 candidate)
  R-protected (empi-  = O classified as RATIO or ABSOLUTE in S80 W0-9
   rical S80 W0-9)      catalog (under the W11-3 NCG-Structural-Exclusion
                        META-THEOREM mapping)

Step 1 (definition of concordance):
  concordance = (1/184) · Σ_{i=1}^{184} I[ criterion_i == empirical_i ]
  where I is the indicator function and criterion_i / empirical_i are
  the boolean R-protection labels assigned to observable O_i by the
  criterion and by the empirical catalog respectively.

Step 2 (substitute the criterion definition):
  criterion_i = I[|m_0^{O_i}| < 1e-8 AND |m_2^{O_i}| < 1e-8
                  AND |m_6^{O_i}| < 1e-8]   [for all 5 atlas regulators]
  empirical_i = I[O_i ∈ RATIO ∪ ABSOLUTE in S80 W0-9 catalog]

Step 3 (simplify):
  concordance = (1/184) · Σ_i I[ I[|m_0,2,6^{O_i}| < tol] ==
                                  I[O_i ∈ RATIO ∪ ABSOLUTE] ]

Step 4 (direction):
  PASS criterion (concordance ≥ 0.95) is interpreted as:
    The lizzi S-1 §IV.5 criterion CORRECTLY classifies R-protection
    on at least 95% of the 184 empirical observables. Direction:
    high concordance ⇒ criterion VALIDATED (Mellin-moment vanishing
    at n ∈ {0, 2, 6} is a sufficient and necessary structural signature
    of R-protection on the 5-atlas).

  FAIL (concordance < 0.80) is interpreted as:
    The criterion DISAGREES with empirical classification on ≥20% of
    observables. Direction: low concordance ⇒ criterion REFUTED
    (Mellin-moment vanishing at n ∈ {0, 2, 6} is NOT a complete
    structural signature; the criterion is missing structure or
    over-restrictive). The S87 follow-up uses the FP+FN counter-
    example CSV to propose a refined criterion (e.g., add n ∈ {4, 8}
    to the moment set, or restrict to a specific atlas subset).

  INFO band (0.80 ≤ concordance < 0.95) direction:
    Criterion is partially valid; the per-class breakdown determines
    whether the partial validity is class-restricted (e.g., works for
    RATIO + ABSOLUTE but not MIXED), atlas-restricted, or moment-set-
    restricted. The classification of the partial-validity mode is
    the S87 carry-forward.

Conclusion: the direction "criterion VALIDATED vs REFUTED" is read
off the concordance ratio at the pre-registered 0.95 / 0.80 thresholds.
The thresholds themselves are pre-registered and not adjusted post-hoc.
```

### 11. What PASSES / FAILS MEAN for solution space
- **PASS** lands a new theorem-grade structural identity: R-protection on the 5-atlas is equivalent to vanishing of the 3 Mellin moments `m_n^O = 0 ∀ n ∈ {0, 2, 6}`. This is a Level-2 win — the substrate's R-protection structure has a 3-moment compact characterization, simplifying every future R-protection check to 3 Mellin integrals. Direct downstream impact: the `_r_protection_classifier.py` (currently runs full 5-atlas regulator-comparison) can be replaced by a 3-Mellin-moment computation, ≈10× speedup on every future R-protection gate.
- **FAIL** refutes the lizzi S-1 §IV.5 criterion. The substrate's R-protection structure is NOT captured by 3 Mellin moments at n ∈ {0, 2, 6}. The Level-2 corridor closes; the FP+FN counter-example CSV becomes the S87+ exploration substrate for a refined criterion (more moments, atlas restriction, or a non-Mellin characterization). Constraint-map gain: one wrong characterization eliminated, surviving criteria narrower.
- **INFO** lands a banded result: criterion is partially valid; the per-class breakdown identifies the validity domain (e.g., "works for RATIO + ABSOLUTE classes but fails on MIXED") which becomes a structural sub-result registered at §VII.S.<new-letter> with a refinement carry-forward.
- **INFO-DEFER** is the budget-protection clause; S87 W-aux re-dispatches with the same gate spec.

### 12. Effort estimate
8-12h HIGH. ≈2-3h script setup + S80 W0-9 catalog load + Mellin density discretization. ≈3-4h GPU-batched 552-integral Mellin moment compute (184 observables × 3 orders × possibly 5 atlas regulators if criterion is atlas-conjunctive). ≈2-3h confusion matrix + per-class concordance + counter-example CSV. ≈1-2h L=10 vs L=8 cross-check.

DEFER-ELIGIBLE: skip if W9 cumulative > 14h or C26 + C24 > 11h combined.

### 13. Substrate-framing reminder
The substrate's spectral-functional ledger has property `R-protection of observable O is characterized by m_n^O = 0 for n ∈ {0, 2, 6}` under condition `the 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}` — IF the criterion PASSes. If FAIL, the substrate's R-protection structure is GEOMETRICALLY richer than a 3-moment characterization captures, and the criterion is refuted as an over-restrictive structural model. Either way, the result is a property of the substrate's spectral-functional ring under the atlas, NOT a property of fields living in a container.

---

## §X. Wave W9 → Downstream Decision Point

The W9 wave is a registry-completion + criterion-test wave; it produces no live downstream gate dependency in S86 itself. Its outcomes feed S87+:

| Outcome | Downstream impact |
|:--------|:------------------|
| C26.A + C26.B both PASS | W2-2 mother-theorem registry slot is COMPLETE. S87 plan §VII.P-prime + §VII.K-DUAL-q registry entries land as theorem-grade with dual-SHA. |
| C26.A or C26.B FAIL | W2-2 mother-theorem registry slot loses 1 (or both) predicted instantiations. S87 plan must register a retraction-edit on the W2-2 registry block citing the FAIL closure-SHA. |
| C24 PASS | §VII.P parity-family registry is structurally complete at S86 close. The S85 W2-7 FAIL-with-refinement carry-forward is closed. Downstream §VII.P-family registry is locked. |
| C24 FAIL | §VII.P-v2 refinement is NOT the correct direction; HP^0-content-distinct restriction does not separate (C_H, C_epsH) twin pairs. S87+ exploration needed for a stronger refinement candidate. |
| C24 INFO | §VII.P-v2 lands without §VII.P'; S87 carry-forward registers the §VII.P' GV diagnostic re-check at higher L_max or via an alternative cocycle. |
| C44 PASS | R-protection criterion VALIDATED. `_r_protection_classifier.py` ≈10× speedup on every future R-protection gate. Level-2 win added to permanent-results-registry. |
| C44 FAIL | Criterion REFUTED. FP+FN counter-example CSV becomes S87+ exploration substrate for refined criterion. Level-2 corridor closes; constraint map gains one wrong characterization eliminated. |
| C44 INFO | Banded result; per-class breakdown identifies validity domain; class-restricted criterion lands as a §VII.S sub-entry with refinement carry-forward. |
| C44 INFO-DEFER | S87 W-aux re-dispatches with same gate spec; W9 closes on C26 + C24 only. |

W9 has no PASS-required prerequisite for any other S86 wave. Its outputs are CONSUMED by the S87 planning cycle.

---

## §0.10. Wave W9 Machinery-Enumeration Pin (PRDR aggregate)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, the wave-level PRDR enumerates every gate-relevant machinery parameter. W9 aggregate:

| Parameter | C26 value | C24 value | C44 value | Source / Pin Justification |
|:----------|:----------|:----------|:----------|:---------------------------|
| `L_max_primary` | 10 | 10 | 10 | S85 W2-2 / W2-7 / S80 W0-9 baseline |
| `L_max_cross_check` | 12 | 8 | 8 | C26 stress-test upward; C24 + C44 stability-test downward |
| `scheme` | `ncg-cohomological` | `ncg-corridor-equivalence` | `Mellin-moment-criterion-test` | per-gate canonical |
| `convention` | `HP^k-Pontryagin-rank-2-Spin8-extension` (C26.A) / `HP^even-q-deformed-4-bucket` (C26.B) | `HP^0-content-distinct + odd-parity-GV` | `criterion-vs-empirical` | per-gate canonical |
| `tolerance` (theorem-grade) | 1e-10 | THEOREM (integer + 1e-12 ε) | THEOREM (concordance threshold ABS) | each gate's tolerance class |
| `random_seed` | 0 | 0 | 0 | deterministic (no Monte Carlo in any of the 3 gates) |
| `q_range` (C26.B only) | `[0.50, 0.55, ..., 0.95]` | N/A | N/A | non-perturbative deformation, mild enough for stability |
| `twin_pair_class` (C24 only) | N/A | `(C_H, C_epsH)` | N/A | from S85 W2-7 §VII.P parity-blindness FAIL closeout |
| `moment_orders` (C44 only) | N/A | N/A | `(0, 2, 6)` | verbatim from lizzi S-1 §IV.5 |
| `moment_zero_tolerance` (C44 only) | N/A | N/A | `1e-8` ABS | criterion: m_n^O = 0 means \|m_n^O\| < 1e-8 |
| `concordance_PASS_threshold` (C44 only) | N/A | N/A | `0.95` | ≥95% of 184 entries |
| `concordance_INFO_low_threshold` (C44 only) | N/A | N/A | `0.80` | INFO band 0.80-0.95 |
| `atlas_regulators` (C44 only) | N/A | N/A | `(zeta, Zubarev, SDW, cutoff_sqrt, anomaly)` | S80 W0-9 5-atlas baseline; pinned conditional on C28 W4 outcome (4 vs 5 regulators) |
| `defer_eligibility` (C44 only) | N/A | N/A | TRUE if W9 cumulative > 14h OR C26+C24 > 11h | Level-2/3 budget protection |
| `GPU_path` | `torch.linalg.eigvals` / `torch.linalg.svd` | `torch.linalg.eigvalsh` / `torch.linalg.matrix_rank` | `torch.trapz` / `torch.einsum` | matrix dim ≥ 100 routes to GPU |
| `CPU_fallback` | `OMP_NUM_THREADS=8` before `import numpy` | same | same | per `.claude/rules/math-scripts.md` |

**Diagnostic-only parameters** (not gate-relevant; declared as such per PRDR Class-8 protection):
- C26.B `q_step = 0.05` is a sampling resolution; varying q_step within [0.025, 0.10] should not change the 4-bucket count or boundary-stability conclusion. If it does, the result is pre-pinned as INFO.
- C44 `RATIO/ABSOLUTE → R-protected` mapping is a definitional pin from the S80 W0-9 closeout; if the closeout uses a different mapping than this plan assumes, the script REPORTS the discrepancy in stdout and the agent flags it (does NOT auto-correct).

PRU-Class-8 vulnerabilities **none identified at plan-time**: every gate-relevant parameter is pinned. The diagnostic-only parameters are explicitly declared.

---

## §0.11. Wave W9 Input-SHA Ledger

Each gate's producing script computes its closure-SHA from the ordered input-pin map. The pins below are the input set; `<computed-at-runtime>` markers are populated by the script at first-line stdout per the computation-script template.

### C26 (W9-1)
| Pin name | Path / source | SHA at plan-write |
|:---------|:-------------|:------------------|
| `computations/canonical_constants.py` | static | `<read-at-runtime>` |
| W2-2 mother-theorem closure-SHA | `computations/s85_gate_verdicts.txt` (grep `S85-W2-2`) | `<read-at-runtime>` |
| T2 §VII.R NCG-Meta-Theorem closure-SHA | `computations/s86_gate_verdicts.txt` (grep `S86-VII-R-NCG-META-THEOREM-LANDING`) | `<computed-at-S86-W1a-runtime>` |
| D_K spectral cache L=10 | `computations/cache/dk_spectrum_L10.npz` | `<read-at-runtime>` |
| D_K spectral cache L=12 | `computations/cache/dk_spectrum_L12.npz` | `<read-at-runtime>` |
| Spin(8) ⊃ SU(3) embedding cite | Connes-Chamseddine 2007 §3 (no SHA; documentation) | N/A |
| C18 W0c canonical entries (HP1_dim, etc.) | `computations/canonical_constants.py` post-W0c | `<computed-at-S86-W0c-runtime>` |

### C24 (W9-2)
| Pin name | Path / source | SHA at plan-write |
|:---------|:-------------|:------------------|
| `computations/canonical_constants.py` | static | `<read-at-runtime>` |
| W2-7 §VII.P parity-blindness FAIL closure-SHA | `computations/s85_gate_verdicts.txt` | `<read-at-runtime>` |
| T2 §VII.R NCG-Meta-Theorem closure-SHA | as above | `<computed-at-S86-W1a-runtime>` |
| **S84 W10-115 odd-parity GV diagnostic** | `sessions/archive/session-84/computations-artifacts/s84_w10a_115_gv_explicit.npz` | `<read-at-runtime>` (file is DELETED in current branch per `git status`; planner flags this — the C24 producing script must restore the file from `git show` against a prior commit, OR if the artifact is unrecoverable, the gate emits a `MissingUpstreamArtifact` error and exits 2). |
| C18 W0c canonical entries (HP1_dim, FI_parity_exclusion) | as above | `<computed-at-S86-W0c-runtime>` |

### C44 (W9-3)
| Pin name | Path / source | SHA at plan-write |
|:---------|:-------------|:------------------|
| `computations/canonical_constants.py` | static | `<read-at-runtime>` |
| T10 60-row composite atlas closure-SHA | `computations/s86_gate_verdicts.txt` (grep `S86-FI-RD-PERMANENT-REGISTRY`) | `<computed-at-S86-W1c-runtime>` |
| **S80 W0-9 184-entry RATIO/ABSOLUTE/MIXED catalog** | path TBD (likely `sessions/archive/session-80/computations-artifacts/s80_w09_*.npz` or structured CSV; agent uses `mcp__knowledge__search_knowledge("W0-9 184-entry RATIO/ABSOLUTE/MIXED")` to locate at runtime) | `<read-at-runtime>` |
| S80 W0-9 RATIO/ABSOLUTE → R-protected mapping note | from W0-9 closeout text (sessions/archive/session-80/) | `<read-at-runtime>` |
| lizzi S-1 §IV.5 criterion text | embedded as docstring; cite path | N/A (documentation) |
| D_K spectral cache L=10 | `computations/cache/dk_spectrum_L10.npz` | `<read-at-runtime>` |
| D_K spectral cache L=8 | `computations/cache/dk_spectrum_L8.npz` | `<read-at-runtime>` |
| 5-atlas regulator constants | `computations/canonical_constants.py` (F_4 + M atlas) | `<read-at-runtime>` |
| C28 W4 cutoff_sqrt verdict (atlas size pin) | `computations/s86_gate_verdicts.txt` (grep `S86-W-4-CUTOFF-SQRT-ADJUDICATION`) | `<computed-at-S86-W4-runtime>` (conditional input — only if C28 lands STRUCTURALLY-EXCLUDED, atlas drops to 4-regulator) |

### Closure-SHA computation
Every gate's producing script computes its `audit_sha256` as:
```
audit_sha256 = sha256( json.dumps(ordered_input_pin_map, sort_keys=True).encode() )
```
The `content_sha256` is the SHA-256 of the output `.npz` content. Both go into the canonical verdict line + dual-SHA companion comment row per `.claude/rules/gate-verdicts.md` and the computation-script template.

NEVER hardcode the closure-SHA; NEVER copy-paste it from a prior gate; NEVER truncate to less than 64 hex chars. Per `.claude/rules/gate-verdicts.md`, `_consolidate_intake.py` rejects verdict lines with SHAs shorter than 40 hex chars.

---

## §Y. Script-Prefix Convention

All W9 producing scripts use the prefix `computations/s86_w9_<slug>.py`:

- C26 → `computations/s86_w9_C26_w22_predicted_instantiations.py`
- C24 → `computations/s86_w9_C24_vii_p_v2_parity_extension.py`
- C44 → `computations/s86_w9_C44_r_protection_mellin_criterion.py`

Each starts from `.claude/templates/script-template.py` and uses the template's `append_verdict(verdict, value, closure_sha)` helper for atomic single-line append to `computations/s86_gate_verdicts.txt`. Do NOT write to any variant path; do NOT use truncate-and-rewrite; do NOT print verdict lines to stdout instead of file-appending.

---

## §Z. Wave W9 Plan-Self-Audit (PRU + closure)

PRU-Class-8 audit at plan-write:
- **C26.A**: every parameter pinned (L_max, scheme, convention, tolerance, random_seed, GPU path, Spin(8) embedding). PRU-clean.
- **C26.B**: every parameter pinned (L_max, scheme, convention, q_range, q_step, tolerance, random_seed, GPU path). q_step pre-declared as diagnostic. PRU-clean.
- **C24**: every parameter pinned (L_max, scheme, convention, twin_pair_class, tolerance, random_seed, GPU path, S84 W10-115 input pin). S84 W10-115 file deletion is FLAGGED as a runtime risk (not a PRU vulnerability — the file existed and was deleted; restoration path is documented). PRU-clean.
- **C44**: every parameter pinned (L_max, scheme, convention, moment_orders, moment_zero_tolerance, concordance thresholds, atlas_regulators, defer_eligibility, RATIO/ABSOLUTE mapping). RATIO/ABSOLUTE mapping pinned conditionally on S80 W0-9 closeout text — the script reports any deviation. atlas_regulators pinned conditionally on C28 W4 outcome (4 vs 5 regulators) — both conditional pins are explicitly declared, NOT left implicit. PRU-clean.

Substitution-chain audit:
- C26.A magnitude direction claim: chain present (§10).
- C26.B magnitude direction claim: chain present (§10b).
- C24: definitional/classification only; chain not required (per `.claude/rules/math-scripts.md`).
- C44 criterion-direction claim: chain present (§10).

Substrate-framing audit:
- All three gates framed as "the substrate's [structure] has property X under condition Y" (per `.claude/rules/phononic-framing.md`). No container-thinking in any §13 reminder. PRU-clean.

GPU-pinning audit:
- All three gates explicitly name `torch.linalg` for matrices ≥ 100, with `OMP_NUM_THREADS=8` CPU fallback, per `feedback_compute-environment.md`. PRU-clean.

Verdict-file audit:
- All three gates write to `computations/s86_gate_verdicts.txt` (canonical path per `.claude/rules/gate-verdicts.md`). Both Method §6 and §0 Summary state the path explicitly. C26 emits TWO verdict lines (sub-gates A and B); C24 + C44 each emit ONE. Dual-SHA companion comment row required for all. PRU-clean.

Ready for runtime dispatch in Batch-2 per partition manifest §4.

---

**End of Wave W9 plan.**
