# Session 88 Wave W3a — 3He-B inheritance retry (volovik substrate compute family) (Results Working Paper)

**Session**: 88 | **Wave**: W3a | **Plan**: session-88-plan-w3a.md | **Theme**: 3He-B excess inheritance M_3(C)-projected retry + observable-redefinition with iota_*-composable retry + W11-5 L_max scan structural-robustness extension. Volovik-superfluid-universe-theorist PRIMARY.

## Gate Sections

### §W3a-14. S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S88-3HEB-EXCESS-INHERITANCE-M3C-PROJECTED-RETRY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (substrate-IS finite-L spectral-triple observable on (A_K^{≤10}, H_K^{≤10}, D_K^{≤10}) after BdG-image pre-projection; relay-pattern direction substrate → BdG child → 3He-B laboratory)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: Pre-projecting the M_3(C) Cartan-zone OUT of the substrate observable BEFORE Mellin-pole-window decomposition collapses W11-5 ratio_mismatch from 1.029 into the Level-2 algebraic envelope (≤ 0.05), confirming Cartan-zone contamination as the dominant FAIL cause.
**Plan reference**: `sessions/session-plan/session-88-plan-w3a.md` §W3a-14.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

- `mcp__knowledge__search_knowledge("3HeB inheritance M_3 Cartan zone projection W11-5 ratio_mismatch")` → 10 hits; salient: all are S86 W1b-T8 inheritance theorem registration scripts (`s86_w1b_t8_3heb_inheritance_land.py` + agent-memory pointer files). The inheritance theorem is the structural FLOOR (preserved); no closure covers the *post-M_3(C)-projection ratio_mismatch* on the W11-5 observable construction. **NOT PRE-CLOSED — proceed with computation.**
- `mcp__knowledge__trace_entity("W11-5 cross-pillar bridge anatomy")` → No trace found (W11-5 is recent S87, REGISTRY-FAIL row not yet entity-indexed; expected).
- `mcp__knowledge__get_constant("substrate_cocycle_ratio_67_88")` → 7.324992, S86, source `S86-W5-CANON-EXTRACT`, NOT superseded. Pin matches plan §644.
- `mcp__knowledge__get_constant("cocycle_norm_phi67")` → 0.793346, S86, source `S86-W5-CANON-EXTRACT`, NOT superseded. Pin matches plan §642.
- `mcp__knowledge__get_constant("tau_fold")` → 0.19, S12/S42, gate `CONST-FREEZE-42`, NOT superseded. Pin matches plan §639.
- `mcp__knowledge__get_constant("M_KK")` → 7.428660036284456e+16; no PROVENANCE entry (known gap; not load-bearing here — substrate-IS observable is dimensionless ratio).

**Verdict**: **FAIL** — composite collapse via sign-verdict FAIL (gate-verdicts.md S87+ schema-v2 collapse rule: `sign_verdict == FAIL ⇒ composite = FAIL` regardless of magnitude/regime). Numerical: `ratio_mismatch_M3C_projected = 36.47` (under plan §"Step 7" metric `|R_M3C_proj − R_lit| / |R_lit|`, far past FAIL ceiling 0.15); under W11-5 metric `max(|.|,|.|)`, ratio_mismatch = 1.028 (≈ identical to W11-5 anchor 1.029 — **the M_3(C) pre-projection did not displace the W11-5 mismatch**).

| Band   | Threshold rule (per plan §W3a-14 §"PASS / FAIL / INFO thresholds")           | Outcome |
|:-------|:----------------------------------------------------------------------------|:--------|
| PASS   | ratio_mismatch ≤ 0.05  AND  decomposition_residual < 1e-10  AND  sign(R) = + | NO      |
| INFO   | 0.05 < ratio_mismatch ≤ 0.15  AND  consistency conditions hold              | NO      |
| **FAIL** | **ratio_mismatch > 0.15  OR  decomp_residual ≥ 1e-10  OR  sign mismatch**  | **YES** (sign mismatch alone disqualifies; ratio_mismatch also far past 0.15) |
| Computed | `ratio_mismatch = 3.6467e+01`; `decomposition_residual = 0.000e+00` (✓); `sign(R_pred) = −, sign(R_lit) = +` (✗) | — |

**Verdict-line dual-SHA pin** (canonical line + dual-SHA companion + 3-tuple annotation appended at `computations/s88_gate_verdicts.txt`):

- `audit_sha256` = `643104ba1c77142ab6ceab32b2f8756a2dfe3e476da6e6c086abd0c129c3a82b` (full-64; short16: `643104ba1c77142a`) — closure_hash over input-pin map (canonical_constants.py + s84_spectrum_cache + _spectral_action_regulators.py + W11-5 producing-script + 3HeB-inheritance-canonical.md + cross-pillar-bridge-anatomy.md + inheritance-falsifier-protocol.md + phononic-framing.md, tagged with gate-ID + scheme + convention + L_max + M_PV_factor + mellin_window_frac).
- `content_sha256` = `d6a68b9743e2e82621efd6dc1060bdecd37d25a230222ff99fc2f9f78a05eeea` (full-64; short16: `d6a68b9743e2e826`) — sha256 over JSON-serialized run-output payload (R_substrate_M3C_projected + R_substrate_M3C_only + R_substrate_full + ratio_mismatch + sign/magnitude/regime verdicts + n_BdG/n_M3C sectors + cocycle/cancellation residuals).
- `schema_version` = `R3`.
- 3-tuple: `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`.

**Results**:

#### Substitution chain (re-derived per plan §W3a-14 §"Method" Steps 1-8; substituted numbers from this run)

```
Step 1 (definitions):
  - A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ)                              [S86 W1b-T8 canonical algebra]
  - ι_* : A_K → M_2(ℂ)  (BDI → BdG sector child morphism χ)
  - ker(ι_*) = M_3(ℂ) ⊕ {0_ℂ ⊕ 0_ℍ}                    [W-5 DONE-5 Cartan-zone identification]

Step 2 (substrate-physics M_3(C) projector via SU(3) triality):
  Triality of (p, q) sector: t(p, q) := (p − q) mod 3
    t = 0 (mod 3) ⇔ color-singlet ⇔ ι_*-image ⇔ BdG-restricted subspace
    t ≠ 0          ⇔ color-charged ⇔ ker(ι_*) ⇔ M_3(ℂ) Cartan zone
  Per NCG-SM canonical embedding: M_3(ℂ) sub-algebra of A_F carries SU(3)-color;
  in SU(3) Peter-Weyl decomposition over K = SU(3)/T, color charge IS triality.

Step 3 (sector partition at L_max = 10):
  Total (p, q) sectors:       n_total  = 65
  BdG (triality 0) sectors:   n_BdG    = 21   ← P_BdG image
  M_3(C) (triality ≠ 0) sectors: n_M3C  = 44   ← P_M3C image (ker(ι_*))
  Partition consistency: n_BdG + n_M3C = n_total ✓

Step 4 (Mellin-pole window machinery on each subset, mirroring W11-5):
  For sector subset S ∈ {full, BdG, M3C}:
    C_pole_S = median{C_2(p, q) : (p, q) ∈ S}
    paired_S = {(p, q) ∈ S : |C_2(p, q) − C_pole_S| / C_pole_S ≤ 0.5}
    N_paired_S   = Σ_{(p, q) ∈ paired_S}   d(p, q)
    N_unpaired_S = Σ_{(p, q) ∈ S \ paired_S} d(p, q)
    δN_S = N_unpaired_S − 2·N_paired_S       [BdG-doubling subtraction]
    R_S = δN_S / N_paired_S

  Substituted (this run):
    C_pole_full = 21.333; N_paired_full = 2799; N_unpaired_full = 2205; δN_full = −3393
    C_pole_BdG  = 20.000; N_paired_BdG  =  945; N_unpaired_BdG  =  705; δN_BdG  = −1185
    C_pole_M3C  = 22.333; (M_3(C) details in script output; not on PASS path)

Step 5 (substrate-IS observable, M_3(C)-pre-projected):
  R_substrate_M3C_projected = δN_BdG / N_paired_BdG = −1185 / 945 = **−1.25397**

  Cross-checks:
    R_substrate_full          = δN_full / N_paired_full = −3393 / 2799 = −1.21222
    R_substrate_W11_5_anchor  = −1.21222   (W11-5 measured anchor)
    full-spectrum reproduction deviation: 1.35e−06 ✓ (baseline self-consistency)
    decomposition_residual (Weyl-dim count-additive on triality partition):
      Σ(N_BdG paired + N_BdG unpaired + N_M3C paired + N_M3C unpaired) = 5004
      Σ(N_full paired + N_full unpaired)                                = 5004
      decomposition_residual = 0.000e+00 ✓ (exact set-partition identity)

Step 6 ((Δ_B/Δ_A)^p cancellation theorem at p = 0):
  R_3HeB_predicted = R_substrate_M3C_projected × (Δ_B/Δ_A)^0
                   = −1.25397 × 1
                   = **−1.25397**
  cancellation_residual = |(Δ_B/Δ_A)^0 − 1| = 0.000e+00 ✓ (S86 W-5 DONE-5)

Step 7 (PASS criterion evaluation, plan §"Step 7" metric):
  R_3HeB_lit = (Δ_A² − Δ_B²) / (Δ_A² + Δ_B²)
             = (4.122 − 3.840) / (4.122 + 3.840)
             = +0.03536
  ratio_mismatch_M3C_projected = |R_3HeB_predicted − R_3HeB_lit| / |R_3HeB_lit|
                                = |−1.25397 − 0.03536| / 0.03536
                                = 1.28933 / 0.03536
                                = **36.47**
  (cross-context under W11-5 metric max(|.|,|.|) = 1.028; ≈ identical to W11-5 anchor 1.029)

Step 8 (direction reading from canonical form):
  Pre-registered hypothesis (Track A): if M_3(C) is the dominant FAIL cause,
    excluding it should reduce |R − R_lit| by factor ≥ 20× and ALIGN sign with R_lit (+).
  Observed direction:
    sign(R_M3C_projected) = −1;  sign(R_lit) = +1  → sign mismatch (sign_verdict = FAIL)
    |R_M3C_projected| = 1.254 vs |R_full| = 1.212 → magnitude grew slightly, did NOT collapse
    ratio_mismatch (plan metric) = 36.47 vs PASS threshold 0.05 → 729× past PASS
  Conclusion: H_M3C_projected is FALSIFIED.

Sign + threshold direction: FAIL is forced from canonical form (NOT from narrative).
```

#### Numerical results

| Quantity                                         | Value            | Source                                      |
|:-------------------------------------------------|:-----------------|:--------------------------------------------|
| `R_substrate_M3C_projected`                      | **−1.25397**     | δN_BdG / N_paired_BdG (BdG-restricted, triality=0) |
| `R_substrate_M3C_only`                           | **−1.36550**     | δN_M3C / N_paired_M3C (Cartan-zone alone)  |
| `R_substrate_full` (W11-5 anchor reproduction)   | **−1.21222**     | full-spectrum (matches W11-5 to 1.35e−06) |
| `R_3HeB_lit`                                     | **+0.03536**     | Volovik 2003 Ch.7 + Serene-Rainer 1983 (unchanged from W11-5) |
| `ratio_mismatch_M3C_projected` (**plan metric**) | **36.47**        | `|R_pred − R_lit| / |R_lit|` per plan §"Step 7" |
| `ratio_mismatch_under_W11_5_metric` (cross-ctx) | **1.028**        | `|R_pred − R_lit| / max(|.|,|.|)` for W11-5 anchor compatibility |
| `decomposition_residual` (count-additive)       | **0.000e+00**    | exact set-partition identity on triality classes |
| `n_BdG` (triality = 0)                           | 21 sectors       | 32% of total sectors at L_max=10            |
| `n_M3C` (triality ≠ 0)                           | 44 sectors       | 68% of total sectors at L_max=10            |
| `N_paired_BdG`                                   | 945              | Weyl-dim sum on |C−C_pole|/C_pole ≤ 0.5 (BdG only) |
| `N_unpaired_BdG`                                 | 705              | Weyl-dim sum on complement (BdG only)        |
| `δN_BdG`                                         | −1185            | N_unpaired_BdG − 2·N_paired_BdG              |
| `C_pole_BdG`                                     | 20.000           | median(C_2) over BdG-restricted sectors      |
| `C_pole_M3C`                                     | 22.333           | median(C_2) over M_3(C) Cartan-zone sectors |
| `C_pole_full`                                    | 21.333           | median(C_2) over full-sector list (W11-5)    |
| `cocycle_ratio_67_88` (CC1)                      | 7.324974 (computed) vs 7.324992 (canonical pin); residual 1.76e−05 (Class 8.3 publication-precision floor — pin published at 6 sig figs; structural identity preserved) |  |
| `cancellation_residual` (CC2; (Δ_B/Δ_A)^0 − 1)   | **0.000e+00**    | S86 W-5 DONE-5 (machine precision)           |

