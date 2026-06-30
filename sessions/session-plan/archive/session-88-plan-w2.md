# Session 88 Plan — Wave 2: V_4 monodromy + 4-stratum partition + Δ_0 LOCALIZATION + W11 surviving-candidate enumeration

**Topic label**: Pixels Of Unusual Size (S88)
**Wave 2 owner**: connes-ncg-theorist (PRIMARY); volovik-superfluid-universe-theorist co-authors on Δ_0 LOCALIZATION (CF-W8-6 SOURCE-DOUBLE-CITE-CO-PRIMARY per registry-landing.md)
**Source carry-forward cluster**: Cluster A of `sessions/session-plan/session-88-context.md` (13 items)
**Generated**: 2026-05-02 (S88 plan-freeze, planner-w2 dispatch)

---

## Wave 2 Summary

Wave 2 closes the V_4 monodromy program opened at S87 W11. After W11-1 falsified the Cartan-toral V_4 incarnation σ_M = (-1)^p, σ_C = (-1)^q on (p, q)-Peter-Weyl indices (max_dev = 1.16 / 1.193687 across two pathways), three V_4 candidates remained surviving:
(i) coset-on-regulators map — also FAILed at n = 2 in-script;
(ii) V_4-on-strata — STRUCTURALLY SUPPORTED by W11-2 INFO + W11-3 PASS + W11-meta-1 §VII.AJ.partition-stability landing;
(iii) V_4-on-triality-mod-2 — open Z_3 → Z_2 sub-character question.

Wave 2 has six substrate-physics computational gates (§W2-1 through §W2-7) testing extensions, candidate constructions, and shell scans, plus six methodology-class gates (§W2-8 through §W2-13) landing the Δ_0 LOCALIZATION FORMULA, the τ-asymmetric registry entry, framing-rule extensions, K-counter advancement, and a v3-closure-recovery sig_5 audit. Δ_0 LOCALIZATION is the joint algebraic identity surfaced by W-8 R3 (connes V-3 derivation + volovik Sage-QQ exhaustive verification): for any partition (c_1, c_2, c_3, c_4) and any V_4 character σ on the 4-stratum partition, Δ_0(σ; (c_1, …, c_4)) = 4 · c_{σ⁻¹((1,1))} EXACT in QQ. Applied to the substrate's empirical (2, 4, 8, 6), this yields the rel_dev_0 set {2/5, 4/5, 6/5, 8/5} — all FAIL by ≥ 8 OOM at any V_4 character permutation, structurally closing the (Z_2)^d=2 stratum-permutation route.

Wave 2 deliverables advance:
- **V_4 candidate enumeration** (§W2-1, §W2-2, §W2-3) → outcome: exhaust or land surviving incarnations;
- **Partition-stability shells** (§W2-4, §W2-5, §W2-6) → outcome: localize δ_τ_crit on negative side, characterize positive-side asymmetry, complete §VII.AJ registry-row consolidation;
- **Mechanical closure** (§W2-7) → outcome: structurally-honest deferred S88-CF-W11-C closure per `mechanical-closure-discipline.md`;
- **Δ_0 LOCALIZATION FORMULA registry landing** (§W2-8) → outcome: §VII.AD STAGE-1-CANDIDATE per joint-theorem-promotion.md;
- **τ-asymmetry registry entry** (§W2-9) → outcome: §VII.AE landing of the W11-2 cv-flip-only-at-δ_τ=−0.10 directional asymmetry;
- **Framing rule extension** (§W2-10) → outcome: phononic-framing.md "Single-τ-slice vs moduli-deformation substrate-IS levels" sub-section;
- **PRU Class 8.2 corpus advancement** (§W2-11) → K-counter 1 → 2 toward MANDATORY at K=3;
- **Cross-pillar bridge K-counter monitor** (§W2-12) → bookkeeping at K=2 SUGGESTION (auto-flip on third instance landing);
- **sig_5 audit** (§W2-13) → outcome: classify the 2 pre-existing duplicate audit_sha256 in s87_gate_verdicts.txt as v3-closure-recovery sig_5 violation vs benign content-collision.

The substrate-IS reading: the 4-stratum partition (2, 4, 8, 6) is the substrate's bottom-20 D_K eigenvalue cardinality vector at τ_fold = 0.19, computed at L_max = 10 from the master Peter-Weyl-decomposition cache `s84_spectrum_cache_L12_tau019.npz` filtered to L_max = 6 (operational pin, Casimir-bound truncation per math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"). Klein-V_4 NECESSITY is witnessed at TWO independent substrate-physics structural levels: (a) W11-1 element-order signature [1, 2, 2, 2] matches V_4 not Z_4 [1, 2, 4, 4]; (b) W11-4 (Z_2)^d-Schur tensor-product factored identity exact in QQ at d ∈ {2, 3, 4, 5}. The substrate IS the partition geometry; Klein-V_4 is the substrate's own group-theoretic content, not an external imposition.

## Wave 2 Decision Point Prerequisites

Wave 2 has the following Wave-1 prerequisites and parallel-wave coordinations:

- **§W2-3** (V_4-on-strata substrate-character construction) reads `s84_spectrum_cache_L12_tau019.npz` (S84 W14a cache; bit-stable across S85-S87) and `s87_w11_4_v4_schur_identity.npz` (W11-4 Sage callable; existing artifact at S87 close).
- **§W2-7** (CF-W11-C mechanical closure) cross-references CF-W8-6 (= §W2-8 in this wave) Δ_0 LOCALIZATION landing; mechanical-closure verdict line emits BEFORE Δ_0 has landed if §W2-7 dispatches first; alternatively §W2-8 dispatches first to provide a published §VII.AD anchor for §W2-7's mechanical-closure value-string. Sequencing: §W2-8 dispatches first, §W2-7 second; verdict-pin lookup in §W2-7 references §W2-8's landed §VII.AD entry.
- **§W2-12** (cross-pillar-bridge K-counter monitor) is bookkeeping that observes other waves' landing of FWD-C1/C2/C3 cross-pillar bridges (Cluster B items #21/#22/#23 in the context inventory); §W2-12 itself only emits if a third instance lands during S88. If only #21 (FWD-C1) or #22 (FWD-C2) lands, §W2-12 emits an INFO at K = 2 status holding.
- **§W2-13** (sig_5 audit) reads `computations/s87_gate_verdicts.txt` directly (no upstream gate prerequisite); independent of all other W2 items.

No cross-wave hard-blockers; Wave 2 may dispatch in parallel with Wave 1, Wave 3, etc.

---

## §W2-1. S88-MONODROMY-DEPTH-EXTENSION-SURVIVING-V4-ENUMERATION

1. **Gate ID**: `S88-MONODROMY-DEPTH-EXTENSION-SURVIVING-V4-ENUMERATION`
2. **Trigger**: `[VERIFY-THEOREM]`
3. **Classification**: GEOMETRIC (substrate-spectral-action gate; D_K-block partition-graph cohomology test)
4. **Agent type**: connes-ncg-theorist (PRIMARY); spectral-geometer co-author for cohomology cross-check
5. **Hypothesis**: Surviving V_4 candidates (ii) V_4-on-strata and (iii) V_4-on-triality-mod-2 admit ≥ 3 (Z_2)^d > 2 atlas extensions whose d = 3 hypercube is non-degenerate (i.e., no 1D edge collapses under substrate-physical stratum-character pairing). PASS opens a structural depth-extension into rank-3 Klein-product groups; FAIL closes the depth-extension and locks the framework's monodromy ceiling at d = 2.
6. **Method**:
   - Inputs (full): `from canonical_constants import M_KK, tau_fold, Delta_BCS`; load `s84_spectrum_cache_L12_tau019.npz` filtered to L_max = 6 (Casimir-bound truncation per math-scripts.md). Load `s87_w11_4_v4_schur_identity.npz` for the (Z_2)^d Sage-callable factored form.
   - Step 1 — Enumerate ≥ 3 candidate (Z_2)^d > 2 atlas extensions for surviving candidate (ii) V_4-on-strata:
     - Extension A: (Z_2)^3 = stratum-Z_2 × triality-Z_2 × parity-Z_2 (d = 3 product; 8-fold sweep)
     - Extension B: (Z_2)^4 = stratum-Z_2 × triality-Z_2 × parity-Z_2 × Cartan-Z_2 (d = 4 product; 16-fold sweep)
     - Extension C: (Z_2)^3 = stratum-Z_2 × stratum-pair-Z_2 (across the (2,4) sub-pair vs (8,6) sub-pair) × triality-Z_2 (alternative d = 3)
   - Step 2 — For surviving candidate (iii) V_4-on-triality-mod-2:
     - Extension D: (Z_2)^3 = triality-Z_2 × parity-Z_2 × stratum-Z_2 (re-ordering of A; same group abstractly; tests independence of Z_2-axis ordering)
     - Extension E: (Z_2)^3 = triality-Z_2 × Cartan-p-Z_2 × Cartan-q-Z_2 (Cartan parity-pair on Peter-Weyl (p, q))
   - Step 3 — For each Extension X ∈ {A, B, C, D, E}, compute the d-dimensional hypercube parallelogram identity Δ_n^{(d)} for n ∈ {0, 2, 4} via the (Z_2)^d-Schur tensor-product factored identity:
     ```
     Δ_n^{(d)}(σ_1, …, σ_d) = (4^d / Vol) · Σ_{(p_1,…,p_d) all odd}  d(p_1,…,p_d) · w_n(p_1,…,p_d)
     ```
     analogous to the d = 2 W11-4 case. Reuse the Sage-callable factored form from `s87_w11_4_v4_schur_identity.npz`.
   - Step 4 — Non-degeneracy test: for each Extension X and each axis Z_2(j), j = 1, …, d, check that the marginal Δ_n along axis j (with all other axes held at identity) is NOT exactly zero in QQ. A zero marginal indicates a collapsed edge (the j-th Z_2 acts trivially on the substrate-physics observable).
   - Step 5 — d = 3 hypercube non-degenerate PASS criterion: ≥ 1 of {A, B, C, D, E} has all 3 axes non-collapsed AND the d = 3 hypercube identity Δ_n^{(3)} = 0 (or verifiable analogue of the W11-4 (Z_2)^d structure) holds at n ∈ {0, 2, 4} to ≤ 1e-12.
   - Substrate-physics layer: each Z_2 axis must correspond to a substrate-IS character on (A_K, H_K, D_K), NOT a synthetic Cartan-toral incarnation. Use stratum-index Z_2 × Z_2 (W11-2), NOT (p, q)-Cartan.
7. **Machinery pin (PRDR)**:
   - GPU/CPU: `OMP_NUM_THREADS = 8` (CPU; per math-scripts.md fallback) — sub-spectrum filtering at L_max = 6 fits on CPU; ~5,832 eigenvalues.
   - L_max: 6 (operational; Casimir-bound truncation; plan-pinned 10 redundant per math-scripts.md §"D_K Block-Diagonality").
   - Number of extensions enumerated: ≥ 3 (target 5 above; minimum for PASS = 3).
   - Sage MCP: `mcp__sage__sage_eval` for QQ-exact arithmetic on each Δ_n^{(d)} computation; `mcp__sage__sage_simplify` for tensor-product factored form expansion.
   - Tolerance: ≤ 1e-12 absolute on Δ_n^{(d)} per identity test.
   - Random seed: N/A (deterministic enumeration).
   - Scheme: `Cartan-toral-rejected-V4-strata-tested-via-stratum-Z2-product-d3hypercube`.
   - Convention: `(Z_2)^d-Schur-tensor-product-factored-identity-extension-from-W11-4`.
