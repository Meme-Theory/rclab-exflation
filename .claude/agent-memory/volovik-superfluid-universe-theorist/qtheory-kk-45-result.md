---
name: qtheory-kk-45-result
description: S45 Q-THEORY-KK-45 INFO. Gibbs-Duhem crossing moves from 1.23 (S43) to 0.47 (S45), 2.6x closer. Inside domain [0,0.5] but outside gate [0.10,0.25]. Spline artifact at 0.223 identified and excluded. BCS correction (236% of TL) is key open channel.
type: project
---

## Q-THEORY-KK-45 Result (Session 45 W1-R1)

### Gate: INFO (2026-03-15)

Three S44 corrections (trace-log, EIH singlet, discrete KK tower) applied to q-theory self-tuning. Gibbs-Duhem zero crossing moves from tau* ~ 1.23 (S43 QFIELD-43) to tau* ~ 0.47 (S45). Factor 2.6 improvement. Inside physical domain [0, 0.50] but outside gate window [0.10, 0.25].

### Key Numbers
- tau*_S43 = 1.230 (polynomial full spectrum)
- tau*_S45 = 0.472 (trace-log singlet, quadratic fit to 7 eigenvalue points)
- tau*_artifact = 0.223 (SPLINE ARTIFACT from ratio-interpolation, excluded)
- tau*_TL_full = 1.454 (trace-log full spectrum)
- TL_singlet(fold) = -1.917 (negative: all eigenvalues < M_KK)
- rho_gs(fold) = -0.413 M_KK^4 units
- rho_gs(fold) in GeV^4 = 7.96e+64 (111.5 orders above obs)
- Suppression from S43: 1.8 orders (4.9e66 -> 8.0e64)
- Singlet eigenvalues: 3 distinct lambda^2 = {0.672, 0.714, 0.944} (16 modes total)
- BCS correction: 236% of TL (sign flip: -1.917 -> +2.599)
- mu_ref dependence: ZERO (cancels exactly in rho_gs)
- Epsilon convex: YES (within 7-point range, d2eps in [19.97, 21.48])

### Structural Findings
1. Trace-log + singlet projection QUALITATIVELY changes the structure: epsilon(tau) is negative-valued for singlet TL, moving the crossing 2.6x closer
2. Extended-data crossing at 0.223 is SPLINE ARTIFACT (inflection from ratio-interpolation, verified by direct 7-point convexity check)
3. BCS correction (Delta = 0.770) flips TL sign from negative to positive. This would restructure the Gibbs-Duhem entirely
4. mu_ref cancels EXACTLY in rho_gs (proven both analytically and numerically at 4 scales)
5. Singlet sector is INDEPENDENT of max_pq_sum truncation (always 16 modes)

### Key Open Channel
q-theory with BCS-corrected Bogoliubov spectrum: lambda_k^2 -> lambda_k^2 + Delta_k^2. This changes TL sign and curvature. Could pull crossing from 0.47 toward the fold. Requires tau-dependent Delta(tau).

**Why:** The single most important open computation (S44 7/7 convergence). Demonstrates q-theory structurally moves in the correct direction. BCS intersection is next.
**How to apply:** Any future CC computation should use q-theory on TL singlet with BCS correction, not polynomial full SA. The bare TL singlet gives tau* = 0.47. BCS correction is the decisive next step.

Files: s45_qtheory_kk.py, s45_qtheory_kk.npz, s45_qtheory_kk.png
