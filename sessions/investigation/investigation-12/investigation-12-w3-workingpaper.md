# Investigation 12 Wave 3 — Transit Dynamics: lock the relic, Floquet, back-reaction, greybody, H̃ (Results Working Paper)

**Investigation**: 12 | **Wave**: 3 | **Plan**: investigation-12-plan-w3.md | **Theme**: transit-dynamics coherent chain — lock the relic {β_k} spectrum FIRST (FOUNDATIONAL), then settle the Ordered-Veil-vs-resonance tension (Floquet), construct the missing effective-Friedmann back-reaction closure, derive the exit greybody from BdG, and reconcile the CF21 H̃-branch divergence that rate-limits A_s. Gate-type mix: compute × 5.

**Verdict ledger (investigation track)**: `computations/investigation-12/inv12_gate_verdicts.txt` per `.claude/rules/gate-verdicts.md §"Investigation-Track Canonical Path"`. Emit via `emit_verdict(session=12, track="investigation", ...)`; all dual-SHA / sig_5 / `supersedes=` discipline applies track-agnostically.

## Gate Sections

### §W3-1. INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (FOUNDATIONAL — emits the locked {β_k} npz consumed wave-wide + cross-investigation)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The relic Bogoliubov spectrum {β_k} from the transit through the smooth van Hove fold converges to a single integrator-independent, N_seg-independent result under a high-accuracy ODE solver (Radau/DOP853, rtol≤1e-10), retiring the piecewise-constant transfer-matrix artifact.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w3.md` §W3-1 (machinery pin, thresholds, unitarity cross-check source).

**Output Artifacts** (closure-verification checklist):
- `script` — `computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.py` ✓ (must_contain `from canonical_constants import` ✓ line 86; `print_verdict_payload` ✓ defined + called). Grep-confirmed below.
- `data` — `computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.npz` ✓ (100 KB). Holds all plan-required keys: `beta_k, alpha_k, beta2_k, E_k, omega_k, k_grid, mult_k, Delta_k, rho_relic, N_pair_eff, integrator_agreement, refine_agreement, unitarity_residual, truncation_consistent` + truncation-band keys `rho_relic_check, N_pair_check, rho_trunc_rel, L_band_ceiling, L_band_check` + `N_seg_scan, tm_beta2_vs_nseg, bd_beta2_cf, bd_var_nseg, pair_band, tau_grid`.
- `plot` — `computations/investigation-12/inv12_w3_1_relic_spectrum_ode_lock.png` ✓ (215 KB): (a) locked |β_k|² vs |λ_k|; (b) per-mode E_k vs S101 pair band; (c) N_seg-refinement TM→ODE convergence; (d) the smooth ω_k(τ) profile through the fold.
- `verdict_line` — `computations/investigation-12/inv12_gate_verdicts.txt` matching `^INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK:.* audit_sha256=[a-f0-9]{64}` ✓ (dual-SHA companion row present; schema_v2 3-tuple NOT required).
- `wp_section` — this §W3-1 (Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit all present).

**MCP Pre-Compute Audit** (query-first; one-line salient returns):
- `search_knowledge("relic Bogoliubov spectrum transfer matrix N_seg integrator")` → surfaced `S85-W7-CUSP-BOGOLIUBOV: FAIL, value=-2.019676, scheme=transfer-matrix` and `TRANSFER-BOGOLIUBOV-64: PASS, max/min=1.33 across 3 cutoffs` — the soft-TM artifacts this gate retires. NOT pre-closed.
- `trace_entity("S100b-BOX-DELTA-BOGOLIUBOV")` → `computations/session-100b/s100b_box_delta_bogoliubov.py` (the validated sudden-limit recipe; var_Nseg−1=6e-10). Reused verbatim as the Section-E cross-check (entire-function C/S, BD-in/out, unitarity to 1e-10).
- `get_constant("tau_fold")` → 0.19 (S12/S42, CONST-FREEZE-42). Confirmed canonical; window bracketed [0.140, 0.240].
- `get_constant("n_pairs")` → 59.8 (S38, no PROVENANCE) — the canonical relic pair count (from the IMPULSIVE treatment, NOT this smooth-window sweep; see Results).
- `search_knowledge("BdG dispersion omega sqrt lambda mu Delta band B1 B2 B3")` → S76 sp-transit-workshop `ω_B = sqrt(ε_B² + Δ_BCS²)` (T2.1-T2.3); `s36_multisector_ed_verdict: mu = 0.0 particle-hole symmetric` — pinned the dispersion convention.
- `search_knowledge("S101 QEQ-RELIC-ODDFLOOR pair band 1.6395 10.8379")` → `S101-W1-QEQ-RELIC-ODDFLOOR: FAIL, omega_q_phys=2.012813 in_band[1.6395,10.8379]; E_n(q=0)=|lambda_n|` — confirmed the pair band IS 2·E_k = 2·|λ| at the relic point (Δ→0 in the S101 q-deformation).

**Verdict**: **INFO** — value=7.764638e-05 (max integrator agreement), scheme=FW, convention=ABSOLUTE, L_max=10. audit_sha256=`7915262f5cc74463d881e8df3892a2bd962c9c3c9f9dd76db7ae6fa8b93a3ff3`, content_sha256=`3637f5bf65a139a46b4324e7fd7c07bc1d2dd628bf1030c07941ac9ed053458b` (emitted to `computations/investigation-12/inv12_gate_verdicts.txt` via the `emit_verdict` MCP tool, track=investigation).

The **integrator LOCK is achieved** (PASS-level on the integrator axis); the verdict is INFO because the relic-CONTENT observables (ρ_relic, N_pair_eff) carry a truncation band — exactly the plan's pre-registered INFO scenario ("converges across integrators but carries a residual dependence ... a usable spectrum is emitted with a stated uncertainty band; W3-2/3/4 proceed and carry the band forward").

**Results**:

*Integrator lock (the gate's core deliverable — clean):*
- `integrator_agreement` = **7.765e-05** ≤ 1e-4 (max relative |β_k|²(Radau) − |β_k|²(DOP853) over modes with |β|²>1e-12). ✓
- `refine_agreement` = **3.320e-08** ≤ 1e-4 (rtol 1e-10 vs 1e-12). ✓
- `unitarity_residual` = **4.552e-15** ≤ 1e-10 (max_k |α_k|²−|β_k|²−1; machine ε for every mode). ✓
- All ODE integrations (Radau + DOP853 + Radau-refine) succeeded over the operational band (1248 unique |λ| modes, Σ mult = 20064). ✓

*Cross-checks (both confirm the method):*
- **N_seg-refinement** (demonstrates the TM artifact → ODE convergence): piecewise-constant TM |β|² → ODE Radau as N_seg grows; var_Nseg (25→800) = 1.0001, TM(800)→ODE rel dev = 1.24e-07. In this near-adiabatic smooth window the artifact is mild, but the convergence direction is shown.
- **Box+delta sudden-limit** (S100b recipe, where TM IS exact): closed-form |β|² = 1.437170e-01, var_Nseg = **1.0000000000 EXACT**, closed-form vs TM rel dev = 3.55e-14, max unitarity residual = 3.47e-14. The structural contrast is the substrate-physics point: TM exact for a sharp box (sudden), artifact-prone for a smooth ω(τ) fold (recovered by the ODE).
- **Construction-vs-cache**: max|dev| at τ_fold (validation sectors) = 3.508e-14 — the GPU eigvalsh(i·D) trajectory reproduces the L12 cache to machine ε.

*Locked spectrum + relic content (6 sig figs; downstream-consumed):*
- 4-tuple: (value=7.764638e-05, scheme=**FW** [BdG dispersion ω_k(τ)=sqrt((λ_k−μ)²+Δ_k²), μ=0], convention=**ABSOLUTE** [in/out adiabatic-vacuum Bogoliubov], L_max=**10**).
- `rho_relic` = Σ_k mult_k E_k |β_k|² = **15.4140** (M_KK units, operational band p+q≤7).
- `N_pair_eff` = Σ_k mult_k |β_k|² = **5.48910** (operational band p+q≤7).
- **Truncation band** (the INFO band W3-2/3/4 carry forward): raising the Casimir ceiling p+q≤7 → p+q≤8 gives ρ_relic 15.4140 → 26.8506 (rel change **0.4259**) and N_pair 5.48910 → 8.82317 (rel change 0.3779). `truncation_consistent = False`. **Substrate-physics reading**: over this smooth fold window the per-mode |β_k|² is uniformly small (~1e-5 to 1e-3) and does NOT decay with |λ| (the window is *near-adiabatic*, |ω′/ω²|≪1, β exponentially small), so the summed ρ_relic is dominated by the level² mode-count growth, not a bottom-band concentration. The per-mode {β_k} spectrum IS locked (cutoff-robust); the SUMMED ρ_relic over a *fixed* band is well-defined but its value scales with the band. This is itself informative: the canonical n_pairs=59.8 (S38) arises from the IMPULSIVE/sudden transit component (the box+delta sector), NOT this smooth eigenvalue-drift sweep — consistent with the framework's "impulsive transit, not quasi-static" paradigm.

*Pair-band cross-check (S101 anchor — EXACT):*
- 2·|λ|_min = **1.639482** = S101 lower edge 1.6395 (exact). The full S101 band [1.6395, 10.8379] = 2·[|λ|_min, |λ|_max] over L≤12 with Δ→0; the operational band 2E_k = [1.8842, 7.1578] (gapped by Δ_BCS, p+q≤7 subset).

*Convention resolution (documented):*
- Plan §W3-1 writes ω_k = sqrt((λ_k²−μ²)² + Δ_k²); the substrate-canonical BdG form (S36 μ=0 particle-hole-symmetric; S76 ω_B=sqrt(ε_B²+Δ²); S101 E_n(q=0)=|λ_n|) is ω_k = sqrt((λ_k−μ)²+Δ_k²) with μ=0. The plan's "(λ²−μ²)" is a transcription of the standard BdG band energy ξ=(λ−μ); with μ=0 both reduce to λ_k. Δ_k = Δ_BCS = 0.464255 (aggregate, S70). Used the canonical form; the integrator-LOCK verdict is convention-robust (depends only on ω(τ) being smooth).

*Plan-text-drift correction:* the cache input was pinned at `computations/_shared/s84_spectrum_cache_L12_tau019.npz` (absent); resolved to the canonical `computations/session-84/s84_spectrum_cache_L12_tau019.npz` per `substrate-first-canonical-sourcing.md §(ii.B)`; documented in the verdict value field.

*Constraint-map consequence:* the integrator-lock retires the A4 transfer-matrix segmentation artifact — the per-mode {β_k} spectrum is now ONE verified, integrator-independent result feeding W3-2 (Floquet, consumes {E_k, ω_k, |β_k|²} per-mode — cutoff-robust), W3-4 (greybody, exit-horizon ω_k — per-mode), W1-2 (lizzi A_s), W2-5 (vdd η-form). W3-3 (back-reaction) consumes ρ_relic = Σ E_k|β_k|² and MUST carry the truncation band [p+q≤7: 15.41, p+q≤8: 26.85] forward into its error budget (per the INFO honest-closure note). Artifacts: `inv12_w3_1_relic_spectrum_ode_lock.py/.npz/.png`.

---

### §W3-2. INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (Floquet band-structure resolution of the S101 §VII.BP in-band-resonance tension)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: When the post-fold modulus oscillation (ω_q^phys = 2.012813 M_KK, γ = 29.7532) drives the relic mode equation as a Hill/Mathieu problem, the relic-band modes [1.6395, 10.8379] sit in stability GAPS (Re μ = 0, frozen) — vindicating the diabatic-freeze Ordered Veil — rather than resonance BANDS (Re μ > 0, re-pumped).
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w3.md` §W3-2 (FORWARD INTRA-INVESTIGATION PIN on the W3-1 npz; consumes {E_k, ω_k, |β_k|²}).

**Output Artifacts** (closure-verification checklist):
- `script` — `computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.py` ✓ (29,857 bytes). must_contain confirmed: `from canonical_constants import M_KK, Delta_BCS, tau_fold`; `def print_verdict_payload(...)` defined + called (the script PRINTS the payload, never writes the verdict file).
- `data` — `computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.npz` ✓ (242,502 bytes). All plan-required keys present (verified): `k_grid (2000,), Re_mu (2000,), Im_mu (2000,), A_k (2000,), q_Mathieu (2000,), tr_monodromy (2000,), resonance_band_mask (2000,), fraction_resonance=0.0, zone_centers (6,), pair_band (2,)`. Plus the verdict-bearing discrete-relic arrays `E_k, omega_k, beta2_k, mult_k, A_relic, q_relic, Re_mu_relic, Im_mu_relic, tr_relic, relic_resonance_mask, frac_resonance_weighted` and the n-aware zone diagnostics `nearest_n, dist_to_zone_A, tongue_halfwidth_relic, in_principal_tongue, in_n1_width_crude, n_zone_crossing, n_crude_n1, n_tail_cross_s101, i_closest`.
- `plot` — `computations/investigation-12/inv12_w3_2_floquet_ordered_veil_resonance.png` ✓ (329,243 bytes): (a) Re μ(2E) across the S101 pair band with resonance bands shaded + relic-mode 2E_k marked + zone centers 2E=n·ω_q; (b) stability discriminant |Tr M|−2 (>0 band, <0 gap); (c) per-mode |A−n²| vs the n-aware (q^n-scaled) tongue half-width; (d) locked |β_k|² occupation vs 2E_k colored by band/gap.
- `verdict_line` — `computations/investigation-12/inv12_gate_verdicts.txt` matching `^INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE:.* audit_sha256=[a-f0-9]{64}` ✓ (dual-SHA companion row present; schema_v2 3-tuple NOT required — trigger `[VERIFY]`, not `[SIGN]`).
- `wp_section` — this §W3-2 (Status COMPLETED / Verdict PASS / Output Artifacts / MCP Pre-Compute Audit all present).
- Forward-pin resolution: `inv12_w3_1_relic_spectrum_ode_lock.npz` PRESENT at runtime (SHA `323f1c74a9fc8bbc…`); W3-1 closed INFO (integrator-LOCK achieved, per-mode {β_k} integrator-independent) so W3-2 proceeds on the verified per-mode spectrum. The W3-1 truncation band does NOT propagate into this verdict — the verdict is per-mode (each mode's monodromy), cutoff-robust; see Results.

**MCP Pre-Compute Audit** (query-first; one-line salient returns; NOT pre-closed):
- `search_knowledge("Floquet Mathieu stability gap relic resonance Ordered Veil")` → surfaced `ORDERED-VEIL-SUBSTRATE-CLOCK: value=5251.82 (R_therm)` + The Ordered Veil (S38) PROVEN "the transit IS the physics" — the diabatic-freeze result this gate stress-tests against in-band resonance. NOT a Floquet closure; gate is open.
- `trace_entity("S101 VII.BP COINCIDENCE-BOUNDED in-band resonance")` → no direct trace by that name; the tension is captured in the S101-W1-QEQ-RELIC-ODDFLOOR verdict (next query).
- `search_knowledge("omega_q_phys 2.012813 …")` → `S101-W1-QEQ-RELIC-ODDFLOOR: FAIL_IN-band_resonance-LIVE: omega_q_phys=2.012813 in_band[1.6395,10.8379]; gamma=29.753211; Delta_res_occ=0.000046<guard0.1; tail_crossing=24modes_14occ; oddratio=2.6976e-02` — the exact in-band COINCIDENCE this gate adjudicates with the FULL Floquet band structure.
- `search_knowledge("s87 Re(mu)=0 stability gaps …")` → `Re(mu)=0 in stability gaps` (s87-pixelation-lock + investigation-10-plan-w2): "Re(μ_F)>0 in the resonance band (parametric amplification), Re(μ_F)=0 in the stability gaps" — confirms the monodromy-trace dichotomy. Documented structural anchor, NOT a canonical import.
- `search_knowledge("s63 mu_broad 1.790887 …")` → `mu_broad = 1.790887 M_KK` (s63_ab_parametric_output.txt) "Non-perturbative growth rate" + the `q_conservative=3e-3 → q_broad~1` regime note. Documented broad-resonance anchor; here the substrate q_M ~ 5e-3 ≪ 1 (narrow regime), so mu_broad is the q~1 contrast scale, NOT a value imported.
- `get_constant("M_KK")` → 7.428660e16 GeV (S42, CONST-FREEZE-42); `get_constant("Delta_BCS")` → 0.4642547 (S70, R-PROTECTED) — both consumed as canonical imports.
- Drive-amplitude pin (from my own S101 QEQ-RELIC-ODDFLOOR canonical record): `h_par = 8.3e-4` (FULL Mathieu modulation depth, guard-floor-dominated; h_par = q_osc/(λ_k²+q̄)); crossing geometry E_k∈[0.820,0.873], 24 tail-crossing modes, 14 occupied.

**Verdict**: **PASS** — value `fraction_resonance=0.000000e+00` (0 of 1248 relic modes in resonance bands; max |Tr M|=1.99999996 < 2), scheme=FW, convention=ABSOLUTE-Floquet-monodromy-width-aware-h_par, L_max=10. audit_sha256=`59b0b64370c2a877d97e899f80dbdc1e849e2b6310e1403adbe3b2e6672416f4`, content_sha256=`a0672a0f95888cb4d1035effd48f1c762fdf69626e679ebf47802898f25e79c2` (emitted via `emit_verdict`, track=investigation; dual-SHA companion + 6 detail rows).

**Results**:

*Governing structure (mode equation → monodromy Floquet decision):*
The post-fold modulus (the residual ringing of the Jensen deformation parameter τ at ω_q^phys = 2.012813 M_KK) drives each relic mode as a parametric oscillator. Writing the mode equation as a Hill equation in Mathieu standard form with drive phase z = (ω_q/2)·t:

> `u_k'' + [A_k − 2 q_M cos(2z)] u_k = 0`,  `A_k = (2E_k/ω_q)²`,  `q_M = A_k · h_par/2`

The verdict is decided by the **monodromy matrix** M(k) (the 2×2 map advancing (u, u′) over ONE drive period T = 2π/ω_q). The bare Hill equation has no friction, so by Liouville `det M = 1` and the two Floquet multipliers are a reciprocal pair `e^{±μT}`. The gap/band dichotomy follows from `|Tr M|` ALONE:
- `|Tr M| < 2` ⇒ multipliers on the unit circle ⇒ **Re μ = 0** (STABILITY GAP, frozen);
- `|Tr M| > 2` ⇒ real reciprocal pair, one with |multiplier|>1 ⇒ **Re μ = (1/T)·arccosh(|Tr M|/2) > 0** (RESONANCE BAND, exponential re-pumping).

The Ordered Veil survives its own resonance iff every relic-band mode lands in a gap.

*Floquet band structure (the core deliverable):*
- **fraction_resonance = 0.000000** (0 of 1248 unique relic modes in resonance bands; PASS iff =0). ✓
- **max Re μ over all 1248 relic modes = 0.000000 M_KK** — every relic mode is frozen.
- **max |Tr M| over relic modes = 1.99999996 < 2** — the closest mode *grazes* the band boundary but never crosses it.
- Continuous-grid scan (2000 points across the full S101 pair band [1.6395, 10.8379]): max Re μ = 0, zero grid-points in any band. The entire pair band is one stability gap at this drive amplitude.
- **Liouville cross-check**: max |det M − 1| = 2.9e-11 (grid), 1.9e-11 (relic) — the DOP853 monodromy integration (rtol=1e-10) preserves the Wronskian to ~1e-11, confirming the 2×2 fundamental-solution propagation is faithful.

*Why the in-band COINCIDENCE deposits zero re-pumping (the substrate-physics point):*
The S101 frequency coincidence is real and reproduced — ω_q^phys = 2.012813 sits inside the band [1.6395, 10.8379], and a coarse |2E_k − ω_q| < 0.5 count returns 21 near-resonant modes (consistent with the S101 anchor of 24 tail-crossing, 14 occupied). But a frequency coincidence is **necessary, not sufficient** for re-pumping: the drive amplitude must also open an instability tongue *wider* than the mode's detuning. It does not. The Mathieu depth `q_M = A_k·h_par/2 ≤ 5.25e-3 ≪ 1` puts the system deep in the **narrow-resonance regime**. The n-th instability tongue at A_k = n² has small-q half-width (Sage-verified, McLachlan/DLMF 28.6):

> n=1: `q` ; n=2: `q²/4` ; n=3: `q³/64`

The single relic mode closest to any zone sits near **n=3** (A = 9.000371 ≈ 3²), with detuning |A−9| = 3.712e-4. The true n=3 tongue half-width there is `q³/64 = 1.628e-9` — the mode is **2.28×10⁵ half-widths away**, utterly deep in the gap. (A crude n=1-width estimate `|A−n²| < q` would mislabel this single mode as "in band"; the n-aware width and the exact monodromy both correctly place it in the gap. The crude-vs-n-aware discrepancy was caught and corrected in-session — the diagnostic now agrees bit-for-bit with the monodromy ground truth: n-aware tongue count = 0, crude n=1 count = 1.)

*Cross-check anchors (documented, NOT canonical imports):*
- **s87 `Re(μ)=0 in stability gaps`** (structural): reproduced exactly — the monodromy-trace dichotomy is the s87 statement made quantitative on the relic band.
- **s63 `mu_broad = 1.790887 M_KK`** (broad-resonance growth scale): this is the q~1 (broad) non-perturbative growth rate. Here q_M ≤ 5.25e-3 ≪ 1 (narrow), so mu_broad is the CONTRAST scale showing how far from broad-resonance the substrate sits — re-pumping at the broad rate would require h_par ~ O(1), 3 OOM above the canonical 8.3e-4 (consistent with the s87 `q_conservative=3e-3 → q_broad~1` note that drifting to broad needs a ~2 OOM pump-amplitude increase).
- **Width-aware drive (S100a W-1 D-2 lesson, pinned in convention)**: the tongue WIDTH is set by the FULL Mathieu depth q_M (∝ h_par), NOT by the suppressed rectified-force amplitude φ_k (which governs throughput only). This gate honors that lesson AND sharpens it: the width is additionally n-dependent (q^n-scaled), so even the principal-width-aware estimate over-counts at n≥2 zones. The monodromy Tr M is the ground truth regardless of the analytic width estimate.

*4-tuple*: (value=fraction_resonance=0.0, scheme=**FW** [Hill equation A_k=(2E_k/ω_q)², q_M=A_k·h_par/2], convention=**ABSOLUTE-Floquet-monodromy-width-aware-h_par**, L_max=**10**).

*Dual-prior re-allocation (plan §W3-2)*: prior (Track A 0.55 / Track B 0.45). **PASS → 0.9 to Track A**: the relic-band modes sit in stability GAPS; the Ordered Veil survives its own in-band modulus resonance; the diabatic-freeze argument (R_therm=5251.82, S_ent=0) is vindicated against the S101 §VII.BP in-band-crossing tension. The S101 "in-band single-frequency check" was indeed reading a frequency coincidence as live resonance without the full band structure — exactly the Track-A reading.

*Constraint-map consequence*: This converts the S101 §VII.BP **COINCIDENCE-BOUNDED** euphemism into a **computed Floquet verdict**. The S101-W1-QEQ-RELIC-ODDFLOOR `{IN-band: resonance LIVE}` end-state is now resolved: the resonance is live as a *frequency coincidence* but deposits *zero* exponential re-pumping into the relic band (Re μ = 0 for all modes; the drive amplitude h_par = 8.3e-4 is 3 OOM too weak to open a tongue wider than any relic mode's detuning). The C1 Ordered-Veil-survival contradiction (survey R2) is RESOLVED in favor of Side A: the relic, once frozen by the diabatic transit, is NOT re-disturbed by the modulus' afterglow. This feeds the W4-1 A_s wall workshop (the relic survives intact → A_s overproduction is a genuine amplitude, not a post-transit re-pumping artifact) and removes the dilution-rate-vs-resonance-rate comparison from the critical path (no resonance to outrun). The result is per-mode and cutoff-robust, so the W3-1 INFO truncation band does NOT propagate into this verdict. Artifacts: `inv12_w3_2_floquet_ordered_veil_resonance.py/.npz/.png`.

---

### §W3-3. INV12-W3-3-BACK-REACTION-CLOSURE-HSQ (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W3-3-BACK-REACTION-CLOSURE-HSQ`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (effective-Friedmann back-reaction closure — the framework's #1 transit-side gap, G2)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The effective-Friedmann closure H²_eff(τ) = (8πG_eff/3)ρ_relic(τ) + Λ_eff, sourced by the FULL locked relic energy density ρ_relic = Σ_k E_k|β_k|² (NOT the 8-mode BCS source, the WRONG object per T6 FAIL at 133,200× overwhelm), yields a deceleration parameter q_eff(τ) that lands WITHIN the SCALE-FACTOR-54 band (q: −0.97 → +0.81).
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w3.md` §W3-3 ([SIGN] substitution chain; FORWARD INTRA-INVESTIGATION PIN on the W3-1 npz ρ_relic; `schema_v2_3tuple_required: true`).

**Output Artifacts** (closure-verification checklist):
- `script` — `computations/investigation-12/inv12_w3_3_back_reaction_closure_hsq.py` (40,293 B). `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (`from canonical_constants import (` line 88; `def print_verdict_payload(` line 393). ✓
- `data` — `computations/investigation-12/inv12_w3_3_back_reaction_closure_hsq.npz` (45,341 B). Plan-required keys ALL PRESENT (verified `np.load`): `tau_grid, H_eff_sq, q_eff, rho_relic_tau, Lambda_eff, G_eff, q_band_lo, q_band_hi, max_excursion, T6_8mode_overwhelm` (+ truncation-band, two-reading, and comparator keys). `T6_8mode_overwhelm = 133200.0` ✓. ✓
- `plot` — `computations/investigation-12/inv12_w3_3_back_reaction_closure_hsq.png` (122,657 B). Left: q_eff(τ) Reading-A/B + trunc-band, SCALE-FACTOR-54 band [−0.97,+0.81] shaded, s54 comparator, τ_fold marked; right: Ω_relic(τ) + ρ_relic(τ) dilution. ✓
- `verdict_line` — `computations/investigation-12/inv12_gate_verdicts.txt`, canonical line matches `^INV12-W3-3-BACK-REACTION-CLOSURE-HSQ:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=7952dc072cb8470e07bb7649ccc6b584f7de16b83e51f2e89e58e57c52d3fce5`); dual-SHA companion row present; schema_v2 [SIGN] 3-tuple row present (`# sign_verdict=PASS magnitude_verdict=INFO regime_verdict=MARGINAL`); composite-precedence disclosure row present. ✓
- `wp_section` — this §W3-3 (Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit all present). ✓

**MCP Pre-Compute Audit** (queries run BEFORE writing the script):
- `get_constant("a_2_FW_zeta")` → **2776.165389** (S88, regulator a_2^{ζ}; gate S88-A-N-FW-CANONICALIZATION). The Sakharov G_eff leg.
- `search_knowledge("SCALE-FACTOR-54 deceleration band Connes distance proxy")` → gate **SCALE-FACTOR-54** | PASS | `q: −0.97 → +0.81` (Connes-distance proxy; NOT a_eff per II.1). Also surfaced **S95-W4-4** INFO: "a2_proxy_q OUT of band; only Connes proxy reproduces band" — the live tension.
- `trace_entity("SCALE-FACTOR-54")` → confirmed the band IS the deceleration parameter of the Connes-distance growth; `s54_scale_factor.npz` present with q(τ) running −0.97323 → +0.81438, q_at_fold=−0.786, a_at_fold=2.117.
- `search_knowledge("Sakharov induced Newton constant G_eff a_2 channel E30")` → `G_eff^{-1}=Λ²f₂a_2(D_K)` (PB-8); `M_Pl_eff²=a_2^{ζ}/(48π²)` (S100b-plan-w7 chain); `G_N=1/(16π a_2 M_KK²)` (cc-path-a).
- `search_knowledge("T6 Friedmann BCS lock 8-mode source overwhelm 133200")` → gate **T6** | BROKEN | `133,200×` overwhelm (atlas-04/S39 FRIED-39: spectral action 155,984 modes overwhelms BCS 8 modes; "recast as back-reaction-closure gap §II.4").
- `search_knowledge("DILUTION-CC Volovik tracking vacuum dilution effacement w")` → **DILUTION-CC** PROVEN (114-OOM CC gap closed; ρ_vac/ρ_obs=1.032); session-96-plan-w1 canonical two-fluid: **ρ_n (GGE relic, w=0 dust)** + ρ_s (effacement residual, w=−1). PRE-CLOSED check: NO closure covers this back-reaction-closure gate (G2 is OPEN; T6 is BROKEN-not-closed).
- `get_constant("M_KK_gravity")` → 7.4287e16 GeV (S42); `Gamma_effacement` → 0.99970 (S37).

**Verdict**: **INFO** (composite) — `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=MARGINAL`.
- 4-tuple: `(value=max_excursion=0.000000_q_band_traversal_n_eff=3.0000, scheme=FW-effective-Friedmann, convention=ABSOLUTE-Connes-proxy-q, L_max=10)`, `regulator_pin=a_2^{ζ}`.
- `audit_sha256=7952dc072cb8470e07bb7649ccc6b584f7de16b83e51f2e89e58e57c52d3fce5`, `content_sha256=82e8f04648acea5fd414ae9134fce68301190782e587d5e703d181cf1afe3c14`.

**Results**:

**Pre-flight — the 8-mode BCS source is the WRONG object (T6 FAIL confirmed).** ρ_relic = Σ_k mult_k E_k|β_k|² reproduces the locked-npz `rho_relic` to **0.00e+00** relative (1248 unique modes, 20,064 with multiplicity). The documented T6 overwhelm is **133,200×** (atlas-04/S39 FRIED-39); the spectral-action/BCS mode-count ratio (155,984/8 = 19,498×) is reported as the structural anchor. Conclusion: the BCS pairing source is a fiber-internal Ricci-type correction, not the cosmological relic energy — the correct source is the full locked spectrum ρ_relic.

**Effective Friedmann assembly.** Sakharov a_2 channel (E30): M_Pl_eff² = a_2_FW_zeta/(48π²) = **5.860091** M_KK² ⇒ 8πG_eff = 1/M_Pl_eff² ⇒ **G_eff = 6.789781e−03**. Substrate scale factor a(τ) taken from SCALE-FACTOR-54 (a/d_mean = 1.0085 const ⇒ a(τ) IS the Connes-distance growth; the SAME object whose Connes-proxy q carved the band). Λ_eff anchored at the LATE-end effacement floor (q→Q_BAND_LO), NOT fit to the s54 q-curve: Λ_eff(lo ρ)=8.934911, Λ_eff(hi ρ)=15.564234.

**[SIGN] substitution chain WITH substituted numbers** (Sage-verified, exact-rational):
- Step 1: ρ_relic(τ) = Σ_k mult_k E_k|β_k|²(τ) = **15.4140** (p+q≤7) M_KK⁴ units [full locked source; NOT ρ_BCS^(8)].
- Step 2: G_eff = 1/(8π·M_Pl_eff²), M_Pl_eff² = a_2_FW_zeta/(48π²), a_2_FW_zeta = **2776.165389** ⇒ G_eff = **6.789781e−03**.
- Step 3: H²_eff(a) = (8πG_eff/3)ρ_relic(a) + Λ_eff, relic = w=0 dust ⇒ ρ_relic(a) ∝ a⁻³.
- Step 4: q_eff = −1 − Ḣ_eff/H_eff² = (3/2)Ω_relic − 1 (dust+vacuum).
- Step 5: ρ̇_relic < 0 (relic dilutes) ⇒ the relic term raises q above the pure-Λ floor. Sage-exact: **q − (−1) = ½·C·n·ρ₀/(Λaⁿ + Cρ₀) > 0** (C,n,ρ₀,Λ all > 0). DIRECTION: a diluting positive-energy relic **DECELERATES** (q raised above −1). Computed: q_eff(early, relic-dom) = **−0.854212**, q_eff(late, vac-dom) = **−0.970000** ⇒ relic-dominated end decelerates more. **sign_verdict = PASS.**

**Band containment + the two-reading w-ambiguity** (the magnitude finding):
- **Reading A (CANONICAL, GGE-as-dust, w=0, n=3)** — session-96-plan-w1 two-fluid assignment. Relic-dominated asymptote q = n/2−1 = **+0.5000** (IN band). q_eff(τ) ∈ [−0.970, −0.854] over the post-fold window ⇒ literal `max_excursion = 0.000000` (≤ band_tol=0.05). **BUT** this is a band-as-RANGE containment: the dust trajectory spans only **6.5%** of the band, hugging the lower edge, and the **upper edge +0.81 is STRUCTURALLY UNREACHABLE** — a sub-unity dust fraction caps q at +0.5 (Sage: q=+0.81 needs Ω_relic = 181/150 > 1, impossible). The upper ~40% of the band is unreachable by pure dust.
- **Reading B (kinetic gas, sensitivity)** — treating the BdG gap Δ=0.464255 as a rest mass gives energy-weighted KE fraction 0.8347 ⇒ n_eff = **3.8347**, w_eff = +0.2782, relic-dominated asymptote q = **+0.917337**, which **OVERSHOOTS +0.81** by 0.107 (> band_tol). Only contained over the finite window because Λ_eff caps it.
- **Truncation band**: ρ_relic = 15.414 (p+q≤7) → 26.851 (p+q≤8), rel 0.426 (W3-1 INFO band). Because q_eff = −1 − Ḣ/H² is INVARIANT under constant rescaling of H, the absolute-ρ band cancels in q_eff (sensitivity max|q_hi − q_lo| = 0.000000); the band enters only via the Λ_eff/ρ_relic ratio (the deposit/crossover anchor). max_excursion is robust to the truncation band.

**Structural theorem (Sage-exact, permanent).** For ANY two non-interacting diluting fluids `H² = c₁a^{−n₁} + c₂a^{−n₂}`, **dq/da ∝ −(n₁−n₂)² ≤ 0** — q is monotonically NON-INCREASING in a. With a constant-Λ (n=0) + diluting relic (n>0), q ALWAYS falls toward −1. SCALE-FACTOR-54 has q RISING (−0.97 → +0.81). Therefore the relic-back-reaction Friedmann q and the s54 Connes-distance-proxy q are **DIFFERENT observables** (sharpening S95-W4-4): the relic-Friedmann closure reproduces the band as a RANGE, NOT as the monotone-rising deceleration history. The rising-q history requires either ongoing relic energy production through the transit OR a faster-diluting effacement term (the DILUTION-CC tracking vacuum) — beyond a passive relic + constant Λ.

**Composite-precedence disclosure.** The plan §W3-3 operator (`q_eff ∈ band`, PASS iff max excursion ≤ band_tol) is ambiguous between LETTER (max_exc=0 ⇒ PASS) and INTENT (the closure REPRODUCES the band as a deceleration history). The letter gives a VACUOUS-MARGIN containment (trajectory in a 6.5% sliver, upper edge unreachable). Resolved to **INFO** per the substrate-faithful INTENT reading — disclosed via the `# composite-precedence:` companion row (gate-verdicts.md plan-frozen-operator precedence). The plan's own `INFO_meaning` pre-registers exactly this regime-conditional-partial-closure outcome ("q_eff stays within the band over part of the τ-window... regime-conditional; the honest status is a stated τ-window of validity"), so INFO is a pre-registered outcome, not a moved goalpost.

**Schema_v2 3-tuple + composite-collapse**: `sign_verdict=PASS` (relic decelerates, direction confirmed) ∧ `magnitude_verdict=INFO` (partial band reproduction, upper edge unreachable) ∧ `regime_verdict=MARGINAL` (band-span 6.5% < 50%; relic-Friedmann q is a valid output but is the band-as-range, not the deceleration-history the band encodes). Composite-collapse: `magnitude==INFO ⇒ composite=INFO`.

**Dual-prior re-allocation** (plan §W3-3): the INFO outcome maps to **unchanged** track weights (track_A 0.45 closure-achieved / track_B 0.55 loop-back-open). The closure is regime-conditional: the [SIGN] direction is right and the canonical-dust reading is contained (supporting track_A), but the band's decelerating upper portion is structurally unreachable by a passive relic + const Λ and the s54 rising shape is not reproduced (supporting track_B). Net: neither track strengthened; the partial closure is the honest middle.

**Constraint-map consequence.** G2 (the #1 transit-side gap: no derived a(t)/effective-Friedmann map) is **partially healed** at the effective-Friedmann level — the substrate-derived closure H²_eff = (8πG_eff/3)ρ_relic + Λ_eff with the CORRECT (full-relic, non-BCS) source produces a q_eff with the right SIGN (relic decelerates) and a canonical-dust trajectory contained in the lower band. C2/T6 (the dynamical loop-back) is advanced: the 8-mode BCS source is confirmed the wrong object (133,200×), and ρ_relic is the right one. C1 (τ = cosmic time) remains ASSUMED. The residual gap is now SHARP and named: (i) the relic equation of state (dust w=0 vs kinetic w=+0.28) is the open substrate-physics question deciding whether the relic-dominated asymptote lands at +0.5 (in-band) or +0.917 (overshoot); (ii) the s54 rising-q history is a DIFFERENT observable (Connes-distance proxy) from the relic-Friedmann q — reproducing the monotone-rising deceleration history requires ongoing relic production or a diluting (DILUTION-CC tracking) Λ, a forward compute. This feeds the INV12-W4-1 A_s wall workshop (the closure bears on whether A_s overproduction is real in a partially-closed effective-Friedmann) and the survey-R2 Ordered-Veil-survival rate inequality (which needs the H(τ) this gate provides).

---

### §W3-4. INV12-W3-4-GREYBODY-FROM-BDG (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W3-4-GREYBODY-FROM-BDG`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (analog-gravity greybody derivation — tests removal of the A_s tuning knob, A2)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The exit-horizon greybody Γ(ω) filtering the overproduced squeeze down to the observed A_s is DERIVABLE as the transmission coefficient through the effective Schrödinger potential of the linearized BdG fluctuation equation around the τ~0.16 exit horizon (analog-gravity, Steinhauer / Macher-Parentani) — NOT a fitted Pöschl-Teller — and the derived ∫Γ(ω)dω agrees with the fitted transmitted_fraction = 0.512 (S95 W4-3), collapsing the A_s band.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w3.md` §W3-4 (FORWARD INTRA-INVESTIGATION PIN on the W3-1 npz exit-horizon ω_k; CROSS-CHECK-ONLY read of the S95 fitted greybody npz).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):
- `script` — `computations/investigation-12/inv12_w3_4_greybody_from_bdg.py` ✓ (28,480 B). `grep -E 'from canonical_constants import|print_verdict_payload'` → both present (`from canonical_constants import (` line 97; `def print_verdict_payload(` line 152, called line 519 — the script PRINTS the payload, never writes the verdict file). Imports `kappa_exit, T_compound, Delta_BCS, A_s_CMB, M_KK, tau_fold`. ✓
- `data` — `computations/investigation-12/inv12_w3_4_greybody_from_bdg.npz` ✓ (159,008 B). All plan-required keys PRESENT (verified `np.load`, zero missing): `omega_grid (2000,), Gamma_derived (2000,), V_eff (4000,), x_tortoise (4000,), integral_Gamma_derived=0.036265, transmitted_fraction_fitted=0.511872, agreement=0.929152, A_s_band_derived (2,), A_s_band_fitted (2,), band_collapse_ratio=0.246920`. Plus the bracket/cross-check arrays `Gamma_derived_tcomp, integral_Gamma_tcomp=0.835892, flat_band_avg, kappa_eff=47.6146, V0_marginal=566.7875, V0_tcomp, omega_check, gamma_ode_check, gamma_closed_check, ode_vs_closed=1.131e-09, omega_k, Gamma_at_modes, w_mode, omega_grid_fit, Gamma_grid_fit`. ✓
- `plot` — `computations/investigation-12/inv12_w3_4_greybody_from_bdg.png` ✓ (91,851 B): (left) derived Γ(ω) (BdG V_eff, κ_eff=κ_exit=47.6) + the V_0=T_compound² bracket + the FITTED Pöschl-Teller (S95 W4-3) over the relic band, with the fitted band-support shaded; (right) transmitted-fraction bar chart fitted 0.512 vs derived 0.036 vs bracket 0.836 with the agreement/verdict annotation. ✓
- `verdict_line` — `computations/investigation-12/inv12_gate_verdicts.txt`, canonical line matches `^INV12-W3-4-GREYBODY-FROM-BDG:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=a770882b2e1061941173dce0e11ae9958410e7f770716059dd719692c24cb651`); dual-SHA companion row present; schema_v2 3-tuple NOT required (trigger `[VERIFY]`, no `[SIGN]` directional pre-reg per plan `schema_v2_3tuple_required: false`); 4 detail rows present (regulator_pin, derived-greybody PRIMARY, fitted-comparator-PLACED, inv-4 cross-ref). ✓
- `wp_section` — this §W3-4 (Status COMPLETED / Verdict FAIL / Output Artifacts / MCP Pre-Compute Audit all present). ✓
- Forward-pin resolution: `inv12_w3_1_relic_spectrum_ode_lock.npz` PRESENT at runtime (SHA `323f1c74a9fc8bbc…`); W3-1 closed INFO (per-mode {β_k} integrator-LOCKED). The S95 fitted-greybody npz `computations/session-95/s95_w4_3_hawking_greybody_as.npz` (SHA `6f9cda9bd28ad0c4…`) was read CROSS-CHECK-ONLY (no write to any session-track file). The W3-1 truncation band does NOT propagate — the greybody Γ(ω) is per-frequency (a barrier transmission), independent of the relic-amplitude normalization.

**MCP Pre-Compute Audit** (query-first; one-line salient returns; NOT pre-closed):
- `search_knowledge("Hawking greybody transmitted fraction 0.512 A_s exit horizon")` → surfaced the provenance of `w4_3_hawking_greybody_as` (S95) + the equation `A_s = (produced squeeze at fold) × ∫ Γ(ω) dω` (phonic-exflation-equation-hawking-collab) — confirms the greybody is a MULTIPLICATIVE filter on the produced squeeze; the gate is OPEN (no closure covers the derived-vs-fitted comparison).
- `search_knowledge("analog gravity greybody factor BdG fluctuation potential acoustic white hole transmission")` → `Acoustic white hole — PROVEN S85` (causal-disconnect formalized, pre/post-fold separated) + `T_acoustic=0.112 M_KK; S43/S95 greybody machinery (Γ(ω) transmission)`. The acoustic white-hole exit horizon is the substrate object whose near-horizon barrier I transmit through. Documented structural anchor, NOT a pre-closure.
- `get_constant("A_s_CMB")` → **2.1e-9** (Planck 2018 VI; S96-OBS-ANCHOR-HYGIENE) — the observational anchor the A_s band brackets.
- `get_constant("Delta_BCS")` → **0.4642547** (S70, R-PROTECTED; OES/pair-addition gap) — the BdG dispersion gap (`ω_k=sqrt((λ²−μ²)²+Δ²)` floor; consumed as canonical import).
- `get_constant("T_acoustic")` → 0.112 (GGE acoustic temperature, S42/S47) — the acoustic scale, contextual.
- Inspected the fitted comparator `s95_w4_3_hawking_greybody_as.npz` directly (CROSS-CHECK read): `transmitted_fraction=0.5119`, `gamma_min=0.0414`, `gamma_max=0.9586`, `omega_peak=0.9418`, `lam_barrier=0.2440`, `A_s_band [3.11e-9,4.27e-9]→filtered [3.213e-9,4.167e-9]`. Inspected the S95 W4-3 SCRIPT: the fitted Γ is a sigmoid `1/(1+exp(−2π(ω−ω_peak)/lam))` with **ω_peak = 0.5(ω_min+ω_max) = support midpoint** and **lam = support width** (script lines 300–317; the script's own comment notes the literal curvature λ=T_compound=7.578 "transmits ~uniformly" because the support sits far below T_compound, so the barrier was re-localized to the band).
- `get_constant("kappa_exit")` → **47.6146** M_KK (S95; "Exit-horizon surface-gravity analog; a_4 BCS condensation-energy gradient barrier height; T_exit=κ/2π=7.5781=T_compound; Substrate-first pre-promotion for INV4-W1-4-EXIT-GREYBODY"). Confirmed DERIVED (S95-W4-2-HAWKING-ANALOG-T-LEDGER PASS, Visser κ=½d_n(c²−v²)|_exit, corpus dev 0.0000) — this IS the substrate barrier scale (inverse tortoise width); NOT a fit.

**Verdict**: **FAIL** — value `derived_int_Gamma=0.036265; fitted_0.512=0.511872; agreement=0.929152 (≫ agree_tol=0.10); band_collapse_ratio=0.246920 (> collapse_tol=0.10); agree_pass=False; collapse_pass=False`, scheme=FW, convention=ABSOLUTE, L_max=10. `audit_sha256=a770882b2e1061941173dce0e11ae9958410e7f770716059dd719692c24cb651`, `content_sha256=50dc478080134b5cb71efaf56e2ce6f91d7906116df894005bc36e39c9bc5847` (emitted via `emit_verdict`, track=investigation; dual-SHA companion + 4 detail rows). **This is an HONEST, informative FAIL** (per `math-scripts.md §"All Results Are Good Results"`): it EXPOSES the fitted greybody as a tuning knob rather than removing it — the expected Track-B outcome (prior 0.60).

**Results**:

*Governing structure (BdG fluctuation → tortoise-coordinate scattering → greybody):*
The linearized fluctuation δφ_k around the τ~0.16 acoustic white-hole exit-horizon background reduces, in a tortoise coordinate x_* (horizon at x_*→−∞), to a 1D Schrödinger scattering problem:

> `−d²ψ/dx_*² + V_eff(x_*) ψ = ω² ψ`,  `V_eff(x_*) = V_0 sech²(κ_eff x_*)`

This is the universal analog-gravity near-horizon form (Macher-Parentani 0903.2224; Steinhauer 1510.00621 measured the corresponding BEC analog spectrum). The greybody is the barrier transmission `Γ(ω) = |T(ω)|²`. The Pöschl-Teller transmission has the EXACT closed form (Landau-Lifshitz QM §25; Sage-verified limits `Γ(ω→0)=0` reflective, `Γ(ω→∞)=1` transmissive, monotone increasing):

> `Γ(ω) = sinh²(πω/κ_eff) / [ sinh²(πω/κ_eff) + cosh²(π·s) ]`,  `s = sqrt(V_0/κ_eff² − 1/4)`

*The two barrier parameters are SUBSTRATE-FIXED, NOT placed at the band (the load-bearing point):*
- **κ_eff = κ_exit = 47.6146 M_KK** — the exit-horizon surface gravity (Visser `κ=½d_n(c²−v²)|_exit`; S95-W4-2 PASS, corpus dev 0.0000; the a_4 BCS condensation-energy gradient barrier). This IS the inverse tortoise width.
- **V_0 = κ_exit²/4 = 566.7875 M_KK²** (PRIMARY, marginal over-barrier s=0: the white-hole exit's only near-horizon energy scale is the surface gravity itself). A second substrate reading `V_0 = T_compound² = 57.43 M_KK²` (the Hawking-analog temperature scale) is carried as a bracket. **Neither is placed at the relic band.**

*Method validation (independent scattering ODE vs closed PT):*
An INDEPENDENT 1D scattering-ODE solve through V_eff(x_*) (DOP853, rtol=1e-9, N_x=4000, tortoise window x_max=12/κ_eff) — imposing a transmitted-only wave on the left, decomposing into incident+reflected at +x_max — reproduces the closed-form Pöschl-Teller transmission to **max abs dev = 1.131e-09** across ω ∈ {0.941, 2.33, 3.72, 95.2 M_KK} (the last well above κ_eff). The derived Γ is genuinely a scattering output, not an asserted profile. `regime_verdict = VALID` (method consistent).

*The discriminating numbers (derived vs fitted):*
- **Derived squeeze-weighted ∫Γ_derived dω (PRIMARY, V_0=κ_exit²/4) = 0.036265** vs fitted **0.511872** ⇒ **agreement = 0.929152 ≫ 0.10**. The half-transmission frequency is `ω_½ = √V_0 = 23.81 M_KK`, sitting **6.4× ABOVE** the relic band's upper edge (3.72 M_KK). The surface-gravity barrier reflects ~96% of the relic band: `Γ(ω_min=0.941)=0.0038`, `Γ(ω_mid=2.33)=0.017`, `Γ(ω_max=3.72)=0.058`.
- **Bracket reading (V_0=T_compound²): ∫Γ_derived dω = 0.835892** ⇒ agreement 0.633. Transmits ~84% of the band. The two substrate readings **BRACKET 0.512 (0.036 < 0.512 < 0.836) but neither reproduces it** — there is no substrate-derived barrier scale at the band.
- **A_s band-collapse: band_collapse_ratio = 0.246920 > 0.10**. Applying the derived greybody at the relic-band edge frequencies gives derived A_s band width 2.354e-10 vs the fitted-filtered 9.532e-10; the ratio 0.247 does NOT meet the ≤0.10 collapse criterion (and the derived "narrowing" is a scale artifact of near-total reflection, not a genuine pinning to a point).

*Why the derived greybody cannot reproduce the fit (the substrate-physics point):*
The fitted comparator placed `ω_peak = 0.5(ω_min+ω_max) = 0.9418` (the relic-band support MIDPOINT) and `lam = 0.2440` (the support WIDTH). With those choices the sigmoid crosses 0.5 EXACTLY at the band midpoint and rises 0→1 across the band, forcing `∫Γ ≈ 0.5` **by construction**. The substrate barrier has slope `~π/κ_eff ≈ 0.066` per unit ω; the fit's slope is `2π/lam ≈ 25.8` per unit ω — **390× steeper**. A barrier whose inverse-width is the surface gravity (47.6 M_KK) is nearly FLAT across a band at ω~1–4 M_KK; it cannot produce the steep band-localized half-transmission the fit imposed. The fit's narrow width λ=0.244 is the **band width itself**, not any substrate scale — circular by construction (the script's own comment admits re-localizing the barrier to the band because the literal T_compound curvature "transmits uniformly").

*4-tuple*: (value=derived_int_Gamma=**0.036265**, scheme=**FW** [BdG fluctuation V_eff = V_0 sech²(κ_eff x_*) from ω_k=√((λ_k²−μ²)²+Δ_k²) at the exit horizon, κ_eff=κ_exit, V_0=κ_exit²/4], convention=**ABSOLUTE** [analog-gravity transmission Γ(ω)=|T(ω)|² via tortoise-coordinate Schrödinger scattering, closed PT cross-checked by ODE to 1.1e-9], L_max=**10**). regulator_pin context: the barrier scale κ_exit is the a_4-channel surface gravity (S95-W4-2; Visser formula).

*Cross-check vs the S95 W4-3 fitted Pöschl-Teller (CROSS-CHECK ONLY):* the `.npz` was read read-only (no session-track mutation). The fitted `transmitted_fraction=0.5119` is reproduced exactly from the comparator file and is the FAIL comparator — the derived 0.036 (primary) / 0.836 (bracket) bracket it without matching.

*Dual-prior re-allocation (plan §W3-4)*: prior (Track A 0.40 / Track B 0.60). **FAIL → 0.9 to Track B**: the derived Γ(ω) does NOT match the fitted 0.512 and the A_s band does not collapse. The fitted Pöschl-Teller was doing tuning work the first-principles BdG barrier does not reproduce — exactly the Track-B reading ("a genuinely-independent derivation is unlikely to reproduce 0.512 exactly; an honest mismatch is itself informative — it shows the greybody was doing tuning work"). The prior anticipated this; the FAIL confirms it.

*Constraint-map consequence*: **A2 (the hidden greybody tuning knob) is EXPOSED, not removed.** The exit greybody cannot be derived from the BdG fluctuation potential at the value the A_s ledger needs: the substrate-derived barrier (κ_eff=κ_exit=47.6 M_KK) reflects ~96% of the relic band (∫Γ=0.036), while the bracket (V_0=T_compound²) transmits ~84% (∫Γ=0.836) — the fitted 0.512 sits between two substrate readings but at NO substrate-derived barrier scale. The A_s "prediction" therefore RETAINS a load-bearing fitted filter on the greybody side: A_s is `(produced squeeze, UNIFIED-AS-79 ledger) × (FITTED greybody 0.512)`, and the 0.512 is set by placing the barrier at the relic band it filters, not by substrate physics. This SHARPENS the INV12-W4-1 A_s wall workshop: the overproduction-vs-artifact adjudication must now account for the greybody being a fitted knob (the A_s band-collapse claim depends on a fitted filter). It also constrains the G4 compact-object QNM sector: the same near-horizon-fluctuation machinery gives QNM ringdowns at the surface-gravity scale κ_exit=47.6 M_KK (ω_½=23.8 M_KK), NOT at the relic-band scale — so a QNM-greybody for a localized compact object would live far above the relic band, consistent with this gate's finding. **CROSS-REFERENCE (do NOT merge)**: this greybody Γ(ω) is the SAME physical object as **inv-4 W1-4** (hawking exit-horizon greybody) but via DIFFERENT machinery — this gate is the analog-gravity BdG-fluctuation-potential derivation; inv-4 W1-4 is the black-hole-thermodynamics route. The two routes to the same greybody are an independent cross-check, not a duplication; if inv-4 W1-4 (thermodynamics) ALSO fails to reproduce 0.512, the two-route agreement that the fitted value is non-substrate is strong. Artifacts: `inv12_w3_4_greybody_from_bdg.py/.npz/.png`.

---

### §W3-5. INV12-W3-5-CF21-HTILDE-RECONCILE (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `INV12-W3-5-CF21-HTILDE-RECONCILE`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (A_s rate-limiter — the CF21 H̃-branch divergence, open since S82)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The CF21 H̃-branch divergence — the TD anchor H_tilde_canonical_TD = 5.9076e-3 sitting factor 1.57 above the substrate-baseline PASS window [4.599e-3, 4.829e-3] (centre 4.714e-3) — is reconcilable to ONE canonical horizon-exit reading by identifying which substrate-distance reading is the physical H̃; the atlas figure discrepancy (4.56-OOM vs 2.38-OOM) is a resolvable bookkeeping inconsistency; and via CC3 (d ln A_s/d ln H̃ = +2, machine-ε) the factor-1.57 in H̃ IS the A_s overproduction rate-limiter.
**Plan reference**: `sessions/investigation/investigation-12/investigation-12-plan-w3.md` §W3-5 (independent of W3-1 — consumes only canonical constants + CC3 + the two atlas figures; ledger/figure reconciliation, NOT a new substrate compute).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML per `.claude/templates/r3-yaml-gate-block.yaml`):

| Artifact | Path | must_contain check |
|:---------|:-----|:-------------------|
| `script` | `computations/investigation-12/inv12_w3_5_cf21_htilde_reconcile.py` | `from canonical_constants import` ✓ + `print_verdict_payload` ✓ (both grep-confirmed) |
| `data` | `computations/investigation-12/inv12_w3_5_cf21_htilde_reconcile.npz` | keys present: `H_tilde_TD`, `H_tilde_baseline_centre`, `H_tilde_window`, `A_s_at_TD`, `A_s_at_baseline`, `cc3_derivative`(=2.0), `A_s_ratio_from_Htilde`(=1.5705), `ledger_compensation`, `oom_figure_456`, `oom_figure_238`, `figure_identification`, `canonical_reading_selected`, `divergence_is_structural` ✓ |
| `plot` | `computations/investigation-12/inv12_w3_5_cf21_htilde_reconcile.png` | A_s vs H̃ +2 log-slope panel + TD/baseline/LI markers + Planck band + figure-reconciliation bar panel ✓ |
| `verdict_line` | `computations/investigation-12/inv12_gate_verdicts.txt` | `^INV12-W3-5-CF21-HTILDE-RECONCILE:.* audit_sha256=[a-f0-9]{64}` ✓; companion dual-SHA row present; schema_v2 3-tuple NOT required (trigger `[VERIFY]`, not `[SIGN]`) |
| `wp_section` | this §W3-5 | Status COMPLETED / Verdict / Output Artifacts / MCP Pre-Compute Audit ✓ |

Independent of W3-1 (no forward-pin); dispatched in parallel. Verification by content presence (regex), NOT line/byte counts.

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("CF21 H_tilde branch divergence horizon exit A_s rate limiter")` | **CF21 STILL OPEN, figure drifted → 4.56-OOM** (atlas-08-freshness-S97); "rate-limiting open question for A_s closure since S84 retracted branch-(iv)"; equation `H_tilde_PASS = H_tilde_old·sqrt([1.995e-9,2.205e-9]/3.299e-9)` confirms CC3 inversion. NOT pre-closed — this gate is the reconciliation. |
| `trace_entity("CC3 d ln A_s d ln H_tilde")` | eq_5505: "CC3: d(ln A_s)/d(ln H_tilde) = +2 ⇒ A_s(H_tilde_new)=A_s_old·(H_tilde_new/H_tilde_old)²" — the EXISTING machine-ε identity, verified here not newly asserted. |
| `get_constant("H_tilde_canonical_TD")` | 0.0059076 (Branch-A TD/zeta anchor). |
| `get_constant("H_tilde_lo")` / `get_constant("H_tilde_hi")` | 0.004599 / 0.004829 (baseline PASS window; centre `H_tilde_center`=0.004714). |
| `get_constant("H_tilde_canonical_LI")` | 2.46411e-5 (Branch-B LI/SDW divergence-chase endpoint). |
| `get_constant("a_2_FW_zeta")` | 2776.165389 (S88; regulator a_2^{ζ}; cited for provenance). |
| `get_constant("c_sub_baseline")` | 2.238 (UNIFIED-AS-79 divisor). |
| `get_constant("A_s_CMB")` | 2.1e-9 (Planck 2018 VI; S96-OBS-ANCHOR-HYGIENE). |

NOT PRE-CLOSED: CF21 is an OPEN carry-forward (atlas-08 VIII / atlas-04 Summary). This gate produces the reconciliation. (Per `.claude/rules/knowledge-index-usage.md`.)

**Verdict**: **PASS** — `value='cf21_reconciled:cc3=2.000000_As_TD=3.2994e-09_ratioPlanck=1.5712_oomH_TDLI=2.3798_oomAs_TDLI=4.7595_fig238=Htilde-space_fig456=As-space-stale-live4.76_Hratio_TD_base=1.2532_sqrt157=1.2535_canonical_reading=BranchA-TD-MukhanovSasaki_structural=False'`
`scheme=UNIFIED-AS-79 convention=RATIO L_max=NA audit_sha256=c4daa505586e764300578d2ccbabadc715bbde5491af01d970f287e5b66894e3 content_sha256=068469f1bf73c46a303b02b95abf18c3dff8f5ea4378c7c526599b7b82ecc83b schema_version=S84+`

Dual-SHA companion + `regulator_pin=a_2^{ζ}` row + two reconciliation-detail rows emitted via `emit_verdict(track=investigation)`.

**Results**:

NUMBERS first. The reconciliation rests on a single observation: in the UNIFIED-AS-79 ledger `A_s = (H̃²/8π²)·(1/ε_H)·F_amp·(1/c_sub)·f_conv·S_IC`, **every factor except H̃ is branch-shared** (identical across the two H̃ readings). Therefore the A_s gap between any two H̃ readings is governed *exactly* by the CC3 log-derivative `d ln A_s/d ln H̃ = +2` — verified here, not asserted.

*Ledger evaluation (branch-shared factors ε_H=0.02163, F_amp_slot=0.388545, c_sub=2.238, f_conv=9.30e-4, S_IC=1):*

| H̃ reading | H̃ value | A_s | ratio/Planck | Δ_OOM | verdict |
|:----------|:--------|:----|:-------------|:------|:--------|
| Branch-A TD/zeta (Mukhanov-Sasaki) | 5.9076e-3 | **3.29944e-9** | **1.5712** | +0.1962 | PASS-F2 |
| Branch-B LI/SDW (divergence-chase endpoint) | 2.46411e-5 | 5.7403e-14 | 2.733e-5 | −4.5633 | FAIL-GT15 |
| Baseline window centre (CC3-inverted A_s-PASS target) | 4.714e-3 | 2.1009e-9 | 1.0004 | +0.0002 | PASS (by construction) |

A_s(TD) = 3.29944e-9 reproduces the S82 canonical 3.2994e-9 to **0.0011% rel-err** (cross-check PASS).

*(1) FIGURE RECONCILIATION (the two-place atlas inconsistency 2.38-OOM vs 4.56-OOM):* the figures live in **two different spaces**, which is the source of the confusion. Each is now identified with its ledger intermediate:
- **2.38-OOM** = the **H̃-space** TD-vs-LI gap: `log₁₀(5.9076e-3 / 2.46411e-5) = +2.3798` (matches atlas-08/S82-W-1 to |diff|=0.0002 ≪ fig_tol=0.05). **EXACT identification.**
- **4.56-OOM** = the **A_s-space** TD-vs-LI gap, but the atlas-04 printed figure is **STALE/rounded**. The live full-ledger value is `log₁₀(A_s(TD)/A_s(LI)) = +4.7595`, which equals the exact CC3 image `2 × 2.3798 = 4.7596` (CC3-vs-full-ledger consistency residual = 0.00e+00). atlas-04's 4.56 differs from the live 4.76 by 0.20 OOM. **Identified-as-A_s-space + stale-figure correction flagged: atlas-04 Summary should read ~4.76, not 4.56.**

*(2) CC3 PROPAGATION:* `d ln A_s/d ln H̃ = 2.0000000000` by central finite-difference (|diff from +2| = 4.66e-12 ≪ cc3_tol=1e-6) and by 10-point log-slope fit (|diff| = 3.50e-13). The substitution chain (existing identity, not new): `A_s = C·H̃²` with `C` = product of the five H̃-independent legs ⇒ `ln A_s = ln C + 2 ln H̃` ⇒ `d ln A_s/d ln H̃ = 2`. The ledger-compensation decomposition makes the rate-limiter mechanism explicit: bare `H̃²/8π² = 4.4201e-7` at TD; the fixed-leg product `(1/ε_H)·F_amp·(1/c_sub)·f_conv·S_IC = 7.46461e-3` is **H̃-INDEPENDENT**, so it cannot absorb the H̃² excess — the H̃ divergence passes **uncompensated** into A_s as H̃². This is precisely *why* CF21 is the A_s rate-limiter.

*Resolving the task's "factor 1.57":* the headline "factor 1.57" is the **A_s overproduction** (A_s(TD)/A_s_Planck = 1.5712), NOT an H̃ ratio. The corresponding H̃ excess is √1.57 = 1.2535 (CC3 inverse). The actual TD-vs-baseline-centre H̃ ratio is 5.9076e-3/4.714e-3 = 1.2532 (agreeing to 3 sig figs; the 0.0003 residual is because the baseline centre lands A_s at 1.0004×Planck, not exactly 1.0000). Forward: (H̃_TD/H̃_base)² = 1.5705 = the A_s overproduction via CC3 (+2). **The factor-1.57-in-A_s and the factor-1.25-in-H̃ are the same divergence at the two ends of the CC3 exponent.**

*(3) SUBSTRATE-DISTANCE READING SELECTION:* the two H̃ readings are substrate-distance-distinct evaluations of the SAME horizon-exit observable (SCALE-AND-CHANNEL-TAGGING, the same structure the framework uses for n_T and α_s, where which value a detector sees is set by the transport degree deg(T_BZ→pivot)). Selection:
- **Branch-B LI RULED OUT** as the canonical horizon-exit reading: A_s(LI) is FAIL-GT15 (Δ_OOM=−4.56, a ~4.5-OOM *under*production). It is the divergence-chase ENDPOINT, not a physical horizon-exit reading.
- **Branch-A TD SELECTED** as canonical: the substrate-native Mukhanov-Sasaki horizon-exit reading, PASS-F2 (Δ_OOM=+0.196, 1.57× Planck within factor-2).
- **Baseline window is NOT a competing reading**: it is the CC3-inverted H̃ that makes A_s land on the Planck band by construction — a *consistency target*, not an independent substrate derivation. TD anchor in baseline window = False (the divergence: TD sits factor 1.253 above the window centre in H̃).

⇒ **`divergence_is_structural = False`**: a single canonical horizon-exit H̃ reading IS namable (Branch-A TD/zeta Mukhanov-Sasaki, 5.9076e-3). The "factor 1.57" is the residual between the substrate-native reading and the A_s-PASS target — a *physical* overproduction (the A_s amplitude floor), not a branch ambiguity.

**4-tuple**: `(value=PASS, scheme=UNIFIED-AS-79 [five-factor ledger, Branch-A Zubarev/zeta, N_pivot=55], convention=RATIO [CC3 log-derivative=+2], L_max=NA [ledger at fixed L_max=10 inputs])`; `regulator_pin=a_2^{ζ}`.

**Dual-prior re-allocation**: PASS → **0.9 to Track A** (rate-limiter resolved at the H̃ level: a single canonical horizon-exit reading is named, the figure inconsistency is reconciled, CC3 is confirmed). Track-B prior (0.60, "divergence structural") is retired for the *branch-selection* question — but see the constraint-map consequence: the rate-limiter is resolved as a *reading-selection* matter, while the residual 1.57× A_s overproduction (the substrate amplitude floor) is a SEPARATE structural fact, not a branch ambiguity.

**Constraint-map consequence**:
- **C3 contradiction (H̃-in-A_s-ledger-vs-its-own-PASS-window) RESOLVED**: the TD anchor sitting outside the baseline PASS window is NOT a contradiction — the baseline window is the A_s-PASS target (CC3-inverted from Planck), the TD anchor is the substrate-native reading, and the gap between them IS the +0.196-OOM (1.57×) A_s overproduction. There is no "H̃ leg outside its own PASS window" inconsistency; there are two distinct objects (a substrate prediction and an A_s-PASS target) related by the CC3 exponent.
- **CF21 figure inconsistency RESOLVED + atlas-04 correction flagged**: 2.38-OOM = H̃-space TD-vs-LI gap (EXACT); 4.56-OOM = A_s-space TD-vs-LI gap but STALE — atlas-04 Summary should read ~4.76 (= 2×2.38, the exact CC3 image). Carry-forward: a one-line atlas-04 figure correction (4.56 → 4.76) is routed below.
- **The A_s rate-limiter is RELOCATED, not eliminated**: CF21 (the *branch divergence*) is resolved — there is one canonical horizon-exit reading. What remains is the substrate **A_s amplitude floor** (3.02×Planck per atlas-04 S83 / 1.57× here at N_pivot=55), a PERMANENT structural-position wall (atlas-04 Summary): the substrate genuinely overproduces A_s by a factor-1.5–3 from zero free parameters, within factor-2 of Planck (PASS-F2). This is a *prediction*, not a tuning failure. It feeds W4-1 sub-question (c): the transit honest-status "A_s bounded ~1.5–3 by a ledger whose H̃ leg sits outside its PASS window" is now sharpened — the H̃ leg is NOT "outside its PASS window" (that conflated the substrate reading with the A_s-PASS target); the honest status is "A_s overproduced by 1.57× via an uncompensated H̃² in a closed ledger, CC3-locked."
- **SCALE-AND-CHANNEL-TAGGING framing**: the TD/zeta and LI/SDW readings are at distinct substrate distances along the Mukhanov-Sasaki vs SDW derivation; the canonical horizon-exit reading is the TD/zeta Mukhanov-Sasaki one, the same way the canonical α_s at the CMB pivot is the Goldstone reading (≈0) and the inside-BZ reading is the substrate-distance-1 value (−0.0859). The substrate carries both; the physical horizon-exit observable is the TD/zeta one.

**Artifacts**: `inv12_w3_5_cf21_htilde_reconcile.py` / `.npz` / `.png`.

---

## Wave 3 Synthesis (team-lead)

**Per-gate roll-up** (all 5 verified on disk; W3-1 the FOUNDATIONAL lock dispatched as Wave 0):

| Gate | Verdict | Result | Constraint-map move |
|:-----|:--------|:-------|:--------------------|
| W3-1 RELIC-SPECTRUM-ODE-LOCK | **INFO** | integrator-lock machine-exact (unitarity 4.55e-15, Radau↔DOP853 7.76e-5, N_seg-independent); ρ_relic carries L_max band 15.41→26.85 | per-mode {β_k} LOCKED (firm for all 5 consumers); 2\|λ\|_min=1.6395 matches S101 edge; INFO only on absolute ρ_relic |
| W3-2 FLOQUET-ORDERED-VEIL-RESONANCE | **PASS** | fraction_resonance = 0 across the pair band | Ordered Veil SURVIVES its own in-band resonance — the relic does not self-repump; A_s overproduction is genuine |
| W3-3 BACK-REACTION-CLOSURE-HSQ | **INFO** | sign PASS (diluting relic decelerates, q raised above −1); magnitude INFO (dust trajectory spans 6.5% of band, hugs lower edge) | G2 partially healed at effective-Friedmann level; STRUCTURAL THEOREM dq/da ∝ −(n₁−n₂)² ≤ 0 ⇒ relic-Friedmann q ≠ s54 proxy q (sharpens S95-W4-4) |
| W3-4 GREYBODY-FROM-BDG | **FAIL** | first-principles BdG greybody ∫Γ=0.036 vs fitted 0.512 (agree 0.93, band-collapse 0.25, both outside 0.1 tol); method-consistent (ODE↔closed 1e-9) | static surface-gravity barrier ruled out; A_s upper-edge filter is a FITTED knob → relocates open physics to the dynamical-resonance forward gate |
| W3-5 CF21-HTILDE-RECONCILE | **PASS** | CF21 H̃ reconciled to one canonical horizon-exit reading | H̃ leg pinned; the factor-1.57 excess (TD 5.9076e-3 vs centre 4.714e-3) IS the A_s overproduction via CC3 (+2) |

**Structural reading**: the relic is **locked and survives** (W3-1 per-mode firm, W3-2 no in-band resonance) — so the A_s overproduction is a genuine substrate-IS excess, not a re-pumping artifact. Back-reaction (W3-3) closes the gap at the effective-Friedmann level with the CORRECT SIGN but only PARTIAL magnitude (a sub-unity dust fraction reaches only the lower band edge), and produces a permanent structural theorem (two diluting fluids give monotone-non-increasing q) that proves the relic-Friedmann q and the SCALE-FACTOR-54 Connes-distance-proxy q are DIFFERENT observables. The decisive open leg is W3-4 FAIL: the first-principles BdG greybody does NOT reproduce the fitted 0.512 filter, so the A_s upper-edge is currently a fitted knob — the live question relocates to whether a *dynamical* near-horizon resonance (finite quench rate τ̇) supplies a substrate-derived filter. Feeds: all → W4-1 (A_s wall) + W4-3 (three-route synthesis).

**Effected In-Session** (non-math; investigation track registry-quarantined — no session-track register mutation):
- [x] No in-track register edits — W3-3's STRUCTURAL THEOREM (dq/da ∝ −(n₁−n₂)² ≤ 0; relic-q ≠ s54-proxy-q, sharpening S95-W4-4) is a registry-promotion candidate routed to session-promotion at `/rclab-investigate --investigation 12` close. Recorded in §W3-3 + housekeeping ledger §D.

## Carry-Forward Computations

### CF-INV12-W3-A — A_s upper-edge greybody: dynamical near-horizon resonance scan (THE decisive A_s compute)

| Field | Specification |
|:------|:--------------|
| **What** | Scan the BdG fluctuation potential at the τ≈0.16 exit horizon for ANY substrate-derived barrier (static OR dynamical-resonance) whose half-transmission ω_½=√V_0^sub lands inside the relic band [0.94, 3.72] M_KK and reproduces ∫Γ=0.512±10% — OR prove no such scale exists. Critical un-scanned candidate: a dynamical near-horizon resonance set by the finite quench rate τ̇(τ) (finite-rate Bogoliubov / Floquet-WKB correction to the sudden-limit κ_exit), NOT the static surface-gravity barrier W3-4 already ruled out. |
| **Inputs** | W3-1 locked {α_k,β_k} + pair_band [0.94,3.72] (§W3-1); W3-4 V_eff scanner + Pöschl-Teller machinery (§W3-4); τ̇(τ) near-exit trajectory (S95-W4-2-HAWKING-ANALOG-T-LEDGER); canonical κ_exit=47.6146, Δ_BCS=0.4642547, T_acoustic=0.112, T_compound=7.578; fitted comparator ∫Γ_fitted=0.512. |
| **Gate** | NEW (transit-dynamics). PASS (A_s bounded-AND-derived) iff ∃ substrate V_0^sub with √V_0^sub ∈ [0.94,3.72] AND ∫Γ=0.512±10%. FAIL (A_s bounded-but-filter-fitted; permanent upper-edge knob) iff every substrate scale gives ω_½ outside the band. INFO iff a resonance lands in-band but ∫Γ misses 0.512 by >10%. Pre-register tol=10% RATIO + finite-rate WKB regime_verdict. |
| **Effort** | ~1 parameter scan + 1 finite-rate transmission computation; ~1 agent-session. Single decisive gate, no multi-wave dependency; all inputs on disk. |

(W3-1/W3-2/W3-5 closed in-session; W3-3 closed INFO with its forward content folded into the back-reaction-history question, which the CF-INV12-W3-A scan + the W4 forward gates jointly address.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-17 | Relic spectrum {β_k} | not locked to one ODE | LOCKED per-mode (W3-1 INFO; ρ_relic band-flagged) | Radau↔DOP853 7.76e-5, unitarity 4.55e-15, N_seg-independent |
| 2026-06-17 | Ordered-Veil in-band resonance | untested | SURVIVES (W3-2 PASS, fraction_resonance=0) | no Floquet instability band in the pair band |
| 2026-06-17 | Back-reaction closure (G2) | open | partially healed, sign-correct (W3-3 INFO) | diluting relic decelerates; dust trajectory at lower band edge |
| 2026-06-17 | relic-Friedmann q vs SCALE-FACTOR-54 q | conflated | DISTINCT observables (W3-3 STRUCTURAL THEOREM) | dq/da ∝ −(n₁−n₂)² ≤ 0; s54 q rises, relic q monotone-non-increasing |
| 2026-06-17 | A_s exit greybody filter (0.512) | fitted Pöschl-Teller knob | static barrier RULED OUT; FITTED-knob status (W3-4 FAIL) | first-principles BdG ∫Γ=0.036 ≠ 0.512 |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict line |
|:-----|:-------|:------------|:------------|:------------|
| W3-1 | inv12_w3_1_relic_spectrum_ode_lock.py | ✓ | ✓ | INFO (foundational; cache-path drift corrected) |
| W3-2 | inv12_w3_2_floquet_ordered_veil_resonance.py | ✓ | ✓ | PASS |
| W3-3 | inv12_w3_3_back_reaction_closure_hsq.py | ✓ | ✓ | INFO ([SIGN] 3-tuple + composite-precedence row) |
| W3-4 | inv12_w3_4_greybody_from_bdg.py | ✓ | ✓ | FAIL (re-run as w3-4b after a no-op first dispatch) |
| W3-5 | inv12_w3_5_cf21_htilde_reconcile.py | ✓ | ✓ | PASS |

All verdict lines at `computations/investigation-12/inv12_gate_verdicts.txt`; sig_5 unique.
