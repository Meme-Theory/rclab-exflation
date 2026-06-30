# Session 117 Wave 1 — A_s amplitude normalization (the Q23 rate-limiter) (Results Working Paper)

**Session**: 117 | **Wave**: 1 | **Plan**: session-117-plan-w1.md | **Theme**: A_s scalar-amplitude *magnitude* closure (the Q23 rate-limiter). The substrate over-produces A_s vs Planck (`A_s_CMB = 2.1e-9 ± 0.0294e-9`); the over-production *sign* is robust (`Γ ≤ 1`, both fork members positive), but the *magnitude* sits on a 2-member 𝒩-gap fork `{+0.196, +0.864}` OOM (gap = 0.6682 OOM = 2·log₁₀(2.15814), ≈410.5σ), adjudicated by the between-grid scale-coincidence sub-discriminator GS-1.

**Wave shape**: pure COMPUTE wave — 4 `gate_type: compute` gates, all PHONONIC, all `transit-dynamics-theorist`. Triggers: 1-1/1-2/1-3 `[SIGN]` (schema-v2 sign/magnitude/regime 3-tuple companion row REQUIRED); 1-4 `[VERIFY]` (NO 3-tuple). All close via a verdict line in `computations/session-117/s117_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`).

**Intra-wave dispatch order (load-bearing)**: **1-2 (GS-1) → 1-1**. GS-1 is plan-freeze-blocking for 1-1: 1-1 cannot emit a composite PASS/FAIL without GS-1's three-branch verdict already in `s117_gate_verdicts.txt`; if GS-1 has not landed, 1-1 honestly closes per `mechanical-closure-discipline.md` (`value='PRE-REG-INC_blocked_by_CF-S117-GS-1_UNCOMPUTED'`). 1-3 and 1-4 are independent and parallel-dispatchable with the 1-2/1-1 pair.

**Substrate framing (phononic)**: A_s IS the squeezed-exit power of the post-transit GGE relic — `D_K eigenvalues → Bogoliubov |β_k̂|² at the van Hove fold → exit normalization 𝒩 under the deg_T_BZ_pivot=+2 transport → A_s = |ζ_k̂(exit)|²/(2π²)`. The fork is not a fitting ambiguity; it is the substrate carrying TWO physically distinct normalization scales (microscopic KZ-coherence length vs hydrodynamic acoustic sound-horizon). GS-1 asks the substrate which scale the curvature/a₂-channel observable reads at; ALT-GREYBODY asks whether the substrate supplies the attenuation that closes the over-production without a fitted knob.

## Gate Sections

### §W1-1. CF-S117-T-FOLD-EXIT-NORMALIZATION (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-T-FOLD-EXIT-NORMALIZATION`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (post-fold exit normalization 𝒩; Mukhanov-Sasaki Radau propagation across `k/aH: 14.7 → 1`)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The post-fold exit normalization 𝒩 in `ζ_k̂(exit) = 𝒩·(k̂/aH)^{+2}·|β_k̂|(fold)` is intra-grid Parker-invariant (𝒩-spread ≤ 0.1 OOM across ≥5 matching surfaces), and the A_s magnitude fork `{+0.196, +0.864}` OOM collapses to a SINGLE value iff GS-1 selects a grid (CONVENTION-BLOCKED or PHYSICS-SCALE-SEPARATION); else the ≈410.5σ fork stands. Composite verdict keyed on the GS-1 (1-2) three-branch verdict; SIGN (over-production) is robust across both fork members, MAGNITUDE is the GS-1-adjudicated fork.
**Plan reference**: `sessions/session-plan/session-117-plan-w1.md` §W1-1 (machinery pin, thresholds, substitution chain, composite-precedence operator).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block per `.claude/templates/r3-yaml-gate-block.yaml` — verify by content presence (regex match), NEVER line/byte counts, per `feedback_max-effort-full-fidelity.md`):
- [x] **script** `computations/session-117/s117_t_fold_exit_normalization.py` — contains `from canonical_constants import` (Section 1) AND `print_verdict_payload` (def + call) ✓
- [x] **data** `computations/session-117/s117_t_fold_exit_normalization.npz` ✓
- [x] **plot** `computations/session-117/s117_t_fold_exit_normalization.png` ✓ (4-panel: MS curvature freezing | Parker 𝒩-spread | A_s magnitude fork | GS-1 composite collapse)
- [x] **verdict line** in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-T-FOLD-EXIT-NORMALIZATION:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + schema-v2 [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) ✓ + the `# composite-precedence:` disclosure row (empty-WKB-leg = RESOLVED-FROZEN ≠ BREAKDOWN/MARGINAL) ✓ + 3 extra companion rows (Parker cross-check; grid-discipline; plan-text-drift) ✓. Emitted via race-safe `emit_verdict` (7 rows, sig_5 unique).
- [x] **WP §W1-1 section** (this section) — `**Status**: COMPLETED`, `**Verdict**: FAIL`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present ✓

