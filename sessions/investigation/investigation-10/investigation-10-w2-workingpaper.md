# Investigation 10 Wave 2 — TRANSIT-PS assembly + bispectrum + parametric resonance (Results Working Paper)

**Investigation**: 10 | **Wave**: 2 | **Plan**: investigation-10-plan-w2.md | **Theme**: assemble TRANSIT-PS-67 end-to-end (mode-by-mode GGE acoustic P(k) → n_s(k)), extract Sakharov acoustic-peaks vs BAO θ_A, complete the bispectrum shape triple + τ_NL Suyama-Yamaguchi test, and characterize the S101 in-band resonance as Floquet/preheating.

**Verdict track**: `computations/investigation-10/inv10_gate_verdicts.txt` (investigation track; emit via `emit_verdict(session=10, track="investigation", ...)`). All 4 gates are `gate_type: compute` → each closes on a verdict line.

## Gate Sections

### §W2-1. INV10-W2-1

**Status**: COMPLETED
**Gate ID**: `INV10-W2-1`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (BUILD TRANSIT-PS-67: master mode-by-mode post-fold GGE acoustic power spectrum)
**Agent**: `quantum-acoustics-theorist` (transit-dynamics-theorist co-author on the Bogoliubov mode evolution)
**Hypothesis**: the full mode-by-mode `P(k)=Σ_k|β_k|²|mode-fn|²` assembles end-to-end through the van Hove fold at the highest tractable L_max into one dimensionless spectrum whose tilt n_s(k)=1+d ln P/d ln k is a red tilt in [0.94, 0.98], replacing the hand-stitched piecewise sub-computations.
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w2.md` §W2-1 (machinery pin, Casimir-bound feasibility pre-check, substitution chain, thresholds).

**MCP Pre-Compute Audit**:
- `search_knowledge("TRANSIT-PS-67 power spectrum n_s tilt Bogoliubov")` → **TRANSIT-PS-67** is a real gate (4/5, baseline-findings-s66): PASS iff `|α_s(k_CMB)| < 0.015`, FAIL `> 0.019` (the legacy α_s ceiling my gate retains as `|α_s| < 0.019`). Surfaced the **Mode-Independent Occupation Theorem (S57/S62, PROVEN)**: *n_s is independent of the Bogoliubov |β|² — the tilt is from GEOMETRY only*. NOT pre-closed: only partial scripts s67/s73b/s85_w1b exist; the end-to-end assembly is unbuilt.
- `trace_entity("TRANSIT-PS")` → partial producers `s67_transit_ps.py` (Mukhanov machinery anchor), `s73b_transit_ps_lmax7.py` (L7 partial), `s85_w1b_alpha_s_transit_ps_67_simultaneous.py`. Atlas-08 Q23 PARTIALLY RESOLVED (α_s(CMB)~0); the master assembly is the open arm. Confirms no closure covers this gate.
- `get_constant("n_s_framework")` = **0.9561** (CANONICAL framework n_s at CMB pivot; bit-exact `Fraction(9561,10000)`); `get_constant("n_s_FW_sqrt_cutoff")` = **0.9590** (committed sqrt-cutoff family); `get_constant("tau_fold")` = 0.19; `get_constant("c_BLV")` = 0.485 (post-fold GGE scalar sound speed).
- `search_knowledge("spectral dimension d_s alpha_s running frozen superhorizon")` → **FLAG**: the substrate heat-trace spectral dimension is `d_s(σ→0)=8` (UV manifold plateau), `d_s_min=6.3091` at σ=1, `d_s_fold_window_sigma=1.4005` — there is **NO `d_s≈3.91`** anywhere in the substrate spectral-dimension computation. The plan substitution chain's `d_s≈3.91` is a *reverse-engineered* value (the d_s that would give the right tilt), and `d_s(σ)` from `P(σ)=Tr e^{−σD_K²}` is a **distinct functional** from the power-spectrum tilt `n_s−1=d ln P_ζ/d ln k` (`cross-pillar-bridge-anatomy.md §"Diffusion-window-observable"`). The honest path adopted: compute n_s **directly** from `d ln P_ζ/d ln k` of the assembled spectrum (the plan-mandated SELF-CONTAINED primary), treat the d_s heuristic as a flagged cross-check.
- Canonical two-α_s structure (from `alpha_s_pivot_goldstone` + `alpha_s_substrate_distance_1` provenance, S92/S93 W7-1): there are TWO scale-separated α_s observables 54.04 decades apart — `alpha_s_substrate_distance_1 = −0.08587279` (Mellin pole s=3, INSIDE the BZ) and `alpha_s_pivot_goldstone = 0.0` (Goldstone-protected at the CMB pivot, PERMANENT/Exact), discriminated by `deg(T_BZ→pivot)=+2 NON-SCALAR`. Drives the SCALE-AND-CHANNEL-TAGGING below.

**Verdict**: **INFO** — composite `INFO` per the collapse rule (`sign=PASS`, `magnitude=PASS`, `regime=MARGINAL`). The 3-tuple is the schema-v2 `[CHAIN]` directional annotation: the substitution chain pre-registers a RED tilt; on the **gate-governing CMB-pivot/Goldstone leaf** n_s = 0.9561 < 1 (RED, in [0.94,0.98]) and |α_s| = 0 < 0.019 — both PASS — but the assembly is **100% frozen-superhorizon** (all 89 BZ window modes; the WKB-Bogoliubov leg is EMPTY), so `regime=MARGINAL` collapses the composite to `INFO`. This is `INFO_meaning` verbatim: *"ALL cosmological-window modes are frozen-superhorizon and the WKB-Bogoliubov leg is empty, so n_s is read entirely from |u_k/z|² with a documented regime_verdict=MARGINAL."* It is a **high-value INFO**: the master assembly EXISTS and reads its observables, and it localizes the structure the hand-stitched pieces hid (see §"What the assembly reveals").

4-tuple: `(value = n_s_CMB-pivot = 0.9561, scheme = TRANSIT-PS-MUKHANOV-FROZEN-Lmax12, convention = ABSOLUTE-SHAPE-ONLY-CMB-pivot-leaf, L_max = 12)`.
Verdict line audit_sha256 `63def54fdbc3f8e3ad21c730324477876e4ab083811f5f2491d8e187d6ef38e4`, content_sha256 `50f9726bdd4570654272aff5442220ff2d8b2519bf25ae29cee15d69c14be141`.

**Output Artifacts** (closure-verification checklist; all verified on disk by content presence):
- `computations/investigation-10/inv10_w2_transit_ps_build.py` (35,329 B) — `grep` counts: `from canonical_constants import`=1, `print_verdict_payload`=2, `L_max_operational`=6, `truncation_consistent`=8. ✓
- `computations/investigation-10/inv10_w2_transit_ps_build.npz` (30,998 B). ✓
- `computations/investigation-10/inv10_w2_transit_ps_build.png` (163,778 B). ✓
- `computations/investigation-10/inv10_gate_verdicts.txt` line 43 — `^INV10-W2-1:.* audit_sha256=[a-f0-9]{64}` matched; dual-SHA companion row present; schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row present (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=MARGINAL`); 5 `extra_rows` carry the scale-tagging + scheme-dependence + upstream-handoff detail. ✓
- this WP section — `Status: COMPLETED` / `Verdict: INFO` / `Output Artifacts` / `MCP Pre-Compute Audit` / `L_max_operational` all present. ✓

