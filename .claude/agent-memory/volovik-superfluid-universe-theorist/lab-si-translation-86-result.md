---
name: lab-si-translation-86-result
description: S86 W11-1 S86-LAB-SI-TRANSLATION INFO verdict; 9-row M_KK -> SI lab-falsifier table (3He-A / FeSe / 173Yb)
type: project
---

S86 W11-1 S86-LAB-SI-TRANSLATION INFO. 9-row table populated; 6 rows provisional (sigma_detect upper-bound, not single-shot).

**Why**: W8-4 (S85) gave 9 dimensionless M_KK-normalized substrate ratios across 3 SU(3)-unique directions (lambda_6, _7, _8) x 3 platforms (3He-A, FeSe, 173Yb). C5 multiplies by per-platform SI prefactor and pins sigma_detect to literature SHA-anchors, opening the 9-entry LAB-FALSIFIER corridor (W14-W6 NEW row class) and feeding C6 EVOI tree.

**How to apply**:
- 9-row CSV at `sessions/archive/session-86/computation-artifacts/s86_w11_lab_si_translation.csv`; pull rows directly downstream — do NOT recompute SI translation.
- Detection_ratio range: SW1/XA1/XB1 (3He-A) at 5.9e4 / 5.9e4 / 1.97e4; SW3/XA3/XB3 (173Yb) at 28.5/55/132; SW2/XA2/XB2 (FeSe) at 73/31/73. All above platform sigma_detect.
- Per-platform sigma_detect: 3He-A 1 kHz (Eltsov 1005.0546, ROTA NMR linewidth, upper-bound); FeSe 5 ppm (Zhou 2010.01020, 77Se NMR single-shot); 173Yb 0.05/s (Cazalilla 0905.4948, theoretical 3-body rate floor at n=1e14 cm^-3, upper-bound).
- Per-platform SI prefactor: 3He-A nu_Delta_3HeA = 34.146 MHz (T_c=0.929 mK Greywall, Delta = 1.764 k_B T_c, /h); FeSe K_baseline = 200 ppm (Zhou normal-state); 173Yb Gamma_3B_inherited = 0.5 /s (K_3=5e-29 cm^6/s, n=1e14 cm^-3).
- Provisional flag (6 rows: 3He-A and 173Yb) signals S87+ refinement target — replace upper-bound sigma_detect with explicit single-shot 3-sigma floor.
- audit_sha256 = 6a2d523920c34032..., content_sha256 = 5d2449353ebdae40...
- W8-4 magnitudes (NPZ inputs) FROZEN: obs_3HeA = [1.7267, 0.5756, 0.0709] for lambda_6/7/8; obs_FeSe = [0.7674, 1.8226, 0.3544]; obs_Yb = [5.494, 13.185, 2.85].

**Microscopic-to-emergent mapping established**:
M_KK (substrate compactification scale, 7.43e16 GeV) -> Delta_BCS (substrate gap ratio 0.464 in M_KK units) -> per-platform Delta (3He-A weak-coupling BCS at 0 bar; FeSe Knight-shift baseline; 173Yb 3-body rate). The dimensionless W8-4 ratios are M_KK-INVARIANT (numerator and denominator both M_KK-normalized in W8-4); only the platform-native prefactor sets the SI scale. This mirrors the Volovik program's "substrate measured at different compactification ratios" (3He-A is a controlled realization of the substrate's SU(3) restriction to SU(2)-triplet; not an analog).
