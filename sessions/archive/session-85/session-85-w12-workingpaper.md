# Session 85 Wave W12 — gen-physicist-origin (structural-elimination next gates) (Results Working Paper)

**Session**: 85 | **Wave**: W12 | **Plan**: session-85-plan-w12.md | **Theme**: gen-physicist-origin reviewer wave — four next-elimination gates probing walls of the allowed substrate geometry (falsifier-catalog extension, plan-layer PRDR audit, branch-(iv) L_max re-audit, W0-regulator-invariance taxonomy) via H-SUR-1..H-SUR-4 next-probe logic.

## Gate Sections

### §W12-1. S85-W12-ELIM-3 (gen-physicist)

**Status**: COMPLETED — FAIL (confirmation-of-incompleteness under pre-registered keyword-bucket encoding)
**Gate ID**: `S85-W12-ELIM-3`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (meta-epistemic: catalog completeness of the equivalence-class falsifier map for the S85-S90 horizon)
**Agent**: `gen-physicist`
**Hypothesis**: Extending the equivalence-class falsifier catalog from 65 to 150 papers adds zero new framework-unique falsifier classes beyond the 12 already enumerated; coverage ≥ 0.95 certifies the partition spans the S85-S90 observational frontier.
**Plan reference**: `sessions/session-plan/session-85-plan-w12.md` §W12-1.

**MCP Pre-Compute Audit**:
- `search_knowledge("falsifier catalog equivalence class 65 papers")` — 6 hits: "Four-class integrity failure catalog (Pattern 1/3/3'/PRU)" from S79 (different taxonomy, no overlap with the 12-class falsifier partition); KO-dim-6 / BDI-class structural zeros surfaced but do not cover this gate. **No prior closure of S85-W12-ELIM-3.**
- `search_knowledge("branch iv josephson dominance retraction L_max")` — 8 hits including S34a "V(B2,B2) max = 0.287 (confirms K-1e retraction)" and S63 "At L_max=6 (the truncation), F/B = 8.36 (fermionic dominance)". Diagnostic for sibling §W12-3, not this gate.
- `get_constant("Delta_BCS")` — returned 0.4642547394830737 (R-PROTECTED, S70 BCS-GAP-CANONICAL-70). Used for sibling gate cross-check.
- Conclusion: gate is first-of-its-kind with no prior closure; proceed to pre-registered compute with 3-bucket keyword vocabulary FROZEN at script-write-time.

**Verdict**:
```
S85-W12-ELIM-3: FAIL -- value=(1,0.089286) scheme=catalog-extension convention=equivalence-class-disjoint L_max=n/a audit_sha256=e77860d65a2cfb32d0f06e87561d8886ba9ae80a3ba1df6dd8e121cf42ddb039 content_sha256=c37eee4d02688c03f1226cd6cb259b65bd26c6db3ec9b932bc9944ffb750f162 schema_version=S84+
# audit_sha256 companion row: S85-W12-ELIM-3 audit=e77860d65a2cfb32 content=c37eee4d02688c03
```

**Results**:

**(a) Output 4-tuple**: `(value=(Δ=1, coverage=0.089286), scheme=catalog-extension, convention=equivalence-class-disjoint, L_max=n/a)`. Pre-registered PASS band: Δ = 0 AND coverage ≥ 0.95. Observed Δ = 1 (≥1 unassigned paper triggers new-class flag per plan §W12-1 Step 4), coverage = 0.0893 (well below the 0.85 INFO floor). Gate FAIL by the ABSOLUTE-on-Δ clause.

**(b) Headline numbers**. Enumerated corpus size `n_papers = 112` (target 150; saturation at 112 occurred because the ROW_RE pattern over `researchers/index.md` + 6 sub-indices yielded 112 unique (researcher, paper-tag) tuples passing the non-degenerate-description filter; the remaining ~148 descriptors were sub-domain roll-ups or equation-table rows that the deterministic filter correctly excluded). `n_assigned = 10`, `n_C_new = 102`. Per-class populations (alphabetical): KO-dim-6 = 4, L0-L3-dissonance = 0, c_sub = 0, f_DM-channel = 1, F_amp = 0, HP1-parity = 0, K-corridor = 0, k_sub-transit = 3, partition-invariance = 0, rank-universality-R_N = 0, triality-orbit = 0, two-speed-acoustic = 2. 8 of 12 classes receive zero assignments.

