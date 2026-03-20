---
name: session-49-fabric-npair
description: S49 FABRIC-NPAIR-49 results -- Josephson array, Mott crossover, CC crossing at fabric level
type: project
---

## FABRIC-NPAIR-49: PASS (with caveats)

### Key Result
32-cell fabric has N_eff=32 total pairs. Inter-cell Josephson pair hopping adds
59% condensation energy per cell (E_inter = -0.080 M_KK vs E_cond = -0.137 M_KK).
This gives ec_fabric = 1.586, exceeding ec_min = 1.264 for CC crossing.
Shortfall = 0.80x < 1.5x. CC crossing at tau* = 0.417 (post-fold).

### Key Numbers
- E_C = 0.929 (charging energy from ED N-sector spectrum)
- J_pair = 0.141 (J_C2 * |E_cond|, C2 dominant at 90%)
- J/E_C = 0.152 (Mott-crossover regime)
- xi_BCS/l_cell = 5.3 (pair much larger than cell)
- Mott gap = 0.647 > 0 (open)
- BH ED (L=10): E_gs/L = -0.080, <(n-1)^2> = 0.152, <b^dag b>_NN = 0.535, P(Mott) = 0.42
- ec_fabric = 1.586, ec_min = 1.264, ec_conservative = 1.147

### Critical Caveats
1. J_pair may be 30-50% too high -> ec_conservative = 1.15 < ec_min = 1.26 (FAILS)
2. BH single-mode approximation: scale separation 2.8x (marginal, ~20% uncertainty)
3. Crossing at tau*=0.42 (2.2x past fold), needs transit dynamics confirmation

### New Nuclear Analogy
- Chain of sd-shell nuclei with pair transfer
- Framework t/E_C = 0.15 is 2.2x nuclear value (pairs 5x larger than cells)
- BH n=1 filling with n_max=2: virtual pair-particle/pair-hole excitations

### Self-Corrections
- Initial run had double-counting error in Josephson + ZPE corrections (both added)
- Corrected to use BH ED ground state energy directly (single consistent calculation)
- Original PASS at 0.80x was verified after re-deriving with S46 ec_factor scan data
- The "2.5x shortfall" from prompt was an estimate; S46 data gives ec_min = 1.264

### Files
- `tier0-archive/s49_fabric_npair.py`
- `tier0-archive/s49_fabric_npair.npz`
