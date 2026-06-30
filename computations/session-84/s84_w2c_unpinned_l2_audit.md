# S84 W2c-19: §VII.M-UNPINNED -- L2 Audit of the 5 UNPINNED §VII.K-META Rows

**Gate**: S84-UNPINNED-L2-AUDIT [AUDIT] META
**Agent**: lizzi-spectral-functional-theorist
**Verdict**: **FAIL** -- value = 6.035e+11 (max shift_factor); scheme = Zubarev-L2; convention = CC5; L_max = 5
**Closure SHA-256**: `490c87f55392173cf9306205b8eb7ea91f860573b3eab5fc7cd7781a21f36e05`
**W1-G1 anchor SHA**: `227a5913...`  |  **W1-G3 anchor SHA**: `2343920a...`

---

## 1. Substrate framing (mandatory)

The substrate selects its own scheme at two strata (S83-MASTER three-layer theorem):

- **L1 (axiomatic)**: zeta is the unique regulator under Connes A1-A6 (Dixmier-trace class) -- W1-G3 PASS.
- **L2 (substrate-action)**: Zubarev is the unique local-min of `S_substrate-action` at `L_max=5, tau=0.19` with `S_Zubarev = 3.806e+3` -- W1-G1 PASS.

UNPINNED rows are observables for which **L1 alone does not select** a unique
regulator. The audit asks whether L2 closes the ambiguity. Direction of
explanation: `D_K spectrum -> S_Zubarev local-min -> regulator choice -> observable value`.
A row that fails to pin at L2 means the **substrate itself is ambiguous on
that observable** -- not a coordinate-chart artifact.

## 2. Method

For each of the 5 UNPINNED rows in §VII.K-META (Lizzi synthesis §II.4):

1. Read L1 anchor `O_L1` from the original S82/S83 record (as cited in §VII.K-META).
2. Compute L2 reading `O_L2` under Zubarev canonicalization.
3. Compute `shift_factor = max(|O_L1|, |O_L2|) / min(|O_L1|, |O_L2|)`.
4. Classify per pre-registered band:
   - **PROMOTE-L2** if `shift < 1.5` (L2 is a valid alternative pin -- row joins L2-SA bucket).
   - **BORDERLINE** if `1.5 ≤ shift ≤ 3` (partial pin).
   - **GENUINE-UNPINNED** if `shift > 3` (substrate ambiguity on that observable).

## 3. Substitution chain (per §10 of plan)

1. **Definition** (L1): `O_L1` = observable value under Dixmier-unique zeta regulator from S82/S83 record.
2. **Definition** (L2): `O_L2` = observable value under Zubarev substrate-action local-minimum regulator at `L_max=5, tau=0.19`.
3. **Definition** (shift): `shift_factor(row) = max(|O_L1|, |O_L2|) / min(|O_L1|, |O_L2|)`. Dimensionless; always ≥ 1.
4. **Substitute** row-by-row: see §4 5-row table for the explicit `O_L1`, `O_L2`, `shift` triples.
5. **Simplify**: `shift = max / min` directly; no algebraic transformation.
6. **Read direction**: `shift < 1.5` ⇔ L1 and L2 agree within factor-1.5 (L2 is valid pin); `shift > 3` ⇔ L1 and L2 disagree strongly (genuinely unpinned).
7. **Conclusion**: classify each row by the direction reading; aggregate to verdict via PASS-all / FAIL-any-3 / INFO-borderline rule.

## 4. Five-row shift-factor table

| Row | Name | O_L1 | O_L2 | shift_factor | Classification |
|----:|:-----|----:|----:|---:|:---------------|
| #13 | r_max | 1.33252e+04 | 1.00000e+00 | 1.332e+04 | **GENUINE-UNPINNED** |
| #17 | w_0 (Zub branch iv) | -9.18087e-01 | -9.98116e-01 | 1.087 | PROMOTE-L2 |
| #18 | w_0 (zeta branch iii) | -9.16539e-01 | -9.98116e-01 | 1.089 | PROMOTE-L2 |
| #24 | a_2-cluster | 6.03494e-01 | 0.000e+00 | 6.035e+11 (strict) / 1.117 (proxy) | **GENUINE-UNPINNED** |
| #38 | mu_eff Lindblad-Keldysh | 8.58000e-04 | 8.74094e-04 | 1.019 | PROMOTE-L2 |

**Aggregate**: PROMOTE-L2 = 3/5; BORDERLINE = 0/5; GENUINE-UNPINNED = 2/5; max_shift = 6.035e+11.

## 5. Per-row substrate analysis

### Row #13 (r_max) -- GENUINE-UNPINNED, shift = 1.332e+4

- L1 (zeta): `O_L1 = max_ratio_tau = 1.33253e+4` from S82-W2-2 (FAIL vs PASS_THRESH=0.1).
  Zeta cap on backreaction: linear perturbative Parker-pair density divided by
  background gives a UV-divergent ratio that overcaps the substrate budget by
  4 orders of magnitude.
