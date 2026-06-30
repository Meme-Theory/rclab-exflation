# Session 84 Plan — Wave 10a: Audit-Integrity Closeout (12 items)

**Session**: 84
**Wave**: 10a (audit-integrity closeout, sub-block "a" of Wave 10)
**Items**: 12 (rows 110-121 of §4.L in `session-84-context.md`)
**Format**: compute (parallel independent agents)
**Planner**: sagan-empiricist
**Canonical constants**: `computations/canonical_constants.py` (all scripts must `from canonical_constants import *` and tag intermediates `# (local)`)
**Python env**: `phonon-exflation-sim/.venv312/Scripts/python.exe` (GPU ROCm torch 2.9.1 available)
**Script prefix**: `s84_w10a_<slug>.py`

---

## W10a Summary

Wave 10a closes out the audit-integrity debts inherited from S82 that were sharpened by the S83 G55 FAIL (1/3 SHA-collision rate detected in S82 verdicts W1-1-TD, W2-13, W3-7). The wave groups into four bands:

1. **SHA-integrity regeneration + uniqueness (110, 118)** — regenerate the three colliding S82 SHAs under the full-pin-map discipline required by the S84+ dual-SHA protocol; prove propagation-atlas SHAs distinct.
2. **Formal write-ups + header repairs (111, 112)** — rank-universality proof formalization; S80 Wave-1 stale-header corrections.
3. **GV / K-theory cohomology explicit computations (113, 114, 115)** — framework-wide GV-secondary classification; ε_H class location in HP¹(A_F) via direct cocycle computation; explicit [GV(F_Jensen)] in H³(M⁴) matching G56's -4.06e+04 stencil.
4. **Layer / K-pairing / composition audits (116, 117, 119, 120, 121)** — W1-G6 1/8 functor failure diagnosis; R-protected observable K-pairing classification; τ_fold=0.190 uniqueness on (Γ1' ∧ Γ5' ∧ Γ6); Γ5' sign-gear convexity lever coverage; small-action saddle inventory closure vs S_inst ≤ 4.34 Borel threshold.

**What each band constrains (not a rhetorical count — the mapped surface)**:

- Band 1 defines the boundary of verdict-provenance reliability: after Wave 10a, every post-S82 SHA in use must be regenerated under the canonical ordered-pin protocol, and every propagation-atlas SHA must trace to an independent pin map. This eliminates the S83 G55 failure mode from the live corpus.
- Band 2 moves two deferred formalization items into their canonical registry locations. No new physics claims; repairs only.
- Band 3 computes three cohomological objects that are currently asserted but not directly verified: (i) whether ε_H is genuinely outside image(ch: K_0 → HP⁰), not just classified as "secondary CM Hopf"; (ii) whether the [GV(F_Jensen)] primary response truly vanishes after the Atiyah-Singer index-theoretic correction (G56 v2 = PASS) with a -4.06e+04 secondary stencil; (iii) whether the framework-wide GV classification is self-consistent across F_KK-scope observables.
- Band 4 audits five structural claims that live downstream of pinned machinery but have not been directly re-verified: composite functoriality layer-crossings, R-protection K-pairing provenance, τ_fold fixed-point uniqueness, sign-gear coverage completeness, and small-action saddle absence.

**Classification**: All 12 gates are **AUDIT** or **VERIFY** class. None are new physical predictions. The wave produces no EVOI-positive observational claim; its role is hardening the provenance chain so that Wave 10b+ physics-facing gates can be trusted.

**Relationship to probability**: Wave 10a is BF ≈ 1.0 for framework probability by construction — audits do not test predictions against observation. A clean PASS across all 12 maintains the current probability; a FAIL on 110, 114, or 115 would DECREASE confidence by exposing a load-bearing claim as unsupported. There is no upside.

**Trigger-prefix distribution**:
- `[AUDIT]` (re-examining prior verdicts): 110, 112, 113, 116, 117, 118, 119, 121
- `[VERIFY]` (PASS/FAIL within factor 3 of threshold): 114, 115, 120
- `[VERIFY-THEOREM]` (theorem-level formalization): 111

---

## W10a Decision Point Prerequisites

Before W10a dispatch:

1. **S82 verdict-file must be read-only for this wave**. W10a regenerates SHAs; the original closures remain the historical record. The new SHAs go to `s84_w10a_gate_verdicts.txt` with explicit cross-reference to the S82 lines being superseded.
2. **S83 G55 verdict artifact must be in place**: `sessions/archive/session-83/computations-artifacts/s83_g55_sha_collision_audit.json` (containing the 1/3 collision event and the pin-map discipline used for detection).
3. **S80 Wave-1 source files must be accessible** for header repair (§112): `sessions/archive/session-80/session-80-w1-*.md`.
4. **G56 v2 stencil data required for §115**: `gv_response = -4.0579e+04`, `stencil_err = 5.98e-07`, primary = 0 (post-Atiyah-Singer index correction). Available from `sessions/archive/session-83/computations-artifacts/s83_g56_godbillon_vey_*.npz`.
5. **42-row §VII.K-PROP propagation atlas must exist** for §118: `computations/_vii_k_prop_atlas.json`.

If any of 1-5 is missing or in conflict with the SHA-regenerator's expected inputs, the responsible gate is PRE-REG-INCOMPLETE (PRU Class 8), not FAIL. Pin the machinery before dispatching.

---

## §W10a-110 S84-SHA-COLLISION-REGEN

**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (audit-integrity)
**Agent type**: sagan-empiricist

**Hypothesis being tested**: Three S82 verdict lines (W1-1-TD, W2-13, W3-7) that produced duplicate/colliding SHA-256 closures in S83 G55's audit can be deterministically regenerated under the full-pin-map discipline (canonical ordered input-pin sequence, UTF-8 encoding, no path-normalization shortcuts), yielding three distinct full 64-char hexdigests — one per verdict.

**Machinery pin (PRDR)**:
- `N_eval`: 3 verdict lines (W1-1-TD, W2-13, W3-7)
- `pin_map_ordering`: canonical sort = (input_path_posix, then content_type, then size), deterministic
- `hash_algorithm`: `hashlib.sha256` stdlib; no custom wrapper
- `encoding`: UTF-8 with byte-level normalization (no `.strip()` on content)
- `input_pin_source`: `sessions/archive/session-82/computations-artifacts/s82_w{N}_{slug}_inputs.json` for each verdict
- `tolerance`: EXACT (byte-for-byte); no approximation
- `random_seed`: N/A (deterministic)
- `GPU path`: N/A (hash computation is CPU-bound and sub-second)

