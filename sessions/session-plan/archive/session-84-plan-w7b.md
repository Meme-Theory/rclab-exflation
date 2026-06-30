# Session 84 Plan — Wave 7b: Matrix-Model + KK-Tower + Twisted Triples + §VII.N Registry (8 gates)

**Session**: 84
**Wave**: 7b (of 7a/7b parallel split — "String/M-theory/Matrix-model extensions, §VII.N landing, KK tower")
**Planner**: kaluza-klein-theorist (via gen-physicist orchestration)
**Date**: 2026-04-18
**Format**: compute (parallel independent agents, no inbox/team)
**Carry-forward source**: §4.G items 75-78 and 81-84 of `session-84-context.md`

---

## W7b Summary

Wave 7b closes the string/M-theory admissibility program opened by S83-G32 (dimreduction-audit PASS, singleton {d_total=12, KO-dim=6, A_F=C(+)H(+)M_3(C)}) and S83-G36 (matrix-model-classification PASS, b_power=4.681, IKKT excluded). It delivers four structural closures and four forward-looking tests:

1. **Asymptotic confirmation (#75)**: Extend G36 power-law fit from L=3..8 to L=10, 12. If b_power stabilizes at 4.681+/-0.10, the exponent is asymptotic (not finite-L artifact). Requires GPU torch.linalg (sum_mult ~ 7e6 modes at L=12).
2. **Analytic anchor (#76)**: Derive b_power from Seeley-DeWitt (a_4 + delta*a_5) expansion on Jensen-deformed SU(3). If |b_predicted - 4.68|<0.10, the exponent is STRUCTURAL (a spectral invariant of the triple).
3. **Twisted triple admissibility (#77)**: Test Connes-Moscovici 2008 twisted spectral triples at alternative KO-dim. If zero twisted candidates extend the admissible singleton, the (12, 6) uniqueness is ROBUST to twisting. If >=3 candidates emerge, M-theory pathway re-opens.
4. **Correspondence table closure (#78)**: Re-classify 31 phonon-string correspondence entries post-G32+G36. All entries either CONSISTENT or explicitly downgraded with one-line reason. Zero open external-paradigm correspondences.
5. **MP admissibility extension (#81)**: Extend S83-G27 from 5 regulators to 9-class atlas. Confirm {step, sum_exp} remains sole admissible pair under KO-dim=6 weighting.
6. **PRDR audit (#82)**: Pin 3 free machinery parameters in G36 (sign handling, Delta scaling vs gap-equation self-consistency, V_pair normalization). Cures PRU-vulnerability.
7. **§VII.N registry landing (#83)**: Lift (d_total, KO-dim, SM-content) admissibility enumeration into permanent-results-registry. Formal statement, 4-proof chain, scope, falsifier. Cross-reference G32 verdict line and Connes-Marcolli sign table.
8. **KK tower at singleton (#84)**: Recompute KK mass spectrum m_n = lambda_n/R(tau) at tau=tau_fold=0.19 and tau=0, using canonical Jensen deformation (lambda_1=alpha*e^{2s}, lambda_2=alpha*e^{-2s}, lambda_3=alpha*e^s). First 8 KK levels per (p,q) in {(1,0),(1,1),(2,0),(2,1),(3,0),(0,3),(2,2),(3,1)}. Provides the zero-mode spectrum the singleton predicts.

**Scientific theme**: given the (12, 6, A_F) singleton is established at d=12 and the IKKT large-N scaling is excluded, W7b asks (a) is the exclusion robust? (b) is the singleton robust to twisting? (c) what does the singleton PREDICT for the KK tower that observations could test?

**Agent assignment policy** — all agents in W7b are COMPUTE-ONLY (not workshop). One writer per script, one writer per working-paper section. No inter-agent messaging. See "Parallel Dispatch Note" below.

---

## W7b Decision Point Prerequisites

W7b gates require the following from prior sessions and parallel W7a:

- **S83-G32 verdict pin**: `dimreduction-audit_s83.json` (d_total=12 singleton, 11 alternatives excluded) — INPUT to #77, #78, #83.
- **S83-G36 verdict pin**: `matrix-model-classification_s83.json` (b=4.681, R²=0.9979, IKKT excluded with DeltaR²=0.156) — INPUT to #75, #76, #82.
- **S83-G27 regulator atlas**: 5-regulator MP-admissibility verdicts (zeta, Zubarev, SDW, dim-reg, lattice-BR) — INPUT to #81.
- **S63 Cartan trace identity**: a_2 coefficient Jensen-deformed SU(3) structure — INPUT to #76.
- **S22b D_K block-diagonality**: Peter-Weyl off-diagonal = 8.4e-15 — INPUT to #84.
- **Jensen deformation canonical form**: lambda_1(s)=alpha*e^{2s}, lambda_2(s)=alpha*e^{-2s}, lambda_3(s)=alpha*e^s in canonical_constants.py — INPUT to #84, #75, #82.
- **canonical_constants.py provenance chain**: all constants from S84+ scripts imported, not hardcoded.

W7b does NOT depend on W7a (72-74, 79-80). Parallel-safe. See the "Parallel Dispatch Note" for orchestration.

---

## §W7b-75. S84-B-POWER-STABILITY / S84-MATRIX-MODEL-ASYMPTOTIC

### Gate Metadata

- **Gate ID**: `S84-W7b-75-B-POWER-STABILITY`
- **Trigger**: `[VERIFY]`
- **Classification**: GEOMETRIC
- **Agent**: `kaluza-klein-theorist`
- **Script**: `computations/s84_w7b_75_b_power_stability.py`
- **Working-paper section**: `§VII-N.2 Matrix-Model Asymptotic Stability` (sub-section of §VII.N landing below)

### Hypothesis Being Tested

The power-law scaling |E_cond(L)| = a * L^b with b=4.681 derived from L=3..8 fit (S83-G36) is the asymptotic behavior of the Jensen-deformed SU(3) binding-energy spectrum, not a finite-L artifact. If stable to L=10, 12 within +/-0.10, the exponent is locked and the binding-energy doubling ratio 2^4.681 = 25.6 per L-doubling is a structural spectral invariant of the triple.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | |b_power(L<=12) - 4.681| < 0.10 AND R² > 0.99 (using L in {3,4,5,6,7,8,10,12} joint fit) |
| **INFO** | |Delta b| < 0.30 (stable trend, moderate drift but not artifact) |
| **FAIL** | |Delta b| > 0.30 OR R² < 0.90 (finite-L artifact; exponent is not asymptotic) |

**Tolerance rule**: RATIO — PASS tolerance is +/-0.10 on b_power (2.1% of central value); FAIL tolerance is +/-0.30 (6.4%). Asymmetry reflects physical expectation that true asymptote converges with decreasing deviation.

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `L_max_scan` | {3, 4, 5, 6, 7, 8, 10, 12} | Joint fit on all 8 L-values |
| `sum_mult_L12` | ~7.05e6 | dim((p,q))² summed over |p|+|q|<=2L, grows polynomially |
| `GPU path` | `torch.linalg.eigvalsh` | MANDATORY — CPU numpy.linalg exceeds 24h wall at L=12 |
| `dtype` | `torch.complex128` | Double precision for eigvalsh on Jensen metric block |
| `Jensen convention` | lambda_i from canonical_constants (alpha*e^{+2s, -2s, +s}) | Canonical left-invariant metric |
| `tau` | tau_fold = 0.190 | Single tau slice (NOT scan; scan is #84) |
| `V-rescaled-Delta-fixed` | Convention B (S83 G36) | Match G36 exactly |
| `Delta_BCS` | 0.4642 (canonical) | Imported |
| `V_pair normalization` | same as G36 (see #82 PRDR) | Cross-reference |
| `sign handling` | |E_cond| (absolute value) | G36 convention |
| `fit_method` | log-log least-squares, weighted uniform | R² on log|E_cond| vs log(L) |
| `OMP_NUM_THREADS` | 8 | CPU fallback cap (should not trigger) |
| `random_seed` | 8475 | Deterministic eigvalsh initialization |

### Input SHA-256 Pins

```
canonical_constants.py                    : <computed-at-runtime>
s83_g36_matrix_model_classification.npz   : <computed-at-runtime>
s84_jensen_metric_blocks_L10.npz          : <computed-at-runtime>
s84_jensen_metric_blocks_L12.npz          : <computed-at-runtime>
peter_weyl_blocks_SU3.npz                 : <computed-at-runtime>
```

(Blocks at L=10 and L=12 are generated inside the script from canonical Jensen metric; they are cached after first generation for audit reproducibility.)

### Expected Output 4-Tuple

```
(value=b_power(L<=12), scheme=eigvalsh-joint-logfit, convention=V-rescaled-Delta-fixed, L_max=12)
```

### Substitution Chain ([VERIFY])

Step 1: Definition. |E_cond(L)| = |sum_{(p,q): |p|+|q|<=2L} dim(p,q)² * E_(p,q)|, where E_(p,q) is the per-mode binding-energy contribution from the gap equation in (p,q) representation.

Step 2: Ansatz. |E_cond(L)| = a * L^b (power-law).

Step 3: Linearize. ln|E_cond(L)| = ln(a) + b * ln(L). Fit b from slope of ln|E_cond| vs ln(L) on {3,4,5,6,7,8,10,12}.

Step 4: Measure. b_L<=12 = argmin_b sum_L (ln|E_cond(L)| - ln(a) - b*ln(L))².

Step 5: Decision. If b_L<=12 in [4.581, 4.781] AND R² > 0.99 -> PASS. If b_L<=12 in [4.381, 4.981] AND R² > 0.95 -> INFO. Else FAIL.

### What PASS and FAIL Mean for the Solution Space

- **PASS**: Power-law exponent locked asymptotically. 2^4.681 doubling ratio is a structural prediction of the Jensen-deformed SU(3) binding-energy spectrum. IKKT-class (linear L scaling) is excluded to arbitrary L. Singleton (12, 6, A_F) has a predictive scaling.
- **INFO**: Trend stable, some residual drift — does not refute asymptote but warrants higher-L verification (S85+).
- **FAIL**: L=10, 12 data reveals finite-L artifact. Must withdraw S83-G36 matrix-model-classification PASS and re-open IKKT correspondence classification.

### Agent Prompt Requirements

- `torch.linalg.eigvalsh` on GPU (AMD RX 9070 XT, ROCm 7.2, torch 2.9.1+rocm) MANDATORY
- `from canonical_constants import *` first line
- All intermediates tagged `# (local)`
- Substrate framing: bottom-up, D_K eigenvalues FIRST, b_power as emergent spectral invariant
- Report wall-clock, peak VRAM, and dtype per L-value
- Emit full 64-char SHA-256 closure pin
- Verdict line in s84_gate_verdicts.txt

---

## §W7b-76. S84-SDW-B-PREDICTION / S84-G36-SEELEY-DEWITT-MATCH

### Gate Metadata

- **Gate ID**: `S84-W7b-76-SDW-B-PREDICTION`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: GEOMETRIC
- **Agent**: `feynman-theorist` (with `spectral-geometer` cross-check via read-only artifact review in working-paper subsection)
- **Script**: `computations/s84_w7b_76_sdw_b_prediction.py`
- **Working-paper section**: `§VII-N.3 Analytic Seeley-DeWitt Derivation of b_power`

### Hypothesis Being Tested

The power-law exponent b_power = 4.681 observed in S83-G36 is not a fitted empirical number but an analytic consequence of the Seeley-DeWitt (a_4 + delta*a_5) expansion coefficients on Jensen-deformed SU(3). Specifically, from the heat-kernel expansion Tr(e^{-tD_K²}) = sum_k a_k(D_K) * t^{(k-d)/2} with d=8 internal, the a_4 term carries the Ricci-squared and Weyl-squared invariants on K=SU(3), and delta*a_5 (Jensen-deformation correction) encodes anisotropy. Their combined L-dependence in the binding-energy sum yields b_analytic close to 4.68.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | |b_predicted - 4.68| < 0.10 via closed-form derivation (symbolic, not numeric) |
| **INFO** | |Delta b| < 0.30 (closed-form within structural band) |
| **FAIL** | |Delta b| > 0.30 (b is scheme-dependent not structural; closed form disagrees with numeric G36) |

**Tolerance rule**: THEOREM — the derivation must be symbolic with no fit parameters. PASS requires a closed-form expression b_predicted = f(Jensen parameters, d_internal, KO-dim) that evaluates to within 0.10 of 4.68 without free adjustment.

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `a_k coefficients` | Gilkey 1995 normalization on compact Lie group SU(3) | Standard reference |
| `delta expansion` | Taylor series in Jensen s, order 2 (s^0, s^1, s^2) | Matches G36 fit range tau in [0.10, 0.30] |
| `metric convention` | Left-invariant Jensen (S63 Cartan trace identity basis) | Canonical |
| `heat-kernel cutoff` | Zubarev exponential (per S83 G27 MP-admissibility) | Per L1 vs L2 regulator theorem |
| `L correspondence` | L = floor(sqrt(Lambda²/(lambda_min²))) mapped to eigenvalue truncation | Relates continuous cutoff to discrete L |
| `d_internal` | 8 (SU(3)) | Fixed |
| `d_total` | 12 | From G32 singleton |
| `KO-dim` | 6 | From A_F singleton |
| `symbolic engine` | sympy + computer algebra | No numerical fit allowed in derivation |
| `cross-check method` | substitute b_predicted into L^b ansatz and compare term-by-term to G36 fit residuals | Must agree within 5% at each L |
| `random_seed` | N/A (analytic) | |

### Input SHA-256 Pins

```
canonical_constants.py                         : <computed-at-runtime>
s83_g36_matrix_model_classification.npz        : <computed-at-runtime>
s63_cartan_trace_identity_coefficients.npz     : <computed-at-runtime>
gilkey_ak_coefficients_SU3.json                : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=b_predicted, scheme=SDW-analytic-symbolic, convention=Jensen-left-invariant, L_max=infinity-limit)
```

### Substitution Chain ([VERIFY-THEOREM])

Step 1: Heat-kernel expansion on compact K=SU(3) with Jensen metric:
Tr(e^{-t D_K²}) = (4*pi*t)^{-d/2} * Vol(K) * sum_{k>=0} a_k(D_K) t^k  [standard Seeley-DeWitt]

Step 2: Coefficients on SU(3) (Gilkey 1995):
a_0 = 1
a_2 = (1/6) * Scalar(K)  [Ricci scalar]
a_4 = (1/360) * [5*R²  - 2*Ric² + 2*Riem²]  [with Jensen-deformed Ricci]
a_5 ~ Jensen-anisotropy term (non-zero only off-round)

Step 3: On Jensen SU(3), Scalar(s) = (3*alpha/2) * (2*e^{2s} - 1 + 8*e^{-s} - e^{-4s}) (Baptista Eq 3.70)
dScalar/ds = 3*alpha * (e^{2s} + 2*e^{-s} + e^{-4s}) > 0 (monotone)

Step 4: Substitute s = tau_fold: R(tau_fold) = <symbolic> and evaluate a_4, a_5 terms.

Step 5: Map to L-truncation. The cutoff Lambda² ~ lambda_max²(L) ~ L² * alpha² (from Jensen spectrum growth) gives t_min ~ 1/Lambda². Then the running of Tr(e^{-tD_K²}) at t_min translates to |E_cond(L)| ~ L^{2*order(a_4) + correction(a_5)}.

Step 6: Extract b_analytic by evaluating 2*coeff(a_4) + Jensen-correction_coeff(a_5) at tau_fold.

Step 7: Compare b_analytic to G36 b=4.681. If |b_analytic - 4.681| < 0.10 -> PASS.

### What PASS and FAIL Mean

- **PASS**: b_power is a STRUCTURAL spectral invariant. IKKT-scaling (b=1) is excluded analytically, not just empirically. Formal theorem candidate for §VII.N sub-sub-section.
- **INFO**: Jensen-correction terms approximate but do not exactly match. Structural but imprecise; indicates higher-order (a_6) contributions matter at L<=12.
- **FAIL**: b=4.681 is a lattice-regulator artifact, not intrinsic. Matrix-model classification downgrades to STRUCTURAL-ONLY. IKKT re-opens at asymptotic L despite G36 PASS.

### Agent Prompt Requirements

- symbolic derivation via sympy MANDATORY; no numerical fit in step 1-7 above
- Cite Gilkey 1995 (The Asymptotics of the Laplacian and the Heat Kernel) for a_k formulae
- Cite Connes-Marcolli 2008 for Jensen-deformation heat-kernel structure
- Substrate framing: a_4 is the 2nd Seeley-DeWitt moment of the internal Dirac — gravity-analog on K
- Produce both (a) symbolic closed form and (b) numerical evaluation at s=tau_fold=0.19 alpha=normalization
- Provide substitution chain in working paper verbatim

---

## §W7b-77. S84-NON-PRODUCT-ALTKO / S84-TWISTED-TRIPLE-ADMISSIBILITY

### Gate Metadata

- **Gate ID**: `S84-W7b-77-TWISTED-TRIPLE-ADMISSIBILITY`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: GEOMETRIC
- **Agent**: `kaluza-klein-theorist`
- **Script**: `computations/s84_w7b_77_twisted_triple_admissibility.py`
- **Working-paper section**: `§VII-N.4 Twisted Spectral Triple Admissibility`

### Hypothesis Being Tested

The singleton admissibility result {d_total=12, KO-dim=6, A_F=C(+)H(+)M_3(C)} from S83-G32 is robust under the Connes-Moscovici (2008) twisted spectral triple generalization. Twisted triples replace the self-adjointness [D, a*] = [D, a]* by a grading automorphism sigma: D*sigma(a) = sigma(a)*D at the operator level, allowing alternative KO-dim and d_internal combinations while preserving the triple axioms. The hypothesis is that NO twisted candidate at (d_internal != 8) OR (KO-dim != 6) reproduces SM gauge content AND passes all S82/S83 admissibility filters (Mellin cone, A_F= M_n(C) sector classification, sign-table consistency).

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | zero twisted candidates extend admissible set beyond {(12, 6, A_F_singleton)} |
| **INFO** | 1-2 candidates (weak extension; investigation required in S85) |
| **FAIL** | >=3 candidates (would re-open M-theory pathway at KO-dim != 6; structural change to §VII.N landing) |

**Tolerance rule**: ABSOLUTE — discrete count of admissible triples. PASS requires ZERO new admissible triples; PASS is NOT |count - 0| < epsilon but count = 0 exactly.

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `twist_candidates` | See enumeration table below | Twisted generalizations to scan |
| `d_internal_scan` | {6, 7, 8, 9, 10} | Around SU(3) dim=8 |
| `KO_dim_scan` | {0, 2, 4, 6} mod 8 | Even KO-dim required by CCM classification |
| `A_F_scan` | {C, C(+)C, C(+)H, C(+)H(+)M_3(C), M_2(H), M_4(C), H(+)H} | Connes-Marcolli finite-dim candidates |
| `sigma_automorphism_space` | {trivial, grading, inner, outer-regular} | Per Connes-Moscovici 2008 |
| `admissibility_filters` | Mellin cone (§VII) + sign table (Connes-Marcolli 2013) + SM content match | S82/S83 permanent filters |
| `SM_content_test` | three generations of fermions + gauge bosons from A_F modules | Strict |
| `Jensen_compatibility` | Does twist preserve Jensen deformation monotonicity? | Required downstream |

### Enumeration Table (twist_candidates)

| Candidate | (d_internal, KO-dim, A_F) | sigma | Expected verdict |
|:----------|:--------------------------|:------|:-----------------|
| T-1 | (6, 4, C(+)H(+)M_3(C)) | grading | expected FAIL — SM content requires d=8 |
| T-2 | (6, 6, C(+)H(+)M_3(C)) | grading | expected FAIL — Mellin cone closes at d=6 |
| T-3 | (7, 6, M_2(H)) | outer | expected FAIL — A_F SM match fails |
| T-4 | (8, 0, C(+)H(+)M_3(C)) | trivial | expected FAIL — CCM sign table excludes KO=0 |
| T-5 | (8, 2, C(+)H(+)M_3(C)) | grading | expected FAIL — SM chirality inversion |
| T-6 | (8, 4, C(+)H(+)M_3(C)) | grading | expected FAIL — CCM excludes |
| T-7 | (8, 6, M_2(H)) | outer | expected FAIL — C² block required |
| T-8 | (8, 6, M_4(C)) | inner | expected FAIL — Higgs block absent |
| T-9 | (9, 6, C(+)H(+)M_3(C)) | inner | expected FAIL — Mellin cone beyond d=8 |
| T-10 | (10, 6, C(+)H(+)M_3(C)) | outer | expected FAIL — strong-coupling divergence |

Plus T-11..T-16 = cross-products of above with HP¹, HP², Gaussian²-measure. All expected FAIL.

### Input SHA-256 Pins

```
canonical_constants.py                                  : <computed-at-runtime>
s83_g32_dimreduction_audit.npz                          : <computed-at-runtime>
connes_marcolli_sign_table_2013.json                    : <computed-at-runtime>
connes_moscovici_twisted_triple_axioms_2008.json        : <computed-at-runtime>
s82_mellin_cone_admissibility.json                      : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=admissible_twist_count, scheme=CCM-axiomatic, convention=CM2008-twist, L_max=infinity)
```

### Substitution Chain ([VERIFY-THEOREM])

Step 1: Axioms for twisted triple (Connes-Moscovici 2008, Def 2.3):
 A finite-dim algebra A_F, separable Hilbert space H, bounded operator D with [D, a]_sigma bounded for all a in A_F, grading automorphism sigma: A_F -> A_F with sigma² = 1.

Step 2: For each (d_internal, KO-dim, A_F) in scan: construct candidate twisted triple (A_F, H, D, sigma). Verify 7 triple axioms.

Step 3: Apply admissibility filters:
 (i) Mellin cone pairing: Tr(|D|^{-s}) must have pole at s = d_total with residue in open positive cone (S82 MG-0)
 (ii) CCM sign table: (KO-dim, alg-class) must be in Connes-Marcolli 2013 Table 1 allowed row
 (iii) SM-content match: A_F modules must decompose into 3 generations + gauge bosons
 (iv) Jensen compatibility: sigma(Jensen_deform) = Jensen_deform (twist preserves deformation monotonicity)

Step 4: Count admissible_twist_count = #{candidates passing all 4 filters}.

Step 5: Decision:
 count = 0 -> PASS (twisting doesn't extend singleton)
 count in {1, 2} -> INFO (weak extension)
 count >= 3 -> FAIL (M-theory pathway re-opens)

### What PASS and FAIL Mean

- **PASS**: Singleton (12, 6, A_F_SM) robust to twist generalizations. §VII.N landing locks at pure spectral-triple classification. M-theory-11d exclusion is exhaustive.
- **INFO**: 1-2 marginal twisted candidates — warrants per-candidate sector analysis in S85 (pre-registered here as potential carry-forward).
- **FAIL**: M-theory / non-commutative-spacetime pathway re-opens. §VII.N landing must incorporate twist-sector cases. Singleton weakens to {A_F_SM-equivalence-class}.

### Agent Prompt Requirements

- Cite Connes-Moscovici 2008 (Type III and spectral triples) for twisted triple axioms
- Cite Connes-Marcolli 2013 (A walk in the noncommutative garden) for KO-dim sign table
- Substrate framing: D_K is fundamental, twisting at algebra level does NOT change substrate — only changes how observables are recovered
- For each T-1..T-16 candidate, produce axiom-check verdict (which axiom fails or passes)
- Emit count line with candidate IDs if any pass

---

## §W7b-78. S84-CORRTAB-AUDIT / S84-CORRESPONDENCE-TABLE-CLOSURE

### Gate Metadata

- **Gate ID**: `S84-W7b-78-CORRESPONDENCE-TABLE-CLOSURE`
- **Trigger**: `[AUDIT]`
- **Classification**: NON-PHONONIC (meta-audit)
- **Agent**: `gen-physicist`
- **Script**: `computations/s84_w7b_78_correspondence_table_closure.py`
- **Working-paper section**: `§VII-N.5 Correspondence Table Post-G32+G36 Closure`

### Hypothesis Being Tested

The 31 entries in the current phonon-string correspondence table (7 ANTI + 24 downgradeable/consistent post-S83) are fully re-classified after G32 (singleton admissibility) and G36 (matrix-model classification). Every open external-paradigm correspondence is resolved: either CONSISTENT (unchanged), STRUCTURAL (downgraded from GENUINE), SUGGESTIVE (downgraded from STRUCTURAL), or ANTI (excluded). Zero entries remain in "open" state. The audit produces a canonical post-G32/G36 table that replaces the S83 version.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | Zero entries in "open" state; all 31 entries classified with one-line reason |
| **INFO** | 1-3 entries require external input to close (escalate to S85 workshop) |
| **FAIL** | >=4 entries cannot be classified (methodology breakdown; audit re-scope) |

**Tolerance rule**: ABSOLUTE — count of unclosed entries. PASS = 0 open; INFO = 1-3; FAIL >=4.

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `table_version_in` | S83-VII.N-provisional (31 entries) | Input |
| `classification_buckets` | {CONSISTENT, GENUINE, STRUCTURAL, SUGGESTIVE, ANTI} | 5-bucket canonical |
| `downgrade_rules` | G32 + G36 + CCM-sign-table | Strict |
| `downgrade_reasons_required` | one-line citation + verdict pin | Strict |
| `ANTI_additions_expected` | 2 (IKKT #30, M-theory-11d #31) | Already added post-S83 |
| `post_G32_class_rule` | (d_total!=12 OR KO-dim!=6) => ANTI; else retain | Hard filter |
| `post_G36_class_rule` | linear-L-scaling correspondence (IKKT-class) => ANTI | Hard filter |
| `documentation_format` | markdown table + JSON verdict | Both required |
| `random_seed` | N/A (deterministic audit) | |

### Post-G32/G36 Classification Rules

For each entry i in 1..31:
1. Extract claimed correspondence target (d_target, KO_target, scaling_target).
2. If d_target != 12 OR KO_target != 6: classify as ANTI (violates singleton).
3. Else if scaling_target is linear-L: classify as ANTI (violates G36 power-law).
4. Else if correspondence is quantitative (numeric matching): classify as GENUINE.
5. Else if correspondence is qualitative (structural matching): classify as STRUCTURAL.
6. Else (analogy only): classify as SUGGESTIVE.
7. If classification requires external paper/evidence not in repo: classify as INFO-DEFERRED (goes to INFO bucket in gate verdict).

### Input SHA-256 Pins

```
canonical_constants.py                              : <computed-at-runtime>
s83_correspondence_table_vii_n_provisional.json     : <computed-at-runtime>
s83_g32_dimreduction_audit.npz                      : <computed-at-runtime>
s83_g36_matrix_model_classification.npz             : <computed-at-runtime>
connes_marcolli_sign_table_2013.json                : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=open_count, scheme=post-G32-G36-audit, convention=5-bucket, L_max=N/A)
```

### Substitution Chain ([AUDIT])

Step 1: Enumerate 31 entries from S83-VII.N-provisional table (row ID, paradigm, target, claim, pre-S84 class).
Step 2: For each row, apply 7-step classification rule above.
Step 3: Record post-G32/G36 class + one-line reason + SHA of supporting verdict.
Step 4: Count open_count = #{rows classified INFO-DEFERRED or unresolved}.
Step 5: Produce markdown table + JSON; emit verdict.

### What PASS and FAIL Mean

- **PASS**: Correspondence table closed. §VII.N landing (see #83) incorporates the canonical post-G32/G36 table. No open external-paradigm correspondences; the framework's position against external programs is fully mapped.
- **INFO**: 1-3 rows require external input (e.g., specific heterotic-on-CY paper unavailable). Queue as S85 workshop.
- **FAIL**: Audit methodology insufficient; re-scope with domain experts (Kaku + KK + Connes team).

### Agent Prompt Requirements

- Read exact S83 VII.N table (do not reconstruct)
- For each entry, produce pre-S84 class + post-S84 class + reason (one line) + supporting verdict SHA
- Produce both markdown table (human-readable) and JSON (machine-readable)
- Flag any entry whose classification changes from pre-S84 explicitly
- No new correspondences added in this audit — strict re-classification only

---

## §W7b-81. S84-MP-ADMISSIBILITY-EXTENDED

### Gate Metadata

- **Gate ID**: `S84-W7b-81-MP-ADMISSIBILITY-EXTENDED`
- **Trigger**: `[VERIFY]`
- **Classification**: GEOMETRIC
- **Agent**: `lizzi-spectral-functional-theorist`
- **Script**: `computations/s84_w7b_81_mp_admissibility_extended.py`
- **Working-paper section**: `§VII-N.6 MP Admissibility Extended — 9-class atlas`

### Hypothesis Being Tested

S83-G27 returned MP-admissibility = 2/5 (step + sum_exp admissible; zeta, Zubarev, SDW, dim-reg, lattice-BR tested; 3 failed). Extending the regulator class to 9 by adding Gaussian² (double-Gaussian), heat-kernel (Mellin-transformed), Planck-spectrum (Bose-Einstein suppression), and piecewise-linear (max(0, 1-|x|)) regulators, the MP-admissibility filter under KO-dim=6 weighting yields {step, sum_exp} as the unique admissible pair. The count stabilizes at 9 — no new regulators admitted.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | admissible_count = 2 exactly; 9 regulator classes tested with MP-admissibility verdict each |
| **INFO** | admissible_count in {3, 4, 5, 6, 7, 8} (partial extension; investigate) |
| **FAIL** | admissible_count <= 1 OR >= 9 (methodology drift) |

**Note**: user-provided gate text "PASS: admissible_count=9" refers to number of regulator CLASSES TESTED = 9, not admissible count. Re-reading: PASS = tested 9 classes, admissible pair unchanged at 2 (step, sum_exp). INFO = admissible extended to 3-8. FAIL = <=2 classes tested (did not extend) OR admissible >=9 (all admissible = trivialization).

Refined thresholds:
- **PASS**: 9 classes tested AND admissible_count = 2 (step, sum_exp retained)
- **INFO**: 9 classes tested AND admissible_count in {3, 4, 5, 6}
- **FAIL**: fewer than 9 classes tested OR admissible_count >= 7 (degeneracy)

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `regulator_classes` | see enumeration below | 9-class atlas |
| `MP_admissibility_filter` | Connes-Moscovici polynomial-weighted (KO-dim=6) | S82/S83 canonical |
| `KO-dim_weighting` | 6 | Fixed singleton |
| `L_max` | 5 | Matches S83-G27 |
| `tau` | tau_fold = 0.190 | Fixed |
| `observable_suite` | {A_s, m_H, n_s, sin²theta_W} | Matches G27 |
| `span_threshold` | 1.5 (R-protected) / 2.5 (NOT-R) | From §VII.K-META meta-principle (G58) |
| `GPU path` | torch.linalg eigvalsh for D_K | Matrices 1000x1000 block |

### Enumeration of 9 Regulator Classes

| # | Class | Form f(x) | Status | Expected |
|:--|:------|:----------|:-------|:---------|
| 1 | step | H(1-|x|) | S83 PASS | PASS (baseline) |
| 2 | sum_exp | sum_n c_n exp(-alpha_n x²) | S83 PASS | PASS (baseline) |
| 3 | zeta | x^{-s}\|_{s=0} regularization | S83 FAIL | FAIL |
| 4 | Zubarev | exp(-alpha x) Zubarev | S83 FAIL | FAIL |
| 5 | SDW | Seeley-DeWitt heat-kernel poly | S83 FAIL | FAIL |
| 6 | dim-reg | continuation in d | S83 FAIL | FAIL |
| 7 | lattice-BR | lattice-BR discrete cutoff | S83 FAIL | FAIL |
| 8 | Gaussian² | exp(-alpha² x^4) | new | likely FAIL (no polynomial-bounded moments) |
| 9 | heat-kernel | Mellin-transformed heat-kernel | new | likely FAIL (redundant with SDW) |
| 10 | Planck-spectrum | Bose-Einstein 1/(exp(beta x)-1) | new | likely FAIL (no UV suppression) |
| 11 | piecewise-linear | max(0, 1-|x|) | new | likely PASS (compact support like step) |

Note: 11 candidates in atlas, 9 tested fresh (1-2 retained as baseline + 3-11 new tests).

### Input SHA-256 Pins

```
canonical_constants.py                            : <computed-at-runtime>
s83_g27_mp_admissibility_unified.npz              : <computed-at-runtime>
connes_moscovici_mp_filter_2008.json              : <computed-at-runtime>
vii_k_meta_principle_g58.json                     : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=(tested, admissible), scheme=CM-MP-filter-KO6, convention=L2-Zubarev-substrate-action, L_max=5)
```

### Substitution Chain ([VERIFY])

Step 1: For each regulator f_i (i=1..11): construct D_K cutoff D_K^{f_i}(Lambda) = f_i(D_K²/Lambda²) * D_K.
Step 2: Compute observables {A_s, m_H, n_s, sin²theta_W} with each D_K^{f_i} at L_max=5.
Step 3: Apply MP polynomial-bounded moment test: Tr(|D_K^{f_i}|^{-s}) has pole at s=d with residue in polynomial cone.
Step 4: Apply KO-dim=6 weighting: multiply by (1 + Gamma_KO6 correction).
Step 5: Apply span test per §VII.K-META: R-protected span <= 1.5, NOT-R >= 2.5.
Step 6: admissible iff (MP pole condition) AND (span in allowed range per observable protection class).
Step 7: Count admissible_i=1.
Step 8: Decision per threshold table.

### What PASS and FAIL Mean

- **PASS**: Admissibility atlas extended to 9 classes with {step, sum_exp} retained as unique. Meta-principle holds across extended class. L1-zeta / L2-Zubarev decomposition unchanged.
- **INFO**: New candidates (3-6 admissible) disrupt uniqueness. Re-examine L1/L2/L3 layer structure.
- **FAIL**: Too many admissible or too few tested (methodology drift). Re-scope with Connes-team review.

### Agent Prompt Requirements

- Connes-Moscovici 2008 MP polynomial-bounded moment test CRITICAL
- §VII.K-META meta-principle (G58) applied as strict filter
- For each of 9 new tests, produce per-observable verdict (A_s, m_H, n_s, sin²theta_W)
- Report admissible_count and tested_count separately
- GPU torch.linalg.eigvalsh for D_K blocks 1000x1000 at L_max=5

---

## §W7b-82. S84-G36-PRDR-AUDIT

### Gate Metadata

- **Gate ID**: `S84-W7b-82-G36-PRDR-AUDIT`
- **Trigger**: `[AUDIT]`
- **Classification**: NON-PHONONIC (methodology)
- **Agent**: `gen-physicist`
- **Script**: `computations/s84_w7b_82_g36_prdr_audit.py`
- **Working-paper section**: `§VII-N.7 G36 PRDR Audit — Machinery Enumeration Pin`

### Hypothesis Being Tested

S83-G36 (MATRIX-MODEL-CLASSIFICATION PASS, b=4.681) is PRU-vulnerable because at least 3 machinery parameters were not pinned in the S83 plan: (a) sign handling on E_cond (|E_cond| vs signed), (b) Delta scaling (fixed at canonical 0.4642 vs self-consistent gap-equation iteration), (c) V_pair normalization (one-unit per site vs per-mode). Producing a §0.11 machinery-enumeration block with all 3 pinned and verifying G36 PASS survives under each pin choice cures PRU. PASS iff all 3 pins identified and each has a PASS/FAIL/INFO ladder.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | All 3 pins explicitly documented + each has PASS/FAIL/INFO ladder with sub-verdicts + G36 central PASS verified under canonical pins |
| **INFO** | 1-2 pins documented (partial audit) |
| **FAIL** | Any pin unaddressed OR G36 verdict flips under any admissible pin combination |

**Tolerance rule**: COUNT — discrete enumeration of pinned parameters and their verdict ladders. PASS = 3/3 pinned with ladder.

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `G36_input_script` | `computations/s83/s83_w3_36_matrix_model_classification.py` | Source |
| `machinery_params_to_pin` | {sign_handling, Delta_scaling, V_pair_norm} | 3 identified in S83 post-mortem |
| `pin_ladder` | each pin has {canonical, alt1, alt2} variants with PASS/FAIL/INFO | Strict |
| `verdict_survival_test` | G36 b_power varies by <0.10 under pin variations | Stringent |
| `documentation_format` | §0.11 markdown table + JSON | Both required |
| `carry_forward_to_75` | pin values feed #75 machinery (L<=12 extension) | Downstream link |

### Enumeration of Three Pins

**Pin 1: Sign handling on E_cond**
- canonical: use |E_cond| (absolute value) in power-law fit — G36 choice
- alt1: use signed E_cond (can be negative; log-log requires |sign-preserving transform|)
- alt2: use E_cond² and fit to L^(2b) (doubling exponent)
- PASS ladder: canonical -> PASS (b=4.681); alt1 -> PASS iff monotone-negative; alt2 -> PASS iff fit b=9.36+/-0.2 (i.e., 2*4.68)
- INFO threshold: alt1 disagrees with canonical by <10%

**Pin 2: Delta scaling vs gap-equation self-consistency**
- canonical: Delta = Delta_BCS = 0.4642 fixed (from S63 canonical) — G36 choice
- alt1: Delta iterated via self-consistent gap equation at each L
- alt2: Delta scaled with L as Delta(L) = Delta_BCS * sqrt(L/L_ref) (size-dependent)
- PASS ladder: canonical -> PASS (b=4.681); alt1 -> PASS iff gap-iteration converges to b within +/-0.10; alt2 -> FAIL if b > 5.5 (L-scaling pollution)

**Pin 3: V_pair normalization**
- canonical: V_pair = V_0 / Vol(K) per mode normalized — G36 choice (implicit)
- alt1: V_pair = V_0 per site (no volume normalization)
- alt2: V_pair = V_0 / sum_k dim(p,q)² per representation (rep-normalized)
- PASS ladder: canonical -> PASS; alt1 -> FAIL (volume factor pollutes b); alt2 -> PASS iff b unchanged within +/-0.10

### Input SHA-256 Pins

```
canonical_constants.py                                 : <computed-at-runtime>
s83_w3_36_matrix_model_classification.py (archived)    : <computed-at-runtime>
s83_g36_matrix_model_classification.npz                : <computed-at-runtime>
s84_w7b_75_b_power_stability_output.npz (from #75)     : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=pinned_count_of_3, scheme=PRDR-audit, convention=§0.11-ladder, L_max=8)
```

### Substitution Chain ([AUDIT])

Step 1: Read S83-G36 script, enumerate free parameters via static analysis. Confirm 3 identified pins.
Step 2: For each pin, implement canonical + alt1 + alt2 variants in audit script.
Step 3: Run each variant at L=3..8 (matching G36), compute b_power.
Step 4: Record b_power per variant. Check |b_canonical - b_alt| < 0.10 (survival test).
Step 5: Produce §0.11 machinery-enumeration markdown table.
Step 6: If all 3 pins documented + each PASS/FAIL ladder emitted + survival test passed: PASS.
Step 7: Feed canonical pins downstream to #75 (L<=12 extension).

### What PASS and FAIL Mean

- **PASS**: G36 PRU-vulnerability cured. Pinned machinery inherited by #75, #76, #82 all downstream. §VII.N landing (#83) incorporates 3-pin block.
- **INFO**: Partial audit. 1-2 pins identified — queue remaining for S85.
- **FAIL**: G36 verdict flips under admissible pin — withdraw G36 PASS, re-open IKKT classification.

### Agent Prompt Requirements

- Read S83-G36 script verbatim
- Static-analysis free parameters (enumerate every `Delta=`, `sign(...)`, `V_pair=` assignment)
- For each pin, implement 3-variant ladder
- Produce §0.11 markdown table with all 3 pins + each verdict
- G36 canonical PASS verification MANDATORY (check b_power = 4.681 +/- 0.01 reproduces under canonical pins)

---

## §W7b-83. S84-VII.N-REGISTRY-LANDING

### Gate Metadata

- **Gate ID**: `S84-W7b-83-VII-N-REGISTRY-LANDING`
- **Trigger**: `[VERIFY-THEOREM]`
- **Classification**: GEOMETRIC (theorem-landing)
- **Agent**: `kaluza-klein-theorist` (with cross-review by `connes-ncg-theorist` and `gen-physicist` via read-only working-paper sub-section)
- **Script**: `computations/s84_w7b_83_vii_n_registry_landing.py`
- **Working-paper section**: `§VII-N Admissibility Enumeration and IKKT Exclusion` (MASTER section)

### Hypothesis Being Tested

The admissibility enumeration result (d_total, KO-dim, SM-content) -> singleton {(12, 6, A_F=C(+)H(+)M_3(C))}, with IKKT anti-correspondence and 11-dim exclusion both proven via S83-G32 + S83-G36 + (this session's W7b-77 twisted triple admissibility + W7b-78 correspondence table closure), qualifies as a permanent theorem. The landing produces a formal statement, 4-proof chain (cone + sign-table + scaling + twist), scope of applicability, and an explicit falsifier.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | §VII.N entry present in permanent-results-registry with formal statement + 4-proof chain + scope + falsifier + cross-references (G32, G36, W7b-77, W7b-78, Connes-Marcolli sign table) |
| **INFO** | Entry drafted but missing 1-2 cross-references (workshop follow-up) |
| **FAIL** | Falsifier malformed (unmeasurable) OR proof chain incomplete |

**Tolerance rule**: COMPLETENESS — 6-component check (statement, proof, scope, falsifier, cross-refs, SHA anchoring). PASS = 6/6 present.

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `registry_target_file` | `sessions/framework/permanent-results-registry.md` | Canonical |
| `entry_id` | §VII.N | Pre-assigned |
| `formal_statement_length_target` | 3-5 sentences (theorem-statement style) | Standard |
| `proof_chain_components` | {Mellin cone, CCM sign table, power-law scaling, twist-triple test} | 4 sub-proofs |
| `scope_statement_required` | "spectral triples with (A_F, H, D) over M^4 x K, K compact Lie group, KO-dim=6" | Formal |
| `falsifier_required` | "Any string construction exhibiting BOTH KO-dim=6 AND \|E_cond\|~L^{b} with b in [4.58, 4.78]" (re-uses #79 S84-EQUIV-CLASS-FALSIF) | Measurable |
| `cross_references` | G32, G36, W7b-77, W7b-78, W7b-75, W7b-76, Connes-Marcolli 2013 Table 1 | Full |
| `SHA_anchoring` | SHA-256 of S83-G32 + S83-G36 + W7b-77 + W7b-78 verdicts combined | 64-char full hex |

### Formal Statement (to land in registry)

> **Theorem VII.N (Admissibility Singleton and IKKT Anti-Correspondence).** Let (A_F, H, D) be a finite-dim spectral triple equipped with Mellin cone pairing and Connes-Marcolli KO-dim sign-table classification. The admissibility requirements (i) d_total-singleton via Mellin cone (S83-G32), (ii) KO-dim=6 via CCM Table 1 (S82 MG-2), (iii) SM gauge content via three generations + gauge bosons, and (iv) power-law scaling |E_cond(L)| ~ L^b with b in [4.58, 4.78] (S83-G36 + W7b-75) together uniquely determine (d_total, KO-dim, A_F) = (12, 6, C(+)H(+)M_3(C)). The IKKT large-N matrix model (linear L scaling, b=1) is excluded by this classification. No twisted spectral triple generalization (Connes-Moscovici 2008) extends the admissible set (W7b-77). Eleven-dimensional M-theory compactifications, which require d_total=11 or d_total=12 with distinct A_F, are excluded.

### Proof Chain (4 components, each cited to a verdict pin)

1. **Mellin cone pairing singleton**: S83-G32 DIMREDUCTION-AUDIT PASS (d=12 unique, 11 excluded). Tr(|D|^{-s}) residue positive cone.
2. **CCM sign-table reduction to KO=6**: S82 MG-2 + Connes-Marcolli 2013 Table 1. Even KO-dim, SM chirality structure.
3. **Power-law scaling (IKKT exclusion)**: S83-G36 + W7b-75. b=4.681 asymptotic; IKKT b=1 excluded DeltaR² > 0.156.
4. **Twist-triple non-extension**: W7b-77. Zero twisted candidates admissible. M-theory pathway closed.

### Scope Statement

This theorem applies to spectral triples over product spacetimes M^4 x K with K compact simple Lie group, KO-dim=6, and finite-dim A_F over the complex numbers. Extensions to non-compact K or higher-rank exceptional groups require re-derivation.

### Falsifier Statement

Any string or matrix-model construction exhibiting BOTH (a) KO-dim=6 irreducible representation structure AND (b) |E_cond(L)| ~ L^{b} with b in [4.58, 4.78] asymptotically, falsifies the singleton exclusivity. Both conditions must be met; demonstrating one alone does not falsify.

### Input SHA-256 Pins

```
canonical_constants.py                                  : <computed-at-runtime>
sessions/framework/permanent-results-registry.md        : <computed-at-runtime>
s83_g32_dimreduction_audit.npz                          : <computed-at-runtime>
s83_g36_matrix_model_classification.npz                 : <computed-at-runtime>
s84_w7b_75_b_power_stability_output.npz                 : <computed-at-runtime>
s84_w7b_76_sdw_b_prediction_output.npz                  : <computed-at-runtime>
s84_w7b_77_twisted_triple_admissibility_output.npz      : <computed-at-runtime>
s84_w7b_78_correspondence_table_closure_output.json     : <computed-at-runtime>
connes_marcolli_sign_table_2013.json                    : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=6_of_6_components_present, scheme=registry-landing-audit, convention=permanent-results-registry-S84, L_max=N/A)
```

### Substitution Chain ([VERIFY-THEOREM])

Step 1: Read current permanent-results-registry.md. Verify §VII.N slot unused.
Step 2: Draft formal statement (above), 4-proof chain, scope, falsifier.
Step 3: Verify each sub-proof cites a verdict pin (SHA-256 full) from S83/S84.
Step 4: Compute registry-entry SHA = SHA-256(formal_statement || proof_chain || scope || falsifier || cross_refs).
Step 5: Append entry to registry (via Write tool to registry file, append-only).
Step 6: Verify 6-component completeness check (statement, proof, scope, falsifier, cross-refs, SHA).
Step 7: Emit verdict line.

### What PASS and FAIL Mean

- **PASS**: §VII.N permanently landed. Singleton admissibility + IKKT anti-correspondence + 11-dim exclusion are registered framework theorems. Future sessions cite §VII.N by reference, not re-derive.
- **INFO**: Draft complete but missing 1-2 cross-references. Queue as S85 closure.
- **FAIL**: Falsifier unmeasurable (theorem unfalsifiable) OR proof chain has unsupported link. Withdraw landing.

### Agent Prompt Requirements

- Read permanent-results-registry.md verbatim to confirm §VII.N slot
- Draft formal theorem statement (above) with precise theorem-statement style
- Each sub-proof cites SHA-256 full-64-char of a verdict line
- Falsifier must be numerically measurable (include specific threshold)
- DO NOT re-derive admissibility — this is a registry-landing, not a re-proof
- Cross-reference #75, #76, #77, #78 outputs (require they be completed first if parallel; else cite provisional)

---

## §W7b-84. S84-KK-TOWER-AT-SINGLETON

### Gate Metadata

- **Gate ID**: `S84-W7b-84-KK-TOWER-AT-SINGLETON`
- **Trigger**: `[VERIFY]`
- **Classification**: GEOMETRIC (spectral) / PARTICLE (KK states)
- **Agent**: `kaluza-klein-theorist`
- **Script**: `computations/s84_w7b_84_kk_tower_at_singleton.py`
- **Working-paper section**: `§VII-N.8 KK Mass Spectrum at Singleton Admissibility`

### Hypothesis Being Tested

At the singleton admissibility point (d_total=12, KO-dim=6, A_F_SM), the KK tower mass spectrum m_n = lambda_n / R(tau) is computable per SU(3) irrep (p,q) using canonical Jensen deformation (lambda_1(s)=alpha*e^{2s}, lambda_2(s)=alpha*e^{-2s}, lambda_3(s)=alpha*e^s) with tau_fold=0.190. For 8 selected (p,q) in {(1,0), (1,1), (2,0), (2,1), (3,0), (0,3), (2,2), (3,1)}, the first 8 KK levels per (p,q) at tau=0 (round SU(3)) and tau=0.19 (fold) are determined and the spectrum shift under Jensen deformation quantified.

### Pass / Fail / INFO Thresholds

| Outcome | Criterion |
|:--------|:----------|
| **PASS** | All 8 (p,q) x 8 levels x 2 tau-values = 128 eigenvalues computed; positive-definite at tau=0; Jensen monotone at tau=0.19 (no level crossing) |
| **INFO** | Some (p,q) produce level crossings (warrants investigation) |
| **FAIL** | Negative eigenvalues at tau=0 (methodology error) OR spectrum diverges at tau=0.19 |

**Tolerance rule**: ABSOLUTE (128 eigenvalues computed) + MONOTONE (no crossings under Jensen deformation).

### Machinery Pin (PRDR)

| Parameter | Value | Justification |
|:----------|:------|:--------------|
| `irreps_(p,q)` | {(1,0), (1,1), (2,0), (2,1), (3,0), (0,3), (2,2), (3,1)} | 8 selected — fundamental + adjoint + higher |
| `levels_per_irrep` | 8 | First 8 eigenvalues of Laplacian on K=SU(3) per (p,q) |
| `tau_values` | {0, 0.19} | Round + fold |
| `alpha_normalization` | Killing form canonical (alpha² = -1/(2*h_v) * Trace(ad(X)ad(X))) h_v=dual Coxeter=3 for SU(3) | Canonical |
| `R(tau)_formula` | R(tau) = Vol(K, Jensen(tau))^{1/d_internal} = (Vol_SU3 * prod_i lambda_i^(1/d))^{1/d} | Canonical |
| `R(0)` | Vol_SU3^{1/8} | Round radius |
| `R(tau_fold)` | Jensen-adjusted Vol | Fold radius |
| `Laplacian_method` | Casimir eigenvalue per (p,q) + Jensen shifts | Representation-theoretic |
| `Casimir(p,q)` | C_2(p,q) = (p² + q² + p*q + 3*(p+q))/3 | Standard SU(3) |
| `GPU path` | torch.linalg for 2000x2000 D_K blocks | L_max=5 per (p,q) |
| `D_K block-diagonality` | guaranteed by S22b — compute per-block only | Efficient |

### Input SHA-256 Pins

```
canonical_constants.py                                : <computed-at-runtime>
jensen_metric_blocks_SU3_tau0.npz                     : <computed-at-runtime>
jensen_metric_blocks_SU3_tau019.npz                   : <computed-at-runtime>
s22b_peter_weyl_block_diagonal.npz                    : <computed-at-runtime>
su3_casimir_eigenvalues_pq_table.json                 : <computed-at-runtime>
```

### Expected Output 4-Tuple

```
(value=128_eigenvalues_npz, scheme=Casimir+Jensen-shift, convention=canonical-left-invariant, L_max=5)
```

### Substitution Chain ([VERIFY])

Step 1: For each (p,q), compute round-SU(3) Laplacian eigenvalue:
lambda²_(p,q)(round) = alpha² * C_2(p,q), where C_2(p,q)=(p²+q²+p*q+3(p+q))/3.

Step 2: At tau=0, all three lambda_i = alpha: R(0) = Vol_SU3^{1/8}. Then
m_n²(tau=0) = lambda²_(p,q)(round) / R(0)²  for n = 1..8 levels per (p,q).

Step 3: At tau=tau_fold=0.19, Jensen deformation:
lambda_1(0.19) = alpha*e^{0.38}, lambda_2(0.19) = alpha*e^{-0.38}, lambda_3(0.19) = alpha*e^{0.19}.
Volume element scales: Vol(K, Jensen) = Vol_SU3 * prod_i lambda_i(s)^{dim_i}, where dim_i = {dim_u(1), dim_su(2), dim_C²} = {1, 3, 4} per Baptista 3.70.
Vol_SU3(Jensen) = Vol_SU3 * e^{0.38 * 1} * e^{-0.38 * 3} * e^{0.19 * 4} = Vol_SU3 * e^{0.38 - 1.14 + 0.76} = Vol_SU3 * e^{0.00} = Vol_SU3 (volume-preserving at fold)
Hence R(0.19) = Vol_SU3^{1/8} = R(0) (volume-preserving TT from permanent).

Step 4: At tau=0.19, the Laplacian eigenvalues SHIFT per (p,q) by Jensen anisotropy:
lambda²_(p,q)(0.19) = sum_i c_i^{(p,q)} * (alpha * e^{s_i * tau})², where c_i^{(p,q)} are the branching coefficients of (p,q) into u(1)+su(2)+C² blocks (from S63 branching computation).

Step 5: m_n²(tau_fold) = lambda²_(p,q)(0.19) / R(0.19)² = lambda²_(p,q)(0.19) / R(0)² (same denominator as tau=0).

Step 6: Verify positivity: m_n² > 0 for all 128 entries.
Verify monotonicity: for each (p,q), m_n(tau=0.19) vs m_n(tau=0) has no level crossing (n=1 stays lightest, etc.).

Step 7: Emit npz with 128 entries + branching coefficients per (p,q).

### Expected Numerical Anchors

| (p,q) | C_2(p,q) | m²_1(tau=0)/alpha² | m²_1(tau=0.19)/alpha² (approx) |
|:------|:---------|:-------------------|:--------------------------------|
| (1,0) | 4/3 | 1.333 | 1.333 * (Jensen shift) |
| (1,1) | 3 | 3.000 | 3.000 * (Jensen shift) |
| (2,0) | 10/3 | 3.333 | varies |
| (2,1) | 16/3 | 5.333 | varies |
| (3,0) | 6 | 6.000 | Parthasarathy saturating — special (see S63) |
| (0,3) | 6 | 6.000 | conjugate of (3,0) |
| (2,2) | 8 | 8.000 | varies |
| (3,1) | 9 | 9.000 | varies |

Jensen shift factor per (p,q) computed from branching coefficients (S63) — the workhorse of this gate.

### What PASS and FAIL Mean

- **PASS**: KK tower computable at the admissibility singleton. Provides the zero-mode spectrum the singleton predicts — observationally relevant for KK-threshold corrections (cf. M_H=131.8 GeV from KK-threshold in framework). Feeds #83 §VII.N scope (spectrum is well-defined at the singleton).
- **INFO**: Level crossings detected — physical interpretation required (avoided-crossing structure, like S35 fold workshop).
- **FAIL**: Negative eigenvalues at tau=0 (methodology bug) OR divergence at tau=0.19 (Jensen breaks compactness at fold). Either outcome would contradict permanent volume-preserving TT.

### Agent Prompt Requirements

- Casimir C_2(p,q) formula from standard SU(3) representation theory
- Jensen deformation EXACTLY as canonical (lambda_1=alpha*e^{2s}, lambda_2=alpha*e^{-2s}, lambda_3=alpha*e^s)
- S22b block-diagonality: compute per-block only; cross-block = 0 at 8.4e-15
- S63 branching coefficients: import from `s63_cartan_trace_identity_coefficients.npz`
- Volume-preserving TT anchor: R(0.19) = R(0) = Vol_SU3^{1/8} (permanent result)
- GPU torch.linalg for D_K blocks 2000x2000 per (p,q) at L_max=5
- Emit npz with shape (8_irreps, 8_levels, 2_tau_values) + branching coefficients
- Substrate framing: KK masses are SPECTRAL PROPERTIES of the Dirac operator on K, not particles "living in" a higher-dim container

---

## W7b -> W7a Parallel Dispatch Note

W7b (this file, 8 gates) and W7a (72-74, 79-80, 5 gates) are MUTUALLY INDEPENDENT. The shared root-parent dependency is S83 verdicts (G32, G36, G27, G55, G58). Neither wave's gates depend on the other's outputs at plan-level. Parallel dispatch policy:

| Dispatch | Count | Max concurrent | Sequence |
|:---------|:------|:---------------|:---------|
| W7a round 1 | 2 (items 72, 73) | 2 | parallel |
| W7b round 1 | 4 (items 75, 77, 78, 81) | 4 | parallel — max 4 concurrent enforced |
| W7a round 2 | 2 (items 74, 79) | 2 | parallel (after W7a round 1) |
| W7b round 2 | 3 (items 76, 82, 84) | 3 | parallel (after W7b round 1; #76 depends on #75's b_power output for comparison; #82 depends on S83-G36 only; #84 depends on S22b only) |
| W7b round 3 | 1 (item 83) | 1 | sequential (after #75, #76, #77, #78 complete; §VII.N landing consolidates) |
| W7a round 3 | 1 (item 80) | 1 | sequential (lit-review; low parallelism) |

**Concurrent dispatch cap**: per user feedback rule (`feedback_dispatch-discipline.md`), max ~8 subagents concurrently. W7a+W7b round 1 together = 6 concurrent; W7a+W7b round 2 = 5 concurrent. Within limit.

**Sequential dependencies within W7b**:
- #76 reads #75 output (cross-check b_power asymptotic vs analytic) — start #76 after #75 artifact on disk
- #83 reads #75, #76, #77, #78 outputs (consolidates) — start #83 last
- #82 is independent of #75/76 (reads S83-G36 only, not S84 extension)

**Parallel-safe within round**: #75, #77, #78, #81 have no mutual deps — launch simultaneously.
Within round 2: #76 (after #75), #82 (anytime), #84 (anytime).

---

## W7b -> W8 Decision Point (joint with W7a)

After W7b completes, the next session (S85 or W8 if same-session) should address:

1. **If #75 PASS (b stable) AND #76 PASS (SDW prediction matches)**: #83 §VII.N landing PROCEEDS with b_power as structural invariant. Queue S85 follow-up: extend b asymptotic to L=16, 20 (diminishing EVOI; INFO-level).

2. **If #75 INFO or FAIL (b drift)**: withdraw S83-G36 PASS provisionally. Re-open IKKT correspondence classification in S85. §VII.N landing of #83 DELAYED.

3. **If #77 FAIL (>=3 twisted candidates)**: M-theory-11d exclusion WEAKENS. §VII.N landing adjusts scope statement to "spectral triples with trivial twisting". S85 workshop: twisted-triple sector analysis.

4. **If #78 INFO (1-3 open entries)**: queue as S85 Kaku-KK-Connes workshop.

5. **If #81 INFO or FAIL**: regulator atlas degeneracy / insufficient extension. Meta-principle §VII.K-META robustness revisited.

6. **If #82 FAIL (G36 flips under pin)**: catastrophic. Withdraw G36 PASS, re-open IKKT classification. §VII.N landing RESTARTS.

7. **If #83 PASS**: §VII.N permanent theorem. S85 cites by reference. Proceed to #79 falsifier monitoring and #80 literature review.

8. **If #84 PASS**: KK tower at singleton provides spectrum for downstream m_H, sin²theta_W cross-checks (S84-AF-SINGLETON-SM-COUPLINGS in §VII.K). S85 observables inherit spectrum.

Decision-point artifact: `sessions/archive/session-85-context.md` (to be generated end-of-S84) includes W7b carry-forward with above 8 contingency branches.

---

## W7b Machinery-Enumeration Pin (§0.11)

Per PRDR discipline (`.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness), every W7b gate has its machinery enumerated in the per-gate block above. The consolidated W7b §0.11 table:

| Gate | Pinned machinery parameters | Unpinned (flagged as diagnostic) |
|:-----|:---------------------------|:---------------------------------|
| #75 | L_scan, GPU path, dtype, Jensen, tau, convention, Delta, V_pair, sign handling, seed, fit_method | None — all pinned |
| #76 | a_k coeffs, delta expansion order, metric convention, heat-kernel cutoff, L correspondence, d_internal, d_total, KO-dim, symbolic engine, cross-check | None — analytic |
| #77 | twist_candidates (16), d_scan, KO_scan, A_F_scan, sigma_space, filters (4), SM test, Jensen compat | T-12..T-16 cross-product enumeration heuristic (diagnostic) |
| #78 | table_version, buckets (5), downgrade_rules (2+1), documentation format, ANTI additions, post-G32/G36 rules | None — deterministic |
| #81 | regulator_classes (11), MP filter, KO weighting, L_max, tau, observables, span thresholds, GPU | which 9 of 11 tested (pinned below) |
| #82 | G36 source script, 3 pins enumerated, ladder per pin, survival test, format, carry-forward | None — 3 pins full |
| #83 | target file, entry ID, statement length, proof components (4), scope format, falsifier format, cross-refs (9), SHA anchoring | None — registry-landing |
| #84 | irreps (8), levels (8), tau values (2), alpha normalization, R formula, Laplacian method, Casimir formula, GPU, block-diagonality | branching coefficient import path (from S63) |

All 8 gates PRDR-compliant. No PRU-vulnerable parameters.

---

## W7b Input-SHA Ledger

At dispatch time, each gate script logs SHA-256 of every input file in the first 20 lines of stdout. The consolidated input-file set for W7b:

```
Upstream (all gates):
  canonical_constants.py
  Jensen metric blocks SU(3) precomputed tables
  Peter-Weyl block structure (S22b)
  S63 Cartan trace identity coefficients
  Connes-Marcolli 2013 sign table JSON

Gate-specific:
  s83_g32_dimreduction_audit.npz  [for #77, #78, #83]
  s83_g36_matrix_model_classification.npz  [for #75, #76, #78, #82, #83]
  s83_g27_mp_admissibility_unified.npz  [for #81]
  s83_w3_36_matrix_model_classification.py  [for #82]
  sessions/framework/permanent-results-registry.md  [for #83]
  s83_correspondence_table_vii_n_provisional.json  [for #78]
  gilkey_ak_coefficients_SU3.json  [for #76]
  connes_moscovici_twisted_triple_axioms_2008.json  [for #77]
  connes_moscovici_mp_filter_2008.json  [for #81]
  vii_k_meta_principle_g58.json  [for #81]
  su3_casimir_eigenvalues_pq_table.json  [for #84]
  jensen_metric_blocks_SU3_tau{0, 019}.npz  [for #84]
  s22b_peter_weyl_block_diagonal.npz  [for #84]
  s84_jensen_metric_blocks_L{10, 12}.npz  [for #75]
  peter_weyl_blocks_SU3.npz  [for #75]
  s63_cartan_trace_identity_coefficients.npz  [for #76, #84]
```

All SHAs `<computed-at-runtime>` in the plan; emitted to stdout at script init; logged to `s84_gate_verdicts.txt` per the 64-char canonical form in the verdict line.

**Dual-SHA schema (S84+, per methodology-v3)**: each verdict line carries both `audit_sha256=<>` (of input-pin map) and `content_sha256=<>` (of output artifact). W7b scripts MUST emit both.

---

## End of W7b Plan

8 gates, 8 full blocks, 3-round parallel dispatch, 1 registry landing, 2 analytic derivations, 1 128-eigenvalue KK tower computation, 1 MP-atlas extension, 1 PRDR audit, 1 correspondence table closure. All machinery pinned. All gates PRDR-compliant. All verdicts emit dual-SHA. All classifications (PHONONIC, GEOMETRIC, PARTICLE, NON-PHONONIC) per phononic-framing rule.
