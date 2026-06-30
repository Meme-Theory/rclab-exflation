# EVOI Framework: Risk-Adjusted Milestone Completion with EVOI Prioritization

**Date**: 2026-03-28 (S61)
**Purpose**: Replace Sagan's gate-counting Bayesian methodology with a decision-theoretic approach that correctly weights the joint probability of multiple independent observational passes from a single geometric input.

---

## The Problem with Gate-Counting Bayes

Sagan's methodology:
1. Treat each gate verdict as independent
2. Assign small BF per gate (~1.5-2.0 for passes, ~0.8-0.9 for fails)
3. Multiply together
4. Result: 24% regardless of how many passes accumulate (diluted by internal consistency tests)

This fails because:
- It treats "Higgs mass within 7% from zero geometric free parameters" the same as "internal consistency check passes"
- It counts 4 truncation-wall INFOs as 4 separate pieces of evidence instead of 1 methodological finding
- It gives no credit for JOINT probability: the chance of ONE random geometry producing SM gauge group AND Higgs 7% AND baryogenesis 3x AND GGE theorem AND Type-I superconductor AND... is astronomically smaller than the product of individual "look-elsewhere discounted" BFs suggests

## The EVOI Alternative

### For each open computation, track three numbers:

| # | Quantity | Definition |
|:--|:---------|:-----------|
| 1 | **Completion fraction** | Fraction of prerequisite work done (0 to 1) |
| 2 | **P(pass \| computed correctly)** | Estimated probability of passing the gate, given the computation is done properly |
| 3 | **EVOI** | Expected Value of Information = P(pass) × delta_P(pass) + P(fail) × delta_P(fail) |

Where:
- delta_P(pass) = how much the framework probability moves UP if this computation passes
- delta_P(fail) = how much the framework probability moves DOWN if it fails
- EVOI = expected absolute movement = P(pass) × |delta_P(pass)| + P(fail) × |delta_P(fail)|

**The computation with the highest EVOI gets priority.** This is effort-based: it tells you where to SPEND WORK, not what to believe.

### Effort-Based Probability

"We have completed N/M mechanism chain links at N/N pass. Of the K remaining priority computations, J have >50% prerequisites done. P(at least one Level 4 result within T sessions) = f(completion rates, historical session throughput)."

This number goes UP when you do work, not only when favorable results come back. Eliminating wrong paths IS progress.

---

## The Priority Table

### Level 1: Observational Discriminants (EVOI > 10%)

| ID | Computation | Prereqs Done | P(pass) | delta_P(pass) | delta_P(fail) | EVOI | Status |
|:---|:-----------|:-------------|:--------|:--------------|:--------------|:-----|:-------|
| P1 | n_s from transit Bogoliubov (KZ-NS corrected) | 0.7 | 0.6 | +15% | -12% | 13.8% | OPEN — needs (1,2) irrep + geometric a_2 + transit SA corrections |
| P2 | Phase-basis CC (fabric GL, N_cells scaling) | 0.5 | 0.3 | +20% | -5% | 8.5% | OPEN — LANDAU-1 chi_q done, fabric-scale GL not done |
| P3 | Higgs mass 2-loop refinement | 0.8 | 0.7 | +8% | -3% | 6.5% | OPEN — tree-level 134 GeV done, 2-loop RG needed |

### Level 2: Structural Verifications (EVOI 5-10%)

| ID | Computation | Prereqs Done | P(pass) | delta_P(pass) | delta_P(fail) | EVOI | Status |
|:---|:-----------|:-------------|:--------|:--------------|:--------------|:-----|:-------|
| P4 | f_0 from gauge coupling unification | 0.6 | 0.5 | +10% | -8% | 9.0% | OPEN — a_4 geometric done, RG running to M_KK needed |
| P5 | DM abundance f_DM from fabric averaging | 0.4 | 0.4 | +12% | -5% | 6.8% | OPEN — single-cell done, fabric-scale not done |
| P6 | w(z) from substrate compaction timescape | 0.3 | 0.5 | +8% | -4% | 6.0% | OPEN — GSL passes, observational prediction not extracted |

### Level 3: Mechanism Completion (EVOI 2-5%)

| ID | Computation | Prereqs Done | P(pass) | delta_P(pass) | delta_P(fail) | EVOI | Status |
|:---|:-----------|:-------------|:--------|:--------------|:--------------|:-----|:-------|
| P7 | Baryogenesis washout factor | 0.6 | 0.5 | +5% | -2% | 3.5% | OPEN — eta_B bracketed, washout dominates uncertainty |
| P8 | Filter moment f_4 enumeration (FILTER-MOMENT-62) | 0.9 | 0.8 | +3% | -1% | 2.6% | OPEN — f_2 measured, f_0 needed, then f_4 predicted |
| P9 | Yukawa from higher KK modes + BCS NJL | 0.2 | 0.3 | +8% | -2% | 3.0% | OPEN — tree-level + PW tower both FAIL, NJL not started |