**MCP Pre-Compute Audit** (query-first per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("T-fold exit normalization A_s Mukhanov-Sasaki Radau frozen superhorizon")` → INV4-W1-4-EXIT-GREYBODY-A-S-NORMALIZATION (FAIL; a DIFFERENT, greybody, gate); `A_s = 3.30e-9 (FROZEN; Bulletin #3 corridor)` + `Z_norm = 1 (superhorizon, frozen)` (S77/S86 structural anchors, consistent with this gate's frozen-superhorizon regime); `A_s = squeeze × exit greybody filter` (S116 plan). **No prior `T-FOLD-EXIT-NORMALIZATION` closure** ⇒ gate is genuinely new (NOT PRE-CLOSED).
- `get_constant("A_s_FW")` → `1.5367059962762235e-8` (S111-CF-AS3a box-delta; ξ_KZ-grid fork member, round-trip anchor).
- `get_constant("deg_T_BZ_pivot")` → `2.0` (S110-CF-CV6B-DS-M4; the deg=+2 NON-SCALAR transport, canonical:717 / S93 W7-1).
- `get_constant("A_s_CMB")` → `2.1e-9` (Planck 2018 VI, σ = 0.03e-9; S96-OBS-ANCHOR-HYGIENE). Plan substitution-chain pins σ = 0.0294e-9 (→410.5σ); 0.03e-9 gives 402σ — both ~400σ.
- `get_constant("xi_KZ_FW")` → `0.018760052113614718` (S89; N_norm = ξ_KZ³ = 6.6024e-6).
- `get_constant("H_tilde_canonical_TD")` → `0.0059076` (canonical TD H̃; the +0.196 grid anchor via inv12_w3_5 A_s(H̃)=3.2994e-9).
- Input SHAs verified against plan pins at dispatch: s77 `80fbf580…` ✓, s111 `557b9c19…` ✓, inv12_w3_1 `323f1c74…` ✓, inv12_w3_5 `a5514a74…` ✓; GS-1 verdict line read from `s117_gate_verdicts.txt` (intra-wave, plan-freeze-blocking).

**Verdict**: **FAIL** (composite; physics-blocked by GS-1=INFO-RESIDUAL-PREFACTOR). schema-v2 3-tuple **sign_verdict=PASS / magnitude_verdict=FAIL / regime_verdict=VALID** → composite **FAIL** (gate-verdicts.md collapse: magnitude FAIL ∧ regime VALID ⇒ FAIL; AND plan-frozen operator: GS-1 ∉ {CONVENTION-BLOCKED, PHYSICS-SCALE-SEPARATION} ⇒ not PASS). `audit_sha256 = 89b51de59f4fd49a8a6055857f9df25faa1174d2dd21aa64ecf06c090fea89dd`, `content_sha256 = 92beda256d2635bd1f396898aef104fe2c09a106a4b5be04ab4bbe6bd525afdd`. 4-tuple: (value=𝒩-spread=0.016965 OOM [headline metric] with 𝒩_ξKZ=1 / 𝒩_H̃=0.21471, scheme=MS-RADAU-IMPULSE-QUENCH-BOGOLIUBOV, convention=GRID-DISCIPLINED-xi_KZ-vs-Htilde-foldgeom9.37-REJECTED-deg+2, L_max=N/A — z(τ) from s77, no fresh D_K diagonalization).

**Results**:

*Mukhanov-Sasaki Radau propagation (the genuine physics).* Background: quasi-de-Sitter, with `ν² ≡ (z''/z)/(aH)²` fixed BY s77 to `ν² = (k/aH)²_fold / [k²/(z''/z)]_fold = 14.672122² / 107.635582 = 2.00000000` — pure de Sitter, the ζ-freezing geometry. In `x ≡ k/(aH) = −kη` the MS equation is `d²v/dx² + (1 − ν²/x²)v = 0`. Radau (`solve_ivp`, rtol=1e-10, atol=1e-12, dense_output) propagated from `x_fold = 14.672` (BD adiabatic IC) through horizon crossing `x=1` into the deep-superhorizon frozen regime `x=0.0125`. **ODE success = True**; cross-check vs the analytic de-Sitter BD mode `v(x)=(1+i/x)e^{ix}`: max rel-dev `1.27e-11` over `x∈{10,5,2,0.5,0.1,0.025}` (the integration is faithful to 11 digits).

*Curvature freezing (RESOLVED-FROZEN regime confirmation).* `|ζ(x)|² = |v(x)|²·x²` (z ∝ a ∝ 1/x, z₁=1 units). `|ζ|²` at horizon crossing (x=1) = **2.000000**; at the deep-superhorizon surface (x=0.0125) = **1.000156**; ratio exit/frozen = **1.9997** — the textbook de-Sitter signature `|ζ(x)|² = ζ_∞²(1+x²)` → ζ freezes (∂ζ/∂x → 0) on the superhorizon side. This IS the "empty WKB leg / 89-of-89 frozen / Z_norm=1" S111-CF-AS3a regime, now demonstrated by direct propagation: `ω²(x) = k²(1−ν²/x²) < 0` for `x < √2`, so there is no subhorizon WKB oscillation phase past freeze-out — the curvature is conserved, NOT a regime breakdown.

*Intra-grid Parker 𝒩-spread (the DEMOTED consistency cross-check, GRID-INDEPENDENT).* Across ≥5 deep-superhorizon matching surfaces `x ∈ {0.20, 0.10, 0.05, 0.025, 0.0125}`, the frozen curvature normalized to the deepest surface gives `𝒩_i = {1.039838, 1.009842, 1.002343, 1.000469, 1.0}` ⇒ **𝒩-spread = max_i|log₁₀(𝒩_i/𝒩_ref)| = 0.016965 OOM ≤ 0.1** (PASS the demoted band). The residual is the `O(x²)` approach-to-frozen (a CONSERVATIVE upper bound — it → 0 as surfaces go deeper), not a Parker violation. Independent confirmation via the subhorizon leg: the adiabaticity parameter `|ω'/ω²| = |Ω'|/Ω²` at `x ∈ {14,11,8,6,4.5}` is `{7e-4, 1.5e-3, 4.1e-3, 1.0e-2, 2.6e-2}`, so the adiabatic occupation `|β_k|²` is Parker-conserved to `O((max|ω'/ω²|)²) = 2.857e-4 OOM`. Both measures are **grid-INDEPENDENT** (the curvature transfer shape is a ratio; both grids share the same MS propagation) ⇒ the 𝒩-spread is the same for ξ_KZ and H̃, confirming the S-1 audit's structural finding: **the 𝒩-spread is Parker-TRIVIAL and does NOT discriminate the grid SELECTION** (it is a within-grid robustness check, not the fork adjudicator).

*Exit normalization 𝒩 + round-trip.* ξ_KZ grid: `𝒩 ≡ A_s/A_s_FW = 1.000000` (A_s_FW IS the box-delta ξ_KZ value) ⇒ `A_s = 1.536706e-8`. Round-trip `A_s = β²_k̂/(2π²) = 3.033336e-7/(2π²) = 1.5367059963e-8` vs canonical `A_s_FW = 1.5367059962762235e-8` ⇒ **rel_dev = 0.0** (≤ 1e-4; S111 anchor 3.9e-6). H̃ grid: `𝒩 = A_s(H̃)/A_s_FW = 3.2994e-9/1.5367e-8 = 0.214708` ⇒ `A_s = 3.299435e-9`. The deg=+2 transport (`deg_T_BZ_pivot = +2.0`, NON-SCALAR, canonical:717) enters `ζ_k̂(exit) = 𝒩·(k̂/aH)^{+2}·|β_k̂|(fold)`.

*Grid discipline (fold-geometry grid EXPLICITLY REJECTED).* `OOM_naive_extrap = 9.373678` (s111) — the naive UV-slope (−0.003135) extrapolation of the fold-window REGIME spectrum to the box-delta MAGNITUDE scale k̂ — is the documented **artifact**, REJECTED (flag True). TWO-SPECTRA-TWO-ROLES: box-delta = MAGNITUDE source (A_s = β²_k̂/(2π²)); fold-window = REGIME source (89/89 frozen-superhorizon). The grid-disciplined OOM values are **+0.86437 (ξ_KZ) and +0.19622 (H̃)** — never 9.37.

*[SIGN] over-production substitution chain.* `OOM_G1 = log₁₀(A_s_FW/A_s_CMB) = log₁₀(1.5367059962762235e-8/2.1e-9) = +0.86437` (ξ_KZ); `OOM_G2 = log₁₀(3.2994349182266295e-9/2.1e-9) = +0.19622` (H̃); both **> 0 ⇒ over-production is SIGN-robust across BOTH fork members** (the `Γ ≤ 1` one-sided falsifier survives the fork). Fork gap `= OOM_G1 − OOM_G2 = 0.66815 OOM = 2·log₁₀(2.158120)` (Sage RealField-200; identity rel-dev `1.66e-16`). Fork separation in Planck units `= (1.5367e-8 − 3.2994e-9)/0.0294e-9 = 410.46σ` (σ=0.0294e-9 plan-pin; 402σ at σ=0.03e-9). The plan's 4-sig-fig forms (+0.86442/+0.19617, gap 0.66825 = 2·log₁₀(2.15814)) match these exact npz-sourced values to 5e-5 (A_s(H̃) rounding).

*GS-1 prerequisite read + composite collapse.* GS-1 (1-2) verdict read from `s117_gate_verdicts.txt` (supersession-aware; single non-superseded line): **INFO / INFO-RESIDUAL-PREFACTOR** (audit_sha `d7f28d3e…`). Per the plan FAIL_meaning: GS-1=INFO-RESIDUAL-PREFACTOR ⇒ the deg=+2 transport is NOT the sole carrier ⇒ the ≈410.5σ {+0.196, +0.864} fork is **genuine and unresolved** ⇒ `gs1_selects = False`. Plan-frozen operator: `composite PASS iff GS-1 ∈ {CONVENTION-BLOCKED, PHYSICS-SCALE-SEPARATION} ∧ 𝒩-spread ≤ 0.1` — first conjunct fails ⇒ **not PASS**. The 3-tuple: `sign_verdict = PASS` (over-production), `magnitude_verdict = FAIL` (fork stands), `regime_verdict = VALID` (composite-precedence override, below) ⇒ generic collapse `magnitude=FAIL ∧ regime=VALID ⇒ composite FAIL`. **Both readings agree: COMPOSITE = FAIL.** The Q23 rate-limiter is NOT closed this session; the A_s magnitude remains a multi-member plurality (cf. §W1-3 third value +0.384 ⇒ ≥3 members; `[[s114-as-functional-selection]]`).

**Composite-precedence companion row** (plan §W1-1 `composite_precedence`; gate-verdicts.md §"Plan-frozen gate-block operator precedence"): the empty WKB leg (`n_wkb=0`, 89/89 frozen-superhorizon, `Z_norm=1`, S111-CF-AS3a RESOLVED-FROZEN) is the **CORRECT frozen-superhorizon physics** ⇒ `regime_verdict = VALID`, OVERRIDING the generic "WKB-leg-empty ⇒ MARGINAL" reading. This is load-bearing: without the override the empty WKB leg would read regime=MARGINAL, and `magnitude=FAIL ∧ regime=MARGINAL ⇒ composite INFO` — the override correctly yields **FAIL** (the fork genuinely stands, not a marginal-regime INFO). Disclosed via the `# composite-precedence:` verdict-file companion row.

**Substitution chain** ([SIGN], per math-scripts.md §"Double-Check Logic Before Compute"; numbers substituted):
```
Claim: A_s^squeeze > A_s^Planck (OOM>0, over-production) is SIGN-robust across BOTH fork members;
       the MAGNITUDE (which OOM, +0.196 vs +0.864) is the GS-1-adjudicated fork, NOT the 𝒩-spread.
Def 1: ζ_k̂(exit) = 𝒩·(k̂/aH)^{+2}·|β_k̂|(fold)        [exit curvature; deg_T_BZ_pivot=+2, canonical:717]
Def 2: A_s = |ζ_k̂(exit)|²/(2π²)·N_norm                [squeezed-exit scalar amplitude]
Def 3: A_s^Planck = A_s_CMB = 2.1e-9, σ = 0.0294e-9   [canonical:84, Planck 2018 VI]
Def 4: ξ_KZ grid  ⇒ 𝒩=1      ⇒ A_s = A_s_FW = 1.5367059962762235e-8   [round-trip β²/(2π²), reldev 0.0]
       H̃  grid  ⇒ 𝒩=0.21471 ⇒ A_s = 3.2994349182266295e-9            [inv12_w3_5, UNIFIED-AS-79]
Substitute (ξ_KZ): OOM_G1 = log10(1.5367059962762235e-8/2.1e-9) = +0.86437
Substitute (H̃):    OOM_G2 = log10(3.2994349182266295e-9/2.1e-9)  = +0.19622
Simplify (gap):    OOM_G1 − OOM_G2 = log10(4.65728) = 0.66815 = 2·log10(2.158120)  [Sage-exact, resid 1.66e-16]
Simplify (σ):      fork_σ = (1.5367e-8 − 3.2994e-9)/0.0294e-9 = 410.46σ
Direction (SIGN):      sign(OOM_G1)=sign(OOM_G2)=+ ⇒ over-production SIGN-robust UNCONDITIONALLY ⇒ sign_verdict PASS
Direction (𝒩-spread):  Parker forces 𝒩-spread=0.0170 OOM ≤ 0.1 in BOTH grids (grid-INDEPENDENT) ⇒ does NOT resolve the 0.668 gap
Direction (MAGNITUDE): GS-1 = INFO-RESIDUAL-PREFACTOR ⇒ fork STANDS ⇒ magnitude_verdict FAIL
Direction (REGIME):    empty-WKB-leg = RESOLVED-FROZEN (composite_precedence) ⇒ regime_verdict VALID (not MARGINAL)
Conclusion:            composite = FAIL (sign PASS, magnitude FAIL, regime VALID; gate-verdicts.md collapse
                       + plan-frozen operator GS-1∉{CONV-BLOCKED,PHYS-SCALE-SEP}).
```

**Substrate framing (phononic, IS-not-IN)**: A_s IS the squeezed-exit power of the post-transit GGE relic — `D_K eigenvalues at the van Hove fold → Bogoliubov pair-production |β_k̂|² (the fold REORGANIZES the fiber spectrum; the excitations ARE the reorganization, not particles produced IN a box) → exit normalization 𝒩 under the deg=+2 transport → A_s = |ζ_k̂(exit)|²/(2π²)`. The MS Radau propagation demonstrates, from first principles, that this curvature FREEZES on the superhorizon side (|ζ|² → const, exit/frozen → 2 is the de-Sitter signature) — the "empty WKB leg" is the substrate's correct frozen-superhorizon physics, not a numerical breakdown. The 𝒩-spread cross-check confirms the within-grid normalization is Parker-stable (0.017 OOM), but — and this is the S-1 audit's structural point — it is GRID-INDEPENDENT and therefore CANNOT adjudicate the fork: Parker invariance holds inside EITHER grid trivially. The fork is the substrate carrying TWO physically distinct normalization scales (the microscopic KZ-coherence length ξ_KZ vs the hydrodynamic acoustic sound-horizon), whose ratio under the common deg=+2 transport IS the 0.668-OOM gap. GS-1 (1-2) asked the substrate which scale the curvature/a₂-channel observable reads at, and the substrate's answer was INFO-RESIDUAL-PREFACTOR — neither a clean coincidence nor a clean deg=+2 scale-separation; a residual non-scale prefactor (the greybody fitted knob / c_sub Mellin-weight / F_amp backreaction, all scheme-bearing) co-carries the fork. So 1-1 inherits an un-collapsed fork: the over-production is real and sign-robust (the framework over-produces A_s relative to Planck, unconditionally), but its MAGNITUDE is a genuine ≥2-member plurality, not a zero-parameter prediction this session.

---

### §W1-2. CF-S117-GS-1 (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-GS-1`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (between-grid scale-coincidence sub-discriminator; plan-freeze-blocking for 1-1)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: The two A_s normalization grids — `ℓ_occ = ξ_KZ` (KZ coherence/healing length, UV) and `ℓ_horizon = c_s/(aH)|_exit` (acoustic sound-horizon comoving scale, IR) — either coincide (`Δ_scale ≤ 0.05` OOM ⇒ the 0.668-OOM fork is a normalization-convention artifact ⇒ CONVENTION-BLOCKED) or are genuinely distinct substrate scales whose ratio under the common deg=+2 transport IS the fork (`|2·Δ_scale − 0.668| ≤ 0.1` OOM ⇒ Volovik hydrodynamic selection picks the acoustic-horizon grid ⇒ PHYSICS-SCALE-SEPARATION); neither ⇒ INFO-RESIDUAL-PREFACTOR. This gate supplies the deciding computation WITHOUT pre-judging the fork (held open per the S-1 audit; the three branches are the substrate's three possible answers).
**Plan reference**: `sessions/session-plan/session-117-plan-w1.md` §W1-2 (machinery pin, three-branch thresholds, substitution chain, carrier-exponent sign resolution).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block per `.claude/templates/r3-yaml-gate-block.yaml` — verify by content presence (regex match), NEVER line/byte counts, per `feedback_max-effort-full-fidelity.md`):
- [x] **script** `computations/session-117/s117_gs1_grid_selection.py` — contains `from canonical_constants import` (Section 1) AND `print_verdict_payload` (def + call) ✓
- [x] **data** `computations/session-117/s117_gs1_grid_selection.npz` ✓
- [x] **plot** `computations/session-117/s117_gs1_grid_selection.png` ✓
- [x] **verdict line** in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-GS-1:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + schema-v2 [SIGN] 3-tuple row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) ✓ + 2 extra companion rows (required-c_s window; 3He-B lab cross-check) ✓
- [x] **WP §W1-2 section** (this section) — `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("A_s grid selection xi_KZ acoustic horizon scale coincidence fork")` → only S47 `acoustic_horizon` + investigation-6 priors; NO prior GS-1 grid-selection closure ⇒ gate is genuinely new (NOT PRE-CLOSED).
- `get_constant("Mach_max_framework")` → 13.75 (S85; van Hove fold supersonic Mach; alias `Mach_max`).
- `get_constant("c_Gold")` → 0.915 (S52 GL-Josephson; Goldstone sound speed, M_KK units).
- `get_constant("deg_T_BZ_pivot")` → 2.0 (S110-CF-CV6B-DS-M4; the deg=+2 NON-SCALAR transport, canonical:717 / S93 W7-1).
- canonical_constants.py: `xi_KZ_FW=0.018760052113614717` (L617), `c_BLV=0.485` (L516, post-fold GGE scalar c_s), `H_fold=586.5267713`, `dt_transit=1.1301575e-3`.
- s77_n_pivot_map.npz (pinned, sha256 `80fbf580…`): `k_pivot_com_fold=14.311093`, `k_over_aH_fold=14.672122`, `pivot_a_at_exit=22.610503`, `pivot_H_at_exit=0.632940`.

