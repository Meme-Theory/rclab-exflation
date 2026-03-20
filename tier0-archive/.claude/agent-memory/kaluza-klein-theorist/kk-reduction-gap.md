---
name: KK Reduction Gap
description: The 12D->4D Kerner-type reduction on M4 x SU(3) was never executed — K_pivot, M_KK, and beta are all consequences of this gap
type: project
---

The framework went from 12D geometry directly to the spectral action, bypassing the standard KK step where integration over the fiber produces the 4D effective Lagrangian.

**Three unexecuted computations identified**:
1. KK modulus kinetic term from 12D Einstein-Hilbert (fixes G_mod = 5.0 from first principles)
2. DDG power-law running with 992-mode tower (fixes M_KK from measured gauge couplings; data exists in s44_dos_tau.npz)
3. KK derivation of SA-Goldstone mixing parameter beta (determines if beta > 0.9 at K < K*)

**Why**: W4 (monotonicity) is derivable from R_K(tau) monotonically increasing — pure geometry, no spectral action needed. The SA Seeley-DeWitt expansion at leading order IS the KK modulus potential. Subleading terms differ between SA and KK.

**How to apply**: When evaluating EFOLD-MAPPING-52 or Window 1, the KK reduction provides the modulus equation of motion. Without it, the e-fold count is approximate.

**Source**: atlas-kk-collab.md (summary/), compiled 2026-03-20
