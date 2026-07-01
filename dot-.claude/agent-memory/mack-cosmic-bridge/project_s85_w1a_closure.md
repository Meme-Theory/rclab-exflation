---
name: S85 W1a closure (mack-origin reviewer wave, solo-in-session execution)
description: All 10 W1a gates closed in a single session without agent fan-out; verdict distribution, structural findings, and carry-forwards from 2026-04-23
type: project
---

## Context

S85 Wave W1a dispatched to mack-cosmic-bridge as solo reviewer for 10 carry-forward items from S84. Due to a Claude Code infrastructure bug causing parallel-agent dropouts, this wave executed **sequentially in the main session**, one compute per cycle, with live working-paper updates. No Agent tool spawns; all scripts written and run directly via `"phonon-exflation-sim/.venv312/Scripts/python.exe"`.

## Verdict distribution (10 gates)

| Verdict | Count | Gates |
|:--------|:------|:------|
| PASS | 4 | W1a-6 LISA fix-k/f consistency; W1a-7 LISA decisiveness (SNR=1.68e13); W1a-8 LiteBIRD n_T STRUCTURAL-FLOOR; W1a-9 7D Fisher log10(BF)=+828 |
| FAIL | 3 | W1a-1 SCHEME-DEP (0.125 > 0.046); W1a-2 ALPHA-S residual 0.79; W1a-3 d_spec max residual 1.19 (truncation) |
| PENDING-EVENT | 2 | W1a-4 BK-Array 2026; W1a-5 DR3 (window opens today but not public yet) |
| INFO | 1 | W1a-10 rank-universality monitor (4/4 alt groups PENDING) |

## Structural findings

- **F1 (scheme-dependence is permanent)**: W1a-1 established Path (b) — 2-loop Z_R expansion is convergent (2L/1L ratio 0.080) but sign-aligns with 1-loop. Variance GROWS from 4.65% → 12.5% under higher orders. Every downstream prediction that consumes f_conv must be tagged (value, scheme). This is now a solution-space wall.

- **F2 (α_s = n_s² − 1 is scheme-specific)**: W1a-2 FAIL. Topological vs spectral-second-moment partitions disagree by 79% of α_s_obs; neither matches PDG. S50–51 identity holds as topological-scheme prediction ONLY; registry row stays single-scheme.

- **F3 (d_spec = 12 is topologically exact, numerically hard at L=10)**: W1a-3. Route (iii) topological = 8+4 = 12 EXACT. Routes (i) Weyl-law and (ii) zeta extract 10.81 and 11.37 respectively at L_max=10; residuals are finite-size, shrink as L → ∞.

- **F4 (LISA is DECISIVE, not just consistent)**: W1a-6 PASS at residual 3.3e-4 (fix-k/f dual pre-reg consistent). W1a-7 PASS at SNR = 1.68e13 under 3σ error-budget tightening. LISA graduates from channel to flagship discriminator.

- **F5 (LiteBIRD EVOI=0 on n_T is GEOMETRIC)**: W1a-8 PASS at normalized=588.78 (S84 [540, 654] reproduced within 7%). The 54-decade k-space separation between transit (+0.468) and CMB (−3e-3) n_T is structural, not detector contingent.

- **F6 (7D Fisher reproduces S84 subset; pre-reg flagships dominate)**: W1a-9 PASS at log10(BF)=+828. χ² excl (r, β_s) = 14.86 ≈ S84 W4-49 13.9 target (7% match, within 20% tolerance). β_s + r carry 3798 of 3813 total χ² — pre-registered discriminators by 2030.

## Exit-code convention (ratified mid-session)

User confirmed that FAIL is a physics result, not a script error. All 10 scripts return exit 0 on any clean run (PASS, INFO, FAIL). Exit != 0 reserved for genuine script breakage (Python traceback, import failure). W1a-1 and W1a-2 were re-run after exit-code fix to regenerate canonical SHAs. Rule subsequently landed in `.claude/rules/math-scripts.md` §"Exit Codes and Verdict Semantics".

## Convention translation (mack-bridge native work)

| W1a gate | Framework quantity | Observational quantity | Detector |
|:---------|:-------------------|:-----------------------|:---------|
| W1a-4 | r_CMB_framework = 0.01173 (S83 G46) | r tensor-to-scalar | BICEP Array + Keck 2026 |
| W1a-5 | w_0_FW = −0.918 (S58 Volovik + effacement) | CPL w_0 | DESI DR3 (opens 2026-04-23) |
| W1a-6/7 | ρ_AC(fix-k)=2.10, ρ_AC(fix-f)=2.38 | Ω_GW at f_pivot=3 mHz | LISA (2034+) |
| W1a-8 | n_T_transit=+0.468 vs n_T_CMB=−3e-3 (54-decade separation) | tensor spectral index | LiteBIRD (2030+) |
| W1a-9 | 7D (w_0, w_a, n_T, r, β_s, α_s, f_NL) | joint multi-channel | DESI+LiteBIRD+CMB-S4+SKA-1 |

**Important caveat documented in W1a-9**: the 7D Fisher uses n_T_CMB, NOT n_T_transit. Plan's verbatim vector listed n_T=0.468 which would produce a spurious 586σ Fisher artefact because LiteBIRD cannot probe the transit k-scale (consistent with W1a-8 STRUCTURAL-FLOOR). I used the detector-matched prediction n_T_CMB=−3e-3; this deviation from plan step 7 is documented in the WP §W1a-9 and in the script docstring.

## Carry-forward

1. Re-run W1a-3 at L_max=30 (needs GPU eigvals, 8 h)
2. Register "all framework predictions are (value, scheme) tuples" in atlas-04
3. DR3 re-fire on 2026-05 data release
4. BK-Array re-fire on 2026 data release
5. Land LISA flagship pre-registration (W1a-6 + W1a-7 combined) in atlas-XX
6. Land LiteBIRD n_T STRUCTURAL-FLOOR row in atlas-04
7. tesla W13 carry-forward: R_N(G_2), R_N(F_4), R_N(A_3), R_N(C_3) at L_max=10
8. kaku W10 cascade scripts for DR3 FAIL response (S85-R_842-PHYSICAL-ANCHOR-REAUDIT, S85-W0-L-INVERTED-BRANCH-ENUMERATION)

## Lessons learned (meta)

- **Solo-in-session execution is viable** for 10 gates of modest compute complexity (all finished in ~0.1–0.3 s CPU each). Total wall time for the 10 scripts was under 2 seconds of Python runtime; most time went into thinking, script-writing, and WP updates. Good fit when agent infrastructure is unstable.

- **Exit code convention ratification** happened mid-session because user corrected the FAIL-exits-2 pattern. Rule is now in force project-wide. Saves future ambiguity between script breakage and physics FAIL.

- **Show-one-before-fan-out** enforced via hook was genuinely useful: the W1a-1 run confirmed template (dual-SHA, verdict append format, NPZ schema) before I fanned the remaining 9 scripts from the same pattern. Saved from propagating any template error.

- **Live working-paper updates** per user request — updating §W1a-N as each gate closes avoids the "20-gate synthesis dump at end" anti-pattern. User interrupted at W1a-8 to remind me; thereafter I updated per-gate consistently.

- **The n_T convention trap in W1a-9** is a real interpretive caveat: plan verbatim vectors sometimes list the transit-scale value for an observable the detector cannot probe. Agent must choose the DETECTOR-MATCHED scale, not the literal plan vector. Documented inline.
