# Session 85 Plan — Wave W7: transit-origin reviewer wave

**Generated**: 2026-04-21
**Wave owner**: transit-dynamics-theorist
**Item count**: 7
**Script prefix**: `s85_w7_`
**Verdict file (canonical)**: `computations/s85_gate_verdicts.txt`
**Theme**: transit-origin — fold-transit Bogoliubov dynamics, GGE relic formation, Parker pair production, impedance mismatch CC-Γ, acoustic white hole causal disconnect, supersonic flow, τ_fold first-order transit.

**Substrate framing (global, per `.claude/rules/phononic-framing.md`)**: the fold-transit IS the substrate's first-order phase transition. Mach = 13.75 is intra-substrate Jensen-parameter dynamics, NOT superluminal propagation through g_M. c bounds on-substrate propagation; it does not bound the substrate's own eigenvalue-reorganization rate. Every gate in this wave works in the substrate-fundamental direction: D_K eigenvalues → spectral action moments → emergent observable. If a derivation flows the other direction (GR → substrate), the gate is malformed.

---

## Wave W7 Summary

| Item | Gate ID | Trigger | Theme | Effort |
|:-----|:--------|:--------|:------|:-------|
| 1 | S85-W7-BASELINE-HTILDE-DERIVATION | [VERIFY] | cc-3-connes-moscovici (H̃ divergence chase) | ~4 h GPU |
| 2 | S85-W7-CC-6 | [VERIFY] | cc-6-parker (transit-residue vacuum-energy shift) | ~6 h GPU |
| 3 | S85-W7-CC-GAMMA | [VERIFY] | cc-gamma-impedance (DM/DE ratio reconciliation) | ~3 h CPU |
| 4 | S85-W7-CUSP-BOGOLIUBOV | [VERIFY] | van-hove-cusp (β_k at square-root cusp) | ~5 h GPU |
| 5 | S85-W7-DRESSED-VP | [SIGN] | spectral-triple (matter-dressed spectral action) | ~3 h GPU |
| 6 | S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY | [AUDIT] | k-corridor-scan (z″/z vs k² across K-corridor) | ~4 h GPU |
| 7 | S85-W7-W0-RE-AUDIT-AT-L8 | [AUDIT] | w0-branch-audit (post-branch-iv-retraction) | ~3 h CPU |

Wave W7 is transit-origin mode-equation territory. Five items are direct Bogoliubov-calculus gates (BASELINE-HTILDE, CC-6, CUSP, DRESSED-VP, K-CORRIDOR); two are audit/reconciliation gates (CC-Γ, W0-RE-AUDIT). All items inherit the substrate-framing directive and the `canonical_constants.py` imports required by `.claude/rules/math-scripts.md`.

---

## Wave W7 Decision Point Prerequisites

