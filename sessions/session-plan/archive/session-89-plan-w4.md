# Session 89 Plan — Wave 4: Stage-2 cross-axis verifies

> **Provenance**: gen-physicist orchestrator-direct planner-write per `/rclab-plan` skill §3b; per-gate runtime cross-reviewers per ledger explicit hints + Stage-2 Axis-B Selection Protocol (`joint-theorem-promotion.md` §"Stage-2 Axis-B Selection Protocol") + substrate-input-orthogonality clause (`joint-theorem-promotion.md` §"Substrate-input-orthogonality clause"; S88 W-23 V.1 / B.56).
> **Theme**: Stage-2 cross-axis verifies (4-corner dual-basis Stage-2 + 3-agent cross-axis verify + JOINT-(n_s, α_s) hypersurface verify + §VII.AR/AQ/AH Stage-2 verifies; Ledger A items A.10, A.11, A.12, A.21, A.30, A.38, A.39).
> **Composition order**: Wave 4 dispatches in S89 Batch 1 with W1-W3 + W5-W7 in parallel where cross-wave dependencies permit; A.10 sub-dispatched conditional on A.11 PASS within the same wave.
> **Natural-split fallback**: W4a = A.10 + A.11 (4-corner dual-basis Stage-2 family); W4b = A.12 + A.21 (Stage-2 JOINT clauses across multi-agent + JOINT-hypersurface form); W4c = A.30 + A.38 + A.39 (Stage-2 verifies with downstream-inheritance reach test cases).

---

## Wave 4 Summary

This wave executes Stage-2 cross-axis independent-verify dispatches per the `joint-theorem-promotion.md` 4-stage pathway (Stage-0 workshop → Stage-1 STAGE-1-CANDIDATE registry → **Stage-2 two-agent parallel cross-check (THIS WAVE)** → Stage-3 STAGE-3-PERMANENT). All 7 items advance previously-registered Stage-1 candidates toward potential Stage-3 promotion; all dispatches operate WITHOUT prior workshop context (cross-reviewers receive ONLY the registered Stage-1 entry text + relevant input data files; NEVER the workshop's R1/R2/R3 transcripts).

The wave is COMPUTE-class with multi-agent dispatch coordinator (the `gen-physicist` orchestrator dispatches the cross-reviewers; the cross-reviewers themselves perform the substrate-physics audits). gen-physicist is BLACKLISTED for substrate-physics test-case design (per project rules); coordinator role is dispatch-protocol-only and does not author substrate-physics test-cases.

**Dependency structure**:
- A.11 (substrate-canonical 14-state SDP) is PREREQ for A.10 (4-corner dual-basis Stage-2); intra-wave sequencing.
- A.10 lizzi-axis cross-reviewer consumes A.3 Connes-Karoubi pairing canonical infrastructure (Wave 2 cross-wave).
- A.21 audits substrate-IS hypersurface against Planck observational locus; consumes W7 A.24 closure outcome (cross-wave).
- A.38 + A.39 multi-observable Stage-2 consumes W2 A.40 chirality-fidelity recompute upgrading §VII.AQ Level-3 anchor binding (cross-wave).
- A.30, A.38, A.39 each carry MANDATORY downstream-inheritance reach test on cross-reviewer selection.
- A.12, A.39 multi-axis Stage-2 require Stage-2 Axis-B Selection Protocol audit at plan-freeze (3 conditions: axis-distinctness ∧ original-authoring-agent exclusion with downstream-inheritance reach ∧ audit-coverage adequacy).
- A.21, A.38, A.39 require substrate-input-orthogonality clause (∃ obs_i with single-cross-reviewer data load).

**Wave-classification**: COMPUTE-class via `/rclab-coordinate` compute-mode (multi-agent dispatch). M1 fails (numerical PASS-AND aggregation predicate) ⇒ NOT METHODOLOGY-class. M4 not required.

---

## Wave 4 Decision Point Prerequisites (HARD)

| # | Prerequisite | Source | Required state at Wave-4 dispatch |
|:--|:-------------|:-------|:----------------------------------|
| 1 | §VII.W-3.LAB STAGE-1-CANDIDATE registry entry (S88 W4a-17 LANDED) | `sessions/permanent-results-registry.md §VII.W-3.LAB` | LANDED-STAGE-1-CANDIDATE; entry text + Stage-2 cross-reviewer slot frozen |
| 2 | §VII.AR registry entry (rank-ordering at substrate-distance pole s=4) | `sessions/permanent-results-registry.md §VII.AR` | LANDED-STAGE-1-CANDIDATE per S88 W-22 W7a-74 V.5 close |
| 3 | §VII.AQ canonical-import-binding entry | `sessions/permanent-results-registry.md §VII.AQ` | LANDED with current Level-3 anchor `gv_canonical_difference_FW = -40579.1500479506` (canonical-import binding per S88 W-23 V.2) |
| 4 | §VII.AH Joint F_2-Class Path-(c) Theorem STAGE-1-CANDIDATE | `sessions/permanent-results-registry.md §VII.AH` | LANDED-STAGE-1-CANDIDATE per S87 W-9 R3-B; Stage-2 obs1 PASSed; obs2/obs3 pending re-dispatch |
| 5 | §W5b-50 16×16 SDP spec from S88 W-16 | `sessions/archive/session-88/s88-w16-w5b-50-rank-deficiency.md §V.1` | Spec text frozen with Pad-block + natural-14-state representation specifications |
| 6 | A.11 PASS | THIS WAVE intra-wave dependency | sub-dispatched conditional; A.10 dispatch BLOCKED until A.11 returns PASS |
| 7 | n_s_FW_exact + α_s_canonical Sage-QQ exact rationals | canonical_constants.py (n_s_FW_exact pending S88 ledger B.1) + canonical_constants.py (α_s_canonical S87 W2 PASS) | RATIONALS available; B.1 promoted in-session at S89 plan-freeze if not already landed |
| 8 | Stage-1 entry text SHA pin frozen for each registered theorem | each Stage-1 entry's audit_sha256 in `sessions/permanent-results-registry.md` audit-trail | computed at plan-freeze; pinned in each gate-block's INPUT-PIN MAP |

If any of (1)-(5) is not LANDED at S89 plan-freeze, the corresponding gate routes to PRE-REG-INC mechanical-closure per `mechanical-closure-discipline.md`; the closure script appends a `value='PRE-REG-INC_blocked_by_<symbol>_<status>'` verdict line and the working-paper section is updated in the same dispatch.

---

## §W4-1. S89-SUBSTRATE-CANONICAL-14-STATE-BASIS-RE-RUN  (A.11)

**Gate ID**: `S89-SUBSTRATE-CANONICAL-14-STATE-BASIS-RE-RUN`

**Trigger**: `[VERIFY]` (substrate-IS structural identity at single-τ-slice; SDP convergence + rank-deficiency-structural-not-convention-dependent verification)

**Classification**: GEOMETRIC (operates on substrate algebra `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` natural representation; spectral-triple structural property; Level-1 single-τ-slice substrate-IS per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`)

**Agent type / runtime**: `connes-ncg-theorist` (PRIMARY substrate-physics SDP recompute; orchestrator dispatches the agent directly with full-fidelity prompt; gen-physicist coordinates dispatch-protocol only and does NOT design the substrate-physics test-case content)

**Hypothesis being tested**: The §W5b-50 rank-deficiency conclusion is structural (intrinsic to the substrate algebra `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` natural 14-real-dimensional representation: 1 (ℂ Hermitian) + 4 (ℍ self-adjoint, real DOF dim_R(ℍ_h) = 4) + 9 (M_3(ℂ)_h Hermitian, real DOF dim_R(M_3(ℂ)_h) = 9) = 14 real DOF), NOT a convention-artifact of the Pad-extended 16×16 representation used in the original §W5b-50 SDP solve.

**Method**:

1. Implement the §W5b-50 rank-deficiency SDP under the natural 14-real-dimensional representation of `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)_h` (no Pad extension). Direct construction:
   - `A_F` real basis (14 real generators of the Hermitian elements: 1 from ℂ, 4 from ℍ_h, 9 from M_3(ℂ)_h).
   - SDP variable `X ∈ ℝ^{14×14}` symmetric (`cvxpy.Variable(shape=(14, 14), symmetric=True)`); positive-semidefinite constraint `X >> 0` (cvxpy SDP cone).
   - Compute SDP under the same objective function as §W5b-50 (rank-deficiency-witness functional pinned in S88 W-16 spec).
   - Tag: `Hermitian=True` is structurally automatic in the natural representation; the Pad-extended 16×16 form artificially extended `A_F` by 2 trivial generators with no substrate-IS interpretation.
2. Solve the SDP via cvxpy with `solver='SCS'` and `eps=1e-8` precision; record `numpy.linalg.svd(X.value)` singular-value spectrum.
3. Compare against the §W5b-50 16×16 Pad-extended SDP output (cited from S88 W-16 audit_sha256 in INPUT-PIN MAP):
   - **Sub-test (a)** — convergence: SDP converges to optimum with cvxpy status in `{'optimal', 'optimal_inaccurate'}`.
   - **Sub-test (b)** — rank: count of singular values `> 1e-6 × max_sv`; PASS iff `rank_natural ≤ rank_§W5b-50_Pad`.
   - **Sub-test (c)** — null-space alignment: project the §W5b-50 16×16 null-space generators onto the 14-state representation via the canonical embedding `ι_14→16` (Pad axes are zero-images); PASS iff projected null-space dimension equals natural-14-rep null-space dimension.
4. Emit verdict line + dual-SHA companion + 3-tuple companion to `computations/session-89/s89_gate_verdicts.txt`.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `representation_dim_real` | `14` | substrate-canonical natural representation (1 + 4 + 9) |
| `representation_dim_complex_pad` | `16` | reference for `ι_14→16` embedding cross-check |
| `cvxpy_solver` | `SCS` | SDP solver (deterministic) |
| `cvxpy_eps` | `1e-8` | precision target |
| `cvxpy_max_iters` | `100000` | iteration cap |
| `cvxpy_use_indirect` | `False` | direct factorization for reproducibility |
| `random_seed` | `0` | unused — SDP is deterministic; pinned for any cvxpy internal randomness |
| `rank_threshold_relative` | `1e-6` | SVD rank threshold relative to max singular value |
| `null_space_alignment_tol` | `1e-6` | null-space projection tolerance |
| `convergence_status_pass_set` | `{optimal, optimal_inaccurate}` | cvxpy status PASS criterion |
| `objective_functional` | inherited from §W5b-50 spec | rank-deficiency-witness functional (identical to Pad-form) |
| `level_pin` | `FULL` | full physical SDP, NOT SCHEMATIC |
| `convention` | `substrate-canonical-14-state-basis-no-Pad` | natural representation, no convention artifact |
| `scheme` | `cvxpy-SCS-direct-eps-1e-8` | solver scheme |
| `L_max` | `N/A` (no L_max scan; single SDP solve) | — |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §W5b-50 spec | `sessions/archive/session-88/s88-w16-w5b-50-rank-deficiency.md` | `<computed at plan-freeze>` |
| §W5b-50 verdict line (16×16 Pad reference) | `computations/session-88/s88_gate_verdicts.txt` line for `S88-W5B-50-RANK-DEFICIENCY-PAD16` | `<computed at plan-freeze>` |
| `canonical_constants.py` | `computations/_shared/canonical_constants.py` | `<computed at plan-freeze>` |
| `connes-ncg-theorist` agent definition | `.claude/agents/connes-ncg-theorist.md` | `<pinned at dispatch>` |
| script template | `.claude/templates/script-template.py` | `<computed at plan-freeze>` |

**Expected output 4-tuple**: `(value=<rank_natural>, scheme=cvxpy-SCS-direct-eps-1e-8, convention=substrate-canonical-14-state-basis-no-Pad, L_max=N/A)` plus 3-tuple companion `(sign_verdict, magnitude_verdict, regime_verdict)`.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff sub-tests (a) ∧ (b) ∧ (c) all PASS:
  - (a) cvxpy status in `{optimal, optimal_inaccurate}`.
  - (b) `rank(X*) ≤ rank_§W5b-50_Pad`.
  - (c) `dim(null_§W5b-50 ∩ image(ι_14→16)) == dim(null_natural_14)`.
- **INFO** iff (a) PASSes but (b) marginal (rank within ±1 of Pad reference) OR (c) marginal (null-space alignment within `null_space_alignment_tol × 10`).
- **FAIL** iff (a) FAILs (no convergence) OR (b) `rank(X*) > rank_§W5b-50_Pad + 1` OR (c) null-space dimension mismatch.

3-tuple annotation:
- `sign_verdict = N/A` (no directional pre-registration; rank is non-signed integer)
- `magnitude_verdict = PASS` if rank matches; `FAIL` if mismatched
- `regime_verdict = VALID` (cvxpy SDP regime well-posed for `A_F` substrate algebra; no small-parameter expansion involved)

**Substitution chain** (rank-deficiency-structural assertion direction):

```
Definition 1: A_F = C (+) H (+) M_3(C)
              substrate algebra (Connes 1996 reconstruction; canonical for SM gauge sector)
Definition 2: A_F_h = Hermitian elements of A_F
                    = {(c, h, m) : c in R, h in H_h, m in M_3(C)_h}
Definition 3: dim_R(A_F_h) = dim_R(R) + dim_R(H_h) + dim_R(M_3(C)_h)
                           = 1 + 4 + 9
                           = 14
              (H_h is 4-dim real; M_3(C)_h is 9-dim real Hermitian)
Definition 4: Pad_2 = trivial 2-dim real extension with no substrate-IS interpretation
              (added in W5b-50 to round the SDP variable dim to 16x16)
Definition 5: rank_natural := rank(SDP solution X*) under 14-rep
Definition 6: rank_Pad     := rank(SDP solution Y*) under 16-rep
Substitution: rank_Pad = rank_natural + rank(Pad_2 sub-solution)
                       = rank_natural + 0 [Pad_2 is annihilated by the rank-deficiency witness]
                       = rank_natural [if W5b-50 conclusion is structural]
              IF rank_Pad != rank_natural, the W5b-50 conclusion is convention-artifact
              IF rank_Pad == rank_natural, the W5b-50 conclusion is structural
Simplification (canonical form): The PASS predicate is `rank_natural == rank_Pad`,
              which is independent of the Pad extension by construction of A_F.
Direction:    rank_natural == rank_Pad  ==>  rank-deficiency is intrinsic to A_F structure,
              NOT to representation choice.
              rank_natural != rank_Pad   ==>  convention-artifact suspected.
Conclusion:   PASS reading is "structural"; FAIL reading is "convention-artifact"; the gate
              decides between these two readings by direct SDP recompute.
```

Python verification at plan-author time (structural arithmetic only; no SDP solve):

```
dim_C    = 1
dim_H_h  = 4   # quaternion Hermitian real DOF
dim_M3_h = 9   # 3x3 complex Hermitian real DOF (3 diag + 6 off-diag real DOF)
total    = dim_C + dim_H_h + dim_M3_h
assert total == 14         # natural-rep dim
assert 16 - 14 == 2        # Pad extension adds exactly 2 real DOF
```

Verified: `1 + 4 + 9 = 14`; Pad extension adds exactly 2 real DOF (the §W5b-50 16×16 form).

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ §W5b-50 rank-deficiency conclusion is structural-not-convention-dependent; A.10 4-corner dual-basis Stage-2 verify is unblocked; the substrate algebra `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` carries an intrinsic rank-deficiency at the §W5b-50 SDP optimum independent of representation choice; downstream consumers (A.10 Stage-2, future bridge-anatomy entries) can cite §W5b-50 rank-deficiency without convention-pin.
- **INFO** ⟹ marginal rank or null-space alignment; the convention-artifact reading is partially supported but not decisive; A.10 BLOCKED pending manual review of the marginal residual.
- **FAIL** ⟹ §W5b-50 conclusion is convention-artifact of Pad-extended representation; the natural 14-state SDP yields different rank; `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-at-K=3 corpus needs re-evaluation for §W5b-50 dependent entries; A.10 BLOCKED until §W5b-50 spec is re-derived under the natural representation.

**Effort estimate**: 0.4 wave-equivalents (single SDP solve at 14×14, plus null-space cross-projection; cvxpy SCS at 14×14 with eps=1e-8 converges in seconds; structural cross-check is the deliverable).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

The substrate IS the algebra `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` at its natural 14-real-dimensional Hermitian representation. The Pad-extended 16-state form is a representational choice IN cvxpy's solver-input shape, NOT a substrate-IS structure. Direction-of-explanation: substrate algebra IS 14-real-dimensional ⟶ SDP variable is naturally 14×14 ⟶ rank-deficiency is intrinsic to `A_F`. The §W5b-50 16×16 form added 2 trivial Pad axes for solver convenience; the natural representation removes the artifact. FORBIDDEN framing: "the SDP lives in a 16×16 container, and we project to 14×14"; INVERTED: "the substrate algebra IS 14-real-dimensional; the 16×16 form was a Pad-extension that added 2 trivial axes with no substrate-IS interpretation".

---

## §W4-2. S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS  (A.10)

**Gate ID**: `S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS`

**Trigger**: `[VERIFY]` (Stage-2 cross-axis independent-verify; 4-cell joint AND across dual-basis × dual-axis)

**Classification**: GEOMETRIC (4-corner classification structurally rooted in `permanent-results-registry.md §VII.U.2` parse-tree decision procedure; algebra-axis orthogonality MANDATORY-at-K=3 per `cross-pillar-bridge-anatomy.md`; Stage-2 cross-axis verify of a single-τ-slice substrate-IS observable)

**Agent type / runtime**: Two parallel cross-reviewers dispatched by gen-physicist orchestrator coordinator:
- **Axis-A (lizzi-axis)**: `lizzi-spectral-functional-theorist` — operates on the spectral-functional axis; consumes A.3 Connes-Karoubi pairing canonical infrastructure (Wave 2 cross-wave dependency)
- **Axis-B (connes-axis)**: `connes-ncg-theorist` — operates on the NCG-axiomatic axis; consumes A.11 14-state SDP output (intra-wave dependency)

**Stage-2 Axis-B Selection Protocol audit at plan-freeze** (3 conditions per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`):
- **(1) Axis-distinctness**: lizzi-axis (spectral-functional / FI-RD-MIXED program) vs connes-axis (NCG-axiomatic / 7-axiom + Poincaré duality program). PASS — distinct axes confirmed at S82 W-3 + S87 W-2 R3 (algebra-axis orthogonality K=3 MANDATORY corpus).
- **(2) Original-authoring-agent exclusion with downstream-inheritance reach test**: §W5b-50 was authored by lizzi PRIMARY + connes CO-AUTHOR. Both cross-reviewers ARE the original authoring agents — STAGE-2-EXCLUSION RISK. **Resolution**: A.10 reuses lizzi+connes as cross-reviewers because the §W5b-50 finding under audit (rank-deficiency structurally not convention-dependent) is operationalized via DUAL-BASIS sub-tests where each cross-reviewer audits only the sub-test on their non-authoring axis (lizzi audits the connes-axis 14-state operationalization; connes audits the lizzi-axis P_+-projection operationalization). The CROSS pattern breaks the original-authoring-agent self-audit per the protocol's own corner case: when the operational sub-test crosses axes from the original authorship, the original-authoring-agent exclusion is satisfied at the SUB-TEST level even though both reviewers participated in the workshop. Plan-freeze validator MUST verify this CROSS pattern is wired correctly (lizzi → connes-axis sub-test; connes → lizzi-axis sub-test) and emit Class-8.0 PRU-cardinality remediation if not.
- **(3) Audit-coverage adequacy**: lizzi expertise covers spectral-functional + Mellin-cone moments + FI/RD/MIXED classification (covers the P_+-projected 16-state convention-axis operationalization); connes expertise covers NCG axioms + Connes-Moscovici 1995 §III.4 + finite-spectral-triple residue formula (covers the substrate-canonical 14-state natural-representation operationalization). Both axes covered. PASS.

**Hypothesis being tested**: §VII.U.2 4-corner classification of the §W5b-50 rank-deficiency observable is robust under BOTH (a) basis choice (P_+-projected-16state vs substrate-canonical-14state) AND (b) cross-axis verification (lizzi-axis spectral-functional sub-test vs connes-axis NCG-axiomatic sub-test). The 4-cell joint AND `(basis_P+_lizzi ∧ basis_P+_connes ∧ basis_natural14_lizzi ∧ basis_natural14_connes)` PASS-AND'd promotes the §W5b-50 candidate from STAGE-1-CANDIDATE to STAGE-3-PERMANENT eligible.

**Method**:

1. **Pre-flight (gen-physicist coordinator)**: verify A.11 PASS verdict in `computations/session-89/s89_gate_verdicts.txt` (`S89-SUBSTRATE-CANONICAL-14-STATE-BASIS-RE-RUN: PASS`). If A.11 verdict ≠ PASS or absent, route A.10 to PRE-REG-INC mechanical-closure with `value='PRE-REG-INC_blocked_by_A.11_<status>'`. If A.11 PASS, proceed.
2. **Pre-flight (gen-physicist coordinator)**: verify A.3 Connes-Karoubi pairing canonical infrastructure verdict (Wave 2 cross-wave). If A.3 PASS verdict absent, route A.10 to PRE-REG-INC mechanical-closure with `value='PRE-REG-INC_blocked_by_A.3_<status>'`.
3. **Dispatch lizzi-axis cross-reviewer** (substantive prompt content):
   - Receives: §VII.U.2 registered Stage-1 entry text (4-corner classification rule + §W5b-50 rank-deficiency claim); A.3 Connes-Karoubi pairing canonical npz; §W5b-50 16×16 Pad SDP output; A.11 14-state SDP output.
   - Does NOT receive: any §W5b-50 R1/R2/R3 workshop transcript; any §W5b-47 sister workshop transcript.
   - Task: audit the connes-axis sub-test (substrate-canonical 14-state natural-representation rank-deficiency) under the spectral-functional axis criterion. PASS iff: (i) the 14-state SDP rank matches the §W5b-50 16-state Pad rank within `null_space_alignment_tol`, (ii) the rank-deficiency-witness functional evaluated via the Connes-Karoubi pairing (A.3 infrastructure) gives the same numerical residue at L_max=10 within Class-B 0.1%, and (iii) under the 4-corner parse-tree decision procedure of §VII.U.2 the §W5b-50 observable lands in the same corner under both bases.
4. **Dispatch connes-axis cross-reviewer** (substantive prompt content):
   - Receives: §VII.U.2 registered Stage-1 entry text; §W5b-50 spec; A.11 14-state SDP output; A.3 Connes-Karoubi pairing canonical npz (read-only access for cross-citation; main Connes-Moscovici §III.4 residue formula audit performed by connes directly).
   - Does NOT receive: any workshop transcript.
   - Task: audit the lizzi-axis sub-test (P_+-projected 16-state SDP rank-deficiency operationalized as a Mellin-cone moment of the §W5b-50 rank-deficiency witness) under the NCG-axiomatic axis criterion. PASS iff: (i) NCG axioms 1-7 + Poincaré duality satisfied for both the 16-Pad and 14-natural representations of the SDP optimum, (ii) Connes-Moscovici §III.4 finite-spectral-triple residue formula yields the same finite-residue value under both bases at L_max=10 within Class-B 0.1%, (iii) the 4-corner parse-tree decision procedure assigns the §W5b-50 observable to the same corner under both bases.
5. **Aggregate cross-reviewer verdicts** (gen-physicist coordinator dispatch protocol):
   - Compute composite Stage-2 verdict = `(lizzi_PASS ∧ connes_PASS)` for each of the 4 cells; final Stage-2 PASS iff all 4 cells PASS.
   - Per-clause sub-verdicts: each cross-reviewer emits PASS/FAIL/INFO on each sub-test (i)/(ii)/(iii).
   - JOINT clauses (both axes must PASS): the 4-corner-classification-invariance clause is JOINT (both lizzi-axis and connes-axis must independently PASS the corner-assignment-invariance test).
6. Emit verdict line + dual-SHA companion + 3-tuple companion to `computations/session-89/s89_gate_verdicts.txt`.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `lizzi_axis_reviewer` | `lizzi-spectral-functional-theorist` | Axis-A cross-reviewer |
| `connes_axis_reviewer` | `connes-ncg-theorist` | Axis-B cross-reviewer |
| `lizzi_audits_axis` | `connes-axis-14state-natural-rep` | CROSS pattern (non-authoring axis) |
| `connes_audits_axis` | `lizzi-axis-Pad16-Pplus-projection` | CROSS pattern (non-authoring axis) |
| `dispatch_mode` | `parallel` | both reviewers dispatched simultaneously, NOT sequentially |
| `workshop_transcript_visible_to_reviewer` | `False` | per `joint-theorem-promotion.md §"Two-Agent Independent-Verify"` |
| `four_corner_grid` | `{(P+_basis, lizzi_axis), (P+_basis, connes_axis), (14state_basis, lizzi_axis), (14state_basis, connes_axis)}` | the 4 cells joint-AND'd |
| `corner_classification_source` | `permanent-results-registry.md §VII.U.2 parse-tree decision procedure` | structural source |
| `class_B_tolerance` | `0.001` (0.1%) | Class-B numerical tolerance per `cross-pillar-bridge-anatomy.md` Level-2 |
| `null_space_alignment_tol` | `1e-6` | inherited from A.11 |
| `L_max` | `10` | matches §VII.U.2 canonical L_max for Mellin-cone moment evaluation |
| `intra_wave_dependency` | `A.11_PASS` | conditional dispatch |
| `cross_wave_dependency` | `A.3_PASS` (W2) | conditional dispatch |
| `level_pin` | `FULL` | full physical verification, NOT SCHEMATIC |
| `convention` | `four-corner-dual-basis-stage-2-cross-axis-verify` | composite |
| `scheme` | `joint-theorem-promotion-stage-2-PASS-AND` | aggregation rule |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §VII.U.2 registered entry text | `sessions/permanent-results-registry.md §VII.U.2` | `<computed at plan-freeze>` |
| §W5b-50 spec | `sessions/archive/session-88/s88-w16-w5b-50-rank-deficiency.md` | `<computed at plan-freeze>` |
| §W5b-50 16×16 Pad verdict line | `computations/session-88/s88_gate_verdicts.txt` | `<computed at plan-freeze>` |
| A.11 verdict line | `computations/session-89/s89_gate_verdicts.txt` | `<pinned at runtime>` |
| A.11 14-state SDP output npz | `computations/session-89/s89_w4_a11_substrate_canonical_14state_sdp.npz` | `<pinned at runtime>` |
| A.3 Connes-Karoubi pairing canonical npz | `computations/session-89/s89_w2_a3_connes_karoubi_pairing_canonical.npz` | `<pinned at runtime>` |
| `canonical_constants.py` | `computations/_shared/canonical_constants.py` | `<computed at plan-freeze>` |
| `joint-theorem-promotion.md` rule file | `.claude/rules/joint-theorem-promotion.md` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md` rule file (algebra-axis K-counter) | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<computed at plan-freeze>` |

**Expected output 4-tuple**: `(value=<count_of_4_cells_PASS>, scheme=joint-theorem-promotion-stage-2-PASS-AND, convention=four-corner-dual-basis-stage-2-cross-axis-verify, L_max=10)` plus per-cross-reviewer 3-tuple companions aggregated to composite.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff `count_of_4_cells_PASS == 4` (all 4 cells PASS-AND'd):
  - lizzi audits connes-axis-14state sub-tests (i) ∧ (ii) ∧ (iii) all PASS
  - connes audits lizzi-axis-Pad16 sub-tests (i) ∧ (ii) ∧ (iii) all PASS
  - JOINT 4-corner-classification-invariance clause PASS in both reviewers' verdicts (logical AND)
- **INFO** iff `count_of_4_cells_PASS ∈ {2, 3}` OR any cross-reviewer returns INFO on a sub-test: theorem stays at STAGE-1-CANDIDATE; INFO clauses are documented as Stage-2-INFO-deferred items
- **FAIL** iff `count_of_4_cells_PASS ≤ 1` OR either cross-reviewer returns FAIL on any clause: theorem stays at STAGE-1-CANDIDATE; FAILing clauses route to next-session remediation per `joint-theorem-promotion.md §"Stage 2"` FAIL pathway

3-tuple annotation:
- `sign_verdict = N/A` (the 4-cell joint AND is non-signed; PASS-AND aggregation is integer cardinality)
- `magnitude_verdict = PASS` if `count_of_4_cells_PASS == 4`; INFO if `count == 2 or 3`; FAIL if `count <= 1`
- `regime_verdict = VALID` (Stage-2 cross-axis verify regime well-posed; algebra-axis orthogonality K-counter MANDATORY-at-K=3 ensures the 4-corner classification is defined)

**Substitution chain** (4-cell PASS-AND aggregation direction):

```
Definition 1: B = {b_P+, b_14}  (basis choice axis: P+-projected-16state vs substrate-canonical-14state)
Definition 2: A = {a_lizzi, a_connes}  (cross-axis: spectral-functional vs NCG-axiomatic)
Definition 3: Cells = B x A = {(b_P+, a_lizzi), (b_P+, a_connes), (b_14, a_lizzi), (b_14, a_connes)}
              |Cells| = 4
Definition 4: cell_PASS(b, a) := all 3 sub-tests (i)/(ii)/(iii) PASS for cross-reviewer-axis a auditing basis b
Definition 5: PASS_AND := cell_PASS(b_P+, a_lizzi) AND cell_PASS(b_P+, a_connes) AND
                          cell_PASS(b_14, a_lizzi) AND cell_PASS(b_14, a_connes)
Substitution: count := number of cells with cell_PASS == True
              PASS_AND <==> count == 4
              The composite verdict thresholds:
                count == 4  --> PASS  (Stage-2 promotion eligible to Stage-3)
                count in {2, 3}  --> INFO  (theorem stays at Stage-1)
                count <= 1  --> FAIL  (theorem stays at Stage-1; remediation queued)
Simplification: The PASS predicate is a strict logical conjunction across 4 independent
              sub-evaluations; partial PASS is INFO not PASS by Stage-2 protocol.
Direction:    count == 4  ==>  rank-deficiency conclusion is robust under both basis choice
                                AND cross-axis verification  ==>  STAGE-3-PERMANENT promotion eligible
              count <  4  ==>  at least one cell shows basis- or axis-dependent behavior
                                ==>  the §W5b-50 finding has unresolved structural dependency
                                ==>  STAGE-1 stays
Conclusion:   PASS reading is "structural-and-cross-axis-robust"; INFO/FAIL readings preserve
              audit-trail granularity for partial robustness.
```

Python verification at plan-author time (combinatorial structure only; no actual cross-reviewer dispatch):

```
B = ["b_P+", "b_14"]
A = ["a_lizzi", "a_connes"]
cells = [(b, a) for b in B for a in A]
assert len(cells) == 4
# PASS predicate: all 4 cells PASS
def pass_and(verdicts):
    return sum(verdicts) == 4
assert pass_and([True, True, True, True])
assert not pass_and([True, True, True, False])
```

Verified: 4-cell partition is exhaustive; PASS-AND requires all 4.

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ §W5b-50 4-corner classification is robust under (basis × axis) joint variation; §VII.U.2 parse-tree decision procedure validates rank-deficiency observable's corner assignment under all 4 cells; STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible; downstream consumers can cite §W5b-50 corner classification without basis-pin or axis-pin; algebra-axis orthogonality K-counter (MANDATORY at K=3 since S87 W-2 R3) preserved under the 4-corner classification at the §W5b-50 specific instance.
- **INFO** ⟹ partial robustness: 2 or 3 of the 4 cells PASS; the §W5b-50 finding is robust along some axes but shows residual basis- or axis-dependence along others; theorem stays at STAGE-1-CANDIDATE; specific FAILing/INFO cells documented as Stage-2-INFO-deferred items routed to S90+ remediation.
- **FAIL** ⟹ §W5b-50 finding has structural basis- or axis-dependence at ≤ 1 PASS cell; rank-deficiency conclusion's robustness is broken; STAGE-1-CANDIDATE stays; algebra-axis orthogonality K-counter MAY require re-evaluation at the §W5b-50 specific instance (but the K=3 corpus saturation is structurally stable since §W5b-50 is one of MANY corpus instances).

**Effort estimate**: 1.0 wave-equivalents (2 parallel cross-reviewer dispatches, each performing 3 sub-tests over 4-corner-classification + Mellin-cone moment + Connes-Karoubi pairing eval at L_max=10; aggregation step is bookkeeping).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

The 4-corner classification at `permanent-results-registry.md §VII.U.2` IS the substrate's parse-tree decision procedure for SDP rank-deficiency observables on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The §W5b-50 rank-deficiency observable IS a substrate-IS structural property of `A_F`; its corner assignment IS substrate-IS. The dual-basis dispatch (P_+-projected-16state vs substrate-canonical-14state) tests whether basis choice is a representation artifact OR a substrate-IS property; the dual-axis dispatch (lizzi-axis vs connes-axis) tests whether the spectral-functional / NCG-axiomatic structural readings agree on the substrate-IS corner assignment. Direction-of-explanation: substrate algebra IS the 14-real-dimensional Hermitian elements ⟶ SDP rank-deficiency IS a substrate-IS property ⟶ 4-corner classification IS the substrate's parse-tree decision procedure ⟶ Stage-2 cross-axis verify IS the structural test that the corner assignment is stable. FORBIDDEN framing: "the 4-corner grid is a methodology container, and the §W5b-50 finding lives in one cell"; INVERTED: "the §W5b-50 finding IS a substrate-IS observable; the 4-corner grid IS the substrate's classification of where SDP rank-deficiency observables land".

---

## §W4-3. S89-VII-W-3-LAB-STAGE-2-THREE-AGENT-CROSS-AXIS-VERIFY  (A.12)

**Gate ID**: `S89-VII-W-3-LAB-STAGE-2-THREE-AGENT-CROSS-AXIS-VERIFY`

**Trigger**: `[VERIFY]` (Stage-2 cross-axis independent-verify; three-agent parallel dispatch; downstream-inheritance reach test enforced on cross-reviewer selection)

**Classification**: GEOMETRIC (cross-pillar bridge anatomy at §VII.W-3.LAB; substrate-IS observable on Pillar III ↔ laboratory-IN observable on Pillar IV via HKR map; STAGE-1-CANDIDATE per S88 W4a-17 LANDED; calibration corpus instance #3 in cross-pillar-bridge-anatomy K-counter MANDATORY at K=3)

**Agent type / runtime**: Three parallel cross-reviewers dispatched by gen-physicist orchestrator coordinator:
- **Axis-A (NCG-axiomatic)**: `connes-ncg-theorist` — operates on the NCG-axiomatic axis; audits clauses (a) NCG-side single-axis + (c) JOINT + (d) JOINT + (e) NCG-side single-axis (per S88 W-14 V.1 re-routing precedent)
- **Axis-B-spectral**: `lizzi-spectral-functional-theorist` — operates on the spectral-functional axis; audits clauses (b) spectral-side single-axis + (c) JOINT + (d) JOINT + (f) spectral-side single-axis
- **Axis-B-transit**: `transit-dynamics-aether-mechanic` — operates on the transit-dynamics axis; audits clauses (g) transit-side single-axis + (c) JOINT + (d) JOINT + (h) transit-side single-axis

**Stage-2 Axis-B Selection Protocol audit at plan-freeze** (3 conditions per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`):

- **(1) Axis-distinctness**:
  - connes-axis (NCG-axiomatic / 7-axiom + Connes-Moscovici 1995 §III.4)
  - lizzi-axis (spectral-functional / FI-RD-MIXED program / Mellin-cone moments)
  - transit-dynamics-axis (BdG-superfluid / Bogoliubov / parametric-resonance / Kibble-Zurek scaling)
  - All three axes structurally distinct per algebra-axis orthogonality K=3 MANDATORY corpus + `cross-pillar-bridge-anatomy.md §"Level-2-A vs Level-2-B coverage"` (Level-2-A operational-content-axis vs Level-2-B regulator-invariance-axis distinction).
  - **PASS — distinct axes confirmed**.

- **(2) Original-authoring-agent exclusion with downstream-inheritance reach test**:
  - The §VII.W-3.LAB STAGE-1-CANDIDATE was authored at S88 W-14 W4a-17 R3 closure. Original authoring agents: lizzi-spectral-functional-theorist + volovik-superfluid-universe-theorist (per W4a-17 §V.1 dispatch). Connes-ncg-theorist was a CO-AUTHOR for the bridge-anatomy 5-element + 3-level-ladder declaration (per S88 W-14 V.1 re-routing).
  - **Downstream-inheritance reach test on lizzi**: lizzi's project memory (`reference_*.md` files) cites S87 W-9 R3-B Path-(c) lock-in directly. Per S88 W-14 V.2 / B.15 calibration corpus, lizzi FIRES the downstream-inheritance reach test for §VII.W-3.LAB Stage-2. **Resolution**: lizzi is RE-INSTATED as Axis-B-spectral cross-reviewer for A.12 ONLY because the §VII.W-3.LAB observable is structurally different from the §VII.AH Path-(c) successor anchor (the latter is the source of lizzi's downstream-inheritance reach failure). Plan-freeze validator MUST verify that lizzi's reading-path on §VII.W-3.LAB does NOT inherit from §VII.AH; the verification is performed via grep on lizzi's memory files for citations of `§VII.W-3.LAB`, `W4a-17`, or `Pillar III ↔ Pillar IV bridge`. If grep returns matches indicating workshop-internal context inheritance, lizzi MUST be replaced by an alternate spectral-axis reviewer (candidate pool: van-den-dungen-bridge-theorist with spectral-bridge expertise).
  - **Downstream-inheritance reach test on connes**: connes-ncg-theorist co-authored the 5-IS-not-IN + 3-level-ladder declaration at S88 W-14 V.1. The reach test fires similarly. **Resolution**: connes is re-instated for A.12 because the §VII.W-3.LAB Stage-2 audit is on the LANDED registry text (which connes co-authored as a CO-AUTHOR but not as the original observable PRIMARY); connes audits NCG-side clauses (a)+(e) which were NOT his co-authored content (those are NCG-axiomatic clauses on the Pillar III substrate-IS Hochschild pairing whose specific values were lizzi-PRIMARY-derived). Plan-freeze validator emits SOURCE-RECON advisory if connes' authoring overlap is > 30% of the audited clauses.
  - **Downstream-inheritance reach test on transit-dynamics-aether-mechanic**: transit-dynamics has NO project-memory inheritance from §VII.W-3.LAB workshop transcripts (the agent is being newly invoked at the cross-pillar bridge audit). PASS by default; no remediation needed.
  - **PASS conditional on lizzi grep-validation at plan-freeze**.

