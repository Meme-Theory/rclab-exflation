# Session 100a Wave W3 — Freeze-in / Envelope Dynamics (Results Working Paper)

**Session**: 100 | **Wave**: W3 | **Plan**: session-100a-plan-w3.md | **Theme**: Is the S99 transit squeezed-vacuum freeze-in an over-constrained predictor of the SM flavor sector — flavor SHAPE from `exp(−S₀·C₂)` on the triality-distinct Casimir grading, envelope over-determination via the sonic greybody filter, and threshold-fixing of the envelope magnitude.

## Gate Sections

### §W3-9. S100a-FREEZEIN-OVERCONSTRAINED (transit-dynamics-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-FREEZEIN-OVERCONSTRAINED`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (diabatic freeze-in over-constraint on the SM flavor sector)
**Agent**: `transit-dynamics-theorist`
**Hypothesis**: Fitting `{S₀, |w|}` to the three charged-lepton masses and `arg(w)` to one CKM datum (3 real inputs) predicts the six quark mass ratios, three CKM angles, and J_CP (~12 held-out PDG observables) with no further freedom — PASS = flavor SHAPE is a substrate prediction; FAIL = the over-constraint breaks, closing the dynamical-freeze-in corridor cleanly.
**Plan reference**: `sessions/session-plan/session-100a-plan-w3.md` §W3-9 (machinery pin, dual-track thresholds, substitution chain, dual-prior).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `search_knowledge("freeze-in overconstrained flavor CKM quark mass ratio")` | NOT pre-closed. Surfaced the S99 panel equation `V_CKM = U_up† U_down`, `U_sector` = eigenbasis of the frozen block `[[d,w],[w*,d]]^sector` (session-99-fermion-mass-transit.md §3-B) — the structure this gate executes. S96-MATTER-PMNS-3X3 INFO pins the ascending-mass flavor-basis convention. |
| `search_knowledge("S98 yukawa eps_LX between generation multiplicity")` | S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN PASS (NCG-INNER-FLUCT-EXTERNAL-NONLI, convention `EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE` — inherited here); S97-YUKAWA-FAMILY-DERIVE FAIL (`1:1:1` democratic, the wall this gate's dynamical route attacks); `m_e` pinned at S98 with PDG-pole-scale note. |
| `trace_entity("freeze-in Casimir grading")` | No prior trace — gate not previously evaluated. |
| `list_constants("m_e\|m_mu\|m_tau\|V_us\|CKM\|quark")` + `get_constant("m_tau")` + `get_constant("m_mu")` | **Name-collision catch**: canonical `m_tau = 2.062` is the S42 MODULUS mass (M_KK units), NOT the tau lepton; the designated PDG anchor is `m_tau_PDG = 1.77686` (S100a pin, provenance note explicit). `m_mu = 0.1056583745`, `m_e = 5.10998950e-4` canonical. Quark masses + CKM data absent → added 11 PDG 2024 anchors with provenance BEFORE the run (`m_u/d/s_msbar_2GeV`, `m_c_msbar_mc`, `m_c_pole`, `m_b_msbar_mb`, `V_us_PDG`, `V_us_sigma_PDG`, `V_ub_PDG`, `V_cb_PDG`, `J_CP_PDG`). |
| `list_constants("P_exc\|R_therm\|C2")` | `P_exc_kz = 1.0`, `R_therm = 5251.82` (S95) — the diabatic-regime witnesses; C₂ not a stored constant (representation-theoretic, computed in-script from `C2(p,q) = (p²+q²+pq+3p+3q)/3`). |

**Verdict**: **FAIL** — the over-constraint breaks; the dynamical-freeze-in corridor for the SM flavor SHAPE is **closed cleanly** (Track B, posterior 0.90 per the plan dual-prior discriminator). Schema-v2 3-tuple: `sign_verdict=PASS` (hierarchy direction correct: `m_t/m_u_pred = 3473 ≫ 1` with the C₂-ordered sign), `magnitude_verdict=FAIL` (neither the mass group 2/6 nor the mixing group 0/4 all-passes), `regime_verdict=VALID` (lepton fit converged to max|res| = 2.2e-16 ≪ 1e-10 plan tolerance, fitted parameters strictly inside the scan domains, diabatic witnesses `P_exc_kz = 1.000`, `R_therm = 5251.82 ≫ 1`, `δt/T_L = 1.25e-5 ≪ 1`). Composite per the pre-registered gate-verdicts.md collapse rule: `magnitude FAIL ∧ regime VALID → FAIL`. Gross misses in **all three** observable classes (ratio > 1 OOM, angle > 3σ, J > 1 OOM from PDG central) — the dual-prior FAIL discriminator fires unambiguously.

**Results**:

*Canonical structure (declared before compute; script docstring D1–D5).* The 3×3 Hermitian freeze-in block assembles the plan's 2×2 pairing blocks `[[d_i, w],[w*, d_j]]` over all three generation pairings with ONE shared complex `w`; diagonal `d_i = exp(−S₀·C₂_i)` on the plan-pinned triality tower (1,0)/(1,1)/(3,0), `C₂ = (4/3, 3, 6)` (SU(3) quadratic Casimir, analytic). Generation map (D2): mass ASCENDS as C₂ DESCENDS — gen1 ↔ (3,0) C₂=6 (deepest freeze = lightest), gen2 ↔ (1,1) C₂=3, gen3 ↔ (1,0) C₂=4/3 — the plan Step-5 "C₂-ordered sign", independently confirmed by the W2 Item-6 npz `e_sector=(3,0)` and by the diagonal log-gap ratio `(6−3)/(3−4/3) = 9/5 = 1.800` vs observed `ln(m_μ/m_e)/ln(m_τ/m_μ) = 1.889`. Tower phases from the W2 Z₃ triple {π, +2π/3, −2π/3} (D3): leptons at the unique self-conjugate point (`w_ℓ = −|w|`, real — REQUIRED by the plan's 2+1 split fit protocol, which needs phase-free lepton masses), up/down quark towers at mutually conjugate phases `w_u = |w|e^{+iΘ}`, `w_d = w_u*` (BDI J-conjugacy (p,q)↔(q,p)). `Λ_u = Λ_d` J-locked (D4) — the same-generation ratios are absolute SHAPE predictions. Canonical root = smallest-|w| diagonal-dominant branch (D5).

*Fit stage (3 real inputs, exact root at machine ε):*

| Fitted | Value | Note |
|:-------|:------|:-----|
| `S0_fit` | **1.694153** (pub. 4 s.f.: 1.694) | in scan [1.0, 6.0]; diag-limit legs S₀(μ/e) = 1.7772, S₀(τ/μ) = 1.6934 — the 5% leg spread is exactly closed by the off-diagonal |
| `w_abs_fit` | **2.215474e-04** (pub. 4 s.f.: 2.215e-4) | 2 roots found; canonical = smaller-\|w\| branch (D5); second root S₀=1.6992, \|w\|=6.20e-4 |
| `arg_w_fit` | **+1.570918 rad** (≈ π/2) | the \|V_us\| **maximizer**, NOT the anchor: max reachable \|V_us\| = **0.0717** vs PDG 0.22500 ± 0.00067 — the anchor is UNREACHABLE by a 3.14× shortfall; the Stage-B fit converges to the boundary of the achievable set (model shortfall = magnitude failure, not a regime failure) |

