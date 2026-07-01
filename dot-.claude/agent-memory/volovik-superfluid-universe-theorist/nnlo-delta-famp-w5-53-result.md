---
name: W5-53 NNLO->N3LO 1/N scan F_amp convergence at K=2.035
description: S84 W5-53 INFO verdict. F_amp(N3LO)=1.0165 at K=2.035, SU(3). Series Borel-convergent (R_Borel=0.285<1) but plateaus 3.16x above target 0.4454. Dynamics-WALL refined: convergent-but-short, not divergent-saturating.
type: project
---

# S84 W5-53 GATE-NNLO-DELTA-FAMP — INFO

**Fact**: The Berges 3PI 1/N expansion at K=2.035 converges in order (r_2 = 0.285 < 1 Borel radius, sat_ratio=0.285 << 0.75 FAIL threshold), but the convergent limit F_amp ≈ 1.0165 at SU(3) is **3.16× short** of the F_amp_target = 0.4454 needed for dynamics-layer rescue. Cumulative suppression at N3LO = 20.65%; required = 65.23%.

**Why:** The plan's PASS/FAIL thresholds were binary: PASS = (F_N3LO ≤ 0.4454 AND monotonic-convergence ratio ≥ 10); FAIL = (F_N3LO ≥ 0.4454 AND series divergent-saturating with sat_ratio ≥ 0.75). Neither is met. Verdict = INFO, with structural content that tracks the "W5-53 FAIL" policy branch: dynamics-layer (1/N) rescue through K=2.035 is inaccessible at any order. Promotes a refined dynamics-WALL-at-2.035 theorem candidate: failure mode is "convergent-but-short" rather than "divergently-saturating".

**How to apply:**
- Next-session plans for K=2.035 branch A_s closure must route through regulator-layer (H_tilde, baseline-layer) or cross-corridor K-values. Higher-order 1/N is not a viable rescue direction.
- Forward to W5-54 (regulator-invariance of K_R5 floor) and the W6 baseline-layer tightening gate.
- The INFO verdict is orthogonal to plan threshold enumeration — document if revising plan templates to include "convergent-but-target-unreachable" as an explicit INFO sub-type.

**Key numbers**:
- R_req = F_amp_bare / F_amp_target = 1.281 / 0.4454 = 2.876066 (plan-stated 2.876, verified).
- a_1 = 0.6192 (pinned to S82 W1-2 F_amp_canonical=1.0166)
- a_2 = 9.298e-4 (pinned to S83 G11 Δ_NNLO=1.32e-4)
- a_3 = 2.653e-4 (Berges Borel-summable via Jensen barrier S_0=4.34)
- F_amp(LO)=1.281 → F_amp(NLO)=1.0166 → F_amp(NNLO)=1.01650 → F_amp(N3LO)=1.01649
- rel_delta_ratio = 0.9049 (< 10, PASS fails)
- sat_ratio = 0.2853 (< 0.75, FAIL fails)
- Borel R = 0.2853 < 1 (series convergent)
- GPU cross-check: torch.linalg.eigvalsh on 480×480 kernel, eigvals ∈ [+0.828, +7.739], all positive.

**Files**:
- Script: `computations/s84_w5_nnlo_delta_famp.py`
- Data: `computations/s84_w5_53_data.npz`
- Plot: `computations/s84_w5_53_plot.png`
- Verdict: `W5-53: INFO -- value=1.016485 scheme=Zubarev convention=K=2.035 L_max=5 sha256=c849a0908ade1f5dbec935fa85a236e4b689913a15c59ff280a85e4229034022`
- Working paper: `sessions/archive/session-84/session-84-w5-workingpaper.md` §W5-53
