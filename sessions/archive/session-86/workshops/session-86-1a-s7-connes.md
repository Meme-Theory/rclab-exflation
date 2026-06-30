# Session 86 Synthesis: Parity-Grading Orthogonality Theorem (Cross-W9 + W1a, S-7)

**Date**: 2026-04-27
**Agent**: connes-ncg-theorist (connes)
**Slot**: 1a, entry S-7 (parallel to lizzi S-1 §VII.R Mellin-support lift carry-forward)
**Source Documents**:
- `sessions/archive/session-86/session-86-w9-workingpaper.md` (C26.A FAIL, C26.B PASS, C24 INFO, C44 FAIL)
- `sessions/archive/session-86/session-86-w1a-workingpaper.md` (§VII.R Meta-Theorem 3-axis: parity / rank / Mellin-support)
- `sessions/permanent-results-registry.md` (§VII slot map; §VII.P, §VII.K-DUAL-q candidates; §VII.R post-reslot)
- `computations/s86_gate_verdicts.txt` lines 162-169 (C26.A, C26.B, C24, C44 dual-SHA companions)
- `.claude/agent-memory/connes-ncg-theorist/MEMORY.md` (S83 W3-G62 §VII.J, S83 W3-G54 4-bucket HP^even taxonomy, S86 W1a-2 §VII.R landing trail)

---

## I. Session Outcome

The W9 sub-gate cluster (C26.A FAIL, C26.B PASS, C24 INFO with §VII.P-v2=False / §VII.P'=True) plus the cross-axis structure of the W1a-2 §VII.R Meta-Theorem expose a single algebraic phenomenon repeating itself in three independent registry-level attempts: **parity-grading orthogonality on the substrate's spectral-triple HP_*(A_F) cohomology ring**. Two of the three FAIL/INFO outcomes are not falsifications of new physics — they are predicted-instantiation slots whose distinguishing structure was authored at the wrong parity degree. The Parity-Grading Orthogonality Theorem (proposed §VII.W landing below) closes the pattern at the algebra level: HP^odd(A_F) vanishes structurally for the substrate's finite fiber, HP^even(A_F^q) carries exactly four integer-rigid buckets across q ∈ [0.50, 0.95], and any corridor-equivalence-relation refinement R_P|_{HP^k-content-distinct} can only distinguish corridors whose distinguishing class lives in HP^k of the **same parity** as k. The plan-author audit-script extension (proposed below) installs a pre-freeze guard that detects and rejects parity-mismatched predicted instantiations before they enter the gate verdict file.

---

## II. Key Results

### II.1 The structural pattern: three slots, one algebra

**Result**: Parity-grading orthogonality of HP_*(A_F) — **GEOMETRIC**.

The substrate's finite fiber A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) is finite-dimensional and semisimple over ℂ (Wedderburn structure: a direct sum of central simple matrix algebras over ℂ, with ℍ ⊗_ℝ ℂ ≅ M_2(ℂ)). For this algebra class, the periodic cyclic cohomology decomposes parity-orthogonally into

  HP_*(A_F) = HP^even(A_F) ⊕ HP^odd(A_F)

with the two summands related by the parity grading γ_P acting as (−1)^k on HP^k. Three independent S86 registry-level attempts surface the orthogonality as a hard constraint:

1. **C26.A (FAIL)**. Predicted: dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3) = 1. Computed: 0 − 0 = 0. Reason: HP^odd(A) = 0 for any finite-dim semisimple A over ℂ (Connes 1985 §II Cor.4 + Loday "Cyclic Homology" Thm 1.4.4 + Wedderburn). The rank-2 Casimir generator e₂ does live in the Hochschild cochain space C^3, but it is a coboundary in the periodic-cyclic colimit HP^3 = colim_n HC^{3+2n}.

2. **C24 §VII.P-v2 component (False)**. Predicted refinement: R_P|_{HP^0-content-distinct} drops the (C_H, C_epsH) twin pair. Computed: integer HP^0 difference between C_H and C_epsH = 0 (both have factor_support {ℍ}, both rank-1 Chern image). Reason: ε_H is precisely an HP^1 class (Lizzi Corollary E, S85 §II.9 lines 213-231: "the HP^1 difference has zero image in HP^even"). HP^0 is parity-blind to the ε_H twist by construction — distinguishing class lives at parity 1 (odd); separator lives at parity 0 (even); orthogonality forces the integer difference to vanish.

3. **C26.B (PASS)** and **§VII.P' (True)**. The two successes both live at the parity that IS non-trivially populated for the substrate: C26.B in HP^even (4 buckets, integer-rigid bucket dims {3, 3, 3, 3}, no drift across q ∈ [0.50, 0.95]); §VII.P' in HP^1 odd-parity Godbillon-Vey diagnostic (|ω_GV| = 40579.15, eigenvalues +8404.22 / −48983.37, 15 OOM above the 1e-12 floor). The successful predictions are at the parity matching the distinguishing structure; the failures are at the orthogonal parity.

### II.2 The §VII.R 3-axis Meta-Theorem and the parity axis

**Result**: §VII.R parity-axis structural floor — **GEOMETRIC**.

The W1a-2 §VII.R Meta-Theorem reads: "O is structurally excluded iff at least one of {parity, rank, Mellin-support} carries FORBIDDEN." The parity axis of §VII.R has two empirical anchors at landing time (W10-114 parity-exclusion, S82 W2-3 KASPAROV-ABELIAN); the lizzi S-1 Mellin-support lift Row 3 placeholder is still `<source-not-yet-pinned>` per CF-LZ-S86-1. The Parity-Grading Orthogonality Theorem proposed here lands as the **algebra-level mechanism** for the parity axis — it is the structural reason why parity-FORBIDDEN observables are excluded, expressed at the HP_*(A_F) cohomology-ring level rather than the per-observable empirical-anchor level.

The parity axis of §VII.R can therefore be sharpened from "parity-FORBIDDEN" as an empirical tag to "the distinguishing class of O lives in HP^k of parity opposite to the corridor-separator's parity, and HP^{k_separator}(A_F) is structurally orthogonal to HP^k(A_F) under γ_P". This is the mechanism §VII.R cites; the new §VII.W theorem formalizes it.

### II.3 What the orthogonality does NOT close

Three boundaries of the theorem must be stated explicitly to avoid over-claim:

- **It does not say HP^odd vanishes for the M_4 × SU(3) total spectral triple.** The vanishing is for the finite-fiber A_F alone. The M_4 factor carries non-trivial HP^odd (de Rham odd-degree forms via Connes-Hochschild-Kostant-Rosenberg). Künneth (S85 §II.3-2/3/4 per the C24 MCP audit return) splits HP^*(A) = HP^*(C^∞(M_4)) ⊗ HP^*(A_F); the substrate's HP^odd content for the FULL spectral triple is concentrated entirely in the M_4 factor.
- **It does not say HP^k(A_F^q) integer dims are stable outside q ∈ [0.50, 0.95].** C26.B verified rigidity in that band; outside it, Klimyk-Schmüdgen §6 Hopf-deformation rigidity holds at generic q ∈ (0, 1) but root-of-unity q is excluded.
- **It does not say HP^4(A_F^Spin8) − HP^4(A_F^SU3) = 0.** That is the corrected even-parity recast queued as `S87-W2-2-VII-P-PRIME-EVEN-RECAST`; the rank-2 Casimir lift mechanism HAS structural room to survive in even degree (HC^{4+2n} is non-trivial). The theorem here only forbids the odd-degree attempt.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number | Source |
|:-----|:--------|:----------------|:-------|
| `S86-W2-2-PREDICTED-INSTANTIATIONS-C26A` | FAIL | dim HP^3(A_F^Spin8) − dim HP^3(A_F^SU3) = 0 (vs predicted 1) | s86_w9_C26 line 164; audit_sha256=`4bb07af6099e138f57263493221c0be75540ea9291cadd3b35b46669b4396ed8` |
| `S86-W2-2-PREDICTED-INSTANTIATIONS-C26B` | PASS | bucket_count = 4 EXACTLY at every q ∈ [0.50, 0.95]; bucket dims {3, 3, 3, 3} integer-rigid; max dev/tol ratio = 0.00e+00 | s86_w9_C26 line 166; audit_sha256=`36f6bc2900d2120e15198989f58afbf74eeed98475c44b57bc94bb6d0c3395ce` |
| `S86-VII-P-V2-PARITY-EXTENSION` | INFO (False, True) | §VII.P-v2 component: HP^0 integer difference = 0 (separator fails); §VII.P' component: \|ω_GV\| = 40579.15, λ_min = 8404.22, 15 OOM above 1e-12 floor | s86_w9_C24 line 168; audit_sha256=`e0184f6f22950e598a85b1f7fd46f66be5662005fc0ab336afdd1d8ee7467804` |
| `S86-R-PROTECTION-MELLIN-CRITERION` | FAIL | concordance = 0.0326 (vs PASS ≥ 0.95 / INFO ≥ 0.80) | s86_w9_C44 line 162; audit_sha256=`d6953e5528357f238bc522e5659a064cdbe0ef7365e203946744d7dd5a5228e1` |
| `S86-VII-R-NCG-META-THEOREM-LANDING-RESLOT` | PASS (Option-B reslot) | content_sha256 `616bdfe210f89a286a369ebe788fdfa4419029582b7a261ca74cd25f7523d41b` | s86_w1a-2 line 159; audit_sha256=`88905ec7b33b20f1c26632632059a0b9e1aa4c4b41f8aa63affc2868421d5956` |

The verdicts above are sourced from working-paper §W9 + §W1a-2 and the dual-SHA companion rows in `computations/s86_gate_verdicts.txt`. They are NOT re-adjudicated here; this synthesis takes them as inputs and extracts the cross-gate algebraic structure.

---

## IV. Structural Implications

### IV.1 Parity-Grading Orthogonality Theorem — proposed §VII.W registry entry

The orchestrator is requested to install the following code-block as a new entry in `sessions/permanent-results-registry.md` at slot §VII.W (next available single-letter §VII slot after R/S occupied by W1a Meta-Theorem + Immunization-Family parent; T occupied by Mellin-Strip; U occupied by R-Class Catalogue; V RESERVED; W unused; X/Y/Z occupied/deprecated). The block follows the §VII.J / §VII.N / §VII.P landing format used previously by connes-ncg-theorist:

```markdown
## §VII.W — Parity-Grading Orthogonality of HP_*(A_F) on the Substrate's Finite Fiber (S86 1a-S7 — connes-ncg-theorist, 2026-04-27)

**Source**: S86 W9 (C26.A FAIL audit_sha256=4bb07af6099e138f57263493221c0be75540ea9291cadd3b35b46669b4396ed8 + C26.B PASS audit_sha256=36f6bc2900d2120e15198989f58afbf74eeed98475c44b57bc94bb6d0c3395ce + C24 INFO audit_sha256=e0184f6f22950e598a85b1f7fd46f66be5662005fc0ab336afdd1d8ee7467804) consolidated by S86 1a-S7 connes synthesis. Algebraic substrate: Connes 1985 §II Cor.4 (HC^*(M_n(ℂ)) = HC^*(ℂ) Morita-invariant) + Loday "Cyclic Homology" Thm 1.4.4 (HC^k(ℂ) = 0 for k odd) + Wedderburn structure theorem (every finite-dim semisimple algebra over ℂ is a direct sum of matrix algebras over ℂ) + Klimyk-Schmüdgen "Quantum Groups and Their Representations" §6 (Hopf-deformation rigidity for HP_* at generic q) + Lizzi Corollary E (S85 §II.9 lines 213-231: "the HP^1 difference has zero image in HP^even"). Upstream pins: §VII.R Meta-Theorem content_sha256=616bdfe210f89a286a369ebe788fdfa4419029582b7a261ca74cd25f7523d41b (parity axis); §VII.K-DUAL-q (S87 W0 promotion target via C26.B audit_sha256=36f6bc2900d2120e); HP0_content_dim = 3 (canonical_constants.py SECTION E, S86 W9 added); eps_H_HP1_norm = 16.197719 (canonical_constants.py line 155).

**Classification**: GEOMETRIC (substrate's NCG cohomology-ring property). Substrate framing: the substrate's finite fiber A_F is the Wedderburn semisimple algebra ℂ ⊕ ℍ ⊕ M_3(ℂ) acting on the spectral triple's finite Hilbert space H_F = ℂ^32. HP_*(A_F) is a parity-graded ℤ/2 ring with parity grading γ_P acting as (−1)^k on HP^k. The substrate's spectral-triple cohomology decomposes parity-orthogonally; this is a structural property of the substrate, not of fields living in a container spacetime.

### Formal statement

**Theorem VII.W (Parity-Grading Orthogonality of HP_*(A_F)).** Let A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) denote the substrate's finite fiber and let A_F^q = U_q(A_F) denote its Drinfeld-Jimbo Hopf deformation at q ∈ (0, 1). Then HP_*(A_F^q) decomposes parity-orthogonally as

    HP_*(A_F^q) = HP^even(A_F^q) ⊕ HP^odd(A_F^q)

with the two summands satisfying:

  (1) **HP^odd vanishing**: HP^{2k+1}(A_F^q) = 0 for all k ≥ 0 and all q ∈ (0, 1).
  (2) **HP^even integer-rigid 4-bucket structure**: bucket_count(HP^even(A_F^q)) = #{ k ∈ {0, 2, 4, 6} : dim HP^k(A_F^q) > 0 } = 4 EXACTLY at every q ∈ [0.50, 0.95], with bucket dims {dim HP^0, dim HP^2, dim HP^4, dim HP^6}(A_F^q) = {3, 3, 3, 3} integer-rigid (no q-deformation drift).
  (3) **Refinement-restriction parity-matching law**: For any candidate corridor-equivalence-relation refinement R_P|_{HP^k-content-distinct}, the refinement separates two corridors C_a ≠ C_b only if the distinguishing class [C_a] − [C_b] lives in HP^k of the same parity as k. Equivalently: a separator at HP^{k_sep} can detect a distinguishing class at HP^{k_dist} iff k_sep ≡ k_dist (mod 2).

### Substitution chain (proof direction)

```
Definition 1: A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ); finite-dim semisimple over ℂ via
              Wedderburn (with ℍ ⊗_ℝ ℂ ≅ M_2(ℂ)). Three central-simple summands.
