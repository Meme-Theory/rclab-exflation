---
name: S77 N-PIVOT-MAP Results
description: CRITICAL normalization finding -- k_pivot SUBhorizon at fold (not 57 OOM superhorizon); N_pivot=3.12; mode equation needs re-solving with k=14.31 M_KK
type: project
---

## S77-B1-NPIVOT: N_pivot Map

**Date**: 2026-04-13
**Gate**: S77-B1-NPIVOT (INFO)

### Critical Finding: S73B Normalization Error

S73B compared k_pivot (physical today, a_today=1 convention) = 4.30e-57 M_KK with aH (fold trajectory, a_fold=1 convention) = 0.975 M_KK. Mixed normalizations. The correct comoving k in fold normalization is:

k_pivot(fold) = k_pivot(today) * exp(N_total) = 14.31 M_KK

Mode is **SUBhorizon** at the fold: k/aH = 14.7.

### Key Results

| Scale | k_com [M_KK] | N_exit | N_before_rh |
|-------|-------------|--------|-------------|
| k_today | 0.064 | superhorizon at fold | >63.4 |
| k_recomb | 1.19 | 0.60 | 62.8 |
| k_pivot | 14.31 | 3.12 | 60.3 |
| k_BBN | 9.95e6 | 16.57 | 46.8 |

N_* = 60.3 (consistent with standard inflation for T_rh ~ 10^16 GeV).

### Impact

- k^2/(z''/z) ~ 108 at fold (NOT 1.04e-116 as W1-B reported)
- F_amp NOT necessarily 1 -- re-evaluation required
- Mode oscillates inside horizon for first 3.1 e-folds
- Stiff-to-dS transition DIRECTLY affects CMB pivot mode
- W1-B A_s computation needs complete revision

**Why**: The mode equation for k_pivot must be re-solved with k = 14.31 M_KK, not 4.30e-57 M_KK. This changes the entire structure of the A_s computation: the pivot mode is NOT frozen from birth; it has 3.1 e-folds of subhorizon evolution where the mode equation dynamics matter.

**How to apply**: Any future mode equation computation must use the correct comoving k in fold normalization. The "57 OOM superhorizon" statement from S73B should be flagged as incorrect whenever referenced.
