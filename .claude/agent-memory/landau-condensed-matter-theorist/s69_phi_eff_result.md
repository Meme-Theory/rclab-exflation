---
name: S69 PHI-EFF-BCS-BOGOL-69 Result
description: BCS squeeze phase phi_eff = 0.558*pi, enhancement 1.105, gate INFO. Structural result from BCS mixing angles.
type: project
---

Gate PHI-EFF-69: **INFO**. Enhancement = 1.105 in [1.0, 1.3].

phi_eff = 1.753 rad = 0.558*pi. cos(phi_eff) = -0.181. At r_eff = 0.338.

**Why:** Squeeze phase is STRUCTURAL, not dynamical. Determined by BCS anomalous phase 2*theta_BCS:
- B2 at Fermi surface: theta_BCS = pi/2, phi = 3pi/2, cos = 0 (no interference)
- B3 above Fermi: theta_BCS = 1.29, phi = 4.15, cos = -0.53 (partially destructive)
- B1 below Fermi: theta_BCS = 1.63, phi = 4.82, cos = +0.11 (weakly constructive)
- Net: optical sector (50.6% weight, B3 modes) tips cos(phi_eff) negative

Dynamical phase from transit integral negligible (< 0.016 rad) because supersonic.
Profile-independent, transit-duration-independent, weighting-scheme-independent.

r_eff needed for PASS (enh >= 1.3): 0.483 (43% above current 0.338).

**How to apply:** The A_s gap correction from non-BD squeeze is +0.043 OOM, modest.
Remaining gap: 0.759 - 0.043 = 0.716 OOM. Need additional channels or larger r_eff.
QA prediction (phi=0) EXCLUDED. Josephson analogy (pi/4) EXCLUDED.
KZ Z_3 prediction (cos=-0.5) close but not exact (-0.181 vs -0.5).
Files: `computations/s69_phi_eff.{py,npz,png}`
