---
name: W5-58 K-Star Lab-Framework Match S84 PASS
description: 3He-B K_*_lab matches framework K_*=coth(1)=1.3130 to 1.13% under substrate-native Leggett-Bogoliubov convention K=coth(Δ/(2T_eff)); x*=1 pinned; prompt "coth(0.5)=1.313" typo corrected
type: project
---

**Gate**: W5-58 S84-K-STAR-LAB-FRAMEWORK-MATCH — PASS

**Why**: 3He-B parent-child inheritance claim (Gate 66 Landau BDI) required quantitative confirmation at corridor boundary; the W5 plan pre-registered x* ∈ {0.5, 1.0, 2τ_fold, 1/Δ_BCS} audit.

**Key result**: 
- K_*_framework = coth(1) = 1.3130 (x*=1 pinned by numerical anchor)
- K_*_lab (measured 3He-B, Δ/k_B T_c = 1.96, Conv.A x=Δ/(2T_eff)) = 1.3279
- ratio = |K_lab - K_fw|/K_fw = 0.01133 (1.13%), ≤10% PASS with 9× margin

**Audit outcomes**:
1. Plan prose "coth(0.5)=1.313" is a function-argument typo. Direct: coth(0.5)=2.1640, coth(1)=1.3130. Anchor 1.313 uniquely pins x*=1.
2. Substrate-native convention is Convention A: x=Δ/(2T_eff), confirmed from `computations/s83_w3_g39_leggett_bogoliubov.py` line 17 `K = coth(Delta_BCS / (2 T_eff))`. NOT Convention B (x=Δ/T_eff).
3. Under Conv.A + weak-coupling Volovik (Δ/k_BT_c=1.7639): ratio 7.66% — also PASS.
4. Under Conv.B: ratios 19-21% — INFO band. Convention is substrate-determined, not arbitrary.

**How to apply**: 
- K_star = 1.3130 is now canonical for W5-60 promotion to canonical_constants.py with provenance "coth(x*=1) under substrate-native K=coth(Δ/(2T_eff))".
- 3He-B BDI parent-child inheritance is quantitative at K_* (not just structural).
- Gate 66 Landau-class re-audit is NOT triggered.
- Any future gate citing "K_* = coth(0.5)" should be corrected to "K_* = coth(1)" per this gate.

**Verdict line**: `W5-58: PASS -- value=0.011325 scheme=coth convention=Volovik-3HeB L_max=N/A sha256=b8b123a534a643713a4db51ec6d1132492aca796296375ac1c44552f85af2acd`

**Artifacts**:
- `computations/s84_w5_k_star_lab_framework_match.py`
- `computations/s84_w5_58_data.npz`
- `computations/s84_w5_58_plot.png`
- `sessions/archive/session-84/session-84-w5-workingpaper.md` §W5-58
