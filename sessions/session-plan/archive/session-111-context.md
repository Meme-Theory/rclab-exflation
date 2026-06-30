# Session-111 — Plan Context (deduplicated carry-forward scope)

**Session:** 111.  **Prior:** 110.  **Mode:** fanout, COMPUTE (+ Stage-1/Stage-2 registration gates).
**Built by:** `/rclab-plan --session 111` (2026-06-21) from the S110 per-wave WP `## Carry-Forward Computations` blocks (`session-110-w{2,3,4}-workingpaper.md`) + the 8 W1 workshop Wrap-Ups (`session-110/workshops/*.md` + `session-110-connes-mack-workshop.md`) + the housekeeping mirror (`session-110-housekeeping.md`). Deduplicated; canonical scope for every per-wave planner.
**Theme:** harvest the S110 M_KK-keystone session — the a(t)/Friedmann Tier-1 #1 spine (FORM now MONOTONE-robust ⇒ residual = M_KK magnitude + clock-triple), the M_KK-DERIVATION τ-RG-invariance decider, the fermion-mass/Yukawa relocation, and the compact-object / Floquet / Stage-2 cohort.

> **Planner rule:** This file is your authoritative scope. Do NOT read `session-110-plan-*.md` or individual S110 synthesis files (too large; watchdog-stall risk). Query the `knowledge` MCP directly for prior verdicts / constants. Every npz input named below is on disk under `computations/session-110/` or as cited.

---

## Source manifest + dedup record

| CF (S111 gate ID) | Source(s) | Convergence | Reviewer origin |
|:--|:--|:--|:--|
| S111-CF-AS3 | W2 WP + WS-AS-1 (CF-AS-3) | 2 (merged) | transit-dynamics / lizzi |
| S111-CF-YUK-FULLFLAVOR | W3 WP | 1 | connes / van-den-dungen |
| S111-CF-B5A-ISLAND | W4 WP | 1 | hawking |
| S111-CF-CO34A-12D-BUBBLE | W4 WP | 1 | schwarzschild-penrose |
| S111-CF-CO34B-LRDT | W4 WP (sharpened by connes-mack WS) | 1 | mack |
| S111-CF3-H0-RESIDUAL | W4 WP (sharpened by connes-mack WS; volovik a₀-audit) | 1 | mack / volovik |
| S111-CF-VIICE-NW | W4 WP | 1 | volovik / einstein |
| S111-CF-MKK-RG-INVARIANCE | WS-CC-H₀ | 1 | einstein / volovik |
| S111-CF-CLOCKLOC1-CED | WS-CLOCKLOC CF-1 | 1 | hawking + schwarzschild-penrose |
| S111-CF-CLOCKLOC2-MONOTONE | WS-CLOCKLOC CF-2 | 1 | schwarzschild-penrose |
| S111-CF-CLOCKLOC3-R16EPS | WS-CLOCKLOC CF-3 (Stage-1) | 1 | schwarzschild-penrose + hawking |
| S111-CF-CLOCKLOC4-UNIQUE | WS-CLOCKLOC CF-4 (low priority) | 1 | schwarzschild-penrose |
| S111-CF-NOHOLOFLUX | WS-ATFORM (Stage-1) | 1 | gen / connes |
| S111-CF-TAUCUSP | WS-ATFORM | 1 | transit-dynamics / lizzi |
| S111-CF-FLOQUET1..4 | WS-FLOQUET | 1 each | transit-dynamics / berry |
| S111-CF-WEINBERG-C2COSET | WS-C2COSET | 1 | baptista / connes |
| S111-CF-YUK-C2COSET-CONFIRM | WS-C2COSET (= S110-CF1-YUK-C2COSET down-tiered) | 1 | baptista / van-den-dungen |
| S111-CF-M1-INTERTWINER | WS-M1-INTERTWINER | 1 | van-den-dungen + connes |
| S111-CF-KSIGN-PARITY-STAGE2 | connes-mack WS (§VII.CF Stage-1 landed S110) | 1 | NON-AUTHORS: lizzi/vdd + volovik/transit |

**Closed, NOT carried (verified):** CF-AS-2 (exit-filter greybody) — RAN in S110 as `S110-CF-AS2-GREYBODY` FAIL (bounded-but-filter-fitted; floor permanent). WS-CO-1 CF-CO-2 — closed-not-run (STERILE-confirmed). WS-SA-FREE-ENERGY — collapsed (CCDARK-2 Reading-A). DMAB-REFINE — 3 legs settled INFO. The connes-mack WS produced NO new single-observable CF (it SHARPENED the two existing W4 CFs — folded into their gate specs below).

**Register-sourced standing gaps (high-leverage, NO tractable pre-registrable gate this session — recorded, NOT wave gates):** atlas-04 C2 K_pivot (the single largest observational gap); 170× DM mass-anchor (HARDENED-OPEN); τ_fold-RELAXATION (corridors dead S95); M8(c) external-likelihood layer; DESI-WZ-LENSING-BIAS / branch-iv (~2027 DR3). Register-semantics HOLD: HK-SA-RETAG (atlas-04 S3 retag) — Q2 status-tag adjudication, housekeeping §B.W1, not a compute gate. Phase 1c-REGISTERS.CONSUME confirmed no additional tractable register candidate beyond the 22 CFs below.

---

## WAVE 1 — a(t) / clock theorems (Tier-1 #1 spine; planner: hawking-theorist)

The a(t)/effective-Friedmann FORM is now MONOTONE-robust (S110 WS-ATFORM); the §6.3 residual is {M_KK magnitude (→ W2) + the clock-triple well-posedness (this wave)}. All from WS-CLOCKLOC + WS-ATFORM.

