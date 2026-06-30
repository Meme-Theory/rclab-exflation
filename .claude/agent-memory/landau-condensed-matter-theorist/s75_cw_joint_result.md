---
name: S75 CW-Joint A_s and n_s result
description: S75-A4-CW-JOINT FAIL. n_s=0.9595 passes (1.28 sigma) but A_s=243.5 is +11.06 OOM above observed. H_fold^2/(8*pi*a_2*eps_H) formula. Same conversion problem as W1-G and W2-H.
type: project
---

## S75-A4-CW-JOINT: FAIL

Gate: n_s in [0.955, 0.975] AND |log10(A_s/A_s_obs)| < 1.0

**Results**:
- n_s (Hubble) = 0.959506 (1.28 sigma, PASSES sub-criterion)
- A_s (spectral) = 2.435e+02, log10(A_s/A_s_obs) = +11.064 (FAILS)
- eps_H = 0.020247 (shape parameter, OK)
- eps_V = 5.263 (slow-roll VIOLATED in potential convention)

**Key formula**: A_s = H_fold^2 / (8*pi * a_2 * eps_H) -- purely spectral, M_KK-independent.
- H_fold = 586.5, a_2 = 2776.2, eps_H = 0.02025
- All three fixed by spectral triple. A_s is a prediction, not adjustable.

**Why:** The 11-OOM gap comes from H_fold >> 1 (transit is supersonic, Mach 13.75). This is the same conversion/projection problem seen from all A_s routes.

**How to apply:** The CW route succeeds for n_s (shape) but fails for A_s (absolute scale). Any future A_s computation must address the conversion factor between spectral action internal energy and 4D perturbation amplitude. The bottleneck is NOT the one-loop correction or BCS dressing -- it is the transit Hubble parameter.

**Four A_s routes compared**:
1. Standard slow-roll (eps_V): invalid (eps_V >> 1)
2. Hamilton-Jacobi (transit H): +10.98 OOM
3. Spectral formula: +11.06 OOM
4. Bogoliubov (S74 W1-G): +9.47 OOM
All independent, all FAIL, all point to conversion problem.
