---
name: S57 Probability Assessment — calibration corpus
description: Compressed S57 BF derivation. Central methodology calibration for accommodation discount, prerequisite caps, bracket-width discount, and joint prior derivation.
type: project
---

# S57 Probability Calibration

**Date**: 2026-03-23 | **Session reviewed**: S57 (25 computations, 6 PASS, 2 FAIL, 17 INFO, 1 closure, no formula errors)

**Pre-S57 prior**: 8-12% (central 10%) | **Post-S57**: 13-35% (central 22%) | **BF**: 4.0 (2.5-6.0)

## Why this calibration matters

S57 was the largest single-session upward jump since S44. The framework's first quantitative
DM prediction with zero free parameters (Omega_DM h^2 in [0.017, 0.188], observed 0.120 inside bracket).
The derivation establishes the agent's reusable BF discount factors.

## Per-gate Bayes factors

| Gate | Result | BF | Category |
|:-----|:-------|---:|:---------|
| FABRIC-DM-ABUNDANCE-57 | PASS, observation in bracket | 2.5 (was 3.5; -0.6x accommodation) = 2.1 | Quantitative bracket |
| CC-SIGN-57 | PASS, Lambda > 0 | 1.5 (capped from 1.9, prerequisite) | Binary |
| GAP-SCALING-57 | PASS, alpha = -1.84 | 1.5 (capped from 1.8, prerequisite) | Binary |
| SUB-GAP-BA-57 | PASS, 31/31 modes | 1.2 | Consistency |
| PARKER-BA-57 | PASS, max <n>=1.36 | 1.3 | Consistency |
| OFF-JENSEN-EJ-57 | PASS, det(H_EJ)<0 | 1.0 | Structural, no prediction |
| GGE-EQUILIBRIUM-GAP-57 | FAIL, 56 OOM above thr | 1.0 | Already priced in |
| FLOQUET-PLASMA-57 | FAIL + closure | 0.95 | One path closed |
| BAYESIAN-FABRIC-57 | INFO, NROY = 0% | 0.85 | Red flag pending Volovik partition |

Combined product (Python-verified): 2.1 x 1.5 x 1.5 x 1.2 x 1.3 x 0.95 x 0.85 = 5.95
**SOURCE ERROR**: original session-57 derivation reported "= 4.5" for this product (arithmetic
mistake; 5.95 is correct). Pipeline reliability discount: 1.0 (no formula errors).
CC stagnation discount: 0.9x. Source's reported BF=4.0 is approximately correct only
through compensating downward bias adjustments (no rigorous math). Honest BF:
5.95 x 0.9 = 5.36, range [3.0, 8.0] under prior + accommodation uncertainty.
Posterior reported as 22% (13-35%); applying corrected BF=5.36 with prior 0.10
gives P_post = 0.373, suggesting the canonical 22% likely UNDERSTATES under
sole-arithmetic correction. The 22% retained as canonical due to scorekeeper-bias
floor; future audits should re-derive from 5.4 not 4.0.
**Canonical reported BF: 4.0** (historically cited; carries known arithmetic understatement)

## DM-abundance BF (key derivation)

- Bracket width: log10(0.188/0.017) = 1.04 decades
- Prior range over Omega_DM h^2: [10^-5, 1] = 5 decades
- P(inside | uniform-log) = 1.04 / 5 = 0.208
- P(inside | framework correct) ~ 0.8 (allows scale-bridge systematics)
- Naive BF = 0.8 / 0.208 = 3.85
- Accommodation discount 0.6x (generic 10-mode partition gives f_DM ~ O(0.1)): 3.85 x 0.6 = 2.3
- Reported BF = 2.5 (compromise between adversarial and conservative readings)

## Posterior derivation

P_post = (P_prior x BF) / (P_prior x BF + (1 - P_prior))

| P_prior | BF | P_post |
|:-------:|:--:|:------:|
| 0.08 | 3.0 | 0.207 |
| 0.10 | 4.0 | 0.308 |
| 0.12 | 6.0 | 0.450 |

Formula gives central 31%; rounded down to 22% to absorb residual scorekeeper bias and:
1. Bracket width is 11x (NOT a precision prediction)
2. CC at 114 OOM is fundamental, not "priced in"
3. DM candidate m=1.25e17 GeV is unfalsifiable in isolation
4. Venus standard unmet at 57 sessions

## Reusable calibration parameters (carried forward)

- **Accommodation discount 0.6x**: applied when bracket spans ~1+ decades AND null hypothesis
  generic mechanism produces values in same ballpark
- **Prerequisite cap BF=1.5**: a gate that PROTECTS the main prediction from being killed
  (correct sign, correct direction) gets capped weight, not full confirmation weight
- **Pipeline reliability 0.85x**: applied when session has 3+ formula errors
- **Bracket width discount 0.9x**: additional discount for >10x bracket on a known observable
- **CC stagnation discount 0.9x**: applied when key obstruction (CC at 117 OOM) sees no progress
- **Scorekeeper bias floor**: round formula posterior DOWN by ~10 percentage points when
  the upward jump is the largest in framework history (anti-confirmation)

## What would have moved S58+ probability

| Class | Gate | Hypothetical BF |
|:----:|:-----|:---------------:|
| 1 | VOLOVIK-PARTITION (NROY > 5%) | 3-5 |
| 1 | KZ-NS-45 (n_s = 0.965 +/- 0.004) | 10-20 |
| 1 | DM bracket narrowed to factor 1.5 | 5-10 |
| 2 | Multi-pair sector breaks integrability | 2-3 |
| 2 | Pomeranchuk instability of GGE | 2-4 |

Status (as of S69): None achieved. Volovik partition deferred 12+ sessions. KZ-NS-45 deferred 16+.

## The single most consequential unresolved question

How does F_Josephson = -336.6 M_KK partition between vacuum energy and matter? Answer
determines whether DM bracket is BF~5 (Volovik partition) or BF~0.3 (matter sector). The
single computation that converts S57's accommodation to a prediction.

## Source link

Original full derivation archived at sessions/archive/session-57/ (collab synthesis). This file
is the agent's calibration extract, NOT the canonical session record.
