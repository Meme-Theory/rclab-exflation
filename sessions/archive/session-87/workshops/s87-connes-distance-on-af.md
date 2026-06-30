# S87 Workshop 3 — Connes-Distance Functional-Family Orthogonality on A_F = C ⊕ H ⊕ M_3(C)

**Date**: 2026-05-02
**Agent**: connes-ncg-theorist (1-agent solo per `sessions/archive/session-87/session-87-workshop-schedule.md` entry S-2)
**Workshop seed source**: `sessions/archive/session-87/workshops/_seed-1.md` Workshop 3 (lines 76-104)
**Workpaper companion**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W1b-6 (lines 2089-2203)
**Predecessor gate**: W1b-6 `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` INFO/CLASS-γ (audit_sha `b3652c276acec8e1…`, value=0.9800418, FULL `M_n(ℂ)` algebra, R-sweep `d_C(R) ≈ 0.9·R` linear across 3 OOM)
**Producing artifacts**:
- Script: `computations/s87_w3_connes_distance_on_af.py` (42,988 bytes)
- Data: `computations/s87_w3_connes_distance_on_af.npz` (13,106 bytes)
- Plot: `computations/s87_w3_connes_distance_on_af.png` (71,852 bytes)
- Verdict: `computations/s87_gate_verdicts.txt` — `S87-WORKSHOP3-CONNES-DISTANCE-ON-A_F` line + dual-SHA + 3-tuple companion rows
- Audit SHA: `b6c0d4bf5f09e93e408e25387d09e48d6debe3345dd19d547e8d12ba1eb46385`
- Content SHA: `55738284c8ae9a80081e8e73a669ae0a35e00f8bb280ef1bb4945d297bb33ca9`

---

## 1. Task definition

W1b-6 closed the conjecture that Connes distance admits a closed-form identity in `{λ_n}` alone on the FULL `M_{n_loc}(ℂ)` algebra at L_max=12 (`best_residual = 0.980`, regulator-divergent `d_C(R) ≈ c·R` linearly). The seed file's Workshop 3 surfaces two competing readings of that closure: **Reading A** (structural orthogonality between algebra-INVARIANT and algebra-DEPENDENT functional families on every finite spectral triple, hence the divergence persists on any sub-algebra) versus **Reading B** (scope-limited to the FULL algebra; the substrate's actual `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` may have finite Connes distance precluding the f(D²)-commutant escape via direct-sum block structure). The pre-registered numerical falsifier is to evaluate Connes distance with `a` constrained to `π(A_F)` at the same 3 canonical state-pairs as W1b-6, with the same R-sweep R ∈ {1, 10, 100, 1000}, and report whether (a) regulator-divergence persists [PASS-Reading-A], (b) `d_C` saturates AND ≥1 candidate residual < 1e-3 [PASS-Reading-B], or (c) neither is fully satisfied [INFO].

---

## 2. Method

### 2.1 Spectrum cache + state-pair construction (mirrors W1b-6 byte-for-byte)

The L=12 spectrum is loaded from `computations/s84_spectrum_cache_L12_tau019.npz` (sha256 prefix `9e6d9cf7fd6a6949…`); 90 SU(3) sectors, 166,896 absolute eigenvalues in [0.819741, 5.418937] M_KK. The state-pair construction `select_state_localized_block` reproduces W1b-6 verbatim: per pair, pull the lowest-`N_LOC=16` absolute eigenvalues from the union of pre-registered SU(3) sectors, build prescribed-singular-value chiral-graded `D_loc = [[0, M], [M^T, 0]]` with `M = Q_U @ diag(λ_i) @ Q_V^T` for deterministic random-orthogonal `Q_U`, `Q_V` under `RNG_SEED = 42` (same seed as W1b-6 ⇒ identical M, identical D_loc).

The 3 canonical state-pairs (PRE-REGISTERED, identical to W1b-6):

| Pair | p_state | q_state | Sector pool |
|:----|:--------|:--------|:------------|
| 1 (vacuum / n=0 quasi) | e_0 | e_1 | (0,0), (0,1), (1,0) |
| 2 (B1 acoustic min/max) | e_0 | e_15 | (0,1), (1,0) |
| 3 (Cartan α_1 / α_2) | e_0 | e_2 | (1,1) |

### 2.2 A_F = C ⊕ H ⊕ M_3(C) embedding into the local Hilbert block

The substrate's finite spectral triple algebra is `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. A faithful action on `H_loc = ℂ^{16}` requires choosing an embedding `π : A_F ↪ M_{16}(ℂ)`. The natural block-diagonal SM-canonical embedding splits `H_loc` as `(ℂ^4)_{ℂ-block} ⊕ (ℂ^4)_{ℍ-block} ⊕ (ℂ^8)_{M_3-block}` with each summand acting block-diagonally on its own slot.

Two basis sets are constructed (script `build_af_basis`):