Lepton-fit residual max|res| = 2.22e-16 (plan tolerance 1e-10); targets `m_μ/m_e = 206.7683`, `m_τ/m_μ = 16.8170` from canonical `m_mu`, `m_e`, `m_tau_PDG`.

*Predict stage — the 12-slot held-out vector (slots 0–1 fit diagnostics, slot 2 anchor):*

| # | Observable | Predicted | PDG 2024 | Deviation | Band | Pass |
|:--|:-----------|:----------|:---------|:----------|:-----|:-----|
| 0 | m_μ/m_e (fit) | 206.768 | 206.768 | 0.0000 dex | 0.5 dex | ✓ |
| 1 | m_τ/m_μ (fit) | 16.817 | 16.817 | 0.0000 dex | 0.5 dex | ✓ |
| 2 | θ₁₂ (anchor) | 4.110° | 13.003° | 8.89° = **68.4σ** | 0.13° | ✗ gross |
| 3 | m_u/m_d | 1.000 | 0.4596 | 0.338 dex | 0.5 dex | ✓ |
| 4 | m_c/m_s | 1.000 | 13.615 | **1.134 dex** | 0.5 dex | ✗ gross |
| 5 | m_t/m_b | 1.000 | 41.284 | **1.616 dex** | 0.5 dex | ✗ gross |
| 6 | m_c/m_u | 206.54 | 589.35 | 0.455 dex | 0.5 dex | ✓ |
| 7 | m_s/m_d | 206.54 | 19.894 | **1.016 dex** | 0.5 dex | ✗ gross |
| 8 | m_t/m_c | 16.817 | 135.66 | 0.907 dex | 0.5 dex | ✗ |
| 9 | θ₁₃ | 0.2431° | 0.2189° | 0.0243° = 1.87σ | 0.013° | ✗ (near-hit) |
| 10 | θ₂₃ | 0.2583° | 2.3383° | 2.08° = 5.2σ | 0.4° | ✗ gross |
| 11 | J_CP | ±1.368e-6 | 3.08e-5 | 1.35 dex below | [2e-5, 4e-5] | ✗ gross |

`per_obs_pass = [T,T,F,T,F,F,T,F,F,F,F,F]` → 4/12 total; mass group 2/6, mixing group 0/4. 4-tuple: `(value='S0=1.6942;|w|=2.2155e-04;argw=+1.5709;…;trackB_0.90', scheme=FW, convention=EPS-LX-BETWEEN-GENERATION-MULTIPLICITY-PDG-POLE, L_max=N/A-algebraic-block)`.

*Why it fails — two structural collisions, both forced by the pre-declared structure:*
1. **The J-conjugacy that enables CKM kills the up/down mass split.** `M_d = M_u*` (the only zero-new-parameter up/down distinction) forces identical up/down spectra: up/down conjugate-spectrum identity dev = **0.0e+00 exact**. Predicted m_u/m_d = m_c/m_s = m_t/m_b = 1; PDG spans 0.46 → 41.3 (1.95 OOM). Slots 4, 5, 7 fail at > 1 OOM.
2. **The lepton-fit |w| is too small to mix.** The hierarchy-preserving root demands |w| = 2.2e-4 ≪ d₂ = e^{−3S₀} = 6.2e-3; the 1-2 mixing angle is then t ≈ |w|/(d₂−d₃) = 0.036 rad, and the conjugate-tower mismatch caps |V_us| ≤ 2t·|sinΘ| = 0.0717 < 0.225. The SAME |w| cannot both preserve the e–μ–τ hierarchy and produce Cabibbo-scale mixing — the over-constraint breaks exactly where the plan's counting (`N_fit = 3 < N_pred ≈ 12`, ~9 dof over-determined) said a wrong texture must break.

*Substitution chain (plan §W3-9 item 7, numbers substituted):* `d_i = exp(−S₀C₂_i)` ⇒ `ln(m_j/m_i) = −S₀(C₂_j − C₂_i)` ⇒ at S₀ = 1.6942: `m_t/m_u = exp(+S₀·(6 − 4/3)) = exp(+14S₀/3) = e^{7.906} = 2716` diag-limit (3473 with off-diagonal) ≫ 1 with the C₂-ordered sign ⇒ **sign_verdict = PASS**: the freeze-in predicts the correct hierarchy DIRECTION in every tower (heavier rep = larger C₂ = smaller `exp(−S₀C₂)` amplitude = lighter fermion; PDG ordering reproduced), while the magnitudes break.

*Cross-checks (all pass):* CKM unitarity max|VV†−I| = 1.0e-15; w→0 diagonal limit reproduces `exp(−S₀ΔC₂)` ratios to 2.4e-14 and V→𝟙 to 3.2e-10; J branch antisymmetry J(−Θ) = −J(+Θ) exact (the ±Θ two-valued J under the single-|V_us|-anchor protocol, analogous to the `delta_CP_PMNS_substrate` two-valued set); pole-scheme variant (c,b,t pole vs MS-bar headline) flips 1/6 ratio-band memberships (m_c/m_u crosses 0.5 dex: 0.455 → 0.554) — does NOT change the group verdicts or the composite; eigenbasis convention = ascending-mass (S96).

*Diagnostics (NOT gated):* `S0_seed = 3.2` (Track-A fit seed; the fit re-derives S₀ = 1.694 — the seed's (ε_LX-split)/(horizon κ) provenance is W3-11's question, which now consumes `S0_fit` from the npz). `seed_vs_fit_agreement = [5.43e-4, 0.5235]`: the fitted freeze-in |w| is 1843× SMALLER than the W2 static-overlap |w| = 1/√6 = 0.4082 — the squeezed-vacuum inter-sector coefficient is NOT the geometric Yukawa-overlap off-diagonal; and min|Δθ| vs the Z₃ triple = 0.5235 rad = π/6 exactly (Θ* = π/2 sits midway between the conjugate Z₃ pair). Variant V2 (lepton sign +|w|): S₀ = 1.6942, |w| = 2.224e-4 — sign-insensitive at this |w| (cubic phase term negligible). Variant V3 (nearest-neighbor-only, w₁₃ = 0): θ₁₂ = 4.11° unchanged, θ₁₃ collapses to 0.0093°, J = 5.6e-12 — strictly worse; the canonical full-pairing structure was the steelman.

*Near-hits worth recording:* θ₁₃ = 0.243° vs 0.219° (1.87σ, 11% relative — the SMALLEST CKM angle lands closest, from pure conjugate-phase mismatch); m_c/m_u = 206.5 vs 589 (0.455 dex, inside band); m_u/m_d = 1 vs 0.46 (0.34 dex, inside). The lepton-side machinery is genuinely strong: ONE S₀ with the (4/3, 3, 6) grading reproduces both lepton log-gaps to 5% before |w|, and exactly with it.

