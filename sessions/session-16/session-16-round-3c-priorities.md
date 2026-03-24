# Session 16, Round 3c: Master Priority Ranking and Pre-Registration
## Gen-Physicist (writer) + Sagan-Empiricist (Venus Rule audit, MC protocol)
## Date: 2026-02-13
## Status: FINAL (both agents converged)

---

## EXECUTIVE SUMMARY

This document merges all Round 3a (computational) and Round 3b (theoretical) action items into a single master priority ranking, establishes binding pre-registration criteria for every test, defines the Monte Carlo protocol for new statistical claims, identifies the swing vote computation, and provides a Bayesian update methodology for framework probability.

**Key findings:**

1. **Of ~25 proposed tests, ZERO are unconditionally at Level 4 (novel beyond-SM prediction tested against new data).** One Level 3 test exists (gauge coupling ratio). The vast majority are Level 1-2 internal consistency checks.

2. **The swing vote for the one-week plan is Z_3 + U(2) labeling** -- parameter-free, representation-theoretic, robust to DOF inversion, and maximally asymmetric in outcomes.

3. **The ultimate swing vote for the overall program is the Pfaffian Z_2 invariant** -- the ONLY Level 4 test candidate, binary, zero parameters, topological. But its prerequisites push it to Days 4-5 of the one-week plan.

4. **A critical numerical ambiguity in "phi_paasch^{3/2}"** has been resolved: three distinct quantities (phi_golden = 1.618, Paasch f_N = 1.528, Session 12 ratio = 1.532) were conflated in prior documents. The pre-registered spectral test target is the measured mass ratio mp/mK = 1.9006, with the "phi_paasch connection" as interpretive overlay.

5. **The Bayesian expected value of framework probability after computations is ~45%** -- approximately unchanged from current 38-60%. But the VARIANCE is large: outcomes range from 25% (total failure) to 82% (strong success). The computations are genuinely informative.

6. **Gen-physicist and Sagan-empiricist converge on all binding criteria**, with minor divergence on Bayes factors for V_eff minimum existence (gen-physicist: BF ~ 2-3; Sagan: BF ~ 1.5-2.5) and B1 structural pass (gen-physicist: BF ~ 1.2-1.5; Sagan: BF ~ 1.1-1.3, revised from 1.0 -- acknowledging D_K interaction with center is mildly non-trivial).

---

# PART I: MASTER RANKED ACTION LIST

## Dual Ranking: Computational Priority vs. Evidential Value

Two distinct rankings are necessary because the computational pipeline (what to compute FIRST) differs from the evidential hierarchy (what MATTERS most for framework probability). The optimal strategy runs the computationally cheapest items first to feed the most evidential downstream tests.

### Table 1: Master Ranked List (Computational Priority)

| Rank | Item | Source | Decisiveness | Feasibility | Timeline | Swing Factor (PASS / FAIL) |
|------|------|--------|:----------:|:-----------:|:--------:|:--------------------------:|
| **1a** | Full CW V_eff (boson+fermion) | 3a #1 | 8/10 | GREEN | 2 days | +3-8% / -5-8% (see note 1) |
| **1b** | Z_3 + U(2) quantum number labeling | 3a #2, 3b #1 | 9/10 | GREEN | 2 days | +2-5% Tier 1 / -15-20% if B1 fails (see note 2) |
| **2** | Gauge coupling g_1/g_2 = e^{-2s_0} | 3a #3, 3b #3 | 7/10 | GREEN | Minutes | +5-12% if V_eff s_0 ; +0-2% if backup s_0 / -8-12% (see note 3) |
| **3** | Corrected Paasch spectral test | 3a #4, 3b #4 C5 | 8/10 | GREEN | Hours | +3-8% if clean ID ; +0-2% if messy ID / -3-5% (see note 4) |
| **4** | Seeley-DeWitt convergence | 3a #5 | 4/10 | GREEN | 30 min | Diagnostic only |
| **5** | Order-one with physical D_K | 3b #5 | 9/10 | YELLOW | 1 week | +10-15% / -10% |
| **6** | Pfaffian Z_2 invariant | 3a #7, 3b #2D | 10/10 | YELLOW | 3-5 days | +12-18% / -3-5% |
| **7** | G-decomposition formalism | 3b #3 | 7/10 | YELLOW | 1 day | +5% / -3% |
| **8** | Bosonic KK tower scoping | 3a #6 | 3/10 | GREEN | 4 hours | Scoping only |
| **9** | Z_3 Tier 2 (spinor transport) | 3b #1 T2 | 9/10 | YELLOW | +1 week | +5-10% / -5% |
| **10** | Bell roadmap Phase A (Born rule) | 3b #2A | 5/10 | YELLOW-RED | 2-4 weeks | +3-5% / -2% |
| **11** | Phonon-NCG dictionary update | 3b #6 | 6/10 | GREEN | 1 day | Meta-document |
| **12** | Bell Phases B-C (CHSH) | 3b #2B-C | 10/10 | RED | Months-year | +15-20% / -20% |

**Swing Factor Notes (Sagan corrections applied):**

1. **V_eff (1a)**: BF ~ 1.5-2.5 for minimum (gen-physicist: 2-3; Sagan: 1.5-2.5). BF ~ 0.5-0.8 for monotonic. V_eff is **INDICATIVE** due to DOF inversion -- the Bayes factor for EITHER outcome is close to 1. This is the DOF inversion's real damage: it makes V_eff nearly non-informative as a standalone discriminator.