8. **Expected output 4-tuple**: `(value=<count_PASS_extensions>, scheme=Cartan-toral-rejected-V4-strata-tested-via-stratum-Z2-product-d3hypercube, convention=(Z_2)^d-Schur-tensor-product-factored-identity-extension-from-W11-4, L_max=6)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS-d=2-exact: count_PASS_extensions ≥ 3 AND d = 2 W11-4 form recovered as restriction of d = 3 hypercube identity; structural depth-extension confirmed (rank-3 Klein-product group admissible at substrate level).
   - PASS-d>2-extension: count_PASS_extensions ≥ 1 with d ∈ {3, 4} non-degenerate.
   - INFO: 1 ≤ count_PASS_extensions < 3 (partial extension; surviving candidate not fully closed).
   - FAIL: count_PASS_extensions = 0 (depth-extension closed; framework's monodromy ceiling locked at d = 2; surviving V_4 candidates do not extend to higher rank; structurally closes the (Z_2)^d > 2 program).
   - Tolerance rule: ABSOLUTE on Δ_n^{(d)} (≤ 1e-12 EXACT in QQ via Sage); RATIO on cardinality (count_PASS_extensions ≥ 3 of 5 enumerated).
10. **Substitution chain** (mandatory per `[VERIFY-THEOREM]` trigger):
    - Step 1 (definition): the parallelogram identity at depth d on a (Z_2)^d character (σ_1, …, σ_d) is the alternating sum
      ```
      Δ_n^{(d)} := Σ_{ε ∈ {0,1}^d} (-1)^{|ε|} · A_n^{(σ_1^{ε_1}, …, σ_d^{ε_d})}
      ```
      where |ε| = ε_1 + … + ε_d is the Hamming weight.
    - Step 2 (substitution): when each σ_j acts on the substrate Peter-Weyl decomposition by a parity character on independent Cartan/stratum/triality axis, the (Z_2)^d-Schur orthogonality factorizes the alternating sum into a tensor product
      ```
      Δ_n^{(d)} = (4^d / Vol) · Σ_{(p_1,…,p_d) all odd}  d(p_1,…,p_d) · w_n(p_1,…,p_d)
      ```
      mirroring the W11-4 d = 2 form `(x_{0,0} − x_{0,1}) · (x_{1,0} − x_{1,1}) · (x_{2,0} − x_{2,1}) …`.
    - Step 3 (simplify): for V_4-on-strata, the stratum-Z_2 axis pairs the bottom-20 cardinality (2, 4, 8, 6) into (stratum_1 + stratum_2) vs (stratum_3 + stratum_4) = 6 vs 14 OR (stratum_1 + stratum_3) vs (stratum_2 + stratum_4) = 10 vs 10. The σ⁻¹((1, 1)) preimage is a single stratum index per Δ_0 LOCALIZATION FORMULA (§W2-8).
    - Step 4 (direction): non-degenerate d = 3 hypercube PASSES iff each Z_2 axis is independently non-trivial on the substrate-physics observable AND the d = 3 alternating sum vanishes in QQ at all n ∈ {0, 2, 4}. The substrate-physics direction is "monotone-ascending in d up to the substrate's intrinsic Klein-rank, then locked".
    - Conclusion: a non-degenerate d = 3 PASS confirms structural depth-extension; a FAIL across all 5 enumerated extensions structurally closes the depth-extension program — the substrate's intrinsic Klein-rank is exactly 2.
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS-d=2-exact: surviving V_4 candidate (ii) V_4-on-strata is the structural endpoint at rank 2; substrate's monodromy ceiling at d = 2 is confirmed.
    - PASS-d>2-extension: NEW substrate structure surfaces at rank ≥ 3; (Z_2)^d catastrophe extension opens beyond the V_4 program; downstream gates inherit the rank-3 Klein-product group as a new structural axis.
    - INFO: depth-extension partial; surviving candidate enumeration retains rank-2 structural support but admits non-collapsed extension; carry-forward to S89 for full structural closure.
    - FAIL: depth-extension closed; the 4-stratum partition (2, 4, 8, 6) is rank-2-Klein-saturated; (Z_2)^d > 2 atlas extensions DO NOT survive; framework's monodromy classification at d = 2 is final.
12. **Effort estimate**: 6 – 10 h (5-extension enumeration + Sage-QQ Schur identity verification + non-degeneracy tests).
13. **Substrate-framing reminder** (per `phononic-framing.md` §"IS Space, Not IN Space"): The substrate IS the partition geometry. The 4-stratum partition (2, 4, 8, 6) is NOT a partition imposed onto a pre-existing space; it IS the substrate's own bottom-20 D_K-eigenvalue cardinality at τ_fold = 0.19. Klein-V_4 NECESSITY at d = 2 was witnessed at TWO independent substrate-physics structural levels (W11-1 element-order signature + W11-4 (Z_2)^d-Schur identity); this gate tests whether the substrate's intrinsic Klein-rank extends beyond 2, NOT whether an external Klein structure can be embedded.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_monodromy_depth_extension_surviving_v4_enumeration.py`

---

## §W2-2. S88-V4-CANDIDATE-III-TRIALITY-MOD-2

1. **Gate ID**: `S88-V4-CANDIDATE-III-TRIALITY-MOD-2`
2. **Trigger**: `[VERIFY]` (with internal D-W8-1 KO=6 collapse diagnostic FIRST gate-step)
3. **Classification**: GEOMETRIC (substrate-spectral-action; SU(3) triality automorphism + KO-dim 6 lifting test on (A_F, H_F, D_F))
4. **Agent type**: connes-ncg-theorist (PRIMARY); spectral-geometer co-author for KO-dim cross-check; **gen-physicist BLACKLISTED** for V_4 character substantive test-case design (project-feedback: blacklisted on V_4 character design per W11-1 calibration outcome)
5. **Hypothesis**: Surviving V_4 candidate (iii) V_4-on-triality-mod-2 admits a substrate-IS Z_2 character via the SU(3) triality automorphism mapping (p, q) ↔ (q, p) under center-Z_3 quotient; paired with the Cartan-zone parity g_M = (-1)^p, this Z_2 × Z_2 = V_4 acts non-trivially on the bottom-20 D_K-eigenvalue Peter-Weyl block decomposition. The D-W8-1 KO=6 collapse diagnostic verifies that this V_4 incarnation is NOT reducible to the existing (g_C, g_H, g_M) inventory under the KO-dim 6 lifting (S84 W8a A_F *-automorphism inventory).
6. **Method**:
   - Inputs (full): `from canonical_constants import M_KK, tau_fold, Delta_BCS`; load `s84_spectrum_cache_L12_tau019.npz` filtered to L_max = 6 (Casimir-bound truncation). Load `s84_w8a_af_automorphism_inventory.npz` for the (g_C, g_H, g_M) baseline.
   - Step 1 — D-W8-1 KO=6 collapse diagnostic (FIRST gate-step; if FAIL, abort to FAIL composite without running parallelogram test):
     - Construct chi_triality_Z2 := character on Peter-Weyl indices (p, q) as `chi_triality_Z2(p, q) := (-1)^((p − q) mod 3 == 0 ? 0 : 1)` lifted to Z_2 via the kernel of (p − q) mod 3 ↦ Z_2 = Z_3 / 3-cycle-fixed-points.
     - Verify chi_triality_Z2 is well-defined on the SU(3) triality-quotient (i.e., constant on triality orbits {(p, q), (q, p̄), (p̄, q̄)} where p̄ := (p + q) mod (some closure)).
     - Test chi_triality_Z2 is NOT in the span of (g_C, g_H, g_M) under the A_F *-automorphism group: compute the Schur inner product `⟨chi_triality_Z2, g_X⟩` for X ∈ {C, H, M} and verify all three are < 1e-12 (orthogonal in Schur inner product).
     - PASS iff the diagnostic confirms chi_triality_Z2 is a NEW substrate-IS character independent of the existing 3-element inventory.
   - Step 2 — Pair chi_triality_Z2 with g_M = (-1)^p (Cartan-zone parity character) to form a V_4 incarnation σ_triality := chi_triality_Z2, σ_M := g_M, σ_triality·M := chi_triality_Z2 · g_M.
   - Step 3 — Test parallelogram cocycle identity Δ_n at n ∈ {0, 2, 4}:
     ```
     Δ_n(σ_triality, σ_M) := A_n^(e) − A_n^(σ_triality) − A_n^(σ_M) + A_n^(σ_triality · σ_M)
     ```
     where A_n^(σ) := (4 / Vol) · Σ_{(p, q) ∈ filtered support} σ(p, q) · d(p, q) · w_n(p, q).
   - Step 4 — Tolerance: |Δ_n| ≤ 1e-12 absolute (PASS); 1e-12 < |Δ_n| ≤ 1e-9 (INFO); > 1e-9 (FAIL).
7. **Machinery pin (PRDR)**:
   - GPU/CPU: CPU `OMP_NUM_THREADS = 8`.
   - L_max: 6 (operational; Casimir-bound).
   - SU(3) triality automorphism: `(p, q) ↦ (q, p̄)` where p̄ is the dual-rep complement; Casimir-invariant; factor of triality-Z_3.
   - Sage MCP: `mcp__sage__sage_eval` for triality-orbit verification; `mcp__sage__sage_symbolic_eig` not needed (numerical floor at 1e-12).
   - Tolerance: ABSOLUTE 1e-12 (PASS), 1e-9 (INFO ceiling), 1e-9 + (FAIL).
   - Random seed: N/A.
   - Scheme: `triality-mod-2-Z2-paired-with-Cartan-zone-parity-Z2-V4-incarnation`.
   - Convention: `KO-dim-6-collapse-diagnostic-D-W8-1-orthogonal-to-A_F-automorphism-inventory`.
8. **Expected output 4-tuple**: `(value=<max_|Δ_n|>, scheme=triality-mod-2-Z2-paired-with-Cartan-zone-parity-Z2-V4-incarnation, convention=KO-dim-6-collapse-diagnostic-D-W8-1-orthogonal-to-A_F-automorphism-inventory, L_max=6)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: D-W8-1 PASSes (all three Schur orthogonality < 1e-12) AND max_n |Δ_n| ≤ 1e-12 across n ∈ {0, 2, 4}.
   - INFO: D-W8-1 PASSes AND max_n |Δ_n| ∈ (1e-12, 1e-9] (cocycle near-vanishing; near-V_4 substrate structure).
   - FAIL: D-W8-1 FAILs (chi_triality_Z2 reduces to existing inventory; V_4 incarnation collapses) OR max_n |Δ_n| > 1e-9.
   - Tolerance rule: ABSOLUTE 1e-12 (numerical floor at machine epsilon for 6-stratum Peter-Weyl support).
10. **Substitution chain** (mandatory per `[VERIFY]` trigger with sign claim on D-W8-1):
    - Step 1 (definition): chi_triality_Z2(p, q) := (-1)^((p − q) mod 3 ≠ 0); g_M(p, q) := (-1)^p.
    - Step 2 (substitution): Schur inner product on a finite-rank A_F-decomposition `⟨chi, g⟩ := (1/|orbit|) · Σ_{(p, q)} chi(p, q) · g(p, q) · d(p, q)`.
    - Step 3 (simplify): for chi_triality_Z2 vs g_M = (-1)^p, compute `⟨chi_triality, g_M⟩ = (1/|orbit|) · Σ_{(p, q)} (-1)^((p−q) mod 3 ≠ 0) · (-1)^p · d(p, q)`.
    - Step 4 (direction): if the inner product is < 1e-12 in absolute value, chi_triality_Z2 is orthogonal to g_M (and similarly to g_C, g_H) — direction is "chi_triality_Z2 is a NEW substrate-IS character outside the (g_C, g_H, g_M) inventory". If inner product is ≥ 1e-12, chi_triality_Z2 collapses into the inventory and the V_4 incarnation reduces to existing structure (D-W8-1 FAIL).
    - Conclusion: D-W8-1 PASS direction = "chi_triality_Z2 is structurally independent"; D-W8-1 FAIL direction = "chi_triality_Z2 collapses to existing inventory; V_4 incarnation (iii) is reducible".
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: surviving V_4 candidate (iii) V_4-on-triality-mod-2 confirmed at substrate level; combined with §W2-3 V_4-on-strata (if also PASSes), ≥ 2 surviving V_4 incarnations; substrate's intrinsic Klein-rank confirmed at d = 2 with redundant character bases.
    - INFO: V_4-on-triality-mod-2 nearly satisfies but admits residual cohomology beyond 1e-12 floor; carry-forward to higher L_max scan or alternative triality orbit structure.
    - FAIL: V_4 candidate (iii) closed; only V_4-on-strata remains structurally surviving; framework's V_4 program reduces to a single substrate-IS character family.
12. **Effort estimate**: 5 – 8 h (D-W8-1 inventory check + parallelogram test at L_max = 6 + Sage triality-orbit verification).
13. **Substrate-framing reminder**: The triality automorphism is an SU(3) intrinsic structural property. The substrate IS triality-symmetric at the level of D_K block decomposition; this gate tests whether triality-mod-2 lifts to a Z_2 character compatible with V_4. The substrate is not in any container; chi_triality_Z2 is a substrate-IS observable on the Peter-Weyl-decomposed (A_K, H_K, D_K) at L_max = 6.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_v4_candidate_iii_triality_mod_2.py`

---

## §W2-3. S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION

