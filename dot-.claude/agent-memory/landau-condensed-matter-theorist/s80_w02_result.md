---
name: S80 W0-2 W2-C REMED + L8 Drift Results
description: Zeta-Josephson abelian u(1) R-protection test; CLT hypothesis falsified in stronger-than-CLT direction
type: project
---

# S80 W0-2: R2 W2-C Clean Re-Run + P4-B CLT Test at L=8

**Why**: S78 W2-C drift_u1(L=6) = 83.75% exposed the u(1) abelian branch of Jensen-deformed SU(3) as violating per-branch R-protection. The P4-B closer (s79) hypothesized this was CLT-structured residual (drift^CLT(N) = 0.5 + 0.5/sqrt(N)), which would predict drift decreases with L. The L=8 measurement is decisive.

**How to apply**: Any future Kasparov-abelian argument on the SU(3) fiber must avoid the CLT dual-argument track. For dim H_pi = 1 branches, R-protection failure is STRUCTURAL not statistical.

## Results (S80)

- **S80-W2-C-REMED** = PASS: drift_u1(L=6)=83.7462% reproduces S78 ref 83.7500% to 0.005% under 5 PRU pins. Confirms S78 value was not a PRU artifact.

- **S80-W2C-L8-DRIFT** = FAIL-Sc2: drift_u1(L=8)=88.5390% > 80% (pre-reg threshold). CLT hypothesis (predicted 0.6768 at L=8, band [0.56, 0.76]) FALSIFIED.

## L-scan (GPU torch.linalg.eigvalsh, AMD RX 9070 XT)

| L | drift_u1 | CLT(L) | obs/CLT |
|:-:|:-:|:-:|:-:|
| 4 | 0.7367 | 0.7500 | 0.982 |
| 5 | 0.7975 | 0.7236 | 1.102 |
| 6 | 0.8375 | 0.7041 | 1.189 |
| 7 | 0.8653 | 0.6890 | 1.256 |
| 8 | 0.8854 | 0.6768 | 1.308 |

**Key structural reading**: drift monotonically INCREASES in L while CLT predicts DECREASE. Divergence grows (~33% by L=8). Abelian u(1) branch R-protection failure is asymptotic and structural, not finite-size or statistical.

## Mechanism implications

- **Closes** the CLT dual-argument track for W2-3 KASPAROV-ABELIAN-PROOF.
- **Preserves** the K-only track (Kasparov-module K-theoretic obstruction argument).
- **Strengthens** the integrability constraint requirement: any auxiliary condition must accommodate monotone non-decay of drift_u1 across L.
- **Preserves** S78 W2-C canonical value (83.75%) under PRU-pinned reproduction.

## PHONONIC classification

J_b^{func} quantities are second derivatives of the spectral action along branch-projected gauge directions — they are Josephson couplings of the substrate at the fold. Substrate-first: per-branch ratio J_b^{zeta2}/J_b^{SDW} tests whether the Mellin transform of each branch's |lambda| distribution preserves the branch's shape. For dim H_pi = 1 (u(1)/Cartan lambda_8 only), within-sector averaging is absent -> structural non-self-averaging.

## GPU refactor pattern (reusable)

Replaced numpy.linalg.eigvalsh with torch.linalg.eigvalsh for Hermitian complex128 matrices >= 100x100. On RX 9070 XT: ~40x speedup vs CPU. Cross-validation at 100x100: max abs err = 5.684e-14 (machine epsilon). For the L=8 run (biggest 2000x2000 matrix, 45 sectors, 33k eigenvalues): total 324s GPU vs projected hours CPU.

## Files

- `computations/s80_w2c_remed.py` / `.npz` / `.png`
- `computations/s80_w2c_l8_drift.py` / `.npz` / `.png`
- Working paper: `sessions/archive/session-80/session-80-results-workingpaper.md` §W0-2 (lines 133+)
- Verdicts: `computations/s80_gate_verdicts.txt` lines 9 (REMED) + 20 (L8-DRIFT)
