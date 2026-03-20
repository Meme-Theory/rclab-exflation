---
name: KZ-SPATIAL-50 result
description: S50 KZ-SPATIAL-50 FAIL. Spatially-resolved KZ on 32-cell fabric featureless. delta_n/n=1.59e-4. Sudden-quench universality theorem. 13th n_s route CLOSED.
type: project
---

## S50 KZ-SPATIAL-50: FAIL

Spatially-resolved Kibble-Zurek pair creation on 32-cell fabric (4x4x2 lattice).

**Key numbers:**
- delta_n/n = 1.59e-4 (fractional density variation across cells)
- var(n)/<n>^2 = 2.52e-8 (power spectrum amplitude)
- P_LZ(B2) = 0.9968 (deep sudden-quench regime)
- |ln P_LZ| = 3.16e-3 (exponential suppression factor)
- n_s fit = -1.21 +/- 0.78 (UNDEFINED, fitting noise)
- 600 parameter configurations all give featureless spectrum

**Why:** Sudden-quench universality theorem. The transit is deep in the sudden regime (tau_Q << tau_0 for all sectors). P_LZ ~ 1 exponentially, so sensitivity to local quench rate is exp-suppressed:
  delta_P/P = |ln P_LZ| * delta_rate/rate = 3.2e-3 * 0.033 = 1.05e-4

**How to apply:** 13th n_s route CLOSED. Spatial KZ cannot produce red tilt because transit is too fast. 3He analog: KZ defect density n ~ 1/xi^d independent of quench details in sudden limit. Remaining n_s routes must use mechanisms beyond single-mode LZ (multi-mode interference, spectral function, order parameter texture).
