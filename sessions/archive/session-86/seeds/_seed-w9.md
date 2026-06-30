# Seed file — sessions/archive/session-86/session-86-w9-workingpaper.md

**Date**: 2026-04-26
**Investigator**: phonon-first-cosmologist
**Source WP**: `sessions/archive/session-86/session-86-w9-workingpaper.md` (616 lines, 65,362 bytes; read in full in two chunks)

## Substance digest (for orientation)

W9 produced four sub-gate verdicts touching three structurally-distinct topics:

- **C26.A** (`S86-W2-2-PREDICTED-INSTANTIATIONS-C26A`): **FAIL** — `dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3) = 0` (predicted 1). Theorem-grade FAIL by HP^odd vanishing on finite-dim semisimple algebras over ℂ (Connes 1985 §II Cor.4 + Loday Cyclic Homology Thm 1.4.4 + Wedderburn). Plan §10 Step 2 conflated cochain-level (where rank-2 Casimir generator e₂ exists in C³) with periodic-cyclic colimit (where e₂ is a coboundary). The S85 W2 disjoint-corridor theorem already established the obstruction. Carry-forward `S87-W2-2-VII-P-PRIME-EVEN-RECAST` re-attempts at HP⁴.

- **C26.B** (`S86-W2-2-PREDICTED-INSTANTIATIONS-C26B`): **PASS** — bucket_count = 4 EXACTLY at every q ∈ [0.50, 0.95] step 0.05; bucket dims `{3, 3, 3, 3}` integer-rigid; max dev/tol ratio = 0.00e+00. Stronger than the plan's O((1−q)²) tolerance. Extends S83 W2-G20 Cartan sub-factor 4-bucket result to the full A_F^q.

- **C24** (`S86-VII-P-V2-PARITY-EXTENSION`): **INFO** — composite (False, True). §VII.P-v2 component **fails**: HP⁰-content-distinct restriction does NOT separate the (C_H, C_epsH) twin pair (both have factor_support `{H}` and HP⁰ dim = 1). §VII.P' component **passes**: |ω_GV| = 40579.15, eigenvalues +8404.22 and −48983.37, 15 OOM above 1e-12 floor. Carry-forward `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` queues HP¹-content-distinct using `eps_H_HP1_norm = 16.197719`.

- **C44** (`S86-R-PROTECTION-MELLIN-CRITERION`): **FAIL** — concordance 0.0326 / 184. The lizzi S-1 §IV.5 criterion reduces under scalar-pin Dirac-delta spectral density to capturing only structural zeros (3) + MIXED external-cancellation observables (3); misses 178/181 empirical-R observables. Failure is regulator-independent (5-atlas ≡ ζ-only) and L_max-independent (L=10 ≡ L=8). Method substituted Dirac-delta spectral density for the missing `dk_spectrum_L{10,8}.npz` cache.

Two structural patterns recur across the four gates:

1. **Parity-grading orthogonality**: HP^odd vanishes on semisimple/ℂ; HP⁰ is parity-blind to HP¹ twists. C26.A + C24 §VII.P-v2 both failed because predicted lifts lived in the wrong parity slot. C26.B + §VII.P' both passed because they lived in correctly-populated slots. The substrate's NCG cohomology ring respects parity grading exactly.

2. **Structural pre-refutation by S85 closure material**: C26.A FAIL was already implied by `S85-W2-HP3-DISJOINT-CORRIDOR-THREE-WAY` (PASS, value=0). C24 §VII.P-v2 FAIL was already implied by Lizzi Corollary E in S85 §II.9. The W9 plan instantiated predictions whose answers were determinable from prior closure material — neither was a coincidence; both were artefacts of the S85 closeout's prediction text being internally inconsistent with its own algebraic body.

The C44 method-deviation note is also non-trivial: the plan §6 promised D_K-cache spectral density, but the cache was absent and the script substituted Dirac-delta. The substitution is honest under scalar-pin observables, but it is a structurally weaker test than the plan envisioned — and the S87 (a) carry-forward is the proper-method re-run.

## Candidates

### Candidate 1 — Multi-eigenvalue Mellin criterion test (C44 carry-forward (a) execution)

**What it would do**: Reconstruct the missing `computations/cache/dk_spectrum_L{10,8}.npz` D_K eigenvalue cache (~155,984 eigenvalues at L_max=10), then re-run the lizzi S-1 §IV.5 Mellin-moment criterion under multi-eigenvalue spectral density f_O(t) — i.e., not the Dirac-delta substitute used at S86 W9. Test whether concordance recovers above the 0.80 INFO threshold once the spectral density is genuinely multi-modal. Compare against the empirical 184-row W0-9 catalog. Decompose by sub-bucket (DK_RATIO, PDG_OBS, PLANCK_OBS, etc.) to see which sub-buckets the criterion can characterize under the proper method.