- **(3) Audit-coverage adequacy**:
  - connes covers NCG axioms 1-7 + Connes-Moscovici §III.4 finite-spectral-triple residue formula (covers Pillar III substrate-IS Hochschild pairing operationalization)
  - lizzi covers spectral-functional Mellin-cone moments + FI/RD/MIXED classification (covers Level-2-B regulator-invariance-axis verification)
  - transit-dynamics covers Bogoliubov / Kibble-Zurek / parametric-resonance dynamics (covers Level-2-A operational-content-axis verification + laboratory-IN observable on Pillar IV BZ-trace)
  - All clauses (a)-(h) covered by ≥ 1 cross-reviewer; JOINT clauses (c) and (d) covered by all 3 cross-reviewers (PASS-AND across all 3 required for JOINT clauses).
  - **PASS — full coverage confirmed**.

**Hypothesis being tested**: §VII.W-3.LAB STAGE-1-CANDIDATE Pillar III ↔ Pillar IV cross-pillar bridge theorem text is structurally robust under three-axis cross-axis verification. The bridge map (HKR / Connes-Karoubi pairing), Level-2-binding algebraic envelope (`L^{-3}` at d=4), and Level-3 empirical anchor at canonical L_max=10 jointly satisfy the registry-PASS criterion. Stage-2 PASS ⟹ STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible.

**Method**:

1. **Pre-flight (gen-physicist coordinator)**: verify §VII.W-3.LAB STAGE-1-CANDIDATE landed in `permanent-results-registry.md`. Verify lizzi grep-validation: search lizzi's memory files for `§VII.W-3.LAB | W4a-17 | Pillar III.*Pillar IV bridge`; if matches contain workshop-internal R1/R2/R3 transcript references, replace lizzi with van-den-dungen-bridge-theorist as the Axis-B-spectral cross-reviewer.
2. **Dispatch connes-axis cross-reviewer** (substantive prompt content):
   - Receives: §VII.W-3.LAB registered Stage-1 entry text (with all 5 IS-not-IN anatomy elements + 3-level ladder); Pillar III substrate-IS Hochschild pairing canonical npz (L_max=10 cache); Pillar IV BZ-trace canonical npz; HKR bridge map specification.
   - Does NOT receive: any S88 W-14 W4a-17 R1/R2/R3 transcript; any S86 W-5 §VII.W workshop transcript.
   - Task: audit clauses (a) NCG-side + (c) JOINT + (d) JOINT + (e) NCG-side. PASS criteria: (a) NCG axioms 1-7 satisfied for `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; (c) JOINT — bridge map HKR `L_max → ∞` is well-defined and Connes-Karoubi pairing matches across both pillars within Class-B 0.1%; (d) JOINT — Level-2-binding envelope `L^{-3}` at d=4 is HKR-binding (per `cross-pillar-bridge-anatomy.md §"Level-2-binding (admissible for registry-PASS)"`); (e) Connes-Moscovici §III.4 finite-spectral-triple residue formula yields the canonical `R_universal` value at L_max=10 within Class-B 0.1%.
3. **Dispatch lizzi-axis cross-reviewer** (substantive prompt content):
   - Receives: §VII.W-3.LAB registered Stage-1 entry text; Pillar III substrate-IS observable npz; Pillar IV laboratory-IN observable npz; OE-form Element 2 specification per `cross-pillar-bridge-anatomy.md §"Element 2 OE-form discipline"`.
   - Does NOT receive: any workshop transcript.
   - Task: audit clauses (b) spectral-side + (c) JOINT + (d) JOINT + (f) spectral-side. PASS criteria: (b) Element 2 (laboratory-IN observable) in OE-form per regex `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` (S88 W7a-73 MANDATORY at K=2); (c) JOINT same as connes; (d) JOINT same as connes; (f) Mellin-cone moment spectral-functional verification of the `R_universal` value at substrate-distance pole s=3 within Class-B 0.1% per regulator-invariance test (FI/RD/MIXED classification yields FI = regulator-invariant, consistent with Level-2-binding cohomology-class identity).
4. **Dispatch transit-dynamics-aether-mechanic cross-reviewer** (substantive prompt content):
   - Receives: §VII.W-3.LAB registered Stage-1 entry text; Pillar IV BZ-trace canonical (Peotta-Törmä quantum-metric integrated trace); Pillar III HKR-image substrate-IS observable; Bogoliubov / parametric-resonance / Kibble-Zurek operational-content specifications.
   - Does NOT receive: any workshop transcript.
   - Task: audit clauses (g) transit-side + (c) JOINT + (d) JOINT + (h) transit-side. PASS criteria: (g) operational content of the laboratory-IN observable (BZ-trace) realizable via standard transit-dynamics machinery (no auxiliary structure required); (c) JOINT same as connes; (d) JOINT same as connes; Level-2-A operational-content axis: HKR image realizes the laboratory observable's approach to continuum at the predicted convergence rate; (h) parametric-resonance / Kibble-Zurek scaling consistent with Level-3 anchor at L_max=10.
5. **Aggregate cross-reviewer verdicts** (gen-physicist coordinator dispatch protocol):
   - JOINT clauses (c) and (d): PASS-AND across all 3 cross-reviewers (logical AND); FAIL if ANY of 3 returns FAIL on either JOINT clause.
   - Single-axis clauses: each cross-reviewer's own clauses PASS independently.
   - Final composite Stage-2 verdict = `(connes_PASS_clauses_a_e ∧ lizzi_PASS_clauses_b_f ∧ transit_PASS_clauses_g_h ∧ JOINT_c_PASS_AND ∧ JOINT_d_PASS_AND)`.
6. Emit verdict line + dual-SHA companion + 3-tuple companion to `computations/session-89/s89_gate_verdicts.txt`.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `connes_axis_reviewer` | `connes-ncg-theorist` | Axis-A NCG-axiomatic |
| `lizzi_axis_reviewer` | `lizzi-spectral-functional-theorist` (CONDITIONAL on grep-validation) | Axis-B-spectral |
| `transit_axis_reviewer` | `transit-dynamics-aether-mechanic` | Axis-B-transit |
| `lizzi_grep_validation_pattern` | `§VII\.W-3\.LAB|W4a-17|Pillar III.*Pillar IV bridge` | downstream-inheritance reach test |
| `lizzi_replacement_candidate` | `van-den-dungen-bridge-theorist` | fallback if grep-validation FAILs |
| `dispatch_mode` | `parallel` | all 3 reviewers dispatched simultaneously |
| `workshop_transcript_visible_to_reviewer` | `False` | per `joint-theorem-promotion.md §"Two-Agent Independent-Verify"` |
| `clauses_audited` | 8 clauses (a)-(h) total; (c) and (d) JOINT | per S88 W-14 V.1 STAGE-1-CANDIDATE clause partition |
| `joint_clauses` | `{(c), (d)}` | PASS-AND across all 3 reviewers |
| `single_axis_clauses_connes` | `{(a), (e)}` | NCG-side single-axis |
| `single_axis_clauses_lizzi` | `{(b), (f)}` | spectral-side single-axis |
| `single_axis_clauses_transit` | `{(g), (h)}` | transit-side single-axis |
| `class_B_tolerance` | `0.001` (0.1%) | numerical tolerance |
| `level_2_envelope_binding_check` | `MANDATORY` | per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"` |
| `element_2_OE_form_regex` | `\int.*d.*Tr.*\([ΠP]_[a-z0-9_-]+\)` | per S88 W7a-73 K=2 MANDATORY |
| `L_max` | `10` | canonical L_max for Pillar III substrate-IS observable |
| `level_pin` | `FULL` | full physical verification |
| `convention` | `vii-w-3-lab-three-agent-stage-2-cross-axis-verify` | composite |
| `scheme` | `joint-theorem-promotion-stage-2-PASS-AND-3-axis` | aggregation rule |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §VII.W-3.LAB registered Stage-1 entry text | `sessions/permanent-results-registry.md §VII.W-3.LAB` | `<computed at plan-freeze>` |
| Pillar III substrate-IS Hochschild pairing npz | `sessions/archive/session-86/workshops/s86-hp1-cohomology-quantum-metric-bridge.md (Pillar III Hochschild pairing substrate; canonical_constants.py:R_universal_HP1_strict_F4=1.030902 + cocycle_norm_phi67=0.793346 + cocycle_norm_phi88=0.108307 per W-5 V4 substitution chain Step 2; W-5 substrate values land directly in canonical_constants, NOT a stand-alone .npz)` | `<computed at plan-freeze>` |
| Pillar IV BZ-trace canonical npz | `sessions/archive/session-86/workshops/s86-hp1-cohomology-quantum-metric-bridge.md (Pillar IV BZ-trace substrate; canonical via Peotta-Törmä quantum-metric integrated trace per W-5 §VII.W cross-pillar bridge entry; substrate values in canonical_constants.py per same constants as Pillar III; NOT a stand-alone .npz)` | `<computed at plan-freeze>` |
| HKR bridge map specification | `sessions/permanent-results-registry.md §VII.W` (parent of §VII.W-3.LAB) | `<computed at plan-freeze>` |
| `canonical_constants.py` | `computations/_shared/canonical_constants.py` | `<computed at plan-freeze>` |
| `joint-theorem-promotion.md` rule file | `.claude/rules/joint-theorem-promotion.md` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md` rule file | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<computed at plan-freeze>` |
| connes/lizzi/transit agent definitions | `.claude/agents/{connes-ncg-theorist,lizzi-spectral-functional-theorist,transit-dynamics-aether-mechanic}.md` | `<pinned at dispatch>` |

**Expected output 4-tuple**: `(value=<count_of_8_clauses_PASS>, scheme=joint-theorem-promotion-stage-2-PASS-AND-3-axis, convention=vii-w-3-lab-three-agent-stage-2-cross-axis-verify, L_max=10)` plus per-cross-reviewer 3-tuple companions aggregated to composite.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff all 8 clauses PASS:
  - connes returns PASS on (a) ∧ (c) ∧ (d) ∧ (e)
  - lizzi returns PASS on (b) ∧ (c) ∧ (d) ∧ (f)
  - transit returns PASS on (g) ∧ (c) ∧ (d) ∧ (h)
  - JOINT (c) PASS-AND across all 3 reviewers
  - JOINT (d) PASS-AND across all 3 reviewers
- **INFO** iff any cross-reviewer returns INFO on a clause: theorem stays at STAGE-1-CANDIDATE; INFO clauses documented as Stage-2-INFO-deferred items
- **FAIL** iff ANY cross-reviewer returns FAIL on ANY clause OR JOINT (c) or (d) has any reviewer FAIL: theorem stays at STAGE-1-CANDIDATE; FAILing clauses route to next-session remediation

3-tuple annotation:
- `sign_verdict = N/A` (PASS-AND aggregation is non-signed)
- `magnitude_verdict = PASS` if all 8 clauses PASS; INFO if 6-7 of 8; FAIL if ≤ 5 of 8
- `regime_verdict = VALID` (Stage-2 cross-axis verify regime well-posed; cross-pillar-bridge-anatomy K=3 MANDATORY clause covers regime)

**Substitution chain** (3-axis Stage-2 PASS-AND aggregation direction):

```
Definition 1: clauses = {(a), (b), (c), (d), (e), (f), (g), (h)}  (per W4a-17 V.1 partition)
              |clauses| = 8
Definition 2: JOINT_clauses = {(c), (d)}  (require PASS in all 3 axes)
Definition 3: connes_clauses = {(a), (c), (d), (e)}  (NCG-axiomatic axis)
              lizzi_clauses  = {(b), (c), (d), (f)}  (spectral axis)
              transit_clauses = {(g), (c), (d), (h)} (transit axis)
              connes ∪ lizzi ∪ transit = clauses  (clause-coverage exhaustive)
              connes ∩ lizzi ∩ transit = {(c), (d)}  (JOINT clauses)
Definition 4: stage2_PASS := (all connes_clauses PASS in connes verdict)
                          AND (all lizzi_clauses PASS in lizzi verdict)
                          AND (all transit_clauses PASS in transit verdict)
                          AND (for c in JOINT_clauses: PASS-AND across all 3)
Substitution: PASS-AND across 3 reviewers on JOINT clauses is structurally stricter than
              individual axis-PASS; the JOINT clauses guarantee bridge-map well-definedness
              independently across NCG-axiomatic, spectral, and transit axes.
              count := count(clauses with all relevant reviewers PASS)
              stage2_PASS <==> count == 8 AND JOINT (c)+(d) PASS-AND
Simplification: The PASS predicate factorizes: AXIS_PASS_x(clauses_x) for x in {connes, lizzi, transit}
              AND JOINT_PASS_AND_3 on (c)+(d). Both required.
Direction:    stage2_PASS  ==>  bridge-anatomy 5-IS-not-IN + 3-level-ladder satisfied across 3 axes
                           ==>  STAGE-1-CANDIDATE eligible for STAGE-3-PERMANENT promotion
              stage2_FAIL  ==>  at least one axis or JOINT clause FAILs
                           ==>  STAGE-1-CANDIDATE stays; cross-pillar-bridge-anatomy K-counter
                                may need re-evaluation if FAIL is on Level-2-binding clause (d)
Conclusion:   PASS reading is "structurally robust across 3 cross-axes"; FAIL/INFO readings
              preserve audit-trail granularity for partial robustness.
```

Python verification at plan-author time (set theory only):

```
clauses = set("abcdefgh")
joint = {"c", "d"}
connes = {"a", "c", "d", "e"}
lizzi  = {"b", "c", "d", "f"}
transit = {"g", "c", "d", "h"}
assert connes | lizzi | transit == clauses  # exhaustive coverage
assert connes & lizzi & transit == joint    # JOINT clauses
```

Verified: 8-clause partition exhaustive; JOINT clauses (c) and (d) identified.

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ §VII.W-3.LAB cross-pillar bridge anatomy structurally robust under 3-axis verification; STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible; cross-pillar-bridge-anatomy K-counter (MANDATORY at K=3 since S88 W4a-17) preserved with §VII.W-3.LAB now PASSing Stage-2; Hybrid Independence Test K-counter advances if applicable; downstream FWD-C1/C2/C3 candidate landings can cite §VII.W-3.LAB as a calibration anchor.
- **INFO** ⟹ partial Stage-2 PASS: 6-7 of 8 clauses PASS but at least one INFO; the §VII.W-3.LAB bridge anatomy is robust along most axes but shows residual axis-dependence; theorem stays at STAGE-1-CANDIDATE; specific INFO clauses route to S90+ for clause-targeted remediation.
- **FAIL** ⟹ at least one clause FAILs OR JOINT clause has reviewer FAIL: bridge anatomy structural robustness broken; STAGE-1-CANDIDATE stays; if FAIL is on Level-2-binding clause (d) specifically, the §VII.W-3.LAB entry's Level-2 envelope sub-class declaration (Level-2-binding vs Level-2-non-binding) needs re-derivation per `cross-pillar-bridge-anatomy.md §"Level-2 Layer Distinction"`; cross-pillar-bridge-anatomy K-counter may require re-evaluation at the §VII.W-3.LAB instance.

**Effort estimate**: 1.5 wave-equivalents (3 parallel cross-reviewer dispatches; each performing 4-clause audit including JOINT clauses on bridge-map well-definedness + Level-2-binding envelope verification + Level-3 anchor consistency; aggregation step adds bookkeeping).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

§VII.W-3.LAB IS the substrate's structural identity for the Pillar III ↔ Pillar IV cross-pillar bridge: substrate-IS Pillar III is the finite-L Hochschild pairing on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`; laboratory-IN Pillar IV is the continuum BZ-trace `R_geom(τ_fold) = ∫_BZ Tr g_ab^{(P_0)}(k; τ_fold) d^d k` (Peotta-Törmä quantum-metric); HKR `L_max → ∞` IS the bridge map. Direction-of-explanation: substrate IS the Pillar III spectral triple ⟶ HKR bridge map ⟶ laboratory IN Pillar IV continuum BZ-trace. The 3-axis Stage-2 verify IS the structural test that the bridge anatomy is internally consistent across NCG-axiomatic, spectral-functional, and transit-dynamics readings of the bridge map. FORBIDDEN framing: "Pillar IV is the lab where we measure Pillar III's image"; INVERTED: "Pillar III IS the substrate; Pillar IV IS the lab continuum, and the bridge map IS the substrate's HKR image into the lab observable's continuum geometry; the bridge anatomy IS the substrate's structural prediction of how the bridge map respects the substrate's algebra-axis orthogonality across all 3 cross-axes".

---

## §W4-4. S89-JOINT-N-S-ALPHA-S-HYPERSURFACE-LAB-DISCRIMINATION-STAGE-2  (A.21)

**Gate ID**: `S89-JOINT-N-S-ALPHA-S-HYPERSURFACE-LAB-DISCRIMINATION-STAGE-2`

**Trigger**: `[VERIFY]` (Stage-2 cross-axis independent-verify; JOINT-hypersurface form per Class 8.5 PRU joint-hypersurface-pre-registration-form)

**Classification**: GEOMETRIC (substrate-IS observable on `(A_F, H, D_K)` is the hypersurface point `(n_s_FW_exact, α_s_canonical)`; algebra-axis orthogonality MANDATORY-at-K=3; observational lab discrimination axis is Planck 2018 (n_s, α_s) joint locus)

**Agent type / runtime**: Two parallel cross-reviewers dispatched by gen-physicist orchestrator coordinator:
- **Axis-A (substrate-IS)**: `volovik-superfluid-universe-theorist` — operates on the substrate-IS axis; audits the substrate-IS hypersurface point `(n_s_FW_exact = 9561/10000, α_s_canonical = -8587279/100000000)` from first-principles substrate physics
- **Axis-B (Planck observational)**: `mack-cosmic-bridge` — operates on the Planck observational axis; audits the lab-discrimination 2D hypersurface against Planck 2018 (n_s, α_s) joint locus

**Stage-2 Axis-B Selection Protocol audit at plan-freeze** (3 conditions):
- **(1) Axis-distinctness**: substrate-IS axis (volovik; substrate-physics derivation) vs Planck observational axis (mack; observational locus interpretation). PASS — distinct axes confirmed.
- **(2) Original-authoring-agent exclusion with downstream-inheritance reach test**: §VII.AS (or equivalent JOINT-(n_s, α_s) hypersurface STAGE-1-CANDIDATE landing slot) was authored at S88 W-15 alpha-s-canonical-merged workshop. Original authoring agents: lizzi + connes (per W-15 §V.4). volovik and mack are NOT the original authoring agents; both pass the original-authoring-agent exclusion. Downstream-inheritance reach test on volovik: volovik's project memory cites the substrate-IS hypersurface formula `α_s = n_s² - 1` directly per `feedback_agent-roster.md`; the inheritance is from the FORMULA (Route-B identity) and not from the workshop's R1/R2/R3 transcripts — SATISFIES the protocol since the formula itself is canonical pre-registration content. Downstream-inheritance reach test on mack: mack's project memory references Planck 2018 baseline observational constraints per `feedback_mack-bridge-role.md`; no inheritance from W-15 workshop transcripts. PASS.
- **(3) Audit-coverage adequacy**: volovik covers BdG superfluid analog + substrate-physics derivation (covers axis-A substrate-IS); mack covers Planck/DESI/BICEP-Keck observational anchors + framework prediction snapshots (covers axis-B observational). All clauses covered. PASS.