### S111-CF-CLOCKLOC1-CED — (C,E,D)-triple self-consistency in the substrate-natural frame [PRIME a(t) backbone]
- **What:** Compute the self-consistency of the minisuperspace triple `(C) 3M_P²H² = ½σ̇²+(5/2)τ̇²+V`, `(E) τ̈ = −3Hτ̇ − (1/5)dV/dτ`, `(D) t_internal := ∫dτ/τ̇, H = τ̇·d ln a/dτ` in the substrate-natural frame (τ = Jensen modulus). Feed σ²=5τ̇² and V_spec into (C)→H(τ); feed H into (E)→evolve τ; verify (D) closes (the `Λ=3H²` / `c_track=3` de Sitter relation is the (C)∧(D) consistency at the fixed point).
- **Inputs:** S19b homogeneous-sector action (`H² = (1/(3M_P²))[½σ̇²+(5/2)τ̇²+V]`, `τ̈=−3Hτ̇−(1/5)V'`); σ²=5τ̇² (INV4-W2-2); V_spec(τ) (S24a `closed_79`/`closed_170`); `c_track=3` (INV4-W3-1); transit-corridor τ-grid τ∈[0,0.19] (from CLOCKLOC2).
- **Gate:** PASS iff the triple closes with `|residual|<1e-6` on the de Sitter fixed-point `Λ−3H²=0` AND (D) is well-posed (τ̇≠0 throughout). INFO iff closes but (D)-well-posedness is corridor-boundary-sensitive. FAIL iff no substrate-natural frame closes it. Zero free params once σ²=5τ̇² and V_spec pinned.
- **Effort:** Medium (ODE-integration + fixed-point check; inputs pinned). Executor: hawking-theorist + schwarzschild-penrose cross-check on (D)-well-posedness.
- **PRDR note (housekeeping §D / ws-clockloc):** the PIN MAP MUST carry (a) a `V_spec monotone` same-object declaration (the a₄ minisuperspace operator IS the V_spec potential sign, dominated) and (b) a **Level-2-clock tag** (the advancing clock is the τ Level-2 Jensen-modulus coordinate, NOT an a₀/a₂/a₄ grade) — prevents re-import of the grade-primacy conflation WS-CLOCKLOC dissolved.

### S111-CF-CLOCKLOC2-MONOTONE — deparametrization monotonicity corridor (the τ-window τ̇≠0) [feeds CLOCKLOC1]
- **What:** Compute the upper τ-bound below which the Level-2 clock τ is strictly monotone (τ̇≠0), i.e. the corridor on which (D) is well-posed. Locate the first clock turning point above the fold; confirm [0,0.19] is interior to it.
- **Inputs:** S19b EOM `τ̈=−3Hτ̇−(1/5)V'`; the modulus-space turning-point map (OVERSHOOT TURNAROUND τ=1.614, S77; tau_NEC=1.382); `dS/dτ=+58,673` one-signed; `N_zeros=1` (S96-GEOM-PENROSE-2CONE).
- **Gate:** PASS iff τ̇>0 on a connected corridor containing [0,0.19], first zero at τ_turn (report τ_turn). INFO iff monotone on [0,0.19] but upper bound scheme-sensitive. FAIL iff a turning point inside [0,0.19] (would break the single-asymmetric-open Penrose diagram).
- **Effort:** Low (turning-point root-find on pinned EOM; the map brackets the answer 0.19–1.614). Executor: schwarzschild-penrose-geometer. Feeds CLOCKLOC1's corridor scoping.

### S111-CF-CLOCKLOC3-R16EPS — r=16ε-inapplicability as a layer-obstruction theorem (STAGE-1-CANDIDATE registration)
- **What:** Formalize + register (STAGE-1-CANDIDATE via `joint-theorem-promotion.md`) the structural no-go: a Level-2 deformation parameter cannot enter a Level-1 single-field consistency relation, so `r=16ε` has no substrate image. State as: no Level-1 functional `ε[φ]` exists (φ a config-space field carrying the H-rate) because the H-rate's clock is the Level-2 modulus τ (a moduli-space coordinate, not a section over g_M).
- **Inputs:** the Level-1/Level-2 distinction (`phononic-framing.md §"Single-τ-slice vs moduli-deformation"`); the 5-argument VdD-Hawking `r=16ε` inapplicability (existing); the (C,E,D)-triple layer reading (WS-CLOCKLOC EMERGENCE-2/3).
- **Gate:** PASS (Stage-1 registration) iff stated as a clause-structured theorem with explicit Level-1 vs Level-2 typing AND a declaration of distinctness from the 5 existing arguments (6th independent argument, or the structural ROOT subsuming them? — the distinctness declaration is the load-bearing pre-registration). Stage-2 = separate later gate (causal-structure + semiclassical-gravity axes).
- **Effort:** Medium (structural-theorem write-up + registration). Executor: schwarzschild-penrose-geometer + hawking-theorist.