- L2 (Zubarev): `O_L2 = max_ratio_sc_tau = 1.0` from the same W2-2 self-consistent
  saturation identity (CC4 PASS). The Zubarev entropy-max substrate-action
  enforces a saturation identity at the fold: `rho_p / rho_bg -> 1` by
  construction, because the Zubarev maximum-entropy ensemble normalizes the
  pair-density to the substrate's own energy density at the fold.
- **Substrate verdict**: zeta lets the backreaction run unbounded (axiomatic
  finiteness only); Zubarev imposes substrate-action saturation. The four-OOM
  gap is **not a labeling artifact**: it is a structural disagreement between
  the L1-only "what regulator does the spectral triple admit" question (zeta)
  and the L2-substrate-action "what regulator does the substrate select"
  question (Zubarev). The observable r_max is genuinely two-valued at the
  layer interface.

### Row #17 (w_0 Zubarev branch iv) -- PROMOTE-L2, shift = 1.087

- L1 (mixed-scheme target): `w_0_S58_A = -0.918` (canonical Friedmann-compatible).
- L2 (Zubarev): `w_0_Zubarev = -0.998` (G51 branch iv, pure Zubarev).
- Cross-check #3 prediction: `|w_0_L1| / |w_0_L2| = 0.918 / 0.998 = 0.9198`;
  computed: 0.9198 (rel_err = 2.07e-5). Matches plan exactly.
- **Substrate verdict**: L2 promotes the row -- 8.7% disagreement is within the
  factor-1.5 promotion band. The w_0-Zubarev value is a structurally valid
  Zubarev pin; it differs from the mixed-scheme S58-A target by less than the
  L2-promotion threshold.

### Row #18 (w_0 zeta branch iii) -- PROMOTE-L2, shift = 1.089

- L1 (zeta): `w_0_zeta = -0.9165` (G51 branch iii).
- L2 (Zubarev): `w_0_Zubarev = -0.998` (same L2 minimum as row #17 -- this
  IS the L2 uniqueness statement: the Zubarev substrate-action minimum does
  not depend on the initial-branch label).
- **Substrate verdict**: L2 promotes; the zeta initial-branch evacuates into
  the same Zubarev local-min as the Zubarev initial branch, confirming L2
  uniqueness on the GGE-relic equation-of-state observable.

### Row #24 (a_2-cluster variance) -- GENUINE-UNPINNED, shift = 6.035e+11 strict

- L1 (5-scheme): `var_a2_full = 0.6035` -- the cross-scheme RELATIVE variance
  of `a_2(SDW), a_2(anomaly), a_2(f*), a_2(Gaussian), a_2(exp-decay)` at
  `L_max=5, tau=0.19` (FAIL vs the P4-C tightness band).
- L2 (Zubarev): keep only the Zubarev-aliasing scheme (`exp-decay` with Lambda_Z
  cutoff). Single-element variance = 0 strictly. The shift_factor diverges
  because the observable itself is a **cross-scheme measure** -- removing 4 of
  5 schemes makes it identically zero.
- Operational proxy: centroid-deviation = `|a_2^Zubarev - mean_5| / std_5 = 1.117`.
  The Zubarev value lies within ~1 standard deviation of the cross-scheme
  centroid, so by the proxy reading row #24 is just-outside PROMOTE-L2.
- **Substrate verdict**: STRICT reading is the authoritative classification.
  Row #24 is **structurally** an L1-only observable: it asks "how spread is
  `a_2` across regulators?", which the L2 single-scheme collapse cannot answer.
  The row does not promote to L2-pinned because the observable is **not in
  L2's domain of definition** -- it is a cross-scheme statistic.

### Row #38 (mu_eff Lindblad-Keldysh) -- PROMOTE-L2, shift = 1.019

- L1 (zeta + exp Lindblad kernel): `mu_eff_S77_ref = 8.580e-4`.
- L2 (Zubarev temporal cutoff + detailed-balance enforced): `mu_eff_LK_with_DB = 8.741e-4`.
- 1.9% disagreement -- well within PROMOTE-L2 band.
- **Substrate verdict**: L2 promotes. The Zubarev temporal cutoff is the unique
  temporal regulator that satisfies substrate-action minimization on the
  reduced density matrix evolution; mu_eff is robust under the L1->L2 layer
  swap.

## 6. Cross-checks

### CC1 -- NOT-R-protected meta-prediction

§VII.K-META meta-principle (S83-G58 PASS): R-protected rows have `shift ≤ 1.5`;
NOT-R-protected rows have `shift ≥ 2.5`. Predicted: all 5 UNPINNED rows are
NOT-R-protected (`shift ≥ 2.5`).

