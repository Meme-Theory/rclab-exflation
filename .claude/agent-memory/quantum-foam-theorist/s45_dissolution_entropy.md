---
name: S45 Dissolution Entropy Results
description: DISSOLUTION-ENTROPY-45 INFO. S_ent(eps_c) ~ N^{0.106} (sub-volume, near-logarithmic). S/S_Page ~ 0.5 at all N. Entanglement phase transition at dissolution.
type: project
---

## DISSOLUTION-ENTROPY-45 (S45, W6-7)

### Gate Verdict: INFO (characterization, not pass/fail)

### Key Results

**QF-81**: S_ent(epsilon_c, N) ~ N^{0.106} (R^2 = 0.890) or ~ 0.151*ln(N)+0.457 (R^2 = 0.871).

| max_pq_sum | N | d_A | S_ent(eps_c) | S_Page | S/S_Page |
|:-----------|:--|:----|:-------------|:-------|:---------|
| 1 | 112 | 8 | 1.216(27) | 1.794 | 0.678 |
| 2 | 432 | 18 | 1.201(37) | 2.515 | 0.478 |
| 3 | 1232 | 28 | 1.561(22) | 3.014 | 0.518 |
| 4 | 2912 | 52 | 1.617(40) | 3.487 | 0.464 |
| 5 | 6048 | 72 | 1.805(34) | 3.848 | 0.469 |

- Constant scaling EXCLUDED (R^2 = -0.001).
- S/S_Page ~ 0.5 at all N (mean 0.521). Universal half-Page entanglement at dissolution.
- Bipartition: C^N = C^{d_A} x C^{d_B} with d_A = largest divisor of N <= sqrt(N).

### Physical Significance

- Entanglement scaling = SUB-VOLUME (area law + logarithmic correction).
- Classification: dissolution is a QUANTUM CRITICAL POINT (Calabrese-Cardy type).
- Spectral crossover (<r> = midpoint) and entanglement buildup occur at same eps_c.
- Entanglement NOT saturated at eps_c; full Page value requires eps >> eps_c.
- Half-Page universality (S/S_Page ~ 0.5) is a structural finding across 5 data points.
- Emergence sequence: spectral triple exists below dissolution scale, dissolves above it.

### Connection to W-FOAM-7

- S44: epsilon_c ~ N^{-0.457} (threshold vanishes). SPECTRAL diagnostic.
- S45: S_ent(eps_c) ~ ln(N). ENTANGLEMENT diagnostic.
- Both confirm: spectral triple is emergent. Dissolution = quantum phase transition.

### Files
- Script: `tier0-archive/s45_dissolution_entropy.py`
- Data: `tier0-archive/s45_dissolution_entropy.npz`
- Plot: `tier0-archive/s45_dissolution_entropy.png`
