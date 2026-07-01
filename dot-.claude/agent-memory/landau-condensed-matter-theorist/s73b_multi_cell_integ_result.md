---
name: S73B MULTI-CELL-INTEG-73B result
description: N_pair=4 level statistics on 4-cell C_4 ring from CG(24) -- R-G integrability survives
type: project
---

# S73B W3-B: MULTI-CELL-INTEG-73B

**Date**: 2026-04-10
**Gate**: PASS. <r> = 0.4044 +/- 0.0015 < 0.45 threshold. Brody eta = 0.000.

## Key Result

Multi-cell Richardson-Gaudin integrability SURVIVES at N_pair = 4 on the 4-cell C_4 ring subgraph of CG(24). The 35,960-state Hilbert space fully diagonalized via Z_4 cyclic orbit decomposition.

Reference values:
- Poisson (integrable): 0.386
- GOE (chaotic): 0.536
- Measured: **0.4044** (alpha = 0.123, only 12.3% from Poisson toward GOE)

## Critical Structural Insight

**Multi-cell N_pair=4 is MORE integrable than single-cell N_pair=4**.

- S73B W2-E single cell, N=4 sector: <r> = 0.5596 (GOE-like)
- S73B W3-B 4-cell C_4, N_pair=4: <r> = 0.4044 (Poisson)

The single-cell chaos at N=4 is a **Fock-space saturation artifact** (N=4 saturates 8-mode single-cell filling). Distributing the same particle number across 4 cells restores the dilute R-G regime where Cooper pairs decorrelate. The physical fabric (32 cells) is ALWAYS in this dilute limit.

## Method: Z_4 Orbit-Based Symmetry Reduction

- Dense 35,960 x 35,960 matrices require 10 GB; computationally prohibitive.
- Orbit decomposition: period-1 (8 orbits), period-2 (56), period-4 (8960). Total 9024 orbits.
- Sector dimensions: k=0 (9024), k=pi/2 (8960), k=pi (9016), k=3pi/2 (8960). Sum = 35960 (verified).
- Per-sector ~9000x9000 complex Hermitian, diagonalized via eigvalsh.
- Matrix element formula: <k, o' | H | k, o> += amp * sqrt(p_o / p_o') * exp(i*k*n')
  where n' is the orbit phase of the target state.
- Trace cross-check: sum of all sector eigenvalues = direct trace of diagonal H to 4.5e-9.

## Physical Parameters

- E_J = 3.3969 M_KK (from S56 self-consistent)
- Delta_BCS = 0.4643 M_KK (canonical)
- E_J/Delta = 7.32 (strong coupling, Josephson-dominated)
- 8 modes per cell (4 B2 + 1 B1 + 3 B3)
- V_fold from S56 (includes B2 scattering channel)

## Control Pathology (Important)

E_J = 0 control gave <r> = 0.2272, pathologically below Poisson. This is a DEGENERACY artifact, not a methodology failure:
- When cells decouple, spectrum = direct sum of single-cell products.
- 6762/9023 gaps are < 1e-10 in k=0 sector (massive degeneracies).
- Filtering degenerate gaps: <r>_ctrl = 0.3918 (exactly Poisson, as expected).

The Josephson term LIFTS these local-pair-number degeneracies but does NOT induce chaos.

## Files

- `computations/s73b_multi_cell_integ.py`
- `computations/s73b_multi_cell_integ.npz`
- `computations/s73b_multi_cell_integ.png`
- Runtime: 429 s

## Implications

1. **R-G integrability wall INTACT at multi-cell N_pair=4**. Strongest test to date.
2. **Luttinger superselection (S73A) and intra-sector integrability are INDEPENDENT**. Both hold.
3. **GGE statistical description strengthened**. Dilution across cells restores integrability.
4. **Ordered Veil picture consistent**. Chaos doesn't emerge from multi-cell physics.
5. **Next frontier**: N_pair >= 5 (Fock saturation onset), or lower-symmetry topologies.
