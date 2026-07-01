---
name: S82 W2-5 Heat-Kernel MP-Exclusion Theorem (PROVEN)
description: Formal proof that regulators with sqrt(x) cusp at x=0 fail MP in continuum; finite-L_max carves out a trivially-admissible regime. S82-HEAT-KERNEL-MP-EXCLUSION PASS.
type: project
---

S82 W2-5 proved the MP-exclusion theorem for non-C^1 regulators with fractional-power branches at x=0. Verdict: PASS with proof_status=PROOF-COMPLETE, closure_sha 98267d631c9f7a2c57f68e5feb767284a211f1987bc1e7fd412f2cfdfbf693c0.

Why: four independent substitution chains all support the same structural obstruction:
  1. f*(x) = 0.912 sqrt(x) + 0.088 exp(-x) fails C^1 at x=0 (f*'(0+) = +inf).
  2. sqrt(x) fails Hausdorff-Bernstein-Widder completely-monotonic test at n=1; no positive Radon Laplace-Borel measure exists.
  3. Mellin transform of sqrt(x) contributes t^(-3/2) branch-point, outside integer dimension spectrum Sd -> log(Lambda^2) corrections to MP.
  4. At finite L_max, Tr_{L_max} f* is a finite sum of positive reals, trivially convergent.

How to apply:
- When discussing f* vs {SDW, zeta, anomaly-sharp} regulator contrast, cite this as the STRUCTURAL reason f* is categorically outside the sibling cluster, not a numerical coincidence.
- The a_0-vs-a_2 sign flip under f* (P4-C §E2) is now understood as a manifestation of MP-non-uniformity projected onto different spectral moments.
- Discrete-spectrum carve-out: step regulators (anomaly-sharp) survive in the finite D_K sum via indicator-on-measure-zero-set argument; P4-C §E4 S80-DISCRETE-MP-ADMISSIBILITY pre-registered for formal enumeration.
- Taxonomy (§V.E.3): fractional-power, log-type, step in continuous MP -> excluded; sum-of-exp, pure exp -> admissible; step in discrete-spectrum sum -> admissible (carve-out).
- Carry-forward: P4-C §Q-L4 `S80-MP-ADMISSIBILITY-GENERAL` (full classification) remains open for future session.

Artifacts:
- computations/s82_w2_5_heat_kernel_mp.py
- computations/s82_w2_5_heat_kernel_mp.npz
- computations/s82_w2_5_heat_kernel_mp.png
- sessions/archive/session-82/session-82-results-workingpaper.md §V.E

References:
- Chamseddine-Connes 1996 §2.2-2.3
- Connes-Moscovici 1995 §5
- Widder (1941) Laplace Transform, Ch. IV
- P4-C (sessions/archive/session-79/workshops/p4-c-w2d-fstar-outside-cluster.md) §SG1