**Input SHA-256 pins**:
- `sessions/archive/session-82/s82_gate_verdicts.txt`: `<computed-at-runtime>` (frozen at script start)
- `sessions/archive/session-82/computations-artifacts/s82_w1_1_td_inputs.json`: `<computed-at-runtime>`
- `sessions/archive/session-82/computations-artifacts/s82_w2_13_inputs.json`: `<computed-at-runtime>`
- `sessions/archive/session-82/computations-artifacts/s82_w3_7_inputs.json`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g55_sha_collision_audit.json`: `<computed-at-runtime>`
- `computations/canonical_constants.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<bool_all_distinct>, scheme=canonical_pin_ordering, convention=S84_dual_sha, L_max=N/A)`

**Pass / Fail / INFO thresholds**:
- **PASS**: All 3 regenerated SHAs are 64-char hexdigests, all distinct pairwise, and each verifies against its frozen pin-map input (the SHA recomputed from the same pin-map matches on a second pass to byte-exact equality).
- **FAIL**: Any of (a) any two regenerated SHAs coincide, (b) any regenerated SHA is <64 chars, or (c) any SHA fails its own round-trip verification.
- **INFO**: One or more source `*_inputs.json` files absent — the verdict being audited cannot be reconstructed. Mark as PRE-REG-INCOMPLETE (PRU Class 8) and defer to Wave 10b with an explicit reconstruction protocol.

**What PASS means for the solution space**: The v3 dual-SHA migration protocol (schema_version=S84+) is empirically grounded — a documented procedure that, when applied to the three known-collision cases, produces distinct canonical hashes. The S82 corpus can be retroactively validated case-by-case by re-running this protocol.

**What FAIL means for the solution space**: The collision is NOT an audit-protocol artifact; it is structural in either the input-pin recording (S82 machinery) or the hash function's interaction with the pin-map schema. Either the S82 inputs were non-unique (an irreparable provenance gap) or the pin-map schema must be redesigned before further SHAs can be trusted.

**Substitution chain** (AUDIT class, identity-check only — no sign claim):
1. **Definition**: `closure_sha256(v) := sha256(canonical_pin_map(v).to_utf8_bytes())` where `canonical_pin_map(v) = sorted_deterministic_list_of_(path, sha256_of_content, size)` for every input read by the script producing verdict v.
2. **Regenerator**: For each v ∈ {W1-1-TD, W2-13, W3-7}, recompute `pin_map_v` from `s82_{v}_inputs.json`, re-apply canonical ordering, re-hash.
3. **Distinctness test**: `|{closure_sha256(W1-1-TD), closure_sha256(W2-13), closure_sha256(W3-7)}| == 3`.
4. **Round-trip test**: For each v, recompute `closure_sha256(v)` twice independently; bytes-equal result required.

**Script**: `computations/s84_w10a_sha_collision_regen.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_110_sha_regen.json`, verdict line appended to `computations/s84_gate_verdicts.txt`
**Effort**: 0.2 session (infrastructure; no physics)

---

## §W10a-111 S84-RANK-UNIVERSALITY-PROOF-TEXT

**Trigger**: `[VERIFY-THEOREM]`
**Classification**: GEOMETRIC (representation theory on compact simple Lie groups)
**Agent type**: sagan-empiricist

**Hypothesis being tested**: The S82 W3-1 PASS (rank-universality, value = 1.0, all compact simple Lie groups yield identical normalized gauge-coupling ratio at fixed spectral-triple inputs) admits a formal written proof in ≤4 pages consisting of (i) statement, (ii) three lemmas (Peter-Weyl decomposition; adjoint-rep Casimir dependence; normalization invariance of the ratio under rank change), (iii) the proof proper, (iv) a rigor checklist. The proof is landable either at `sessions/archive/session-82/theorems/rank_universality.md` (retroactive) or at §VI.A of `phonon_exflation_cosmology.md`.

**Machinery pin (PRDR)**:
- `N_eval`: 1 formalization document, ≤4 pages (no line-count requirement — per `feedback_max-effort-full-fidelity.md`)
- `scope`: Compact simple Lie groups G with rank r, adjoint rep ad_G, Killing form κ
- `observable`: `R(G) := (normalized coupling ratio) / (sum of spectral weights)`, computed at Jensen-fold inputs
- `ansatz_space`: all compact simple G with KO-dim = 6 compatible fiber embedding (i.e., rank-independent Mellin balance)
- `derivation_path`: (a) Peter-Weyl, (b) Casimir identity `C_2(ad_G) = 2 h^∨ · I_{dim G}` where h^∨ is dual Coxeter, (c) normalization `R(G) = 1` iff ratio numerator and denominator both scale linearly in h^∨
- `tolerance`: PROOF-COMPLETE or NOT (binary); no numerical residual
- `random_seed`: N/A
- `GPU path`: N/A (pure formal write-up; script is a LaTeX-to-markdown renderer, not a compute)

**Input SHA-256 pins**:
- `sessions/archive/session-82/s82_gate_verdicts.txt` (W3-1 line): `<computed-at-runtime>`
- `sessions/archive/session-82/computations-artifacts/s82_w3_1_rank_universality.npz`: `<computed-at-runtime>`
- `researchers/Connes/` + `researchers/Baptista/` Peter-Weyl reference anchors: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<proof_complete_bool>, scheme=peter_weyl_casimir, convention=r_independent_normalization, L_max=N/A)`

**Pass / Fail / INFO thresholds**:
- **PASS**: Proof document exists at pinned path with (i) theorem statement, (ii) ≥3 lemmas with independent proofs, (iii) proof step-by-step, (iv) rigor checklist covering edge cases G_2, F_4, E_6, E_7, E_8. Second independent read by a separate agent confirms no gap.
- **FAIL**: Any of (a) a lemma proof has a circular citation, (b) an exceptional-group case is claimed without check, or (c) the rank-r dependence cancels only up to O(1/r) (not exactly).
- **INFO**: Proof exists but rigor-checklist second read identifies a non-load-bearing gap (e.g., minor notational convention) — acceptable to land with a known-errata note.

**What PASS means**: The S82 W3-1 numerical PASS has a structural companion. Rank-universality becomes permanent — it holds by theorem, not by empirical coincidence across the groups tested.

**What FAIL means**: The numerical PASS is an artifact of the specific groups surveyed (likely SU(N) only), not a universal property. Re-open the §VI.A question about which fiber algebras are rank-universal.

**Script**: `computations/s84_w10a_rank_universality_proof.py` (renders proof from structured markdown; not a numerical gate)
**Output artifacts**: `sessions/archive/session-82/theorems/rank_universality.md` (the proof), `sessions/archive/session-84/computations-artifacts/s84_w10a_111_proof_checklist.json`
**Effort**: 0.3 session

---

## §W10a-112 S84-S80-HEADER-REPAIR

**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (documentation repair)
**Agent type**: sagan-empiricist

**Hypothesis being tested**: S80 Wave-1 subsection headers W1-1..W1-6 display the status string "NOT STARTED" while the corresponding bodies contain landed PASS/FAIL verdicts. This is a consistency defect: the section-heading status flags are stale.

**Machinery pin (PRDR)**:
- `N_eval`: 6 headers (W1-1, W1-2, W1-3, W1-4, W1-5, W1-6)
- `source_file`: `sessions/archive/session-80/session-80-plan.md` (or per-wave file if split)
- `header_pattern`: `## W1-N <slug> — <status>` where status ∈ {NOT STARTED, IN PROGRESS, PASS, FAIL, INFO, PRE-REG-INCOMPLETE}
- `body_verdict_extraction`: match `PASS|FAIL|INFO` tokens in the first 5 lines after header
- `tolerance`: EXACT (header status must match extracted body verdict)
- `random_seed`: N/A
- `GPU path`: N/A

