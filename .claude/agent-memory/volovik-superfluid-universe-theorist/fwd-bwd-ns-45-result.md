---
name: fwd-bwd-ns-45-result
description: S45 FWD-BWD-NS-45 FAIL (908 sigma). Forward/backward pair creation asymmetry gives n_s=-2.847. Red tilt confirmed but slope -3.85 (need -0.035). 4th n_s route closed. (Delta/omega)^4 power law is structural.
type: project
---

## FWD-BWD-NS-45 Result (Session 45 W5-R5)

### Gate: FAIL (2026-03-15, 908 sigma)

Forward/backward Bogoliubov pair creation asymmetry at q-theory equilibrium tau*=0.209 produces red-tilted spectrum but n_s = -2.847, far outside [0.80, 1.10].

### Key Numbers
- n_s (per-mode, primary): -2.847 +/- 0.032
- n_s (with Weyl): +2.695
- n_s (fwd-only): -2.855
- R(k) slope: -7.739
- R^2 (per-mode): 0.967
- Planck deviation: 908 sigma
- BCS enhancement: 310x mean over bare
- R(k) range: [0.11, 2.86e8] — 9 orders of magnitude spread
- B3 has R < 1 (backward dominates for smallest gap)

### Sensitivity
- tau_back: n_s ranges -2.86 (0.21) to -0.68 (0.50) — always negative
- Delta: n_s ranges -3.92 (0.5x) to -1.89 (2x) — always below -1.8
- EIH weighting: n_s = -2.60
- Forward at tau=0.15: n_s = -3.28

### Structural Diagnosis
Same root cause as KZ-NS-45: |beta_k|^2 ~ (Delta/omega_k)^4 at high omega. Spectrum spans 2.5x in eigenvalue, Delta constant -> steep power law n_s ~ -3. No infrared acoustic regime in KK tower.

### N_s Route Closure Count
1. Lifshitz eta (S44 W1-3): FAIL (eta=0 mean-field)
2. Bogoliubov quench (KZ-NS-45): FAIL (n_s=-0.588, 370 sigma)
3. Forward/backward asymmetry (FWD-BWD-NS-45): FAIL (n_s=-2.847, 908 sigma)
4. (epsilon_H invariance, S44 W4-3: FAIL by construction)

All 4 routes closed. Any future n_s must invoke k-dependent Delta or entirely different physics.

**Why:** The (Delta/omega)^4 power law is structural: BCS gap is approximately constant across the KK tower while eigenvalues span a factor of 2.5x. This makes every Bogoliubov-based n_s mechanism produce slopes ~ -4 (too steep by 100x).

**How to apply:** n_s from KK Bogoliubov pair creation is permanently closed (4 routes, all FAIL). Next n_s attempt must either (a) find k-dependent Delta(k) that flattens the tilt, or (b) invoke physics outside Bogoliubov channel (e.g., topological defects, domain wall correlations).

Files: s45_fwd_bwd_ns.py, s45_fwd_bwd_ns.npz, s45_fwd_bwd_ns.png
