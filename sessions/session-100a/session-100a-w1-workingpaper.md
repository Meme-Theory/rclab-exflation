# Session 100a Wave 1 — Cosmology Keystone Successors + Register-Sourced Tier-2 (Results Working Paper)

**Session**: 100 | **Wave**: 1 | **Plan**: session-100a-plan-w1.md | **Theme**: EVOI Tier-1 a(t)/C10 keystone-successor gates (S99 corridor-maps) + EVOI Tier-2 register-sourced observational gates (n_s NLO precision-stability; Leggett-channel DM direct-detection).

## Gate Sections

### §W1-1. S100a-W1-1-SF54-MAPPING (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-W1-1-SF54-MAPPING`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The SF54 deceleration band `[−0.97, +0.81]` is the right comparison object for the bare-frame `q_bare(τ)` history only after a frame/normalization correction of the `a_eff→SF54` Connes-distance proxy; under the corrected map the substrate is mostly-accelerating post-fold, so the S99 W1-1 band-miss is a genuine substrate prediction, not an ill-defined mapping.
**Plan reference**: `sessions/session-plan/session-100a-plan-w1.md` §W1-1 (machinery pin, three-branch rubric, substitution chain, Ω_BA_fold / a_2^{ζ} sources).

**Output Artifacts**:
- `computations/session-100a/s100a_w1_sf54_mapping.py` — producing script (carries `from canonical_constants import` + `print_verdict_payload`; OMP_NUM_THREADS=8 set before numpy import per the `GPU_path=numpy cpu-cap-OMP8` machinery pin)
- `computations/session-100a/s100a_w1_sf54_mapping.npz` — full-float64 data (gate arrays + three-map-ladder arrays + SF54 re-derivation + all six cross-check scalars; Class-8.3 round-trip source)
- `computations/session-100a/s100a_w1_sf54_mapping.png` — 4-panel plot (corrected history vs band + band generator; three-frame Hubble ladder; map-ladder slopes A(τ); one-sided miss histogram)
- Verdict line in `computations/session-100a/s100a_gate_verdicts.txt` (canonical line + dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row + 3 extra companion rows, emitted via the race-safe `emit_verdict` knowledge-MCP tool)
- `audit_sha256 = f41bdf1fc80562daabe09784a1dee0d9e93e0bb3a549dcdd061f5d6b1e290002` (script+canonical+pinmap) / `content_sha256 = 091360aa8e3af58f35ae2372279c4bb4d6e69687e2575e6987804a4fca2a4cb7` (script only)

**MCP Pre-Compute Audit**:
1. `search_knowledge("SCALE-FACTOR-54 Connes distance deceleration")` → SF54 = SCALE-FACTOR-54 gate (PASS): `q: −0.97 → +0.81` Connes-distance proxy; equation hits pin `a(τ_fold)/a(0) = 2.117` monotone ⟨d_D⟩ growth (S54 QA-Hawking workshop / Baptista collab). Band provenance confirmed.
2. `get_constant("Omega_BA_fold")` → 2.241353 (S95 `s95_w4_4_sp_conformal_embed.npz`; canonicalized S97-W1-OMEGA-PROFILE PASS, rel 1.5e-4). Matches plan pin exactly.
3. `get_constant("a_2_FW_zeta")` → 2776.165389 (S88-A-N-FW-CANONICALIZATION). Matches plan pin exactly.
4. `search_knowledge("SF54 mapping frame correction band_frac q_bare")` → NO prior SF54-MAPPING evaluation exists (gate NOT pre-closed); predecessor `S99-W1-Q-NONRATIO-OBSERVABLE` INFO (band_frac_primary=0.490196) + `S96-W1-GFT-FRIEDMANN` INFO both used the same `q_SF54_band=[-0.97,0.81]` convention; atlas-08 Q13 tagged ADVANCED on the S99 INFO.
5. `trace_entity("S99-W1-Q-NONRATIO-OBSERVABLE")` → gate INFO + npz provenance + Q13 open-channel chain. Verdict: gate is FRESH — proceed to compute.

**Verdict**: **INFO** (composite; schema-v2 3-tuple: `sign=PASS`, `magnitude=INFO`, `regime=VALID`) — **Track B at 0.9 posterior per the pre-registered discriminator**: `band_frac_corrected = 0.5015 < 0.90` AND the corrected map is well-defined (finite 999/999, positive-slope A=1, bijective Spearman ρ=1.000000) AND `median(q_corrected) = −0.8662 < 0`. The substrate is structurally mostly-accelerating post-fold; SF54 is the WRONG deceleration band for the bare-frame post-fold history; the S99 W1-1 band-miss is a genuine substrate prediction, NOT a mapping defect.

**Results**:

*Output 4-tuple*: `(value=band_frac_corrected=0.501502 (4sf 0.5015), scheme=FW, convention=CONNES-DISTANCE-PROXY-FRAME-CORRECTED, L_max=N/A)`. Canonical anchors consumed: `Omega_BA_fold = 2.241353`, `a_2_FW_zeta = 2776.165389` (a_2^{ζ} regulator-pinned channel provenance), `tau_fold = 0.190` — all via `from canonical_constants import`, zero hardcodes.

