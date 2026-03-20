---
name: session-49-multi-t-friedmann
description: MULTI-T-FRIEDMANN-49 gate result: multi-T shifts w_0 toward DESI by 33%, S48 correction discovered
type: project
---

## MULTI-T-FRIEDMANN-49: PASS

**What was computed**: Modified Friedmann equation for 8-temperature GGE relic. Apples-to-apples comparison of multi-T vs single-T at same total energy.

**Key numbers**:
- w_0(GGE, multi-T) = -0.430, alpha_Z = 1.327
- w_0(single-T, same E) = -0.323, alpha_Z = 2.101
- Shift: delta_w_0 = -0.107 (33.3%), toward DESI
- Distance from DESI reduced by 25% (0.430 -> 0.322)
- Still 5.6 sigma from DESI (vs 7.4 sigma for single-T)
- Alpha shortfall: 4.0x (need alpha = 0.33, have 1.33)
- w_a = 0 (quasiparticles trapped in fiber, no free-streaming)
- No phantom crossing in any formulation

**S48 correction**: S48 used S46 quench-projection occupations (sum n_k = 1.000), not GGE occupations (sum n_k = 0.813). S48 w_0 band [-0.465, -0.589] needs revision. GGE Zubarev alpha = 1.327 gives w_0 = -0.430, OUTSIDE S48 band.

**Alpha definition**: S48 line 185: alpha = E/P (not P/E). w_0 = -1/(1+alpha) = -P/(E+P).

**Physical mechanism**: Multi-T redistributes pressure relative to energy. B2 modes (T=0.59) have P/E=0.78. B3 modes (T=0.15) have P/E=0.16. In single-T, all contribute P/E=0.48. GGE concentrates 95% of energy in low-alpha B2, increasing net P/E from 0.48 to 0.75.

**Why**: The DM/DE ratio alpha is COMPOSITION-DEPENDENT. Temperature non-uniformity is a physical effect on w_0.
**How to apply**: Any future w_0 computation must use GGE occupations (not S46 quench projection). The 4.0x alpha shortfall is the decisive number for DESI compatibility.

**Files**: `tier0-archive/s49_multi_t_friedmann.{py,npz,png}`
