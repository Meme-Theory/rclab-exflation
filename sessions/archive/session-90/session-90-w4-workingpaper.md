# Session 90 Wave W4 — W1 cascade-tail + α(M) ALT-CORRIDOR + LRD + PBH substrate-physics (Results Working Paper)

**Session**: 90 | **Wave**: W4 | **Plan**: session-90-plan-w4.md | **Theme**: W1 cascade-tail + α(M) ALT-CORRIDOR + LRD + PBH substrate-physics — 5 items led by W-1 workshop's (d)∘(b) compositional primary corridor; CF-37 is 3.5 we BIG (largest single S90 item); three-axis Stage-2 verify follows post-PASS (lizzi + volovik + mack; EXCLUDES connes + phonon-first).

## Gate Sections

### §W4-1. CF-37 — S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION (phonon-first-cosmologist + connes-ncg-theorist)

**Status**: **composite FAIL** at PROXY-REFINEMENT-PENDING level — Sub-A PASS, Sub-B FAIL (rel_dev = 0.78 ≫ 0.30 RATIO band), Sub-C FAIL (n ≈ 0 over M-scan; α' approximately constant). Per plan §11 FAIL clause for Sub-clause B: (d)∘(b) compositional primary corridor is CLOSED as the LRD α-anchor candidate at the structural-ansatz layer; routes to S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor. PROXY-REFINEMENT-PENDING caveat: a full CM-1995 §III.4 finite-spectral-triple residue formula re-evaluation at the (d)∘(b) corridor on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` (queued as separate workshop ~3.5 we) could in principle revise the χ'_weight factor away from the Wedderburn-rank-ratio choice 0.5 used here.
**Gate ID**: `S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION`
**Trigger**: `[VERIFY-THEOREM]` ∧ `[SIGN]`
**Classification**: **GEOMETRIC** (Cell-I cohomology-class observable; algebra-INVARIANT spectrum-only functional)
**Agent**: `phonon-first-cosmologist` (PRIMARY; orchestrator-conducted under /rclab-solo agent-ownership-takeover) + `connes-ncg-theorist` (CO-AUTHOR content for χ' inheritance morphism — derived theorem cited from S89 §W2-3 npz, audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`)
**Hypothesis**: α'(M_LRD=10⁷, L_max=10) is a finite positive ratio in (0,1) lying within 30% RATIO (CF-38 FAIL'd; default band retained — see §W4-2) of empirical anchor 1/458 ≈ 2.18e-3, with M-asymptotic envelope `α'(M) = 1 + c·(M/M_threshold)^{-n}` having `n>0`; establishes calibration corpus instance #2 of the simultaneous element-1 + element-3 double-deformation pattern (instance #1 = §VII.AF.1.OP-PROJ W-5 baseline).
**Plan reference**: `sessions/session-plan/session-90-plan-w4.md` §W4-1 (machinery pin, three-sub-clause thresholds, 7-step substitution chain source; ~3.5 we BIG).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("alpha LRD horizon microstate Connes-Karoubi pairing")` | Hits include S87 pixelation-lock-hawking-transit (M_LRD=10⁸ context, not 10⁷), W-5 cross-pillar bridge baseline. No closure on (d)∘(b) corridor exists. |
| `search_knowledge("chi prime inheritance morphism W2-3 Wedderburn 9 8")` | S89 §W2-3 derived theorem 8-step proof retrieved: ker(χ'\|_M_3(C)) = entire M_3(C) (rank 9); target M_2(C) ⊗ Cl(1) (dim 8); Wedderburn 9 > 8 forces zero map. |
| `search_knowledge("Hochschild cocycle gradient symmetric VII.AF.1.OP-PROJ")` | §VII.AF.1.OP-PROJ baseline canonical: `R_universal = ⟨[φ_g^{sym}], [Ch(P_0(τ_fold))]⟩` regulator-INVARIANT pairing; cocycle source line 14704 of registry. |
| `get_constant("M_KK")` | 7.428660036284456e+16 GeV (M_KK_gravity default; canonical_constants.py line 341) |
| `get_constant("M_Pl_reduced")` | 2.435e+18 GeV (CODATA 2018) |
| `get_constant("R_universal_HP1_strict_F4")` | 1.030902 (S86 W-5 V4 substitution chain Step 2; Class-(d) PROVENANCE; PRIMARY canonical = `eps_H_HP1_norm = 16.197719`) |
| `get_constant("alpha_LRD_FW")` | "Constant 'alpha_LRD_FW' not found" — confirms CF-38 FAIL outcome (no canonical pin); CF-37 Sub-B retains 30% RATIO. |
| `trace_entity("simultaneous element-1 element-3 double-deformation calibration corpus")` | Instance #1 = §VII.AF.1.OP-PROJ W-5 baseline LANDED S87 W5-1; instance #2 = THIS GATE's structural target (CF-37). |

Per `.claude/rules/knowledge-index-usage.md`: queries executed before script-write; not PRE-CLOSED — gate reaches a structural-ansatz verdict.

**Verdict**:

`S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION: FAIL -- value='alpha_prime_M_LRD=4.80000e-04;empirical_anchor_1over458=2.18341e-03;rel_dev=0.7803;sub_A=PASS;sub_B=FAIL;sub_C=FAIL;composite=FAIL;chi_prime_weight=3_over_6_eq_0.5;R_universal_baseline=1.030902;M_KK_over_M_Pl_reduced_sq=9.30729e-04;envelope_n=-1.341959469194494e-20;envelope_R_squared=0.2000;L_max=10;bot20_occupation_at_L10={(0, 0): 8, (0, 1): 6, (1, 0): 6};proxy_refinement_pending=True;full_cm1995_residue_evaluation_deferred=True;chi_prime_anchor_audit_sha=90bba262af80a04c;after_pattern_compliance=True' scheme=connes-karoubi-pairing-on-chi-prime-inheritance convention=substrate-IS-Cell-I-K-counter-instance-2-PROXY-REFINEMENT-PENDING L_max=10 audit_sha256=10ee072fe2c193f38c3ef6c9e766806fb1d5ed8fe0cded5414f79ceff17022ca content_sha256=23f63d7f228439bfef11cc274fb3402fbcaa355a456d7f056582e995e4f0ee56 schema_version=S87+`

Dual-SHA companion row: `# audit_sha256_short=10ee072fe2c193f3 content_sha256_short=23f63d7f228439bf # S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION dual-SHA companion row (W9a-99 split)`

3-tuple annotation row (per S87 schema-v2): `# sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID # S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION 3-tuple annotation (S87 schema-v2)`

Disposition: **composite FAIL with structural meaning** per plan §W4-1 §11: "Sub-clause B FAIL: the (d)∘(b) corridor returns a finite positive ratio in (0, 1) but it is NOT the empirical LRD α-anchor 1/458. The corridor is closed as the LRD α-anchor candidate; an alternative anchor source must be identified. The secondary (c)∘(d) corridor is opened at S91+ AUX-4 as the next candidate." The PROXY-REFINEMENT-PENDING tag in the convention field signals that the verdict is at the structural-ansatz layer (Wedderburn-rank-ratio χ'_weight = 3/6 = 0.5 + dimensional bridge M_KK²/M_Pl_reduced²); a FULL CM-1995 §III.4 residue formula evaluation is queued separately and could revise.

**Results**:

*Key returns (4-tuple).*
- 4-tuple: `(value='alpha_prime_M_LRD=4.80000e-04;...', scheme=connes-karoubi-pairing-on-chi-prime-inheritance, convention=substrate-IS-Cell-I-K-counter-instance-2-PROXY-REFINEMENT-PENDING, L_max=10)`
- α'(M_LRD=10⁷, L_max=10) full float64 = 4.797450e-04
- α'(M_LRD) publication precision (5 sig figs per Class 8.3) = 4.80000e-04
- empirical anchor 1/458 = 2.18341e-03
- rel_dev = |α' - 1/458|/(1/458) = 0.7803 (78.0%)
- audit_sha256 (full 64-char): `10ee072fe2c193f38c3ef6c9e766806fb1d5ed8fe0cded5414f79ceff17022ca`
- content_sha256 (full 64-char): `23f63d7f228439bfef11cc274fb3402fbcaa355a456d7f056582e995e4f0ee56`

*Input SHA pins (5 files, 16-char prefixes shown).*
- `computations/session-84/s84_spectrum_cache_L12_tau019.npz`: `<runtime SHA captured>` (S84 master cache)
- `computations/session-89/s89_w1_alpha_m_horizon_microstate_count.npz`: `<runtime SHA>` (S89 §W1-1 FAIL diagnostic; corridor (a) CLOSED reference only)
- `computations/session-89/s89_w2_a7_chi_prime_inheritance_morphism.npz`: `<runtime SHA>`; anchor audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`
- `sessions/permanent-results-registry.md`: `910792333e1a61f0...`
- `computations/_shared/canonical_constants.py`: `5a19a04e0adef8cd...`

*Substrate spectral content at L_max=10.*
- 65 Peter-Weyl sectors (p,q) with p+q ≤ 10 (filtered from 90 in L=12 master cache)
- 78,080 total eigenvalues at L_max=10
- |λ|_min = 0.819741 M_KK-units (sector (0,0))
- |λ|_max = 4.670218 M_KK-units (highest-level sector at L=10)
- bot-20 occupation: `{(0, 0): 8, (0, 1): 6, (1, 0): 6}` total 20 ✓
  - NOTE: the plan §5 step 1 references S88 W2-6 cardinality vector (2, 4, 8, 6); my computed bot-20 occupation at L_max=10 differs because (2,4,8,6) is the level-stratification of DISTINCT eigenvalue strata at the W2-6 observable, not the bot-20 occupation by sector. The 20-count itself matches.

*χ' inheritance morphism verification (S89 §W2-3 derived theorem).*
- chi_prime_morphism_matrix shape: (9, 9); stored 9×9 form for source basis representation
- kernel_M3C_dimension: 9 (entire M_3(ℂ) summand)
- chi_target_dim: 4 (= M_2(C))
- chi_prime_target_dim: 8 (= M_2(C) ⊗ Cl(1) ≅ M_2(C) ⊕ M_2(C))
- composite verdict: PASS (S89 W2-3); K_counter advanced 2 → 3
- Operative content: Wedderburn 9 > 8 forces χ'\|_M_3(ℂ) = 0 (zero map); ker = entire M_3(ℂ).
- Wedderburn rank ratio χ'_weight = (rank(C) + rank(M_2(C))) / (rank(C) + rank(M_2(C)) + rank(M_3(C))) = (1+2)/(1+2+3) = **3/6 = 0.5**

*W-5 §VII.AF.1.OP-PROJ baseline cross-check (un-restricted reproduction).*
- R_universal_HP1_strict_F4 = 1.030902 (canonical pin per S86 W-5 V4 substitution chain Step 2)
- eps_H_HP1_norm = 16.197719 (PRIMARY canonical per Class-(d) PROVENANCE)
- Reproduction at un-restricted projector (χ'_weight = 1, no inheritance restriction): R_universal value cited verbatim from canonical_constants.py — matches canonical pin to publication precision (Class 8.3 1e-5: True). The cross-check is the substrate-first-canonical-sourcing layer (per `substrate-first-canonical-sourcing.md` — uses canonical pin, not external-paper provenance).

*M-scan computation table.*

| M [M_sun] | Λ(M)/M_KK | g(M, L=10) | α'(M) |
|:----------|:----------|:-----------|:------|
| 1e+05 | 4.582e+43 | 1.000000 | 4.797450e-04 |
| 1e+06 | 4.582e+44 | 1.000000 | 4.797450e-04 |
| 1e+07 (M_LRD) | 4.582e+45 | 1.000000 | 4.797450e-04 |
| 1e+08 | 4.582e+46 | 1.000000 | 4.797450e-04 |
| 1e+09 | 4.582e+47 | 1.000000 | 4.797450e-04 |

α'(M) is approximately CONSTANT across the M-scan: at every probed mass, Λ(M)/M_KK ≫ |λ|_max = 4.67, so the inheritance-restricted projector P_HSS'(M) at L_max=10 spans the entire substrate spectrum. The substrate-saturation factor g(M, L=10) = N_χ'_image / N_substrate = 1.000 across the M-scan. This is a STRUCTURAL prediction of the L_max=10 truncation: at any mass scale where M ≫ M_Pl_reduced, the substrate at L_max=10 is fully enclosed within the horizon-area cutoff.

*Sub-clause A — sign verdict (substitution chain per plan §10, 7 steps).*

  1. **Definition**: `φ_g^{sym} ∈ HH^1(A_K)` is the gradient-symmetric Hochschild 1-cocycle on A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ); cohomology class [φ_g^{sym}] is regulator-class INVARIANT (W-5 calibration corpus instance #1 anchor); χ': A_K → M_2(C) ⊗ Cl(1) is the inheritance morphism with ker(χ'\|_M_3(C)) = M_3(ℂ) entire (S89 §W2-3); P_HSS'(M) = χ'^*(P_HSS(M)) is the inheritance-restricted Peter-Weyl horizon-spanning projector.
  2. **Substitution (positivity of numerator)**: P_HSS'(M_LRD) is a positive idempotent in K_0(BdG-sub-algebra) → [Ch(P_HSS'(M_LRD))] is a non-negative element of HH^*_even. [φ_g^{sym}] is gradient-SYMMETRIC → its pullback χ'^*[φ_g^{sym}] is non-negative on the cone of positive idempotents.
  3. **Substitution (Connes-Karoubi positivity)**: pairing of a non-negative cohomology class with a non-negative K-class is non-negative. Computed `pairing_numerator = 5.154510e-01` (must be > 0). Strictly positive because χ' has non-zero image on at least one of the C or H summand blocks (Wedderburn 9 > 8 only kills M_3(ℂ), not C ⊕ H).
  4. **Substitution (positivity of denominator + dimensional bridge)**: M_KK² > 0 (canonical positive); S_BH^semicl(M_LRD; M_Pl_reduced²) > 0 for M > 0; ratio (M_KK/M_Pl_reduced)² = 9.307286e-04 > 0.
  5. **Substitution (substrate saturation)**: g(M_LRD, L=10) = 1.000000e+00 ∈ (0, 1] (inheritance-restricted projector saturates the L=10 substrate at M_LRD).
  6. **Combine**: α'(M_LRD) = R_universal × χ'_weight × (M_KK/M_Pl_reduced)² × g(M_LRD, L=10) = 1.030902 × 0.5 × 9.307286e-04 × 1.000 = **4.797450e-04**.
  7. **Direction read-off**: 0 < 4.797450e-04 < 1 ⇒ **Sub-clause A PASS** (existence + bounded-by-(0,1) substrate prediction confirmed).

  Python verification log (script Step 10): `pairing_value > 0` ✓; `area_ratio > 0` ✓; `g(M_LRD) > 0` ✓; `0 < alpha_prime < 1` ✓.

*Sub-clause B — empirical anchor comparison (30% RATIO band; CF-38 FAIL'd ⇒ default band retained).*
- α'(M_LRD) = 4.797450e-04
- empirical anchor 1/458 = 2.183406e-03
- rel_dev = |α' - 1/458|/(1/458) = 0.7803 (78.0%)
- Sub-clause B band: PASS ≤ 0.10, INFO 0.10–0.30, FAIL > 0.30
- 0.78 > 0.30 ⇒ **Sub-clause B FAIL**

*Sub-clause C — M-asymptotic envelope fit.*
- envelope form per plan §9: α'(M) = 1 + c·(M/M_thr)^{-n}; require n > 0 AND R² ≥ 0.95
- Log-log linearization on (1 - α'(M)) vs M: c = -9.995203e-01; M_thr = 1.000000e+07 M_sun (anchored at M_LRD); n = -1.34e-20 ≈ 0; R² = 0.20
- Reason: α'(M) is approximately constant across the M-scan (substrate at L_max=10 is fully spanned by P_HSS'(M) for all M in scan range); the envelope fit is structurally underdetermined.
- n ≤ 0 (numerically ≈ 0; falls outside `n > 0` strict prediction) ⇒ **Sub-clause C FAIL**

*Composite collapse (per plan §9 + `gate-verdicts.md §"Composite-collapse rule"`).*

| Sub-clause | Verdict |
|:-----------|:--------|
| A (sign 0<α'<1) | PASS |
| B (rel_dev ≤ 30% RATIO) | FAIL |
| C (n>0 AND R²≥0.95) | FAIL |

Collapse: any Sub-clause FAIL ⇒ composite FAIL. Composite verdict = **FAIL**.

3-tuple annotation: sign=PASS (α' > 0); magnitude=FAIL (|α' - 1/458|/1/458 > info_band); regime=VALID (L_max=10 truncation per Friedrich-Bär saturation S87 W11-3 — operational truncation, not regime breakdown). Per gate-verdicts.md collapse: regime=VALID + magnitude=FAIL ⇒ composite FAIL (matches above).

*Cross-checks performed.*
- **CC1 (un-restricted baseline reproduction)**: cited canonical pin R_universal_HP1_strict_F4 = 1.030902 from canonical_constants.py; Class 8.3 publication precision check (|R - 1.030902| < 1e-5) PASS by definition (no re-derivation).
- **CC2 (χ' kernel rank)**: S89 §W2-3 derived theorem (8 steps) verified via npz read; ker dimension = 9 = entire M_3(ℂ); composite verdict PASS at S89; K_counter 2 → 3.
- **CC3 (Wedderburn rank ratio)**: rank(A_K) = 1+2+3 = 6; rank(χ' image) = 1+2 = 3; ratio = 0.5 (used as χ'_weight in the structural ansatz). Honest disclosure: alternative defensible weights are 5/14 ≈ 0.357 (dim_C ratio of A_K summands) or 1.0 (no dim suppression on spectral pairing); FULL CM-1995 §III.4 evaluation would PIN the factor unambiguously.
- **CC4 (substrate saturation across M-scan)**: at M_LRD = 10⁷ M_sun, Λ(M)/M_KK = 4.58e+45 ≫ |λ|_max(L=10) = 4.67. The L_max=10 substrate is fully spanned by P_HSS'(M_LRD) → g(M_LRD, L=10) = 1.000. Same holds for all 5 M-scan points.
- **CC5 (verdict-file SHA uniqueness)**: audit_sha256 = `10ee072fe2c193f38c3ef6c9e766806fb1d5ed8fe0cded5414f79ceff17022ca`; unique vs prior 46 verdicts in s90_gate_verdicts.txt (last prior was CF-38 at `bbaf9be166c09346...`).

*Data files produced.*
- script: `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.py` (~430 lines; PROXY-REFINEMENT-PENDING tagged in convention field per `cross-pillar-bridge-anatomy.md §"deferred-pending"`)
- data: `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.npz` (9.7 KB; 25 keys including alpha_prime_M_LRD_value, M_scan, g_M_scan, envelope fit, sub-clause verdicts)
- plot: `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.png` (45 KB; α'(M) vs M log-log with empirical anchor + 30% RATIO band overlaid)
- verdict: `computations/session-90/s90_gate_verdicts.txt` (canonical line + dual-SHA companion + 3-tuple annotation)

*Solution-space implication.*

The (d)∘(b) compositional primary corridor is CLOSED as the LRD α-anchor candidate at the PROXY-REFINEMENT-PENDING structural-ansatz layer: under the Wedderburn-rank-ratio χ'_weight = 3/6 = 0.5 and the dimensional bridge M_KK²/M_Pl_reduced² = 9.31e-4, the structural prediction α'(M_LRD) = 4.80e-4 is a factor ~4.5× smaller than the empirical 1/458 = 2.18e-3 anchor (78% RATIO deviation, well outside the 30% band).

Per plan §11 FAIL clause, this routes to **S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor** as the next candidate. The (c)∘(d) corridor is structurally distinct from (d)∘(b) — element-1 (c) replaces the χ'-pullback with a different cohomology-class deformation, while element-3 (d) retains the inheritance-restricted projector. The secondary corridor's γ(s) ≠ Γ(s) modified-universal-kernel choice supplies a different scale-factor in the residue evaluation; whether this lands α' in the 30% RATIO band of 1/458 is the S91+ test.

The PROXY-REFINEMENT-PENDING caveat is structurally important: a FULL CM-1995 §III.4 finite-spectral-triple residue evaluation at the (d)∘(b) corridor on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` (queued ~3.5 we) could revise the χ'_weight factor away from 0.5. If the FULL evaluation produces χ'_weight ~ 4.6× larger than 0.5 (e.g., 2.3, accounting for the 4.5× factor discrepancy), the (d)∘(b) corridor could RECOVER as the LRD anchor candidate. This is the carry-forward ambiguity preserved at PROXY-REFINEMENT-PENDING level.

Calibration corpus impact: instance #2 of the simultaneous element-1 + element-3 double-deformation pattern at the Cell-I cohomology-class layer is NOT LANDED as a CONFIRMED instance at PROXY-REFINEMENT-PENDING level. The pattern's K-counter advancement (Hybrid Independence Test per `cross-pillar-bridge-anatomy.md`) does NOT proceed at S90 W4; deferred to FULL CM-1995 §III.4 evaluation in S91+ workshop dispatch.

*Self-assessment.*

The CF-37 compute reached a structurally-meaningful FAIL verdict via a transparent ansatz layer. The substrate framing was honored: the substrate IS the spectral triple (A_K, H_K, D_K) at L_max=10; the inheritance-restricted projector is substrate-IS (NOT a horizon embedded in spacetime); the Wedderburn rank ratio is substrate-derived from the S89 §W2-3 derived theorem; the dimensional bridge M_KK²/M_Pl_reduced² carries substrate-IS area scale to laboratory-IN reduced-Planck scale at Element 3 of the bridge anatomy.

The PROXY-REFINEMENT-PENDING convention tag honestly discloses the structural-ansatz layer: the verdict is reliable AT THIS LAYER but does not foreclose the corridor at the FULL CM-1995 §III.4 layer. Per `cross-pillar-bridge-anatomy.md §"deferred-pending"` clause SUGGESTION at K=1, this disclosure protocol is the structurally-correct compliance pattern; future S91+ FULL CM-1995 §III.4 evaluation could revise to PASS or confirm FAIL.

The Sub-clause A 7-step substitution chain executed cleanly — sign verdict PASS BY CONSTRUCTION (Connes-Karoubi positivity + Wedderburn 9 > 8 + (M_KK/M_Pl)² > 0). The Sub-clause B FAIL is the primary closure; Sub-clause C FAIL on n ≈ 0 is a derivative consequence of g(M, L=10) saturating to 1 across the M-scan (substrate at L_max=10 is too coarse a truncation to resolve M-dependence of the inheritance-restricted projector).

Direction-of-explanation flowed correctly: substrate eigenvalues (78,080 at L_max=10) → χ'-image inheritance restriction (39,040 states under Wedderburn rank ratio) → cohomology pairing (R_universal × χ'_weight = 0.515) → bridge map (× M_KK²/M_Pl²) → emergent α'(M) interpretation. NO container-thinking inversion (no "BH horizon embedded in spacetime"; framed as "inheritance-restricted Peter-Weyl projector spanning substrate eigenvalues at L_max=10 cutoff").

Downstream gates affected:
- Three-axis Stage-2 verify (S91+ AUX-5) is NOT triggered (composite FAIL at S90 W4 closes the candidate; Stage-2 would only fire on PASS).
- S91+ AUX-4 secondary (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor activates as next candidate (this is the substantive carry-forward).
- §VII registry STAGE-1-CANDIDATE landing for Cell-I cohomology-class double-deformation calibration corpus instance #2 is DEFERRED to S91+ FULL CM-1995 §III.4 evaluation.

L_max stability: the L_max=10 truncation is operationally feasible per Friedrich-Bär saturation argument from S87 W11-3 (`math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"`). The substrate's |λ|_max(L=10) = 4.67 sits well inside the inheritance-restricted projector's Λ(M_LRD)/M_KK = 4.58e+45 cutoff, so no sectors with > 1% contribution are discarded. Higher L_max would not change the verdict at PROXY-REFINEMENT-PENDING level (the χ'_weight ansatz choice dominates the structural prediction); only FULL CM-1995 §III.4 evaluation would.

---

### §W4-2. CF-38 — S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY (phonon-first-cosmologist)

**Status**: FAIL — anchor not promoted; CF-37 Sub-clause B retains default 30% RATIO band (documentation-truthful per plan §11; NOT a substrate-physics failure).
**Gate ID**: `S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY`
**Trigger**: `[AUDIT]` (mechanical pre-flight; outcome conditionally tightens CF-37 Sub-clause B)
**Classification**: **NON-PHONONIC** (registry-state classification check; no substrate-physics derivation)
**Agent**: `phonon-first-cosmologist` (PRIMARY; orchestrator-conducted per /rclab-solo agent-ownership-takeover; mechanical knowledge-MCP query + deterministic re-grep)
**Hypothesis**: Empirical anchor `1/458 ≈ 2.18e-3` (S88 W1b1-63 branch (c)) is either STAGE-3-PERMANENT in `permanent-results-registry.md` OR registered as canonical pin `alpha_LRD_FW` in `canonical_constants.py` with substrate-derived PROVENANCE; PASS tightens CF-37 Sub-clause B from 30% RATIO to 10% RATIO.
**Plan reference**: `sessions/session-plan/session-90-plan-w4.md` §W4-2 (W-1 AUX-2 pre-flight; 0.1 we mechanical).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("empirical anchor 1/458 LRD alpha M_LRD S88 W1b1-63 branch c promotion status")` | 10 hits returned. Closest hit (`s87-pixelation-lock-hawking-transit.md`) uses M_LRD = 10⁸ M_sun (NOT the LRD pivot 10⁷ M_sun); other hits are unrelated (cross-pillar bridge MANDATORY status, K-counter advancement, generic Level-3 anchor template text). NO STAGE-3-PERMANENT registry entry containing "1/458" with substrate-derived provenance was returned. |
| `trace_entity("alpha_LRD empirical anchor 1/458")` | "No trace found" — explicit absence; the entity does not exist in the project knowledge index across any of the 9 entity types (theorems, closed, gates, sessions, open, researchers, equations, provenance, constants). |
| `get_constant("alpha_LRD_FW")` | "Constant 'alpha_LRD_FW' not found" — explicit absence; the canonical pin does not exist in `canonical_constants.py`. |

Per `.claude/rules/knowledge-index-usage.md`: queries executed before script-write, salient returns documented; not PRE-CLOSED (the question itself is the gate).

**Verdict**:

`S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY: FAIL -- value='promotion_status=FAIL_retain_30pct;criterion_a_pass=False;criterion_b_pass=False;intermediate_promotion=False;cf37_sub_b_band=30pct_RATIO;plan_edit_applied=False;mcp_search_knowledge_no_stage3_hit=True;mcp_trace_entity_no_trace_found=True;mcp_get_constant_alpha_LRD_FW_not_found=True;registry_grep_anchor_token_present=False;registry_grep_stage_3_in_file=True;registry_grep_co_located=False;canonical_grep_alpha_LRD_FW_assignment=False;canonical_grep_alpha_LRD_FW_provenance=False;after_pattern_compliance=True' scheme=knowledge-mcp-registry-query convention=mechanical-pre-flight-AUX-2 L_max=N/A audit_sha256=bbaf9be166c09346296e34ac3bf02b4b7980fd6fc3c48517404992872ccd9dbb content_sha256=17d718c39f77264c694e64c26af9cf071525dd345aed2fa2c1590055c5022d98 schema_version=S87+`

Dual-SHA companion row: `# audit_sha256_short=bbaf9be166c09346 content_sha256_short=17d718c39f77264c # S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY dual-SHA companion row (W9a-99 split)`

Disposition: **FAIL — documentation-truthful**. Per plan §W4-2 §11 FAIL clause: "Empirical anchor 1/458 retains pre-promotion status; CF-37 Sub-clause B threshold is the default 30% RATIO; the (d)∘(b) corridor PASS criterion is the wider band (`α' ∈ [1.527e-3, 2.836e-3]`). No substrate-physics implication." The verdict reflects the registry/canonical state factually; it does NOT close any substrate-physics corridor.

**Results**:

*Key returns (4-tuple).*
- 4-tuple: `(value='promotion_status=FAIL_retain_30pct;...', scheme=knowledge-mcp-registry-query, convention=mechanical-pre-flight-AUX-2, L_max=N/A)`
- audit_sha256 (full 64-char): `bbaf9be166c09346296e34ac3bf02b4b7980fd6fc3c48517404992872ccd9dbb`
- content_sha256 (full 64-char): `17d718c39f77264c694e64c26af9cf071525dd345aed2fa2c1590055c5022d98`

*Input SHA pins (3 files, full 64-char prefixes shown).*
- `sessions/permanent-results-registry.md`: `910792333e1a61f0...`
- `computations/_shared/canonical_constants.py`: `5a19a04e0adef8cd...`
- `sessions/session-plan/session-90-plan-w4.md`: `a1f66516b5b7ff01...`

*Criterion (a) — STAGE-3-PERMANENT registry entry containing 1/458 / alpha_LRD with substrate-derived provenance.*
Per-paragraph deterministic scan of `permanent-results-registry.md` (split on blank lines; regex `(1/458|alpha_LRD|LRD α-anchor|LRD alpha-anchor)` AND literal `STAGE-3-PERMANENT` in the same block):
- `anchor_token_present` (any of the 4 tokens anywhere in file) = **False**
- `stage_3_permanent_present_in_file` (literal somewhere) = True
- `anchor_co_located_with_stage_3_permanent` (in same blank-line-delimited block) = **False**
- **criterion_a_pass = False** (anchor token never appears in the registry text — the registry contains 0 matches for "1/458" or any of the alternate anchor labels)

*Criterion (b) — `alpha_LRD_FW` canonical pin with substrate-derived PROVENANCE.*
Two regex tests on `canonical_constants.py`:
- `^\s*alpha_LRD_FW\s*=` (assignment line) = **False** (no assignment exists)
- `"alpha_LRD_FW"\s*:` (PROVENANCE dict key) = **False** (no PROVENANCE entry)
- **criterion_b_pass = False** (the canonical pin does not exist; PROVENANCE dict has no entry)

*Intermediate-promotion check (informs INFO band).*
Per-paragraph scan for anchor token co-located with `STAGE-1-CANDIDATE` or `STAGE-2`:
- `intermediate_promotion_co_located = False` (no partial-promotion entry; INFO band not triggered)

*Verdict logic (plan §W4-2 §9 collapse table).*
| Logical state | Verdict | CF-37 Sub-clause B band |
|:--------------|:--------|:------------------------|
| (a) ∨ (b) | PASS | tightens 30% → 10% RATIO |
| ¬(a) ∧ ¬(b) ∧ intermediate | INFO | retains 30% RATIO (partial promotion documented) |
| ¬(a) ∧ ¬(b) ∧ ¬intermediate | **FAIL** ✓ | **retains default 30% RATIO** ✓ |

Result: ¬False ∧ ¬False ∧ ¬False = ¬False ∧ True ⇒ FAIL branch fires. Plan-block edit NOT applied (plan-w4.md §W4-1 §9 retains the 30% RATIO Sub-clause B band as authored).

*Cross-checks performed.*
- **CC1 (MCP-vs-script consistency)**: All three MCP returns (search_knowledge, trace_entity, get_constant) confirm the same negative result that the deterministic in-script regex re-grep produces. The MCP and the script are in agreement on (a) and (b) being False.
- **CC2 (anchor-token registry-grep universality)**: The 4-pattern regex `(1/458|alpha_LRD|LRD α-anchor|LRD alpha-anchor)` returned 0 matches across the entire registry file (910 KB). This is consistent with the orchestrator's pre-flight grep (the only "1/458"-adjacent registry mentions in the project's session files are in plan/working-paper documents, not in the canonical registry).
- **CC3 (canonical-pin universality)**: `grep -n "alpha_LRD"` on `canonical_constants.py` returns 0 hits (verified during pre-flight). The PROVENANCE dict has no `alpha_LRD_FW` key.
- **CC4 (verdict-file SHA uniqueness)**: `audit_sha256 = bbaf9be166c09346...` is unique vs the prior 45 verdict lines in `s90_gate_verdicts.txt` (last prior unique was `49cd6c08fc29d809...` for `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING`).

*Substitution chain.* Not required per plan §W4-2 §10 ("Not required (no sign/direction/threshold substrate prediction). The gate is mechanical; the verdict reflects the registry/canonical state factually.")

*Data files produced.*
- script: `computations/session-90/s90_w4_cf38_anchor_promotion_status.py` (~230 lines; canonical AFTER-pattern with `from canonical_constants import *`, `compute_dual_sha`, `emit_verdict`)
- verdict line append: `computations/session-90/s90_gate_verdicts.txt` (canonical line + dual-SHA companion row)
- NO `.npz` / `.png` artifacts (mechanical pre-flight; plan §W4-2 §6 specifies no data files)

*Solution-space implication.*
CF-38 FAIL closes one branch of CF-37's Sub-clause B threshold space: the tightening pathway to 10% RATIO is not authorized at S90 W4 dispatch. The default 30% RATIO band stands; CF-37 dispatches with PASS criterion `α' ∈ [1.527e-3, 2.836e-3]` (per plan §W4-1 §9). The S91+ Stage-2 verify (W-1 AUX-5) post-CF-37-PASS will likewise inherit the 30% band rather than the tightened 10% band.

The S88 W1b1-63 branch (c) anchor 1/458 remains unpromoted because no substrate-derived derivation has yet been registered for it as a STAGE-3-PERMANENT theorem. CF-37 itself, on PASS, would be a candidate to drive that promotion (the (d)∘(b) corridor's α'(M_LRD) being substrate-IS would supply the substrate-derived provenance the registry currently lacks). This is a forward dependency note, not a S90 W4 carry-forward.

*Self-assessment.*

The mechanical pre-flight executed cleanly. Three independent verification axes (MCP search, MCP trace, MCP get_constant) all returned negative; the in-script deterministic regex re-grep confirmed at the byte level. The verdict is FAIL with full audit-trail transparency: the value-field documents which of (a), (b), intermediate fired (none); the dual-SHA pins are unique against prior session verdicts; the plan-block was NOT edited (correct, since FAIL).

Substrate framing was honored per plan §W4-2 §13: the verdict reflects DOCUMENTATION STATE, not substrate physics. The "FAIL" label signifies "anchor not yet promoted in the registry/canonical bookkeeping layer", NOT "the LRD α-anchor is wrong" or "the (d)∘(b) corridor is closed". The bookkeeping framing is preserved verbatim in both the verdict-value field and this WP entry.

Downstream gates affected:
- §W4-1 (CF-37) dispatches with default 30% RATIO Sub-clause B band (no tightening applied).
- The S91+ Stage-2 verify (W-1 AUX-5) inherits the 30% band on CF-37 PASS.
- A future session may RE-RUN CF-38 if the 1/458 anchor is later promoted (e.g., as a downstream consequence of CF-37 PASS supplying substrate-derived provenance); this is forward observation, not a current carry-forward.

L_max stability: not applicable (mechanical pre-flight; no spectral truncation). The `L_max=N/A` tag in the verdict-line is the correct convention per plan §6 machinery pin.

---

### §W4-3. CF-39 — S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY (mechanical closure; orchestrator-authored)

**Status**: **FAIL — mechanical closure** as PRE-REG-INC blocked by CF-40 FAIL upstream prerequisite. Per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` 5 admissibility clauses ALL satisfied; per plan §W4-3 §5 prerequisite text + plan §W4-4 §11 BLOCKED clause. NOT a substrate-physics failure; the (d)∘(b) downstream cosmological-horizon prediction remains structurally awaitable on a refined CF-40 retry at S91+. Option A supersedes-tag emission to S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY (full 64-char `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d`) is **DEFERRED** to refined-CF-40-PASS at S91+ (per `gate-verdicts.md` Option A protocol — supersedes tags only fire on CORRECTIVE PASS lines, not on FAIL/PRE-REG-INC closures).
**Gate ID**: `S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY`
**Trigger**: `[VERIFY]` (re-execution of S88 §W1-2 deferred FAIL under refined CF-40 species-multiplicity input; emits Option A `supersedes`-tagged corrective canonical line per `gate-verdicts.md §"Option A"` absolute verdict permanence — DEFERRED on FAIL/PRE-REG-INC closure)
**Classification**: **PHONONIC** (substrate cascade-tail observable at substrate-pinned horizon equilibrium T_H = 1.057 MeV; substrate-clock observable, single-τ-slice substrate-IS Level 1)
**Agent**: `mack-cosmic-bridge` was the planned PRIMARY (sole writer per observational-anchor + registry-write authority); however due to upstream CF-40 FAIL the closure is **orchestrator-authored mechanical closure** per `mechanical-closure-discipline.md` (no Mack agent dispatch — saves agent dispatch tokens; preserves audit-trail integrity).
**Hypothesis**: With refined CF-40 `g_*(T_H = 1.057 MeV)` (lattice-QCD + Boltzmann threshold-suppressed at m_e), the canonical re-pinning `L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴` returns within 0.5 log-OOM ABSOLUTE of `f(M_at_W1c69)` AND `Step5_residual_post_correction` shrinks by ≥ 1.0 log-OOM relative to the S88 §W1-2 FAIL pre-correction residual.
**Plan reference**: `sessions/session-plan/session-90-plan-w4.md` §W4-3 (prereq: CF-40 PASS; 0.5 we).

**MCP Pre-Compute Audit** (mechanical closure — substantive MCP queries deferred to refined-CF-40-PASS retry at S91+):

| Query | Salient return |
|:------|:---------------|
| Disk grep for `S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED` in `s90_gate_verdicts.txt` | Status = FAIL; audit_sha256 = `66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6`; max_rel_dev = 0.135414; g_star_BS_T_H = 9.408297 (candidate, NOT promoted) |
| Disk grep for S88 supersedes target full 64-char in `s88_gate_verdicts.txt` | `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` confirmed present (S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY at line 34); ready for refined-CF-40-PASS Option A supersedes-tag emission at S91+ |
| `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` 5-clause admissibility check | ALL 5 clauses PASS — see §"Closure admissibility checklist" below |

Substantive MCP queries pre-registered for the refined-CF-40-PASS retry (deferred to S91+): `get_constant("T_H")` (verify 1.057 MeV substrate-pinned per S88 W6 §V.1), `get_constant("A_horizon")` (substrate-IS horizon area), `trace_entity("substrate cascade-tail formula S88 W6 V.5")`, `search_knowledge("L_H_canonical re-pinning cascade-tail 13 OOM Option A supersedes")`.

**Verdict**:

`S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY: FAIL -- value='PRE-REG-INC_blocked_by_S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED=FAIL_g_star_BS_T_H_pending_FD_BE_integrated_form_refinement;cf40_max_rel_dev=0.135414;cf40_g_star_BS_T_H_candidate_not_promoted=9.408297;cf40_audit_sha_full_64=66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6;option_a_supersedes_target_full_64=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d;option_a_supersedes_emission_deferred=True;refinement_pathway=Kolb-Turner_Eq3.62_FD_BE_integrated_forms;deferred_to_S91=True;plan_decision_point_routing=session-90-plan-w4.md_§W4-3_§5_prereq_halt_+_§W4-4_§11_BLOCKED_clause;closure_kind=mechanical-orchestrator-authored-no-mack-dispatch;closure_admissibility_per_mechanical-closure-discipline.md=ALL_5_CLAUSES_PASS;after_pattern_compliance=True' scheme=substrate-pinned-T_H-cascade-tail convention=canonical-re-pinning-Option-A-supersedes-MECHANICAL-CLOSURE-CF40-BLOCKED L_max=10 audit_sha256=017258e3c8613ec855b5576df6c17f48bc7373621d95f8c58c786d5208cd3917 content_sha256=617f648717c9e6fd56feddc124bf78f400eaaf9e643d624faf6a70dceba2be62 schema_version=S87+`

Dual-SHA companion row: `# audit_sha256_short=017258e3c8613ec8 content_sha256_short=617f648717c9e6fd # S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY dual-SHA companion row (W9a-99 split)`

PRE-REG-INC comment row: `# PRE-REG-INC per session-90-plan-w4.md §W4-3 §5 + §W4-4 §11; deferred to S91; required prereq: [S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED=PASS]; closure_script=computations/session-90/s90_w4_cf39_mechanical_closure_blocked_by_cf40.py`

Disposition: **mechanical closure FAIL** — documented prereq-block per `mechanical-closure-discipline.md`. NO retroactive edit of S88 verdict file (absolute verdict permanence per `gate-verdicts.md` Option A clause 1). NO Option A supersedes-tag emission (deferred to refined-CF-40-PASS at S91+). NO substantive `L_H_canonical = (π²/60)·g_*(T_H)·A_horizon·T_H⁴` numerical evaluation under FAIL'd `g_star_BS_T_H` (would propagate Class-(b) PIN-LOOSE-SOURCE-TIGHT contamination per `epistemic-discipline.md §"Source Reconciliation"`).

**Closure admissibility checklist** (per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` 5 clauses):

| Clause | Requirement | Status |
|:-------|:------------|:-------|
| (1) | Upstream-block topology is the cause: ≥1 upstream prerequisite with verdict ≠ PASS, plan documents the prereq-block scenario | ✓ — CF-40 verdict = FAIL on disk; plan §W4-3 §5 documents "If CF-40 is not PASS yet, halt and request CF-40 dispatch first"; plan §W4-4 §11 documents "CF-39 is BLOCKED until model PASSes" |
| (2) | Verdict honesty: emit FAIL or PRE-REG-INC, NEVER PASS | ✓ — closure verdict = FAIL with `value='PRE-REG-INC_blocked_by_<sym>_<status>_*'` pattern matching the rule's canonical signature |
| (3) | Per-gate-distinct audit_sha256 | ✓ — closure script computes audit_sha256 = `017258e3c8613ec855b5576df6c17f48bc7373621d95f8c58c786d5208cd3917` from input pin map + per-gate identity keys (embed_keys = {_gate_id, _wp_id, _scheme, _convention, _closure_kind}) per rule §3; distinct from CF-40's `66209e0d71b1ed19...` |
| (4) | Audit-trail signature: descriptive `value=` string naming blocking prereq + status | ✓ — value field names CF-40 gate ID + status FAIL + max_rel_dev value + g_star_BS_T_H candidate + Option A supersedes target + refinement pathway; grep-verifiable across the canonical line |
| (5) | Working-paper update is in-script (or equivalent in-session orchestrator follow-up) | ✓ — handled by orchestrator WP-write Task 8 (this entry) per /rclab-solo two-task-per-gate decomposition |

ALL 5 CLAUSES PASS → mechanical closure is admissible.

**Results**:

*Key returns (4-tuple).*
- 4-tuple: `(value='PRE-REG-INC_blocked_by_S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED=FAIL_*', scheme=substrate-pinned-T_H-cascade-tail, convention=canonical-re-pinning-Option-A-supersedes-MECHANICAL-CLOSURE-CF40-BLOCKED, L_max=10)`
- audit_sha256 (full 64-char): `017258e3c8613ec855b5576df6c17f48bc7373621d95f8c58c786d5208cd3917`
- content_sha256 (full 64-char): `617f648717c9e6fd56feddc124bf78f400eaaf9e643d624faf6a70dceba2be62`

*Input SHA pins (4 files).*
- `computations/session-90/s90_gate_verdicts.txt`: `0702ce17c1093931...` (CF-40 verdict source)
- `computations/session-88/s88_gate_verdicts.txt`: `3d67eacec7accba0...` (S88 supersedes target reference)
- `computations/_shared/canonical_constants.py`: `5a19a04e0adef8cd...`
- `sessions/session-plan/session-90-plan-w4.md`: `a1f66516b5b7ff01...` (plan reference)

Per `mechanical-closure-discipline.md §3`: per-gate identity keys embedded in audit_sha256 computation: `{_gate_id: "S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY", _wp_id: "session-90-w4-workingpaper.md::§W4-3", _scheme: "substrate-pinned-T_H-cascade-tail", _convention: "canonical-re-pinning-Option-A-supersedes-MECHANICAL-CLOSURE-CF40-BLOCKED", _closure_kind: "PRE-REG-INC-upstream-blocked"}` — preserves sig_5 SHA uniqueness.

*Prereq-block verification (Step 1 + Step 2 of closure script).*

Closure script grepped CF-40 verdict line on disk and confirmed:
- Status: **FAIL** (NOT PASS — mechanical closure trigger satisfied per rule §1 clause 1)
- audit_sha256: `66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6` (full 64-char; matches §W4-4 entry above)
- max_rel_dev: 0.135414 (CF-40 max anchor deviation; > 10% PASS band)
- g_star_BS_T_H: 9.408297 (CF-40 candidate, NOT promoted to canonical_constants per Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention)

If CF-40 had returned PASS, the mechanical closure script would have errored out with exit code 3 ("CF-40 PASSed; mechanical closure NOT applicable. Re-dispatch CF-39 with the actual L_H_canonical computation per plan §5."). The PASS-branch absence is enforced by construction.

*S88 supersedes target SHA verification (Step 3 of closure script).*

S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY at audit_sha256 head `2afd17ef99c81123` confirmed present in `s88_gate_verdicts.txt` AT FULL 64-CHAR FORM `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d`. The full 64-char form is the supersedes-tag target on a hypothetical CF-39 PASS at S91+ refined-CF-40-PASS retry. **Per `gate-verdicts.md` Option A protocol clause 5: supersedes tags only fire on CORRECTIVE CANONICAL PASS lines, NOT on FAIL/PRE-REG-INC closures.** This mechanical closure does NOT emit a supersedes tag; the S88 verdict file is NOT modified (absolute verdict permanence preserved). The full-64-char form is documented in the value field for future-S91+ readiness.

*Refinement pathway (deferred to S91+).*

The S91+ refined-CF-40-PASS retry pathway is structurally:

1. Refine CF-40 model: replace simplified `exp(-m/T)` Boltzmann factor approximation with proper Fermi-Dirac and Bose-Einstein integrated forms per Kolb-Turner Eq.3.62 `g_*_eff(T) = (15/π⁴) ∫ x²√(x² + (m/T)²) / (exp(√(x² + (m/T)²)) ± 1) dx`. Re-run 3-anchor cross-check at PDG-canonical band 10% RATIO.
2. On CF-40 PASS: promote `g_star_BS_T_H` (and T_H if not yet pinned) to `canonical_constants.py` with substrate-derived PROVENANCE. This becomes the canonical pin source for CF-39 dispatch.
3. Dispatch CF-39 with the canonical g_star_BS_T_H value: compute `L_H_canonical = (π²/60) · g_*(T_H) · A_horizon · T_H⁴`; compare against `f(M_at_W1c69)` reference at 0.5 log-OOM ABSOLUTE; check `log_residual_improvement ≥ 1.0` log-OOM.
4. On CF-39 PASS: emit Option A `supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` tagged corrective canonical line per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`. The S88 verdict file is NOT retroactively edited; the corrective line APPENDS to S91+ verdict file with the supersedes tag pointing back to the S88 line. Downstream consumers cite the latest non-superseded line per the supersession-chain reading discipline.

*Cross-checks performed.*
- **CC1 (rule-§1-clause-1 admissibility)**: CF-40 status ≠ PASS confirmed via grep; plan §W4-3 §5 prereq text + plan §W4-4 §11 BLOCKED clause confirmed via plan-text inspection. Mechanical-closure admissibility is structurally satisfied.
- **CC2 (rule-§2 verdict honesty)**: closure verdict = FAIL emitted per the rule's "emit FAIL or PRE-REG-INC, NEVER PASS" clause. NO PASS-branch in script (would error out at Step 2 if CF-40 PASSed).
- **CC3 (rule-§3 per-gate-distinct SHA)**: audit_sha256 = `017258e3c8613ec8...` distinct from CF-40 (`66209e0d71b1ed19...`), CF-37 (`10ee072fe2c193f3...`), CF-38 (`bbaf9be166c09346...`); embed_keys per-gate identity per rule §3.
- **CC4 (rule-§4 audit-trail signature)**: value field grep-verifiable; canonical line + dual-SHA companion + PRE-REG-INC comment row all on disk.
- **CC5 (verdict-file SHA uniqueness across S90)**: audit_sha256 unique vs all 47 prior S90 verdicts.

*Substitution chain.* Not required — mechanical closure is substantively a documented prereq-block routing, not a substrate-physics derivation. The structural reasoning is the 5-clause admissibility check above + plan §W4-3 §5 + §W4-4 §11 quoted text.

*Data files produced.*
- script: `computations/session-90/s90_w4_cf39_mechanical_closure_blocked_by_cf40.py` (~200 lines; mirrors `mechanical-closure-discipline.md` 5-clause admissibility template + canonical AFTER-pattern with embed_keys)
- verdict line + dual-SHA companion + PRE-REG-INC comment row appended to `computations/session-90/s90_gate_verdicts.txt`
- NO `.npz` / `.png` artifacts (mechanical closure; substantive computation deferred to S91+ refined retry)
- **Carry-forward immutability hazard (per `mechanical-closure-discipline.md §"Carry-forward script-bytes immutability"`)**: this closure script SHOULD be made read-only or have its current SHA snapshotted before any future edit, to preserve audit-reproducibility of the verdict line. Operationally deferred to /weave --update or post-session housekeeping.

*Solution-space implication.*

CF-39 mechanical closure does NOT close any substrate-physics corridor — it documents the structural cascade dependency on CF-40 PASS. The (d)∘(b) downstream cosmological-horizon prediction (S88 W6 §V.5 substrate cascade-tail formula's image into the cosmological-horizon observation) remains structurally awaitable on a refined CF-40 retry at S91+.

The Option A supersedes-tag emission to S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY is **DEFERRED, not foreclosed**. The S88 verdict (PASS at the BBN-PBH-LRD-metallicity band-window protocol) stands as the current canonical reading; on refined-CF-40-PASS at S91+, CF-39 PASS would emit a corrective canonical line with supersedes-tag pointing to the S88 SHA, and downstream consumers would shift to the latest non-superseded line per the supersession-chain reading discipline.

Carry-forward to S91+: refined CF-40 retry under proper Kolb-Turner Eq.3.62 FD/BE integrated forms (deferred-pending; the structurally-meaningful CF-40 FAIL diagnosis identified the refinement pathway). PASS at refined CF-40 unblocks CF-39 substantive dispatch + g_star_BS_T_H canonical promotion + L_H_canonical computation + Option A supersedes-tag emission for S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY chain.

*Self-assessment.*

The CF-39 mechanical closure executed per the documented `mechanical-closure-discipline.md` rule with all 5 admissibility clauses satisfied. The closure script was orchestrator-authored (not Mack-dispatched) — saving agent dispatch tokens and preserving audit-trail integrity by avoiding a doomed Mack dispatch with FAIL-cascade INFO degradation. The user's --extra "you may dispatch Mack agent for their assigned tasks IAW /rclab-coordinate" did not override the structural cascade closure rule; per `mechanical-closure-discipline.md` the orchestrator-authored mechanical closure is the structurally-correct response when an upstream prerequisite has FAIL'd within the same wave.

Substrate framing was honored: the substrate cascade FORM (S88 W6 §V.5) is preserved as canonical; the laboratory-IN g_*(T) refinement is awaited at S91+; the substrate-clock T_H = 1.057 MeV reading is preserved as the substrate-pinned anchor for the future computation. Direction of explanation: substrate cascade form → consumes refined laboratory-IN g_*(T) → bridge at S91+ refined-CF-40-PASS retry. NO container-thinking inversion.

PROHIBITED_ACTIONS Class-1 (convention-shopping) prevention: the closure does NOT relax the prereq band, does NOT switch CF-40 verdict from FAIL to PASS, does NOT iterate-until-PASS. The structural cascade is honored exactly as the plan + rule prescribe.

PROHIBITED_ACTIONS Class-3 (post-hoc audit-trail editing) prevention: the S88 verdict file is NOT modified (absolute verdict permanence per `gate-verdicts.md` Option A); the supersedes-tag emission is DEFERRED to S91+ refined-CF-40-PASS where it would emit on a FUTURE corrective canonical PASS line, not retroactively.

Downstream gates affected:
- §VII registry STAGE-1-CANDIDATE landing for the L_H_canonical re-pinning (plan §11 PASS clause): DEFERRED to S91+ refined-CF-40-PASS retry chain.
- S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY canonical reading: UNCHANGED at S90 W4 close (no supersedes-tag emitted; S88 verdict stands as current canonical).
- BBN-PBH metallicity-anchor band-window predictions downstream: UNCHANGED (the S88 PASS reading is the current canonical anchor).

L_max stability: not exercised (mechanical closure; no substantive L_H_canonical computation). The `L_max=10` tag in the verdict-line is the substrate cascade-tail's plan-pinned L_max from §W4-3 §6; consistent with the CF-37 substrate L_max=10 and the substrate cascade form's natural truncation.

---

### §W4-4. CF-40 — S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED (mack-cosmic-bridge)

**Status**: **composite FAIL** — 2 of 3 PDG/Planck cross-check anchors exceed the 10% RATIO PASS band (100 GeV: rel_dev = 13.54% FAIL; 1 GeV: rel_dev = 5.99% INFO; 1 MeV: rel_dev = 13.03% FAIL). Per plan §11 FAIL clause: "CF-39 is BLOCKED until model PASSes." Structurally-meaningful FAIL: the simplified `exp(-m/T)` Boltzmann-factor approximation is too aggressive vs the canonical Bose-Einstein / Fermi-Dirac integrated forms (Kolb-Turner Eq.3.62); refinement pathway identified for S91+ retry. `g_star_BS_T_H = 9.4083` produced as canonical-pin CANDIDATE but NOT promoted to `canonical_constants.py` (Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention per `epistemic-discipline.md §"Source Reconciliation"`).
**Gate ID**: `S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED`
**Trigger**: `[VERIFY]` (re-execution of S88 §W1-3 species-multiplicity lookup under lattice-QCD-corrected `g_*(T)` near Λ_QCD ≈ 200 MeV + Boltzmann threshold-suppression at m_e/m_W/m_top; 3 PDG/Planck cross-check anchors at T ∈ {100 GeV, 1 GeV, 1 MeV})
**Classification**: **PARTICLE** (species-multiplicity g_*(T) is a particle-physics-derived count; lattice-QCD corrections + Boltzmann threshold-suppression on laboratory-IN input; substrate cascade FORM remains pinned at S88 W6 §V.5)
**Agent**: `mack-cosmic-bridge` (PRIMARY sole writer per observational-anchor authority; dispatched via Agent tool per user --extra "may dispatch Mack agent for their assigned tasks IAW /rclab-coordinate")
**Hypothesis**: Across 3 cross-check anchors T ∈ {100 GeV, 1 GeV, 1 MeV}, the Boltzmann-suppressed reference `g_*_BS(T)` matches the PDG/Planck reference within 10% RATIO per anchor; this validates the refined species-multiplicity model as the appropriate input for CF-39 L_H_canonical re-pinning at T_H = 1.057 MeV.
**Plan reference**: `sessions/session-plan/session-90-plan-w4.md` §W4-4 (CF-W1-3-RETRY + CRITERION-REVISION; 1.3 we; CF-40 PRECEDES CF-39 wave-internal).

**MCP Pre-Compute Audit** (executed by mack agent at dispatch time):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("g_star T lattice QCD Borsanyi 2016 Boltzmann threshold suppression")` | Borsanyi et al. 2016 (Nature 539, 69) lattice-QCD g_*(T) crossover identified as canonical shape source. PDG 2024 SM masses for species table. |
| `trace_entity("substrate cascade form S88 W6 V.5")` | Substrate cascade-tail formula `L_H = (π²/60)·g_*(T)·A·T⁴` per S88 W6 §V.5 Result 2; substrate FORM canonical, g_*(T) input is laboratory-IN refinement target. |
| `search_knowledge("PDG g_star T 100 GeV 1 GeV 1 MeV anchor")` | PDG-canonical ~106.75 / 60-65 / 3.36-10.75 at the 3 anchor temperatures. |
| `get_constant("T_H")` | Not in canonical_constants.py at S90 dispatch; mack used inline T_H = 1.057 MeV (S88 W6 §V.1 substrate-pinned). |
| `get_constant("m_e")`, `get_constant("m_W")`, `get_constant("m_top")`, `get_constant("m_H_obs")` | SM particle masses retrieved from PDG-canonical pins. |

**Verdict**:

`S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED: FAIL -- value='all_3_anchors_rel_dev_le_10pct=False;rel_dev_100GeV=0.135414;rel_dev_1GeV=0.059943;rel_dev_1MeV=0.130267;g_star_BS_T_H=9.408297;g_star_BS_100GeV=92.2946;g_star_BS_1GeV=65.4515;g_star_BS_1MeV=9.3496;max_rel_dev=0.135414;T_H_value_MeV=1.057;lattice_QCD_pin=Borsanyi+2016_shape_anchored_crossover_PDG_2024_SM_masses;cascade_form_pin=S88_W6_V5;composite=FAIL' scheme=lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade convention=PDG-canonical-3-anchor-cross-check L_max=N/A audit_sha256=66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6 content_sha256=dbb0e8c327a9771dadd773618716de0a6a483987592423b484c0254c9d8e49cb schema_version=S87+`

Dual-SHA companion row: `# audit_sha256_short=66209e0d71b1ed19 content_sha256_short=dbb0e8c327a9771d # S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED dual-SHA companion row (W9a-99 split)`

Disposition: **composite FAIL with structurally-meaningful diagnosis**. Per plan §W4-4 §11 FAIL clause: "Model misses lattice-QCD or Boltzmann threshold-suppression; needs deeper refinement (deferred-pending to S91+). CF-39 is BLOCKED until model PASSes." The FAIL is NOT a hardware/script failure; it is a structurally-meaningful identification of the simplified `exp(-m/T)` Boltzmann factor approximation's insufficiency vs the canonical Bose-Einstein / Fermi-Dirac integrated forms. Mack identified the refinement pathway (Kolb-Turner Eq.3.62 integrated form) for S91+ retry.

**Results**:

*Key returns (4-tuple).*
- 4-tuple: `(value='all_3_anchors_rel_dev_le_10pct=False;...;composite=FAIL', scheme=lattice-QCD-corrected-Boltzmann-suppressed-substrate-cascade, convention=PDG-canonical-3-anchor-cross-check, L_max=N/A)`
- audit_sha256 (full 64-char): `66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6`
- content_sha256 (full 64-char): `dbb0e8c327a9771dadd773618716de0a6a483987592423b484c0254c9d8e49cb`

*3-anchor cross-check table.*

| T anchor | g_*_BS (model) | g_*_PDG (reference) | rel_dev | Verdict band |
|:---------|:---------------|:--------------------|:--------|:-------------|
| 100 GeV | 92.2946 | 106.75 | **13.54%** | **FAIL** (> 10%) |
| 1 GeV | 65.4515 | 61.75 | **5.99%** | **INFO** (5%–10%) |
| 1 MeV | 9.3496 | 10.75 | **13.03%** | **FAIL** (> 10%) |

PASS predicate (per plan §9): all 3 anchors rel_dev ≤ 10% RATIO. Result: 1 PASS / 1 INFO / 2 FAIL → **composite FAIL** (any anchor FAIL → composite FAIL). max_rel_dev = 13.54% (at 100 GeV).

*g_star_BS_T_H at the CF-39 anchor (NOT promoted to canonical_constants).*
- T_H = 1.057 MeV (substrate-pinned per S88 W6 §V.1; inline to mack's script as not yet in canonical_constants.py)
- `g_star_BS_T_H = 9.408297` (full float64; computed under simplified Boltzmann factor model)
- Promotion decision: **NOT promoted** to `canonical_constants.py` per Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention. Mack's structural reasoning (verbatim from agent summary): "FAIL verdict means the model has not been validated at the pre-registered 10% RATIO band; promoting a FAIL'd value would be Class-(b) PIN-LOOSE-SOURCE-TIGHT per `epistemic-discipline.md §"Source Reconciliation"` and a PROHIBITED_ACTIONS Class-1 boundary risk."

*Lattice-QCD source + cascade-form pin.*
- `lattice_QCD_pin = "Borsanyi et al. 2016 (Nature 539, 69) shape-anchored crossover; PDG 2024 SM masses"`
- `cascade_form_pin = "S88 W6 §V.5"`
- Borsanyi numerical interpolation table NOT loaded in mack's script; the model uses Borsanyi 2016 qualitative shape (smooth log-tanh interpolation across QCD crossover band [50 MeV, 1 GeV]) anchored to PDG 2024 SM particle masses.

*Cross-checks performed (mack's script log).*
- **CC1 (PDG anchor verification)**: g_*_PDG values (106.75, 61.75, 10.75) cited from PDG 2024; consistent with plan §5 Step 5 expected values.
- **CC2 (substrate cascade FORM preservation)**: substrate cascade-tail formula `L_H = (π²/60)·g_*(T)·A·T⁴` from S88 W6 §V.5 is NOT modified by CF-40; only the laboratory-IN g_*(T) input is refined.
- **CC3 (Boltzmann band [0.2, 5])**: applied per plan §6 machinery pin; species with m_i/T ∈ [0.2, 5] use exp(-m/T); outside band: 1 (relativistic) or 0 (decoupled).
- **CC4 (verdict-file SHA uniqueness)**: audit_sha256 = `66209e0d71b1ed19969595b8f263d526dcb972d2c84895e86bdfd58ecb9573c6` is unique vs prior S90 verdicts (last prior was CF-37 at `10ee072fe2c193f3...`).
- **CC5 (artifact existence verification by orchestrator post-dispatch)**: script (26.7 KB), npz (7.9 KB) with all 13 mandatory keys, png (79 KB), json sidecar (4.0 KB), verdict line + dual-SHA companion all confirmed on disk via `ls -la` + `tail -3` + npz key inspection. Mack's summary matches filesystem reality bit-for-bit.

*Substrate framing separation (per plan §13).*

The substrate cascade FORM is substrate-pinned per S88 W6 §V.5; the `g_*(T)` quantity itself is laboratory-IN PDG-canonical. The refinement here is on the laboratory-IN INPUT to the substrate cascade-tail formula:
- (a) **Substrate-IS cascade form** (NOT refined here; pinned at S88 W6 §V.5): `L_H = (π²/60) · g_*(T) · A_horizon · T⁴` is the canonical substrate-derived cascade-tail observable formula.
- (b) **Laboratory-IN species-multiplicity g_*(T)** (refined here; PDG/Planck-canonical with lattice-QCD shape + Boltzmann threshold-suppression): the count of effective relativistic degrees of freedom at temperature T.
- **Bridge between (a) and (b)**: the 3-anchor cross-check level (100 GeV, 1 GeV, 1 MeV); substrate cascade form CONSUMES the laboratory-IN g_*(T) refined input.

Direction of explanation: substrate cascade form → consumes laboratory-IN g_*(T) → ratio against PDG/Planck reference at 3 anchors. NOT "thermal bath at T" or "early-universe radiation-dominated era" container framing.

*Structural diagnosis (mack's identification of FAIL root cause).*

The composite FAIL is not a script bug; it is a structurally-meaningful identification of the simplified Boltzmann-factor approximation's insufficiency:

- **At T = 100 GeV** (FAIL): W±/Z/H/top all have m_i/T ∈ [0.2, 5] and contribute `exp(-m/T) ≈ 0.18-0.45` instead of the canonical fully-relativistic 1.0 in the proper Bose-Einstein/Fermi-Dirac integrated form. Total shortfall ~14 dof. The simplified `exp(-m/T)` is more aggressive than the canonical `g_*_eff(T) = (15/π⁴) ∫ x²√(x² + (m/T)²) / (exp(√(x² + (m/T)²)) ± 1) dx` per Kolb-Turner Eq.3.62.
- **At T = 1 MeV** (FAIL): e± has m_e/T = 0.511 → exp(-0.511) = 0.600 instead of canonical full-relativistic 1.0; shortfall ~1.4 dof.
- **At T = 1 GeV** (INFO borderline): the QCD-crossover-band species (light quarks + gluons at the deconfined-confined transition) lie outside the threshold band; the rel_dev is dominated by Borsanyi crossover model uncertainty rather than Boltzmann factor.

Refinement pathway for S91+: replace `boltzmann_factor()` helper with proper Fermi-Dirac and Bose-Einstein integrated forms per Kolb-Turner Eq.3.62. This is a deferred-pending refinement; cannot fire in S90 W4 dispatch budget.

*Data files produced.*

| File | Path | Size |
|:-----|:-----|:-----|
| script | `computations/session-90/s90_w4_cf40_species_multiplicity_retry.py` | 26.7 KB |
| data | `computations/session-90/s90_w4_cf40_species_multiplicity_retry.npz` | 7.9 KB (20 keys) |
| plot | `computations/session-90/s90_w4_cf40_species_multiplicity_retry.png` | 79 KB |
| json sidecar | `computations/session-90/s90_w4_cf40_species_multiplicity_retry.json` | 4.0 KB |
| verdict | `computations/session-90/s90_gate_verdicts.txt` (canonical line + dual-SHA companion) | appended |

NOTE on path convention: mack wrote to `computations/session-90/s90_w4_cf40_*` per current canonical convention (per `gate-verdicts.md §"Canonical Verdict-File Path"` + CLAUDE.md project structure). The plan §5 Step 8 wrote `computations/_shared/s90_w4_f_m_species_multiplicity_retry.{py,npz,png}` which is the older `_shared/` convention with `f_m_` prefix; the actual mack output uses the per-session canonical convention with `cf40_` prefix. This is a WP-shell-vs-runtime variance; the canonical path is mack's actual write location.

*Solution-space implication.*

CF-40 FAIL closes one branch of the species-multiplicity model space: the simplified `exp(-m/T)` Boltzmann-factor approximation does NOT validate at the 10% RATIO band over the 3 PDG anchors. The model's structural form is sound (lattice-QCD shape + Boltzmann threshold suppression skeleton), but the threshold-suppression numerics need refinement to the proper FD/BE integrated forms.

Downstream consequence for CF-39: **CF-39 is BLOCKED at the structural-prerequisite level** per plan §W4-3 §5 ("Verify CF-40 PASS verdict line at computations/session-90/s90_gate_verdicts.txt (grep for S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED). If CF-40 is not PASS yet, halt and request CF-40 dispatch first.") and plan §W4-4 §11 ("CF-39 is BLOCKED until model PASSes."). Per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` clause 1, CF-39 should close as PRE-REG-INC blocked by CF-40 FAIL with documented decision-point routing. Alternative: dispatch CF-39 WITH explicit FAIL-status caveat on g_star_BS_T_H = 9.4083, expecting composite-FAIL/INFO outcome. Decision is made at the next §W4-3 task.

Carry-forward to S91+: refined CF-40 retry under proper Kolb-Turner Eq.3.62 FD/BE integrated forms; PASS at 3-anchor 10% RATIO band would unblock CF-39 dispatch + g_star_BS_T_H canonical promotion + L_H_canonical re-pinning Option A supersedes-tag emission.

*Self-assessment (orchestrator review of mack's output).*

Mack's CF-40 dispatch produced a substantively meaningful FAIL, not a script failure. The structural diagnosis (Boltzmann-factor approximation vs Kolb-Turner Eq.3.62 integrated form gap) is correctly identified and reproducibly traceable in the mack script log. The promotion-decision discipline (NOT promoting g_star_BS_T_H to canonical because of FAIL-status) is correct application of `epistemic-discipline.md §"Source Reconciliation"` Class-(b) prevention.

Substrate framing was honored: the substrate cascade FORM (S88 W6 §V.5) is preserved as canonical; the laboratory-IN g_*(T) is the refinement target; the bridge is at the 3-anchor cross-check level. Direction of explanation flowed correctly substrate → laboratory-IN → bridge-cross-check.

The PASS/FAIL/INFO band is pre-registered; the FAIL is honest at the pre-registered threshold; no convention-shopping or threshold-loosening attempted (PROHIBITED_ACTIONS Class 1 + Class 6 honored).

Downstream impact on CF-39 will be addressed at the next compute task (Task 7 — CF-39 dispatch); per plan §W4-3 §5 prerequisite + §W4-4 §11 blocked clause, CF-39 should mechanical-close as PRE-REG-INC blocked by CF-40 FAIL OR dispatch with FAIL-cascade INFO degradation.

L_max stability: not applicable to CF-40 (mechanical particle-physics anchor refinement; no spectral truncation). The `L_max=N/A` tag in the verdict-line is the correct convention per plan §6.

---

### §W4-5. CF-41 — S90-N-PBH-BAND-EDGE-TENSION-PROMOTE (mack-cosmic-bridge)

**Status**: **composite PASS** (the only PASS in S90 W4) — sign=PASS, magnitude=PASS, regime=VALID. Refined `n_PBH_structural_central(g_BBN, refined) = 8.033e-23 m⁻³` lands inside the target PASS region `[5.495e-23, 1e-20] m⁻³` (1.46× above lower edge; 7 OOM below upper edge), inside CF-CURV-6 prior `[10⁻³⁰, 10⁻²⁰]`, AND inside §W1c-69 PASS-magnitude posterior `[8.4e-24, 2.2e-22]`. Effective conjunct band `[5.495e-23, 2.2e-22]` PASS. Upper-22.6% sub-band `[1.83e-22, 2.2e-22]` NOT achieved by Option A baseline (n_PBH 2.27× below upper-22.6% threshold 1.83e-22); Options B/C land closer (Option C 1.641e-22 closest to but still below the upper-22.6% lower edge). Per plan §W4-5 §11 PASS clause: §W1-4 band-edge-INFO promotes to broader PASS region; S91+ §VII registry STAGE-1-CANDIDATE landing target queued (mack sole writer; deferred to S91+).
**Gate ID**: `S90-N-PBH-BAND-EDGE-TENSION-PROMOTE`
**Trigger**: `[VERIFY]` ∧ `[SIGN]` (refined β_PBH at L_max=12 substrate pinning + cascade-tail-mass-distribution refinement; promotes §W1-4 band-edge-INFO to upper-22.6%-conjunct PASS region inclusion)
**Classification**: **GEOMETRIC** (PBH substrate-derived number density via substrate-clock-cancellation factorization `n_PBH = n_edge · prob_form / L_pix_LRD³` per S88 W1a-59 §0; substrate-IS at cardinality level, single-τ-slice substrate-IS Level 1 at τ_fold)
**Agent**: `mack-cosmic-bridge` (PRIMARY sole writer per observational-anchor + registry-write authority; dispatched via Agent tool per user --extra "may dispatch Mack agent for their assigned tasks IAW /rclab-coordinate")
**Hypothesis**: With (a) refined β_PBH at L_max=12 substrate pinning + (b) cascade-tail-mass-distribution refined beyond M_LRD · 2⁻ᵍ in cascade-tail regime g ∈ [143..384], `n_PBH_structural_central(g_BBN, refined)` falls in the upper-22.6%-conjunct AND posterior intersection PASS region `[5.495e-23, 1e-20] m⁻³`; sign_verdict = PASS BY CONSTRUCTION; regime_verdict = VALID at L_max=12 operational truncation.
**Plan reference**: `sessions/session-plan/session-90-plan-w4.md` §W4-5 (CF-W1-4-PROMOTE; ~1.0 we; independent of CF-37/CF-39/CF-40 chain).

**MCP Pre-Compute Audit** (executed by mack agent at dispatch time):

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("n_PBH band edge tension W1-4 promote upper 22.6 conjunct")` | §W1-4 baseline at L_max=10 + S88 W1a-59 §0 substrate-clock-cancellation factorization identified. |
| `trace_entity("substrate-clock-cancellation factorization S88 W1a-59")` | Factorization `n_PBH = n_edge·prob_form/L_pix_LRD³` per S88 W1a-59 §0 lines 60-66; substrate-IS at cardinality level. |
| `get_constant("M_KK")`, `get_constant("tau_fold")` | M_KK = 7.428660036284456e+16 GeV; tau_fold = 0.19. |
| `search_knowledge("CF-CURV-6 prior n_PBH 10^-30 10^-20")` | CF-CURV-6 prior band [10⁻³⁰, 10⁻²⁰] m⁻³. |
| `search_knowledge("W1c-69 PASS-magnitude posterior 8.4e-24 2.2e-22")` | §W1c-69 posterior support [8.4e-24, 2.2e-22] m⁻³. |

**Verdict**:

`S90-N-PBH-BAND-EDGE-TENSION-PROMOTE: PASS -- value='n_PBH=8.0330e-23_m^-3;composite_verdict=PASS;sign_verdict=PASS;magnitude_verdict=PASS;regime_verdict=VALID;target_PASS_lower=5.4954e-23;target_PASS_upper=1.0000e-20;conjunct_lower=5.4954e-23;conjunct_upper=2.2000e-22;upper_22pt6pct_threshold=1.8270e-22;in_target_PASS=True;in_CF_CURV_6_prior=True;in_W1c_69_posterior=True;cascade_mass_distribution_option=A;n_PBH_option_A=8.0328e-23;n_PBH_option_B=1.0627e-22;n_PBH_option_C=1.6413e-22;n_edge_L12=13927053960;n_edge_L10=3048204160;n_edge_ratio_L12_over_L10=4.5689;N_eigs_L12=166896;N_eigs_L10=78080;prob_form_baseline=0.155729;prob_form_refined_A=0.155729;L_pix_LRD_cubed=2.7000e+31;s89_w1_4_audit_sha=2e1993dcd5d5ce6a;s89_w1_4_n_PBH=1.7581e-23;baseline_reproduction_rel_dev=0.000015;after_pattern_compliance=True' scheme=L_max-12-substrate-pinning-cascade-tail-refinement convention=upper-22.6pct-conjunct-posterior-intersection L_max=12 audit_sha256=459863f26cdcfbc56c3045b06db9c81c91138a11ab92033189dc281e36ad72e9 content_sha256=47d334105e49e27552ceacaca634a4800d880411f9f52261ee9abc602d68d649 schema_version=S87+`

Dual-SHA companion row: `# audit_sha256_short=459863f26cdcfbc5 content_sha256_short=47d334105e49e275 # S90-N-PBH-BAND-EDGE-TENSION-PROMOTE dual-SHA companion row (W9a-99 split)`

3-tuple annotation row (per S87 schema-v2 [SIGN] trigger): `# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S90-N-PBH-BAND-EDGE-TENSION-PROMOTE 3-tuple annotation (S87 schema-v2)`

Disposition: **composite PASS** with all 3 sub-clauses PASS — the §W1-4 band-edge-INFO is promoted to the broader PASS region inclusion. The structurally-meaningful finding: the L_max=10 → L_max=12 substrate cardinality refinement ALONE drives the promotion (n_edge ratio 4.5689× via N_eigs ratio 2.137× compounded by C(N_eigs, 2) ≈ N_eigs²/2 binomial form); cascade-tail-mass-distribution Options B/C are NOT REQUIRED for the broader PASS but provide diagnostic alignment with the W1c-69 posterior right-edge.

**Results**:

*Key returns (4-tuple).*
- 4-tuple: `(value='n_PBH=8.0330e-23_m^-3;composite_verdict=PASS;...', scheme=L_max-12-substrate-pinning-cascade-tail-refinement, convention=upper-22.6pct-conjunct-posterior-intersection, L_max=12)`
- n_PBH_structural_central_refined (full float64) = 8.032772249305555e-23 m⁻³
- n_PBH_publication (4 sig figs per Class 8.3) = 8.033e-23 m⁻³
- audit_sha256 (full 64-char): `459863f26cdcfbc56c3045b06db9c81c91138a11ab92033189dc281e36ad72e9`
- content_sha256 (full 64-char): `47d334105e49e27552ceacaca634a4800d880411f9f52261ee9abc602d68d649`

*Substrate cardinality refinement L_max=10 → L_max=12 (the dominant promotion driver).*

| Quantity | L_max=10 | L_max=12 | Ratio |
|:---------|:---------|:---------|:------|
| N_eigs (eigenvalue count) | 78,080 | 166,896 | 2.1374× |
| n_edge = C(N_eigs, 2) | 3,048,204,160 | 13,927,053,960 | **4.5689×** |
| Δ N_eigs | — | +88,816 | — |
| Δ n_edge | — | +10,878,849,800 | — |

The C(N_eigs, 2) ≈ N_eigs² / 2 binomial form compounds the N_eigs ratio quadratically. This is the structural mechanism for the band-edge promotion: NO mass-distribution-refinement contribution is required to reach the broader PASS region.

*Cascade-tail-mass-distribution Options A/B/C.*

| Option | Mass-distribution form | n_PBH (m⁻³) | Region inclusion |
|:-------|:------------------------|:------------|:------------------|
| A (canonical) | M(g) = M_LRD · 2⁻ᵍ | **8.033e-23** | target PASS ✓ |
| B (linear corr.) | M(g) = M_LRD · 2⁻ᵍ · (1 + γ·g) | 1.063e-22 | target PASS ✓ + closer to upper-22.6% |
| C (curvature corr.) | M(g) = M_LRD · exp(-g·ln(2)) · (1 + ε·g²) | 1.641e-22 | target PASS ✓ + closest to upper-22.6% (still 11% below) |

Per S88 W6 §V.5 substrate cascade-tail form, **Option A (`M_LRD · 2⁻ᵍ`) is canonical**. Per substrate-clock-cancellation factorization (S88 W1a-59 §0), n_PBH is g-independent at saturated threshold (g ≥ 143); the M(g) refinement enters only via prob_form 2nd-order correction. Options B/C are diagnostic, not canonical.

*Region inclusion table.*

| Region | Bounds (m⁻³) | n_PBH = 8.033e-23 inside? |
|:-------|:-------------|:---------------------------|
| Target PASS region (plan §9) | [5.495e-23, 1e-20] | **YES** (1.46× above lower; 7 OOM below upper) |
| CF-CURV-6 prior | [10⁻³⁰, 10⁻²⁰] | **YES** (well within prior support) |
| §W1c-69 PASS-magnitude posterior | [8.4e-24, 2.2e-22] | **YES** (inside posterior support) |
| Effective conjunct band | [5.495e-23, 2.2e-22] | **YES** |
| Upper-22.6% sub-band | [1.83e-22, 2.2e-22] | NO (n_PBH 2.27× below lower edge) |

Per plan §W4-5 §9 composite PASS predicate: `n_PBH ∈ [5.495e-23, 1e-20] m⁻³` AND sign_verdict = PASS AND regime_verdict = VALID. **All 3 sub-checks PASS** ⇒ composite PASS.

*Sub-clause sign_verdict — substitution chain (per plan §10, MANDATORY for [SIGN] trigger).*

  1. **Definitions**: `n_edge ∈ ℤ_{>0}` (cardinality is positive integer = 13,927,053,960 at L_max=12); `prob_form ∈ (0, 1]` (substrate-derived formation probability = 0.155729; strictly positive when cascade formation amplitude ≠ 0); `L_pix_LRD³ ∈ ℝ_{>0}` (substrate pixel-volume scale = 2.7e+31 m³; volume strictly positive).
  2. **Substitution**: n_PBH = n_edge · prob_form / L_pix_LRD³ = 13,927,053,960 · 0.155729 / 2.7e+31 = 8.033e-23 m⁻³.
  3. **Sign analysis**: numerator = n_edge · prob_form = 13927053960 × 0.155729 = 2,168,847,820,200 > 0; denominator = L_pix_LRD³ = 2.7e+31 > 0; ratio = numerator / denominator > 0.
  4. **Direction read-off**: n_PBH_structural_central(g_BBN, refined) > 0 ⇒ **sign_verdict = PASS BY CONSTRUCTION**.

  Python verification log (mack's script):
  ```
  Sign verification:
    n_edge (L_max=12) = 13927053960    (must be > 0)  ✓
    prob_form_refined = 1.557290e-01  (must be > 0)  ✓
    L_pix_LRD_cubed = 2.700000e+31    (must be > 0)  ✓
    n_PBH = 8.032772e-23 m^-3         (must be > 0)  ✓
  ```
  All 4 asserts PASS.

*Cross-checks performed.*
- **CC1 (baseline reproduction at L_max=10)**: mack reproduced §W1-4 baseline at L=10 Option A with rel_dev = 1.5e-5 vs S89 §W1-4 pin (n_PBH = 1.7581e-23 m⁻³ at L=10); well below 1e-3 reproduction threshold. The substrate-clock-cancellation factorization is empirically VERIFIED as a structural identity (the 4.57× n_edge ratio + identical prob_form / L_pix³ at L=10 → L=12 produces the 4.57× n_PBH ratio expected from the binomial form).
- **CC2 (Friedrich-Bär saturation at L_max=12)**: bot-20 substrate first eigenvalues at L=12 dominated by sectors (1,1) at λ = 0.836 (multiplicity 12); regime_verdict = VALID per S87 W11-3 Friedrich-Bär saturation argument (`math-scripts.md §"D_K Block-Diagonality"`).
- **CC3 (substrate-clock-cancellation factorization)**: factorization `n_PBH = n_edge · prob_form / L_pix_LRD³` per S88 W1a-59 §0 lines 60-66; structural form preserved across L_max scan.
- **CC4 (verdict-file SHA uniqueness)**: audit_sha256 = `459863f26cdcfbc56c3045b06db9c81c91138a11ab92033189dc281e36ad72e9` is unique vs all 48 prior S90 verdicts (last prior was CF-39 mechanical closure at `017258e3c8613ec8...`).
- **CC5 (artifact existence verification by orchestrator post-dispatch)**: script (43.7 KB), npz (18.8 KB) with 54 keys (39 mandatory + 15 diagnostic extras), png (194.6 KB), verdict line + dual-SHA companion + 3-tuple annotation all confirmed on disk via `ls -la` + `tail -4` + npz key inspection. Mack's summary matches filesystem reality bit-for-bit.

*Substrate framing (per plan §13).*

n_PBH is substrate-derived: n_edge is substrate cardinality at L_max=12 truncation; prob_form is substrate formation probability; L_pix_LRD³ is substrate pixel-volume scale at LRD pivot. The substrate-clock-cancellation factorization is substrate-IS at the cardinality level (`phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` Level 1, single-τ-slice at τ_fold). The laboratory-IN observable is the BBN-constrained PBH abundance n_PBH(z=z_BBN); the bridge map is the substrate-derived n_PBH → BBN abundance constraint at z=z_BBN.

Direction of explanation: substrate cardinality (13.9 billion edge-pairs at L_max=12) → formation probability (substrate-derived 0.155729) → pixel-volume scale (2.7e+31 m³ at LRD pivot) → laboratory-IN BBN abundance constraint. NOT "PBHs forming in spacetime"; framed as "substrate cascade-edge cardinality manifesting as BBN-era PBH number density".

*Structural finding (the dominant promotion driver).*

The §W1-4 band-edge INFO → broader PASS region promotion is driven ALMOST ENTIRELY by the substrate cardinality refinement L_max=10 → L_max=12 (4.57× n_edge ratio), NOT by cascade-tail-mass-distribution refinement. The N_eigs scaling 2.137× compounds via the binomial C(N_eigs, 2) ≈ N_eigs²/2 form to give the 4.57× n_edge ratio — a STRUCTURAL property of the substrate-clock-cancellation factorization, not a coincidence.

Cascade-tail-mass-distribution Options B/C provide diagnostic alignment with the W1c-69 posterior right-edge (Option C 1.64e-22 closest to upper-22.6% lower edge 1.83e-22 but still 11% below). To reach the upper-22.6% sub-band [1.83e-22, 2.2e-22] would require either (a) a higher L_max (L=14+) substrate refinement, (b) a more aggressive cascade-tail-mass-distribution beyond Options B/C, OR (c) a different prob_form refinement at the substrate-derived formation probability layer. None of these are required for the broader PASS region inclusion at S90 W4 close.

*Data files produced.*

| File | Path | Size |
|:-----|:-----|:-----|
| script | `computations/session-90/s90_w4_cf41_n_pbh_band_edge_tension_promote.py` | 43.7 KB |
| data | `computations/session-90/s90_w4_cf41_n_pbh_band_edge_tension_promote.npz` | 18.8 KB (54 keys; 39 mandatory + 15 diagnostic) |
| plot | `computations/session-90/s90_w4_cf41_n_pbh_band_edge_tension_promote.png` | 194.6 KB (4-panel visualization) |
| verdict | `computations/session-90/s90_gate_verdicts.txt` (canonical line + dual-SHA companion + 3-tuple annotation) | appended |

NOTE on path convention: mack wrote to `computations/session-90/s90_w4_cf41_*` per current canonical convention; the plan §5 Step 8 wrote `computations/_shared/s90_w4_n_pbh_band_edge_tension_promote.{py,npz,png}` which is the older `_shared/` convention. The actual mack output uses the per-session canonical convention with `cf41_` prefix. WP-shell-vs-runtime variance; canonical path is mack's actual write location.

*Solution-space implication.*

CF-41 PASS LOCATES the §W1-4 PBH band-edge prediction within the broader target PASS region [5.495e-23, 1e-20] m⁻³, an INFO → PASS promotion driven by the substrate L_max=12 cardinality refinement. The substrate-IS prediction `n_PBH ≈ 8.03e-23 m⁻³` becomes a candidate for STAGE-1-CANDIDATE §VII registry landing at S91+ (mack sole-writer per `feedback_mack-bridge-role.md`).

The upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] is NOT reached at Option A canonical (n_PBH = 8.03e-23 sits 2.27× below the upper-22.6% lower edge). The narrower sub-band PASS criterion (per plan §11 PASS clause expanded reading) is open via S91+ refinement (higher L_max OR alternative prob_form construction). This is a forward observation, not a current failure.

Calibration corpus impact: CF-41 is a Level-1 single-τ-slice substrate-IS observable at the cardinality layer (per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`). Its registry landing at §VII at S91+ would be a new substrate-IS Level-1 calibration corpus instance.

*Self-assessment (orchestrator review of mack's output).*

Mack's CF-41 dispatch produced a STRUCTURALLY MEANINGFUL PASS — the only PASS in S90 W4. The dominant promotion driver (substrate L=12 cardinality refinement) was correctly identified and structurally explained (the binomial C(N_eigs, 2) ≈ N_eigs²/2 compounds the 2.14× N_eigs ratio to 4.57× n_edge ratio). The Options B/C diagnostic exploration was thorough and correctly flagged as non-canonical; Option A canonical was confirmed per S88 W6 §V.5 substrate cascade-tail form.

Substrate framing was honored throughout: substrate cardinality → formation probability → pixel-volume scale → laboratory-IN BBN abundance constraint. NO container-thinking inversion (no "PBHs forming in spacetime"). The substrate-clock-cancellation factorization is preserved as the substrate-IS Level 1 single-τ-slice observable.

The PASS verdict is honest at the pre-registered threshold; no convention-shopping or threshold-loosening attempted (PROHIBITED_ACTIONS Class 1 + Class 6 honored). The npz contains 54 keys (more than the 39 mandatory) — mack added per-Option breakdowns + diagnostic comparisons as bonus content; the only minor variance is `prob_form_refined` key absent (replaced with `prob_form_refined_A/B/C` per-Option keys, which is more informative).

Downstream consequence: S91+ §VII registry STAGE-1-CANDIDATE landing target queued for mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`. The substrate-IS observable to land: `n_PBH_structural_central(g_BBN, refined) = 8.033e-23 m⁻³` at L_max=12 substrate pinning + Option A canonical cascade-mass-distribution.

L_max stability: VALID at L_max=12 per Friedrich-Bär saturation argument from S87 W11-3 (`math-scripts.md §"D_K Block-Diagonality"`). The substrate's |λ|_min(L=12) ≈ 0.836 (sectors (1,1) multiplicity 12) sits well above the Friedrich-Bär saturation floor; bot-20 substrate first eigenvalues at L=12 are stable and deterministic. Higher L_max (L=14+) would refine n_edge further (the binomial form scales as N_eigs² which diverges); the broader PASS region inclusion at L=12 would persist at higher L (the n_PBH would only INCREASE, not decrease, away from the lower edge — pushing closer to the upper-22.6% sub-band). The L=12 truncation is operational; not regime-of-validity boundary.

---

## Wave W4 Synthesis (team-lead)

**Date**: 2026-05-14. **Gates**: 5 (1 PASS = CF-41; 4 FAIL = CF-37 + CF-38 + CF-39 + CF-40). **Dispatched**: orchestrator phonon-first-cosmologist (CF-37 + CF-38 + CF-39 mechanical closure) + mack-cosmic-bridge agent (CF-40 + CF-41) per user `--extra` "may dispatch Mack agent for their assigned tasks IAW /rclab-coordinate". All artifacts on disk; verdict file carries 5 new lines + dual-SHA companions + 2 [SIGN]-trigger 3-tuple annotations + 1 PRE-REG-INC comment row. Total wave effort: ~6.4 we per plan; actual orchestrator + agent compute closed in-session.

### 1. Structural outcome — (d)∘(b) corridor CLOSED at PROXY-REFINEMENT-PENDING level (CF-37 + CF-38 joint)

The (d)∘(b) compositional primary corridor (W-1 workshop's selected primary candidate for the LRD α-anchor) is **CLOSED as the LRD anchor candidate at the structural-ansatz layer**. CF-37 returns α'(M_LRD = 10⁷, L_max=10) = 4.80e-4, a factor ~4.5× smaller than empirical 1/458 = 2.18e-3 (rel_dev = 0.78 ≫ 0.30 RATIO band). Sub-clauses A (sign 0<α'<1) PASS; B (anchor 30% RATIO) FAIL; C (envelope n>0, R²≥0.95) FAIL. Composite FAIL.

The closure is at PROXY-REFINEMENT-PENDING level per `cross-pillar-bridge-anatomy.md §"deferred-pending"` SUGGESTION at K=1: a FULL CM-1995 §III.4 finite-spectral-triple residue formula re-evaluation at (d)∘(b) (queued ~3.5 we) could in principle revise the χ'_weight factor away from the Wedderburn-rank-ratio choice 0.5 used here. The PROXY-REFINEMENT-PENDING tag in the convention field signals this honestly.

CF-38 mechanical pre-flight FAIL'd: the empirical anchor 1/458 is NOT promoted to STAGE-3-PERMANENT registry entry NOR registered as `alpha_LRD_FW` canonical pin. CF-37 Sub-clause B retained the default 30% RATIO band rather than tightening to 10%. Both knowledge-MCP queries (search_knowledge + trace_entity) and deterministic in-script regex re-grep of registry + canonical_constants confirmed the negative result; CF-38 FAIL is documentation-truthful, not substrate-physics.

Joint reading: the **(c)∘(d) secondary corridor at S91+ AUX-4 is the structurally correct next candidate** for the LRD α-anchor, with γ(s) ≠ Γ(s) modified-universal kernel as the discriminator. CF-37 INFO outcome routing (per plan §11) was anticipated at INFO band but the FAIL is more decisive — closes (d)∘(b) decisively at the PROXY-REFINEMENT-PENDING layer and sharpens the case for (c)∘(d) at S91+.

### 2. CF-39/CF-40 cascade — Boltzmann factor approximation insufficient; CF-39 mechanically blocked

CF-40 mack agent dispatch returned composite FAIL: 2 of 3 PDG/Planck cross-check anchors exceed the 10% RATIO PASS band (T = 100 GeV: rel_dev = 13.54% FAIL; T = 1 GeV: 5.99% INFO; T = 1 MeV: 13.03% FAIL). The structurally-meaningful diagnosis from mack's script log: the simplified `exp(-m/T)` Boltzmann-factor approximation is too aggressive vs the canonical Bose-Einstein / Fermi-Dirac integrated forms. At T = 100 GeV, W±/Z/H/top species in the threshold band m/T ∈ [0.2, 5] contribute exp(-m/T) ≈ 0.18-0.45 instead of canonical full-relativistic 1.0; total shortfall ~14 dof. At T = 1 MeV, e± with m/T = 0.511 → exp(-0.511) = 0.600 instead of 1.0; shortfall ~1.4 dof.

The refinement pathway is identified: replace `boltzmann_factor()` helper with proper Fermi-Dirac and Bose-Einstein integrated forms per Kolb-Turner Eq.3.62 `g_*_eff(T) = (15/π⁴) ∫ x²√(x²+(m/T)²) / (exp(√(x²+(m/T)²))±1) dx`. This is queued as carry-forward `CF-S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED` (~1.0 we).

`g_star_BS_T_H = 9.4083` produced as canonical-pin CANDIDATE but **NOT promoted** to `canonical_constants.py` per Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention (`epistemic-discipline.md §"Source Reconciliation"`). Mack's correct application of PROHIBITED_ACTIONS Class-1 boundary discipline.

CF-39 closure: mechanical orchestrator-authored closure as PRE-REG-INC blocked by CF-40 FAIL upstream prerequisite per `mechanical-closure-discipline.md §"When mechanical closure IS acceptable"` 5 admissibility clauses (all PASS). NO Mack dispatch (would have produced doomed FAIL-cascade INFO degradation). NO Option A supersedes-tag emission to S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY (full SHA `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` confirmed present in S88 verdict file; emission DEFERRED to S91+ refined-CF-40-PASS retry per `gate-verdicts.md` Option A protocol clause 5 — supersedes tags only fire on CORRECTIVE PASS lines). NO retroactive edit of S88 verdict file (absolute verdict permanence preserved).

### 3. CF-41 PASS — substrate L=12 cardinality refinement promotes §W1-4 band-edge INFO to broader PASS region

CF-41 mack agent dispatch returned composite PASS — the only PASS in S90 W4. `n_PBH_structural_central(g_BBN, refined) = 8.033e-23 m⁻³` lands inside the target PASS region [5.495e-23, 1e-20] m⁻³ (1.46× above lower edge), inside CF-CURV-6 prior [10⁻³⁰, 10⁻²⁰], AND inside §W1c-69 PASS-magnitude posterior [8.4e-24, 2.2e-22]. 3-tuple: sign=PASS, magnitude=PASS, regime=VALID.

The structural finding: the L_max=10 → L_max=12 substrate cardinality refinement ALONE drives the promotion. N_eigs ratio 2.137× compounds via the binomial C(N_eigs, 2) ≈ N_eigs²/2 form to give n_edge ratio 4.5689× — a structural property of the substrate-clock-cancellation factorization, not a coincidence. Cascade-tail-mass-distribution Options B/C are NOT REQUIRED for the broader PASS but provide diagnostic alignment with the W1c-69 posterior right-edge.

Caveat: the upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] is NOT reached at Option A canonical (n_PBH = 8.03e-23 sits 2.27× below the upper-22.6% lower edge). Options B/C land closer (Option C 1.64e-22 closest, 11% below upper-22.6% lower edge). Reaching the narrower sub-band would require higher L_max (L=14+) substrate refinement OR alternative prob_form construction; queued as carry-forward `CF-S91-CF41-UPPER-22.6-EXTENSION` (~1.5 we).

S91+ §VII registry STAGE-1-CANDIDATE landing target queued for mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (~0.3 we; carry-forward `CF-S91-CF41-VII-LANDING`).

### 4. Downstream implications

| Stream | Effect of W4 | S91+ action |
|:-------|:-------------|:------------|
| (d)∘(b) corridor as LRD anchor candidate | CLOSED at PROXY-REFINEMENT-PENDING level (CF-37 composite FAIL) | (a) FULL CM-1995 §III.4 residue evaluation queued to revise χ'_weight (could revisit FAIL); (b) (c)∘(d) secondary corridor activates with γ(s) ≠ Γ(s) modified-universal kernel (sharper case after (d)∘(b) closure) |
| Empirical LRD α-anchor 1/458 promotion status | NOT promoted (CF-38 FAIL); CF-37 retains 30% RATIO band | If (c)∘(d) corridor produces substrate-derived α' near 1/458 at S91+, that PASS would supply substrate-derived provenance for canonical promotion |
| L_H_canonical re-pinning + Option A supersedes-tag for S88 chain | DEFERRED (CF-39 mechanical PRE-REG-INC closure); no S88 edit | refined CF-40 PASS at S91+ unblocks CF-39 substantive dispatch + Option A supersedes-tag emission to `2afd17ef99c81123...` chain |
| Species-multiplicity model g_*(T) | Boltzmann factor approximation FAIL'd at 10% RATIO band; structural form sound, threshold-suppression numerics need refinement | Replace `exp(-m/T)` with Kolb-Turner Eq.3.62 FD/BE integrated forms; re-test at 3 anchors; PASS unblocks downstream cascade |
| §W1-4 PBH band-edge prediction | INFO → broader PASS region (CF-41 PASS); n_PBH = 8.03e-23 m⁻³ at L=12 substrate pinning + Option A canonical | (a) S91+ §VII registry STAGE-1-CANDIDATE landing for PBH-band-edge-conjunct prediction (mack sole writer); (b) upper-22.6%-conjunct sub-band extension via L_max=14+ substrate refinement OR alternative prob_form |
| Calibration corpus instance #2 of element-1 + element-3 double-deformation pattern at Cell-I | NOT LANDED at PROXY-REFINEMENT-PENDING (CF-37 FAIL); K-counter unchanged at K=1 (W-5 baseline only) | FULL CM-1995 §III.4 evaluation at S91+ could land instance #2; Hybrid Independence Test K-counter advancement deferred |

### 5. Session classification

This is a **constraint-map-advancing** wave with one structurally meaningful PASS (CF-41) and four structurally meaningful FAILs (CF-37 + CF-38 + CF-39 + CF-40), each closing or deferring a specific corridor. Taken as a set, W4 has:

- **Closed** the (d)∘(b) corridor as LRD anchor candidate at PROXY-REFINEMENT-PENDING level (CF-37 — primary substrate-physics outcome).
- **Documented** the absence of empirical anchor 1/458 promotion to STAGE-3-PERMANENT (CF-38 — registry-state truth).
- **Closed** the simplified `exp(-m/T)` Boltzmann-factor approximation at the species-multiplicity layer (CF-40 — particle-physics anchor refinement); identified the Kolb-Turner Eq.3.62 refinement pathway.
- **Mechanically blocked** CF-39 substantive computation per `mechanical-closure-discipline.md` (CF-39 — orchestrator-authored cascade closure); preserved S88 absolute verdict permanence.
- **Located** the §W1-4 PBH band-edge prediction within the broader target PASS region [5.495e-23, 1e-20] m⁻³ (CF-41 — substrate L=12 cardinality refinement; the only PASS).

Wave 4's structurally weightiest finding: the (d)∘(b) corridor closure at PROXY-REFINEMENT-PENDING level **redirects the LRD α-anchor search to the (c)∘(d) secondary corridor at S91+ AUX-4**, with the FULL CM-1995 §III.4 evaluation as the deferred-pending fallback that could revisit (d)∘(b). The CF-41 PASS is the wave's positive structural anchor: substrate L_max=12 refinement reproducibly drives §W1-4 INFO → PASS region inclusion via the binomial C(N_eigs, 2) cardinality form, a structural property not a coincidence.

The CF-37/CF-40 FAILs are NOT framework refutations — they are corridor-elimination + refinement-pathway-identification at honest pre-registered thresholds, exactly the constraint-map-advancing role expected of structurally rigorous gates per `evoi-prioritization.md` "negative results are boundaries, not failures" + `math-scripts.md §"All Results Are Good Results"`. The CF-39 mechanical closure preserves audit-trail integrity per `mechanical-closure-discipline.md` and `gate-verdicts.md` Option A absolute verdict permanence.

---

## Carry-Forward Computations

Per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`: each carry-forward is a 4-field spec (what / inputs / gate / effort) describing GENUINE future computation. `/rclab-plan` consumes this section as the canonical CF source for next-session planning per `Investigating-Workshops.md`. Process observations / in-session bookkeeping live elsewhere (Constraint-Map Updates, Files Produced, synthesis narrative) and DO NOT appear here.

### CF-S91-CF37-FULL-CM1995-RESIDUE — FULL CM-1995 §III.4 finite-spectral-triple residue formula evaluation at (d)∘(b) corridor

| Field | Value |
|:------|:------|
| **What** | Replace the structural-ansatz layer in CF-37 (Wedderburn-rank-ratio χ'_weight = 3/6 + dimensional bridge M_KK²/M_Pl²) with FULL Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula evaluation on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` at the (d)∘(b) compositional primary corridor. Compute χ'^*[φ_g^{sym}] pullback rigorously (verify dχ'^*φ_g^{sym} = 0 at machine epsilon); construct P_HSS'(M) = χ'^*(P_HSS(M)) inheritance-restricted Peter-Weyl horizon-spanning projector with cutoff form derived from inheritance restriction (NOT naive λ² ≤ M_KK²·(M_LRD/M_KK²)); compute Chern character via residue formula on Peter-Weyl-decomposed triple; re-evaluate Connes-Karoubi pairing as finite trace sum. Could revise CF-37's PROXY-REFINEMENT-PENDING FAIL verdict if the FULL χ'_weight differs from 0.5 by ~4.5× in the direction of empirical 1/458 anchor. |
| **Inputs** | `s84_spectrum_cache_L12_tau019.npz` filtered to L_max=10 (78,080 eigenvalues across 65 sectors); `s89_w2_a7_chi_prime_inheritance_morphism.npz` (audit_sha256 `90bba262af80a04c4c33e40376491f850c4ca224aa5c7b8506567a75f9f68843`); §VII.AF.1.OP-PROJ registry text (lines 14690-14722; cocycle source line 14704); canonical_constants pins (R_universal_HP1_strict_F4 = 1.030902, eps_H_HP1_norm = 16.197719, M_KK, M_Pl_reduced, tau_fold); Connes-Moscovici 1995 §III.4 paper for residue formula machinery. |
| **Gate** | `α'(M_LRD=10⁷, L_max=10) ∈ [1.527e-3, 2.836e-3]` (Sub-clause B 30% RATIO band against 1/458) AND sign 0<α'<1 (Sub-clause A) AND envelope α'(M) = 1 + c·(M/M_thr)^{-n} with n>0 + R²≥0.95 (Sub-clause C); composite PASS. PASS revises CF-37 verdict to PASS at FULL-CM1995 layer; FAIL confirms (d)∘(b) closure structurally. |
| **Effort** | ~3.5 we (matches CF-37's original effort estimate; FULL CM-1995 §III.4 residue evaluation is the substantive computation that CF-37 deferred via the structural ansatz). |

### CF-S91-CF37-AUX-4-SECONDARY-CORRIDOR — (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor

| Field | Value |
|:------|:------|
| **What** | Activate the W-1 workshop's secondary corridor (c)∘(d) where element-1 deformation is replaced by a modified-universal-kernel γ(s) ≠ Γ(s) cohomology-class shift (instead of (b) χ'-pullback). Element-3 retains the inheritance-restricted projector P_HSS'(M). Compute α''(M_LRD=10⁷, L_max=10) at (c)∘(d) corridor and test against empirical anchor 1/458. The (c)∘(d) corridor is the W-1 workshop's pre-registered secondary candidate after (d)∘(b) closure (CF-37 FAIL). |
| **Inputs** | Modified-universal-kernel γ(s) ≠ Γ(s) specification (W-1 workshop §AUX-4 source); same substrate inputs as CF-37 (s84_spectrum_cache_L12, s89_w2_a7_chi_prime, canonical pins); §VII.AF.1.OP-PROJ registry baseline; Connes-Moscovici 1995 §III.4 residue formula (modified for γ(s) ≠ Γ(s) kernel choice). |
| **Gate** | `α''(M_LRD=10⁷, L_max=10) ∈ [1.527e-3, 2.836e-3]` (30% RATIO band against 1/458; possibly 10% RATIO if `CF-S91-EMPIRICAL-ANCHOR-PROMOTION` PASSes first) AND Sub-clause A sign + Sub-clause C envelope; composite PASS opens (c)∘(d) as LRD anchor candidate with substrate-derived provenance. |
| **Effort** | ~3.5 we (similar to CF-37; equally BIG at the substantive evaluation layer). |

### CF-S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED — Refined CF-40 retry under proper Fermi-Dirac and Bose-Einstein integrated forms

| Field | Value |
|:------|:------|
| **What** | Replace the simplified `boltzmann_factor()` helper in CF-40 (which used `exp(-m/T)` for species in band m/T ∈ [0.2, 5]) with proper Fermi-Dirac and Bose-Einstein integrated forms per Kolb-Turner Eq.3.62: `g_*_eff(T) = (15/π⁴) ∫ x²√(x²+(m/T)²) / (exp(√(x²+(m/T)²))±1) dx`. Re-test at the same 3 PDG cross-check anchors T ∈ {100 GeV, 1 GeV, 1 MeV}; the proper integrated form is less aggressive than the bare exp(-m/T) and should bring rel_dev within the 10% RATIO band. PASS unblocks CF-39 substantive dispatch + g_star_BS_T_H canonical promotion + L_H_canonical Option A supersedes-tag emission. |
| **Inputs** | Mack's CF-40 script `s90_w4_cf40_species_multiplicity_retry.py` (43,760 bytes; replace `boltzmann_factor()` function); same lattice-QCD source (Borsanyi 2016 + PDG 2024 SM masses); Kolb-Turner "The Early Universe" Eq.3.62 reference; numerical-integration library (scipy.integrate.quad). |
| **Gate** | `rel_dev_i ≤ 0.10` (10% RATIO PASS band) at ALL 3 anchors T ∈ {100 GeV, 1 GeV, 1 MeV} against PDG/Planck reference (106.75, 60-65, 3.36-10.75); composite PASS. PASS unblocks CF-39 + g_star_BS_T_H canonical promotion. |
| **Effort** | ~1.0 we (replace 1 helper function + scipy.quad integration; re-test at 3 anchors; emit corrective verdict). |

### CF-S91-CF39-RE-DISPATCH-POST-CF40-PASS — CF-39 substantive computation + Option A supersedes-tag emission

| Field | Value |
|:------|:------|
| **What** | Conditional on `CF-S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED` PASS at 3-anchor 10% RATIO band: re-dispatch CF-39 substantively per plan §W4-3 §5 procedure. Compute `L_H_canonical = (π²/60) · g_*(T_H = 1.057 MeV) · A_horizon · T_H⁴` using refined g_star_BS_T_H from refined CF-40; compare against `f(M_at_W1c69)` reference at 0.5 log-OOM ABSOLUTE; check `log_residual_improvement ≥ 1.0` log-OOM. On PASS, emit Option A `supersedes=2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d` tagged corrective canonical line per `gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute verdict permanence"`. |
| **Inputs** | Refined CF-40 PASS npz (g_star_BS_T_H canonical pin promoted to canonical_constants.py); T_H = 1.057 MeV (substrate-pinned per S88 W6 §V.1; promote to canonical_constants if not already); A_horizon (substrate-IS horizon area; promote to canonical_constants if not already); S88 W6 §V.5 cascade form; S88 §W1c-69 reference workshop or npz for f(M_at_W1c69); S88 verdict file for full 64-char audit_sha256 grep of `2afd17ef99c81123...`. |
| **Gate** | `delta_log < 0.5` ABSOLUTE log-OOM AND `log_residual_improvement ≥ 1.0` log-OOM AND supersedes-token correctly emitted as full 64-char form (NOT 16-char head per `gate-verdicts.md`); composite PASS. PASS emits Option A corrective canonical line; downstream consumers shift to the latest non-superseded line per supersession-chain reading discipline. |
| **Effort** | ~0.5 we (matches CF-39's original effort estimate; mack sole writer per `feedback_mack-bridge-role.md`). |

### CF-S91-CF41-VII-LANDING — S91+ §VII registry STAGE-1-CANDIDATE landing for PBH-band-edge-conjunct prediction

| Field | Value |
|:------|:------|
| **What** | Land STAGE-1-CANDIDATE registry entry at `§VII.{next-free}` for the PBH-band-edge-conjunct prediction that CF-41 produced: `n_PBH_structural_central(g_BBN, refined) = 8.033e-23 m⁻³` at L_max=12 substrate pinning + Option A canonical cascade-mass-distribution. The entry should follow `cross-pillar-bridge-anatomy.md §"5 IS-not-IN anatomy elements + 3-level ladder discipline"` if classified as a cross-pillar bridge (substrate cardinality ↔ laboratory-IN BBN PBH abundance), OR the standard §VII STAGE-1-CANDIDATE template if classified as a single-pillar substrate-IS observable. Per `feedback_mack-bridge-role.md`, mack is sole writer for §VII registry-text landings on observational-anchor predictions. Per `joint-theorem-promotion.md` Stage-2 verify follows on PASS. |
| **Inputs** | Mack's CF-41 npz `s90_w4_cf41_n_pbh_band_edge_tension_promote.npz` (54 keys; n_PBH = 8.033e-23 m⁻³ + structural finding + cross-checks); `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"` (Level 1 single-τ-slice classification); `cross-pillar-bridge-anatomy.md §"5 IS-not-IN anatomy elements"` template if cross-pillar; `joint-theorem-promotion.md` Stage-1-Candidate template. |
| **Gate** | Registry entry written at `§VII.{next-free}` slot with all 5 IS-not-IN anatomy elements + 3-level ladder (if cross-pillar) declared explicitly OR standard §VII STAGE-1-CANDIDATE template fields populated. Mack's signature on the entry per `feedback_mack-bridge-role.md`. PASS lands the entry; FAIL would require remediation (e.g., classification review). |
| **Effort** | ~0.3 we (registry-text landing; mack sole writer). |

### CF-S91-CF41-UPPER-22.6-EXTENSION — Reach upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] m⁻³

| Field | Value |
|:------|:------|
| **What** | Refine CF-41 to reach the narrower upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] m⁻³ (Option A canonical at L=12 sits at 8.03e-23 m⁻³, 2.27× below upper-22.6% lower edge). Three pathways to explore: (a) extend substrate cardinality refinement to L_max=14+ (would compound the binomial C(N_eigs, 2) form further; structurally would push n_PBH higher); (b) more aggressive cascade-tail-mass-distribution refinement beyond Options B/C (Option D quadratic correction or higher-order); (c) refinement of substrate-derived prob_form (the formation probability layer) beyond the baseline 0.155729. The L_max=14+ path is the structurally cleanest; per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` it is feasible with proper caching. |
| **Inputs** | If pathway (a): higher L_max substrate cache (need to extend `s84_spectrum_cache_L12_tau019.npz` to L=14 via additional Casimir-projection construction; or use Friedrich-Bär saturation theorem to bound NEW-sector contributions analytically). If pathway (b): Option D mass-distribution form specification. If pathway (c): substrate-derived prob_form refinement (e.g., gravitational-collapse threshold β_form per Hawking 1971 Page-style derivation refined with substrate cardinality input). |
| **Gate** | `n_PBH ∈ [1.83e-22, 2.2e-22]` m⁻³ ABSOLUTE-IN-INTERVAL; AND sign_verdict = PASS; AND regime_verdict = VALID. PASS reaches the upper-22.6%-conjunct sub-band, sharpening the §W1-4 promotion further. |
| **Effort** | ~1.5 we (pathway (a) is most tractable; mack consults phonon-first on substrate-cardinality refinement). |

**Carry-forward summary**: 6 carry-forwards totaling ~10.3 wave-equiv (CF-S91-CF37-FULL-CM1995 3.5 + CF-S91-CF37-AUX-4 3.5 + CF-S91-CF40-KOLB-TURNER 1.0 + CF-S91-CF39-RE-DISPATCH 0.5 + CF-S91-CF41-VII-LANDING 0.3 + CF-S91-CF41-UPPER-22.6 1.5). Dependencies: CF-S91-CF39-RE-DISPATCH depends on CF-S91-CF40-KOLB-TURNER PASS; CF-S91-CF41-VII-LANDING is independent (CF-41 PASS already secured); CF-S91-CF41-UPPER-22.6 is independent of the CF-37/CF-39/CF-40 chain. CF-S91-CF37-FULL-CM1995 and CF-S91-CF37-AUX-4 are EITHER/OR alternative pathways for the LRD α-anchor (FULL CM-1995 could revisit (d)∘(b); AUX-4 advances to (c)∘(d) secondary corridor; both could be queued in parallel for S91+ workshop dispatch).

---

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-05-14 | S90-W1-1-EMPIRICAL-ANCHOR-1-458-PROMOTION-STATUS-VERIFY (CF-38) | OPEN (W-1 AUX-2 pre-flight) | FAIL — anchor 1/458 not promoted to STAGE-3-PERMANENT NOR alpha_LRD_FW canonical pin | All 3 MCP queries (search_knowledge, trace_entity, get_constant) returned negative; deterministic in-script regex re-grep confirmed; CF-37 Sub-clause B retains default 30% RATIO band |
| 2026-05-14 | S90-W1-1-ALT-CORRIDOR-SELECTED-LRD-ALPHA-DERIVATION (CF-37) | OPEN (W-1 PRIMARY corridor candidate) | composite FAIL at PROXY-REFINEMENT-PENDING level — α'(M_LRD)=4.80e-4 vs 1/458=2.18e-3, rel_dev=0.78 ≫ 0.30 | Wedderburn-rank-ratio χ'_weight = 0.5 + dimensional bridge M_KK²/M_Pl² gives α' a factor ~4.5× smaller than empirical anchor; (d)∘(b) corridor CLOSED at structural-ansatz layer; FULL CM-1995 §III.4 evaluation could revise (queued S91+) |
| 2026-05-14 | (d)∘(b) compositional primary corridor as LRD anchor candidate | OPEN (W-1 workshop primary candidate) | CLOSED at PROXY-REFINEMENT-PENDING level (CF-37 composite FAIL) | Routes to (c)∘(d) secondary corridor at S91+ AUX-4 with γ(s) ≠ Γ(s) modified-universal kernel as discriminator |
| 2026-05-14 | Calibration corpus instance #2 of element-1 + element-3 double-deformation pattern at Cell-I | OPEN (CF-37 PASS would land instance #2; K=1 from W-5 baseline only) | NOT LANDED at PROXY-REFINEMENT-PENDING (CF-37 FAIL); K-counter unchanged at K=1 | FULL CM-1995 §III.4 evaluation at S91+ (CF-S91-CF37-FULL-CM1995) could land instance #2; Hybrid Independence Test K-counter advancement deferred |
| 2026-05-14 | S90-F-M-SPECIES-MULTIPLICITY-RETRY-BOLTZMANN-SUPPRESSED (CF-40) | OPEN (CF-W1-3-RETRY) | composite FAIL — 2 of 3 PDG anchors > 10% RATIO band (100 GeV: 13.54%; 1 GeV: 5.99% INFO; 1 MeV: 13.03%) | Simplified `exp(-m/T)` Boltzmann factor approximation too aggressive vs canonical Fermi-Dirac/Bose-Einstein integrated forms; refinement pathway = Kolb-Turner Eq.3.62 (queued as CF-S91-CF40-KOLB-TURNER) |
| 2026-05-14 | g_star_BS_T_H canonical pin (T_H = 1.057 MeV) | NOT-EXISTING in canonical_constants.py | NOT PROMOTED — candidate value 9.4083 (CF-40 produced but FAIL'd at validation band) | Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention per `epistemic-discipline.md §"Source Reconciliation"`; promotion conditional on refined CF-40 PASS at S91+ |
| 2026-05-14 | S90-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM-RETRY (CF-39) | OPEN (re-execution of S88 §W1-2 deferred FAIL) | mechanical FAIL closure (PRE-REG-INC blocked by CF-40 FAIL) per `mechanical-closure-discipline.md` 5-clause admissibility | Orchestrator-authored cascade closure; preserves S88 absolute verdict permanence; Option A supersedes-tag emission DEFERRED to S91+ refined-CF-40-PASS retry |
| 2026-05-14 | Option A supersedes-tag emission to S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY (full SHA `2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d`) | EXPECTED on CF-39 PASS (per plan §W4-3 §5) | DEFERRED to S91+ refined-CF-40-PASS retry per `gate-verdicts.md` Option A protocol clause 5 (supersedes only on CORRECTIVE PASS lines) | NO retroactive edit of S88 verdict file (absolute verdict permanence); S88 PASS reading stands as current canonical until S91+ corrective canonical line emitted |
| 2026-05-14 | S90-N-PBH-BAND-EDGE-TENSION-PROMOTE (CF-41) | INFO at §W1-4 baseline (L_max=10) | composite PASS — n_PBH = 8.033e-23 m⁻³ inside target PASS region [5.495e-23, 1e-20] AND inside CF-CURV-6 prior AND inside W1c-69 posterior | Substrate L=12 cardinality refinement (4.57× n_edge ratio via binomial C(N_eigs, 2)) drives §W1-4 INFO → PASS region inclusion; structural property of substrate-clock-cancellation factorization |
| 2026-05-14 | §W1-4 PBH band-edge-INFO state | INFO (L_max=10 baseline) | PROMOTED to broader target PASS region [5.495e-23, 1e-20] m⁻³ at L=12 + Option A canonical | CF-41 PASS; sub-band upper-22.6% [1.83e-22, 2.2e-22] NOT YET reached at Option A canonical (queued as CF-S91-CF41-UPPER-22.6-EXTENSION via L_max=14+ or alternative prob_form) |
| 2026-05-14 | §VII registry STAGE-1-CANDIDATE landing for PBH-band-edge-conjunct prediction | OPEN (queued in plan §W4-5 §11 PASS clause) | DEFERRED to S91+ — mack sole writer per `feedback_mack-bridge-role.md` (carry-forward CF-S91-CF41-VII-LANDING) | CF-41 produces substrate prediction n_PBH = 8.033e-23 m⁻³; registry-text landing is a separate gate (~0.3 we) |
| 2026-05-14 | S91+ AUX-5 three-axis Stage-2 cross-axis independent-verify (lizzi + volovik + mack) for CF-37 | EXPECTED on CF-37 PASS (per plan §W4-1 §11) | NOT TRIGGERED (CF-37 composite FAIL) | Stage-2 verify only fires on PASS per `joint-theorem-promotion.md` Stage-2; S91+ AUX-4 secondary corridor (c)∘(d) becomes the structurally correct next gate instead |

---

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| §W4-2 (CF-38) | `computations/session-90/s90_w4_cf38_anchor_promotion_status.py` (~230 lines) | — (mechanical pre-flight; no .npz) | — | — | ~10 KB |
| §W4-1 (CF-37) | `computations/session-90/s90_w4_alpha_m_alt_corridor_d_compose_b.py` (~430 lines) | `s90_w4_alpha_m_alt_corridor_d_compose_b.npz` (9.7 KB; 25 keys) | `s90_w4_alpha_m_alt_corridor_d_compose_b.png` (45.7 KB) | — | ~70 KB |
| §W4-4 (CF-40) | `computations/session-90/s90_w4_cf40_species_multiplicity_retry.py` (26.7 KB) | `s90_w4_cf40_species_multiplicity_retry.npz` (7.9 KB; 20 keys) | `s90_w4_cf40_species_multiplicity_retry.png` (79.0 KB) | `s90_w4_cf40_species_multiplicity_retry.json` (4.0 KB) | ~118 KB |
| §W4-3 (CF-39) | `computations/session-90/s90_w4_cf39_mechanical_closure_blocked_by_cf40.py` (~200 lines; mechanical closure) | — (no substantive npz; deferred to S91+ refined-CF-40-PASS) | — | — | ~9 KB |
| §W4-5 (CF-41) | `computations/session-90/s90_w4_cf41_n_pbh_band_edge_tension_promote.py` (43.8 KB) | `s90_w4_cf41_n_pbh_band_edge_tension_promote.npz` (18.8 KB; 54 keys) | `s90_w4_cf41_n_pbh_band_edge_tension_promote.png` (194.7 KB; 4-panel) | — | ~257 KB |

Verdicts appended to `computations/session-90/s90_gate_verdicts.txt` (5 new canonical lines + 5 dual-SHA companion rows + 2 [SIGN]-trigger 3-tuple annotations + 1 PRE-REG-INC comment row). Total wave artifact size: ~464 KB across 5 gates. All gate verdicts are unique vs prior S90 verdicts (audit_sha256 uniqueness verified via grep); per-gate audit_sha256 leading 16-hex prefixes: CF-38 `bbaf9be166c09346`, CF-37 `10ee072fe2c193f3`, CF-40 `66209e0d71b1ed19`, CF-39 `017258e3c8613ec8`, CF-41 `459863f26cdcfbc5`.

---

## Closing Notes — researcher-who-did-the-work reflection (2026-05-14)

### What stood out

**(1) CF-41 PASS via the binomial cardinality compounding — substrate truncation level is the dominant lever, NOT the cascade-mass-distribution choice (Structural surprise).**
I went into CF-41 expecting Options A/B/C cascade-tail-mass-distribution refinement to do real work alongside the L=10 → L=12 substrate cardinality scale-up. Instead, the L=12 cardinality refinement ALONE drives the §W1-4 INFO → broader PASS region promotion: N_eigs ratio 2.137× compounds via the binomial C(N_eigs, 2) ≈ N_eigs²/2 form to give n_edge ratio 4.5689× (Wave Synthesis §3 + WP §W4-5 *Substrate cardinality refinement table* lines 567-575). All three Options A/B/C land in the target PASS region [5.495e-23, 1e-20] m⁻³; their differences are diagnostic alignment with the §W1c-69 posterior right-edge, not promotion drivers. The structural reading: the substrate-clock-cancellation factorization `n_PBH = n_edge · prob_form / L_pix_LRD³` has its own quadratic-in-N_eigs scaling that swamps the linear-in-Option mass-distribution corrections. Cardinality is the lever; cascade-mass-distribution is the diagnostic.

**(2) CF-37 α'(M_LRD) under-shoots empirical 1/458 by 4.5×, not over-shoots — direction was opposite of my prior (Physics surprise).**
Prior expectation (mine, going into the compute): a structural ansatz built on the un-restricted W-5 baseline `R_universal_HP1_strict_F4 = 1.030902` would either land NEAR the empirical anchor (PASS at 30% RATIO), or OVER-shoot it (because the baseline retains the full coefficient and the χ' restriction zeros only the M_3(C) sector). The actual result: α'(M_LRD) = 4.797450e-04 vs 1/458 = 2.183e-3, so the structural ansatz UNDER-shoots by factor 4.55×, rel_dev = 0.78 (WP §W4-1 *Sub-clause B verdict*, line 247-251). The dimensional bridge `(M_KK/M_Pl_reduced)² = 9.31e-4` does the work I didn't anticipate — it suppresses much harder than the χ'_weight = 0.5 dimensional dilution. The implication: if FULL CM-1995 §III.4 evaluation gives a χ'_weight that's ~4.5× larger than 0.5 (e.g., 2.3 — possible if the spectral pairing is dominated by the M_3(C) sector that χ' kills, inverting my Wedderburn-rank-ratio intuition), the (d)∘(b) corridor could revisit. The PROXY-REFINEMENT-PENDING tag is honest about this; the closure is conditional, not absolute.

**(3) CF-37 Sub-clause C envelope-fit was structurally underdetermined by the L_max=10 truncation, not by the (d)∘(b) substrate physics (Kinematic surprise).**
The plan §10 substitution chain Step 6 said "α(M_LRD, L_max=10) < 1 + ε for small ε" — anticipating a near-saturated substrate. What actually happened in the M-scan: at L_max=10, Λ(M)/M_KK = 4.58e+45 even at M = 10⁵ M_sun, completely swamping |λ|_max(L=10) = 4.67. So `g(M, L=10) = 1.000000` at every probed mass, and α'(M) is approximately constant across {10⁵, 10⁶, 10⁷, 10⁸, 10⁹} M_sun (WP §W4-1 *M-scan computation table* lines 220-228). The envelope α'(M) = 1 + c·(M/M_thr)^{-n} fit collapses: c → -0.998 at M_thr = 10⁷, n → -1.34e-20, R² = 0.20 (line 252). Sub-clause C FAIL is essentially a kinematic artifact of the substrate's full enclosure within the horizon-area cutoff at any reasonable BH mass — the M-scan probes a region where the L=10 substrate is structurally invariant. To resolve M-dependence, you'd need either (a) much smaller M (sub-Planck scales where the substrate isn't fully spanned), or (b) much higher L_max where the cutoff Λ(M) starts to bite the spectrum. Neither is the natural test. Sub-clause C as pre-registered is hard to satisfy at L_max=10 + reasonable BH mass scan; this is plan-design feedback for S91+.

**(4) Mack's CF-40 FAIL diagnosis was structurally precise — exp(-m/T) vs Kolb-Turner Eq.3.62 integrated form (Methodological surprise).**
I went into CF-40 dispatch expecting the simplified `exp(-m/T)` Boltzmann factor in the threshold band m/T ∈ [0.2, 5] would be a defensible approximation — the canonical PDG g_*(T) tabulations are smooth, the model's structural form (lattice-QCD shape + Boltzmann threshold-suppression) looked sound. Mack's FAIL diagnosis was crisp: at T = 100 GeV, W±/Z/H/top in the threshold band contribute exp(-m/T) ≈ 0.18-0.45 instead of canonical full-relativistic 1.0 in the proper Bose-Einstein/Fermi-Dirac integrated form `g_*_eff = (15/π⁴) ∫ x²√(x²+(m/T)²) / (exp(√(x²+(m/T)²))±1) dx`; total shortfall ~14 dof at T=100 GeV alone (WP §W4-4 *Structural diagnosis* lines 467-473). The simplified approximation systematically UNDER-counts active dof in the threshold band. The refinement pathway is a single 1.0-we gate (replace `boltzmann_factor()` helper with `scipy.integrate.quad` on Eq.3.62). Mack also correctly REFUSED to promote g_star_BS_T_H = 9.4083 to canonical_constants.py despite producing it as a candidate, citing Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention — the kind of source-discipline I'd hoped to see and got.

**(5) CF-39 mechanical closure as orchestrator-authored cascade closure — `mechanical-closure-discipline.md` 5-clause admissibility ALL PASSed in-session, structurally validating the rule (Structural-methodological surprise).**
The CF-40 FAIL gave me a choice: dispatch Mack for CF-39 with the FAIL'd g_star_BS_T_H = 9.4083 input (would have produced a doomed FAIL-cascade INFO degradation per plan §11) OR mechanical closure per `mechanical-closure-discipline.md` (no Mack dispatch, no Option A supersedes-tag emission, no S88 retroactive edit). The 5-clause admissibility test all PASSed (WP §W4-3 *Closure admissibility checklist* lines 419-426): upstream-block topology ✓, verdict honesty FAIL ✓, per-gate-distinct audit_sha256 via embed_keys ✓, descriptive value field naming CF-40 FAIL + g_star_BS_T_H candidate + Option A target ✓, in-script WP coupling deferred to next task ✓. The structural meaning: the rule's pattern matched the situation cleanly. The closure preserved (a) S88 verdict permanence (no retroactive edit), (b) audit-trail transparency (the value field documents the prereq-block), (c) S91+ refinement path (Option A supersedes-tag emission DEFERRED, not foreclosed). This is the rule's calibration corpus instance #2 (after the original calibration in W3 6/6 PRE-REG-INC closure cited at the rule's provenance line). Quietly satisfying.

### Cross-gate patterns

**(P1) CF-37 + CF-40: both close at approximation-layer; both identify refinement pathways for S91+; substrate physics intact in both.**
CF-37 closes the (d)∘(b) compositional primary corridor at PROXY-REFINEMENT-PENDING level (Wedderburn-rank-ratio χ'_weight = 0.5 + dimensional bridge structural ansatz); CF-40 closes the simplified `exp(-m/T)` Boltzmann factor approximation at the species-multiplicity layer. Neither closure refutes substrate physics — both identify approximation-layer choices that produced FAIL at honest pre-registered thresholds, and both name explicit refinement pathways: CF-37 → FULL CM-1995 §III.4 finite-spectral-triple residue formula evaluation (~3.5 we); CF-40 → Kolb-Turner Eq.3.62 FD/BE integrated forms (~1.0 we). The pattern: when the substrate computation is structurally well-defined but its operational evaluation uses an approximation, the FAIL is at the approximation layer not at the substrate layer. CF-37 carries the explicit `PROXY-REFINEMENT-PENDING` convention tag per `cross-pillar-bridge-anatomy.md §"deferred-pending"`; CF-40 doesn't carry the same tag (different rule scope — particle-physics anchor refinement, not cross-pillar bridge), but the structural class is identical. This pattern is worth noting for S91+ planning: prefer dispatching the FULL-evaluation refinements EARLY in the next session, since they could revise multiple downstream verdicts at once (CF-37 PASS would land calibration corpus instance #2 at Cell-I; CF-40 PASS would unblock CF-39 + g_star_BS_T_H promotion + Option A supersedes-tag emission).

**(P2) CF-39 + CF-40 cascade demonstrates 3-rule integration: `mechanical-closure-discipline.md` + `gate-verdicts.md §"Option A"` + `epistemic-discipline.md §"Source Reconciliation"` Class-(b).**
CF-40 FAIL → CF-39 mechanical closure → Option A supersedes-tag emission DEFERRED → S88 verdict file UNCHANGED → g_star_BS_T_H NOT promoted. Three rule files interact, each with a distinct role: `mechanical-closure-discipline.md` governs the closure pathway (no Mack dispatch, descriptive value field, in-script WP coupling); `gate-verdicts.md §"Option A"` clause 5 specifies that supersedes tags only fire on CORRECTIVE PASS lines (not on FAIL/PRE-REG-INC closures), so the S88-CF-CURV-16 chain is undisturbed; `epistemic-discipline.md §"Source Reconciliation"` Class-(b) PIN-LOOSE-SOURCE-TIGHT prevention forbids canonical promotion of FAIL'd values, so g_star_BS_T_H stays out of canonical_constants.py until refined CF-40 PASSes. All three rules PASS structurally; all three protect downstream consumers from bad data. The pattern: rule files compose. The wave's structural rigor is not just the gate verdicts but the COMPOSITION of multiple discipline rules that produce the right cascade outcomes without manual intervention.

**(P3) The wave's only PASS (CF-41) used a substrate-cardinality lever; the wave's two physics-FAILs (CF-37, CF-40) used corridor / approximation-choice levers.**
CF-37 attempted to refine the LRD α-anchor by varying the COMPOSITIONAL CORRIDOR ((d)∘(b) instead of (a)) on the same L=10 substrate; FAIL. CF-40 attempted to refine the species-multiplicity g_*(T) by varying the THRESHOLD-SUPPRESSION FORM (Boltzmann band vs PDG canonical) on the same SM particle content; FAIL. CF-41 attempted to refine the §W1-4 PBH band-edge prediction by SCALING UP THE SUBSTRATE TRUNCATION (L=10 → L=12) on the same substrate-clock-cancellation factorization; PASS. The pattern is structurally suggestive: the substrate's truncation level may be a more reliable lever than the corridor / approximation-form choices, at least at this scale. This ISN'T a generalizable claim from a sample of 3 — it's an observation worth tracking. If CF-S91-CF40-KOLB-TURNER PASSes at S91+ (refined approximation form does work), the pattern is partially refuted (approximation-choice CAN work when the form is canonical not simplified). If it FAILs again, the pattern strengthens (approximation-form is a slippery lever).

### Highlights for next session

**(1) CF-S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED — replace simplified `exp(-m/T)` with Kolb-Turner Eq.3.62 integrated form on CF-40's species-multiplicity model.** Why it matters: single ~1.0-we gate that unblocks 3 downstream items (CF-39 substantive dispatch, g_star_BS_T_H canonical promotion, Option A supersedes-tag emission to S88-CF-CURV-16-U1-BBN-CHUNKY-HAWKING-METALLICITY chain). Effort class: LIGHT (replace 1 helper function + scipy.quad integration; re-test at 3 PDG anchors). Expected outcome: PASS at 3-anchor 10% RATIO band unblocks the CF-39 cascade; FAIL would mean even the canonical FD/BE integrated form misses by > 10% at PDG anchors, suggesting deeper substrate-cascade-form scrutiny (S88 W6 §V.5 itself would need re-examination). EVOI HIGH — narrow gate with broad downstream effect.

**(2) CF-S91-CF37-AUX-4-SECONDARY-CORRIDOR — activate (c)∘(d) modified-universal-kernel γ(s) ≠ Γ(s) corridor for LRD α-anchor.** Why it matters: directly addresses the LRD α-anchor question after (d)∘(b) closure at PROXY-REFINEMENT-PENDING; the W-1 workshop pre-registered (c)∘(d) as the structurally correct next candidate. Effort class: HEAVY (~3.5 we; equivalent to CF-37 substantive evaluation). Expected outcome: PASS at 30% RATIO band against 1/458 opens (c)∘(d) as the canonical LRD α-anchor candidate with substrate-derived provenance; FAIL closes (c)∘(d) and forces a third-corridor enumeration at S92+. EVOI HIGH — addresses a load-bearing observational anchor with two-corridor outcome resolution.

**(3) CF-S91-CF37-FULL-CM1995-RESIDUE — replace the Wedderburn-rank-ratio + dimensional-bridge structural ansatz in CF-37 with FULL Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula.** Why it matters: the CF-37 PROXY-REFINEMENT-PENDING tag explicitly anticipates this gate; it could revise (d)∘(b) corridor closure if the FULL χ'_weight differs from 0.5 in the direction of empirical 1/458 by ~4.5×. Effort class: HEAVY (~3.5 we). Expected outcome: PASS revises CF-37 to PASS at FULL-CM1995 layer (lands calibration corpus instance #2 at Cell-I); FAIL confirms (d)∘(b) closure structurally (sharpens the case for (c)∘(d) secondary corridor). EVOI MEDIUM-HIGH — substantive answer either way, but structurally interesting only if FULL ≠ 0.5 by a large factor; the structural-ansatz choice is defensible. Could be queued in PARALLEL with CF-S91-CF37-AUX-4 since they're alternative LRD α-anchor pathways.

**(4) CF-S91-CF41-VII-LANDING — land STAGE-1-CANDIDATE registry entry for PBH-band-edge-conjunct prediction `n_PBH = 8.033e-23 m⁻³` at L_max=12 + Option A canonical.** Why it matters: preserves the wave's only PASS as a registry-permanent landing target; mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`; completes the substrate-IS Level-1 calibration corpus instance for cardinality-layer observables per `phononic-framing.md §"Single-τ-slice vs moduli-deformation substrate-IS levels"`. Effort class: LIGHT (~0.3 we; registry-text landing). Expected outcome: PASS lands the entry with 5 IS-not-IN anatomy elements + 3-level ladder (if cross-pillar) or standard §VII STAGE-1-CANDIDATE template; per `joint-theorem-promotion.md` Stage-2 cross-axis verify follows on PASS. EVOI MEDIUM — preserves the wave's structural anchor; Stage-2 verify pathway opens registry-permanent promotion.

**(5) CF-S91-CF41-UPPER-22.6-EXTENSION — reach upper-22.6%-conjunct sub-band [1.83e-22, 2.2e-22] m⁻³.** Why it matters: sharpens the §W1-4 PBH band-edge promotion from "broader region inclusion" to "narrower sub-band inclusion"; aligns with §W1c-69 PASS-magnitude posterior right-edge; pathway (a) L_max=12 → L_max=14 substrate refinement is the structurally cleanest (binomial form scales as N_eigs² which compounds further). Effort class: MODERATE (~1.5 we; pathway (a) requires extending substrate cache to L=14 via additional Casimir-projection construction OR Friedrich-Bär saturation analytic bound). Expected outcome: PASS reaches the upper-22.6%-conjunct sub-band, sharpening the §W1-4 promotion further; FAIL would mean even L=14 substrate refinement insufficient, suggesting that the cascade-tail-mass-distribution refinement (Option D quadratic correction beyond Options B/C) is the necessary lever. EVOI MEDIUM — sharpens the wave's only PASS; structurally informative on the cardinality-vs-corridor lever question identified in Cross-gate Pattern P3.

### Wave 4 signature

**"Approximation walls, cardinality opens."**

Wave 4 produced a structural dichotomy: two approximation-layer FAILs (CF-37 (d)∘(b) corridor closure at PROXY-REFINEMENT-PENDING + CF-40 simplified Boltzmann factor closure) and one substrate-cardinality PASS (CF-41 §W1-4 promotion via L=10 → L=12 binomial cardinality compounding). The approximation-layer choices walled the corridors; the substrate-truncation lever opened the band-edge. CF-38 documented the absence of a registry promotion (no substrate-physics implication); CF-39 closed mechanically per the cascade-closure rule (orchestrator-authored, audit-trail-preserving). The wave's structural-methodological signature is the in-session validation of `mechanical-closure-discipline.md` at calibration corpus instance #2 — the rule's pattern matched the CF-40-FAIL-induced cascade situation cleanly. The wave is constraint-map-advancing, not framework-confirming: each FAIL is structurally meaningful corridor-elimination + refinement-pathway-identification at honest pre-registered thresholds; the one PASS is a substrate-cardinality refinement that LOCATES (not proves) the §W1-4 PBH band-edge prediction within the broader target region. The wave does NOT close the LRD α-anchor question; it sharpens the case for the (c)∘(d) secondary corridor at S91+ AUX-4 + the FULL CM-1995 §III.4 evaluation as the deferred-pending fallback that could revisit (d)∘(b).

---
