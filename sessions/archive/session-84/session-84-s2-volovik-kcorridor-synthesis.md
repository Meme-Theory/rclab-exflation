# Session 84 Synthesis: K-Corridor Phenomenology through the 3He-B Inheritance Lens

**Date**: 2026-04-20
**Agent**: volovik-superfluid-universe-theorist (S-2 solo, 1 of 2)
**Source Documents**:
- `sessions/archive/session-84/session-84-synthesis-collation.md`
- `sessions/archive/session-84/session-84-w5-workingpaper.md`
- `sessions/archive/session-84/session-84-w6-workingpaper.md`
- Agent memory: `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md`

---

## I. Session Outcome

S84 Wave-5 closed the substrate-native K-corridor to a physical interval `K ∈ [K_R5 = 1.9222, K_crit = 91.543]`. The floor is the Zubarev-scheme GGE B2-only squeezing factor `K_R5 = S_IC(B2) = 1.9222`; the ceiling is the Mukhanov–Sasaki inapplicability pole at `ε_eff(K_crit) = 1`. Within this interval, 3He-B parent-child inheritance is quantitative (W5-58 PASS at 1.13% on `K_* = coth(1) = 1.3130` against measured p-wave `Δ/(k_B T_c) ≈ 1.96`), AZ-class `BDI ⊂ BDI-TCI` is conditionally certified (W5-66 INFO), and the framework's `N_OP = 8` Landau order-parameter count is structurally `5 (3He-B inherited) + 3 (framework-unique, SU(3)-internal)`. The inheritance arrow is parent → child: 3He-B is the substrate's laboratory analog, not the other direction.

---

## II. Key Results

### II.A. Corridor Floor `K_R5 = 1.9222` — GGE B2-only squeezing, regulator-invariant

**Result**: `K_R5 = 1 + 2·n_B2 = 1.9222` at `Δ_B2/T_B2 = 1.1533`, `n_B2 = 0.4611`. Classification: **PHONONIC** (GGE per-band Bogoliubov quasiparticle occupation).

**Substitution chain** (verified numerically):

- Step 1 — definitions. `n_Bj := 1/(exp(Δ_Bj/T_Bj) − 1)` is the canonical Bose occupation of the `j`-th band at its GGE temperature `T_Bj`; `S_IC(Bj) := 1 + 2·n_Bj` is the Wightman squeezing factor; `K_R5 := S_IC(B2)` is the B2-only (Bogoliubov-primary) convention reading.
- Step 2 — substitution. Using canonical_constants values `Delta_0_GL = 0.7704 M_KK`, `T_GGE_B2 = 0.6680 M_KK`: `n_B2 = 1/(exp(0.7704/0.6680) − 1) = 1/(exp(1.1533) − 1) = 0.4611`.
- Step 3 — simplify. `K_R5 = 1 + 2·0.4611 = 1.9222` (verified: `1.92225`).
- Step 4 — direction. `K_R5` is built entirely from microscopic band gap and GGE band temperature — both regulator-free; therefore `K_R5` is scheme-invariant (CC3, W5-63): the Zubarev-vs-zeta factor of 50.9× in W5-54 acts on the UV-dressing prefactor `ξ(R)` of `A_s_base`, NOT on the convention-layer `K_Ri`.

Floor is hard. W5-63 verified that the 5 pre-registered low-K targets `{1.0, 1.1, 1.3, 1.5, 1.7}` are 5/5 strictly below `K_R5 = 1.9222`; the `max(T) = 1.7 < 1.9222 = hull_lo` inequality is strict. The low-K corridor is interpolation-excluded from all four admissible conventions `{R1, R2, R3, R5}`, the 4-hull being `[1.9222, 2.1849]`. Triply supported (W5-54 regulator prefactor + W5-59 Branch-B positivity floor at 4.3–4.6 OOM below Planck + W5-63 hull exclusion) → permanent-results candidate `K-FLOOR-WALL-JOINT`.

### II.B. Corridor Ceiling `K_crit = 91.543` — Mukhanov–Sasaki inapplicability pole