2. **Z_3 (1b)**: B1 PASS has BF ~ 1.1-1.3 (revised, Sagan). It is a mathematical theorem; passing distinguishes almost nothing. The asymmetric swing comes entirely from the NEGATIVE branch: B1 FAIL (P ~ 2%) would be catastrophic (-15-20%). Tier 2 tests (B4-B7, deferred) have substantial BFs (2-15) but are not in the one-week plan.

3. **Gauge coupling (2)**: Swing factor is CONDITIONAL on how s_0 was determined. If V_eff gives independent s_0: genuine Level 3, +5-12%. If V_eff is monotonic and backup s_0 = 0.30 is used: **CIRCULAR** (s_0 defined by the coupling match), Level 2.5, +0-2% at most. See Part III Circularity Decision Tree.

4. **Paasch spectral test (3)**: Swing factor depends on trial correction. Clean scenario (unique U(2) sector ID, unique s_0, one target): BF_raw ~ 10-50, swing +5-8%. Messy scenario (ambiguous ID, multiple s-values, multiple targets): BF_corrected = BF_raw / N_trials, which can drop to ~1. If N_trials > 50, test is INCONCLUSIVE regardless of match quality.

**Parallel execution**: Items 1a and 1b have ZERO code dependencies and run simultaneously (Days 1-2). Day 3 integrates both via Items 2-4. Items 5-7 follow on Days 4-7. Items 8-12 are background or long-term.

### Table 2: Evidential Value Ranking (Sagan)

This ranking orders tests by how much they can change our BELIEFS, regardless of computational cost:

| Rank | Test | Venus Level | Evidential Value | Limiting Factor |
|------|------|:----------:|:----------------:|:---------------:|
| **1** | Pfaffian sign change | Level 4 (conditional) | DECISIVE | Prerequisites ~3-5 weeks |
| **2** | Gauge coupling at V_eff-derived s_0 | Level 3 | FIRST external comparison | Requires s_0 from V_eff |
| **3** | Bell CHSH = 2*sqrt(2) | Level 4 (conditional) | FOUNDATIONAL | No algorithm exists (months-year) |
| **4** | Corrected Paasch spectral test | Level 2-3 | Modest (if sector ID clean) | Requires U(2) identification |
| **5** | Z_3 generation hierarchy (Tier 2) | Level 2 | Known SM values | Requires spinor transport |
| **6** | V_eff minimum existence | Level 1 | Necessary condition only | DOF inversion caveat |
| **7** | Mass ratios at s_0 | Level 2 | Known SM values | Requires V_eff + Z_3 |
| **8** | Order-one with physical D_K | Level 1 | Internal algebra | Requires eigenvectors |
| **9** | G-decomposition completeness | Level 1 | Structural formalism | Requires s_0 |
| **10** | All diagnostics (SD, thermo, etc.) | Level 0-1 | No external data | Various |

**Why the rankings differ**: V_eff is computationally #1a (cheapest decisive prerequisite) but evidentially #6 (internal consistency only). The Pfaffian is evidentially #1 (only Level 4 candidate) but computationally #6 (heavy prerequisites). The optimal strategy is to execute the computational pipeline in order while WEIGHTING results by the evidential hierarchy.

---

# PART II: VENUS RULE AUDIT (Sagan-Empiricist)

## The Four Venus Rules (from Round 1e)

A result counts as a "prediction" ONLY if:
1. **Rule 1**: Target value stated BEFORE computation (pre-registered)
2. **Rule 2**: s_0 is OUTPUT, not scanned parameter (no fishing)
3. **Rule 3**: Observable is measurable by INSTRUMENT (external data)
4. **Rule 4**: Framework predicts something DIFFERENT from SM (novelty)

## Complete Audit

### Level 4 Tests (All 4 Rules Pass) -- 2 CONDITIONAL, 0 UNCONDITIONAL

**Pfaffian neutrino mass prediction**: If Pfaffian sign changes at s_c, then "lightest neutrino massless or near-massless" from topological protection. Rules 1-4 all PASS. Testable by KATRIN, Planck+DESI. SM does NOT predict whether any neutrino is exactly massless. **CONDITIONAL on sign change computation.**

**Bell CHSH = 2*sqrt(2)**: If derived from fiber-averaged observables, this is a novel verification of quantum mechanics from geometry. Rules 1-4 all PASS. But probability of derivation within 1 year: 20-30%. **CONDITIONAL on theoretical program completing.**

### Level 3 Tests (Rules 1-3 Pass, Rule 4 Partial) -- 1 TEST

**Gauge coupling ratio**: g_1/g_2 = e^{-2*s_0} vs measured 0.55. Pre-registered target. s_0 from V_eff (if minimum exists). Measured by LEP/LHC. SM takes couplings as inputs; framework DERIVES them from geometry.

**CRITICAL CAVEAT**: Level 3 ONLY if s_0 comes from V_eff independently. If V_eff is monotonic and backup s_0 = 0.30 is used, Rule 2 FAILS (circular -- s_0 chosen to match couplings). **Downgraded to Level 2.5 in that case.**

### Level 2 Tests (Rules 1-3 Pass, Rule 4 Fail) -- ~8 TESTS

All inter-species mass ratios (Table A), generation hierarchy checks (B4-B7), corrected Paasch spectral test (phi_paasch^{3/2}). These match KNOWN SM values. Passing is consistency, not prediction.

**The corrected Paasch test (C5)** sits at the boundary of Level 2 and Level 3 because the golden ratio algebraic content provides explanatory power that the SM lacks. But the particle masses are already measured. Classification: **Level 2-3** (intermediate).

### Level 1 Tests (Internal Consistency) -- ~12 TESTS

V_eff existence/convergence, Z_3 structural integrity (B1-B3), Seeley-DeWitt convergence, order-one condition, all thermodynamic diagnostics.