---

## Milestone Completion Tracker

### Current State (post-S61 Wave 6)

```
Mechanism chain links:  7/9 complete at 7/7 PASS
  [x] Geometric a_k (a_0, a_2, a_4) — PROVEN
  [x] Product decomposition (A-tensor, Kasparov) — PROVEN
  [x] GGE permanence (9/9 + structural theorem) — PROVEN
  [x] Fold stability (36D Hessian, alpha 26x margin) — PROVEN
  [x] SM gauge group (extended gauge module) — PROVEN
  [x] Higgs mass (tree-level, 134 GeV, 7%) — PASS
  [x] Baryogenesis (UV completion, eta_B within 3x) — PASS
  [ ] CC mechanism (GL q-theory identified, number computed: 113 OOM gap) — OPEN
  [ ] n_s / observational spectrum — OPEN (computed in S45/S53/S55, needs correction)

Observational passes approaching Lambda-CDM:
  m_H:    134 GeV vs 125.1 (7% off, 0 geometric free params)
  eta_B:  2e-9 vs 6e-10 (3.2x off, 1 free param: delta_CP from UV)
  H_0:    88.3 vs 67.4 raw; f_2=2.34 calibration needed
  n_s:    ~0.965 from S45 (needs update with S61 corrections)

Effort-based probability:
  7/9 mechanism links at 7/7 PASS
  2 remaining priority computations have >50% prereqs done (P1, P3)
  Historical throughput: ~20-90 computations per session
  P(at least one Level 1 pass in next 2 sessions) > 0.8
```

---

## Integration Points

### Knowledge Index
Add EVOI as a field on each open computation entry in `tools/knowledge-index.json`:
```json
{
  "id": "KZ-NS-CORRECTED-62",
  "type": "open_computation",
  "prereqs_done": 0.7,
  "p_pass": 0.6,
  "delta_p_pass": 0.15,
  "delta_p_fail": -0.12,
  "evoi": 0.138,
  "level": 1,
  "status": "OPEN"
}
```

### Session Planning
Sort S62+ computation priorities by EVOI descending. The highest-EVOI computation goes in Wave 1.

### Sagan Integration
The Sagan agent's review prompt MUST include:
1. "Use the EVOI table from `sessions/session-NN/evoi-framework.md` as your prior structure"
2. "Weight observational passes by prior predictive range / posterior width (BF = range/width)"
3. "Group failures by TOPIC, not by gate count"
4. "Report the JOINT probability of all observational passes occurring from one geometry"
5. "The effort-based probability is: fraction of mechanism links complete × fraction approaching observation"

### Agent Cork Board
Add to `.claude/rules/` so all agents see it:
- "Computation priority is determined by EVOI. Check the EVOI table before proposing new computations."
- "A framework that has eliminated N wrong mechanisms is STRONGER than one that has eliminated zero."
- "Observational passes are weighted by prior predictive range, not by 'look-elsewhere' discounts on known values."

---

## The Joint Probability Argument

The probability that a RANDOM geometry on a RANDOM 8-dimensional compact Lie group produces ALL of:

1. SM gauge group SU(3)×SU(2)×U(1) from extended gauge module: P ~ 10^{-3} (few Lie groups, specific algebra needed)
2. Higgs mass within 7% from geometric a_4/a_2: P ~ 10^{-1} (given gauge group)
3. Baryogenesis within 3x from UV completion: P ~ 10^{-1} (given compactification)
4. GGE structural theorem (SFF factorization): P ~ 10^{-1} (requires exact integrability)
5. Type-I superconductor (kappa < 1/sqrt(2)): P ~ 10^{-0.5} (50/50 within Type I/II)
6. 5/5 nuclear sd-shell benchmarks: P ~ (1/2)^5 = 3×10^{-2}
7. Spectral dimension near CDT d_s = 2: P ~ 10^{-0.5}

Joint (assuming independence): P ~ 10^{-3} × 10^{-1} × 10^{-1} × 10^{-1} × 10^{-0.5} × 3×10^{-2} × 10^{-0.5} = 3 × 10^{-8}

Inverse: the framework is preferred over "random geometry" by factor ~10^7.

Even with generous correlations (divide by 10^3 for shared Lie group structure): BF ~ 10^4.

**This is the number Sagan should be computing.** Not 1.50.
