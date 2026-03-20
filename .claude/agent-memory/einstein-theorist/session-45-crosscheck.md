---
name: session-45-crosscheck
description: KZ-NS-45 cross-check results -- Bogoliubov coefficients endorsed, n_s extraction rejected as structurally ill-defined on discrete SU(3) spectrum
type: project
---

# Session 45: KZ-NS-45 Einstein Cross-Check

## Task
Independent verification of Bogoliubov coefficients and spectral tilt n_s
from Kibble-Zurek particle creation during the tau=0 -> tau=0.19 transit.

## Key Results

### Bogoliubov Coefficients: ENDORSED
- Scenario A (gap disappears, physical): |beta_k|^2 in [1.63e-5, 3.03e-2], n_pair = 315.7
- Scenario B (gap unchanged, reference): |beta_k|^2 in [7.28e-8, 4.17e-3], n_pair = 45.4
- Scenario C (no gap): |beta_k|^2 in [1.18e-7, 5.70e-3], n_pair = 66.9
- Matches primary agent to 6+ significant figures across all 992 modes

### n_s: STRUCTURALLY ILL-DEFINED
- n_s spans [-2.0, +5.8] across k-mappings and scenarios
- R^2 < 0.05 for eigenvalue-based k-mappings (P(k) is not a power law)
- R^2 ~ 0.99 for dim^{1/3} mapping but gives n_s ~ 3-4 (wrong value)
- 5 structural obstacles: discrete spectrum, eigenvalue reordering, degeneracy dominance, no scale separation, compact manifold

### WKB Assessment
- Physical transit: Q_median = 19.5, 99% non-adiabatic
- Sudden approximation EXACT for the physical transit
- WKB valid only for dt > 0.10 M_KK^{-1} (90x slower than physical)

### Quench Profile Sensitivity
- 5 profiles tested (3 linear ramps, 2 tanh)
- |beta_k|^2 suppressed 2.5-3.5x for finite-time quenches
- n_s INSENSITIVE to profile (all ~3.2-3.5, R^2 < 0.05)

## Principle-Theoretic Diagnosis
The k-mapping (internal SU(3) mode -> 4D wavenumber) is not a free parameter
to be chosen but must be DERIVED from the EIH projection. No such derivation
exists. This is not a technical uncertainty; it is a missing step in the
physical argument. Asking for n_s from 992 discrete modes spanning a 2.2x
dynamic range is like asking for the refractive index of a single atom.

## Files
- Script: `tier0-archive/s45_kz_ns_crosscheck.py`
- Data: `tier0-archive/s45_kz_ns_crosscheck.npz`
- Results: `sessions/archive/session-45/session-45-results-workingpaper.md` (W1-2x section)