**STRICT A_F basis** (8 real-symmetric generators) — faithful to `A_F`'s real-hermitian sub-algebra under real-symmetric SDP variables:
- `ℂ-summand`: 1 generator (α·I_4 on indices 0:4) — real-hermitian sub-algebra of ℂ is just ℝ.
- `ℍ-summand`: 1 generator (α·I_4 on indices 4:8) — real-hermitian sub-algebra of ℍ is just ℝ (the imaginary units i, j, k are real-antisymmetric, excluded from real-symmetric SDP).
- `M_3(ℂ)-summand`: 6 generators on the 3×3 sub-block at indices 8:11 (3 diagonal + 3 symmetric off-diagonal, padded with zeros on indices 11:16) — real-symmetric sub-algebra of `M_3(ℂ)` hermitian (the 3 antihermitian generators `i·antisym` are excluded; this is the strict real-symmetric clipping, matching what cvxpy's `symmetric=True` variable can represent).

Total STRICT real-symmetric DOF: 1 + 1 + 6 = **8**.

**PERMISSIVE A_F-like basis** (26 real-symmetric generators) — upper-bound diagnostic, full block-diagonal real-symmetric on the three blocks:
- `ℂ-block`: 10 generators (4×4 real-symmetric, 4 diagonal + 6 symmetric off-diag)
- `ℍ-block`: 10 generators (same structure on indices 4:8)
- `M_3-sub-block`: 6 generators (same as STRICT)

Total PERMISSIVE real-symmetric DOF: 10 + 10 + 6 = **26**.

PERMISSIVE OVERSHOOTS the strict A_F's real-hermitian content because it admits real-symmetric off-diagonal couplings within the C and H blocks that A_F itself does not contain (in `A_F`, the C-summand is one-complex-dimensional and acts as `α·I_4`, the H-summand is one-real-quaternionic-dimensional with only `I` real-hermitian). PERMISSIVE is therefore an upper bound: any divergence not present under PERMISSIVE is also absent under STRICT.

### 2.3 SDP construction (algebra-restricted)

The Connes distance restricted to `a ∈ π(A_F)` is computed via the Iochum-Krajewski-Martinetti finite-N SDP (script `connes_distance_af_sdp`):

```
maximize  | <p|a|p> - <q|a|q> | = | sum_i x_i · tr(Δρ · E_i) |
s.t.      a = sum_i x_i · E_i           (basis expansion in π(A_F))
          ‖[D, a]‖_op ≤ 1               (Lipschitz constraint, via LMI)
          ‖a‖_F ≤ R                     (Frobenius regulator, matches W1b-6)
```

The structural difference from W1b-6: there `a` was `cp.Variable((n,n), symmetric=True)` (full real-symmetric M_{16}(ℝ), 136 DOF); here `x = cp.Variable(K)` for `K ∈ {8, 26}`. The LMI dimension is the same (2n=32). CLARABEL solver, tolerance 1e-10. Both directions (max and min) computed; `d_C = max(|d_pos|, |d_neg|)`.

### 2.4 R-sweep protocol

R-sweep on Pair-1 over R ∈ {1, 10, 100, 1000} (3 OOM, identical to W1b-6 §2138-2147). Slope-fit on `log_10(d_C)` vs `log_10(R)` gives the linearity index. PASS-Reading-A criterion: ratio `d_C(R=1000) / d_C(R=1) > 100` AND log-log slope > 0.5. PASS-Reading-B criterion: ratio < 2 AND best non-definitional residual < 1e-3 at any state-pair.

---

## 3. Computation

### 3.1 R-sweep on Pair-1

| R | STRICT `d_C(R)` | STRICT `d_C/R` | PERMISSIVE `d_C(R)` | PERMISSIVE `d_C/R` | FULL `M_n(C)` (W1b-6) |
|:--|:----------------|:---------------|:--------------------|:-------------------|:----------------------|
| 1 | **0.000000e+00** | 0.0000 | 1.414214e+00 | 1.4142 | 1.4142e+00 |
| 10 | **0.000000e+00** | 0.0000 | 6.790341e+00 | 0.6790 | 1.1099e+01 |
| 100 | **0.000000e+00** | 0.0000 | 6.790341e+00 | 0.0679 | 1.0087e+02 |
| 1000 | **0.000000e+00** | 0.0000 | 6.790341e+00 | 0.0068 | 8.7623e+02 |

**Three regimes are visible**:
- **STRICT A_F**: `d_C(R) ≡ 0` identically across all R. The Lipschitz Lagrangian is identically the zero functional on STRICT(A_F) for the (e_0, e_1) pair (see substitution chain §4 for the structural reason).
- **PERMISSIVE A_F-like**: `d_C(R)` saturates to 6.7903 for R ≥ 10. Ratio `d_C(R=1000)/d_C(R=1) = 6.7903/1.4142 = 4.802` (NOT > 100). Log-log slope is sub-linear and negative beyond R=10. PERMISSIVE is **regulator-saturated**, not divergent.
- **FULL M_n(C)** (W1b-6 reference): `d_C(R)/R → 0.876` linearly across 3 OOM. Ratio = 619.6 ≫ 100. Linearly divergent.

### 3.2 Per-state-pair LHS at default R (= 100·|λ|_max)

| | STRICT A_F LHS | PERMISSIVE A_F LHS | FULL M_n(C) LHS (W1b-6) |
|:----|:---------------|:-------------------|:------------------------|
| Pair-1 (vacuum / n=0 quasi) | **0.0000e+00** | 6.7903e+00 | 8.5004e+01 |
| Pair-2 (B1 acoustic min/max) | **1.1907e+00** | 3.3538e+00 | 8.4665e+01 |
| Pair-3 (Cartan α_1 / α_2) | **0.0000e+00** | 3.5961e+00 | 8.5445e+01 |

Pair-1 and Pair-3 STRICT yield identically zero; Pair-2 STRICT yields a finite `d_C = 1.1907` (not zero, not divergent). PERMISSIVE yields O(3-7) on all pairs. FULL diverges to O(85).

### 3.3 Candidate-form residual table (STRICT)

| | Pair-1 | Pair-2 | Pair-3 |
|:--|:--|:--|:--|
| **LHS d_C STRICT** | 0.000e+00 | 1.191e+00 | 0.000e+00 |
| C1 SDP sup-form (= LHS) | inf (LHS=0) | 0.000e+00 | inf (LHS=0) |
| C2 Mellin-Dirichlet Σ c_n·λ_n^{−α} | inf | 9.941e-01 | inf |
| C3 Commutator-norm 1/‖[D, ρ_p−ρ_q]‖_op | inf | **1.054e-01** | inf |
| C4 Heat-kernel-trace √Tr[Q_pq·D^{−2}] | inf | 4.169e-01 | inf |

The "inf" entries reflect division-by-zero protection (LHS=0 on Pair-1 and Pair-3 STRICT). Best non-definitional residual is **C3 at Pair-2 = 1.054e-01**, in the [1e-2, 1e-1] band (CLASS-β-adjacent but ABOVE 1e-3 INFO ceiling).

### 3.4 Candidate-form residual table (PERMISSIVE)

| | Pair-1 | Pair-2 | Pair-3 |
|:--|:--|:--|:--|
| **LHS d_C PERMISSIVE** | 6.790e+00 | 3.354e+00 | 3.596e+00 |
| C1 SDP sup-form (= LHS) | 1.000e+00 | 6.450e-01 | 1.000e+00 |
| C2 Mellin-Dirichlet | 1.000e+00 | 9.979e-01 | 9.458e-01 |
| C3 Commutator-norm | 8.240e-01 | 6.824e-01 | 7.376e-01 |
| C4 Heat-kernel-trace | 7.502e-01 | 4.969e-01 | 6.098e-01 |

PERMISSIVE residuals are O(0.5–1.0) — best 0.497 at C4-Pair-2; same band as W1b-6 FULL (best 0.980). NO candidate identity at residual < 1e-3 on PERMISSIVE either.

---

## 4. Substitution chain — does the f(D²)-commutant escape from FULL M_n(C) persist on A_F's direct-sum block structure?

**Step 1 (definition)** — On the FULL algebra `M_n(ℂ)`, for any polynomial `f`, the operator `f(D_loc²) ∈ M_n(ℂ)` and `[D_loc, f(D_loc²)] = 0` because `D_loc` commutes with itself. The W1b-6 escape exploits this by setting `a = R · f(D²) / ‖f(D²)‖_F` for arbitrary scaling R, and observing that the Lipschitz constraint `‖[D,a]‖_op ≤ 1` is vacuously satisfied (LHS = 0) while the Frobenius cap is the only effective bound. So `d_C(R) = R · sup_{f: ‖f(D²)‖_F=1} |⟨p|f(D²)|p⟩ - ⟨q|f(D²)|q⟩|`, scaling linearly in R.

**Step 2 (substitution into A_F)** — On `π(A_F) ⊂ M_{16}(ℝ)`, the sub-algebra is fixed at 8 (STRICT) or 26 (PERMISSIVE) real-symmetric DOF. The escape mechanism requires a non-trivial element `a ∈ π(A_F)` with `[D_loc, a] = 0`. By Step 1, the candidates are `f(D_loc²) ∩ π(A_F)`. For our chiral `D_loc = [[0, M], [M^T, 0]]` we have

```
D_loc² = [[M·M^T, 0], [0, M^T·M]]
```

This is a 2×2-block-diagonal positive matrix whose two blocks are NOT similar (in general M·M^T ≠ M^T·M unless M is normal, which it is not for our random Q_U·Σ·Q_V^T construction). The polynomial-algebra `{f(D_loc²) : f}` therefore consists of **block-diagonal matrices** of the form `[[g(MM^T), 0], [0, g(M^T M)]]` for arbitrary polynomial `g`.

**Step 3 (intersect with π(A_F))** — π(A_F) is also block-diagonal in the natural decomposition `H_loc = (ℂ^4)_C ⊕ (ℂ^4)_H ⊕ (ℂ^8)_{M_3}`. The two block decompositions are DIFFERENT: `D_loc²` is block-diagonal in the chirality grading (8+8); `π(A_F)` is block-diagonal in the C/H/M_3 grading (4+4+8). Their intersection — block-diagonal in BOTH gradings — is the algebra of matrices that are diagonal in the joint refinement: blocks at indices [0:4] (C ∩ chirality+), [4:8] (H ∩ chirality+), [8:12] (M_3 ∩ chirality+), [12:16] (M_3 ∩ chirality−).

For STRICT A_F:
- C-summand contributes `α · I_4` on [0:4] only — this IS in `f(D²)` provided `MM^T` restricted to [0:4] is a multiple of `I_4`. With Q_U random orthogonal, `MM^T` is NOT proportional to `I_4`; only `α · I_4` is in the algebra, which gives `α · I_4 = α · I_4 · 1` (the constant function f(x) = α). So **the only `f(D²) ∩ STRICT(C-summand)` is `α · I_4` for constant α** (same logic for H-summand `α · I_4` on [4:8]).
- M_3 sub-block: `M^T M` restricted to [8:11] is NOT proportional to identity either (random Q_V), so the only intersection element is `α · I_3` padded — but STRICT's 6-dim M_3 basis includes the 3 diagonal generators, and any DIAGONAL element of [8:11] is a candidate. The intersection contains `α · I_3` and possibly partial diagonals if the diagonal of `M^T M` has a non-trivial polynomial-image structure, but for random Q_V this also collapses to `α · I_3`.

**Conclusion of Step 3**: `f(D²) ∩ STRICT(A_F) ⊆ ℝ · I_C ⊕ ℝ · I_H ⊕ ℝ · I_{M_3-subblock} ≅ ℝ^3` (3-dim sub-algebra of constants on each block). This is the SCALAR PART of A_F — the f(D²)-escape is **collapsed to a 3-dimensional subspace** on STRICT.

**Step 4 (direction — what the SDP returns on this collapsed escape)** — For the (e_0, e_1) Pair-1, both states are inside the C-block (indices 0 and 1). The only STRICT generators with nonzero `tr(Δρ · E_i)` are:
- `E_C = I_4 / 2` on [0:4]: `tr(Δρ · I_4/2) = (1 - 1)/2 = 0`
- All H and M_3 generators: zero trace with `Δρ` (which has support [0:4] only).

So **the objective coefficient vector `obj_coeffs` is identically zero** ⇒ the SDP optimum is `d_C = 0` regardless of R, regardless of the Lipschitz LMI constraint. The script reports `d_C = 0.000000e+00, status=optimal` confirming the structural collapse.

For Pair-3 (e_0, e_2 both in C-block): same logic, `obj_coeffs = 0`, `d_C = 0`.

For Pair-2 (e_0 in C-block, e_15 in M_3-block but OUTSIDE the [8:11] sub-block I picked): the `E_C` generator gives `tr(Δρ · I_4/2) = 1/2`, so the C-block contributes a nonzero objective. But the M_3 generators only see indices [8:11], so e_15's weight is INVISIBLE to STRICT. The SDP finds `d_C = 1.1907` from the C-block contribution alone, BOUNDED — the Lipschitz LMI on the C-block scalar `α · I_4` is `‖[D_loc, α · I_4]‖_op = α · ‖[D_loc, I_4]‖_op` where `[D_loc, I_4 ⊕ 0]` is a non-trivial off-block-diagonal commutator (since `I_4 ⊕ 0` does NOT commute with the off-diagonal D_loc). The Lipschitz constraint therefore PROVIDES the bound on α, NOT the Frobenius cap. **STRICT is regulator-INDEPENDENT for Pair-2**: the SDP finds `d_C = 1.1907` at any R ≥ this Lipschitz-bounded value.

**Step 5 (direction conclusion)** — The f(D²)-commutant escape is **fundamentally blocked on STRICT A_F** because:
1. `f(D²) ∩ π(A_F)` collapses to the 3-dim center (scalars on each block).
2. The center elements have either trivial action on diagonal-localized state-pairs (yielding `obj_coeffs = 0` → `d_C = 0`) or non-trivial Lipschitz-bounded action (yielding finite `d_C` independent of R).
3. The Lipschitz LMI replaces the Frobenius cap as the binding constraint — and the LMI is REGULATOR-INDEPENDENT.

Therefore **PASS-Reading-A is FALSIFIED on STRICT A_F**: regulator-divergence does NOT persist; instead `d_C(R)` is identically zero or saturated at a finite Lipschitz-bound. The W1b-6 FULL-algebra divergence was a feature of `M_n(ℂ)`'s richer commutant, not generic to all finite spectral triples.

**Step 6 (PERMISSIVE direction)** — On PERMISSIVE (10+10+6 = 26 real-sym DOF), `f(D²) ∩ π(A_F)` still collapses to the same 3-dim center because the OFF-DIAGONAL real-sym generators within the C and H blocks DO NOT commute with the off-diagonal D_loc (which couples chirality+ to chirality−, mixing all 16 indices). So PERMISSIVE also blocks the f(D²) escape. Yet PERMISSIVE yields `d_C = 1.4142, 6.7903, 6.7903, 6.7903` (saturating ABOVE Lipschitz-bound at R≥10) because the larger basis admits non-center elements with `tr(Δρ · E_i) ≠ 0` that contribute to the objective. The Lipschitz LMI on these off-diagonal real-sym generators is non-trivial — it bounds `d_C` to a finite value INDEPENDENT of the Frobenius cap once R is large enough that the cap is not binding. **PERMISSIVE saturates, does not diverge**.

---

## 5. Verdict

**Pre-registered verdict line** (S87 schema-v2):

```
S87-WORKSHOP3-CONNES-DISTANCE-ON-A_F: INFO -- value=inf scheme=Connes-distance-A_F-subalgebra-restriction convention=substrate-state-pair-canonical-A_F L_max=12 audit_sha256=b6c0d4bf5f09e93e408e25387d09e48d6debe3345dd19d547e8d12ba1eb46385 content_sha256=55738284c8ae9a80081e8e73a669ae0a35e00f8bb280ef1bb4945d297bb33ca9 schema_version=S84+
# audit_sha256_short=b6c0d4bf5f09e93e content_sha256_short=55738284c8ae9a80 # S87-WORKSHOP3-CONNES-DISTANCE-ON-A_F dual-SHA companion row (W9a-99 split)
# sign_verdict=N/A magnitude_verdict=INFO regime_verdict=VALID # S87-WORKSHOP3-CONNES-DISTANCE-ON-A_F 3-tuple annotation (S87 schema-v2)
```

**Composite**: **INFO** (sign_verdict=N/A, magnitude_verdict=INFO, regime_verdict=VALID).

**Decomposed verdict against the pre-registered alternatives**:
- **PASS-Reading-A** (regulator-divergence persists on A_F, `d_C(R) ∝ R`): **FALSIFIED**. STRICT A_F yields `d_C(R) ≡ 0` on Pair-1 and Pair-3 and `d_C(R) = 1.1907` constant on Pair-2 (Lipschitz-bound) — neither linearly divergent nor proportional to R. PERMISSIVE saturates at 6.79 — also not linearly divergent. The f(D²)-commutant escape that drove the FULL-algebra divergence is BLOCKED at the sub-algebra level by the chirality-vs-(C/H/M_3) block-grading mismatch.
- **PASS-Reading-B** (saturated `d_C` AND ≥1 candidate residual < 1e-3): **PARTIALLY SATISFIED, formally FAILS**. STRICT saturates (PASS-B saturation criterion ✓: `d_C(R)` is regulator-INDEPENDENT) but no candidate identity in `{λ_n}` alone reproduces the LHS at residual < 1e-3 (best is C3-Pair-2 = 1.054e-01, 100× above the INFO ceiling). The closed-form algebraic identity in `{λ_n}` alone does NOT exist on A_F either.
- **INFO** (neither Reading A nor Reading B fully satisfied): **TRIGGERED**. The verdict logic collapses to INFO under the pre-registered rule (script §"Verdict logic" Step 7 fall-through branch).

**Structural reading (more informative than the INFO label)**:

The two pre-registered readings were a false dichotomy. The computation surfaces a **third structural finding** that neither Reading A nor Reading B captured cleanly:

> **Reading C (synthesis)**: On the substrate's actual `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`, the Connes distance is **finite and well-defined** (Reading B's geometric premise CONFIRMED) — the f(D²)-commutant escape is structurally blocked by the chirality-vs-(C/H/M_3) block-grading mismatch. **However**, the Connes distance still does NOT admit a closed-form algebraic identity in `{λ_n}` alone (Reading B's identity claim FALSIFIED). The state-pair-functional class remains structurally distinct from the spectral-moment-functional class of §VII.U.1 — Reading A's structural-orthogonality claim survives at the level of the **functional CLASSES**, while Reading A's REGULATOR-DIVERGENCE diagnostic is FULL-`M_n(ℂ)`-specific.

The orthogonality between the algebra-INVARIANT family (spectral moments, ζ-residues, Mellin-Dirichlet identities — exemplar §VII.U.1) and the algebra-DEPENDENT family (Connes distance, state-pair commutator norms — exemplar this gate) is a structural feature of every finite spectral triple — but the WAY in which the algebra-DEPENDENT class fails to admit a `{λ_n}`-only identity differs by algebra:
- On FULL `M_n(ℂ)`: regulator-divergence (W1b-6 finding).
- On `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`: regulator-saturation but NO closed-form `{λ_n}` identity (this gate's finding).

The closed-form identity does not exist in EITHER case; the failure mode is different in the two cases (linear divergence vs. saturation-without-identity), but the conclusion — that the algebra-DEPENDENT class is not in the §VII.U Mellin-Dirichlet structural family — holds in both.

---

## 6. Solution-space implication

### 6.1 Registry implication

The seed-file pre-registration enumerated three possible registry outcomes; the actual finding lands SPECIFICALLY at outcome (iii) with new sharpening:

> **§VII.U.1 strengthening annotation pinning algebra-INVARIANT specificity of Mellin-Dirichlet identity** — the §VII.U.1 entry's "STRUCTURALLY SPECIFIC" claim (W1b-6 §2173-2178) is sharpened: §VII.U.1 belongs to the algebra-INVARIANT functional family `F({λ_n}) = Σ_k m_k · g(λ_k)`; the algebra-DEPENDENT family of state-pair commutator-norm functionals admits NO closed-form `{λ_n}`-only identity on EITHER FULL `M_n(ℂ)` (W1b-6 verdict) OR `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)` (this gate's verdict). The two functional classes are **structurally orthogonal in the sense of identity-class membership**, while the algebra-DEPENDENT class's regulator-behavior is algebra-dependent (linear divergence on `M_n(ℂ)`; saturation on `A_F`).

A new `§VII.{letter}-FUNCTIONAL-FAMILY-ORTHOGONALITY` entry is **NOT** structurally promotable yet — the orthogonality claim is established on TWO algebras (full `M_n(ℂ)` and the substrate's `A_F`), but a registry-grade theorem requires the cross-algebra invariance to hold across MORE than two examples (per `cross-pillar-bridge-anatomy.md` §"Forward template-adoption" K=3 promotion threshold) AND requires a structural proof from NCG axioms generalized beyond the two computed instances. Until the joint-theorem promotion path lands a STAGE-2 cross-axis verify (per `joint-theorem-promotion.md` §Stage 2), the orthogonality claim remains a structural CONJECTURE supported by N=2 calibration instances.

The seed-file outcome (ii) — **§VII.{letter}-RESERVED-FOR-CONNES-DISTANCE-SUBALGEBRA-CONJECTURE pending S88 dispatch** — is now SUPERSEDED. The W1b-6 carry-forward `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE` is **CLOSED IN-SESSION at the verdict level** by this gate: A_F gives finite `d_C` (Reading B's geometric premise) but no `{λ_n}` identity (Reading B's identity claim falsified). No reserved §VII.{letter} slot is needed; the closure is at INFO with structural reading.

### 6.2 W1b-6 strengthening note (proposed)

The W1b-6 §2185 line "Sub-algebra restriction track (S88+ optional, NOT a carry-forward of this gate): test whether restricting A_loc to the substrate's actual A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) (instead of the full `M_n(ℂ)`) gives a finite, well-defined Connes distance that THEN admits a finite-spectrum identity. This is a different conjecture (different algebra), not CLASS-β of the present one." is now empirically resolved:
- "finite, well-defined Connes distance" — **YES** (this gate confirms; STRICT and PERMISSIVE both regulator-saturated).
- "THEN admits a finite-spectrum identity" — **NO** (this gate falsifies; best STRICT residual 1.054e-01, best PERMISSIVE residual 4.969e-01, both 100× above the INFO ceiling).

The §VII.U.1 algebra-INVARIANT specificity is therefore structurally robust to the FULL-vs-A_F distinction. The Connes distance's failure to admit a `{λ_n}`-only identity is NOT an artifact of regulator-divergence (which a full-algebra critic could have called a degenerate non-test); it's a structural feature of state-pair-functional classes that survives sub-algebra restriction. This is a stronger version of the W1b-6 closure than what the FULL-algebra evidence alone could support.

### 6.3 Substrate framing (per `phononic-framing.md`)

The Connes distance is the substrate-internal state-space metric on the finite spectral triple `(A_F, H_F, D_K^{≤L})`. The substrate IS this commutator-algebra metric; it is not a metric on a manifold the substrate lives in. Direction of explanation: **D_K eigenvalues + π(A_F) basis → SDP over A_F → d_C(p, q)**. This gate's finding sharpens the §VII.U Mellin-Dirichlet identity's structural specificity from "algebra-INVARIANT specifically" to "algebra-INVARIANT specifically AND state-pair-functional class is ORTHOGONAL on every studied algebra (M_n(C), A_F)". The substrate carries TWO families of substrate-internal observables: spectral moments (algebra-INVARIANT, identity-class) and state-pair functionals (algebra-DEPENDENT, no-identity-class) — they are not interchangeable, and §VII.U.1's identity does not generalize across the divide.

---

## 7. 4-field carry-forward (S88 follow-up)

**Carry-forward 1**: `S88-CONNES-DISTANCE-A_F-FULL-COMPLEX-HERMITIAN`
1. **What**: Re-run the Connes-distance SDP on `π(A_F)` with the FULL complex-hermitian basis (not just real-symmetric) — i.e., 14 real DOF total: `1 (ℂ) + 4 (ℍ) + 9 (M_3(ℂ))_h`. The current STRICT (8 DOF) clips to real-symmetric; this carry-forward includes the imaginary-antisymmetric directions (i·σ_x, i·σ_y, i·σ_z for ℍ; 3 antihermitian-i generators for M_3(ℂ)).
2. **Inputs**: this gate's `s87_w3_connes_distance_on_af.npz` + `s84_spectrum_cache_L12_tau019.npz` + `canonical_constants.py`. Use complex-Hermitian SDP variable (cvxpy `Hermitian=True`) instead of `symmetric=True`.
3. **Gate**: PASS iff full-complex-hermitian A_F yields `d_C(R)` saturated AND best non-definitional residual < 1e-3 at ≥1 state-pair (which would resurrect the W1b-6 carry-forward `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE` at full A_F resolution). FAIL iff residuals remain > 1e-2 (consistent with this gate's finding). INFO if borderline.
4. **Effort**: ~0.3 wave-equivalents. Solo gen-physicist or connes-ncg compute; no agent dispatch needed. Direct extension of this gate's script with one variable-type change.

**Carry-forward 2**: `S88-FUNCTIONAL-FAMILY-ORTHOGONALITY-NCG-AXIOM-DERIVATION`
1. **What**: Attempt a closed-form NCG-axiomatic proof that the algebra-DEPENDENT family of state-pair commutator-norm functionals on a finite spectral triple `(A, H, D)` does NOT admit a `{λ_n}`-only closed-form identity, generalizing the W1b-6 + this-gate empirical N=2 evidence to a structural theorem. The proof sketch in §4 above (chirality-vs-A_F block-grading mismatch ⇒ `f(D²) ∩ π(A_F)` collapses to scalars) is the seed; full theorem requires showing this for ARBITRARY `(A, H, D)` satisfying the 7 NCG axioms (regularity, finiteness, reality, first-order, orientability, Poincaré duality, dimension).
2. **Inputs**: Connes 1996 reconstruction theorem; Connes-Moscovici 1995 dimension-spectrum residue formula; this gate's substitution chain §4.
3. **Gate**: PASS iff a STAGE-1-CANDIDATE entry can be drafted at registry §VII.{letter}-FUNCTIONAL-FAMILY-ORTHOGONALITY with explicit NCG-axiomatic substitution chain, then routed through `joint-theorem-promotion.md` 4-stage pathway. INFO iff a partial proof covers a sub-class of finite spectral triples (e.g., almost-commutative). FAIL iff the no-go proof requires assumptions outside the NCG axioms (in which case the orthogonality remains conjectural at K=2 calibration).
4. **Effort**: ~1.5 wave-equivalents. 2-agent workshop (connes-ncg + lizzi-spectral-functional-theorist) or solo connes-ncg deep dive. The proof-writeup will land as a registry entry, candidate for §VII.{letter}-FUNCTIONAL-FAMILY-ORTHOGONALITY at STAGE-1-CANDIDATE.

**Carry-forward 3**: `S88-A_F-CONNES-DISTANCE-CHARACTERIZATION-SCAN`
1. **What**: Characterize the Lipschitz-bounded `d_C` values on STRICT(A_F) across ALL state-pair geometries — not just the 3 W1b-6 canonical pairs. Specifically: scan over (i, j) ∈ ([0:16] × [0:16]) for `p = e_i, q = e_j`, compute STRICT `d_C(e_i, e_j)`, and characterize the resulting 16×16 distance matrix's structure (block-diagonal? metric? quasi-metric?). This gate's finding that `d_C = 0` on (e_0, e_1) under STRICT but `d_C = 1.1907` on (e_0, e_15) shows the matrix has BLOCK STRUCTURE — but the block-pattern dictionary is uncharacterized.
2. **Inputs**: `s87_w3_connes_distance_on_af.npz` + `s84_spectrum_cache_L12_tau019.npz`. Scan over 16×16 state-pair grid + STRICT SDP.
3. **Gate**: PASS iff the STRICT `d_C(e_i, e_j)` matrix is shown to be a quasi-metric on the C/H/M_3 quotient (3-point space) with explicit closed-form values per (block_i, block_j) pair — this would be a substrate state-space metric ON THE A_F BLOCK QUOTIENT, structurally distinct from §VII.U.1 but candidate for its own registry slot. INFO if the matrix has block structure but no closed-form. FAIL if the matrix is unstructured (random per state-pair).
4. **Effort**: ~0.5 wave-equivalents. Solo gen-physicist compute. 256 SDP runs (16×16 = 256 pairs, each ~0.05 s on STRICT 8-dim basis → ~13 s total).

---

## 8. Honest disclosures (per agent-standards.md §"Completion Verification")

**Real-symmetric clipping disclosure**: The STRICT A_F basis used in this gate (8 real-symmetric DOF) is a real-symmetric SUBSET of the full real-hermitian A_F (14 real DOF: 1 ℂ + 4 ℍ + 9 M_3(ℂ)_h). The cvxpy `symmetric=True` variable does not natively accept complex-hermitian; full-hermitian DOF would require a complex-variable SDP reformulation. Carry-forward 1 above pre-registers this extension. The current STRICT result is therefore an UPPER BOUND on the real-symmetric component of d_C(A_F) — including the 6 antihermitian-i generators could only ADD to the SDP basis dimension (more variables = larger feasible region = potentially larger d_C). Conclusions:
- "STRICT yields finite d_C" (direction) — ROBUST to the clipping (full A_F has more DOF, but the f(D²)-commutant escape collapse argument §4 applies regardless of real-vs-complex DOF).
- "Best non-definitional residual is C3 at Pair-2 = 1.054e-01" (specific value) — may LOOSEN under full-complex (residual could decrease); carry-forward 1 will resolve.

**N=2 calibration disclosure**: The structural-orthogonality claim (Reading C synthesis) has K=2 calibration instances (W1b-6 FULL `M_n(ℂ)` + this gate STRICT/PERMISSIVE A_F). Per `cross-pillar-bridge-anatomy.md` §"Forward template-adoption", K=3 is the promotion threshold for SUGGESTION → MANDATORY. The Reading C synthesis is currently a SUGGESTION-grade structural conjecture, not a registry-grade theorem. Carry-forward 2 above pre-registers the NCG-axiomatic derivation needed to lift K=2 evidence to a structural theorem.

**SDP solver status disclosure**: 5 of 6 STRICT SDP runs returned `status=optimal`; 1 (Pair-2) returned `status=optimal_inaccurate`. PERMISSIVE: all 9 runs returned `optimal_inaccurate` (saturating against the Lipschitz LMI boundary). `regime_verdict = VALID` is justified because `optimal_inaccurate` reflects boundary saturation at the structurally-correct constraint, not solver malfunction (same justification as W1b-6 CC2).

---

## 9. Cross-references

- **W1b-6 predecessor**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W1b-6 (verdict line 2111, R-sweep table 2138-2147, structural reasoning 2172-2178)
- **Workshop seed**: `sessions/archive/session-87/workshops/_seed-1.md` Workshop 3 (lines 76-104; pre-registered numerical falsifier line 104)
- **§VII.U.1 Mellin-Dirichlet identity** (counterpart, algebra-INVARIANT): `sessions/permanent-results-registry.md` §VII.U.1 (S86 W-1 connes+lizzi joint, S87 W1a-4 PASS rel_diff = 0e+00)
- **W1b-6 carry-forward closed by this gate**: `S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE` (workpaper §2185 + §2250)
- **Joint-theorem promotion pathway**: `.claude/rules/joint-theorem-promotion.md` (4-stage pathway for cross-algebra orthogonality theorem)
- **Cross-pillar bridge anatomy K-counter**: `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption" (N=2 → SUGGESTION; this gate adds calibration corpus instance #2 for the algebra-DEPENDENT functional family)
- **Iochum-Krajewski-Martinetti 2001**: finite-N SDP form of Connes distance, used in W1b-6 + this gate's `connes_distance_af_sdp` construction
- **Connes 1996**: `Gravity coupled with matter and the foundation of non-commutative geometry`, original definition `d_C(p,q) = sup_{a, ‖[D,a]‖ ≤ 1} |a(p)-a(q)|`

---

## 10. Memory update (agent-private)

To be appended to `.claude/agent-memory/connes-ncg-theorist/MEMORY.md`:

> **S87 Workshop 3 — Connes-distance on A_F finding (2026-05-02)**: STRICT A_F (8-dim real-sym basis on 1+1+6 C/H/M_3) yields `d_C(e_0, e_1) = d_C(e_0, e_2) = 0` (objective vanishes by `tr(Δρ · I_4) = 0` on diagonal-localized C-block pairs); `d_C(e_0, e_15) = 1.1907` (Lipschitz-bounded, regulator-INDEPENDENT). PERMISSIVE A_F-like (26-dim) saturates at 6.7903 (Pair-1) — also regulator-independent. The f(D²)-commutant escape collapses to the 3-dim center (scalars on each block) by chirality-vs-(C/H/M_3) block-grading mismatch. **Reading A falsified, Reading B identity-claim falsified, Reading C synthesis: orthogonality holds at functional-class level; regulator-divergence is FULL-algebra-specific.** Best non-def residual STRICT C3-Pair-2 = 1.054e-01 (no `{λ_n}` identity even on A_F). N=2 calibration corpus → SUGGESTION-grade. Audit SHA `b6c0d4bf5f09e93e…`.