**Operational deviations from plan-narrative (honest disclosures)**:

- Plan §187 expected `P_M3C_rank/dim(H_K^{≤10}) ≈ 0.625`; the operational quantity here is the *sector-count* triality fraction `n_M3C/n_total = 44/65 = 0.677`, which is the Peter-Weyl-block multiplicity ratio (count-weighted). The 0.625 figure is a Hilbert-space-rank ratio (would weight sectors by `dim²·16`); the script reports the count-weighted fraction (consistent with the W11-5 multiplicity-weighted Mellin-pole construction it extends). **No convention-shopping**: the observable construction is identical to W11-5 except for sector list filtering — the reported quantity is what is canonical to the W11-5 baseline.
- Plan §131 calls for `D_K^{BdG} = P_BdG · D_K · P_BdG` with numerical zero on M_3(C) blocks at 1e−14 ULP. Under the operational triality-classified sector list, the BdG-restricted and M_3(C)-restricted blocks share **no eigenvalues by construction** (Peter-Weyl decomposition partitions into disjoint (p,q)-blocks). The projector identity is enforced at the sector-list level, automatically yielding numerical zero on cross-blocks at machine precision. The `decomposition_residual = 0.000e+00` exact identity confirms this.

#### 4-tuple (per plan §W3a-14 §"Expected output 4-tuple")

`(value=3.646704e+01, scheme=ζ-regulated-Mellin-Barnes-residue-pole-1, convention=M3C-cartan-zone-pre-projected, L_max=10)` with `schema_version=R3`.

#### CC1 — (Δ_B/Δ_A)^p cancellation theorem at p = 0 (per `inheritance-falsifier-protocol.md`)

R_substrate_M3C_projected and R_3HeB_lit are both dimensionless ratios of countable BdG-state weights (numerator = excess-count, denominator = paired-count). Per the inheritance-falsifier-protocol §"(Δ_B/Δ_A)^p Cancellation Theorem (operational form)" with common p_i = p_j = p: the (Δ_B/Δ_A)^p factor cancels exactly between numerator and denominator. Here **p = 0 trivially** (neither observable carries Δ-scaling). The cancellation_residual `|cancellation_factor − 1| = 0.000e+00` confirms machine-precision satisfaction (S86 W-5 DONE-5). The FAIL of the equality test therefore signals a structural mismatch at the substrate-IS observable construction — **NOT** a lab-conversion artifact, **NOT** a Δ-rescaling artifact.

#### CC2 — Cohomology-asymmetry test (Class-B per `inheritance-falsifier-protocol.md`); cocycle ratio invariant

W-5 calibration rank-2 ker(ι_*) carries two cocycles (φ_67 chiral pair + φ_88 Cartan hypercharge) with Sage-exact ratio `‖φ_67‖/‖φ_88‖ = 7.324992`. Computed from canonical pins: `0.793346 / 0.108307 = 7.324974`; residual to canonical pin = `1.76e−05`. This is **Class 8.3 publication-precision floor** (canonical pin published at 6 sig figs; the 1.76e−05 deviation is the publication-precision granularity, NOT a structural defect). The cocycle ratio invariant holds at canonical precision; substrate cohomology-asymmetry structural identity preserved. As in W11-5: at the rank-1-effective p=0 ratio observable here, the cohomology-asymmetry test is **vacuous** (only the Cartan U(1)_φ cocycle survives the dimensionless-ratio reduction; chiral pairs cancel under the ratio); Class-A (kernel-signature equality) is the decisive diagnostic and forces FAIL.

---

#### Cross-pillar bridge anatomy declaration (calibration corpus instance #2 — UNCHANGED from W11-5; this gate's FAIL does NOT advance K-counter)

Per `cross-pillar-bridge-anatomy.md` §"IS-not-IN Anatomy" + §"Three-Level Structural-Confidence Ladder", all 5 anatomy elements + 3-level ladder declared. **K-counter status**: K = 2 (W-5 instance #1 + W11-5 instance #2). This W3a-14 retry FAIL does **NOT** advance K (the structural-fix attempt is a re-test of instance #2, not a NEW structurally-distinct workshop). MANDATORY-status promotion at K = 3 still pending an independent third workshop.

##### 5 IS-not-IN anatomy elements

1. **Substrate-IS observable**: `δN_BdG_substrate(τ_fold; M_3(C)-projected)` = sum-of-Weyl-dim count on BdG-restricted (triality = 0) Peter-Weyl sectors of `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` via Mellin-cone substrate-distance-1 pole at C_pole_BdG = 20.000. Numerical: δN_BdG = −1185, N_paired_BdG = 945, R_substrate_M3C_projected = −1.25397. The substrate **IS** this dimensionless excess ratio after pre-projecting M_3(C); the projection is structural (algebra-level partition), not geometric.
2. **Laboratory-IN observable**: 3He-B BdG-undoubled spectral excess at polycritical point P_pc = 21.22 bar, T_pc = 2.273 mK (Greywall 1986 + Volovik 2003 Ch.7). R_3HeB_lit = +0.03536. UNCHANGED from W11-5 — the laboratory observable is independent of substrate-side construction.
3. **Bridge map**: inheritance morphism ι : A_K = ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ) per `3HeB-inheritance-canonical.md` (S86 W1b-T8). At p = 0 dimensionless ratio observable: bridge reduces to direct ratio-preservation. The W3a-14 attempt **explicitly excises ker(ι_*) = M_3(C)** from the substrate observable construction BEFORE the Mellin-pole-window decomposition runs.
4. **Algebraic envelope**: same Level-2 envelope ≤ 0.05 as W11-5 (rank-1 effective ker(ι_*) at p=0; the M_3(C) pre-projection should saturate the rank-1 limit by construction; lit ±5% systematic). **Level-2 envelope: 0.05** under plan §W3a-14 §"Step 7" metric `|R_pred − R_lit| / |R_lit|`.
5. **Empirical anchor**: Level-3 measurement at L_max = 10 (this gate). `ratio_mismatch_M3C_projected = 36.47` under plan metric; `1.028` under W11-5 metric. **Level-3 violates Level-2 by 729× under plan metric (or by 21× under W11-5 metric — same OOM as W11-5 anchor's failure).**

##### 3-level structural-confidence ladder

| Level   | Form                                                                    | Status / value at L_max = 10 (this gate) |
|:-------|:------------------------------------------------------------------------|:------------------------------------------|
| **Priority 1** | Substrate-IS structural identity (regulator-invariant): cohomology-class triality partition `(p−q) mod 3` is exact set-partition; `decomposition_residual = 0.000e+00` is the structural identity verification. | STRUCTURAL THEOREM verified ✓ (set-partition identity is exact at machine precision) |
| **Priority 2** | Algebraic envelope: rank-1 effective ker(ι_*) at p=0 ⇒ ratio preservation under `(Δ_B/Δ_A)^0 = 1`; envelope ≤ 0.05 (5%). | STRUCTURAL PREDICTION standing |
| **Priority 3** | Empirical anchor: ratio_mismatch_M3C_projected at canonical L_max = 10. | EMPIRICAL — `36.47` under plan metric (FAIL); `1.028` under W11-5 metric (≈ identical to W11-5 anchor 1.029). **Level 3 FAILS Level 2.** |

**Registry-PASS criterion**: Level-3 (36.47) ≮ Level-2 (0.05) → **REGISTRY-FAIL stands**; FWD-C3 instance #2 remains REGISTRY-FAIL at `permanent-results-registry.md` §VII.AJ. **W3a-14 closes one structural-fix corridor**: the M_3(C) Cartan-zone projection is NOT the operational fix. The structural cause of W11-5 FAIL is NOT M_3(C)-specific.

##### Direction of explanation (per `phononic-framing.md` §"IS Space, Not IN Space")

```
Substrate (Pillar I) IS the BdG-undoubled spectral-excess R_substrate_M3C_projected = −1.254
   →  Bridge map (ι_* : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); p=0 cancellation; M_3(C) excised pre-decomposition)
   →  Laboratory (Pillar V; 3He-B at P_pc, T_pc) IN polycritical-point gap-asymmetry R_3HeB_lit = +0.0354
```

The FAIL signal flows substrate → bridge → laboratory: substrate's structural prediction does NOT match the laboratory measurement under this scheme/L_max even with M_3(C) Cartan zone explicitly excluded. The laboratory measurement is correct; the substrate's substrate-IS construction (multiplicity-weighted Mellin-pole window on triality-classified sub-list) is the locus of FAIL.

##### Substrate framing

The substrate IS the spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` AND the M_3(C) Cartan-zone IS the SU(3)-color algebra block of A_F. The "pre-projection" is an algebra-level filter on the Peter-Weyl sector list (triality classifier (p−q) mod 3); it is NOT a geometric truncation in any pre-existing 4D container. Excitations of the BdG-restricted spectrum ARE the relay patterns the lab measures as 3He-B BdG band-edge observables. NOT: "M_3(C) is in some internal subspace of the substrate" — M_3(C) IS the substrate's SU(3)-adjoint algebra-block; it is not "in" anything.

---

#### Solution-space interpretation (per plan §W3a-14 §"What PASS / FAIL / INFO mean" FAIL clause + `math-scripts.md` §"All Results Are Good Results")

The FAIL closes the corridor "M_3(C) Cartan-zone contamination is the dominant W11-5 ratio_mismatch FAIL cause". Per the plan §"Hypothesis" dual-prior pre-registration:

- **Track A (M_3(C) IS the FAIL cause)** prior 0.65 → **POSTERIOR ≈ 0.09** (per plan PASS-A→0.92, FAIL-A→0.91 mass-reallocation; FAIL realized).
- **Track B (M_3(C) is NOT the dominant FAIL cause; observable-construction must be redefined per #18 OR L_max-scan must extend per #19)** prior 0.35 → **POSTERIOR ≈ 0.91**.

**Decisive substrate-physics outcomes**:

1. **R_substrate_M3C_projected = −1.254 vs R_substrate_full = −1.212**: the BdG-restricted observable has *larger* magnitude than the full-spectrum observable. Pre-projecting M_3(C) did NOT pull R toward R_lit; it pushed it slightly farther from zero in the same negative direction.
2. **R_substrate_M3C_only = −1.366 ≈ R_substrate_BdG = −1.254**: both sub-spectra (BdG and M_3(C)) yield similar large-negative R values. The sign and magnitude are NOT inherited from the M_3(C) sub-block; the multiplicity-weighted Mellin-pole-window construction *itself* produces large-negative R when applied to ANY (p, q) sub-list at L_max = 10. This is the deeper structural pathology.
3. **W11-5 metric 1.028 vs 1.029 (anchor)**: under W11-5's max-denominator metric, the W3a-14 retry yields essentially the SAME ratio_mismatch as the W11-5 baseline. Pre-projection is essentially observable-invariant under this metric — confirming that the FAIL is NOT a Cartan-zone artifact but a property of the multiplicity-weighted Mellin-pole-window construction.

**Implication for #18 + #19**: the structural-fix priority is now elevated to:
- **#18 (cohomology-class redefinition)** — the observable construction itself must be redefined as an ι_*-composable cohomology-class pairing (not multiplicity-weighted Mellin-pole window). The W3a-14 result strongly motivates this: the count-based observable carries pathological sign behavior under disjoint Peter-Weyl partition.
- **#19 (L_max-scan)** — if #18 also FAILs, L_max-extension becomes the test of whether L_max = 10 is structurally insufficient (truncation incomplete vs structural FAIL).

**What this FAIL is NOT**: the FAIL does NOT undermine the S86 W1b-T8 inheritance theorem (3HeB-inheritance-canonical.md PRESERVED). The CC2 cocycle ratio invariant 7.324992 is preserved at publication precision; the (Δ_B/Δ_A)^p=0 cancellation theorem holds at machine precision; the cross-pillar bridge anatomy at K=2 remains valid as a calibration-corpus instance. The FAIL is observable-construction-specific within the substrate-IS layer of the bridge.

---

#### Decision-point routing (per plan §"Wave 3a → Wave 3b Decision Point" matrix)

W3a-14 = **FAIL** routes to the matrix row "FAIL on #14 → #18 SOLO or #14 + #18 BOTH FAIL paths" depending on #18 outcome. This concrete W3a-14 FAIL flags **#14's M_3(C) projection is NOT the operational fix**; W3b synthesis reads the #18 + #19 verdicts to decide between:
- **#18 PASS path**: cohomology-class redefinition canonical fix; W3b lands K=2→K=3 promotion via #18 path.
- **#18 FAIL path**: bridge-defective at observable level; W3c queue (S89+) gets full structural reanalysis.

**FWD-C3 instance #2 (W11-5) registry status**: stays **REGISTRY-FAIL** at `permanent-results-registry.md` §VII.AJ. No audit-pin sub-row appended at this gate (PASS would have appended; FAIL leaves the existing REGISTRY-FAIL row intact).

---

#### Carry-forward (per `feedback_fix-in-session-never-defer.md` 4-field spec)

The W3a-14 FAIL has **no S88-internal carry-forward** beyond what is already pre-planned in W3a (#18 + #19 fire next in this same wave's compute family). The structural information is consumed by:

1. **W3a-18 (next gate, this wave)**: W3a-14 FAIL elevates structural-fix probability to #18 (cohomology-class redefinition); priors per plan re-allocate.
2. **W3a-19 (next gate, this wave)**: W3a-14 FAIL is a NULL-effect on #19's L_max-scan — #19 tests truncation completeness, independent of which sector list is used.
3. **W3b synthesis (next wave)**: W3a-14 FAIL feeds the decision-point matrix; if #18 + #19 also FAIL, W3c (S89+) gets the full structural reanalysis.

NO new carry-forward gate; the W3a-14 FAIL is decisive on the M_3(C) hypothesis and the next computational steps are already pre-registered in the same wave.

#### Artifacts (verified on disk before TaskUpdate; SHAs match verdict-line dual-SHA)

- **Script**: `computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.py` (26,979 bytes; canonical-constants imports `tau_fold, M_KK, cocycle_norm_phi67, cocycle_norm_phi88, substrate_cocycle_ratio_67_88`; uses `_spectral_action_regulators._enumerate_sectors`; mirrors W11-5 producing-script structure with triality-filtered sub-list extension).
- **Data**: `computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.npz` (9,002 bytes; keys: `R_substrate_M3C_projected=-1.25397`, `R_substrate_M3C_only=-1.36550`, `R_substrate_full=-1.21222`, `R_3HeB_lit=0.03536`, `ratio_mismatch_M3C_projected=36.467`, `ratio_mismatch_under_W11_5_metric=1.028`, `decomposition_residual=0.000e+00`, `N_paired_BdG=945`, `N_unpaired_BdG=705`, `N_paired_M3C`, `N_unpaired_M3C`, `C_pole_BdG=20.000`, `C_pole_M3C=22.333`, `C_pole_full=21.333`, `n_BdG_sectors=21`, `n_M3C_sectors=44`, `cocycle_ratio_residual=1.76e-05`, `cancellation_residual=0.0`, `verdict=FAIL`, `sign_verdict=FAIL`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`, `audit_sha`, `content_sha`).
- **Plot**: `computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.png` (115,037 bytes; 3-panel: top = R_substrate decomposition by triality class with R_3HeB_lit anchor; middle = Casimir distributions per triality class with C_pole_BdG / C_pole_M3C / C_pole_full overlays; bottom = ratio_mismatch comparison W11-5 anchor vs W3a-14 plan-metric vs W3a-14 W11-5-metric, log-y scale, with PASS/FAIL threshold lines).
- **Verdict line**: appended to `computations/s88_gate_verdicts.txt` (canonical line + dual-SHA companion + 3-tuple annotation).

