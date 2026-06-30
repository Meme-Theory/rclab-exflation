---
name: S76 Z_2 Domain Breaking Result
description: FAIL - domain formation suppresses B1-B3 asymmetry; Josephson network symmetrizes; J_u1 enhancement 14.2x found
type: project
---

## S76-B6-Z2-BREAK: FAIL

Domain formation on 8-cell BCC tessellation does NOT produce Z_2-odd Leggett excitations.

**Why:** The multi-cell Josephson network symmetrizes B1-B3 quasiparticle weight. Delocalization across cells averages out the structural B1(1 mode) vs B3(3 mode) asymmetry. Anomalous sin(dphi) coupling is B1<->B3 symmetric by detailed balance.

**How to apply:**
- Z_2 domain-wall DM production is CLOSED permanently.
- The B1-B3 asymmetry is a SINGLE-CELL structural property, not a multi-cell dynamical effect.
- DM production must come from a different mechanism (not Z_2 breaking at domain walls).

**Numbers:**
- n_Z2(excess) = -3.87 (negative = suppression)
- f_Z2(ensemble) = 0.363 +/- 0.027 (50 samples) -- structural, not Z_2 breaking
- Single-cell baseline f_Z2 = 0.478 > multi-cell 0.363

**BONUS: J_u1 enhancement = 14.2x**
- B2-mediated virtual process: J_{B1,B2} * J_{B2,B3} / Delta_E = 0.530 M_KK
- This is the dominant B1-B3 coupling (not direct J_u1=0.038)
- Exceeds 6.2x threshold for mu_eff rescue
- The B2 adjoint sector acts as a bridge through J_C2=0.933

**Cross-checks:** CHK1-3 all PASS. Leggett tau_DM = 1.3e6 * t_universe.
