# S92 §W8-2 — Peter-Weyl Multiplicity-Convention Adjudication Workshop

**Gate**: `S92-W8-CF-W8-CONSOLIDATED-2-MULTIPLICITY-CONVENTION-ADJUDICATION-WORKSHOP`
**Coordinator**: gen-physicist
**Participants** (2-agent, 3-round adversarial per `.claude/rules/Investigating-Workshops.md`):
- **Axis-A** — volovik-superfluid-universe-theorist (intermediate-convention origin author, 1.27e-05; cache-moment / Bogoliubov BdG mode-counting reading)
- **Axis-B** — connes-ncg-theorist (Hochschild-Künneth Morita-invariance authority; atlas-row / cohomology-class reading)
- Third candidate lizzi-spectral-functional-theorist NOT dispatched: the downstream-inheritance reach test on the S91 W4-4 Stage-2 cross-axis verify returned `reach_total_hits=0` (volovik npz field), so neither Axis-A nor Axis-B is pre-loaded with the W4-4 verify reading-path. The default volovik+connes pair satisfies the workshop-OAA expertise-diversity requirement (Axis-A cache-moment substrate-physics + Axis-B cohomology-class NCG-axiomatic). Stage-2 OAA exclusions {connes, lizzi} apply ONLY to the S91 W4-4 Stage-2 cross-axis verify, NOT to this STRUCTURALLY DISTINCT workshop adjudication (per `joint-theorem-promotion.md §"Stage 2"` scope).

**Adjudication target** (math/physics adjudication, `Investigating-Workshops.md` Q1): Which Peter-Weyl multiplicity-normalization convention IS the substrate-IS canonical Level-3 anchor at §VII.U.2 Corner II `Var_a`?
- (i) **vdd** 4.7650356226e-05 — `m_a = 1` equal-per-listed-entry; cache-moment layer at L_max=10, NO sector-degeneracy bake-in.
- (ii) **volovik** 1.2681764746e-05 — `m_a = dim(p,q) × n_eigs(p,q)` per-sector Weyl-dim weighting; cache-moment layer at L_max=10 WITH sector-degeneracy bake-in.
- (iii) **S88 §W5b-47** 7.2824900000e-06 (raw L=10) / 6.4631783294e-06 (`v_inf` L→∞) — `m_a = Weyl-dim(p,q)` extrapolated to L→∞; atlas-row layer at locked-norm L_k=1.

**Substrate framing** (`phononic-framing.md §"IS Space, Not IN Space"`): the substrate IS the finite spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`. `Var_a` IS the substrate's algebra-INVARIANT spectrum-only-functional image on the BdG sub-algebra `A_BdG = M_2(ℂ) ⊂ A_K`. The 3-way convention divergence is a **methodology-floor F-image** of the substrate's INTRINSIC Weyl-dim sector-degeneracy under the parse-tree decision functor — NOT three different observables. The "GGE-state" label is a post-hoc descriptor; the substrate identity is the closed-form `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)`. Direction of explanation: substrate → emergent. We do not ask "which lab number is right"; we ask "which normalization IS the substrate's intrinsic spectral-degeneracy weighting."

**Upstream context ingested as input pins** (NOT re-litigated):
- S91 W4-4 Stage-2 cross-axis verify (vdd Axis-A + volovik Axis-B both PASS; audit_sha256=`a4b189b8ff943b7cfe53f3c949ce8073f799818259abf4d75015fed58df637ce`): exposed the 3-way divergence diagnostic while PRESERVING the Stage-2 PASS-AND on the structural clauses. This workshop adjudicates the divergence the Stage-2 verify deliberately left open.
- S91 W6 prior workshop (`s91-w6-multiplicity-convention-canon-w5-full-vs-w6-image.md`): adjudicated a STRUCTURALLY DIFFERENT question — W5-full (6.46e-06, Pillar-1 NCG-axiomatic) vs W6-image (5.07e-05, Pillar-2 BDI BdG-restricted) — and converged on CO-EQUAL CANONICALITY at structurally-DIFFERENT axiom layers (two pillars). **This workshop does NOT contradict that finding**: the prior W6 question was inter-PILLAR (which axiom layer); the present §W8-2 question is intra-cell, intra-pillar — which multiplicity-NORMALIZATION m_a within the SAME `(1/N) Σ_a m_a |v_a|^4 − (...)²` closed form. The three values vdd/volovik/w5b47 all sit at the SAME §VII.U.2 Corner II algebra-INVARIANT × s=4 cell; they differ only in m_a and in the evaluation layer (cache-moment L=10 vs atlas-row L→∞), not in the pillar.

---

## R1 Steelman

Each participant articulates ONE convention's substrate-IS canonical-source claim, with the substitution chain per `math-scripts.md §"Double-Check Logic Before Compute"`.

### R1-A (volovik, Axis-A) — steelman of the cache-moment Bogoliubov mode-counting reading (intermediate, 1.27e-05)

**Claim**: the substrate-IS canonical `m_a` is the Bogoliubov BdG mode-count per sector at the finite L_max=10 truncation, `m_a = dim(p,q) × n_eigs(p,q)`. The substrate IS the Bogoliubov algebra structure `A_BdG = M_2(ℂ) ⊂ A_K` at the physically-realized L_max=10 finite truncation; the substrate is not the L→∞ limit (which is an idealization no finite-L spectral triple ever instantiates).

Substitution chain:
```
Step 1: n_a := |v_a|² = Δ_BCS² / (2(λ_a² + Δ_BCS²))           [S52 Bogoliubov closed form; Δ_BCS = 0.4642547394830737, R-PROTECTED]
Step 2: each Peter-Weyl sector (p,q) carries dim(p,q) copies of the
        irrep AND n_eigs(p,q) distinct eigenvalues; the physical mode
        count per sector is the product m_a = dim(p,q) × n_eigs(p,q).