**Why it's worthwhile**: C44 closed at concordance 0.0326 under a documented method substitution — Dirac-delta spectral density `f_O(t) = δ(t − |v_O|)` instead of D_K-cache spectral density. The §11 carry-forward (a) explicitly queues this re-run as the "proper-method" test. Without it, we cannot distinguish "criterion is structurally wrong" from "criterion is right but the scalar-pin instantiation neutered it." The method-deviation footnote on lines 545–546 acknowledges the FAIL is genuine ONLY under the substituted method. The cache reconstruction is itself a precondition for any future spectral-density-based gate (the W9 plan already demanded `dk_spectrum_L{10,8}.npz` and was forced to substitute). Effort estimate from §11 is 8-12h, which fits a solo dispatch.

**Type**: solo (1 agent)

**Suggested agents**: lizzi-spectral-functional-theorist (criterion source author; owns S-1 §IV.5)

**Rounds (workshops only)**: n/a (solo)

**Context the workshop will need**:
- Pinned upstream: `S86-R-PROTECTION-MELLIN-CRITERION` content_sha256 `e05b3f0def8d7087...` (the FAIL that is being re-tested under proper method)
- Cache reconstruction protocol: D_K Peter-Weyl construction at L_max ∈ {8, 10} on Jensen-deformed SU(3); ~155,984 eigenvalues at L=10 per the canonical-constants pin
- Atlas: same 5-regulator atlas {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} as C44, per S80 W0-9 baseline
- Empirical baseline: `computations/s80_w09_canonical_classification.py` CLASSIFICATION dict (RATIO=123, ABSOLUTE=58, MIXED=3); `s80_w09_classification_table.md` for human-readable reference
- Pre-registered thresholds: PASS ≥ 0.95, INFO ∈ [0.80, 0.95), FAIL < 0.80 (same as C44; the gate is whether multi-eigenvalue density rescues concordance)
- Key adjudication question: does multi-eigenvalue density change the verdict on the 178 FN observables (full counter-example list at `computations/s86_w9_C44_counterexamples.csv`)?

---

### Candidate 2 — HP¹-content-distinct §VII.P-v2 refinement (C24 carry-forward execution)

**What it would do**: Re-attempt the §VII.P-v2 wall refinement using HP¹-content-distinct corridor restriction (the structurally-correct separator), replacing the failed HP⁰-content-distinct attempt. The ε_H twin-pair (C_H, C_epsH) shares factor_support `{H}` and HP⁰ content dim = 1, but C_epsH carries the GV-twist class with `eps_H_HP1_norm = 16.197719` (canonical_constants.py line 155) — so HP¹-content-distinct DOES separate the pair by construction. Verify that R_P|_{HP¹-content-distinct} drops the (C_H, C_epsH) twin pair to strict (i.e., 7 classes, not 6).

**Why it's worthwhile**: The C24 §11 solution-space note explicitly identifies this as the corrected refinement direction: "the S85 closeout's prediction (HP⁰-content-distinct as separator) was internally inconsistent with the same closeout's Corollary E." The carry-forward `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` is logged with effort 3-4h. Importantly, this is NOT a duplicate of the S85 W2-7 §VII.P closure — it is the structurally-corrected refinement that the S85 closeout's Corollary E itself implies but did not execute. Together with §VII.P' (which already landed at C24), this would complete the §VII.P parity-family registry.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (owned C24 in W9; has the corridor catalog and ε_H machinery in working memory)

**Rounds (workshops only)**: n/a (solo)

**Context the workshop will need**:
- Pinned upstream: `S86-VII-P-V2-PARITY-EXTENSION` content_sha256 `16f18e735d7153e2...` (the INFO that this gate refines)
- Canonical: `eps_H_HP1_norm = 16.197719` (canonical_constants.py line 155); `HP1_dim = 3` (line 165); `HP0_content_dim = 3` (line 423, added in W9)
- Corridor catalog: 7-corridor `computations/s85_w2_disjoint_corridor_counter_construction.json` (canonical pre-W9 catalog). C24 already enumerated all 7 with HP⁰ content + Seeley-DeWitt signatures + GV-twist column.
- Pre-registered threshold: integer difference in HP¹ content dim between C_H and C_epsH must equal 1 (PASS); 0 (FAIL); other integer (INFO with structural reason).
- Cross-check: the Hermitian Ω_GV kernel restricted to {C_H, C_epsH} from C24 already has rank 1 (single non-zero ω-driven coupling); this gate must reconcile that rank-1 finding with the HP¹-content-distinct count.

