# S118 W1-1 — Substrate-first c_s closes the A_s magnitude fork (Q23)

**Gate**: CF-S118-AS-CS-SUBSTRATE-FIRST | **PASS** (sign=PASS/mag=PASS/regime=MARGINAL) | audit `172c85bea1e5ed06…`
**Script**: `computations/session-118/s118_as_cs_substrate_first.py`

## Result
Substrate-first a₂^{ζ}-channel hydrodynamic-IR sound speed **c_s = 0.5685** (primary; robust band 0.568–0.608 across estimators) lands IN the GS-1 window [0.5163972, 0.6501056]. Magnitude |2·Δ_scale − fork_OOM| = 0.0165 ≤ 0.10. Bracketed c_BLV=0.485 ≤ c_s ≤ c_Gold=0.915. ⇒ deg=+2 substrate→pivot transport is the **SOLE carrier** of the 0.668-OOM fork ⇒ A_s resolves to the **acoustic-horizon (H̃, +0.196) grid, A_s=3.2994e-9**; Q23 closes **zero-parameter**. dual_prior → 0.9 Track A. Box-δ (+0.864) grid demoted to regime-diagnostic. No FAIL-branch (CF-S118-AS-PREFACTOR-SOURCE NOT triggered).

## Method (the precise G_ij/G_ττ decomposition — reusable)
**c_s² = K_grad/K_inertia = group velocity² = IR dispersion slope dλ²/dC₂.** Substrate phonon dispersion: ω²=λ² (Dirac energy², from s84 L12 cache τ_fold=0.19), k²=C₂(p,q) (SU(3) Casimir = fiber-Laplacian momentum², `C₂=(p²+q²+pq+3p+3q)/3`). Weighted-LSQ slope of λ² on C₂ over IR window C₂∈[C₂_min, C₂_min·e]=[1.333,3.624], intercept=gap (condensate rest-energy, separated):
- K_grad = Cov_w(λ²,C₂)=288.31 (gradient-stiffness cross-moment; >0 PSD); K_inertia = Var_w(C₂)=891.98 (Casimir 2nd moment).
- weight w = a₂^{ζ} density (dim·|λ|⁻²) × GGE occupation.

## Three load-bearing lessons (carry forward)
1. **CAUSALITY ORIENTS THE RATIO.** The literal ⟨C₂⟩/⟨λ²⟩ = 2.788 (c_s=1.670) is ACAUSAL — bare Casimir over-runs Jensen-deformed λ² at high (p,q) ((12,0): C₂=60 vs λ²∈[13.5,29.4]). The c_s≤1 wall FORCES the inverse (group-velocity) orientation c_s²=dλ²/dC₂. ALWAYS compute c_s as the dispersion SLOPE (energy²/momentum²), never the bare Casimir/energy ratio.
2. **GGE occupation = SATURATED Parker, NOT thermal BE.** P_exc_kz=1.000, band-uniform (all L12 modes λ·dt_transit≤6e-3 ≪1, deep sudden). The GGE never thermalizes (R_therm=5252) so cold Bose-Einstein at T_acoustic is the WRONG regime (it gives a degenerate below-window 0.383). Use saturated/uniform n_k.
3. **Machinery validation anchor:** the acoustic-MINIMUM branch of λ²(C₂) reproduces **c_BLV=0.48510** (reldev 0.02% vs canonical 0.485 = S64 second-sound floor = GS-1 lower bracket) — it falls out independently, confirming the a₂-trace channel sits mid-bracket at the MEAN (not min) energy. The uniform-weighted slope is EXACTLY window-independent (0.59085 across all 90 sectors) = clean linear-acoustic signature.

## Regime caveat
a₄K⁴/a₂K² = 0.102 at IR window edge ⇒ MARGINAL under my conservative 5%/50% band (NOT changed post-hoc), but ≪ the plan's explicit breakdown criterion (a₄K⁴ ≳ a₂K²); the IR extraction (C₂→0) is well within validity. Composite PASS robust.

## Cross-refs
Resolves the [[s117_w1_as_fork_resolution]] 2-member 0.668-OOM fork (ξ_KZ +0.864 vs H̃ +0.196). Feeds [[s114-as-functional-selection]] (A_s magnitude pluralism — this PASS collapses the dominant fork to the H̃/ζ leaf). c_s heat-kernel via FULL physical spectral_action.py (CLASS=FULL, NOT SCHEMATIC). Inputs SHA-pinned: canonical d884a2b5, s84 L12 9e6d9cf7, gs1 dbecfedd, spectral_action 2ca6d921.
