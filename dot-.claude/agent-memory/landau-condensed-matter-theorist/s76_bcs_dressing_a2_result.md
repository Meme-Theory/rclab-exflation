---
name: S76 BCS dressing of a_2 result
description: BCS correction to spectral moment ratio a_2/a_0 -- INFO verdict, wrong sign, f_conv BCS-immune
type: project
---

**Gate S76-B4-BCS-DRESS: INFO**

BCS dressing of the a_2 Seeley-DeWitt coefficient at the fold.

- delta_a_2 = -4.501 (from 16 eigenvalues in (0,0) singlet sector)
- delta_a_2/a_2(canon) = -1.62e-3 (-0.162%)
- A_s(bare) = 1.585e-9, A_s(BCS) = 1.579e-9
- Gap: -0.122 OOM -> -0.124 OOM (widens by 0.0014 OOM)
- WRONG SIGN: delta_a_2 < 0, A_s decreases, gap widens

**Why:** BCS pairing replaces lambda_k -> E_k = sqrt(lambda_k^2 + Delta^2) for modes near the Fermi surface. This pushes eigenvalues APART, reducing the inverse-square spectral sum. Only 16/(12880 PW) eigenvalues participate (singlet sector). The correction is real (~0.16%) but has the wrong sign for closing the A_s gap.

**How to apply:** f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 is BCS-immune. The 0.12 OOM A_s residual cannot be resolved by spectral moment corrections. A_s(fiber) is the remaining degree of freedom.

Key normalization note: canonical a_2_fold uses Peter-Weyl (dim d_pq) weighting from heat-kernel extraction, not d_pq^2 used by S72 spectral action scripts. For (0,0) sector both give the same delta_a_2 since d=1. f_conv uses M_Pl_unreduced (1.221e19 GeV), not M_Pl_reduced (2.435e18 GeV).

All 5 cross-checks PASS. Consistent with S72v2 (BCS dressing of n_s also negligible: +3.8e-6).
