---
name: S82 W2-11 S++-FULL-ED result
description: S82 full-ED audit on (0,0)+(1,1) subspace — PASS by machine precision via Z_2 gauge degeneracy theorem
type: project
---

# S82 W2-11 S++-FULL-ED

**Verdict**: PASS (pre-registered), but the structural finding is that the
s++/s+- margin on the 2-active-sector subspace is EXACTLY ZERO by Z_2 gauge
invariance, not by convergence.

## Why the margin is structurally zero

Two-sector Richardson-type Hamiltonian with ONE inter-sector Josephson bond:
H(+J) and H(-J) are unitarily equivalent via U = diag((-1)^{n_a}).

Verified bitwise: max|spec(H(+J)) - spec(H(-J))| = 0.00 (exact, 3-mode test).

## Physical reading

- The 2-sector / 1-bond graph has no loop → Aharonov-Bohm flux is trivial →
  sign is pure gauge.
- The s78_w1d mean-field margin (5.81e-04) was a GAUGE ARTIFACT of the
  uniform-gap BdG anomalous-block sign flip — a stronger reading than the
  R1/R2 workshop framing of "iteration noise."
- The 4-sector MF Eliashberg determination of s++ remained sensible because
  the 4-sector graph HAS loops. The s++ label does NOT transfer to the
  projected 2-active subspace.

## Carry-forward

Any framework observable claimed to depend on s++/s+- on the 2-sector subspace
must factor through a loop observable or an explicit Z_2-breaking term.
Enumerate such observables in a future session.

## File pointers
- Script: `computations/s82_w2_11_s_pp_full_ed.py`
- Data: `computations/s82_w2_11_s_pp_full_ed.npz`
- Plot: `computations/s82_w2_11_s_pp_full_ed.png`
- Working paper: §V.K in `sessions/archive/session-82/session-82-results-workingpaper.md`
- Verdict: `computations/s82_gate_verdicts.txt`
  (line: `S82-S-PP-FULL-ED: PASS -- value=-5.807769e-04 scheme=EXACT-DIAG convention=fstar L_max=9 sha256=00052e55d7a4b463d1ca22ea011ff172b871700a5072ad5b1c8918992fc4345c`)