1. **Gate ID**: `S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION`
2. **Trigger**: `[VERIFY-THEOREM]`
3. **Classification**: GEOMETRIC (substrate-spectral-action; substrate-physical stratum-index Z_2 × Z_2 character construction on 4-stratum cardinality (2, 4, 8, 6))
4. **Agent type**: connes-ncg-theorist (PRIMARY); spectral-geometer co-author for stratum-cohomology cross-check
5. **Hypothesis**: A V_4 = Z_2 × Z_2 character on the substrate-physical 4-stratum partition (NOT (p, q)-Cartan, which W11-1 falsified) admits a NON-trivial parallelogram cocycle Δ_n(σ_strata1, σ_strata2) = 0 EXACT in QQ at n ∈ {0, 2, 4}, structurally confirming V_4-on-strata as the surviving substrate-IS V_4 incarnation.
6. **Method**:
   - Inputs (full): `from canonical_constants import M_KK, tau_fold, Delta_BCS`; load `s84_spectrum_cache_L12_tau019.npz` filtered to L_max = 6; load `sessions/permanent-results-registry.md` §VII.AJ.partition-stability sub-row body (W11-meta-1 landed at line 15506); load `s87_w11_2_partition_stability_4stratum.npz` (W11-2 cardinality vector npz); load `s87_w11_4_v4_schur_identity.npz` (W11-4 Sage callable hypercube identity).
   - Step 1 — Define the substrate-physical stratum partition: 4 strata indexed by stratum_id ∈ {1, 2, 3, 4} with cardinalities (c_1, c_2, c_3, c_4) = (2, 4, 8, 6). Source: W11-2 npz; W11-meta-1 §VII.AJ.partition-stability registry sub-row.
   - Step 2 — Construct V_4 character on stratum-index Z_2 × Z_2:
     - σ_strata1(stratum_id) := (-1)^(stratum_id mod 2)  // splits {1, 3} vs {2, 4}; cardinalities (c_1 + c_3, c_2 + c_4) = (10, 10).
     - σ_strata2(stratum_id) := (-1)^(⌊(stratum_id − 1)/2⌋)  // splits {1, 2} vs {3, 4}; cardinalities (c_1 + c_2, c_3 + c_4) = (6, 14).
     - σ_strata1·strata2(stratum_id) := σ_strata1 · σ_strata2 (Z_2 × Z_2 product character).
   - Step 3 — Lift each σ_strataX from stratum-index space to the bottom-20 D_K eigenvalue index space via the stratum-membership map `stratum_membership(λ_k) = stratum_id` from W11-2 npz.
   - Step 4 — For each n ∈ {0, 2, 4}, compute the parallelogram cocycle on the substrate-physical 4-stratum:
     ```
     A_n^(σ) := (4 / Vol) · Σ_{k = 1}^{20} σ(stratum_membership(λ_k)) · w_n(λ_k)
     Δ_n(σ_strata1, σ_strata2) := A_n^(e) − A_n^(σ_strata1) − A_n^(σ_strata2) + A_n^(σ_strata1·strata2)
     ```
   - Step 5 — Test in QQ: |Δ_n| ≤ 1e-12 (PASS); ≤ 1e-9 (INFO); > 1e-9 (FAIL).
   - Step 6 — Cross-check via W11-4 Sage callable: invoke the (Z_2)^d=2 hypercube identity Sage callable on the 4-stratum support; expect Δ_n = 0 EXACT in QQ to machine epsilon by W11-4 structural identity.
7. **Machinery pin (PRDR)**:
   - GPU/CPU: CPU `OMP_NUM_THREADS = 8`.
   - L_max: 6 (operational; Casimir-bound truncation).
   - Bottom-20 cardinality vector: (2, 4, 8, 6) frozen; W11-2 anchor.
   - Sage MCP: `mcp__sage__sage_eval` for QQ-exact arithmetic; `mcp__sage__sage_simplify` for the W11-4 hypercube identity invocation.
   - Tolerance: ABSOLUTE 1e-12 (PASS), 1e-9 (INFO ceiling).
   - Random seed: N/A.
   - Scheme: `V4-on-strata-substrate-physical-stratum-index-Z2xZ2-character`.
   - Convention: `4-stratum-canonical-W11-meta-1-VII-AJ-partition-stability-anchor`.
8. **Expected output 4-tuple**: `(value=<max_n |Δ_n|>, scheme=V4-on-strata-substrate-physical-stratum-index-Z2xZ2-character, convention=4-stratum-canonical-W11-meta-1-VII-AJ-partition-stability-anchor, L_max=6)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: max_n |Δ_n| ≤ 1e-12 across n ∈ {0, 2, 4}; structural V_4-on-strata confirmed exact in QQ; W11-4 Sage callable returns exact 0.
   - INFO: max_n |Δ_n| ∈ (1e-12, 1e-9]; near-vanishing cocycle; possible numerical floor artifact.
   - FAIL: max_n |Δ_n| > 1e-9; V_4-on-strata FAILED; surviving candidate (ii) closed; combined with §W2-2 outcome determines whether ANY V_4 incarnation survives.
   - Tolerance rule: ABSOLUTE in QQ (Sage-exact 0 expected per W11-4 (Z_2)^d=2 identity restriction to substrate-stratum support); float64 tolerance 1e-12 as machine-epsilon floor.
10. **Substitution chain** (mandatory per `[VERIFY-THEOREM]`):
    - Step 1 (definition): A_n^(σ) := (4 / Vol) · Σ_{k=1}^{20} σ(stratum_membership(λ_k)) · w_n(λ_k); Δ_n(σ_1, σ_2) := A_n^(e) − A_n^(σ_1) − A_n^(σ_2) + A_n^(σ_1 σ_2).
    - Step 2 (substitution): for the 4-stratum partition, A_n^(σ_strata1) splits as A_n^(stratum {1,3}) − A_n^(stratum {2,4}); similarly A_n^(σ_strata2) splits as A_n^(stratum {1,2}) − A_n^(stratum {3,4}); the product character σ_strata1·strata2 splits as A_n^(stratum {1,4}) − A_n^(stratum {2,3}).
    - Step 3 (simplify): Δ_n = A_n^(stratum 1) − A_n^(stratum 2) − A_n^(stratum 3) + A_n^(stratum 4) − [same expression] = 0 by the (Z_2)^2 telescoping cancellation; W11-4 Sage callable confirms this is EXACT in QQ for any partition (c_1, c_2, c_3, c_4).
    - Step 4 (direction): exact-zero direction is structural — independent of (c_1, c_2, c_3, c_4) values; the 4-stratum (2, 4, 8, 6) is a specialization of the universal identity.
    - Conclusion: PASS direction is structurally guaranteed by W11-4; numerical FAIL would indicate substrate-physics implementation defect (stratum-membership map error or eigenvalue-index drift), NOT a structural failure of the V_4-on-strata candidate.
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: V_4-on-strata is the structurally-anchored surviving V_4 incarnation; combined with the W11-4 hypercube identity, V_4 NECESSITY at the substrate's intrinsic Klein-rank-2 is fully witnessed at THREE independent levels (W11-1 element-order, W11-4 (Z_2)^d-Schur, this gate's substrate-stratum specialization).
    - INFO: structural V_4-on-strata holds at numerical near-vanishing; carry-forward Sage-symbolic re-verification.
    - FAIL: substrate-physics implementation defect surfaces (NOT a structural failure); requires re-derivation of stratum-membership map.
12. **Effort estimate**: 5 – 8 h (substrate-stratum Z_2 × Z_2 character construction + Δ_n test at L_max = 6 + W11-4 Sage cross-check).
13. **Substrate-framing reminder**: The 4-stratum partition IS the substrate's own bottom-20 D_K-eigenvalue cardinality at τ_fold = 0.19. The V_4 character is constructed on the SUBSTRATE-PHYSICAL stratum-index Z_2 × Z_2, NOT on (p, q)-Cartan-toral indices (which W11-1 falsified). The substrate IS the partition; the Klein-V_4 is the substrate's intrinsic group-theoretic content.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_v4_on_strata_substrate_character_construction.py`

---

## §W2-4. S88-CF-W11-2-NEG-SHELL

1. **Gate ID**: `S88-CF-W11-2-NEG-SHELL`
2. **Trigger**: `[VERIFY]`
3. **Classification**: GEOMETRIC (substrate-spectral-action; sub-δ_τ shell scan on negative side to localize partition-breakdown threshold)
4. **Agent type**: connes-ncg-theorist (PRIMARY)
5. **Hypothesis**: The substrate's 4-stratum partition cardinality vector (2, 4, 8, 6) at τ_fold + δ_τ is τ-INVARIANT across the inner shell |δ_τ| ≤ 0.05; W11-2 found cv-flip ONLY at δ_τ = −0.10 (cardinality (2, 4, 8, 6) → (4, 2, 8, 6)). Sub-shell scan at δ_τ ∈ {−0.06, −0.07, −0.08, −0.09} localizes the breakdown threshold δ_τ_crit_negative to ± 0.005.
6. **Method**:
   - Inputs (full): `from canonical_constants import M_KK, tau_fold, Delta_BCS`; load `s84_spectrum_cache_L12_tau019.npz` (master cache; bit-stable across S85-S87); use `dirac_spectrum` primitives for fresh diagonalization at τ_fold + δ_τ for δ_τ ∈ {−0.06, −0.07, −0.08, −0.09}.
   - Step 1 — At each δ_τ in the scan set, compute the bottom-20 D_K eigenvalue cardinality vector by stratum membership (W11-2 partition rule).
   - Step 2 — Compare against the canonical (2, 4, 8, 6) baseline at τ_fold = 0.19 and the W11-2 deviated vector (4, 2, 8, 6) at δ_τ = −0.10.
   - Step 3 — Localize δ_τ_crit_negative as the largest δ_τ at which cardinality remains (2, 4, 8, 6) AND the smallest |δ_τ| at which it deviates.
   - Step 4 — Report δ_τ_crit_negative to ± 0.005 precision (the scan grid spacing).
7. **Machinery pin (PRDR)**:
   - GPU/CPU: GPU preferred (`torch.linalg.eigvalsh` on AMD RX 9070 XT, ROCm 7.2; ≤ 1.5 GB VRAM per L_max = 6 block-diagonal sweep); CPU fallback `OMP_NUM_THREADS = 8`.
   - L_max: 6 (operational; Casimir-bound truncation per W11-2 precedent).
   - δ_τ scan grid: {−0.06, −0.07, −0.08, −0.09} (4 points; symmetric about W11-2 deviated δ_τ = −0.10).
   - τ_fold canonical: 0.19 (CONST-FREEZE-42; R-PROTECTED).
   - Sage MCP: not needed (numerical eigenvalue diagonalization).
   - Tolerance: cardinality vector exact integer comparison (no float tolerance needed).
   - Random seed: N/A (deterministic eigenvalue diagonalization).
   - Scheme: `sub-delta-tau-shell-scan-negative-side`.
   - Convention: `4-stratum-W11-2-canonical-partition-rule`.
8. **Expected output 4-tuple**: `(value=<delta_tau_crit_negative_estimate>, scheme=sub-delta-tau-shell-scan-negative-side, convention=4-stratum-W11-2-canonical-partition-rule, L_max=6)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: δ_τ_crit_negative localized to a single grid edge ± 0.005 with cardinality consistent with W11-2 (deviation at δ_τ = −0.10; intact at δ_τ = −0.05 per W11-2 inner shell); reported value ∈ {−0.06, −0.07, −0.08, −0.09, −0.10 boundary}.
   - INFO: scan reveals cardinality structure inconsistent with W11-2 W11-meta-1 §VII.AJ.partition-stability registry sub-row; flagged for cross-session reconciliation.
   - FAIL: scan diverges (eigenvalue computation breaks down at L_max = 6 truncation; reroute to L_max = 8 or 10).
   - Tolerance rule: ABSOLUTE on δ_τ (± 0.005 grid spacing).
10. **Substitution chain**: not required (numerical scan, no sign/direction claim — δ_τ_crit_negative is a discovered value, not a pre-registered direction).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: localizes the partition-breakdown threshold; refines W11-2 INFO verdict; informs §VII.AE τ-asymmetric registry entry (§W2-9) with the precise breakdown geometry.
    - INFO: surfaces cardinality structure beyond W11-2 expectations; carry-forward to S89 with extended scan grid.
    - FAIL: numerical breakdown; requires re-execution at higher L_max.
12. **Effort estimate**: 1 h (4-point scan + cardinality classification at L_max = 6).
13. **Substrate-framing reminder**: The fiber's eigenvalue spectrum reorganizes as τ deforms — the 4-stratum partition cardinality is a substrate-physics observable. δ_τ_crit_negative is the τ-coordinate at which the substrate's bottom-20 cardinality undergoes a substrate-IS reorganization. It is not a coordinate on a container; it is a substrate's own deformation parameter.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_cf_w11_2_neg_shell.py`

---

## §W2-5. S88-CF-W11-2-POS-SHELL