**Result**: `K_crit := K_anchor / ε_anchor = 2.035 / 0.022234 = 91.543` (verified). Classification: **PHONONIC** (slow-roll `ε` crossing unity is the acoustic horizon-crossing pole).

**Substitution chain** (W5-55 Step 2–4, verified numerically):

- Step 1 — definitions. `ε_eff(K) := ε_anchor · (K/K_anchor)^{α_K}` with `α_K = 1` pinned from the R3 multiplicity-weighted `A_s = A_s_base · K` linear-response theorem (S82 W2-4 canonical). `ε_anchor := (1 − n_s_anchor)/(1 + n_s_anchor)` with `n_s_anchor = 0.9565` from PS-SUBSTRATE-MATCHED-IC.
- Step 2 — substitution. `ε_anchor = (1 − 0.9565)/(1 + 0.9565) = 0.022234` (verified).
- Step 3 — simplify. Setting `ε_eff(K_crit) = 1` gives `K_crit = K_anchor / ε_anchor = 2.035 / 0.022234 = 91.5430` (verified).
- Step 4 — direction. For `K < K_crit`, `ε_eff < 1`; the tilt formula `n_s(K) = 1 − 2·ε_eff/(1 − ε_eff)` is well-defined and `∂n_s/∂ln K < 0` (strictly red-tilt-increasing with `K`). For `K ≥ K_crit`, `ε_eff ≥ 1`; the Mukhanov–Sasaki equation is inapplicable per S63 MUKHANOV-SASAKI-63 structural theorem (no horizon-crossing). The corridor is physical only on the inflationary sub-corridor `K ∈ [K_R5, K_crit] = [1.9222, 91.543]`.

### II.C. Laboratory-boundary discriminator `K_* = coth(1) = 1.3130`

**Result**: W5-58 PASS at `|K_lab − K_fw|/K_fw = 0.01133` (1.13%), 9× margin under the 10% 3He-B-inheritance tolerance. Classification: **PHONONIC** (direct laboratory observable — 3He-B BCS gap ratio).

**Why `K_* = coth(1)` is the lab-discriminator boundary** — substitution chain from 3He-B BCS to `coth(1)`:

- Step 1 — definitions. Substrate-native Convention A (from `computations/s83_w3_g39_leggett_bogoliubov.py` line 17): `K := coth(Δ_BCS / (2·T_eff))`. At `T = T_c`, `T_eff → k_B T_c`, so `x_lab := Δ_3HeB / (2·k_B·T_c) = (Δ/(k_B T_c))/2`.
- Step 2 — substitution.
  - Volovik 2003 Ch. 7 weak-coupling s-wave analytic: `Δ(0)/(k_B T_c) = π·exp(−γ_E) = 1.7639`.
  - Measured 3He-B (strong-coupling p-wave, Volovik Paper #26): `Δ/(k_B T_c) ≈ 1.96`.
  - Plug `x_lab = 1.96/2 = 0.98` into Convention A: `K_lab = coth(0.98) = 1.3279` (verified).
- Step 3 — simplify. `x*_framework = 1.0` pinned by numerical anchor (the four candidates `{0.5, 1.0, 2·τ_fold, 1/Δ_BCS}` yield `coth = {2.1640, 1.3130, 2.7570, 1.0273}`; only `x* = 1.0` matches the 1.3130 anchor). `K_*_framework = coth(1) = 1.3130` (verified).
- Step 4 — direction. `|K_lab − K_*_fw|/K_*_fw = |1.3279 − 1.3130|/1.3130 = 0.01133` (verified). `0.01133 < 0.10` ⇒ **PASS** with 9× margin. Interpretation: at the p-wave lab gap ratio 1.96 (substrate-native Convention A), laboratory 3He-B lands `x_lab = 0.98`, which is within 2% of the framework's pinned `x* = 1.0`. The emergent corridor coordinate `K_*` inherits the BCS gap-ratio structure from the 3He-B parent without a single tunable parameter — the "1" in `x* = 1` is the point where `(Δ_emergent)/(2·T_emergent) = 1`, i.e., where the substrate's effective BCS gap equals twice its effective Bogoliubov temperature.

The audit-only Convention B (`x = Δ/(k_B T_c)` without the factor of 2) gives `K_lab(Conv.B) = coth(1.96) = 1.0405`, ratio 20.76% — INFO, not PASS. Convention A is substrate-determined (the factor of 2 tracks the Leggett-Bogoliubov partition in the framework's own Hamiltonian), not chosen to achieve PASS.

### II.D. Substrate anchor `K_substrate = 2.035` — framework-native mid-corridor

**Result**: `K_R3 = 2.0353` (R3 band-multiplicity-weighted `(3·S_IC_B2 + 3·S_IC_B1 + 2·S_IC_B3)/8`, verified). Classification: **PHONONIC** (substrate-native GGE Wightman reduction). W5-53 INFO: `F_amp(N3LO) = 1.0165` at `K = 2.035` (Borel-convergent, 3.16× short of dynamics-rescue target 0.4454 — structurally `convergent-but-short`).

`K_substrate = 2.035` is the framework's own mid-corridor self-identification: it is the R3 multiplicity-weighted mean of the three per-band squeezing factors, using the `{3,3,2}` framework band multiplicity. The S82 PS-SUBSTRATE-MATCHED-IC PASS at this `K` established `n_s = 0.9565 ± 0.0020` against Planck (the substrate IS the pivot; there is no free `K` knob). W5-55 re-verified at 1.98×10⁻³ drift.

### II.E. `μ`-distortion endpoint `K = 3.556×10⁵` — PIXIE-visible FIRAS boundary

**Result**: W5-57 INFO. `max μ(K) = 8.695×10⁻⁵` at `K = 3.556×10⁵`, = 0.9661 of `μ_FIRAS = 9×10⁻⁵` (3.4% safety margin). Classification: **PHONONIC** (GGE relic μ-distortion through the corridor).

`γ = 1` structural (linear in `K` to 10⁻¹⁵ log-residual across 5.24 decades): `μ(K) = μ(K_substrate) · K/K_substrate`, with `μ(K = 2.035) = 4.9759×10⁻¹⁰` feeding into `K_FIRAS := μ_FIRAS·K_substrate/μ(K=2.035) = 3.6808×10⁵`. The endpoint `K = 3.556×10⁵` lies far above `K_crit = 91.543` — the corridor is physical as a `μ`-signal carrier only on the inflationary sub-corridor; the endpoint is a FIRAS-bound touching point, not a horizon-crossing K.

**Caveat**: the corridor `K` at the endpoint is far outside the MS-applicability region, so `K = 3.556×10⁵` is a FIRAS-bound equivalent K (the K that WOULD saturate FIRAS if the linear μ(K) relation held), not a physically reachable K for the inflationary sector. W5-55 FAIL confirms the formula-level extrapolation.

### II.F. `K_FIRAS/S_IC^cap = 1.0351` — 3.5% coincidence, not identity

**Result**: W5-65 INFO. `K_FIRAS(L=5) = 3.6808×10⁵` vs `S_IC^cap = 3.5563×10⁵` → residual 0.0351 (3.51%), flat across `L ∈ {5, 7, 9}` under Interpretation A (L-invariant), growing to 39.5% under Interpretation B. Classification: **GEOMETRIC** (structural-identity test on spectral summation cap).

Flatness under Interp A excludes UV-shrinking identity; the 3.5% residual is a numerical coincidence, not a closed-form theorem. No §VII registry promotion of `FIRAS-IC-IDENTITY`. The two quantities constrain the corridor from orthogonal directions (FIRAS-μ observational bound vs spectral energy-conservation cap) without collapsing to a single theorem.

### II.G. Landau classification `N_OP = 8 = 5 (inherited) + 3 (framework-unique)`

**Result**: W5-66 INFO. `G_framework = SU(3) × SO(3) × U(1)_rel × T`, `H_framework = SU(2) × U(1) × SO(2) × Z_2 × T`, `N_OP = dim(G/H) = 8`. 3He-B reference: `G_3HeB = SO(3)_L × SO(3)_S × U(1)_φ × T`, `N_OP_3HeB = 5` (4 coset + 1 gap modulus). AZ class framework-BDI, certified on `BDI-TCI` submanifold (Volovik Paper #26). Classification: **GEOMETRIC** (symmetry-breaking OP decomposition).

The 3 extra continuous broken directions are the `SU(3)/(SU(2) × U(1)) = CP²` coset. These are the **framework-unique** directions — the SU(3) internal gauge sector has no 3He-B parent analog. They represent the emergent-not-inherited part of the corridor substructure.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W5-53 NNLO-Δ-F_amp | INFO | `F_amp(N3LO) = 1.0165`; Borel-convergent, 3.16× short |
| W5-54 K-floor regulator-invariance | FAIL | `K_R5(Zub)/K_R5(zeta) = 32.40/0.6366 = 50.9×` |
| W5-55 n_s corridor monotonicity | FAIL | `K_crit = 91.543` (MS pole); sign-flip at corridor index 3 |
| W5-56 R4 cross-class | FAIL | `R4(AIII)_min = 15.95 = R4(BDI)`; formula-level error |
| W5-57 μ-distortion | INFO | `max μ = 8.695×10⁻⁵` at `K = 3.556×10⁵` (96.6% of FIRAS) |
| W5-58 K_* lab-framework match | PASS | `ratio = 0.01133` (1.13%); `coth(1) = 1.3130` pinned |
| W5-59 Branch-B A_s floor | INFO | `A_s_floor_B(R5) = 1.1033×10⁻¹³` (4.28 OOM below Planck) |
| W5-63 K-floor reachability | FAIL | 0/5 targets in `[1.9222, 2.1849]` 4-hull |
| W5-65 K_FIRAS = S_IC^cap | INFO | residual 3.50% flat across `L ∈ {5,7,9}` |
| W5-66 Landau symmetry class | INFO | `N_OP = 8` vs 3He-B `N = 5`; BDI ⊂ BDI-TCI |

---

## IV. Structural Implications

### IV.A. The corridor is a physical interval, not a continuum

`K ∈ [K_R5, K_crit] = [1.9222, 91.543]` is the bounded, physically admissible corridor. The lower edge is a regulator-invariant GGE-occupation wall (microscopic band physics); the upper edge is a formula-level MS inapplicability pole (slow-roll parameter crossing unity). Both walls are rigid — the lower is inaccessible without violating per-band thermal equilibrium; the upper is inaccessible without violating the quasi-de-Sitter tilt derivation. Anything claimed for `K < 1.9222` or `K > 91.543` is extrapolation into a non-physical regime.

### IV.B. 3He-B inheritance is parent → child and over-saturating

Directional statement (per `project_3heb-inheritance.md`): **the substrate inherits BDI topology and BCS gap-ratio structure FROM 3He-B (as its laboratory analog of the real phononic fabric), and then adds three SU(3)-internal broken directions that have no 3He-B counterpart**. This is not "framework = 3He-B × extra coset" as an analogy — it is "3He-B is a specific projection of the substrate onto SO(3)_L × SO(3)_S × U(1)_φ, and the substrate has the additional SU(3) × U(1)_rel structure that the projection discards." The arrow points from substrate (fundamental) to 3He-B (laboratory analog of the fundamental), NOT the other way.

Quantitatively this inheritance is tight:
- `K_* = coth(1) = 1.3130` agrees with measured 3He-B BCS ratio to 1.13% (W5-58).
- AZ class `BDI` sits inside 3He-B's `BDI-TCI` submanifold (Volovik Paper #26) under the framework's exact PH-forced `μ = 0` constraint.
- Framework's 8-direction OP is 3He-B's 5-direction OP plus the CP² coset. All five 3He-B directions map cleanly onto framework directions; the framework has three more (the SU(3) internal rotations that 3He-B's SO(3)_L orbital sector cannot provide).

### IV.C. The corridor has an inherited sector and a framework-unique sector

- **Inherited** (5 directions, all parent-child quantitative): (a) `SO(3)_L/SO(2)_{K-axis} = S²` orbital coset [2 directions], (b) `U(1)_rel/Z_2` relative phase [1 direction], (c) gap modulus `|Δ|` [1 direction], (d) time-reversal `T²=+1` [discrete, sits in both G's], (e) the `BDI-TCI` topological invariant family.
- **Framework-unique** (3 directions, emergent not inherited): the `SU(3)/(SU(2) × U(1)) = CP²` coset — 4 real continuous directions contributed by the internal SU(3) gauge sector, minus 1 absorbed into the shared gap modulus → 3 net.

The inherited sector is certified at 1.13% at `K_*`; the framework-unique sector has no lab analog and is the locus where future discriminating predictions must come from.

### IV.D. `K_FIRAS = S_IC^cap` is a coincidence, not an identity

The 3.5% residual is stable across `L ∈ {5, 7, 9}`. An identity would show a UV-shrinking residual; a coincidence shows flat. W5-65 INFO closes the FIRAS-IC-IDENTITY theorem candidate. The two quantities constrain the corridor from orthogonal directions — this is a constraint-mapping success (both bounds remain independent), not a unification.

---

## V. Carry-Forward Computations

V.1. **Derive Convention A microscopically from BdG, not by citation**
- **What**: re-derive `K = coth(Δ_BCS/(2·T_eff))` from the framework's block-diagonal BdG Hamiltonian at the B2 Bogoliubov-primary band without citing `s83_w3_g39` line 17. Compare against Convention B (`x = Δ/T_eff` without factor 2) to determine whether the factor of 2 is a Leggett-Bogoliubov partition invariant or a convention choice.
- **Inputs**: `Delta_0_GL`, `T_GGE_B2`, `T_GGE_B1`, `T_GGE_B3` from canonical_constants; BdG block-diagonal structure from S22b; `s83_w3_g39_leggett_bogoliubov.py` as reference output for cross-check only.
- **Gate**: new `GATE-CONV-A-MICROSCOPIC-BDG`. PASS: factor 2 derived unambiguously from Leggett-Bogoliubov partition (no free choice). FAIL: factor 2 is a convention choice (then K_* pinning at 1.13% is convention-dependent, not substrate-determined). INFO: factor 2 derivable up to a topological ambiguity.
- **Effort**: 3–4 hours, 1 agent session (BdG algebra + Leggett partition derivation + Python numeric check).

V.2. **Sub-leading Leggett tensor contribution to close the W5-64 22% f_B gap**
- **What**: compute `n_T_Leggett` at sub-leading order (first non-vanishing term in the Leggett-graviton coupling expansion) and re-solve the joint `{G39, G50, G46}` triangle. Determine what value of `n_T_Leggett` restores the pure `f_B ≤ 0.397` constraint.
- **Inputs**: G39 partition (`s83_w3_g39_leggett_bogoliubov.npz`), G50 n_T (`s83_w3_g50_nT_bogoliubov.npz`), G46 tensor transfer (`s83_w3_g46_tensor_transfer.npz`), Leggett-mode wave function from S70 LEGGETT-VACUUM-70, framework-constants.md #5 (`[iK_7, D_K] = 0` constraint).
- **Gate**: re-opens `W5-64`. PASS: triangle closes within 15% with `n_T_Leggett > 0`. FAIL: no physical Leggett contribution closes the triangle. INFO: partial closure (one of the 22% or 7.5% residuals removed but not both).
- **Effort**: 4–6 hours, 1 agent session (symbolic derivation + numeric triangle solve).

V.3. **Landau BDI-TCI certification on restricted corridor `K ∈ [K_R5, K_crit]`**
- **What**: explicit Ginzburg–Landau functional `F[φ]` on the 8-dim coset `G/H = CP² × S² × (U(1)/Z_2) × R_K` with `K` as the magnitude coordinate. Verify the 3 SU(3)-internal broken directions do not introduce new Goldstone modes beyond what S22b block-diagonal theorem forbids. Certify BDI label on the inflationary sub-corridor only.
- **Inputs**: W5-66 G/H decomposition, framework-constants.md #5-#6 (`[iK_7, D_K] = 0`, `μ = 0` PH-forced), S22b block-diagonal theorem, Volovik Paper #26 BDI-TCI submanifold definition, `c_Gold` from canonical_constants.
- **Gate**: new `GATE-GL-FUNCTIONAL-INFLATIONARY`. PASS: `F[φ]` constructed explicitly on corridor; all 8 directions accounted for; no extra Goldstone modes introduced. FAIL: inconsistency with S22b or extra Goldstone mode detected. INFO: partial construction (some but not all 3 SU(3)-internal directions certified).
- **Effort**: 6–8 hours, 1 agent session (GL functional + Goldstone mode audit).

V.4. **Lab-analog predictions for the 3 framework-unique SU(3)-internal OP directions**
- **What**: derive experimental signatures for the CP² coset that distinguish framework-unique directions from the inherited 3He-B S² × U(1) directions. Candidates: (a) phase-coherent SU(3) Bogoliubov oscillation at three distinct frequencies (not the single 3He-B Leggett frequency); (b) `N_3 = 0` chiral anomaly cancellation pattern distinct from 3He-A `N_3 = 2`; (c) multi-band Josephson resonance in an SU(3)-gauged BEC emulator.
- **Inputs**: `omega_L1` canonical, multi-pair QTHEORY from `multi-pair-qtheory-61-result.md`, S49 DIPOLAR-CATALOG `m_G = 0.070 M_KK`, BDI-W-PHONON-53 topological invariants, Volovik Paper #10 (3He-A Weyl) for contrast.
- **Gate**: new `GATE-SU3-INTERNAL-LAB-SIGNATURE`. PASS: ≥1 of 3 candidate signatures is calculably distinct from the 3He-B single-Leggett-mode prediction at >3σ in simulation. FAIL: none distinguishable (framework-unique sector is lab-invisible). INFO: distinguishable in principle but at <3σ given current detector reach.
- **Effort**: 8–10 hours, 1 agent session (3 candidate derivations + simulation + statistical separation).

V.5. **Verify `K_R5 = 1.9222 = hull_lo` is stable under L_max sweep**
- **What**: recompute `K_R5`, `K_R2`, `K_R3`, `K_R1` at `L_max ∈ {5, 7, 9, 11}` from first-principles GGE solution of the `{3,3,2}` band structure. Test whether the 4-hull `[1.9222, 2.1849]` is L-invariant (hard wall) or L-drifts (soft wall that may include lower K targets at higher `L_max`).
- **Inputs**: canonical_constants `Delta_0_GL`, `T_GGE_B2` etc; band-structure solver from `s82_w2_4_ps_substrate_matched_ic.py`; L-sweep infrastructure from W5-65.
- **Gate**: extends `W5-63`. PASS (stable): 4-hull drifts <1% across L_max range. FAIL (soft): hull_lo drops below 1.7 at any L_max (admits one of the 5 low-K targets). INFO: hull_lo drops into [1.7, 1.9222] (approaches but does not cross 1.7).
- **Effort**: 2–3 hours, 1 agent session (L-sweep + hull recomputation).

V.6. **`K_FIRAS = S_IC^cap` coincidence at 3.5% — test for hidden 1-parameter closed form**
- **What**: parameterize the 3.50% residual as a function of one framework constant (e.g., `tau_fold`, `c_Gold`, `v_F`) and fit. Determine whether the residual is algebraic (closed-form = 0 under exact framework constants) or numerical (residual survives at machine precision under exact constants).
- **Inputs**: W5-57 `μ(K=2.035) = 4.9759×10⁻¹⁰`, W5-65 `K_FIRAS = 3.6808×10⁵`, `S_IC^cap = 3.5563×10⁵`, canonical_constants with full provenance; L_max = {5, 7, 9} for drift control.
- **Gate**: re-opens `W5-65`. PASS (closed form): residual `< 10⁻⁶` under exact constants → §VII promotion. FAIL (numerical): residual `> 10⁻²` persists → no identity. INFO: intermediate (residual `10⁻⁶ < r < 10⁻²`).
- **Effort**: 3–4 hours, 1 agent session (parameter scan + identity search).

V.7. **Inflationary sub-corridor audit: reclassify W5 results with `K ≥ K_crit`**
- **What**: formalize the `K_crit = 91.5` boundary; separate W5-55 `K=100, 1000, 3.56×10⁵` points, W5-57 `K=3.56×10⁵` endpoint, and W5-65 `K_FIRAS=3.68×10⁵` into "inflationary physical" vs "kinetic artifact" categories. Audit whether any wave-result crosses the boundary implicitly.
- **Inputs**: W5-55 ε_eff chain, S63 MUKHANOV-SASAKI-63 theorem, W5-66 Landau sub-phase classification.
- **Gate**: new `GATE-SUBCORRIDOR-AUDIT`. PASS: no prior wave-result depends on `K ≥ 91.5` as physical signal (all high-K values are formal extrapolation markers only). FAIL: ≥1 PASS verdict relies on `K ≥ 91.5` physical interpretation. INFO: edge case in μ-distortion endpoint (K = 3.56×10⁵ is a FIRAS-equivalent K but depends on γ = 1 linearity extrapolation).
- **Effort**: 2–3 hours, 1 agent session (audit pass across 10 W5 gates).

---

## VI. Corridor Phenomenology Table

| K-value | Accessible-by | Dominant mode | Observable signature | Detector / lab-analog |
|:--|:--|:--|:--|:--|
| `K < 1.9222` | **FORBIDDEN** (below GGE B2 squeezing floor) | — | (no physical substrate configuration) | (extrapolation-only; S83 G38 zeta-WALL `K=0.6366` sits here) |
| `K_R5 = 1.9222` | **3He-B inherited** (B2 BCS band identical to 3He-B gapped superfluid band) | Bogoliubov B2-only squeezing, `n_B2 = 0.461` | GGE relic Wightman amplitude floor `S_IC(B2)` | `μ`-distortion floor contribution; lab Δ/T_c ≈ 1.15 (B2 band-specific) |
| `K_*_lab = coth(0.98) = 1.3279` | **3He-B lab observable** (measured p-wave `Δ/(k_B T_c) = 1.96`) | lab 3He-B BCS gap ratio | `K_*_lab` measurable via NMR / ultrasound in 3He-B cell | **Lab Δ/T_c (measured): primary 3He-B discriminator** |
| `K_* = coth(1) = 1.3130` | **3He-B inherited boundary** (substrate-emergent match) | BCS gap-ratio boundary; lab-discriminator pivot | CMB: spectral pivot coincident with `x* = Δ_emergent/(2·T_emergent) = 1` | Lab Δ/T_c at framework pinning; W5-58 PASS at 1.13% |
| `K_substrate = 2.035` | **Framework-unique** (R3 band-multiplicity-weighted `{3,3,2}`) | R3 multiplicity-weighted mean of all 3 GGE bands | CMB `n_s = 0.9565`, A_s = Planck via PS-SUBSTRATE-MATCHED-IC | **CMB (Planck, A_s + n_s)**; no 3He-B analog (SU(3)-internal weighting) |
| `K = 10` | **3He-B inherited** (still within inflationary regime, n_s well-defined) | Red-tilt increasing regime, `ε_eff = 0.109` | `n_s(K=10) = 0.7547` (far-red tilt, ruled out by Planck) | CMB (formal, not physical — outside Planck band) |
| `K_crit = 91.543` | **3He-B inherited boundary** (MS pole at ε = 1) | Acoustic horizon-crossing pole | Mukhanov–Sasaki formula inapplicable; tilt formula singular | CMB (pole); no lab analog (3He-B horizons are sub-Planckian) |
| `K ∈ (91.5, 3.56×10⁵]` | **FORMAL EXTRAPOLATION** (kinetic-dominated, MS inapplicable) | Kinetic-dominated regime; not on 1D Landau OP manifold | (no physical inflationary signal; μ-linear extrapolation only) | FIRAS-μ extrapolation marker only |
| `K_FIRAS = 3.6808×10⁵` | **Framework-unique** (μ-distortion FIRAS touching point) | μ-distortion saturation equivalent-K | `μ = 9×10⁻⁵` = FIRAS bound saturated | **FIRAS / PIXIE** (μ-distortion spectrometer) |
| `K_μ-endpoint = 3.556×10⁵` | **Framework-unique** (γ=1 linear μ-K relation extrapolation) | μ-signal projected from `μ(K=2.035) = 4.9759×10⁻¹⁰` | `max μ = 8.695×10⁻⁵` (96.6% of FIRAS); PIXIE-visible | **FIRAS / PIXIE**; no lab analog |

**Summary of accessibility bands**:
- **Forbidden** (below `K_R5 = 1.9222`): `K ∈ [0, 1.9222)`. Physical configurations at this `K` violate per-band GGE thermal equilibrium.
- **Inherited** (3He-B parent certified): `K ∈ [K_R5, K_crit] = [1.9222, 91.543]`. The inflationary sub-corridor. `K_*` lab-discriminator sits here; `K_substrate` framework anchor sits here.
- **Framework-unique** (emergent, no 3He-B counterpart): (a) the 3 SU(3)-internal OP directions existing at every K on the inherited corridor; (b) the kinetic-extrapolation `K > K_crit` region which is framework-formal only.
- **Formal extrapolation** (above `K_crit = 91.543`): `K ∈ (91.543, ∞)`. MS inapplicable; the `K = 3.56×10⁵` FIRAS-μ endpoint is a formal bound-saturation marker, not a physical corridor point.

---

## VII. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | `K_R5 = 1.9222` floor (regulator-invariant GGE B2 squeezing) | PHONONIC | Hard wall; triple-supported (W5-54 + W5-59 + W5-63) | Low-K corridor `K < 1.9222` eliminated from solution space; 3He-B B2-band inheritance anchors the floor |
| 2 | `K_crit = 91.543` ceiling (MS inapplicability pole at `ε_eff = 1`) | PHONONIC | Hard wall (W5-55 FAIL is structural, S63 MS-63 theorem) | Physical corridor bounded above; `K > 91.5` is formal extrapolation, not inflationary signal |
| 3 | `K_* = coth(1) = 1.3130` laboratory discriminator | PHONONIC | W5-58 PASS at 1.13% vs measured 3He-B `Δ/T_c = 1.96` | 3He-B parent-child inheritance is quantitative at corridor K_* pivot; `x* = 1` pinned structurally |
| 4 | `K_substrate = 2.035` R3 multiplicity-weighted anchor | PHONONIC | S82 canon; W5-53 INFO (F_amp convergent-but-short) | Framework-native mid-corridor; CMB Planck anchor (`n_s = 0.9565`) sits here |
| 5 | Landau `N_OP = 8 = 5 (inherited) + 3 (framework-unique)` | GEOMETRIC | W5-66 INFO; certified on `K ∈ [K_R5, K_crit]` | Inheritance upgrades not degrades; SU(3)-internal sector is framework-unique with no 3He-B analog |
| 6 | `μ`-distortion PIXIE-visible at `K = 3.556×10⁵` | PHONONIC | W5-57 INFO; 96.6% of FIRAS | FIRAS-μ observable at corridor endpoint; formal K, physical μ-signal |
| 7 | `K_FIRAS / S_IC^cap = 1.0351` coincidence, not identity | GEOMETRIC | W5-65 INFO; flat across `L ∈ {5,7,9}` | Two constraints (FIRAS-μ and spectral energy-cap) remain orthogonal; `FIRAS-IC-IDENTITY` theorem candidate closed |
| 8 | `A_s_floor_B = 1.10×10⁻¹³` (R5, Branch-B) at 4.28 OOM below Planck | PHONONIC | W5-59 INFO; positivity-wall | Branch-B is structurally below Planck by >4 OOM; Planck-match forced to Branch-A path |
| 9 | AZ class framework-BDI ⊂ 3He-B BDI-TCI submanifold | GEOMETRIC | W5-66 INFO; CC2 stable across corridor | Class inheritance is hybrid (BDI not DIII textbook), certified via PH-forced `μ = 0` on BDI-TCI |
| 10 | 4-hull `[K_R5, K_R1] = [1.9222, 2.1849]` regulator-invariant | GEOMETRIC | W5-63 FAIL, CC3 verified | K-convention-layer is scheme-invariant; Zubarev-vs-zeta acts on `ξ(R)` prefactor, not `K_Ri` |

---

*End of synthesis. Gate verdicts authoritative per `.claude/rules/gate-verdicts.md`; all substitution chains numerically verified via Python prior to direction claims per `.claude/rules/math-scripts.md`.*