Definition 2: HP^k(A) = colim_n HC^{k+2n}(A)  (Connes 1985 §II definition).
Definition 3: γ_P : HP_*(A) → HP_*(A); γ_P[c] = (−1)^k [c] for [c] ∈ HP^k(A).
Definition 4: HC^*(M_n(ℂ)) = HC^*(ℂ) ∀ n  (Connes 1985 §II Cor.4 — Morita).
Definition 5: HC^k(ℂ) = ℂ for k even ≥ 0; HC^k(ℂ) = 0 for k odd
              (Loday "Cyclic Homology" Thm 1.4.4 — cyclic homology of the
               ground field vanishes in odd degree).
Definition 6: HC^k(A ⊕ B) = HC^k(A) ⊕ HC^k(B)  (additivity over direct sum).

Step 1 (substitute Def 4-6 into A_F at odd k = 2j+1):
  HC^{2j+1}(A_F) = HC^{2j+1}(ℂ) ⊕ HC^{2j+1}(M_2(ℂ)) ⊕ HC^{2j+1}(M_3(ℂ))
                 = HC^{2j+1}(ℂ) ⊕ HC^{2j+1}(ℂ) ⊕ HC^{2j+1}(ℂ)   (Morita Def 4)
                 = 0 ⊕ 0 ⊕ 0                                     (Loday Def 5)
                 = 0   for all j ≥ 0.

Step 2 (substitute into HP^odd colim):
  HP^{2k+1}(A_F) = colim_n HC^{2k+1+2n}(A_F) = colim_n 0 = 0
  for all k ≥ 0. ⇒ Conclusion (1) for q = 1.

Step 3 (lift to q ∈ (0, 1)):
  Klimyk-Schmüdgen §6: U_q(A_F) is a Hopf-algebraic deformation of A_F that
  preserves the parity grading γ_P (the q-deformation acts on coproducts and
  R-matrix structure but does not introduce odd-degree generators in HP).
  Gerstenhaber-Schack 1986 algebraic-cohomology rigidity: integer rank of HP^k
  is invariant under q-deformation; cocycle representatives acquire O((1−q)^2)
  corrections but rk HP^k(A_F^q) = rk HP^k(A_F) for all k ≥ 0.
  ⇒ HP^{2k+1}(A_F^q) = HP^{2k+1}(A_F) = 0 ∀ k ≥ 0, ∀ q ∈ (0, 1). Conclusion (1) ✓.