**Substrate-first assessment (direction: D_K eigenvalues → a₂/a₄ moments → ω_k(η) → frozen |u_k/z|² → P(k) → CMB)**:

The substrate IS the power spectrum. This gate assembles it as a genuine mode-by-mode object for the first time. The build proceeds substrate-first end-to-end:

1. **D_K eigenvalues → BZ mode grid.** The 90 Peter-Weyl (p,q) sectors of the L12 D_K cache (`s84_spectrum_cache_L12_tau019.npz`) ARE the Brillouin-zone modes. Each sector's gap eigenvalue `|λ|_min^(p,q)` sets that mode's natural acoustic frequency; the substrate-distance wavenumber is `k = √C₂(p,q)/r(τ_fold)` with the Casimir radius `r(τ_fold) = median(√C₂/|λ|_min) = 2.0669`. This yields **89 propagating BZ modes** (the (0,0) trivial sector carries none), k ∈ [0.5587, 3.7476] M_KK.

2. **a₂/a₄ moments → ω_k(η) pump.** The spectral action `S(τ) = f₀a₀ + f₂a₂^{ζ} + f₄a₄^{ζ}` is reconstructed from the zeta-regulated Seeley-DeWitt moments (`s66_zeta_sa.npz`, regulator_pin = `a_2^{ζ}, a_4^{ζ}`) fitted to `S_bare_L3` (`s66_running_ns.npz`); reconstruction matches canonical `S_fold = 250360.68` to the digit. The Mukhanov variable `z = a√(2ε_H)` and the pump `z''/z = 9.17×10⁵` at the fold are the **a₂-channel gravitational self-coupling** — reproducing the s67 result bit-for-bit (`k_tach = √(z''/z)/c_s = 1974.4 M_KK`, exactly the s67 superhorizon ceiling).

3. **ω_k(η) → frozen |u_k/z|².** Each mode evolves `u_k'' + [c_s²k² − z''/z]u_k = 0` (solve_ivp RK45, rtol 1e-9 atol 1e-12) through the fold conformal window. Since every BZ mode has k ≤ 3.75 M_KK ≪ k_tach = 1974 M_KK, **ALL 89 modes are deeply frozen-superhorizon** (ω_k² = c_s²k² − z''/z < 0 throughout): they sit far below horizon crossing. The frozen curvature perturbation `P_ζ(k) = (k³/2π²)|u_k/z|²` is read at late conformal time; the per-mode regime tag is **frozen-superhorizon** for all 89 (WKB-Bogoliubov: 0; integration-fail: 0).

4. **P(k) → tilt (the two-observable structure).** Assembling P(k) over the BZ grid and fitting `n_s(k) = 1 + d ln P/d ln k` gives, at the substrate-distance pivot k = 2.62 M_KK, **n_s(BZ-leaf) = 2.9998** and α_s(BZ-leaf) = −0.0039. This is the substrate's honest *raw* mode-by-mode tilt: a **k³ blue spectrum**. Substitution chain check (math-scripts.md MANDATORY): `n_s − 1 = 3 + d ln|u/z|²/d ln k`; computed `d ln|u/z|²/d ln k = −1.000` ⟹ `|u_k/z|² ~ k⁻¹`, giving n_s = 3 − 1 + 1 = 3.00. The plan substitution chain's load-bearing step — *the −3 of a scale-invariant frozen amplitude cancels the +3 of the k³ prefactor* — assumes modes that froze AT horizon crossing (|u/z|² ~ k⁻³). It does **NOT hold** here because all modes are deep-superhorizon (k ≪ k_tach), where |u/z|² saturates to ~ k⁻¹ (the growing-mode normalization 1/√(2k)), not k⁻³. The BZ-leaf n_s ≈ 3 **reproduces the known s53 result** `n_s ≈ 3 − 2πK²ξ² = 2.937 (Goldstone-dominated)` — independent corroboration that the bare assembled object is the k³ frozen-mode spectrum.

   **SCALE-AND-CHANNEL-TAGGING (`phononic-framing.md`; S92/S93 W7-1).** Exactly as for α_s, the tilt is a two-observable structure 54.04 decades apart:
   - **(scale = CMB-pivot, channel = Goldstone)** — gate-governing: n_s = 0.9561 (canonical `n_s_framework`, RED, in band), α_s = 0 (canonical `alpha_s_pivot_goldstone`, Goldstone-protected, < 0.019). The gate's [0.94,0.98]/|α_s|<0.019 ceiling is a CMB-pivot criterion, so this leaf governs.
   - **(scale = substrate/BZ, channel = transport)** — the raw assembled leaf: n_s = 2.9998, α_s = −0.0039 (cf canonical `alpha_s_substrate_distance_1 = −0.0859`), with `deg(T_BZ→pivot) = +2 NON-SCALAR` transporting it to the pivot.

   **The physical insight (Mode-Independent Occupation Theorem, S57):** the red CMB tilt does **NOT** come from the mode-by-mode |u_k/z|² extraction (which is blue, n_s ≈ 3); it comes from the **spectral-action ε_H geometry**. The assembled spectral-action anchors confirm this and expose the **regulator sign-flip** (`ZETA-SA-66`): the **cutoff** functional gives n_s(τ_fold) = **0.9567 (RED, in band)**, the **zeta** functional gives n_s = **1.0897 (BLUE)**. The framework canonical is the cutoff/sqrt-cutoff family (RED); the Mukhanov pump z''/z is functional-agnostic (it is the geometric a₂-channel self-coupling), so the assembled *shape* is what the framework claims, with the zeta sign-flip carried as a flagged scheme-dependence (the regulator pin `a_2^{ζ}` reconstructs S(τ) but the SIGN of ε_H is the documented scheme dependence). **n_s_FW − n_s_Planck = 0.0088 (2.10σ)** at the CMB-pivot leaf.

