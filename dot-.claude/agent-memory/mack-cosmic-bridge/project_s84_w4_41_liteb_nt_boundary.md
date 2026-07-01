---
name: S84 W4-41 LiteBIRD n_T inaccessibility closure
description: 2026-04-19 bookkeeping gate that set EVOI=0 on LiteBIRD n_T-tilt discrimination for 2030-2040; 54-decade k-separation between transit and CMB is structural reason; registered as OBSERVATIONAL-BOUNDARY-LITEB-NT
type: project
---

## S84 W4-41 — S84-BLUE-TRANSIT-TILT-INACCESSIBILITY

**Date**: 2026-04-19. **Agent**: mack-cosmic-bridge. **Verdict**: PASS.

### Core claim (permanent)
LiteBIRD (3-yr σ_nT = 0.0540 from G43) and LB+CMB-S4 joint (σ_nT = 0.0654 realized from #37; 0.040 was plan fiducial) STRUCTURALLY cannot discriminate the framework from slow-roll on n_T at CMB scales within 2030-2040.

### Numerical anchors
- `n_T(transit)` = +0.4676036871525688 (S65 = G50 = S68, max disagreement < 1e-10)
- `n_T(k_CMB)` = -3.0235881896944388e-3 (S68 = #39, deviation exactly 0)
- `delta_nT_FW_SR` = 0.0 exactly (S68 analytic saturation of slow-roll consistency)
- `decades_separation` = 54.04394284969212 (k_transit = 5.53e52 Mpc^-1 vs k_CMB = 0.05 Mpc^-1)
- Discrimination ratios (using Δ_floor = 1e-4):
  - R_LB_3yr = 1.852e-3 → 540.1x below 1-σ
  - R_joint_plan = 2.500e-3 → 400.0x below 1-σ
  - R_joint_realized = 1.530e-3 → 653.8x below 1-σ (WORSE than plan)

### Why: substrate framing
The +0.4676 BLUE tilt is the substrate prediction AT the transit scale (f_transit = 8.55e37 Hz, 34 decades above LIGO). Bogoliubov squeezing (|β|² ≈ 1.015) operates only at k > k_transit. At k_CMB (54 decades below transit), modes exit the horizon before the transit and never experience the squeezing. They see only quasi-de Sitter background, which reverts to slow-roll consistency n_T = -2ε_H via G46 tensor transfer. NOT a failure — a geometric property.

### EVOI closure
- Before: 4.50% (inherited from S78-W3-C TENSOR-FAMP proxy at discrimination-channel level)
- After: 0 for LiteBIRD n_T sub-channel in 2030-2040 window
- Rank-27 S83 priority-table row (S78-W3-C) annotated; residual EVOI reflects BICEP/Keck 2026 r-channel + non-LiteBIRD only

### Next weighted channels (named in EVOI payload)
1. 21-cm ISW cross-power (S71 21CM-ISW, SNR=4.16 ideal)
2. CMB-S4 f_NL bispectrum (S77 Mack-QA: 21-cm sole novel GGE channel)
3. Euclid ISW tracking (S68 ISW-TRACKING, 2.5-σ)
4. CMB-S4 running α_s (S84 ALPHA-S-PRE-REGISTRATION, 2.94-σ)

### Artifacts
- Script: `computations/s84_w4_blue_transit_tilt_inaccessibility.py`
- JSON: `computations/s84_w4_blue_transit_tilt_inaccessibility.json`
- NPZ: `computations/s84_w4_blue_transit_tilt_inaccessibility.npz`
- Registry entry: `sessions/permanent-results-registry.md` (tag OBSERVATIONAL-BOUNDARY-LITEB-NT)
- EVOI closure: `sessions/evoi-framework.md` (Items CLOSED + rank-27 annotation)
- Working paper: `sessions/archive/session-84/session-84-w4-workingpaper.md` §W4-41 (120 lines)

### SHA pins (dual-SHA S84+ schema)
- content_sha256 = `11370802f478ba4c9ccc12194c5e004a7692e9131af89db6328ce0711eb65a37`
- audit_sha256 = `9f6df37364b5de799eb9ddecd62ac36ff00fd6ba8d293721f108894d1815f3d6`

### Reopening condition
EITHER (a) instrument with σ(n_T) ≲ 2e-4 (two orders below foreseeable CMB-S4),
OR (b) framework-internal mechanism that pushes Δ(n_T)_CMB above the 1e-4 floor.