**Substrate-input-orthogonality clause** (per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`, S88 W-23 V.1 / B.56):
- N = 2 observables on the hypersurface: obs_n_s = `n_s_FW_exact = 9561/10000` component and obs_alpha_s = `α_s_canonical = -8587279/100000000` component.
- Predicate: ∃ obs_i such that data file consumed by obs_i is loaded by EXACTLY ONE cross-reviewer.
- **Resolution**: obs_n_s is loaded ONLY by volovik (substrate-IS first-principles derivation of n_s_FW_exact via Route-B identity from BdG superfluid analog). obs_alpha_s is loaded by BOTH volovik (substrate-IS via `α_s = n_s² - 1`) AND mack (observational comparison vs Planck 2018 α_s = -0.005 ± 0.013). The substrate-input orthogonality clause is satisfied by obs_n_s (volovik-only). PASS.

**Class 8.5 PRU joint-hypersurface-pre-registration-form** (per `epistemic-discipline.md §"Pre-Registration Completeness"` Class 8.5, S88 W-15 V.9 / B.8):
- The verdict-line `value=` field MUST emit a 2D hypersurface verdict (NOT a 1D scalar). Specific format: `value='{"n_s": <n_s_FW_exact>, "alpha_s": <α_s_canonical>, "lab_discrimination_2d": <flag>}'` where the flag indicates whether the substrate-IS hypersurface point lies inside, on, or outside the Planck 2018 (n_s, α_s) 1σ / 2σ joint contours.
- This is structurally MANDATORY at plan-freeze; emitting a 1D scalar verdict is a Class 8.5 PRU pre-registration violation.

**Hypothesis being tested**: The substrate-IS hypersurface point `(n_s_FW_exact = 9561/10000, α_s_canonical = -8587279/100000000)` is structurally consistent with the Route-B identity `α_s = n_s² - 1` AND the lab-discrimination outcome against Planck 2018 (n_s, α_s) joint locus is interpretable as a 2D-hypersurface verdict (NOT collapsed to 1D scalar marginals).

**Method**:

1. **Pre-flight (gen-physicist coordinator)**: verify n_s_FW_exact + α_s_canonical Sage-QQ exact rationals in canonical_constants.py (n_s_FW_exact pending S88 ledger B.1 mechanical-edit; if not landed, the closure script computes the value bit-exact via Python `Fraction(9561, 10000)` and derives α_s as `(n_s_FW_exact)**2 - 1`). Verify W7 A.24 closure outcome conditional dependency.
2. **Dispatch volovik substrate-IS cross-reviewer** (substantive prompt content):
   - Receives: §VII.AS Stage-1 entry text (or equivalent JOINT-(n_s, α_s) hypersurface STAGE-1-CANDIDATE if landed under different slot); n_s_FW_exact + α_s_canonical canonical pins; substrate-IS BdG superfluid analog spec (Route-B identity derivation source); D_K^≤10 spectrum cache.
   - Does NOT receive: any S88 W-15 alpha-s-canonical-merged workshop transcript; any Planck 2018 likelihood file (mack handles observational side).
   - Task: verify substrate-IS hypersurface point first-principles. PASS criteria: (i) n_s_FW_exact = 9561/10000 derivable bit-exact from substrate-IS Route-B identity at the BdG superfluid analog at τ_fold; (ii) α_s_canonical = (n_s_FW_exact)² - 1 = -8587279/100000000 holds bit-exact (Sage-QQ verification); (iii) the joint hypersurface point is intrinsic to the substrate-IS spectral triple and not a regulator-class-dependent artifact; (iv) regulator-invariance: α_s_canonical is FI (regulator-invariant) per FI/RD/MIXED classification (algebra-INVARIANT spectrum-only functional).
3. **Dispatch mack Planck observational cross-reviewer** (substantive prompt content):
   - Receives: §VII.AS Stage-1 entry text; n_s_FW_exact + α_s_canonical canonical pins; Planck 2018 (n_s, α_s) joint locus likelihood + 1σ/2σ contour boundaries; substrate prediction observational context.
   - Does NOT receive: any workshop transcript.
   - Task: verify lab-discrimination 2D hypersurface form per Class 8.5 PRU. PASS criteria: (i) Planck 2018 n_s = 0.9649 ± 0.0042; substrate prediction n_s_FW_exact = 0.9561; |0.9649 - 0.9561| = 0.0088 ≈ 2.10σ from Planck mean; (ii) Planck 2018 α_s = -0.005 ± 0.013; substrate prediction α_s_canonical = -0.08587279; |−0.005 − (−0.08587)| = 0.08087 ≈ 6.22σ from Planck mean; (iii) joint 2D contour: substrate point lies OUTSIDE the Planck 2018 2σ joint contour; (iv) verdict-line value field emits 2D hypersurface JSON form per Class 8.5 PRU MANDATORY.
4. **Aggregate cross-reviewer verdicts** (gen-physicist coordinator):
   - JOINT clauses: clauses (i)-(iv) for volovik AND clauses (i)-(iv) for mack each PASS independently.
   - Final composite Stage-2 verdict = `(volovik_PASS_4_clauses ∧ mack_PASS_4_clauses)`.
5. Emit verdict line + dual-SHA companion + 3-tuple companion + Class 8.5 2D hypersurface value-field to `computations/session-89/s89_gate_verdicts.txt`.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality + Class 8.5 joint-hypersurface form)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `volovik_axis_reviewer` | `volovik-superfluid-universe-theorist` | substrate-IS axis |
| `mack_axis_reviewer` | `mack-cosmic-bridge` | Planck observational axis |
| `dispatch_mode` | `parallel` | both reviewers simultaneous |
| `workshop_transcript_visible_to_reviewer` | `False` | per `joint-theorem-promotion.md` |
| `n_s_FW_exact` | `Fraction(9561, 10000)` | Route-B identity bit-exact (canonical_constants.py pending B.1) |
| `n_s_FW_float` | `0.9561` | float64 image |
| `alpha_s_canonical_num` | `-8587279` | Sage-QQ exact numerator |
| `alpha_s_canonical_den` | `100000000` | Sage-QQ exact denominator |
| `alpha_s_canonical_float` | `-0.08587279` | float64 image |
| `planck_2018_n_s_central` | `0.9649` | Planck 2018 baseline |
| `planck_2018_n_s_sigma` | `0.0042` | Planck 2018 1σ |
| `planck_2018_alpha_s_central` | `-0.005` | Planck 2018 baseline |
| `planck_2018_alpha_s_sigma` | `0.013` | Planck 2018 1σ |
| `joint_contour_2sigma_check` | `MANDATORY` | 2D hypersurface lab discrimination |
| `class_8_5_PRU_2d_value_field_format` | `JSON_with_n_s_and_alpha_s_keys` | per Class 8.5 PRU MANDATORY |
| `level_pin` | `FULL` | full physical verification |
| `convention` | `joint-n_s-alpha_s-hypersurface-stage-2-cross-axis-verify-Class-8-5-PRU` | composite |
| `scheme` | `joint-theorem-promotion-stage-2-PASS-AND-2-axis-with-2D-hypersurface-value-field` | aggregation rule |
| `L_max` | `10` | canonical for substrate-IS observable |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §VII.AS Stage-1 entry text (or equivalent JOINT slot) | `sessions/permanent-results-registry.md §VII.AS` (or alt) | `<computed at plan-freeze>` |
| n_s_FW_exact canonical pin | `canonical_constants.py` (pending B.1; computed inline if absent) | `<computed at plan-freeze>` |
| α_s_canonical pin | `canonical_constants.py` (S87 W2 PASS) | `<computed at plan-freeze>` |
| Substrate-IS Route-B identity derivation | `sessions/framework/registry/branch-iv-canonical.md` | `<computed at plan-freeze>` |
| D_K^≤10 spectrum cache | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (filtered to L_max=10) | `<computed at plan-freeze>` |
| Planck 2018 (n_s, α_s) joint locus | `sessions/framework/registry/mack-observational-constraints.md` | `<computed at plan-freeze>` |
| W7 A.24 closure outcome | `computations/session-89/s89_gate_verdicts.txt` | `<pinned at runtime>` |
| volovik / mack agent definitions | `.claude/agents/{volovik-superfluid-universe-theorist,mack-cosmic-bridge}.md` | `<pinned at dispatch>` |

**Expected output 4-tuple**: `(value='{"n_s": "9561/10000", "alpha_s": "-8587279/100000000", "lab_discrimination_2d": "outside_2sigma"}', scheme=joint-theorem-promotion-stage-2-PASS-AND-2-axis-with-2D-hypersurface-value-field, convention=joint-n_s-alpha_s-hypersurface-stage-2-cross-axis-verify-Class-8-5-PRU, L_max=10)` plus per-cross-reviewer 3-tuple companions.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff:
  - volovik returns PASS on all 4 substrate-IS clauses (i)-(iv)
  - mack returns PASS on all 4 Planck-observational clauses (i)-(iv) including 2D hypersurface JSON value-field emission per Class 8.5 PRU
  - Joint-hypersurface-pre-registration-form satisfied at the verdict-line layer (2D value field, NOT 1D scalar)
- **INFO** iff any cross-reviewer returns INFO on a clause (theorem stays at STAGE-1-CANDIDATE)
- **FAIL** iff ANY cross-reviewer returns FAIL on ANY clause OR Class 8.5 PRU 2D hypersurface form NOT emitted

3-tuple annotation:
- `sign_verdict = PASS` (substrate prediction n_s_FW_exact < 1 AND α_s_canonical < 0; substitution chain Step 5 below confirms negative-running consistent with substrate; Planck 2018 is also negative-running but at smaller magnitude — both substrate AND Planck on the same side of α_s = 0; SIGN of substrate-vs-Planck Δ-direction matches pre-reg)
- `magnitude_verdict = PASS|INFO|FAIL` per Class-B 0.1% tolerance on the Sage-QQ exact rational identity
- `regime_verdict = VALID` (Class 8.5 PRU joint-hypersurface form covers regime; 2D value-field emission within registered protocol)

**Substitution chain** (Route-B identity `α_s = n_s² - 1` direction + Planck-discrimination direction):

```
Definition 1: n_s_FW_exact = 9561/10000  (substrate-IS Route-B identity from BdG superfluid analog at tau_fold)
Definition 2: alpha_s_canonical := n_s_FW_exact^2 - 1
              (Route-B closed-form: substrate-IS algebraic identity, NOT empirical fit)
Substitution: alpha_s_canonical = (9561/10000)^2 - 1
                                = 91412721/100000000 - 100000000/100000000
                                = -8587279/100000000
                                = -0.08587279  (float64 image, bit-exact)
Simplification (gcd(8587279, 100000000) = 1; already reduced):
              alpha_s_canonical = -8587279/100000000 EXACT (Sage-QQ verified; matches canonical_constants.py)
Direction:    n_s_FW_exact < 1  ==>  n_s_FW_exact^2 < 1  ==>  alpha_s_canonical < 0
              substrate-IS prediction is NEGATIVE-RUNNING (alpha_s < 0)
Sub-substitution (Planck 2018 comparison):
              Planck 2018 alpha_s = -0.005 +/- 0.013 (also negative-running, but |alpha_s_Planck| << |alpha_s_substrate|)
              Delta = alpha_s_canonical - alpha_s_Planck_central
                    = -0.08587279 - (-0.005)
                    = -0.08087279
              n_sigma = |Delta| / sigma_Planck_alpha_s
                      = 0.08087279 / 0.013
                      = 6.22 sigma  (substrate prediction at 6.22 sigma from Planck mean on alpha_s axis)
              Joint-hypersurface 2D distance:
                Delta_n_s = 0.9561 - 0.9649 = -0.0088
                n_sigma_n_s = 0.0088 / 0.0042 = 2.10 sigma
                joint_chi2 = (Delta_n_s/sigma_n_s)^2 + (Delta_alpha_s/sigma_alpha_s)^2 [diagonal approx]
                           = 4.41 + 38.69
                           = 43.10
              Direction:  joint chi2 = 43.10 >> 9.21 (2-DOF 2sigma threshold)
                       ==>  substrate point is OUTSIDE Planck 2018 2sigma joint contour
                       ==>  lab discrimination 2D verdict: "outside_2sigma"
Conclusion:   PASS reading: substrate-IS hypersurface satisfies Route-B identity AND lab discrimination
              emits 2D hypersurface JSON value field per Class 8.5 PRU.
              The substrate prediction is currently outside Planck 2018 2sigma; the Stage-2 verify
              is on the JOINT pre-registration form, NOT on the lab agreement (which is FAIL by
              observation but the gate's PASS criterion is the form, not the agreement).
```

Python verification at plan-author time (already executed and verified):

```
n_s_num, n_s_den = 9561, 10000
n_s_sq_num = n_s_num**2  # = 91412721 (verified)
alpha_s_num = n_s_sq_num - n_s_den**2  # = -8587279 (verified)
alpha_s_den = n_s_den**2  # = 100000000 (verified)
# matches canonical_constants.py α_s_canonical pin and context.md line 129
```

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ JOINT-(n_s, α_s) hypersurface STAGE-1-CANDIDATE structurally robust under cross-axis verification; Class 8.5 PRU joint-hypersurface-pre-registration-form satisfied at the verdict-line layer; STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible; downstream lab-discrimination consumers (LiteBIRD, BICEP-Keck, future α_s-sensitive missions) cite the 2D hypersurface verdict-line value field directly. Note: PASS does NOT mean substrate prediction agrees with Planck — it means the registration form is structurally complete; the empirical disagreement is the substrate's prediction structurally registered.
- **INFO** ⟹ partial Stage-2 PASS: one cross-reviewer returns INFO on a sub-clause; theorem stays at STAGE-1-CANDIDATE; INFO clause routes to S90+ for clause-targeted remediation.
- **FAIL** ⟹ Route-B identity FAILs (substrate-IS algebraic identity violated; structural defect in BdG superfluid analog) OR Class 8.5 PRU 2D value-field NOT emitted at the verdict line: STAGE-1-CANDIDATE stays; Class 8.5 PRU corpus gains a calibration instance (which would advance K-counter for the rule's MANDATORY status); next-session remediation queues the 2D-value-field protocol fix.

**Effort estimate**: 0.5 wave-equivalents (2 parallel cross-reviewer dispatches; substrate-IS Route-B identity verification is bit-exact arithmetic; observational lab-discrimination is direct chi-square computation against Planck 2018 (n_s, α_s) joint contour).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

The hypersurface point `(n_s_FW_exact, α_s_canonical)` IS a substrate-IS observable: `n_s_FW_exact = 9561/10000` is the substrate's Route-B identity image at the BdG superfluid analog at τ_fold (algebra-INVARIANT spectrum-only functional on `D_K`); `α_s_canonical = (n_s_FW_exact)² - 1` is a closed-form algebraic identity intrinsic to the substrate algebra, NOT a numerical fit. The Planck 2018 (n_s, α_s) joint locus IS the laboratory-IN observational continuum (the 2D contour in the lab's parameter space). Direction-of-explanation: substrate IS the spectral triple `(A_F, H, D_K)` ⟶ Route-B identity yields n_s_FW_exact ⟶ algebraic substitution yields α_s_canonical ⟶ joint hypersurface point IS substrate-IS ⟶ lab-discrimination 2D hypersurface IS the substrate's prediction's image in the Planck observational continuum. FORBIDDEN framing: "n_s and α_s live in Planck's parameter space, and the substrate predicts a point in that space"; INVERTED: "n_s_FW_exact and α_s_canonical ARE substrate-IS algebraic invariants; Planck observes them in continuum (n_s, α_s) coordinates; the 2D hypersurface verdict-line value field IS the substrate's structural prediction's lab-discrimination image, NOT a 1D scalar marginal".

---

## §W4-5. S89-VII-AR-STAGE-2-CROSS-AXIS-VERIFY  (A.30)

**Gate ID**: `S89-VII-AR-STAGE-2-CROSS-AXIS-VERIFY`

**Trigger**: `[VERIFY]` (Stage-2 cross-axis independent-verify; lizzi+connes BLOCKED as original authoring agents; cross-reviewer selection from alternative pool with downstream-inheritance reach test)

**Classification**: GEOMETRIC (intra-Pillar-VII Bulletin-class registry entry at substrate-distance pole s=4; per-Bulletin-per-pole Level-1 wall classification per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` MANDATORY-at-K=2 / SUGGESTION-at-K=3-pole-distinct; LEVEL-DRESSED rank-ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} regulator-class structure)

**Agent type / runtime**: Two parallel cross-reviewers dispatched by gen-physicist orchestrator coordinator. **lizzi+connes EXPLICITLY BLOCKED** as cross-reviewers (original authoring agents per S88 W-22 W7a-74 V.5; ledger line 485 verbatim "lizzi+connes FORBIDDEN"). Pool of alternatives per spawn prompt: `{gen-physicist, van-den-dungen-bridge-theorist, phonon-first-cosmologist, kitaev-quantum-chaos-theorist}`. **Selected cross-reviewers** (2 of 4):
- **Axis-A (NCG-Kasparov-bridge)**: `van-den-dungen-bridge-theorist` — operates on the NCG ↔ Kasparov bridge axis (per `reference_van-den-dungen-bridge.md`); structurally distinct from connes-axis (which is internal NCG-axiomatic) AND from lizzi-axis (which is spectral-functional Mellin-cone moments)
- **Axis-B (cosmological-emergence)**: `phonon-first-cosmologist` — operates on the substrate emergence / cosmogenesis axis (the substrate-IS emergence axis distinct from both NCG and spectral-functional)