**Verdict**: **INFO** — `INFO-RESIDUAL-PREFACTOR`. schema-v2 3-tuple **sign_verdict=PASS / magnitude_verdict=INFO / regime_verdict=VALID** → composite **INFO** (gate-verdicts.md collapse: magnitude INFO ⇒ composite INFO). audit_sha256 `d7f28d3e2cf5c22b466ace299d1c537423c12d17dea2f9c40b9452780422a4bf`, content_sha256 `990ba8ea3469caa3e972f7554891bc5e40e924082735efe8e2278cb48ee5f0c3`. 4-tuple: (value=Δ_scale=0.532514, scheme=GRID-SELECTION-DISJOINT-SCALES, convention=ξ_KZ-coherence-UV-vs-acoustic-sound-horizon-IR, L_max=N/A).

**Results**:

NUMBERS (M_KK⁻¹ unless noted):
- `ℓ_occ = ξ_KZ = 0.0187600521` (UV coherence / KZ healing length).
- `(aH)|_exit` resolved from transit kinematics: at horizon exit `k = aH`, so `(aH)|_exit = k_pivot = 14.311093`. TWO routes agree to rel-dev `2.5e-16`: (i) `k_pivot_com_fold = 14.311093`; (ii) `pivot_a_at_exit × pivot_H_at_exit = 22.610503 × 0.632940 = 14.311093`. Kinematic consistency: `H_fold·dt_transit = 0.662868 ≈` plan-pin 0.663; `(k/aH)|_fold = 14.672 ≈ 14.7`; `aH|_fold = 0.975394` (cross-check).
- c_s PRIMARY (plan-pin) `= c_Gold = 0.915` (Goldstone first-sound). Mach relation ⇒ implied `v_transit = Mach·c_s = 13.75×0.915 = 12.581`. `ℓ_horizon = c_s/(aH)|_exit = 0.915/14.311 = 0.0639364` (dimension: [c_s]=M_KK⁰, [aH]=M_KK ⇒ M_KK⁻¹ length-consistent).
- c_s CROSS-CHECK `= c_BLV = 0.485` (post-fold GGE scalar c_s) ⇒ `ℓ_horizon = 0.0338898`.

