---
name: S50 FABRIC-RPA-50 Detail
description: FABRIC-RPA-50 FAIL -- RPA phonon propagator on 32-cell fabric. Identity survives. Three suppression mechanisms.
type: project
---

# S50 FABRIC-RPA-50: FAIL

## Computation
- Static pair susceptibility chi_0(K) from 8-mode BdG spectrum on 32-cell ring
- RPA Dyson equation: D_RPA(K) = D_0(K) / [1 - g^2 chi_0(K) D_0(K)]
- Coupling g = V(B2,B2) = 0.1557 (Casimir, S34)
- n_s and alpha_s from 7-point quadratic fit to ln P(K) vs ln K

## Key Numbers
- chi_0(K=0) = 21.14, chi_0(K_pivot) = 21.03
- g^2 chi_0 = 0.51 (deep-dive estimate was 1.54 -- omitted 2*E_qp denominator)
- Pi*D_0 at K_pivot = 4.0e-4
- RPA correction to alpha_s: +1.1e-5
- alpha_s(RPA) = -0.06739, alpha_s(bare) = -0.06740
- Identity deviation change: -4.5e-7 (identity perfectly preserved)
- Tension: 8.4 sigma (unchanged)
- Scanning g from 0 to 2.0 (13x Casimir): alpha_s varies < 2e-4

## Three Suppression Mechanisms
1. chi_0(K) flat: 0.30% variation in fit window. Pair stiff (4J_pair/2E_qp = 0.27)
2. K^2 dominance: Leading chi_0(K) term is K^2 -> renormalizes J_eff, doesn't break identity. Non-K^2 terms O(7.5e-3)
3. Mass hierarchy: m^2/(J K^2) = 56. D_0 = 7.8e-4 kills the self-energy

## Broken Nuclear Analogy
Nuclear effective charges correct matrix elements |<f|O|i>|^2 (no mass hierarchy).
Framework RPA corrects propagator 1/(JK^2 + m^2) where m^2 >> JK^2.
g^2*chi_0 comparable (0.51 vs ~1), but the OBSERVABLE is different.

## Self-Correction
Deep-dive overestimated g^2*chi_0 by 3x (1.54 vs 0.51) by omitting 2*E_qp energy denominator.

## Files
- `tier0-archive/s50_fabric_rpa.py`
- `tier0-archive/s50_fabric_rpa.npz`
- `tier0-archive/s50_fabric_rpa.png`