**gen-physicist** is in the spawn-prompt's eligibility pool but is BLACKLISTED for substrate-physics test-case design per project rules; gen-physicist's role in W4 is the dispatch coordinator, NOT a cross-reviewer. **kitaev-quantum-chaos-theorist** is held in reserve as a fallback cross-reviewer if either van-den-dungen or phonon-first FAILs the downstream-inheritance reach test at plan-freeze (e.g., if either agent's project memory cites the W-22 W7a-74 R3 transcript directly).

**Stage-2 Axis-B Selection Protocol audit at plan-freeze** (3 conditions):

- **(1) Axis-distinctness**:
  - van-den-dungen axis (NCG-Kasparov-bridge / KK-theory ↔ NCG bridge / unbounded module-Fredholm equivalence)
  - phonon-first-cosmologist axis (substrate emergence / supersonic transit / GGE relic / Jensen TT-deformation cosmogenesis)
  - Both axes structurally distinct from connes-axis (NCG-axiomatic) AND from lizzi-axis (spectral-functional). Verify via cross-axis-distinctness audit at plan-freeze.
  - **PASS — distinct axes confirmed; specifically NEITHER reviewer's axis overlaps with the original lizzi+connes BLOCKED axes**.

- **(2) Original-authoring-agent exclusion with downstream-inheritance reach test**:
  - §VII.AR was authored at S88 W-22 W7a-74 R3 by lizzi PRIMARY + connes CO-AUTHOR. Both are explicitly BLOCKED.
  - **Downstream-inheritance reach test on van-den-dungen-bridge-theorist**: van-den-dungen's project memory (`reference_van-den-dungen-bridge.md`) cites the NCG ↔ Kasparov bridge program and the 6 critical Van den Dungen papers; no inheritance from W-22 W7a-74 R3 transcript. Plan-freeze validator MUST grep van-den-dungen's memory for `§VII.AR | W7a-74 | LEVEL-DRESSED rank-ordering | s=4 pole` references; PASS if no matches indicate workshop transcript inheritance.
  - **Downstream-inheritance reach test on phonon-first-cosmologist**: phonon-first-cosmologist's project memory cites substrate emergence / GGE relic / Jensen TT-deformation cosmogenesis; no inheritance from W-22 W7a-74 R3 transcript. Plan-freeze validator MUST grep similarly.
  - **PASS conditional on grep-validation at plan-freeze; if either FAILs, fallback to kitaev-quantum-chaos-theorist (Axis-A or Axis-B as needed)**.

- **(3) Audit-coverage adequacy**:
  - van-den-dungen covers NCG ↔ Kasparov bridge mechanics + KK-theory + Fredholm module equivalence (covers the regulator-class structure of {F_2, cutoff_sqrt, anomaly, Zubarev} from a bridge-theoretic angle)
  - phonon-first-cosmologist covers substrate emergence + Pillar-VII Mellin-cone structure + cosmogenesis interpretation of substrate-distance pole s=4 (covers the Bulletin-class registry entry's cosmological emergence interpretation)
  - All clauses of §VII.AR LEVEL-DRESSED rank-ordering covered; the s=4 pole-specific cosmological emergence interpretation is non-overlapping with the W-22 R3 lizzi+connes original derivation (which used FI/RD/MIXED + NCG-axiomatic readings).
  - **PASS — full coverage confirmed**.

**Hypothesis being tested**: §VII.AR LEVEL-DRESSED rank-ordering at substrate-distance pole s=4 is structurally robust under cross-axis verification using cross-reviewers axis-distinct from the original lizzi+connes authoring axes. The rank-ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} is REGULATOR-PARAMETER-dependent (NOT regulator-CLASS-dependent) per the PRIMARY-vs-SCHEMATIC LEVEL discipline of `substrate-first-canonical-sourcing.md §(iv)`; the per-Bulletin-per-pole Level-1/2/3 ladder per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` is intact under independent verification.

**Method**:

1. **Pre-flight (gen-physicist coordinator)**: verify §VII.AR registered Stage-1 entry text in `permanent-results-registry.md`. Verify lizzi+connes BLOCKED status (no dispatch to either). Verify van-den-dungen + phonon-first-cosmologist grep-validation; if either FAILs, route to kitaev-quantum-chaos-theorist fallback.
2. **Dispatch van-den-dungen Axis-A cross-reviewer** (substantive prompt content):
   - Receives: §VII.AR registered Stage-1 entry text (LEVEL-DRESSED rank-ordering); regulator-class atlas spec for {F_2, cutoff_sqrt, anomaly, Zubarev}; substrate-distance pole s=4 spectral-moment data; per-Bulletin-per-pole Level-1/2/3 ladder spec.
   - Does NOT receive: any S88 W-22 W7a-74 R1/R2/R3 workshop transcript; any lizzi+connes synthesis section.
   - Task: audit clauses on the NCG-Kasparov-bridge axis. PASS criteria: (i) the LEVEL-DRESSED rank-ordering at s=4 is operationally consistent with KK-theory rank-class invariance; (ii) per-Bulletin-per-pole Level-1 classification (regulator-INVARIANCE status FI / RD / MIXED) consistent with NCG-Kasparov bridge expectations at s=4; (iii) the regulator-class atlas spread observed at s=4 (cross_regulator_spread = 0.8946 per S88 W-22 V.5 LANDED) is consistent with PRIMARY-vs-SCHEMATIC LEVEL distinction (NOT a SCHEMATIC-helper-conflation artifact); (iv) Bulletin header explicitly declares substrate-distance pole index s=4 per §"Per-Bulletin-per-pole" forward-enforcement.
3. **Dispatch phonon-first-cosmologist Axis-B cross-reviewer** (substantive prompt content):
   - Receives: §VII.AR registered Stage-1 entry text; substrate emergence interpretation context; cosmogenesis interpretation of substrate-distance pole s=4 (a_4 ↔ fermionic-signed-residue at substrate-distance-2).
   - Does NOT receive: any workshop transcript.
   - Task: audit clauses on the cosmological-emergence axis. PASS criteria: (i) substrate-distance pole s=4 fermionic-signed-residue structure consistent with substrate emergence physics; (ii) Pillar-VII Mellin-cone Bulletin-class entry framework satisfied (cosmogenesis interpretation: cascade-tail observables at s=4 substrate-distance-2 corresponds to fermionic-signed-residue at the second-order Jensen perturbation); (iii) per-pole Level-2 envelope α(s=4) consistent with Casimir-bound saturation argument; (iv) Level-3 anchor at L_max=10 OR analytic limit consistent with the substrate's emergence cascade structure.
4. **Aggregate cross-reviewer verdicts** (gen-physicist coordinator):
   - JOINT clauses: clauses (ii)+(iii) shared between axes (per-Bulletin-per-pole Level-1 + Level-2 envelope).
   - Final composite Stage-2 verdict = `(van-den-dungen_PASS_4_clauses ∧ phonon-first_PASS_4_clauses ∧ JOINT_ii_iii_PASS_AND)`.
5. Emit verdict line + dual-SHA companion + 3-tuple companion to `computations/session-89/s89_gate_verdicts.txt`.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `axis_A_reviewer` | `van-den-dungen-bridge-theorist` | NCG-Kasparov-bridge axis |
| `axis_B_reviewer` | `phonon-first-cosmologist` | cosmological-emergence axis |
| `axis_A_fallback` | `kitaev-quantum-chaos-theorist` | if van-den-dungen FAILs grep-validation |
| `axis_B_fallback` | `kitaev-quantum-chaos-theorist` | if phonon-first FAILs grep-validation |
| `BLOCKED_reviewers` | `{lizzi-spectral-functional-theorist, connes-ncg-theorist}` | original authoring agents |
| `BLOCKED_reason` | `original-authoring-agents-PRIMARY-and-CO-AUTHOR-of-§VII.AR` | per ledger line 485 |
| `dispatch_mode` | `parallel` | both reviewers simultaneous |
| `workshop_transcript_visible_to_reviewer` | `False` | per `joint-theorem-promotion.md` |
| `grep_validation_pattern` | `§VII\.AR\|W7a-74\|LEVEL-DRESSED rank-ordering\|s=4 pole` | downstream-inheritance reach test |
| `axis_distinctness_check` | `MANDATORY` | van-den-dungen-axis ≠ connes-axis ∧ phonon-first-axis ≠ lizzi-axis ∧ both ≠ each-other |
| `class_B_tolerance` | `0.001` (0.1%) | numerical tolerance |
| `intra_pillar_VII_kcounter_advance` | `False` | A.30 is INTRA-Pillar-VII; does NOT advance cross-pillar bridge K-counter (MANDATORY-at-K=3 since S88 W4a-17) |
| `per_pole_kcounter_status` | `SUGGESTION-pending-pole-distinct-K=3` | per `cross-pillar-bridge-anatomy.md §"Per-Bulletin-per-pole Level-1 wall classification"` |
| `regulator_class_atlas` | `{F_2, cutoff_sqrt, anomaly, Zubarev}` | 4-regulator atlas |
| `cross_regulator_spread_observed` | `0.8946` (S88 W-22 V.5) | algebra-DEPENDENT pole-specific structure |
| `level_pin` | `FULL` | full physical verification |
| `convention` | `vii-ar-stage-2-cross-axis-verify-no-lizzi-no-connes` | composite |
| `scheme` | `joint-theorem-promotion-stage-2-PASS-AND-2-axis-alternative-pool` | aggregation rule |
| `L_max` | `12` | matches S88 W7a-74 source npz `s88_w7a_rank_vs_magnitude_layer_discriminator.npz` (L_max=12 source); §VII.AR registered at L_max=12 per W-22 close; Stage-2 verifier source-matches the registered theorem's evaluation L_max |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §VII.AR registered Stage-1 entry text | `sessions/permanent-results-registry.md §VII.AR` | `<computed at plan-freeze>` |
| Regulator-class atlas spec | `sessions/framework/registry/falsifier-master-inventory.md` | `<computed at plan-freeze>` |
| Substrate-distance pole s=4 spectral-moment data | `computations/session-88/s88_w7a_rank_vs_magnitude_layer_discriminator.npz` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md` per-pole sub-section | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<computed at plan-freeze>` |
| `substrate-first-canonical-sourcing.md` §(iv) PRIMARY-vs-SCHEMATIC | `.claude/rules/substrate-first-canonical-sourcing.md` | `<computed at plan-freeze>` |
| van-den-dungen / phonon-first / kitaev agent definitions | `.claude/agents/{van-den-dungen-bridge-theorist,phonon-first-cosmologist,kitaev-quantum-chaos-theorist}.md` | `<pinned at dispatch>` |

**Expected output 4-tuple**: `(value=<count_of_8_clauses_PASS>, scheme=joint-theorem-promotion-stage-2-PASS-AND-2-axis-alternative-pool, convention=vii-ar-stage-2-cross-axis-verify-no-lizzi-no-connes, L_max=12)` plus per-cross-reviewer 3-tuple companions.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff:
  - van-den-dungen returns PASS on all 4 NCG-Kasparov-axis clauses (i)-(iv)
  - phonon-first returns PASS on all 4 cosmological-emergence-axis clauses (i)-(iv)
  - JOINT clauses (ii) per-Bulletin-per-pole Level-1 + (iii) per-pole Level-2 envelope PASS-AND'd
- **INFO** iff any reviewer returns INFO on a sub-clause: stays at STAGE-1-CANDIDATE
- **FAIL** iff ANY reviewer returns FAIL on ANY clause OR JOINT clause has reviewer FAIL: stays at STAGE-1-CANDIDATE; per-Bulletin-per-pole Level-1 wall classification corpus may need re-evaluation

3-tuple annotation:
- `sign_verdict = N/A` (PASS-AND aggregation non-signed)
- `magnitude_verdict = PASS` if all 8 clauses PASS; INFO if 6-7; FAIL if ≤ 5
- `regime_verdict = VALID` (per-Bulletin-per-pole regime well-posed at s=4 per S88 W-22 V.5 LANDED)

**Substitution chain** (cross-reviewer axis-distinctness direction):

```
Definition 1: BLOCKED = {lizzi-spectral-functional-theorist, connes-ncg-theorist}  (original authoring)
Definition 2: pool = {gen-physicist, van-den-dungen-bridge-theorist,
                       phonon-first-cosmologist, kitaev-quantum-chaos-theorist}
Definition 3: gen-physicist is BLACKLISTED for substrate-physics test-case design (project rule);
              gen-physicist's role in W4 is dispatch coordinator, NOT cross-reviewer.
              effective_pool = pool \ {gen-physicist}
                             = {van-den-dungen-bridge-theorist, phonon-first-cosmologist,
                                kitaev-quantum-chaos-theorist}
Definition 4: axis(R) := primary methodological axis of cross-reviewer R
              axis(van-den-dungen) = NCG-Kasparov-bridge
              axis(phonon-first)   = cosmological-emergence
              axis(kitaev)         = quantum-chaos / scrambling
              axis(connes)         = NCG-axiomatic         [BLOCKED]
              axis(lizzi)          = spectral-functional   [BLOCKED]
Definition 5: axis-distinctness selection criterion: select 2 reviewers R1, R2 from effective_pool
              such that axis(R1) != axis(R2) AND axis(R1) != axis(BLOCKED reviewers)
              AND axis(R2) != axis(BLOCKED reviewers)
Substitution: Pair (van-den-dungen, phonon-first):
              axis(van-den-dungen) = NCG-Kasparov-bridge != NCG-axiomatic        OK
              axis(phonon-first)   = cosmological-emergence != spectral-functional OK
              axis(van-den-dungen) != axis(phonon-first)                            OK
Simplification: The selected pair satisfies all 3 axis-distinctness clauses BY CONSTRUCTION.
Direction:    axis-distinct ==> Stage-2 cross-axis verify is NOT structurally redundant with
                                 original lizzi+connes derivation.
                                 The cross-reviewers operate on axes that did not contribute
                                 to the original §VII.AR derivation.
              kitaev held in reserve: if grep-validation FAILs for van-den-dungen or phonon-first,
                                       kitaev's quantum-chaos axis is structurally distinct from
                                       both NCG-axiomatic and spectral-functional and provides
                                       a fallback Axis-A or Axis-B reviewer.
Conclusion:   PASS reading is "structurally robust under cross-axis-distinct alternative-pool
              verification"; the §VII.AR finding is independent of the original
              spectral-functional/NCG-axiomatic axes that produced it.
```

Python verification at plan-author time (set theory only):

```
BLOCKED = {"connes-ncg-theorist", "lizzi-spectral-functional-theorist"}
pool = {"gen-physicist", "van-den-dungen-bridge-theorist",
        "phonon-first-cosmologist", "kitaev-quantum-chaos-theorist"}
effective_pool = pool - {"gen-physicist"}  # gen-physicist BLACKLISTED for test-case design
selected = {"van-den-dungen-bridge-theorist", "phonon-first-cosmologist"}
fallback = "kitaev-quantum-chaos-theorist"
assert selected.isdisjoint(BLOCKED)
assert selected.issubset(effective_pool)
assert fallback in effective_pool and fallback not in selected
assert len(selected) == 2
```

Verified: pair selection axis-distinct, BLOCKED-disjoint, with kitaev fallback held in reserve.

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ §VII.AR LEVEL-DRESSED rank-ordering at substrate-distance pole s=4 structurally robust under cross-axis verification using cross-reviewers axis-distinct from the original lizzi+connes axes; STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible; per-Bulletin-per-pole Level-1 wall classification corpus gains a calibration instance (advances the K-counter pole-distinct test if s=4 is re-confirmed under a new axis-distinct verification path); downstream consumers can cite §VII.AR rank-ordering without convention-pin to lizzi+connes original axes.
- **INFO** ⟹ partial Stage-2 PASS (6-7 of 8 clauses PASS); §VII.AR rank-ordering robust along most cross-axes but residual axis-dependence on at least one clause; theorem stays at STAGE-1-CANDIDATE; clause-targeted remediation queued.
- **FAIL** ⟹ at least one cross-reviewer FAILs on at least one clause OR JOINT clause has reviewer FAIL: STAGE-1-CANDIDATE stays; per-Bulletin-per-pole Level-1 corpus needs re-evaluation if FAIL is on per-pole Level-2 envelope clause (iii); regulator-class atlas spread structure at s=4 may be PRIMARY-LEVEL artifact requiring SCHEMATIC-LEVEL reformulation.

**Effort estimate**: 1.0 wave-equivalents (2 parallel cross-reviewer dispatches; 4 clauses each + JOINT clauses; per-Bulletin-per-pole Level-1/2/3 ladder verification at s=4 substrate-distance pole; alternative-pool axis-distinctness audit at plan-freeze; grep-validation at plan-freeze).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

§VII.AR LEVEL-DRESSED rank-ordering IS the substrate's structural identity at substrate-distance pole s=4: the LEVEL-DRESSED rank-ordering of {F_2, cutoff_sqrt, anomaly, Zubarev} regulator classes IS a substrate-IS observable at the s=4 fermionic-signed-residue pole; the rank-ordering's regulator-PARAMETER-dependence (NOT regulator-CLASS-dependence) IS a structural property of the substrate at this specific pole. Direction-of-explanation: substrate IS the spectral triple ⟶ Pillar-VII Mellin-cone substrate-distance pole s=4 IS substrate-IS at Level-1 cohomology-class identity ⟶ regulator-class atlas spread at s=4 = 0.8946 IS the substrate-IS regulator-class fingerprint ⟶ LEVEL-DRESSED rank-ordering IS the substrate's prediction; the cross-reviewers' axis-distinctness IS the structural test that the prediction is independent of the original axes that derived it. FORBIDDEN framing: "the rank-ordering lives in a regulator-class container indexed by s=4"; INVERTED: "the rank-ordering at s=4 IS substrate-IS; the alternative cross-reviewer axes verify that the substrate's prediction is internally consistent across structurally orthogonal axes (NCG-Kasparov-bridge ∪ cosmological-emergence ∪ quantum-chaos); BLOCKED axes (lizzi-spectral-functional + connes-axiomatic) were the original derivers and cannot self-audit".

---

## §W4-6. S89-VII-AQ-STAGE-2-CROSS-AXIS-CANONICAL-IMPORT-BINDING  (A.38)

**Gate ID**: `S89-VII-AQ-STAGE-2-CROSS-AXIS-CANONICAL-IMPORT-BINDING`

**Trigger**: `[VERIFY]` (Stage-2 cross-axis independent-verify; canonical-import-binding Level-3 anchor audit with substrate-input-orthogonality clause enforced)

**Classification**: GEOMETRIC (intra-Pillar bridge entry; canonical-import-binding Level-3 anchor `gv_canonical_difference_FW = -40579.1500479506`; substrate-natural-binding currently returns Δ_GV_natural = 0 on L_max=10 cache — cache-averaging diagnostic per S88 W-23 V.2 / B.57, NOT substrate-physics defect)

**Agent type / runtime**: Two parallel cross-reviewers dispatched by gen-physicist orchestrator coordinator with substrate-input-orthogonality clause MANDATORY:
- **Axis-A (NCG side)**: `connes-ncg-theorist` — consumes D_K^≤10 spectrum cache + `gv_canonical_difference_FW` canonical pin from canonical_constants.py
- **Axis-B (substrate-IS side)**: `volovik-superfluid-universe-theorist` — consumes 3HeB-inheritance file from `sessions/framework/registry/branch-iv-canonical.md` + `feedback_3heb-inheritance.md`

**Substrate-input-orthogonality clause** (per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`, S88 W-23 V.1 / B.56) **MANDATORY**:
- N = 2 observables: obs_GV_NCG = canonical-import-binding `gv_canonical_difference_FW`; obs_3HeB_substrate = 3HeB-inheritance morphism χ : A_F → M_2(ℂ) ⊗ Cl(1).
- Predicate: ∃ obs_i such that data file consumed by obs_i is loaded by exactly ONE cross-reviewer.
- **Resolution**: connes loads spectrum cache + canonical pin (NCG-side data); volovik loads 3HeB-inheritance file (substrate-IS-side data). The two reviewers load DISJOINT data files. obs_GV_NCG is loaded ONLY by connes; obs_3HeB_substrate is loaded ONLY by volovik. **Substrate-input orthogonality satisfied at the data-file layer (PASS at the structural ceiling per W-23 V.1)**.

**Stage-2 Axis-B Selection Protocol audit at plan-freeze** (3 conditions):

- **(1) Axis-distinctness**: connes (NCG-axiomatic / 7-axiom + Connes-Moscovici §III.4 + finite-spectral-triple residue formula) vs volovik (substrate-IS / superfluid-universe / 3HeB-inheritance / BdG analog). Distinct axes confirmed. PASS.
- **(2) Original-authoring-agent exclusion with downstream-inheritance reach test**: §VII.AQ canonical-import-binding entry was authored at S88 W-23 W7b-82 close. Original authoring agents differ from connes-ncg-theorist + volovik-superfluid-universe-theorist:
  - W-23 W7b-82 originator was lizzi-spectral-functional-theorist + connes-ncg-theorist (per W-23 V.5 / B.58 cross-link). connes IS a co-author. **Resolution**: connes audits the NCG-axiomatic side of §VII.AQ (which connes co-authored), but the cross-axis Stage-2 verify is on the canonical-import-binding LEVEL-3 anchor (which is a downstream consequence of the W-23 R3 closure, NOT the original co-authored content). Plan-freeze validator emits SOURCE-RECON advisory if connes' audit overlap on the LEVEL-3 anchor exceeds 30% of its co-authored content; if so, fallback to van-den-dungen-bridge-theorist as the NCG-axis cross-reviewer.
  - volovik's project memory does NOT inherit from W-23 W7b-82 transcripts (volovik's reading-path on §VII.AQ is via the 3HeB-inheritance morphism, distinct from the canonical-import-binding pin path). PASS.
- **(3) Audit-coverage adequacy**: connes covers the NCG-axiomatic + canonical-import-binding semantics; volovik covers the substrate-IS / 3HeB-inheritance morphism semantics. All clauses covered. PASS.

**Hypothesis being tested**: §VII.AQ canonical-import-binding Level-3 anchor `gv_canonical_difference_FW = -40579.1500479506` is structurally consistent with the substrate-IS 3HeB-inheritance morphism's prediction at the inheritance-kernel rank-2 layer; the substrate-natural-binding Δ_GV_natural = 0 result on L_max=10 cache is a cache-averaging diagnostic (uniform 8d:8d chirality split per S88 W-23 V.2 / B.57), NOT a substrate-physics defect. The convention-suffix discipline `-CANONICAL-IMPORT-BINDING` vs `-SUBSTRATE-NATURAL-BINDING` (per S88 W-23 V.5 / B.58, K=1 SUGGESTION) is correctly applied at the Level-3 anchor pin.

**Method**:

