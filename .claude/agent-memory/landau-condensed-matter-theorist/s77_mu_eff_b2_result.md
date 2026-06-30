---
name: S77 mu_eff B2-mediated result
description: S77-A3-MU-EFF-B2 FAIL. mu_eff=8.58e-4 (1.08 decades below 0.0102). B2 mediation gives 3.2x not 202x because bottleneck migrates to B2-B3.
type: project
---

S77-A3-MU-EFF-B2: mu_eff = 8.576e-4. Gate: FAIL (< 0.001 threshold).

**Why:** B2 mediation through J_u1(eff) = 0.530 (from S76 WS4) enhances the B1-B3 rate by (0.530/0.038)^2 = 195x, but the slow eigenvalue of the 3x3 L-K matrix only improves by 3.2x. The slow eigenvector at J(B1-B3) = 0.530 is B2-dominated (B2: -0.50, B1: +0.21, B3: +0.29) — the bottleneck has migrated from B1-B3 (J_u1 = 0.038) to B2-B3 (J_su2 = 0.059). Reaching target requires J(B1-B3) = 1.90 (49.9x bare), unphysical from single-channel enhancement.

**How to apply:** The isocurvature decay rate mu_eff = 0.0102 for n_s = 0.9649 cannot be derived from the B1-B3 channel alone. Three remaining routes: (1) multi-cell fabric coherence boosting ALL inter-branch rates, (2) time-dependent BCS dynamics (gap formation vs transit timing), (3) full fabric L-K matrix (32-cell tessellation with Josephson network). Route 2 is addressed by W2-H (BCS-TIMING).

Key facts:
- Bare mu_eff = 2.672e-4 (reproduces S76 W1-A exactly)
- B2-mediated mu_eff = 8.576e-4 (3.21x enhancement)
- Deficit reduced from 1.58 to 1.08 decades
- Feshbach of Josephson Hamiltonian gives J_eff = 0.018 (0.48x bare) — the bonding B2 eigenstate at E=3.64 PULLS coupling down
- 5 cross-checks: ALL PASS