---

### Candidate 3 — W2-2 mother-theorem post-W9 closure audit + §VII.K-DUAL-q registry promotion

**What it would do**: Execute the S87 W0 registry-side closure for the W2-2 mother-theorem (`S85-W2-CROSS-SESSION-THEOREM-FAMILY`): (a) promote §VII.K-DUAL-q from PREDICTED to VERIFIED in `s85_w2_theorem_family.py` `INSTANTIATIONS` list, citing C26.B's `audit_sha256=36f6bc2900d2120e...`; (b) retract §VII.P-prime from `PREDICTED_INSTANTIATIONS`, citing C26.A's `audit_sha256=4bb07af6099e138f...`; (c) write the corresponding theorem-grade entry in `sessions/permanent-results-registry.md` for §VII.K-DUAL-q with full provenance; (d) audit the mother-theorem's family count (3→4 verified, 2→0 predicted).

**Why it's worthwhile**: The W9 synthesis explicitly defers this to S87 W0 (carry-forward `S87-W2-2-VII-K-DUAL-Q-PROMOTION`, effort 1h, registry-write only). It is mechanical but load-bearing — without it, the registry lags reality, downstream gates citing §VII.K-DUAL-q as VERIFIED would be technically citing a forward-pointer. Per CLAUDE.md "no technical debt" and `feedback_fix-in-session-never-defer.md`: registry-write hygiene that fixes a known state mismatch should not wait. The S86 W9 close left this open ONLY because the registry-write is canonically a W0 wave activity. If S87 W0 absorbs this trio (promotion + retraction + permanent-results write), the W2-2 mother-theorem reaches its first stable post-S85 state.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (owns the W2-2 family across S85-S86)

**Rounds (workshops only)**: n/a (solo)

**Context the workshop will need**:
- W2-2 mother-theorem source: `s85_w2_theorem_family.py` (the `INSTANTIATIONS` and `PREDICTED_INSTANTIATIONS` blocks)
- Verifying SHAs (from W9 verdict file lines 164-167): C26.B `audit=36f6bc2900d2120e...`, C26.A `audit=4bb07af6099e138f...`
- Permanent-results registry pattern: see `sessions/permanent-results-registry.md` for prior §VII.J / §VII.K / §VII.N entries (the 3 already-verified instantiations) as templates
- Cross-reference: the W9 synthesis table at lines 549-552 shows S85→S86 family count delta (3→4 verified, 2→0 predicted) — that table is the closure ledger this gate must match

---

### Candidate 4 — Parity-grading orthogonality theorem (cross-W9 structural synthesis)

**What it would do**: Convert the cross-W9 observation — that C26.A + C24 §VII.P-v2 both failed because predicted lifts lived in the wrong parity slot, while C26.B + §VII.P' both passed because they lived in correctly-populated slots — into a registered structural theorem of the form "for the substrate's spectral-triple A_F = ℂ ⊕ ℍ ⊕ M₃(ℂ), HP_*(A_F^q) decomposes parity-orthogonally as (HP^even non-vanishing, 4 buckets, integer-rigid) ⊕ (HP^odd vanishing on semisimple/ℂ); refinements of corridor equivalence relations must respect this orthogonality (a HP^k separator can only distinguish corridors whose distinguishing class lives in HP^k of the same parity)." This is a synthesis-grade landing that captures the underlying constraint pattern that W9 surfaced four times.

**Why it's worthwhile**: The W9 cross-gate consistency note (lines 569-571) already articulates the pattern verbally but does not register it as a theorem. Two of the four W9 gates failed at HP-degree-mismatch, both pre-determined by S85 closure material — meaning future predicted instantiations of the W2-2 family will continue to fail at this pattern UNLESS it is registered as an explicit constraint at plan-authorship time. Registering it would (a) prevent S87+ plan authors from instantiating new HP^odd predictions on semisimple A_F, (b) prevent HP^k separators from being proposed for corridor classes whose distinguishing data live in HP^{k±1}, (c) provide the §VII-family with an explicit parity constraint axis. Effort is medium (one synthesis-grade write-up + one registry write). This is exactly what the `.claude/rules/teammate-behavior.md` "structural insight registration" pattern is for.

**Type**: solo (2 agents)

**Suggested agents**: connes-ncg-theorist + lizzi-spectral-functional-theorist (the two NCG-cohomology owners; their joint signature is appropriate for a parity-grading theorem)