`Δ_scale = |log₁₀(ℓ_occ) − log₁₀(ℓ_horizon)|`:
- PRIMARY (c_Gold): `Δ_scale = 0.532514`, `2·Δ_scale = 1.065029`.
- CROSS-CHECK (c_BLV): `Δ_scale = 0.256835`, `2·Δ_scale = 0.513670`.

deg=+2 backbone (Sage RealField-200): `fork_OOM = log₁₀(A_s_G1/A_s_G2) = log₁₀(1.5367e-8/3.2994e-9) = 0.668154 = 2·log₁₀(2.158127)`; identity `2·log₁₀(√r) = log₁₀(r)` rel-dev `= 0.0e0` (< 1e-6 tol). Plan anchor `2·log₁₀(2.15814) = 0.668159` matches to 5e-6 (5-sig-fig A_s rounding).
- backbone residual (c_Gold): `|2·Δ_scale − fork_OOM| = |1.065 − 0.668| = 0.396874` OOM.
- backbone residual (c_BLV): `0.154484` OOM.

THREE-BRANCH PARTITION (on PRIMARY c_Gold):
- CONVENTION-BLOCKED (`Δ_scale ≤ 0.05`)? **No** (0.5325 ≫ 0.05).
- PHYSICS-SCALE-SEPARATION (`|2·Δ_scale − 0.668| ≤ 0.1`)? **No** (0.397 > 0.1).
- backbone diverges (`|2·Δ_scale − 0.668| > 1.0`, FAIL trigger)? **No** (0.397 < 1.0).
- ⇒ **INFO-RESIDUAL-PREFACTOR**. ROBUST across the sound-speed choice: c_BLV also lands INFO (2·Δ = 0.514, residual 0.155 > 0.1).

WHY INFO (structural root): the required c_s for PHYSICS-SCALE-SEPARATION is the window `c_s ∈ [0.51640, 0.65011]` M_KK (center 0.57941, Sage-200bit), i.e. `ℓ_horizon ∈ [0.03608, 0.04543]`. The two canonical sound speeds STRADDLE this gap — c_BLV = 0.485 just below, c_Gold = 0.915 well above — so NO canonical sound speed places the acoustic-horizon scale at the deg=+2 fork-carrying separation. The 0.668-OOM fork is therefore NOT a pure scale-separation under deg=+2; a residual non-scale prefactor (the greybody fitted-knob / c_sub Mellin-weight / F_amp backreaction differences between the impulse and TD/ζ assemblies — cf. INV12-W3-4 greybody-as-fit, S114/S115 magnitude pluralism) co-carries it.

[SIGN] carrier↔scale exponent: `deg_T_BZ_pivot = +2` (>0) ⇒ A_s ∝ carrier², carrier ∝ scale^{+1}; `carrier_exponent e = deg/2 = +1`, sign = + (consistent with deg>0). `|e| = 1` is the load-bearing magnitude; the near-flat sudden-spectrum slope −0.003135 renders the within-grid tilt sub-dominant. **sign_verdict = PASS**.

3He-B LAB CROSS-CHECK (V.2, non-gating): `R_scale = ℓ_occ/ℓ_horizon = 0.293417 < 1` (PRIMARY c_Gold). R_scale is DIMENSIONLESS ⇒ the S86 W11-1 M_KK→SI length map cancels (numerator and denominator scale identically — a (Δ_B/Δ_A)^p-style ratio cancellation), so the lab twin reads the SAME R_scale: microscopic (UV coherence) below causal (IR horizon) corroborated, NO in-framework sign contradiction ⇒ does not trip the FAIL guard.

DOWNSTREAM: per the plan INFO_meaning, INFO-RESIDUAL means the deg=+2 transport is NOT the sole carrier of the fork ⇒ **1-1's fork STANDS** (CF-S117-T-FOLD-EXIT-NORMALIZATION cannot collapse to a single-valued A_s on a clean scale-coincidence; it routes to its physics-blocked branch). The two A_s grid values remain a genuine 2-member plurality whose 0.668-OOM split is partly scale-separation (≤ the c_BLV reading, 2·Δ = 0.514) and partly residual prefactor.

**Substitution chain** ([SIGN], per math-scripts.md §"Double-Check Logic"):
```
Claim: carrier ∝ scale^{+1} under deg=+2 (carrier-scale exponent sign is +), and the 0.668-OOM
       A_s fork is EITHER a convention artifact (scales coincide) OR a genuine two-scale separation.
Def 1: l_occ      = xi_KZ = 0.018760052113614717        [xi_KZ_FW, canonical:617]
Def 2: c_s        = c_Gold = 0.915                       [transit-frame Goldstone sound speed,
                                                         canonical sound-speed identification;
                                                         Mach=13.75 => v_transit = Mach*c_s = 12.581]
Def 3: (aH)|_exit = k_pivot = 14.311093                  [at horizon exit k=aH; s77 npz]
Def 4: l_horizon  = c_s/(aH)|_exit = 0.915/14.311 = 0.0639364   [comoving acoustic sound horizon]
Def 5: D_scale    = |log10(l_occ) - log10(l_horizon)| = |-1.72697 - (-1.19437)| = 0.532514
Def 6: deg_T_BZ_pivot = +2  =>  A_s ~ carrier^2, and deg == d(ln A_s)/d(ln scale) = 2*e
Step (SIGN):  2*e = +2  =>  e = +1  =>  carrier ~ scale^{+1};  sign(e) = + (deg>0) => sign_verdict PASS
Step (fork):  fork_OOM = log10(A_s_G1/A_s_G2) = 0.668154 = 2*log10(2.158127)  [Sage-exact identity, rel-dev 0]
Step (branch): 2*D_scale = 1.065029;  |1.065029 - 0.668154| = 0.396874 > 0.1 (and D_scale=0.5325 > 0.05)
              => neither definitive branch  =>  INFO-RESIDUAL-PREFACTOR
Step (root):  required c_s in [0.516, 0.650] for PHYSICS-SCALE-SEP; c_BLV=0.485 below, c_Gold=0.915 above
              => no canonical sound speed in the fork-carrying band => residual non-scale prefactor exists
Conclusion:   sign_verdict = PASS (e=+1, deg=+2); magnitude_verdict = INFO (INFO-RESIDUAL-PREFACTOR);
              regime_verdict = VALID (closed-form scalar evals, no expansion breakdown) => composite INFO.
```

