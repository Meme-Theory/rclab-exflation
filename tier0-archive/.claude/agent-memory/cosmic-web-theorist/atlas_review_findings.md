---
name: Atlas Review Key Findings (2026-03-20)
description: Key positions from atlas collaborative review -- sigma_8 precision threshold, ALPHA-ENV-43 closure, void size function as next warning, K_pivot scope
type: project
---

## sigma_8 = 0.799 Discrimination Threshold
- Needs sigma(sigma_8) < 0.004 for 3-sigma discrimination from Planck (0.811)
- DESI Y5 void+galaxy forecasts sigma(sigma_8) ~ 0.006 (Paper 32)
- Euclid targets sigma(sigma_8) ~ 0.005 (Paper 33)
- Not achievable before ~2029 full Euclid survey
- sigma_8 = 0.799 NOT unique to framework -- massive neutrinos, WDM, f(R) all produce similar values

**Why:** The framework lists this as "sole surviving prediction" but it is currently indistinguishable from LCDM at available precision.

**How to apply:** Do not present sigma_8 = 0.799 as evidence for the framework. Present it as a consistency check that passes, with the precision threshold for a genuine test.

## ALPHA-ENV-43 is CLOSED (not queued)
- Closed in S43 by ALPHA-PATTERN-43 (W6-4)
- 1/sqrt(N_domains) suppression: N_domains ~ 10^74, signal ~ 10^{-44}
- MEMORY.md still lists it as "queued for S43+" -- that entry is STALE
- No surviving LSS discriminant unique to framework

**Why:** Previous memory entry was outdated.

**How to apply:** Correct any references to ALPHA-ENV-43 as "queued" or "sole surviving." It is permanently closed.

## Void Size Function as Next Warning
- n_v ~ sigma_8^5 amplifies alpha_s sensitivity
- alpha_s = -0.069 (O-Z) predicts 15-25% excess voids at R = 15-20 h^{-1} Mpc vs LCDM
- alpha_s ~ -0.035 (SA-Goldstone) predicts 8-12% excess
- DESI Y5 + ASTRA classification can detect at 3-5 sigma (O-Z) or 2-3 sigma (SA mixing)
- Should have flagged this in S49 instead of the sigma_8 overestimate

**Why:** Voids probe the small-scale tail of P(k) where spectral running accumulates, unlike sigma_8 which averages over R = 8 Mpc/h.

**How to apply:** In future discussions of LSS predictions, lead with void size function sensitivity, not sigma_8.

## K_pivot Invalidates ALL LSS Predictions (not just n_s)
- sigma_8 = 0.799 is conditional on the same K_pivot mapping as n_s and alpha_s
- If K_pivot > 0.5 M_KK: n_s >= 1 (excluded), alpha_s >= 0 (excluded), sigma_8 > 0.83 (excluded)
- Door 4 (sigma_8) should be reclassified as Window, conditional on EFOLD-MAPPING-52

**Why:** The atlas presents sigma_8 as independent of the n_s crisis, but they share the same load-bearing assumption.

**How to apply:** Always note sigma_8 conditionality on K_pivot when discussing surviving predictions.

## S8 Tension Status (2026)
- KiDS Legacy S8 = 0.815 +/- 0.021 (0.73 sigma from Planck) -- RESOLVED
- DES Y6 S8 = 0.768 +/- 0.022 (2.6 sigma) -- survey-specific systematics suspected
- ~70% of KiDS-DES discrepancy attributable to identified systematics (Paper 36)
- Framework prediction compatible with KiDS; if DES correct, framework is in the middle

## DESI DR3 Decision Tree
- BAO-only w_0 with sigma ~ 0.03 is the key measurement
- If |w_0 + 1| < 0.05 from BAO alone: framework survives
- If w_a remains at -0.65 with sigma(w_a) < 0.20: framework killed (w_a = 0 triple-locked)
- Wang-Mota (Paper 37) shows DR2 DDE preference driven by dataset tension + SN systematics