### S111-CF-CLOCKLOC4-UNIQUE — substrate-natural-clock uniqueness [lower priority]
- **What:** Determine whether τ = Jensen modulus is the UNIQUE substrate-natural deparametrization clock, or one of a class of monotone substrate-intrinsic functions (a₄-monotone `|C|²(τ)`, a₀(τ)) preserving `Λ=3H²` under relabeling. Compute the reparametrization class `t→g(t)` over which `Λ=3H²` is frame-invariant; check whether a second substrate-monotone function lands in it.
- **Inputs:** the reparam-invariance check `Λ−3H_t²=Λ(1−g'²)` (WS-CLOCKLOC R3); the monotone substrate functions `|C|²(τ)` (S96-GEOM-CCC-WEYL), a₀(τ), `dS/dτ` (Jensen); `c_track=3`.
- **Gate:** PASS (UNIQUE) iff τ is the only substrate-intrinsic monotone clock preserving `Λ=3H²` without extra structure. INFO (UNIQUE-UP-TO-CLASS) iff a class preserves it and ≥2 substrate-monotone functions land in it. FAIL iff frame-invariant only for τ exactly (g'=1 only), making "substrate-natural" degenerate.
- **Effort:** Low-medium (Sage reparam-class compute + a check of substrate-monotone functions). Executor: schwarzschild-penrose-geometer (Sage cross-check). Orthogonal to CLOCKLOC1/2 (does not gate them).

### S111-CF-NOHOLOFLUX — spectral-triple-no-holonomy-flux root (STAGE-1-CANDIDATE registration)
- **What:** Register (STAGE-1-CANDIDATE via `joint-theorem-promotion.md`) the unified inadmissibility root — "a spectral triple `(A_K,H_K,D_K(τ))` has no holonomy-flux sector, hence no matter-sector bounce density by construction; the operator/parameter/causal inadmissibility grounds are three projections of this single quantization-framework fact" — Stage-0 text frozen in WS-ATFORM CONVERGENCE-3 + EMERGENCE-1; distinct from + citing the S85 τ_fold van-Hove-cusp PERMANENT theorem.
- **Inputs:** WS-ATFORM frozen Stage-0 text (CONVERGENCE-3 three-projection chain; einstein EMERGENCE-1; L1/L2 conjugate-pair + dimensional-type arguments); `joint-theorem-promotion.md` Stage-1 protocol; next-free §VII registry slot per `regulator-pin-discipline.md` next-free-letter.
- **Gate:** Stage-1 PASS iff registry entry written with all clauses + joint-clause flags + cross-axis author attribution (lqg-side: conjugate-pair/dimensional-type; einstein-side: principle-theoretic/equivalence-principle). Stage-2 = SEPARATE S112+ dual-dispatch (NCG-axiomatic + cosmological-bridge non-authors).
- **Effort:** ~0.3 wave Stage-1 registration. Executor: gen-physicist or connes-ncg-theorist.

### S111-CF-TAUCUSP — τ-cusp observable asymmetry (conjugate-pair split's positive falsifiable content)
- **What:** Compute whether the τ-sector van Hove cusp at τ_fold=0.190 leaves a distinct spectral-tilt signature in the GGE-relic running/tilt structure, separable from the smooth monotone-ramp matter sector — operationalizing the predicted asymmetry "bounded structure in spectral-complexity observables (n_s/α_s), absent in expansion-history observables (no bounce)."
- **Inputs:** the τ_fold DOS-divergence structure (S85 van-Hove-cusp theorem, `s85_w0_van_hove_cusp_theorem.py`); the GGE-relic spectral imprint (`n_s=0.9561`; substrate-distance running `α_s=−0.08587279` via Mellin residue s=3, `canonical_constants.py`); the monotone-ramp matter-sector `dH²/dρ=+8πG_eff/3` (WS-ATFORM gap-as-ceiling reduction).
- **Gate:** PASS = a feature in running/tilt attributable specifically to the DOS divergence at τ_fold, magnitude exceeding the smooth-ramp baseline by a pre-registered threshold AND a detector axis (CMB-S4 / CMB-HD tilt/running sensitivity). FAIL = the τ-cusp leaves no separable tilt signature (observationally sterile, like the matter-sector no-bounce). INFO = signature present but below detector horizon.
- **Effort:** ~1 wave (substrate-IS spectral-tilt compute, no new infrastructure). Executor: transit-dynamics-theorist or lizzi-spectral-functional-theorist.

---

## WAVE 2 — M_KK keystone + H-sector + CC (Tier-1 #2 / Tier-2 M_KK-DERIVATION; planner: volovik-superfluid-universe-theorist)

### S111-CF-MKK-RG-INVARIANCE — M_KK τ-RG-invariant-transmutation-scale vs bare-import discriminator [PRIME Topic-1 decider]
- **What:** Determine whether `w = M_KK` admits a τ-RG-invariant dimensional-transmutation origin. Construct `Λ_eff(τ)·exp(−1/(λ_eff(τ)·N₀(τ)))` from the Jensen-deformed D_K(τ) spectrum and test whether it is τ-INVARIANT (a single dimensionful M_KK independent of the modulus-flow evaluation point, the Λ_QCD-analog μ-independence) OR whether the only dimensionful scale enters through an external cutoff (a `w`-import). Audit-log EVERY scale-import; the discriminator is dimension-of-output + presence/absence of an external cutoff.
- **Inputs:** `D_K(τ)` Jensen-deformed spectrum over τ∈[0.190,0.6] (`s84_spectrum_cache_L12_tau019.npz` + τ-scan; `λ_eff(τ),N₀(τ)` read off each slice — BCS coupling + DOS as functions of τ, NOT fixed-τ_fold); `S110-CF-CV2A` output (`M_KK/M_Pl = exp(−1/(λ_eff·N₀))`, the dimensionLESS ratio whose τ-running is tested — on disk `s110_cf_cv2a_mkk_transmut_promote.npz`); `canonical_constants.py`: `M_KK_gravity=7.428660036284456e16` (CONST-FREEZE-42, must be reproduced INDEPENDENTLY to count as dynamical), `M_Pl_reduced=2.435e18` (CODATA, must be ABSENT for PASS), `gap_factor=4.266426` (finite-L pole no-go); §VII.BS NNU rank-1 theorem (`O=w·Ô`).
- **Gate:** τ-RG-invariance of `Λ_eff(τ)·exp(−1/(λ_eff(τ)N₀(τ)))` — relative spread across the τ-scan < pre-registered band (e.g. 5e-2 mirroring the CAC convergence band) ⟹ DYNAMICAL (PASS, Reading-B-residual survives); spread NOT convergent OR the only dimensionful scale traces to a CODATA-unit cutoff ⟹ BARE-IMPORT (FAIL, constructive-O3 confirmed).
- **Effort:** Medium (τ-scan of λ_eff(τ),N₀(τ) off D_K(τ); bottom-K DOS L_max-saturated at L=12 per Friedrich-Bär ⇒ feasible). GATED ON `S110-CF-CV2A` (landed; ratio on disk). Executor: nazarewicz-nuclear-structure-theorist (BCS-transmutation machinery, continuity with CV2A) framed by the volovik/einstein M_KK-origin question.

### S111-CF3-H0-RESIDUAL — residual H₀-relief channel beyond the a₂ τ-clock [dimensionless-Ô layer; ∥ MKK-RG, independent axis]
- **What:** The a₂ focusing-clock relief, transported via deg(T)=+2, lands PARTIAL (S110 CF3 INFO, 6.125% of the shift, below the ~9% band). Compute the residual relief from the a₀-orthogonal channel (w0_FW=−0.918) and/or a refined transport; test whether the substrate closes the FULL `ΔH₀/H₀ ∈ [0.08,0.10]` with zero fitted knobs.
- **Inputs:** `inv7_w1_4_kbc_timescape_h0.npz` (clock_coeff=−3.08); `s110_cf3_timescape_h0.npz` (partial transported relief); w0_FW=−0.918.
- **Gate:** `ΔH₀/H₀ ∈ [0.08,0.10]` PASS (full close) / partial INFO. **SHARPENED (connes-mack WS):** `ΔH₀/H₀` is `d_A=0`, so its transport CANNOT invoke the 54.04-dec scale leg (the +2 full-homogeneity reading is dimensionally INADMISSIBLE). Restrict the residual-relief search to **dimensionless-morphism channels** (the a₂ focusing-clock 6.125% + any a₀⊥a₂ dimensionless RELATION); **pre-register the partial-relief fraction `49/800=6.125%` as the honest outcome (~94% held)** and route the residual to the **dimensionless-slot**. Correct PASS criterion: a substrate-derived dimensionless RELATION predicting the shift once `w=M_KK` is fixed by one observation.
- **Layer-scope (volovik a₀-orthogonality audit, `session-110-volovik-cf3-a0-orthogonality-audit.md`):** the a₀ "draw" is licensed at the **dimensionless-Ô layer ONLY** (a₀⊥a₂ standing fact, FUNCTIONAL-INDEPENDENT S66 / W2-E PASS S75); it refines a₀/a₂ Ô-*relations*, it does NOT draw a dimensionful relief budget out of a₀ (the workshop-killed O2 / Layer-1 wall — "a dimensionless ratio cannot close a dimensional gap"). **NOT gated on** S111-CF-MKK-RG-INVARIANCE (independent axis; may proceed in parallel).
- **Effort:** ~1 wave. Executor: mack-cosmic-bridge (H₀/observational) + volovik (a₀-orthogonality cross-check). Interlocks with MKK-RG-INVARIANCE.

### S111-CF-AS3 — A_s number/band pin + all-frozen-superhorizon regime resolution (= WS-AS-1 CF-AS-3; convergence 2)
- **What:** Pin the TRANSIT-PS-67 amplitude A_s (number + band) from the impulse-quench `|β_k|²` functional, resolving the all-frozen-superhorizon regime (S110 B1 INFO regime=MARGINAL: 89/89 frozen, WKB-Bogoliubov leg empty), and decide the magnitude epistemic type per the WS-AS-1 Reading-A-conditional Friedrich-Bär-temp PASS. **DECISIVE SUB-COMPUTE:** the nazarewicz FB-temp per-sector test — does `λ_pivot=−ln(n_pivot/(1−n_pivot))` shift when a NEW high-Casimir in-band (p,q) sector is added at L_max+1, holding n_pivot fixed? Register prediction: NO (per-charge multiplier) ⟹ POINT.
- **Inputs:** `inv10_w2_transit_ps_build.npz` (locked {β_k}); `s110_cf_b1_transit_ps_promote.npz` (two-leaf build); the WS-AS-1 verdict; `inv5_w2_1_*.npz`, `inv6_w2_2_*.npz`; falsifier Row 8 (5.078e-9 TD-canonical); k_pivot, deg(T)=+2; `s84_spectrum_cache_L12_tau019.npz` (FB-temp per-sector eigenvalue-floor test); GGE `λ_k=−ln(n_k/(1−n_k))` (S38/S39); Friedrich-Bär `η_FB(p,q)` predicate (S87 W11-2/3).
- **Gate:** PASS iff one defensible impulse-quench A_s magnitude lands (a POINT if FB-temp PASS ⟹ verdict-(A) physical-d.o.f.; a BAND if FB-temp FAIL ⟹ verdict-(B) L_max-soft) with scheme-tag + OOM-distance + the FB-temp per-sector verdict; regime resolved; the row keeps SCHEME-DEPENDENT for the magnitude + adds the FI/PERMANENT floor sub-annotation. Canonical write-order (verdict → canonical_constants → inventory Row 8 via mack, sole writer).
- **Effort:** ~0.3 wave (mechanical promotion) + the FB-temp per-sector compute (~0.3 wave). Executor: transit-dynamics-theorist (impulse-quench) + nazarewicz-nuclear-structure-theorist (FB-temp per-sector sub-compute — the planner MAY split into AS3a/AS3b).

### S111-CF-VIICE-NW — derive the n-occupation ↔ w-EoS dictionary (sharpen §VII.CE)
- **What:** §VII.CE clause-(a) PASSed on the perfect-square form + sign, but the substitution `(n₁−n₂) ↔ (w₁−w₂)` (band occupations ↔ two-fluid EoS) is author-side, recorded INFO-not-falsified. Derive the dictionary from first principles (relic occupation → effective barotropic w map) so the now-PERMANENT §VII.CE rests on a substrate-derived, not stipulated, identification.
- **Inputs:** `inv12_w3_3_back_reaction_closure_hsq.npz`; the relic-occupation → ρ_i(a) dilution chain; §VII.CE registry entry.
- **Gate:** the n↔w map is substrate-derived (THEOREM/exact) PASS; numerical-correspondence-only INFO.
- **Effort:** ~1 wave. Executor: volovik-superfluid-universe-theorist (two-fluid EoS / relic occupation) + einstein cross-check.

---

## WAVE 3 — fermion-mass / Yukawa / NCG-categorical (Tier-2 #9b; planner: connes-ncg-theorist)

### S111-CF-YUK-FULLFLAVOR — full-flavor Yukawa magnitude (down-sector + CKM + same-gen J-conjugacy lock)
- **What:** Extend the S110 CF2-YUK-EPSLX up-sector INFO (mass_grp 2/6) to the full flavor sector — the 4 held-out slots (3 same-generation ratios J-conjugacy-locked to ≈1 by Λ_u=Λ_d, + the down-only m_s/m_d) structurally unaddressed by an up-sector texture; develop the down-sector ε_LX texture + the CKM angles.
- **Inputs:** `s110_cf2_yuk_epslx.npz` (the up-sector pairing-dependent {ρ13,ρ23} texture); the J-conjugacy lock structure; PDG down-sector + CKM targets.
- **Gate:** mass_grp ≥ 5/6 (down-sector ratios in-band + the same-gen lock resolved or its origin pinned); pre-register the band.
- **Effort:** ~1–2 waves (up-sector machinery exists; new work = down-sector + CKM d.o.f. + resolving the J-conjugacy lock). Executor: connes-ncg-theorist (§VII.BL multiplicity-bundle / Yukawa) + baptista/van-den-dungen support.

### S111-CF-WEINBERG-C2COSET — off-Jensen Weinberg-angle / a₂-response sensitivity [the productive C²-coset relocation; prime candidate]
- **What:** Compute the response SLOPE `d(sin²θ_W)/dδ_C²|_0` and `d(a₂)/dδ_C²|_0` under the T4 (C²-split) left-invariant deformation `L3·I_4→diag(...)` on `C2_IDX=[3,4,5,6]` at the fold τ-anchor; `sin²θ_W(δ_C²)=3L2/(L1+3L2)`, `a₂` the G_N-feeding Seeley-DeWitt coefficient. NEW observable (response derivative on the irrep-leg spectrum), distinct from INV12-W2-1's a₂-additivity-leak BOUND.
- **Inputs:** `dirac_spectrum.py` (D_K builder); `inv2_w1_off_u2_dirac_yukawa.py` (deformed-split-metric machinery, swap to C²-block sensitivity); `s84_spectrum_cache_L12_tau019.npz`; canonical `J_C2=0.933`, `J_su2=0.059` (`canonical_constants.py:732-733`), `tau_fold=0.19` (CONST-FREEZE-42); INV12-W2-1 npz (`‖T‖²=7.81e-4` off-Jensen at δ=0.05).
- **Gate:** PASS iff `|d(sin²θ_W)/dδ_C²|_0| > eps_sens` (pre-register `eps_sens` at plan-freeze) with sign matching the L2/(L1+3L2) substitution chain; INFO if sub-threshold. Pre-register the algebra-INVARIANT / **FI tag** per `regulator-pin-discipline.md §"β_shell FI Classification"` (a₂-ratio is FI, parented to the F_traj a₂-ratio FI theorem at locked-norm L_k=1). Output `d(sin²θ_W)/dδ_C²|_0` ± regime tag + `d(a₂)/dδ_C²|_0`; npz + png. Format `computations/session-111/s111_weinberg_c2coset_offjensen.py`.
- **Effort:** MED (a sensitivity probe; not a discriminator on a permanent theorem). Executor: baptista-spacetime-analyst (Jensen/O'Neill geometry) or connes-ncg-theorist (spectral-action a₂). Declare distinct-from-INV12-W2-1 (response SLOPE, not additivity-leak bound) at plan-freeze.

### S111-CF-YUK-C2COSET-CONFIRM — C²-coset Yukawa-rank confirmation witness (= S110-CF1-YUK-C2COSET, down-tiered)
- **What:** Build the T4 C²-coset anisotropy modulus (split `L3·I_4→diag` on `C2_IDX=[3,4,5,6]`, `J_C2=0.9330 M_KK`, transverse to U(2)) via `inv2_w1_off_u2_dirac_yukawa.py` (swap the split block su(2)→C²); re-run the off-U(2) Dirac + Yukawa-overlap on the d=2 generation multiplet. **A confirmation-when-convenient numerical witness, NOT a live discriminator** — converts "C²-coset is the surviving open seam" → "closed like every other internal modulus."
- **Inputs:** `inv2_w1_off_u2_dirac_yukawa.py` (deformed-split-metric + Y_ij(δ)); `dirac_spectrum.py`; canonical `tau_fold=0.19`, `L3=e^τ`, `J_C2=0.933`; INV2-W1-1 su(2)-split-null baseline (audit `1481b775…`).
- **Gate (PRE-REGISTERED dual prior ~0.90 FAIL / ~0.10 PASS):** `|dY_12/dδ|_0 > eps_lift=1e-3` AND `rank(Y_ij) 1→≥2` for δ∈(0,0.20]. **FAIL → 0.95 Track B** (confirms §VII.BL on C²-coset; rank-1 wall off-ALL-internal-moduli; hierarchy PINNED to external ε_LX). **PASS → 0.90 Track A AND a flagged §VII.BL Stage-2 CONTRADICTION** (counterexample to a STAGE-3-PERMANENT theorem → Stage-2 re-audit, NOT a quiet "Reading A wins"). **INFO → unchanged, route to higher L_max.** Output `dY_12/dδ|_0`, `rank(Y_ij)`, `gen_degen_lift` (bool); npz + png. Format `computations/session-111/s111_yuk_c2coset_confirm.py` (folds into the same wave as YUK-FULLFLAVOR; no standalone dispatch overhead).
- **Effort:** MED-LOW (run when a Yukawa-sector compute wave is already open; do NOT lead a session with it). Executor: baptista-spacetime-analyst or van-den-dungen-bridge-theorist.

### S111-CF-M1-INTERTWINER — categorical construct-or-obstruct proof for the M1 intertwiner [HIGH effort; two-conjunct]
- **What:** NAME a NON-ACM vertically-elliptic symbol `σ_v` on the U(2)-fibre of SU(3)→CP² that simultaneously (i) SELECTS exactly `ker(ι_*)=M₃(ℂ)` AND (ii) carries a NON-trivial integrated K-homology class — OR prove the categorical obstruction theorem closing BOTH conjuncts at once (the vertically-elliptic-symbol non-existence theorem on the U(2)-fibre). Sub-targets: conjunct (ii) [the image — extend Axis-1's one-bridge `(0,0,0)` to the all-bridge-maps statement that every K-natural bridge sends the M₃-generator of `K⁰(A_K)=ℤ³` to zero]; conjunct (i) [the selection-by-deletion — extend Axis-2's ACM-route foreclosure to all SU(3)→CP² C*-algebra-homomorphism constructions].
- **Inputs:** gate S93-W2-1 `[φ_cd]=(0,0,0)` (Axis-1 one-bridge anchor); `05_2014_van_den_Dungen_Globally_Non_Trivial_ACM.md` (1405.5368; Axis-2 ACM-route foreclosure); `01_2018_van_den_Dungen_..._Riemannian_submersions.md` (1811.07824, Thm 3.4 + vertical-ellipticity def); `dirac_spectrum.py` lines 102-108 (`u(1)⊕su(2)⊕C²` split, `U2_IDX=[0,1,2,7]`/`M_IDX=[3,4,5,6]`); registry §VII.W-3 (two-axis obstruction record); `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"`.
- **Gate:** PASS = an explicit `σ_v` threading both conjuncts is exhibited + machine-checked (⇒ LBA-5 DISCHARGES, re-opens HK-N37) — OR the categorical two-conjunct obstruction theorem is proven (⇒ (c) upgrades to "categorically obstructed for all bridge maps," LBA-5 permanently undischargeable as a THEOREM). FAIL/INFO = neither closes; verdict stays "Reading B on two decidable axes," CF re-propagates. PRIOR (not pre-judgment): categorical obstruction lands.
- **Effort:** HIGH (constructive Kasparov-product / KK-theory compute on the SU(3)→CP² U(2)-fibre; multi-wave). Executor: van-den-dungen-bridge-theorist (conjunct (i)/Axis-2 categorical) + connes-ncg-theorist (conjunct (ii)/Axis-1 categorical) JOINT, axes pre-assigned.

---

## WAVE 4 — compact-object / black-hole (Tier-2/3; planner: schwarzschild-penrose-geometer)

### S111-CF-B5A-ISLAND — boundary-island microstate count vs A/4
- **What:** Compute the QES/island-construction boundary entropy `S_island` on the white-hole exit slice; test `|S_island/(A_horizon_FW/4) − 1| ≤ 0.10` — the deeper microstate construction the naive boundary-edge-mode count FAILed (S110 B5A magnitude FAIL: count ≠ A/4).
- **Inputs:** `inv4_w1_euclidean_replica.npz` (a₂-conical 1/4, c_conical=0.25); `s84_spectrum_cache_L12_tau019.npz`; `A_horizon_FW=71226.26338976152`; inv-4 W1-1 bulk-charge null (2.86 OOM undercount).
- **Gate:** `|S_island/(A/4) − 1| ≤ 0.10` PASS / ≤0.25 INFO / >0.25 FAIL (RATIO).
- **Effort:** ~1–2 waves (QES extremization on the L12 exit-slice spectral triple). Executor: hawking-theorist (QES/island/black-hole).

### S111-CF-CO34A-12D-BUBBLE — full-12D Gregory-Laflamme bubble maturation
- **What:** Lift the reduced (4+8) τ̇²-gated GL growth (N_efold=0.232 sub-critical) to the full 12D acoustic-metric perturbation; recompute `N_efold = ∫ growth_rate dτ` over the transit window — test whether mode-coupling the dropped sectors reaches the 1-e-fold permanent-structure threshold.
- **Inputs:** `inv4_w2_gregory_laflamme_dynamical.npz` (min ω²_eff=−44.26 M_KK²); S95 white-hole transit kinematics (Mach 13.75); L12 cache / 90 Peter-Weyl sectors.
- **Gate:** `N_efold ≥ 1` PASS (matures) / `<1` INFO (transient).
- **Effort:** ~1–2 waves (12D eigenproblem heavy). Executor: schwarzschild-penrose-geometer (GL / exact-solutions).

### S111-CF-CO34B-LRDT — correct transport degree for the LRD photosphere temperature
- **What:** `deg(T_{BZ→pivot})=+2` OVERSHOOTS for temperature (T_pivot=2.95e-79 K, ~80 OOM below the 3500–6500 K LRD band). Derive the substrate-natural transport DEGREE/kernel proper to the temperature channel and re-test T_pivot ∈ [3500,6500] K.
- **Inputs:** `inv7_w2_2_substrate_photosphere_temperature.npz` (T_bare=3.55e29 K, fold-robust 0.69%); `s110_cf_cv6b_ds_m4.npz` (deg_T=2.0); per-observable transport-degree taxonomy (`cross-pillar-bridge-corpus.md §23`).
- **Gate:** `T_pivot ∈ [3500,6500] K` PASS via a substrate-natural (non-fitted) transport degree. **SHARPENED (connes-mack WS §23.0(5) parity selection rule):** T's substrate-natural degree IS DERIVED as `d_A=+1` (the `M_KK^1` scale leg), NOT a free search — **pin deg=+1 a priori and verify, not scan**. Pre-register the **κ-sign-consistency predicate**: "∃ a substrate-natural transport with `deg(B)=d_A=+1` AND a `|κ|>1` morphism leg?" — expected **FALSE** by the κ-sign∧parity theorem (the deg=+1 residual is a +28.17-dec ASCENT requiring `|κ|>1`; eff deg 0.4787 is non-integer AND sub-scalar). Gate routes to **dimensionful-slot-collision ∧ sign-lock (HELD/INFO)**, NOT a fitted knob. The CF's real open compute: whether ANY substrate-natural object supplies an ascending morphism without a fitted dial (theorem says no — falsifiable pre-registration; LRD-T is a DIRECT JWST measurement with no relocation channel ⇒ held-ness is falsifier-grade).
- **Effort:** ~1 wave. Executor: mack-cosmic-bridge (transport-degree + LRD) + little-red-dots-jwst-analyst (JWST band) cross-check.

---

## WAVE 5 — Floquet confirmatory + Stage-2 verify (planner: transit-dynamics-theorist)

The 4 Floquet CFs are CONFIRMATORY or FORWARD-EXTENDING — NONE gates the §VII.BP DEAD verdict (already pinned by `max|Tr M|<2`, the depth derivation, and the 84× threshold).

### S111-CF-FLOQUET1 — per-mode monodromy print at the single most-at-risk mode (Q-B closeout) [trivial, confirmatory]
- **What:** Extract the stored `Tr M(A=0.965, q_M=0.965·8.3e-4/2=4.005e-4)` scalar from the inv-12 W3-2 npz; confirm individually `∈ (−2,2)` and matches the analytic `+1.98756 ± O(5e-6)`. Converts the aggregate `max|Tr M|=1.99999` bound into a per-mode certificate at the smallest detuning-to-half-width point.
- **Inputs:** inv-12 W3-2 npz (`Re_mu_relic`/`tr_relic` arrays + relic `A_relic` grid; locate the A=0.965 mode); `h_par=8.3e-4` (S101-W1-QEQ-RELIC-ODDFLOOR pin); analytic prediction `+1.98756`.
- **Gate:** `|Tr M_stored − 1.98756| < 1e-3` AND `|Tr M_stored| < 2` (RATIO + ABSOLUTE). NON-verdict-gating (confirmatory).
- **[plan-w5 PRDR correction, supersedes the workshop value]:** the npz GROUND TRUTH is `tr_relic[i_closest] = −1.9969618432` (SIGN and value differ from the workshop's analytic `+1.98756`). Per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift, plan-w5 pins the runtime value (`value='...drift_corrected_from_+1.98756_to_-1.9969618432...'`) and reformulates the gate to the magnitude comparison `|Tr M_stored| < 2` (= 1.99696, strict-interior, gap 3.038e-3) — the sign-sensitive `|x−1.98756|<1e-3` would spuriously FAIL on the drift, not on physics. The plan-w5 block is authoritative.
- **Effort:** Trivial (1-line `np.load` + scalar compare). Executor: transit-dynamics-theorist or berry-geometric-phase-theorist.

### S111-CF-FLOQUET2 — exact DTC counterfactual-depth threshold + δτ_amp map (QA-R2-2 closeout) [trivial, INFO registration]
- **What:** Pin Sage-exact `h_par_crit = 2·0.035/A = 0.0725` (at A=0.965, the period-2 half-width first catching the nearest-a=1 mode), the miss-factor `h_par_crit/8.3e-4 = 84.34×`, and the linear `δτ_amp` map `δτ_amp_crit = δτ_amp·84.34`. Registers the DTC-absence as a falsifiable structural prediction tied to the Ordered-Veil `S_ent=0` freeze.
- **Inputs:** nearest-a=1 relic detuning `|A−1|=0.035` (inv-12 W3-2); `h_par=8.3e-4`; period-2 half-width law `Δa_½ ≈ q_M = A·h_par/2`.
- **Gate:** Sage-exact `h_par_crit` + miss-factor against analytic forms (THEOREM tolerance, machine-ε). INFO-class (structural-prediction registration; no PASS/FAIL on substrate physics).
- **[plan-w5 PRDR correction, supersedes the workshop figures]:** Sage-exact `h_par_crit = 2·(35/1000)/(965/1000) = 70/965 = 14/193 = 0.07253886`; miss-factor `(14/193)/(83/100000) = 1400000/16019 = 87.396×`. The workshop's `0.0725 / 84.34×` was internally inconsistent (`2·0.035/A = 0.0725` divides by A, but `0.07/8.3e-4 = 84.34` did NOT) — plan-w5 uses the consistent Sage-exact `14/193 / 87.396×`. The plan-w5 block is authoritative.
- **Effort:** Trivial (Sage one-liner + registry-text prediction). Executor: transit-dynamics-theorist or berry-geometric-phase-theorist.

### S111-CF-FLOQUET3 — first-principles δτ_amp derivation from the diabatic-freeze afterglow [moderate]
- **What:** DERIVE `δτ_amp` (the residual modulus ring-down amplitude after the Mach-13.75 transit-freeze) from the substrate dynamics, independently of the S101-W1 guard-floor pin; verify `h_par = (dω²/dτ)·δτ_amp/ω² → 8.3e-4`. Closes the one input the depth-crux concession takes on trust.
- **Inputs:** post-fold modulus relaxation trajectory `τ(t)` near the τ_fold exit (the residual oscillation after diabatic freeze); spectral sensitivity `dω_n²/dτ` at the relic modes; `ω_{n,0}²` (relic band); Ordered-Veil freeze parameters (`S_ent=0`, `R_therm=5251.82`).
- **Gate:** `|h_par_derived − 8.3e-4|/8.3e-4 < 0.1` (RATIO, 10% — the guard-floor pin's own band). NON-verdict-gating (a PASS upgrades `h_par` from guard-floor-asserted to substrate-derived).
- **Effort:** Moderate (requires the post-fold modulus trajectory; a focused single-script compute). Executor: transit-dynamics-theorist.

### S111-CF-FLOQUET4 — cutoff-robustness scaling theorem registration (QA-R2-1 formalization) [Stage-1]
- **What:** Register the structural theorem "no L_max ≥ 12 truncation extension reopens the §VII.BP relic resonance at `h_par=8.3e-4`," because any new high-A mode lands near a zone `n` whose Mathieu half-width `Δa_½^{(n)} ∝ q_M^n` (n≥3 ⇒ `≲10⁻⁷`) falls faster than the mode density concentrates at integer-² centers. The EXPONENT `n` is the theorem; the prefactor is convention-ambiguous (×16) and explicitly NOT registered.
- **Inputs:** McLachlan tongue-half-width scaling `Δa_½^{(n)} ∝ (q_M/2)^n`; relic spectrum `A_relic ∈ [0.876, 12.6]` (inv-12); `q_M(A)=A·h_par/2`; the L12 master spectrum cache for the mode-density argument.
- **Gate:** `[VERIFY-THEOREM]` on the scaling exponent (analytic, machine-ε against the McLachlan form); the prefactor is declared diagnostic-only. Stage-1-candidate → Stage-2 cross-axis verify per `joint-theorem-promotion.md` if promoted to permanent-results.
- **Effort:** Moderate (analytic theorem statement + Sage verification + a mode-density-vs-half-width argument). Executor: transit-dynamics-theorist or berry-geometric-phase-theorist.

### S111-CF-KSIGN-PARITY-STAGE2 — Stage-2 two-agent NON-AUTHOR cross-check of the κ-sign-lock ∧ Wodzicki-parity joint theorem (§VII.CF)
- **What:** Stage-2 two-agent parallel independent-verify of the STAGE-1-CANDIDATE `κ-sign-lock ∧ Wodzicki-parity` joint theorem (registered S110, §VII.CF). Axis-A (NCG/spectral) cross-reviewer audits the Wodzicki degree-rigidity + integer-parity clause; Axis-B (transport/cosmological-bridge) cross-reviewer audits the transport-κ sign-lock clause; the JOINT clause (the conjunction forecloses ALL substrate-natural ascending morphisms for a `d_A=+1` anchor) is PASS-AND'd across both. Both operate WITHOUT prior workshop context (read only the registered §VII.CF Stage-1 entry, NOT the connes-mack workshop file).
- **Inputs:** the registered §VII.CF STAGE-1-CANDIDATE entry in `permanent-results-registry.md` (joint-clause flags); `s110_gate_verdicts.txt` W3 mint `f60cff36…` + W4 consumers `2a654897…`/`7bfda02a…`; corpus §18.0 Conjunct-1 (`deg(B)=d_A`, Wodzicki); the Sage substitution chains (Q-M-1 connes; M1 mack).
- **Gate:** BOTH cross-reviewers PASS their single-axis clauses AND the JOINT conjunction PASSes independently in BOTH verdicts (logical AND) ⇒ STAGE-3-PERMANENT. ANY clause FAIL ⇒ stays STAGE-1-CANDIDATE, FAILing clause routed to remediation.
- **Effort:** ~1 wave (2 parallel cross-reviewers; NON-AUTHORS — must NOT be connes or mack per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`). Executors: **axis-A = lizzi-spectral-functional-theorist** (Wodzicki/spectral; or van-den-dungen-bridge-theorist) + **axis-B = volovik-superfluid-universe-theorist** (transport/cosmological-bridge; or transit-dynamics-theorist). Dispatch the two IN PARALLEL.

---

## Gate-ID convention + collision

All S111 gate IDs prefixed `S111-CF-`; verdict file `computations/session-111/s111_gate_verdicts.txt` (canonical per `gate-verdicts.md`). No collision with S110 (`s110_*`). Stage-1 registration gates (CLOCKLOC3, NOHOLOFLUX, FLOQUET4) emit a verdict line (registry-landing); their Stage-2 verifies are SEPARATE future gates. KSIGN-PARITY-STAGE2 is itself a Stage-2 verify of the S110-landed §VII.CF.

## Run-order notes

- **Tier-1 spine first:** W1 (a(t)/clock) + W2 (M_KK keystone) are the highest-EVOI waves — the a(t)/Friedmann residual = {M_KK magnitude (W2) + clock-triple (W1)}. They may run in parallel.
- **Intra-wave dependency:** CLOCKLOC2 (monotone corridor) feeds CLOCKLOC1's corridor scoping — sequence CLOCKLOC2 → CLOCKLOC1 within W1.
- **Upstream-landed (ready):** MKK-RG-INVARIANCE gated on CV2A (on disk, `s110_cf_cv2a_*.npz`); KSIGN-PARITY-STAGE2 gated on the §VII.CF Stage-1 entry (landed S110). Both ready.
- **CF3-H0-RESIDUAL ∥ MKK-RG-INVARIANCE** (independent axes per the volovik a₀-audit) — no sequencing constraint.
- **S111 also carries a workshop schedule** (`session-110-s111-workshop-schedule.md`, separate stream) — NOT part of this compute plan; runs via `/rclab-coordinate` workshop-mode.