**Substrate framing**: PHONONIC. GS-1 asked the substrate which of its two intrinsic lengths the curvature/a₂-channel (hydrodynamic IR) observable reads at — ℓ_occ (the KZ healing length: microscopic coherence over which the post-transit GGE relic's pair correlations set in, UV) or ℓ_horizon (the acoustic sound-horizon: causal scale of first-sound across the supersonic Mach-13.75 transit, IR). These are two substrate-IS lengths the fabric carries, not coordinates in a container. The substrate's answer is NEITHER a clean coincidence NOR a clean deg=+2 scale-separation: the two lengths are separated by 0.533 OOM (factor 3.41), which under deg=+2 would over-produce a 1.065-OOM A_s fork, but the realized fork is only 0.668 OOM. The 0.40-OOM shortfall IS the substrate telling us a non-scale prefactor (the greybody exit knob, the c_sub Mellin-weight, the F_amp backreaction factor — all scheme-bearing per the established greybody-as-fit and magnitude-pluralism results) co-carries the fork. The 3He-B lab twin (a controlled realization OF the substrate transit) corroborates the microscopic-below-causal ordering R_scale = 0.293 < 1, conversion-invariantly. The fork is held open as a genuine 2-member plurality; 1-1 inherits an un-collapsed fork.

---

### §W1-3. CF-S117-ROUTE-B-PW-SOCC (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-ROUTE-B-PW-SOCC`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (Route-B Peter-Weyl A_s recompute with the occupied-state functional `S_occ = (1+2n_k)·S_fold`)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: Recomputing the Route-B Peter-Weyl A_s with the OCCUPIED-state spectral functional `S_occ = (1+2n_k)·S_fold` (NOT the vacuum `S_fold`), CC3-threaded (`d ln A_s / d ln H̃ = +2`), images the box-delta/impulse magnitude (+0.864 OOM, PASS-as-image) rather than the TD/ζ magnitude (+0.196, FAIL), OR lands at a distinct third value (INFO), expanding the A_s plurality from 2 to 3 members. SIGN: the S_occ lift is positive (occupied-state squeezes MORE) but by ≪ 0.1 OOM, so the image identity is set by the BASE Route-B-PW assembly.
**Plan reference**: `sessions/session-plan/session-117-plan-w1.md` §W1-3 (machinery pin, image-classification thresholds, substitution chain, regulator pin).

**Output Artifacts** (closure-verification checklist; mirrors the plan `output_artifacts:` block per `.claude/templates/r3-yaml-gate-block.yaml` — verify by content presence (regex match), NEVER line/byte counts, per `feedback_max-effort-full-fidelity.md`):
- [x] **script** `computations/session-117/s117_route_b_pw_socc.py` — contains `from canonical_constants import` (line ~88) AND `print_verdict_payload` (def + call) ✓
- [x] **data** `computations/session-117/s117_route_b_pw_socc.npz` ✓
- [x] **plot** `computations/session-117/s117_route_b_pw_socc.png` ✓
- [x] **verdict line** in `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-ROUTE-B-PW-SOCC:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓ + schema-v2 [SIGN] 3-tuple companion row (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`) ✓ + 4 extra companion rows (regulator_pin, base-provenance, K_sub-reading robustness, plan-text-drift) ✓
- [x] **WP §W1-3 section** (this section) — `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present ✓

**MCP Pre-Compute Audit** (queries executed BEFORE writing the script, per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("Route-B Peter-Weyl A_s AMPLITUDE-NORM-66 amplitude normalization")` → confirmed gate **AMPLITUDE-NORM-66** = FAIL (marginal), "A_s gap 3.15 OOM (Route B, PW)"; closed-mechanism **AS-ROUTE-B-PW-S66** (the S66 crisis lineage, NOT a closure that pre-empts this gate); open-channel **Q23** "A_s normalization is the sole open residual" — gate is LIVE, not pre-closed.
- `get_constant("A_s_FW")` → `1.5367059962762235e-8` (S111-CF-AS3a box-delta; ξ_KZ-grid fork member, comparator).
- `get_constant("A_s_CMB")` → `2.1e-9` (Planck 2018 VI; S96-OBS-ANCHOR-HYGIENE).
- `get_constant("H_tilde_canonical_TD")` → `0.0059076` (canonical TD H̃; CC3 anchor).
- npz inspection of `s66_amplitude_norm.npz` (Route-B PW raw `A_s_route_B_PW=2.918e-6`, `frac_PW=3.19e-4`) and `inv12_w1_2_a_s_gge_modular_reference.npz` (base `A_s_BD=5.078171e-9`, `n_bar_mw=2.7358e-4`, K_sub readings R1–R4). Input SHAs verified against plan pins at dispatch (all 3 matched).
- **Not pre-closed**: AMPLITUDE-NORM-66 is the S66 FAIL lineage; this gate is a fresh route-robustness recompute under the modern (reconciled) normalization with the occupied-state functional. PROCEED.

**Verdict**: **INFO** (composite). Schema-v2 [SIGN] 3-tuple: `sign_verdict=PASS`, `magnitude_verdict=INFO`, `regime_verdict=VALID` → collapse → **INFO**.
`audit_sha256=219802b75289933fefde4dc09c0559a9b2d1c9f95f06703bde897ebdafb83ad5`
`content_sha256=35876f256adf11d970b2062d72a3f902917caae26012d3f911c6e9cd131bc6ba`
4-tuple: `(value=0.38372558938069795 [OOM_RB], scheme=ROUTE-B-PETER-WEYL-S_occ-CC3, convention=OCCUPIED-state-S_occ=(1+2n_k)·S_fold-Branch-A-Zubarev, L_max=10)`.

**INFO meaning (image = third point; plurality 2→3)**: the S_occ-corrected Route-B Peter-Weyl assembly images **neither** fork member. `OOM_RB = +0.38373` lies `0.481` OOM from the box-delta image (+0.864) and `0.188` OOM from the TD/ζ image (+0.196) — both > the 0.1 tolerance. The A_s magnitude plurality **expands from 2 members to 3**: box-delta (ξ_KZ, +0.864) / TD-ζ (H̃, +0.196) / Route-B-PW GGE-modular (+0.384). The magnitude question widens rather than narrows. This is the pre-registered INFO branch and the third-point feeds the `[[s114-as-functional-selection]]` PLURALISM-PERMANENT lineage: A_s magnitude is genuinely functional-selection-dependent (an open structural d.o.f.), not a single-route artifact.

**Results**:

*Base assembly (CC3-anchored TD-canonical Route-B / Bunch-Davies floor):*
- `A_s^RouteB-vac = A_s_BD = 5.078171e-9` (S82 W2-4 / S84 AS-PIN-MAP-COMMIT; the modern reconciled image of the S66 Route-B-PW raw crisis value `2.918e-6` / gap 3.143 OOM, brought to canonical H̃ via UNIFIED-AS-79 + CC3). OOM(base) = **+0.38349**.

*S_occ occupied-state lift (R2 mult-weighted-mean = plan-pinned reading):*
- `n̄ = n_bar_mw = 2.735794e-4` (inv12_w1_2 locked relic); `K_sub = 1 + 2n̄ = 1.0005471589` (stored-R2 residual `0.00e+00`).
- `A_s^RouteB-SOcc = K_sub · A_s^RouteB-vac = 5.080950e-9`. `ΔOOM_Socc = log₁₀(K_sub) = +2.376e-4` OOM ≪ 0.1 ⇒ **S_occ does NOT bridge the fork**; the base assembly fixes the image.
- `OOM_RB = log₁₀(A_s^RouteB-SOcc / A_s_CMB) = +0.38373`.

*Image classification (tolerance 0.1 OOM):*
- box-delta (ξ_KZ): `OOM_box = +0.86437`, `|dist| = 0.48065` > 0.1 → not imaged.
- TD/ζ (H̃ grid): `OOM_TD = +0.19622`, `|dist| = 0.18751` > 0.1 → not imaged.
- ⇒ **image = third-point** → `magnitude_verdict = INFO`.

*K_sub-reading robustness (R1–R4):* OOM per reading = {R1_softest +0.383497, R2_mult_weighted_mean +0.383726, R3_geometric_mean +0.383652, R4_max_occupation +0.385151}; **spread = 0.001654 OOM; all_third_point = True**. The S_occ occupation-reading choice (R1/R2/R3/R4) does NOT change the image — the third-value verdict is functional-reading-robust. (inv12_w1_2 R1-softest cross-check: K_sub=1.00002045, A_s_GGE=5.078275e-9, OOM=+0.38350.)

*CC3 thread:* `d ln A_s / d ln H̃ = 2.000000000888` (target 2.0; residual 8.88e-10 < 1e-9 rel_tol → PASS); A_s(H̃_can) consistency `5.080950e-9 == A_s^RouteB-SOcc`. The Route-B base carries the +2 power-law H̃-dependence (UNIFIED-AS-79 CC3 identity), confirming the H̃-anchoring.

**Substitution chain** (math-scripts.md MANDATORY; numbers substituted):
- Claim: S_occ INCREASES A_s but by ≪ 0.1 OOM, so the image is set by the BASE Route-B-PW assembly, not by S_occ.
- Def 1: `S_occ = (1+2n_k)·S_fold` [occupied-state functional]; Def 2: `n̄ = 2.7358e-4` [inv12_w1_2]; Def 3: `K_sub = 1 + 2(2.7358e-4) = 1.0005472`; Def 4: `A_s^RouteB-vac = A_s_BD = 5.078171e-9` [CC3-anchored to H̃=5.9076e-3]; Def 5: `A_s^RouteB-SOcc = K_sub·A_s^RouteB-vac = 5.080950e-9`; Def 6: `OOM_RB = log₁₀(5.080950e-9 / 2.1e-9) = +0.38373`.
- Substitute: `ΔOOM_Socc = log₁₀(1.0005472) = +2.376e-4`; `|ΔOOM_Socc| = 2.4e-4 ≪ 0.1`.
- Direction (SIGN): `K_sub > 1 ⇒ A_s^RouteB-SOcc (5.080950e-9) > A_s^RouteB-vac (5.078171e-9)`, Δ = +2.78e-12 > 0 ⇒ lift confirmed ⇒ `sign_verdict = PASS`.
- Direction (IMAGE): `|0.38373 − 0.864| = 0.481 > 0.1` AND `|0.38373 − 0.196| = 0.188 > 0.1` ⇒ neither fork member ⇒ third point ⇒ `magnitude_verdict = INFO`.
- Conclusion: composite **INFO** (sign=PASS, magnitude=INFO, regime=VALID, per gate-verdicts.md collapse rule).