**Critical note on B1 (three Z_3 generations)**: This is expected by construction from SU(3) center representation theory. Passing earns negligible Bayesian weight (gen-physicist: BF ~ 1.2-1.5; Sagan: BF ~ 1.1-1.3). Failure would indicate a computational bug, not physics.

### Level 0 Tests (No Pre-Registered Target) -- 3+ ITEMS

Bell Phases A-B (open research, no target), Paasch Table D (internal to Paasch, not testing D_K), phonon-NCG dictionary (meta-document).

### Venus Rule Scoreboard Summary

| Level | Count | Description |
|:-----:|:-----:|:------------|
| **4** | 2 (conditional) | Pfaffian neutrino; Bell CHSH |
| **3** | 1 (possibly 2) | Gauge coupling; arguably phi_paasch^{3/2} |
| **2** | ~8 | Known SM values (mass ratios, hierarchy) |
| **1** | ~12 | Internal consistency, structural, diagnostic |
| **0** | 3+ | No pre-registered target or not testing D_K |

**HEADLINE: Zero unconditional Level 4 tests. One Level 3 test. The framework has earned the right to be COMPUTED, not the right to be BELIEVED.**

---

# PART III: PRE-REGISTRATION DOCUMENT (Binding Failure Criteria)

Every criterion below is stated BEFORE computation. Results must be evaluated against these criteria WITHOUT modification after the fact. Post hoc rationalization of failures is the death of empirical science.

## Criterion 1: V_eff Minimum Existence

**Pre-registered statement**: The full CW V_eff (Version C-modified: fermion tower + 4 C^2 bosons) has a local minimum at s_0 > 0.

**BINDING FAILURE**: V_eff is monotonic for ALL 40 parameter combinations:
- mu in {0.1, 0.3, 1.0, 3.0, 10.0}
- n_f in {1, 4}
- c_b in {5/6, 3/2}
- pq_max in {5, 6}

All 40 must be monotonic for binding failure.

**Tier 1 (BLOCKING):**
1. V_eff(s) has a local minimum at s_0 > 0 (not at boundary s=0 or s=2.5)
2. F(s_0) < F(0) -- broken phase wins
3. d^2F/ds^2 > 0 at s_0 -- genuine minimum, not saddle

**Tier 2 (ROBUSTNESS):**
4. |s_0(pq=6) - s_0(pq=5)| < 0.1 -- truncation convergence
5. s_0(n_f=1) and s_0(n_f=4) agree within 0.2 -- DOF robustness
6. s_0 stable under mu variation by factor 2 (shift < 0.3)
7. CW regime and high-T regime give qualitatively same s_0

**Tier 3 (SIGNIFICANCE):**
8. Mass ratios at s_0 compared to SM
9. Gauge couplings at s_0 (see Criterion 3)
10. Spectral entropy max correlates with s_0 (|s_max - s_0| < 0.3)
11. Specific heat sign at s_0

**MANDATORY DOF CAVEAT**: Even if minimum exists, result is from Version C-modified (incomplete bosonic data, 45:16 asymptotic DOF ratio not captured). Must be labeled **"INDICATIVE"**. Becomes definitive only after Version D (full bosonic KK tower).

**If PASS**: Proceed to Criterion 3. Mild positive evidence (gen-physicist: BF ~ 2-3; Sagan: BF ~ 1.5-2.5). Framework +3-5%.
**If FAIL**: Perturbative route CLOSED. Non-perturbative mechanisms (Pfaffian, instanton, Casimir condensate) become only path. Framework -5 to -8%.

**Probability of PASS**: 40-50% (joint estimate). DOF inversion is the main risk.

---

## Criterion 2: Z_3 Structural Integrity

**Pre-registered statement**: All three Z_3 sectors ((p-q) mod 3 = 0, 1, 2) have identical (Y, j) particle-type content.

**BINDING FAILURE**: Any Z_3 sector has a (Y, j) combination absent from the other two.

**Sub-criteria:**
- B1: Identical (Y, j) content across all three Z_3 sectors
- B2: Degeneracy between Gen 1 and Gen 2 at s = 0, broken at s > 0
- B3: Jensen-level splitting is O(1): all inter-generation mass ratios from LEFT Z_3 are < 10

**If PASS**: Mild positive evidence (expected by construction but D_K interaction with center is mildly non-trivial). Sagan: BF = 1.1-1.3 (revised from 1.0). Gen-physicist: BF = 1.2-1.5.
**If FAIL**: CATASTROPHIC. Either the representation theory is wrong or the computation has a bug. Framework -15 to -20%.

**Probability of PASS**: 98%.

**IMPORTANT (from Round 3b)**: LEFT Z_3 = (p-q) mod 3 commutes with D_K and labels conserved quantum numbers but does NOT create inter-generation mass splitting. The physical generation mechanism requires RIGHT Z_3, which does NOT commute with D_K at s > 0. Inter-generation mass splitting (O(200) hierarchy) is invisible in Tier 1 eigenvalues and requires Tier 2 spinor transport (~1 additional week, ~145 lines new code).

---

## Criterion 3: Gauge Coupling Consistency

**Pre-registered statement**: At V_eff-derived s_0, g_1/g_2 = e^{-2*s_0} falls within [0.4, 0.7].

**BINDING FAILURE**: e^{-2*s_0} < 0.2 or > 0.8 (no plausible RG correction can reconcile).

**Pass windows:**