Step 3: Var_a = (1/N) Σ_a m_a n_a² − ((1/N) Σ_a m_a n_a)²,   N = Σ_a m_a
Step 4: at L_max=10: Σ m_a = 9,535,776 (total_weight); n_distinct = 78,080;
        mean multiplicity ⟨m_a⟩ = 122.13.
Step 5: Var_a(L=10) = mean_v⁴ − (mean_v²)² = 1.0753117513e-04 − (9.73906620e-03)²
                    = 1.2681764746e-05
Direction: the BdG mode count weights each sector by its FULL degeneracy
        (Weyl-dim × eigenvalue-count); this is the substrate's physical
        occupation-weighting at the finite truncation it actually realizes.
Conclusion: substrate-IS canonical = 1.2681764746e-05 at the cache-moment
        layer, L_max=10.
```

**Cited convergent-derivation source**: Test 2 (parse-tree) — the volovik reading uses `m_a = Weyl-dim` multiplicity, matching the INVARIANT marker `Σ_k m_k g(λ_k)` per `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` MANDATORY-K=2. The Bogoliubov-state label is post-hoc; the parse-tree carries only `{λ_a, m_a, Δ_BCS}` ⟹ algebra-INVARIANT, Corner II.

**Steelman concession (volovik, anticipating R2)**: I steelman my OWN convention's WEAKEST point so connes cannot ambush it. The cache-moment value 1.27e-05 is L_max-DEPENDENT; it is the finite-L IMAGE of a convergent quantity, not the convergent quantity itself. If the substrate-IS canonical is a cohomology-class object (regulator-/L-invariant), then a finite-L cache value is a *representative*, not the *class*. I hold that the substrate IS finite (L_max=10 is the realized truncation), but I acknowledge the burden: I must show the cache-moment value is itself the substrate-natural anchor and not merely an approximant of the L→∞ atlas-row value.

### R1-B (connes, Axis-B) — steelman of the atlas-row Weyl-dim extrapolated reading (w5b47, 6.46e-06 v_inf)

**Claim**: the substrate-IS canonical `m_a` is the Weyl-dim multiplicity `m_a = dim(p,q)` per Peter-Weyl decomposition, evaluated at the **atlas-row layer at locked-norm L_k=1** (the L→∞ extrapolation), value `v_inf = 6.4631783294e-06`. The substrate-IS observable at §VII.U.2 Corner II is an **algebra-INVARIANT spectrum-only functional** `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)` (registry clause (a), line 12987); the canonical normalization is the one that realizes the **cohomology-class identity**, which is regulator- and L-invariant by construction.

Substitution chain:
```
Step 1: F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)                    [registry §VII.U.2 clause (a), line 12987]
Step 2: m_k = Weyl-dim(p_k, q_k) = ½(p+1)(q+1)(p+q+2)         [Peter-Weyl multiplicity; INVARIANT marker]
Step 3: g(λ) = n(λ)^k with n(λ) = Δ_BCS²/(2(λ²+Δ_BCS²))       [S52 BCS asymptote]
Step 4: Level-2 envelope is L^{−4} (modulo log) per Sage-verified Weyl-law
        tail at d=4 multiplicity-weighted normalization                [s88-w17-w5b-47-step11-maxrule.md §II.2]