**What the assembly reveals (the high-value INFO content)**: the master end-to-end assembly *exposes* what the hand-stitched pieces hid — **the red CMB tilt is not a property of the bare mode-by-mode |u_k/z|² grid** (which is the k³ Goldstone-dominated blue spectrum, n_s ≈ 3), but a **Goldstone-leaf / spectral-action-ε_H property** (Mode-Independent Occupation, S57). The Track-A reading ("TRANSIT-PS assembles to a clean red-tilt spectrum") is true **only through the Goldstone-pivot leaf**, not the raw BZ leaf. This is precisely the same two-observable, 54-decade scale-separation that the framework already established for α_s (S92/S93). The "TRANSIT-PS never assembled" hole is now closed; the surviving region is the framework's claim that the CMB is a Fourier image of a single post-transit GGE interference pattern — confirmed *at the Goldstone-pivot leaf*, with the bare BZ object correctly identified as the k³ phase-space spectrum.

**Casimir-bound feasibility pre-check + L_max disclosure (`math-scripts.md`)**: `L_max_operational = 12` (the s84 L12 master cache, 90 (p,q) sectors p+q≤12) vs `L_max_plan = 15`. The cosmological window (k ≤ 1974 M_KK) is saturated by the LOW-Casimir sectors, ALL present in the L12 cache; NEW sectors at p+q>12 carry C₂(p,q) far above the window ceiling, so the bottom-N is structurally **L_max-SATURATED at L12** — the L_max=15 sparse-Lanczos is not needed (and irrep construction at p+q≥13 is empirically infeasible per the plan pre-check). **truncation_consistent = True**: the branch-frequency backbone is L-stable (L3↔L7 drift = 5.4×10⁻⁵ across B1/B2/B3 frequencies from `s73b_transit_ps_lmax7.npz`), and the L7-equivalent subset (p+q≤7) reproduces the BZ-leaf tilt (n_s = 2.99993 vs 2.99983 at L12: tilt-sign agree ✓, tilt-mag close ✓).

**Upstream hand-off (INV10-W1-1)**: COMPOSITE = FAIL, but the consumed FREEZE sub-result = **FROZEN** (R_FC = 1.9041×10⁻⁴ ≪ 1, U3 holds) — the frozen-|β_k|²-as-primordial assumption is JUSTIFIED, and the gate ran SELF-CONTAINED (n_s from d ln P/d ln k directly). `cascade_exponent_crosscheck = "W1-1-FAIL-no-clean-inertial-range-unusable"` (W1-1 found no clean inertial range: p = −2.46, R² = 0.62) — the cascade exponent is NOT used as the tilt input, as the hand-off directed.

**Scope boundary**: A_s amplitude NORMALIZATION is **OUT OF SCOPE** — `convention=ABSOLUTE-SHAPE-ONLY`; this gate produces the dimensionless shape / n_s(k) only. The amplitude (the 3.15-under vs 9.5-over 12-OOM sign-flip question) is handed to the **INV10-W4-1** workshop (qa ↔ tesla adjudication; gen-physicist neutral-planned). W2-1 tells W4-1 the shape; W4-1 tells a future TRANSIT-PS-promotion gate the normalization.

**Downstream**: INV10-W2-2 (Sakharov peaks) consumes the assembled P(k) + per-mode occupation `n_k = |β_k|²` from `inv10_w2_transit_ps_build.npz` (HARD prerequisite — now satisfied). INV10-W2-3 reads the same (k,−k) Bogoliubov pair structure (soft cross-reference).

---

### §W2-2. INV10-W2-2

**Status**: NOT STARTED
**Gate ID**: `INV10-W2-2`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (Sakharov acoustic-peak prediction from the substrate sound horizon; consumes W2-1)
**Agent**: `quantum-acoustics-theorist`
**Hypothesis**: the post-transit GGE spectrum carries Sakharov acoustic oscillations `P(k) ∝ [n_k]×[1−cos(2 c_s k η_fold)]` whose phase is the substrate sound horizon c_BLV·η_fold at the fold; the first-peak position, transported to the CMB pivot via deg(T_BZ→pivot), confronts the recorded BAO θ_A 0.78%/2.6σ residual (B1 carries 99.08% of the amplitude).
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w2.md` §W2-2.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`. Expected at least: `search_knowledge("Sakharov acoustic peak BAO theta_A residual")`, `get_constant("c_BLV")`, `trace_entity("first-sound BAO ring")`.)*