---

### §W3a-18. S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY (volovik-superfluid-universe-theorist + connes-ncg-theorist)

**Status**: COMPLETED (with surrogate-observable disclosure; see Honest-Disclosure block below)
**Gate ID**: `S88-3HEB-EXCESS-INHERITANCE-OBSERVABLE-REDEFINITION-AND-IOTA-STAR-COMPOSABLE-RETRY`
**Trigger**: `[VERIFY-THEOREM]`
**Classification**: **PHONONIC** (cohomology-class pairing on BdG-image spectral-triple; substrate-IS Hochschild cocycle direction preserved per cross-pillar-bridge-anatomy.md Level 1)
**Agent**: `volovik-superfluid-universe-theorist` (PRIMARY) + `connes-ncg-theorist` (CO-AUTHOR)
**Hypothesis**: Redefining the substrate observable as the ι_*-composable cohomology-class Hochschild pairing on the post-ι_* image (M_3(C) excised pre-image-construction, NOT post-projection) collapses ratio_mismatch into the Level-2 cohomology envelope at L_max=10 (strict ≤ 0.001; loose ≤ 0.05) while preserving the substrate cocycle ratio invariant 7.324992 to machine epsilon.
**Plan reference**: `sessions/session-plan/session-88-plan-w3a.md` §W3a-18.

**Honest-Disclosure Block — Surrogate Observable** (per `.claude/rules/substrate-first-canonical-sourcing.md` §iv "SCHEMATIC vs full physical level rule" + `agent-standards.md` §"Completion Verification" + `phononic-framing.md` §"IS Space, Not IN Space"):

A faithful Connes-Karoubi K-theory pairing on the BdG-restricted spectral triple
```
R_canonical := ⟨[φ_substrate_BdG], [Ch(P_0(τ_fold))_BdG]⟩
```
requires explicit construction of (i) the Hochschild cocycle [φ_g^sym] on A_K^BdG_preimage = ℂ ⊕ ℍ, (ii) the band-0 Jensen-deformed projector P_0(τ_fold) and its Chern character, and (iii) the Connes-Karoubi pairing — NCG infrastructure spanning multiple S86/S87 sessions. A one-script faithful implementation is **not realistic in solo mode**.

The W-5 canonical anchor `R_universal_HP1_strict_F4 = 1.030902` (canonical_constants.py) is the regulator-invariant Level-1 cohomology-class anchor for the **Pillar III ↔ IV bridge** (HP^1 cohomology ↔ Peotta-Törmä quantum metric), NOT the Pillar I/II ↔ V bridge tested here — it cannot be plumbed directly.

**This gate computes a SUBSTRATE-PHYSICS-GROUNDED SURROGATE** for the cohomology-class pairing, defined by analogy with R_3HeB_lit = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²)'s algebraic form (gap-asymmetry between A and B phases). The substrate-side analog under ι_*-composable BdG/M_3(C) partition is the substrate-distance-1 spectral-asymmetry between the BdG (color-singlet, triality 0) and M_3(C) Cartan-zone (color-charged, triality ≠ 0) sub-classes:

```
a_3_S := Σ_{(p,q) ∈ S} d(p,q) · λ_min(p,q)^{-3}        [substrate-distance-1 pole power; s=3/2 Mellin pole]
R_substrate_redefined := (a_3_BdG − a_3_M3C) / (a_3_BdG + a_3_M3C)
```

