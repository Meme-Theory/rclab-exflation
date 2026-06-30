# Session 100b Wave W5 — Transit Dynamics (box+delta Bogoliubov re-attempt; fold fast-quench universality class) (Results Working Paper)

**Session**: 100b | **Wave**: W5 | **Plan**: session-100b-plan-w5.md | **Theme**: transit-dynamics forward computes from the S99 non-equilibrium-transit litreview (G6, CONVERGENT report pair) — box+delta sudden-limit re-open of the S85 smooth-cusp transfer-matrix FAIL; fold fast-quench universality class (rate- vs range-controlled GGE-relic formation).

## Gate Sections

### §W5-1. S100b-BOX-DELTA-BOGOLIUBOV (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-BOX-DELTA-BOGOLIUBOV`
**Trigger**: `[VERIFY]` (substitution chain pre-registers μ_pivot² > 0 — schema-v2 3-tuple companion row required)
**Classification**: **PHONONIC** (fold |β_k|² transfer-matrix recipe — sudden-limit box+delta vs S85 smooth-cusp)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: Honest re-open of the S85-W7-CUSP-BOGOLIUBOV FAIL under a structurally NEW discretization class (a recipe pre-registration with open outcome, not a claim it passes): the fold's genuine impulsive geometry as box potential + two switch-boundary deltas (Sparn Eq. 4) gives an N_seg-stable |β_pivot|² (variation < 2× across N_seg ∈ {50, 100, 200, 400}) matching the Schmidt Eq. 75 sub-horizon closed form within 10% — attributing the S85 OOM-instability to smooth-cusp segmentation rather than to the transfer-matrix method itself.
**Plan reference**: `sessions/session-plan/session-100b-plan-w5.md` §W5-1 (honest re-open laws (a)–(d), machinery pins, thresholds, substitution chain, input-SHA pins).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("box delta Bogoliubov transfer matrix sudden Sparn")` | NO prior box+delta closure — gate genuinely open. Hits: `S85-W7-CUSP-BOGOLIUBOV: FAIL` (value=−2.019676, scheme=transfer-matrix, BD-in-out, audit `b17807eb…`) = the predecessor exactly as the plan cites; S66 mack-transit workshop Eq. T.50 (piecewise transfer-matrix structure, reused here); `TRANSFER-BOGOLIUBOV-64: PASS` (different gate — cutoff stability, max/min = 1.33); Sparn Eq. 4 equation entity from the S99 litrev. |
| `trace_entity("S85-W7-CUSP-BOGOLIUBOV")` | Evidence chain: gate FAIL line + provenance `s85_w7_cusp_bogoliubov.py` + open-channel row (−2.020). Predecessor is permanent, NOT superseded; honest-re-open laws (a)–(d) apply. |
| Canonical constants | Verified by direct read of SHA-pinned `canonical_constants.py` (runtime pin `a13dddb1…`): `tau_fold=0.19`, `dt_transit=1.1301575037571713e-3` (S38), `H_fold=586.5267713108464` (S38), `Mach_max_framework=13.75`, `dS_fold=58672.80241318`, `d2S_fold=317862.84898132`, `PI`. In-script cross-checks vs s64 npz channels: rel dev 0.00e+00 on H_fold/dS_fold/d2S_fold. |

NOT PRE-CLOSED: no knowledge-base entity evaluates the box+delta (sudden-limit) discretization class; the S85 closure covers only the SMOOTH-CUSP-AIRY class.

**Verdict**: **PASS** — `var_Nseg = 1.0000000006 < 2.0` (RATIO) AND `rel_dev = 1.631e-06 ≤ 0.10` (RATIO). Schema-v2 3-tuple: `sign_verdict=PASS` (computed V_box preserves μ_pivot² = 202.90 > 0, chain-exact), `magnitude_verdict=PASS` (conjunction met), `regime_verdict=VALID` (unitarity 1.9e-14 < 1e-10; plateau flat to 2.2e-3; full intended window, f_used = 1.0). Composite via the pre-registered `gate-verdicts.md` collapse rule: PASS.

> **The transfer-matrix corridor for the fold |β_k|² REOPENS in the sudden limit.** The S85 OOM N_seg-instability is confirmed as a smooth-cusp segmentation artifact, not a transfer-matrix failure per se: under the fold's genuine box+delta geometry the same machinery is N_seg-stable to 6×10⁻¹⁰ relative across N_seg ∈ {50, 100, 200, 400} and matches the Schmidt-Eq.-75-class closed form to 1.6×10⁻⁶. Dual prior: 0.95 posterior to Track A (smooth-cusp pathology reading). The S85 FAIL stands permanently on its own machinery class (law (d); `predecessor=` row emitted, NOT `supersedes=`).

**Results**:

*Verdict line (emitted via race-safe `emit_verdict`; 6 rows in `computations/session-100b/s100b_gate_verdicts.txt`)*:

```
S100b-BOX-DELTA-BOGOLIUBOV: PASS -- value='beta2_pivot=3.045e-07;var_Nseg=1.000000;rel_dev=1.631e-06;beta2_closed=3.045e-07;beta2_ODE=3.045e-07;mu2_pivot=202.9046;V_box=1.9028;Om_on=+0.4872;Om_off=-0.4882;Deta=1.1301e-03;CHK_N=1.0000;unit_resid=1.9e-14;branchC_var=1.0000;branchC_reldev=2.13e-06;S85_pathology=SMOOTH-CUSP-SEGMENTATION-CONFIRMED' scheme=BOX-DELTA-SUDDEN convention=BD-in-out L_max=N/A audit_sha256=297a597c3cfe6fa00eddf97cccc538241f12faf339793c05a195ad915e7e6498 content_sha256=649194ac0119a14fd01e69f360b62d52c872bb75baa99acf16c5732e6fe20110 schema_version=S84+
```

Companion rows: dual-SHA short row; schema-v2 3-tuple row (PASS/PASS/VALID); `predecessor=b17807eb5930d0bb80142b4b45ae579cdb9465ac7181e4b6f9f8e45f46bd579c` honest-re-open row (cross-gate audit context, explicitly NOT a `supersedes=` token — law (d)); normalization row (Convention-B fold units, CHK_N_ratio, branch-(c) sensitivity); `regulator_pin=N/A` row.

*Core numbers (4-tuple: scheme=BOX-DELTA-SUDDEN, convention=BD-in-out, L_max=N/A)*:

| Quantity | Value | Criterion |
|:---------|:------|:----------|
| \|β_pivot\|² per N_seg ∈ {50,100,200,400} | 3.0453993282e-07 / 3.0453993267e-07 / 3.0453993264e-07 / **3.0453993263e-07** | — |
| var_Nseg = max/min | **1.0000000006** | < 2.0 RATIO → OK |
| \|β_pivot\|²_closed-form (Schmidt Eq.-75-class, identical V_box/Ω_on/Ω_off/Δη) | 3.0454042927e-07 | — |
| rel_dev = \|β²_TM(N400)/β²_closed − 1\| | **1.631e-06** | ≤ 0.10 RATIO → OK |
| \|β_pivot\|²_ODE (Radau, rtol 1e-10; standing valid route) | 3.0453993262e-07 (TM-vs-ODE rel dev 7.4e-12) | diagnostic |
| Unitarity max residual \|\|α\|²−\|β\|²−1\| (all 65+ evaluations) | 1.87e-14 | < 1e-10 ABS → OK |
| CHK-N: re-derived 2(ãH̃)²\|_fold vs k_pivot²/107.63558173571887 | CHK_N_ratio = **0.9999631** (1.9027147 vs 1.9027850) | within 5% → PASS (no abort) |
| Publication value (4 sig figs, Class-8.3 pin; full float64 in npz) | \|β_pivot\|² = **3.045e-07** | — |

*Substitution chain (runtime-substituted numbers — the pre-registered branch claim)*:

```
Step 1: V_box = 1.90278504            (computed window plateau, canonical branch)
Step 2: k_pivot² = 204.80737394       (k_pivot = 14.311092688448717, s77 pin)
Step 3: μ_pivot² = k² − V_box = 202.90458890
Step 4: μ_pivot²/k_pivot² = 0.99070939 ≡ chain pre-registration 1 − 1/107.63558173571887 = 0.99070939 (EXACT to printed digits)
Step 5: μ_pivot² > 0 ⇒ OSCILLATING (sub-horizon) sector; the sin[μ_k Δη] comparator
        (Schmidt Eq. 75) is the correct branch; Λ_k → iμ_k continuation NOT engaged
        at k_pivot. sign_verdict = PASS.
