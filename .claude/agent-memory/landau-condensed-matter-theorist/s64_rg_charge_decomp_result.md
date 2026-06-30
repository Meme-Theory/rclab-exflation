---
name: S64 R-G-CHARGE-DECOMPOSITION-64 Results
description: Gaudin charge decomposition — all 8 broken by gravity, 94.6% of rho_ZP outside Gaudin space
type: project
---

## S64 R-G-CHARGE-DECOMPOSITION-64 Results (Wave 1)

- Gate: **PASS** (7/8 broken charges have |<R_k|rho_ZP>|/max > 0.01; only R_2 at 0.009 fails)
- ALL 8 Gaudin charges broken by O(alpha_G) gravitational perturbation
- No selection rule protects any charge, including R_0 (B2[0]) despite C_2^{PW}(0,0) = 0
- Breaking transmitted through exchange denominators 1/(eps_k - eps_l), not Casimir structure

**Why:** The R-G charge decomposition was requested to determine whether the gravitational channel (3.88% eigenvalue shift, S63 W6-02) affects the charges conjugate to vacuum energy.

**How to apply:**
- The sector-selective obstruction (VdD Re:V1) is QUANTITATIVE, not structural — B2[0] charge broken at 0.094 relative strength
- The 94.6%/5.4% split is the key new finding: Gaudin charges control only 5.4% of rho_ZP
- This means R-G integrability protects only the pair-correlated part of vacuum energy
- The 108-OOM gap (cc-path-b.md) is NOT resolved: O(alpha_G) * 5.4% = O(10^{-5}) net effect

### Key Numbers
- Breaking strength: R_0=0.094, R_7=0.190 (monotone B2->B3)
- rho_ZP overlap: R_0=0.576, R_7=1.000 (R_2=0.009 is sole sub-threshold)
- R^2(rho_ZP on span{R_k}) = 0.054 — Gaudin charges span 5.4% of vacuum energy
- R^2(H_grav on span{R_k}) = 0.018 — gravitational perturbation 98.2% orthogonal to Gaudin algebra
- delta_CC total = -2.89e-4 M_KK — dominated by B3 modes, B2[0] contribution identically zero (eps_0 ~ 0)
- Gaudin charge rank = 7 (not 8) due to sum rule constraint
- Files: `computations/s64_rg_charge_decomp.{py,npz,png}`