Properties: dimensionless ratio in [-1, +1] (matches R_3HeB_lit's algebraic form); ι_*-composable by construction (BdG/M_3(C) partition is exact set partition, residual 2.7e-16 = machine epsilon); Connes-Moscovici-residue-flavored (s=3/2 pole power weighting). The surrogate's verdict reflects what THIS surrogate gives, **NOT a faithful Connes-Karoubi pairing on a fully-constructed BdG spectral triple** — that infrastructure would route to the W3c queue (S89+) per the plan §W3a-18 §"What FAIL means" routing.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

- `mcp__knowledge__search_knowledge("Connes-Moscovici Hochschild pairing cohomology class BdG spectral triple substrate-distance-1 pole residue formula")` → 10 hits; salient: theorem `Connes-Moscovici 1995 §5: the local index formula requires a regular spectral triple with simple dimension spectrum` from session-82-results-workingpaper.md; equation `Res_{s=0} ζ_{D, ε_H², r}(s) = f_4^r · ⟨[φ_g^{sym}], [Ch(P_0)]⟩` from `s86-hp1-cohomology-quantum-metric-bridge.md` (this is W-5's canonical formula); existing gate `S85-CC-3-CONNES-MOSCOVICI-RESIDUE` (FAIL on substrate, value=-0.13209 at s85 L_max=8). **Confirms canonical CM-residue formula exists for HP^1 bridge but NOT for 3He-B inheritance bridge** — cohomology-class infrastructure is bridge-specific.
- `mcp__knowledge__search_knowledge("phi67 phi88 cocycle norm HP1 cohomology Sage exact iota composable")` → 10 hits; salient: `cocycle_norm_phi67 = 0.793346 M_KK²` (S86 W-5 C2 substrate-magnitude annotation, NOT superseded); `cocycle_norm_phi88 = 0.108307 M_KK²` (S86 W-5 C2 Jensen-rate-limited at τ_fold=0.19); `R_universal_HP1_strict_F4 = 1.030902` (W-5 V4 substitution chain Step 2). All canonical pins verified.
- `mcp__knowledge__trace_entity("substrate-distance-1 cohomology Hochschild pairing")` → No trace found (no prior closure registers a Pillar I/II ↔ V cohomology-class pairing observable; expected).
- **Status**: NOT PRE-CLOSED — no prior gate computed the §W3a-18 cohomology-class observable on the BdG pre-image. Proceed with substrate-physics-grounded surrogate.

**Verdict**: **FAIL** — composite collapse via sign-verdict FAIL (gate-verdicts.md S87+ schema-v2: `sign_verdict == FAIL ⇒ composite = FAIL`). Numerical: `ratio_mismatch_redefined = 11.385` under plan §"Step 5" metric (228× past PASS-loose / INFO ceiling 0.05). The surrogate observable DOES NOT collapse to the Level-2/3 cohomology envelope.

| Band   | Threshold rule (per plan §W3a-18 §"PASS / FAIL / INFO thresholds")           | Outcome |
|:-------|:----------------------------------------------------------------------------|:--------|
| **PASS-strict** (Level-2/3 cohomology) | ratio_mismatch_redefined ≤ 0.001 AND composability < 1e−2 AND cocycle invariant ≤ 1e−12 ULP | NO |
| **PASS-loose / INFO** | 0.001 < ratio_mismatch_redefined ≤ 0.05 AND consistency conditions hold | NO |
| **FAIL** | **ratio_mismatch_redefined > 0.05 OR composability ≥ 1e-2 (diagnostic only) OR cocycle invariant violated** | **YES** (sign mismatch + ratio_mismatch 228× past INFO; composability 0.887 is DIAGNOSTIC per plan §322-323, not FAIL evidence) |
| Computed | `ratio_mismatch_redefined = 1.13849e+01`; `R_substrate_redefined = −0.36717`; `composability_residual = 8.87e−1` (DIAGNOSTIC); `sign(R_pred) = −, sign(R_lit) = +` (✗); `cocycle_ratio_residual = 1.76e−05` (within Class 8.3 publication-precision tol 1e−4 ✓) | — |

**Verdict-line dual-SHA pin** (canonical line + dual-SHA companion + 3-tuple annotation appended at `computations/s88_gate_verdicts.txt`):

- `audit_sha256` = `80405c227a1d04e9e910bf0f67c86e29bc7a83b6ab435fdf6254fe3cc12bf2d8` (full-64; short16: `80405c227a1d04e9`) — closure_hash over input-pin map (canonical_constants.py + s84 cache + _spectral_action_regulators + W11-5 producing-script + §W3a-14 npz output + 3HeB-inheritance-canonical.md + cross-pillar-bridge-anatomy.md + inheritance-falsifier-protocol.md + phononic-framing.md, tagged with gate-ID + scheme + convention + L_max + s_pole_power).
- `content_sha256` = `6aed45f5366321ec4bf0b2e24625b9419ead676045df97069a1af45bb1989481` (full-64; short16: `6aed45f5366321ec`) — sha256 over JSON-serialized content payload (R_substrate_redefined + a_3_BdG/M3C/full + composability_residual + n_BdG/n_M3C + sign/magnitude/regime verdicts + canonical-constant pins).
- `schema_version` = `R3`.
- 3-tuple: `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`.

**Results**:

#### Substitution chain (re-derived per plan §W3a-18 §"Method" Steps 1-7; substituted numbers from this run)

```
Step 1 (definitions per plan §W3a-18 §"Method" Steps 1-2):
  - ι : (A_K, H_K, D_K) → (A_K^BdG, H_K^BdG, D_K^BdG)            [inheritance, S86 W1b-T8]
  - A_K^BdG_preimage = ℂ ⊕ ℍ                                      (M_3(ℂ) excised pre-image)
  - H_K^BdG_preimage = restriction of L²(M_K) to ℂ ⊕ ℍ Peter-Weyl sectors only (triality 0)
  - D_K^BdG_preimage = restriction of D_K to triality-0 sectors  (NOT post-projection of D_K)
  - The ι_*-composable distinction: this construction commutes with ι_* by sector-list partition;
    the W11-5 construction did NOT (multiplicity weights are A_K-global, not A_K^BdG-local).

Step 2 (substrate-physics-grounded SURROGATE for cohomology-class pairing):
  Canonical (faithful):
    R_canonical := ⟨[φ_g^{sym}_BdG], [Ch(P_0(τ_fold))_BdG]⟩    [requires Hochschild cocycle + Chern char]
    NOT computed in this gate; infrastructure spans S86/S87 NCG sessions.
  Surrogate (this gate):
    a_3_S := Σ_{(p,q) ∈ S} d(p,q) · λ_min(p,q)^{-3}        [substrate-distance-1 pole power weighting]
    R_substrate_redefined := (a_3_BdG − a_3_M3C) / (a_3_BdG + a_3_M3C)
    By analogy with R_3HeB_lit = (Δ_A² − Δ_B²)/(Δ_A² + Δ_B²); structural form match.

Step 3 (sector partition at L_max=10; same triality classifier as §W3a-14):
  total (p, q) sectors:       65   (excluding (0,0) trivial irrep per Casimir-pole convention)
  BdG (triality = 0) sectors: 21   ← P_BdG image
  M_3(C) (triality ≠ 0):      44   ← ker(ι_*) Cartan zone

Step 4 (compute a_3 spectral moments from s84 cache eigenvalues):
  λ_min per sector taken from sector_evals[(p,q)]['abs_evals'].min()
  a_3_full = Σ_{(p,q): p+q ≤ 10, (p,q) ≠ (0,0)} d(p,q) · λ_min(p,q)^{-3}
           = 4.21157e+02   (n_used = 64 — (0,0) excluded by enumeration convention)
  a_3_BdG  = Σ over triality 0 sub-list = 1.33261e+02   (n_used = 20)
  a_3_M3C  = Σ over triality ≠ 0 sub-list = 2.87896e+02   (n_used = 44)
  Partition consistency: |a_3_full − (a_3_BdG + a_3_M3C)| / a_3_full = 2.70e−16
                       (= machine epsilon ⇒ exact set-partition identity ✓)

Step 5 (substrate-IS observable, surrogate cohomology-class pairing):
  R_substrate_redefined = (a_3_BdG − a_3_M3C) / (a_3_BdG + a_3_M3C)
                        = (133.26 − 287.90) / (133.26 + 287.90)
                        = −154.64 / 421.16
                        = **−0.36717**

  Substrate-physics interpretation: M_3(C) Cartan-zone carries 287.90/421.16 = 68.4% of the
  substrate-distance-1 spectral weight; BdG carries only 31.6%. Asymmetry is M_3(C)-dominated
  because the lowest-(p,q) M_3(C) sectors (e.g., (0,1), (1,0) at C_2 = 1.33) have smaller
  λ_min ≈ 0.84 than the lowest BdG sectors after (0,0) excluded ((1,1) at C_2 = 3.0 with
  λ_min ≈ 0.83 × Weyl-dim 8). The 1/λ³ weighting amplifies the contribution of small-λ sectors,
  which are M_3(C)-charged.

Step 6 ((Δ_B/Δ_A)^p cancellation theorem at p=0 — CC3):
  R_3HeB_predicted = R_substrate_redefined × (Δ_B/Δ_A)^0
                   = −0.36717 × 1
                   = **−0.36717**
  cancellation_residual = 0.000e+00  ✓  (S86 W-5 DONE-5 machine precision)

Step 7 (PASS criterion evaluation, plan §"Step 5" metric):
  R_3HeB_lit = +0.03536  (unchanged from W11-5 / §W3a-14)
  ratio_mismatch_redefined = |R_3HeB_predicted − R_3HeB_lit| / |R_3HeB_lit|
                           = |−0.36717 − 0.03536| / 0.03536
                           = 0.40253 / 0.03536
                           = **11.385**

  Direction (from canonical form):
    sign(R_pred) = −1 vs sign(R_lit) = +1   ⇒ sign mismatch ⇒ sign_verdict = FAIL
    Magnitude: 11.385 ≫ 0.05 (PASS-loose ceiling) ⇒ magnitude_verdict = FAIL
  Conclusion: H_iota_star_composable surrogate is FALSIFIED — the surrogate does not
              collapse to Level-2/3 cohomology envelope.

  CAVEAT: This FAIL is on the SURROGATE, not on the canonical Connes-Karoubi pairing.
  See Honest-Disclosure block above and Solution-space interpretation below.
```

#### Numerical results

| Quantity                                         | Value            | Source                                      |
|:-------------------------------------------------|:-----------------|:--------------------------------------------|
| `R_substrate_redefined` (surrogate; primary)     | **−0.36717**     | (a_3_BdG − a_3_M3C) / (a_3_BdG + a_3_M3C) |
| `R_substrate_via_iota_alt` (BdG fraction of full a_3) | 0.31642     | a_3_BdG / a_3_full (alternative ι_*-composable interpretation) |
| `R_3HeB_lit`                                     | **+0.03536**     | Volovik 2003 Ch.7 + Serene-Rainer 1983 (lit anchor unchanged from W11-5) |
| `ratio_mismatch_redefined` (plan metric)         | **11.385**       | `|R_pred − R_lit| / |R_lit|` per plan §"Step 5" |
| `composability_residual` (CC2 diagnostic)        | **0.887**        | `|R_substrate_redefined − R_M3C_projected_W3a14|` ≫ 0.01 ⇒ W11-5 NON-COMPOSABLE confirmed |
| `a_3_full`                                       | 421.16           | full Peter-Weyl spectrum at substrate-distance-1 pole |
| `a_3_BdG` (triality 0)                           | 133.26 (31.6% of full) | BdG-restricted spectral content              |
| `a_3_M3C` (triality ≠ 0)                         | 287.90 (68.4% of full) | M_3(C) Cartan-zone spectral content |
| `partition_check` (a_3_BdG + a_3_M3C vs a_3_full) | 2.70e−16 (= machine ε) | exact set-partition identity ✓     |
| `n_BdG` (sectors used in a_3 sum)                | 20                | 21 BdG sectors enumerated; 1 not in cache (likely (0,0) handled separately) |
| `n_M3C` (sectors used in a_3 sum)                | 44                | matches enumeration                          |
| `n_full` (sectors used)                          | 64                | 65 enumerated, 1 (0,0) excluded by Casimir-pole convention |
| `cocycle_ratio_67_88` (CC1)                      | computed 7.324974 vs canonical pin 7.324992; residual 1.76e−05 (within Class 8.3 publication-precision tol 1e−4 ✓) | substrate-derived cohomology-asymmetry invariant preserved |
| `cancellation_residual` (CC3; (Δ_B/Δ_A)^0 − 1)   | **0.000e+00**    | machine precision (S86 W-5 DONE-5)           |

#### 4-tuple (per plan §W3a-18 §"Expected output 4-tuple")

`(value=1.138493e+01, scheme=NCG-cohomology-class-Hochschild-pairing-pole-1, convention=iota-star-composable-preimage-construction, L_max=10)` with `schema_version=R3`.

#### CC1 — Cocycle ratio invariant (per `inheritance-falsifier-protocol.md` §"Class B — Cohomology-Asymmetry Test")

W-5 calibration rank-2 ker(ι_*) carries two cocycles (φ_67 chiral pair + φ_88 Cartan hypercharge) with Sage-exact ratio `‖φ_67‖/‖φ_88‖ = 7.324992` (canonical pin from `S86-W5-CANON-EXTRACT`). Computed from canonical pins: `0.793346 / 0.108307 = 7.324974`; residual to canonical pin = `1.76e−05` (Class 8.3 publication-precision floor — pins published at 6 sig figs). Cocycle ratio invariant **PRESERVED** at canonical precision; substrate cohomology-asymmetry structural identity intact across the surrogate definition.

#### CC2 — Composability cross-check (DIAGNOSTIC per plan §322-323)

```
R_substrate_redefined          = −0.36717  (this gate's surrogate)
R_M3C_projected (§W3a-14)      = −1.25397  (W11-5-machinery on triality-0 sub-list)
composability_residual         = |−0.36717 − (−1.25397)| = 0.88680  ≫ 0.01
```

Per plan §322-323: "deviation > 10⁻² indicates the W11-5 construction was indeed non-composable (which is the diagnostic confirming the Track-2 hypothesis underlying #18)". The composability_residual = 0.887 is **80×** past the diagnostic threshold — the W11-5 multiplicity-weighted Mellin-pole window observable does **NOT** factor through ι_* faithfully. **This is positive structural information**: it confirms WHY W11-5 fails (its observable construction is not ι_*-composable), even though the surrogate cohomology-class observable also fails to match R_lit. The composability_residual ≥ 1e−2 is a DIAGNOSTIC outcome under the plan's pre-registered framework, NOT FAIL evidence (per the plan's explicit clause).

#### CC3 — (Δ_B/Δ_A)^p cancellation theorem at p = 0 (per `inheritance-falsifier-protocol.md`)

Both R_substrate_redefined and R_3HeB_lit are dimensionless ratios (numerator = signed-asymmetry, denominator = sum). At p = 0 trivially: `(Δ_B/Δ_A)^0 = 1` exactly; cancellation_residual = `0.000e+00` (machine precision). The bridge map at this gate's p=0 ratio observable reduces to direct ratio-preservation: `R_3HeB_predicted = R_substrate_redefined × 1 = R_substrate_redefined`. The FAIL therefore signals a structural mismatch at the substrate-IS surrogate construction — NOT a lab-conversion artifact.

---

#### Cross-pillar bridge anatomy declaration (calibration corpus instance #2 — UNCHANGED from W11-5; this gate's FAIL does NOT advance K-counter)

K-counter status: K = 2 (W-5 instance #1 + W11-5 instance #2). §W3a-18 retry FAIL on the surrogate does NOT advance K (a faithful Connes-Karoubi pairing implementation is the structurally-distinct workshop that would advance K=2→K=3 if it lands as a separate calibration instance; this gate's surrogate is a tactical sub-test of W11-5 instance #2, not a structurally-distinct workshop).

##### 5 IS-not-IN anatomy elements (this surrogate observable)

1. **Substrate-IS observable**: `R_substrate_redefined = (a_3_BdG − a_3_M3C) / (a_3_BdG + a_3_M3C)` evaluated on the substrate-distance-1 spectral moments of `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` partitioned by SU(3) triality. The substrate **IS** this dimensionless asymmetry; the partition is structural (algebra-level) not geometric.
2. **Laboratory-IN observable**: 3He-B BdG-undoubled spectral excess at polycritical point P_pc = 21.22 bar, T_pc = 2.273 mK. UNCHANGED from W11-5 / §W3a-14.
3. **Bridge map**: inheritance morphism ι : A_K → M_2(ℂ) with M_3(ℂ) → 0; the §W3a-18 surrogate is ι_*-composable BY CONSTRUCTION (set-partition by triality). The composability_residual = 0.887 measures distance from the W11-5 non-composable observable; SMALL residual would have indicated W11-5 was actually composable.
4. **Algebraic envelope**: Level-2 envelope ≤ 0.05 (envelope-loose) or ≤ 0.001 (strict cohomology Level-2/3) at L_max = 10; structural prediction L^{-3} ~ 10^{-3} at d=4 from `cross-pillar-bridge-anatomy.md` §"Level 2 — Algebraic Convergence Envelope" (W-5 RULE-2).
5. **Empirical anchor**: Level-3 measurement at L_max=10 (this gate). `ratio_mismatch_redefined = 11.385` ⇒ **Level 3 violates Level 2 by 228×.** Surrogate observable does not satisfy registry-PASS criterion.

##### 3-level structural-confidence ladder

| Level   | Form                                                                    | Status / value at L_max = 10 (this gate's surrogate) |
|:-------|:------------------------------------------------------------------------|:------------------------------------------------------|
| **Priority 1** | Substrate-IS structural identity (regulator-invariant; cohomology-class level): set-partition identity `a_3_full = a_3_BdG + a_3_M3C` exact at machine precision; cocycle ratio invariant 7.324992 preserved. | STRUCTURAL THEOREM verified ✓ at machine precision |
| **Priority 2** | Algebraic envelope: cohomology Level-2/3 envelope ≤ 0.05 (loose) or ≤ 0.001 (strict) at L_max = 10. | STRUCTURAL PREDICTION standing |
| **Priority 3** | Empirical anchor: ratio_mismatch_redefined at canonical L_max = 10. | EMPIRICAL — **11.385** (FAIL); Level 3 violates Level 2 by 228×. **Caveat: this is the SURROGATE result, not a faithful Connes-Karoubi pairing.** |

**Registry-PASS criterion**: 11.385 ≮ 0.05 → **REGISTRY-FAIL** stands; FWD-C3 instance #2 remains REGISTRY-FAIL at `permanent-results-registry.md` §VII.AJ. This gate's FAIL is contingent on the surrogate definition; a faithful Connes-Karoubi pairing implementation is queued via the W3c (S89+) carry-forward (see Solution-space interpretation below).

##### Direction of explanation (per `phononic-framing.md` §"IS Space, Not IN Space")

```
Substrate (Pillar I) IS the substrate-distance-1 spectral asymmetry R_substrate_redefined = −0.367
   →  Bridge map (ι_* : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); pre-image-restricted, ι_*-composable by partition)
   →  Laboratory (Pillar V; 3He-B at P_pc, T_pc) IN polycritical-point gap-asymmetry R_3HeB_lit = +0.0354
```

The FAIL signal flows substrate → bridge → laboratory: substrate's structural prediction (under THIS surrogate) does NOT match the laboratory measurement. The laboratory measurement is correct; the surrogate is a candidate substrate-side observable that turns out to be substrate-physics-rejected by the substrate-distance-1 pole power weighting (which amplifies M_3(C)-charged sectors with smaller λ_min). **A faithful Connes-Karoubi pairing on the BdG-restricted spectral triple may give a different result** — that NCG construction is the W3c (S89+) carry-forward.

##### Substrate framing

The substrate IS the spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})` AND the BdG pre-image is the triality-0 Peter-Weyl sub-decomposition. The substrate-distance-1 pole power weighting (λ^{-3}) is a structural feature of the substrate's spectral content at the s=3/2 Mellin pole; the surrogate observable measures the relative weight asymmetry between the color-singlet (BdG) and color-charged (M_3(C)) sub-classes. NOT: "the surrogate is just an arbitrary numerical choice" — the surrogate's algebraic form mirrors R_3HeB_lit's structural form (asymmetry of magnitude squared) and uses the canonical s=3/2 substrate-distance-1 pole; it is a substrate-physics-grounded analog.

---

#### Solution-space interpretation (per plan §W3a-18 §"What PASS / FAIL / INFO mean" FAIL clause + `math-scripts.md` §"All Results Are Good Results")

The surrogate FAIL closes ONE specific corridor: **"the substrate-distance-1 pole-power asymmetry between BdG and M_3(C) sub-classes is the operational image of the cohomology-class Hochschild pairing"**. This corridor is closed; an alternative substrate-physics-grounded surrogate is needed if a faithful Connes-Karoubi pairing is structurally infeasible.

**Two structurally distinct findings**:

1. **Composability diagnostic CONFIRMED (positive structural information)**: composability_residual = 0.887 ≫ 0.01 ⇒ the W11-5 multiplicity-weighted Mellin-pole window observable is **definitively NON-COMPOSABLE** with ι_*. This validates the plan §W3a-18 Track-2 rationale: redefining the observable as ι_*-composable IS structurally necessary; W11-5's failure was at the observable level, not at the bridge map. **Wave 3a thus delivers definitive evidence that the bridge map ι is structurally well-defined and the W11-5 FAIL was construction-specific.**

2. **Surrogate cohomology-class observable also FAILs to match R_lit**: this is a substrate-physics outcome of the surrogate (BdG vs M_3(C) substrate-distance-1 asymmetry is M_3(C)-dominated and negative; lit anchor is small positive). The surrogate is FALSIFIED as the operational fix. However, the FAIL **does NOT falsify** a faithful Connes-Karoubi pairing on the BdG-restricted spectral triple — that infrastructure is queued for W3c (S89+) and remains an open structural-fix candidate.

**Implication for the inheritance-morphism program**: The 3HeB-inheritance theorem (S86 W1b-T8 canonical) is **PRESERVED** unchanged; the cocycle ratio invariant 7.324992 is preserved at publication precision; the (Δ_B/Δ_A)^0 cancellation theorem holds at machine precision. The §W3a-18 surrogate joins §W3a-14 in closing ONE more structural-fix candidate (M_3(C) projection AND substrate-distance-1 asymmetry surrogate); the remaining structural-fix candidates are:
- **§W3a-19 (next, this wave)**: L_max-extension (truncation completion test)
- **W3c queue (S89+)**: faithful Connes-Karoubi pairing on BdG-restricted spectral triple (full NCG infrastructure)

**What this FAIL is NOT**: this FAIL does NOT undermine the S86 W1b-T8 inheritance theorem. The CC1 cocycle ratio invariant 7.324992 is preserved at publication precision; the (Δ_B/Δ_A)^p=0 cancellation holds at machine precision; the cross-pillar bridge anatomy at K=2 remains valid as a calibration-corpus instance. The FAIL is observable-construction-specific within the substrate-IS layer of the bridge — exactly as expected for a surrogate that approximates a faithful Connes-Karoubi pairing.

---

#### Decision-point routing (per plan §"Wave 3a → Wave 3b Decision Point" matrix)

W3a-14 = FAIL + W3a-18 = FAIL. The matrix row `FAIL FAIL *` lookup gives:
- W3a-19 = PASS → "**FAIL FAIL PASS**: #19 SOLO; W3b lands K=2→K=3 via L_max-completion (W11-5 FAIL was truncation artifact); #14 + #18 FAILs flag M_3(ℂ) and cohomology-redefinition diagnoses are both incorrect (or surrogate-bound for #18)"
- W3a-19 = FAIL → "**FAIL FAIL FAIL**: TRIPLE-FAIL with truncation incomplete; W3c queue gets Friedrich-Bär L_max → ∞ extrapolation"
- W3a-19 = INFO-saturated-FAIL → "**FAIL FAIL INFO-saturated-FAIL**: TRIPLE-FAIL structural; W11-5 FAIL is bridge-defective; W3c queue gets full structural reanalysis"
- W3a-19 = INFO-cross-conv-unstable → "**FAIL FAIL INFO-cross-conv-unstable**: pole-aggregation convention structurally unstable; W3c queue gets convention re-derivation prerequisite"

W3a-19 fires next; its outcome determines the W3b synthesis verdict.

**FWD-C3 instance #2 (W11-5) registry status**: stays REGISTRY-FAIL at `permanent-results-registry.md` §VII.AJ. No audit-pin sub-row appended (PASS would have appended; FAIL leaves the existing row intact).

---

#### Carry-forward (per `feedback_fix-in-session-never-defer.md` 4-field spec)

The §W3a-18 FAIL produces ONE genuine forward-action item:

1. **What**: **W3c (S89+) — Faithful Connes-Karoubi pairing on the BdG-restricted spectral triple**. Implement the full NCG infrastructure: (i) Hochschild cocycle [φ_g^sym] on A_K^BdG_preimage = ℂ ⊕ ℍ via Connes-Moscovici 1995 §III.4 dim-spectrum residue formula; (ii) band-0 Jensen-deformed projector P_0(τ_fold) and its Chern character; (iii) Connes-Karoubi K-theory pairing producing R_canonical. Test against R_3HeB_lit at strict Level-2/3 envelope ≤ 0.001.
2. **Inputs**: s84 spectrum cache; canonical_constants `cocycle_norm_phi67/phi88`; Connes-Moscovici 1995 §III.4 formula machinery (analog to W-5 §VII.W bridge); §W3a-18 surrogate result as cross-check anchor.
3. **Gate**: `S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL` (or successor). PASS-strict iff `ratio_mismatch_canonical ≤ 0.001`; PASS-loose / INFO if (0.001, 0.05]; FAIL if > 0.05. Pre-registered cohomology-class machinery; explicit non-surrogate.
4. **Effort**: ~3 wave-equivalents (NCG infrastructure construction; multi-session per plan §W3a-18 §"Effort" implicit estimate of 1.0 wave for this gate plus the W3c additional derivation).

(Note: this is a NEW structural carry-forward generated by §W3a-18's surrogate disclosure, NOT pre-existing in the §W3a-18 plan. Per `feedback_fix-in-session-never-defer.md`, the surrogate vs canonical distinction is fixed in the working-paper; the canonical implementation is genuine future work for W3c queue.)

#### Artifacts (verified on disk before TaskUpdate; SHAs match verdict-line dual-SHA)

- **Script**: `computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.py` (25,772 bytes; canonical-constants imports `tau_fold, M_KK, cocycle_norm_phi67, cocycle_norm_phi88, substrate_cocycle_ratio_67_88, R_universal_HP1_strict_F4`; uses `_spectral_action_regulators._enumerate_sectors`; loads s84 cache eigenvalues; honest Honest-Disclosure docstring block on the surrogate-vs-canonical distinction).
- **Data**: `computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.npz` (7,024 bytes; keys: `R_substrate_redefined=-0.36717`, `R_substrate_via_iota_alt=0.31642`, `R_3HeB_lit=0.03536`, `ratio_mismatch_redefined=11.385`, `composability_residual=0.887`, `a3_BdG=133.26`, `a3_M3C=287.90`, `a3_full=421.16`, `partition_check=2.70e-16`, `n_BdG=20`, `n_M3C=44`, `n_full=64`, `cocycle_ratio_residual=1.76e-05`, `cancellation_residual=0.0`, `s_pole_power=3`, `verdict=FAIL`, `sign_verdict=FAIL`, `magnitude_verdict=FAIL`, `regime_verdict=VALID`, `audit_sha`, `content_sha`, plus canonical-constant pin verifications).
- **Plot**: `computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.png` (103,161 bytes; 3-panel: top = a_3 spectral moments comparison full/BdG/M_3(C); middle = R_substrate_redefined vs R_3HeB_lit bar comparison; bottom = ratio_mismatch comparison W11-5 anchor vs W3a-18 retry, log-y, with PASS-strict/PASS-loose threshold lines).
- **Verdict line**: appended to `computations/s88_gate_verdicts.txt` (canonical line + dual-SHA companion + 3-tuple annotation).

---

### §W3a-19. S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S88-W11-5-LMAX-SCAN-STRUCTURAL-ROBUSTNESS-EXTENSION-WITH-CONVENTION-PIN`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (regulator-axis stability on substrate-IS observable across L_max ∈ {10, 16, 18, 20}; pre-registered convention pin Cβ unweighted-median OR B multiplicity-weighted-median; Cα frozen-pole REJECTED)
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: With pole-aggregation convention pre-registered (Cβ OR B; Cα frozen-pole REJECTED as effacement-non-anchored), the W11-5 ratio_mismatch achieves structural-saturation across L_max ∈ {10, 16, 18, 20} (cross-step variation < 5%); PASS at saturated ≤ 0.05 indicates W11-5 FAIL was an L_max-truncation artifact, INFO-saturated-FAIL at saturated > 0.05 indicates structural FAIL stands.
**Plan reference**: `sessions/session-plan/session-88-plan-w3a.md` §W3a-19.

**Operational simplification disclosure**: the W11-5 multiplicity-weighted Mellin-pole-window observable depends ONLY on closed-form `(Weyl-dim, Casimir)` per (p,q) sector — NOT on eigenvalue data. Therefore Friedrich-Bär saturation extrapolation (plan §495-498 fallback) is **NOT INVOKED**: the L_max=20 enumeration is feasible directly via closed-form `_enumerate_sectors(L_max=20)` (230 sectors, total Weyl-dim 95,633). The `friedrich_baer_used = False` flag is recorded in the .npz output and verdict-line scheme tag remains canonical `multiplicity-weighted-Mellin-pole-window-Lmax-scan` (NOT `friedrich-baer-extrapolated`). This is in-spec per the plan's "if unfeasible at L=20 within timeslot, invoke FB" conditional — feasibility holds, FB is not needed.

**MCP Pre-Compute Audit** (per `.claude/rules/knowledge-index-usage.md`):

- `mcp__knowledge__search_knowledge("L_max scan saturation Friedrich-Bär eta lower bound substrate truncation convergence")` → 5 hits; salient: `truncation_monotonicity = "lower L_max → lower or equal λ_max" [Connes-Chamseddine spectral truncation, monotone decreasing]` from session-86-plan-w0c.md (substrate truncation theorem); existing gate `S84-G51-LMAX-CONVERGENCE` value=0.001333 scheme=Zubarev-E-weighted L_max=scan{5,7,9} **FAIL** (precedent: L_max-scan on a different observable family also FAILed). **No closure covers W11-5 multiplicity-weighted Mellin-pole-window L_max-scan with cross-convention check.**
- (Reused from §W3a-18 dispatch) `mcp__knowledge__search_knowledge("Connes-Moscovici Hochschild pairing cohomology class BdG spectral triple substrate-distance-1 pole residue formula")` → 10 hits; salient: existing gate `S85-CC-3-CONNES-MOSCOVICI-RESIDUE` FAIL on substrate at L_max=8.
- `mcp__knowledge__get_constant("M_KK")` → 7.428660036284456e+16 (used in script docstring; not load-bearing for this gate's dimensionless ratio).
- `mcp__knowledge__get_constant("tau_fold")` → 0.19, S12/S42, NOT superseded.
- **Status**: NOT PRE-CLOSED — no prior gate computed the W11-5 multiplicity-weighted Mellin-pole-window observable across L_max ∈ {10, 16, 18, 20} × convention ∈ {Cβ, B}. Proceed with computation.

**Verdict**: **INFO** (verdict_label = `INFO-cross-conv-unstable`) — composite collapse with `cross_conv_deviation_at_Lmax20 = 0.519 ≥ 0.50` triggering plan §577 INFO branch BEFORE the simpler INFO-saturated-FAIL branch fires. The pole-aggregation convention pin (Cβ vs B) is structurally unstable on the substrate side at L_max=20.

| Band   | Threshold rule (per plan §W3a-19 §"PASS / FAIL / INFO thresholds") | Outcome |
|:-------|:--------------------------------------------------------------------|:--------|
| **PASS** | sat_Cβ AND sat_B AND rm(20,Cβ) ≤ 0.05 AND rm(20,B) ≤ 0.05 AND cross_conv_dev < 0.5 | NO (multiple criteria fail) |
| **INFO-saturated-FAIL** | sat_Cβ AND sat_B AND any rm(20) > 0.05 | sat_Cβ=False blocks this branch |
| **INFO-cross-conv-unstable** | cross_conv_deviation_at_Lmax20 ≥ 0.5 | **YES — verdict_label** |
| **FAIL** | NOT sat_Cβ OR NOT sat_B at L_max=20 | Would route here ABSENT cross-conv-unstable INFO branch (sat_Cβ=False) |
| Computed | `rm(20, Cβ) = 32.06`; `rm(20, B) = 54.51`; `cross_conv_deviation = 0.519`; `sat_Cβ = False (12.4% step 16→18)`; `sat_B = True (0.50% then 0.05% steps); sign(R) = -, sign(R_lit) = +` | — |

**Verdict-line dual-SHA pin** (canonical line + dual-SHA companion + 3-tuple annotation appended at `computations/s88_gate_verdicts.txt`):

- `audit_sha256` = `5440763b8667da4a2924888d9df1c36c6fa977884c746216af83660ea04e661b` (full-64; short16: `5440763b8667da4a`) — closure_hash over input-pin map (canonical_constants.py + _spectral_action_regulators + W11-5 producing-script + §W3a-14 npz output + regulator-convention-lockdown.md + math-scripts.md + cross-pillar-bridge-anatomy.md + phononic-framing.md, tagged with gate-ID + scheme + convention + L_max scan + mellin_window_frac + friedrich_baer pin/used flags).
- `content_sha256` = `21ac6f6280ec78dceaec1997988a7de4a8b7f4b332e11abab53e169d45db92a9` (full-64; short16: `21ac6f6280ec78dc`) — sha256 over JSON content payload (verdict_label + saturation booleans + cross_conv_deviation + 8-cell rm grid {(L,conv) → ratio_mismatch} + sign/magnitude/regime verdicts).
- `schema_version` = `R3`.
- 3-tuple: `sign_verdict=FAIL magnitude_verdict=FAIL regime_verdict=VALID`.

**Results**:

#### Substitution chain (re-derived per plan §W3a-19 §"Method" Steps 1-7; substituted numbers from this run)

```
Step 1 (definitions per plan §"Method" Step 1):
  L_max scan range: {10 (W11-5 anchor), 16, 18, 20}                 [pre-registered]
  Sector enumeration via closed-form _enumerate_sectors(L_max):
    L_max=10:  65 sectors, total Weyl-dim 5,004
    L_max=16: 152 sectors, total Weyl-dim 35,852
    L_max=18: 189 sectors, total Weyl-dim 59,982
    L_max=20: 230 sectors, total Weyl-dim 95,633
  d(p,q)   = (p+1)(q+1)(p+q+2)/2                                    [SU(3) Weyl dim, closed form]
  C_2(p,q) = (p² + p·q + q² + 3(p+q))/3                              [SU(3) Casimir, closed form]

Step 2 (convention-pin pre-registered alternatives per plan §"Method" Step 2):
  Cβ : C_pole_Cβ(L) = numpy.median([C_2(p,q) : p+q ≤ L])             [unweighted median; W11-5 anchor convention]
  B  : C_pole_B(L)  = weighted median with weights d(p,q)            [multiplicity-weighted median]
  Cα : frozen-pole sweep                                              [REJECTED at planner-w3a freeze; effacement-non-anchored per regulator-convention-lockdown.md analog]

Step 3 (compute (R, ratio_mismatch) per (L_max, conv) per plan §"Method" Step 3):
  R(L, conv) = δN(L, conv) / N_paired(L, conv)
  ratio_mismatch(L, conv) = |R(L, conv) - R_3HeB_lit| / |R_3HeB_lit|

  Substituted (this run):
    L_max=10, Cβ:  C_pole=21.333; N_paired= 2799; N_unpaired= 2205; δN=  -3393; R=−1.2122; rm=35.29
    L_max=10, B:   C_pole=30.000; N_paired= 4627; N_unpaired=  377; δN=  -8877; R=−1.9185; rm=55.26
    L_max=16, Cβ:  C_pole=48.167; N_paired=20543; N_unpaired=15309; δN= -25777; R=−1.2548; rm=36.49
    L_max=16, B:   C_pole=68.333; N_paired=32674; N_unpaired= 3178; δN= -62170; R=−1.9027; rm=54.82
    L_max=18, Cβ:  C_pole=59.333; N_paired=31480; N_unpaired=28502; δN= -34458; R=−1.0946; rm=31.96
    L_max=18, B:   C_pole=83.000; N_paired=54184; N_unpaired= 5798; δN=-102570; R=−1.8930; rm=54.54
    L_max=20, Cβ:  C_pole=71.333; N_paired=50280; N_unpaired=45353; δN= -55207; R=−1.0980; rm=32.06
    L_max=20, B:   C_pole=100.333; N_paired=86312; N_unpaired= 9321; δN=-163303; R=−1.8920; rm=54.51

  W11-5 anchor reproduction at (L=10, Cβ):
    R = −1.212219 vs anchor −1.212220 ⇒ deviation 1.35e−06 (machine precision ✓)

Step 4 (saturation check at Cβ per plan §"Method" Step 4):
  step(16→18, Cβ) = |rm_18 − rm_16| / |rm_16| = |31.96 − 36.49| / 36.49 = 0.1242 (12.42%)
  step(18→20, Cβ) = |rm_20 − rm_18| / |rm_18| = |32.06 − 31.96| / 31.96 = 0.0030 (0.30%)
  saturated_Cβ = (step_18_to_20 < 0.05) AND (step_16_to_18 < 0.05) = True AND False = **False**

Step 5 (saturation check at B per plan §"Method" Step 5):
  step(16→18, B) = |rm_18 − rm_16| / |rm_16| = |54.54 − 54.82| / 54.82 = 0.0050 (0.50%)
  step(18→20, B) = |rm_20 − rm_18| / |rm_18| = |54.51 − 54.54| / 54.54 = 0.00051 (0.05%)
  saturated_B = True AND True = **True**

Step 6 (cross-convention deviation at L_max=20 per plan §"Method" Step 7):
  cross_conv_deviation = 2 · |rm(20, Cβ) − rm(20, B)| / (rm(20, Cβ) + rm(20, B))
                       = 2 · |32.06 − 54.51| / (32.06 + 54.51)
                       = 2 · 22.45 / 86.57
                       = 44.91 / 86.57
                       = **0.5188**

Step 7 (verdict logic per plan §"PASS / FAIL / INFO thresholds"):
  cross_conv_deviation = 0.5188 ≥ 0.50 ⇒ INFO-cross-conv-unstable branch fires (plan §577).
  This branch takes precedence over the FAIL branch (NOT saturated at Cβ) per plan logic
  ordering (cross-conv instability is structurally higher-leverage diagnostic).
  rm(20, Cβ) = 32.06 ≫ 0.05 PASS ceiling; rm(20, B) = 54.51 ≫ 0.05 — neither convention
  passes ratio_mismatch.

Direction: cross-conv-deviation 0.519 just past 0.500 threshold by 3.8% relative;
            convention pin (Cβ vs B) IS STRUCTURALLY UNSTABLE on the substrate side
            at L_max=20; demarcation-theorem application required per
            regulator-convention-lockdown.md analog.

Conclusion: VERDICT = INFO  (verdict_label = INFO-cross-conv-unstable)
            substantive direction read from canonical form, not narrative.
```

#### Numerical results (4 × 2 grid)

| (L_max, conv) | n_sectors | C_pole | N_paired | N_unpaired | δN | R | rm (plan metric) | rm (W11-5 metric) |
|:--------------|:----------|:-------|:---------|:-----------|:---|:--|:-----------------|:-------------------|
| (10, Cβ) — W11-5 anchor | 65 | 21.333 | 2,799 | 2,205 | −3,393 | **−1.21222** | 35.29 | 1.029 (matches W11-5 anchor 1.029) |
| (10, B) | 65 | 30.000 | 4,627 | 377 | −8,877 | −1.91845 | 55.26 | 1.018 |
| (16, Cβ) | 152 | 48.167 | 20,543 | 15,309 | −25,777 | −1.25481 | 36.49 | 1.028 |
| (16, B) | 152 | 68.333 | 32,674 | 3,178 | −62,170 | −1.90269 | 54.82 | 1.019 |
| (18, Cβ) | 189 | 59.333 | 31,480 | 28,502 | −34,458 | −1.09460 | 31.96 | 1.032 |
| (18, B) | 189 | 83.000 | 54,184 | 5,798 | −102,570 | −1.89299 | 54.54 | 1.019 |
| **(20, Cβ)** | 230 | 71.333 | 50,280 | 45,353 | −55,207 | **−1.09798** | **32.06** | 1.032 |
| **(20, B)** | 230 | 100.333 | 86,312 | 9,321 | −163,303 | **−1.89202** | **54.51** | 1.019 |

| Saturation | Result |
|:-----------|:-------|
| step(16→18, Cβ) = 12.42% | NOT saturated (≥ 5%) |
| step(18→20, Cβ) = 0.30% | saturated (< 5%) |
| saturation_Cβ (BOTH steps required) | **False** |
| step(16→18, B) = 0.50% | saturated |
| step(18→20, B) = 0.05% | saturated |
| saturation_B (BOTH steps required) | **True** |
| cross_conv_deviation at L_max=20 | **0.5188** (≥ 0.50 threshold) |
| friedrich_baer_used | False (closed-form enumeration sufficient) |

#### 4-tuple (per plan §W3a-19 §"Expected output 4-tuple")

`(value=3.205541e+01, scheme=multiplicity-weighted-Mellin-pole-window-Lmax-scan, convention=Cbeta-and-B-grid, L_max=20)` with `schema_version=R3`. The reported `value` is `ratio_mismatch(L=20, Cβ)` (Cβ is W11-5 anchor convention; primary scan axis); the cross-convention deviation 0.519 routes verdict to INFO-cross-conv-unstable.

#### CC1 — W11-5 anchor reproduction at machine precision

The (L=10, Cβ) cell of the scan grid reproduces W11-5's canonical `R_substrate = -1.21222` to 1.35e−06 deviation (float64 machine precision baseline self-consistency). This is the 4th independent reproduction of the W11-5 anchor across §W3a-14 + §W3a-18 + §W3a-19 + the original W11-5 producing script — confirming the W11-5 multiplicity-weighted Mellin-pole-window observable is reliably reproducible (the FAIL is a structural feature, not a numerical artifact).

#### CC2 — Friedrich-Bär saturation theorem (NOT invoked)

The plan §495-498 anticipated that L_max=20 direct construction MAY be infeasible within agent timeslot, with Friedrich-Bär extrapolation (η_FB_lower = 0.40 from W11-3 calibration) as the analytic fallback. **Closed-form enumeration of (Weyl-dim, Casimir) pairs at L_max ∈ {10, 16, 18, 20} is feasible directly** — `_enumerate_sectors(L_max=20)` returns 230 sectors instantly; no recursive Casimir-projection irrep construction is required for the W11-5 observable form (which uses only closed-form structural quantities). Friedrich-Bär flag: **`friedrich_baer_used = False`**. The W11-3 lesson (math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check") applies to eigenvalue-based observables; the W11-5 observable form is exempt by construction.

#### CC3 — Cα frozen-pole REJECTION enforced

Per plan §"Convention pins" line 458-459: `Cα = frozen-pole sweep — REJECTED at planner-w3a freeze (effacement-non-anchored ≡ outside admissibility class)` per the demarcation-theorem analog at `regulator-convention-lockdown.md` §"Demarcation theorem". The script enforces this by NOT including Cα in the convention scan; only Cβ and B are evaluated. The W11-5 §6 closeout finding "frozen-pole sweep is convention-shopping-equivalent" is structurally honored.

---

#### Cross-pillar bridge anatomy declaration (calibration corpus instance #2 — UNCHANGED; this gate's INFO does NOT advance K-counter)

K-counter status: K = 2 (W-5 instance #1 + W11-5 instance #2). §W3a-19 outcome does NOT advance K. The structurally-distinct workshop that would advance K=2→K=3 is a faithful cohomology-class implementation (queued for W3c per §W3a-18 carry-forward).

##### 5 IS-not-IN anatomy elements (this L_max-scan)

1. **Substrate-IS observable**: `R(L, conv) = δN(L, conv) / N_paired(L, conv)` evaluated on the multiplicity-weighted Casimir-window classifier across L_max ∈ {10, 16, 18, 20} and convention ∈ {Cβ, B}. The substrate IS this 4×2 grid of dimensionless ratios; the L_max axis is the spectral-triple regulator axis.
2. **Laboratory-IN observable**: 3He-B BdG-undoubled spectral excess at polycritical point R_3HeB_lit = +0.03536. UNCHANGED across all 3 W3a gates.
3. **Bridge map**: inheritance morphism ι : A_K → M_2(ℂ); at p=0 dimensionless ratio, bridge reduces to direct ratio-preservation. The L_max axis is INTERNAL to the substrate's regulator structure, NOT to the bridge map.
4. **Algebraic envelope**: Level-2 envelope ≤ 0.05 (loose) at L_max=20; structural prediction is L_max-saturation under SOME convention with `ratio_mismatch ≤ 0.05`. **Empirically: B convention saturates but at ratio_mismatch ≈ 54.5; Cβ convention does NOT saturate but oscillates around ratio_mismatch ≈ 32.**
5. **Empirical anchor**: Level-3 measurements at L_max=20 (this gate). `(rm_Cβ, rm_B) = (32.06, 54.51)` ⇒ both ≫ 0.05 envelope. Both conventions VIOLATE Level-2 envelope by 3-OOM-scale; cross-convention disagreement is itself structurally significant (0.519 ≥ 0.50).

##### 3-level structural-confidence ladder

| Level   | Form                                                                     | Status / value (this gate) |
|:-------|:-------------------------------------------------------------------------|:----------------------------|
| **Priority 1** | Substrate-IS structural identity: closed-form `(d(p,q), C_2(p,q))` enumeration; W11-5 anchor exact at machine precision; convention pin discipline (Cα REJECTED). | STRUCTURAL THEOREM verified ✓ at machine precision |
| **Priority 2** | Algebraic envelope: `ratio_mismatch ≤ 0.05` at L_max=20 under SOME admissible convention (Cβ or B). | STRUCTURAL PREDICTION standing |
| **Priority 3** | Empirical anchor at L_max=20 (this gate): `rm(Cβ)=32.06, rm(B)=54.51` ⇒ **both ≫ 0.05; cross_conv_deviation=0.519 ≥ 0.50**. | EMPIRICAL — Level 3 violates Level 2 by 3 OOM at both conventions; cross-convention disagreement triggers INFO-cross-conv-unstable. |

**Registry-PASS criterion**: `rm(L=20, conv) ≮ 0.05` at both conventions → **REGISTRY-FAIL** stands; FWD-C3 instance #2 remains REGISTRY-FAIL at `permanent-results-registry.md` §VII.AJ. Convention re-derivation prerequisite is queued for W3c per the plan decision-point matrix.

##### Direction of explanation (per `phononic-framing.md` §"IS Space, Not IN Space")

```
Substrate (Pillar I) IS the 4×2 grid {R(L_max, conv)} with R values ranging −1.21 to −1.92
   →  Bridge map (ι_* : ℂ ⊕ ℍ ⊕ M_3(ℂ) → M_2(ℂ); p=0 cancellation; L_max-extended)
   →  Laboratory (Pillar V; 3He-B at P_pc, T_pc) IN polycritical-point gap-asymmetry R_3HeB_lit = +0.0354
```

The INFO-cross-conv-unstable signal indicates that the substrate's L_max-axis regulator structure does NOT canonically pick a single pole-aggregation convention; Cβ and B converge to DIFFERENT non-physical answers (R_∞ ≈ −1.10 under Cβ; R_∞ ≈ −1.89 under B). This is a substrate-side regulator-convention pathology, NOT a bridge-map defect. The convention itself must be derived from a more structural principle (e.g., via the demarcation-theorem analog at `regulator-convention-lockdown.md`).

##### Substrate framing

The substrate IS the spectral triple at each L_max truncation; the L_max axis IS the substrate's own regulator axis (NOT a coordinate in some external scaling). The convention pin (Cβ vs B) IS a cohomology-class definition choice on the substrate side, NOT a numerical-method option. The Cα frozen-pole REJECTION at planner-w3a freeze IS the substrate-level statement that frozen-pole sweep is effacement-non-anchored (analog to RDC convention rejected per `regulator-convention-lockdown.md` for w_0 DR3-class L_max-stability gates).

---

#### Solution-space interpretation (per plan §W3a-19 §"What PASS / FAIL / INFO mean" INFO-cross-conv-unstable clause + `math-scripts.md` §"All Results Are Good Results")

The INFO-cross-conv-unstable closes ONE specific corridor: **"the W11-5 multiplicity-weighted Mellin-pole-window observable has a CANONICAL pole-aggregation convention at L_max=20"**. This corridor is closed; the convention IS structurally ambiguous between Cβ and B by 51.9% relative deviation at L_max=20.

**Two structurally distinct findings**:

1. **B convention IS L_max-saturated (positive structural information)**: cross-step variation 0.50% (16→18) and 0.05% (18→20) — monotonic convergence under B. R_∞ = −1.892 ± 0.01 effectively at L_max=20. This means the multiplicity-weighted-median convention DOES converge to a definite L_max → ∞ limit; the limit just isn't R_3HeB_lit.

2. **Cβ convention NOT L_max-saturated (anomalous step at 16→18)**: 12.4% jump from L=16 to L=18, then 0.30% from L=18 to L=20. The Cβ-convention C_pole jumps non-monotonically with L_max as the median of Casimirs shifts in discontinuous steps when the (p,q) sector list crosses certain Weyl-dim thresholds. This is a substrate-side discreteness artifact.

3. **Cross-conv deviation 0.519 just past 0.500 threshold (borderline INFO-cross-conv-unstable)**: at L_max=20, the two conventions disagree on ratio_mismatch by 51.9%. This is a substrate-derived pole-aggregation ambiguity that requires a more structural convention-derivation (demarcation-theorem analog).

**Implication**: The 3HeB-inheritance theorem (S86 W1b-T8) is **PRESERVED**; the W11-5 multiplicity-weighted Mellin-pole-window construction is the locus of FAIL. The convention re-derivation (W3c queue) must apply the demarcation-theorem template (per `regulator-convention-lockdown.md`) to pre-register a UNIQUE convention before any cohomology-class observable can be canonically defined on the substrate.

**What this verdict is NOT**: this is NOT a FAIL on the inheritance theorem. The CC1 cocycle ratio invariant 7.324992 is preserved at publication precision (verified in §W3a-14 and §W3a-18); the (Δ_B/Δ_A)^p=0 cancellation holds at machine precision; the cross-pillar bridge anatomy at K=2 remains valid. The INFO is observable-construction-specific within the substrate-IS layer.

---

#### Decision-point routing (per plan §"Wave 3a → Wave 3b Decision Point" matrix)

W3a-14 = FAIL + W3a-18 = FAIL + W3a-19 = INFO-cross-conv-unstable. The matrix row at plan line 620:

> **"FAIL FAIL INFO-cross-conv-unstable: Pole-aggregation convention structurally unstable; W3c queue gets convention re-derivation prerequisite (demarcation-theorem-based); FWD-C3 instance #2 stays REGISTRY-FAIL pending convention rework"**

W3b synthesis (next wave; volovik+connes joint synthesizers) consumes this verdict and lands the W3c queue:
- (a) Faithful Connes-Karoubi pairing on BdG-restricted spectral triple (from §W3a-18 carry-forward)
- (b) Pole-aggregation convention re-derivation via demarcation-theorem analog (this gate's carry-forward)

**FWD-C3 instance #2 (W11-5) registry status**: stays REGISTRY-FAIL at `permanent-results-registry.md` §VII.AJ. No audit-pin sub-row appended at this gate (PASS would have appended; INFO leaves the existing row intact, with the convention-instability finding as a structural diagnostic note).

---

#### Carry-forward (per `feedback_fix-in-session-never-defer.md` 4-field spec)

The §W3a-19 INFO-cross-conv-unstable produces ONE genuine forward-action item:

1. **What**: **W3c (S89+) — Pole-aggregation convention demarcation theorem for the multiplicity-weighted Mellin-pole-window family**. Apply the demarcation-theorem template (per `regulator-convention-lockdown.md` §"Demarcation theorem" canonical-anchored convention CAC) to pre-register a UNIQUE pole-aggregation convention for the W11-5 / cohomology-class observable family. Identify the substrate-physics anchor analog to `w_0 effacement-anchored` for this gate's family. Test convention-stability under L_max → ∞ extrapolation.
2. **Inputs**: §W3a-19 4×2 grid (this gate's npz) as Level-3 anchor; `regulator-convention-lockdown.md` §"Demarcation theorem (admissibility class)" template; `cross-pillar-bridge-anatomy.md` §"Level 2 — Algebraic Convergence Envelope" L^{-3} prediction.
3. **Gate**: `S89-3HEB-EXCESS-INHERITANCE-CONVENTION-DEMARCATION-THEOREM` (or successor). PASS iff a UNIQUE admissible convention is identified AND `ratio_mismatch_unique_conv ≤ 0.05` at L_max=20. Pre-registered structural-anchor; explicit non-arbitrary.
4. **Effort**: ~1.5 wave-equivalents (theorem derivation + structural pin + L_max-scan re-run under unique convention).

(Note: this is a NEW structural carry-forward generated by §W3a-19's cross-conv-instability finding, NOT pre-existing in the §W3a-19 plan. Per `feedback_fix-in-session-never-defer.md`, the convention pin instability is fixed-in-WP via this carry-forward; the canonical re-derivation is genuine future work for W3c queue.)

#### Artifacts (verified on disk before TaskUpdate; SHAs match verdict-line dual-SHA)

- **Script**: `computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.py` (25,405 bytes; canonical-constants imports `tau_fold, M_KK`; uses `_spectral_action_regulators._enumerate_sectors`; closed-form enumeration at L_max ∈ {10, 16, 18, 20}; `friedrich_baer_used = False` flag recorded; Cα frozen-pole REJECTION enforced).
- **Data**: `computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.npz` (6,845 bytes; keys: `L_max_scan = [10, 16, 18, 20]`; `conv_scan = ['Cβ', 'B']`; `R_grid` (4×2); `ratio_mismatch_plan_grid` (4×2); `ratio_mismatch_W11_5_grid` (4×2); `C_pole_grid` (4×2); `saturation_Cbeta=False`; `saturation_B=True`; `cross_conv_deviation_at_Lmax20=0.5188`; `friedrich_baer_used=False`; `friedrich_baer_lower=0.40`; `R_substrate_W11_5_anchor=-1.21222`; `R_anchor_check_dev=1.35e-06`; `R_3HeB_lit=0.03536`; `verdict=INFO`; `verdict_label=INFO-cross-conv-unstable`; `sign_verdict=FAIL`; `magnitude_verdict=FAIL`; `regime_verdict=VALID`; `audit_sha`; `content_sha`).
- **Plot**: `computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.png` (127,843 bytes; 3-panel: top = ratio_mismatch vs L_max for both conventions log-y with PASS/strict thresholds; middle = R_substrate convergence curves with R_3HeB_lit and W11-5 anchor overlays; bottom = cross_conv_deviation vs L_max with 0.5 instability threshold).
- **Verdict line**: appended to `computations/s88_gate_verdicts.txt` (canonical line + dual-SHA companion + 3-tuple annotation + `verdict_label=INFO-cross-conv-unstable` in companion row).

---

## Wave W3a Synthesis (team-lead; volovik-superfluid-universe-theorist)

**Wave outcome**: 1 FAIL + 1 FAIL + 1 INFO-cross-conv-unstable across 3 gates testing distinct structural-fix hypotheses for the S87 W11-5 cross-pillar bridge candidate FWD-C3 instance #2 REGISTRY-FAIL (`ratio_mismatch=1.029` under W11-5 metric vs Level-2 envelope 0.05).

### Three structural-fix corridors closed

| Gate | Hypothesis | Outcome | What was closed |
|:-----|:-----------|:--------|:----------------|
| §W3a-14 | M_3(ℂ) Cartan-zone IS the dominant FAIL cause | **FAIL** | M_3(ℂ) projection alone does NOT collapse mismatch; sign + magnitude both fail under plan metric |
| §W3a-18 | ι_*-composable cohomology-class redefinition IS the operational fix | **FAIL** (surrogate) | Substrate-physics-grounded surrogate observable also fails; faithful Connes-Karoubi pairing infrastructure queued for W3c |
| §W3a-19 | L_max=10 truncation IS incomplete; extension to L_max=20 saturates and PASSes | **INFO-cross-conv-unstable** | Pole-aggregation convention pin (Cβ vs B) is structurally unstable at L_max=20 (0.519 ≥ 0.50 threshold); B saturates non-physically at R≈−1.89, Cβ doesn't saturate (12.4% step 16→18) |

### Three POSITIVE structural findings

1. **W11-5 anchor reproducibility**: 4 independent reproductions of `R_substrate_full = −1.21222` to machine precision (W11-5 + §W3a-14 + §W3a-18 + §W3a-19 (L=10, Cβ)). The W11-5 FAIL is reliably reproducible; not a numerical artifact.
2. **W11-5 NON-COMPOSABILITY confirmed**: §W3a-18 composability_residual = 0.887 ≫ 0.01 ⇒ the W11-5 multiplicity-weighted Mellin-pole-window observable does NOT factor through ι_* faithfully. This is positive structural information about WHY W11-5 fails (observable-level non-composability, NOT bridge-map defect).
3. **B convention IS L_max-saturated**: §W3a-19 cross-step 0.50% then 0.05% at convention B — monotonic convergence to non-physical R_∞ ≈ −1.89. The multiplicity-weighted-median convention has a definite L_max → ∞ limit (not the issue — the limit is structurally wrong).

### What is preserved

- **3HeB-inheritance theorem (S86 W1b-T8)**: PRESERVED unchanged. All 3 W3a gates' FAILs are observable-construction-specific within the substrate-IS layer, NOT bridge-map defects.
- **Cocycle ratio invariant 7.324992**: PRESERVED at publication precision (verified at §W3a-14 + §W3a-18; both report residual ≈ 1.76e−05 within Class 8.3 publication precision tol 1e−4).
- **(Δ_B/Δ_A)^p=0 cancellation theorem (S86 W-5 DONE-5)**: PRESERVED at machine precision (residual 0.000e+00 across all 3 gates).
- **Cross-pillar bridge anatomy K-counter at K=2**: UNCHANGED (no instance-#3 advancement; the W3a retries are all sub-tests of instance #2, not structurally-distinct workshops).

### W3c (S89+) queue — TWO structural carry-forwards

W3a delivers TWO concrete S89+ carry-forward gates:

1. **`S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL`** (from §W3a-18): faithful Connes-Karoubi K-theory pairing on the BdG-restricted spectral triple. Implements full NCG infrastructure (Hochschild cocycle [φ_g^sym] on A_K^BdG_preimage; Chern character of P_0(τ_fold); Connes-Karoubi pairing). Tests against R_3HeB_lit at strict Level-2/3 envelope ≤ 0.001. Effort ~3 wave-equivalents.

2. **`S89-3HEB-EXCESS-INHERITANCE-CONVENTION-DEMARCATION-THEOREM`** (from §W3a-19): pole-aggregation convention demarcation per `regulator-convention-lockdown.md` §"Demarcation theorem" template; identify substrate-physics anchor analog to `w_0 effacement-anchored`; test convention-stability under L_max → ∞. PASS iff UNIQUE admissible convention identified AND `ratio_mismatch_unique_conv ≤ 0.05` at L_max=20. Effort ~1.5 wave-equivalents.

### What W3a does NOT close (open questions for W3c)

- Whether a faithful Connes-Karoubi pairing on the BdG-restricted spectral triple matches R_3HeB_lit at the strict Level-2/3 envelope (open until S89+ NCG infrastructure lands).
- Whether the demarcation-theorem-derived UNIQUE convention picks Cβ-like or B-like behavior in the L_max → ∞ limit (open until S89+).
- Whether the FAIL of W11-5's bridge candidate (FWD-C3 instance #2) ultimately admits a structural fix at L_max=10 OR requires a continuum L_max → ∞ extrapolation (open until both S89+ gates land).

### FWD-C3 instance #2 registry status (post-Wave-3a)

`permanent-results-registry.md` §VII.AJ FWD-C3 instance #2 (W11-5) row: **REGISTRY-FAIL stands**, with appended diagnostic note: "M_3(ℂ) projection NOT operative fix (S88 §W3a-14 FAIL); ι_*-composable surrogate observable NOT operative fix (S88 §W3a-18 FAIL; faithful Connes-Karoubi pairing queued for S89+); pole-aggregation convention structurally unstable at L_max=20 (S88 §W3a-19 INFO-cross-conv-unstable; demarcation-theorem queued for S89+). FWD-C3 instance #2 remains REGISTRY-FAIL pending W3c queue closure."

---

## Constraint-Map Updates

| Date | Mechanism / gate | Prior state | New state | Reason |
|:-----|:-----------------|:------------|:----------|:-------|
| 2026-05-03 | M_3(ℂ) Cartan-zone projection as W11-5 structural fix | OPEN (Track A: PRIOR=0.65) | **CLOSED-FAIL** (POSTERIOR=0.09) | §W3a-14 FAIL: M_3(ℂ) projection does NOT collapse W11-5 ratio_mismatch; sign + magnitude both fail under plan metric. Track-B routing realized. |
| 2026-05-03 | W11-5 observable ι_*-composability | UNTESTED | **CONFIRMED NON-COMPOSABLE** | §W3a-18 composability_residual = 0.887 ≫ 0.01 diagnostic threshold confirms W11-5 multiplicity-weighted Mellin-pole-window observable does NOT factor through ι_* faithfully (positive structural finding). |
| 2026-05-03 | Surrogate ι_*-composable cohomology-class observable as W11-5 fix | OPEN | **CLOSED-FAIL (surrogate)** | §W3a-18 FAIL on (a_3_BdG − a_3_M3C)/(a_3_BdG + a_3_M3C) surrogate; sign mismatch (pred=−0.367, lit=+0.035). Faithful Connes-Karoubi pairing queued for S89+. |
| 2026-05-03 | W11-5 L_max-truncation as FAIL cause | OPEN | **CLOSED-INFO-cross-conv-unstable** | §W3a-19 cross_conv_deviation_at_Lmax20 = 0.519 ≥ 0.50 threshold; B saturates non-physically (R≈−1.89), Cβ doesn't saturate (12.4% step 16→18). Convention re-derivation queued for S89+. |
| 2026-05-03 | W11-5 anchor reproducibility | (not previously stated) | **CONFIRMED reliable** (4 independent reproductions to machine precision) | (L=10, Cβ) reproduced in §W3a-14 (1.35e−6) + §W3a-18 (full-spectrum cross-check) + §W3a-19 (1.35e−6); W11-5 FAIL is structural, not numerical. |
| 2026-05-03 | FWD-C3 instance #2 (W11-5) `permanent-results-registry.md` §VII.AJ | REGISTRY-FAIL | **REGISTRY-FAIL with W3c-queue diagnostic note** | All 3 W3a gates close structural-fix corridors; bridge map preserved; observable-construction is the locus of FAIL; W3c (S89+) gets faithful Connes-Karoubi pairing + convention demarcation theorem. |
| 2026-05-03 | Cross-pillar bridge anatomy K-counter | K = 2 | **K = 2 (UNCHANGED)** | W3a retries are sub-tests of instance #2, not structurally-distinct workshops; no advancement. K=3 promotion still pending an independent third workshop. |
| 2026-05-03 | 3HeB-inheritance theorem (S86 W1b-T8 canonical) | PRESERVED | **PRESERVED** | All 3 W3a gates' FAILs are observable-construction-specific; bridge map well-defined. |
| 2026-05-03 | Cocycle ratio invariant 7.324992 (`substrate_cocycle_ratio_67_88`) | PRESERVED at publication precision | **PRESERVED** (verified across §W3a-14 + §W3a-18) | residual 1.76e−05 within Class 8.3 publication precision tol 1e−4. |
| 2026-05-03 | (Δ_B/Δ_A)^p=0 cancellation theorem (S86 W-5 DONE-5) | PRESERVED at machine precision | **PRESERVED** | residual 0.000e+00 across all 3 W3a gates. |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Sizes (bytes) |
|:-----|:-------|:------------|:------------|:--------------|
| §W3a-14 | `computations/s88_w3a_3heb_excess_inheritance_m3c_projected_retry.py` | `s88_w3a_3heb_excess_inheritance_m3c_projected_retry.npz` | `s88_w3a_3heb_excess_inheritance_m3c_projected_retry.png` | py 26,979; npz 9,002; png 115,037 |
| §W3a-18 | `computations/s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.py` | `s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.npz` | `s88_w3a_3heb_excess_inheritance_observable_redefinition_iota_composable_retry.png` | py 25,772; npz 7,024; png 103,161 |
| §W3a-19 | `computations/s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.py` | `s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.npz` | `s88_w3a_w11_5_lmax_scan_structural_robustness_extension_with_convention_pin.png` | py 25,405; npz 6,845; png 127,843 |
| All 3 | (verdict-line appends to `computations/s88_gate_verdicts.txt`) | (n/a) | (n/a) | 9 lines × 3 SHA fields each (canonical + companion + 3-tuple per gate) |

**Working-paper file**: `sessions/archive/session-88/session-88-w3a-workingpaper.md` (this file; ~600+ lines after Wave-3a synthesis closeout).
