---
name: S52 Off-Jensen PMNS Results
description: OFFJENSEN-PMNS-52 gate results — off-Jensen metrics generate B1-B3 mixing only, B2 isolated, sin2_13 tunable to measured value
type: project
---

## OFFJENSEN-PMNS-52 Gate: INTERMEDIATE

**Why:** Off-Jensen left-invariant metrics on SU(3) can generate nonzero sin^2(theta_13) by splitting the C^2 coset directions, but sin^2(theta_12) = sin^2(theta_23) = 0 structurally. The PMNS is 2x2 (B1-B3), never full 3x3.

**How to apply:** Any future PMNS mechanism must break the B2 isolation. The B2 4-fold eigenspace is protected by a spinor symmetry that survives all left-invariant metric perturbations. Full 3x3 PMNS requires inter-sector, non-left-invariant, or NCG inner fluctuation mechanisms.

## Key Numerical Results

- U(2)-preserving off-Jensen: ZERO mixing (confirms S36 Schur closure)
- U(2)-breaking C^2 split: O matrix block-diagonal — 2x2 (B1,B3) + 1x1 (B2)
- sin^2(theta_13) vs C^2 split: monotonic, matches NuFit 0.02225 at split = 0.0918
- R at matching split: 7.03 (vs target 33.8, 4.8x below)
- Normal ordering preserved at all off-Jensen points
- B2 isolation survives all 10 tested perturbation directions

## Structural Wall (proven)

Off-Jensen singlet PMNS is 2x2 (B1,B3). sin^2(theta_12) = sin^2(theta_23) = 0 for ANY left-invariant metric perturbation of the singlet Dirac operator Omega.

## Files

- `computations/s52_offjensen_pmns.py` (main), `s52_offjensen_analysis.py` (supplementary)
- `computations/s52_offjensen_pmns.npz`, `s52_offjensen_pmns_supp.npz`
- `computations/s52_offjensen_pmns.png`, `s52_offjensen_pmns_supp.png`