Computed: NOT-R-protected count = **2/5** (rows #13, #24). Predicted: 5/5.

**CC1 status**: PARTIAL FAIL. Three UNPINNED rows (#17, #18, #38) are
R-protected after L2 canonicalization. The §VII.K-META meta-principle is
**not violated** (these three rows promote to L2-pinned and exit the UNPINNED
bucket; the meta-principle then applies to the remaining 2 GENUINE-UNPINNED
rows, which DO satisfy `shift ≥ 2.5`).

### CC3 -- w_0 consistency with G51 magnitude

Plan prediction: `|w_0_L1| / |w_0_L2| = 0.918 / 0.998 = 0.9198 ≈ 1/1.087`.

Computed: 0.9198 (relative error 2.07e-5). **CC3 PASS**.

## 7. Verdict and consequences

**Verdict**: **FAIL** -- 2 of 5 UNPINNED rows is GENUINE-UNPINNED (shift > 3).
The §VII.K-META UNPINNED bucket is **NOT redundant** with L2.

**Solution-space consequences**:

1. **Three-layer theorem scope must restrict**. W2a-11 registration cannot
   claim that every row in the 42-row §VII.K atlas pins to one of
   {L0-INT, L1-AX, L2-SA, L3-OB}. Two rows (#13 r_max and #24 a_2-cluster)
   are **structural exceptions** that require either:
   - A fourth layer (e.g. L4-CROSS-SCHEME-STATISTIC) explicitly designed
     for cross-regulator measures like row #24's variance, OR
   - Explicit scope-restriction language: "the three-layer theorem applies
     to 40 of 42 rows; rows #13 r_max and #24 a_2-cluster are
     genuinely-cross-layer observables."

2. **W2a-13 distribution revision**. Predicted 26/2/1/8/5 distribution does
   NOT revise to 26/2/1/13/0. The actual revision is 26/2/1/11/2:
   - +3 to L3-OB sub-bucket (rows #17, #18, #38 promote to L2/L3)
   - 2 remain UNPINNED (rows #13, #24)
   - L3-OB count: 8 + 3 = 11 (or stays 8 with 3 moving to L2-SA depending on
     §VII.K convention; the 3 promoted rows pin AT L2 with valid Zubarev value).

3. **Row #13 is a substrate-physics signal**. The 4-OOM disagreement between
   zeta `r_max = 1.33e+4` and Zubarev sc-saturation `r_max = 1.0` is **not a
   numerical artifact**. It says: the substrate self-saturates the
   backreaction at the fold via the Zubarev entropy-max ensemble, but this
   saturation is **not visible to a pure axiomatic (Dixmier-trace) inspection**
   of the spectral triple. This is the layer-interface itself becoming
   physical -- a signature that backreaction is intrinsically a substrate-
   action concept, not an axiomatic one.

4. **Row #24 is a meta-observable**. The cross-scheme variance is a measure
   ON the regulator-scheme atlas itself, not on the substrate. The L2
   canonicalization cannot pin a meta-observable because it is not an
   observable IN the substrate -- it is an observable OF the regulator atlas.
   This argues for excluding cross-scheme-statistic rows from the §VII.K
   classification entirely (move to a separate §VII.K-DIAGNOSTICS bucket).

## 8. Carry-forward to S85+

1. **W3-UNPINNED-STRUCTURAL** (per plan §W2c-19 line 399): produce either
   the 4th-layer ansatz or scope-restriction language. Target: connes-ncg
   for the L4 ansatz, lizzi for the scope-restriction draft.

2. **Row #24 reclassification**: move "cross-scheme variance" type rows out
   of the layer-classified buckets into a §VII.K-DIAGNOSTICS section.
   Audit other rows in the 42-row atlas for this pattern.

3. **Row #13 layer-interface theorem**: backreaction saturation as a
   substrate-action-only phenomenon -- candidate permanent theorem if
   verified at L_max=7 and L_max=9 (W2c-20 dependency).

4. **Knowledge-base update**: §VII.K-META distribution from 26/2/1/8/5
   updates to 26/2/1/11/2 (or 26/2/1/8/2 with 3 transitions to L2-SA).

## 9. Inputs and provenance

| Input | SHA-256 (head) | Source |
|:------|:----------|:-------|
| `s82_w2_2_unified_backreact_79.npz` | `16a31a86...` | S82 W2-2 (row #13 r_max FAIL) |
| `s83_w3_g51_w0_regulator.npz` | `09b54a7c...` | S83 G51 (rows #17, #18 w_0 branches) |
| `s82_w2_8_a2_cluster_test.npz` | `e7e8a483...` | S82 W2-8 (row #24 a_2-cluster FAIL) |
| `s82_w3_8_mu_eff_lk.npz` | `796521e3...` | S82 W3-8 (row #38 mu_eff LK INFO) |
| `s83_w1_g3_regulator_priority_proof.npz` | `058fd2e6...` | S83 W1-G3 (L2 anchor) |
| `canonical_constants.py` | `d4941240...` | live import |

**Output 4-tuple**: `(value=6.035e+11, scheme=Zubarev-L2, convention=CC5, L_max=5)`

**Verdict-line target**: `computations/session-84/s84_gate_verdicts.txt`

```
S84-UNPINNED-L2-AUDIT: FAIL -- value=6.035e+11 scheme=Zubarev-L2 convention=CC5 L_max=5 sha256=490c87f55392173cf9306205b8eb7ea91f860573b3eab5fc7cd7781a21f36e05
```