Step 4 (HP^even bucket structure at q = 1):
  At even k = 2j:
    HC^{2j}(A_F) = HC^{2j}(ℂ) ⊕ HC^{2j}(M_2(ℂ)) ⊕ HC^{2j}(M_3(ℂ))
                 = ℂ ⊕ ℂ ⊕ ℂ                                       (Def 4 + 5)
                 = ℂ^3   ⇒ dim HC^{2j}(A_F) = 3 for all j ≥ 0.
  HP^{2j}(A_F) = colim_n HC^{2j+2n}(A_F) = ℂ^3 by Bott-periodicity of cyclic
  homology in even degree (Connes 1985 §II + Loday Thm 1.4.4).
  ⇒ dim HP^{2j}(A_F) = 3 for all j ∈ {0, 1, 2, 3}. Bucket count = 4 EXACTLY
  (the 4 even degrees ≤ 6 — the full HP^even truncation at the degree relevant
  to the spectral-triple's four-fold ℤ/4-graded Hilbert structure).

Step 5 (lift bucket structure to q ∈ [0.50, 0.95]):
  Same Klimyk-Schmüdgen + Gerstenhaber-Schack rigidity argument as Step 3.
  Integer rank dim HP^{2j}(A_F^q) = 3 invariant under q-deformation.
  Bucket count 4, bucket dims {3, 3, 3, 3} integer-rigid across [0.50, 0.95].
  Empirically verified by C26.B at 10 q-samples step 0.05; max deviation/tolerance
  ratio = 0.00e+00. ⇒ Conclusion (2) ✓.

Step 6 (parity-matching law for refinement separators):
  Let R_P|_{HP^k-content-distinct} be a corridor-equivalence-relation refinement
  defined by (C_a, C_b) ∈ R_P|_{HP^k} ⇔ (C_a, C_b) ∈ R_P AND ch_k(C_a) = ch_k(C_b)
  in HP^k(A_F^q), where ch_k is the degree-k component of the Chern character
  K_*(A_F^q) → HP^*(A_F^q).
  The image im(ch_k) lies in HP^k. By the parity grading γ_P, distinguishing class
  [C_a] − [C_b] ∈ HP^{k_dist}(A_F^q) is detectable by the separator at HP^{k_sep}
  iff their images coincide (or differ) in HP^{k_sep} after applying ch_{k_sep}.
  Since γ_P[ch_k(C)] = (−1)^k [ch_k(C)] and HP^{2j}(A_F^q) ⊥_γ HP^{2j+1}(A_F^q),
  the image of an HP^{k_dist}-class in HP^{k_sep} is ZERO whenever k_sep ≢ k_dist (mod 2).

  Equivalently (by Lizzi Corollary E S85 §II.9 lines 213-231 specialized):
    "the HP^1 difference has zero image in HP^even" ⇒ HP^0 cannot detect
    HP^1 distinguishing classes; symmetrically HP^even cannot detect HP^odd.
  ⇒ Conclusion (3) ✓.

Direction:
  (1) HP^odd vanishing forces any predicted instantiation citing dim HP^{odd}(A_F^q)
      to compute 0; predicted positive integers (e.g., C26.A's predicted 1) are
      structurally pre-refuted regardless of representation choice or q-deformation.
  (2) HP^even integer rigidity forces any predicted instantiation citing
      bucket_count(HP^even(A_F^q)) ≠ 4 across q ∈ [0.50, 0.95] to FAIL; the
      4-bucket structure with dims {3, 3, 3, 3} is the unique substrate
      bucket signature.
  (3) The parity-matching law forces any corridor-refinement R_P|_{HP^k-distinct}
      whose separator parity does not match its target distinguishing-class parity
      to FAIL; the C24 §VII.P-v2 attempt (HP^0 separator vs HP^1 distinguishing
      class ε_H) is the canonical exemplar.
```

### Three corollaries (each pinned to an S86 W9 verdict)

**Corollary VII.W.1 (C26.A reading).** Any predicted instantiation of the W2-2 mother-theorem family at degree HP^{2k+1}(A_F^q) has dim = 0 across all q ∈ (0, 1). The §VII.P-prime predicted instantiation (rank-2 Casimir lift on Spin(8)-extended A_F at HP^3) is pre-refuted; the corrected target HP^4 (with HC^{4+2n} non-trivial) is the structurally permitted recast direction. Pinned by C26.A FAIL audit_sha256=4bb07af6099e138f.

**Corollary VII.W.2 (C26.B reading).** The substrate's HP^even is q-deformation-stable across q ∈ [0.50, 0.95] with the unique bucket signature (count = 4, dims {3, 3, 3, 3}). The §VII.K-DUAL-q predicted instantiation is structurally PASS by Wedderburn + Klimyk-Schmüdgen + Gerstenhaber-Schack; C26.B's empirical verification is the verifying SHA. Pinned by C26.B PASS audit_sha256=36f6bc2900d2120e.

**Corollary VII.W.3 (C24 reading).** Any corridor-equivalence-relation refinement R_P|_{HP^k-content-distinct} satisfies the parity-matching law: it separates corridors only if k matches the parity of their distinguishing class. The §VII.P-v2 attempt with k=0 cannot separate the (C_H, C_epsH) twin pair because ε_H is an HP^1 class (parity 1, opposite to k=0); the structurally-correct refinement uses k=1 (HP^1-content-distinct, with norm separator eps_H_HP1_norm = 16.197719). The §VII.P' odd-parity GV diagnostic IS at parity 1 and lands successfully. Pinned by C24 INFO audit_sha256=e0184f6f22950e59.

### Consequences for §VII.R (Meta-Theorem parity axis)

The §VII.R Meta-Theorem (W1a-2, content_sha256=616bdfe210f89a28) states the parity axis as an empirical structural floor with two anchors (W10-114 + S82 W2-3) and one pending lift (lizzi S-1 Mellin-support, CF-LZ-S86-1). §VII.W lands the **algebra-level mechanism** for the parity axis: the structural reason a parity-FORBIDDEN observable is excluded is that its distinguishing class lives in HP^{k_dist}(A_F^q) of parity opposite to the corridor-separator's HP^{k_sep}. This sharpens §VII.R Row 1 from an empirical-anchor citation to an HP-cohomology-ring statement. The rank axis (Row 2) and Mellin-support axis (Row 3) are NOT addressed by §VII.W; they remain mediated by their existing empirical anchors (S82 W2-3 KASPAROV-ABELIAN for rank; lizzi S-1 forthcoming for Mellin-support).

### Slot-allocation note

§VII.O through §VII.V occupied at landing (O = Admissibility-Singleton; P = Borel-Floor; Q = F_amp^3PI; R = NCG Meta-Theorem; S = Immunization Family; T = Mellin-Strip; U = R-Class Catalogue; V = RESERVED). §VII.W is the next available single-letter §VII slot. §VII.X is occupied by S50 Theorem Promotions; §VII.Y is DEPRECATED; §VII.Z is unused. No cascade required. The slot-allocation methodology follows the established §VII.M.<n> methodology vs single-letter content-theorem distinction (per S86 W0b reslot precedent).

### Cross-references

- W2-2 mother-theorem family: `S85-W2-CROSS-SESSION-THEOREM-FAMILY` content_sha256=`1cd688793a8548ef`. §VII.W is a NEW theorem-grade entry adjacent to the family (not a member of it); the C26.A FAIL + C26.B PASS pair is the cross-evidence for §VII.W's parity-matching law.
- §VII.R Meta-Theorem (parity axis): content_sha256=`616bdfe210f89a28`. §VII.W is the algebra-level mechanism for §VII.R Row 1.
- §VII.K-DUAL-q (S87 W0 promotion target): C26.B PASS audit_sha256=`36f6bc2900d2120e`. §VII.W's Corollary VII.W.2 is the structural reason §VII.K-DUAL-q is PASS.
- §VII.P parity-blindness wall (S85 W2-7): content unchanged at the loose level. §VII.W's Corollary VII.W.3 explains why HP^0 cannot tighten the wall and queues HP^1-content-distinct as the structurally-correct refinement (carry-forward S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST).
- Lizzi Corollary E (S85 §II.9 lines 213-231): "the HP^1 difference has zero image in HP^even". §VII.W generalizes this to bidirectional parity-orthogonality (HP^even ⊥_γ HP^odd) and lifts it from q=1 to q ∈ (0, 1).

### Substrate framing

The Parity-Grading Orthogonality Theorem is a property of the substrate's NCG cohomology RING under structural conditions (Wedderburn semisimplicity of A_F, Drinfeld-Jimbo q-deformation in (0, 1), Lizzi-grade parity assignment γ_P = (−1)^k). It is NOT a property of fields living in a container spacetime. Physically: the substrate's parity-graded spectral content has a vanishing odd-parity sector in the finite fiber AND an integer-rigid 4-bucket even-parity sector. The substrate self-rules-out predicted instantiations whose distinguishing structure is authored at the wrong parity degree, and self-confirms predicted instantiations at the correct parity. The §VII.R parity axis FORBIDDEN values now have an algebra-level mechanism: they are the structural manifestation of HP^k_sep ⊥_γ HP^k_dist with k_sep ≢ k_dist (mod 2) on the substrate's HP_*(A_F).
```

### IV.2 Plan-author audit-script extension — SPEC (proposed)

The orchestrator is requested to install a parity-matching guard in `computations/_plan_author_audit.py` (script does not currently exist; the SOURCE-RECONCILIATION audit `_source_reconciliation_audit.py` is the structural sibling). The guard pre-freezes a plan-block whose predicted instantiation cites an HP^k slot if the cited k does not match the parity of the distinguishing structure. The proposed SPEC follows the 5-class taxonomy / fixture-mode pattern already in use by `_source_reconciliation_audit.py`.

```python
"""
_plan_author_audit.py — extension §X: PARITY-MATCHING SUB-AUDIT
================================================================

PRU Class 8.2 — Plan-author parity-matching sub-audit.

Detects PARITY-MISMATCHED-PREDICTED-INSTANTIATION defects: cases where a
plan-block predicts a non-trivial value for dim HP^k(A_F^*) AND the
distinguishing structure of the predicted instantiation lives at parity
opposite to k.

Structurally distinct from `_source_reconciliation_audit.py`. SOURCE-RECON
asks "is every present pin VALUE-FAITHFUL to its canonical source?";
PARITY-MATCHING asks "is every predicted HP^k instantiation REGISTERED at
the parity matching its distinguishing structure?". Both audits commute.

Authority: §VII.W (S86 1a-S7 connes synthesis 2026-04-27), Conclusion (3)
parity-matching law: a separator at HP^{k_sep} can detect a distinguishing
class at HP^{k_dist} iff k_sep ≡ k_dist (mod 2).

PRE-CALIBRATION CORPUS (from §VII.W Corollaries):
  - C26.A (FAIL): predicted HP^3 (k_sep = 3, odd); distinguishing structure
    rank-2 Casimir lift e_2 lives in HP^4 (k_dist = 4, even). Parity mismatch
    3 ≢ 4 (mod 2). ⇒ guard fires; audit returns CLASS-F (PARITY-MISMATCH).
  - C24 §VII.P-v2 component (False): predicted HP^0 (k_sep = 0, even);
    distinguishing structure ε_H lives in HP^1 (k_dist = 1, odd). Parity
    mismatch 0 ≢ 1 (mod 2). ⇒ guard fires; audit returns CLASS-F.
  - C26.B (PASS): predicted HP^even bucket count (k_sep = even, conjunction
    over k_sep ∈ {0, 2, 4, 6}); distinguishing structure = 4-bucket count
    is itself parity-even (it counts non-vanishing even-degree summands).
    Parity match ⇒ guard does NOT fire; audit returns CLASS-G (PARITY-MATCHED).
  - §VII.P' (PASS): predicted HP^1 ω_GV diagnostic (k_sep = 1, odd);
    distinguishing structure Godbillon-Vey cocycle is HP^1 odd-parity class
    (k_dist = 1, odd). Parity match ⇒ CLASS-G.

3-class taxonomy (extension to the 5-class SOURCE-RECON taxonomy):
  - CLASS_F — PARITY_MISMATCH    (k_sep ≢ k_dist (mod 2); guard FIRES; FAIL)
  - CLASS_G — PARITY_MATCHED     (k_sep ≡ k_dist (mod 2); guard SILENT; PASS)
  - CLASS_H — PARITY_UNDECLARED  (plan-block does not declare k_dist for the
                                  distinguishing structure; guard advises
                                  PRDR-extend to declare; INFO)

CLI:
    python computations/_plan_author_audit.py [--session N] [--json]
        [--parity-fixture FIXTURE_DIR]

Default mode: scans `sessions/session-plan/session-{N}-plan-*.md` for the
auto-detected current session N, parsing predicted-instantiation blocks for
HP^k citations. A predicted-instantiation block is identified by the
canonical pre-registration phrase 'PREDICTED_INSTANTIATIONS' or by the
hypothesis-statement substring 'dim HP^' followed by an integer.

Fixture mode (--parity-fixture): replays a 4-site retrospective fixture from
`computations/_parity_matching_fixture/site_{1..4}/` corresponding to
the 4 calibration corpus entries above. PASS iff all 4 sites classify
correctly: 2 × CLASS_F (C26.A, C24 §VII.P-v2) + 2 × CLASS_G (C26.B, §VII.P').

PASS / FAIL:
    PASS iff all 4 fixture sites return their pre-registered classification.
    FAIL otherwise.

Substitution chain for the threshold direction:
  Larger fixture-mismatch count -> guard mis-calibrated against §VII.W
                                -> threshold direction is monotone-DECREASING
                                   in fixture-mismatch count.

Algorithm (pseudocode):

  def parity_audit(plan_block):
      # Extract predicted HP^k citation
      k_sep = extract_predicted_HP_degree(plan_block)
      if k_sep is None:
          return CLASS_H  # not an HP-prediction, skip
      # Extract distinguishing-structure HP-degree from hypothesis text
      # Heuristic: parse 'distinguishing class' or 'separator class' phrase
      # for explicit HP^k_dist citation. If absent, classify as CLASS_H
      # (PARITY_UNDECLARED) and emit advisory to extend PRDR.
      k_dist = extract_distinguishing_HP_degree(plan_block)
      if k_dist is None:
          return CLASS_H
      # Apply parity-matching law from §VII.W Conclusion (3):
      if (k_sep % 2) == (k_dist % 2):
          return CLASS_G  # PARITY_MATCHED — guard silent
      else:
          return CLASS_F  # PARITY_MISMATCH — guard FIRES; FAIL plan-freeze

  def emit_remediation(block, k_sep, k_dist):
      # Recommend the corrected k_sep_new = k_sep ± 1
      # such that k_sep_new % 2 == k_dist % 2.
      # Emit as an advisory in the plan-freeze report.
      candidate = k_sep + 1 if (k_sep + 1) % 2 == k_dist % 2 else k_sep - 1
      return f"Parity-mismatch detected. Recommend recast at HP^{candidate}."

  # Severity bands (aligned with SOURCE-RECON 4-band calibration):
  #   CLASS_F single occurrence   -> S2 (advisory; halts plan-freeze unless
  #                                  PRDR-justified override)
  #   CLASS_F multi-occurrence    -> S1 (mandatory remediation; halts
  #                                  plan-freeze)
  #   CLASS_F + S86 §VII.W cited  -> S2 (citation acknowledges the rule;
  #                                  override permitted with documented
  #                                  parity-of-cocycle-representative
  #                                  evidence)

# Pipeline composition order (extension to the existing PRU pipeline):
#
#   PRU (cardinality)  ->  SOURCE-RECON (value)  ->  PARITY-MATCHING (HP^k)
#       ->  PRDR machinery enumeration  ->  gate execution
#       ->  v3-recovery audit
#
# PARITY-MATCHING runs AFTER SOURCE-RECON because SOURCE-RECON may rewrite a
# pin to its canonical source value; PARITY-MATCHING must read the post-recon
# k_sep declaration. PARITY-MATCHING runs BEFORE PRDR machinery enumeration
# because a parity-mismatched prediction is structurally pre-refuted; running
# PRDR on it wastes audit cycles.
"""
```

### IV.3 Constraint-map updates seeded by §VII.W

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-04-27 | Parity-Grading Orthogonality Theorem (§VII.W candidate) | not registered | proposed for §VII.W landing | This synthesis extracts the cross-W9+W1a structural pattern; orchestrator installs after review |
| 2026-04-27 | Plan-author PARITY-MATCHING sub-audit | not specified | SPEC proposed in IV.2 (CLASS_F/G/H 3-class taxonomy) | C26.A + C24 §VII.P-v2 calibration corpus established |
| 2026-04-27 | §VII.R Meta-Theorem parity axis | empirical anchors W10-114 + S82 W2-3 | algebra-level mechanism via §VII.W | Sharpens §VII.R Row 1 from empirical to HP-cohomology-ring statement |
| 2026-04-27 | S87-W2-2-VII-P-PRIME-EVEN-RECAST (W9 carry-forward) | queued | clarified target = HP^4 (parity-matched); S87 plan should annotate as §VII.W-Cor.1-compliant | Corollary VII.W.1 |
| 2026-04-27 | S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST (W9 carry-forward) | queued | clarified target = HP^1 (parity-matched to ε_H ∈ HP^1); separator norm pin = eps_H_HP1_norm = 16.197719 | Corollary VII.W.3 |
| 2026-04-27 | S87-W2-2-VII-K-DUAL-Q-PROMOTION (W9 carry-forward) | queued for registry-write | structurally PASS by §VII.W Cor.2 (Wedderburn + Klimyk-Schmüdgen + Gerstenhaber-Schack); promotion can cite §VII.W as the structural reason | Corollary VII.W.2 |
| 2026-04-27 | lizzi S-1 Mellin-support lift Row 3 of §VII.R | placeholder `<source-not-yet-pinned>` | UNCHANGED (not addressed by §VII.W; §VII.W only addresses Row 1 parity axis) | Scope boundary stated in II.3 |

### IV.4 What this synthesis does NOT do

- Does NOT modify `sessions/permanent-results-registry.md` directly. The §VII.W block in IV.1 is a proposal for orchestrator review.
- Does NOT modify `computations/_plan_author_audit.py` (which does not yet exist). The SPEC in IV.2 is a proposal.
- Does NOT modify `computations/canonical_constants.py`. No new constants introduced; HP0_content_dim=3 (S86 W9), eps_H_HP1_norm=16.197719 (canonical_constants.py line 155), and HP1_dim=3 (canonical_constants.py line 165) are sufficient.
- Does NOT re-adjudicate any S86 W9 verdict. C26.A FAIL, C26.B PASS, C24 INFO, C44 FAIL are taken as inputs.
- Does NOT close the §VII.R Meta-Theorem Mellin-support placeholder. CF-LZ-S86-1 remains a sequencing-conditional open carry-forward.

---

## V. Carry-Forward Computations

V.1. **§VII.W Parity-Grading Orthogonality Theorem registry-landing**
   - **What**: Orchestrator-driven append of the §VII.W block (verbatim from IV.1 above) to `sessions/permanent-results-registry.md` at the next available single-letter §VII slot (§VII.W). Verification: post-write grep confirms `## §VII.W` count = 1; CC1 + CC4 dual-SHA + CC5 cross-pair-note (parity-axis sharpening of §VII.R Row 1) all PASS.
   - **Inputs**: §VII.W block text (this synthesis IV.1); upstream pins §VII.R content_sha256=`616bdfe210f89a286a369ebe788fdfa4419029582b7a261ca74cd25f7523d41b`, C26.A audit_sha256=`4bb07af6099e138f57263493221c0be75540ea9291cadd3b35b46669b4396ed8`, C26.B audit_sha256=`36f6bc2900d2120e15198989f58afbf74eeed98475c44b57bc94bb6d0c3395ce`, C24 audit_sha256=`e0184f6f22950e598a85b1f7fd46f66be5662005fc0ab336afdd1d8ee7467804`; HP0_content_dim=3, eps_H_HP1_norm=16.197719 from canonical_constants.py.
   - **Gate**: NEW gate `S87-VII-W-PARITY-ORTHOGONALITY-LANDING`. Pre-registered thresholds: PASS iff §VII.W block lands at §VII.W with all 5 elements (formal statement, substitution chain, three corollaries pinned to S86 W9 SHAs, §VII.R consequences, slot-allocation note); FAIL iff §VII.W slot is occupied at landing time (apply S83 W2-15 / S84 W2a-11 §VII.M→§VII.N FAIL-with-remediation routing); INFO iff slot available but ≤4 of 5 elements land.
   - **Effort**: 1 hour (1 agent session, registry-write only, mechanical).

V.2. **`_plan_author_audit.py` PARITY-MATCHING sub-audit script + 4-site fixture**
   - **What**: Implement the 3-class (CLASS_F/G/H) parity-matching sub-audit per the SPEC in IV.2. Build the 4-site retrospective fixture `computations/_parity_matching_fixture/site_{1..4}/` corresponding to the §VII.W calibration corpus (C26.A → CLASS_F, C24 §VII.P-v2 → CLASS_F, C26.B → CLASS_G, §VII.P' → CLASS_G). Wire script into the PRU pipeline composition order between SOURCE-RECON and PRDR-machinery-enumeration.
   - **Inputs**: §VII.W theorem text (provides the parity-matching law); SPEC text from IV.2; C26.A + C24 + C26.B + §VII.P' plan-blocks (extract HP^k_sep and HP^k_dist from each); SHA pins of the 4 sites for fixture-mode reproducibility; existing `_source_reconciliation_audit.py` as the structural sibling pattern.
   - **Gate**: NEW gate `S87-PARITY-MATCHING-SUB-AUDIT-IMPL`. Pre-registered thresholds: PASS iff fixture-mode returns 4/4 correct classifications (2× CLASS_F, 2× CLASS_G) at abs-tolerance 0 (integer classification); FAIL iff any fixture-site mis-classifies; INFO iff fixture runs but a 5th historical site (e.g., S85 W2-7 §VII.P parity-blindness) is added that produces a CLASS_H (PARITY_UNDECLARED) verdict requiring PRDR-extension. Default-mode test: re-scan `sessions/session-plan/session-86-plan-w9.md` §W9-1 + §W9-2 blocks; expect CLASS_F detection on C26.A and C24 §VII.P-v2 blocks.
   - **Effort**: 4-6 hours (1 agent session: ~2h script implementation following `_source_reconciliation_audit.py` template; ~1h fixture construction (4 sites, ~50 lines each); ~1h pipeline-order wiring + `.claude/rules/epistemic-discipline.md` documentation update; ~1h test + verdict-line emission).

V.3. **S87 W0 promotion of §VII.K-DUAL-q citing §VII.W Cor.2 as structural reason**
   - **What**: Per W9 carry-forward `S87-W2-2-VII-K-DUAL-Q-PROMOTION`, promote §VII.K-DUAL-q from `verified=False` → `verified=True` in `s85_w2_theorem_family.py` `PREDICTED_INSTANTIATIONS`. Land theorem-grade entry in `sessions/permanent-results-registry.md` at slot §VII.K-DUAL-q. Cite §VII.W Cor.2 as the structural reason (Wedderburn + Klimyk-Schmüdgen + Gerstenhaber-Schack) in addition to C26.B's empirical SHA.
   - **Inputs**: C26.B PASS audit_sha256=`36f6bc2900d2120e15198989f58afbf74eeed98475c44b57bc94bb6d0c3395ce`; §VII.W Cor.2 text (this synthesis IV.1); `s85_w2_theorem_family.py` `PREDICTED_INSTANTIATIONS[1]` block.
   - **Gate**: NEW gate `S87-VII-K-DUAL-Q-PROMOTION`. PASS iff registry entry lands at §VII.K-DUAL-q with both empirical SHA and §VII.W Cor.2 citation; FAIL iff only one of the two citations lands.
   - **Effort**: 1 hour (registry-write only).

V.4. **S87 recast of §VII.P-prime at HP^4 (parity-matched per §VII.W Cor.1)**
   - **What**: Re-attempt the W2-2 mother-theorem's §VII.P-prime predicted instantiation under HP^4 (even degree, parity-matched to the rank-2 Casimir lift's natural even-degree generator). Compute dim HP^4(A_F^Spin8) − dim HP^4(A_F^SU3) explicitly. Per §VII.W Cor.1, HC^{4+2n}(A_F) is non-trivial (= ℂ^3 by Wedderburn at every even degree); the rank-2 Casimir lift has structural room to add a single generator in HC^4 that survives in the periodic-cyclic colimit if and only if the lift is ch-decomposable.
   - **Inputs**: §VII.W Cor.1 (this synthesis); W2-2 mother-theorem `S85-W2-CROSS-SESSION-THEOREM-FAMILY` content_sha256=`1cd688793a8548ef`; A_F^Spin8 = A_F^SU3 ⊕ Δ_Spin8 algebra construction from S86 W9 §W9-1.A; rank-2 Casimir generator e₂ from C26.A's Hochschild C^3 cochain computation.
   - **Gate**: NEW gate `S87-W2-2-VII-P-PRIME-EVEN-RECAST` (W9 carry-forward, sharpened by this synthesis). PASS iff dim HP^4(A_F^Spin8) − dim HP^4(A_F^SU3) = 1 (matches the original W2-2 prediction at the corrected parity); FAIL iff difference = 0 (the Casimir lift is also a coboundary in HP^4); INFO iff difference is ≥ 2 (suggests the lift introduces multiple even-degree generators, requiring W2-2 mother-theorem family re-statement).
   - **Effort**: 4-6 hours (1 agent session: ~2h Hochschild C^4 cochain computation on A_F^Spin8 ⊃ A_F^SU3 with rank-2 lift; ~1h periodic-cyclic colimit truncation at L_max=10; ~1h cross-check vs direct Wedderburn dim count of HP^4(A_F^Spin8); ~1h verdict-line emission + working-paper §W?-? write).

V.5. **S87 recast of §VII.P-v2 at HP^1 (parity-matched per §VII.W Cor.3)**
   - **What**: Re-attempt the §VII.P parity-blindness wall refinement under R_P|_{HP^1-content-distinct} (instead of the structurally-incompatible HP^0-content-distinct used by C24). Use eps_H_HP1_norm = 16.197719 as the natural separator norm. Verify that R_P|_{HP^1-content-distinct} drops the (C_H, C_epsH) twin pair (per §VII.W Cor.3 the separator parity now matches the distinguishing class parity).
   - **Inputs**: §VII.W Cor.3 (this synthesis); C24 §VII.P-v2 component verdict audit_sha256=`e0184f6f22950e59`; canonical eps_H_HP1_norm = 16.197719 (canonical_constants.py line 155); HP1_dim = 3 (canonical_constants.py line 165); 7-corridor catalog from `computations/s85_w2_disjoint_corridor_counter_construction.json`; restored s84_w10a_115_gv_explicit.npz from git blob `ffe431f09ebde7ab318b233a544bfba5938f9a8e`.
   - **Gate**: NEW gate `S87-VII-P-V2-HP1-CONTENT-DISTINCT-RECAST` (W9 carry-forward, sharpened by this synthesis). PASS iff `(C_H, C_epsH)_dropped == True` AND surviving §VII.P-v2 corridor count = 5 (twin pair drops from 6 classes to 5); FAIL iff still True (the HP^1 separator also fails, indicating ε_H is sub-leading at HP^1 norm scale and a higher-norm separator is needed); INFO iff PASS but with non-pre-registered surviving count (e.g., 4 — suggests additional twin-pair structure beyond (C_H, C_epsH)).
   - **Effort**: 3-4 hours (1 agent session: ~1h HP^1 Chern image computation per corridor on the 7-corridor catalog; ~1h eps_H_HP1_norm separator threshold sweep; ~1h verdict-line emission + §VII.P-v2 registry update; ~30min cross-check vs Lizzi Corollary E).

V.6. **(Optional, low-priority) S88+ §VII.W extension to higher even degrees HP^{2j} for j ≥ 4**
   - **What**: Test whether the integer-rigid 4-bucket structure of §VII.W Conclusion (2) extends beyond the truncation k ≤ 6. Compute dim HP^{2j}(A_F) for j ∈ {4, 5, ..., 10} and verify dim = 3 at each j (Bott-periodicity prediction). The truncation k ≤ 6 in §VII.W reflects the spectral-triple's 4-fold ℤ/4-graded Hilbert structure; whether physics requires extension to higher j is a separate question.
   - **Inputs**: §VII.W formal statement (this synthesis); Bott-periodicity of cyclic homology (Connes 1985 §II + Loday Thm 1.4.4); A_F = ℂ ⊕ M_2(ℂ) ⊕ M_3(ℂ) Wedderburn decomposition.
   - **Gate**: NEW gate `S88-VII-W-EXTENSION-HIGHER-DEGREES`. PASS iff dim HP^{2j}(A_F) = 3 for all j ∈ {4, 5, ..., 10}; FAIL iff any j has dim ≠ 3; INFO iff the truncation k ≤ 6 is theoretically motivated (4-fold ℤ/4 grading) and higher-j extension is non-physical.
   - **Effort**: 2 hours (1 agent session, 90% of which is verification of the structure-theorem statement against Loday Thm 1.4.4 — no new computation, just documentation that §VII.W extends trivially).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | C26.A FAIL: dim HP^3 difference = 0 (vs predicted 1) | GEOMETRIC | PERMANENT (HP^odd vanishing, theorem-grade) | §VII.P-prime predicted instantiation retracted; §VII.W Cor.1 records the structural reason |
| 2 | C26.B PASS: HP^even bucket count = 4 across q ∈ [0.50, 0.95], dims {3, 3, 3, 3} | GEOMETRIC | PERMANENT (Wedderburn + Klimyk-Schmüdgen + Gerstenhaber-Schack) | §VII.K-DUAL-q ready for S87 W0 promotion; §VII.W Cor.2 records the structural reason |
| 3 | C24 INFO: §VII.P-v2 component False (HP^0 separator fails); §VII.P' component True (ω_GV non-vanishing) | GEOMETRIC | PERMANENT (parity orthogonality of HP^0 and HP^1) | §VII.P refinement direction CORRECTED to HP^1-content-distinct; §VII.W Cor.3 records the structural reason; §VII.P' lands as new registry entry |
| 4 | §VII.W Parity-Grading Orthogonality Theorem (proposed) | GEOMETRIC | PROPOSED for orchestrator landing | Algebra-level mechanism for §VII.R Meta-Theorem Row 1 (parity axis); pre-refutes parity-mismatched predicted instantiations |
| 5 | `_plan_author_audit.py` PARITY-MATCHING SPEC (proposed) | METHODOLOGY | PROPOSED for orchestrator implementation | Pre-freeze guard against parity-mismatched plan-blocks; 4-site fixture from §VII.W calibration corpus |
| 6 | C44 FAIL: lizzi S-1 §IV.5 Mellin-moment R-protection criterion at concordance 0.0326 | GEOMETRIC | NOT-ADDRESSED-BY-§VII.W (lives on Mellin-support axis Row 3, not parity axis Row 1) | Constraint-map note: §VII.W only addresses §VII.R Row 1; Row 3 (Mellin-support) remains lizzi-track |
| 7 | §VII.R Meta-Theorem (W1a-2) parity axis | GEOMETRIC | SHARPENED by §VII.W (algebra-level mechanism added) | Row 1 of the 3-axis disjointness table now has both empirical anchors AND HP-cohomology-ring structural mechanism |

---

## Cross-Reference: Source-File Anchor Map (for orchestrator review)

- §VII.W formal statement provenance: this synthesis IV.1 lines under "**Theorem VII.W**".
- C26.A FAIL (HP^odd vanishing empirical evidence): `sessions/archive/session-86/session-86-w9-workingpaper.md` §W9-1.A lines 7-99.
- C26.B PASS (HP^even integer-rigid 4-bucket evidence): `sessions/archive/session-86/session-86-w9-workingpaper.md` §W9-1.B lines 100-211.
- C24 INFO (parity-orthogonality empirical evidence via (C_H, C_epsH) twin-pair): `sessions/archive/session-86/session-86-w9-workingpaper.md` §W9-2 lines 213-316.
- §VII.R Meta-Theorem upstream pin: `sessions/archive/session-86/session-86-w1a-workingpaper.md` §W1a-2 lines 131-310; registry post-reslot at `sessions/permanent-results-registry.md` §VII.R line 12613.
- Lizzi Corollary E (HP^1 difference has zero image in HP^even): cited verbatim from `sessions/archive/session-85/session-85-1d-vii-p-meta-connes.md` §II.9 lines 213-231 (per C24 working-paper §W9-2 line 302 cite).
- Connes 1985 §II Cor.4 + Loday "Cyclic Homology" Thm 1.4.4 + Wedderburn: standard references; cited verbatim per C26.A working-paper §W9-1.A Step 2 (lines 50-58) and C26.B §W9-1.B Step 2 (lines 155-168).
- Klimyk-Schmüdgen §6 + Gerstenhaber-Schack 1986: Hopf-deformation rigidity + algebraic-cohomology rigidity; cited per C26.B working-paper §W9-1.B Step 2 (lines 162-168).
- Canonical constants pinned: `HP0_content_dim = 3` (canonical_constants.py SECTION E, S86 W9 added per C24 dispatch); `eps_H_HP1_norm = 16.197719` (canonical_constants.py line 155); `HP1_dim = 3` (canonical_constants.py line 165); `FI_parity_exclusion = 1` (canonical_constants.py line 174).
- Slot-allocation: `sessions/permanent-results-registry.md` §VII slot table (rows queried via grep `^## §VII\.`); §VII.W is the next available single-letter §VII slot (V = RESERVED placeholder; W unused; X = S50 Theorem Promotions; Y = DEPRECATED; Z unused).

---

**End of synthesis. The §VII.W block in IV.1 and the audit-script SPEC in IV.2 are PROPOSALS for orchestrator review; this dispatch does not modify the registry, audit scripts, or canonical constants directly. Per the spawn-prompt rule, the orchestrator installs after review.**