**Input SHA-256 pins**:
- `sessions/archive/session-80/session-80-plan.md` (or all W1 sub-files): `<computed-at-runtime>`
- `sessions/archive/session-80/s80_gate_verdicts.txt`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<headers_repaired_count>, scheme=header_body_consistency, convention=s80_w1_only, L_max=N/A)`

**Pass / Fail / INFO thresholds**:
- **PASS**: All 6 W1 headers updated to match their body-verdict strings; a follow-up audit pass confirms zero mismatches.
- **FAIL**: One or more header updates introduces a new inconsistency (e.g., overwriting a "PASS" with "FAIL" where the body says PASS).
- **INFO**: A header has no extractable body verdict (i.e., the body is still a stub) — mark as PRE-REG-INCOMPLETE for that specific header; other 5 proceed.

**What PASS means**: The S80 documentation is internally consistent. Downstream agents reading S80 headers get accurate status without having to scan bodies.

**What FAIL means**: Header repair is non-mechanical; requires a human arbiter to adjudicate each mismatch. Escalate to the user.

**Substitution chain**: not required (header-string replacement is a direct rewrite, no sign/direction claim).

**Script**: `computations/s84_w10a_s80_header_repair.py`
**Output artifacts**: Updated `sessions/archive/session-80/session-80-plan.md`, diff file `sessions/archive/session-84/computations-artifacts/s84_w10a_112_s80_header_diff.patch`, verdict line
**Effort**: 0.1 session

---

## §W10a-113 S84-GV-SECONDARY-EXCLUSION-AUDIT

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (cyclic cohomology classification)
**Agent type**: connes-ncg-theorist

**Hypothesis being tested**: Every F_KK-scope observable in the framework's propagation atlas has a correctly-classified Godbillon-Vey-vs-primary cyclic-cohomology status. No observable currently classified as "primary-KK" has a secondary GV lift that was missed; no observable classified as "GV-secondary" has a primary KK channel that was overlooked.

**Machinery pin (PRDR)**:
- `N_eval`: all F_KK-scope observables in §VII.K-PROP atlas (42 rows; after a carry-forward from row 23, extended to 50+ if §W10a-118 produces extensions)
- `classification_bins`: {PRIMARY-KK, GV-SECONDARY, BOTH, NEITHER, UNCLASSIFIABLE}
- `cohomology_test`: for each row, compute (a) KK primary channel via Chern character ch: K_0 → HP^even, (b) GV secondary via Connes-Moscovici Hopf lift at H^3(F_Jensen)
- `zero_threshold`: primary coefficient |c_KK| < 1e-10 ⇒ treat as "not primary"; secondary |c_GV| < 1e-10 ⇒ "not secondary"
- `tolerance`: per-row binary classification agreement with prior registry
- `random_seed`: N/A
- `GPU path`: CPU-only for cohomology (dense matrix size <64, but audits 42+ rows so batch with `numpy.linalg` and OMP_NUM_THREADS=8)

**Input SHA-256 pins**:
- `computations/_vii_k_prop_atlas.json`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g56_gv_jensen_deform.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g2_epsilon_h_heitsch_cm_hopf.npz` (for ε_H comparison): `<computed-at-runtime>`
- `computations/canonical_constants.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<per_row_classification_table>, scheme=chern_plus_cm_hopf, convention=hp_even_vs_h3, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: 100% of rows classified into the 5 bins; every row's classification matches or supersedes its prior registry entry with a stated cohomological reason.
- **FAIL**: Any row yields BOTH non-zero primary AND non-zero secondary but is currently classified as only one — indicates the registry is under-refined and downstream span claims may be mis-attributed.
- **INFO**: A row cannot be classified because its D_K block is truncation-sensitive at L_max=5 — flag as "L_max-dependent classification" and defer the final classification to an L_max=9 run.

**What PASS means**: The R-protected vs NOT-R-protected meta-principle (G58) is cohomologically grounded, not numerically empirical. Span<1.5 for R-protected observables is enforced by the structural absence of GV-secondary leakage.

**What FAIL means**: The G58 meta-principle is a numerical regularity without cohomological support; some "R-protected" observables may have hidden secondary channels that could drive span above 1.5 at higher L_max.

**Substitution chain** (required — claims direction of "secondary vs primary"):
1. **Definition**: `primary_KK(O) := ch(O) projected to HP^0`; `secondary_GV(O) := Hopf_cyclic_lift(O) projected to H^3(M^4)`.
2. **Null hypothesis**: If O is "R-protected", then primary_KK(O) ≠ 0 AND secondary_GV(O) = 0.
3. **Alternative**: primary_KK(O) ≠ 0 AND secondary_GV(O) ≠ 0 (mixed) — misclassification if registered as "primary only".
4. **Direction claim** (to verify): for each O, the dominant channel (|c_primary| vs |c_secondary|) sets the classification. If |c_primary|/|c_secondary| > 10 ⇒ "PRIMARY-KK"; if inverse ⇒ "GV-SECONDARY"; if ratio ∈ [0.1, 10] ⇒ "BOTH" (mixed). Classification is a direct read from the canonical form.
5. Read off classification from the magnitude ratio; no inequality-direction claim beyond the ratio threshold.

**Script**: `computations/s84_w10a_gv_secondary_exclusion_audit.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_113_gv_classification_table.csv`, verdict line
**Effort**: 0.5 session

---

## §W10a-114 S84-EPSH-K-CLASS-LOCATION

**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (K-theory / cyclic cohomology localization)
**Agent type**: van-den-dungen-bridge-theorist

**Hypothesis being tested**: The ε_H class lies in HP¹(A_F) (odd cyclic cohomology, secondary CM Hopf location) and [GV] is its image under the Connes-Moscovici Godbillon-Vey lift. Equivalently, ε_H is outside the image of the Chern character ch: K_0(A_F) → HP⁰(A_F), confirming that ε_H cannot be reached from any K-theoretic primary channel (which is why W1-G2 FAIL with heitsch_ratio = 16.20 is structural, not correctable by a coefficient redefinition).

**Machinery pin (PRDR)**:
- `N_eval`: 1 class location claim with 3 sub-verifications
- `A_F`: `C ⊕ H ⊕ M_3(C)` (canonical from A_F-singleton result)
- `K_0(A_F)`: computed from direct algebraic decomposition; rank = 3 (one generator per summand)
- `ch: K_0 → HP^0`: Chern-character matrix on the 3 generators; computed explicitly
- `image_test`: is the cocycle representing ε_H in ch(K_0)? compute residuals on basis
- `cocycle_extraction`: ε_H as an odd cyclic 1-cocycle from the Heitsch-type construction (W1-G2 value heitsch_ratio = 16.20 enters as the normalization check)
- `tolerance`: residual of ε_H against image(ch) basis must be > 1e-8 (outside image); if < 1e-8, the class is in the image and the claim FAILS
- `random_seed`: N/A
- `GPU path`: CPU-only; matrices <20×20

**Input SHA-256 pins**:
- `sessions/archive/session-83/computations-artifacts/s83_g2_epsilon_h_heitsch_cm_hopf.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g4_epsilon_h_substrate_derivation.npz`: `<computed-at-runtime>`
- `computations/_a_f_singleton_decomposition.json`: `<computed-at-runtime>`
- `researchers/Connes/moscovici_hopf_cyclic_cohomology.md`: `<computed-at-runtime>`
- `computations/canonical_constants.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<eps_H_residual_from_image_ch>, scheme=cm_hopf_h1, convention=hp_odd_vs_hp_even, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: ε_H cocycle residual against image(ch: K_0 → HP⁰) > 1e-4 (decisively outside image); and the direct HP¹ cocycle computation yields a non-zero representative matching the Connes-Moscovici Godbillon-Vey lift formula within 1e-6 relative.
- **FAIL**: residual < 1e-8 (ε_H in image(ch)), OR the HP¹ representative vanishes — either falsifies the claim that ε_H is a secondary class.
- **INFO**: residual ∈ [1e-8, 1e-4] — the numerical separation is marginal; flag for L_max-extrapolation to confirm structural (not truncation) origin.

**What PASS means**: The W1-G2 FAIL (heitsch = 16.20) is permanent. ε_H has no primary K-theoretic channel; no coefficient redefinition can recover it. This structurally closes the "ε_H as primary observable" corridor and validates the §W10a-113 secondary-exclusion framework.

**What FAIL means**: ε_H has a primary channel that was missed. The S83 G2 closure must be re-opened and the Heitsch-ratio claim re-derived with the primary channel included.

**Substitution chain** (required — claims containment "outside image"):
1. **Definition**: `image(ch) := {ch(x) : x ∈ K_0(A_F)} ⊂ HP^0(A_F)`; `HP^1(A_F) ∩ image(ch) = 0` by parity (HP^0 is even, HP^1 is odd).
2. **Cocycle representative**: `ε_H = φ_Heitsch(g)` where g ∈ G (the Hopf algebra), φ_Heitsch is the Heitsch 1-cocycle; `[ε_H] ∈ HP^1(A_F)`.
3. **Image(ch) location**: since ch lands in HP^0 (even), and [ε_H] ∈ HP^1 (odd), the two subspaces intersect trivially BY PARITY ALONE. The non-zero residual follows structurally.
4. **Substitution**: `residual = ||[ε_H] - proj_{HP^0}([ε_H])||_{HP^0}` — but `proj_{HP^0}([ε_H]) = 0` by parity, so `residual = ||[ε_H]||_{HP^1}`.
5. **Direction**: `residual > 0 ⇔ [ε_H] ≠ 0 in HP^1` (which W1-G2 already established — heitsch_ratio = 16.20 is a non-trivial cocycle norm).
6. **Conclusion**: `[ε_H] outside image(ch) = HP^0` by parity + non-vanishing cocycle norm. The gate PASSES iff both legs hold.

