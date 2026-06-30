---
name: S66 GOLDSTONE-GAP-SCALING Results
description: Spectral gap of SU(3) representation graph Laplacian closes as N^{-0.90} (Goldstone theorem), but N_crit = 10^{131} >> N=32 physical fabric. f_DM secure.
type: project
---

## S66 GOLDSTONE-GAP-SCALING Results

Gate: **FAIL** (alpha = 0.896 +/- 0.027 > 0.8)

**Why:** Goldstone's theorem mandates gap closure in the infinite-volume limit. U(1)^N -> U(1)_diag breaking produces N-1 massless modes as N -> infinity. The representation graph Laplacian eigenvalue lambda_1 ~ N^{-0.90} is the Weyl law for a bounded domain of the 2D Dynkin label lattice.

**How to apply:** The FAIL is a mathematical inevitability, not a threat to f_DM. Three protections:

1. N_crit = 4.0e131 (need 10^131 cells before gap reaches H_0). Physical fabric has 32 cells.
2. At N=32: omega_Gold_min = 0.387 M_KK = 2.0e58 * H_0. All modes spectacularly massive.
3. Leggett gap omega_L1 = 0.138 M_KK is N-independent (inter-band coupling, not finite-size). Even if ALL Goldstones became massless, Leggett-only DM gives f_DM ~ 0.26.

Key distinction: lambda_1 vs N scales as N^{-0.90}, but lambda_1 vs C_2^max scales as C_2^{-0.99} -- confirming the 2D Dirichlet Weyl law lambda_1 ~ 1/R^2 ~ 1/C_2_max.

Cross-check: lambda_1(N=32, unweighted) = 0.500273 matches s54 stored value exactly.

Files: `computations/s66_goldstone_gap.{py,npz,png}`
