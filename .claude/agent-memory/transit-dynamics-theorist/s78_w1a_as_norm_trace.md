---
name: S78 W1-A A_s Normalization Trace
description: PASS verdict for S78-W1-A-AS-NORM-TRACE; A_s=1.713e-9 at f*/POWER-RATIO/L_max=10, factor 0.996 of expected 1.72e-9; all 6 cross-checks PASS
type: project
---

Gate **S78-W1-A-AS-NORM-TRACE**: **PASS** (2026-04-15).

**Master equation (POWER-RATIO pinned, LINEAR)**: `A_s = F_amp × P_dS × f_conv × S_IC`

**Pinned product (f*, S_IC=1, L_max=10)**:
- F_amp(k_pivot) = 6857.69 (Wronskian ratio, scheme-independent)
- P_dS = 9.8075e-4 (H_dS²·(M_KK/M_Pl_red)²/(8π²·eps_dS), target units)
- f_conv^{SDW} = 2.5471e-10 (canonical spectral projection from s75)
- S_IC = 1 (symbolic baseline; W1-E supplies numerical value)
- **A_s^{framework}(f*) = 1.7131e-9** (vs expected 1.72e-9; factor 0.996)
- delta-to-Planck(2.1e-9) = **-0.0884 OOM**

**Why:** The S77 overproduction reading (+9.5 OOM) and the Lizzi-Landau match (-0.09 OOM) are NOT contradictory computations; they are two different FACTOR ASSIGNMENTS in the same ledger. The key was eliminating F_amp² (which S77 inherited). Under POWER-RATIO pin (F_amp linear), the pinned product matches Planck within factor 0.83.

**How to apply:** In any future S78+ computation touching A_s, use F_amp LINEARLY. Any d(ln A_s)/d(ln F_amp) that returns ~2 is a silent F_amp² bug.

**Three-account factor identification (not multiplicative R_scheme)**:
- **LL (Lizzi-Landau)**: NONE (pinned product, all four factors canonical) → A_s = 1.71e-9, -0.09 OOM
- **TE (Transit-Einstein)**: f_conv → 1 (claims (M_KK/M_Pl_red)² already in P_dS double-counts with f_conv) → A_s = 6.73, +9.5 OOM overproduction
- **SPT (SP-Transit)**: F_amp → 1 (backreaction cap at energy conservation) → A_s = 2.50e-13, -3.9 OOM underproduction

**Cross-checks (all six PASS)**:
1. Dimensional consistency: closed before numerics (all four factors dimensionless)
2. R-protection: f_conv^{zeta}/f_conv^{SDW} = 1/R_1 = 0.98736 exact (drift 0.0%, threshold 1.3%)
3. Null trace: A_s^{null}(F_amp=1, S_IC=1) = 2.498e-13; delta = log10(F_amp) = +3.8362 OOM exactly
4. **Code-level pin test**: d(ln A_s)/d(ln F_amp) = 1.000000 (POWER-RATIO confirmed in code)
5. Tilt ratio: 2^(1-n_s) = 1.0246 with Planck n_s (scheme-invariant)
6. Tag audit: 9/9 ledger entries fully tagged (value, scheme, convention, L_max)

**Three-scheme spread**: 0.0055 OOM (SDW vs zeta), well within factor-2 propagated error (0.301 OOM). Scheme-dependence NOT material for this gate.

**Files**:
- `computations/s78_as_normalization_trace.py`
- `computations/s78_as_normalization_trace.npz`
- `computations/s78_as_normalization_trace.png`
- `computations/s78_gate_verdicts.txt` (line 1)

**Rate-limiting for master gate**:
- W1-C (BACKREACTION-SELFCONSIST) decides whether SPT branch fires
- W2-D/W2-F resolve TE vs LL double-count question
- W1-E supplies numerical S_IC (currently symbolic = 1)

The branch selection CANNOT be made from W1-A alone. W1-A has produced a tagged, convention-pinned ledger with three factor-identified accounts.