**Rounds (workshops only)**: n/a (parallel solo writes against shared theorem source; consolidator merges)

**Context the workshop will need**:
- Source verdicts (all four): C26.A FAIL, C26.B PASS, C24 (False, True), C44 FAIL — with audit_sha256 pins as listed in W9 §616 verdict file appendix
- Algebraic substrate: Connes 1985 §II Cor.4 (HC^k of ground field vanishes in odd degree), Loday Cyclic Homology Thm 1.4.4 (Morita invariance), Wedderburn structure theorem (any finite-dim semisimple over ℂ is a sum of matrix algebras), Klimyk-Schmüdgen §6 (Hopf-deformation rigidity of parity grading), Lizzi Corollary E (HP¹ difference has zero image in HP^even)
- Pre-registered theorem statement: must articulate (i) HP^odd vanishing on A_F^q semisimple/ℂ for q ∈ (0, 1], (ii) HP^even integer-rigid 4-bucket structure, (iii) constraint on corridor-equivalence refinements (HP^k separator must match parity of distinguishing class)
- Suggested permanent-results slot: §VII.W (next available letter after §VII.V, the §VII.R reslot from S86 W1a)
- Cross-reference target for plan-author guard: `_plan_author_audit.py` would gain a check "for any predicted HP^k instantiation, verify k matches the parity of the distinguishing structure"

---

### Candidate 5 — D_K cache reconstruction infrastructure precedent (W9 substrate gate)

**What it would do**: Codify the cache-reconstruction protocol implicitly introduced by C44's method substitution. The C44 §11 carry-forward (a) demands `computations/cache/dk_spectrum_L{10,8}.npz` reconstruction, with a rough effort estimate of 8-12h. This candidate breaks that into the precondition gate: a clean rebuild of the D_K eigenvalue cache at L_max ∈ {8, 10}, validated against canonical-constants pins (e.g., `M_KK`, `Vol_SU3`, the existing eigenvalue-spectrum-derived constants), with full provenance (Peter-Weyl truncation parameters, Jensen deformation `tau_fold` value, GPU/CPU path documentation). Output is the cache + a validation script + a reusable cache-loader utility for future Mellin-density gates.

**Why it's worthwhile**: Two precedents converge here. (1) C44's method substitution was unforced once but should not become a recurring crutch — Mellin-density-based gates are likely to recur (the canonical-constants `mellin_f_star_f0/f2/f4` exist; future criterion tests in §VII.S family will need the cache). (2) C24's first-documented cross-session-deleted-artifact recovery (line 577) shows the project HAS the mechanical machinery for cache restoration via `git ls-tree` + `git cat-file -p` against historical commit blobs — but the D_K cache may not exist in any prior commit, in which case it must be re-derived from canonical machinery rather than restored. Establishing the cache reconstruction protocol BEFORE candidate 1 above prevents candidate 1 from diverging into an ad-hoc cache-build subtask. This is also a CLAUDE.md "fix in-session, never defer" instance: the missing cache is a structural debt the project incurred at S86 W9; carrying it forward without the reconstruction protocol postpones a recurring problem.

**Type**: solo (1 agent)

**Suggested agents**: connes-ncg-theorist (owns the D_K Peter-Weyl machinery) — alternatively a fresh-eyes pick of the gen-physicist if connes is loaded with candidates 2 and 3.

**Rounds (workshops only)**: n/a (solo)

**Context the workshop will need**:
- Cache-reconstruction precedent: C24 §C24 GV-blob recovery pattern (line 237 of WP) — `git ls-tree b9b3394 -- ...` to locate, `git cat-file -p <blob_sha> > <path>` to restore. This works only if the file existed in some prior commit.
- D_K canonical machinery: Peter-Weyl truncation at L_max=10 yielding ~155,984 eigenvalues; Jensen deformation parameter `tau_fold` from canonical_constants; SU(3) volume `Vol_SU3`; the relevant generator script likely lives in computations/_shared or its archive (S52+ if the cache is post-S52, computation-archive S7-S51 otherwise).
- Validation pins: existing canonical-constants entries that are spectral-derived (e.g., `c_Gold`, `c_fabric` if they trace to D_K spectral moments) provide round-trip validation.
- Pre-registered acceptance: cache reconstructs to bit-exact match against any existing prior cached version (if a prior version exists in git history); else, validation by canonical-constant round-trip.
- Output target: `computations/cache/dk_spectrum_L{8,10}.npz` plus `computations/_dk_cache_loader.py` reusable utility.