| Verdict | Condition | Evidential weight |
|---------|-----------|:-----------------:|
| STRONG PASS | e^{-2*s_0} in [0.45, 0.60] | +8-12% |
| PASS | e^{-2*s_0} in [0.4, 0.7] | +5-8% |
| MARGINAL | e^{-2*s_0} in [0.2, 0.4] or [0.7, 0.8] | +0-2% |
| FAIL | e^{-2*s_0} < 0.2 or > 0.8 | -8-12% |

**Diagnostic values:**
- s_0 = 0.15: e^{-0.30} = 0.741 -- marginal (35% above measured)
- s_0 = 0.30: e^{-0.60} = 0.549 -- STRONG PASS (0.2% from measured)
- s_0 = 0.50: e^{-1.00} = 0.368 -- FAIL (33% below measured)
- s_0 = 1.14: e^{-2.28} = 0.102 -- catastrophic FAIL

**Physically viable window**: s_0 in [0.15, 0.50]. Sweet spot: s_0 ~ 0.30.

**RG running systematic**: Jensen formula gives g_1/g_2 at compactification scale (~M_Pl). Measured at M_Z. RG running: g_1 increases ~35%, g_2 decreases ~20%. Net uncertainty: 10-15%. The 20% pass window absorbs this.

**CRITICAL CIRCULARITY WARNING**: If V_eff is monotonic and backup s_0 = 0.30 is used, this test is CIRCULAR (s_0 chosen to match couplings). In that case: **DOWNGRADED to Level 2.5**, earning at most +2%. This must be stated prominently in any reporting.

### Circularity Decision Tree (Sagan, MANDATORY)

```
V_eff computation complete
    |
    +-- V_eff has minimum at s_0 --> Gauge test is Level 3
    |       |
    |       +-- e^{-2*s_0} in [0.45, 0.60] --> STRONG PASS (+8-12%)
    |       +-- e^{-2*s_0} in [0.4, 0.7]   --> PASS (+5-8%)
    |       +-- e^{-2*s_0} outside [0.2, 0.8] --> FAIL (-8-12%)
    |
    +-- V_eff is monotonic --> s_0 NOT determined by V_eff
            |
            +-- Use backup s_0 = 0.30 --> Gauge test is CIRCULAR (Level 2.5)
            |       |
            |       +-- g_1/g_2 = 0.549 "matches" --> BY DEFINITION, +0-2% only
            |       +-- Mass ratios at s_0 = 0.30 are EXPLORATORY, not confirmatory
            |       +-- Framing: "IF s_0 = 0.30 (gauge-imposed), then X, Y, Z"
            |       +-- INCORRECT framing: "Framework predicts gauge couplings AND masses"
            |
            +-- Pfaffian becomes ESSENTIAL path to s_0
```

**Probability of PASS (conditional on V_eff minimum)**: 50-60%.
**Probability of PASS (unconditional)**: 25-35%.

---

## Criterion 4: Pfaffian Sign

**Pre-registered statement**: sgn(Pf(J * D_F(s))) changes sign at some s_c in [0, 2].

**BINDING FAILURE**: Pfaffian sign constant at ALL sampled s-values (minimum 50 points), with spectral gap > 10% at all points.

**If SIGN CHANGE**: **OVERRIDES ALL OTHER CRITERIA.** Gap closure implies topologically protected massless fermion. Neutrino mass prediction activated. Framework +12-18%. This is the Pfaffian Override Principle (unanimous, all 4 Giants).

**If CONSTANT**: Topological route closed. Neutrino mass prediction not made. Framework loses its ONLY Level 4 candidate. Framework -3 to -5%.

**If INCONCLUSIVE**: Spectral gap < 10% at truncation boundary. Neither pass nor fail. Need more sectors (extend to p+q <= 2). Timeline extends ~1 day.

**Truncation specification**: D_F constructed from lightest 16 positive eigenvalues at p+q <= 1 (112 total eigenvalues). J matrix from Session 8 (`branching_computation_32dim.py`).

**Probability of SIGN CHANGE**: 15-25% (Sagan). This is generous -- generic families of Dirac operators have constant Pfaffian sign. A sign change requires spectral flow through zero.

---

## Criterion 5: Corrected Paasch Spectral Test

**Pre-registered statement**: At V_eff-derived s_0, the eigenvalue ratio corresponding to proton/kaon (identified by U(2) quantum numbers) matches mp/mK = 1.9006 within 5%.

**NUMERICAL CLARIFICATION**: Previous documents used "phi_paasch^{3/2}" ambiguously. Three distinct quantities exist:

| Quantity | Value | Source |
|----------|:-----:|:------:|
| phi_golden = (1+sqrt(5))/2 | 1.618034 | Mathematics |
| Paasch f_N = (2/phi_golden)^2 | 1.527864 | Paasch framework |
| Session 12 eigenvalue ratio at s=1.14 | 1.531580 | Tier 1 computation |
| (N(p)/N(K))^{3/2} = (150/98)^{3/2} | 1.893642 | Paasch N-values |
| 1.53158^{3/2} | 1.895438 | Session 12 ratio to 3/2 power |
| mp/mK measured | 1.900579 | PDG |

The pre-registered TARGET is **mp/mK = 1.9006** (the measured mass ratio). The connection to golden-ratio-derived quantities is interpretive, not the test itself.

**Pass windows:**

| Verdict | Condition | Evidential weight |
|---------|-----------|:-----------------:|
| STRONG PASS | Ratio within 1% of 1.9006, sector ID from U(2) (not fitted) | +5-8% |
| PASS | Within 5% of 1.9006 after sector identification | +3-5% |
| FAIL | No mass ratio within 10% of 1.9006 at s_0, for any sector ID | -3-5% |