**Regulator pin**: `a_n^{ζ}` (Branch-A Zubarev/zeta-regularized; no regulator mixing across the A_s ledger per S83 W1-G1).

**Plan-text-drift note** (`substrate-first-canonical-sourcing.md §(ii.B)`): `canonical_constants.py` drifted from the plan-pinned `8c850fd95a3214211cfb37ee66bec7da19f2344fb03d976a85cf0f2c4a4bbdaa` (verified at dispatch start) to runtime `d884a2b51200139296369dc6ed6ef2818b70386aee24e36b6c95365b43d3d78c` — the sibling in-session gate **W0-1 (CF-S117-HK-RHOS-C2-PROMOTE, gen-physicist)** appended `rho_s_C2 = 7.962` (S48 MASS-48; +4 lines). **BENIGN**: the three constants this gate consumes (`A_s_CMB`, `A_s_FW`, `H_tilde_canonical_TD`) are bit-identical pre/post; `OOM_RB` is unaffected. The emitted `audit_sha256` correctly reflects the runtime file state per §(ii.B) (item 3: emit with runtime canonical state; plan-pinned value preserved as the audit-trail pointer in the verdict companion row).

**Substrate framing (phononic, IS-not-IN)**: Route-B Peter-Weyl IS the substrate's spectral-sum reading of A_s — `D_K eigenvalues → van Hove fold reorganization → squeezed power summed over the Peter-Weyl (p,q) sectors → A_s`. It is an INDEPENDENT assembly of the same substrate-IS observable, distinct from the box-delta impulse-propagation route (single mode k̂) and the TD/ζ five-factor SR ledger. The occupied-state functional `S_occ = (1+2n_k)·S_fold` replaces the Bunch-Davies vacuum reading with the GGE-relic occupation the substrate actually carries (n̄ = 2.736e-4 frozen quasiparticle pairs; the Ordered Veil `S_ent=0` licenses the frozen-n reading — the excitations ARE the fold reorganization, not particles produced IN a container). The gate asked whether the substrate's spectral-sum route lands on the same magnitude as its impulse route: it does **not** — Route-B images a third value (+0.384), sitting between the two fork members. The substrate carries (at least) THREE distinct A_s normalization magnitudes; which one a detector reads is set by the functional-selection / grid-selection question (GS-1, gate 1-2), not pre-fixed. This is the substrate-IS content of the A_s magnitude PLURALISM (`[[s114-as-functional-selection]]`).

---

### §W1-4. CF-S117-ALT-GREYBODY (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `CF-S117-ALT-GREYBODY`
**Trigger**: `[VERIFY]`
**Classification**: **PHONONIC** (exit-greybody filter corridor; two substrate-IS bridge maps in the d_A=0 even-morphism parity-admissible sector)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: At least one of two alternative substrate-IS exit-greybody bridge maps — (1) spectral-moment-ratio `Γ = Res_W(s)/Res_W(s')` (Wodzicki two-pole / `a_n^{Pauli-Villars}` moment ratio on the exit-horizon BdG sector), (2) Connes-distance `Γ` from `d_C = 1/(λ_max − λ_min)` — reaches the required attenuation `Γ_req = 10^{−OOM}` (0.137 box-delta / 0.636 slow-roll), or the fitted comparator 0.512, within rel_tol ≤ 0.10 at a substrate-natural (non-in-band, non-fitted) scale, WITHOUT the S95 A2 in-band V0 sigmoid knob. FAIL ⇒ "NOT substrate-derivable" generalizes from one corridor (INV12-W3-4) to three construction classes (toward a structural wall).
**Plan reference**: `sessions/session-plan/session-117-plan-w1.md` §W1-4 (machinery pin, rel_tol ≤ 0.10 agreement gate, substitution chain, regulator + Mellin pole convention pins).

**Output Artifacts** (verified on disk by content presence, NEVER line/byte counts, per `feedback_max-effort-full-fidelity.md`):
- (1) script `computations/session-117/s117_alt_greybody.py` — PRESENT (24,839 B); `from canonical_constants import` ✓, `print_verdict_payload` ✓
- (2) data `computations/session-117/s117_alt_greybody.npz` — PRESENT (8,491 B)
- (3) plot `computations/session-117/s117_alt_greybody.png` — PRESENT (117,519 B; bridge-values-vs-targets bar + PV regulator-mass knob diagnostic)
- (4) verdict line `computations/session-117/s117_gate_verdicts.txt` matching `^CF-S117-ALT-GREYBODY:.* audit_sha256=[a-f0-9]{64}` ✓ + dual-SHA companion row ✓; NO schema-v2 3-tuple ([VERIFY] trigger, `schema_v2_3tuple_required: false`). `audit_sha256=649ce24486c60645…d66b25`, `content_sha256=308fbf259e332e05…a02f6dd9`. Emitted via race-safe `emit_verdict` (8 rows, sig_5 unique).
- (5) this WP §W1-4 section (Status COMPLETED, Verdict, Output Artifacts, MCP Pre-Compute Audit).

