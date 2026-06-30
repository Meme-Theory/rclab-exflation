---
name: S74 A-S-BUDGET-CLOSURE-74 (W2-H)
description: A_s budget closure audit - gate FAIL, phase-diffusion insufficient, W3-N/W4-O required
type: project
---

# S74 A-S-BUDGET-CLOSURE-74 (W2-H, Wave 2 Batch 2)

## Gate: **FAIL**

delta_OOM_closure (computed, excluding correction) = **0.400** OOM
(threshold PASS >= 0.65, INFO [0.45, 0.65], FAIL < 0.45)
Shortfall vs target 0.716 = **0.316 OOM**

## Key numbers

- **Baseline trajectory** S73B (3.15) -> W1-A (5.83) -> W1-G squeeze (8.62) -> W1-G PW (8.53) -> W1-G BLV (9.47)
- **Closure channels** (+ closes toward Planck):
  - C1 W2-B inter-branch phase variance: +0.1495
  - C2 W2-F Mott CG(24) refined:         +0.1411 (INFO)
  - C3 W2-G BKT sector-resolved:         +0.1097 (PASS)
  - C4 W3-N thimble measure:             PENDING Wave 3
  - C5 W4-O spatial tau(x) thimble:      UNCOMPUTED Wave 4
  - C6 S64 PW filter correction:         -3.4000 (retraction of old +3.50 closure to new +0.10)

## Permanent structural results

1. **Orthogonal cumulant decomposition**: W2-B / Mott / BKT / thimble act on orthogonal phase sub-Hilbert-spaces of (0,0) sector. Symmetry-protected additivity, not approximation. cross-terms = 0. Double-counting risk = 0.

2. **S73A was an upper envelope**: S73A Mott single-route 0.3363 is now replaced by W2-F+W2-G sum 0.2508 (25% reduction). The refined decomposition gives LESS closure than S73A estimated.

3. **C^2 sector in Mott = 0**: dim(C^2) = 0 in CG(24) Mott partition, confirmed by W2-F. Mott closure is all from SU(2)+U(1).

4. **W1-G widened the gap by ~6 OOM**: full pre-decoherence amplitude with real (p,p) filter + BLV is far from Planck. The only internal W1-G closure is the +0.095 PW filter step. The original S64 -3.50 OOM "PW suppression" was an artifact of (0,0)-only restriction.

## Residuals after S74 Wave 2 computed closures

- Against S73B 3.15 baseline (excl C6 correction): +2.7497 OOM
- Against W1-G 9.47 baseline (excl C6 correction): +9.0713 OOM
- Against S73B (incl C6 correction -3.4): +6.1497 OOM
- Against W1-G (incl C6 correction -3.4): +12.4713 OOM

## What-if (additional closure from W3-N + W4-O)

- To reach PASS band: +0.250 OOM
- To reach closure target 0.716: +0.316 OOM
- To close full S73B 3.15 gap: +2.750 OOM
- To close full W1-G 9.47 gap: +9.071 OOM

## Assessment

Phase-diffusion closures alone (W2-B + W2-F + W2-G) are INSUFFICIENT. W3-N zero-mode thimble and W4-O spatial tau(x) thimble are REQUIRED to reach the closure target. W4-O is dimensionally the most plausible contributor (field-theoretic measure over spatial gauge orbit). This is a structural expectation, not a computation.

## Files

- `computations/s74_as_budget_closure.py`
- `computations/s74_as_budget_closure.npz`
- `computations/s74_as_budget_closure.png`