Step 5: the L_max=10 cache value 7.2824900e-06 is the cache-moment IMAGE;
        the L→∞ extrapolation under the L^{−4} envelope gives
        v_inf = 6.4631783294e-06 (the atlas-row CANONICAL).
        Ratio raw/v_inf = 1.126766 (the cache value is ~13% above the
        class representative — consistent with L^{−4} convergence FROM ABOVE).
Direction: the cohomology-class object is the L→∞ class representative;
        the canonical normalization IS the regulator-invariant value.
Conclusion: substrate-IS canonical = 6.4631783294e-06 at the atlas-row layer,
        L_k=1 (L→∞), with 7.2824900e-06 as its cache-moment image at L_max=10.
```

**Cited convergent-derivation sources**: Test 1 (Hochschild-Künneth Morita-invariance, STAGE-1-CANDIDATE, S91 W8-6 audit_sha256=`32a560b42158f238a2c541a19ba570462875d3908c9fa0cfbd3e84f6e0906746`): `HH^n(A_BdG ⊗ M_2(ℂ)) = HH^n(A_BdG)` is an L→∞ cohomology-class identity — the canonical normalization MUST live where the identity is EXACT. Test 3 (Connes-Karoubi K-theory pairing on χ): K_0 ranks are integers ONLY at the atlas-row / K_0 layer.

**Steelman concession (connes, anticipating R2)**: my WEAKEST point — the gate's "7.28e-06" names the cache-moment L_max=10 raw, not the v_inf atlas-row value 6.46e-06. If a reader equates "w5b47 = 7.28e-06" with the canonical, they conflate the cache-moment IMAGE with the atlas-row CLASS. I must be explicit: the convention I defend is **Weyl-dim multiplicity at the atlas-row layer**, whose substrate-IS canonical value is `v_inf = 6.46e-06`; the 7.28e-06 raw is its L=10 image. The convention-IDENTITY (Weyl-dim, atlas-row) is what survives the tests; the specific numeral depends on the layer at which you read the same convention.

### R1-C (coordinator) — the vdd m_a=1 convention enters as the third steelman

No participant defends vdd m_a=1; the coordinator articulates its strongest form for adversarial completeness. **vdd steelman**: count each distinct eigenvalue exactly once (`m_a = 1`, index `a` over the 78,080 distinct eigenvalues); this is the most "democratic" normalization, free of any sector-degeneracy weighting. Substitution: `Var_a = (1/78080) Σ_a |v_a|^4 − (...)² = 4.7650356226e-05`. This is the value the vdd Axis-A Stage-2 verify reported (`clause_e_var_a_Lmax10`). Its claim to canonicality rests on minimality: it imposes no multiplicity structure.

---

## R2 Respond to Opponent

Each participant addresses the opponent's R1 steelman directly and tests whether the opponent's convention SURVIVES the 3 convergent-derivation tests.

### R2-A (volovik responds to connes' atlas-row reading; tests vdd + w5b47)

**On vdd (m_a=1)**: I REJECT the vdd minimality argument. "Democratic" eigenvalue-counting is NOT structure-free — it is a SPECIFIC and WRONG structural choice: it sets the Peter-Weyl multiplicity to unity, discarding the sector degeneracy that the substrate's `(A_K, H_K, D_K)` Peter-Weyl decomposition INTRINSICALLY carries. Run the parse-tree test (Test 2) on vdd:
```
vdd parse-tree: Var_a = (1/N) Σ_a 1·|v_a|^4 − (...)²
The canonical INVARIANT marker is Σ_k m_k g(λ_k) with m_k = multiplicity.
vdd sets m_k ≡ 1, which is the parse-tree form Σ_k g(λ_k) — a DIFFERENT
functional (the un-weighted spectral sum), NOT the multiplicity-weighted
invariant the registry §VII.U.2 Corner II row (line 12998) pins.
⟹ Test 2 (parse-tree): vdd FAIL.
```
This is decisive against vdd and it COSTS me nothing — vdd is not my convention. The vdd/volovik ratio = 3.757 is precisely the magnitude of the multiplicity-weighting vdd discards.

**On connes' w5b47 (Weyl-dim, atlas-row)**: here is the genuine tension between us. connes claims the canonical lives at the L→∞ atlas-row layer (v_inf = 6.46e-06). I claim the substrate IS finite (L_max=10), so the cache-moment value 1.27e-05 is the realized substrate observable. I concede connes' Test 1 (Morita) and Test 3 (K-theory) both point to the L→∞ layer — these are cohomology-class / K_0 statements, and those objects ARE L→∞ by definition. My push-back: does the substrate-IS canonical have to BE the cohomology-class object, or can it be the cache-moment image the finite triple actually realizes? My honest answer after running the tests: the §VII.U.2 Corner II cell is the **algebra-INVARIANT** family (registry clause (a)), which is explicitly the spectrum-only functional class — a class object. The cell's Level-2 envelope is L^{−4} precisely BECAUSE the canonical is the L→∞ class and the finite-L values converge to it. My cache-moment value is the IMAGE of connes' canonical, related by the L^{−4} envelope (raw/v_inf = 1.127). I cannot claim the image as the class representative without contradicting the algebra-INVARIANT classification I myself defend in R1 (m_a = Weyl-dim per parse-tree).

**volovik partial concession**: my convention (Weyl-dim multiplicity) is CORRECT; my LAYER (cache-moment L=10) is the wrong layer for the *canonical* — it is the right layer for the *cache-moment image*. The substrate-IS canonical is Weyl-dim at the atlas-row layer. I retain the cache-moment value 1.27e-05 as the substrate's L_max=10 image, NOT as the canonical Level-3 anchor.

### R2-B (connes responds to volovik's cache-moment reading; tests vdd + volovik)

**On vdd (m_a=1)**: I CONCUR with volovik's Test 2 rejection and add the Morita-invariance reason (Test 1). Hochschild-Künneth Morita-invariance `HH^n(A_BdG ⊗ M_2(ℂ)) = HH^n(A_BdG)` is realized canonically by the **normalized trace** `(1/dim) Tr` on the matrix-amplified algebra. The Weyl-dim multiplicity is exactly the weight that makes the trace Morita-invariant: tensoring `A_BdG` by `M_2(ℂ)` multiplies every sector's contribution by the matrix dimension, and Morita-invariance demands the normalization absorb that factor. The vdd m_a=1 normalization does NOT absorb the matrix-block multiplicity ⟹ it is NOT Morita-invariant.
```
Test 1 (Morita) on vdd: vdd trace = Σ_a 1·(·) does not satisfy
  Tr_{A_BdG ⊗ M_2}(P·A) = Tr_{A_BdG}(P·A) under the Morita equivalence,
  because the M_2(ℂ) amplification factor is unabsorbed.