**MCP Pre-Compute Audit** (query-first per `.claude/rules/knowledge-index-usage.md`):
- `search_knowledge("exit greybody attenuation A_s substrate-derivable Wodzicki Connes distance")` → INV12-W3-4-GREYBODY-FROM-BDG **FAIL** (derived ∫Γ=0.036265 vs fitted 0.512, agreement 0.929); S95-W4-3-HAWKING-GREYBODY-AS **INFO** (transmitted_fraction 0.511872); synthesis identity `|O_g| = e^{−d/ℓ} = Γ(ω)e^{−2πω/κ}` (Connes distance = greybody modulus, eq_18220). `CF-S117-ALT-GREYBODY` itself NOT pre-existing ⇒ genuinely new.
- `trace_entity("greybody")` → 6 prior gates (S43, S101, S95-W4-3, S110-CF-AS2, INV12-W3-4, INV4-W1-4); S110-CF-AS2 had in-band rel_dev 0.049 but WKB-INVALIDATED (eps_WKB BREAKDOWN); **none** uses the Wodzicki moment-ratio or Connes-diameter bridge maps tested here ⇒ the two classes are genuinely UNTESTED (INV12-W3-4's "NOT substrate-derivable" is SCOPED to the Pöschl-Teller near-horizon-barrier family).
- `get_constant("kappa_exit")` → 47.6146 (S95); `get_constant("Delta_BCS")` → 0.4642547 (S70, R-protected). Both confirmed against the plan pins.

**Verdict**: **FAIL** (composite; regime VALID). Both bridge maps miss all three targets at every substrate-natural (knob-free) scale; composite best `rel_dev = 0.1838 ≫ 0.10`. Not INFO (INFO requires exactly one bridge map reaching; here BOTH miss).

**Results**:

*Substrate eigenvalue inputs* (closed-form bridge-map evaluations on EXISTING caches; no new spectrum build): D_K spectrum from `s84_spectrum_cache_L12_tau019.npz` (L_max=12, τ_fold=0.19; n=166,896 with multiplicity; |λ| ∈ [0.819741, 5.418937]); exit-horizon BdG dispersion ω_k from `inv12_w3_4_greybody_from_bdg.npz` (n=1248; ω ∈ [0.940917, 3.720580], ω_k = √(λ_k⁴+Δ²), μ_chem=0).

*Targets (substitution chain)*: Γ_req(box-delta) = A_s_CMB/A_s_FW = 2.1e-9 / 1.5367e-8 = **0.136656** (OOM_box = log₁₀(A_s_FW/A_s_CMB) = +0.86437); Γ_req(slow-roll) = 10^{−0.19617} = **0.636546** (A_s(H̃) plan-pinned OOM); Γ_fit = **0.511872** (s95 fitted comparator; cross-checked = expected to 1e-6). The fitted 0.512 lies BETWEEN the two Γ_req — matching NEITHER (placed at band-midpoint by the S95 A2 sigmoid knob).

*Bridge map (2) — Connes distance* `d_C = 1/(λ_max − λ_min)` [genuinely knob-free; one number per spectrum, no placement freedom]:
- `Connes_DK` = 1/4.599196 = **0.217429** (plan-pinned s84 λ_max/λ_min) → best rel_dev 0.575 (vs fit)
- `Connes_BdG` = 1/2.779663 = **0.359756** (exit-horizon BdG sector ω_k) → best rel_dev **0.297** (vs fit)
- Connes bridge map MISSES (best 0.297 ≫ 0.10).

*Bridge map (1) — Wodzicki / a_n^{Pauli-Villars} moment ratio* `Γ = M(s=3)/M(s=2) = a_2/a_4` [poleconv-A-double, d=8: a_2 pole `(pole_in_s=3, curvature_grade_n=2)`, a_4 pole `(pole_in_s=2, curvature_grade_n=4)`; ratio degree −2(3−2) = −2 EVEN ⇒ d_A=0 parity-admissible per cross-pillar-bridge-corpus §23.0(5)]:
- `moment_a2a4_DK` (bare) = **0.254545** → best rel_dev 0.503 (vs fit)
- `moment_a2a4_BdG` (bare) = **0.417799** → best rel_dev **0.184** (vs fit) — the closest of ALL knob-free readings
- Moment-ratio bridge map MISSES (best 0.184 ≫ 0.10).

*Composite operator*: min over {moment-ratio, Connes-distance} of best knob-free rel_dev = min(0.184, 0.297) = **0.1838 ≫ 0.10** → **FAIL**. Robust under the strict D_K-only parenthetical reading too (Connes_DK 0.575, moment_DK 0.503; min 0.503).

*KNOB-LOCATION corollary (the [VERIFY] payload)*: the moment-ratio carries a hidden knob — the Pauli-Villars regulator mass `M_reg`. The physically-correct UV-regulator limit `M_reg ≥ λ_max` (ABOVE the spectrum) recovers the bare ratio (M_reg=8·λ_max → 0.2546 D_K / 0.4178 BdG; MISS — converges to bare). Only placing `M_reg` in the spectral BULK (`M_reg = M_KK = 1` in cache units, BELOW λ_max=5.42 and just above λ_min=0.82) tunes the ratio onto a target: M_reg=M_KK gives 0.5325 D_K (rel_dev 0.040 vs fit) and 0.6389 BdG (rel_dev 0.004 vs slow-roll). That in-bulk placement is the moment-ratio analog of the forbidden S95 in-band V0 sigmoid knob — EXCLUDED by the convention pin "substrate-natural scale (NON-in-band)". So the only way either bridge map reaches Γ_req is to re-introduce a fitted (in-bulk) scale; the knob-free spectral geometry does not supply it. The Connes distance has NO such knob and misses outright. This LOCATES the knob in the moment-ratio class and CONFIRMS the gate's hypothesis-negation.

*Solution-space reading*: the FAIL GENERALIZES "NOT substrate-derivable" from the INV12-W3-4 Pöschl-Teller near-horizon-barrier family (one corridor) to {Wodzicki moment-ratio, Connes-distance} = **3 construction classes total**. The exit-greybody Γ that would close the A_s over-production is NOT supplied by the substrate's own spectral geometry at any knob-free scale; it requires an irreducibly fitted filter factor (A_s = squeeze × FITTED Γ — the A2 knob stands exposed). This promotes the fitted-Γ from a one-corridor boundary toward a **structural-wall candidate** (atlas-09), consistent with S116-W1-AS-CF2 (exact finite-rate FAIL, straddles 0.512 at no substrate scale) and the S114/S115 A_s magnitude PLURALISM-PERMANENT lineage. The A_s magnitude filter leg does NOT close.

*4-tuple*: (value=composite_best_rel_dev=0.1838, scheme=ALT-GREYBODY-MOMENT-RATIO-AND-CONNES-DISTANCE, convention=dA0-even-morphism-parity-admissible-substrate-natural-NONinband, L_max=12). Dual-SHA (full 64): `audit_sha256=649ce24486c60645fa7616284620bd7f742dc1940aa618c585e577cef4d66b25`, `content_sha256=308fbf259e332e05fe5c6e937356c25d0c0ca5459582bfa898fcf826a02f6dd9`. Regulator pin: `a_n^{Pauli-Villars}` + Wodzicki `Res_W(s)`, poleconv-A-double (per `regulator-pin-discipline.md`). NO [SIGN] 3-tuple ([VERIFY] trigger). **Canonical-drift note** (substrate-first §ii.B): plan-pinned `canonical_constants` SHA `8c850fd9…` → runtime `d884a2b5…` (concurrent W0-1 `rho_s_C2`=7.962 append, UNRELATED to consumed values; verified A_s_FW/A_s_CMB/M_KK/kappa_exit/Delta_BCS/tau_fold UNCHANGED); the `audit_sha256` reflects the true runtime canonical; verdict unaffected. **GPU deviation**: bridge maps are vector reductions on cached eigenvalues (no ≥100×100 diagonalization), so the plan's conditional `torch.linalg` path was NOT triggered; cpu-cap-OMP8 is correct (honest disclosure per v3-closure-recovery Class-1 boundary).

**Substrate framing (phononic)**: The exit-greybody Γ IS the substrate's own transmission of the squeezed GGE-relic power through the post-fold a_4 condensation-energy barrier at the acoustic white-hole exit horizon — `D_K` eigenvalues → BdG quasiparticle dispersion ω_k → transmission Γ. Both bridge maps read Γ off the substrate's intrinsic spectral geometry (the Wodzicki residue ratio of `D_K`'s own zeta-poles; the Connes inverse spectral diameter), NOT from a barrier placed IN a container. The substrate does not hand back any of {0.137, 0.512, 0.637} from a knob-free reading of that geometry; the only reach requires re-inserting a fitted scale (the PV regulator mass in the spectral bulk = the V0 in-band placement). The substrate IS the over-production; the attenuation that would reconcile it with Planck is not substrate-IS in these two construction classes.

---

## Wave 1 Synthesis (team-lead)

All four Wave-1 gates closed; the **Q23 A_s-magnitude rate-limiter does NOT close this session** — and the *shape* of why is the wave's durable output.

**The GS-1 → 1-1 adjudication.** GS-1 (1-2) returned **INFO-RESIDUAL-PREFACTOR**: the two normalization scales (ℓ_occ = ξ_KZ = 0.01876 UV vs ℓ_horizon = c_s/(aH)|_exit IR) are separated by Δ_scale = 0.5325 OOM, which under the deg=+2 transport would over-produce a 1.065-OOM A_s fork, but the realized fork is only 0.668 OOM. Neither branch fired (not CONVENTION-BLOCKED Δ≤0.05, not PHYSICS-SCALE-SEPARATION |2Δ−0.668|≤0.1). Per its pre-registered rubric, GS-1=INFO ⇒ 1-1 collapsed to **composite FAIL** (sign=PASS over-production robust, magnitude=FAIL fork stands, regime=VALID frozen-superhorizon). The A_s over-production is real and sign-robust unconditionally (Γ≤1, both members >0); only the magnitude is a plurality.

### (a) Numerical revisions
- A_s magnitude fork → **3-member plurality**: +0.196 OOM (H̃/TD-ζ grid, A_s=3.299e-9), +0.384 OOM (Route-B-PW GGE-modular, A_s=5.081e-9), +0.864 OOM (ξ_KZ/box-delta, A_s=1.537e-8). Gap +0.196↔+0.864 = 0.668 OOM = 2·log₁₀(2.158) Sage-exact, ≈410σ in Planck units.
- GS-1 Δ_scale = 0.5325 (c_Gold) / 0.2568 (c_BLV); required c_s window for PHYSICS-SCALE-SEPARATION = **[0.516, 0.650]** M_KK (center 0.579), straddled by c_BLV=0.485 (below) and c_Gold=0.915 (above).
- 1-1 MS-Radau: de-Sitter ν²=2.0000 exact; |ζ|² exit/frozen = 1.9997 (de-Sitter freezing signature); intra-grid Parker 𝒩-spread = 0.0170 OOM ≤ 0.1 — but GRID-INDEPENDENT ⇒ does NOT adjudicate the fork (the S-1 audit's structural point, confirmed by direct propagation).
- 1-4 ALT-GREYBODY: knob-free best rel_dev = 0.184 (Wodzicki a₂/a₄ BdG moment-ratio) / 0.297 (Connes BdG) — both ≫ 0.10; only an in-bulk PV regulator mass (the forbidden V0-in-band analog) reaches a target.

### (b) Structural changes
- **A_s magnitude is functional-selection-dependent, not a single value** (epistemic-TYPE change): three independent assembly routes (impulse box-delta, TD/ζ five-factor, Route-B Peter-Weyl) land on three distinct magnitudes. The s114-as-functional-selection PLURALISM-PERMANENT lineage is confirmed — not a convergence-pending number.
- **Exit-greybody "NOT substrate-derivable" generalizes from 1 corridor to 3 construction classes** (1-4): {Pöschl-Teller near-horizon (INV12-W3-4), Wodzicki moment-ratio, Connes-distance}. The fitted-Γ filter is promoted from a one-corridor boundary toward a **structural-wall candidate** — the substrate's knob-free spectral geometry does not supply the attenuation that would reconcile the over-production with Planck.

### Wave 1 → Wave 2 decision point
Per plan: GS-1=INFO-RESIDUAL-PREFACTOR → 1-1 FAIL (fork stands) → the Q23 rate-limiter stays OPEN; A_s magnitude is a 3-member plurality. This does NOT block any Wave-2+ gate (the A_s magnitude is not a numerical input to W2's seesaw/mixing gates). The α_s(primordial)~0 tilt falsifier (W0-2) stands INDEPENDENT of this magnitude fork (𝒩-fork-independent by the multiplicative-normalization log-derivative annihilation).

## Carry-Forward Computations

### CF-S118-AS-CS-SUBSTRATE-FIRST — substrate-first curvature-channel sound speed vs the GS-1 fork-carrying window

| Field | Spec |
|:------|:-----|
| **What** | Compute the a₂/curvature-channel (hydrodynamic IR) sound speed c_s from substrate first principles (the spectral-action a₂ first-sound/second-sound ratio at the post-fold GGE state) and test whether it lands in the GS-1 fork-carrying window [0.516, 0.650] M_KK. PASS ⇒ GS-1 PHYSICS-SCALE-SEPARATION fires ⇒ the A_s fork resolves to the acoustic-horizon (H̃, +0.196) grid, closing Q23 to a zero-parameter magnitude. FAIL ⇒ residual non-scale prefactor confirmed. |
| **Inputs** | s84 L12 spectrum cache; the a₂ Seeley-DeWitt coefficient (G_ττ sector); c_Gold=0.915, c_BLV=0.485 (canonical); the GS-1 window [0.516,0.650] (this wave, `s117_gs1_grid_selection.npz`); ξ_KZ=0.01876; (aH)|_exit=14.311 (s77). |
| **Gate** | PASS iff substrate-first c_s ∈ [0.516, 0.650] (⇒ |2·Δ_scale − 0.668| ≤ 0.1); FAIL ⇒ route to CF-S118-AS-PREFACTOR-SOURCE (identify the greybody knob / c_sub Mellin-weight / F_amp backreaction co-carrying the 0.40-OOM shortfall). |
| **Effort** | ~1 wave (one a₂-channel sound-speed evaluation on the L12 cache + the GS-1 window comparison). |

The A_s magnitude PLURALISM (3 functional-selection-dependent members) is the standing Q23 / s114-as-functional-selection program; CF-S118-AS-CS-SUBSTRATE-FIRST is its highest-leverage next step because the GS-1 window pinpoints exactly what an in-band substrate c_s must satisfy to collapse the fork.

### Investigator-surfaced carry-forwards (S117 `/rclab-investigate` consolidation; append-only)

Two NEW items first-surfaced by the `/rclab-investigate` pass, distinct from the wave-close physics CF above and absent from `session-117-housekeeping.md`. (The conditional `CF-S118-AS-PREFACTOR-SOURCE` is NOT lifted as a standalone block — it is already captured as a FAIL-branch pointer inside `CF-S118-AS-CS-SUBSTRATE-FIRST`'s Gate field; the S118 planner picks it up if the primary CF FAILs.)

#### CF-W1-1 — ALT-GREYBODY structural-wall upgrade (Q-other — forward compute)

| Field | Spec |
|:------|:-----|
| **What** | Upgrade the atlas-09 exit-greybody "structural-wall candidate" (1-4 `CF-S117-ALT-GREYBODY` FAIL; 3 knob-free construction classes failed — Pöschl-Teller, Wodzicki-PV moment-ratio Γ=a₂/a₄, Connes-distance) toward an actual structural wall OR falsify it. Two routes: (a) test a 4th knob-free substrate-IS greybody bridge map — e.g. a full BdG S-matrix transmission coefficient on the exit-horizon sector, distinct from the three failed classes; OR (b) attempt a structural no-go derivation that the substrate's knob-free spectral geometry cannot supply a sub-unity Γ at any physical (M_reg ≥ λ_max) scale. |
| **Inputs** | `s117_alt_greybody.py` machinery (1-4, audit `649ce244`); the 3 failed construction classes + targets {0.137 box-delta, 0.637 slow-roll, 0.512 fit}; the KNOB-LOCATION corollary (moment-ratio reaches a target only with M_reg in the spectral BULK — the forbidden S95 in-band-knob analog); exit-horizon BdG sector spectrum (L12/L14 caches); INV12-W3-4 Pöschl-Teller corridor. |
| **Gate** | Route (a): a 4th-class knob-free Γ within rel_dev 0.10 of a target at the physical UV limit M_reg ≥ λ_max ⇒ PASS (knob-free greybody EXISTS, candidate FALSIFIED); miss ⇒ FAIL (wall strengthened to 4 classes). Route (b): valid no-go derivation ⇒ PASS (candidate promoted to structural wall); invalid ⇒ INFO. |
| **Effort** | medium (1 agent; a new BdG S-matrix transmission compute on the exit-horizon sector OR a knob-free-impossibility no-go derivation). Surfaced by the W1 seed; NOT previously in the WP CF. |

#### CF-W1-2 — §EVOI.BF A_s-liability freshness-fold (Q2 — registry-hygiene carry-forward)

| Field | Spec |
|:------|:-----|
| **What** | Fold the S117 W1 A_s refinements into the `§EVOI.BF` A_s-liability prose, which currently references only through S114 even though the EVOI currency marker is already S117-stamped (so the staleness audit, keying on the content marker, will NOT auto-detect the lag). Fold in: the 3-member magnitude plurality {+0.196, +0.384, +0.864} OOM (full 5-route band [+0.196, +1.527]); the GS-1 c_s scale-separation window [0.516, 0.650] M_KK (straddled by c_BLV=0.485 and c_Gold=0.915); the 3-construction-class greybody-wall candidate. |
| **Inputs** | `sessions/evoi-framework.md §EVOI.BF` (prose stale through S114); the W1 seed digest (3-member plurality, GS-1 window, greybody wall); `s117_gs1_grid_selection.npz`. |
| **Gate** | Registry-freshness (artifact-existence): §EVOI.BF prose updated to reflect the S117 W1 refinements; routes via `/rclab-plan` Step 1c-REGISTERS at S118 plan-freeze. |
| **Effort** | low (prose freshness-fold; no compute). |

## Effected In-Session / routed to session-close

The W1 outcomes touch the falsifier surface (mack-cosmic-bridge sole writer) and a capstone-governing register (atlas-09 wall/retraction log). Routed to the **session-close capstone-hygiene pass** → `session-117-housekeeping.md`:
- falsifier-master-inventory A_s leg: Q23 NOT closed S117; A_s magnitude = 3-member plurality {+0.196, +0.384, +0.864}; exit-greybody fitted-Γ now a 3-construction-class "NOT substrate-derivable" generalization (structural-wall CANDIDATE). (mack)
- atlas-08 Q23 / atlas-09: record the fitted-Γ structural-wall candidate + the 3-member A_s plurality; reconcile against the register (Q3 capstone-hygiene).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | Q23 A_s magnitude (1-1/1-2/1-3) | 2-member fork {+0.196,+0.864}, GS-1 to adjudicate | OPEN; 3-member plurality {+0.196,+0.384,+0.864}; GS-1=INFO-RESIDUAL-PREFACTOR (c_s window [0.516,0.650] straddled) | 1-1 FAIL, 1-2 INFO, 1-3 INFO |
| 2026-06-28 | exit-greybody fitted-Γ (1-4) | 1-corridor "NOT substrate-derivable" (INV12-W3-4) | 3-construction-class generalization; structural-wall CANDIDATE | 1-4 FAIL (Wodzicki + Connes both miss knob-free) |
| 2026-06-28 | A_s over-production SIGN | sign-robust (prior) | sign-robust CONFIRMED unconditionally (both fork members >0, Γ≤1) | 1-1 sign_verdict PASS |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict | 
|:-----|:-------|:------------|:------------|:--------|
| 1-1 | `s117_t_fold_exit_normalization.py` | `.npz` | `.png` (4-panel) | FAIL (+[SIGN] 3-tuple) |
| 1-2 | `s117_gs1_grid_selection.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple) |
| 1-3 | `s117_route_b_pw_socc.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple) |
| 1-4 | `s117_alt_greybody.py` | `.npz` | `.png` | FAIL ([VERIFY], no 3-tuple) |