**Script**: `computations/s84_w10a_eps_h_k_class_location.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_114_eps_h_hp1_cocycle.npz`, verdict line
**Effort**: 0.5 session

---

## §W10a-115 S84-GV-CLASS-EXPLICIT

**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (de Rham / cyclic cohomology explicit cocycle)
**Agent type**: connes-ncg-theorist

**Hypothesis being tested**: The Godbillon-Vey class of the Jensen deformation, `[GV(F_Jensen)]`, is a non-zero element of H³(M⁴) represented by the 3-form `ω_J ∧ dω_J = e^{-τ} dτ ∧ d(e^{-τ} dτ)`. Direct computation matches the G56 stencil value `gv_response = -4.0579e+04` to within `stencil_err = 5.98e-07` relative. (G56 history: withdrawn then PASS after Atiyah-Singer index-theoretic correction set the primary response to 0; the secondary -4.06e+04 is the genuine signal.)

**Machinery pin (PRDR)**:
- `N_eval`: 1 integral ∫_{M^4} ω_J ∧ dω_J, computed on the fiber `SU(3)(τ=τ_fold)` with Jensen deformation
- `ω_J`: `e^{-τ} dτ` (where τ is the Jensen parameter); evaluated at `τ = τ_fold = 0.190`
- `dω_J`: `-e^{-τ} dτ ∧ dτ = 0` classically; but on the non-commutative fiber, `dω_J` acquires a curvature correction from the Hopf algebroid structure — this is where the -4.06e+04 arises
- `integration_domain`: `M^4` (4-dim base) × `SU(3)/T²(τ_fold)` (compact fiber), volume factor `Vol_SU3` from canonical_constants
- `stencil_method`: 5-point central difference on τ-derivatives; `stencil_err` target ≤ 1e-6
- `tolerance`: match G56 value `gv_response = -4.0579e+04` within 1% relative (RATIO tolerance); `stencil_err` ≤ 1e-6 absolute
- `random_seed`: N/A (deterministic integral)
- `GPU path`: recommended if integrand mesh ≥100³; otherwise CPU numpy.trapezoid suffices