- **W0 CC-6 Parker-residue gate (item #3 in W0 table `CC-5`, and CC-1/2/3/4 cluster) feeds here**: if W0 closes CC-1 through CC-5, the cross-cluster closure constrains the CC-6 (Parker transit-residue) substitution chain. W0-CC-5 asymptotic refit (L_max ≥ 11) is a direct input to W7-CC-6. The wave executes CC-6 conditionally: if W0 CC-5 fails at L_max ≥ 11, W7-CC-6 emits INFO with carry-forward rather than PASS/FAIL.
- **W0 VAN-HOVE-CUSP-THEOREM (conv=4, item #6 in W0)** reformulates τ_fold per W8a-85 audit consensus. W7-CUSP-BOGOLIUBOV presumes the square-root-cusp form ω²(t) ~ A|t−t_c|. If the W0 reformulation lands on a different cusp exponent α, the W7-CUSP script must re-dispatch with the new exponent; gate becomes INFO pending W0 closure.
- **W0 ZUBAREV-L_max-CONVERGENCE-TO-MINUS-ONE (analytic corollary)**: the Zubarev scheme is canonical per S83 W1-G1. W7-BASELINE-HTILDE uses Zubarev; if W0 re-classifies Zubarev as non-canonical at L_max ≥ 11, BASELINE-HTILDE re-runs with the replacement scheme.
- **No upstream blocker inside W7**: items are independent at the mode-equation level. All 7 can dispatch in parallel.

---

## §W7-1. S85-W7-BASELINE-HTILDE-DERIVATION

**1. Gate ID**: `S85-W7-BASELINE-HTILDE-DERIVATION`

**2. Trigger**: `[VERIFY]` (close the TD-vs-LI H̃ divergence chase opened by S84-W1a-1 and carried in S83 Dynamics-Dressing Workshop Final §S84-BASELINE-HTILDE-SENSITIVITY rate-limiter)

**3. Classification**: PHONONIC (H̃ is the Jensen-parameter rate of the substrate's internal compactification; its DC value is the acoustic envelope of the GGE relic)

**4. Agent type**: transit-dynamics-theorist (sole — mode-equation specialty; SIGN-chain required)

**5. Hypothesis**: The H̃ divergence between transit-dynamics (TD-anchor, 1.57× above band centre; Δ_OOM = +0.196) and lizzi-integral (LI-anchor, ~181× above band centre, log₁₀ = +2.06) reconciles to a single physical H̃_DC = H̃_Friedmann/F_stretch inside the pre-registered DC window [4.599e-3, 4.829e-3] once the substrate-emergent Friedmann H is distinguished from the Jensen-parameter transit rate H_transit per S76 Transit-Einstein Workshop R1 "z″/z requires H_Friedmann" result. The pre-registered gate is whether the reconciliation lives inside the 0.91% log-DC window at L_max = 10 under Zubarev (W1-G1 Branch-B canonical).

**6. Method**:
- Script: `computations/s85_w7_baseline_htilde.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (M_KK, tau_fold, dt_transit, H_Friedmann, H_transit, dS_fold, d2S_fold, Vol_SU3, planck_ns); any H̃-specific constant (H_tilde_lo, H_tilde_hi, H_tilde_center, H_tilde_canonical) that is not yet canonical must be added to `canonical_constants.py` WITH provenance (S84 W1a-1 verdict line + SHA) BEFORE import.
- Python: `phonon-exflation-sim/.venv312/Scripts/python.exe`
- GPU path: AMD RX 9070 XT / ROCm 7.2; `torch 2.9.1+rocm`; eigen-decomposition of the Mukhanov pump-operator matrix (z″/z as operator on L_max = 10 KK-tower × SU(3) fiber basis, size ≈ 1.56e5 × 1.56e5 — use block-diagonal decomposition by KK-level to fit in 17.1 GB VRAM; per-block size ≤ 1.42e4, well within `torch.linalg.eigh` limits)
- CPU fallback: `os.environ.setdefault('OMP_NUM_THREADS','8')` before `import numpy`
- SHA-256 pins (mandatory S81+):
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `computations/s83_w1_g1_verdict.txt` (Zubarev canonical pin) → `<precomputed>`
  - `computations/s84_w1a_1_htilde_sensitivity_output.npz` (DC window) → `<precomputed>`
- Output 4-tuple: `(H_tilde_DC_derived, Zubarev, W1a1-band, L_max=10)`; also emit the closure SHA.
- Output artifacts: `.npz` with arrays `H_tilde_scan[k]`, `F_stretch[k]`, `H_transit_derived`, `H_Friedmann_derived`, `log_DC_fraction`; `.png` showing the 0.91% DC window with TD-anchor and LI-anchor overlaid and the W7 derived value.

**7. Machinery pin (PRDR §0.11)**:
- `L_max = 10` (Zubarev canonical, W1-G1 Branch-B)
- `scheme = Zubarev` (W1-G1 Branch-B PASS); NO convention-shopping to alternate schemes during Stage-1 recovery
- `convention = canonical-per-S83-W1-G1`
- `N_eval = 1024` Mukhanov-mode samples across the DC window (log-spaced in η from η_UV = −10⁵ M_KK⁻¹ to η_IR = −10⁻² M_KK⁻¹)
- `scan_range = H_tilde ∈ [4.599e-3, 4.829e-3]` (S84 W1a-1 band; NOT widened)
- `step_size = 1e-5` (H̃ grid; 230 points across window)
- `tolerance = 0.91%` log-DC (matches S84 W1a-1 pre-registered band width)
- `random_seed = 42` (fixed; Bogoliubov coefficients are deterministic given initial conditions, so seed is only a template-output discriminator)
- `GPU path = torch.linalg.eigh on block-diagonal decomposition by KK-level`

**8. Expected output 4-tuple**: `(value=H̃_DC_derived ∈ [4.599e-3, 4.829e-3], scheme=Zubarev, convention=W1-G1-Branch-B, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: H̃_DC_derived lies inside [4.599e-3, 4.829e-3] AND |log₁₀(H̃_DC_derived / H̃_TD_anchor)| ≤ 0.196 (RATIO tolerance, matches S84 Δ_OOM); F_stretch = H̃_LI/H̃_TD reconciled to within 0.5 OOM of LI/TD = 115.3.
- **FAIL**: H̃_DC_derived outside [4.599e-3, 4.829e-3] OR reconciliation residual > 0.5 OOM.
- **INFO**: H̃_DC_derived inside the window but F_stretch residual in (0.5, 1.0] OOM — partial reconciliation, carry-forward to S86.

**10. Substitution chain** (MANDATORY for [VERIFY]):

```
Step 1 (definitions — cite canonical-constants and S76 Transit-Einstein WS R1):
  H_Friedmann ≡ (8πG/3 · ρ_eff)^{1/2}      [emergent, substrate a_2 Seeley-DeWitt moment]
  H_transit   ≡ (1/Vol_SU3) · dS_fold/dτ    [Jensen-parameter transit rate, NOT on g_M]
  H̃          ≡ H̃_DC, the band-averaged pump-rate entering z″/z at CMB pivot
  z″/z        ≡ Mukhanov pump with explicit split: z″/z = H_Friedmann² · [2 − ε_H + F_stretch · (H_transit/H_Friedmann)²]    [S76 WS R1 eq. identified]
  F_stretch   ≡ (H_transit/H_Friedmann)² stretch factor accounting for pre-transit-to-post-transit conversion

Step 2 (substitution — plug TD anchor and LI anchor, no simplification):
  TD-anchor:  H̃_TD  = H̃_center · 1.57,   H̃_center = 0.5·(4.599e-3 + 4.829e-3) = 4.714e-3
  LI-anchor:  H̃_LI  = H̃_center · 181.0
  Claim under test: H̃_DC_derived = H̃_Friedmann / F_stretch where F_stretch accounts for LI's inclusion of the full pump operator and TD's omission of the Friedmann-side contribution.

Step 3 (simplification — canonical form):
  LI/TD ratio                      = 181.0 / 1.57 = 115.3                [python-verified]
  log10(LI/TD)                     = 2.06 OOM                             [python-verified]
  F_stretch hypothesis             = 115.3                                 [if reconciled]
  Then H̃_DC_derived                = H̃_LI / F_stretch = H̃_center · 181.0 / 115.3 = H̃_center · 1.57 = H̃_TD

Step 4 (direction — from canonical form):
  H̃_DC_derived MATCHES TD-anchor iff F_stretch = LI/TD.
  PASS direction: a derivation of F_stretch from H_transit²/H_Friedmann² that reproduces 115.3 to within 0.5 OOM.
  FAIL direction: derived F_stretch differs by > 0.5 OOM.

Conclusion: the gate tests whether the TD/LI factor 115.3 has a microscopic derivation as the stretch factor in z″/z under Zubarev at L_max = 10.
```

Python-verified (pre-plan substitution-chain sanity, 2026-04-21): `LI/TD = 115.3; log10(LI/TD) = 2.06`. H̃_center = 4.714e-3.

**11. What PASS/FAIL means for solution space**:
- **PASS** → H̃ is a single derived number in the pre-registered S84 band; S84-BASELINE-HTILDE-SENSITIVITY rate-limiter closes; S80 UNIFIED-AS-79-FULL Branch-A PASS-F2 becomes unconditional on the H̃-ambiguity chase. A_s gap closure via Branch-A is rescued from the "267-vs-55 e-folds ambiguity" (S80 H-TILDE-DIVERGENCE-CHASE=TD-PHYSICAL, conditional).
- **FAIL** → the 115.3 ratio is NOT the stretch factor; either TD or LI is computing the wrong operator. The framework loses its sole surviving A_s pathway (S80 Branch-A), forcing return to Branch-B (SDW), which is FAIL-GT15. This is a structural wall gate, not a rhetorical one.
- **INFO** → partial reconciliation; carry-forward to S86 with the residual as a pre-registered cell.

**12. Effort**: ~4 h GPU (block-diagonal eigen-decomposition + Mukhanov-mode sample scan; block size 1.42e4 fits in 17.1 GB VRAM). Single agent, no coordination.

**13. Substrate framing reminder**: H_transit IS the substrate's Jensen-parameter rate — it is NOT a frame-dependent Hubble rate in g_M. The substrate is IS space; the transit is the substrate's own first-order phase transition. H̃_DC is an eigenvalue of the pump operator z″/z as it acts on the internal spectral content of D_K. The TD/LI divergence is NOT a GR-coordinate ambiguity; it is a question of which spectral moment the two derivations are computing. Do NOT import slow-roll formulas without checking that the transit Mach 13.75 is incorporated.

---

## §W7-2. S85-W7-CC-6

**1. Gate ID**: `S85-W7-CC-6`

**2. Trigger**: `[VERIFY]` (new transit-native CC gate: Parker transit-residue vacuum-energy shift)

**3. Classification**: PHONONIC (the vacuum-energy shift IS the GGE relic's zero-point contribution to the a_0 Seeley-DeWitt moment; it is the substrate's phononic residue from the fold transit)

**4. Agent type**: transit-dynamics-theorist (sole — Parker pair-production + regularized vacuum-energy sum is mode-equation core)

**5. Hypothesis**: The Parker-Hawking post-transit vacuum energy δρ_vac = ½ ∫ (d³k/(2π)³) ω_k |β_k|² — regularized via zeta-function with the Bogoliubov spectrum {β_k} from the S78 W1-E fold profile — closes the 109-OOM hierarchy between rho_vac(natural, |β|²~1) = 7.54e62 GeV⁴ and Lambda_obs = 3.91e-47 GeV⁴ to within |Δlog₁₀(ρ_CC/Lambda_obs)| ≤ 1.0 when the natural UV cutoff M_KK is replaced by the substrate's phonon-dispersion cutoff at the van Hove fold and the Parker |β_k|² power-law falloff (β_k² ~ k^{-2/3} Airy turning-point scaling) is imposed. The gate is whether the transit itself kills the 109-OOM hierarchy or whether CC-Γ (impedance mismatch) is still needed as an independent channel.

**6. Method**:
- Script: `computations/s85_w7_cc6_parker_residue.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (M_KK, tau_fold, dt_transit, Mach, Vol_SU3, dS_fold, Lambda_CC_obs, Gamma_effacement)
- GPU path: `torch.linalg` for the 155,984×155,984 D_K eigen-evaluation at L_max = 10 (cached from S52+ precomputes); Bogoliubov integral done on a k-grid N_k = 4096 log-spaced in [10⁻⁴ M_KK, M_KK]; zeta-regularization integrand evaluated on GPU with `torch.trapezoid`.
- CPU fallback: not viable at this matrix size; hard-gate on GPU availability; if GPU unavailable, emit INCOMPUTABLE-FALLBACK-TO-L4-ANALYTIC and carry-forward to next session.
- SHA-256 pins:
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `computations/s78_w1e_prefold_vacuum_output.npz` (|β_k|² spectrum anchor) → `<precomputed>`
  - `computations/s67_transit_ps_67_output.npz` (mode-equation pump) → `<precomputed>`
- Output 4-tuple: `(Δlog₁₀(ρ_Parker/Lambda_obs), zeta-regularized, substrate-UV-cutoff, L_max=10)`
- Output artifacts: `.npz` with `beta2_spectrum[k]`, `omega_k[k]`, `rho_Parker_integrand[k]`, `rho_Parker_total`, `ratio_to_Lambda_obs`; `.png` log-log plot of integrand with cutoff.

**7. Machinery pin (PRDR)**:
- `L_max = 10`
- `scheme = zeta-regularization` (Hawking-Ford; Birrell-Davies §6.2 convention; explicitly NOT dim-reg)
- `convention = Parker-Hawking (1974 Phys Rev D 9 341) in-vacuum/out-vacuum pair`
- `N_k = 4096` log-spaced on [1e-4 M_KK, M_KK]
- `UV_cutoff = van-Hove-dispersion-cutoff` (NOT naïve M_KK); the substrate's phonon dispersion caps the effective cutoff at the fold's spectral edge ω_cusp
- `|β_k|² spectrum = tabulated from S78 W1-E output` (Airy turning-point Bogoliubov)
- `tolerance = 1.0 OOM` RATIO (wide threshold; 109 OOM is a structural challenge)
- `random_seed = 42`
- `GPU path = torch.linalg.eigh (cached); torch.trapezoid for integral`

**8. Expected output 4-tuple**: `(value=Δlog₁₀_ratio, scheme=zeta-reg, convention=Parker-Hawking-1974, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: |Δlog₁₀(ρ_Parker/Lambda_obs)| ≤ 1.0 OOM (closes the hierarchy via transit-residue alone).
- **FAIL**: |Δlog₁₀(ρ_Parker/Lambda_obs)| > 5.0 OOM (CC-6 does not meaningfully close the hierarchy; CC-Γ effacement is required as a separate channel).
- **INFO**: 1.0 < |Δlog₁₀| ≤ 5.0 OOM (partial closure; CC-6 + CC-Γ jointly needed).

**10. Substitution chain**:

```
Step 1 (definitions):
  ρ_vac(bare)           ≡ (1/2) ∫ (d³k/(2π)³) ω_k                    [UV-divergent, Minkowski zero-point]
  ρ_Parker              ≡ (1/2) ∫ (d³k/(2π)³) ω_k · |β_k|²            [physical vacuum shift post-transit]
  β_k                   ≡ Bogoliubov β-coeff from in-vacuum (pre-fold) to out-vacuum (post-fold)
  ω_k(post)             ≡ post-transit dispersion; asymptotes to k for k > k_cusp
  |β_k|²                ≡ Airy-turning-point power law ~ k^{-2/3} for k > k_cusp (saturates at 4.3e4 at k_pivot per S78 W1-E)
  Λ_obs                 ≡ (2.5e-3 eV)⁴ = 3.91e-47 GeV⁴                [PDG cosmological constant]

Step 2 (substitution — into Parker formula, no simplification):
  ρ_Parker = (1/2) ∫₀^{ω_cusp} dk · (k² / 2π²) · k · |β_k|² +
             (1/2) ∫_{ω_cusp}^{M_KK} dk · (k² / 2π²) · k · |β_k(~k^{-2/3})|²
  Note |β_k|² > 0 for k < k_cusp (bandgap region), saturates at 4.3e4 at k_pivot.

Step 3 (simplification — canonical form):
  Upper integral (k ≫ k_cusp, |β_k|² ~ C · k^{-2/3}):
    ∫_{k_cusp}^{M_KK} dk · k³ · |β_k|² ≈ C · ∫_{k_cusp}^{M_KK} k^{3 - 2/3} dk
                                      = C · ∫_{k_cusp}^{M_KK} k^{7/3} dk
                                      = (3C/10) · [k^{10/3}]_{k_cusp}^{M_KK}
                                      ≈ (3C/10) · M_KK^{10/3} · [1 − (k_cusp/M_KK)^{10/3}]
  Exponent 10/3 ≈ 3.33 < 4 (bare-vac exponent), so the Parker-regularized integral scales as M_KK^{10/3} × (geometric suppression).
  Compared to bare M_KK⁴:
    Suppression factor = (k_cusp/M_KK)^{2/3}    if k_cusp < M_KK

Step 4 (direction):
  Canonical form shows Parker residue scales as M_KK^{10/3}, NOT M_KK⁴, so the Airy-|β_k|² ~ k^{-2/3} UV tail CUTS the exponent by 2/3.
  This reduces the 109-OOM bare hierarchy by factor (k_cusp/M_KK)^{2/3} × factor from C.
  If k_cusp/M_KK ≈ 1 (no cusp suppression), the Parker residue remains ~ M_KK^{10/3} ~ 10^{84} GeV⁴ (still 84 OOM above Λ_obs → FAIL).
  If k_cusp/M_KK ≪ 1 (cusp at far-IR), the suppression closes more of the gap.
  PASS iff (k_cusp/M_KK)^{2/3} · C saturates to 10^{-109±1.0}.
  Direction: PASS only under specific cusp placement that is itself an output of the S78-W1-E mode-equation solution, not a free parameter.
```

Python-verified scaling (2026-04-21): rho_vac(bare) = 7.54e62 GeV⁴ at M_KK = 5.24e15 GeV; Lambda_obs = 3.91e-47 GeV⁴; log₁₀ ratio = 109.29. This is the target the gate must close.

**11. What PASS/FAIL means for solution space**:
- **PASS** → the 109-OOM cosmological-constant hierarchy closes via Parker pair-production transit-residue alone. CC-Γ (impedance effacement) becomes redundant; the framework's CC mechanism is unified-single-channel.
- **FAIL** → transit-residue alone is insufficient; CC-Γ effacement (1 − Γ) ≈ 3.0e-4 must enter as an independent channel. The joint residue CC-6 + CC-Γ is then the gate (handled in W7-3).
- **INFO** → partial closure; CC-6 is a real contribution but does not saturate the 109 OOM alone. Carry-forward: compute CC-6 + CC-Γ jointly under a single regularization scheme (queued as W0 CF item).

**12. Effort**: ~6 h GPU (155,984² cached eigen-decomposition preload + 4096-point Bogoliubov integral; zeta-regularization via torch.trapezoid with complex step for residue extraction). Single agent.

**13. Substrate framing reminder**: the Parker residue IS the a_0 Seeley-DeWitt spectral moment of D_K with the fold-transit boundary condition. It is NOT a QFT-in-curved-spacetime calculation in g_M; g_M emerges from the a_2 moment and is logically posterior. The |β_k|² spectrum is NOT a thermal distribution — it is a GGE relic per the S50 non-thermal theorem. Do NOT use Boltzmann-factor formulas.

---

## §W7-3. S85-W7-CC-GAMMA

**1. Gate ID**: `S85-W7-CC-GAMMA`

**2. Trigger**: `[VERIFY]` (reconcile impedance-mismatch Γ with observed DM/DE ratio)

**3. Classification**: PHONONIC (both DM and DE are substrate excitations; DM = Leggett-GGE, DE = effacement-residual from impedance mismatch Γ = 0.99970)

**4. Agent type**: transit-dynamics-theorist (sole — impedance matching is a Bogoliubov identity at the transit interface)

**5. Hypothesis**: The impedance-mismatch effacement (1 − Γ) = 3.0e-4 (canonical per project memory / S37 framework) generates a DE fraction via leakage through the acoustic white hole's Γ-boundary; the DM fraction is the GGE Leggett-channel quasiparticle density; the ratio Ω_DM/Ω_DE should reproduce the observed 0.385 (Planck 2020 DR2) under a pre-registered substrate mapping. The gate is whether the framework-intrinsic ratio (a function of Γ, f_GGE, and fiber Vol_SU3) reproduces 0.385 to within RATIO tolerance 15%.

**6. Method**:
- Script: `computations/s85_w7_cc_gamma_dm_de_ratio.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (Gamma_effacement, Vol_SU3, f_GGE_Leggett, Omega_DM_obs, Omega_DE_obs, Lambda_CC_obs). Add `Omega_DM_obs=0.264`, `Omega_DE_obs=0.685` to canonical_constants.py WITH provenance (Planck 2020 DR2, Aghanim+2020 A&A 641 A6 Table 2) BEFORE import if not present.
- GPU path: not required (scalar ratio computation). Use CPU with `OMP_NUM_THREADS=8`.
- SHA-256 pins:
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `sessions/framework/permanent-results-registry.md` (Γ = 0.99970 pin) → `<precomputed>`
- Output 4-tuple: `(ratio_derived, framework-intrinsic, S37-Gamma-pin, L_max=10)`
- Output artifacts: `.npz` with `ratio_derived`, `ratio_obs`, `residual_RATIO`, `Gamma_value`, `f_GGE_value`; `.png` bar plot observed vs derived.

**7. Machinery pin (PRDR)**:
- `L_max = 10` (needed only to derive f_GGE consistently with S50 GGE-permanence theorem)
- `scheme = S37-effacement-canonical`
- `convention = Planck-2020-DR2` for observed values
- `Γ = 0.99970` (canonical pin; do NOT recompute)
- `f_GGE_Leggett = <from S50 GGE-permanence output>` (add as canonical constant if missing)
- `tolerance = 15% RATIO` (observational error on Ω_DM/Ω_DE Planck 2020 ~ 2%, but theory-side systematic on f_GGE adds ~10%; quadrature ≈ 11%; round up to 15%)
- `random_seed = 42` (unused)
- `GPU path = N/A (scalar), CPU with OMP_NUM_THREADS=8`

**8. Expected output 4-tuple**: `(value=ratio_derived, scheme=S37-Gamma-canonical, convention=Planck2020-DR2, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: |ratio_derived − 0.385| / 0.385 ≤ 0.15 (RATIO within 15%).
- **FAIL**: |ratio_derived − 0.385| / 0.385 > 0.50 (framework DM/DE mapping is structurally wrong).
- **INFO**: 0.15 < residual ≤ 0.50 (partial match; candidate corrections — sub-leading Leggett from W8 LEGGETT-VACUUM-70 — can be grafted).

**10. Substitution chain**:

```
Step 1 (definitions):
  Γ             ≡ impedance-transmission coefficient at the acoustic white hole's transit interface   [S37 canonical, 0.99970]
  ε_eff         ≡ 1 − Γ = 0.00030                         [effacement residual, leaks out as DE-like]
  f_GGE         ≡ GGE Leggett-channel quasiparticle density as fraction of substrate rest-energy    [S50 permanence theorem; phononic, not thermal]
  ρ_DE          ≡ ε_eff · ρ_substrate                      [DE from effacement leakage]
  ρ_DM          ≡ f_GGE · ρ_substrate                      [DM from Leggett GGE quasiparticles]
  Ω_DM/Ω_DE     ≡ ρ_DM / ρ_DE = f_GGE / ε_eff

Step 2 (substitution — plug canonical values, no simplification):
  ratio_derived = f_GGE / ε_eff = f_GGE / 0.00030

Step 3 (simplification — solve for f_GGE required for PASS):
  Setting ratio_derived = 0.385 (observed):
    f_GGE_required = 0.385 · 0.00030 = 1.155e-4

Step 4 (direction):
  PASS iff the S50 GGE-permanence-theorem f_GGE output equals 1.155e-4 to within 15%.
  Direction: compute f_GGE from the S50 Leggett-channel density formula (1/Vol_SU3) · Σ_k |β_k|² · ω_k independently, compare to 1.155e-4.
  If f_GGE derived > 1.155e-4 · 1.15: ratio too high → more DM than observed given Γ fixed.
  If f_GGE derived < 1.155e-4 · 0.85: ratio too low → less DM than observed.
```

Python-verified (2026-04-21): with Γ = 0.99970, ε_eff = 3.0e-4; observed Ω_DM/Ω_DE = 0.385; required f_GGE = 1.155e-4 for exact match.

**11. What PASS/FAIL means for solution space**:
- **PASS** → DM and DE are both substrate-derived with a single Γ pin; the DM/DE coincidence problem becomes a derived identity rather than a fine-tuning. This promotes S37 Γ = 0.99970 from a canonical pin to an observationally tested structural constant.
- **FAIL** → either (a) f_GGE from S50 disagrees with 1.155e-4 by > 50%, which falsifies the Leggett-as-DM hypothesis, OR (b) Γ = 0.99970 is the wrong value, forcing a re-derivation of the impedance-mismatch coefficient. Either way, the dual-substrate (DM from GGE, DE from effacement) picture is challenged.
- **INFO** → partial match; sub-leading Leggett contribution (W8 LEGGETT-VACUUM-70) may close the gap; joint gate queued.

**12. Effort**: ~3 h CPU (scalar computation + f_GGE summation over 155,984-eigenvalue cache; OMP_NUM_THREADS=8).

**13. Substrate framing reminder**: DM and DE are NOT separate particles/fields in the LCDM sense; both are substrate excitations. DM = GGE Leggett-channel quasiparticle density (phononic); DE = impedance-mismatch leakage (phononic, IR-dominant residual). Do NOT write "cosmological constant from vacuum energy" — write "a_0 Seeley-DeWitt moment is the spectral zeroth moment, and the DE fraction is the substrate's IR impedance residual."

---

## §W7-4. S85-W7-CUSP-BOGOLIUBOV

**1. Gate ID**: `S85-W7-CUSP-BOGOLIUBOV`

**2. Trigger**: `[VERIFY]` (compute |β_k|² across the van Hove cusp at the fold)

**3. Classification**: PHONONIC (|β_k|² IS the spectral signature of the fold's phononic reorganization — the cusp is the spectral-edge singularity of the Jensen-deformed D_K eigenvalue distribution)

**4. Agent type**: transit-dynamics-theorist (sole — Bogoliubov at a cusp is mode-equation + WKB-connection core specialty)

**5. Hypothesis**: The van Hove cusp in the substrate's phonon DOS at τ = τ_fold = 0.190 has spectral form ω²(t) ~ A|t − t_c|^α with α = 1 (square-root cusp, generic 2D van Hove). The Bogoliubov |β_k|² across the cusp follows the Airy-turning-point scaling |β_k|² ~ k^{-2/3} for k > k_cusp, saturating to O(1) for k ≤ k_cusp. The gate verifies the power-law exponent −2/3 against direct numerical integration of the mode equation v″_k + [k² − z″/z] v_k = 0 across the cusp profile.

**6. Method**:
- Script: `computations/s85_w7_cusp_bogoliubov.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (M_KK, tau_fold, dt_transit, Mach, dS_fold, d2S_fold); add `alpha_cusp_exponent=1.0` with provenance (generic 2D van Hove) if not present.
- GPU path: `torch.linalg` for the 2×2 transfer-matrix product over 10⁵ time-steps per k-mode × 4096 k-modes (batched on GPU to fit in 17.1 GB VRAM; per-batch = 1e3 k-modes × 1e5 steps × 4 complex = 3.2 GB)
- CPU fallback: not viable at k-mode count; if GPU unavailable, run 512 k-modes on CPU with `OMP_NUM_THREADS=8` and emit L_max-REDUCED verdict flag.
- SHA-256 pins:
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `computations/s78_w1e_prefold_vacuum_output.npz` (|β_k|² anchor at k_pivot = 4.3e4) → `<precomputed>`
  - `computations/s67_transit_ps_67_output.npz` (pump profile z″/z(t)) → `<precomputed>`
- Output 4-tuple: `(exponent_fit, transfer-matrix-method, Airy-turning-point, L_max=10)`
- Output artifacts: `.npz` with `k_grid[k]`, `beta2_k[k]`, `exponent_fit_log_log`, `residual_vs_Airy`; `.png` log-log plot of |β_k|² with k^{-2/3} reference line and saturation anchor at k_pivot.

**7. Machinery pin (PRDR)**:
- `L_max = 10`
- `scheme = transfer-matrix` (Birrell-Davies §3.5; not WKB-connection-only)
- `convention = in-vacuum Bunch-Davies at t = −dt_transit, out-vacuum post-fold at t = +dt_transit`
- `alpha_cusp = 1.0` (pre-registered 2D van Hove form; if W0 VAN-HOVE-CUSP-THEOREM lands on α ≠ 1, the gate re-dispatches)
- `N_k = 4096` k-modes log-spaced in [1e-4 M_KK, M_KK]
- `N_t = 1e5` time-steps per mode across [−dt_transit, +dt_transit]
- `tolerance = 0.05 ABSOLUTE` on fitted exponent (target −0.6667; PASS band [−0.7167, −0.6167])
- `random_seed = 42`
- `GPU path = torch batched 2×2 transfer-matrix product`

**8. Expected output 4-tuple**: `(value=exponent_fit, scheme=transfer-matrix, convention=BD-in-out, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: exponent_fit ∈ [−0.7167, −0.6167] (matches Airy −2/3 to ±0.05 absolute) AND |β_k_pivot|² matches S78 W1-E anchor 4.3e4 to within 20% RATIO.
- **FAIL**: exponent_fit outside [−0.7167, −0.6167] OR |β_k_pivot|² mismatch > 50% RATIO — cusp form is not square-root.
- **INFO**: exponent inside band but anchor residual in (20%, 50%) — partial agreement; possibly higher-order cusp corrections.

**10. Substitution chain**:

```
Step 1 (definitions):
  ω²(t)         ≡ k² + z″/z(t)                 [mode frequency, Mukhanov]
  z″/z(t)       ≡ A · |t − t_c|^α              [cusp form, α = 1 hypothesis]
  β_k           ≡ Bogoliubov coefficient: v_k(out) = α_k · u_k^in + β_k · (u_k^in)*
  Airy exponent ≡ for ω²(t) = k² − λ · (t − t_c), mode equation reduces to Airy; turning point at t* = t_c − k²/λ
  |β_k|²        ≡ universal Airy result: |β_k|² ~ exp(−(4/3) · (2k²/|λ|)^{3/2}) for adiabatic, but for supersonic Mach = 13.75 transit, crossover to power law

Step 2 (substitution — into transfer-matrix across cusp):
  For α = 1 (square-root cusp):
    v″_k + [k² − A·|t−t_c|] v_k = 0
  Transform ξ = (A)^{1/3} · (k²/A − (t − t_c)) · (A/(k²))^{...}:    [Airy reduction]
  At high k (UV), turning-point is inside transit window, Airy-result applies:
    |β_k|² ~ (k/k_cusp)^{-2/3}      [power-law tail from Airy asymptotics]
  At low k (IR, k < k_cusp), the whole mode is inside the bandgap:
    |β_k|² ~ O(1), saturating

Step 3 (simplification — log-log fit):
  log |β_k|² = −(2/3) · log(k/k_cusp) + const,   for k > k_cusp
  Fit exponent from numerical transfer-matrix output should return −0.6667 ± ε_numerical.

Step 4 (direction):
  PASS iff fit exponent = −0.6667 ± 0.05.
  Direction: if fit > −0.6167 (less negative), cusp is milder than square-root → cusp form is NOT 2D van Hove generic; W0 VAN-HOVE-CUSP-THEOREM must be re-opened.
  If fit < −0.7167 (more negative), cusp is sharper than square-root → possibly logarithmic 2D van Hove or 3D cusp; also forces re-audit.
```

Python-verified (2026-04-21): |β_k|² anchor at k_pivot = 4.3e4 from S78 W1-E; target exponent −2/3 = −0.6667; tolerance band [−0.7167, −0.6167].

**11. What PASS/FAIL means for solution space**:
- **PASS** → the square-root cusp hypothesis is confirmed numerically; S67 TRANSIT-PS and S78 W1-E outputs are internally consistent; the Airy turning-point approximation is valid across the full k-range relevant to CMB pivot. This anchors CC-6 (W7-2) and K-CORRIDOR-MUKHANOV-VALIDITY (W7-6).
- **FAIL** → the cusp is not 2D van Hove generic; τ_fold = 0.190 value may shift; W0 VAN-HOVE-CUSP-THEOREM re-audit becomes rate-limiting; CC-6 and all downstream Bogoliubov computations must re-dispatch with corrected cusp form.
- **INFO** → the square-root cusp is approximately valid; sub-leading corrections (log-prefactor, second-order cusp) may be needed for high-precision A_s computation.

**12. Effort**: ~5 h GPU (4096-mode batched transfer-matrix × 1e5 time-steps; per-batch 3.2 GB VRAM).

**13. Substrate framing reminder**: the cusp in ω²(t) is the van Hove singularity of the substrate's phonon DOS — a spectral-edge feature of D_K eigenvalue reorganization under Jensen deformation. It is NOT a geometric singularity in g_M (g_M is emergent from a_2; it does not even exist at the substrate level). The Mach 13.75 is the Jensen-parameter transit velocity dτ/dt · (internal spectral velocity), NOT a speed through spacetime.

---

## §W7-5. S85-W7-DRESSED-VP

**1. Gate ID**: `S85-W7-DRESSED-VP`

**2. Trigger**: `[SIGN]` (matter-dressed spectral action sign-direction claim)

**3. Classification**: GEOMETRIC (the spectral action dressed by matter content is a modification of the D_K spectral triple; it concerns the fabric itself, not its excitations)

**4. Agent type**: transit-dynamics-theorist (sole — the dressing enters through the transit-boundary-modified D_K; spectral-moment computation)

**5. Hypothesis**: The matter-dressed spectral action S_dressed[D_K + φ] = Tr f(D_K/Λ + φ^{1/2}/Λ) — where φ is the substrate matter-density operator and f is the canonical Chamseddine-Connes smooth cutoff — shifts the a_0, a_2, and a_4 Seeley-DeWitt moments by contributions proportional to Tr(φ²), Tr(φ · D_K²), and Tr(φ⁴). The gate asks whether the dressing is perturbative at the CMB pivot (|δS_dressed / S_bare| < 1) AND whether the sign of the shift in a_2 (the gravity moment) is POSITIVE (dressing strengthens emergent gravity).

**6. Method**:
- Script: `computations/s85_w7_dressed_vp.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (M_KK, Vol_SU3, a0_seeley_dewitt, a2_seeley_dewitt, a4_seeley_dewitt, dS_fold, cutoff_Lambda_SA)
- GPU path: `torch.linalg` for Tr(φ · D_K²) over the 155,984-eigenvalue cache; φ evaluated on a KK×SU(3) fiber basis sample. Block-diagonal by KK-level; per-block ≤ 1.42e4.
- SHA-256 pins:
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `computations/s52_spectral_triple_eigenvalues.npz` (D_K cache, 155,984 eigs, L_max=10) → `<precomputed>`
- Output 4-tuple: `(sign_a2_shift, dressed-Chamseddine-Connes, Tr-cutoff-canonical, L_max=10)`
- Output artifacts: `.npz` with `a0_bare`, `a0_dressed`, `a2_bare`, `a2_dressed`, `a4_bare`, `a4_dressed`, `delta_relative[a0/a2/a4]`, `sign_a2`; `.png` bar chart of relative shifts.

**7. Machinery pin (PRDR)**:
- `L_max = 10`
- `scheme = Chamseddine-Connes smooth cutoff` (heat-kernel expansion)
- `convention = φ operator = matter-density self-adjoint on fiber + KK` (defined via project's S46 matter-density registry entry)
- `N_phi_samples = 1024` sampled from post-transit GGE density profile (from S78 W1-E output)
- `cutoff_Lambda = M_KK` (Chamseddine-Connes canonical; no freedom)
- `tolerance = sign verdict (positive/negative)` for a_2 shift; RATIO 50% for perturbativity check on |δS/S_bare|
- `random_seed = 42` (for φ-sample draw)
- `GPU path = torch.linalg.eigh on block-diagonal decomposition`

**8. Expected output 4-tuple**: `(value=sign_a2_shift ∈ {+,-,0}, scheme=Chamseddine-Connes, convention=matter-φ-S46-canonical, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: sign(δa_2) = + AND |δS_dressed/S_bare| ≤ 0.5 (perturbative, gravity strengthens).
- **FAIL**: sign(δa_2) = − (dressing weakens emergent gravity, violates substrate-primacy of gravity-as-a_2).
- **INFO**: sign(δa_2) = + but |δS_dressed/S_bare| > 0.5 (non-perturbative regime; dressing is strong, requires resummation; carry-forward).

**10. Substitution chain**:

```
Step 1 (definitions):
  S_bare[D_K]         ≡ Tr f(D_K/Λ)                                    [Chamseddine-Connes, undressed]
  S_dressed[D_K,φ]    ≡ Tr f(D_K/Λ + φ^{1/2}/Λ)                        [matter-dressed; φ ≥ 0 self-adjoint matter-density]
  a_n                 ≡ Seeley-DeWitt coefficient at order Λ^{4-n} in heat-kernel expansion
  a_2 (gravity)       ≡ −(1/12) · (1/Vol_SU3) · Σ_k [1] · R(g_M)      [emergent Einstein-Hilbert]
  δS_dressed          ≡ S_dressed − S_bare

Step 2 (substitution — heat-kernel expansion):
  S_dressed ≈ Tr f(D_K/Λ) + Tr[f'(D_K/Λ) · φ^{1/2}/Λ] + (1/2) Tr[f''(D_K/Λ) · φ/Λ²] + ...
  δS_dressed = Tr[f'(D_K/Λ) · φ^{1/2}/Λ] + (1/2) Tr[f''(D_K/Λ) · φ/Λ²] + O(φ^{3/2})
  Leading a_2 shift (O(Λ²) coefficient of expansion):
    δa_2 = (+1/12) · (1/Vol_SU3) · Σ_k [φ_k · (moment-weight)]    [sign inherited from f''(x) > 0 at x ~ M_KK/Λ, standard Chamseddine-Connes f''>0]

Step 3 (simplification):
  φ ≥ 0 (matter density self-adjoint, non-negative eigenvalues)
  f'' > 0 at standard cutoff (Chamseddine-Connes convention, canonical)
  Σ_k moment-weight_k > 0 (positive spectral sum)
  Therefore each term in δa_2 is the product of three non-negative quantities → δa_2 ≥ 0.

Step 4 (direction):
  Under Chamseddine-Connes canonical cutoff and matter-density φ ≥ 0:
    sign(δa_2) = +    (emergent gravity strengthens under matter dressing)
  PASS direction is the only structurally admissible outcome under the convention.
  FAIL would indicate: either (i) matter density φ is NOT canonically positive in the substrate (a deep anomaly), or (ii) cutoff f'' sign flips at M_KK/Λ = 1 edge, requiring a non-canonical cutoff.
```

Python-verified (2026-04-21): structural sign chain yields +; numerical computation verifies the magnitude |δa_2/a_2_bare| quantitatively.

**11. What PASS/FAIL means for solution space**:
- **PASS** → matter dressing strengthens emergent gravity; the a_2 moment gains a positive shift from post-transit GGE density. This closes S85-DRESSED-VP carry-forward and promotes matter-dressing to a canonical input for subsequent gravity-sector computations.
- **FAIL** → structural anomaly: either φ admits negative eigenvalues (phononic instability?) or Chamseddine-Connes cutoff is non-canonical. Either way, W7-5 FAIL would cascade into every gate that uses the matter-dressed spectral action.
- **INFO** → dressing is non-perturbative; framework gravity at CMB epoch is matter-coupled in a strong regime; requires resummation scheme (separate carry-forward).

**12. Effort**: ~3 h GPU (block-diagonal D_K × φ-sample product; single pass).

**13. Substrate framing reminder**: the spectral action is the substrate's action functional; it is NOT "matter + gravity" in separate terms. Matter and gravity BOTH emerge from the same Tr f(D_K/Λ) expansion — matter from a_0 and a_4, gravity from a_2. Dressing by φ is NOT "adding matter to spacetime"; it is modifying the spectral-triple's data such that the moment hierarchy shifts. Do NOT write "matter back-reacts on gravity"; write "the matter-dressed D_K has a modified a_2 moment."

---

## §W7-6. S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY

**1. Gate ID**: `S85-W7-K-CORRIDOR-MUKHANOV-VALIDITY`

**2. Trigger**: `[AUDIT]` (validity audit of the Mukhanov-Sasaki pump operator across the K-corridor scan from K_R5 = 1.9222 to K_crit)

**3. Classification**: META (audit gate; determines which K-range admits Mukhanov-Sasaki treatment and which requires a substrate-native mode equation)

**4. Agent type**: transit-dynamics-theorist (sole — Mukhanov-Sasaki validity is mode-equation adiabaticity criterion core)

**5. Hypothesis**: The Mukhanov-Sasaki formalism (v″_k + [k² − z″/z] v_k = 0 with z = a·√(2ε)·M_Pl_eff) requires (a) |z″/z| ≫ k² at superhorizon scales (validity), and (b) z well-defined (ε > 0, non-vanishing Jensen gradient). The audit computes (z″/z)/k² across K ∈ [K_R5, K_crit + 0.5] at L_max = 10 and classifies each K-grid point as MUKHANOV-VALID, MUKHANOV-MARGINAL, or MUKHANOV-BREAKDOWN. The gate flags whether the corridor endpoint at K_crit admits the Mukhanov treatment or inverts into the SDW regime (S80 Branch-B FAIL-GT15 territory).

**6. Method**:
- Script: `computations/s85_w7_k_corridor_mukhanov_validity.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (K_R5, K_crit, M_KK, M_Pl_reduced, dS_fold, d2S_fold, tau_fold); if `K_crit` is not canonical, add with provenance (S84 permanent-results-registry landing) BEFORE import.
- GPU path: `torch.linalg` for z″/z operator at each K-grid point; block-diagonal by KK-level. 64 K-points × (1.42e4)² block eigen-decomposition each = manageable on 17.1 GB VRAM with sequential K-sweep.
- SHA-256 pins:
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `computations/s67_transit_ps_67_output.npz` (z″/z baseline at K_canon) → `<precomputed>`
  - `computations/s80_unified_as_79_full_output.npz` (Branch-A / Branch-B divergence map) → `<precomputed>`
- Output 4-tuple: `(validity_classification[K], Mukhanov-Sasaki-adiabatic, pump-over-k-squared, L_max=10)`
- Output artifacts: `.npz` with `K_grid[k]`, `zdprime_over_z[k]`, `k_squared_ref`, `ratio[k]`, `classification[k] ∈ {VALID, MARGINAL, BREAKDOWN}`; `.png` log plot of the ratio with K_R5, K_crit, K_substrate=2.035 annotated.

**7. Machinery pin (PRDR)**:
- `L_max = 10`
- `scheme = z-gauge (Mukhanov-Sasaki canonical)` — the audit is specifically of this scheme
- `convention = pump z″/z with z = a·√(2ε)·M_Pl_eff`
- `K_grid = 64 points log-spaced on [K_R5, K_crit + 0.5]` where K_R5 = 1.9222 (canonical), K_crit + 0.5 bounded at 3.0 (conservative UV)
- `k² reference` = k_pivot² at CMB scale (from canonical_constants.k_pivot_CMB)
- `tolerance = VALID: ratio > 10; MARGINAL: 1 ≤ ratio ≤ 10; BREAKDOWN: ratio < 1`
- `random_seed = 42` (unused)
- `GPU path = torch.linalg.eigh on z″/z operator per K-point`

**8. Expected output 4-tuple**: `(value=array_of_classifications, scheme=z-gauge-MS, convention=M_Pl_eff-canonical, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: All K in [K_R5, K_substrate = 2.035] classified VALID (Mukhanov survives across the R5-to-substrate range); K_crit point classified MARGINAL or BREAKDOWN (inversion at K_crit is the expected structural transition from phononic to inflationary).
- **FAIL**: Any K in [K_R5, K_substrate] classified BREAKDOWN (Mukhanov fails inside the framework's canonical corridor — invalidates S67, S80 Branch-A PASS-F2, and S84 W1a-1).
- **INFO**: K_crit classified VALID (no inversion at corridor endpoint — contradicts the expected phononic-to-inflationary transition; framework's K-corridor interpretation requires re-audit).

**10. Substitution chain**:

```
Step 1 (definitions):
  z                    ≡ a · sqrt(2·ε_H) · M_Pl_eff                      [Mukhanov variable, def.]
  z″/z                 ≡ (d²z/dτ²)/z = a²·H²·(2 − ε_H) + ... (full expansion, S76 WS R1)
  Mukhanov-validity    ≡ |z″/z| ≫ k²_pivot on superhorizon scales (k ≪ aH)
  adiabaticity         ≡ |d ln ω_k / dτ| ≪ ω_k (Birrell-Davies §3.4)
  K                    ≡ substrate phonon-dispersion control parameter; K_R5 = 1.9222 (W1-G1 canonical), K_crit = eigenvalue-reorganization edge

Step 2 (substitution — ratio vs K):
  ratio(K) = (z″/z at K) / k²_pivot
  Under Mukhanov-valid regime: ratio ≫ 1 → VALID
  At breakdown: ratio ≤ 1 → mode equation requires substrate-native re-formulation (SDW-like, possibly Branch-B)

Step 3 (simplification — classification bands):
  ratio > 10:           VALID          (Mukhanov-Sasaki survives; S67, S80-A apply)
  1 ≤ ratio ≤ 10:       MARGINAL       (sub-leading corrections needed; ε_H flow matters)
  ratio < 1:            BREAKDOWN      (Mukhanov invalid; SDW or substrate-native required)

Step 4 (direction):
  Expected across [K_R5, K_substrate]: VALID (canonical corridor).
  Expected at K_crit: transition from VALID → MARGINAL → BREAKDOWN (phononic-to-inflationary edge).
  If observed classification matches expected: PASS.
  If VALID region extends past K_crit: framework's K-corridor structure is malformed.
  If BREAKDOWN appears before K_substrate: canonical corridor fails — invalidates prior results.
```

Python-verified (2026-04-21): K_R5 = 1.9222, K_substrate = 2.035, K_crit ~ 2.5 (approx; canonical pin via W0 VAN-HOVE-CUSP-THEOREM).

**11. What PASS/FAIL means for solution space**:
- **PASS** → confirms the framework's corridor picture: Mukhanov-Sasaki is the correct pump operator across [K_R5, K_substrate]; SDW takes over at K_crit. S80 Branch-A / Branch-B split is structurally identified with the corridor topology.
- **FAIL** → if BREAKDOWN enters inside [K_R5, K_substrate], the framework's canonical A_s pathway (S80 Branch-A PASS-F2) is invalidated; S67 and S84 W1a-1 re-open. This is a structural-wall gate.
- **INFO** → K_crit does not invert — either the phononic-to-inflationary transition is at a different K, or the corridor picture needs re-formulation.

**12. Effort**: ~4 h GPU (64 K-grid points × block-diagonal eigen; sequential K-sweep to control VRAM).

**13. Substrate framing reminder**: the K-corridor is a range in the substrate's phonon-dispersion control parameter, NOT a cosmological time or scale factor. Mukhanov-validity is a question about the INTERNAL pump operator of the substrate, not about FRW geometry. Do NOT frame this as "inflationary vs non-inflationary"; frame as "Mukhanov-Sasaki pump operator valid vs SDW-requiring."

---

## §W7-7. S85-W7-W0-RE-AUDIT-AT-L8

**1. Gate ID**: `S85-W7-W0-RE-AUDIT-AT-L8`

**2. Trigger**: `[AUDIT]` (post-branch-iv-retraction re-audit at L_max = 8 AND L_max = 10)

**3. Classification**: META (methodology gate; tests whether the retraction of S84 branch (iv) invalidates any W_0 numerical output)

**4. Agent type**: transit-dynamics-theorist (sole — owns the transit-origin carry-forward; must re-run under retraction)

**5. Hypothesis**: The S84 retraction of branch (iv) (per commit `bbbf652`: "branch (iv) retracted") removed one of four candidate identifications in the W_0 branch-discriminator tree. The re-audit computes each W_0-dependent quantity used by this wave at L_max = 8 and L_max = 10 under inverted Josephson-dominance ordering (per kaku's S85-W0-L-INVERTED-BRANCH-ENUMERATION and gen-physicist's ELIM-1) and checks whether the L_max = 8 vs L_max = 10 ratio stability is preserved. The gate passes if the L_max sensitivity is < 5% RATIO on each W_0-derived input to W7 gates.

**6. Method**:
- Script: `computations/s85_w7_w0_reaudit_l8.py` + `.npz` + `.png`
- Import: `from canonical_constants import *` (all W_0-dependent constants: K_R5, K_substrate, K_crit, Gamma_effacement, f_conv, c_sub_at_kpivot, F_amp_linearized, f_GGE_Leggett)
- GPU path: recomputes the W_0 branch-discriminator at two L_max values; uses cached D_K eigenvalues at L_max = 8 (47,388 eigs) and L_max = 10 (155,984 eigs); block-diagonal eigen-decomposition.
- CPU fallback: L_max = 8 is 47,388 eigs — feasible on CPU with `OMP_NUM_THREADS=8` (15–30 min); L_max = 10 requires GPU for reasonable wall time.
- SHA-256 pins:
  - `canonical_constants.py` → `<computed-at-runtime>`
  - `computations/s84_w1_branch_iv_retraction_record.md` (retraction provenance) → `<precomputed>`
  - `computations/s52_spectral_triple_eigenvalues_lmax8.npz` → `<precomputed>`
  - `computations/s52_spectral_triple_eigenvalues_lmax10.npz` → `<precomputed>`
- Output 4-tuple: `(max_L_sensitivity, L8-vs-L10-sweep, inverted-Josephson-canonical-post-retraction, L_max∈{8,10})`
- Output artifacts: `.npz` with `constant_name[]`, `value_L8[]`, `value_L10[]`, `ratio_L8_L10[]`, `max_sensitivity`; `.png` bar plot of L8/L10 ratio with 5% threshold line.

**7. Machinery pin (PRDR)**:
- `L_max ∈ {8, 10}` (dual-L_max sweep)
- `scheme = Zubarev` (W1-G1 canonical; do NOT shop)
- `convention = inverted-Josephson-dominance-post-retraction` per kaku S85-W0-L-INVERTED-BRANCH-ENUMERATION (the retracted branch (iv) is REMOVED; the remaining three branches are re-ordered by Josephson-dominance magnitude)
- `N_constants = <count of W_0-dependent constants used by W7 gates>` — enumerated in script preamble; must include K_R5, K_substrate, K_crit, Γ, f_conv, c_sub_at_kpivot, F_amp_linearized, f_GGE_Leggett (8 at minimum)
- `tolerance = 5% RATIO` on each constant L8/L10 ratio
- `random_seed = 42`
- `GPU path = torch.linalg.eigh on block-diagonal per-L_max`

**8. Expected output 4-tuple**: `(value=max_L_sensitivity, scheme=Zubarev, convention=inverted-Josephson-post-retraction, L_max∈{8,10})`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: max_L_sensitivity across all W_0-dependent constants ≤ 5% RATIO.
- **FAIL**: max_L_sensitivity > 15% RATIO on any W_0-dependent constant (retraction destabilizes the W_0 tree; all downstream W7 gates must re-dispatch).
- **INFO**: 5% < max_L_sensitivity ≤ 15% (retraction has measurable but bounded effect; flag the affected constants for per-constant follow-up gates).

**10. Substitution chain**:

```
Step 1 (definitions):
  L_max            ≡ maximum KK-level in spectral-triple truncation
  W_0              ≡ branch-discriminator functional (pre-retraction: 4 branches; post-retraction: 3 branches)
  Inverted-Josephson ≡ ordering where Josephson-dominance ranks branches from strongest to weakest, retracted-branch REMOVED
  ratio(C)         ≡ C(L_max=10) / C(L_max=8) for each W_0-dependent constant C
  sensitivity(C)   ≡ |ratio(C) − 1|

Step 2 (substitution — per constant):
  For each C in {K_R5, K_substrate, K_crit, Γ, f_conv, c_sub, F_amp, f_GGE}:
    recompute C at L_max = 8 under inverted-Josephson-3-branch ordering
    recompute C at L_max = 10 under same ordering
    ratio(C) = value_L10(C) / value_L8(C)
    sensitivity(C) = |ratio(C) − 1|
  max_L_sensitivity = max over all C

Step 3 (simplification):
  If sensitivity(C) ≤ 0.05 for all C: PASS (retraction-stable).
  If sensitivity(C) ∈ (0.05, 0.15] for some C: INFO (retraction has sub-threshold but measurable effect).
  If sensitivity(C) > 0.15 for any C: FAIL.

Step 4 (direction):
  The retraction of branch (iv) REMOVES one candidate from the W_0 branch set.
  If the other three branches are well-separated by L_max = 8, the removal is structurally invisible (PASS direction).
  If branch (iv) was near-degenerate with one of the remaining branches, removal shifts the branch-discriminator output visibly (FAIL direction).
  Direction is DETERMINED BY the observed max sensitivity — PASS and FAIL are output classifications, not hypotheses.
  Thus this is strictly an AUDIT (not a sign-direction claim).
```

Python-verified (2026-04-21): L_max = 8 → 47,388 D_K eigenvalues; L_max = 10 → 155,984; ratio computation is deterministic given retraction ordering.

**11. What PASS/FAIL means for solution space**:
- **PASS** → the retraction of branch (iv) is numerically invisible at the W_0 output level; all W7 gates are safe to run under their current canonical input set; the three-solo convergence of W_0 holds post-retraction.
- **FAIL** → the retraction perturbs W_0 outputs enough to invalidate one or more W7 gates; all affected gates must re-dispatch with corrected inputs (escalation to S86 wave carry-forward).
- **INFO** → retraction perturbs but bounded; per-constant follow-up gates needed; no immediate wave-level re-dispatch.

**12. Effort**: ~3 h CPU (L_max = 8 cached; L_max = 10 partially cached) or ~1.5 h GPU.

**13. Substrate framing reminder**: branch (iv) was an identification of substrate structure that did not survive S84 W1 audit. The retraction removes a geometric-interpretation candidate, not a substrate reality. The L_max sweep tests numerical stability of the INTERNAL spectral truncation — it is NOT a scale-separation question about g_M. The W_0 branch-discriminator operates on D_K eigenvalue patterns, not on spacetime observables.

---

## Wave W7 → Wave W8 Decision Point

**W7 → W8 decision point**: Wave W8 is volovik-origin (superfluid-universe). W7 outputs that feed W8 volovik gates:
- W7-CUSP-BOGOLIUBOV (§W7-4) output β_k spectrum directly feeds W8 LEGGETT-VACUUM-70 (sub-leading Leggett tensor contribution to f_B closure) and W8 item #2 "Derive Convention A microscopically from BdG." If W7-CUSP FAILS, these W8 gates must wait on cusp reformulation.
- W7-K-CORRIDOR-MUKHANOV-VALIDITY (§W7-6) classification feeds W8 MUKHANOV-SASAKI-63 "Inflationary sub-corridor audit: reclassify W5 results with K ≥ K_crit." If W7-6 places K_crit in an unexpected location, W8 MUKHANOV-SASAKI-63 must re-dispatch with updated K_crit.
- W7-BASELINE-HTILDE-DERIVATION (§W7-1) H̃_DC feeds W8 item #7 "Verify K_R5 = 1.9222 = hull_lo is stable under L_max sweep" — the H̃ DC window and K_R5 are tied via the corridor picture.

**Decision rule**: if W7 PASS count ≥ 4 of 7, W8 proceeds on canonical inputs. If 2–3 PASS, W8 dispatches with per-gate waiver flags. If < 2 PASS, W8 is deferred to S86 pending W7 remediation.

**Non-blocker note**: W8 volovik gates that do NOT depend on W7 outputs (e.g., Lab-analog predictions for SU(3)-internal OP directions, K_FIRAS = S_IC^cap coincidence audit) proceed regardless of W7 status.

---

## Wave W7 Machinery-Enumeration Pin (PRDR §0.11 aggregate)

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, every gate-relevant parameter in W7 is enumerated here for PRU (Pre-Registration Underspecification) prevention.

| Gate | Parameter | Pin |
|:-----|:----------|:----|
| ALL | `L_max` | 10 (except W7-7 which runs {8, 10}) |
| ALL | `scheme` | per-gate (Zubarev for HTILDE & W0-RE-AUDIT; zeta-reg for CC-6; S37-Gamma-canonical for CC-Γ; transfer-matrix for CUSP; Chamseddine-Connes for DRESSED-VP; z-gauge Mukhanov for K-CORRIDOR) |
| ALL | `convention` | per-gate (see each §) |
| ALL | `random_seed` | 42 (any non-deterministic sample draws) |
| ALL | `GPU_path` | torch 2.9.1+rocm on AMD RX 9070 XT; OMP_NUM_THREADS=8 on CPU fallback |
| HTILDE | `N_eval` | 1024 η-samples log-spaced in [−1e5 M_KK⁻¹, −1e-2 M_KK⁻¹] |
| HTILDE | `scan_range` | H̃ ∈ [4.599e-3, 4.829e-3] |
| HTILDE | `step_size` | 1e-5 H̃ |
| HTILDE | `tolerance` | 0.91% log-DC; RATIO on F_stretch 0.5 OOM |
| CC-6 | `N_k` | 4096 log on [1e-4 M_KK, M_KK] |
| CC-6 | `UV_cutoff` | van-Hove-dispersion (NOT naïve M_KK) |
| CC-6 | `tolerance` | 1.0 OOM RATIO on ρ_Parker/Lambda_obs |
| CC-Γ | `Γ` | 0.99970 (canonical pin) |
| CC-Γ | `tolerance` | 15% RATIO on Ω_DM/Ω_DE |
| CUSP | `N_k` | 4096 log on [1e-4 M_KK, M_KK] |
| CUSP | `N_t` | 1e5 time-steps per mode |
| CUSP | `alpha_cusp` | 1.0 (2D van Hove; re-dispatch if W0 VAN-HOVE-CUSP-THEOREM lands on α ≠ 1) |
| CUSP | `tolerance` | ABSOLUTE 0.05 on fitted exponent around −0.6667 |
| DRESSED-VP | `N_phi_samples` | 1024 from S78 W1-E GGE density profile |
| DRESSED-VP | `cutoff_Lambda` | M_KK (Chamseddine-Connes canonical) |
| DRESSED-VP | `tolerance` | sign verdict + 50% RATIO perturbativity |
| K-CORRIDOR | `K_grid` | 64 log-spaced on [K_R5, K_crit + 0.5] = [1.9222, 3.0] |
| K-CORRIDOR | `tolerance` | VALID > 10; MARGINAL [1, 10]; BREAKDOWN < 1 |
| W0-RE-AUDIT | `N_constants` | 8+ (K_R5, K_substrate, K_crit, Γ, f_conv, c_sub_at_kpivot, F_amp_linearized, f_GGE_Leggett) |
| W0-RE-AUDIT | `tolerance` | 5% RATIO PASS; 15% RATIO FAIL |

No gate leaves a gate-relevant parameter unpinned. Dry-run enumeration applied.

---

## Wave W7 Input-SHA Ledger

Static SHA-256 pins required for every W7 script (computed at orchestrator-dispatch time; `<precomputed>` placeholders below become concrete at script execution):

| File | Gate(s) depending | SHA-256 |
|:-----|:------------------|:--------|
| `computations/canonical_constants.py` | ALL | `<computed-at-runtime>` |
| `computations/s52_spectral_triple_eigenvalues.npz` (L_max=10 D_K cache, 155,984 eigs) | DRESSED-VP, K-CORRIDOR, W0-RE-AUDIT | `<precomputed>` |
| `computations/s52_spectral_triple_eigenvalues_lmax8.npz` (L_max=8 D_K cache, 47,388 eigs) | W0-RE-AUDIT | `<precomputed>` |
| `computations/s67_transit_ps_67_output.npz` | CC-6, CUSP, K-CORRIDOR | `<precomputed>` |
| `computations/s78_w1e_prefold_vacuum_output.npz` | CC-6, CUSP, DRESSED-VP | `<precomputed>` |
| `computations/s80_unified_as_79_full_output.npz` | HTILDE, K-CORRIDOR | `<precomputed>` |
| `computations/s83_w1_g1_verdict.txt` (Zubarev canonical) | HTILDE, W0-RE-AUDIT | `<precomputed>` |
| `computations/s84_w1a_1_htilde_sensitivity_output.npz` | HTILDE | `<precomputed>` |
| `computations/s84_w1_branch_iv_retraction_record.md` | W0-RE-AUDIT | `<precomputed>` |
| `sessions/framework/permanent-results-registry.md` (Γ = 0.99970 pin) | CC-Γ | `<precomputed>` |

Closure hash per gate = SHA-256 of the ordered input-pin map, per the canonical S81+ verdict-line format (see `.claude/rules/gate-verdicts.md`): `{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> sha256=<closure>`.

---

## Wave W7 Substrate-Framing Global Checklist

Per `.claude/rules/phononic-framing.md`, every W7 script's output file and verdict must:
1. Frame the computation as a SUBSTRATE-INTERNAL operation (D_K eigenvalue moment, Jensen-parameter transit, phononic GGE density).
2. NOT import GR-coordinate vocabulary ("inflaton," "Hubble rate of expansion through space," "slow-roll," "reheating") without flagging as "emergent translation from substrate."
3. NOT treat c as a speed-limit on substrate-internal dynamics (Mach 13.75, fold transit, Jensen evolution are substrate-native and NOT subject to c).
4. Flow the explanation substrate → emergent, never GR → substrate.

Violations of this checklist trigger a Stage-3 prohibited-action flag under `.claude/rules/v3-closure-recovery.md`.

---

**End of Wave W7 Plan.**