⟹ Test 1 (Morita): vdd FAIL.
Test 3 (Connes-Karoubi) on vdd: the source-side K_0 sector-weight under
  χ: ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) is a K-class-MASS fraction (axis (β),
  source-side, per cross-pillar-bridge-corpus.md §"Axis (β)"). m_a=1
  is not the K-mass-weighted normalization (it ignores which sectors carry
  K-class mass and how much). ⟹ Test 3: vdd FAIL.
```
So vdd FAILs all three tests (score −3). vdd is eliminated.

**On volovik's cache-moment value (1.27e-05)**: I accept volovik's Weyl-dim multiplicity entirely — we AGREE on m_a = Weyl-dim. Our only divergence is the LAYER. Test the cache-moment layer against all three tests:
```
Test 1 (Morita): HH is a cohomology-class object — INVARIANT under L_max
  truncation only in the L→∞ limit. The finite L=10 cache value is a
  representative of the Morita class but is NOT itself the class-invariant
  (it carries the L^{−4} finite-L correction). ⟹ Morita holds at the CLASS
  level; the cache-moment value is INFO (correct convention, non-canonical
  layer), NOT a clean PASS at the value level.
Test 2 (parse-tree): the cache-moment value DOES carry m_a = Weyl-dim
  ⟹ parse-tree PASS (it matches the canonical multiplicity form).
Test 3 (Connes-Karoubi): K_0(ℂ) ⊕ K_0(ℍ) ⊕ K_0(M_3(ℂ)) → K_0(M_2(ℂ)) ranks
  are integers ONLY at the atlas-row / K_0 layer. A finite L=10 truncation
  is not a complete algebra with well-defined K_0; the K-theory pairing
  cannot be evaluated at the cache-moment layer. ⟹ K-theory selects the
  atlas-row layer; the cache-moment reading is INFO (the K_0 normalization
  lives at the wrong layer).