**Input SHA-256 pins**:
- `sessions/archive/session-83/computations-artifacts/s83_g56_gv_jensen_deform.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g56_atiyah_singer_correction.json`: `<computed-at-runtime>`
- `computations/canonical_constants.py` (needs `tau_fold`, `Vol_SU3`, `J_C2`): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<gv_response_direct>, scheme=stencil_5pt_central, convention=omega_J_exp_neg_tau_dtau, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: Direct GF computation yields `gv_response_direct ∈ [-4.10e+04, -4.02e+04]` (within 1% of G56 stencil) AND `stencil_err ≤ 1e-6`.
- **FAIL**: Either (a) |gv_response_direct| < 1e+3 (vanishingly small, contradicts the non-zero secondary claim), or (b) sign opposite to G56 (+4.06e+04 vs G56's -4.06e+04), or (c) stencil_err > 1e-5 (numerical method unreliable).
- **INFO**: gv_response_direct is within an order of magnitude but outside 1% (e.g., -5.2e+04) — flag for method refinement; likely stencil-step-size choice.

**What PASS means**: The secondary GV channel is numerically confirmed independent of G56's stencil. The framework's claim that F_Jensen has a non-trivial H³(M⁴) signature (and that all "GV-SECONDARY" classifications in §W10a-113 inherit from this non-triviality) is empirically grounded.

**What FAIL means**: Either G56's PASS was stencil-artifact, or the Atiyah-Singer correction to zero-primary is wrong, or the Jensen deformation has no genuine H³ content. Any of these triggers re-opening of G56 and the §VII.K-PROP atlas rows that depend on non-trivial GV.

**Substitution chain** (required — claims specific numerical value and sign):
1. **Definition**: `[GV(F)] := [ω ∧ dω] ∈ H^3` where `ω = d ln(transverse form)`; for the Jensen foliation, `ω_J = -dτ + e^{-τ} f(x) dx` (with f the fiber-structure constant coming from Hopf algebroid).
2. **Exterior derivative**: `dω_J = e^{-τ} (df ∧ dx + f · (-dτ ∧ dx)) = e^{-τ} df ∧ dx - e^{-τ} f dτ ∧ dx`.
3. **Wedge**: `ω_J ∧ dω_J = (-dτ + e^{-τ} f dx) ∧ (e^{-τ} df ∧ dx - e^{-τ} f dτ ∧ dx)`. Expanding:
   - `-dτ ∧ e^{-τ} df ∧ dx = -e^{-τ} dτ ∧ df ∧ dx` (3-form)
   - `-dτ ∧ (-e^{-τ} f dτ ∧ dx) = +e^{-τ} f dτ ∧ dτ ∧ dx = 0` (dτ ∧ dτ vanishes)
   - `e^{-τ} f dx ∧ e^{-τ} df ∧ dx = e^{-2τ} f dx ∧ df ∧ dx = 0` (dx ∧ dx vanishes when df is single-component; otherwise contributes via fiber variables)
   - `e^{-τ} f dx ∧ (-e^{-τ} f dτ ∧ dx) = -e^{-2τ} f² dx ∧ dτ ∧ dx = 0` (same reason)
4. **Surviving term**: `ω_J ∧ dω_J = -e^{-τ} dτ ∧ df ∧ dx` (a 3-form).
5. **Integration**: `∫_{M^4} ω_J ∧ dω_J = -∫_{base} e^{-τ_fold} · ∫_{fiber} df ∧ dx · dτ · Vol_{base}`. The fiber integral `∫ df ∧ dx` is the Casimir-like invariant `J_C2` rescaled by `Vol_SU3`.
6. **Direction**: the sign of the response is `-sign(e^{-τ_fold}) · sign(J_C2) · sign(Vol_{base})`. Since `e^{-τ_fold} > 0` and `Vol > 0`, the sign reduces to `-sign(J_C2)`. G56 reported negative ⇒ `sign(J_C2) > 0` is the expected condition.
7. **Magnitude check**: Substitute `e^{-τ_fold} = e^{-0.190} ≈ 0.827`, `J_C2` and `Vol_SU3` from canonical_constants. The magnitude should land near 4.06e+04; verify by Python.

**Script**: `computations/s84_w10a_gv_class_explicit.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_115_gv_explicit.npz`, verdict line
**Effort**: 0.5 session

---

## §W10a-116 S84-W1G6-LAYER-DIAGNOSIS

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (functorial / three-layer structure)
**Agent type**: van-den-dungen-bridge-theorist

**Hypothesis being tested**: The S83 W1-G6 result (42/42 pointwise FI-duality agreement + 7/8 functoriality with 1 borderline composite) has its 1/8 failure located at an L1-L2 cross-pin boundary. Specifically, the failing composite has one factor pinned at the L1 (axiomatic) layer and the other at L2 (substrate-action) layer, and the dual-pin combinator has no canonical cross-layer transport defined. If confirmed, this is an expected (not anomalous) consequence of the three-layer regulator theorem's scope — functoriality is complete within each layer but requires explicit transport across layers.

**Machinery pin (PRDR)**:
- `N_eval`: 1 diagnosis of the specific W1-G6 composite that failed
- `composite_identity`: the failing 1/8 composite — identify by row index from `s83_w1_g6_fi_duality.npz`
- `layer_map`: for each factor in the composite, classify pin as L0-INT / L1-AX / L2-SA / L3-OB / UNPINNED (5-value tag, per W10?-LAYER-PIN-REGISTRY convention from §4.B row 13)
- `functoriality_test`: F(A ∘ B) vs F(A) ∘ F(B); check whether layer mismatch accounts for the gap
- `tolerance`: BINARY — does the failing composite cross L1-L2? Answer YES ⇒ diagnosed. Answer NO ⇒ the failure is something else, escalate.
- `random_seed`: N/A
- `GPU path`: CPU-only (composite analysis is combinatorial)

**Input SHA-256 pins**:
- `sessions/archive/session-83/computations-artifacts/s83_w1_g6_fi_duality.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_vii_m_three_layer_theorem.json`: `<computed-at-runtime>`
- `computations/_vii_k_prop_atlas.json`: `<computed-at-runtime>`
- `computations/canonical_constants.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<is_L1_L2_cross_pin>, scheme=three_layer_diagnosis, convention=vii_k_dual_layer_pin, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: The failing composite has exactly one L1-pinned factor and one L2-pinned factor; the three-layer theorem predicts functoriality failure at cross-layer composites without explicit transport. Diagnosis confirmed; three-layer theorem is self-consistent.
- **FAIL**: The failing composite is within a single layer (e.g., both factors L2). Three-layer theorem does not explain the failure; functoriality has an independent structural gap, and §VII.M registry status must be revisited.
- **INFO**: The failing composite has one or more UNPINNED factors — diagnosis blocked on unrelated item (§W10a is not the place to pin UNPINNED rows; that is §W10a's §4.B family, row 19).

**What PASS means**: The three-layer regulator theorem is closed: 7/8 pointwise functoriality + 1 cross-layer gap with a known cause. §VII.M can land as-is.

**What FAIL means**: §VII.M has a hidden gap; the three-layer theorem is incomplete and needs an additional structural axiom about composite transport.

**Substitution chain**: not required (binary classification of layer tags, no direction claim).

**Script**: `computations/s84_w10a_w1_g6_layer_diagnosis.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_116_w1_g6_diagnosis.json`, verdict line
**Effort**: 0.3 session

---

## §W10a-117 S84-R-PROTECTION-K-AUDIT

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (K-theoretic classification of R-protection)
**Agent type**: van-den-dungen-bridge-theorist

**Hypothesis being tested**: Every observable currently labeled "R-protected" in the G58 meta-principle registry (notably c_s with G14 span=1.227 and α_SDW^NLO with G26 span=1.053) maps to a specific balanced-Mellin K-pairing class — i.e., the R-protection is a consequence of K-theoretic pairing between a first-moment ratio in H^0(M) and a balanced cocycle in H_0 (dual). "R-protected by accident" (i.e., numerically showing span<1.5 without a K-pairing reason) would be a warning that the meta-principle is fragile.

**Machinery pin (PRDR)**:
- `N_eval`: all currently-labeled R-protected observables (minimum: c_s, α_SDW^NLO, F_traj=3/2, R-family members, χ_2)
- `K_pairing_class`: for each observable O, compute the K-pairing `<O, [cocycle]>` where [cocycle] is the Mellin-balanced dual class
- `balance_criterion`: numerator and denominator of O lie in the same Mellin weight class (first-moment matching)
- `classification_bins`: {BALANCED-BY-K-PAIRING, BALANCED-BY-ACCIDENT, NOT-BALANCED}
- `tolerance`: K-pairing value ≠ 0 ⇒ class 1; pairing = 0 but span<1.5 empirically ⇒ class 2; pairing = 0 and span > 1.5 ⇒ class 3
- `random_seed`: N/A
- `GPU path`: CPU-only

**Input SHA-256 pins**:
- `sessions/archive/session-83/computations-artifacts/s83_g14_c_s_regulator_dep.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g26_sdw_nlo.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g58_meta_principle_registry.json`: `<computed-at-runtime>`
- `computations/_vii_k_prop_atlas.json`: `<computed-at-runtime>`
- `computations/canonical_constants.py`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<per_observable_K_pairing_class>, scheme=mellin_balanced_K_pairing, convention=first_moment_matching, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: ≥80% of R-protected observables fall into BALANCED-BY-K-PAIRING; all remaining ≤20% have a stated structural reason (e.g., symmetry protection outside K-theory).
- **FAIL**: ≥30% of R-protected observables are BALANCED-BY-ACCIDENT (no K-pairing, just numerical coincidence). The G58 meta-principle is structurally weaker than the 10/10 empirical run suggests.
- **INFO**: All observables classify cleanly but the registry needs expansion (new observables discovered) — log as a W10b carry-forward.

**What PASS means**: R-protection is K-theoretically grounded. The span<1.5 regularity for NOT-R observables having span>2.5 is enforced by pairing duality, not by coincidence.

**What FAIL means**: G58 is a correlation without causation; some "R-protected" observables could break span<1.5 at higher L_max without structural warning.

**Substitution chain** (required — claim "R-protection ⇒ K-pairing class" is a direction claim):
1. **Definition**: `R-protected(O)` := observable of the form `O = <x, [φ]>` where x ∈ K_0, [φ] ∈ HC^0 (cyclic cohomology even), and the pairing is Mellin-balanced (numerator and denominator in same weight).
2. **K-pairing**: `<x, [φ]> = Tr(x · φ)` on the universal module; well-defined if x, φ live in compatible duality.
3. **Direction**: if `<O, [cocycle_balanced]> ≠ 0`, then O inherits balance from the cocycle — regulator variation that preserves the cocycle class preserves O's span.
4. **Conclusion**: K-pairing ≠ 0 ⇒ R-protection structural; K-pairing = 0 but span<1.5 empirical ⇒ accidental.
5. Read off classification per observable from the computed pairing magnitude.

**Script**: `computations/s84_w10a_r_protection_k_audit.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_117_r_protection_classification.csv`, verdict line
**Effort**: 0.5 session

---

## §W10a-118 S84-VII-K-PROP-SHA-UNIQUENESS

**Trigger**: `[AUDIT]`
**Classification**: NON-PHONONIC (audit-integrity)
**Agent type**: sagan-empiricist

**Hypothesis being tested**: All verdict SHAs in the §VII.K-PROP propagation atlas (42+ rows) are pairwise distinct AND each traces to an independent pin map (no two verdicts share the same canonical input-pin sequence). This is stricter than §W10a-110 (which regenerates three known-collision cases): §W10a-118 scans the full atlas for hidden collisions or pin-map reuse.

**Machinery pin (PRDR)**:
- `N_eval`: 42+ verdict rows in `_vii_k_prop_atlas.json` (exact count from file)
- `sha_field`: `closure_sha256` column of each row
- `pin_map_field`: `input_pin_ordered_list` column (JSON-serialized ordered list of (path, sha256, size) tuples)
- `distinctness_test`: `len(set(sha_list)) == len(sha_list)` AND `len(set(pin_map_serialized_list)) == len(pin_map_serialized_list)`
- `independence_test`: no two pin-map lists share ≥80% of their elements in identical positions (measuring pin-map reuse even under distinct SHAs)
- `tolerance`: EXACT for distinctness; 80% threshold for independence
- `random_seed`: N/A
- `GPU path`: N/A

**Input SHA-256 pins**:
- `computations/_vii_k_prop_atlas.json`: `<computed-at-runtime>`
- `sessions/archive/session-83/s83_gate_verdicts.txt` (G54 FI-REGISTRY-VII-K-LANDING reference): `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g55_sha_collision_audit.json`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<distinct_count_over_total>, scheme=pairwise_sha_plus_pin_map, convention=vii_k_prop_atlas_full, L_max=N/A)`

**Pass / Fail / INFO thresholds**:
- **PASS**: All SHAs pairwise distinct (N/N) AND all pin-maps mutually independent (<80% overlap).
- **FAIL**: Any SHA collision (hidden duplicate in atlas) OR any two pin-maps with ≥80% positional overlap — indicates pin-map reuse that could propagate a single upstream error across multiple atlas rows.
- **INFO**: All distinct but pin-maps cluster (e.g., rows 1-10 share 70% overlap) — flag as a carry-forward for pin-map-diversification without failing.

**What PASS means**: The propagation atlas is provenance-clean. Downstream CC-5 identity claims (§VII.K-PROP, row 21 of §4.C carry-forward) can be trusted row-by-row; the 42+ rows are 42+ independent tests of the propagation law.

**What FAIL means**: The atlas has hidden redundancy; the effective number of independent tests is less than 42. Atlas-based claims about universality are inflated.

**Substitution chain**: not required (set-distinctness and overlap measurements are direct).

**Script**: `computations/s84_w10a_vii_k_prop_sha_uniqueness.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_118_vii_k_prop_uniqueness.json`, verdict line
**Effort**: 0.2 session

---

## §W10a-119 S84-ALTERNATIVE-TAU-MESH-UNIQUENESS

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (fixed-point uniqueness on the Jensen parameter)
**Agent type**: gen-physicist

**Hypothesis being tested**: τ_fold = 0.190 is the unique fixed point of the joint constraint `(Γ1' ∧ Γ5' ∧ Γ6)` on the search interval `[0.10, 0.30]` up to a Γ1' residual tolerance of 0.134%. No alternative τ in this interval simultaneously satisfies all three gear constraints within this residual.

**Machinery pin (PRDR)**:
- `N_eval`: dense mesh over τ ∈ [0.10, 0.30] with step 1e-4 ⇒ 2001 candidate τ values
- `Γ1'`: first-derivative condition `dS/dτ = 0`; residual `|dS/dτ(τ)| / |dS/dτ(τ=0)| < 0.134%`
- `Γ5'`: second-derivative convexity `d²S/dτ² > 0` (locks the genuine minimum, expected `+317,863` per S70)
- `Γ6`: third-gear condition from the §VII-B gear registry — the cubic-BC override at a=12 (per §4.I row 93)
- `joint_test`: AND of the three gear residuals at each τ; count survivors
- `tolerance`: Γ1' residual 0.134%; Γ5' strict positivity; Γ6 mesh-specific threshold from registry
- `random_seed`: N/A (deterministic mesh scan)
- `GPU path`: CPU-only (2001-point 1D scan; sub-second)

**Input SHA-256 pins**:
- `computations/canonical_constants.py` (needs `tau_fold`, `d2S_fold=+317,863`, `S_fold`): `<computed-at-runtime>`
- `sessions/archive/session-70/computations-artifacts/s70_35d_vp_hessian.npz`: `<computed-at-runtime>`
- `computations/_vii_b_gear_registry.json`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<survivor_count>, scheme=triple_gear_AND, convention=tau_mesh_1e_4_step, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: Exactly 1 τ on the mesh satisfies `(Γ1' ∧ Γ5' ∧ Γ6)` within tolerance; that τ is `0.190` (within mesh resolution, |τ_found - 0.190| ≤ 5e-5).
- **FAIL**: ≥2 τ values satisfy all three gears simultaneously (τ_fold is not unique), OR 0 τ values satisfy them (the pre-registered tolerance is too tight).
- **INFO**: Exactly 1 survivor but at τ ≠ 0.190 (e.g., 0.192 or 0.188) — indicates the canonical τ_fold value needs refinement; flag for canonical_constants update.

**What PASS means**: τ_fold is structurally unique under the triple-gear constraint — not just a local minimum of S but the only point satisfying all three independent gear conditions. MG-1 (τ_fold as gear output) has uniqueness, not just existence.

**What FAIL means**: There is either a second fold-point (framework admits τ-degeneracy, rejecting MG-1 uniqueness), or the triple-gear cannot pick τ_fold at all (one of Γ1', Γ5', Γ6 is vacuous at τ=0.190). Either breaks MG-1.

**Substitution chain** (required — claims "unique" fixed point with directional tolerance):
1. **Definition**: `Γ1'(τ) := |dS/dτ(τ)|`, `Γ5'(τ) := d²S/dτ²(τ)`, `Γ6(τ) := cubic_BC_override(τ)`.
2. **Joint constraint**: `joint(τ) := [Γ1'(τ) / Γ1'(0) < 1.34e-3] AND [Γ5'(τ) > 0] AND [Γ6(τ) within registry tolerance]`.
3. **Uniqueness**: `|{τ ∈ mesh : joint(τ) = True}| == 1`.
4. **Direction claim**: the claim is NOT about sign/direction of any quantity; it is about SET CARDINALITY. Substitution chain reduces to: compute joint(τ) at each mesh point, count Trues. No further simplification.
5. Read off survivor count from the computed set; PASS if cardinality == 1 AND at 0.190.

**Script**: `computations/s84_w10a_alternative_tau_mesh_uniqueness.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_119_tau_mesh_survivors.npz`, verdict line
**Effort**: 0.3 session

---

## §W10a-120 S84-GAMMA5-MASTER-SIGN-GEAR

**Trigger**: `[VERIFY]`
**Classification**: GEOMETRIC (convexity lever / gear dependency)
**Agent type**: gen-physicist

**Hypothesis being tested**: The second-derivative convexity condition `d²S/dτ²|_{τ_fold} = +317,863` (S70 permanent, 35D VP Hessian positive at fold) is the master sign-gear: it locks not only `sign(n_T) > 0` (BLUE transit tilt, G50 PASS n_T = +0.468), but ALSO the directions of four additional composite quantities:
1. `sign(F_amp - 1)` — is F_amp > 1 or < 1 at the fold?
2. `sign(dc_sub/dτ)` — does c_sub increase or decrease across the fold?
3. `sign(c_Gold - c_fabric)` — is the Goldstone speed above or below fabric speed?
4. 4-speed ordering `c_mod > c_BLV > c_BA > c_L` — the full causal hierarchy.

**Machinery pin (PRDR)**:
- `N_eval`: 5 direction claims (n_T already locked by G50; 4 new), all derived from the single convexity lever `d²S/dτ² > 0`
- `convexity_value`: `+317,863` (S70 canonical; from 35D VP Hessian at fold)
- `derivation_chain`: for each of the 4 new quantities, write the explicit substitution chain from d²S/dτ² > 0 to the quantity's sign
- `cross_check`: each sign claim against its direct computation (e.g., F_amp at τ_fold from G7 PASS value; c_Gold - c_fabric from `canonical_constants.c_Gold` minus `c_fabric`)
- `tolerance`: BINARY per direction (sign agrees with convexity-predicted sign or it does not)
- `random_seed`: N/A
- `GPU path`: CPU-only (5 derivation chains + 5 direct computations, trivial)

**Input SHA-256 pins**:
- `computations/canonical_constants.py` (d2S_fold, c_Gold, c_fabric, c_mod, c_BLV, c_BA, c_L, F_amp, c_sub): `<computed-at-runtime>`
- `sessions/archive/session-70/computations-artifacts/s70_35d_vp_hessian.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g50_n_t_bogoliubov.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_g7_cc7_dynamical.npz` (F_amp_lin=1.026 reference): `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<sign_predictions_confirmed>, scheme=convexity_lever, convention=gamma5_master_gear, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: All 5 direction claims (n_T + 4 new) agree with the convexity-lever prediction; each has a written substitution chain showing the derivation from d²S/dτ² > 0.
- **FAIL**: One or more direction claim has opposite sign from the direct computation. Γ5' is not the master sign-gear; the convexity lever does not cover the full sign structure.
- **INFO**: 4/5 agree; the 1 dissenter has a known structural reason (e.g., comes from a different gear entirely). Log as Γ5' covers 4/5 with Γ_other covering the remaining; no retreat on master-gear claim.

**What PASS means**: The MG-1 gear machine (τ_fold with convexity +317,863) has reach beyond n_T; it determines the sign structure of the entire fold-epoch composite ledger. This consolidates multiple apparently-independent sign claims into one lever.

**What FAIL means**: The sign structure is NOT unified by Γ5'. Multiple independent gears control different signs; the MG-1 machine is less parsimonious than claimed.

**Substitution chain** (required — 5 direction claims, each with chain):

**(1) sign(n_T) — already locked, re-verify**:
1. Defn: `n_T = +2 · (d²S/dτ² / (dS/dτ)²)|_{fold} · something_positive`, specifically `n_T ∝ d²S/dτ² / (slow-roll quantities)` at fold.
2. At fold, `dS/dτ = 0` so the "slow-roll" quantities are replaced by Bogoliubov-partition weights; `n_T = +0.468` empirically.
3. Direction: `d²S/dτ² > 0 ⇒ n_T > 0`. CONFIRMED by G50 PASS (+0.468 BLUE).

**(2) sign(F_amp - 1)**:
1. Defn: `F_amp := amplification factor at fold = 1 + integral_of_{Hessian at fold}`.
2. `F_amp - 1 = integral(d²S/dτ²) × (positive prefactor from normalization)`.
3. Direction: `d²S/dτ² > 0 ⇒ integral > 0 ⇒ F_amp > 1`.
4. Verify against G7 PASS: `F_amp_lin = 1.026 > 1`. CONFIRMED.

**(3) sign(dc_sub/dτ)**:
1. Defn: `c_sub(τ) := substrate propagation speed`, normalized; `dc_sub/dτ` evaluated at τ_fold.
2. At a convex minimum, the 2nd derivative of effective potential determines phonon-speed flow. `dc_sub/dτ = f(d²S/dτ²)` where f has known positive coefficient.
3. Direction: `d²S/dτ² > 0 ⇒ dc_sub/dτ > 0 (if f's coeff > 0)` OR `< 0` depending on the sign convention of the coupling between S's convexity and c_sub flow.
4. **Verify via Python** (substitution chain alone does not pin the coefficient sign; direct computation required at runtime from canonical_constants.c_sub).

**(4) sign(c_Gold - c_fabric)**:
1. Defn: `c_Gold := Goldstone mode speed on Jensen fiber = sqrt(c_2_Goldstone)`; `c_fabric := emergent fabric speed = sqrt(c_2_fabric)`.
2. Both are spectral moments of D_K; at fold, their ratio is controlled by the balance of the acoustic vs optical channels.
3. Direction: framework claims `c_Gold > c_fabric` (Goldstone is stiffer than fabric because Goldstone lives on lower-rank sub-fiber). From convexity: d²S/dτ² > 0 at fold stabilizes the relative ordering (destabilization would require d²S/dτ² < 0).
4. **Verify via Python** at runtime by direct comparison of `canonical_constants.c_Gold` and `canonical_constants.c_fabric`.

**(5) 4-speed ordering `c_mod > c_BLV > c_BA > c_L`**:
1. Defn: 4 propagation speeds (moduli, BLV, B-A, Leggett) on different sub-fibers.
2. Ordering is a composite direction claim — 3 pairwise inequalities. Each pairwise inequality derives from the relative curvature of S along the corresponding sub-fiber direction.
3. Direction: at a convex minimum in τ (d²S/dτ² > 0), sub-fiber hierarchy is pinned IF the Hessian is positive-definite in the full 35D VP space (not just τ). S70 canonical result confirms the full 35D Hessian is positive at fold.
4. **Verify via Python** at runtime by reading all 4 speed constants from canonical_constants and confirming the ordering.

**Script**: `computations/s84_w10a_gamma5_master_sign_gear.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_120_master_gear_signs.json`, verdict line
**Effort**: 0.5 session

---

## §W10a-121 S84-TAU-KINK-INVENTORY-CLOSURE

**Trigger**: `[AUDIT]`
**Classification**: GEOMETRIC (saddle-point inventory / Borel summability)
**Agent type**: gen-physicist

**Hypothesis being tested**: The full inventory of small-action saddles in Jensen-parameter space contains no saddle family with `min S_inst < 4.34` (the Borel threshold). The `S_fold = 2.5e5` instanton action is isolated in the sense that no neighboring saddle family has action below the Borel-summability cutoff. This closes the "hidden small-action saddle" concern for the Borel-resummed perturbative series.

**Machinery pin (PRDR)**:
- `N_eval`: enumeration of saddle families over Jensen parameter space; each family characterized by (τ-location, order-of-saddle, action S_inst, multiplicity)
- `search_grid`: τ ∈ [0.05, 0.35] (wider than §W10a-119's [0.10, 0.30] to capture extremes); 35D VP directions at each τ using Hessian eigendirection scan
- `saddle_criterion`: `|dS/dτ| < ε_saddle` AND at least one Hessian eigenvalue flipped sign (Morse index ≥ 1)
- `action_threshold`: report all saddles with `S_inst < 10.0` (buffer above Borel threshold 4.34); flag any below 4.34
- `Borel_threshold`: `S_inst = 4.34` (from canonical_constants or §W2-HARMONIC-NOT-INSTANTON theorem context)
- `tolerance`: RATIO — `min(S_inst) / 4.34 > 1.0` ⇒ PASS; `< 1.0` ⇒ FAIL
- `random_seed`: 42 (reproducibility for Hessian eigendirection sampling)
- `GPU path`: recommended — 35D Hessian eigendecomposition × many τ samples benefits from `torch.linalg.eigh`; fall back to numpy.linalg with OMP_NUM_THREADS=8 if GPU unavailable

**Input SHA-256 pins**:
- `computations/canonical_constants.py` (S_fold, S_harm, tau_fold, d2S_fold): `<computed-at-runtime>`
- `sessions/archive/session-70/computations-artifacts/s70_35d_vp_hessian.npz`: `<computed-at-runtime>`
- `sessions/archive/session-83/computations-artifacts/s83_w2_harmonic_not_instanton_theorem.json`: `<computed-at-runtime>`

**Expected output 4-tuple**: `(value=<min_S_inst>, scheme=hessian_eigendirection_scan, convention=jensen_tau_wide_mesh, L_max=5)`

**Pass / Fail / INFO thresholds**:
- **PASS**: Minimum saddle action across all discovered families satisfies `min(S_inst) > 4.34` with `min(S_inst) / 4.34 > 1.0`; ideally `min(S_inst) ≳ S_fold / (small factor)` consistent with S_fold's isolation.
- **FAIL**: Any saddle family has `S_inst < 4.34` — the Borel summability argument leaks; the §W2-HARMONIC-NOT-INSTANTON theorem's applicability is narrower than claimed.
- **INFO**: `min(S_inst) ∈ (4.34, 10.0)` — no Borel leak, but the saddle structure is denser than S_fold alone suggests; log as a carry-forward for deeper analysis without failing.

**What PASS means**: The Borel-summable perturbative series around τ_fold has a clean well: no hidden small-action competitor. Semi-classical predictions derived from S_fold alone are justified.

**What FAIL means**: There is a competing saddle below the Borel threshold; semi-classical predictions need to account for multi-instanton contributions, invalidating several framework numerical claims (e.g., any calculation that assumed S_fold is the dominant non-perturbative action).

**Substitution chain** (required — direction claim "no saddle below threshold" is a quantified inequality):
1. **Definition**: `saddle_family := {(τ, direction_vector) : |dS/dτ| < ε_saddle AND Hessian has eigenvalue of each sign}`; `S_inst(saddle) := S(saddle) - S(τ_fold) + S_fold` (action measured from fold).
2. **Threshold**: `4.34` is the Borel radius `|S_inst| > 4.34 ⇔ the corresponding exp(-S_inst) contribution is summable in the asymptotic series`.
3. **Claim**: `min_{saddle families} S_inst > 4.34`.
4. **Direction**: the direction claim is `min > threshold`. Substitution: compute `min_over_saddles(S_inst)` via enumeration; compare to 4.34.
5. **Read off**: PASS iff min > 4.34 (from direct comparison of the computed min against the threshold value).
6. **Justification for threshold**: per §4.L anchor, `Borel threshold S_inst ≤ 4.34 for small-action saddles` comes from the Borel-plane singularity analysis; no substitution beyond numerical comparison required.

**Script**: `computations/s84_w10a_tau_kink_inventory_closure.py`
**Output artifacts**: `sessions/archive/session-84/computations-artifacts/s84_w10a_121_saddle_inventory.npz`, verdict line
**Effort**: 0.8 session (Hessian-eigendirection scan across wide τ mesh; most expensive item in W10a)

---

## W10a → W10b Parallel Dispatch Note

Wave 10a produces 12 verdict lines, each on an independent script under `computations/s84_w10a_*.py`. All 12 items are independent (no inter-item dependencies within W10a); they can be dispatched as a single parallel batch, respecting the **concurrent-dispatch cap of ≤8**:

**Batch 1 (8 concurrent)**: 110, 111, 112, 113, 114, 115, 116, 117
**Batch 2 (4 concurrent, after Batch 1 completes)**: 118, 119, 120, 121

Agent assignment:
- **sagan-empiricist**: 110, 111, 112, 118 (audit-integrity + formalization, 4 items)
- **connes-ncg-theorist**: 113, 115 (GV / cyclic cohomology explicit computations, 2 items)
- **van-den-dungen-bridge-theorist**: 114, 116, 117 (K-theoretic classification + layer diagnosis, 3 items)
- **gen-physicist**: 119, 120, 121 (fixed-point / convexity / saddle inventory, 3 items)

Each dispatch prompt MUST include:
1. The full §W10a-<NN> gate block verbatim (no abbreviation per `feedback_max-effort-full-fidelity.md`).
2. Explicit substrate-framing correction (GR/QFT-to-substrate inversion, per `phononic-framing.md`).
3. Canonical-constants import discipline (`from canonical_constants import *`; tag intermediates `# (local)`).
4. GPU prompt directive for §W10a-121 (`torch.linalg.eigh` required; numpy fallback with OMP_NUM_THREADS=8 only if GPU unavailable).
5. Pre-registered SHA pin discipline (full 64-char hexdigest; the `closure_sha256` is computed from the ordered input-pin map).

## W10a → (session close) Decision Point

W10a dispatches in parallel with other Wave 10 sub-blocks (W10b, W10c, ...) as organized by the session-84 plan orchestrator. The wave itself has no internal decision branching; it proceeds to completion as a closeout sweep.

**Session-close gate**: After all 12 W10a verdicts land, the S83 G55 FAIL is formally addressed. If §W10a-110 PASSES, the v3 dual-SHA migration is empirically ready to deploy. If §W10a-110 FAILS, escalate to a dedicated Wave 11 for v3-protocol-redesign.

---

## W10a Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, the PRDR machinery enumeration for W10a is:

| Gate | Free parameters enumerated | All pinned? |
|:-----|:-----|:-----|
| 110 | pin_map_ordering, hash_algorithm, encoding, 5 input-pin sources, tolerance | YES |
| 111 | scope (compact simple G), observable R(G), ansatz_space, derivation_path, tolerance (binary) | YES |
| 112 | N_eval=6 headers, source_file, header_pattern, body_verdict_extraction, tolerance (EXACT) | YES |
| 113 | 42-row atlas, 5 classification bins, cohomology_test method, zero_threshold=1e-10, tolerance | YES |
| 114 | 1 claim + 3 sub-verifications, A_F=C⊕H⊕M_3(C), K_0 rank=3, ch matrix, image_test, cocycle_extraction, tolerance 1e-8 outside / 1e-4 inside | YES |
| 115 | ω_J=e^{-τ}dτ, tau_fold=0.190, stencil_method=5pt central, stencil_err≤1e-6, integration_domain=M^4×SU(3)/T² | YES |
| 116 | 1 diagnosis, composite_identity (index from s83_w1_g6), layer_map (5-value tag), functoriality_test, tolerance (BINARY YES/NO) | YES |
| 117 | R-protected observable list, K_pairing computation, balance_criterion, 3 classification bins, tolerance (pairing ≠ 0 vs = 0) | YES |
| 118 | 42-row atlas, sha_field, pin_map_field, distinctness_test, independence_test 80% threshold | YES |
| 119 | τ mesh [0.10, 0.30] step 1e-4, Γ1' tolerance 0.134%, Γ5' strict positivity, Γ6 registry threshold | YES |
| 120 | 5 direction claims (n_T + 4 new), convexity_value=+317,863, derivation_chain per claim, cross_check from canonical_constants | YES |
| 121 | τ mesh [0.05, 0.35], ε_saddle threshold, Hessian-eigendirection scan, Borel_threshold=4.34, random_seed=42, GPU torch.linalg.eigh | YES |

**PRU audit**: 12/12 gates have all free parameters pinned. No PRU Class 8 vulnerability.

**Dry-run confirmations required before dispatch**:
- §W10a-110: confirm `s82_*_inputs.json` files exist for W1-1-TD, W2-13, W3-7.
- §W10a-115: confirm `J_C2` and `Vol_SU3` values are current in canonical_constants.py.
- §W10a-119: confirm `d2S_fold = +317,863` is the canonical value (matches S70 35D VP Hessian result).
- §W10a-121: confirm `S_fold = 2.5e5` and Borel threshold `4.34` are current constants.

---

## W10a Input-SHA Ledger

The following file paths must have their SHA-256 digests computed at script-start and logged in the first 20 lines of stdout per gate (per `.claude/rules/gate-verdicts.md`):

| Gate | Input pin files |
|:-----|:----------------|
| 110 | s82_gate_verdicts.txt; s82_w1_1_td_inputs.json; s82_w2_13_inputs.json; s82_w3_7_inputs.json; s83_g55_sha_collision_audit.json; canonical_constants.py |
| 111 | s82_gate_verdicts.txt; s82_w3_1_rank_universality.npz; Peter-Weyl reference anchors in researchers/Connes, researchers/Baptista |
| 112 | session-80-plan.md (or W1 sub-files); s80_gate_verdicts.txt |
| 113 | _vii_k_prop_atlas.json; s83_g56_gv_jensen_deform.npz; s83_g2_epsilon_h_heitsch_cm_hopf.npz; canonical_constants.py |
| 114 | s83_g2_epsilon_h_heitsch_cm_hopf.npz; s83_g4_epsilon_h_substrate_derivation.npz; _a_f_singleton_decomposition.json; researchers/Connes/moscovici_hopf_cyclic_cohomology.md; canonical_constants.py |
| 115 | s83_g56_gv_jensen_deform.npz; s83_g56_atiyah_singer_correction.json; canonical_constants.py |
| 116 | s83_w1_g6_fi_duality.npz; s83_vii_m_three_layer_theorem.json; _vii_k_prop_atlas.json; canonical_constants.py |
| 117 | s83_g14_c_s_regulator_dep.npz; s83_g26_sdw_nlo.npz; s83_g58_meta_principle_registry.json; _vii_k_prop_atlas.json; canonical_constants.py |
| 118 | _vii_k_prop_atlas.json; s83_gate_verdicts.txt; s83_g55_sha_collision_audit.json |
| 119 | canonical_constants.py; s70_35d_vp_hessian.npz; _vii_b_gear_registry.json |
| 120 | canonical_constants.py; s70_35d_vp_hessian.npz; s83_g50_n_t_bogoliubov.npz; s83_g7_cc7_dynamical.npz |
| 121 | canonical_constants.py; s70_35d_vp_hessian.npz; s83_w2_harmonic_not_instanton_theorem.json |

All verdict lines MUST carry the full 64-char `sha256=<closure>` hexdigest (S81+ canonical form).

All W10a scripts declare `schema_version = "S84+"` and emit both `audit_sha256=<>` and `content_sha256=<>` in addition to the legacy `sha256=<>` line (dual-SHA schema, per §W10a-110 carry into the canonical verdict format).

---

*End of Wave 10a plan. 12 items pre-registered. All PRDR-complete. Ready for parallel dispatch under the 8-concurrent cap (2 batches).*
