---
name: S70 ANNIHILATION-TIME-70 Results
description: Bucher Test 4 — pair annihilation timescale on CG(24), t_ann = 9.68e-42 s, INFO gate
type: project
---

## S70 ANNIHILATION-TIME-70: Pair Annihilation Timescale

Gate: **INFO**. t_ann = 9.68e-42 s in absolute range [1e-43, 1e-40]. Ratio t_ann/t_BA = 0.031 outside [0.1, 10].

**Why:** Bucher Test 4 — compute the timescale at which singularity-antisingularity pairs would annihilate on CG(24) if integrability were broken, and compare with BA lifetime from S67.

**How to apply:** The absolute timescale confirms the prompt's prediction (t_ann ~ 10^{-42} s). The ratio failure is physical: kinematic approach (c_Gold) and collective oscillation (Delta_B3) are structurally different scales with a factor-30 hierarchy. The comparison with S67 BA lifetimes [3.8e-42, 3.3e-41] s gives ratios in [0.3, 2.6] — same order of magnitude.

### Key Numbers
- t_ann = hbar / (c_Gold * M_KK) = 9.68e-42 s (log10 = -41.01)
- t_BA = 2*pi*hbar / (Delta_B3 * M_KK) = 3.16e-40 s (log10 = -39.50)
- t_relax = t_ann / gamma_RP^2 = 6.11e-39 s (log10 = -38.21)
- t_ann / tau_BA_min(S67) = 2.56, t_ann / tau_BA_max(S67) = 0.29
- t_ann / t_Planck = 180 (safely above Planck scale)

### Timescale Hierarchy (log10 seconds)
-44.00 t_transit | -43.27 t_Planck | -41.42 tau_BA_min | -41.01 t_ann
-40.48 tau_BA_max | -39.50 t_BA_osc | -39.39 t_Leggett | -38.83 tau_Leggett | -38.21 t_relax

### Bucher Connection
GGE pair density frozen by Richardson-Gaudin integrability. BA modes overdamped (Q<2), Leggett underdamped (Q=18.6). Pair population is a SNAPSHOT, not steady-state.

### Files
- `computations/s70_annihilation_time.{py,npz}`
