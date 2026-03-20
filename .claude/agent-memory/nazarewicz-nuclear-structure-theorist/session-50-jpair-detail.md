---
name: S50 J-PAIR-CALIBRATE-50 results
description: Independent J_pair calibration from pair-transfer matrix element -- 7 methods, INFO verdict
type: project
---

## S50 J-PAIR-CALIBRATE-50: INFO

### Gate Result
- **Verdict**: INFO (J_pair > 0.096 at best, but 41% systematics > 30% threshold)
- J_pair(primary, Method 2b) = 0.1153 M_KK (nuclear pair-transfer formula)
- J_pair(secondary, Method 3) = 0.2288 M_KK (Tr(V*C) from ED correlator)
- J_pair range (7 methods): [0.115, 0.329] M_KK -- ALL exceed 0.096
- J_pair(1-sigma low) = 0.068 M_KK -- below 0.096
- J_pair(floor) = 0.080 M_KK -- below 0.096

### ec_fabric Results
- ec_fabric(best, Method 2b) = 1.392 > ec_min = 1.264 (PASS)
- ec_fabric(1-sigma low) = 1.138 < ec_min (FAIL)
- BH ED correction factor = 1.874 (beyond perturbative, from S49 cluster comparison)
- 9/9 methods pass ec_min at corrected scaling

### Key Intermediate Quantities
- F_transfer = sum u_k v_k = 2.130 (pair condensate amplitude from S48 ED)
- Delta_OES = 0.464 M_KK (odd-even staggering from S37)
- E_C = 0.929 M_KK (charging energy from S49)
- J/E_C = 0.124 (best, Method 2b)
- Correction factor (BH ED / perturbative) = 1.874

### Systematic Uncertainty
- J_C2: 30% (dominant -- requires independent calibration)
- Mode truncation: 19% (from S36 convergence)
- BH single-mode: 20% (marginal scale separation)
- Combined: 41%

### Rate-Limiting Step
Independent J_C2 calibration (Berry phase or off-Jensen deformation) would reduce dominant systematic from 30% to ~15%, bringing combined to 31%.

### Method 3_dos Warning
Tr(V_eff * C) = 2.169 M_KK is WRONG: double-counts DOS. V_eff already has sqrt(rho) from Hamiltonian construction; pair_corr also absorbs DOS through occupation factors. Use bare V for inter-cell coupling.

### Files
- Script: `tier0-archive/s50_jpair_calibrate.py`
- Data: `tier0-archive/s50_jpair_calibrate.npz`
