---
name: S83 W2-G12 DRESSING-FACTOR-TAU-FLOW
description: Tau-stationarity test of F_amp, c_sub, f_conv in UNIFIED-AS-79; PASS at 57x below threshold; Branch-B Zubarev consistent
type: project
---

**S83 W2-G12 RESULT** (2026-04-18): PASS -- max_slope=1.751295e-03 vs threshold 0.1 (ratio 0.0175; factor 57 below PASS).

**Why**: UNIFIED-AS-79's epoch-gating validity depends on the three dressing factors F_amp, c_sub, f_conv being tau-stationary at the CMB pivot. A FAIL would mean the "evaluate at horizon-exit" prescription is ambiguous. PASS confirms epoch-rigidity.

**How to apply**:
- Reference as foundational for UNIFIED-AS-79 epoch-gating in S84+ computations.
- The factor-2 A_s agreement with Planck (S80 W1-2 Branch-A PASS-F2) is NOT an artifact of tau-drifting dressing factors.
- Branch-B (Zubarev, W1-G1 PASS carry-forward) consistent: the Jensen potential parameters (S_fold, dS_fold, d2S_fold) are regulator-independent, and the dressing factors at the central-scheme level are Branch-invariant.

**Key physics**:
- F_amp(tau) = F_amp_central * exp(-2 eps_H N(tau))  -- Birrell-Davies slow-roll Bogoliubov saturation
- c_sub(tau) = c_sub_central * [1 + delta_M ln(H(tau)/H_fold)]  -- Mellin-moment running
- f_conv(tau) = (M_KK/M_Pl_red)^2  -- frozen at CONST-FREEZE-42 (machine-epsilon rigid)

**Cross-checks (5/5 PASS)**:
1. f_conv machine-frozen (slope = 0 exactly)
2. F_amp slope = -2 eps_H dN/dtau analytic (0.26% agreement)
3. c_sub slope = delta_M d(lnH)/dtau (0.1% agreement)
4. Plan-grid span (0.1) >> physical trajectory span (~0 from W1-G4)
5. Adiabatic limit F_amp(tau_fold) = F_amp_central

**Files**:
- computations/s83_w2_g12_dressing_tau_flow.py
- computations/s83_w2_g12_dressing_tau_flow.npz
- computations/s83_w2_g12_dressing_tau_flow.png
- sessions/archive/session-83/session-83-results-workingpaper.md §W2-G12

**Caveats**:
- Plan-grid tau_pivot = tau_fold + 0.1 = 0.29 is 1.5e29x larger than the physical slow-roll trajectory span across [N_pivot +- 10]. Test is STRICTER than physical regime.
- The Mellin-running coefficient delta_M = 0.01 used here is an O(alpha_s) estimate; a 10x perturbation would still keep PASS verdict.

**SHA closure**: 551c7a815a510a2f31f4ab0308417ce3fa81c3e558d9d011af846312de9daf21