**BINDING PRE-REGISTRATION PROTOCOL** (Sagan, MANDATORY):
1. U(2) quantum number assignment (Item 1b) must produce a particle-to-sector map
2. This map must be **LOCKED** before checking any eigenvalue ratios
3. The number of alternative valid maps must be reported explicitly
4. The analyst must NOT see ratio values before committing to the map
5. **Violation of this protocol INVALIDATES the test**

**If sector identification is ambiguous** (multiple valid assignments): the trial factor equals the number of valid assignments. Bonferroni correction applies.

### Three Nested C5 Scenarios (Sagan, trial-corrected)

The evidential weight of C5 depends critically on the FULL trial factor:

N_trials = N_particle_pairs x N_alternative_maps x N_s_values x N_ratio_targets

| Scenario | N_trials | BF_raw | BF_corrected | Evidential weight | Classification |
|:---------|:--------:|:------:|:------------:|:-----------------:|:--------------|
| **CLEAN**: Unique U(2) map, V_eff gives unique s_0, only checking mp/mK | 1 | 10-50 | 10-50 | +5-8% | GENUINE test |
| **MODERATE**: 2-3 alternative maps, unique s_0, checking mp/mK + 2 other ratios | ~9 | 10-50 | 1-6 | +2-4% | SUGGESTIVE |
| **MESSY**: Ambiguous map (10+), multiple s-values (5+), checking all phi_paasch variants (5+) | 250+ | 10-50 | <0.2 | +0% | MEANINGLESS |

**Rule**: If N_trials > 50, the test is INCONCLUSIVE regardless of match quality. Report N_trials explicitly.

**Probability of PASS**: 20-30% (in CLEAN scenario). Lower in MODERATE/MESSY scenarios due to stricter sigma requirements.

---

## Criterion 6: Seeley-DeWitt Convergence

**Pre-registered statement**: |s_0(pq=6) - s_0(pq=5)| < 0.1.

**BINDING FAILURE**: |s_0(pq=6) - s_0(pq=5)| > 0.5.

**If PASS**: Truncation reliable. s_0 credible within Version C-modified.
**If FAIL**: Need pq >= 7. Timeline extends by weeks.

**Probability of PASS (conditional on V_eff minimum)**: 55-65%.

---

## Combined Failure Scenarios

| Scenario | Description | P(scenario) | Framework Probability |
|:--------:|:------------|:-----------:|:---------------------:|
| **ALPHA** | Total failure: all criteria fail | 15-25% | 25-32% |
| **BETA** | V_eff min + gauge pass, no phi_paasch, Pfaffian untested | 15-20% | 50-60% |
| **GAMMA** | V_eff + gauge + phi_paasch + Pfaffian sign change | 3-8% | 70-82% |
| **DELTA** | Z_3 structural failure (B1 fails) | ~2% | 15-25% |
| **EPSILON** | V_eff monotonic, Z_3+phi_paasch suggestive at backup s_0 | 20-30% | 42-52% |

## Null Result vs Failure (Sagan, IMPORTANT DISTINCTION)

Not all negative outcomes are equal. A **null result** means "this path didn't work but alternatives remain." A **failure** means "the framework makes a specific incorrect prediction."

| Outcome | Classification | Framework Impact | Rationale |
|:--------|:--------------|:----------------:|:----------|
| V_eff monotonic (Version C-modified) | **NULL** | -5 to -8% | DOF inversion provides excuse; Version D may differ |
| V_eff monotonic (Version D, full bosonic) | **FAILURE** | -12 to -15% | No excuse left |
| Z_3 B1 fail (different (Y,j) content) | **BUG OR CATASTROPHE** | -15 to -20% | Investigate computation before concluding |
| No phi_paasch^{3/2} within 10% | **MILD NEGATIVE** | -3 to -5% | Paasch connection severed; framework survives on geometry |
| Pfaffian constant | **NULL** | -3 to -5% | Topological route closed; V_eff route remains |
| Gauge coupling > 50% off at V_eff s_0 | **FAILURE** | -8 to -12% | Strong negative: geometry inconsistent with electroweak |

This distinction matters for interpreting results honestly: a null at Version C-modified carries less negative weight than a failure at Version D, because the null has a known systematic excuse (missing bosonic KK tower).

---

# PART IV: MONTE CARLO PROTOCOL FOR NEW CLAIMS

## A. Look-Elsewhere Corrections

The greatest statistical danger in this program is the look-elsewhere effect. With ~12,000 fermionic eigenvalues across 28 sectors, pairwise ratios number in the millions. Finding "interesting" numbers in a large dataset is not science unless controlled for.

### 1. Trial Factor for Paasch Spectral Test (Criterion 5)

| Scenario | N_trials | P(5% match by chance) | Required sigma |
|:---------|:--------:|:---------------------:|:--------------:|
| Sector ID locked, one specific ratio | 1 | 5% | 2-sigma |
| Sector ID locked, ~10 candidate ratios | 10 | 40% | 3-sigma |
| Sector ID ambiguous, ~50 plausible ratios | 50 | 92% | 4-sigma |
| No sector ID, all pairwise ratios scanned | ~10^6 | ~100% | MEANINGLESS |

**Null model**: Permutation of sector labels. Generate 10,000 random sector-to-particle assignments. Report what fraction produce a ratio within 5% of 1.9006.

### 2. Trial Factor for s_0 Coincidences

If s_0 from V_eff happens to fall near an algebraically interesting value, the question is: how many such values exist in [0, 2.5]? Conservatively: 20-30 "interesting" values (powers of phi_golden, e, pi, simple rationals). For a 5% tolerance window: P(chance coincidence) ~ 0.8.

