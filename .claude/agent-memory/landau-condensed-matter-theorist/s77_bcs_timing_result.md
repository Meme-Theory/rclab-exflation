---
name: S77 BCS Timing Sequence
description: PASS — t_BCS/dt_transit in [102, 160], gap absent during Bogoliubov squeeze, validates GGE construction
type: project
---

## S77-B8-BCS-TIMING: PASS

**Gate**: t_BCS/dt_transit > 100 => PASS

**Three independent arguments**:
1. N_osc = dt_transit / T_BCS_osc = 8.4e-5 << 1. BCS interaction cannot complete one oscillation during transit.
2. tau_relax = 0.068 M_KK^{-1} = 60.1 * dt_transit. First e-fold of gap growth takes 60x transit.
3. t_BCS(90%) in [0.115, 0.255] M_KK^{-1} = [102, 226] * dt_transit depending on seed.

**Seed models**:
- A (random walk): Delta_seed = Delta_eq/sqrt(8) = 0.164, t_BCS = 102 * dt_transit
- B (single-mode quantum): Delta_seed = 1/sqrt(rho_F*N_BCS) = 0.067, t_BCS = 160 * dt_transit
- C (GGE thermal): Delta_seed = sqrt(T_GGE/(rho_F*N)) = 0.022, t_BCS = 226 * dt_transit

**Counterfactual**: Even if gap present during transit, LZ gives P_diabatic = 0.9996, suppression = 0.04%.

**Timescale hierarchy**: dt_transit (1.1e-3) << 1/H_fold (1.7e-3) << tau_relax (0.068) << t_BCS (0.12-0.26) << 1/Delta (2.15) << T_BCS_osc (13.5)

**Why:** Confirms self-consistency of the Bogoliubov squeeze calculation (n_Bog = 0.999 from ungapped modes).
**How to apply:** The post-transit GGE is validated — gap forms AFTER squeezing, not during. All downstream results (n_s, A_s, DM) that depend on n_Bog are on solid ground.

**Files**: `computations/s77_bcs_timing_sequence.py`, `computations/s77_bcs_timing_sequence.npz`