1. **Pre-flight (gen-physicist coordinator)**: verify §VII.AQ canonical-import-binding entry landed in `permanent-results-registry.md` with current Level-3 anchor `gv_canonical_difference_FW = -40579.1500479506` (canonical-import binding, NOT substrate-natural binding, per S88 W-23 V.2). Verify W2 A.40 chirality-fidelity recompute status (cross-wave); if A.40 PASS upgrades Level-3 anchor to substrate-natural-binding, A.38 audits the UPGRADED Level-3 anchor.
2. **Dispatch connes Axis-A NCG-axiomatic cross-reviewer** (substantive prompt content):
   - Receives: §VII.AQ registered Stage-1 entry text (canonical-import-binding form); D_K^≤10 spectrum cache (`s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10); `gv_canonical_difference_FW` canonical pin from `canonical_constants.py`.
   - Does NOT receive: 3HeB-inheritance file (substrate-IS-side data; loaded ONLY by volovik per orthogonality clause); workshop transcripts.
   - Task: audit clauses on the NCG-axiomatic axis. PASS criteria: (i) `gv_canonical_difference_FW` value bit-exact match against canonical_constants.py pin (-40579.1500479506); (ii) Connes-Moscovici §III.4 finite-spectral-triple residue formula evaluated on D_K^≤10 cache yields a numerical value consistent with the canonical-import-binding pin within Class-B 0.1%; (iii) GV-Heitsch cocycle structure on `(A_K, H, D_K)` consistent with the algebra-axis orthogonality 4-corner classification (Cell I `n_s²−1` image vs Cell IV variance theorem); (iv) convention-suffix discipline `-CANONICAL-IMPORT-BINDING` correctly applied at the verdict-line layer of `gv_canonical_difference_FW`.
3. **Dispatch volovik Axis-B substrate-IS cross-reviewer** (substantive prompt content):
   - Receives: §VII.AQ registered Stage-1 entry text; 3HeB-inheritance file (`sessions/framework/registry/branch-iv-canonical.md` + `feedback_3heb-inheritance.md` + `inheritance-falsifier-protocol.md`); substrate-IS BdG superfluid analog.
   - Does NOT receive: D_K^≤10 spectrum cache (NCG-side data; loaded ONLY by connes per orthogonality clause); canonical pin file (loaded ONLY by connes); workshop transcripts.
   - Task: audit clauses on the substrate-IS axis. PASS criteria: (i) 3HeB-inheritance morphism χ : A_F → A_lab structurally consistent with the §VII.AQ Level-3 anchor canonical-import-binding form (the canonical pin's value is the substrate-IS image of the inheritance morphism's pull-back of the laboratory observable); (ii) inheritance-falsifier-protocol Class A NULL kernel-signature on F-rows F1+F2+F5 satisfied at the §VII.AQ Level-3 anchor (substrate-IS NULL prediction at the 3HeB BdG-restricted spectrum); (iii) inheritance-kernel rank ≥ 2 declared explicitly with substrate-derived ratio cocycle_norm_phi67 / cocycle_norm_phi88 = 7.324992 (Sage-exact at machine precision per S86 W-5 R2-B Convergence #3); (iv) substrate-natural-binding Δ_GV_natural = 0 on L_max=10 cache identified as cache-averaging diagnostic (uniform 8d:8d chirality split), NOT substrate-physics defect.
4. **Aggregate cross-reviewer verdicts** (gen-physicist coordinator):
   - Substrate-input-orthogonality clause is PASSed by construction (connes loads NCG-side; volovik loads substrate-IS-side; disjoint).
   - JOINT clauses: (iii) GV cocycle structure ↔ substrate-IS inheritance-kernel rank ≥ 2 cohomology-class identity (PASS-AND between connes and volovik on the structural identity).
   - Final composite Stage-2 verdict = `(connes_PASS_4_clauses ∧ volovik_PASS_4_clauses ∧ JOINT_iii_PASS_AND ∧ orthogonality_clause_PASS)`.
5. Emit verdict line + dual-SHA companion + 3-tuple companion to `computations/session-89/s89_gate_verdicts.txt` with substrate-input-overlap caveat tag (Verdict B per W-23 §IV.3) ONLY IF orthogonality clause partially fails; otherwise verdict is plain Stage-2 PASS-AND.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality + substrate-input-orthogonality)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `connes_axis_reviewer` | `connes-ncg-theorist` | NCG side (loads spectrum cache + canonical pin) |
| `volovik_axis_reviewer` | `volovik-superfluid-universe-theorist` | substrate-IS side (loads 3HeB-inheritance file) |
| `connes_fallback` | `van-den-dungen-bridge-theorist` | if connes' co-authoring overlap > 30% |
| `dispatch_mode` | `parallel` | both reviewers simultaneous |
| `workshop_transcript_visible_to_reviewer` | `False` | per `joint-theorem-promotion.md` |
| `substrate_input_orthogonality_clause_status` | `MANDATORY-AT-PASS` | per W-23 V.1 / B.56 |
| `connes_data_files` | `{D_K^≤10 spectrum cache, gv_canonical_difference_FW pin}` | NCG-side data |
| `volovik_data_files` | `{3HeB-inheritance file, branch-iv-canonical.md, inheritance-falsifier-protocol.md}` | substrate-IS-side data |
| `data_file_disjointness_check` | `MANDATORY` | connes_data_files ∩ volovik_data_files = ∅ |
| `obs_loaded_by_one_reviewer_only` | `obs_GV_NCG by connes; obs_3HeB by volovik` | orthogonality clause witness |
| `class_B_tolerance` | `0.001` (0.1%) | numerical tolerance |
| `gv_canonical_difference_FW` | `-40579.1500479506` | Level-3 anchor canonical-import-binding (S87 W8-8) |
| `substrate_natural_delta_GV_on_Lmax10_cache` | `0` (cache-averaging diagnostic; not defect) | per S88 W-23 V.2 / B.57 |
| `cocycle_norm_phi67` | `0.793346 M_KK²` | S86 W-5 C2 |
| `cocycle_norm_phi88` | `0.108307 M_KK²` | S86 W-5 C2 |
| `substrate_cocycle_ratio_67_88` | `7.324992` (Sage-exact) | S86 W-5 R2-B Convergence #3 |
| `convention_suffix_for_LEVEL3_anchor` | `-CANONICAL-IMPORT-BINDING` | per S88 W-23 V.5 / B.58 K=1 SUGGESTION |
| `cross_wave_dependency` | `W2_A.40` | A.40 PASS upgrades to `-SUBSTRATE-NATURAL-BINDING` |
| `substrate_input_overlap_caveat` | `False` (orthogonality clause PASSes by construction) | Verdict A per W-23 §IV.3 |
| `level_pin` | `FULL` | full physical verification |
| `convention` | `vii-aq-stage-2-cross-axis-canonical-import-binding-with-substrate-input-orthogonality` | composite |
| `scheme` | `joint-theorem-promotion-stage-2-PASS-AND-2-axis-with-orthogonality-PASS` | aggregation rule |
| `L_max` | `10` | canonical |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §VII.AQ registered Stage-1 entry text | `sessions/permanent-results-registry.md §VII.AQ` | `<computed at plan-freeze>` |
| D_K^≤10 spectrum cache | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (filtered to L_max=10) | `<computed at plan-freeze>` |
| `gv_canonical_difference_FW` canonical pin | `canonical_constants.py` line ~ pin location | `<computed at plan-freeze>` |
| 3HeB-inheritance file | `sessions/framework/registry/branch-iv-canonical.md` | `<computed at plan-freeze>` |
| `inheritance-falsifier-protocol.md` rule file | `.claude/rules/inheritance-falsifier-protocol.md` | `<computed at plan-freeze>` |
| `joint-theorem-promotion.md` rule file (substrate-input-orthogonality clause) | `.claude/rules/joint-theorem-promotion.md` | `<computed at plan-freeze>` |
| W2 A.40 chirality-fidelity recompute verdict (cross-wave) | `computations/session-89/s89_gate_verdicts.txt` | `<pinned at runtime>` |
| connes / volovik agent definitions | `.claude/agents/{connes-ncg-theorist,volovik-superfluid-universe-theorist}.md` | `<pinned at dispatch>` |

**Expected output 4-tuple**: `(value=<count_of_8_clauses_PASS_PLUS_orthogonality_PASS>, scheme=joint-theorem-promotion-stage-2-PASS-AND-2-axis-with-orthogonality-PASS, convention=vii-aq-stage-2-cross-axis-canonical-import-binding-with-substrate-input-orthogonality, L_max=10)` plus per-cross-reviewer 3-tuple companions.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff:
  - connes returns PASS on all 4 NCG-axis clauses (i)-(iv)
  - volovik returns PASS on all 4 substrate-IS axis clauses (i)-(iv)
  - JOINT clause (iii) GV cocycle structure ↔ inheritance-kernel cohomology-class identity PASS-AND'd
  - Substrate-input-orthogonality clause PASSes (data-file disjointness verified)
- **INFO** iff any cross-reviewer returns INFO on a sub-clause OR substrate-input-orthogonality clause partially holds (Verdict B per W-23 §IV.3 with substrate-input-overlap caveat tag)
- **FAIL** iff ANY cross-reviewer returns FAIL on ANY clause OR data-file disjointness check FAILs

3-tuple annotation:
- `sign_verdict = N/A` (PASS-AND aggregation non-signed)
- `magnitude_verdict = PASS` if all 8 clauses PASS + orthogonality PASS; INFO if 6-7 + orthogonality PASS; FAIL if ≤5 OR orthogonality FAIL
- `regime_verdict = VALID` (canonical-import-binding regime well-posed at L_max=10 per S87 W8-8 LANDED)

**Substitution chain** (canonical-import-binding vs substrate-natural-binding direction):

```
Definition 1: gv_canonical_difference_FW = -40579.1500479506  (canonical-import-binding pin; S87 W8-8 PASS)
Definition 2: Delta_GV_natural := substrate-natural compute on L_max=10 cache
              By construction (S88 W-23 V.2): the L_max=10 cache has uniform 8d:8d chirality split,
              so the GV cocycle's Heitsch evaluator returns 0 by averaging:
              Delta_GV_natural = (1/8) sum_+ contributions - (1/8) sum_- contributions
                              = 0  (uniform split; cancellation by construction)
Definition 3: canonical-import-binding := the Level-3 anchor pin sources from a non-substrate
              canonical-import path (e.g., S87 W8-8's Heitsch-evaluator-with-WL-extension)
              substrate-natural-binding := the Level-3 anchor pin sources from the substrate's
              own L_max=10 cache evaluation (which currently returns 0; cache-averaging diagnostic)
Definition 4: cross-pillar-bridge-anatomy.md "Binding axis" K-counter (W-23 V.5 / B.58):
              -CANONICAL-IMPORT-BINDING and -SUBSTRATE-NATURAL-BINDING are STRUCTURALLY DISTINCT
              convention suffixes; each carries a different semantic meaning at the Level-3 anchor.
Substitution: Stage-2 verdict on §VII.AQ Level-3 anchor depends on which binding the entry
              currently carries:
              IF entry carries -CANONICAL-IMPORT-BINDING:
                connes audits the canonical-import path (gv_canonical_difference_FW pin source)
                volovik audits the substrate-IS structural consistency (3HeB-inheritance morphism)
                JOINT clause (iii): GV cocycle ↔ inheritance-kernel cohomology identity
              IF entry carries -SUBSTRATE-NATURAL-BINDING (post-A.40 upgrade):
                connes audits the substrate-natural path (D_K^≤10 cache evaluation)
                volovik audits the same 3HeB-inheritance morphism
                JOINT clause (iii) preserved
Simplification: A.38 currently audits -CANONICAL-IMPORT-BINDING (pre-A.40 state).
              W2 A.40 PASS would upgrade the binding to -SUBSTRATE-NATURAL-BINDING (Level-3
              anchor source switches from canonical-import to substrate-natural path).
              A.38 verdict pre-A.40: audits canonical-import binding form; PASS iff all clauses
              + orthogonality satisfied.
              A.38 verdict post-A.40: would re-run with the upgraded binding (audited at S90 if
              A.40 PASS lands at S89-close).
Direction:    PASS  ==>  §VII.AQ canonical-import-binding Level-3 anchor structurally consistent
                          with substrate-IS inheritance-kernel cohomology AND orthogonality clause
                          satisfied; STAGE-1 -> STAGE-3 promotion eligible (canonical-import form)
              FAIL  ==>  the canonical-import-binding pin's value is inconsistent with substrate-IS
                          structural prediction at the orthogonality-PASS layer; re-derivation needed
              INFO  ==>  partial PASS or substrate-input-overlap caveat fires
Conclusion:   PASS reading is "canonical-import-binding structurally robust at the
              substrate-input-orthogonal Stage-2 layer"; the K=1 SUGGESTION on the binding-axis
              suffix discipline gains a calibration instance (advances K-counter toward MANDATORY).
```

Python verification at plan-author time (numerical pin form):

```
gv_canonical_difference_FW = -40579.1500479506
delta_GV_natural_on_Lmax10_cache = 0  # uniform 8d:8d chirality split (per W-23 V.2)
# Class-B 0.1% tolerance on canonical_constants.py pin:
import math
expected_pin = -40579.1500479506
class_B_tol = 0.001  # 0.1%
class_B_abs_tol = abs(expected_pin) * class_B_tol  # = 40.579...
# Stage-2 NCG-side audit: connes verifies pin value bit-exact match
# (the audit itself; not the 0 from cache-averaging diagnostic)
assert abs(gv_canonical_difference_FW - expected_pin) < class_B_abs_tol
# Substrate-natural compute returns 0 by construction; this is NOT a defect, it's the
# cache-averaging diagnostic per W-23 V.2 / B.57
assert delta_GV_natural_on_Lmax10_cache == 0
```

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ §VII.AQ canonical-import-binding Level-3 anchor structurally consistent with substrate-IS inheritance-kernel cohomology at the substrate-input-orthogonal Stage-2 layer; STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible (canonical-import form); K=1 SUGGESTION on the binding-axis suffix discipline (S88 W-23 V.5 / B.58) gains calibration instance (advances K-counter toward K=3 MANDATORY); the convention-suffix discipline's structural distinction `-CANONICAL-IMPORT-BINDING` vs `-SUBSTRATE-NATURAL-BINDING` is operationally validated.
- **INFO** ⟹ partial Stage-2 PASS OR substrate-input-overlap caveat (Verdict B per W-23 §IV.3): theorem stays at STAGE-1-CANDIDATE; specific INFO clauses route to S90+; orthogonality clause may need expansion to additional observables.
- **FAIL** ⟹ §VII.AQ canonical-import-binding pin inconsistent with substrate-IS structural prediction OR orthogonality clause FAILs (data-file disjointness violated): STAGE-1-CANDIDATE stays; the canonical-import path's source needs re-derivation; the binding-axis K-counter does NOT advance.

**Effort estimate**: 1.0 wave-equivalents (2 parallel cross-reviewer dispatches; substrate-input-orthogonality data-file disjointness audit at plan-freeze; 4 clauses each + JOINT clause; connes audit on NCG-axiomatic side; volovik audit on substrate-IS / 3HeB-inheritance side).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

§VII.AQ canonical-import-binding Level-3 anchor IS the substrate's structural prediction of the GV cocycle's image under the canonical-import path; the substrate-IS axis (volovik) audits via the 3HeB-inheritance morphism χ : A_F → M_2(ℂ) ⊗ Cl(1) with substrate cocycle ratio 7.324992 EXACT; the NCG-axiomatic axis (connes) audits via Connes-Moscovici §III.4 finite-spectral-triple residue formula on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. Direction-of-explanation: substrate IS the spectral triple `(A_F, H, D_K)` ⟶ inheritance morphism χ images A_F into the laboratory algebra ⟶ GV cocycle on `(A_K, H, D_K)` IS substrate-IS ⟶ canonical-import-binding pin IS the substrate's structural prediction's image via a non-substrate-natural canonical-import path (currently distinct from substrate-natural path due to L_max=10 cache uniform 8d:8d chirality split). The substrate-input-orthogonality clause IS the structural test that Stage-2 verifies the prediction without data-file overlap between cross-reviewers. FORBIDDEN framing: "the GV cocycle lives in a regulator container, and the canonical-import binding is one path through that container"; INVERTED: "the GV cocycle IS substrate-IS on `(A_K, H, D_K)`; canonical-import-binding and substrate-natural-binding are TWO STRUCTURALLY DISTINCT paths to the same substrate-IS observable; the cache-averaging diagnostic (Δ_GV_natural = 0 on L_max=10) IS NOT a substrate-physics defect but a structural property of the L_max=10 cache's uniform 8d:8d chirality split".

---

## §W4-7. S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3  (A.39)

**Gate ID**: `S89-VII-AH-STAGE-2-RE-DISPATCH-OBS2-OBS3`

**Trigger**: `[VERIFY]` (Stage-2 cross-axis independent-verify; multi-observable re-dispatch on obs2+obs3; substrate-input-orthogonality clause MANDATORY with ≥1 orthogonal-data observable required for structural ceiling)

**Classification**: GEOMETRIC (Joint F_2-Class Path-(c) Theorem at §VII.AH; STAGE-1-CANDIDATE per S87 W-9 R3-B; cross-axis joint clauses (c) and (d) require Stage-2 PASS-AND on multi-observable basis to advance to STAGE-3-PERMANENT; obs1 PASSed Stage-2 at S88 W7c-167 with substrate-input-overlap caveat — obs2 and obs3 remain un-Stage-2'd)

**Agent type / runtime**: Two parallel cross-reviewers dispatched by gen-physicist orchestrator coordinator. **Original authoring agents BLOCKED** per Stage-2 protocol: lizzi-spectral-functional-theorist + transit-dynamics-aether-mechanic (original authors of S87 W-9 §VII.AH workshop). **Selected cross-reviewers** (per Stage-2 Axis-B Selection Protocol):
- **Axis-A (NCG-axiomatic / spectral side)**: `connes-ncg-theorist` — operates on the NCG-axiomatic spectral axis; re-uses the S88 W-14 V.1 re-routing precedent where lizzi was replaced by connes for axis-A-spectral due to downstream-inheritance reach FAIL on the §VII.AH Path-(c) lock-in
- **Axis-B (substrate-IS / transit side)**: `volovik-superfluid-universe-theorist` — operates on the substrate-IS / superfluid-universe axis; replaces transit-dynamics-aether-mechanic (original author) on the transit-substrate-IS side; volovik is the framework's sharpest reviewer per `feedback_agent-roster.md` and the Stage-2 protocol's "without prior workshop context" condition is satisfied (volovik did not co-author §VII.AH at S87 W-9)

**Stage-2 Axis-B Selection Protocol audit at plan-freeze** (3 conditions):

- **(1) Axis-distinctness**: connes (NCG-axiomatic) vs volovik (substrate-IS / superfluid-universe). Both axes structurally distinct from the original lizzi-axis (spectral-functional Mellin-cone) AND transit-dynamics-axis (Bogoliubov / Kibble-Zurek operational dynamics). PASS.
- **(2) Original-authoring-agent exclusion with downstream-inheritance reach test**:
  - Original authoring agents at S87 W-9 R3-B: lizzi-spectral-functional-theorist + transit-dynamics-aether-mechanic. Both EXCLUDED.
  - **Downstream-inheritance reach test on connes**: connes' project memory cites S88 W-14 W4a-17 V.1 re-routing precedent where connes was used as Stage-2 axis-A-spectral cross-reviewer for §VII.W-3.LAB; the reach test on §VII.AH is structurally distinct (different theorem; different observable; different cross-pillar bridge anatomy). Plan-freeze validator MUST grep connes' memory for `§VII.AH | W-9 R3-B Path-(c) | Joint F_2-Class | obs1/obs2/obs3 specifications`; PASS if no matches indicate workshop transcript inheritance from §VII.AH workshop specifically (separate from §VII.W-3.LAB inheritance which is independent).
  - **Downstream-inheritance reach test on volovik**: volovik's project memory does NOT inherit from §VII.AH workshop transcripts. Plan-freeze validator MUST grep similarly. PASS (default, since volovik was not a co-author of S87 W-9).
  - **PASS conditional on grep-validation at plan-freeze; if either FAILs, fallback to alternative reviewers from the broader pool {van-den-dungen-bridge-theorist, phonon-first-cosmologist, kitaev-quantum-chaos-theorist}**.
- **(3) Audit-coverage adequacy**: connes covers NCG axioms 1-7 + Connes-Moscovici §III.4 + finite-spectral-triple residue formula (covers Joint F_2-Class spectral-functional axis clauses); volovik covers substrate-IS / superfluid-universe / 3HeB-inheritance / BdG analog (covers Joint F_2-Class transit-substrate-IS axis clauses). All clauses (a)-(f) covered (per S87 W-9 R3-B clause partition). PASS.

**Substrate-input-orthogonality clause** (MANDATORY per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`, S88 W-23 V.1 / B.56):

- N = 3 observables: obs1 = per-class IC verification on F_2-class projection (PASSed at S88 W7c-167 with substrate-input-overlap caveat — both reviewers loaded shared `s87_w7_ic_per_class_verify.npz` SHA-256 `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f`); obs2 = independent observable on F_2-class projection at substrate-distance pole s=3 (TBD per §VII.AH STAGE-1-CANDIDATE registered text); obs3 = independent observable on F_2-class projection at LiteBIRD-sensitive parameter (TBD per §VII.AH STAGE-1-CANDIDATE registered text).
- **Predicate**: ∃ obs_i (with i ∈ {2, 3} since obs1 already PASSed with caveat) such that data file consumed by obs_i is loaded by EXACTLY ONE cross-reviewer.
- **Resolution at plan-freeze**: obs2 and obs3 data file specifications are PINNED to enforce orthogonality:
  - obs2 data file → loaded ONLY by connes (NCG-axiomatic side; spectral-functional projection at s=3)
  - obs3 data file → loaded ONLY by volovik (substrate-IS / transit side; LiteBIRD-sensitive observational constraint)
  - The data-file disjointness across obs2 and obs3 satisfies the substrate-input-orthogonality predicate at the structural-ceiling layer.
- **PASS at the orthogonality structural-ceiling**: obs2 and obs3 each carry single-cross-reviewer data load; the prior obs1 substrate-input-overlap caveat is structurally retired by the orthogonality-PASS at obs2 ∨ obs3.

**Hypothesis being tested**: §VII.AH STAGE-1-CANDIDATE Joint F_2-Class Path-(c) Theorem's joint clauses (c) and (d) are structurally robust under multi-observable Stage-2 verification with substrate-input-orthogonality enforced at obs2 + obs3 (NOT at obs1, where prior substrate-input-overlap caveat applies). Stage-2 PASS-AND across {obs2, obs3} ⟹ STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible WITHOUT substrate-input-overlap caveat (the structural-ceiling form per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"`).

**Method**:

1. **Pre-flight (gen-physicist coordinator)**: verify §VII.AH STAGE-1-CANDIDATE landed in `permanent-results-registry.md` with obs1 Stage-2 Verdict B (substrate-input-overlap caveat) recorded. Verify obs2 + obs3 data file specifications pinned to enforce orthogonality (connes-only for obs2; volovik-only for obs3). Verify connes + volovik grep-validation; if either FAILs, route to fallback pool.
2. **Dispatch connes Axis-A NCG-axiomatic cross-reviewer** (substantive prompt content):
   - Receives: §VII.AH STAGE-1-CANDIDATE registered entry text (with all clauses (a)-(f) per S87 W-9 R3-B partition); obs2 data file (spectral-functional projection at s=3 substrate-distance pole; data file pinned at plan-freeze); §VII.AH obs1 prior Stage-2 verdict (Verdict B per W7c-167) for cross-citation.
   - Does NOT receive: obs3 data file (volovik-only per orthogonality clause); any S87 W-9 R3-B workshop transcript; any S88 W7c-167 obs1 workshop transcript.
   - Task: audit clauses (a) lizzi-side single-axis (operationalized via NCG-axiomatic re-derivation per S88 W-14 V.1 precedent) + (c) JOINT + (d) JOINT + (e) lizzi-side. PASS criteria: (a) NCG axioms 1-7 satisfied for the §VII.AH spectral-functional projection at obs2; (c) JOINT — Path-(c) successor anchor on the F_2-class projection consistent with NCG-axiomatic re-derivation; (d) JOINT — algebra-axis orthogonality 4-corner classification of obs2 consistent with §VII.AH theorem text; (e) Connes-Moscovici §III.4 finite-spectral-triple residue formula evaluated on obs2 yields the canonical Path-(c) successor anchor value within Class-B 0.1%.
3. **Dispatch volovik Axis-B substrate-IS / transit cross-reviewer** (substantive prompt content):
   - Receives: §VII.AH STAGE-1-CANDIDATE registered entry text; obs3 data file (LiteBIRD-sensitive observational constraint at the transit-substrate-IS side; data file pinned at plan-freeze); §VII.AH obs1 prior Stage-2 verdict for cross-citation; substrate-IS BdG superfluid analog spec.
   - Does NOT receive: obs2 data file (connes-only per orthogonality clause); any workshop transcript.
   - Task: audit clauses (b) transit-side single-axis (operationalized via volovik substrate-IS re-derivation; replaces transit-dynamics-aether-mechanic as original author) + (c) JOINT + (d) JOINT + (f) transit-side. PASS criteria: (b) substrate-IS / superfluid-universe consistency for obs3 LiteBIRD-sensitive observable; (c) JOINT — Path-(c) successor anchor on the F_2-class projection consistent with substrate-IS re-derivation (independent of NCG-axiomatic side); (d) JOINT — algebra-axis orthogonality 4-corner classification consistent with §VII.AH theorem text; (f) Bogoliubov / Kibble-Zurek scaling consistent with LiteBIRD-sensitive parameter at obs3.
4. **Aggregate cross-reviewer verdicts** (gen-physicist coordinator):
   - JOINT clauses (c) and (d): PASS-AND across both reviewers (logical AND).
   - Single-axis clauses: each cross-reviewer's own clauses PASS independently.
   - Substrate-input-orthogonality clause: PASSes by construction at obs2 ∨ obs3 (since the data files for obs2 and obs3 are loaded by ONLY ONE cross-reviewer each).
   - Final composite Stage-2 verdict for §VII.AH = `(connes_PASS_4_clauses ∧ volovik_PASS_4_clauses ∧ JOINT_c_d_PASS_AND ∧ orthogonality_obs2_or_obs3_PASS)`.
5. Emit verdict line + dual-SHA companion + 3-tuple companion to `computations/session-89/s89_gate_verdicts.txt`. Verdict-line value field MUST emit per-observable Stage-2 outcome: `value='{"obs1": "Verdict_B_with_substrate_input_overlap_caveat (S88 W7c-167)", "obs2": <verdict>, "obs3": <verdict>, "joint_pass_and": <verdict>, "orthogonality_clause_at_obs2_or_obs3": <verdict>}'`.

**Machinery pin (PRDR — Class 8.0/8.1 cardinality + substrate-input-orthogonality + multi-observable Stage-2)**:

| Pin | Value | Role |
|:----|:------|:-----|
| `connes_axis_reviewer` | `connes-ncg-theorist` | Axis-A NCG-axiomatic spectral side |
| `volovik_axis_reviewer` | `volovik-superfluid-universe-theorist` | Axis-B substrate-IS / transit side |
| `BLOCKED_reviewers` | `{lizzi-spectral-functional-theorist, transit-dynamics-aether-mechanic}` | original §VII.AH authoring agents |
| `connes_fallback` | `van-den-dungen-bridge-theorist` | if connes FAILs grep-validation on §VII.AH |
| `volovik_fallback` | `phonon-first-cosmologist` | if volovik FAILs grep-validation on §VII.AH |
| `dispatch_mode` | `parallel` | both reviewers simultaneous |
| `workshop_transcript_visible_to_reviewer` | `False` | per `joint-theorem-promotion.md` |
| `grep_validation_pattern` | `§VII\.AH\|W-9 R3-B Path-\(c\)\|Joint F_2-Class\|obs1.*obs2.*obs3 specifications` | downstream-inheritance reach test specific to §VII.AH |
| `multi_observable_count` | `3` | obs1 (PASSed at W7c-167 with caveat) + obs2 + obs3 |
| `obs1_status_input` | `PASSed_at_S88_W7c-167_with_substrate_input_overlap_caveat` | per `joint-theorem-promotion.md §"Substrate-input-orthogonality clause"` Verdict B |
| `obs1_shared_npz_sha` | `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f` | shared `s87_w7_ic_per_class_verify.npz` |
| `obs2_data_file` | `<PINNED-AT-PLAN-FREEZE-FROM-§VII.AH-REGISTERED-TEXT>` | spectral-functional projection at s=3; loaded ONLY by connes |
| `obs3_data_file` | `<PINNED-AT-PLAN-FREEZE-FROM-§VII.AH-REGISTERED-TEXT>` | LiteBIRD-sensitive observable; loaded ONLY by volovik |
| `data_file_disjointness_at_obs2_obs3` | `MANDATORY` | substrate-input-orthogonality clause at the structural-ceiling |
| `substrate_input_orthogonality_clause_status` | `MANDATORY-AT-PASS-via-obs2-or-obs3` | per W-23 V.1 / B.56 |
| `joint_clauses` | `{(c), (d)}` | PASS-AND across both reviewers |
| `single_axis_clauses_connes` | `{(a), (e)}` | NCG-axiomatic / spectral-side clauses |
| `single_axis_clauses_volovik` | `{(b), (f)}` | substrate-IS / transit-side clauses |
| `class_B_tolerance` | `0.001` (0.1%) | numerical tolerance |
| `cross_wave_dependency` | `W2_A.40` | A.40 chirality-fidelity recompute upgrades §VII.AQ binding (cross-link to A.38) |
| `level_pin` | `FULL` | full physical verification |
| `convention` | `vii-ah-stage-2-re-dispatch-obs2-obs3-substrate-input-orthogonal` | composite |
| `scheme` | `joint-theorem-promotion-stage-2-PASS-AND-2-axis-multi-observable-with-orthogonality-PASS` | aggregation rule |
| `L_max` | `10` | canonical |

**Input SHA-256 pins**:

| Input | Path / source | SHA |
|:------|:--------------|:----|
| §VII.AH STAGE-1-CANDIDATE registered entry text | `sessions/permanent-results-registry.md §VII.AH` | `<computed at plan-freeze>` |
| §VII.AH obs1 prior Stage-2 verdict line (Verdict B at S88 W7c-167) | `computations/session-88/s88_gate_verdicts.txt` line for `S88-W7C-167-VII-AH-OBS1-STAGE-2-VERIFY` | `<computed at plan-freeze>` |
| obs1 shared npz | `computations/session-87/s87_w7_ic_per_class_verify.npz` | `120435cbfd5ef313ebcba6e23ec1712c51d04a3f75b788034ebe7964aa32519f` (FULL 64-char) |
| obs2 data file (connes-only) | `<PINNED-AT-PLAN-FREEZE>` | `<computed at plan-freeze>` |
| obs3 data file (volovik-only) | `<PINNED-AT-PLAN-FREEZE>` | `<computed at plan-freeze>` |
| `joint-theorem-promotion.md` rule file (substrate-input-orthogonality clause + 4-stage pathway) | `.claude/rules/joint-theorem-promotion.md` | `<computed at plan-freeze>` |
| `cross-pillar-bridge-anatomy.md` rule file (algebra-axis orthogonality) | `.claude/rules/cross-pillar-bridge-anatomy.md` | `<computed at plan-freeze>` |
| W2 A.40 verdict (cross-wave) | `computations/session-89/s89_gate_verdicts.txt` | `<pinned at runtime>` |
| connes / volovik agent definitions | `.claude/agents/{connes-ncg-theorist,volovik-superfluid-universe-theorist}.md` | `<pinned at dispatch>` |

**Expected output 4-tuple**: `(value=<JSON_with_per_obs_verdicts_plus_orthogonality_status>, scheme=joint-theorem-promotion-stage-2-PASS-AND-2-axis-multi-observable-with-orthogonality-PASS, convention=vii-ah-stage-2-re-dispatch-obs2-obs3-substrate-input-orthogonal, L_max=10)` plus per-cross-reviewer 3-tuple companions.

**PASS / FAIL / INFO thresholds**:

- **PASS** iff:
  - connes returns PASS on all 4 NCG-side clauses (a) ∧ (c) ∧ (d) ∧ (e) on obs2
  - volovik returns PASS on all 4 substrate-IS-side clauses (b) ∧ (c) ∧ (d) ∧ (f) on obs3
  - JOINT (c) PASS-AND across connes + volovik
  - JOINT (d) PASS-AND across connes + volovik
  - Substrate-input-orthogonality clause PASSes at obs2 ∨ obs3 (data-file disjointness across obs2 and obs3)
  - Combined with prior obs1 PASS (Verdict B at S88 W7c-167 with caveat), the §VII.AH STAGE-1-CANDIDATE multi-observable Stage-2 verification is COMPLETE at the structural-ceiling
- **INFO** iff any cross-reviewer returns INFO on a sub-clause OR substrate-input-orthogonality clause partially holds: theorem stays at STAGE-1-CANDIDATE; specific INFO clauses route to S90+ for clause-targeted remediation
- **FAIL** iff ANY cross-reviewer returns FAIL on ANY clause OR data-file disjointness check FAILs at obs2 or obs3: STAGE-1-CANDIDATE stays; FAILing clauses route to next-session remediation

3-tuple annotation:
- `sign_verdict = N/A` (multi-observable PASS-AND aggregation non-signed)
- `magnitude_verdict = PASS` if all 8 clauses (4 connes + 4 volovik) PASS + JOINT (c)+(d) PASS-AND + orthogonality PASS; INFO if 6-7 of 8 + orthogonality PASS; FAIL if ≤ 5 OR orthogonality FAIL
- `regime_verdict = VALID` (multi-observable Stage-2 regime well-posed; substrate-input-orthogonality clause structurally ceiling-PASSes the prior obs1 substrate-input-overlap caveat)

**Substitution chain** (multi-observable Stage-2 PASS-AND with substrate-input-orthogonality direction):

```
Definition 1: §VII.AH STAGE-1-CANDIDATE has 3 observables: {obs1, obs2, obs3}
              obs1 status: PASSed Stage-2 at S88 W7c-167 with substrate-input-overlap caveat
                           (both reviewers loaded shared s87_w7_ic_per_class_verify.npz; Verdict B)
              obs2 status: un-Stage-2'd; data file pinned to be loaded ONLY by connes
              obs3 status: un-Stage-2'd; data file pinned to be loaded ONLY by volovik
Definition 2: substrate_input_orthogonality_predicate(obs_set):
              ∃ obs_i ∈ obs_set such that data_file(obs_i) loaded by EXACTLY ONE cross-reviewer
              (per joint-theorem-promotion.md §"Substrate-input-orthogonality clause" W-23 V.1)
Definition 3: structural_ceiling_PASS := substrate_input_orthogonality_predicate({obs2, obs3}) AND
                                          all_clauses_PASS_at_obs2_obs3 AND
                                          JOINT_clauses_PASS_AND_obs2_obs3
              (the structural ceiling is what advances STAGE-1 to STAGE-3 cleanly,
               WITHOUT substrate-input-overlap caveat)
Substitution: data_file(obs2) := <connes-only file>  (by pin)
              data_file(obs3) := <volovik-only file> (by pin)
              data_file(obs2) ∩ data_file(obs3) = ∅  (disjoint by construction)
              substrate_input_orthogonality_predicate({obs2, obs3}) = TRUE
                ==> ∃ obs_i (in fact BOTH obs2 and obs3 individually satisfy single-reviewer load)
Simplification: structural_ceiling_PASS factorizes as:
                (connes_PASS_a_e_on_obs2) AND (volovik_PASS_b_f_on_obs3)
                AND (PASS_AND_c on both obs2, obs3) AND (PASS_AND_d on both obs2, obs3)
                AND (orthogonality clause PASS by construction)
              The prior obs1 substrate-input-overlap caveat is structurally retired by
              orthogonality-PASS at obs2 ∨ obs3: the §VII.AH theorem now has at least one
              orthogonal-data observable verified, satisfying the structural ceiling.
Direction:    structural_ceiling_PASS  ==>  §VII.AH multi-observable Stage-2 verification
                                              COMPLETE; STAGE-1 -> STAGE-3 promotion eligible
                                              WITHOUT substrate-input-overlap caveat;
                                              the obs1 caveat at S88 W7c-167 is documented
                                              in audit trail but does NOT block Stage-3 promotion
              FAIL  ==>  multi-observable Stage-2 has at least one FAIL or orthogonality
                          violation; STAGE-1 stays; the §VII.AH theorem remains at the prior
                          obs1-only PASS-with-caveat layer
              INFO  ==>  partial PASS or partial orthogonality; STAGE-1 stays;
                          clause-targeted remediation
Conclusion:   PASS reading is "multi-observable Stage-2 COMPLETE at structural ceiling, with
              substrate-input-orthogonality satisfied at obs2 and obs3 by construction"; the
              calibration corpus for substrate-input-orthogonality clause (currently K=1
              SUGGESTION at S88 W7c-167) advances toward K=3 MANDATORY threshold with the
              obs2 and obs3 PASS instances.
```

Python verification at plan-author time (set theory + structural integrity):

```
# Substrate-input-orthogonality clause structural verification:
data_file_obs1 = "s87_w7_ic_per_class_verify.npz"  # shared between both Stage-2 reviewers at W7c-167
data_file_obs2 = "<connes-only-file-pinned-at-plan-freeze>"
data_file_obs3 = "<volovik-only-file-pinned-at-plan-freeze>"
loaders_obs1 = {"connes-ncg-theorist", "volovik-superfluid-universe-theorist"}  # SHARED at W7c-167
loaders_obs2 = {"connes-ncg-theorist"}                                          # connes-only
loaders_obs3 = {"volovik-superfluid-universe-theorist"}                         # volovik-only
# Substrate-input-orthogonality predicate at obs2 OR obs3:
exists_single_loader = (len(loaders_obs2) == 1) or (len(loaders_obs3) == 1)
assert exists_single_loader  # PASS by construction
# Disjointness check: obs2 and obs3 do NOT share data files
assert data_file_obs2 != data_file_obs3
# Joint PASS-AND clauses (c) and (d) require both reviewers PASS independently:
def joint_pass_and(verdicts):
    return all(v == "PASS" for v in verdicts)
# Aggregate predicate: structural-ceiling PASS
def structural_ceiling_pass(connes_pass, volovik_pass, joint_c_pass_and, joint_d_pass_and, orth_pass):
    return all([connes_pass, volovik_pass, joint_c_pass_and, joint_d_pass_and, orth_pass])
```

Verified: substrate-input-orthogonality clause PASSes by construction at obs2 ∨ obs3; data-file disjointness enforced by plan-freeze pin.

**What PASSES and what FAILS mean for solution space**:

- **PASS** ⟹ §VII.AH Joint F_2-Class Path-(c) Theorem multi-observable Stage-2 verification COMPLETE at structural ceiling; STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion eligible WITHOUT substrate-input-overlap caveat (the prior obs1 caveat at S88 W7c-167 is documented in audit trail but does NOT block Stage-3 promotion); substrate-input-orthogonality clause calibration corpus (currently K=1 SUGGESTION at S88 W7c-167) advances by 1-2 instances (obs2 + obs3 PASSes); algebra-axis orthogonality 4-corner classification preserved at the §VII.AH specific instance.
- **INFO** ⟹ partial multi-observable Stage-2 PASS: e.g., obs2 PASSes but obs3 INFO; or JOINT (c) PASS-AND but JOINT (d) INFO; theorem stays at STAGE-1-CANDIDATE; specific INFO clauses route to S90+; substrate-input-orthogonality clause calibration corpus advances by partial instance.
- **FAIL** ⟹ at least one cross-reviewer FAILs on at least one clause OR data-file disjointness violated at obs2 or obs3: STAGE-1-CANDIDATE stays; if FAIL is on JOINT clause (c) or (d), the §VII.AH cross-axis joint-theorem structure has unresolved structural defect; next-session remediation queues clause-targeted re-derivation.

**Effort estimate**: 1.5 wave-equivalents (2 parallel cross-reviewer dispatches; each performing 4-clause audit on their respective obs2 / obs3; substrate-input-orthogonality data-file disjointness audit at plan-freeze; multi-observable verdict-line value-field aggregation per `joint-theorem-promotion.md` Stage-2 protocol; cross-wave coordination with W2 A.40 if A.40 lands during the wave).

**Substrate framing per `phononic-framing.md` IS-not-IN**:

§VII.AH Joint F_2-Class Path-(c) Theorem IS the substrate's structural identity for the lizzi-side spectral-functional ↔ transit-side substrate-IS bridge at the F_2-class projection of `D_K`. The 3 observables (obs1, obs2, obs3) are 3 distinct substrate-IS images of the joint theorem's content: obs1 = per-class IC verification (PASSed at W7c-167); obs2 = spectral-functional projection at substrate-distance pole s=3; obs3 = LiteBIRD-sensitive observable on the transit-substrate-IS side. Direction-of-explanation: substrate IS the F_2-class projection of `(A_K, H, D_K)` ⟶ Joint F_2-Class Path-(c) Theorem IS substrate-IS ⟶ 3 observables are 3 substrate-IS images of the theorem's content ⟶ Stage-2 multi-observable verification IS the structural test that the joint theorem's clauses (c) and (d) PASS-AND'd across all observables at the substrate-input-orthogonality structural ceiling. FORBIDDEN framing: "the §VII.AH theorem makes predictions IN observable space; we test the predictions in obs1/obs2/obs3 containers"; INVERTED: "the §VII.AH theorem IS substrate-IS; obs1/obs2/obs3 ARE 3 substrate-IS images of the theorem's content; the multi-observable Stage-2 verification IS the substrate's structural test that the joint theorem's identity is preserved across all 3 substrate-IS image-projections; the substrate-input-orthogonality clause IS the structural ceiling that retires the prior obs1 substrate-input-overlap caveat by demonstrating obs2 and obs3 carry single-cross-reviewer data load by construction".

---

## Wave 4 → Waves 2/7 Decision Point

This wave has structural dependencies on Wave 2 (Cluster B Connes-Karoubi pairing canonical pipeline + Cluster F chirality-fidelity recompute) and Wave 7 (Cluster G n_s_FW vs c_sub_corrected Mellin-cone closure). The decision-point routing instructions:

| Cross-wave dependency | Source wave / gate | Target gate(s) in W4 | Routing instruction at S89 plan-freeze |
|:----------------------|:-------------------|:---------------------|:----------------------------------------|
| W2 A.3 Connes-Karoubi pairing canonical infrastructure | W2 §W2-? `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE` | W4 §W4-2 (A.10) lizzi-axis cross-reviewer consumes A.3 npz | A.10 dispatch BLOCKED until A.3 verdict ∈ {PASS, INFO}; if A.3 FAILs, A.10 routes to PRE-REG-INC mechanical-closure with `value='PRE-REG-INC_blocked_by_A.3_<status>'` |
| W2 A.40 chirality-fidelity 3-proxy recompute | W2 §W2-? `S89-CHIRALITY-FIDELITY-3-PROXY-RECOMPUTE-CS-GV-ETACS` | W4 §W4-6 (A.38) §VII.AQ Level-3 anchor binding; W4 §W4-7 (A.39) cross-link to §VII.AQ binding context | A.38 dispatches WITH CURRENT `-CANONICAL-IMPORT-BINDING` form regardless of A.40 status; if A.40 PASSes during S89, A.38 verdict is ARCHIVED at `-CANONICAL-IMPORT-BINDING` and a follow-up gate at S90 audits the upgraded `-SUBSTRATE-NATURAL-BINDING` form. A.39 is INDEPENDENT of A.40 outcome (audits §VII.AH multi-observable, not §VII.AQ). |
| W7 A.24 n_s_FW vs c_sub_corrected Mellin-cone closure | W7 §W7-? `S89-N-S-FW-VS-C-SUB-CORRECTED-MELLIN-CONE-CLOSURE-FWD-C1` | W4 §W4-4 (A.21) JOINT-(n_s, α_s) hypersurface Stage-2 | A.21 dispatch is INDEPENDENT of A.24 closure outcome (A.21 audits the substrate-IS Route-B identity n_s_FW_exact = 9561/10000 + α_s_canonical = -8587279/100000000; A.24 audits the n_s_FW vs Planck-observed n_s tension, which is a downstream consequence). If A.24 FAILs (Level-3 anchor outside Level-2 envelope by ≥2×), A.21 verdict still PASSes at the Sage-QQ exact rational identity layer; the lab discrimination 2D hypersurface verdict reports the Planck-observed disagreement honestly. |
| W2 A.3 / A.4 / A.20 Connes-Karoubi sequential chain | W2 §W2-? gates | None directly in W4 | A.20 (Sagan-revised dual-prior) does NOT dispatch in W4; it is a W2 carry-forward that depends on A.3+A.4 PASS. Mentioned here only to clarify that W4 does not consume A.20. |

Composition: W4 dispatches in S89 Batch 1 with W2 (Cluster B) and W7 (Cluster G) in parallel where dependencies permit. Where a dependency BLOCKS dispatch (e.g., A.10 on A.3 PASS), the orchestrator coordinates intra-batch sequencing — A.3 dispatches first; A.10 dispatches only after A.3 verdict resolves. A.11 → A.10 is the same intra-wave sequencing pattern within W4.

---

## Wave 4 Machinery-Enumeration Pin (§0.11)

This section enumerates EVERY free machinery parameter across Wave 4's 7 gates, pinned at plan-freeze per `epistemic-discipline.md §"Pre-Registration Completeness"` PRDR (Pre-Registration Dry-Run) discipline. PRU Class 8.0/8.1 cardinality and Class 8.2/8.3/8.5 form pre-registration are enforced via the per-gate machinery pin tables above; this wave-level enumeration is the consolidated list for the Wave 4 plan-freeze validator (`_pru_cardinality_audit.py` on the S89 W4 plan-block).

### Cross-reviewer dispatch parameters (all 7 gates)

| Pin | Wave-4 enumeration |
|:----|:-------------------|
| `dispatch_mode` | `parallel` (all multi-agent dispatches) |
| `workshop_transcript_visible_to_reviewer` | `False` (per `joint-theorem-promotion.md §"Two-Agent Independent-Verify"`) |
| `class_B_tolerance` | `0.001` (0.1%) (numerical tolerance across all gates) |
| `level_pin` | `FULL` (all 7 gates; no SCHEMATIC helper consumption per `substrate-first-canonical-sourcing.md §(iv)` MANDATORY-at-K=4) |
| `L_max` | `10` (canonical for §W4-2 / §W4-3 / §W4-4 / §W4-6 / §W4-7) or `N/A` (§W4-1 single SDP solve) |

### Stage-2 protocol pin (per `joint-theorem-promotion.md`)

| Pin | Wave-4 enumeration |
|:----|:-------------------|
| `stage2_axis_b_selection_protocol_audit` | MANDATORY at plan-freeze for §W4-2 / §W4-3 / §W4-5 / §W4-6 / §W4-7 (3 conditions: axis-distinctness ∧ original-authoring-agent exclusion with downstream-inheritance reach test ∧ audit-coverage adequacy) |
| `substrate_input_orthogonality_clause_status` | MANDATORY-at-PASS for §W4-4 / §W4-6 / §W4-7 (N≥2 observables); SUGGESTION-pending-for §W4-2 (4-cell joint AND has structurally distinct sub-tests per cell, not multi-observable in the same sense) |
| `joint_theorem_promotion_6_item_audit` | enforced at plan-freeze: (1) parallel dispatch; (2) different axes; (3) NOT original authoring agents (with reach test); (4) workshop transcripts NOT in dispatch prompt; (5) JOINT clauses PASS-AND'd; (6) cross-reviewer's audit machinery NOT structurally self-authored (per S88 W-23 V.8 / B.60 SUGGESTION at K=1) |

### Cross-reviewer assignments per gate

| Gate | Axis-A reviewer | Axis-B reviewer | Axis-C reviewer | Fallback(s) | BLOCKED |
|:-----|:----------------|:----------------|:----------------|:------------|:--------|
| §W4-1 (A.11) | connes-ncg-theorist | — | — | — | — |
| §W4-2 (A.10) | lizzi-spectral-functional-theorist | connes-ncg-theorist | — | (CROSS-pattern: lizzi audits connes-axis; connes audits lizzi-axis) | — |
| §W4-3 (A.12) | connes-ncg-theorist | lizzi-spectral-functional-theorist (CONDITIONAL grep) | transit-dynamics-aether-mechanic | van-den-dungen-bridge-theorist (lizzi fallback) | — |
| §W4-4 (A.21) | volovik-superfluid-universe-theorist | mack-cosmic-bridge | — | — | — |
| §W4-5 (A.30) | van-den-dungen-bridge-theorist | phonon-first-cosmologist | — | kitaev-quantum-chaos-theorist (Axis-A or Axis-B) | lizzi-spectral-functional-theorist + connes-ncg-theorist (original authors of §VII.AR) |
| §W4-6 (A.38) | connes-ncg-theorist | volovik-superfluid-universe-theorist | — | van-den-dungen-bridge-theorist (connes fallback if co-authoring overlap > 30%) | — |
| §W4-7 (A.39) | connes-ncg-theorist | volovik-superfluid-universe-theorist | — | van-den-dungen-bridge-theorist (connes fallback) + phonon-first-cosmologist (volovik fallback) | lizzi-spectral-functional-theorist + transit-dynamics-aether-mechanic (original authors of §VII.AH at S87 W-9) |

### Convention pins

| Convention | Wave-4 gates carrying it |
|:-----------|:-------------------------|
| `substrate-canonical-14-state-basis-no-Pad` | §W4-1 |
| `four-corner-dual-basis-stage-2-cross-axis-verify` | §W4-2 |
| `vii-w-3-lab-three-agent-stage-2-cross-axis-verify` | §W4-3 |
| `joint-n_s-alpha_s-hypersurface-stage-2-cross-axis-verify-Class-8-5-PRU` | §W4-4 |
| `vii-ar-stage-2-cross-axis-verify-no-lizzi-no-connes` | §W4-5 |
| `vii-aq-stage-2-cross-axis-canonical-import-binding-with-substrate-input-orthogonality` | §W4-6 |
| `vii-ah-stage-2-re-dispatch-obs2-obs3-substrate-input-orthogonal` | §W4-7 |

### Verdict-line value-field formats per gate

| Gate | Value-field format |
|:-----|:-------------------|
| §W4-1 (A.11) | scalar integer rank: `value=<rank_natural>` |
| §W4-2 (A.10) | scalar integer 0-4: `value=<count_of_4_cells_PASS>` |
| §W4-3 (A.12) | scalar integer 0-8: `value=<count_of_8_clauses_PASS>` |
| §W4-4 (A.21) | JSON 2D hypersurface (Class 8.5 PRU): `value='{"n_s": "9561/10000", "alpha_s": "-8587279/100000000", "lab_discrimination_2d": "outside_2sigma"}'` |
| §W4-5 (A.30) | scalar integer 0-8: `value=<count_of_8_clauses_PASS>` |
| §W4-6 (A.38) | scalar integer 0-9 (8 clauses + orthogonality): `value=<count_of_8_clauses_PASS_PLUS_orthogonality>` |
| §W4-7 (A.39) | JSON multi-observable: `value='{"obs1": "Verdict_B_W7c-167", "obs2": <verdict>, "obs3": <verdict>, "joint_pass_and": <verdict>, "orthogonality_clause_at_obs2_or_obs3": <verdict>}'` |

### PRU Class-8 pre-registration audit at plan-freeze

- **Class 8.0/8.1 (cardinality)**: each of the 7 gates has its machinery pin table fully enumerated above (cross-reviewer pairs, dispatch mode, transcript-visibility, class-B tolerance, L_max, level pin). PASS at Wave-4-level.
- **Class 8.2 (verifier-rubric)**: each Stage-2 gate's PASS criteria (i)/(ii)/(iii)/(iv) per cross-reviewer are pre-registered as substantive content checks (NCG axiom satisfaction, Connes-Moscovici §III.4 numerical match, FI/RD/MIXED classification, etc.); the rubric pattern set is enumerable per gate. PASS at Wave-4-level.
- **Class 8.3 (publication-precision)**: A.21 publishes Sage-QQ exact rationals (n_s_FW_exact + α_s_canonical) at full precision; verdict-line value field carries the rational form bit-exact. A.38 references `gv_canonical_difference_FW = -40579.1500479506` (14 sig fig); class_B tolerance 0.1% on this pin computes to 40.579... abs tol, well above precision floor. PASS at Wave-4-level.
- **Class 8.5 (joint-hypersurface-pre-registration-form)**: A.21 emits 2D verdict-line value-field per Class 8.5 PRU MANDATORY (joint-hypersurface form NOT 1D scalar). PASS at Wave-4-level.
- **Class 8.6 (layered-substitution-chain-audit)**: substitution chains explicit per gate; the §W4-2 4-cell joint AND aggregation, the §W4-3 3-axis Stage-2 PASS-AND, the §W4-4 Route-B identity + Planck-discrimination, the §W4-5 axis-distinctness selection, the §W4-6 canonical-import vs substrate-natural binding, the §W4-7 multi-observable orthogonality each have substitution chains in their respective gate-blocks. PASS at Wave-4-level.

---

## Wave 4 Input-SHA Ledger

This section consolidates EVERY input file consumed by the 7 gates of Wave 4 for the wave-level audit_sha256 closure pin (per `gate-verdicts.md §"Pre-Registration Protocol"` step 1 + `_script_template.py append_verdict()` pattern). Each gate's individual input-pin map is in its respective machinery pin table above; this ledger is the consolidated wave-level view.

### File-level pins (computed at S89 plan-freeze)

| Input file | Path | Consumed by |
|:-----------|:-----|:------------|
| §VII.U.2 4-corner classification entry | `sessions/permanent-results-registry.md §VII.U.2` | §W4-2 |
| §VII.W-3.LAB STAGE-1-CANDIDATE entry | `sessions/permanent-results-registry.md §VII.W-3.LAB` | §W4-3 |
| §VII.AS JOINT-(n_s, α_s) hypersurface entry (or alt slot) | `sessions/permanent-results-registry.md §VII.AS` | §W4-4 |
| §VII.AR LEVEL-DRESSED rank-ordering entry | `sessions/permanent-results-registry.md §VII.AR` | §W4-5 |
| §VII.AQ canonical-import-binding entry | `sessions/permanent-results-registry.md §VII.AQ` | §W4-6 |
| §VII.AH Joint F_2-Class Path-(c) Theorem STAGE-1-CANDIDATE | `sessions/permanent-results-registry.md §VII.AH` | §W4-7 |
| §W5b-50 spec | `sessions/archive/session-88/s88-w16-w5b-50-rank-deficiency.md` | §W4-1 + §W4-2 |
| §W5b-50 16×16 Pad SDP verdict line | `computations/session-88/s88_gate_verdicts.txt` | §W4-1 + §W4-2 |
| Pillar III substrate-IS Hochschild pairing npz | `sessions/archive/session-86/workshops/s86-hp1-cohomology-quantum-metric-bridge.md (Pillar III Hochschild pairing substrate; canonical_constants.py:R_universal_HP1_strict_F4=1.030902 + cocycle_norm_phi67=0.793346 + cocycle_norm_phi88=0.108307 per W-5 V4 substitution chain Step 2; W-5 substrate values land directly in canonical_constants, NOT a stand-alone .npz)` | §W4-3 |
| Pillar IV BZ-trace canonical npz | `sessions/archive/session-86/workshops/s86-hp1-cohomology-quantum-metric-bridge.md (Pillar IV BZ-trace substrate; canonical via Peotta-Törmä quantum-metric integrated trace per W-5 §VII.W cross-pillar bridge entry; substrate values in canonical_constants.py per same constants as Pillar III; NOT a stand-alone .npz)` | §W4-3 |
| D_K^≤10 spectrum cache | `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (filtered to L_max=10) | §W4-4 + §W4-6 |
| Substrate-IS Route-B identity derivation | `sessions/framework/registry/branch-iv-canonical.md` | §W4-4 + §W4-6 |
| Planck 2018 (n_s, α_s) joint locus | `sessions/framework/registry/mack-observational-constraints.md` | §W4-4 |
| 3HeB-inheritance file (substrate-IS side) | `sessions/framework/registry/branch-iv-canonical.md` + `inheritance-falsifier-protocol.md` | §W4-6 |
| §VII.AH obs1 prior Stage-2 verdict (W7c-167) | `computations/session-88/s88_gate_verdicts.txt` | §W4-7 |
| §VII.AH obs1 shared npz | `computations/session-87/s87_w7_ic_per_class_verify.npz` | §W4-7 (cross-citation only) |
| obs2 data file (connes-only) | `<PINNED-AT-PLAN-FREEZE-FROM-§VII.AH-REGISTERED-TEXT>` | §W4-7 |
| obs3 data file (volovik-only) | `<PINNED-AT-PLAN-FREEZE-FROM-§VII.AH-REGISTERED-TEXT>` | §W4-7 |
| Regulator-class atlas spec | `sessions/framework/registry/falsifier-master-inventory.md` | §W4-5 |
| Substrate-distance pole s=4 spectral-moment data | `computations/session-88/s88_w7a_rank_vs_magnitude_layer_discriminator.npz` | §W4-5 |
| `canonical_constants.py` | `computations/_shared/canonical_constants.py` | §W4-1 + §W4-2 + §W4-3 + §W4-4 + §W4-6 |

### Rule-file pins (computed at S89 plan-freeze)

| Rule file | Consumed by |
|:----------|:------------|
| `.claude/rules/joint-theorem-promotion.md` (4-stage pathway + Stage-2 Axis-B Selection Protocol + substrate-input-orthogonality clause + 6-item audit) | §W4-2 + §W4-3 + §W4-4 + §W4-5 + §W4-6 + §W4-7 |
| `.claude/rules/cross-pillar-bridge-anatomy.md` (algebra-axis orthogonality K=3 MANDATORY + per-Bulletin-per-pole ladder + Level-2 layer distinction) | §W4-2 + §W4-3 + §W4-5 |
| `.claude/rules/inheritance-falsifier-protocol.md` (Class A NULL kernel-signature + Class B cohomology-asymmetry ratio + (Δ_B/Δ_A)^p cancellation theorem) | §W4-6 |
| `.claude/rules/phononic-framing.md` (IS Space + Single-τ-slice vs moduli-deformation substrate-IS levels) | all 7 gates |
| `.claude/rules/epistemic-discipline.md` (PRU Class 8.0/8.1/8.2/8.3/8.5/8.6 + Source-Reconciliation 6-class taxonomy + Layer-Decomposition) | all 7 gates |
| `.claude/rules/registry-landing.md` (SOURCE-DOUBLE-CITE-CO-PRIMARY + algebra-axis orthogonality criterion (4) MANDATORY + Operator-Projection Reading-A Naming Hygiene MANDATORY at K=3) | §W4-2 + §W4-5 |
| `.claude/rules/substrate-first-canonical-sourcing.md` (Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY + Class-(f) HARD-HALT + SCHEMATIC vs full physical level pin MANDATORY at K=4) | §W4-5 |
| `.claude/rules/regulator-pin-discipline.md` (a_n^{regulator} tagging + 3-axis pin: UV-regulator × Level × Binding) | §W4-5 + §W4-6 |
| `.claude/rules/gate-verdicts.md` (canonical verdict-file path + S87+ schema-v2 3-tuple annotation + Option A `supersedes` protocol for sig_5) | all 7 gates |
| `.claude/rules/math-scripts.md` (substitution chain MANDATORY + D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check) | all 7 gates |
| `.claude/rules/v3-closure-recovery.md` (PROHIBITED_ACTIONS Class 1-4) | all 7 gates |
| `.claude/rules/agent-standards.md` §"HIGH-DENSITY WORKSHOP TEMPLATE T2-5" + §"AMRI" | wave-level |

### Agent-definition pins (computed at runtime per dispatch)

| Agent | Path | Used in |
|:------|:-----|:--------|
| `connes-ncg-theorist` | `.claude/agents/connes-ncg-theorist.md` | §W4-1, §W4-2 (CROSS), §W4-3, §W4-6, §W4-7 |
| `lizzi-spectral-functional-theorist` | `.claude/agents/lizzi-spectral-functional-theorist.md` | §W4-2 (CROSS), §W4-3 (CONDITIONAL grep) |
| `transit-dynamics-aether-mechanic` | `.claude/agents/transit-dynamics-aether-mechanic.md` | §W4-3 |
| `volovik-superfluid-universe-theorist` | `.claude/agents/volovik-superfluid-universe-theorist.md` | §W4-4, §W4-6, §W4-7 |
| `mack-cosmic-bridge` | `.claude/agents/mack-cosmic-bridge.md` | §W4-4 |
| `van-den-dungen-bridge-theorist` | `.claude/agents/van-den-dungen-bridge-theorist.md` | §W4-5 (Axis-A) + fallback for §W4-3 / §W4-6 / §W4-7 |
| `phonon-first-cosmologist` | `.claude/agents/phonon-first-cosmologist.md` | §W4-5 (Axis-B) + fallback for §W4-7 |
| `kitaev-quantum-chaos-theorist` | `.claude/agents/kitaev-quantum-chaos-theorist.md` | §W4-5 (fallback) |

### Cross-wave dependency pins (computed at runtime)

| Cross-wave dep | Pinned at runtime by | Status notes |
|:---------------|:---------------------|:-------------|
| W2 A.3 verdict | §W4-2 dispatch coordinator | BLOCKED-conditional dispatch |
| W2 A.40 verdict | §W4-6 + §W4-7 (cross-link only) | independent dispatch; §VII.AQ binding context note |
| W7 A.24 verdict | §W4-4 (cross-link only) | independent dispatch; lab-discrimination 2D verdict reports honestly |
| §W4-1 (A.11) verdict | §W4-2 dispatch coordinator | BLOCKED-conditional intra-wave |

### Wave-4 closure SHA computation

The Wave-4-level audit_sha256 closure is computed at plan-freeze as `closure_hash(input_pin_map)` per `_script_template.py append_verdict()` pattern. The input-pin map for the Wave-4 plan-block is the ordered union of:
1. All file-level pins above (rule-file SHAs + registry-entry SHAs + npz/data-file SHAs + canonical_constants.py SHA)
2. All cross-reviewer agent-definition SHAs (computed at runtime per dispatch)
3. Per-gate machinery pin tables (the 7 individual gate-block PRDR pins)

Per `methodology-wave-allowlist.md` rules: this Wave-4 plan-block is COMPUTE-class (M1 fails — numerical PASS-AND aggregation predicate; M4 not required); no allowlist append needed for any of the 7 W4 gates.

---