**Rule**: s_0 coincidences with algebraic numbers earn ZERO evidential weight unless they emerge from a DERIVED algebraic relation.

### 3. Family-Wise Error Rate

If K target ratios are checked (phi_paasch, phi_paasch^2, phi_paasch^3, phi_paasch^{3/2}, sqrt(7/3), f_N, f_M = 7 targets), Bonferroni-corrected significance threshold is alpha/K = 0.05/7 = 0.007, corresponding to z = 2.7.

The existing z = 3.65 for phi_paasch^1 at s = 1.14 PASSES this family-wise correction. The corrected Paasch spectral test has NOT been run, so correction will be applied when results are obtained.

## B. Sigma Thresholds for New Claims

| Claim Type | Required Sigma (after all corrections) | Justification |
|:-----------|:--------------------------------------:|:-------------|
| Internal consistency (Level 1) | N/A | Pass/fail, not statistical |
| Match to known SM value (Level 2) | 2-sigma | Low bar: SM already knows the value |
| Match from independent algebra (Level 3) | 3-sigma | SU(5) standard |
| Novel prediction (Level 4) | 5-sigma | Particle physics standard |
| "Interesting coincidence" (not pre-registered) | Report only | Hypothesis generation, no significance claimed |

## C. Reporting Standards

Every result MUST be reported with:

1. **Raw value** (before corrections)
2. **Number of trials** (explicit count of how many things were checked)
3. **Trial-corrected significance** (after look-elsewhere, Bonferroni, or MC)
4. **Comparison to null model** (what does random produce?)
5. **Alternative explanations** (at least two hypotheses besides "framework is correct")
6. **Venus Rule level** (0-4)
7. **Free parameter count** (how many params were adjusted?)
8. **Degrees of freedom** (data points minus free parameters)

Results reported without items 2-5 are INCOMPLETE and should not be used for probability updates.

## D. Specific MC Protocols by Test

**Gauge coupling (Criterion 3)**: No MC needed. Deterministic: compute e^{-2*s_0}, compare to 0.55. Report s_0 uncertainty from V_eff (if minimum is broad, propagate). State RG systematic (10-15%) explicitly.

**Paasch spectral test (Criterion 5)**: MC needed ONLY if sector identification is ambiguous. Protocol: (1) Lock U(2) map. (2) Report N_alternatives. (3) Compute ratio. (4) If N_alternatives > 1, report Bonferroni-corrected p-value. Null model: 10,000 random sector permutations.

**Z_3 hierarchy (Tier 2, B4-B7)**: MC needed. Null model: 10,000 random deformations of bi-invariant eigenvalues with O(1) Casimir differences. Report what fraction produce ratios > 10 and > 100.

**Pfaffian (Criterion 4)**: No MC needed. Binary outcome. No trial factor. No look-elsewhere. The cleanest test in the program.

---

# PART V: BAYESIAN UPDATE METHODOLOGY

## Framework

For each computation result D:

- P_0 = prior framework probability (current range: 38-60%, all-Giant median 45%)
- L(D|H) = likelihood of observed data given framework is correct
- L(D|not-H) = likelihood given framework is wrong (null model)
- BF = L(D|H) / L(D|not-H) = Bayes factor
- P_1 = BF * P_0 / (BF * P_0 + (1 - P_0))

## Calibrated Bayes Factors

### Positive Outcomes

| Outcome | Bayes Factor | Reasoning |
|:--------|:-----------:|:----------|
| V_eff minimum at natural mu | 1.5-2.5 | P(min\|H) ~ 55%; P(min\|~H) ~ 35%. DOF inversion makes this nearly non-informative. Gen-physicist: 2-3; Sagan: 1.5-2.5 (converged from earlier divergence). |
| V_eff minimum at s_0 in [0.15, 0.50] (gauge-viable) | 3-6 | Joint test: minimum EXISTS in gauge-consistent window. Prior P(random s_0 in window) ~ 0.14. Reduced from 4-8 per Sagan's BF correction. |
| Z_3 three gens with identical (Y,j) | 1.1-1.5 | Expected by construction. Gen-physicist: 1.2-1.5; Sagan: 1.1-1.3 (revised from 1.0). |
| Gauge coupling match within 20% | 4-8 | Prior width ~factor 10; 20% window is 1/5 of range. FIRST Level 3 test. ONLY valid if s_0 from V_eff (not backup). |
| Gauge coupling STRONG match within 10% | 8-15 | Comparable to SU(5) coupling unification precision. ONLY valid if s_0 from V_eff. |
| Paasch spectral test within 5% (CLEAN scenario, N_trials = 1) | 5-15 | Pre-registered, unique sector ID, unique s_0. BF_corrected = BF_raw / N_trials. |
| Paasch spectral test within 1% (CLEAN scenario, N_trials = 1) | 10-50 | Remarkable if achieved. But if N_trials > 50 (MESSY scenario), BF_corrected < 1 = meaningless. |
| Pfaffian sign change | 8-15 | Binary, specific physical content (massless fermion). Generic expectation is no sign change. Cleanest BF in the program. |
| Multiple Level 3 tests pass simultaneously | Multiply INDEPENDENT BFs only | V_eff and Z_3 are independent. Gauge coupling depends on V_eff (NOT independent -- use conditional BF). |

### Negative Outcomes