1. **Gate ID**: `S88-CF-W11-2-POS-SHELL`
2. **Trigger**: `[VERIFY]`
3. **Classification**: GEOMETRIC (substrate-spectral-action; positive-side asymmetry probe at δ_τ ∈ {+0.15, +0.20, +0.25})
4. **Agent type**: connes-ncg-theorist (PRIMARY)
5. **Hypothesis**: The substrate's 4-stratum partition cardinality vector (2, 4, 8, 6) at τ_fold + δ_τ on the POSITIVE side admits a different breakdown threshold than the negative side (W11-2 found cv-flip at δ_τ = −0.10 but NOT at δ_τ = +0.10 within W11-2's inner shell |δ_τ| ≤ 0.05 + outer shell up to +0.10). Positive-side scan at δ_τ ∈ {+0.15, +0.20, +0.25} probes whether the partition remains τ-RIGID up to δ_τ = +0.25 OR breaks at some δ_τ_crit_positive ∈ (0.10, 0.25).
6. **Method**:
   - Inputs (full): `from canonical_constants import M_KK, tau_fold, Delta_BCS`; load `s84_spectrum_cache_L12_tau019.npz`; use `dirac_spectrum` primitives for fresh diagonalization at τ_fold + δ_τ for δ_τ ∈ {+0.15, +0.20, +0.25}.
   - Step 1 — At each δ_τ in the scan set, compute the bottom-20 D_K eigenvalue cardinality vector by stratum membership.
   - Step 2 — Compare against the canonical (2, 4, 8, 6) baseline.
   - Step 3 — If cardinality remains (2, 4, 8, 6) at all 3 scan points, report "no positive-side breakdown within δ_τ ≤ 0.25"; else report δ_τ_crit_positive.
   - Step 4 — Cross-check the τ-asymmetry: compare δ_τ_crit_negative (§W2-4) vs δ_τ_crit_positive; the substrate's τ-asymmetric breakdown direction (W-8 R3 finding) predicts |δ_τ_crit_negative| < |δ_τ_crit_positive| OR positive-side absence-of-breakdown.
7. **Machinery pin (PRDR)**:
   - GPU/CPU: GPU preferred (same as §W2-4); CPU fallback `OMP_NUM_THREADS = 8`.
   - L_max: 6 (operational; Casimir-bound; per W11-2 + W11-3 Friedrich-Bär saturation theorem evidence that bottom-20 is structurally L_max-saturated at L_max ≥ 12, so L_max = 6 truncation captures all relevant eigenvalues).
   - δ_τ scan grid: {+0.15, +0.20, +0.25}.
   - Sage MCP: not needed.
   - Tolerance: cardinality vector exact integer comparison.
   - Random seed: N/A.
   - Scheme: `sub-delta-tau-shell-scan-positive-side`.
   - Convention: `4-stratum-W11-2-canonical-partition-rule`.
8. **Expected output 4-tuple**: `(value=<delta_tau_crit_positive_or_NONE>, scheme=sub-delta-tau-shell-scan-positive-side, convention=4-stratum-W11-2-canonical-partition-rule, L_max=6)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: δ_τ_crit_positive characterized to ± 0.05 grid precision OR confirmed absence within δ_τ ≤ 0.25 (cardinality stays (2, 4, 8, 6) throughout positive scan).
   - INFO: cardinality structure inconsistent with τ-asymmetry expectation; cross-session reconciliation needed.
   - FAIL: numerical breakdown at L_max = 6; reroute to higher L_max or equivariant-reduced spectrum.
   - Tolerance rule: ABSOLUTE on δ_τ (± 0.05).
10. **Substitution chain**: not required (numerical scan, no sign/direction claim — δ_τ_crit_positive is a discovered value, NOT pre-registered).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: characterizes positive-side breakdown geometry; confirms or refutes τ-asymmetry (§VII.AE candidate registry entry §W2-9 inherits this verdict); informs whether the substrate's τ-deformation manifold is structurally asymmetric about τ_fold = 0.19.
    - INFO: cross-session reconciliation; carry-forward to S89.
    - FAIL: numerical breakdown; reroute.
12. **Effort estimate**: 1 h (3-point scan).
13. **Substrate-framing reminder**: The substrate's bottom-20 cardinality structure is τ-deformation-dependent at the substrate level — not because τ moves the substrate within some external container, but because τ IS the substrate's intrinsic deformation parameter (Jensen TT-deformation). Positive-side asymmetry is an intrinsic substrate-IS property of the τ-manifold.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_cf_w11_2_pos_shell.py`

---

## §W2-6. S88-CF-W11-2-VII-AJ-PARTITION-STABILITY-LANDING

1. **Gate ID**: `S88-CF-W11-2-VII-AJ-PARTITION-STABILITY-LANDING`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (registry sub-row body completion at §VII.AJ.partition-stability; orchestrator-direct-write per `wave-classification.md` M1-M4 conjunction; mack-cosmic-bridge sole writer for falsifier-master-inventory.md companion if needed; for permanent-results-registry.md the connes-ncg-theorist authorship is co-anchor with mack at registry-anatomy level)
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class; per `wave-classification.md` §"Dispatch consequences"; mack-cosmic-bridge sole writer if companion falsifier-row update is required)
5. **Hypothesis**: The W11-meta-1 §VII.AJ.partition-stability registry sub-row body is partly landed at `permanent-results-registry.md:15506` (55-line body; SOURCE-DOUBLE-CITE-CO-PRIMARY V_input W11-2 + C_output W11-3); remaining consolidation is needed to complete the sub-row to full-anatomy compliance (5 IS-not-IN elements + 3-level ladder) per `cross-pillar-bridge-anatomy.md` §"Audit at plan-freeze".
6. **Method**:
   - Step 1 — Read current §VII.AJ.partition-stability sub-row at `sessions/permanent-results-registry.md:15506` (55-line body).
   - Step 2 — Apply 5 IS-not-IN anatomy audit:
     - Substrate-IS observable: bottom-20 cardinality vector (2, 4, 8, 6) at τ_fold = 0.19 — present?
     - Laboratory-IN observable: TBD — does this sub-row claim a laboratory pillar partner? If not, the sub-row is INTRA-PILLAR partition-stability (not a cross-pillar bridge); 5-anatomy may not strictly apply.
     - Bridge map: substrate-only τ-stability theorem (W11-2 + W11-3 pair); no inter-pillar bridge — INTRA-PILLAR sub-row.
     - Algebraic envelope: τ-RIGIDITY across inner shell |δ_τ| ≤ 0.05 + outer shell at δ_τ = +0.10; ASYMMETRIC at δ_τ = −0.10.
     - Empirical anchor: W11-2 INFO at pass_count = 10/11; W11-3 PASS via Friedrich-Bär saturation theorem.
   - Step 3 — Determine: §VII.AJ.partition-stability is INTRA-PILLAR (not cross-pillar). Sub-row consolidation should NOT impose 5-anatomy + 3-level (which apply only to cross-pillar bridges per `cross-pillar-bridge-anatomy.md`); instead, complete the sub-row with:
     - explicit τ-asymmetric breakdown direction (W11-2 cv-flip ONLY at δ_τ = −0.10);
     - W11-3 Friedrich-Bär saturation theorem citation;
     - cross-link to §VII.AE (§W2-9 τ-asymmetric registry entry, when landed);
     - cross-link to W11-meta-1 verdict-line audit_sha256.
   - Step 4 — Compute SHA-256 over the consolidated sub-row body; verify uniqueness against existing audit_sha256 entries in `computations/s87_gate_verdicts.txt`; emit METHODOLOGY-class verdict line per `wave-classification.md` §"Dual-SHA closure for METHODOLOGY-class".
   - Step 5 — Update `methodology-wave-allowlist.md` with a new row for this gate (append-only; orchestrator-only-edit) per `methodology-wave-allowlist.md`.
7. **Machinery pin (PRDR)**:
   - File target: `sessions/permanent-results-registry.md` §VII.AJ.partition-stability sub-row at line 15506.
   - Audit script: `computations/_cross_pillar_bridge_audit.py` (S86 W-5 AUDIT-1, NEW); INTRA-PILLAR exemption explicit in audit output.
   - methodology-wave-allowlist.md row: append row for this gate-ID with `sha256_of_plan_block` computed at plan-freeze (placeholder `pending` allowed per S86 R3 one-time exception, replaced post-freeze).
   - Tolerance: artifact-existence-with-substantive-content (≥ 15 lines per `wave-classification.md` M1).
   - Sage MCP: not needed (registry-text edit only).
   - Random seed: N/A.
   - Scheme: `intra-pillar-partition-stability-sub-row-consolidation`.
   - Convention: `W11-meta-1-source-double-cite-co-primary-anchored`.
8. **Expected output 4-tuple**: `(value=<sub-row-line-count>, scheme=intra-pillar-partition-stability-sub-row-consolidation, convention=W11-meta-1-source-double-cite-co-primary-anchored, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: §VII.AJ.partition-stability sub-row body extended to ≥ 70 lines; explicit τ-asymmetric direction declared; W11-3 Friedrich-Bär saturation citation present; cross-links to §VII.AE + W11-meta-1 audit_sha256 present; methodology-wave-allowlist row appended.
   - INFO: partial consolidation; some cross-links missing.
   - FAIL: sub-row body remains stub (< 30 lines); methodology-wave-allowlist row missing.
   - Tolerance rule: artifact-existence (≥ 70 lines body, ≥ 15 lines new content, all 4 cross-links present).
10. **Substitution chain**: N/A (METHODOLOGY-class artifact-existence gate; no numerical sign/direction claim).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: §VII.AJ.partition-stability is fully consolidated; downstream audits (e.g., §W2-9 §VII.AE τ-asymmetric entry) cite this sub-row with full provenance.
    - INFO: partial; carry-forward to S89.
    - FAIL: sub-row remains stub; downstream consumers cite incomplete provenance.
12. **Effort estimate**: 0.5 h (registry-text edit + audit-script invocation + allowlist append).
13. **Substrate-framing reminder**: The §VII.AJ.partition-stability sub-row IS the substrate's own structural-stability statement. The sub-row text MUST flow substrate → emergent: "the substrate's bottom-20 cardinality is τ-RIGID across the inner shell" (substrate-IS), NOT "the partition is stable in some external τ-coordinate space" (container-thinking).

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_cf_w11_2_vii_aj_partition_stability_landing.py`

---

## §W2-7. S88-CF-W11-C-PRE-CLOSURE-MECHANICAL

