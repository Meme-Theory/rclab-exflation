---
name: S72 BCS-DRESSED-SA-72 Results (v2 mode-selective, supersedes v1)
description: Mode-selective BCS-dressed spectral action -- INFO, n_s=0.9567 (essentially bare), BCS correction negligible (3.8e-6)
type: project
---

Gate BCS-DRESSED-SA-72 (v2, mode-selective): **INFO**. n_s^{BCS} = 0.95675, |n_s - 0.9649| = 0.0082 (1.94 sigma).

**v1 (SUPERSEDED, WRONG)**: Applied Delta=0.4643 uniformly to all 1232 eigenvalues, gave n_s=0.9756 (FAIL, 2.54 sigma overshoot). This was physically wrong -- 4900x overestimate.

**v2 (CORRECT)**: Only 16 eigenvalues in (p,q)=(0,0) sector participate in BCS pairing. These carry d^2=1 weight in a spectral action dominated by d^2=225 sectors. Mode-selective BCS correction to n_s is 3.8e-6 (four OOM below Planck uncertainty).

Key numbers:
- eps_H^bare = 0.02163, eps_H^BCS(selective) = 0.02163 (shift: -8.9e-5%)
- n_s^bare = 0.95674, n_s^BCS(selective) = 0.95675
- delta_ns decomposition: +6.2e-7 (fixed-Delta) + 3.2e-6 (gap running) = +3.8e-6 total
- (0,0) sector: 16/155,984 weighted eigenvalues = 1.0e-4 of total
- Per-band S-shift: B2 52.1%, B3 34.5%, B1 13.4%
- Uniform cross-check: n_s=0.9756 exactly reproduces v1 (confirming error was in physics, not numerics)

**Why:** BCS condensate is a color-singlet pairing phenomenon. Only trivial-rep (0,0) modes pair. Higher (p,q) sectors carry color charge and are spectators. The (0,0) sector contributes 0.006% of the total spectral action.

**How to apply:** BCS pairing has NO significant effect on n_s. The bare n_s=0.9567 stands at 1.94 sigma from Planck. The n_s gap must be closed by a mechanism that modifies the FULL spectral action (all sectors), not just the BCS subsystem. Candidates: CW one-loop (acts on all modes), spectral functional f(x) selection, finite-size corrections.

PERMANENT: Mode-selective BCS dressing is negligible for the spectral index. The v1 uniform-gap result was a 4900x overestimate.
PERMANENT: The (0,0) sector contributes 16/155,984 of the weighted spectral sum. Any BCS effect on bulk spectral moments is O(1e-4).

Files: `computations/s72_bcs_dressed_sa_v2.{py,npz,png}` (supersedes v1)