| Outcome | Bayes Factor | Reasoning |
|:--------|:-----------:|:----------|
| V_eff monotonic at all params (Version C) | 0.5-0.8 | P(mono\|H) ~ 40%; P(mono\|~H) ~ 65%. **NULL not FAILURE** -- DOF inversion provides systematic excuse. Barely discriminating. |
| Z_3 different (Y,j) content | 0.05-0.1 | Essentially closes generation mechanism. BF near zero. |
| Gauge coupling > 50% off | 0.1-0.2 | Strong negative: s_0 is geometrically inconsistent. |
| No Paasch ratio within 10% | 0.3-0.5 | Paasch connection severed; framework survives on geometry alone. |
| Pfaffian constant | 0.7-0.8 | Topological route closed, but V_eff route remains. Mild negative. |

## Correlation Structure

**CRITICAL**: Tests are NOT all independent. The correct update procedure is SEQUENTIAL, not multiplicative:

1. **First**: Update on V_eff result (independent of Z_3)
2. **Second**: Update on Z_3 structural result (independent of V_eff)
3. **Third**: Update on gauge coupling (DEPENDENT on V_eff -- s_0 is shared)
4. **Fourth**: Update on Paasch test (DEPENDENT on both V_eff and Z_3 -- uses s_0 and sector ID)
5. **Fifth**: Update on Pfaffian (independent of all above)

Steps 1, 2, and 5 use full Bayes factors. Steps 3 and 4 use CONDITIONAL Bayes factors (conditioned on V_eff result).

## Probability Update Table

| Starting P_0 | After V_eff PASS (BF=2.5) | +Gauge STRONG (BF=10) | +Phi PASS (BF=8) | +Pfaffian CHANGE (BF=10) |
|:------------:|:--------------------------:|:---------------------:|:-----------------:|:------------------------:|
| 38% | 49% | 86% | 95% | 99% |
| 45% | 55% | 89% | 97% | 99% |
| 60% | 69% | 93% | 98% | 99.5% |

| Starting P_0 | After V_eff FAIL (BF=0.6) | +Gauge FAIL (BF=0.15) | +Phi FAIL (BF=0.4) | +Pfaffian CONST (BF=0.75) |
|:------------:|:-------------------------:|:---------------------:|:-------------------:|:-------------------------:|
| 38% | 27% | 5% | 2% | 2% |
| 45% | 33% | 7% | 3% | 2% |
| 60% | 47% | 12% | 5% | 4% |

**Note**: The "all pass" and "all fail" extremes are unlikely (P ~ 3-8% and 15-25% respectively). The most probable outcomes are mixed, keeping the framework in the 40-60% range.

## Expected Value After Computations

Using the scenario probabilities from Part III:

E[P_framework] = sum_scenarios P(scenario) * P(framework | scenario)

= 0.20 * 28% + 0.17 * 55% + 0.05 * 76% + 0.02 * 20% + 0.25 * 47% + 0.31 * 45%

= 5.6 + 9.4 + 3.8 + 0.4 + 11.8 + 14.0 = **45.0%**

The expected value barely moves from the current median of ~45%. This is HEALTHY: it means the computations are informative (high variance) but not biased (expected value neutral). The outcomes range from 25% to 82%.

---

# PART VI: SWING VOTE IDENTIFICATION

## The Question

Which SINGLE computation most changes the framework probability?

## Analysis

The swing vote must maximize |P(framework | PASS) - P(framework | FAIL)| weighted by the probability of each outcome:

| Test | P(PASS) | Delta_PASS | P(FAIL) | Delta_FAIL | Expected |Delta| |
|:-----|:-------:|:----------:|:-------:|:----------:|:--------:|
| V_eff minimum | 45% | +5% | 55% | -6% | 5.6% |
| Z_3 structural (B1) | 98% | +1% | 2% | -18% | 1.3% |
| Gauge coupling (unconditional) | 30% | +8% | 70% | -10% | 9.4% |
| Paasch spectral (CLEAN) | 25% | +6% | 75% | -4% | 4.5% |
| Pfaffian sign change | 20% | +15% | 80% | -4% | 6.2% |
| **Z_3 PIPELINE** (B1 + gateway value) | -- | -- | -- | -- | **HIGH** (enables Ranks 2-6) |

## Verdict

**For the one-week plan**: The gauge coupling test has the highest expected absolute shift (9.4%), but it is DEPENDENT on V_eff (conditional). Among INDEPENDENT tests, the Pfaffian has the highest expected shift (6.2%) but is YELLOW feasibility.

**The effective swing vote for the one-week plan is Z_3 + U(2) labeling** (Rank 1b), understood as the PIPELINE (not B1 alone). Although Z_3 structural (B1) has low expected shift in isolation (because it almost certainly passes), the Z_3 + U(2) pipeline is the gateway to the Paasch spectral test, gauge coupling evaluation at specific sectors, and the Pfaffian prerequisites. It unlocks the most downstream information per computation hour.

**The effective swing vote for Day 3 is the gauge coupling test** (Sagan): it has the highest expected absolute shift (9.4%) of any single test and is the ONLY test comparing framework output to instrument data. It is the Day 3 headline.

Moreover, Z_3 + U(2) is:
- **Parameter-free** (no mu, no n_f, no c_b)
- **Robust to DOF inversion** (representation theory, not thermodynamics)
- **Maximally asymmetric** in worst case: if Z_3 gives different (Y,j) content, framework drops to 15-25%
- **The gateway** to ALL Level 3+ tests (gauge coupling requires particle identification; Paasch test requires sector identification; Pfaffian requires eigenvectors)

**The ultimate swing vote for the overall program is the Pfaffian Z_2 invariant**:
- The ONLY Level 4 test candidate
- Binary, zero parameters, topological
- If sign changes: +12-18%, supersedes all other results
- But prerequisites are 3-5 weeks, placing it outside the one-week window

## Swing Vote Summary