```

*Normalization & window (operational interpretation, disclosed per `math-scripts.md` disclosure discipline)*:

- **Fold normalization (Convention B, S77 canonical)**: ã(τ_fold) = 1 (a_fold,raw = 386.024, N_fold = 5.956); aH_target = k_pivot/k_over_aH = 0.975393518773 M_KK (both keys from the SHA-pinned `s77_n_pivot_map.npz`); clock conversion u = H_fold/aH_target = 601.323 (s64 clock → fold-normalized M_KK clock); conformal rescale Λ = u·a_fold = 232125.15. The S77 anchor `k2_over_zppz_fold = 107.63558173571887` is constructed as k²/(2·aH²) (verified against `s77_n_pivot_map.py` line 475) — the anchor's z″/z is the quasi-dS barrier 2(aH)².
- **CHK-N (non-circular content)**: ãH̃\|_fold re-derived as d(ln ã)/dη̃ from the *assembled* fold-normalized channels (cumulative η-integration + a-normalization + rescale wiring — independent of the anchor-pin pair) = 0.9753755 vs target 0.9753935; 2(ãH̃_re)² = 1.9027147 vs anchor 1.9027850 → ratio 0.9999631 ∈ [0.95, 1.05]. This catches exactly the S73B mixed-convention bug class. PASS.
- **Documented physics gap (NOT a CHK-N failure)**: the stored s64 `zpp_over_z` channel (η_H-corrected GSR formula) in fold units = 2.7641 = **1.4526× anchor** (F_fold = 2.905 vs quasi-dS 2.0 — the known η_H = 0.956 slow-roll violation at the fold, s64 INFO verdict). This is the plan's "cross-check against the independently stored zpp_over_z channel": the gap is pre-existing physics in the pinned inputs, handled by the branch-(c) sensitivity below.
- **Window (pinned reading)**: Δη̃ = conformal image of dt_transit = 1.1301575e-3 M_KK⁻¹ read in the fold-normalized M_KK clock = 1.13014059e-3 (ratio to dt_transit 0.999985; ⟨1/ã⟩ correction). τ-window [0.18994874, 0.19005127] — δτ = 1.025e-4 = 0.116 of one s64 grid cell (**sub-grid**; the cubic interpolant is the pinned machinery per `step_size`). This is the unique reading consistent with the plan block's own diagnostic arithmetic: μ_pivot·Δη = 1.6098e-2 ≪ π, matching the plan's "~1.6e-2" to 2 digits. Impulsiveness: ãH̃·Δη̃ = 1.10e-3 (fold-conformal clock); canonical S38-clock product H_fold·dt_transit = 0.6629 < 1.
- **Box + deltas**: V_box = 1.90278504 (window mean of the anchor-consistent barrier 2(ãH̃)²; plateau flat to 2.23e-3 — genuinely box-like). Ω_on = **+0.48716** (repulsive switch-on), Ω_off = **−0.48824** (attractive switch-off) per the literal pinned rule Ω = (1/2)·ã·[ȧ̃]; the strict distributional weight (1/2)[ȧ] (= Schmidt Table I (H₀/2)[δ_i − δ_f], Jacobian-cancelled) differs by only 5.5e-4 relative since ã(boundary) = 1 ± 6e-4 — both reported, gate criteria invariant. Sign structure = the Schmidt Table I linear-expansion landscape (one repulsive, one attractive), extracted from the pinned PDF at runtime.
- **Runtime PDF extraction (research-corpus rule)**: 17/17 markers FOUND, zero extraction gaps — Sparn Eqs. 2–5 (mode equation, ψ_k = √a·v_k Schrödinger form, V(η) = (1/4)ȧ² + (1/2)ä·a, S_k oscillation, N_k = \|b_k\|²/\|c_k\|², unitarity \|c_k\|² = \|a_k\|² − \|b_k\|², box height H₀²/4 + boundary deltas); Schmidt Table I (rectangular-barrier-bounded-by-δ-peaks: V_r = (H₀²/4)ΘΘ, V_s = (H₀/2)[δ_i − δ_f]) + Eqs. 75/76 markers + sin[(η_f−η_i)μ_k] structure + B41 δ-matching ([ψ′] = +Ωψ); S79 B2 anchor line ("\|beta_2\|^2 ~ 1700") verified at the pinned SHA.

*Barrier-branch and weight sensitivity (verdict-structure invariance)*:

| Branch | V_box | var_Nseg | rel_dev | \|β_pivot\|² |
|:-------|:------|:---------|:--------|:------------|
| (b) canonical: anchor-consistent 2(ãH̃)² | 1.90279 | 1.0000000006 | 1.63e-06 | 3.0454e-07 |
| (c) sensitivity: stored s64 zpp_over_z channel (η_H-corrected) | 2.76408 | 1.0000000008 | 2.13e-06 | 3.0760e-07 |

Both branches PASS both criteria — the verdict is invariant under the F-convention (quasi-dS vs η_H-corrected) barrier choice. The 45% barrier shift moves \|β_pivot\|² by only 1.0% because the switch-boundary deltas dominate the production (channel split: box-only 5.64e-09 vs deltas-only 3.06e-07, **×54.2** — the Parra-López switch-on/off-dominance structure: transitions dominate, stages do not). The z-pump delta-weight variant (Ω_z = [z′/z] = ±1.288) gives \|β\|² = 2.12e-06 (×6.96) — reported sensitivity scalar; rel_dev/var_Nseg unaffected (identical weights on both sides of every criterion). The literal Sparn-Eq.-4 potential built from ã(η̃) (the √a-pump, 2+1D-BEC image) has plateau V_Sparn = 0.7187 = 0.378·V_box — the documented ψ_k = √a·v_k pump-correspondence: Sparn's V is the √a-pump barrier (1/2)a″/a − (1/4)(a′/a)² ≈ (3/4 − ε/2)(aH)², while the substrate mode barrier is the z-pump z″/z ≈ 2(aH)²; the chain's identification V_box ≅ (z″/z)\|_fold uses the z-pump anchor.

*Diagnostics (pre-registered, NOT gate criteria)*:

- **(i) S79 B2-ladder OOM context**: \|β_pivot\|²(this gate, impulsive window only) = 3.05e-07 vs \|β₂\|²(B2 stage) ~ 1.7e+03 → −9.75 OOM. Non-comparable by construction: the B2 stage covers post-fold-WKB → horizon-exit (~3.1 e-folds of pump growth); this gate covers ONLY the impulsive transit window (ΔN ≈ 1.1e-3 e-folds). Context only, per the plan pin.
- **(ii) Ramsauer-Townsend zeros**: μ(K_MAX)·Δη/π = 1.80e-2 → **0 zeros in k ∈ [1, 50]** (plan expectation "none in-window": CONFIRMED); first R-T zero at k ≈ 2779.8 M_KK.
- **(iii) ODE reference**: Radau (rtol 1e-10) direct solve of ψ″ + (k² − U(η̃))ψ = 0 across the window with identical δ-matching — agrees with the TM at 7.4e-12 relative at pivot and across the 64-point spectrum (the standing valid route cross-anchors the matrix mechanics).
- **(iv) Spectrum**: 64 log k-points ∈ [1, 50] + pivot (N_eval = 65 per pin); sin/sinh branch crossover at √V_box = 1.379 M_KK (Λ_k → iμ_k continuation implemented exactly via the entire functions C = cos(μL), S = sin(μL)/μ of μ²); TM/closed-form/ODE overlay in the plot.
- **Window-pin sensitivity (seed for any future refined-window gate — a NEW pre-registration, never a re-run)**: the alternative S38-internal-clock reading (δτ = v_terminal·dt_transit = 0.0300) gives Δη_alt = 0.3349, where the interior is NOT plateau-like (flatness 0.92) and \|β_pivot\|²_alt = 1.29e-03 — the box idealization is poor there, confirming the canonical fold-conformal-clock window as the structurally consistent box+delta reading.
- **Single-box TM ≡ closed form**: 1.37e-13 relative (independent code paths — the plan's `boundary_reachable_analytically` identity confirmed numerically).

*Solution-space interpretation*: The transfer-matrix corridor REOPENS for the fold in the sudden limit (box+delta class); the S85 FAIL is localized to the smooth-cusp segmentation class (interior segmentation of a smoothly varying ω_k(η) accumulates artificial reflections; segmentation of a genuine plateau is benign to 6e-10). The fold \|β_pivot\|² = 3.045e-07 for the impulsive window in BD-in-out normalization becomes the candidate canonical box+delta recipe value — its promotion to `canonical_constants.py` is a SEPARATE Class-8.3-pinned carry-forward step (per the plan's `backward` edge), NOT in-gate. Track A absorbs 0.95 posterior. Forward consumers: B2-ladder refinement / UNIFIED-AS-79 F_amp-slot cross-check candidate (CF); agent-memory regime-boundary note (smooth=invalid / sharp=exact, now calibrated on-disk).

*Substrate framing*: The fold IS the substrate's van Hove reorganization — the D_K eigenvalue spectrum reorganizing through the first-order transit at τ_fold = 0.19, supersonically (Mach 13.75 = Mach_fric to 2.9e-4) and impulsively (H·dt = 0.663). The scattering potential is the laboratory-IN/methodological image (the Sparn BEC and Schmidt closed forms model a simplified projection OF the substrate transit) of the substrate's z″/z mode barrier, itself the spectral-action image of the eigenvalue flow (dS/dτ = +58672.8 at fold). Direction of explanation: D_K eigenvalues → spectral moments → z″/z mode barrier → Bogoliubov \|β_k\|² → GGE relic occupation → acoustic interference pattern. The computed ×54.2 delta-dominance IS the substrate-first realization of the Parra-López switch-on/off-dominance theorem: the production lives at the transitions (the switch-on/off of the spectral reorganization), not in the stage between them — "the transit IS the physics" (atlas-10 #8). \|β_pivot\|² is the occupation of the substrate's own excitation spectrum at the pivot mode: particle production IS the spectral reorganization, not an event inside a geometric container.

**Output Artifacts**:

| Artifact | Path | Content |
|:---------|:-----|:--------|
| Script | `computations/session-100b/s100b_box_delta_bogoliubov.py` | SHA-verified inputs; runtime PDF extraction (17/17 FOUND); fold normalization + CHK-N; box+delta TM (N_seg scan); Schmidt Eq.-75-class closed form (independent code path); Radau ODE reference; dual-SHA + payload via `print_verdict_payload` |
| Data | `computations/session-100b/s100b_box_delta_bogoliubov.npz` | All 14 plan-required keys (`beta2_pivot_per_Nseg`, `var_Nseg`, `beta2_pivot_closed_form`, `rel_dev`, `k_grid`, `beta2_spectrum`, `mu_pivot_sq`, `V_box`, `Omega_on`, `Omega_off`, `Delta_eta`, `unitarity_residual_max`, `beta2_pivot_ODE_reference`, `CHK_N_ratio`) + 40 normalization/sensitivity/diagnostic keys (full float64) |
| Plot | `computations/session-100b/s100b_box_delta_bogoliubov.png` | Panel 1: \|β_k\|² spectrum (TM vs Eq.-75 closed form vs ODE, branch crossover + pivot marked); Panel 2: N_seg stability (branches b + c, PASS band); Panel 3: U(η̃) fold profile with box+delta overlay (Ω arrows, anchor + stored-channel levels) |
| Verdict | `computations/session-100b/s100b_gate_verdicts.txt` | Canonical PASS line + 5 companion rows (dual-SHA, 3-tuple PASS/PASS/VALID, `predecessor=b17807eb…` full-64-hex, normalization, regulator_pin=N/A); audit `297a597c3cfe6fa0…`, content `649194ac0119a14f…` |
| Run log | `computations/session-100b/_s100b_w5_1_run.log` | Full stdout (SHA pins in first 20 lines, extraction log, all cross-checks) |

---

### §W5-2. S100b-FOLD-RANGE-SCALING (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S100b-FOLD-RANGE-SCALING`
**Trigger**: `[SIGN]` (schema-v2 3-tuple companion row required)
**Classification**: **PHONONIC** (fold fast-quench universality class — rate vs range control of the GGE-relic formation amplitude)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The canonical P_exc = 1.000 Parker saturation is fold-RANGE-controlled (Rao v > v_c class), not rate-controlled (slow-quench KZ / Li-survival class): P_exc spreads < 1% absolute across Mach ∈ [5, 30] at fixed range AND relative pair content n_rel(λ) rises monotonically with fold range (ρ_S > 0.99) at fixed rate — the absolute 59.8 never gates (projected-charge caveat).
**Plan reference**: `sessions/session-plan/session-100b-plan-w5.md` §W5-2 (scoping notes: N_pair projected-charge caveat + GGE register scope; machinery pins, thresholds, substitution chain, input-SHA pins).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("fold range scaling Rao fast quench Kibble-Zurek rate-independent saturation")` | NOT PRE-CLOSED — only hits are the S100b-plan-w5 text itself, the S38/S55 saturation pins (`P_exc = 1.000` atlas T1 PROVEN; `xi_KZ = 0.808` sudden-quench floor), and the s88-w2 `z = z_BdG` DERIVATION-TARGET note. No prior fold-range-scaling verdict exists; gate is fresh. |
| `get_constant("P_exc_kz")` | 1.0 (the CHK-S38 reproduction target) |
| `get_constant("dt_transit")` | 0.0011301575037571713 M_KK⁻¹ (rate-map anchor) |
| `get_constant("Mach_max_framework")` | 13.75, S85 provenance; ALIAS Mach_max; the BEC analog Mach_max_analog = 54.3 is a SEPARATE constant (not consumed) |
| `get_constant("dS_fold")` | 58672.80241318 (range-axis amplitude anchor) |
| `get_constant("n_pairs")` | 59.8 (projected charge ⟨Q⟩_GGE — RELATIVE use only per convention pin) |

**Verdict**: **PASS** — composite from the schema-v2 collapse rule applied to (sign=PASS, magnitude=PASS, regime=VALID); identical to the gate-rubric composite (consistency asserted in-script). Emitted race-safe via `emit_verdict` (6 rows: canonical + dual-SHA companion + 3-tuple + 3 annotation rows).

```
S100b-FOLD-RANGE-SCALING: PASS -- value='DeltaP_exc=0.00157;rho_S=1.000000;p_range=1.00;eps=0.0006839;eps_boundary=0.004394;eps_margin_ratio=0.156;CHK_S38=0.0e+00;Li_zprime=2.090_vs_z+1/nu=3.904_SURVIVAL;class=Rao-range-controlled-v-gt-vc' scheme=LZ-PARKER-SUDDEN convention=RELATIVE L_max=N/A audit_sha256=683a7e22e476411d41587ec7f23444e109b6f7dffaaa0d6436b4e663a5a53bc3 content_sha256=daa0425ce51275b189915a972016a7452da7afd4541d6cdeb90ea929a09b90f9 schema_version=S84+
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S100b-FOLD-RANGE-SCALING 3-tuple annotation (schema-v2)
```

**Results**:

NUMBERS first (4-tuple: scheme=LZ-PARKER-SUDDEN, convention=RELATIVE, L_max=N/A; publication precision 3 s.f. on ΔP_exc and p_range, full float64 in the npz):

| Statistic | Computed | Pre-registered criterion | Clause verdict |
|:----------|:---------|:-------------------------|:---------------|
| ΔP_exc = max−min P_exc over Mach ∈ [5, 30] (11 linear pts, 13.75 exact member) | **1.565452795209e−3** (→ 1.57e−3 at 3 s.f.) | < 0.01 ABSOLUTE | PASS (6.4× inside) |
| Spearman ρ_S(n_rel(λ), λ) over λ ∈ [0.25, 4] (9 log pts, 1.0 exact member) | **1.000000000000** (strictly monotone, all diffs > 0) | > 0.99 | PASS |
| p_range (LSQ log-log slope; diagnostic, NOT gated) | **1.0009** ≈ 1 | Rao ρ ~ δ_max analog expects ~1 | confirms range law |
| ε_canonical = −ln P_exc^LZ(13.75) = π·Δ₀²/(2·dΔ/dt) | **6.838563969201e−4** (s38 npz `lz_exponent`, reconstructed to 0.0 rel dev) | — | — |
| ε_boundary (exact brentq root of ΔP_exc(ε) = 0.01) | **4.394488e−3** | — | — |
| ε saturation margin = ε_c/ε_boundary | **0.1556** (factor 6.43× inside the saturation boundary; P_exc(13.75) = 0.999316 > 0.99564) | — | deeply saturated |
| CHK-S38 residual \|P_exc_recon − P_exc_kz\| | **0.0e+00** | < 1e−6 ABS (HARD-ABORT) | PASS |
| Li adjacency: z′_eff vs z_eff + 1/ν_eff | **2.090 < 3.904** | reported only (no gate weight) | SURVIVAL side |

**Substitution chain with substituted numbers** (plan §W5-2 chain, executed):

1. P_exc(v_eff) = exp(−πΔ_min²/(2v_eff)); S38 canonical components Δ₀ = 1/τ₀ = 0.770435098, dΔ/dt = 1363.411906 ⟹ ε := π·Δ₀²/(2·dΔ/dt) = **6.8386e−4** (matches the pinned s38 npz `lz_exponent` to machine precision; exp(−ε) = P_LZ_npz = 0.999316377380 identity at < 1e−10).
2. Rate map v_eff ∝ Mach ⟹ P_exc(Mach) = e^(−ε·13.75/Mach): P_exc(5) = 0.998121162, P_exc(30) = 0.999686615.
3. ΔP_exc = e^(−0.4583ε) − e^(−2.75ε) = **1.5655e−3**; linearized 2.2917·ε = 1.5672e−3 (0.11% curvature gap — the ε ≪ 1 expansion is in-regime).
4. Direction: ε = 6.84e−4 < ε_boundary = 4.39e−3 ⟹ ΔP_exc ≪ 0.01 ⟹ rate-INDEPENDENT, exactly as the saturation P_exc_kz = 1.0 forces (a measured ΔP_exc ≥ 0.01 would have required ε ≥ 4.36e−3, contradicting saturation).
5. Range axis: under saturation the occupation reduces to the COUNT of modes inside the swept excursion window: n_rel(λ) = λ·e^(ε(1−1/λ)) (count ∝ λ·δ_max(1) from the s64 profile integral × per-crossing e^(−ε/λ), v_eff ∝ λ at fixed rate); d ln n_rel/d ln λ = 1 + ε/λ > 0 ∀λ ⟹ strictly increasing ⟹ ρ_S = 1.000000 > 0.99. Computed n_rel: 0.249488 (λ=0.25) → 4.002052 (λ=4).
6. Conclusion (pre-registered signs, both land as predicted): rate-FLAT ∧ range-INCREASING ⟹ **Rao v > v_c range-controlled class**. sign_verdict = PASS.

**Cross-checks (all PASS)**:

- **CHK-S38 (HARD-ABORT pre-flight)**: kz_exp = ν/(1+zν) = 0.25 exact; adiab = τ_Q/τ₀ = 8.707130e−4 ≪ 1 (sudden); raw_P_exc = (τ₀/τ_Q)^1 = 1148.48 → saturated min(·,1) = 1.0; residual vs canonical P_exc_kz = **0.0** < 1e−6.
- **Mode-set validation**: Σρᵢ·√(Eᵢ²+Δ₀²) = 69.0137155070 == pinned s38 npz `E_exc_total` at 2.1e−16 rel (the S38 8-mode fold-window set is npz-certified); Σρᵢ = 60.092 vs n_pairs = 59.8 quoted as projected charge only.
- **s64 anchor cross-checks (HARD-ABORT)**: spline S(τ_fold) vs S_fold_canonical at 1.4e−15 rel; dS(τ_fold) vs dS_fold = 58672.80241318 at 4.1e−10 rel (npz canonical keys == canonical_constants exactly).
- **Window route-independence**: Δτ_w = \|v_terminal\|·dt_transit = 0.030000000 == S38 route N_defect_window·ξ_KZ at 0.0 rel dev.
- **δ_max route-independence**: ∫_W \|dS/dτ\|dτ = 1760.298994 == endpoint route S(τ_hi)−S(τ_lo) at 3.3e−11 rel (dS > 0 throughout W, verified); flat-anchor dS_fold·Δτ_w = 1760.18 (profile curvature correction 6.5e−5).
- **Linearity**: δ_max(λ)/δ_max(1) − λ at 4.4e−16 max (amplitude rescale exactly linear by construction, confirmed numerically per λ point).
- **Rate-anchor**: Mach_fric (s64_sound_speed) = 13.753964771660 vs the EXACT rate-map anchor Mach_max_framework = 13.75 (2.9e−4 rel, documented; 13.75 used per pin).
- **Runtime PDF extraction (fetched sources only, no extraction gaps)**: Rao p1 "critical quench rate vc that scales with the quench range δmax" + "for v > v_c … universal scaling ∼ δmax, independent of the quench rate" (and the v < v_c side "follows the KZM scaling ∼ v^{1/2}"); Rao p3 v_c law "vc = δmax/t̂c = αδmax√(4J²+δ²max)"; Li p1 "z′ < z + 1/ν_µ, where z = 1 (z′ = 1) … ν_µ = 5/4" + "r_µ = z + 1/ν_µ = 9/5". All four extraction flags True in the npz.

**Li-adjacency diagnostic (reported only, no gate weight)**: gap proxy Δ_gap = \|S − S_fold\| on the s64 dense grid, one-sided log-log fits over \|τ−τ_fold\| ∈ [1.76e−3, 0.05] (55/54 pts): (νz)_pre = 0.9521 → z_eff = 1.9041; (νz)_post = 1.0450 → z′_eff = 2.0901 (ν_eff = 0.5 PINNED, S38 BCS mean-field — the 1-parameter fit determines the product only). Li inequality z′ < z + 1/ν: **2.0901 < 3.9041 — SURVIVAL side**, margin 1.81. First-order character explicit: νz ≈ 1 is the ANALYTIC-profile slope (dS_fold ≠ 0); the ±5% deviation from 1 is the d2S curvature ±(d2S/2dS)·δ = ±2.709·\|τ−τ_fold\| over the fit window, NOT an anomalous critical exponent — the fold is first-order, tricritical-ADJACENT only. This (z, z′, ν) triple seeds the kitaev-litrev V.4 tricritical-adjacency follow-up.

**Regime (3-tuple third leg)**: max adiabaticity over the scan = τ_Q(Mach=5)/τ₀ = 2.394e−3; max ε_eff over both axes = 2.735e−3 (at λ=0.25); regime metric 2.7e−3 ≪ 0.1 ⟹ **VALID** (sudden-limit expansion in-regime over the ENTIRE two-axis scan window — no auto-shortening, f_used = 1).

**Model scope note (honest boundary)**: the range-axis mode count uses the UNIFORM-per-unit-spectral-action measure — the pinned-input-faithful choice (L_max = N/A pin: no D_K diagonalization in scope). Van Hove DOS structure could bend p_range away from 1 but CANNOT break monotonicity for a positive measure over the nested window family; resolving the structured-range-response question (the INFO branch's van-Hove-degeneracy reading) requires D_K spectral data — routed to the tricritical-adjacency follow-up, not claimed here.

**Substrate framing**: the fold IS the substrate's first-order spectral reorganization (van Hove fold at τ_fold = 0.19), transited supersonically (Mach 13.75) — impulsive, not quasi-static. "Quench rate" and "quench range" are laboratory-IN images (Rao's trapped-ion LZ sweeps are analogs OF the substrate transit) of two substrate-IS quantities: transit velocity through the fold and spectral excursion across it (dS/dτ = +58,673 at fold). This gate establishes WHICH substrate quantity writes the relic: under P_exc = 1 saturation every swept mode is excited, so the GGE-relic formation content is a **COUNT of modes inside the excursion window — a spectral-geometry quantity, not a kinetic one**. Direction of explanation: D_K eigenvalue flow → fold spectral excursion (not transit velocity) → per-mode Bogoliubov excitation P_exc → GGE relic formation amplitude. The relic is scoped to its canonical register (transit-window validity; CG(24) Poisson integrability; t_therm ≈ 6 M_KK⁻¹, atlas-04 T3 BROKEN for permanence) — this gate concerns FORMATION amplitude only, structurally upstream of thermalization.

**Solution-space update**: the rate-controlled (slow-quench KZ / Li-survival) class is EXCLUDED for the fold's relic formation (ΔP_exc lands 6.4× inside the rate-flat boundary, consistent with — and now quantitatively margining — the S38 saturation); the Rao v > v_c range-controlled class is PINNED with p_range = 1.00 as the fold's analog of Rao's ρ ~ δ_max law. The FAIL branch's S38 re-audit escalation does NOT fire.

**Output Artifacts**:

| Artifact | Path | Content |
|:---------|:-----|:--------|
| Script | `computations/session-100b/s100b_fold_range_scaling.py` | full machinery: SHA pin verification (HARD-ABORT), runtime PDF extraction, CHK-S38, two-axis scan, Li diagnostic, dual-SHA, `print_verdict_payload` |
| Data | `computations/session-100b/s100b_fold_range_scaling.npz` | all 13 plan-required keys (mach_grid, P_exc_vs_mach, Delta_P_exc, lambda_grid, n_rel_vs_lambda, rho_S_spearman, p_range_fit, z_eff, zprime_eff, nu_eff, li_inequality_lhs_rhs, CHK_S38_residual, eps_saturation_margin) + 25 supplementary provenance keys |
| Plot | `computations/session-100b/s100b_fold_range_scaling.png` | 3 panels: P_exc(Mach) w/ 1% band; n_rel(λ) log-log w/ Rao slope-1 guide; Li (z, z′, ν) extraction fits |
| Verdict | `computations/session-100b/s100b_gate_verdicts.txt` | canonical PASS line + dual-SHA companion + schema-v2 3-tuple + regulator/Li/N_pair-caveat rows (emitted via race-safe `emit_verdict`) |

---

## Wave 5 Synthesis (team-lead)

**Written**: 2026-06-07, session close. Both gates landed; verdicts verified on disk against each gate's `output_artifacts` must_contain set. Clean sweep: 2/2 PASS, both with full 3-tuple (PASS/PASS/VALID).

| Gate | Verdict | Headline value |
|:-----|:--------|:---------------|
| §W5-1 S100b-BOX-DELTA-BOGOLIUBOV | **PASS** | \|β_pivot\|² = 3.0454e-07; var_Nseg = 1.0000000006 over N_seg ∈ {50…400}; closed-form rel_dev 1.63e-6; ODE cross-ref 7.4e-12 (audit `297a597c3cfe6fa0…`) |
| §W5-2 S100b-FOLD-RANGE-SCALING | **PASS** | ΔP_exc = 1.57e-3 < 0.01 over Mach ∈ [5,30]; ρ_S(n_rel, λ) = 1.000000; Rao range-controlled class (audit `683a7e22e476411d…`) |

**Wave reading.** Transit dynamics swept its wave, and the two PASSes compose into one statement about the fold: **GGE-relic formation content is a spectral-geometry quantity, not a kinetic one.** W5-1 re-opens the transfer-matrix corridor for the sudden limit under the honest re-open laws — the fold's genuine plateau (flat to 2.2e-3 across the impulsive window) segments benignly (variation 6e-10 across an 8× segmentation sweep), the Schmidt Eq.-75-class closed form agrees to 1.6e-6, an independent Radau integration to 7.4e-12, and the S85 OOM-instability is LOCALIZED to the smooth-cusp segmentation class (`S85_pathology=SMOOTH-CUSP-SEGMENTATION-CONFIRMED`) — the S85 FAIL stands untouched on its own machinery class (law-(d) `predecessor=` row, correctly NOT a supersession). W5-2 pins the fold in Rao's v > v_c **range-controlled** fast-quench class: under P_exc = 1 saturation (ε deeply saturated, margin 0.156 vs the exact boundary), excitation content is a COUNT of modes inside the spectral-excursion window — the rate-controlled KZ class is excluded, the S38 re-audit escalation does not fire, and the Spearman ρ_S = 1.000000 monotonicity over the 16× range sweep is exact. Substrate-first composition: the supersonic transit (Mach 13.75) deposits pairs by WHERE the spectral-excursion window reaches (range), not by HOW FAST it was crossed (rate) — and the validated box+delta recipe now prices that deposit at |β_pivot|² = 3.045e-07 per pivot mode in BD-in-out normalization.

**Decision-point evaluation** (plan §"Wave 5 → Wave 6 Decision Point"): W5-1=PASS row → the |β_pivot|² promotion CF opens (Class-8.3-pinned at 4 s.f.; "promotion is a SEPARATE gate with its own pre-registration — never in-gate", plan verbatim — so this is deliberately NOT an in-session `update_constant`); agent-memory regime-boundary note updated in-gate (smooth=invalid / sharp=exact, calibrated on-disk). W5-2=PASS row → Rao-class pin recorded on the GGE-relic formation surface (constraint map below); "falsifier-surface row (if any)" — none warranted: the class pin is interpretive/structural, no new falsifiable observable value emerged (P_exc saturation already lives on the surface via existing rows); the (z, z′, ν) diagnostic seeds the tricritical-adjacency CF below.

**Carry-Forward Computations (MATH ONLY — propagate to S101)**

### CF-S101-BETA-PIVOT-PROMOTION — pre-registered promotion gate for |β_pivot|²_box-delta + F_amp-slot cross-check

Per the plan's W5-1 PASS routing (decision-point table) + §W5-1 solution-space interpretation: **What** — promote `beta2_pivot_box_delta = 3.045e-07` (Class-8.3 publication precision: 4 sig figs; full float64 in npz) to `canonical_constants.py` via its own pre-registered gate, bundled with the B2-ladder refinement / UNIFIED-AS-79 F_amp-slot cross-check (the −9.75 OOM vs |β₂|² ~ 1.7e3 ladder-stage context pin makes the cross-check non-trivial: the promotion gate must declare which ladder stage the canonical value anchors). **Inputs** — `s100b_box_delta_bogoliubov.npz` (full-precision β², V_box/Ω_on/Ω_off/Δη pins, branch-(c) sensitivity), UNIFIED-AS-79 F_amp slot spec, S79 anchor. **Gate** — promotion PASS iff the 4-s.f. value round-trips the npz at rel_tol ≥ 1e-4 (Class-8.3 item 2) AND the F_amp-slot cross-check declares ladder-stage consistency (pre-registered band at gate authorship); verifier consumes the npz, never the WP rounding. **Effort** — 1 light compute gate (≤ 1 h) + canonical write-order Steps 1-2.

### CF-S101-TRICRITICAL-ADJACENCY — (z, z′, ν) tricritical-adjacency follow-up (kitaev litrev V.4 seed)

Per the plan's W5-2 PASS routing: **What** — evaluate the fold's diagnostic exponent triple (z′ = 2.090, z + 1/ν = 3.904, νz ≈ 1 analytic first-order slope) against the kitaev-litrev V.4 tricritical-adjacency template: does the fold sit in the SURVIVAL-side adjacency band of a tricritical crossover (Li z′ < z + 1/ν), and does the non-monotone n_rel(λ) profile carry the van-Hove-degeneracy reading? **Inputs** — `s100b_fold_range_scaling.npz` (13 plan-required keys incl. mach_grid, lambda_grid, exponent diagnostics), kitaev litrev V.4 report (`sessions/archive/session-99/session-99-litrev-nonequilibrium-transit-kitaev.md`), Li/Rao pinned PDFs. **Gate** — pre-registered at S101 plan-freeze (adjacency band + profile-class criterion to be pinned by the planner from the V.4 template; this CF supplies the inputs and the diagnostic values). **Effort** — 1 compute gate, ≤ half a session.

**Effected In-Session (NON-MATH — completed before STOP)**

- [x] Law-(d) honest re-open discipline executed: `predecessor=b17807eb…` full-64-hex row (NOT supersedes) preserving the S85 FAIL on its own machinery class — transit-dynamics-theorist in-gate — `s100b_gate_verdicts.txt` companion row under W5-1 canonical line — audit `297a597c3cfe6fa0`
- [x] Agent-memory regime-boundary calibration note (smooth=invalid / sharp=exact, on-disk anchors) — transit-dynamics-theorist in-gate per the plan's backward edge — `.claude/agent-memory/transit-dynamics-theorist/MEMORY.md` — agent-private, non-canonical

**Process observations (closed in-session; do NOT propagate)**: two same-type transit agents ran concurrently in one wave with zero collisions (separate scripts, separate WP sections, race-safe emit_verdict) — the sibling-awareness line in both prompts was honored.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-07 | Transfer-matrix corridor for fold \|β_k\|² | CLOSED (S85 FAIL, OOM instability) | REOPENED for the sudden limit (box+delta class); S85 FAIL localized to smooth-cusp segmentation class | W5-1 PASS |
| 2026-06-07 | Fold fast-quench universality class | unclassified (KZ-vs-range open) | PINNED Rao range-controlled (v > v_c); rate-controlled KZ EXCLUDED; formation content = spectral count | W5-2 PASS |
| 2026-06-07 | S38 P_exc = 1.000 saturation record | standing | RE-CONFIRMED (CHK-S38 residual 0.0; saturation deeply inside boundary, margin 0.156) | W5-2 cross-check |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other | Size |
|:-----|:-------|:------------|:------------|:------|:-----|
| W5-1 | s100b_box_delta_bogoliubov.py | ✓ (68 keys) | ✓ (3 pinned panels) | _s100b_w5_1_run.log | 69.0 KB / 21.4 KB / 186 KB |
| W5-2 | s100b_fold_range_scaling.py | ✓ (42 keys) | ✓ | — | 47.0 KB / 11.8 KB / 152 KB |