*The frame-map theorem (the gate's structural core, derived in the script docstring with every step)*: for any conformal reframing `ã(τ) = ω(τ)·a(τ)` with `h = a′/a`, `w = ω′/ω`, the log-rates add (`H̃ = h + w`) and substituting `h′ = −(1+q_bare)h²` into `q̃ = −1 − (h′+w′)/(h+w)²` gives the EXACT pointwise affine map

`q_corrected(τ) = A(τ)·q_bare(τ) + B(τ)`,  `A = (H_bare/H̃)² > 0`,  `B = −1 + A − w′/H̃²`

— confirming the plan's Step-A "positive multiplicative + additive shift" form exactly. **Corollary (map_0)**: for the CONSTANT canonical normalization `C = Ω_BA_fold = 2.241353`, `w = w′ = 0 ⟹ A ≡ 1, B ≡ 0 ⟹ q_corrected ≡ q_bare` EXACTLY — the deceleration parameter is a logarithmic-derivative observable; every constant conformal/amplitude normalization cancels identically. Numerical verification: re-running the exact S99 gradient pipeline on `C·a_bare` reproduces `q_bare` to max rel dev `5.262e-07` (double-gradient float64 roundoff amplification; the identity is exact in real arithmetic).

*Three-map ladder (which correction is THE corrected map)*:
| map | frame target | slope A(τ) on grid | status |
|:----|:-------------|:-------------------|:-------|
| map_0 const `Ω_BA_fold` | normalization-aligned bare frame | A ≡ 1 (B ≡ 0) | **CANONICAL — identity on q (theorem)** |
| map_1 full AOFT `Ω(τ)` | acoustic frame `a_eff` | \|A₁\| median = 1.431e+11, max 6.9e+17; 18 `H_A=0` sign crossings | ILL-DEFINED — the S98-PROVEN 0/0 (stationary `a_eff`, relvar 1.8e-7); excluded |
| map_2 inter-proxy `a_CD/a_bare` | Connes-distance (SF54) frame | A₂ median = 1.468e-03 ∈ [3.45e-04, 5.96e-03], all > 0 | well-defined but comparison-DEGENERATE — slope suppression ~10³ erases the bare history; exact transport reproduces the band's own generator (`h + w_CB = H_CD ⟹ q_corrected ≡ q_CD`, circular); only 60.16% of the S99 grid is S54-data-supported |

The unique non-degenerate, well-defined frame correction is map_0, under which the band comparison is frame-aligned and `q_corrected = q_bare` exactly. **The band-miss is FRAME-ROBUST**: no admissible frame/normalization correction can move `band_frac` toward the 0.90 PASS floor.

*Frame measurement (why SF54 is the wrong band)*: on the overlap window (601/999 pts, τ ∈ [0.1903, 0.3469]) the Connes-distance frame carries `H_CD/H_bare` median **26.10** (range [12.95, 53.81]) — the SF54 band generator lives in a conformal frame ~26× faster than the bare backbone; inter-proxy ratio rel-vars `a_CD/a_bare = 0.143`, `a_CD/a_eff = 0.148` show the CD proxy is conformally distinct from BOTH S99 frames (three genuinely distinct frames). The SF54 band's lower edge `−0.9732` is attained at τ = 0.0000 (PRE-fold quasi-de Sitter) and its upper edge `+0.8144` at τ = 0.3469 (post-fold endpoint): the band conflates pre-fold and post-fold regimes of a different-frame proxy. Restricted to post-fold, SF54's own q-range is [−0.7860, +0.8144] with overlap-window median −0.3975 — even the band generator's post-fold median is accelerating-side.

*Gate observable and miss structure*: `band_frac_corrected = 0.501502` over N = 999 (runtime-read grid, closed inequalities, no tolerance slack, no pole exclusion — `domain_used_frac = 1.000000`); `q_corrected_median = −0.866166` (4sf −0.8662), equal by identity to `q_bare_median` (S99 stored −0.866166, replication dev 0.0). The miss is ONE-SIDED: `miss_below_band = 0.498498`, `miss_above_band = 0.000000` — every out-of-band point lies BELOW −0.97, i.e. the substrate post-fold accelerates HARDER than the band's quasi-de-Sitter floor on half the window (deep-acceleration excursions to q ≈ −514); accelerating fraction (q < 0) = 0.6677.

*Substitution chain with substituted numbers* (plan §W1-1 chain, executed):
- Step A: `q_corrected = map_correct(q_bare)` is the affine map `A(τ)q + B(τ)`; under the canonical constant correction `sign(∂q_corrected/∂q_bare) = A₀ = 1 > 0` at all 999 grid points (map_2 diagnostic: A₂ ∈ [3.45e-04, 5.96e-03] all > 0 — positive-slope there too). ✓ no sign flip.
- Step B: positive-slope reframe with B₀ = 0 preserves the median sign EXACTLY: `median(q_corrected) = −0.8662 < 0` = `median(q_bare)`. ✓ (Caveat landed: Step B's sign-preservation holds because the canonical map's additive shift is exactly zero; for map_2 the additive term B₂ dominates — sign preservation is map-specific, and the canonical map satisfies it by identity.)
- Step C: the band [−0.97, +0.81] straddles q = 0 while the corrected distribution has median −0.8662 with 49.85% of its mass below −0.97 ⟹ `band_frac_corrected = 0.5015 < 0.90` with a well-defined map. ✓
- Canonical form: `sign(median q_corrected) = sign(median q_bare) = NEGATIVE (accelerating)`; map bijective on the grid (Spearman ρ = 1.000000; identity affine). ✓
- Direction: median < 0 ⟹ substrate mostly-accelerating post-fold ⟹ a band straddling q = 0 generated by a ~26×-faster conformal frame is the wrong band ⟹ the miss is INFORMATIVE. ✓

*Cross-checks (six, all clean)*:
| CC | test | result |
|:---|:-----|:-------|
| CC-1 | S99 gradient-pipeline replication (cached `a_bare` → cached `q_bare`) | max rel dev **0.0** (bit-exact) |
| CC-2 | ground-truth replication: median −0.866166 / raw band frac 0.501502 vs stored S99 scalars | dev **0.0** / **0.0** (band_frac_primary = 0.490196 cited as S99 primary-protocol anchor) |
| CC-3 | `Ω(τ grid edge) = 2.240977` vs canonical `Ω_BA_fold = 2.241353` | rel dev 1.678e-04 (consistent with the S97 canonicalization at rel 1.5e-4; grid edge τ=0.190261 ≠ τ_fold exactly) |
| CC-4 | SF54 re-derivation: `a_CD = ⟨d_D⟩/⟨d_D⟩(0)` + spline-q at S54 nodes vs stored | max dev **0.0** / **0.0**; q₅₄ range [−0.9732, +0.8144] rounds to [−0.97, +0.81] ✓; LRD synthesis carries both edges ✓ |
| CC-5 | q_CD two-route internal identity (`−1−Ḣ/H²` vs `−a·a″/a′²`) | max rel dev 2.142e-16 (machine ε) |
| CC-6 | exact affine identity `A₂·q_bare + B₂ ≡ q_CD` on overlap | max rel dev 2.466e-16 (machine ε — the affine decomposition is constructionally exact) |

*Three-branch verdict application*: PASS branch (band_frac ≥ 0.90 — SF54 right band after correction) NOT met (0.5015). FAIL branch (map ill-defined: non-bijective / sign-ambiguous / NaN) NOT met — the canonical map is finite at 999/999, positive-slope, bijective, sign-unambiguous. INFO branch MET on all three conjuncts: band_frac < 0.90 ∧ map well-defined ∧ median(q_corrected) < 0 ⟹ **INFO, Track B** (dual-prior discriminator routes 0.9 → Track B). Composite collapse per gate-verdicts.md: magnitude INFO ⟹ composite INFO (sign PASS, regime VALID — domain_used_frac = 1.0 ≥ 0.95).

*Operational deviation (honest disclosure per math-scripts.md plan-authorship item 4)*: `computations/session-54/s54_scale_factor.npz` was consumed as a FOURTH pinned input (the plan's `input_files` block lists 3). It is the canonical data behind the LRD SF54 derivation (the pinned markdown carries only the rounded band edges + growth ratio; the genuine band re-derivation and the frame measurement require the S54 `a_CD/q_CD/H_CD` arrays). The enrichment ADDS a pin to the audit set (all 4 SHAs logged in stdout and folded into `audit_sha256`); band edges, threshold, and verdict criteria are unchanged from pre-registration. Disclosed in a verdict-file extra companion row.

*Substrate framing (PHONONIC)*: the deceleration history IS the curvature of the emergent-FRW scale factor generated by the a₂ Seeley-DeWitt moment of D_K² — the arrow flows D_K eigenvalues → a₂ spectral moment (a_2^{ζ}) → emergent g_M → a_bare(τ)/a_eff(τ) → q(τ). The SF54 band is swept by the Connes-distance functional ⟨d_D⟩ — the substrate's OWN spectral-triple metric, a third conformal frame of the same substrate, not a laboratory container observable. The gate's finding is a substrate-IS statement: the post-fold bare-frame expansion accelerates harder than the Connes-distance frame's quasi-de-Sitter floor on half the transit window, and no constant frame normalization can reconcile the two q-histories because q is a log-derivative invariant. Forward routing per the plan's Wave-1 decision point: the capstone §7.1 LRD deceleration-history row re-scope (SF54 wrong band; substrate mostly-accelerating post-fold) fires capstone-hygiene Q2/Q3 → `mack-cosmic-bridge` (sole §7 writer).

---

### §W1-2. S100a-W1-2-QEQ-DRIVE (volovik-superfluid-universe-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-W1-2-QEQ-DRIVE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `volovik-superfluid-universe-theorist`
**Hypothesis**: A substrate-internal `q_eq(H)` drive from the Volovik Gibbs-Duhem back-reaction (not an imposed `q ∝ H` CPL closure), re-integrated through the friction ODE on the verified non-stationary H-backbone, yields the tracking slope `d ln q/d ln H = 1` UNFORCED — making the n=2 tracking-vacuum law substrate-forced in both legs.
**Plan reference**: `sessions/session-plan/session-100a-plan-w1.md` §W1-2 (k_curv=+3586.5 from s99 npz, ODE re-integration on arr_H_bare_t, late-time-tail regression, substitution chain).

**MCP Pre-Compute Audit**:
- `search_knowledge("q_eq tracking vacuum slope Gibbs-Duhem H^2 drive")` → the gate's question is the LIVE open channel "Upstream — substrate q_eq(H) drive … OPEN (the live successor)" (S99 litrev-x-c10 mack file); S66 mack-transit equation entity confirms "tracking exponent n = 2 … follows from the Gibbs-Duhem relation **under the assumption of a simple-fluid vacuum equation of state**" — exactly the assumption this gate removes. NOT pre-closed.
- `search_knowledge("S100a QEQ-DRIVE")` → no prior verdict for this gate (only S100a plan-freeze queue entries for other waves). Gate unevaluated.
- `trace_entity("RELAXATION-CLOSURE")` → S99-W2-RELAXATION-CLOSURE canonical verdict string recovered: `slope_bare_UNFORCED=3.415925 … slope_driven_IMPOSED-closure=1.008273 … forced_only=True … domfrac=0.4100 … kcurv=+3586.53` — the predecessor FAIL this gate succeeds.
- `get_constant("a_0_FW_zeta")` → 6440.0 (S88, gate S88-A-N-FW-CANONICALIZATION) — matches the plan pin exactly (D_max = 0).
- `get_constant("k_curv")` → NOT a canonical constant — confirms the plan's runtime-npz sourcing (`K_CURV` from `s99_w2_relaxation_closure.npz`) is the correct provenance, not a missing canonical.
- `search_knowledge("Volovik de Sitter local temperature H/pi entropy density")` → `T_local = ħH/(π k_B)` is corpus-pinned as **Volovik Paper 11** (used at S61 bekenstein-desitter); de Sitter entropy `S_dS = A/4G` machinery at S43/S61/S64. The two thermodynamic identities consumed by the derivation below are project-canonical.

**Verdict**: **FAIL** (composite; schema-v2 3-tuple: `sign=PASS`, `magnitude=FAIL`, `regime=VALID`; collapse rule: magnitude-FAIL ∧ regime-VALID ⇒ composite FAIL) — **Track B at 0.9 posterior per the pre-registered discriminator**. The substrate-derived, parameter-free Gibbs-Duhem drive EXISTS but is exponent-locked at `q_eq ∝ H²` (EVEN in H by thermodynamic parity); on the verified non-stationary backbone it transmits `slope = d ln q/d ln H = 2.0556`, not 1 (`|slope − 1| = 1.0556 ≫ 0.05`), and no parameter can tune that slope (coefficient-invariance dev `7.6e-8`). Slope = 1 is recoverable ONLY under the imposed `q_eq = c·H` fluid closure (reproduced at 1.008273, exact match to S99). The `d ln q/d ln H = 1` leg of the n=2 tracking law is **structurally a fluid-closure INPUT**: C10 Object-C closes STRUCTURALLY-CONDITIONAL; capstone §8.5 stays OPEN by design (no capstone-status change — corridor-map only, per the plan's Wave-1→2 decision table). The "n=2 as unforced fixed-backbone attractor" corridor is closed cleanly — an informative boundary, not a defect.

**Results**:

*Output 4-tuple*: `(value=slope_GD=2.0555509139975348 (4sf 2.0556), scheme=FW, convention=SUBSTRATE-NATURAL-BINDING, L_max=N/A)`. Canonical anchors consumed: `a_0_FW_zeta = 6440.0` (a_0^{ζ} regulator-pinned, well-validity cross-check), `tau_fold = 0.19` — via `from canonical_constants import`, zero hardcodes; `K_CURV = +3586.5311811081065` and `q_boundary = −0.6719754908120351`, `c_main = 0.15` runtime-read from the pinned S99 npz.

*The Gibbs-Duhem derivation (the gate's hard part — plan candidate (i), here EVALUATED; the plan block left it symbolic as `q_eq(H) = (∂q/∂μ)·μ(H)`)*:

- **GD-1** (static equilibrium; Volovik q-theory, corpus Papers 05 / 25 §V / 35; project S62 #19, S95): `μ₀ = dε/dq|_{q*}`, `ρ_vac(q*) = ε − μ₀q* = 0` exactly (Gibbs-Duhem constraint); interior equilibrium `q* = 0` (S99 npz).
- **GD-2** (quadratic well): `ρ_vac(q) = ½·k_curv·q²` with `k_curv = +3586.5312` — the linear term vanishes IDENTICALLY because μ₀ is the equilibrium chemical potential. Vacuum compressibility `χ = ∂q/∂μ = 1/k_curv = 2.788e-4`. [This is the substrate-forced exponent-on-q = 2 — the S99 W2 leg.]
- **GD-3** (Hubble-sourced local state; Volovik dS local thermodynamics, Paper 11 + the 2023–25 dS-thermodynamics corpus): local temperature `T(H) = H/π`; bulk dS entropy density `s(H) = 3H/(4G)` (the volume density whose Hubble-volume integral reproduces Gibbons-Hawking `A/4G`). Eliminating H: `s(T) = (3π/4G)·T` — the dS heat bath has LINEAR-in-T entropy density.
- **GD-4** (the μ(H) shift): Gibbs-Duhem `dP = s·dT + n_q·dμ` across the quasi-static shift at vacuum pressure balance (`dP = 0`): `δμ(H) = −(1/n_q)∫₀^T s dT′ = −(1/n_q)(3π/8G)T² = −(3/(8πG·n_q))·H²`. **Quadratic in H — leading order H², EVEN.**
- **Parity theorem** (the structural reason no linear term can exist): T and s are |H|-odd (only the dissipative sector distinguishes expansion from contraction); the Gibbs-Duhem potential shift `∫s dT` is therefore |H|-EVEN. NO substrate-internal *equilibrium thermodynamic potential* can carry a term linear in H. An H-linear coupling is odd-sector (dissipative) — and in the friction ODE the odd sector is exactly the `3Hq′` friction already explicit, NOT a potential term. The H-linear `q_eq` of the simple-fluid closure is therefore structurally outside the equilibrium-thermodynamics sector: it can only be IMPOSED.
- **GD-5** (tilted-well minimum): `V_eff(q) = ½k_curv q² − δμ(H)·q ⟹ q_eq(H) = χ·δμ(H) = κ₂·H²` with `κ₂ = 3/(8πG·n_q·k_curv)` — **exponent LOCKED at 2**; the coefficient is a fixed substrate expression (G: a₂-channel; n_q: q-charge density; k_curv: D_K eigenfrequency response) with no tunable parameter.

*Integration + tail regression* (friction ODE `q″ + 3H(τ)q′ + k_curv(q − q_eq(H(τ))) = 0` on `arr_H_bare_t`, 999-pt backbone τ ∈ [0.1903, 0.4508], RK45 rtol=1e-8/atol=1e-10/max_step=0.01 per the plan pin; `ω = √k_curv = 59.888`, period 0.1049 — ~2.5 oscillation periods over the window; ln-ln LSQ over the **FULL final-50% tail**, τ ≥ 0.320521, n_tail = 500, ln-H tail range 0.5615, grid uniform to 9.0e-14):

| run | drive | slope = d ln q/d ln H | R² | f_used |
|:----|:------|:----------------------|:---|:-------|
| **GD (PRIMARY)** | `q_eq = κ₂H²` (substrate-derived, exponent-locked) | **2.055551** | 0.9955 | **1.0000** |
| GD ×10κ₂ | coefficient-invariance probe | 2.055551 (dev 7.56e-8) | 0.9955 | 1.0000 |
| GD off-IC (×2) | IC-robustness probe | 2.258285 | — | 1.0000 |
| LIN (imposed) | `q_eq = c·H`, c = 0.15 (S99 closure) | 1.008273 | 0.9590 | 1.0000 |
| BARE | `q_eq = 0` (S99 oscillator) | 3.415907 | 0.0790 | 0.4100 |

`domain_used_frac (PRIMARY) = 1.0000` — the regression used the FULL post-fold tail unconditionally (all 500 points, q > 0 throughout); the S99 W2-1 `domfrac = 0.41` BREAKDOWN pattern is fully avoided ⇒ `regime_verdict = VALID`.

*Cross-checks*:
- **XC-1 transmission**: `|slope_GD − 2| = 0.0556` — the locked drive exponent transmits through the adiabatic tracking with a small dynamical excess. The excess is real tracking-lag: the backbone's Ḣ-spike (max 4.41) sits just inside the tail, where the drive-rate parameter `ε_ad = max|2Ḣ/H|/ω = 0.897` is locally marginal (elsewhere on the tail `3H ≤ 0.92 ≪ ω = 59.9`, deeply adiabatic). The measured slope is the drive exponent 2 plus this lag correction — nowhere near 1.
- **XC-2 imposed-closure reproduction**: `slope_LIN = 1.008273` vs S99 `slope_driven = 1.0082729` — dev 4.6e-8 (my RK45 vs S99 Radau). Exact reproduction of the S99 imposed-closure leg.
- **XC-3 k_curv pin**: npz `K_CURV = 3586.5312` vs plan pin 3586.5 — dev 0.031 (the plan pin is the 5-sf print). Consistent.
- **XC-4 backbone identity**: `arr_H_traj` (w2 npz) ≡ `arr_H_bare_t` (w1 npz), max|ΔH| = 0.0 — the two pinned inputs carry the same backbone.
- **XC-5 κ₂-invariance**: slope shift under κ₂ → 10κ₂ is 7.56e-8 — the multiplicative-normalization cancellation identity (`math-scripts.md` §"Multiplicative-normalization cancellation invariants": the log-derivative annihilates any multiplicative pre-factor `w(κ)·g(H)`). **No coefficient-level freedom can ever tune the slope; only the exponent moves it, and the exponent is GD-locked.**
- **XC-6 IC-robustness**: off-drive (×2) start shifts the tail slope to 2.258 (+0.20) — the weakly damped oscillation (envelope decay e^{−(3/2)∫H dτ} ≈ 0.93 over the window) leaves a residual-oscillation systematic of ~±0.2 on the slope for generic ICs. It moves the slope AWAY from 1, not toward it: the verdict is IC-robust.
- **XC-7 quadratic-well validity**: `V(q_eq,max) = ½·3586.53·0.6720² = 809.75` vs `a_0_FW_zeta = 6440.0` → ratio 0.1257 < 1 (and 0.0099 vs the S97 `rho0_ref = 81493`) — the GD-2 quadratic expansion is valid over the whole driven range.
- **BARE diagnostic**: `slope_BARE = 3.415907` vs S99 3.415925 (dev 1.8e-5), `f_used = 0.4100` exactly matching S99 — the full S99 pipeline is reproduced by this script before the new physics is added.

*Substitution chain with substituted numbers (chain Step D / Direction, executed)*:
`n = (exponent-on-q) × (d ln q/d ln H) = 2 × 2.0556 = 4.11` under the substrate-derived drive — the GD drive produces an **n ≈ 4 vacuum-response law on a fixed backbone, not the n = 2 tracking law**. For n = 2 the chain requires slope = 1 exactly; measured `|slope − 1| = 1.055551 > 0.05` (pass band). Sign leg: predicted positive co-tracking (q decays/grows with H); measured slope +2.06 > 0 ⇒ `sign_verdict = PASS`. Magnitude leg: `|slope − 1| > 0.05` AND κ₂-invariant (no residual parameter tunes the slope toward 1 — the plan's INFO branch antecedent structurally cannot fire) ⇒ `magnitude_verdict = FAIL`. Regime: `f_used = 1.0000 ≥ 0.95`, solver healthy ⇒ `VALID`.

**Residual-free-parameter disclosure** (explicit, per the plan's honest-disclosure clause):
1. **Candidate (i), GD μ-tilt (PRIMARY)**: carries NO tunable closure parameter. The exponent (2) is locked by `s ∝ T` Gibbs-Duhem integration + the quadratic well; the coefficient `κ₂ = 3/(8πG·n_q·k_curv)` is a fixed substrate expression whose *numerical* value in backbone units is not extractable inside this gate (needs the q-charge density n_q and the §6.3 G-normalization, both outside the pinned inputs) — but the slope is rigorously κ₂-INVARIANT (XC-5, structural identity), so the verdict is κ₂-independent. The κ₂ used in the integration is a disclosed *diagnostic normalization* (`|q_boundary|/H_max² = 7.19704`), slope-irrelevant by the cancellation identity.
2. **Candidate (ii), §6.3 inversion `H² = f(ρ_relic, S_SA)`**: inverting the emergent-Friedmann closure for a q-sector energy gives `q_eq = √(2λ_q·ρ_crit(H)/k_curv) ∝ H` ONLY by (a) introducing the free q-share `λ_q` AND (b) asserting "q-sector energy = fixed fraction of the critical density" — which IS the tracking ansatz restated (circular as a derivation). λ_q tunes the amplitude, never the slope (same cancellation identity), so candidate (ii) is not a substrate derivation of the linear form; it is the imposed closure re-dressed. Disclosed and excluded as a derivation route.
3. The only remaining freedoms anywhere in the chain — the dS-temperature convention (`T = H/π` vs `H/2π`) and the §6.3 G-normalization — enter the COEFFICIENT only, never the exponent, and are therefore slope-irrelevant by XC-5.

**Assessment (solution-space interpretation)**. The corridor "n = 2 emerges as an unforced attractor of the friction ODE on the fixed bare backbone" is now closed on both flanks: (a) bare ODE → slope 3.42 with window breakdown (S99); (b) the honest substrate-internal equilibrium drive → slope 2.06, exponent-locked, parameter-free, κ₂-invariant (this gate); (c) slope 1 obtains exactly and only under the imposed `q_eq = c·H` simple-fluid closure (S97/S99, reproduced here at 1.008273). The structural finding sharpens the plan's FAIL branch: it is NOT that "no substrate drive exists" — a parameter-free drive exists and is now derived — but that the substrate's equilibrium-thermodynamic sector is EVEN in H (parity theorem), so no substrate q_eq(H) can carry the odd-in-H linear form that slope = 1 requires on a fixed backbone. In Volovik's own corpus (Klinkhamer-Volovik relaxation, Papers 25 §V / 35), `ρ_vac ~ H²` arises by a THIRD mechanism available to neither run here: oscillation-energy self-consistency, where the q-oscillation energy itself dominates the Friedmann closure, redshifts dust-like (amplitude ∝ a^{−3/2}), and on the SELF-CONSISTENT background a ∝ t^{2/3} this gives amplitude ∝ H — slope 1 from back-reaction, not from a drive. That mechanism is structurally outside this gate's fixed-backbone design (the backbone is pinned, not q-sourced) and is the genuine forward question: a self-consistent gate in which H(τ) is re-derived from the q-oscillation energy through the §6.3 closure, testing whether slope → 1 emerges when the backbone itself responds. Until then, the `d ln q/d ln H = 1` leg is what S99 said it was — the imposed-closure input — now with the reason (H-parity) rather than only the observation. C10 Object-C: STRUCTURALLY-CONDITIONAL; capstone §8.5: OPEN by design; DILUTION-CC residual conditionality on the q∝H closure: pinned, with its structural locus identified.

**Substrate framing** (PHONONIC): the cosmological constant IS the a₀ zeroth spectral moment (`a_0_FW_zeta = 6440.0`, ζ-regulated) — a different spectral moment than gravity (a₂). The Volovik vacuum variable q IS the substrate's own slow degree of freedom; `V(q) = δρ_vac` IS the GGE/zero-point response of the D_K eigenfrequencies (k_curv from the 992-mode ω_n(q) response). The arrow flows D_K eigenvalues → a₀ → V(q) → friction-ODE relaxation → vacuum-energy history. The friction ODE is the substrate's OWN relaxation, not a scalar field rolling IN a container; the gate's scientific content is precisely that the substrate's internal equilibrium thermodynamics (T = H/π heat bath, bulk entropy s = 3H/4G) CANNOT supply the odd-in-H drive that the externally-imposed CPL fluid law smuggles in.

**Output Artifacts**:
- `computations/session-100a/s100a_w1_qeq_drive.py` — producing script (contains `from canonical_constants import`, `print_verdict_payload`; OMP_NUM_THREADS=8 capped before numpy import per the GPU_path pin)
- `computations/session-100a/s100a_w1_qeq_drive.npz` — full data (5 trajectories, slopes, R², cross-checks XC-1…XC-7, tail mask, dual-SHA)
- `computations/session-100a/s100a_w1_qeq_drive.png` — 4-panel figure (backbone+drives; trajectories; tail ln-ln regression with slope-2.056/1.008/target-1 lines; derivation+verdict summary)
- Verdict line (via race-safe `emit_verdict`, 5 rows): `S100a-W1-2-QEQ-DRIVE: FAIL -- value='slope_GDtilt_H2=2.055551_dev1=1.055551_exp_locked_EVEN_in_H_kappa_inv=True_slope_imposed_cH=1.008273_slope_bare=3.4159_domfrac=1.0000_kcurv=+3586.53_no_slope1_capable_substrate_drive_C10-ObjectC-STRUCTURALLY-CONDITIONAL' scheme=FW convention=SUBSTRATE-NATURAL-BINDING L_max=N/A audit_sha256=e31d45cf5309b32cde67804d0576467592196b45ea908ec1edfac7f522212ca4 content_sha256=77683aa76cb1b03137648718da5df91373d325967504ce3b92b56391690a4dc9 schema_version=S84+` + dual-SHA companion row + schema-v2 3-tuple row (`sign=PASS magnitude=FAIL regime=VALID`) + regulator-pin row (`a_0^{ζ}`) + domain_used_frac row (1.0000, full tail)
- Carry-forward candidate for the wave synthesis (4-field-spec-able): self-consistent back-reaction gate — re-derive H(τ) from the q-oscillation energy through the §6.3 closure (`H² = f(ρ_q, S_SA)`) and test whether slope → 1 emerges from q-domination self-consistency (the corpus-faithful Klinkhamer-Volovik mechanism, structurally unavailable on a fixed backbone). Inputs: this gate's npz + s99 backbone; gate: `|slope_selfcons − 1| ≤ 0.05`; effort ~1 wave.

---

### §W1-3. S100a-W1-3-NS-NLO (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-W1-3-NS-NLO`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The second-order slow-variation (NLO) correction to the PROVEN leading-order tilt `n_s = 0.9561` is small — `|Δn_s^{NLO}| < 0.003` — so the headline tilt is NLO-precision-stable and the leading-order value remains canonical.
**Plan reference**: `sessions/session-plan/session-100a-plan-w1.md` §W1-3 (constant-ε slow-roll NLO term from a₂/a₄ moments, Planck-band discrimination floor, regulator_pin a_2^{ζ}/a_4^{ζ}).

**Verdict**: **PASS** (composite, canonical collapse rule; schema-v2 3-tuple: sign_verdict=PASS, magnitude_verdict=PASS, regime_verdict=VALID). `Δn_s^{NLO} = −9.636e-4` (4 s.f.; exact rational `−192721/200000000`), NEGATIVE as pre-registered (slow-roll reddens), `|Δn_s^{NLO}| = 9.636e-4 < 0.003` → the leading-order tilt n_s = 0.9561 is **NLO-precision-stable**; the headline LO value remains the canonical anchor without an NLO caveat. Track-A posterior re-allocation per the plan's dual-prior discriminator (PASS → 0.9 to Track A).

**Results**:

Output 4-tuple: `(value=Δn_s^{NLO}=−9.636050e-04, scheme=FW, convention=CONSTANT-EPSILON-SLOW-ROLL-NLO, L_max=10)`.

*Substitution chain (executed exactly per plan §W1-3 item 7, substituted numbers):*

- **Def 1 (LO anchor, exact)**: `n_s^{LO} = n_s_FW_exact = Fraction(9561,10000) = 0.9561` (canonical, S84 T6 / S85 W9-3 / S88 W-15) ⇒ `ε_H = (1 − n_s^{LO})/2 = Fraction(439,20000) = 0.02195` EXACT. Moment provenance: the S84 T6 constant-ε derivation builds ε_H from the `a_2^{ζ} = 2776.165389` / `a_4^{ζ} = 1350.7216` zeta-regulated Seeley-DeWitt ratios along the B1 trajectory (regulator_pin per `regulator-pin-discipline.md`; canonical imports `a_2_FW_zeta`, `a_4_FW_zeta`, no hardcodes).
- **Def 2 (NLO coefficient, framework-internal)**: the registered EXACT theorem **[T6] Constant-Epsilon — n_s = (1−3ε)/(1−ε)** (atlas-07, W4-01) has exact series `1 − 2ε − 2ε² − 2ε³ − …` (every coefficient beyond order 0 is exactly −2; verified in ℚ at truncation orders k = 1..5 via `n_s^{T6} − [1 − 2Σ₁ᵏεⁿ] ≡ −2ε^{k+1}/(1−ε)`). Hence **C₂ = 2 EXACT**: `n_s^{NLO} = 1 − 2ε_H − 2ε_H² = 191027279/200000000 = 0.955136395` and `Δn_s^{NLO} = −2ε_H² = −192721/200000000 = −9.636050e-4`. Two-route cross-check: the standard second-order Hubble-flow tilt `n_s − 1 = −2ε₁ − ε₂ − 2ε₁² − (2C+3)ε₁ε₂ − Cε₂ε₃` (C = γ_E + ln2 − 2 = −0.7296371545) at ε₂ = 0 reproduces the same value, route diff `1.110e-16 < 1e-12` (plan tolerance pin).
- **Def 3 (η_H, a₄-pulled curvature)**: on the T6 constant-ε class `η_H ≡ ε₂ = d ln ε_H/dN = 0` IDENTICALLY — forced by the LO anchor itself (ε₂ enters the tilt LINEARLY as −ε₂; any ε₂ ≠ 0 at the pivot would shift the PROVEN bit-exact LO value at first order). Off-class envelope quantified two ways: (a) **a₄-pulled proxy** `η_H^{a4} = ε_H·(a_4^{ζ}/a_2^{ζ}) = 0.02195 × 0.486542 = 0.010680` → η-term `|(2C+3)·ε_H·η_H| = 3.612e-4`, envelope `|Δ| = 1.325e-3`; (b) **empirical ε_H-spread** vs the independent S80 dS/dτ route (`eps_H_W6 = 0.02163`): `Δε_H = 3.2e-4`, ΔN = 1 maximally conservative `η_H^{spread} = 0.014579` → η-term `4.930e-4`, worst envelope `|Δ| = 1.457e-3`. Full envelope `|Δn_s^{NLO}| ∈ [4.706e-4, 1.457e-3]` — **all < 0.003**.
- **Sign**: `Δn_s^{NLO} = −9.636e-4 < 0` — NEGATIVE, matching the [SIGN] pre-registration (slow-roll reddens: n_s^{NLO} < n_s^{LO}). Sign-flip would require `|η_H| > 2ε_H/(2C+3) = 0.028493 = 1.298×ε_H`; both proxies are ≤ 0.66×ε_H → sign ROBUST across the entire envelope.
- **Direction read-off**: `|Δn_s^{NLO}| = 9.636e-4 < 0.003` ⇒ NLO does not move the tilt out of its Planck σ-band ⇒ PASS branch of the pre-registered rubric.

*Cross-checks:*

1. **T6-exact (all-orders) residual**: `n_s^{T6-exact} = 18683/19561 = 0.955114769`; NNLO+ residual `−2ε³/(1−ε) = −2.163e-5` = 2.24% of the NLO term — the NLO truncation is self-consistently adequate (regime VALID: series convergence ratio `ε/(1−ε) = 0.0224 ≪ 0.1`).
2. **Planck σ-distance** (`planck_ns = 0.9649 ± 0.0042`): σ_LO = 2.0952 → σ_NLO = 2.3247, shift **0.2294σ < 0.7σ** — stays inside the same Planck σ-band, confirming the plan's analytic-boundary note (0.003 = half-width of the LO-vs-Planck discrimination band).
3. **Two-route C₂**: T6 exact series (framework-internal) and Hubble-flow second-order formula (Stewart-Lyth C-coefficient form) agree at 1.1e-16.
4. **Round-trip (Class 8.3)**: full float64 + exact integer rationals (num/den pairs) → `s100a_w1_ns_nlo.npz`; WP publishes 4 s.f. (`Δn_s^{NLO} = −9.636e-4`, publication-precision pin per plan item 5; downstream verifiers load the npz, rel_tol ≥ 1e-4).

*Functional-sensitivity classification (lizzi output standard):* the NLO coefficient **C₂ = 2 is FUNCTIONAL-INDEPENDENT** (structural — fixed by the constant-ε trajectory class through the exact mode solution / T6 theorem; invariant under cutoff vs zeta spectral-functional choice). The **value of ε_H is scheme-tagged** (zeta-regulated moment route, `a_2^{ζ}/a_4^{ζ}` at L_max=10); the η-envelope inputs mix routes (a₄/a₂ zeta ratio; eps_H_W6 cutoff-route dS/dτ pin) — and the PASS verdict is invariant across the entire mixed-route envelope, so the **precision-stability verdict itself is FUNCTIONAL-INDEPENDENT**.

*Substrate framing (PHONONIC)*: the tilt IS a spectral observable of the gauge-invariant spectral geometry — the arrow flows D_K eigenvalues → a₂/a₄ Seeley-DeWitt moments (a_2^{ζ}, a_4^{ζ}) → slow-variation parameters (ε_H, η_H) → n_s. The NLO term is the next term in the spectral-action slow-variation expansion; its smallness shows the headline 0.9561 is a stable spectral prediction of the supersonic transit through the van Hove fold, not an artifact of leading-order truncation. No inflaton-on-a-potential vocabulary: the constant-ε class is the transit's spectral-moment flow, not a field rolling IN a container.

**MCP Pre-Compute Audit**:

1. `search_knowledge("n_s NLO second-order slow-roll correction precision")` → no prior Δn_s^{NLO} evaluation anywhere in the graph; gate NOT pre-closed. Salient adjacent hits: [NEW S42] slow-roll n_s theorem (eta=0.243, pre-constant-ε era) and the `eps_H_W6` NLO-margin-cap edge (S80/S85) — margin idea existed, the NLO term itself was never computed.
2. `get_constant("n_s_framework")` → 0.9561, S84 T6 constant-epsilon gauge-invariant spectral geometry, bit-exact `n_s_FW_exact = Fraction(9561,10000)` (S88 W-15 W15-V.2), NOT superseded.
3. `get_constant("a_2_FW_zeta")` → 2776.165389 (S88-A-N-FW-CANONICALIZATION), NOT superseded; `get_constant("a_4_FW_zeta")` → 1350.7216 (S75), NOT superseded — both match the plan-freeze pins.
4. `search_knowledge("constant-epsilon gauge-invariant spectral geometry T6 eps_H 0.02195")` → **[T6] Constant-Epsilon Theorem n_s = (1−3ε)/(1−ε), Exact** (atlas-07 permanent results, W4-01) — the framework-internal anchor that pins C₂ = 2 without external import.
5. `trace_entity("eta_H second slow-roll parameter")` → no trace; η_H was never separately canonicalized — the η-envelope quantification here is new content, consistent with the constant-ε class where η_H = 0 on-trajectory.

**Output Artifacts**:

- Script: `computations/session-100a/s100a_w1_ns_nlo.py` (imports `from canonical_constants import *`; emits payload via `print_verdict_payload`; exact-Fraction backbone; OMP_NUM_THREADS=8 capped before numpy per machinery pin)
- Data: `computations/session-100a/s100a_w1_ns_nlo.npz` (full float64 + exact num/den integer rationals, envelopes, σ-distances, bands, verdict strings, dual SHAs)
- Plot: `computations/session-100a/s100a_w1_ns_nlo.png` (tilt ladder LO/NLO/T6-exact vs Planck ±1σ/±2σ band; log-scale NLO magnitude budget vs 0.003/0.009 bands)
- Verdict line: `computations/session-100a/s100a_gate_verdicts.txt` — canonical line + dual-SHA companion + schema-v2 3-tuple row + 2 extra rows (regulator_pin; eta_H-envelope), emitted via the race-safe `emit_verdict` MCP tool. `audit_sha256=05d2f2da0e43056e04e66b5d922d7d3dd320b1a15fa95022fa9ffade50b89310`, `content_sha256=d4d44db310ae83731e1c0dec76c86642c4907f48b12646d00f721f976dd0cf93`.

---

### §W1-4. S100a-W1-4-SIGMA-DM-NUCLEON (landau-condensed-matter-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-W1-4-SIGMA-DM-NUCLEON`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC**
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The spin-independent DM-nucleon cross-section σ_SI of the Leggett-channel GGE quasiparticle (mass `M_DM = 11.97·Δ_BCS·M_KK`) lies below the LZ/XENONnT exclusion at that mass and at/below the neutrino fog — a falsifiable-but-currently-unexcluded direct-detection prediction consistent with the collisionless σ/m anchor.
**Plan reference**: `sessions/session-plan/session-100a-plan-w1.md` §W1-4 (closed-form M_DM + σ_SI from Leggett-channel constants, LZ-2024 exclusion digitization, laboratory-vs-substrate rest-energy frame resolution; mack-cosmic-bridge writes any falsifier-inventory row).

**Verdict**: **PASS** — σ_SI(M_DM) = 1.30e-63 cm² sits **30.92 OOM below** the LZ-2024 exclusion and **30.02 OOM below** the xenon neutrino fog at M_DM = 4.13e17 GeV. Schema-v2 3-tuple: `sign_verdict=PASS` (sign(σ_excl − σ_SI) = +1, the pre-registered PASS direction), `magnitude_verdict=PASS` (σ_SI ≤ σ_νfog — at/below the fog), `regime_verdict=VALID` (frame resolved: Frame A binds; verdict frame-robust; flux-floor and Born-regime checks VALID). Composite per the pre-registered collapse rule: PASS.

**Results**:

4-tuple: `(value=sigma_SI=1.299e-63_cm2_at_M_DM=4.128e+17_GeV(FrameA-substrate-anchor-binds);..., scheme=FW, convention=LEGGETT-CHANNEL-SUBSTRATE-COUPLING, L_max=N/A)`

| Quantity | Value | Provenance |
|:---------|:------|:-----------|
| M_DM (substrate units) | 5.5571 M_KK = 11.97 × Δ_BCS | `Mass_LeggettDM_over_Delta_BCS=11.97` (LEGGETT-MOMENT-70) × `Delta_BCS=0.4642547394830737` (BCS-GAP-CANONICAL-70, R-protected) |
| M_DM laboratory rest energy (Frame A, **binds**) | **4.128202e17 GeV** (3 sf: 4.13e17) | × `M_KK=7.428660036284456e16` GeV (CONST-FREEZE-42) |
| σ_SI per nucleon (canonical) | **1.298925e-63 cm²** (3 sf: 1.30e-63) | pure gravitational vertex α_A = G_N M_DM m_Xe = 3.387e-19; full float64 in npz |
| σ_A(Xe, >E_th) | 3.729e-55 cm² | Rutherford recoil spectrum, E_th = 5 keV, v = 1.1e-3 c |
| σ_excl^LZ(M_DM) | 1.073e-32 cm² | digitized LZ-2024 curve, iso-rate σ ∝ M extrapolation beyond 1e4 GeV |
| σ_νfog(M_DM) | 1.362e-33 cm² | digitized Xe n=2 fog (O'Hare 2021), same extrapolation |
| Margin below exclusion / fog | 30.92 / 30.02 OOM | sign(σ_excl − σ_SI) = +1 |
| DM-DM σ_T/m at Bullet v | 1.688e-53 cm²/g ≤ anchor 5.7e-51 | CC1, `sigma_over_m` (S42, promoted to canonical_constants this gate) |

**Substitution chain** (sign claim, math-scripts.md; substituted numbers):

```
Claim: sigma_SI(M_DM) < sigma_excl^LZ(M_DM)
Step 1: M_DM = Mass_LeggettDM_over_Delta_BCS * Delta_BCS * M_KK
             = 11.97 * 0.4642547394830737 * 7.428660036284456e16 GeV
             = 4.128202e17 GeV                       [Frame A binds; see resolution below]
Step 2: alpha_A = G_N * M_DM * m_Xe = (1/M_Pl^2) M_DM m_Xe
              = 6.7087e-39 * 4.1282e17 * 122.295 = 3.3870e-19   [pure gravitational vertex]
Step 3: sigma_A(>E_th) = (2 pi alpha_A^2/(m_Xe v^2))(1/E_th - 1/E_max)
              = 3.7291e-55 cm^2     [E_max = 2 mu_A^2 v^2/m_Xe = 296 keV; E_th = 5 keV]
Step 4: sigma_SI = sigma_A / [A^2 (mu_A/mu_n)^2 (1 - E_th/E_max)] = 1.2989e-63 cm^2
              [equal-above-threshold-rate contact-SI per-nucleon normalization
               = the axis the LZ curve is published on]
Step 5: sigma_excl^LZ(M_DM) = sigma_excl(1e4 GeV) * (M_DM/1e4) = 1.0733e-32 cm^2
              [iso-rate scaling exact at M >> m_A: rate ~ (rho/M) sigma]
Step 6: sign(sigma_excl - sigma_SI) = sign(1.073e-32 - 1.299e-63) = +1
        => BELOW exclusion (PASS direction), 30.92 OOM margin; 30.02 OOM below fog.
```

**Laboratory-frame vs substrate-M_KK-scale rest-energy resolution (Def 1 core — FRAME A BINDS)**:

- **Frame A (BINDS)**: M_DM^lab = 11.97·Δ_BCS·M_KK = 4.128e17 GeV — the substrate anchor read through the framework's **single unit map**. Three independent arguments: (i) the spectral triple converts M_KK units to GeV exactly once, via the a_2/G_N gravity bridge (CONST-FREEZE-42); every GeV-valued framework observable (KK tower, m_H threshold corrections, v_ew) uses this one conversion — a mode-specific second conversion does not exist in the spectral triple and introducing one would un-pin every PROVEN GeV-valued result. (ii) The Leggett mode is a **gapped quasiparticle**: emergent-4D dispersion ω²(k) = ω₀² + c²k² with ħω₀ = 11.97·Δ_BCS·M_KK; by the Landau quasiparticle correspondence (E² = (mc²)² + (cp)²) the laboratory rest energy IS ħω₀ — rest energy is frame-invariant, the relic is comoving (T^{0i}_4D = 0 exact, atlas-04 C7), and the laboratory moves at only v ~ 1e-3 c relative to it. (iii) GGE bookkeeping: the Parker-pair relic energy budget is fixed in M_KK units; rescaling the per-quantum mass by ~17 OOM without rescaling number density would break the Ω_DM closure by the same ~17 OOM.
- **Frame B (EXCLUDED reading)**: the gap-scale anchor misread as a laboratory-GeV rest energy, M_DM = 5.557 GeV. Computed anyway for frame-robustness: at 5.557 GeV the gravitational σ_SI(>E_th) is a **kinematic null** (E_max = 0.559 keV < E_th = 5 keV; an above-threshold Xe recoil requires v = 3.29e-3 c > the SHM ceiling 2.6e-3 c), i.e. trivially below exclusion as well. **The sign verdict is frame-robust** — the regime_verdict=VALID rests on the structural resolution (i)–(iii), not on the frame choice.

**Coupling-channel derivation (symmetry first — why σ_SI is the pure gravitational floor)**: (1) D_K is block-diagonal (S22b PERMANENT): inter-sector matrix elements vanish identically — no direct Dirac vertex between the BCS-sector coherence mode and SM zero modes. (2) V(gap,gap) = 0 EXACTLY (S23a selection rule) and B1 couples only to B2 (S34 Trap 1) — no cubic vertex routes inter-band coherence into SM channels. (3) The Leggett mode is a CPT-neutral gauge singlet; the relative-phase mode couples to band-density *differences*, so its linear coupling to total-mass-density probes vanishes — the leading surviving coupling is quadratic through the stress tensor. (4) Two-layer architecture (S72 PERMANENT): the BCS sector communicates with the spectral sector only through the metric moments (a_2 = gravity). Therefore α = G_N M_DM m_N with **zero free parameters** — the same coupling class as the S42/S44 collisionless anchor, which is itself the gravitational Rutherford transport cross-section (s44_cdm_construct.py: σ_T = 4π(G_N m)²/v⁴·lnΛ). Born validity: α_A/v = 3.1e-16 ≪ 1 (CC4 VALID). Helm form factor at threshold (qR_Xe ≈ 0.85) is O(1) — immaterial at ≥30-OOM margins, as is any alternative threshold/velocity convention (≤ few OOM).

**Cross-checks** (all PASS):
- **CC1 (σ/m anchor bounds the coupling)**: DM-DM gravitational transport at Bullet-Cluster velocity, σ_T/m = 1.688e-53 cm²/g ≤ anchor `sigma_over_m` = 5.7e-51 cm²/g — CONSISTENT (factor ~340 inside the bound; same zero-free-parameter G_N² class).
- **CC2 (independent event-rate route)**: N_transit(LZ exposure) = 12.1; P(>E_th scatter)/crossing = 7.24e-31; predicted events = 8.78e-30; event-route margin = 29.61 OOM vs curve-route 30.92 OOM; |diff| = 1.30 OOM ≤ 2.0 — the two independent comparison routes AGREE (residual bundles detector geometry/efficiency conventions).
- **CC3 (flux floor)**: 12.1 DM transits through LZ during WS2022+WS2024 — the iso-rate σ ∝ M extrapolation is inside its validity domain at M_DM (it evaporates only at M ≳ 1e19 GeV where fewer than one particle crosses).
- **CC4 (Born regime)**: α_A/v = 3.08e-16 ≪ 1 — deep Born regime, Rutherford form valid.

**Methodology notes (empirical-input digitization)**: `s100a_lz2024_si_exclusion.csv` digitized by this gate from the published LZ-2024 SI limit — LZ collaboration, arXiv:2410.17036, Fig. 6 (WS2022+WS2024 combined, 90% CL observed); published anchor exact: minimum 2.2e-48 cm² at 40 GeV (abstract); 24 points 9 GeV–1e4 GeV at ±0.15 dex figure-read fidelity. Xenon neutrino-fog n=2 boundary digitized from O'Hare, PRL 127, 251802 (2021) + the LZ-2024 plotted boundary (14 points, ±0.3 dex). Both are METHODOLOGICAL empirical cross-check inputs per substrate-first-canonical-sourcing §(i) (citation given; no substrate canonical replaced). Beyond 1e4 GeV both curves are extrapolated linearly in M (iso-rate scaling, exact for M ≫ m_A since rate ∝ (ρ/M)·σ with mass-independent kinematics); digitization fidelity is immaterial against ≥30-OOM margins. Curve interpolation: log-log, well inside the 1e-3 log10(σ) tolerance pin.

**Canonical write-order (executed)**: (1) verdict line emitted via `emit_verdict` (race-safe MCP; canonical line + dual-SHA companion + schema-v2 3-tuple row + frame-resolution companion row in `computations/session-100a/s100a_gate_verdicts.txt`); (2) `sigma_DM_nucleon_FW = 1.2989252548383697e-63` (cm²) and `M_DM_Leggett_GeV = 4.128202383934713e17` promoted to `canonical_constants.py` SECTION E via `update_constant` (session=S100a, source=S100a-W1-4-SIGMA-DM-NUCLEON; both inherit the C7/LEGGETT-MOMENT-70 conditionality Γ_grav < H_0); `sigma_over_m = 5.7e-51` cm²/g (S42 provenance) was promoted to module level pre-compute (it existed only in the audit allowlist). (3) Falsifier-master-inventory row: NOT this gate's — routes to mack-cosmic-bridge (sole writer) at session close.

**Substrate framing**: PHONONIC. Dark matter IS a Leggett-channel GGE quasiparticle — an inter-band coherence mode of the (0,0) BdG sector of D_K, CPT-neutral and non-annihilating. The arrow flows D_K eigenvalues → BdG gap Δ_BCS → Leggett inter-band coherence mode → DM rest mass (11.97·Δ_BCS·M_KK through the one a_2/G_N unit map) → nucleon coupling (gravitational floor, the only inter-sector channel) → σ_SI. A laboratory direct-detection experiment is substrate probing substrate: the coherence mode perturbing a nucleon fiber's eigenvalue spectrum — and the substrate says that perturbation is mediated by the a_2 moment alone. **Constraint-map reading**: the framework predicts a direct-detection NULL at every current and projected experiment (30 OOM below the fog); the falsifier INVERTS — any confirmed DM-nucleon scattering above the gravitational floor falsifies the Leggett-channel DM identity outright. This is a sharp, zero-free-parameter, pre-registered discriminator; per the plan's pre-registered dual-prior discriminator, the PASS outcome routes to Track A (suppressed nucleon coupling consistent with the collisionless anchor). What remains uncomputed: nothing within this gate; the observational row lands via mack-cosmic-bridge.

**Output Artifacts**:
- `computations/session-100a/s100a_w1_sigma_dm_nucleon.py` — producing script (`from canonical_constants import *`, `print_verdict_payload`); exit 0
- `computations/session-100a/s100a_w1_sigma_dm_nucleon.npz` — full-float64 results (masses both frames, σ_SI, curves, margins, CC1–CC4, machinery pins)
- `computations/session-100a/s100a_w1_sigma_dm_nucleon.png` — (M, σ_SI) plane: LZ-2024 curve + iso-rate extrapolation, fog boundary + shaded fog region, Frame-A point (star), Frame-B dotted line
- `computations/session-100a/s100a_lz2024_si_exclusion.csv` — LZ-2024 digitization (header carries source + fidelity + date)
- Verdict line: `S100a-W1-4-SIGMA-DM-NUCLEON: PASS ...` in `computations/session-100a/s100a_gate_verdicts.txt`; `audit_sha256=206a7453699145089f96d07ca56298cf951926dcfc3c39a10b373e0f96b8a444`, `content_sha256=16da18e9adbb9cec1fc1783f3d46d80ae55f1f45d07659343889b25a6c5a150c`; dual-SHA companion + 3-tuple (`sign=PASS magnitude=PASS regime=VALID`) + frame-resolution rows present

**MCP Pre-Compute Audit**:
- `search_knowledge("Leggett DM nucleon cross-section direct detection sigma_SI")` — no prior σ_SI(DM-nucleon) gate exists; nearest hits are abundance gates (LEGGETT-DM-ABUND-60 FAIL lineage) and the C7 conditional anchor — gate NOT pre-closed.
- `search_knowledge("sigma_over_m collisionless self-interaction 5.7e-51")` — atlas-04 C7 + atlas-07 row "[NEW S42] sigma/m (CDM) = 5.7e-51 cm²/g Computed" confirm the anchor's provenance.
- `search_knowledge("neutrino fog LZ XENONnT exclusion direct detection")` — no prior LZ digitization in the corpus; CSV creation confirmed as this gate's first step.
- `get_constant("Mass_LeggettDM_over_Delta_BCS")` = 11.97 (LEGGETT-MOMENT-70; CONDITIONAL Γ_grav < H_0) — matches plan pin.
- `get_constant("Delta_BCS")` = 0.4642547394830737 (R-protected) — matches plan pin.
- `get_constant("M_KK")` = 7.428660036284456e16 GeV (CONST-FREEZE-42) — matches plan pin.
- `get_constant("sigma_over_m")` — NOT FOUND at module level (allowlist-only); promoted to `canonical_constants.py` SECTION E with S42 provenance BEFORE compute (math-scripts.md mandate), then imported.
- `trace_entity("DIRECT-58")` — resolves to EPSILON-DIRECT-58 (effacement gate, unrelated) — confirms no prior direct-detection σ computation. Structural priors retrieved: V(gap,gap)=0 EXACT (S23a), single-Leggett gravitational decay FORBIDDEN (S67), T^{0i}_4D=0 exact (C7).

---

## Wave 1 Synthesis (team-lead)

**Date**: 2026-06-06. **Gates**: 4 (2 PASS, 1 INFO, 1 FAIL). All four `[SIGN]`-trigger gates carry canonical verdict lines with full 64-char dual-SHA closures + schema-v2 3-tuple companion rows in `computations/session-100a/s100a_gate_verdicts.txt`; all artifacts on disk and content-verified (every `output_artifacts:` must_contain pattern matched).

### 1. The a(t)/C10 keystone-successor pair: both corridors closed WITH MECHANISMS NAMED (W1-1 ∧ W1-2)

The two EVOI Tier-1 successors to the S99 corridor-maps did not merely re-confirm the S99 readings — each replaced an observation with a structural theorem.

**W1-1 (INFO, Track B 0.9)**: the **frame-map theorem** — any conformal reframing acts on the deceleration history as the exact affine map `q̃ = A(τ)·q + B(τ)` with `A = (H_bare/H̃)² > 0`, and for any CONSTANT normalization `A ≡ 1, B ≡ 0` because q is a logarithmic-derivative observable. The three-map ladder (canonical const-Ω = identity; acoustic frame ILL-DEFINED by the S98-proven 0/0; CD-frame comparison-DEGENERATE/circular) exhausts the admissible corrections: **the S99 band-miss is FRAME-ROBUST** (`band_frac_corrected = 0.5015 < 0.90`, miss entirely one-sided below −0.97). The SF54 band is generated in a conformal frame ~26× faster than the bare backbone and conflates pre-fold/post-fold regimes — it is the WRONG band, and the substrate is structurally mostly-accelerating post-fold (median q = −0.8662). Downstream: capstone §7.1 LRD deceleration-history row re-scope → `mack-cosmic-bridge` (capstone-hygiene Q2/Q3).

**W1-2 (FAIL, Track B 0.9)**: the **H-parity theorem** — the wave's structurally weightiest finding. A parameter-free substrate drive EXISTS (Gibbs-Duhem μ-tilt: `q_eq = κ₂H²`, exponent LOCKED by `s ∝ T` integration + the quadratic well; slope κ₂-INVARIANT at 7.6e-8 by the multiplicative-normalization cancellation identity), but T and s are |H|-odd ⟹ every equilibrium-thermodynamic potential shift `∫s dT` is |H|-EVEN — **no substrate equilibrium drive can carry the odd-in-H linear form that slope-1 requires; the odd sector IS the `3Hq′` friction**. Measured slope 2.0556 (full-tail, `domain_used_frac = 1.0000`, no W2-1-style breakdown); slope 1 obtains only under the imposed `q_eq = c·H` closure (reproduced 1.008273, dev 4.6e-8 vs S99). The `d ln q/d ln H = 1` leg of the n=2 tracking law is **structurally a fluid-closure INPUT** on any fixed backbone. C10 Object-C → STRUCTURALLY-CONDITIONAL; capstone §8.5 stays OPEN by design (corridor-map only, per the plan's decision table — no capstone-status change). The surviving corridor is corpus-faithful Klinkhamer-Volovik **oscillation-energy self-consistency** (back-reaction, q-sourced backbone) — structurally unavailable on a pinned backbone, hence the CF below.

### 2. Register-sourced Tier-2 pair: two zero-free-parameter observational anchors confirmed (W1-3 ∧ W1-4)

**W1-3 (PASS)**: `Δn_s^{NLO} = −2ε_H² = −9.636050e-4` EXACT (`−192721/200000000`; C₂ = 2 exact from the registered [T6] theorem, two-route cross-check at 1.1e-16), `< 0.003` with the entire mixed-route η-envelope `[4.7e-4, 1.457e-3]` inside the band and the negative sign robust (flip needs `|η_H| > 1.298×ε_H`; proxies reach 0.66×). Planck σ-distance shifts 2.095σ → 2.325σ (0.23σ < 0.7σ). **n_s = 0.9561 is NLO-precision-stable**; the precision-stability verdict is itself FUNCTIONAL-INDEPENDENT. Per the plan's PASS branch: no §7 change.

**W1-4 (PASS)**: σ_SI = 1.299e-63 cm² at M_DM = 4.128e17 GeV — the pure gravitational vertex, **forced by symmetry with zero free parameters** (block-diagonality S22b + V(gap,gap)=0 S23a + Trap-1 S34 + CPT-neutral singlet + two-layer architecture S72 ⟹ the only inter-sector channel is a₂). 30.92 OOM below LZ-2024, 30.02 OOM below the xenon ν-fog; frame-robust (Frame A binds on three independent arguments; Frame B is a kinematic null anyway); CC1-CC4 clean including the σ/m collisionless-anchor consistency (factor ~340 inside). **The framework predicts a direct-detection NULL at every current and projected experiment, and the falsifier INVERTS**: any confirmed DM-nucleon scattering above the gravitational floor falsifies the Leggett-channel DM identity outright. Canonical write-order steps 1-2 executed in-gate; step 3 (inventory row) → `mack-cosmic-bridge` at session close.

### 3. Downstream implications

| Stream | Effect of W1 | Action |
|:-------|:-------------|:-------|
| Capstone §7.1 LRD row | SF54 = wrong band (frame-robust); substrate mostly-accelerating post-fold | mack-cosmic-bridge re-scopes the §7.1 row at session close (capstone-hygiene Q2/Q3) |
| Capstone §8.5 / atlas-04 C10 | `d ln q/d ln H = 1` is a closure INPUT (H-parity); C10 Object-C STRUCTURALLY-CONDITIONAL | NO capstone-status change (corridor-map only, per plan decision table); conditionality + structural locus pinned in §W1-2 + verdict line |
| n_s falsifier row (§7) | NLO-precision-stable (PASS branch) | No §7 change (per plan decision table PASS branch) |
| Direct-detection falsifier surface | New zero-free-parameter NULL prediction + inverted falsifier; `sigma_DM_nucleon_FW`, `M_DM_Leggett_GeV` canonical | mack-cosmic-bridge lands the falsifier-master-inventory row at session close (write-order step 3) |
| C10 successor compute | Fixed-backbone corridor exhausted on both flanks (bare 3.42 / GD 2.06 / imposed 1.008) | CF-S101-W1-QEQ-SELFCONS (below) — the self-consistent back-reaction gate |

### 4. Wave classification

**Constraint-map-advancing + falsifier-sharpening.** W1 closed one corridor with its mechanism named (H-parity ⟹ fixed-backbone n=2 unreachable from equilibrium thermodynamics), frame-robustified one INFO into a genuine substrate prediction (LRD deceleration), and confirmed two zero-free-parameter observational anchors (n_s NLO stability; the σ_SI gravitational floor with inverted falsifier). No gate failed for numerical or process reasons; the FAIL is a structural boundary with its parity-theorem cause derived in-session.

### Effected In-Session (NON-MATH — team-lead orchestrator)

- [x] `sigma_over_m = 5.7e-51` promotion (allowlist-only → module level, S42 provenance) — effected in-gate by W1-4 via `update_constant`; orchestrator import-verified — `computations/_shared/canonical_constants.py` SECTION E — `206a745369914508`
- [x] `sigma_DM_nucleon_FW` + `M_DM_Leggett_GeV` PROVENANCE promotions (canonical write-order step 2) — effected in-gate by W1-4 via `update_constant`; orchestrator import-verified (values 1.2989252548383697e-63 / 4.128202383934713e17) — `computations/_shared/canonical_constants.py` SECTION E — `206a745369914508`
- [x] Housekeeping ledger §A rows A2/A3 recorded — `sessions/session-100a/session-100a-housekeeping.md §A` — anchor A2-A3
- [x] Capstone §7 surface items (W1-1 §7.1 LRD re-scope; W1-4 inventory row) consolidated into the session-close `mack-cosmic-bridge` sole-writer dispatch queue (executes this session before STOP; tracked as task #26 + housekeeping §A-on-completion) — `sessions/session-100a/session-100a-housekeeping.md` — per `feedback_mack-bridge-role.md`
- [x] Orchestrator-direct presentation patches: none required (all four sections landed complete; zero must_contain misses across 4 gates)

## Carry-Forward Computations

### CF-S101-W1-QEQ-SELFCONS — self-consistent back-reaction gate for the n=2 tracking slope

1. **What**: Re-derive `H(τ)` from the q-oscillation energy through the §6.3 closure (`H² = f(ρ_q, S_SA)`) and test whether `d ln q/d ln H → 1` emerges from q-domination self-consistency — the corpus-faithful Klinkhamer-Volovik mechanism (oscillation amplitude ∝ a^{−3/2} ∝ H on the self-consistent a ∝ t^{2/3} background), structurally unavailable on the fixed backbone this wave's gate pinned (per §W1-2 H-parity finding: equilibrium drives are H-even; slope-1 requires back-reaction, not a drive).
2. **Inputs**: `computations/session-100a/s100a_w1_qeq_drive.npz` (GD drive, slopes, k_curv, tail mask; audit `e31d45cf5309b32c`); `computations/session-99/s99_w1_q_nonratio_observable.npz` (backbone); `computations/session-99/s99_w2_relaxation_closure.npz` (K_CURV, q_boundary); canonical `a_0_FW_zeta`, `tau_fold`.
3. **Gate**: `S101-W1-QEQ-SELFCONS` — PASS iff `|slope_selfcons − 1| ≤ 0.05` on the full post-fold tail with `domain_used_frac ≥ 0.95`; FAIL closes the last dynamical route to unforced n=2 (the tracking law would then be irreducibly closure-conditional); INFO band (0.05, 0.5] per the W1-2 rubric form.
4. **Effort**: ~1 wave-equivalent (ODE + Friedmann-closure coupling; no new spectral compute).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-06 | SF54 deceleration-band comparison (S99 W1-1 successor) | INFO — band-miss, mapping-question OPEN (atlas-08 Q13 ADVANCED) | INFO — band-miss FRAME-ROBUST; SF54 = wrong band (different conformal frame, ~26× faster); substrate mostly-accelerating post-fold | S100a-W1-1 frame-map theorem + three-map ladder (`f41bdf1fc80562da`) |
| 2026-06-06 | n=2 tracking-vacuum law, `d ln q/d ln H = 1` leg (C10 Object-C) | OPEN — "substrate q_eq(H) drive" live successor channel | CLOSED-CONDITIONAL — H-parity theorem: no equilibrium-thermodynamic drive can be odd in H; slope-1 = fluid-closure INPUT on fixed backbone; C10 Object-C STRUCTURALLY-CONDITIONAL; self-consistency route remains (CF-S101-W1-QEQ-SELFCONS) | S100a-W1-2 FAIL (`e31d45cf5309b32c`) |
| 2026-06-06 | n_s = 0.9561 precision stability | LO-only (NLO never computed) | NLO-precision-stable: `Δn_s^{NLO} = −9.636e-4 < 0.003`, sign-robust, envelope-FI | S100a-W1-3 PASS (`05d2f2da0e43056e`) |
| 2026-06-06 | Leggett-channel DM direct-detection | No σ_SI prediction on the books | σ_SI = 1.299e-63 cm² (gravitational floor, zero free params); NULL predicted at all experiments; falsifier inverted (any confirmed scattering above floor kills Leggett-DM identity) | S100a-W1-4 PASS (`206a745369914508`) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Other | Size |
|:-----|:-------|:------------|:------------|:------|:-----|
| S100a-W1-1-SF54-MAPPING | `s100a_w1_sf54_mapping.py` | `s100a_w1_sf54_mapping.npz` | `s100a_w1_sf54_mapping.png` | — | 47.4 KB / 118.4 KB / 211.1 KB |
| S100a-W1-2-QEQ-DRIVE | `s100a_w1_qeq_drive.py` | `s100a_w1_qeq_drive.npz` | `s100a_w1_qeq_drive.png` | — | 33.6 KB / 74.6 KB / 265.1 KB |
| S100a-W1-3-NS-NLO | `s100a_w1_ns_nlo.py` | `s100a_w1_ns_nlo.npz` | `s100a_w1_ns_nlo.png` | — | 28.5 KB / 14.2 KB / 99.6 KB |
| S100a-W1-4-SIGMA-DM-NUCLEON | `s100a_w1_sigma_dm_nucleon.py` | `s100a_w1_sigma_dm_nucleon.npz` | `s100a_w1_sigma_dm_nucleon.png` | `s100a_lz2024_si_exclusion.csv` (815 B) + `_s100a_w14_wp_section_write.py` | 35.1 KB / 13.8 KB / 105.9 KB |

(All four gates emit to `computations/session-100a/s100a_gate_verdicts.txt` via the race-safe `emit_verdict` MCP tool; sig_5 SHA-uniqueness holds across all canonical lines.)