**Substrate framing** (PHONONIC): the gate asked whether the SM Yukawa matrix is the frozen-in squeezed-vacuum occupation of the supersonic fold transit — `D_K → C₂(p,q) grading → diabatic amplitude exp(−S₀C₂) → mass ratios + (off-diagonal w) → CKM + J_CP → PDG`. The answer is a clean structural NO at the mixing-magnitude layer: the deeply diabatic transit (P_exc = 1.000, R_therm = 5252) does produce a Casimir-graded, hierarchy-correct (sign-PASS) Bogoliubov production pattern, and its lepton-sector SHAPE is exact; but the single inter-sector coefficient `w` cannot simultaneously be small enough to preserve the frozen hierarchy and large enough to carry Cabibbo mixing, and the J-conjugate up/down towers are spectrum-degenerate by construction. The flavor SHAPE is NOT set by the diabatic amplitude on the Casimir grading alone — per the plan's FAIL_meaning, an alternative carrier (e.g. the geometric multiplicity-bundle distance, Item 8 lineage) must supply the up/down split and the mixing magnitude. The corridor closes as a valid informative boundary: this is the S99 panel's pre-registered falsifiable core doing its job ("there is nowhere to hide because the shape knobs are shared").

**Dual-prior routing**: FAIL with gross misses → 0.90 posterior mass to **Track B (CORRIDOR-CLOSED)** per the plan discriminator. Downstream: W3-10 and W3-11 remain dispatchable — `S0_fit = 1.694153` (+ `S0_seed`) is on the npz as their HARD input; note for W3-11: `S0_threshold = Δω/κ_SONIC ≈ 1.279` vs `S0_fit = 1.694` gives ratio_dev ≈ 0.245 (its INFO band) — the threshold-ratio reading of S₀ survives at O(1) even though the flavor corridor closes.

**Output Artifacts**:
- `computations/session-100a/s100a_freezein_overconstrained.py` (producing script; `from canonical_constants import *`; `print_verdict_payload`)
- `computations/session-100a/s100a_freezein_overconstrained.npz` (87 keys; REQUIRED keys verified on disk: `S0_fit`, `w_abs_fit`, `arg_w_fit`, `quark_ratio_pred[6]`, `ckm_angle_pred[3]`, `J_CP_pred`, `per_obs_pass[12]`, `S0_seed`, `seed_vs_fit_agreement`)
- `computations/session-100a/s100a_freezein_overconstrained.png` (4-panel: ratio scatter vs ±0.5 dex band; per-observable deviation/band bars; |V_us|(θ) reachability sweep with PDG anchor; summary)
- Verdict line + dual-SHA companion + schema-v2 3-tuple + 4 companion rows in `computations/session-100a/s100a_gate_verdicts.txt` (emitted via race-safe `emit_verdict`; `audit_sha256=78ee1d5677d75dc8…`, `content_sha256=99b4dbd40ed9607f…`)
- Canonical-constants additions (PDG 2024, with provenance, pre-run): `m_u_msbar_2GeV`, `m_d_msbar_2GeV`, `m_s_msbar_2GeV`, `m_c_msbar_mc`, `m_c_pole`, `m_b_msbar_mb`, `V_us_PDG`, `V_us_sigma_PDG`, `V_ub_PDG`, `V_cb_PDG`, `J_CP_PDG`

---

### §W3-10. S100a-ENVELOPE-OVERDETERMINE (hawking-theorist)

**Status**: COMPLETED
**Gate ID**: `S100a-ENVELOPE-OVERDETERMINE`
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (double-derivation of the diagonal freeze-in exponent)
**Agent**: `hawking-theorist`
**Hypothesis**: The diagonal exponent is derivable two independent ways — greybody filter at the sonic (Mach-1) surface `2π·ω/κ_SONIC` vs the Item-9 freeze-in amplitude `S₀·C₂` — and they coincide within 10% on the heavy sector pair, so one operator wears two faces (production amplitude AND greybody filter).
**Plan reference**: `sessions/session-plan/session-100a-plan-w3.md` §W3-10 (κ_SONIC Sage-exact pin, 10% gate band, Source-Reconciliation note).

**MCP Pre-Compute Audit**:

| Query | Salient return |
|:------|:---------------|
| `get_constant("T_acoustic")` | `0.112` (canonical; matches the plan's S63 pin; no PROVENANCE dict entry — value cross-confirmed against `canonical_constants.py:706`) |
| `search_knowledge("ENVELOPE-OVERDETERMINE greybody sonic kappa")` | Only plan-text equation hits (this gate's own pre-registration) + heritage machinery: S43 `s43_greybody.py` (GREYBODY-43), S95 `s95_w4_3_hawking_greybody_as.py`, S69 sonic-Penrose, and the S99 fermion-mass panel envelope equation `a_i = Γ(ω_i)e^{−2πω_i/κ}·e^{iΘ_i}`. No closure covers this gate. |
| `search_knowledge("S100a-ENVELOPE-OVERDETERMINE")` | No results — gate unevaluated. **NOT PRE-CLOSED.** |
| Sage MCP (`sage_eval`, QQ-exact) | `2·(112/1000) = 28/125` exact; `28/125·π = 0.70371675440411369` (5 sf `0.70372`); E_A coefficient `2π/κ_SONIC = 125/14` exact; `E_A(0.9) = 225/28` exact. |

**Verdict**: **INFO** — composite per the pre-registered three-band rubric (PASS iff `rel_disc ≤ 0.1` on both heavy sectors; FAIL iff > 1 OOM route divergence; INFO between). Schema-v2 3-tuple: `sign_verdict=PASS / magnitude_verdict=INFO / regime_verdict=VALID`; the collapse rule (`magnitude=INFO ⇒ composite INFO`) is self-checked by assertion in the producing script. Verdict emitted via the race-safe `emit_verdict` MCP tool: `audit_sha256=4ed74d7ee8a494ab54c64261533f09208c34d7dffe4095a71bd941bf94e591bb`, `content_sha256=2e0a3be4cdd4dace0d47265ffb25a20c0a993f9ae023de16770d31a164679910`; canonical line + dual-SHA companion + 3-tuple annotation + regulator/κ-recon/diagnostic rows all landed in `computations/session-100a/s100a_gate_verdicts.txt`.

**Results** (NUMBERS first):

| Quantity | Value | Source |
|:---------|:------|:-------|
| `kappa_SONIC_exact` | `2π·T_acoustic = 28/125·π = 0.7037167544041137 M_KK` (5 sf **0.70372**) | computed in-script from imported canonical `T_acoustic = 0.112`; Fraction-exact + Sage-QQ cross-check (< 1 ulp) |
| `S0_consumed` | `1.6941531565757249` | HARD within-wave: `s100a_freezein_overconstrained.npz` key `S0_fit` (landed — no mechanical closure needed) |
| `C₂` heavy pair | `(3, 6)` for (1,1)/(3,0) | npz `C2_vec[1:]`, asserted equal to the analytic SU(3) Casimirs |
| `E_A_per_sector` (greybody) | `[8.035714285714, 8.035714285714]` (= `225/28` exact; sector-independent — ONE pinned ω) | Route A: `2π·ω/κ_SONIC`, ω = Δω = 0.9 M_KK (ε_LX one-fiber-gap heavy-pair pin) |
| `E_B_per_sector` (freeze-in) | `[5.082459469727, 10.164918939454]` | Route B: `S₀·C₂` |
| `rel_disc_per_sector` | `[0.581068, 0.209466]` vs band `≤ 0.1` | gate operator |
| `log10(E_A/E_B)` per sector | `[+0.198951, −0.102079]` vs FAIL bound `|·| > 1` | same-OOM check |
| 4-tuple | `(value='EA=8.035714_both;EB=5.082459/10.164919;rel_disc=0.581068/0.209466;…', scheme=FW, convention=RATIO, L_max=N/A-scalar-inputs)` | script stdout |

**κ reconciliation to the 4th digit (`kappa_recon_note`, Class-8.3 + Class-(f))**: `2π·0.112 = 28/125·π = 0.7037167544041137`; correct 4-dp rounding `0.7037` (residual `1.675e-5`, log10 = −4.776). The context-header literal `0.7048` has residual `1.083e-3` (log10 = −2.965) = **64.7×** the rounding residual ⇒ `0.7048` is NOT `2π·0.112`; it is transcription drift, **rejected**. Using it would have biased E_A low by 0.154% — inside the 10% band, but a propagating publication-precision defect. One refinement to the plan-freeze note: the plan quoted the 4-dp rounding residual as `2.289e-5` (~47×); the Sage-exact residual is `1.675e-5` (~65×) — same direction, same conclusion (drift ≫ rounding), the canonical pin `28/125·π` unchanged. The script computes κ_SONIC from `2*math.pi*T_acoustic` (imported canonical) with a `Fraction`-exact assertion `2·(112/1000) == 28/125` — provenance-clean by construction, no hardcoded κ literal.

**Substitution chain ([SIGN] direction read-off, executed)**:

```
Step 1:  kappa_SONIC = 2π·T_acoustic            [T_acoustic = 0.112 M_KK, canonical S63]
         E_A(ω) = 2π·ω/kappa_SONIC              [analog-horizon transmission exponent]
         E_B    = S₀·C₂                         [Item-9 diabatic amplitude exp(−S₀C₂)]
Step 2:  kappa_SONIC = 2π·(112/1000) = 28/125·π;  E_A(ω) = (125/14)·ω
Step 3:  28/125·π = 0.7037167544041137 (5 sf 0.70372);  E_A(0.9) = 225/28 = 8.035714…
Step 4:  direction = the two faces coincide. OOM axis: |log10(E_A/E_B)| = 0.199 / 0.102,
         both ≤ 1 on the heavy pair ⇒ sign_verdict = PASS (the plan rubric declares the
         0.1 < rel_disc ≤ ~1 band "directionally confirming"). Band axis: rel_disc =
         0.581 / 0.209, both > 0.1 and ≤ ~1 ⇒ magnitude_verdict = INFO.
Step 5:  Source-Reconciliation direction honored: pin = Sage-exact 28/125·π, not 0.7048.
```

**Fiber-acoustic functional-INDEPENDENCE statement**: κ_SONIC is the surface gravity of the **fiber-acoustic** Mach-1 surface — the `v = c_BLV` sonic crossing at internal-acoustic `T_acoustic = 0.112 M_KK` — and is functional-INDEPENDENT per the lizzi pin: no Seeley-DeWitt `a_n` is cited anywhere in this gate, because an `a_n`-gradient κ would contaminate a regulator-invariant ratio (`regulator_pin = N/A` in the machinery pin map; carried as a companion row on the verdict line). The two other κ-KINDs that coexist at distinct surfaces are **EXCLUDED** by pre-registration: `κ_GH = 1.365` (= 2π·T_GH, the Gibbons-Hawking emergent-4D-horizon KIND at T_GH = 0.2172) and the a₂/a₄ thermodynamic-modulus surfaces. These are different geometric objects, not alternative values of one functional — this gate ran on the SONIC KIND only, and no alternative-κ verdict was computed (the surface choice was fixed at plan-freeze; re-running under another κ would be convention-shopping).

**Cross-checks**:

1. **Exact-rational arithmetic**: `E_A(0.9) = (125/14)·(9/10) = 225/28` asserted via `Fraction`; the float route agrees to < 1e-12. Dimensional check: `[ω]/[κ] = M_KK/M_KK` ⇒ both exponents dimensionless ✓; `S₀` and `C₂` dimensionless ✓.
2. **Limiting cases (kinematic consistency of the identification)**: κ→0 (zero-temperature limit) ⇒ E_A→∞, transmission→0 — no production at T = 0; S₀→∞ (adiabatic transit) ⇒ E_B→∞, amplitude→0 — adiabatic theorem, no freeze-in; ω→0 / C₂→0 ⇒ both exponents →0, weights →1 — zero modes unsuppressed. The two faces share ALL limiting behaviors — the identification is structurally consistent even where the magnitude is INFO.
3. **Greybody transmission cross-check (S43/S95 machinery)**: at amplitude level `exp(−E_A)/exp(−E_B) = [5.22e-2, 8.41]` — the two routes differ by ~1 OOM in transmission weight, which is exactly why the plan gates the EXPONENT (the over-determined quantity), not the amplitude; the Γ(ω) prefactor is not gated.
4. **Matching-frequency diagnostic (the INFO band's pre-registered attribution, made concrete)**: the per-sector frequency at which the two routes coincide EXACTLY is `ω*(C₂) = S₀·C₂·T_acoustic = [0.569235, 1.138471] M_KK` — the pinned scalar Δω = 0.9 sits between them (within 5.4% of their arithmetic mean 0.854). Structurally: E_A is C₂-flat under the single one-fiber-gap pin while E_B is C₂-linear, so a scalar ω cannot match a graded exponent on both heavy sectors at once; the observed straddle (`E_B(3) < E_A < E_B(6)`, pair geometric-mean ratio `E_A/√(E_B₃E_B₆) = 1.118`) is the best a scalar pin can do. The residual is therefore traceable to the **ω-offset choice** — precisely the sub-leading factor the pre-registered INFO_meaning names.
5. **`S₀·T_acoustic` vs `τ_fold`** (diagnostic, NOT gated; flagged to W3-11): `S₀·T_acoustic = 0.189745` vs `τ_fold = 0.190` — relative deviation **0.134%**. Equivalently `ω*(C₂) ≈ C₂·τ_fold·M_KK`: the per-Casimir frequency quantum of the exact-match grading is numerically the fold position itself, i.e. `S₀ ≈ 2π·τ_fold/κ_SONIC = τ_fold/T_acoustic = 1.69643` vs `S0_fit = 1.69415`. If W3-11's threshold identity lands, the double-derivation closes exactly under Casimir-graded offsets `ω_i = C₂_i·τ_fold` with zero free parameters — that is W3-11's adjudication; recorded here only as the route the INFO band's deferral points at.

**Assessment (interpretation third)**: The gate returns the pre-registered middle band, and the band's own meaning text describes the outcome accurately: the greybody-filter face and the freeze-in face agree at OOM on both heavy sectors (directionally confirming — sign PASS), while the 10% magnitude closure is deferred to the ω-offset refinement. What the numbers add beyond the rubric: the failure to close at 10% is NOT noise — it has the exact structural signature of the scalar-ω pin (C₂-flat E_A straddling C₂-linear E_B), and the graded-offset frequencies that WOULD close it exactly carry the fold position as their per-Casimir quantum to 0.134%. Substrate framing preserved: the arrow runs `D_K → fiber-acoustic horizon at Mach-1 → greybody exponent 2πω/κ_SONIC ≈ S₀·C₂ (transit freeze-in)`; the freeze-in exponent is not an ad-hoc fit parameter but (to OOM, pending the graded refinement) the substrate's own analog-horizon filter — relay patterns transmitted through the sonic surface ARE the frozen-in amplitudes, one operator photographed from the production side and from the filter side.

**Output Artifacts**:

- `computations/session-100a/s100a_envelope_overdetermine.py` — producing script (canonical imports; Fraction-exact κ assertions; collapse-rule self-check; `print_verdict_payload`)
- `computations/session-100a/s100a_envelope_overdetermine.npz` — all plan-required keys (`kappa_SONIC_exact`, `E_A_per_sector`, `E_B_per_sector`, `rel_disc_per_sector`, `S0_consumed`, `kappa_recon_note`) + diagnostics + dual SHAs
- `computations/session-100a/s100a_envelope_overdetermine.png` — two-panel: routes A/B per sector with the 10% band; matching-frequency diagnostic
- `computations/session-100a/s100a_gate_verdicts.txt` — canonical INFO line + dual-SHA companion + schema-v2 3-tuple + regulator/κ-recon/diagnostic rows (via `emit_verdict`, race-safe)

---

### §W3-11. S100a-S0-THRESHOLD-JOINT (phonon-first-cosmologist)

**Status**: COMPLETED
**Gate ID**: `S100a-S0-THRESHOLD-JOINT`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (KK-threshold fixing of the envelope magnitude)
**Agent**: `phonon-first-cosmologist`
**Hypothesis**: `S₀ = (ε_LX-split scale)/(horizon κ)` is fixed by the KK-threshold machinery (KK-THRESHOLD-64) — if so the envelope magnitude (S₀) and slope (C₂-grading) close jointly with no free normalization; if not, S₀ stays an empirical anchor (the S99 W3-2 neutrino pattern).
**Plan reference**: `sessions/session-plan/session-100a-plan-w3.md` §W3-11 (three-band PASS/INFO/FAIL ratio thresholds, KK-THRESHOLD-64 pins, substitution chain).

**MCP Pre-Compute Audit**:
- `get_constant("T_acoustic")` → 0.112 (canonical; `canonical_constants.py:706` S42/S47-S63 lineage; no separate PROVENANCE dict entry) — the κ_SONIC source.
- `get_constant("m_H_FW_KK_threshold")` → 131.8 GeV, session S100a, source "KK-THRESHOLD-64 (S64 W4-B, INFO); S28c framework prediction lineage", gate `S100a-M0-MH-INHERITANCE` — confirms the W4-13 in-session promotion; IMPORTED from `canonical_constants.py` (line 672), not pinned as a literal, per the orchestrator override.
- `search_knowledge("KK-THRESHOLD-64 delta 2.35")` → gate record S64 W4-B INFO: δ = 2.35 outside its OWN PASS band [0.73, 1.48]; m_H = 131.8 GeV — the threshold machinery the plan pins quote.
- `search_knowledge("S0 threshold joint envelope magnitude slope")` → only this session's plan-w3 equations returned; NO prior evaluation of the S₀↔threshold relation anywhere in the graph.
- `trace_entity("KK-THRESHOLD-64")` → gate record + `S100a-M0-MH-INHERITANCE` anchor equation + the plan equation; no closed mechanism covers this gate.
- **NOT PRE-CLOSED** — gate fresh; proceeded to compute.

**Verdict**: **INFO** — composite via the schema-v2 collapse rule (`sign_verdict = PASS`, `magnitude_verdict = INFO`, `regime_verdict = VALID`). `ratio_dev = 0.2451 ∈ (0.05, 0.5]`: **S₀ is threshold-CONSTRAINED to O(1) with a 1-parameter residual — NOT threshold-fixed at the 5% no-free-normalization band (PASS refuted), NOT threshold-independent (FAIL refuted).** Per the plan discriminator: track mass unchanged (Track A 0.40 / Track B 0.60); the residual normalization knob is the carry-forward.

**Results**:

*NUMBERS first (plan §W3-11 substitution chain, item 7, substituted values):*

| Step | Quantity | Value | Source |
|:-----|:---------|:------|:-------|
| 1 | `T_acoustic` | 0.112 M_KK (= 14/125 EXACT; dev 0.0e+00) | canonical import (S63) |
| 1 | `kappa_SONIC = 2π·T_acoustic` | **0.7037167544041136** M_KK | computed from canonical (provenance-clean, no literal); bit-identical to `(28/125)·π` in float64; 1 ulp (1.110e−16) from the plan's 16-digit Sage rounding `0.7037167544041137`; 5 s.f. publication `0.70372` |
| 1 | `Delta_omega` | 0.9 M_KK | plan pin (ε_LX one-fiber gap, post shape-preserving-squaring halving) |
| 1 | KK-THRESHOLD-64 context | δ = 2.35; m_H = 131.8 GeV | S64 W4-B gate record; `m_H_FW_KK_threshold` canonical import |
| 2–3 | `S0_threshold = Delta_omega/kappa_SONIC` | **1.2789236498455876** (4 s.f. **1.279**) | threshold-derived candidate, NO free normalization |
| 3 | `S0_fit_consumed` | **1.6941531565757249** | `s100a_freezein_overconstrained.npz` key `S0_fit` (consumed at runtime, never hardcoded) |
| 3 | `ratio = S0_threshold/S0_fit` | 0.7549043868209577 | — |
| 3 | **`ratio_dev`** | **0.24509561317904227** | the gate observable, `\|ratio − 1\|` |
| 5 | **`band_verdict`** | **INFO** (0.05 < 0.2451 ≤ 0.5) | pre-registered three-band, RATIO convention |

*[SIGN] direction read-off (chain Step 4):* `S0_threshold = +1.2789 > 0` — the candidate points in the SUPPRESSION direction of the envelope `exp(−S₀·C₂)`, inheriting the C₂-ordered hierarchy sign the W3-9 chain pre-registered and sign-PASSed; AND `|log10(ratio)| = 0.1221 ≤ 0.5` — same OOM, the plan's own "threshold-constrained to O(1)" vs "no threshold relation" band vocabulary operationalized on the order axis. Both legs hold → `sign_verdict = PASS`. `regime_verdict = VALID` (exact scalar arithmetic on canonical/exact inputs; no expansion window, scan, or truncation to breach).

*Magnitude-via-S₀ / slope-via-C₂ joint-closure read-off:* the envelope `exp(−S₀·C₂)` factorizes into a SLOPE leg — the Casimir grading C₂ = (4/3, 3, 6), fixed representation theory, threshold-INDEPENDENT — and a MAGNITUDE leg, S₀. The joint-closure question (the S99 panel's highest-leverage open item) was whether KK-threshold geometry fixes BOTH at once. Answer: the slope leg closes by construction; the magnitude leg does NOT close at the 5% no-free-norm band — it closes to O(1) with residual knob `S0_fit/S0_threshold = 1.324671`. Partial closure: threshold-CONSTRAINED, not threshold-FIXED.

*Cross-checks:*
- κ_SONIC Sage-exactness: `2π·0.112` bit-identical to `(28/125)·π` (float64); `T_acoustic − 14/125 = 0.0` exact; plan-literal agreement 1 ulp. The 0.7048 transcription drift the plan's Source-Reconciliation note flagged never enters (κ computed from the canonical import).
- Per-leg robustness: both W3-9 lepton diagonal legs give the SAME band — `S0(μ/e) = 1.7772` → dev 0.2804; `S0(τ/μ) = 1.6934` → dev 0.2448; both INFO. The band verdict is not an artifact of the joint-fit weighting.
- Upstream honesty: W3-9 composite FAIL (Track B 0.90 — the 12-slot over-constraint broke on quarks/CKM) BUT the charged-lepton SHAPE leg survived exactly (lepton fit residual 2.2e−16), so `S0_fit` is well-posed for this gate per the orchestrator adjudication + the plan's partial-S₀ branch ("W3-10/W3-11 run on the partial S0 with their own bands").
- Cross-gate coherence (W3-10, landed in parallel): `E_A = 2π·Δω/κ_SONIC = 8.0357 = 2π·S0_threshold` EXACTLY (same Δω, same κ — one quantity, two faces); W3-10 also returned INFO (rel_disc 0.581/0.209 on C₂ ∈ {3,6}, same OOM). Both faces of the exponent — greybody filter (W3-10) and threshold quotient (this gate) — land in the SAME band shape: O(1)-commensurate with the transit-frozen value, neither closed at its no-free-norm tolerance. The envelope's exponent family is horizon/threshold-commensurate everywhere, with O(1) residuals as the surviving free structure.

*Post-hoc diagnostics sharpening the INFO-band knob (reported, NOT gated; both flagged post-hoc):*
- (a) `knob = 1.324671` vs **C₂(1,0) = 4/3**: dev **0.65%** — reading `S0_fit ≈ C₂(1,0)·Δω/κ_SONIC`: one fundamental-Casimir quantum of normalization.
- (b) `Δω_req = S0_fit·κ_SONIC = 1.192204 M_KK` vs **δ/2 = 1.175** (the KK-THRESHOLD-64 δ HALVED — the same halving operation the Δω = 0.9 pin language cites): dev **1.46%**; equivalently `S0_alt(δ/2) = 1.669706`, `ratio_dev_alt = 0.0144` — a would-be PASS-band value had the split scale been pinned δ/2. The PRE-REGISTERED pin is 0.9; the verdict stands on it.
- Both candidates are threshold-INTERNAL quantities: even the residual knob plausibly lives INSIDE the KK-threshold machinery (a Casimir quantum, or a δ-halving split-scale identification), not outside it. That is what makes the INFO reading "1-parameter residual, partial closure" rather than "unrelated scales" — and it gives the carry-forward a sharp discriminating form.

*4-tuple:* `(value='S0_thr=1.279;S0_fit=1.6942;ratio=0.7549;ratio_dev=0.2451_band(0.05,0.5]=INFO;Dw=0.9;kappa=28/125pi=0.70372;knob=1.3247_vs_4/3_dev0.65%;Dw_req=1.1922_vs_delta/2=1.175_dev1.46%;legs_dev=(0.2804,0.2448);upstream_W3-9=FAIL_shape-leg-survived', scheme=FW, convention=RATIO, L_max=N/A)`

**Substrate framing** (GEOMETRIC): the arrow runs `D_K KK-threshold geometry → ε_LX-split scale Δω + sonic-horizon surface gravity κ_SONIC = 2π·T_acoustic → candidate S₀ = Δω/κ_SONIC` vs the transit-frozen `S0_fit`. The fiber gap and the Mach-1 surface gravity are both intrinsic spectral-triple structures — the gate asked whether their ratio IS the envelope magnitude. The substrate's answer: the two scales are commensurate to 25% (same O(1) neighborhood, correct suppression direction), with exactly one residual quantum of normalization unaccounted. The substrate fixes the envelope slope exactly (representation theory) and the magnitude to O(1) (threshold geometry) — the flavor-envelope scale is NOT a free Yukawa-sector dial, but it is not yet a zero-parameter prediction either. This mirrors the S99 W3-2 neutrino pattern at weakened strength: there the Dirac-scale normalization was structurally irreducible; here the residual is O(1), threshold-internal-shaped, and carries two concrete candidate closures.

**Dual-prior routing**: INFO (0.05 < 0.2451 ≤ 0.5) → mass UNCHANGED per the plan discriminator (Track A 0.40 THRESHOLD-FIXED / Track B 0.60 EMPIRICAL-ANCHOR). The threshold pins S₀ to the right order with a single residual normalization knob; the knob is the carry-forward.

**Output Artifacts**:
- `computations/session-100a/s100a_s0_threshold_joint.py` — producing script (`from canonical_constants import *`; `print_verdict_payload`; dual-SHA S84+)
- `computations/session-100a/s100a_s0_threshold_joint.npz` — data (REQUIRED keys verified on disk: `S0_threshold`, `S0_fit_consumed`, `ratio_dev`, `Delta_omega`, `kappa_SONIC`, `band_verdict`; plus chain cross-checks, per-leg devs, knob diagnostics, [SIGN] 3-tuple, dual SHAs)
- `computations/session-100a/s100a_s0_threshold_joint.png` — two-panel plot (S₀ comparison with legs + diagnostics; three-band ratio_dev axis with GATE marker)
- Verdict line + dual-SHA companion + schema-v2 3-tuple + 3 companion rows (regulator_pin N/A, diagnostics, upstream-honesty) in `computations/session-100a/s100a_gate_verdicts.txt` via race-safe `emit_verdict` (`audit_sha256=eeb7e5bd8d30938b…`, `content_sha256=1f768ff61140ec42…`)

**Carry-Forward Computations** (4-field; the plan's INFO discriminator names the residual knob as the carry-forward):
- **What**: discriminate the two threshold-internal knob identifications — (a) `S₀ = C₂(1,0)·Δω/κ_SONIC` (knob = 4/3 exactly; dev today 0.65%) vs (b) `Δω = δ/2` (split scale = halved KK-THRESHOLD-64 δ; dev today 1.46%) — by deriving the ε_LX one-fiber gap Δω from first principles (the provenance of the 0.9 M_KK pin) instead of pinning it.
- **Inputs**: `s100a_freezein_overconstrained.npz` (`S0_fit`), canonical `T_acoustic` (κ_SONIC), KK-THRESHOLD-64 δ = 2.35, the ε_LX spectral-split computation behind the 0.9 M_KK seed (W2/S98 ε_LX-on-multiplicity lineage).
- **Gate**: pre-register `|S0_pred/S0_fit − 1| ≤ 0.01` satisfied by exactly ONE of (a)/(b); both-pass or both-fail → knob unresolved, residual stays empirical (FAIL-shaped boundary, informative).
- **Effort**: 2–3 hours, 1 agent session.

---

## Wave 3 Synthesis (team-lead)

**Date**: 2026-06-06. **Gates**: 3 (1 FAIL, 2 INFO), executed per the within-wave HARD ordering 9 → {10 ∥ 11} (orchestrator verified `S0_fit` on the W3-9 npz before dispatching 10/11). All three `[SIGN]` gates carry canonical verdict lines with full 64-char dual-SHA closures + schema-v2 3-tuples; sig_5 uniqueness holds.

### 1. The over-constraint breaks for NAMED structural reasons — and the SHAPE leg survives (W3-9)

**W3-9 (FAIL, Track B 0.90 — CORRIDOR-CLOSED)**: the 3-input freeze-in fit ({S₀, |w|} to the charged leptons, arg(w) to |V_us|) does NOT predict the ~12 held-out flavor observables (4/12 pass; mixing group 0/4). The break is structural, not numerical, and both causes are forced by the pre-declared zero-freedom structure: **(1)** the BDI J-conjugacy that enables CKM at all (`M_d = M_u*`) makes up/down spectra exactly degenerate — same-generation ratios pinned at 1 against a PDG span of 0.46–41.3; **(2)** the hierarchy-preserving |w| = 2.215e-4 caps |V_us| ≤ 2|w|/(d₂−d₃) = 0.072 — one inter-sector coefficient cannot both preserve the frozen hierarchy and carry Cabibbo mixing. The fit itself is machine-clean (max|res| = 2.2e-16) and the SHAPE leg is the surviving strength: **ONE S₀ = 1.694153 on the C₂ = (4/3, 3, 6) grading carries the full charged-lepton shape exactly** (5% leg spread closed by the off-diagonal), and θ₁₃ lands within 1.87σ. The seed-vs-fit diagnostic confirms the dynamical |w| is NOT the static overlap (1843× below W2-2's 1/√6) — the fit and the geometry see different objects, consistent with the W2→W3 INFO-row regime (|w| fit-output-only).

### 2. The exponent's two faces straddle — and leave a fingerprint (W3-10)

**W3-10 (INFO, directionally confirming)**: greybody `2πω/κ_SONIC` (C₂-FLAT, E_A = 225/28 = 8.0357 exact) vs freeze-in `S₀·C₂` (C₂-LINEAR, E_B = 5.08/10.16) — a scalar ω structurally cannot match a graded exponent on both sectors; observed straddle E_B(3) < E_A < E_B(6), rel_disc [0.581, 0.209] in the pre-registered INFO band. Exact per-sector closure requires Casimir-graded offsets ω*(C₂) = S₀·C₂·T_acoustic — and the per-Casimir quantum **S₀·T_acoustic = 0.18975 = τ_fold to 0.134%** (flagged, not gated). κ_SONIC provenance-clean (28/125·π from the canonical import; the 0.7048 context-header value confirmed as transcription drift at 65× the rounding residual).

### 3. S₀ is threshold-CONSTRAINED, not threshold-FIXED (W3-11)

**W3-11 (INFO)**: S0_threshold = Δω/κ_SONIC = 1.2789 vs S0_fit = 1.6942 → ratio_dev = 0.2451 in the INFO band (0.05, 0.5]. The magnitude leg closes to O(1) with a residual knob S0_fit/S0_threshold = **1.3247**, sharpened post-hoc to two threshold-INTERNAL candidates: knob = C₂(1,0) = 4/3 (dev 0.65%) or Δω = δ/2 (dev 1.46%). Cross-gate identity: W3-10's E_A = 2π·S0_threshold EXACTLY — the two faces of the exponent are the same number read through 2π, both landing INFO, O(1)-commensurate with the transit-frozen value.

### 4. Composite picture + decision-table application

The wave maps the freeze-in corridor's exact boundary: the diabatic transit CAN freeze in the charged-lepton SHAPE (one parameter, exact) and its magnitude is KK-threshold-commensurate to O(1) with a 4/3-flavored residual — but it CANNOT carry the full quark/CKM sector through the BDI-degenerate, single-|w| structure. The plan's FAIL row anticipated closure-on-unlanded-S₀; the actual FAIL **landed** S₀ (fit converged; the over-constraint broke on held-outs), so W3-10/11 ran per the existence-condition ("Items 10 and 11 are mutually independent once S₀ exists") — the coherent reading of the decision table, applied and documented. Per the FAIL row's downstream consequence: **the flavor SHAPE alternative (W2-4 Connes multiplicity-bundle route, itself envelope-resolving this session) vs the freeze-in route is a genuine Q1 workshop seed** — two structurally different machines both produce the charged-lepton envelope; their relationship (same substrate object in two guises, or competing mechanisms?) is an adversarial adjudication for `/rclab-investigate`.

### 5. Wave classification

**Corridor-closing with surviving-structure extraction.** One FAIL with both walls named (BDI degeneracy; |w| ceiling), two INFOs that convert "is it fixed?" into "the residual is one of two (now three — see CF) sharp candidates," plus an unplanned cross-gate fingerprint (S₀·T_acoustic ≈ τ_fold) that makes the magnitude question concretely decidable next session.

### Effected In-Session (NON-MATH — team-lead orchestrator)

- [x] 11 PDG-2024 flavor anchors promoted to `canonical_constants.py` with PROVENANCE (m_u/d/s_msbar_2GeV, m_c_msbar_mc, m_c_pole, m_b_msbar_mb, V_us_PDG, V_us_sigma_PDG, V_ub_PDG, V_cb_PDG, J_CP_PDG) — effected in-gate by W3-9 pre-run; orchestrator import-verified — `computations/_shared/canonical_constants.py` SECTION E — `78ee1d5677d75dc8`
- [x] Housekeeping ledger §A row A7 recorded — `sessions/session-100a/session-100a-housekeeping.md §A`
- [x] Freeze-in-vs-Connes-route Q1 workshop seed recorded for `/rclab-investigate` (this synthesis §4 + W3-9 §"Assessment"; per the plan's pre-registered FAIL-row routing) — NOT a CF, NOT housekeeping (genuine math/physics adjudication per `Investigating-Workshops.md` §Q1)
- [x] Orchestrator-direct presentation patches: none required (all three sections landed complete; the W3-11 agent's mtime race with W3-10 self-resolved; zero must_contain misses)

## Carry-Forward Computations

### CF-S101-W3-S0-KNOB — discriminate the S₀ residual-knob candidate (the magnitude-closure decisive gate)

1. **What**: Derive the ε_LX one-fiber gap Δω from first principles and discriminate the S₀ residual knob among THREE pre-registered candidates: (i) knob = C₂(1,0) = 4/3 (Casimir quantum; dev 0.65% post-hoc), (ii) Δω = δ/2 = 1.175 (halved KK-THRESHOLD-64 split; dev 1.46%), (iii) S₀ = τ_fold/T_acoustic = 1.69643 (the W3-10 per-Casimir-quantum fingerprint S₀·T_acoustic = τ_fold; dev 0.13% post-hoc — numerically strongest). Exactly-one-candidate inside the gate band = the knob identified; zero or multiple = magnitude stays empirical.
2. **Inputs**: `computations/session-100a/s100a_freezein_overconstrained.npz` (S0_fit; audit `78ee1d5677d75dc8`); `computations/session-100a/s100a_s0_threshold_joint.npz` (threshold machinery; audit `eeb7e5bd8d30938b`); `computations/session-100a/s100a_envelope_overdetermine.npz` (graded-offset ω*(C₂); audit `4ed74d7ee8a494ab`); canonical T_acoustic, tau_fold, m_H_FW_KK_threshold, KK-THRESHOLD-64 δ = 2.35.
3. **Gate**: `S101-W3-S0-KNOB` — PASS iff EXACTLY ONE candidate satisfies |S0_pred/S0_fit − 1| ≤ 0.01 (with the first-principles Δω derivation, not the post-hoc comparison); INFO iff ≥2 candidates inside 0.01 (degenerate — needs a second observable); FAIL iff none inside 0.05.
4. **Effort**: ~0.5 wave-equivalents.

> **Addendum (2026-06-07, `/rclab-investigate` consolidation)**: one register-level Q2 item below surfaced FIRST at investigation (`workshops/_seed-w3.md`; the wave synthesis fixed all in-wave hygiene but did not sweep the guiding-star register that quotes the wave's inputs). The freeze-in-vs-Connes carrier adjudication routed per the plan's FAIL-row is scheduled as `session-100a-workshop-schedule.md` W-3; its sub-question (d) feeds CF-S101-W3-S0-KNOB above (does not replace it).

> **Rider (2026-06-07, W-3 carrier workshop R2-B Effected item 5, routed via orchestrator)**: the knob gate's "derive Δω from first principles" compute IS Leg C of S101-ENVELOPE-CARRIER-DISCRIMINATE (W-3 workshop; FEEDS, does not replace); its exactly-one-candidate-inside-0.01 criterion runs DOWNSTREAM of Leg C's graded-vs-scalar output-form binary, now armed against the (i)/(iii) 0.52% shadow degeneracy (2π·τ_fold ≈ 1.2).

### CF-W3-1 — EVOI rank-9b row re-stamp: κ_SONIC drift + post-W3 status [Q2-hygiene — registry-hygiene compute carry-forward; executes at the S101 plan-time EVOI re-stamp]

1. **What**: At the S101 `/rclab-plan` Step 1c-REGISTERS re-stamp of `sessions/evoi-framework.md`, replace the drifted κ_SONIC literal `0.7048 M_KK` in the §2 rank-9b row with the canonical Sage-exact pin `28/125·π = 0.70372` (the W3-10 Class-8.3 reconciliation formally REJECTED the drifted literal: residual 1.083e-3 = 64.7× the 4-dp rounding residual 1.675e-5) AND update the row's pre-execution status text ("ACTIVE — S100a W2+W3+W4") to the post-W3 state: dynamical freeze-in corridor CLOSED (S100a-FREEZEIN-OVERCONSTRAINED FAIL, two named walls), CF-S101-W3-S0-KNOB successor ACTIVE — so the drift is not mechanically copied forward.
2. **Inputs**: `sessions/evoi-framework.md` §2 rank-9b row; `S100a-ENVELOPE-OVERDETERMINE` verdict Class-8.3 reconciliation companion row (audit `4ed74d7ee8a494ab`, verdict file line 87); `S100a-FREEZEIN-OVERCONSTRAINED` verdict (audit `78ee1d5677d75dc8`).
3. **Gate**: re-stamp verified iff the §2 row carries the Sage-exact κ_SONIC pin + post-W3 status AND the `<!-- evoi-content-currency: S{N} -->` marker advances (`_evoi_staleness_audit.py` PASS, lag 0).
4. **Effort**: ~0.05 wave-equivalents (mechanical register edit at plan-time; no compute).

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-06 | Dynamical-freeze-in flavor predictor (full SM sector) | OPEN (S99 squeezed-vacuum successor) | CLOSED — over-constraint breaks structurally: BDI J-conjugacy pins same-generation ratios at 1; \|w\| ceiling caps \|V_us\| at 0.072 (3.14× short); 4/12 held-outs | S100a-FREEZEIN-OVERCONSTRAINED FAIL (`78ee1d5677d75dc8`) |
| 2026-06-06 | Charged-lepton SHAPE from freeze-in | hypothesis | EXACT — one S₀ = 1.6942 on C₂ = (4/3, 3, 6) carries the shape (machine-precision fit); θ₁₃ within 1.87σ | same gate, surviving leg |
| 2026-06-06 | "One operator, two faces" (greybody = freeze-in exponent) | OPEN (double-derivation hypothesis) | INFO — C₂-flat vs C₂-linear straddle (rel_disc 0.58/0.21); exact closure needs graded ω*(C₂); fingerprint S₀·T_acoustic = τ_fold (0.134%) | S100a-ENVELOPE-OVERDETERMINE INFO (`4ed74d7ee8a494ab`) |
| 2026-06-06 | S₀ threshold-fixing (KK-THRESHOLD-64) | OPEN | INFO — threshold-CONSTRAINED to O(1) (dev 0.245); residual knob 1.3247 with 3 sharp candidates (4/3 / δ/2 / τ_fold/T_acoustic); E_A = 2π·S0_threshold exact cross-gate | S100a-S0-THRESHOLD-JOINT INFO (`eeb7e5bd8d30938b`) |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | JSON | Size |
|:-----|:-------|:------------|:------------|:-----|:-----|
| S100a-FREEZEIN-OVERCONSTRAINED | `s100a_freezein_overconstrained.py` | `s100a_freezein_overconstrained.npz` | `s100a_freezein_overconstrained.png` | — | py / npz / png |
| S100a-ENVELOPE-OVERDETERMINE | `s100a_envelope_overdetermine.py` | `s100a_envelope_overdetermine.npz` | `s100a_envelope_overdetermine.png` | — | 27.7 KB / 12.3 KB / 77.5 KB |
| S100a-S0-THRESHOLD-JOINT | `s100a_s0_threshold_joint.py` | `s100a_s0_threshold_joint.npz` | `s100a_s0_threshold_joint.png` | — | 30.5 KB / npz / png |

(All three gates emit to `computations/session-100a/s100a_gate_verdicts.txt` via the race-safe `emit_verdict` MCP tool.)