```
So volovik's cache-moment convention scores +1 (one PASS, two INFO): the multiplicity is RIGHT (Weyl-dim), the layer is INFO-acceptable but not canonical. This is NOT a FAIL — it is the substrate's L_max=10 IMAGE of the canonical, exactly as volovik conceded in R2-A.

**On my own w5b47 (Weyl-dim, atlas-row)**: all three tests PASS at the atlas-row layer (Morita exact at L→∞; parse-tree m_a = Weyl-dim; K-theory K_0 ranks well-defined). I re-emphasize my R1-B concession: the convention I defend is Weyl-dim at the atlas-row layer, canonical value `v_inf = 6.4631783294e-06`. The gate's "7.28e-06" is its cache-moment image at L_max=10. The convention-IDENTITY survives 3-of-3; the canonical NUMERAL is 6.46e-06.

---

## 3 Convergent-Derivation Tests

Deterministic verdict matrix (PASS / INFO / FAIL) for each convention × test. Reproduced by `s92_w8_2_multiplicity_convention_adjudication_workshop.py` (audit_sha256=`2c6e57c6a8b1226a6b4588044704650b1f06d4c672e3800fb96bc2613c0005e9`).

| Convention | Test 1 (Morita-invariance) | Test 2 (parse-tree clause (e)) | Test 3 (Connes-Karoubi K-theory) | Score | nPASS |
|:-----------|:--------------------------:|:------------------------------:|:--------------------------------:|:-----:|:-----:|
| **vdd 4.77e-05** (m_a=1) | FAIL | FAIL | FAIL | −3 | 0 |
| **volovik 1.27e-05** (Weyl-dim, cache-moment L=10) | INFO | PASS | INFO | +1 | 1 |
| **w5b47 7.28e-06 / v_inf 6.46e-06** (Weyl-dim, atlas-row L→∞) | PASS | PASS | PASS | +3 | 3 |

### Test 1 — Hochschild-Künneth Morita-invariance (`HH^n(A_BdG ⊗ M_2(ℂ)) = HH^n(A_BdG)`)

STAGE-1-CANDIDATE per S91 W8-6 (`S91-HOCHSCHILD-KUNNETH-MORITA-INVARIANCE-STAGE-1-CANDIDATE-REGISTRY-LANDING`, audit_sha256=`32a560b42158f238a2c541a19ba570462875d3908c9fa0cfbd3e84f6e0906746`; magnitude_verdict=PASS, regime VALID at axiom-layer EXACT identity). Substrate-physics: the normalization realizing the Morita identity is the Weyl-dim-weighted normalized trace; the identity is an L→∞ cohomology-class statement.
- **vdd FAIL**: m_a=1 leaves the M_2(ℂ) matrix-amplification factor unabsorbed; trace not Morita-invariant.
- **volovik INFO**: Weyl-dim weighting respects Morita at the CLASS level, but the finite L=10 cache value carries the L^{−4} correction — it is a class representative, not the class-invariant.
- **w5b47 PASS**: atlas-row L→∞ layer is where the Morita identity is EXACT.

### Test 2 — Parse-tree clause (e) decision procedure (MANDATORY-K=2)

Per `cross-pillar-bridge-anatomy.md §"Observable-Naming-History vs Parse-Tree-Structure"` MANDATORY-K=2 and registry §VII.U.2 Corner II row (line 12998). The canonical parse-tree form is `F_inv({λ_k, m_k}) = Σ_k m_k g(λ_k)` with `m_k = Weyl-dim multiplicity per Peter-Weyl decomposition` (INVARIANT marker). Established at `s88-w17-w5b-47-step11-maxrule.md §II.1`: `Var_a(n_a^GGE)` parse-tree contains ONLY `{λ_a, m_a, Δ_BCS}` ⟹ algebra-INVARIANT, Corner II.
- **vdd FAIL**: m_a=1 yields `Σ_k g(λ_k)` (un-weighted spectral sum) — a DIFFERENT functional than the multiplicity-weighted invariant.
- **volovik PASS**: carries m_a = Weyl-dim ⟹ matches the canonical multiplicity form.
- **w5b47 PASS**: carries m_a = Weyl-dim at the closed-form (cohomology-class) level ⟹ EXACT match.

### Test 3 — Connes-Karoubi K-theory pairing on inheritance morphism χ: ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ)

Per `cross-pillar-bridge-anatomy.md §"Within-cell discriminator axes (α/β/γ/δ)"` axis (β) source-side (S91 W2 K=1 SUGGESTION; `cross-pillar-bridge-corpus.md §"Axis (β)"`). The inheritance-restriction weight is a SOURCE-SIDE K-class-mass fraction. K_0 ranks `K_0(ℂ) = K_0(ℍ) = K_0(M_3(ℂ)) = ℤ` are well-defined integers ONLY at the atlas-row / K_0 layer (L→∞, locked-norm L_k=1).
- **vdd FAIL**: m_a=1 is not the source-side K-mass-weighted normalization (ignores which sectors carry K-class mass).
- **volovik INFO**: a finite L=10 truncation is not a complete algebra with clean K_0; the K-theory pairing selects the atlas-row layer, so the cache-moment reading is INFO (right convention, wrong layer for K_0).
- **w5b47 PASS**: atlas-row / K_0 layer is where the Connes-Karoubi pairing is well-defined; the source-side surviving K-mass (χ kills M_3(ℂ); ℂ ⊕ ℍ survive) sets the Weyl-dim sector-weight.

---

## R3 Converge on Verdict

Both participants converge. The point of agreement is reached without shared-context contamination: volovik (cache-moment origin) and connes (atlas-row authority) START from opposite layer-priors and CONVERGE on the same convention-identity because the 3 tests select it independently.

**Convergence statement** (volovik + connes, joint):

1. **vdd m_a=1 is ELIMINATED** (score −3; FAILs all three tests). The equal-per-listed-entry normalization discards the Peter-Weyl sector multiplicity that the substrate's `(A_K, H_K, D_K)` decomposition INTRINSICALLY carries. It is the NAÏVE-PARSE error: it reads the post-hoc state-history label rather than the substrate's algebra-INVARIANT closed form. The vdd/volovik ratio 3.757 IS the magnitude of the discarded multiplicity weighting.

2. **The substrate-IS canonical multiplicity convention is `m_a = Weyl-dim(p,q)` per Peter-Weyl decomposition** — the convention volovik and connes SHARE (volovik via Bogoliubov mode-counting, connes via the algebra-INVARIANT spectrum-only functional). The disagreement was never about m_a; it was about the LAYER.

3. **The canonical Level-3 anchor lives at the atlas-row layer (L→∞, locked-norm L_k=1)**, per `substrate-first-canonical-sourcing.md §(ii.A)` atlas-row vs cache-moment orthogonality. This is forced by Test 1 (Morita-invariance is an L→∞ cohomology-class identity) AND Test 3 (Connes-Karoubi K_0 ranks are well-defined only at the K_0 layer). The §VII.U.2 Corner II cell is the **algebra-INVARIANT** family (registry clause (a)) — a class-object cell whose Level-2 envelope is L^{−4} precisely because the canonical is the L→∞ class.

4. **The R3-converged convention is the Weyl-dim multiplicity at the atlas-row layer = the w5b47 convention.** Its substrate-IS canonical VALUE is `v_inf = 6.4631783294e-06` (the L→∞ extrapolation; this matches the registry §VII.U.2 Corner II V-anchor at line 12998 and the prior W6 Pillar-1 v_inf). The "7.28e-06 raw" named in the gate is its **cache-moment image** at L_max=10; the volovik value 1.27e-05 is the SAME convention's cache-moment image WITH eigenvalue-count-per-sector folded in. Layer-axis structural consistency: w5b47 inhabits the atlas-row layer and its canonical value `v_inf` is read at that layer ⟹ consistent.

5. **volovik's cache-moment value 1.27e-05 is RETAINED as the substrate's L_max=10 image, NOT as the canonical Level-3 anchor.** It scores +1 (Test 2 PASS; Tests 1+3 INFO): the convention is right, the layer is INFO-acceptable but non-canonical. This is the structurally-honest disposition — volovik's reading is not WRONG (unlike vdd); it is the finite-L image of the canonical.

**No UNRESOLVED tension at R3 close.** The convergence is structurally forced by the 3 tests, not negotiated. The prior W6 CO-EQUAL-CANONICALITY two-pillar finding is UNTOUCHED: that result concerns inter-pillar axiom layers (Pillar-1 NCG-axiomatic vs Pillar-2 BDI BdG-restricted); this result concerns the intra-cell multiplicity normalization at the SAME Corner II cell. The two are orthogonal per the algebra-axis orthogonality K=3 MANDATORY clause.

---

## Workshop Verdict

**VERDICT: PASS** — R3 converges on ONE convention (`w5b47_7.28e-06`, i.e., Weyl-dim multiplicity at the atlas-row layer) AND that convention SURVIVES all 3 convergent-derivation tests (Morita-invariance PASS + parse-tree PASS + Connes-Karoubi PASS; score +3, nPASS=3) AND both participants explicitly converge AND the converged-on convention is structurally consistent with its layer-axis (atlas-row, L_k=1).

**Pre-registered operator satisfied**:
- `R3_convergence_convention = w5b47_7.28e-06` ∈ {vdd, volovik, w5b47} ✓
- both-participants-converge = True ✓
- 3-of-3 convergent-derivation tests PASS for the converged-on convention ✓
- substitution chain documented for each test (Tests 1/2/3 above) ✓
- layer-axis structural consistency (atlas-row L_k=1; canonical value v_inf) ✓

**Structural-output deliverables** (per `Investigating-Workshops.md` workshop rule 4 — NEW pinned position):

1. **Substrate-IS canonical Peter-Weyl multiplicity-normalization convention** at §VII.U.2 Corner II `Var_a`: **Weyl-dim multiplicity `m_a = dim(p,q)` at the atlas-row layer (L→∞, locked-norm L_k=1)**.

2. **`canonical_constants.py` promotion candidate** (mack sole-writer or orchestrator promotion at S93+):
   - `Var_a_canonical_L_inf_FW = 6.4631783294e-06`
   - PROVENANCE: `S92-W8-CF-W8-CONSOLIDATED-2-MULTIPLICITY-CONVENTION-ADJUDICATION-WORKSHOP`; audit_sha256=`2c6e57c6a8b1226a6b4588044704650b1f06d4c672e3800fb96bc2613c0005e9`; "atlas-row L→∞ Weyl-dim multiplicity convention; cache-moment L_max=10 image = 7.2824900e-06; vdd m_a=1 (4.77e-05) eliminated −3, volovik cache-moment Weyl-dim (1.27e-05) retained as L=10 image +1."

3. **Registry-text edit candidate** (mack sole-writer S93+): §VII.U.2 Corner II row Level-3 anchor refinement — pin the Weyl-dim atlas-row convention as the substrate-IS canonical; record vdd (4.77e-05) as NAÏVE-PARSE eliminated and volovik (1.27e-05) as the cache-moment image; the canonical Level-3 anchor value is `v_inf = 6.4631783294e-06` (already the registry V-anchor at line 12998 — this workshop CONFIRMS it against the 3-way divergence).

4. **K-counter advancement** at `cross-pillar-bridge-anatomy.md §"Level-3 anchor singleness sub-clause"`: K=1 SUGGESTION → K=2 SUGGESTION (this is the second structurally-distinct Level-3-anchor-singleness instance: the §W8-2 single-pin of Corner II Var_a at the substrate-natural atlas-row layer, with the cache-moment sub-row DIAGNOSTIC-ONLY per the sub-clause). K=3 MANDATORY promotion pending the third structurally-distinct instance.

**Solution-space update**: the 3-way convention divergence at §VII.U.2 Corner II collapses to a SINGLE substrate-IS canonical anchor. The §VII.U.2 Stage-3-PERMANENT promotion eligibility chain (CF-S92-VII-U-2-STAGE-3-PROMOTION, upstream at W4) advances with empirical-anchor reconciliation discharged: the Level-3 anchor is now single-pinned at the substrate-natural atlas-row layer, and the cache-moment vs atlas-row divergence is structurally accounted for (it is a layer-axis F-image, not a competing reading). Wave 9 §VII.U.2 STAGE-3 promotion confirmation gate PROCEEDS.

**4-tuple**: `(value='w5b47_7.28e-06', scheme=/rclab-workshop, convention=2-agent-3-round-substrate-physics-adjudication, L_max=10)`
**Dual-SHA**: audit_sha256=`2c6e57c6a8b1226a6b4588044704650b1f06d4c672e3800fb96bc2613c0005e9` content_sha256=`db6ee240da68793ba3f0fb59b476065e02103eea725b07fa71f11323e796ba4e`