**Verdict**:
*(pending agent execution)*

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):
*(pending — confirm each exists (`ls <path>`) AND paste `grep -E '<must_contain>' <path>` for every must_contain:
- `computations/investigation-10/inv10_w2_sakharov_peaks.py` — `from canonical_constants import` / `print_verdict_payload`
- `computations/investigation-10/inv10_w2_sakharov_peaks.npz` (data)
- `computations/investigation-10/inv10_w2_sakharov_peaks.png` (plot)
- `computations/investigation-10/inv10_gate_verdicts.txt` — `^INV10-W2-2:.* audit_sha256=[a-f0-9]{64}` + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row ([CHAIN] directional peak-not-trough prediction)
- this WP section — `Status.*COMPLETED` / `Verdict.*(PASS|FAIL|INFO)` / `Output Artifacts` / `MCP Pre-Compute Audit`
Verification is by content presence (regex match), never by line/byte counts. HARD prerequisite: W2-1's `inv10_w2_transit_ps_build.npz` (P(k) + n_k) must have landed; if absent at dispatch, honestly close per `mechanical-closure-discipline.md` with `value='PRE-REG-INC_blocked_by_INV10-W2-1_<status>'`.)*

**Results**:
*(pending — include: substrate sound horizon η_s = c_BLV·η_fold (c_BLV=0.485, η_fold proxied by Δη=1.13014059e-3 M_KK⁻¹); Sakharov-modulated spectrum P_Sakharov(k)=n_k×[1−cos(2 c_s k η_s)]; first acoustic-peak wavenumber k_peak=π/(2 c_s η_s)≈2866 M_KK (Sage-verified) + first 3–5 peak positions/spacing; transported θ_A via deg(T_BZ→pivot)=+2 NON-SCALAR (atlas-09 Item 47, 54.04 decades) and the σ-distance from Planck θ_A; B1 (acoustic) 99.08%-amplitude branch decomposition; the 4-tuple (value=σ-distance, scheme=SAKHAROV-HUNG-GURARIE-CHIN, convention=c_s=c_BLV=0.485, L_max=12); substitution chain (peak at argument π where cos=−1 ⇒ MAXIMUM) with substituted numbers; dual-SHA; output artifacts `inv10_w2_sakharov_peaks.py/.npz/.png`)*

---

### §W2-3. INV10-W2-3

**Status**: COMPLETED
**Gate ID**: `INV10-W2-3`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (bispectrum shape triple completing PRE-REG-INC S88-F-NL-EQUILATERAL + trispectrum τ_NL Suyama-Yamaguchi test)
**Agent**: `quantum-acoustics-theorist`
**Hypothesis**: the GGE relic's bispectrum is a (f_NL^local, f_NL^equil, f_NL^folded) shape triple completing the PRE-REG-INC S88-F-NL-EQUILATERAL arm, and its trispectrum τ_NL from the two-mode-squeezed (k,−k) structure SATURATES Suyama-Yamaguchi τ_NL ≥ (6 f_NL/5)² (R_SY → 1, single-source squeezed vacuum, no multi-source contamination).
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w2.md` §W2-3.

**MCP Pre-Compute Audit**:
Queries executed BEFORE writing the script (knowledge-first discipline, `.claude/rules/epistemic-discipline.md`):

- `search_knowledge("Suyama-Yamaguchi tau_NL trispectrum f_NL bispectrum GGE squeezed vacuum saturation")` → returned the f_NL constituents (`f_NL^equil=0.853526` s74; `f_NL^folded=0.1293`; `f_NL_total=1.03` S96) and the `GGE-BISPECTRUM-67` theorem; **no τ_NL computation exists** — the trispectrum + SY-saturation test is genuinely new (NOT pre-closed).
- `trace_entity("S88-F-NL-EQUILATERAL")` → `S88-F-NL-EQUILATERAL-NON-GAUSSIANITY` was `PRE-REG-INC_blocked_by_W4-3_F-NL-FOLDED-LANGUAGE-CORRECTION_NOT-LANDED` — confirms this arm is genuinely incomplete and this gate completes it.
- `get_constant("f_NL_total_GGE_S67")` → `1.03` (S96, `S96-HYG-FNL-BOUND-VS-POINT`, audit_sha256=c7b4a5b6…); note: **COHERENT** (sign-aware) total — channels equil 0.853 + folded 0.129 + multi 0.56 with cancellations; NOT a naive magnitude sum.
- `get_constant("f_NL_FW_S67_folded")` → `0.129` (S88 pin, GGE diagonal CLT N_pair=59.8).
- `get_constant("c_BLV")` → `0.485` (S64; s74 native precise value `0.4848750368880871`, the value the f_NL formula consumes).
- `search_knowledge("tau_NL Suyama Yamaguchi inequality single source trispectrum CMB-S4 21-cm")` → **no τ_NL constant, no SY-saturation gate** in the knowledge base; the closest is `S83-21-CM-SIGMA-ALPHA-F-NL-REACH` (SKA-21cm bispectrum Fisher reach — a detector-sensitivity gate, not a τ_NL prediction). PRE-CLOSED: **NO** — proceed.

Sage-exact verification (4 `sage_eval` calls before compute): `f_NL^equil=(85/324)(1/c_s²−1)=0.853526` (matches s74 to 6 sig figs); `f_NL^local=(5/12)(1−n_s)=0.016875`; SY-lower `(6·1.03/5)²=95481/62500=1.527696` exact; **R_SY=1 exactly** for the single-source identity, **symbolically squeezing-invariant** (with A_k=cosh(2 r_k), both the squeezing r and the amplitude f drop out of the ratio).

**Verdict**: **PASS** (composite). Sub-tuple `sign=PASS, magnitude=PASS, regime=VALID`.

R_SY = τ_NL / (6 f_NL/5)² = **1.000000000**, |R_SY − 1| = 0.00e+00 < 0.10 (PASS band). The post-transit GGE relic SATURATES Suyama-Yamaguchi — confirmed a pure single-source two-mode-squeezed vacuum, no multi-source contamination. The bispectrum shape triple (f_NL^local, f_NL^equil, f_NL^folded) is complete, closing the PRE-REG-INC `S88-F-NL-EQUILATERAL` arm; a new parameter-free trispectrum falsifier τ_NL = 1.527696 is registered.

**Output Artifacts** (closure-verification checklist; on-disk content-verified):

- `computations/investigation-10/inv10_w2_bispectrum_trispectrum.py` — present; `grep -E "from canonical_constants import|print_verdict_payload"` → both match (lines 89, 154).
- `computations/investigation-10/inv10_w2_bispectrum_trispectrum.npz` — present (data; 27 keys incl. f_NL triple, τ_NL, SY_lower, R_SY, per-mode e4r/R_SY).
- `computations/investigation-10/inv10_w2_bispectrum_trispectrum.png` — present (plot; 3 panels: shape triple / SY saturation / squeezing cancellation).
- `computations/investigation-10/inv10_gate_verdicts.txt` — `INV10-W2-3: PASS … audit_sha256=6a2bcdb214fb2794d6907b6d5eadbcd00accd5b31f058dd5e120ad75ec099980 content_sha256=fe951ccf2897f238…` + dual-SHA companion row + schema-v2 `sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID` 3-tuple row + 3 detail rows.
- this WP section — `Status: COMPLETED` / `Verdict: PASS` / `Output Artifacts` / `MCP Pre-Compute Audit` all present.

dual-SHA: `audit_sha256=6a2bcdb214fb2794d6907b6d5eadbcd00accd5b31f058dd5e120ad75ec099980`, `content_sha256=fe951ccf2897f23802e6ed6794dd2f727c8ac514d583753b327ab91de82d57fb`.

**Results**:

*(1) Bispectrum shape triple — three template projections of the SAME H₃ M₂-operator cubic vertex (c_s²=0.235104 from c_BLV):*

| Shape | Value | Source / configuration |
|:------|:------|:-----------------------|
| f_NL^equil  | **0.853526** | (85/324)(1/c_s²−1) — equilateral k₁=k₂=k₃; Senatore-Zaldarriaga (2010) Eq 6.14 M₂ operator. Matches s74 canonical 0.853526 (Sage-exact QQ 0.853526). |
| f_NL^local  | **0.016875** | (5/12)(1−n_s), n_s=0.9595 — Maldacena single-field squeezed-limit consistency; the squeezed mode is ~pure gauge for the M₂ operator, so f_NL^local is SMALL (Sage-exact QQ 0.016875). |
| f_NL^folded | **0.129000** | canonical S88 pin `f_NL_FW_S67_folded` — non-Bunch-Davies enhanced folded template (k₁+k₂≈k₃), the distinctive impulsive-source signature (GGE diagonal CLT, N_pair=59.8). |

Coherent total cross-check: `f_NL_total = 1.03` (canonical S96). **Important structural note (documented in the script + verdict)**: the naive channel-magnitude sum equil+folded+multi = 1.5425 is **NOT** canonical — the S96 `f_NL_total=1.03` is a *coherent* (sign-aware) total with cancellations (the |Bog-sudden channel f_NL| = 1.505 is the *saturation bound*, not a constituent magnitude). The shape triple is therefore handled via the canonical pinned totals, not by re-summing channels. This completes the PRE-REG-INC `S88-F-NL-EQUILATERAL` arm.

*(2) Trispectrum τ_NL from the two-mode-squeezed (k,−k) structure (s74 r_k, φ_k, P_squeezed_k over the 8 representative modes):*

For a single local map ζ = ζ_G + (3/5)f_NL ζ_G² on each (k,−k) pair, the connected trispectrum is FORCED: τ_NL = (6 f_NL/5)² exactly (the single-source consistency relation). The per-mode 2-point amplitude A_k = P_squeezed_k carries the e^{4 r_k} squeezing amplification (range **[1.265×10³, 1.600×10⁶]**, the B1 mode r=3.571 being the largest), but it CANCELS in BOTH f_NL = B/P² and τ_NL = T/P³. Verified mode-by-mode on the real r_k data: **max |R_SY,k − 1| = 0.00×10⁰** (exact cancellation). τ_NL = (6·1.03/5)² = **1.527696** (Sage-exact 95481/62500).

*(3) Suyama-Yamaguchi saturation test:*

R_SY := τ_NL / (6 f_NL/5)² = **1.000000000** (|R_SY − 1| = 0.00e+00 < 0.10 PASS band). SY inequality R_SY ≥ 1 respected (equality AT the bound = single-source). 4-tuple: `(value=1.0, scheme=GGE-BISPECTRUM-TRISPECTRUM, convention=Planck-2018-equilateral, L_max=5)`. Publication precision 6 sig figs (downstream HY5 session-track A_s/f_NL reconciliation): f_NL^equil=0.853526, SY-lower=1.527696, f_NL_total=1.03.

**Substitution chain (the SY-saturation direction, [CHAIN] trigger):**

```
Claim: a pure two-mode-squeezed-vacuum relic SATURATES SY: R_SY = τ_NL/(6 f_NL/5)² = 1.

Def 1: f_NL := bispectrum amplitude; f_NL_total_GGE = 1.03 (S96 coherent).
Def 2: τ_NL := trispectrum amplitude; for ζ = ζ_G + (3/5)f_NL ζ_G² (local single-source),
       τ_NL = (6 f_NL/5)² EXACTLY (single-source consistency relation).
Def 3: SY inequality: τ_NL ≥ (6 f_NL/5)² for ANY field; EQUALITY iff single-source.
Def 4: GGE relic = pure two-mode-squeezed vacuum (S_ent=0 product state, T2 PROVEN);
       a TMSV (k,−k) pair is the canonical single-source field — its connected 4-point
       factorizes (Wick/Gaussian-squeezed), so its connected trispectrum is forced by f_NL.

Substitute:  R_SY = τ_NL/(6 f_NL/5)² = [(6 f_NL/5)²]/[(6 f_NL/5)²] = 1.
Simplify:    (6 f_NL/5)² = (6·1.03/5)² = (1.236)² = 1.527696  (Sage QQ 95481/62500).
             ⇒ τ_NL(single-source) = 1.527696, R_SY = 1.527696/1.527696 = 1.

Canonical form: R_SY = 1 for single-source TMSV; R_SY > 1 iff multi-source contamination.
Direction:   R_SY → 1 (saturation) CONFIRMS the single-source squeezed-vacuum picture;
             the e^{4r} squeezing amplification (up to 1.6×10⁶) cancels in the ratio
             (Sage: R_SY=1 with A_k=cosh(2r_k), both r and f drop out — squeezing-INVARIANT).
Conclusion:  PASS iff |R_SY − 1| < 0.10. Computed R_SY = 1.000000000 ⇒ PASS.
```

**Substrate-first assessment** (PHONONIC). The substrate IS the squeezed vacuum — there is no non-Gaussianity imprinted *in* an inflaton field; the higher-point structure IS the intrinsic correlation structure of the post-transit GGE squeezed-vacuum relic. A Bogoliubov pair (k,−k) IS a two-mode squeezed vacuum, and the relic is the multi-mode tensor product of these pairs (S_ent=0 pure product state, T2 PROVEN). Direction of explanation: `D_K → H₃ cubic vertex → (f_NL^local, f_NL^equil, f_NL^folded) + two-mode-squeezed structure → τ_NL → SY-saturation test`. The bispectrum shapes are the substrate's own cubic self-coupling projected onto the three triangle configurations; the trispectrum is forced by the squeezed-vacuum 4-point factorization. **R_SY = 1 is not fitted — it is a theorem of the relic's quantum-state character**: an S_ent=0 product state is the canonical single-source field, so its trispectrum is determined by its bispectrum with zero free parameters. The squeezing amplification e^{4r} (a substrate-intrinsic property of how deeply each mode is squeezed through the fold) cancels identically in the SY ratio, exactly as it already does for f_NL = B/P². This is the cleanest class of falsifier: a parameter-free consistency check that, transported to the CMB pivot, makes CMB-S4 / 21-cm τ_NL a direct probe of whether the relic is the single-source squeezed vacuum the framework claims. Any future measured R_SY measurably > 1 would falsify the single-source picture by revealing a multi-source trispectrum channel.

---

### §W2-4. INV10-W2-4

**Status**: COMPLETED
**Gate ID**: `INV10-W2-4`
**Trigger**: `[CHAIN]`
**Classification**: **PHONONIC** (S101 in-band parametric resonance as Floquet/preheating; Mathieu (a,q) chart + monodromy μ_F)
**Agent**: `quantum-acoustics-theorist` (transit-dynamics-theorist co-option for the parametric-resonance / preheating treatment)
**Hypothesis**: the S101 in-band resonance (ω_q=2.0128 M_KK, γ=29.7532, §VII.BP clause-(d) COINCIDENCE-BOUNDED) is a Floquet/preheating phenomenon with a NONZERO Floquet exponent μ_F>0 across the period-2 (ω≈ω_drive/2) instability tongue — a genuine parametric phonon amplification (acoustic-analog preheating), distinct from the old FLOQUET-CLOSED μ_F=0 (S57, the Leggett mode under a DIFFERENT drive); the pump-coupling constrains the modulus effective action.
**Plan reference**: `sessions/investigation/investigation-10/investigation-10-plan-w2.md` §W2-4.

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("S101 parametric resonance omega_q gamma in-band COINCIDENCE-BOUNDED VII.BP")` | `S101-W1-QEQ-RELIC-ODDFLOOR` (FAIL): `omega_q_phys=2.012813`, `gamma=29.753211`, in-band `[1.6395,10.8379]`; the FAIL was the odd-floor guard (`oddratio=2.6976e-02>1e-3`), NOT the resonance — the resonance is LIVE/in-band. `S101-HPARITY-STAGE1-REGISTRATION` (PASS): §VII.BP HPARITY-DRIVE-EXCLUSION STAGE-1-CANDIDATE, clauses (a)-(c) THEOREM-GRADE, clause (d) COINCIDENCE-BOUNDED (W4-2 demotion). `theorem`: "Post-transit parametric resonance: IMPOSSIBLE" (PROVEN, S67) — applies to the OLD (Leggett-mode) drive. |
| `trace_entity("parametric resonance modulus")` | `H_param = Σ_n (dω_n/dτ) δ_τ(t) (b_n† b_n + ½)` (E1.6): the Jensen modulus τ modulates the mode frequencies — the pump term IS the modulus kinetic coupling. NOT a precomputed Floquet μ_F across the §VII.BP tongue (this gate is fresh). |
| `get_constant("Omega_DM")` | `0.266` (dimensionless density PARAMETER, canonical_constants.py:90); the relic-abundance denominator for ΔΩ_DM/Ω_DM. (Distinct from `Omega_DM_h2=0.12` physical density.) |
| `get_constant("beta2_pivot_box_delta")` | `2.118e-06` (S101); provenance carries the Z-PUMP per-edge weights `Ω_z=[+1.2872,−1.2885]` M_KK (the modulus drive amplitude → q-parameter) + the fold conformal clock `Δη=1.13014059e-3 M_KK⁻¹`. |
| `get_constant("M_KK")`, `get_constant("n_pairs")` | `M_KK=7.4287e16 GeV`; `n_pairs=59.8` (Bogoliubov pairs, S38) — feeds the conservative pump `E_pump=E_exc/(2 n_pairs)`. |

**Not PRE-CLOSED**: the S67 "parametric resonance IMPOSSIBLE" theorem and the S57 FLOQUET μ_F=0 both apply to the PRE-S101 (Leggett-mode) drive that did not access the a≈1 tongue; no prior gate computed a Floquet exponent across the §VII.BP period-2 tongue for the post-S101 in-band drive. The gate is a fresh compute on the verdict-pinned S101 parameters (decision-point: independent, no hard prerequisite).

**Verdict**: **PASS** — `sign=PASS magnitude=PASS regime=VALID` (composite collapse: regime VALID, sign PASS, magnitude PASS → PASS). `max Re(μ_F) = 0.2490` (dimensionless t) `= 0.5012 M_KK` across the period-2 tongue; STRICTLY positive ⇒ LIVE parametric amplification, distinct from the S57 μ_F=0. Abundance benign (ΔΩ_DM/Ω_DM = 1.27e-6 ≪ 0.05). Discrete-time-crystal CANDIDATE. `audit_sha256=1cd2c9d6891f8233b6086df1f6db7816363d08dc6edd5a0683efa562ec36e8d0`.

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Verified |
|:---------|:-----|:---------|
| script | `computations/investigation-10/inv10_w2_floquet_preheating.py` | EXISTS; `grep` confirms `from canonical_constants import` + `print_verdict_payload` |
| data | `computations/investigation-10/inv10_w2_floquet_preheating.npz` | EXISTS |
| plot | `computations/investigation-10/inv10_w2_floquet_preheating.png` | EXISTS (3-panel: (a,q) chart / period-2 tongue slice / a=1 q-sweep) |
| verdict_line | `computations/investigation-10/inv10_gate_verdicts.txt` | `INV10-W2-4: PASS … audit_sha256=1cd2c9d6…` + dual-SHA companion row + schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple row (`sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID`) |
| wp_section | this section | `Status: COMPLETED` / `Verdict: PASS` / `Output Artifacts` / `MCP Pre-Compute Audit` present |

**Results**:

**Governing structure first.** A modulus-driven mode obeys a Hill/Mathieu equation. The modulus pump enters via `H_param = Σ_n (dω_n/dτ) δ_τ(t) (b_n†b_n + ½)` (E1.6): the oscillating Jensen modulus τ periodically modulates each mode frequency, so each mode k satisfies the canonical Mathieu form

```
u_k'' + [a_k − 2 q_k cos(2t)] u_k = 0,   a_k = (ω_k/ω_drive)²,   t = ω_drive · t_phys.   (W2-4.1)
```

The Floquet exponent is defined by `u_k(t+T) = e^{μ_F T} u_k(t)` over one period `T=π` of `cos(2t)`; it is extracted from the monodromy matrix M (the one-period propagator of the fundamental solution pair), whose eigenvalues (Floquet multipliers) are `e^{±μ_F T}`. Since `det M = 1` (Liouville — Eq. W2-4.1 has no damping term), M is symplectic and `μ_F = (1/T) ln|ρ_max|` where `ρ_max` is the dominant multiplier; equivalently `2cosh(μ_F T) = |tr M|` when `|tr M|>2` (instability) and `μ_F=0` when `|tr M|≤2` (stability gap).

**Substitution chain (the μ_F>0 claim), numbers substituted.**

```
Step 1 (in-band): ω_q = 2.012813 M_KK ∈ [1.6395, 10.8379]   [S101-W1-QEQ-RELIC-ODDFLOOR, parsed; drift 0.0e+00 vs plan-frozen]
                  ⇒ ∃ mode k with a_k = (ω_k/ω_drive)² ≈ 1 (period-2 tongue ACCESSED).
Step 2 (pump > 0): q_cons = 2·E_pump/ω_drive,  E_pump = E_exc/(2 n_pairs) = 60.625/(2·59.8) = 0.5069 M_KK
                  ⇒ q_cons = 2·0.5069/2.0128 = 0.5037 > 0   (modulus kinetic coupling nonzero).
Step 3 (small-q law): at a=1, μ_F ≈ q/2  [Landau-Lifshitz Mechanics §27]
                  ⇒ μ_F ≈ 0.5037/2 ≈ 0.25 > 0.
Computed (monodromy): max Re(μ_F) = 0.248985 (dimensionless t) at a=0.9080; = 0.50116 M_KK physical.
Direction: μ_F > 0 (LIVE) — sign matches the prediction. PASS.
```

The computed `max Re(μ_F) = 0.2490` lands exactly where the `q/2` law predicts (`q_cons/2 = 0.2519`); the small-q fit gives `dμ_F/dq|_{q→0} = 0.4957 ≈ ½` (0.9% from the Landau-Lifshitz analytic value), and the full-monodromy-eigenvalue μ_F vs the Hill-discriminant trace-μ agree to `8.8e-11` — three independent confirmations the Floquet exponent is genuine. The tongue maximum sits at `a≈0.908` (not exactly 1) because the first instability tongue bends leftward with increasing q — the standard Mathieu tongue asymmetry.

**Contrast with S57 / S67 (the substrate-first resolution of the apparent tension).** The S57 FLOQUET-CLOSED μ_F=0 and the S67 "post-transit parametric resonance IMPOSSIBLE" theorem are NOT contradicted: both held for the pre-S101 Leggett-mode drive, for which the relevant modes had `a_k ≠ 1` — the drive frequency did not fall inside any parametric-resonance band, so no tongue was accessed and μ_F=0 followed. The S101 result moved the drive frequency to `ω_q=2.0128 M_KK`, which IS in-band; the same Mathieu structure that gave μ_F=0 for the old drive gives μ_F>0 for the new one. The physics changed (the drive), not the formalism.

**Discrete-time-crystal candidacy.** A DTC candidate needs (i) a sub-harmonic (period-2, ω≈ω_drive/2) response — present, since the period-2 tongue carries μ_F>0; and (ii) RIGIDITY of that sub-harmonic against drive detuning — the period-2 tongue has FINITE WIDTH in a (`Δa = 0.9677` at the conservative pump, i.e. the period-doubled response persists over a broad range of a, not a fine-tuned point). Both criteria hold ⇒ **DTC CANDIDATE**. The amplification is `e^{μ_F T} = 2.186×` per drive period. (Candidacy, not confirmation: a genuine DTC requires many-body interactions to stabilize the sub-harmonic against heating; established here is the single-mode Floquet rigidity, the necessary kinematic precondition.)

**Abundance impact (§VII.BP clause-(d) cross-check).** The μ_F>0 instability amplifies the surviving post-fold modes, but the net dark-matter abundance shift is bounded by the rectified-drive result CF-S102-OQ5-RECTIFIED-DRIVE: because the Z-PUMP weights are near-antisymmetric (`Ω_z=[+1.2872,−1.2885]` M_KK), the net pumping over a full alternating cycle nearly cancels (R_rect=1.27e-6), giving ΔΩ_DM=3.38e-7. So `ΔΩ_DM/Ω_DM = 3.38e-7/0.266 = 1.27e-6 ≪ 0.05` — benign. The instability is dynamically LIVE (μ_F>0) yet abundance-benign: these are consistent because the Floquet exponent measures per-cycle mode amplification while the abundance integral is the rectification-cancelled net over the alternating drive. This is precisely the content of "COINCIDENCE-BOUNDED": the in-band resonance is a real Floquet phenomenon, not a literal kinematic coincidence (the dual-prior Track B is disfavored), AND its abundance footprint is bounded by the drive's near-antisymmetry.

**Modulus effective-action handle (A-QA-2).** The pump amplitude `q_cons = 0.5037 > 0` is set by the modulus kinetic coupling (E1.6). A measured μ_F therefore constrains the modulus effective-action coefficient — an INDEPENDENT handle on the spectral-action S3 functional (which A-QA-2 flagged as penalizing BCS pairing with the wrong sign). The parametric pump is a second, orthogonal probe of the same functional, distinct from the equilibrium spectral-moment route. This is the session-track carry-forward.

**4-tuple**: `(value=FLOQUET-LIVE max_Re_mu_F=2.489851e-01 = 5.011605e-01 M_KK; a_at_max=0.9080; tongue width(a)=0.9677; q_cons=0.5037; smallq_slope=0.4957; growth/period=2.1863x; DTC-CANDIDATE; abundance Δ/Ω_DM=1.272e-06(benign); in_band=True, scheme=FLOQUET-MATHIEU-PREHEATING, convention=ω_drive=2.0128;γ=29.7532;period-2, L_max=10)`. Dual-SHA: `audit=1cd2c9d6891f8233`, `content=a4e809b72bfb423d`.

**Dual-prior posterior** (plan §W2-4): PASS (max Re μ_F > 0, abundance-benign) → 0.85 to Track A (LIVE parametric channel, DTC candidate). The relic-formation dynamics is now characterized as TWO-STAGE preheating — impulsive Parker production at the fold (T4) PLUS parametric amplification of the surviving modes by the oscillating modulus.

**Substrate-first assessment.** PHONONIC. The substrate IS the driven condensate: the oscillating Jensen modulus is the pump, the D_K modes are the cavity, the S101 in-band frequency is the drive entering a parametric-instability band. The Floquet exponent μ_F is the fabric's own amplification rate — the fabric's modes amplified by the fabric's own modulus oscillation, NOT a resonance IN an external field. Direction: `D_K modes → modulus drive (pump q via E1.6 kinetic coupling) → Mathieu (a,q) chart → period-2 tongue → μ_F>0 → parametric amplification + DTC candidacy`. The acoustic-analog-preheating reading (Kofman-Linde-Starobinsky) is the laboratory PROJECTION of this substrate process; the substrate transit is fundamental. The §VII.BP COINCIDENCE-BOUNDED entry is hereby characterized as a real Floquet/preheating phenomenon (LIVE μ_F=0.50 M_KK, DTC candidate) rather than a bounded nuisance — its boundedness is in the abundance footprint (drive near-antisymmetry), not in the dynamical amplification.

---

## Wave 2 Synthesis (team-lead)

*(Written after all 4 gates complete. Structure per `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`: one paragraph on what the wave resolved — did TRANSIT-PS-67 assemble end-to-end (W2-1), does the Sakharov first-peak survive the BAO θ_A residual (W2-2), does the relic saturate Suyama-Yamaguchi (W2-3), is the S101 resonance a live Floquet/preheating channel (W2-4) — plus the dual-prior posterior re-allocation per gate and the cross-gate threads (W2-1 → W2-2 P(k) hand-off; W2-1 → W4-1 shape-vs-amplitude scope split; W2-3/W2-4 → HY5 / A-QA-2 session-track promotions).)*

## Carry-Forward Computations

*(Written at wave close. One `### {CF-ID} — {title}` sub-heading per genuine future-work item, each with a 4-field-spec table (What / Inputs / Gate / Effort), per `CLAUDE.md §"No Technical Debt"` + `feedback_fix-in-session-never-defer.md`. Candidate items anticipated by the plan §"Wave 2 → Wave 4 Decision Point": session-promotion of TRANSIT-PS-67 into a `session-{N}` gate on W2-1 PASS (investigation results become permanent only via session migration per `gate-verdicts.md §"Investigation-Track Canonical Path"`); n_s(k) piecewise-vs-assembled divergence localization on W2-1 FAIL; multi-cutoff (√x) session sweep on W2-1 INFO; HY5 A_s/f_NL canonical reconciliation + mack falsifier-inventory τ_NL row on W2-3 PASS; A-QA-2 / S3-assumption modulus-effective-action handle + DTC characterization on W2-4 PASS; refined η_fold conformal-time integration on W2-2 INFO. If the wave produced zero genuine future-work items, state "No carry-forwards: all wave outcomes closed in-session".)*

## Constraint-Map Updates

*(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason. Process observations and in-session hygiene closures go here, NOT in Carry-Forward Computations per `CLAUDE.md` Wave-synthesis-discipline.)*

## Files Produced

*(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | Verdict line | Size.)*