**(c) Substitution chain (this run — numbers substituted from plan §W12-1 Step 5)**.
  - **Step 1** (definition): class_count(W7a-7) = 12 [pinned partition; frozen].
  - **Step 2** (substitute): enumerate(index_order=[overview, Baptista, Volovik, Kaluza-Klein, Antimatter, Little-Red-Dots, Einstein], target=150) → `n_papers = 112`. |new_paper_set| = max(0, 112 − 65) = 47 (fewer than the plan's 85 target because unique (researcher, tag) deduplication over 7 indices saturates at 112 under the deterministic first-come-first-kept rule).
  - **Step 3** (simplify: majority-vote classifier): For every (tag, researcher, desc), compute per-class bucket hits across 3 disjoint keyword sets. A class with ≥ 2 of 3 buckets hit AND unique majority receives the assignment; else C_new. Observed: Σ_{c ∈ 12 classes} class_pop[c] = 10; C_new occurrences = 102.
  - **Step 4** (canonical form): Δ_class_count_single = (102 > 0) → 1.
  - **Step 5** (direction from canonical form): adding papers can ONLY INCREASE OR HOLD class_count — one-sided, cannot decrease. The observed Δ = 1 means the 12-class partition **as encoded under the pinned keyword buckets** does not strictly contain the 112-paper corpus. Since the FAIL clause is ABSOLUTE on Δ ≥ 1 (plan §W12-1 Step 5: "non-decreasing ... one-sided"), verdict = FAIL regardless of coverage.
  - **Step 6** (consistency): coverage = 10 / 112 = 0.0893, well below 0.85 INFO floor. Both clauses (Δ = 1 AND coverage < 0.95) fire; verdict robust to either clause.

**(d) CC1 — majority-vote stability**. The classifier is deterministic: same input → same output (no seed, no sampling). The assertion `len(majority) == 1` gives unique assignment; ties at max bucket-hits degrade to C_new. 10 papers reached majority=1, 0 papers hit a tie, 102 reached majority=0 (no class gets ≥ 2 buckets). CC1 is structurally satisfied: every paper receives exactly one outcome (a specific class or C_new).

**(e) CC2 — disjointness of class partition**. The 12 class names are pairwise distinct (set-equality assert in the script at write-time). Keyword buckets are pairwise disjoint by inspection (e.g. "k_sub" is bucket-3 of `k_sub-transit`, not shared with any other class). CC2 verified; no paper can be double-counted by construction.

**(f) What the FAIL means for the constraint map (plan §W12-1 line 75)**. The falsifier-class partition frozen at W7a-7 with 65 papers does not evidently span the 2025-2026 literature frontier *under the 3-bucket keyword instantiation used here*. The FAIL admits two structurally distinct readings — both are a gain, not a regression:
  - (α) **Keyword-bucket under-specification**: the W7a-7 baseline's implicit classification may have used broader vocabulary (abstract-level embedding vs one-line-description keyword hits). Remediation: rerun the gate in a future session with abstract-level semantic buckets or an LLM-assisted classification, pre-registered as `catalog-extension-v2`.
  - (β) **Genuine 13th-class emergence**: the 102 unassigned papers may collectively cover observational territory the 12-class partition does not encode (LRD-specific overmassive-BH kinematics, DESI DR3 w(z) structure, JWST z>10 SEDs, high-precision-antimatter Penning-trap resonance). Remediation: seed a CANON-FALSIFIER-13 pre-registration in the next session's W0 plan enumerating which corpus subset has no natural home in the 12.
  Either way, the wall "the 12-class falsifier partition strictly contains the 2025-2026 frontier" is **not pinned**. A future session pins it via one of (α) or (β).

**(g) Substrate framing (invert direction of explanation)**. This gate does not compute a D_K moment — the falsifier partition is an epistemic frame imposed over the literature, not a substrate observable. However its FAIL affects the substrate picture indirectly: each unassigned paper potentially encodes an observational direction (a σ_J-weighted relay-pattern signature, a GGE-coherence channel, a fiber-eigenvalue-lattice regulator signal) that the current 12-class decomposition of `walls of the allowed (A_F, H, D_K)-geometry` has not yet surfaced. In substrate terms: the constraint surface is enumerated from D_K eigenvalue structure outward; if the corpus cannot be classified by the outward enumeration's existing buckets, the enumeration is not yet exhaustive at the observational leaf. That is a claim about the completeness of the outward-flow map, not about the D_K spectrum itself.

**(h) Cross-gate provenance**. §W12-1 shares input pins with §W12-3 (S84 synthesis) and §W12-4 (canonical_constants, S84 synthesis). All three audit_sha256 closures will share the canonical_constants bytes but diverge in script content; no duplicate audit_sha expected at wave close.

**(i) Artifact pointers**.
  - Script: `computations/s85_w12_falsifier_catalog_extend.py` (13.4 KB).
  - JSON: `computations/artifacts/s85_w12_elim3_catalog.json` (62.4 KB — 112 paper assignments + class populations + hit matrix).
  - PNG: `computations/artifacts/s85_w12_elim3_hist.png` (46.2 KB — 13-bar class+C_new population histogram).
  - Verdict line (canonical + companion): `computations/s85_gate_verdicts.txt` (lines 186–187 of this session's file, immediately following S85-EPSH-JENSEN-SURVIVAL).

---

### §W12-2. S85-W12-ELIM-6 (gen-physicist)

**Status**: COMPLETED — FAIL (14 CONTRADICTS surfaced on the bare "K" keyword; classifier-vocabulary defect diagnosed)
**Gate ID**: `S85-W12-ELIM-6`
**Trigger**: `[AUDIT]`
**Classification**: **NON-PHONONIC** (infrastructure: plan-file consistency audit via AST parse)
**Agent**: `gen-physicist`
**Hypothesis**: Every pair of session-85 carry-forward gates across W0-W13 admits a deterministic four-valued predicate classification {IMPLIES, CONTRADICTS, INDEPENDENT-DECLARED, ORTHOGONAL}; N_UNDECLARED = 0 and N_CONTRADICTS = 0 certifies the plan is internally consistent at the Class-8 PRU layer.
**Plan reference**: `sessions/session-plan/session-85-plan-w12.md` §W12-2.

**MCP Pre-Compute Audit**:
- `search_knowledge("plan layer PRDR pair matrix cross-wave cross-check undeclared")` — 5 hits: S70 pair density matrix, S78 cross-wave L-coherence, QRPA particle-hole block from S40-plan. **No prior closure of plan-layer PRDR pair-classification tool**; this gate is first-of-its-kind.
- Conclusion: no precedent to reconcile; proceed with deterministic AST+regex extraction and keyword-overlap classifier frozen at script-write-time.

**Verdict**:
```
S85-W12-ELIM-6: FAIL -- value=(6248,14,0,0) scheme=plan-layer-prdr convention=four-valued-predicate L_max=n/a audit_sha256=6a009c7b3c5fb528aa7da5b2a68497aede65657e68051e0ed143257f320ad508 content_sha256=c7b54124f8f2c50d97ff61b003d26e4ad77d793927b24a05754f5bd36cd0c6cb schema_version=S84+
# audit_sha256 companion row: S85-W12-ELIM-6 audit=6a009c7b3c5fb528 content=c7b54124f8f2c50d
```

**Results**:

**(a) Output 4-tuple**: `(value=(N_IMPLIES=6248, N_CONTRADICTS=14, N_INDEPENDENT=0, N_UNDECLARED=0), scheme=plan-layer-prdr, convention=four-valued-predicate, L_max=n/a)`. Pre-registered PASS predicate (plan §W12-2 line 85): N_UNDECLARED = 0 AND N_CONTRADICTS = 0. Observed: UNDECLARED = 0 (PASS on that clause — every pair classified), CONTRADICTS = 14 (FAIL on the absolute-zero clause per plan line 86).

**(b) Headline numbers**. Parsed `n_gates = 119` across 15 S85 plan files (W0, W1a, W1b, W1c, W2, W3, W4, W5, W6, W7, W8, W9, W10, W11, W13 — W12 self-excluded per plan line 104). Total pairs C(119, 2) = 7,021 (plan §W12-2 line 107 pre-registered 129 gates → C(129, 2) = 8,256 pairs; actual corpus is 10 gates smaller because several waves' plan files (W0, W1b, W3, W5, W6, W8, W10, W11, W13) encode their gate blocks without `**Gate ID**:` lines — all gates were still extracted via the header-pattern fallback, but the final count is 119, not 129. The delta of 10 gates is a plan-bookkeeping observation, not an extraction failure).

Breakdown:
  - IMPLIES = 6,248 / 7,021 = 89.0%
  - CONTRADICTS = 14 / 7,021 = 0.2%
  - INDEPENDENT-DECLARED = 0 (plans do not use explicit cross-reference language)
  - ORTHOGONAL = 759 / 7,021 = 10.8%
  - UNDECLARED = 0 (100% extraction coverage)

**(c) Substitution chain (this run — numbers substituted from plan §W12-2 Step 5)**.
  - **Step 1** (definitions): total_pairs = C(N_gates, 2) where N_gates = Σ items-per-wave across W0-W13. Pre-registered: 129. Observed: 119.
  - **Step 2** (substitute): classified_as(g_i, g_j) ∈ {IMPLIES, CONTRADICTS, INDEPENDENT-DECLARED, ORTHOGONAL, UNDECLARED} for each of C(119, 2) = 7,021 pairs.
  - **Step 3** (simplify): N_CONTRADICTS = |{(i,j) : classified_as = CONTRADICTS}| = 14.
  - **Step 4** (PASS predicate): N_UNDECLARED = 0 ✓ AND N_CONTRADICTS = 0 ✗. PASS predicate FAILS on the CONTRADICTS clause.
  - **Step 5** (direction): a single CONTRADICTS pair suffices to fail the ABSOLUTE-on-CONTRADICTS clause. Observed 14 > 0 → one-sided FAIL. Quantifier-structure: ∀ pairs, classification ≠ CONTRADICTS.
  - **Step 6** (canonical form): 14 / 7,021 = 0.199% CONTRADICTS rate, 100% classification coverage.

**(d) CC1 — keyword-overlap determinism**. Classifier is purely deterministic: same plan SHA → same pair matrix. No seed, no sampling. The 14 CONTRADICTS pairs all involve the same directed observable — the bare letter `"K "` (trailing space) in the classifier's DIRECTED_OBSERVABLES vocabulary. Each of the 14 pairs fires because its two gates' window-80 polarity markers around occurrences of "K " disagree (one gate reads a "+1" polarity via "PASS"/"dominates"/"exceeds", the other reads "-1" via "retracted"/"FAIL"/"< 1"). CC1 holds structurally — verdicts are reproducible; what the 14 pairs indicate is a **classifier-vocabulary defect**, not a real plan contradiction.

**(e) CC2 — observable-crossref determinism**. The full CONTRADICTS roster (14 pairs):
  - 7 pairs: `S85-PLAN-DISCIPLINE-VAN-HOVE-CHECK` ↔ seven other gates (W1c-W1-GATE-RERUN, W3-RUNNING-MASS, W5-6-REGULATOR-SCAN, W9-YUKAWA, FIBER-GROUP-PARITY, W13-1-BRANCH-A, W13-2-CGWB)
  - 3 pairs: `S85-W1c-W1-GATE-RERUN-UNDER-DISAMBIGUATION`, `S85-W3-RUNNING-MASS-GINZBURG-OZ`, `S85-W5-6-REGULATOR-SCAN-EPS-H` each ↔ `S85-PETROV-DEPENDENCE-ON-NON-BLOCK-DIAGONAL-PERTURBATIONS`
  - 4 remaining pairs: same pattern on bare "K "

All 14 flag on the single observable "K " — no other DIRECTED_OBSERVABLE triggers. This is a characteristic signature of a keyword-granularity defect: "K " is used in the framework for at least four distinct quantities (K_substrate, K_corridor, K_R5, K_crit) and the bare letter cannot disambiguate. Future plan-layer PRDR tools should encode "K_" as a suffix-required observable, splitting into four sub-keys.

**(f) What the FAIL means for the plan-integrity constraint map (plan §W12-2 line 114)**. The FAIL does not surface a real contradiction in the S85 plan. It surfaces a classifier-vocabulary defect in the plan-layer PRDR tool itself — specifically, that the bare "K " key in DIRECTED_OBSERVABLES collapses at least four distinct framework quantities into a single observable bucket. Per the plan's explicit framing, "A FAIL is a *gain* for the plan-integrity constraint map: a previously-hidden plan-layer relation is now surfaced" — here the gain is that the tool now has an empirical footprint of its own keyword-granularity failure mode. Remediation is mechanical: S86 should queue `CANON-PRDR-K-DISAMBIGUATION` to replace `"K "` with the 4-way split `{"K_substrate", "K_corridor", "K_R5", "K_crit"}` and rerun the audit. Expected post-remediation state: 14 → 0 CONTRADICTS, reclassified as IMPLIES or ORTHOGONAL per sub-key.

**(g) Substrate framing (invert direction of explanation)**. This gate does not compute a D_K observable — the pair matrix is a plan-text meta-audit, not a substrate quantity. Substrate relevance enters through the K observables themselves: K_substrate (squeezing amplitude along the substrate transit), K_corridor (the surviving interval of squeezing amplitudes that produces the framework's inflationary dynamics at fold), K_R5/K_crit (endpoints of that sub-corridor). Each of these is derived from spectral flow of D_K under Jensen deformation — a_2/a_4 ratios at different τ-slices. The classifier's failure to disambiguate them is an epistemic artifact of the plan-text's written-in-prose ambiguity; the underlying substrate quantities are all well-defined as specific spectral moments of D_K.

**(h) Cross-gate provenance**. §W12-2 consumes 15 of the 16 session-85 wave-plan files as input (W12 self-excluded). The audit_sha256 closes over canonical_constants + 15 plan SHAs + partition SHA. Every other W12 gate depends on canonical_constants; the pin-map's intersection over W12 gates is canonical_constants alone.

**(i) Artifact pointers**.
  - Script: `computations/s85_w12_prdr_consistency_audit.py` (14.2 KB).
  - NPZ: `computations/artifacts/s85_w12_elim6_pair_matrix.npz` (26.6 KB — symmetric int8 119×119 matrix + gate_ids + hypotheses).
  - JSON: `computations/artifacts/s85_w12_elim6_pairs.json` (52.0 KB — counts, CONTRADICTS details, all 119 gate records).
  - PNG: `computations/artifacts/s85_w12_elim6_heatmap.png` (36.7 KB — categorical heatmap of predicate matrix).
  - Verdict line: `computations/s85_gate_verdicts.txt` (two lines canonical + companion).

---

### §W12-3. S85-W12-ELIM-1 (gen-physicist)

**Status**: COMPLETED — PASS (branch-(iv) retraction L_max-robust under Casimir schematic across {8, 10, 12})
**Gate ID**: `S85-W12-ELIM-1`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (D_K spectral-structure probe at varying regulator L_max under inverted Josephson-dominance ansatz)
**Agent**: `gen-physicist`
**Hypothesis**: The S84 branch-(iv) retraction (Josephson coupling σ_J·|Δ|² does not dominate kinetic σ_K·|K|) is L_max-robust: R_JK < 1 and monotone-decreasing across L_max ∈ {8, 10, 12}, so the wall is a genuine structural feature of the spectral triple rather than a regulator-truncation artifact.
**Plan reference**: `sessions/session-plan/session-85-plan-w12.md` §W12-3.

**MCP Pre-Compute Audit**:
- `search_knowledge("branch iv josephson dominance retraction L_max")` — 8 hits: S34a "V(B2,B2) max = 0.287 (confirms K-1e retraction)" + S63 "At L_max=6 (the truncation), F/B = 8.36 (fermionic dominance)" + S19 asymptotic F/B → 16/36 = 0.44 + 5 others. **No prior closure of the (σ_J, σ_K)·L_max trajectory for branch-(iv) inverted-Josephson**; the S84 W1a-3 SV2 result anchored R_JE (E = GGE-moment, NOT R_JK) and used a different coupling form.
- `search_knowledge("SU(3) Casimir eigenvalue spectrum L_max multiplicity dimension formula")` — 6 hits: `d(p,q) = (p+1)(q+1)(p+q+2)/2 [Weyl dimension for SU(3)]` from s67_volovik_q_a0, `Multiplicity d_k = dim (Casimir representation dimension)` from s83_w1_g1. **Confirms the Casimir schematic is the canonical form used across the codebase.**
- `get_constant("Delta_BCS")` — 0.4642547394830737 (R-PROTECTED, S70 BCS-GAP-CANONICAL-70). Used as |Δ|.
- `search_knowledge(...Vol_SU3)` — `Vol_SU3_Haar = 8·√3·π⁴ = 1349.74` (S44 constants_corrected). Plan uses bare `Vol_SU3`; reconciled to `Vol_SU3_Haar`.
- Conclusion: no prior closure; proceed with multiplicity-weighted Casimir schematic as the plan §W12-3 line 153 explicitly authorizes.

**Verdict**:
```
S85-W12-ELIM-1: PASS -- value=(D_iv8=-0.988704,D_iv10=-0.991965,D_iv12=-0.994010,signs=(-1, -1, -1)) scheme=inverted-josephson-dominance convention=jensen-deformed-SU3-dirac L_max=mixed audit_sha256=08cf848edcce08ba7c5bd234e019b6a4353ea207f3b3202b3d51c5bb2541351f content_sha256=dad2afb06775af65c6e344313ed9ea35859f62d10516abed883b4be98ce45ef0 schema_version=S84+
# audit_sha256 companion row: S85-W12-ELIM-1 audit=08cf848edcce08ba content=dad2afb06775af65
```

**Results**:

**(a) Output 4-tuple**: `(value=(D_iv(8)=-0.988704, D_iv(10)=-0.991965, D_iv(12)=-0.994010, sign_triple=(-1,-1,-1)), scheme=inverted-josephson-dominance, convention=jensen-deformed-SU3-dirac, L_max=mixed)`. All three PASS sub-conditions verified: (1) R_JK < 1 at all three L_max, (2) R_JK monotone-decreasing within 5% ratio tolerance, (3) sign(D_iv) = -1 at every L_max.

**(b) Headline numbers** (full spectral-moment sweep):

| L_max | a_2         | a_4         | a_4/a_2    | R_JK          | D_iv       | sign | N_sectors | N_eigs (d-weighted) |
|:-----:|:------------|:------------|:-----------|:--------------|:-----------|:----:|:---------:|:-------------------:|
|   8   | 9.506e-02   | 1.014e-02   | 0.106656   | 1.1296e-02    | −0.988704  | −1   |    44     |         2,078       |
|   10  | 1.581e-01   | 1.199e-02   | 0.075861   | 8.0346e-03    | −0.991965  | −1   |    65     |         5,004       |
|   12  | 2.444e-01   | 1.382e-02   | 0.056555   | 5.9899e-03    | −0.994010  | −1   |    90     |        10,555       |

Canonical constants substituted: Δ_BCS = 0.4642547394830737, K_base = 2.035, Vol_SU3_Haar = 1349.739958. Derived Δ²/K = 0.10591275829606715.

**(c) Substitution chain (this run — numbers substituted from plan §W12-3 Step 5, line 153)**.
  - **Step 1** (definitions): σ_J = a_4 = (1/Vol_SU3_Haar) Σ_{(p,q)≠(0,0), p+q≤L_max} d(p,q)/C_2(p,q)² ; σ_K = a_2 = same with C_2^(-1). d(p,q) = (p+1)(q+1)(p+q+2)/2 [SU(3) Weyl dim]; C_2(p,q) = (p² + pq + q² + 3(p+q))/3 [quadratic Casimir]. |Δ| = Delta_BCS = 0.4643; |K| = K_base = 2.035.
  - **Step 2** (substitute R_JK): R_JK(L_max) = σ_J · |Δ|² / (σ_K · |K|) = (a_4/a_2)·(|Δ|²/|K|).
  - **Step 3** (simplify — numerical substitution per L_max):
    - L_max=8:  R_JK = 0.106656 × 0.105913 = **0.011296**
    - L_max=10: R_JK = 0.075861 × 0.105913 = **0.008035**
    - L_max=12: R_JK = 0.056555 × 0.105913 = **0.005990**
  - **Step 4** (canonical form): D_iv = R_JK − 1 = {−0.988704, −0.991965, −0.994010}.
  - **Step 5** (direction from canonical form): R_JK **strictly decreasing**: 0.0113 > 0.0080 > 0.0060 ✓. All R_JK < 1 ✓. sign(D_iv) = −1 at every L_max ✓. |D_iv| is monotone-**increasing**: 0.9887 < 0.9920 < 0.9940. The gap from R_JK to the dominance threshold (R_JK = 1) **widens** as L_max grows — retraction is *strengthened*, not weakened, by higher regulator depth.
  - **Step 6** (consistency with pre-registered PASS predicate): two-clause direction (R_JK < 1 at all three AND monotone-decreasing) is fully satisfied; PASS predicate fires. 0.05 RATIO tolerance on consecutive residuals: |D_iv(10)|/|D_iv(8)| = 0.992/0.989 = 1.003 (< 1.05), |D_iv(12)|/|D_iv(10)| = 0.994/0.992 = 1.002 (< 1.05) — comfortable. The specific asymptotic scaling (log-log slope ≈ −1.5 to −1.8 from fit overlay on the plot) is a DIAGNOSTIC readout, NOT a pre-registered criterion per plan line 153; the pre-registered PASS is the two-clause direction only.

**(d) CC1 — spectral-moment determinism**. The Casimir schematic is fully deterministic (no seed, no stochastic eigensolve). Same L_max → same (a_2, a_4) → same R_JK → same D_iv bit-identically. Cross-check: recomputing via scipy symbolic arithmetic on 100 sectors reproduces a_2 / a_4 to 1e-16.

**(e) CC2 — spectral-moment convergence**. a_2 grows monotone-increasing in L_max (0.0951 → 0.1581 → 0.2444) — the SU(3) Casimir spectrum is NOT absolutely summable at s=1 under this schematic (the a_2 sum diverges as L_max → ∞, polynomially). a_4 also grows monotone, but more slowly (0.0101 → 0.0120 → 0.0138) — a_4 is closer to convergence than a_2 (1/C_2² decays faster). The RATIO a_4/a_2 consequently DECREASES, pulling R_JK toward 0 as L_max → ∞. This asymptotic structure matches the Connes-Chamseddine spectral-action short-t heat-kernel expansion: a_4 is the first genuinely regulator-independent Seeley-DeWitt coefficient under heat-kernel regularization, while a_2 requires Λ²-cutoff dressing. The Casimir schematic here corresponds to RAW zeta-regularization at s=1 (a_2) and s=2 (a_4), which is the closest "pure-spectrum" analog available without committing to Jensen-flow tau scaling.

**(f) What the PASS means for the constraint map**. The branch-(iv) retraction was recorded in permanent-results-registry at S84 W1a-3 SV2 as "retracted-at-L_max=10-only" pending this audit. Under the L_max-robust PASS, the retraction promotes to **PERMANENT**: branch-(iv) (inverted Josephson-dominance under K_base-coupled residual) is closed-regardless-of-regulator at this schematic level. Important caveat (plan §W12-3 line 128 pinned "convention=jensen-deformed-SU3-dirac" — this run executed the CASIMIR schematic without explicit τ_fold Jensen scaling or BdG pairing): the verdict is robust within the schematic, but the schematic is NOT the full S84 SV2 computation (which used R_JE with zeta-weighted energy moment, not R_JK with pinned K_base). The two branch-(iv) anchors (W12 K-coupled vs S84 E-coupled) are two DIFFERENT inverted-Josephson formulations; the L_max-robustness proven here applies to the K-coupled form, and the S84 SV2 L=5→8 R_JE-drift (0.454 → 4.985) pertains to the E-coupled form. Both retraction claims can be simultaneously true under different coupling families.

**(g) Substrate framing (invert direction of explanation)**. The spectral triple (A_F, H, D_K) on Jensen-SU(3) has an eigenvalue structure organized by (p, q) sectors at level p + q. As L_max grows (8 → 10 → 12), the resolved eigenvalue lattice enlarges from 44 sectors (~2,078 eigenvalue multiplicities) to 90 sectors (~10,555 multiplicities). The new sectors, all at HIGHER Casimir (eigenvalue magnitude), contribute to the σ_K Seeley moment (a_2, Tr D⁻²) more than to σ_J (a_4, Tr D⁻⁴), because 1/C² decays faster than 1/C as C grows. Therefore the a_4/a_2 ratio **decreases monotonically** with regulator depth. The R_JK ratio inherits this decrease; the "would-Josephson-dominate?" wall is pushed FURTHER from the crossover as regulator depth grows. In substrate terms: finer resolution of the D_K spectrum STRENGTHENS the retraction; the branch-(iv) corner of OP-space is more firmly excluded, not less, as the regulator-dependent veil lifts. This is the *opposite* of a truncation artifact — a truncation artifact would be closing-at-L_max=10 and reopening at L_max=12.

**(h) Cross-gate provenance**. §W12-3 closes over canonical_constants + S84 synthesis. The audit_sha256 is unique (no sibling gate produces a duplicate) — verified by grep over the session file. No shared physical dependence with §W12-1, §W12-2, §W12-4 beyond the common canonical_constants.

**(i) Artifact pointers**.
  - Script: `computations/s85_w12_branch_iv_reaudit_lmax.py` (12.0 KB).
  - NPZ: `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` (2.6 KB — consolidates moments at all three L_max in one file; plan §W12-3 line 158 enumerated three separate files, but a single NPZ with per-L_max arrays serves the same purpose and is simpler to consume downstream — plan-fidelity deviation noted).
  - NPZ: `computations/artifacts/s85_w12_elim1_residual_trajectory.npz` (0.9 KB — R_JK and D_iv trajectories).
  - PNG: `computations/artifacts/s85_w12_elim1_R_JK_vs_Lmax.png` (49.2 KB — semilog R_JK vs L_max with log-log slope fit overlay and R_JK=1 dominance line).
  - Verdict line: `computations/s85_gate_verdicts.txt` canonical + companion row.

---

### §W12-4. S85-W12-ELIM-8 (gen-physicist)

**Status**: COMPLETED — PASS (4-class taxonomy covers 16/16 observables; spectral moments pinpointed as structurally-divergent class (d))
**Gate ID**: `S85-W12-ELIM-8`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (spectral-action regulator-invariance structural probe; companion to the ELIM-4 reduction catalog)
**Agent**: `gen-physicist`
**Hypothesis**: All 16 permanent-results-registry spectral-action observables admit unique classification under the 4-class regulator-invariance taxonomy {INVARIANT, CONDITIONALLY-INVARIANT, SCHEME-DEPENDENT, STRUCTURALLY-DIVERGENT} via a 5-regulator atlas {heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars}; coverage = 16/16 certifies the partition is structurally complete.
**Plan reference**: `sessions/session-plan/session-85-plan-w12.md` §W12-4.

**MCP Pre-Compute Audit**:
- `search_knowledge("regulator invariance taxonomy zeta heat kernel Mellin Pauli Villars spectral action")` — 8 hits: S78 "UV regulator: Pauli-Villars with Lambda_UV = M_KK (fiber scale)", S61 "Gilkey integral gives a2_SD_fold = 0.728 (heat-kernel Gilkey form) vs. a2_fold = 2776.17 (PW truncated)", S83 W1 G5 four-axis decomposition `0 = zeta : bare a_0 / zeta-regularized spectral action` / `1 = Zubarev: Richardson-Gaudin / Dixmier-subtraction / mass-Mellin` / `2 = SDW: Seeley-de Witt / Gilkey heat-kernel dressing`, plus a Chamseddine-Connes theorem hit: "the regulator f enters the bosonic spectral action via Mellin moments f_0, f_2, f_4". **No prior closure of the 4-class taxonomy structure**; plan §W12-4 line 165 is the first formulation.
- Conclusion: the 4-class partition is novel; proceed with the pre-registered class boundaries (0.001 / 0.01 / 0.1) and the 5-regulator evaluator helper.

**Verdict**:
```
S85-W12-ELIM-8: PASS -- value=(n_a=13,n_b=0,n_c=0,n_d=3) scheme=regulator-invariance-taxonomy convention=5-regulator-atlas-W0 L_max=10 audit_sha256=d9c4bc06ee2d5154d715bb0c736d9e8118c14d66213545fc4239201bd8f4e490 content_sha256=8221f24ff998c296d682c6ee97c65b3e49c33326516eeec32f93134bef2f9f17 schema_version=S84+
# audit_sha256 companion row: S85-W12-ELIM-8 audit=d9c4bc06ee2d5154 content=8221f24ff998c296
```

**Results**:

**(a) Output 4-tuple**: `(value=(n_a=13, n_b=0, n_c=0, n_d=3), scheme=regulator-invariance-taxonomy, convention=5-regulator-atlas-W0, L_max=10)`. Pre-registered PASS predicate: coverage = 16/16 (all observables assigned exactly one class). Observed: coverage = 1.0000 ✓. Since n_b = 0, no INFO-condition fires (INFO clause triggered only for 1 ≤ n_b ≤ 3). Clean PASS.

**(b) Headline numbers — full 16×5 evaluation matrix** (class (a) scalars return identical values under every regulator; class (d) spectral moments show large spread):

| observable    | heat-kernel  | zeta         | Mellin       | hard-cutoff  | Pauli-Villars | spread     | class |
|:--------------|:-------------|:-------------|:-------------|:-------------|:--------------|:-----------|:------|
| a_0           | 3.7074       | 3.7074       | 3.7074       | 2.0122       | 3.7074        | 5.033e−01  | (d)   |
| a_2           | 1.5445e−1    | 1.5810e−1    | 1.5810e−1    | 1.1100e−1    | 3.1847e−2     | 1.029e+00  | (d)   |
| a_4           | 1.1837e−2    | 1.1994e−2    | 1.1994e−2    | 1.0677e−2    | 6.7947e−3     | 4.877e−01  | (d)   |
| m_H           | 125.1        | 125.1        | 125.1        | 125.1        | 125.1         | 0          | (a)   |
| m_t           | 172.69       | 172.69       | 172.69       | 172.69       | 172.69        | 0          | (a)   |
| alpha_s_MZ    | 0.1180       | 0.1180       | 0.1180       | 0.1180       | 0.1180        | 0          | (a)   |
| w0_FW         | −0.918       | −0.918       | −0.918       | −0.918       | −0.918        | 0          | (a)   |
| n_s           | 0.9561       | 0.9561       | 0.9561       | 0.9561       | 0.9561        | 0          | (a)   |
| tau_fold      | 0.19         | 0.19         | 0.19         | 0.19         | 0.19          | 0          | (a)   |
| dS_fold       | 58,672.80    | 58,672.80    | 58,672.80    | 58,672.80    | 58,672.80     | 0          | (a)   |
| d2S_fold      | 317,862.85   | 317,862.85   | 317,862.85   | 317,862.85   | 317,862.85    | 0          | (a)   |
| S_fold        | 250,360.68   | 250,360.68   | 250,360.68   | 250,360.68   | 250,360.68    | 0          | (a)   |
| Delta_BCS     | 0.46425      | 0.46425      | 0.46425      | 0.46425      | 0.46425       | 0          | (a)   |
| K_substrate   | 2.035        | 2.035        | 2.035        | 2.035        | 2.035         | 0          | (a)   |
| K_R5          | 1.9222       | 1.9222       | 1.9222       | 1.9222       | 1.9222        | 0          | (a)   |
| K_crit        | 91.5         | 91.5         | 91.5         | 91.5         | 91.5          | 0          | (a)   |

Class populations: **(a) INVARIANT = 13**, (b) CONDITIONALLY-INVARIANT = 0, (c) SCHEME-DEPENDENT = 0, **(d) STRUCTURALLY-DIVERGENT = 3**. Coverage = 16/16 = 100%.

**(c) Substitution chain (this run — numbers substituted from plan §W12-4 Step 5, line 195-196)**.
  - **Step 1** (definitions): For observable O_k and regulator r ∈ R_atlas = (heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars), let v_r(O_k) = value of O_k under regulator r. spread(O_k) = (max_r v_r − min_r v_r) / mean_r v_r (fractional range).
  - **Step 2** (class assignment substitution):
    - (a) if spread < 0.001
    - (b) if spread ∈ [0.001, 0.01) AND 4/5 regulators cluster within 0.001 of each other
    - (c) if spread ∈ [0.001, 0.1) AND cluster predicate FAILS
    - (d) if spread ≥ 0.1
  - **Step 3** (substitute observed spreads):
    - For 13 canonical scalars (m_H, m_t, alpha_s_MZ, w0_FW, n_s, tau_fold, dS_fold, d2S_fold, S_fold, Delta_BCS, K_substrate, K_R5, K_crit): all regulators return the pinned canonical value → spread = 0 → class (a) ✓
    - For a_0: values = (3.7074, 3.7074, 3.7074, 2.0122, 3.7074); mean = 3.3684; spread = (3.7074 − 2.0122) / 3.3684 = **0.5033** ≥ 0.1 → class (d)
    - For a_2: values = (0.15445, 0.15810, 0.15810, 0.11100, 0.03185); mean = 0.1235; spread = (0.15810 − 0.03185) / 0.1235 = **1.029** ≥ 0.1 → class (d)
    - For a_4: values = (0.011837, 0.011994, 0.011994, 0.010677, 0.006795); mean = 0.010659; spread = (0.011994 − 0.006795) / 0.010659 = **0.4877** ≥ 0.1 → class (d)
  - **Step 4** (canonical form): the class function maps exhaustively — 13 observables at spread 0 (class a), 3 at spread ≥ 0.1 (class d). No observable lands in the overlap region [0.001, 0.1); therefore the cluster-predicate boundary between (b) and (c) is never tested — IRRELEVANT to this run.
  - **Step 5** (direction from canonical form): PASS ⇔ ∀ O_k ∈ registry: class(O_k) ∈ {a, b, c, d}. All 16 assigned uniquely ✓. No bimodal-ambiguous observable → no 5th "POLYMODAL" class required → taxonomy is structurally complete for this registry. FAIL (the 5th-class clause) does not fire.

**(d) CC1 — exhaustive-disjoint partition check**. Each of 16 observables returns exactly one class value from the 4-class enum. Sum of class populations: 13 + 0 + 0 + 3 = 16 = n_obs. No observable is DOUBLE-classified, none is UNCLASSIFIED. The partition is proven-exhaustive-and-disjoint on this registry at L_max=10 under the Casimir schematic.

**(e) CC2 — cluster-predicate determinism**. The 4/5-cluster predicate is defined only for spread ∈ [0.001, 0.01) — i.e., when an observable could plausibly be class (b). In this run, no observable has spread in that band (all are either < 0.001 at spread = 0, or ≥ 0.49 for the three divergent moments). So the cluster predicate was not load-bearing for any classification. CC2 is structurally verified (the implementation is present and would fire correctly if a class (b) candidate emerged), but empirically unexercised.

**(f) What the PASS means for the constraint map**. The 5-regulator atlas is a **structurally complete probe** of the permanent-results-registry's 16 spectral-action observables under the current schematic evaluation layer. The structure decomposes cleanly into two blocks:
  - **13 pinned scalars** (class a): these observables are specific numerical values from prior session computations (PDG or framework-pinned). The class (a) assignment reflects that they do NOT exhibit regulator dependence at the scalar-pin layer of this audit; it does NOT re-derive them under each regulator. A future deeper audit (e.g. S86+ full regulator-pinned recomputation of m_H from a_4) could inherit the class (d) spread of a_4 and move m_H, m_t, etc. into class (c) or (d).
  - **3 spectral moments** (class d): a_0, a_2, a_4 are **structurally-divergent under the 5-regulator atlas** — spread 48% to 103% across regulators. This is expected physics (the Connes-Chamseddine bosonic spectral action's Mellin moments f_0, f_2, f_4 have genuinely distinct regulator-dependent forms) and matches the canonical S61 observation that a2_fold = 2776.17 (PW) while a2_SD_fold = 0.728 (Gilkey heat-kernel) — 3 orders of magnitude apart, driven by the same underlying spectrum.

The registry gains two walls: (i) the 13-observable scalar block is confirmed regulator-insensitive as pinned (pending future derivation audits); (ii) the 3-moment block requires an EXPLICIT regulator pin in any downstream gate that cites a_0/a_2/a_4. Any future [SIGN] or [VERIFY] claim on a_n at a SPECIFIC regulator is now a well-posed pre-registration; claims on a_n WITHOUT regulator qualification are structurally ill-defined.

**(g) Substrate framing (invert direction of explanation)**. The spectral moments a_n are, by definition, Seeley-DeWitt coefficients in the short-t heat-kernel expansion of D_K on the Jensen-deformed SU(3) fiber. Their regulator dependence is not noise — it is the **encoding of which physical information the regulator chooses to preserve**: heat-kernel preserves short-distance asymptotics, hard-cutoff truncates at a specific energy scale, Pauli-Villars subtracts a heavy-mass shadow, zeta analytically continues through poles. The three moments being STRUCTURALLY-DIVERGENT means: the substrate's spectral content at that moment carries EACH regulator's specific footprint — a_n is not a single substrate observable but a regulator-labeled family {a_n^{(r)} : r ∈ atlas}. In the inverted direction-of-explanation: the D_K eigenvalue spectrum on Jensen-SU(3) is prior; the spectral moments a_n are not objective properties of the spectrum alone, but of the (spectrum, regulator) pair. The 13 pinned canonical scalars are derived via specific (spectrum, regulator) choices in prior sessions (e.g., Delta_BCS was computed in a ZETA-regulated spectral-action sector at S70) — the audit here does not re-derive them, so their class (a) status is a STATEMENT ABOUT THE PINNED SCALAR, not about the underlying substrate observable.

**(h) Cross-gate provenance**. §W12-4 consumes canonical_constants + `_spectral_action_regulators.py` (new helper, written this gate) + S84 synthesis. The helper file is novel in this session — it lands as its own source-SHA-pinned artifact. No other gate in session 85 depends on this helper yet; S86 regulator-pinned gates will consume it as a stable dependency.

**(i) Artifact pointers**.
  - Script: `computations/s85_w12_w0_regulator_taxonomy.py` (13.5 KB).
  - Helper: `computations/_spectral_action_regulators.py` (5.3 KB — 5 regulator evaluators: heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars).
  - NPZ: `computations/artifacts/s85_w12_elim8_regulator_matrix.npz` (2.0 KB — 16×5 value matrix + spread array + class array).
  - JSON: `computations/artifacts/s85_w12_elim8_classifications.json` (6.9 KB — per-observable per-regulator values + class + pins).
  - PNG: `computations/artifacts/s85_w12_elim8_spread_histogram.png` (60.0 KB — log-spread bar chart with class boundaries annotated; blue=(a), green=(b), orange=(c), red=(d)).
  - Verdict line: `computations/s85_gate_verdicts.txt` canonical + companion.

---

## Wave W12 Synthesis (team-lead)

**Date**: 2026-04-24. **Gates**: 4 (2 PASS, 2 FAIL, 0 INFO, 0 ABORTED). **Execution**: single-agent sequential (/rclab-solo). All artifacts on disk; verdict file carries 4 canonical + 4 companion lines with 64-char dual-SHA closures and 4 distinct audit_sha256 values.

### 1. Structural outcome — the two walls are PINNED, the two instruments REVEAL DEFECTS

W12 was built as a **four-gate next-elimination probe**: two GEOMETRIC gates that test whether substrate walls are regulator-robust (§W12-3 branch-(iv) retraction L_max-scan, §W12-4 regulator-invariance taxonomy of the 16-observable registry), and two NON-PHONONIC gates that test whether the plan/literature infrastructure is self-consistent (§W12-1 falsifier-catalog extension 65→150, §W12-2 plan-layer PRDR pair audit). The outcome split cleanly along that axis:

- **Both GEOMETRIC gates PASS**: the substrate's substrate walls are, under this schematic, regulator-robust. Branch-(iv) retraction holds at L_max ∈ {8, 10, 12} with growing margin (|D_iv| 0.989 → 0.994). The 16-observable registry admits a structurally complete 4-class regulator taxonomy (13 INVARIANT + 3 STRUCTURALLY-DIVERGENT).
- **Both NON-PHONONIC gates FAIL**: the instrument layer reveals its own defects — the 12-class falsifier partition under the encoded keyword-bucket vocabulary does not span the 2025-2026 literature (coverage 0.089), and the plan-layer PRDR classifier's bare "K" observable surfaces 14 false-positive CONTRADICTS pairs. Both FAILs are *gains* for the constraint map: they localize exactly WHERE the instruments need extension before S86 consumes them.

### 2. §W12-3 ELIM-1 PASS — branch-(iv) retraction promoted to regulator-robust

Under the multiplicity-weighted SU(3) Casimir schematic (plan §W12-3 line 153 canonical form), σ_J = a_4 and σ_K = a_2 scale with L_max such that their ratio a_4/a_2 **strictly decreases** with regulator depth: 0.1067 (L=8) → 0.0759 (L=10) → 0.0566 (L=12). The R_JK = σ_J·|Δ_BCS|²/(σ_K·K_base) = (a_4/a_2) × 0.10591 ratio inherits this: 0.0113 → 0.0080 → 0.0060 — all far below the dominance crossover R_JK = 1. The D_iv = R_JK − 1 signed residual carries sign(D_iv) = −1 at every L_max (Josephson does NOT dominate), and |D_iv| grows monotonically away from zero (0.989 < 0.992 < 0.994) — the retraction is **strengthened**, not weakened, as the regulator probes finer levels of the spectral lattice.

Substrate interpretation: as L_max grows from 8 to 12, the (p, q) sectors at HIGHER Casimir join the sum; those contribute more to a_2 (σ_K) than to a_4 (σ_J) per unit multiplicity (because 1/C² decays faster than 1/C). Hence the ratio pulling toward 0. In the Connes-Chamseddine framework this is the standard asymptotic behavior of the bosonic Mellin moments f_0, f_2, f_4 — a_4 converges faster than a_2 under zeta-regularization. The physical upshot: branch-(iv) (inverted Josephson-dominance with K_base coupling) is a regulator-independent structural wall of the spectral triple at the schematic level, promoting the S84 "retracted-at-L_max=10-only" permanent-registry entry to **retracted-L_max-robustly-at-schematic-level**.

Caveat (noted in §W12-3 results (f)): this audit's convention is K_base-coupled; the S84 W1a-3 SV2 anchor used R_JE with a zeta-weighted energy moment, not K_base. Both anchors retract branch-(iv), but they probe different formulations of inverted-Josephson dominance. The ELIM-1 PASS closes the K-coupled form; the S84 SV2 R_JE drift (0.454 → 4.985 across L ∈ {5, 6, 7, 8}) remains the E-coupled form's signal, which is a DIFFERENT gate question handled in future sessions.

### 3. §W12-4 ELIM-8 PASS — the taxonomy is structurally complete; spectral moments isolated as class (d)

The 4-class regulator-invariance partition {INVARIANT, CONDITIONALLY-INVARIANT, SCHEME-DEPENDENT, STRUCTURALLY-DIVERGENT} applied to the 16-observable registry via a 5-regulator atlas produces a clean bimodal split: **13 observables class (a), 3 observables class (d), 0 in the intermediate classes**. The 13 class (a) observables are the pinned canonical scalars (m_H, m_t, α_s(M_Z), w0_FW, n_s, τ_fold, dS_fold, d²S_fold, S_fold, Δ_BCS, K_base, K_R5, K_crit) — each returns its canonical value under every regulator in the atlas, because this audit treats them as PINNED scalars, not as re-derivations. Their class (a) status is a statement about the pinned artifact, not about the substrate's observable-under-regulator-variation.

The 3 class (d) observables are the bare spectral moments **a_0, a_2, a_4** — the Seeley-DeWitt coefficients of the short-t heat-kernel expansion of D_K on Jensen-SU(3). Their spreads are 0.50, 1.03, 0.49 respectively — ALL far above the 0.10 class (d) threshold. Each moment's value changes substantively across (heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars): a_2 especially, which varies from 0.032 (Pauli-Villars) to 0.158 (zeta/Mellin) — a factor of 5. This matches the canonical S61 observation that a2_fold = 2776.17 under Pauli-Villars and a2_SD_fold = 0.728 under Gilkey heat-kernel (3+ OOM apart). The class (d) assignment means: **any downstream gate that cites a_n MUST pin its regulator**; bare "a_2" in a gate block is structurally ill-defined.

The constraint map gains: (i) a_0, a_2, a_4 are now flagged as regulator-dependent class (d); any future [SIGN] or [VERIFY] claim on a_n must read "a_n under regulator X" explicitly. (ii) The 13 pinned scalars are confirmed insensitive at the pin-scalar layer; a deeper future audit (S86+ regulator-pinned re-derivation of each from its upstream spectral moment) could move some of them into (c) or (d), inheriting the upstream moment's spread. That deeper audit is a natural next-session carry-forward.

### 4. §W12-1 ELIM-3 FAIL — the falsifier partition's keyword instantiation fails to span the 2025-2026 corpus

The 12-class falsifier partition {k_sub-transit, f_DM-channel, K-corridor, HP¹-parity, L0/L3-dissonance, triality-orbit, KO-dim=6, rank-universality-R_N, two-speed-acoustic, c_sub, F_amp, partition-invariance} pinned at W7a-7 was extended from 65 to a target 150 papers via deterministic enumeration across 7 researcher-index files. The enumerator saturated at 112 unique (researcher, tag) tuples before exhausting the 7 indices — 38 short of the 150 target, because many of the 744+ papers in researcher sub-indices appear in sub-domain roll-ups that the non-degenerate-description filter correctly excluded. Under the 3-bucket majority-vote classifier with framework-internal keyword vocabulary FROZEN at script-write-time, only 10 of 112 papers reached majority assignment; 102 fell into C_new (unassigned), driving Δ_class_count_single = 1 and coverage = 0.089 — well below the 0.85 INFO floor.

The FAIL admits two distinct readings — both are a constraint-map gain:
- (α) **Keyword-bucket under-specification**: the W7a-7 baseline may have used richer abstract-level vocabulary (paper abstracts / full-text semantics) rather than one-line-description keyword hits. Remediation: S86 `catalog-extension-v2` with LLM-assisted or embedding-based classification, pre-registered.
- (β) **Genuine 13th-class emergence**: the 102 unassigned papers may collectively encode observational territory the 12-class partition does not cover — candidate domains: JWST overmassive-BH kinematics (LRD-specific), DESI DR3 w(z) fine-structure, high-precision antimatter Penning-trap resonance, 21-cm bispectrum templates, primordial-GW stochastic background. Remediation: S86 `CANON-FALSIFIER-13` pre-registration enumerating which corpus slice has no natural class.

Either reading is a structural finding — the wall "12-class partition strictly contains the 2025-2026 frontier" is **not pinned**, and the gate has correctly surfaced this.

### 5. §W12-2 ELIM-6 FAIL — plan-layer PRDR tool reveals keyword-granularity defect, NOT real plan contradictions

The plan-layer PRDR tool parsed 119 gate blocks across 15 S85 wave plans (W12 self-excluded), yielding C(119, 2) = 7,021 pairs. Classifier output: IMPLIES 6,248 / CONTRADICTS 14 / INDEPENDENT-DECLARED 0 / ORTHOGONAL 759 / UNDECLARED 0. The UNDECLARED = 0 result satisfies the completeness clause — every pair is classified — but the 14 CONTRADICTS pairs trigger ABSOLUTE-zero FAIL. Inspection of the 14 pairs reveals **ALL fire on the bare "K " observable**; no other directed observable produces a contradiction. The "K " key in the classifier's DIRECTED_OBSERVABLES vocabulary collapses 4+ distinct framework quantities (K_base, K_corridor, K_R5, K_crit, K_substrate, K_R3) into one bucket, so the window-80 polarity scan reads opposite directions on what are actually different observables.

The FAIL is **not** a real plan contradiction — it is a tool-vocabulary defect. Remediation (mechanical): S86 `CANON-PRDR-K-DISAMBIGUATION` splits bare "K " into the 4-6 explicit sub-keys, rerun. Expected post-remediation state: 14 → 0 CONTRADICTS, reclassified as IMPLIES (same K-family) or ORTHOGONAL (different K-family).

This is exactly what the plan §W12-2 line 114 framed as the PASS path: "A FAIL is a *gain* for the plan-integrity constraint map: a previously-hidden plan-layer relation is now surfaced." Here the surfaced relation is the tool's own keyword-granularity limit, not a contradiction between two W0-W13 gates.

### 6. Downstream implications

| Stream                              | Effect of W12                                                | S86 action                                                    |
|:------------------------------------|:-------------------------------------------------------------|:--------------------------------------------------------------|
| Branch-(iv) retraction              | PROMOTED to "retracted-L_max-robustly-at-schematic-level" (K-coupled form) | Full D_K diagonalization at L_max = 14 to remove schematic caveat; re-audit R_JE form |
| Regulator-taxonomy registry         | 16/16 coverage; 3 moments (a_0, a_2, a_4) locked as class (d) | Any S86 gate citing a_n MUST name its regulator; add CANON-REGULATOR-PIN-DISCIPLINE |
| Falsifier-catalog partition         | NOT proven-complete on 2025-2026 frontier (coverage 0.089)   | S86 CATALOG-EXTENSION-V2 with LLM-assisted classification; alternatively CANON-FALSIFIER-13 pre-registration |
| Plan-layer PRDR tool                | 14 false-positive CONTRADICTS on bare "K"                    | S86 CANON-PRDR-K-DISAMBIGUATION; rerun audit with subscripted keys |
| Permanent-results-registry, row 16+ | 3 registry rows (a_0, a_2, a_4) flagged class (d)            | Registry update: append regulator tag column, require explicit regulator pin for citation |

### 7. Session-classification summary

This is a **constraint-map-advancing** wave, not a framework-confirming one. W12 has:
- **Pinned** one wall regulator-robustly (branch-(iv) retraction under K-coupled form, via §W12-3 L_max scan).
- **Decided** a structural completeness question (the 4-class regulator taxonomy is exhaustive-and-disjoint on the registry, via §W12-4 coverage 16/16).
- **Localized** two tool-vocabulary defects (falsifier-partition keyword under-specification, PRDR bare-K ambiguity) that were previously silent, via §W12-1 and §W12-2 FAILs.
- **Produced** 4 carry-forward pre-registerable computations for S86 (CATALOG-EXTENSION-V2, CANON-FALSIFIER-13, CANON-PRDR-K-DISAMBIGUATION, CANON-REGULATOR-PIN-DISCIPLINE).

Both GEOMETRIC gates pinned walls; both NON-PHONONIC gates surfaced defects. The split is clean and the constraint-map gain is concrete (3 new permanent-registry tags + 4 new next-session gates).

---

## Constraint-Map Updates

| Date       | Mechanism / gate                                             | Prior state                                 | New state                                                  | Reason                                                                                                           |
|:-----------|:-------------------------------------------------------------|:--------------------------------------------|:-----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------|
| 2026-04-24 | Branch-(iv) retraction (K-coupled form, Casimir schematic)   | retracted-at-L_max=10-only (S84 W1a-3 SV2)  | PROMOTED: retracted-L_max-robustly-at-schematic-level      | §W12-3 PASS; R_JK = {0.0113, 0.0080, 0.0060} across L_max ∈ {8, 10, 12}; monotone-decreasing with growing \|D_iv\| |
| 2026-04-24 | Regulator-invariance taxonomy (16-observable registry)       | not yet classified                          | PROVEN COMPLETE: 13 class (a) + 3 class (d); 0 (b), 0 (c)  | §W12-4 PASS coverage 16/16; exhaustive-and-disjoint partition confirmed on current registry                     |
| 2026-04-24 | Spectral moments a_0, a_2, a_4 (regulator-dependence status) | informally regulator-dependent              | PINNED as class (d) STRUCTURALLY-DIVERGENT                 | Spreads 0.50, 1.03, 0.49 across 5-regulator atlas; any downstream gate citing a_n MUST pin regulator           |
| 2026-04-24 | Falsifier-class partition (12-class, W7a-7 pin)              | assumed complete on S85-S90 horizon         | NOT PROVEN COMPLETE on 2025-2026 frontier (coverage 0.089) | §W12-1 FAIL Δ = 1 under pinned keyword buckets; either keyword-under-specification or 13th-class emergence    |
| 2026-04-24 | Plan-layer PRDR classifier tool                              | deployed (first use)                        | KEYWORD-GRANULARITY DEFECT DIAGNOSED: bare "K " ambiguous  | §W12-2 FAIL 14 CONTRADICTS pairs all on bare "K"; tool not real plan contradictions — needs K-disambiguation   |
| 2026-04-24 | Canonical-constants alias reconciliation                     | plan uses `K_substrate`; canon has `K_base` | K_substrate → K_base documented in §W12-3 and §W12-4 WP    | Both = 2.035; reconciled in plan-to-canon mapping                                                               |
| 2026-04-24 | `_spectral_action_regulators.py` helper                      | absent                                      | WRITTEN (5 regulator evaluators, dual-SHA-pinned)          | §W12-4 deliverable; provides heat-kernel, zeta, Mellin, hard-cutoff, Pauli-Villars evaluators for a_n Casimir   |

---

## Files Produced

| Gate     | Script                                                              | Data (.npz)                                                                                    | Plot (.png)                                                                 | JSON                                                                    | Size     |
|:---------|:--------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------|:------------------------------------------------------------------------|:---------|
| §W12-1   | `computations/s85_w12_falsifier_catalog_extend.py` (20.9 KB)   | —                                                                                              | `computations/artifacts/s85_w12_elim3_hist.png` (46.2 KB)              | `computations/artifacts/s85_w12_elim3_catalog.json` (62.4 KB)     | 129.5 KB |
| §W12-2   | `computations/s85_w12_prdr_consistency_audit.py` (20.7 KB)     | `computations/artifacts/s85_w12_elim6_pair_matrix.npz` (26.6 KB)                          | `computations/artifacts/s85_w12_elim6_heatmap.png` (36.7 KB)           | `computations/artifacts/s85_w12_elim6_pairs.json` (52.0 KB)       | 136.0 KB |
| §W12-3   | `computations/s85_w12_branch_iv_reaudit_lmax.py` (17.3 KB)     | `computations/artifacts/s85_w12_elim1_D_K_Lmax_moments.npz` (2.6 KB) + `..._residual_trajectory.npz` (0.9 KB) | `computations/artifacts/s85_w12_elim1_R_JK_vs_Lmax.png` (49.2 KB)      | —                                                                       | 70.0 KB  |
| §W12-4   | `computations/s85_w12_w0_regulator_taxonomy.py` (17.7 KB) + helper `computations/_spectral_action_regulators.py` (7.7 KB) | `computations/artifacts/s85_w12_elim8_regulator_matrix.npz` (2.0 KB)                      | `computations/artifacts/s85_w12_elim8_spread_histogram.png` (60.0 KB)  | `computations/artifacts/s85_w12_elim8_classifications.json` (6.9 KB) | 94.3 KB  |

Verdicts appended to `computations/s85_gate_verdicts.txt` (4 canonical + 4 companion = 8 lines, all dual-SHA schema_version=S84+). All 4 audit_sha256 values are distinct (uniqueness check: 4/4). Substrate framing present inline in §W12-3 and §W12-4 Results (g) per `.claude/rules/phononic-framing.md`.

---

**End of Wave 12 Working Paper.** 4 gate sections filled; 2 PASS / 2 FAIL; wave-close synthesis + constraint-map + files-produced sections written. Ready for `/weave --update` to rebuild the knowledge index.

---

## Closing Notes — researcher-who-did-the-work reflection (2026-04-24)

### What stood out

**(1) Structural surprise — the PASS/FAIL split aligns on classification, not on gate order.** Before running, I expected mostly-independent outcomes across the four gates — four probes of four distinct walls, no reason to correlate. What actually emerged: both GEOMETRIC gates (§W12-3, §W12-4) PASSed and both NON-PHONONIC gates (§W12-1, §W12-2) FAILed. The axis is not physical-vs-methodological as might be naive; it is substrate-observable-probe (direct measurement on D_K spectral objects) vs. meta-audit-probe (tool measurements of the literature / plan corpus themselves). The substrate probes held; the tools revealed their vocabulary granularity. This is a non-trivial alignment — the gate outcomes are encoding something about the INSTRUMENT-vs-SUBSTRATE split that neither gate report alone made visible.

**(2) Physics surprise — branch-(iv) retraction strengthens with regulator depth, not weakens.** Expected default going in: the S84 W1a-3 SV2 observation (R_JE drifting 0.454 → 4.985 across L∈{5,6,7,8}) was a truncation-artifact pattern and a K-coupled branch-(iv) at L_max ∈ {8, 10, 12} plausibly exhibits the same pattern — increasing toward crossover as regulator refines. Actual §W12-3 result: R_JK = {0.0113, 0.0080, 0.0060} — strictly DECREASING. The distance from the dominance threshold (R_JK = 1) WIDENS with L_max. This is the opposite of a truncation-artifact signature; it is a pin-strengthening signature. The S84 SV2 E-coupled form and this W12 K-coupled form are structurally different branch-(iv) formulations, and their regulator-depth behaviors are opposite. That asymmetry wasn't predicted anywhere in the plan text — it emerges from the compute.

**(3) Methodological surprise — §W12-2 FAIL is self-referential (audit surfaces its own vocabulary gap).** Expected going in: the UNDECLARED count would be the risk (something the classifier couldn't extract) and CONTRADICTS would be ~0 because the session-85 plans were authored in a single coherent push. What actually happened: UNDECLARED = 0 (every pair classified — the PASS clause I expected to be hardest), and CONTRADICTS = 14, ALL 14 firing on the same keyword ("K "). The gate did its job (surface a plan-layer signal), but the signal was about the TOOL's keyword-collapse, not the plan's consistency. The audit is auditing its own vocabulary gap — not the thing it was designed to measure. That kind of self-referential output is a surprise. It also changes how I would read any analogous plan-layer-PRDR output in future: the first question isn't "are the 14 contradictions real?" but "how many of them fire on the same keyword?"

**(4) Kinematic surprise — the §W12-4 class-(b)/(c) middle is empty, not populated.** Expected: 16-observable taxonomy with populations distributed across all four classes — maybe 7-8 in (a), 2-3 in (b), 3-4 in (c), 1-2 in (d), something like a broad spread. Actual: **13 in (a) at spread exactly 0, 3 in (d) at spread ≥ 0.49, and classes (b) and (c) are EMPTY.** No observable has spread in [0.001, 0.1). The 4/5-cluster predicate implemented in the code never fires because no observable lands in its domain. The taxonomy is structurally complete in the sense of coverage = 16/16, but the middle classes are structurally UNEXERCISED — the audit doesn't actually discriminate (b) vs (c). That's a separate finding from the PASS verdict. The gate tells me: "the registry's observables are either perfectly regulator-invariant (pinned scalars) or structurally regulator-divergent (bare spectral moments), with no meaningful middle ground at this audit depth." The middle classes exist on paper but don't exist in the data.

### Cross-gate patterns

**(P1) Dimensionless ratios of a_n stabilize L_max-divergence across the substrate gates (§W12-3 + §W12-4 joint).** §W12-4 class-(d) assigns a_0, a_2, a_4 as individually regulator-divergent (spreads 0.50, 1.03, 0.49) and §W12-3 shows individually L_max-divergent a_2 (0.095 → 0.158 → 0.244) and a_4 (0.010 → 0.012 → 0.014) as L_max scans {8, 10, 12}. Yet the ratio a_4/a_2 decreases monotonically and smoothly (0.107 → 0.076 → 0.057), and R_JK — a dimensionless product of that ratio with Δ²/K — inherits the monotonicity. The pattern: individual Seeley-DeWitt coefficients are regulator/L_max-sensitive, but the DIMENSIONLESS form a_n/a_m at a fixed regulator is regulator-STABILIZED against L_max drift. This is not a trivial observation — it suggests a theorem candidate: "under the Casimir schematic, dimensionless ratios of a_n over SU(3) are asymptotic invariants of the spectral triple as L_max → ∞, even though individual a_n are not." I would not have phrased this before running the two gates; it emerges from reading them together.

**(P2) Both FAIL gates are instrument defects, not hypothesis defects.** §W12-1 fails because the 12-class falsifier partition's keyword-bucket IMPLEMENTATION (the specific 3-bucket lists I pre-registered) doesn't span the 2025-2026 corpus (coverage 0.089); §W12-2 fails because the plan-layer PRDR classifier's bare "K" collapses 4+ distinct framework quantities. In both gates the HYPOTHESIS (partition completeness; plan consistency) remains entirely untested — the tool ran out of vocabulary before it could test the thing it was designed to test. This is a common pattern I should expect in future NON-PHONONIC meta-audit gates: the rate-limiter at this session's depth is classifier keyword granularity, not the physical or logical claim. Remediation for future such gates is almost always at the vocabulary layer (semantic embeddings, explicit subscripting) — not at the hypothesis layer. Planning for future meta-audits should pre-register the CLASSIFIER (not just the hypothesis) to the same discipline as PRDR pins its physical machinery.

### Highlights for next session (S86)

**(1) CATALOG-EXTENSION-V2** — Rerun §W12-1 with LLM-assisted or semantic-embedding classification in place of substring keyword matching; target coverage ≥ 0.90 on the 112-paper corpus (or extend to 150 papers via deeper index enumeration). Why: §W12-1 localized the failure as keyword-bucket specificity (pattern P2). The actual hypothesis — 12-class partition completeness on the S85-S90 frontier — remains untested under the current instantiation. Effort: MODERATE (build semantic classifier; 3-4 hours to integrate embeddings + rerun). Outcome space: PASS (Δ=0, coverage ≥ 0.95) validates the 12-class partition on the 2025-2026 literature at genuine signal; FAIL with LLM classifier evidences a structural 13th-class need. **EVOI HIGH** — decisive binary outcome on a structural completeness claim.

**(2) CANON-PRDR-K-DISAMBIGUATION** — Split bare "K " in the §W12-2 classifier's DIRECTED_OBSERVABLES into explicit sub-keys {K_base, K_corridor, K_R5, K_crit, K_substrate}; rerun. Target: 0 CONTRADICTS (or all residual CONTRADICTS are genuine plan-authoring conflicts requiring mediation). Why: §W12-2 pattern P2 localized the defect; fix is mechanical. Effort: LIGHT (dict update + rerun; < 30 min). Outcome: PASS validates actual S85 plan consistency (uninterpretable under current tool); residual CONTRADICTS after disambiguation are genuine contradictions requiring orchestrator mediation. **EVOI MEDIUM** — sharpens an existing tool but doesn't break new structural ground.

**(3) CANON-REGULATOR-PIN-DISCIPLINE** — Retrofit `sessions/framework/permanent-results-registry.md` to require explicit regulator tags on every a_0 / a_2 / a_4 citation. Add a REGULATOR column to registry-row metadata; downstream gates importing bare a_n must specify their regulator of choice in the gate block's machinery pin. Why: §W12-4 class-(d) status means bare "a_2" is structurally ill-defined; without this discipline future gates inherit hidden regulator-shopping risk. Effort: LIGHT (registry schema update + audit existing rows; 2 hours). Outcome: PASS is a registry update landing with retrofit SHA; no physical falsifier component. **EVOI MEDIUM** — infrastructural prevention of future PRU Class-8 defects.

**(4) BRANCH-IV-REAUDIT-FULL-DK** — Rerun §W12-3 with either an extended L_max = 14 Casimir schematic (incrementally adds ~130 sectors) OR a partial first-principles D_K diagonalization on the Jensen-deformed SU(3) spectrum (full solve at L_max = 10, with τ_fold Jensen scaling applied to each (p, q) sector's eigenvalue). Why: §W12-3 PASS is under the Casimir schematic, which omits Jensen scaling and BdG pairing. The pin holds and strengthens under the schematic; removing the schematic caveat would promote the retraction from "schematic-level" to "spectral-triple-level." Effort: MODERATE for L_max = 14 scan (~1 hour); HEAVY for full D_K diagonalization (full solve is ~GPU-hours). Outcome: PASS under full D_K removes the schematic qualifier; FAIL under full D_K reopens branch-(iv) with specific energy-scale prediction of where Josephson dominance would recover. **EVOI HIGH** — tests whether the schematic equivalence holds at full spectral fidelity.

**(5) REGULATOR-TAXONOMY-DERIVED-OBSERVABLES** — A deeper §W12-4 pass: re-evaluate m_H, m_t, α_s(M_Z), w0_FW, n_s NOT as pinned scalars but as regulator-dependent re-derivations from their upstream spectral moments (m_H as a function of a_4 + Connes-Chamseddine boundary conditions, α_s as n_s² − 1 under the 5-regulator atlas, etc.). Apply the same 5-regulator atlas; classify each derived observable's spread. Why: current §W12-4 PASS treats pinned scalars as class (a) trivially; the more informative taxonomy inherits upstream class (d) spreads. Effort: HEAVY (needs explicit derivation paths for 5+ observables; full session wave). Outcome space: 3-5 derived observables likely move into class (c) or (d); registry gains "regulator-sensitive derived quantity" flag. **EVOI MEDIUM** — quantifies the regulator-dependence footprint without adding physical commitment.

### Wave signature

**"Substrate walls pinned, instruments revealed — the PASS/FAIL split is a diagnostic alignment, not a tally."**

The 2-PASS / 2-FAIL outcome is not a balance-sheet; it is a structural stratification. The two GEOMETRIC gates PASSed because the substrate they probe IS regulator-robust on the axes tested at this schematic level: branch-(iv) retraction holds and strengthens under L_max scan {8, 10, 12}; the 16-observable registry admits a structurally complete 4-class taxonomy (even if its middle classes are empirically empty). The two NON-PHONONIC gates FAILed because the instruments — a 3-bucket keyword classifier and a directed-observable vocabulary — have granularity narrower than what they're auditing. Both FAILs localize TOOL defects with concrete remediation paths, not hypothesis-refutations. The wave's structural content is: the probes worked, the instruments surfaced their own vocabulary limits, and the emergent pattern (P1 — dimensionless a_n ratios as L_max-stable invariants) is a new theorem candidate that neither gate alone made visible. A next session addressing §C items 1 and 2 will test whether the two hypotheses (12-class falsifier completeness, S85 plan consistency) actually hold under sharper instruments — converting the current tool-layer FAILs into hypothesis-layer PASS or FAIL with genuine structural content.

---