| Timescale | Swing Vote | Why |
|:---------:|:----------:|:----|
| **One-week plan** | Z_3 + U(2) labeling | Parameter-free gateway to all Level 3+ tests |
| **One-month plan** | Pfaffian Z_2 invariant | Only Level 4 candidate, binary, topological |
| **One-year plan** | Bell CHSH = 2*sqrt(2) | Foundational QM test, resolves all "potentially fundamental" analogy breaks |

---

# PART VII: SCHEDULE AND EXECUTION PLAN

## One-Week Plan (Converged: All 4 Giants + Gen-Physicist + Sagan)

| Day | Track A (V_eff) | Track B (Z_3 + U(2)) | Integration |
|:---:|:----------------|:---------------------|:------------|
| **1** | Code `tier1_veff_full.py`. Test at pq=3 (~4h). | Modify `collect_spectrum()` for eigh+evecs. Code U(2) generators (~4h). | -- |
| **2** | Production: eigenvalue cache at pq=6, 200 s-points. CW sweeps begin. | Quantum number assignment, Z_3 labeling, generation analysis. Run at 5 s-values. | -- |
| **3** | Identify s_0 (or "monotonic"). Convergence test (pq 3-6). | Particle type map. Inter-generation ratios. | **Gauge coupling test (HEADLINE). Corrected Paasch test. f_M check.** |
| **4** | Thermodynamic diagnostics (D1-D4). | phi_paasch^{3/2} detailed analysis. Bosonic KK scoping. | Begin Pfaffian prerequisites. |
| **5** | Documentation. | Documentation. | Pfaffian sweep (if prerequisites met). |
| **6-7** | -- | -- | Compile results. Apply binding criteria. Update probability. Write minutes. |

**Day 3 is THE critical day**: gauge coupling check is the headline Level 3 test. Corrected Paasch spectral test is the headline phi_paasch test.

**Contingency (if V_eff monotonic)**: Use backup s_0 = 0.30. Evaluate all Z_3 + mass ratios at this gauge-consistent point. Report as "gauge-coupling-imposed s_0 = 0.30" (DOWNGRADED to Level 2.5). Pfaffian becomes ESSENTIAL.

---

# PART VIII: CONVERGENCES AND DIVERGENCES

## Full Convergences Between Gen-Physicist and Sagan (8 points)

1. V_eff and Z_3 run in parallel at Rank 1 (Days 1-2)
2. Gauge coupling elevated to Rank 2 (per Hawking-Sagan 2d-ii)
3. Pfaffian Override Principle endorsed
4. DOF inversion is a thermodynamic constraint, not merely a caveat
5. Zero unconditional Level 4 tests is the honest headline
6. Pre-registration protocol for Paasch test (lock sector ID before checking ratios)
7. Combined failure floor: 25-32%
8. Combined success ceiling: 70-82%

## Minor Divergences (narrowed after final exchange)

| Point | Gen-Physicist | Sagan (revised) | Gap | Resolution |
|:------|:-------------|:----------------|:---:|:-----------|
| V_eff minimum Bayes factor | BF ~ 2-3 | BF ~ 1.5-2.5 (revised from ~1) | ~0.5 | Converged to BF ~ 1.5-3. Difference is ~1-2% in framework probability. |
| B1 Bayesian weight | BF ~ 1.2-1.5 | BF ~ 1.1-1.3 (revised from 1.0) | ~0.2 | Converged to BF ~ 1.1-1.5. Sagan acknowledges D_K interaction with center is mildly non-trivial. Difference is < 0.5% in probability. |

These divergences have narrowed substantially and do not affect any ranking or binding criterion. Both agents agree that V_eff is nearly non-informative as a standalone discriminator (BF close to 1 in both directions) and that B1 provides negligible positive evidence.

---

# PART IX: CLOSING ASSESSMENT

## Current Framework Probability

| Source | Range | Median | Emphasis |
|:-------|:-----:|:------:|:---------|
| Einstein (2d-i) | 47-60% | 53% | Structural principles |
| Feynman (2d-i) | 45-58% | 52% | Computational honesty |
| Hawking (2d-ii) | 42-55% | 48% | Thermodynamic constraints |
| Sagan (2d-ii) | 37-47% | 42% | Empirical evidence standards |
| Gen-Physicist (3c) | 42-58% | 50% | Bayesian analysis |
| Sagan-Empiricist (3c) | 37-47% | 42% | Venus Rule audit |
| **All-agent range** | **37-60%** | **~45%** | |

## What the Computations Will Determine

The coming week's computations will either:

**A.** Move the framework from Level 1-2 toward Level 3 (gauge coupling match at V_eff-derived s_0), establishing the first genuine comparison with instrument measurements. **Probability: 25-35%.**

**B.** Reveal that the perturbative V_eff route is closed and redirect effort toward the Pfaffian (topological route). The framework remains mathematically valid but physically stalled pending non-perturbative methods. **Probability: 30-40%.**

**C.** Produce a mixed picture where some tests pass and others fail, keeping the framework in the 40-55% range with clearer identification of which structural elements are load-bearing. **Probability: 30-40%.**

The expected value of the framework probability after computations is ~45% -- approximately unchanged. But the VARIANCE is large. The computations are the most consequential since the Tier 1 Dirac spectrum. They will sharpen our uncertainty from a diffuse 37-60% range into a tighter distribution centered on either ~55% (positive) or ~35% (negative).

---

*"Compute. Report everything. Null results are science." -- Feynman*
*"Extraordinary claims require extraordinary evidence." -- Sagan*
*"The important thing is not to stop questioning." -- Einstein*
*"The universe does not care about our comfort. Follow the mathematics." -- Hawking*