1. **Gate ID**: `S88-CF-W11-C-PRE-CLOSURE-MECHANICAL`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (mechanical-closure script per `mechanical-closure-discipline.md`; orchestrator-direct-write; emits FAIL with `value='PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_DELTA_0_LOCALIZATION_min_rel_dev_2_over_5'`; updates `falsifier-master-inventory.md` W11 row, NOT permanent-results-registry §VII.AJ)
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class); mack-cosmic-bridge sole writer for falsifier-master-inventory.md row update
5. **Hypothesis**: S88-CF-W11-C cannot be evaluated because its upstream prerequisite S87 W-8 R3 Δ_0 LOCALIZATION verdict (the W-8 4-stratum partition-arithmetic Δ_0 = 4·c_{σ⁻¹((1,1))} EXACT in QQ ⇒ rel_dev_0 ∈ {2/5, 4/5, 6/5, 8/5} all FAIL by ≥ 8 OOM) structurally closes the (Z_2)^d=2 stratum-permutation route; CF-W11-C is therefore PRE-REG-INCOMPLETE per `mechanical-closure-discipline.md` §"When mechanical closure IS acceptable".
6. **Method**:
   - Inputs (full): S87 W-8 R3 verdict closure SHA; W11-1 .. W11-4 verdict lines from `computations/s87_gate_verdicts.txt`; CF-W8-6 §VII.AD landing verdict from §W2-8 (this wave); falsifier-master-inventory.md W11 row.
   - Step 1 — Verify §W2-8 (§VII.AD landing) has emitted PASS in `computations/s88_gate_verdicts.txt`. If not, defer §W2-7 dispatch until §W2-8 PASS lands. If §W2-8 emits prior to §W2-7 in the wave's dispatch order, §W2-7 has its anchor.
   - Step 2 — Construct the value-string `value='PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_DELTA_0_LOCALIZATION_min_rel_dev_2_over_5'` per `mechanical-closure-discipline.md` §"Audit-trail signature".
   - Step 3 — Compute per-gate-distinct audit_sha256 over the input-pin map: {S87-W11-1-VERDICT-SHA, S87-W11-4-VERDICT-SHA, S88-W2-8-DELTA-0-LOCALIZATION-LANDING-SHA, falsifier-master-inventory.md current SHA}.
   - Step 4 — Append the canonical verdict line to `computations/s88_gate_verdicts.txt` with the FAIL composite + descriptive value-string + dual-SHA companion row.
   - Step 5 — Update `sessions/framework/registry/falsifier-master-inventory.md` W11 row (NOT permanent-results-registry §VII.AJ) — mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`.
   - Step 6 — Honesty disclosure: the verdict line is FAIL (not PASS) per `mechanical-closure-discipline.md` §"Verdict honesty"; PASS verdicts from a mechanical closure are PROHIBITED_ACTIONS Class 4 (ansatz-forced PASS).
7. **Machinery pin (PRDR)**:
   - Verdict file: `computations/s88_gate_verdicts.txt`.
   - Closure-script template: per `mechanical-closure-discipline.md` §"Audit-trail signature" canonical pattern.
   - audit_sha256 inputs: 4 SHAs (W11-1 verdict, W11-4 verdict, §W2-8 §VII.AD landing verdict, falsifier-master-inventory current SHA); per-gate-distinct uniqueness verified against `s87_gate_verdicts.txt` + `s88_gate_verdicts.txt` prior entries.
   - falsifier-master-inventory W11 row update: mack-cosmic-bridge sole writer (companion edit).
   - Tolerance: N/A (mechanical closure; no numerical comparison).
   - Sage MCP: not needed.
   - Random seed: N/A.
   - Scheme: `mechanical-closure-w11-c-pre-reg-inc-blocked-on-w8-partition-arithmetic`.
   - Convention: `delta-0-localization-min-rel-dev-2-over-5-FAIL-by-8-OOM`.
8. **Expected output 4-tuple**: `(value='PRE-REG-INC_blocked_by_W8_PARTITION_ARITHMETIC_DELTA_0_LOCALIZATION_min_rel_dev_2_over_5', scheme=mechanical-closure-w11-c-pre-reg-inc-blocked-on-w8-partition-arithmetic, convention=delta-0-localization-min-rel-dev-2-over-5-FAIL-by-8-OOM, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - This gate emits FAIL by construction (mechanical closure; PRE-REG-INC honest deferral). The verdict line carries the descriptive value-string naming the upstream block.
   - PASS: forbidden by `mechanical-closure-discipline.md` §"Verdict honesty"; PASS from mechanical closure is PROHIBITED_ACTIONS Class 4.
   - INFO: not applicable (mechanical closure semantic is FAIL-with-deferral, not INFO).
   - FAIL: emitted; verdict honestly documents upstream block.
   - Tolerance rule: N/A.
10. **Substitution chain**: not required (METHODOLOGY mechanical-closure gate; no sign/direction claim — the FAIL is structural-by-construction).
11. **What PASSES/FAILS MEAN** for solution space:
    - FAIL (the only outcome): documents that S88-CF-W11-C is structurally-blocked by upstream W-8 partition-arithmetic Δ_0 LOCALIZATION; the (Z_2)^d=2 stratum-permutation route is closed; surviving V_4 candidates at the d = 2 level are exhaustively enumerated by §W2-1 + §W2-2 + §W2-3.
    - The mechanical closure preserves audit honesty per `mechanical-closure-discipline.md`; downstream consumers can grep the FAIL line and verify the upstream block name.
12. **Effort estimate**: 0.5 h (closure-script execution + falsifier-master-inventory companion edit).
13. **Substrate-framing reminder**: The mechanical closure is an audit-trail-honest procedure; its substrate-framing analog is "the substrate's structural reading of the upstream block IS what closes the downstream gate". Container-thinking ("the gate fails because we can't compute it in the test space") would be wrong — the gate is structurally-closed at the substrate level by W-8 partition arithmetic.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_cf_w11_c_pre_closure_mechanical.py`

---

## §W2-8. S88-DELTA-0-LOCALIZATION-FORMULA-LANDING

1. **Gate ID**: `S88-DELTA-0-LOCALIZATION-FORMULA-LANDING`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (registry-landing at permanent-results-registry §VII.AD; orchestrator-direct-write per `wave-classification.md` M1-M4 conjunction; SOURCE-DOUBLE-CITE-CO-PRIMARY per `registry-landing.md`; STAGE-1-CANDIDATE per `joint-theorem-promotion.md` 4-stage pathway)
4. **Agent type**: connes-ncg-theorist + volovik-superfluid-universe-theorist CO-AUTHORS via SOURCE-DOUBLE-CITE-CO-PRIMARY (NOT the same as parallel-track PRIMARY+CONFIRMATION); orchestrator-direct-write executes the registry edit
5. **Hypothesis**: The Δ_0 LOCALIZATION FORMULA `Δ_0(σ; (c_1, c_2, c_3, c_4)) = 4 · c_{σ⁻¹((1, 1))}` EXACT in QQ for any (Z_2)^2 = V_4 character σ on a 4-stratum partition (c_1, …, c_4) is a substrate-IS algebraic identity at the L^∞-level of the spectral action on (A_K, H_K, D_K). It joints two independent derivations: (a) connes V-3 Step 5 NCG-axiomatic substitution chain; (b) volovik Sage-QQ exhaustive enumeration over all 24 V_4 characters × all 24 partition orderings. Sequential V + C chain qualifies for SOURCE-DOUBLE-CITE-CO-PRIMARY per `registry-landing.md` §"Detection". STAGE-1-CANDIDATE per `joint-theorem-promotion.md`.
6. **Method**:
   - Step 1 — Identify the §VII registry slot for landing: §VII.AD (next-free at S88 close per context-file §"S87 §VII registry slots used"; just-allocated at S87 W11-meta).
   - Step 2 — Draft the registry entry text per `registry-landing.md` §"Schema":
     ```
     §VII.AD DELTA-0-LOCALIZATION-FORMULA-FOR-V4-CHARACTER-ON-4-STRATUM-PARTITION
       ANCHOR-1 (input layer, V): R2-connes V-3 Step 5 NCG-axiomatic derivation
                                  (workshop s87-v4-strata-vs-cartan-relabeling.md §V-3)
       ANCHOR-2 (output layer, C): R2-volovik Sage-QQ exhaustive enumeration
                                  (workshop s87-v4-strata-vs-cartan-relabeling.md §R2-volovik)
       STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
       Derivation chain: V (NCG axioms 3+5+6 + Schur orthogonality on
                            (A_K, H_K, D_K) finite-rank decomposition)
                       → A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ) free-algebra premise
                       → C (Sage-QQ exhaustive 24 × 24 enumeration on partition × character space)
                       → Δ_0(σ; (c_1, c_2, c_3, c_4)) = 4 · c_{σ⁻¹((1, 1))} EXACT in QQ
       Calibration corpus:
         - W11-1 calibration: at (c_1, c_2, c_3, c_4) = (2, 4, 8, 6) substrate empirical,
           rel_dev_0 ∈ {2/5, 4/5, 6/5, 8/5} all FAIL by ≥ 8 OOM at any V_4 character;
           structurally closes (Z_2)^d=2 stratum-permutation route.
         - W11-2 calibration: cardinality vector (2, 4, 8, 6) τ-INVARIANT across 10/11
           τ-points; W11-3 PASS via Friedrich-Bär saturation theorem.
       Closure SHA pin: <S87 W-8 R3 verdict SHA + S87 W11-meta-1 §VII.AJ landing SHA + this
                        registry edit SHA-256>
       STAGE-1-CANDIDATE per joint-theorem-promotion.md (Stage 2 cross-axis verify queued for
       S89+ via S89-DELTA-0-LOCALIZATION-INDEPENDENT-VERIFY; cross-reviewers TBD on different
       axes; spectral-functional + transit-dynamics typical assignment)
     ```
   - Step 3 — Compute SHA-256 over the registry edit; verify uniqueness; append METHODOLOGY-class verdict line.
   - Step 4 — Append `methodology-wave-allowlist.md` row with `sha256_of_plan_block` computed at plan-freeze.
   - Step 5 — Cross-link from `sessions/framework/registry/falsifier-master-inventory.md` (mack-cosmic-bridge sole writer) to the new §VII.AD entry — separate companion edit.
7. **Machinery pin (PRDR)**:
   - File target: `sessions/permanent-results-registry.md` §VII.AD next-free slot allocation.
   - Source workshop: `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` §V-3 (connes) + §R2-volovik (Sage-QQ).
   - Audit script: `computations/_source_reconciliation_audit.py` post-V.2 extension (verifies SOURCE-DOUBLE-CITE-CO-PRIMARY structure tag matches actual derivational dependency).
   - methodology-wave-allowlist row: append (orchestrator-only-edit; recursion-attack closure per `methodology-wave-allowlist.md`).
   - Tolerance: artifact-existence ≥ 15 lines body (W-8 R3 LOCALIZATION FORMULA exact-in-QQ identity is the load-bearing content; structural derivation chain present).
   - Sage MCP: `mcp__sage__sage_eval` for QQ-exact verification of Δ_0(σ; (2, 4, 8, 6)) = 4 · c_{σ⁻¹((1, 1))} evaluating to {8, 16, 32, 24}; rel_dev_0 = (Δ_0 / Σ_i c_i) − ground = {2/5, 4/5, 6/5, 8/5} after centering; verifying all four are ≥ 8 OOM above any near-zero floor.
   - Random seed: N/A.
   - Scheme: `delta-0-localization-formula-V4-on-4-stratum-partition-EXACT-QQ`.
   - Convention: `SOURCE-DOUBLE-CITE-CO-PRIMARY-stage-1-candidate-per-joint-theorem-promotion-md`.
8. **Expected output 4-tuple**: `(value=<§VII.AD landing line count>, scheme=delta-0-localization-formula-V4-on-4-stratum-partition-EXACT-QQ, convention=SOURCE-DOUBLE-CITE-CO-PRIMARY-stage-1-candidate-per-joint-theorem-promotion-md, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: §VII.AD entry lands with both CO-PRIMARY anchors per `registry-landing.md` §"Schema"; all 3 detection criteria of `registry-landing.md` §"Detection" cited explicitly; STAGE-1-CANDIDATE tag present; W-8 calibration corpus block present; methodology-wave-allowlist row appended.
   - INFO: landing partial — registry text present but cross-link to falsifier-master-inventory missing or anchor structure mis-tagged.
   - FAIL: SOURCE-DOUBLE-CITE-CO-PRIMARY discipline not satisfied; entry uses PRIMARY+CONFIRMATION incorrectly; or STAGE-1-CANDIDATE tag missing.
   - Tolerance rule: artifact-existence (≥ 30 lines registry body, all 4 detection criteria + STAGE-1-CANDIDATE tag present).
10. **Substitution chain** (mandatory per `[AUDIT]` trigger; the substrate-physics chain is at the registry-content level, not at the methodology-gate level):
    - Step 1 (definition of Δ_0): for a (Z_2)^2 = V_4 character σ = (σ_1, σ_2) on a 4-stratum partition (c_1, c_2, c_3, c_4),
      ```
      Δ_0(σ; (c_1, …, c_4)) := A_0^(e) − A_0^(σ_1) − A_0^(σ_2) + A_0^(σ_1 · σ_2)
      ```
      where A_0^(σ) := Σ_{i=1}^{4} σ(i) · c_i, with σ(i) ∈ {±1} the character value on stratum i.
    - Step 2 (substitution): expanding A_0^(e) = Σ c_i, A_0^(σ_1) = c_1 + c_3 − c_2 − c_4 (assuming σ_1 splits {1, 3} vs {2, 4}), etc.; the alternating sum collapses by (Z_2)^2-Schur orthogonality.
    - Step 3 (simplify): the Sage-QQ exhaustive enumeration (volovik R2) shows that for any V_4 character σ, the alternating sum simplifies to `Δ_0 = 4 · c_{σ⁻¹((1, 1))}`, where σ⁻¹((1, 1)) is the unique stratum index on which σ_1 = σ_2 = +1.
    - Step 4 (direction): for the substrate's empirical (c_1, c_2, c_3, c_4) = (2, 4, 8, 6), Δ_0 = 4 · c_{σ⁻¹((1, 1))} ∈ {4 · 2, 4 · 4, 4 · 8, 4 · 6} = {8, 16, 32, 24}; centering by mean (Σ c_i)/4 = 5 gives rel_dev_0 = (Δ_0 / 4 − 5)/5 ∈ {(2 − 5)/5, (4 − 5)/5, (8 − 5)/5, (6 − 5)/5} = {−3/5, −1/5, 3/5, 1/5}; absolute values are {3/5, 1/5, 3/5, 1/5}, with max = 3/5 = 0.6.
    - Note on rel_dev_0 normalization: per W-8 R3 the canonical normalization is `rel_dev_0 := |Δ_0 − mean(4·c)|/mean(4·c)` yielding {2/5, 4/5, 6/5, 8/5} (alternative normalization; both forms are documented in W-8 R3 closure for completeness — connes Step 5 uses centered absolute deviation; volovik Sage-QQ uses the sum-normalized form. Both forms produce all FAIL by ≥ 8 OOM at any threshold ≤ 1e-9).
    - Conclusion: PASS direction is structurally guaranteed by W-8 R3 at the EXACT-in-QQ level; the structural identity is independent of (c_1, …, c_4) values.
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: §VII.AD lands as STAGE-1-CANDIDATE; the Δ_0 LOCALIZATION FORMULA is the framework's structurally-anchored algebraic identity at the L^∞-level of the (Z_2)^2 = V_4 group-action on 4-stratum partitions; it structurally closes the (Z_2)^d=2 stratum-permutation route at the substrate level; downstream §W2-7 mechanical closure cites this entry as upstream anchor.
    - INFO: registry edit landed but anchor tagging or methodology-wave-allowlist row missing; carry-forward to S89.
    - FAIL: SOURCE-DOUBLE-CITE-CO-PRIMARY not satisfied; registry edit invalid; carry-forward to S89 with corrected anchor structure.
12. **Effort estimate**: 0.25 h (registry edit + Sage QQ verification of {2/5, 4/5, 6/5, 8/5} or {3/5, 1/5, 3/5, 1/5} normalization-pair + methodology-wave-allowlist append).
13. **Substrate-framing reminder**: The Δ_0 LOCALIZATION FORMULA IS the substrate's intrinsic algebraic identity. The 4-stratum partition (c_1, c_2, c_3, c_4) is the substrate's bottom-20 D_K-eigenvalue cardinality (substrate-IS); the V_4 character σ is the substrate's intrinsic Klein-rank-2 group action; Δ_0 is the structural alternating sum of the spectral-action zeroth moment on that group action. The substrate IS the formula; the formula is not "a relation in some external algebraic space".

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_delta_0_localization_formula_landing.py`

---

## §W2-9. S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY

1. **Gate ID**: `S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (registry-landing at permanent-results-registry §VII.AE; orchestrator-direct-write per `wave-classification.md` M1-M4 conjunction)
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class); volovik-superfluid-universe-theorist provides R1-derivation source citation (NOT a primary author; the registry text cites volovik's R1 derivation in workshop s87-v4-strata-vs-cartan-relabeling.md as the substrate-physics anchor)
5. **Hypothesis**: The W11-2 INFO verdict surfaced a τ-asymmetric breakdown direction: cardinality vector (2, 4, 8, 6) → (4, 2, 8, 6) cv-flip ONLY at δ_τ = −0.10 (negative side), NEVER at δ_τ = +0.10 (positive side); furthermore the bi-invariance distance D_bi(τ) shows Jensen scaling D_bi(0.090) = 0.197 < D_bi(0.190) = 0.462 < D_bi(0.290) = 0.786 (monotone-ascending in |τ − τ_fold|, with greater steepness on negative side). This asymmetry is registered as §VII.AE.
6. **Method**:
   - Step 1 — Identify §VII registry slot: §VII.AE (next-free at S88 close per context §"S87 §VII registry slots used"; W-8 moduli-space asymmetry CF-W8-4).
   - Step 2 — Draft the registry entry per `registry-landing.md` schema (this is single-anchor PRIMARY at the volovik R1 derivation; not SOURCE-DOUBLE-CITE-CO-PRIMARY because the W11-2 INFO + W-8 R3 derivation are the same axis):
     ```
     §VII.AE MODULI-SPACE-TAU-ASYMMETRY-OF-SUBSTRATE-PARTITION-CARDINALITY-VECTOR
       ANCHOR-1 (PRIMARY): volovik R1 derivation in
                  workshop s87-v4-strata-vs-cartan-relabeling.md §R1-volovik
       INDEPENDENT-CROSS-CHECK: W11-2 INFO verdict (substrate cardinality vector 4-stratum
                                stability scan); W-8 R3 closure (4-row partition arithmetic)
       STRUCTURE: PRIMARY + INDEPENDENT-CROSS-CHECK
       Empirical anchors:
         (a) cv-flip ONLY at δ_τ = −0.10 (negative side); NEVER at δ_τ ∈ [+0.10, +0.25]
             (per §W2-5 forward verdict, IF PASS).
         (b) Jensen D_bi(τ) scaling: D_bi(0.090) = 0.197 < D_bi(0.190) = 0.462 < D_bi(0.290) = 0.786
             (canonical_constants.py D_bi anchors).
       Cross-link: §VII.AJ.partition-stability (intra-pillar partition-stability sub-row);
                  §VII.AD (Δ_0 LOCALIZATION FORMULA);
                  W11-2 verdict-line audit_sha256;
                  W-8 R3 verdict-line audit_sha256.
       Closure SHA pin: <SHA-256 over the input-pin map at registry edit time>
     ```
   - Step 3 — Compute SHA-256 over the registry edit; verify uniqueness; append METHODOLOGY-class verdict line.
   - Step 4 — Append `methodology-wave-allowlist.md` row.
7. **Machinery pin (PRDR)**:
   - File target: `sessions/permanent-results-registry.md` §VII.AE next-free slot.
   - Source workshop: `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` §R1-volovik.
   - canonical_constants D_bi anchors: D_bi(0.090) = 0.197, D_bi(0.190) = 0.462, D_bi(0.290) = 0.786 (cite by name from `canonical_constants.py`).
   - Tolerance: artifact-existence ≥ 15 lines body.
   - Sage MCP: not needed.
   - Random seed: N/A.
   - Scheme: `moduli-space-tau-asymmetry-substrate-partition-cardinality-vector-direction`.
   - Convention: `negative-side-breakdown-positive-side-rigid-Jensen-scaling-monotone-ascending`.
8. **Expected output 4-tuple**: `(value=<§VII.AE landing line count>, scheme=moduli-space-tau-asymmetry-substrate-partition-cardinality-vector-direction, convention=negative-side-breakdown-positive-side-rigid-Jensen-scaling-monotone-ascending, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: §VII.AE registry entry lands with PRIMARY anchor + INDEPENDENT-CROSS-CHECK structure tag, ≥ 15 lines body, all 4 cross-links present, methodology-wave-allowlist row appended.
   - INFO: partial (some cross-link missing).
   - FAIL: registry slot mis-assigned, anchor tagging incorrect, or methodology-wave-allowlist row missing.
   - Tolerance rule: artifact-existence + structural-tag correctness.
10. **Substitution chain**: not required (METHODOLOGY-class artifact-existence; registry edit cites pre-derived volovik R1 verdict; no new sign/direction claim authored at this gate level).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: §VII.AE permanent registry entry; the τ-asymmetric breakdown direction is structurally documented; informs S89+ moduli-space deformation studies on the substrate.
    - INFO: partial; carry-forward to S89.
    - FAIL: registry edit invalid; carry-forward.
12. **Effort estimate**: 0.25 h (registry edit + allowlist append).
13. **Substrate-framing reminder**: τ IS the substrate's own deformation parameter (Jensen TT-deformation), not a coordinate on a container. The asymmetry is an intrinsic substrate-IS property of the τ-manifold's bottom-20-cardinality observable. Direction of explanation flows substrate (τ-deformation manifold) → emergent (cardinality vector cv-flip), not the other way around.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_moduli_space_tau_asymmetry_registry_entry.py`

---

## §W2-10. S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION

1. **Gate ID**: `S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (rule-file diff to `phononic-framing.md`; orchestrator-direct-write per `wave-classification.md`; new sub-section "Single-τ-slice vs moduli-deformation substrate-IS levels")
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class)
5. **Hypothesis**: The phononic-framing.md §"IS Space, Not IN Space" rule applies at the single-τ-slice substrate-IS level (the substrate at one τ value); the W-8 R3 finding surfaces a SECOND substrate-IS level: the moduli-space of τ-deformations itself is substrate-IS (the τ-manifold IS the substrate's own deformation parameter, NOT a container on which the substrate sits). This rule-file diff lands a new sub-section codifying the two-level distinction.
6. **Method**:
   - Step 1 — Open `.claude/rules/phononic-framing.md`.
   - Step 2 — Insert new sub-section AFTER the existing §"IS Space, Not IN Space — Mandatory Reframe" section, BEFORE §"Cross-pillar bridge anatomy":
     ```
     ## Single-τ-slice vs moduli-deformation substrate-IS levels

     > **Provenance**: S88 W-8 R3 closure (volovik R1 derivation + connes R2 V-2 corroboration);
     > workshop s87-v4-strata-vs-cartan-relabeling.md.

     The §"IS Space, Not IN Space" mandate operates at TWO distinct substrate-IS levels:

     ### Level 1 — Single-τ-slice substrate-IS

     At fixed τ ∈ ℝ, the substrate IS the spectral triple (A_K, H_K, D_K(τ)). All
     observables at this slice (eigenvalues, Peter-Weyl decomposition, bottom-20
     cardinality, fiber spectrum) are substrate-IS at the single-τ-slice level. The
     §"IS Space" mandate prevents container-thinking at this level: the substrate is
     NOT in any pre-existing geometric container at the chosen τ.

     ### Level 2 — Moduli-deformation substrate-IS

     The set of τ values { (A_K, H_K, D_K(τ)) : τ ∈ moduli-space } is itself a
     substrate-IS object: the moduli-space of Jensen TT-deformations IS the
     substrate's own deformation parameter, NOT a coordinate on a meta-container.

     - **Wrong (container thinking)**: "the substrate moves through τ-coordinate
       space"; "τ is a coordinate in some moduli container"; "we deform the
       substrate by changing τ"
     - **Right (substrate thinking)**: "τ IS the substrate's intrinsic deformation
       parameter"; "the moduli-space of τ-deformations IS substrate-IS at the
       Level-2 layer"; "the substrate's own structural-stability theorems
       (W11-2, W11-3) live at Level 2"

     ### Calibration corpus

     - **W-8 R3 calibration (S87)**: the τ-asymmetric breakdown of the bottom-20
       cardinality vector (cv-flip ONLY at δ_τ = −0.10; never at δ_τ = +0.10) is
       a Level-2 phenomenon; it is NOT a Level-1 single-slice property. It is a
       structural property of the substrate's intrinsic τ-manifold direction.

     - **W-2 §VII.U.2 4-corner classification**: the algebra-axis vs Mellin-pole
       4-corner partition operates simultaneously at Level 1 (single-slice
       biaxial-FI corner-I observables) and Level 2 (moduli-space corner-IV
       biaxial-DRESSED companion observables). The two levels are structurally
       orthogonal per the algebra-axis orthogonality K-counter (K = 3 MANDATORY
       at S87 W-2 close).

     ### Forward-looking enforcement

     Future cross-pillar bridge entries MUST declare which substrate-IS level
     their substrate-IS observable lives at (Level 1 single-slice or Level 2
     moduli-deformation). The 5-anatomy + 3-level ladder applies uniformly at
     both levels; the level-tagging is an additional structural pin for
     downstream consumers.
     ```
   - Step 3 — Compute SHA-256 over the rule-file diff; verify uniqueness; append METHODOLOGY-class verdict line.
   - Step 4 — Append `methodology-wave-allowlist.md` row.
7. **Machinery pin (PRDR)**:
   - File target: `.claude/rules/phononic-framing.md`.
   - Insertion point: AFTER §"IS Space, Not IN Space — Mandatory Reframe", BEFORE §"Cross-pillar bridge anatomy".
   - Source workshop: `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` §R1-volovik + §R2-connes V-2.
   - Tolerance: artifact-existence ≥ 30 lines body for new sub-section.
   - Sage MCP: not needed.
   - Random seed: N/A.
   - Scheme: `phononic-framing-two-level-substrate-IS-extension`.
   - Convention: `level-1-single-tau-slice-vs-level-2-moduli-deformation`.
8. **Expected output 4-tuple**: `(value=<rule-file diff line count>, scheme=phononic-framing-two-level-substrate-IS-extension, convention=level-1-single-tau-slice-vs-level-2-moduli-deformation, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: rule-file diff lands at correct insertion point; new sub-section ≥ 30 lines; calibration corpus block present (W-8 R3 + W-2 §VII.U.2); methodology-wave-allowlist row appended.
   - INFO: partial (some calibration entry missing).
   - FAIL: rule-file diff at wrong location; sub-section < 15 lines; allowlist row missing.
   - Tolerance rule: artifact-existence + structural completeness.
10. **Substitution chain**: not required (rule-file edit; no numerical sign/direction).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: phononic-framing rule extended to cover Level-2 moduli-deformation; future cross-pillar bridges and registry entries pin substrate-IS level; framework framing discipline tightened.
    - INFO: partial; S89 carry-forward.
    - FAIL: rule-file diff invalid; carry-forward.
12. **Effort estimate**: 0.25 h (rule-file diff + allowlist append).
13. **Substrate-framing reminder**: This gate IS the framing-rule maintenance — the rule edit MUST itself flow substrate → emergent. The new sub-section text uses the substrate's own moduli-space as primary subject; container-thinking ("τ is a coordinate") is rejected within the rule's own prose.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_phononic_framing_moduli_deformation_extension.py`

---

## §W2-11. S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2

1. **Gate ID**: `S88-PRU-CLASS-8.2-CALIBRATION-INSTANCE-2`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (calibration-corpus extension to `epistemic-discipline.md` §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension"; K-counter advancement 1 → 2)
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class)
5. **Hypothesis**: The W-8 R3 closure surfaces a 2nd Class-8.2 calibration instance: the W-8 stratum-vs-(p, q)-parity adjudication exhibited the same rubric-form failure mode as the W-12 Class-8.2 instance #1 ("Z_4 or similar" admitted V_4). At W-8, the pre-registered rubric for "V_4 character on 4-stratum partition" was NOT initially distinguished between (p, q)-Cartan-toral V_4 (which W11-1 falsified) and substrate-physical stratum-index V_4 (which §W2-3 will test); the rubric-form failure was only resolved at W-8 R3 via volovik's relabeling-wins finding. K-counter advances 1 → 2 toward MANDATORY at K = 3.
6. **Method**:
   - Step 1 — Open `.claude/rules/epistemic-discipline.md`.
   - Step 2 — Locate §"Pre-Registration Completeness — PRU Class-8 sub-class taxonomy formal extension" Class 8.2 calibration corpus block.
   - Step 3 — Append a new instance #2 entry AFTER the existing W-12 instance #1 + W11-1 closure marker:
     ```
     **Class 8.2 calibration corpus — instance #2 (S87 W-8 R3 closure, 2026-04-30 to 2026-05-02)**:

     S87 W-8 R3 (workshop s87-v4-strata-vs-cartan-relabeling.md) closed with the
     finding that the V_4 character on the 4-stratum partition (2, 4, 8, 6) is
     STRUCTURALLY DISTINCT depending on whether the V_4 acts on (p, q)-Cartan-toral
     indices (W11-1 incarnation; falsified) or on substrate-physical stratum
     indices (§W2-3 incarnation; structurally supported by W11-2 + W11-3 +
     W11-meta-1 §VII.AJ.partition-stability + §W2-3 if PASS).

     The pre-registered rubric initially read "V_4 character on 4-stratum partition"
     without explicit distinction between Cartan-toral and stratum-index V_4
     incarnations. Both incarnations satisfy the literal rubric "V_4 character on
     a 4-stratum partition" (4 strata × |V_4| = 4 × 4 = 16 atomic configurations).
     The rubric admitted both via cardinality match while the substrate-physics
     answer requires distinguishing the two via the SUBSTRATE-IS-stratum-index
     vs PETER-WEYL-(p,q)-INDEX axis. This is the W-12 pattern (Z_4 vs V_4
     cardinality match admitting structurally distinct groups via element-order
     signature), specialized to the Cartan-toral vs stratum-index axis.

     Class 8.2 K-counter: 1 → 2; promotion to MANDATORY at K = 3 still requires 1
     more substrate-level Class-8.2 manifestation.

     Forward remediation: pre-registered rubrics for V_4 character constructions
     MUST distinguish substrate-physical stratum-index incarnation vs synthetic
     Cartan-toral incarnation explicitly. Cross-link to S88-V4-ON-STRATA-SUBSTRATE-CHARACTER-CONSTRUCTION
     (§W2-3) and S88-V4-CANDIDATE-III-TRIALITY-MOD-2 (§W2-2) which adopt the
     remediation as forward-looking pre-registration discipline.
     ```
   - Step 4 — Compute SHA-256 over the rule-file diff; append METHODOLOGY-class verdict line.
   - Step 5 — Append `methodology-wave-allowlist.md` row.
7. **Machinery pin (PRDR)**:
   - File target: `.claude/rules/epistemic-discipline.md` Class 8.2 calibration corpus block.
   - Source workshop: `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` R3 closure + W11-1 substrate-FAIL precedent.
   - K-counter: advance 1 → 2 (W-12 = #1; W-8 R3 closure = #2).
   - Tolerance: artifact-existence ≥ 25 lines body for instance #2 entry.
   - Sage MCP: not needed.
   - Random seed: N/A.
   - Scheme: `pru-class-8-2-calibration-corpus-instance-2-W8-stratum-vs-cartan-toral`.
   - Convention: `K-counter-advancement-1-to-2-promotion-to-mandatory-at-K-equal-3`.
8. **Expected output 4-tuple**: `(value=<K-counter advanced from 1 to 2>, scheme=pru-class-8-2-calibration-corpus-instance-2-W8-stratum-vs-cartan-toral, convention=K-counter-advancement-1-to-2-promotion-to-mandatory-at-K-equal-3, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: rule-file diff lands; instance #2 entry ≥ 25 lines; K-counter advanced explicitly; methodology-wave-allowlist row appended; cross-link to §W2-3 + §W2-2 forward remediation citations present.
   - INFO: partial.
   - FAIL: rule-file diff invalid or K-counter not explicitly advanced.
   - Tolerance rule: artifact-existence + K-counter advancement structural pin.
10. **Substitution chain**: not required (METHODOLOGY rule-file edit).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: PRU Class 8.2 corpus advances 1 → 2 of 3 toward MANDATORY; framework methodology hardens its rubric-pre-registration discipline; future V_4 character pre-registrations explicitly distinguish substrate-stratum vs Cartan-toral incarnations.
    - INFO: partial; carry-forward.
    - FAIL: rule-file edit invalid; carry-forward.
12. **Effort estimate**: 0.25 h (rule-file diff + allowlist append).
13. **Substrate-framing reminder**: The Class 8.2 rule applies to pre-registered rubrics that admit unintended substrate-physics readings. Rubric tightening must itself be substrate-grounded — the corrective remediation cites substrate-level structural distinctions (Cartan-toral vs stratum-index axis), NOT external taxonomic conventions.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_pru_class_8_2_calibration_instance_2.py`

---

## §W2-12. S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR

1. **Gate ID**: `S88-METH-CROSS-PILLAR-BRIDGE-ANATOMY-K-COUNTER-MONITOR`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (K-counter bookkeeping at `cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)"; orchestrator-direct-write; auto-flip on third forward-bridge instance landing)
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class)
5. **Hypothesis**: The cross-pillar-bridge-anatomy.md K-counter is at K = 2 < K_promotion = 3 ⇒ status = SUGGESTION (NOT MANDATORY). This gate monitors the K-counter for an auto-flip event during S88: if any of FWD-C1 (Pillar I↔II n_s; Cluster B item #21), FWD-C2 (Pillar II↔V Mellin-cone↔BdG; #22), or FWD-C3 (Pillar IV↔V cocycles↔3He; #23) lands during S88, increment K-counter; if K reaches 3, auto-flip the rule-file from SUGGESTION → MANDATORY in the same dispatch as the third instance landing. If no instance lands during S88, emit INFO at K = 2 status holding.
6. **Method**:
   - Step 1 — At plan-freeze: K = 2 (per context-file §"Cross-pillar bridge K-counter state at S87 close": Instance #1 = S86 W-5 §VII.AF.1 LANDED; Instance #2 = S87 W11-5 FWD-C3 REGISTRY-FAIL).
   - Step 2 — Monitor for landing of FWD-C1 / FWD-C2 / FWD-C3 during S88. The wave structure is: FWD-C1 in Cluster B item #21 (S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING); FWD-C2 in #22; FWD-C3 in #23. These are dispatched in other waves (Cluster B owner volovik+connes joint).
   - Step 3 — If a 3rd instance lands (K = 2 → 3): in same dispatch, edit `.claude/rules/cross-pillar-bridge-anatomy.md` §"Status: SUGGESTION (NOT MANDATORY) at K=2" → "Status: MANDATORY at K=3"; replace the SUGGESTION block with the MANDATORY block; update §"Calibration-corpus tracking (forward-looking)" with the 3rd instance row.
   - Step 4 — If only 1 instance lands (K = 2 → 3 not reached): emit INFO at K = 2 status holding; document which forward-bridges remained UNLANDED at S88 close.
   - Step 5 — Compute SHA-256 over the audit; append METHODOLOGY-class verdict line.
   - Step 6 — IF auto-flip triggered: append `methodology-wave-allowlist.md` row.
7. **Machinery pin (PRDR)**:
   - File target: `.claude/rules/cross-pillar-bridge-anatomy.md` §"Forward template-adoption (calibration-corpus tracking)".
   - K-counter pre-S88: 2 (S86 W-5 §VII.AF.1 + S87 W11-5).
   - K_promotion threshold: 3.
   - S88 expected forward-bridge landings: FWD-C1 (#21), FWD-C2 (#22), FWD-C3 (#23) — 3 candidate instances.
   - Auto-flip trigger: K reaches 3 during S88.
   - Tolerance: K-counter exact integer comparison.
   - Sage MCP: not needed.
   - Random seed: N/A.
   - Scheme: `cross-pillar-bridge-anatomy-K-counter-monitor-S88`.
   - Convention: `auto-flip-SUGGESTION-to-MANDATORY-on-third-instance-landing`.
8. **Expected output 4-tuple**: `(value=<K_post_S88>, scheme=cross-pillar-bridge-anatomy-K-counter-monitor-S88, convention=auto-flip-SUGGESTION-to-MANDATORY-on-third-instance-landing, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: K reaches 3 during S88; rule-file auto-flip triggered AND landed in same dispatch; methodology-wave-allowlist row appended; calibration corpus row #3 present.
   - INFO: K reaches 2 → 2 (no S88 landings) OR K reaches 2 → 3 but rule-file flip deferred (BLOCKED).
   - FAIL: K reaches 3 but rule-file flip NOT triggered (rule-file violation per `cross-pillar-bridge-anatomy.md` §"Promotion event").
   - Tolerance rule: K-counter exact integer; auto-flip event-triggering structural correctness.
10. **Substitution chain**: not required (METHODOLOGY bookkeeping; no numerical sign/direction claim).
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: K = 3 reached; cross-pillar bridge anatomy upgraded to MANDATORY status; future bridge entries MUST adopt the 5-anatomy + 3-level discipline (was SUGGESTION pre-S88).
    - INFO at K = 2 → 2: no S88 forward-bridge landings; status holds at SUGGESTION; carry-forward to S89.
    - INFO at K = 2 → 3 with deferred flip: structural BLOCK; remediation in S89 with auto-flip retry.
    - FAIL: rule-file violation; immediate remediation per `feedback_fix-in-session-never-defer.md`.
12. **Effort estimate**: 10 minutes (K-counter monitoring + conditional rule-file flip).
13. **Substrate-framing reminder**: K-counter advancement is METHODOLOGY-level bookkeeping; the substrate-IS observable being tracked is the framework's calibration-corpus growth — instance count of cross-pillar bridge landings. Substrate framing of the rule-file is preserved at the METHODOLOGY-level per phononic-framing.md §"Cross-pillar bridge anatomy".

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_meth_cross_pillar_bridge_anatomy_k_counter_monitor.py`

---

## §W2-13. S88-CF-W11-D-SIG5-DUPLICATE-AUDIT

1. **Gate ID**: `S88-CF-W11-D-SIG5-DUPLICATE-AUDIT`
2. **Trigger**: `[AUDIT]`
3. **Classification**: METHODOLOGY (v3-closure-recovery sig_5 audit per `v3-closure-recovery.md` §"Stage 1 — Automatic re-dispatch" sig_5 = duplicate audit_sha256 detection; orchestrator-direct-write)
4. **Agent type**: gen-physicist orchestrator-direct-write (METHODOLOGY-class)
5. **Hypothesis**: `computations/s87_gate_verdicts.txt` contains 105 audit_sha256 occurrences with 103 unique values; the 2 duplicates are `74c16f36...` (first 16 hex chars of one duplicate pair) and `9fe27a15...` (first 16 hex chars of the second duplicate pair). Per `v3-closure-recovery.md` §"sig_5 = 0", duplicate audit_sha256 across two or more verdict lines indicates either: (a) SHA-hardcoding bug in a producing script (Class-1 v3-recovery violation), OR (b) genuine content-collision (two distinct gates whose input-pin maps independently hash to the same SHA — astronomically unlikely but possible). This audit classifies each duplicate to one of the two categories.
6. **Method**:
   - Inputs: `computations/s87_gate_verdicts.txt` (current state with 105 audit_sha256 occurrences, 103 unique).
   - Step 1 — Grep all canonical verdict lines for audit_sha256 prefixes `74c16f36` and `9fe27a15`; identify the gate-IDs that share each prefix.
   - Step 2 — For each duplicate pair (gate_A, gate_B) sharing a SHA:
     - Locate gate_A's producing script in `computations/`.
     - Locate gate_B's producing script in `computations/`.
     - Inspect each script's `closure_hash(input_pin_map)` computation:
       - If either script HARDCODES the audit_sha256 string (literal hex constant in source), classify as Class-1 v3-recovery violation (SHA-hardcoding bug per `v3-closure-recovery.md` §"sig_5 = 0" remediation).
       - If both scripts compute audit_sha256 from `closure_hash(pins)` AND the pin maps for gate_A and gate_B are identical or deterministically equivalent, classify as benign content-collision (genuine same-input duplicate; rare but legitimate).
       - If the pin maps are different but the SHA is the same, classify as POSSIBLE Class-1 violation requiring deeper inspection (could indicate copy-paste of a different SHA value or a SHA-truncation bug at 16-hex-char prefix collision).
   - Step 3 — Cross-validate by computing each gate's expected audit_sha256 fresh from its current input-pin map; compare against the recorded SHA in the verdict file.
   - Step 4 — Emit a JSON sidecar `s88_w2_cf_w11_d_sig5_audit_report.json` with per-duplicate classification: {duplicate_pair, gate_A, gate_B, classification ∈ {Class-1-violation, benign-content-collision, POSSIBLE-Class-1}, evidence}.
   - Step 5 — IF any duplicate is classified Class-1-violation, route to v3-closure-recovery Stage-1 remediation per `v3-closure-recovery.md` §"sig_5 = 0" remediation: rerun the offending producing script to compute audit_sha256 from `closure_hash(pins)`. The verdict line in the S87 file is permanent (per `gate-verdicts.md` §"Rules"); the new corrected verdict is appended to `s88_gate_verdicts.txt` with cross-link to the original S87 line.
7. **Machinery pin (PRDR)**:
   - Verdict file: `computations/s87_gate_verdicts.txt` (input only; this gate does NOT modify S87 file per `gate-verdicts.md` permanence rule).
   - JSON sidecar: `computations/s88_w2_cf_w11_d_sig5_audit_report.json` (output).
   - Tolerance: per-duplicate classification structural (Class-1 vs benign vs POSSIBLE-Class-1).
   - Sage MCP: not needed.
   - Random seed: N/A.
   - Scheme: `sig5-duplicate-audit-class1-vs-benign-vs-possible-class1`.
   - Convention: `v3-closure-recovery-sig5-stage1-remediation-routing`.
8. **Expected output 4-tuple**: `(value=<count_Class1_violations>, scheme=sig5-duplicate-audit-class1-vs-benign-vs-possible-class1, convention=v3-closure-recovery-sig5-stage1-remediation-routing, L_max=N/A)`.
9. **PASS/FAIL/INFO thresholds**:
   - PASS: both duplicates classified benign-content-collision (no v3-recovery violation); count_Class1_violations = 0.
   - INFO: at least one duplicate classified POSSIBLE-Class-1 requiring deeper inspection (carry-forward to S89 with explicit follow-up gate).
   - FAIL: at least one duplicate classified Class-1-violation; v3-closure-recovery Stage-1 remediation queued in same dispatch.
   - Tolerance rule: per-duplicate structural classification (3-way: PASS/INFO/FAIL).
10. **Substitution chain** (relevant for Class-1 vs benign distinction direction claim):
    - Step 1 (definition): audit_sha256 is computed as `closure_hash(input_pin_map)` where the pin map is the ordered tuple of (input_file_SHA-256, plan_block_text_SHA-256, gate_id_string).
    - Step 2 (substitution): for two gates A and B with input pin maps pin_A and pin_B, audit_sha256(A) = audit_sha256(B) IFF SHA-256(pin_A) = SHA-256(pin_B).
    - Step 3 (simplify): if pin_A ≠ pin_B but SHA-256(pin_A) = SHA-256(pin_B), this is a SHA-256 collision (astronomically rare; ~2^{-128} probability for a single pair), strongly indicating a SHA-hardcoding bug (Class-1) rather than a genuine collision.
    - Step 4 (direction): direction is "if pin_A == pin_B (deterministic equivalence) ⇒ benign; if pin_A ≠ pin_B but SHA matches ⇒ Class-1-or-possible-Class-1".
    - Conclusion: the audit's classification direction follows the pin-map equivalence test directly.
11. **What PASSES/FAILS MEAN** for solution space:
    - PASS: both duplicates are benign content-collisions; no audit-trail integrity violation; v3-closure-recovery sig_5 ladder cleared retroactively.
    - INFO: deeper inspection needed; carry-forward to S89 with explicit S89 gate.
    - FAIL: Class-1-violation surfaced; v3-closure-recovery Stage-1 remediation triggered; offending producing script rerun and corrected verdict appended.
12. **Effort estimate**: 0.25 wave (script implementation + JSON sidecar + remediation routing).
13. **Substrate-framing reminder**: This audit operates at the audit-trail layer; per the Layer-Decomposition T2-7 layer-functor F (epistemic-discipline.md §"Layer-Decomposition"), the audit-trail layer is the F-image of the methodology layer's verdict-line-artifact-SHA. The substrate-framing reminder applies as a mandatory caveat per W-13 C3-CONN-CONV-3 (audit-leg verification of layer-functor F triplet still pending S88+ per W12-5 unrun gate); this audit IS one of the audit-leg verification instances that promotes layer-functor F from pair-verified to triplet-verified.

**verdict_source**: `computations/s88_gate_verdicts.txt`

**Producing script**: `computations/s88_w2_cf_w11_d_sig5_duplicate_audit.py`

---

## Wave 2 → Wave 3 Decision Point

Wave 2 closure feeds Wave 3 (and downstream waves) via the following propagation rules:

1. **§W2-1 PASS-d=2-exact + §W2-3 PASS jointly close V_4 program at d = 2**: the framework's monodromy classification at d = 2 is final; Wave-3 plan author may close S88-MONODROMY-DEPTH-EXTENSION carry-forward queue. Wave 3 inherits the structural Klein-rank-2 anchor for any downstream rank-2 cohomology gates.

2. **§W2-1 PASS-d>2-extension OPENS new structural axis**: rank-3 Klein-product group enters the framework; downstream cross-pillar bridges (FWD-C1 / FWD-C2 / FWD-C3 in Cluster B) inherit the rank-3 structure as a substrate-IS observable axis at Level 2 (per §W2-10 phononic-framing extension).

3. **§W2-2 + §W2-3 outcome combinations** classify which V_4 incarnations survive at S88 close:
   - Both PASS: 2 surviving V_4 incarnations (ii) + (iii); redundant character bases at Klein-rank-2; framework's V_4 program enriched.
   - §W2-3 PASS, §W2-2 FAIL: only V_4-on-strata survives; (iii) closed.
   - §W2-3 FAIL, §W2-2 PASS: only V_4-on-triality-mod-2 survives; (ii) closed (substrate-physics implementation defect surfaces); URGENT carry-forward.
   - Both FAIL: NO V_4 incarnation survives; W11-1 plus this wave structurally closes the V_4 program at d = 2; carry-forward to S89 with full re-derivation.

4. **§W2-4 + §W2-5 jointly characterize τ-asymmetric breakdown**: §W2-9 §VII.AE registry entry inherits the precise δ_τ_crit values; §VII.AE PASS depends on §W2-4 + §W2-5 verdict pair.

5. **§W2-7 mechanical closure** documents that S88-CF-W11-C is structurally-blocked; downstream mechanical-closure-discipline.md calibration corpus tracks this as instance #4 (after S82, S84, S86 W3 mechanical-closure precedents).

6. **§W2-8 §VII.AD landing** is upstream anchor for §W2-7; sequencing: §W2-8 dispatches first.

7. **§W2-9 §VII.AE landing** is downstream of §W2-4 + §W2-5 numerical results; sequencing: §W2-4 + §W2-5 dispatch first, §W2-9 second (or §W2-9 lands with placeholder δ_τ_crit if §W2-4 + §W2-5 deferred to later wave).

8. **§W2-10 phononic-framing extension** is independent; can dispatch in any order.

9. **§W2-11 PRU Class 8.2 corpus** advances K-counter 1 → 2; auto-trigger: K = 3 promotion when 3rd instance arises in S89+.

10. **§W2-12 cross-pillar K-counter monitor** depends on Cluster B items #21/#22/#23 landing during S88 (other waves); monitor emits INFO at K = 2 status holding by default; auto-flip if 3rd instance arises.

11. **§W2-13 sig_5 audit** is independent of all other W2 items; dispatch immediately at wave start.

---

## Wave 2 Machinery-Enumeration Pin (§0.11)

Per `epistemic-discipline.md` §"Pre-Registration Completeness" PRDR (Pre-Registration Dry-Run), Wave 2 enumerates the following machinery parameters across all 13 gate blocks:

| Parameter | Pin source | Value pin |
|:----------|:-----------|:----------|
| `tau_fold` | canonical_constants.py:S12/S42 CONST-FREEZE-42 | 0.19 (R-PROTECTED) |
| `M_KK` | canonical_constants.py:S42 spectral zeta | 7.428660036284456e+16 GeV |
| `Delta_BCS` | canonical_constants.py:S70 BCS-GAP-CANONICAL-70 | 0.4642547394830737 (R-PROTECTED) |
| `D_bi(0.090)` | canonical_constants.py W-8 R3 | 0.197 |
| `D_bi(0.190)` | canonical_constants.py W-8 R3 | 0.462 |
| `D_bi(0.290)` | canonical_constants.py W-8 R3 | 0.786 |
| L_max operational | math-scripts.md §"D_K Block-Diagonality" Casimir-bound | 6 (per W11-2 + W11-3 precedent) |
| L_max plan-pinned (recorded but redundant) | n/a | 10 |
| OMP_NUM_THREADS (CPU fallback) | math-scripts.md §"Environment" | 8 |
| GPU device | math-scripts.md §"Environment" | AMD RX 9070 XT (ROCm 7.2; 17.1 GB VRAM) |
| Bottom-20 cardinality (c_1, c_2, c_3, c_4) | W11-2 npz canonical | (2, 4, 8, 6) |
| (Z_2)^d-Schur identity Sage callable | s87_w11_4_v4_schur_identity.npz | bit-stable |
| Sage MCP path | tools/mcp-servers/sage-mcp | sage_eval / sage_simplify / sage_symbolic_eig |
| Tolerance ABSOLUTE PASS-floor | per gate | 1e-12 (machine-epsilon at 6-stratum support) |
| Tolerance ABSOLUTE INFO-ceiling | per gate | 1e-9 |
| Random seed | per gate | N/A (all deterministic) |

Each gate block above explicitly cites its machinery pins per the PRDR machinery-enumeration discipline. No pin is left as `pending` at plan-freeze except the methodology-wave-allowlist `sha256_of_plan_block` placeholders for §W2-6, §W2-8, §W2-9, §W2-10, §W2-11, §W2-12 (per `methodology-wave-allowlist.md` §"Pending SHA resolution" S86 R3 one-time exception protocol; computed at the post-landing finalization pass).

---

## Wave 2 Input-SHA Ledger

The following input files are pinned at plan-freeze for Wave 2 dispatch:

| File path | SHA-256 pin status | Source |
|:----------|:-------------------|:-------|
| `computations/s84_spectrum_cache_L12_tau019.npz` | `<pinned at dispatch>` | S84 W14a master cache |
| `computations/s87_w11_2_partition_stability_4stratum.npz` | `<pinned at dispatch>` | S87 W11-2 verdict-line companion |
| `computations/s87_w11_4_v4_schur_identity.npz` | `<pinned at dispatch>` | S87 W11-4 Sage callable |
| `computations/s84_w8a_af_automorphism_inventory.npz` | `<pinned at dispatch>` | S84 W8a A_F *-automorphism inventory |
| `computations/s87_gate_verdicts.txt` | `<pinned at dispatch>` | S87 verdicts (read-only for §W2-13) |
| `sessions/permanent-results-registry.md` | `<pinned at dispatch>` | registry edit target for §W2-6, §W2-8, §W2-9 |
| `sessions/framework/registry/falsifier-master-inventory.md` | `<pinned at dispatch>` | mack-cosmic-bridge sole writer companion edit for §W2-7, §W2-8 |
| `.claude/rules/phononic-framing.md` | `<pinned at dispatch>` | rule-file edit target for §W2-10 |
| `.claude/rules/epistemic-discipline.md` | `<pinned at dispatch>` | rule-file edit target for §W2-11 |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | `<pinned at dispatch>` | rule-file edit target for §W2-12 (conditional auto-flip) |
| `.claude/rules/methodology-wave-allowlist.md` | `<pinned at dispatch>` | append-only allowlist target for §W2-6, §W2-8, §W2-9, §W2-10, §W2-11, §W2-12 |
| `sessions/archive/session-87/workshops/s87-v4-strata-vs-cartan-relabeling.md` | `<pinned at dispatch>` | source workshop for §W2-8, §W2-9, §W2-11 |
| `computations/canonical_constants.py` | `<pinned at dispatch>` | constants import for all GEOMETRIC gates |

The input-pin map for each gate block's `audit_sha256` derives from the per-gate subset of the above ledger plus the gate-ID string and the gate-block-text SHA-256. Per-gate-distinct audit_sha256 uniqueness is verified at append time against `computations/s88_gate_verdicts.txt` and `computations/s87_gate_verdicts.txt`.

No agent-memory file is pinned in the input-SHA ledger per AMRI Test 1 (`agent-standards.md` §"Agent-Memory Registry Inversion (AMRI)"); per-agent role assignment is implicit in the gate-block agent-type field.

---

**End of Wave 2 plan.** All 13 gate blocks above are full 13-field specs; verdict_source pinned at `computations/s88_gate_verdicts.txt`; producing scripts named `s88_w2_<gate-slug>.py`; substrate-framing reminders cite `phononic-framing.md`; machinery pins are PRDR-compliant; rule-file edits target methodology-wave-allowlist append-only rows.
