---
name: S80 W0-15 Branch Shortfall Determination
description: Definitive determination that phonon-first's "1D K-cut absorbs Cartan moduli" diagnosis is wrong; the 2 Cartan moduli ARE present as Leggett-1/2.
type: project
---

# S80 W0-15 FOLLOWUP: Rank-Universality Branch-Shortfall

**Date**: 2026-04-17
**Session**: S80, Wave 0 item W0-15 followup
**Primary (phonon-first) verdict**: INFO-6; diagnosed as "1D K-cut absorbs one Cartan moduli"
**Followup (this agent) verdict**: REFUTED — the diagnosis is wrong; correct cause is dual-basis mismatch

## Why: the load-bearing structural fact

The s52 model is a **3-sector BCS phase/amplitude decomposition** (3 complex order parameters Delta_B1, Delta_B2, Delta_B3), NOT a decomposition of the 8 Gell-Mann generators.

- s52: 6 DOF per cell = 3 amplitudes + 3 phases (polar decomposition, basis-independent)
- rank-universality: 7 = 8 gen - 4 Goldstones + 2 Cartan + 1 photon

These are TWO DIFFERENT PARTITIONS of the same substrate:

| s52 branch | rank-universality slot | Identification |
|---|---|---|
| Goldstone (ω=0) | overall U(1)_B (not in rank-univ count) | diagonal phase (1,1,1)/√3 |
| Leggett-1 (ω=0.138) | Cartan h_1 (slot B) | ortho_frac=0.80 |
| Leggett-2 (ω=0.192) | Cartan h_2 (slot C) | ortho_frac=0.82 |
| Branch-3 (ω=0.378) | Higgs slot F (×3) | B1 amp, T-amp_frac=1.0 |
| Branch-4 (ω=1.410) | Higgs slot F (×3) | B2 amp, T-amp_frac=1.0 |
| Higgs-1 (ω=11.47) | Higgs slot F (×3) | B3 amp, T-amp_frac=1.0 |

## How to apply

1. W0-14 canonicalization: canonicalize 6 entries (OPTION b), with explicit annotation mapping to rank-universality slots.
2. Missing slot = A (photon/c_mod residual gauge). It is absent from the BCS-sector basis because there is no unbroken gauge — the photon lives in the M^4-gauge-field sector of M^4 × SU(3), not in the SU(3) collective-mode sector. In Paper 15, c_mod=1.000 is the unbroken U(1)_EM after SU(3)_c × SU(2)_L × U(1)_Y breaking.
3. Future Q: do NOT cite "1D K-cut" as the structural cause of the 6-vs-7 gap. The K-space is explicitly 3D BCC (s52 lines 216-267).
4. Future Q: if 2D-BZ extension is run in S81, prediction is STILL 6 branches — because 6 DOF per cell is basis-independent, fixed by polar decomposition of 3 complex order parameters.

## Key quantitative verifications (via Python, verified)

- Branch 0 phase-block = [+0.5774, +0.5774, +0.5774] = (1,1,1)/sqrt(3) EXACTLY (unit projection onto total-phase direction).
- Branches 1, 2 have ortho_frac ≥ 0.80 in the 2D Cartan subspace.
- T-weighted amplitude fraction: Branches 3, 4, 5 are PURE amplitude (w_amp=1.0000, w_phase=0.0000). The Euclidean amp_frac in s52 §9 was misleading (gave 0.068, 0.254, 2.07) because generalized eigenvectors are not Euclidean-orthonormal.
- Branch-3/Branch-4 labels are diagnostic artifacts — they are physically Higgs-B1 and Higgs-B2.

## Files

- Script: `computations/s80_branch_shortfall_baptista.py`
- Results section: `sessions/archive/session-80/session-80-results-workingpaper.md §W0-15 Results (followup, baptista-spacetime-analyst)`
- Verdict line: appended to `computations/s80_gate_verdicts.txt`
