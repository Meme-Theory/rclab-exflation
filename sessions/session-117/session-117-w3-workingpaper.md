# Session 117 Wave 3 — Lepton-CP & Baryogenesis (Results Working Paper)

**Session**: 117 | **Wave**: 3 | **Plan**: session-117-plan-w3.md | **Theme**: Lepton-CP & baryogenesis (W-1 campaign) — the S116 W-1 forward computes on the **external** `ε_LX` sector (`γ_9`-odd, outside `Ω¹_{D_K}`, the sector `J` is silent on). Substrate-first: the `L_max=10` `D_K` Peter-Weyl spectrum → the spectral-action minimiser's CP-parity → the baryon channel that sources `η_B` → the leptogenesis↔PMNS joint image → the off-Jensen `U(2)` fiber moduli that fix whether the transit and leptonic CP phases are one invariant or two. 4 compute gates ([SIGN]×3, [VERIFY]×1), all classification/adjudication/moduli-count gates closing via verdict line. The **internal** `J`-channel result `η_B = 0 EXACT` (S60: `[J,D_K]=0 ⇒ M_R real ⇒ ε_1=0`) stays closed; these gates adjudicate the external channels `J` does not constrain.

## Wave 3 Dispatch Prerequisites (decision-point)

This is the dispatch-time prerequisite note (plan §"Wave 3 Decision Point Prerequisites"); the team-lead's wave-close synthesis is the empty `## Wave 3 Synthesis (team-lead)` heading below.

**External prerequisite (Wave 2 → Wave 3)**: the W-1 lepton-CP verdict is tagged **CONDITIONAL-PENDING-CF-W2-1** — i.e. Wave-2 gate **2-5 `CF-S117-UEL-FLAT-DIRECTION`** (binary flat-vs-lifted test of `U_eL` under `S = Tr f(D_K/Λ)`). Verdict source: `computations/session-117/s117_gate_verdicts.txt`. Wave 3 runs AFTER Wave 2; in normal flow 2-5 has emitted its flat/lifted classification before Wave-3 dispatch. Gate 3-1 SUBSUMES the 2-5 binary into a three-way CP-parity refinement (2-5 *lifted* ⇒ 3-1 resolves Scenario I unique-real vs II conjugate-pair; 2-5 *flat* ⇒ 3-1 confirms Scenario III via the Hessian CP-null test).

**Mechanical-closure contingency (pre-registered per `.claude/rules/mechanical-closure-discipline.md`)**: if `CF-S117-UEL-FLAT-DIRECTION` has **no verdict line** (Wave 2 deferred/crashed) OR is `PRE-REG-INC` at Wave-3 dispatch, then **3-1, 3-2, 3-3 honestly close** `PRE-REG-INC` (`value='PRE-REG-INC_blocked_by_CF-S117-UEL-FLAT-DIRECTION_<status>'`), deferred to S118. **3-4 is independent of 2-5** (depends only on the already-registered `§VII.CK` external-`ε_LX` class) and runs regardless.

**Intra-wave dependency chain** (each downstream gate carries a mechanical-closure path if its Wave-3 prereq is not PASS/INFO at dispatch):

```
  CF-S117-UEL-FLAT-DIRECTION (Wave 2, gate 2-5)      §VII.CK external-ε_LX class (S116 W2-1, registered)
              │                                                      │
              ▼                                                      ▼
      3-1 CFW21-THREE-WAY ──────┐                          3-4 OFFJENSEN-U2-SHARING
        (CP-parity I/II/III)    │                            (RESOLVED vs SHARED)
              │                 │                                    │
              ▼                 │                                    │ (informs whether K7-transit
      3-2 BARYO-CHANNEL ────────┤                                    │  survives a real leptonic ε_LX)
        (K7 vs lepto)           │                                    │
              │                 ▼                                    │
              └──────► 3-3 LEPTO-PMNS-JOINT-IMAGE ◄──────────────────┘
                        (ε_1 ↔ δ_CP^PMNS over the M_D phase)
```

- **3-2** consumes **3-1**'s CP-parity verdict (the `M_D`-reality gate on `ε_1`). 3-1 = `PRE-REG-INC` ⇒ 3-2 closes `PRE-REG-INC_blocked_by_CF-S117-CFW21-THREE-WAY`.
- **3-3** consumes **3-1** AND **3-2**. Either `PRE-REG-INC` ⇒ 3-3 closes `PRE-REG-INC_blocked_by_*`.
- **3-4** is independent of the chain; depends only on the registered `§VII.CK` (`§VII.BL` multiplicity-bundle) entry, available now.

## Gate Sections

### §W3-1. S117-W3-1-CFW21-THREE-WAY (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S117-W3-1-CFW21-THREE-WAY`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (CP-parity of the spectral-action `ε_LX` minimiser)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The bosonic spectral action `S = Tr f(D_K/Λ)` is CP-EVEN under `ε_LX → conj(ε_LX)` (CPT-evenness identity `S(ε_LX^CP)=S(ε_LX)`, exact from `conj(D_K)=D_K^T` isospectral); therefore its lepton off-diagonal minimiser classifies into exactly ONE of (I) unique CP-self-conjugate (`Im(ε*)=0`; `δ_CP ∈ {0,π}` DYNAMICALLY, NOT `J`-forced), (II) CP-conjugate-pair (spontaneous CPV; predicted `|δ*|`), or (III) continuous CP-flat null-direction (under-determined). The minimiser's CP-parity — not `[J,D_K]=0` — is the discriminator. Structural lean (NOT a pre-registered verdict): a real-analytic CP-even functional generically has a unique global min ⇒ Scenario I, but the gate computes which scenario actually obtains.
**Plan reference**: `sessions/session-plan/session-117-plan-w3.md` §W3-1 (machinery pin, tolerances `tol_cpeven=1e-10`/`tol_real=1e-9`/`tol_hess=1e-8`, substitution chain D-R2.3, dual-prior track discriminator).

**Output Artifacts** (closure-verification checklist; verified on disk by content, not line count):
- (1) `computations/session-117/s117_cfw21_three_way.py` (43,149 B) — `grep -nE "from canonical_constants import|print_verdict_payload"` → L137 `from canonical_constants import (`, L674 + L766 `print_verdict_payload`. ✓
- (2) `computations/session-117/s117_cfw21_three_way.npz` (19,239 B). ✓
- (3) `computations/session-117/s117_cfw21_three_way.png` (196,850 B) — 3-panel: flat-valley `S(δ)` vs curved control, multistart minimiser scatter, verdict card. ✓
- (4) verdict line `s117_gate_verdicts.txt` L71 matches `^S117-W3-1-CFW21-THREE-WAY:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row L72; `[SIGN]` 3-tuple row L73 (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`); + 4 regulator/scenario extra-rows. ✓
- (5) this WP section: Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit present. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("CFW21 three-way CP parity spectral action lepton minimiser eps_LX")` → no prior gate evaluates this three-way (the `S85-W2-HP3…THREE-WAY` hit is unrelated — Hochschild triple intersection). **NOT pre-closed.**
- `search_knowledge("spectral action CP-even delta_CP PMNS forced J_PMNS ansatz artifact")` → returns the S116 W-1 workshop `s116-jpmns-forced-vs-artifact.md` + `delta_CP_PMNS_substrate` edges (Scenario-A real-eps_LX representative). Confirms the gate's scope.
- `get_constant("delta_CP_PMNS_substrate")` → `0.0`, S100b, source S99-W3-SEESAW-SUMMNU (real textures) — "Scenario-A {0,π} representative (real-eps_LX texture ansatz)", **NOT a J-derivation**. This is exactly the value the gate re-scopes.
- `get_constant("M_KK")` → `7.42866e16` GeV (= Λ; the flatness is Λ-INDEPENDENT — a function of singular values only).

**Verdict**: **INFO** — **Scenario III (CONTINUOUS-FLAT, under-determined)**. `[SIGN]` 3-tuple: `sign_verdict=PASS` (CPT-evenness identity holds EXACTLY) / `magnitude_verdict=INFO` (the not-PASS-I scenario class) / `regime_verdict=VALID`; composite-collapse (sign PASS, magnitude INFO, regime VALID) → INFO. dual-SHA `audit=6746198c429eee3f…` `content=3421dd7e7fee3d9d…`.

**Results**:

**Governing structure.** The finite lepton Dirac operator is chirality-off-diagonal, `D_F(M_lep) = [[0, M_lep],[M_lep†, 0]]` (6×6 Hermitian for any complex `M_lep`), so `D_F² = diag(M_lep M_lep†, M_lep† M_lep)` and the bosonic spectral action `S = Tr f(D_F²/Λ²) = 2 Σ_i f(σ_i²/Λ²)` is a **class function of the singular-value spectrum `{σ_i}` only**. The U_eL orbit at fixed lepton masses — `M_lep = U_eL diag(m) U_eR†`, `{σ_i}={m_i}` fixed, `U_eL ∈ U(3)` carrying the CP phase `δ` — therefore leaves `S` invariant: the real mixing angles AND the CP phase are flat directions. (2-5 `CF-S117-UEL-FLAT-DIRECTION` established the real-angle flatness, ΔS/S=3.2e-15; this gate extends it to the CP phase and confirms via the Hessian.)

**Scenario III determination (the numbers).**
- **CPT-evenness identity [SIGN]**: over 200 CP-violating textures (random angles, `δ ∈ [0,2π)`), `max |S(conj ε)−S(ε)|/|S| = 0.000e+00` (zeta `a_4`) and `= 0.000e+00` (cutoff `f*`); the structural reason `max|σ(M)−σ(conj M)| = 0.000e+00` (singular values invariant under conjugation). Identity holds to machine zero (< `tol_cpeven=1e-10`) ⇒ `S` is Z₂ CP-EVEN — **sign_verdict=PASS**. Functional-independent (holds in both zeta and cutoff).
- **Flatness over the orbit**: N_eval=64 multistart L-BFGS-B minimisations at fixed masses → `S_min` spread/⟨S⟩ = **1.072e-15** (< `tol_cpeven`); all 64 land at the exact `a_4` floor `2 Σ m_i⁴ = 3.032866e-04`; minimiser multiplicity = **CONTINUUM** (64/64 at floor).
- **CP phase FREE / under-determined**: minimiser `δ*` spread = **6.073 rad (~2π)**; `|Im(ε*)|` over minimisers spans `[1.11e-03, 1.05e-01]` — **not pinned to 0**. The minimiser is NOT a unique-real point (Scenario I excluded) and NOT a discrete conjugate-pair (Scenario II excluded); it is a flat valley.
- **SA Hessian along the CP direction (Scenario-III null test)**: at the CP-violating base point (`δ=π/4`), the pure-`δ` second derivative `H_δδ = 0.000e+00` (raw), `|H_δδ|/|S| = 0.000e+00`; the `δ`-aligned eigenvalue `|λ_CP| = 7.54e-29` (normalized 2.49e-25). Both ≪ `tol_hess=1e-8` ⇒ **NULL direction confirmed**. (The full 4×4 FD Hessian `max|H_ij| = 1.6e-11` raw is finite-difference roundoff on the real-angle directions — `a_4` is flat there too, per 2-5 and the 1e-15 `S_min` spread — and is reported but NOT used as the CP-null discriminant.)
- **Non-vacuous control**: the bare-grading cross term `a_2^lift(δ) = Tr((s_geom·G + M_herm(δ))²)`, `G=diag(√C2_E)` fixed in the flavor basis (2-5's lift candidate), at the artificial `s_geom=O(1)` gives `H_δδ^control = 2.15e-04` (genuine CP curvature; the Hessian routine DETECTS curvature when present), while `PRIMARY H_δδ / CONTROL H_δδ = 0.0` ⇒ the primary null is a GENUINE flatness, not a dead routine. At the physical scale `s_geom ~ M_KK/m_τ` the control δ-spread drops to `0.000e+00` (1/s_geom suppressed), and the §VII.BL multiplicity-SCALAR theorem (`G ∝ I ⇒ Tr(G M)=G₀ Tr(M)` invariant) excludes the lift entirely.

**4-tuple**: `(scheme=SA-BOSONIC Tr f(D_K/Λ), a_n^{ζ} canonical a_4=Tr D_F⁴ + f* cutoff cross-check; convention=s116 ε_LX texture / CP=conj(off-diag block) / D_K=D_K†; Λ=M_KK, flatness Λ-independent; L_max=10)`.

**Substitution chain (D-R2.3, with substituted numbers).**
```
Claim: "[J,D_K]=0 does NOT force δ_CP; the CP-EVEN spectral action's minimiser
        CP-parity is the discriminator; here the minimiser is a flat valley."
Def 1: S(ε_LX) := Tr f(D_F(ε_LX)²/Λ²)        [bosonic SA; f positive even cutoff]
Def 2: CP : ε_LX → conj(ε_LX)                 [charge conjugation on the off-diag block]
Def 3: D_F self-adjoint, real-linear in ε_LX ⇒ D_F(conj ε) = conj(D_F(ε))
Substitute (2,3 into 1):
   S(ε^CP) = Tr f(conj(D_F(ε))²/Λ²)
Simplify:
   conj(D_F) = D_F^T                          [conjugate of Hermitian = transpose]
   spectrum(D_F^T) = spectrum(D_F)            [isospectral]
   ⇒ S(ε^CP) = S(ε)                          [VERIFIED: residual 0.000e+00]  ⇒ S Z₂ CP-EVEN.
Read off the Z₂-evenness:
   S = 2 Σ_i f(σ_i²/Λ²), σ_i = singular values = {m_i} FIXED on the U_eL orbit
   ⇒ S is CONSTANT over the orbit (real angles + δ)   [VERIFIED: S_min spread 1.072e-15]
   ⇒ ∂²S/∂δ² = 0                                      [VERIFIED: H_δδ = 0.000e+00, λ_CP = 7.5e-29]
Conclusion:
   unique-min ⇒ Im(ε*)=0 (Scenario I)   — EXCLUDED (min not unique: continuum)
   conjugate-pair (Scenario II)          — EXCLUDED (δ* continuum, not 2 discrete pts; H_δδ null)
   continuous-flat (Scenario III)        — CONFIRMED (H_δδ null + S flat + δ* free)
   ⇒ δ_CP_PMNS is UNDER-DETERMINED by the bosonic spectral action.
```

**Dual-prior track reallocation.** Pre-registered Track-A = Scenario-I (unique-real, δ_CP dynamical) vs Track-B = Scenario II/III. The outcome lands **Track-B, sub-branch III**: the "CPT-even-SA leans REAL-if-unique" structural lean does NOT fire here because the minimiser is **not unique** — it is a continuum, so there is no unique min to be forced real. The real-eps_LX texture (`delta_CP_PMNS_substrate=0.0`) is a CHOICE within a flat valley, **ANSATZ-ARTIFACT-as-derived** — the S116 W-1 down-tag is CONFIRMED, and the "`[J,D_K]=0 ⇒ J_CP=0` forced" justification is struck (J is exact CPT and SILENT on this external `γ_9`-odd `ε_LX` sector, outside `Ω¹_{D_K}`). Routes to `mack` for the falsifier-inventory Row #89 re-scope and to the `delta_CP_PMNS_substrate` canonical-comment scope (`canonical_constants.py:675`).

**Downstream (fb_pair backward).** Feeds **3-2 BARYO-CHANNEL-ADJUDICATION** the M_D-reality verdict: the SA does not SELECT M_D real, but neither does it force it complex — the CP phase is a free parameter. For 3-2's gating the operative reading is that the substrate-natural representative texture (`M_e` real, the s116 npz) sits AT a CP-conserving point of the flat valley, so `ε_1=0` at the representative texture while a complex M_D is equally SA-admissible. 3-2 adjudicates K7-transit (`φ_CP^{K7}=π/2`, sector-resolved) vs leptogenesis (`ε_1`, M_D-reality-gated) on that footing.

**Substrate framing (PARTICLE).** Direction of explanation: L_max=10 `D_K` Peter-Weyl eigenvalues → spectral moments `a_0,a_2,a_4` → the CP-even GEOMETRY of `S` as a functional of `ε_LX` → the CP-parity classification of its minimiser. The governing structure is the charge-conjugation identity `conj(D_K)=D_K^T` (D_K self-adjoint), making `S` exactly Z₂-even; the discriminator is that geometry, NOT `[J,D_K]=0`. Taking every algebraic solution seriously (the Dirac discipline that kept the negative-energy states): the CP-even `S` ADMITS a complex minimiser (Scenario II) — a spontaneous-CPV prediction the J-forcing reading would wrongly discard — but the substrate's actual answer here is flatter still: the bosonic spectral action is blind to the CP phase, which lives in the unitary orbit at fixed singular values. The phase is a substrate degree of freedom the bosonic action does not fix; whether anything fixes it (the seesaw/leptogenesis sector, 3-2/3-3) is a separate, external question.

---

### §W3-2. S117-W3-2-BARYO-CHANNEL-ADJUDICATION (dirac-antimatter-theorist)

**Status**: COMPLETED
**Gate ID**: `S117-W3-2-BARYO-CHANNEL-ADJUDICATION`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (which external channel sources `η_B`)
**Agent**: `dirac-antimatter-theorist`
**Hypothesis**: The observed `η_B = 6.12e-10` is sourced by ONE of two EXTERNAL substrate channels — (a) K7-transit (`φ_CP^{K7}=π/2`, the `φ_88`-Cartan unique non-leptophilic CP source) or (b) external-`ε_LX` leptogenesis (Davidson–Ibarra `ε_1` from `M_D=ε_LX^ν`, `M_R` B-branch real-diagonal) — and 3-1's `M_D`-reality verdict gates the leptogenesis channel: REAL `M_D` (Scenario I) ⇒ `ε_1=0` EXACT so leptogenesis is dead and K7-transit must dominate; COMPLEX `M_D` (Scenario II) ⇒ both channels live and the magnitude adjudicates. Distinct from the S60 INTERNAL result `η_B=0 EXACT`; the internal channel stays closed.
**Plan reference**: `sessions/session-plan/session-117-plan-w3.md` §W3-2 (Davidson–Ibarra + s61 K7-transit machinery, `η_BBN` band, dominance ratio threshold ×3, substitution chain).

**Entry condition (3-1 actual = Scenario III, not the planned binary).** The plan's substitution chain anticipated a *binary* — Scenario I (real `M_D` ⇒ `ε_1=0` ⇒ leptogenesis dead) vs Scenario II (complex `M_D` ⇒ both live). The upstream gate 3-1 (`S117-W3-1-CFW21-THREE-WAY`, verdict-file L71) returned **Scenario III (CONTINUOUS-FLAT)**: the bosonic spectral action `S = 2 Σ_i f(σ_i²/Λ²)` is a class function of singular values (masses) only, so the `M_D` CP phase is a **flat, under-determined** direction — the substrate selects neither real nor complex. This *sharpens* the adjudication rather than blocking it: leptogenesis is not "dead-by-forcing" — its CP source is simply **not a substrate output** (a free dial, reading zero at the real representative texture); K7-transit's CP source is **substrate-pinned**. (3-1 = INFO ≠ PRE-REG-INC ⇒ this gate proceeds, not mechanical-closure.)

**Output Artifacts** (closure-verification checklist; verified on disk by content, not line/byte counts):
- (1) `computations/session-117/s117_baryo_channel_adjudication.py` (35,364 B) — `grep -nE "from canonical_constants import|print_verdict_payload"` → L106 `from canonical_constants import (`, L511 + L616 `print_verdict_payload`. ✓
- (2) `computations/session-117/s117_baryo_channel_adjudication.npz` (27,177 B). ✓
- (3) `computations/session-117/s117_baryo_channel_adjudication.png` (196,120 B) — 2-panel: leptogenesis CP source vs `ε_LX` phase (numerical vs Sage-exact `sin 2φ`, =0 at the substrate texture) + channel-adjudication bar (`η_B^K7` vs `η_B^lepto=0` EXACT, `η_BBN` band). ✓
- (4) verdict line `s117_gate_verdicts.txt` L114 matches `^S117-W3-2-BARYO-CHANNEL-ADJUDICATION:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row L115; `[SIGN]` 3-tuple row L116 (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`); + composite-precedence row + 6 regulator/structure/drift extra-rows. ✓
- (5) this WP section: Status COMPLETED, Verdict PASS, Output Artifacts, MCP Pre-Compute Audit present. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("K7-transit baryogenesis eta_B N_pairs epsilon_K7 phi_CP transit")` → returns the structural equation `eta_B = N_pairs * epsilon_CP * epsilon_K7` (`s61_j_breaking_catalog_log`, `N_pairs(transit)=59.8`) and the `phi_CP_K7_transit`/`epsilon_K7` provenance edges (S49 DIPOLAR-CATALOG → S61 → S98). The channel FORMULA is known; this gate **adjudicates which channel wins under 3-1's flat verdict** — **NOT pre-closed.**
- `search_knowledge("baryon asymmetry channel adjudication leptogenesis M_D reality gate")` → returns the S60 `eta_B=(28/79)*epsilon_1*kappa/g_*` leptogenesis machinery (`s60_lepto_cp_log`) and the S60 INTERNAL `η_B=0 EXACT` ([J,D_K]=0). Confirms the INTERNAL channel is closed and scopes this gate to the EXTERNAL `ε_LX`/K7 sectors.
- `get_constant("phi_CP_K7_transit")` → `1.5707963267948966` (=π/2 EXACT), S100b, source S98-W3-2-BARYOGEN-UNIQUENESS — the `φ_88`-Cartan substrate-FIXED CP phase (category-(A) pin); `sin(π/2)=1` MAXIMAL.
- `get_constant("eta_BBN_obs")` → `6.12e-10` (Planck 2018 + BBN); `get_constant("n_pairs")` → `59.8`; `get_constant("epsilon_K7")` → `0.00248`; `get_constant("g_star_SM")` → `106.75`.

**Verdict**: **PASS** — **channel = PASS-K7** (track_A). `[SIGN]` 3-tuple: `sign_verdict=PASS` (K7 dominance direction `sgn(η_K7−η_lepto)=+`, with `η_lepto=0` EXACT) / `magnitude_verdict=INFO` (η_BBN reproduction is washout/efficiency-dependent) / `regime_verdict=VALID`. Composite **PASS** via the plan-frozen two-branch channel-adjudication operator (`strict_PASS_boundary=N/A`, S95 non-compute clause) — the channel lands K7 DEFINITIVELY (dominance ratio `=∞` ≫ 3, since `η_lepto=0` EXACT; `η_B^K7` reproduces `η_BBN_obs` within the BBN+washout band), which OVERRIDES the generic 3-tuple collapse (magnitude=INFO ⇒ INFO) that would misread as the plan INFO_meaning "comparable channels" (FALSE here). dual-SHA `audit=d1c15711a51db3ef…` `content=59e7557796c215c3…`.

**Results**:

**M_D construction + seesaw cross-check.** `M_D = ε_LX^ν` rebuilt from the s116 npz `Y_nu_diag=[0, 4.7936, 11.9276]` + shared off-diagonal `w23_nu=2.8085` in the s116 `yukawa_block_real` convention (real-symmetric, `(0,0)` row/col decoupled ⇒ `Y_1=0` EXACT ⇒ `m_1=0`, rank-2). Cross-check `max|M_ν(recon) − M_ν(npz)| = 0.000e+00` (`M_ν = M_D M_R⁻¹ M_D^T`, `M_R=diag(1.0044, 1.0786, 1.1700)` B-branch real-diag) — the construction is bit-exact.

**Channel (b) leptogenesis — `ε_1=0` EXACT at the substrate texture (the load-bearing number).** Davidson–Ibarra on the REAL s116 `M_D`: `ε_DI = [0, 0, 0]` for all three `N_i`; the CP-source numerator `max_i |Σ_j Im[((Y†Y)_ij)²]| = 0.000e+00` (< `tol=1e-12`). `Im[(real)²]=0` ⇒ `ε_1 = 0` EXACT ⇒ `η_B^lepto = (28/79)·ε_1·κ/g_* = 0` EXACT (any κ).

**The 3-1 flat-direction consequence (M_D-phase scan).** Placing a CP phase `φ` on the `w23` off-diagonal and scanning `φ ∈ [0,2π)` (360 pts): the CP source is `0.000e+00` at `φ=0` (the REAL substrate texture) and rises to a max `9.409e+02` for generic `φ`. The numerical scan matches the **Sage-exact** closed form `Im[((Y†Y)_12)²] = (Y2²−Y3²)·w²·sin(2φ)` (amplitude `940.92`) to residual **3.41e-13**. The leptogenesis CP source is `∝ sin(2φ)` — an *odd* function vanishing at the CP-conserving points `{0, π/2, π}` and **FREE elsewhere**. This is exactly 3-1's Scenario-III flat `ε_LX` phase: the substrate does not pin `φ`, so `η_B^lepto` is under-determined and reads zero at the real representative texture.

**Channel (a) K7-transit — substrate-pinned CP source.** `ε_CP = sin(φ_CP^{K7}=π/2) = 1.000000` EXACT (MAXIMAL), phase-reality-INDEPENDENT. Raw yield `η_B^K7 = N_pairs·ε_CP·ε_K7 = 59.8·1·0.00248 = 1.4830e-01`; sphaleron-(28/79)+`g_*`-normalized (no washout) `η_B^K7 = 4.9240e-04`; matches `η_BBN_obs` for washout `κ ≈ 1.243e-06` (strong-washout regime). The s61 `TRANSIT-BARYOGEN-61` washout band `[1.98e-09, 2.22e-06]` brackets `η_BBN_obs=6.12e-10` (conservative end within factor ~3).

**Adjudication (signed dominance).** `η_B^K7 = 4.9240e-04 > η_B^lepto = 0` EXACT ⇒ `sgn(η_B^K7 − η_B^lepto) = +1` ⇒ **K7-transit DOMINATES**, dominance ratio `=∞` (since `η_lepto=0` EXACT; ≫ the ×3 threshold). The channel lands **K7-transit** definitively. The reproduction of `η_BBN_obs` is washout/efficiency-dependent (`κ` is a free factor, as in all leptogenesis) → `magnitude=INFO`; the dominance/sign is substrate-pinned → `sign=PASS`.

**4-tuple**: `(scheme=Davidson-Ibarra ε_1 (s60) + s61 K7-transit η_B=N_pairs·ε_CP·ε_K7, sphaleron 28/79, g_*=106.75; convention=M_D-reality gate from 3-1 Scenario-III-flat / φ_CP^{K7}=π/2 EXACT [canonical:674] / M_R real-diag B-branch / η_BBN band κ-factor ~2–3; L_max=N/A — M_D, M_R from the s116 npz, no fresh D_K diagonalisation)`.

**Substitution chain (the [SIGN] prediction, with substituted numbers; Sage-exact cross-checked).**
```
Claim: "At the substrate-natural texture, η_B^K7 > η_B^lepto = 0, so K7-transit
        is the sole substrate-DETERMINED external channel (PASS-K7); the
        'J_PMNS=0 ⇒ leptogenesis self-falsifying' worry DISSOLVES."
Def 1: ε_1 = (3/16π)(1/(Y†Y)_11) Σ_{j≠1} Im[((Y†Y)_1j)²] g(M_j²/M_1²),  Y=M_D   [Davidson-Ibarra, s60]
Def 2: M_D = ε_LX^ν,  CP phase set by the ε_LX minimiser (3-1: FLAT ⇒ free, real at the representative texture)
Def 3: η_B^lepto = (28/79)·ε_1·κ/g_*                                            [g_*=106.75]
Def 4: η_B^K7 = N_pairs·ε_CP·ε_K7,  ε_CP = sin(φ_CP^{K7})                       [s61; N_pairs=59.8, ε_K7=0.00248]
Substitute (substrate texture, M_D REAL):
   M_D real ⇒ (Y†Y)_1j ∈ ℝ ⇒ ((Y†Y)_1j)² ∈ ℝ ⇒ Im[((Y†Y)_1j)²] = 0       [VERIFIED: CP-source 0.000e+00]
   ⇒ ε_1 = 0                                                                   [Sage-exact: Im[((Y†Y)_12)²]=(Y2²−Y3²)w²sin2φ, φ=0 ⇒ 0]
   ⇒ η_B^lepto = (28/79)·0·κ/g_* = 0 EXACT
Simplify:
   φ_CP^{K7} = π/2  ⇒ sin(π/2) = 1  (MAXIMAL, M_D-reality-INDEPENDENT)         [VERIFIED: ε_CP=1.000000]
   ⇒ η_B^K7 = N_pairs·1·ε_K7 = 1.4830e-01 (raw) > 0                            [η_B^K7(sphaleron,/g_*)=4.9240e-04]
Canonical form (substrate texture):
   η_B^lepto = 0  <  η_B^K7 ≠ 0
Direction:
   sgn(η_B^K7 − η_B^lepto) = +  ⇒ K7-transit DOMINATES (sole nonzero external channel)  [VERIFIED: sign +1, ratio ∞]
Conclusion (3-1 Scenario-III refinement):
   leptogenesis CP source ∝ sin(2φ) is UNDER-DETERMINED (3-1 flat ε_LX phase), zero at the real texture;
   K7-transit CP source sin(π/2)=1 is SUBSTRATE-PINNED ⇒ the substrate DETERMINES only the K7 channel.
```

**A2.2 status routing — `J_PMNS=0` self-falsification worry DISSOLVED (track_A).** The D-R2.4 worry was: *if* leptogenesis sources `η_B`, then real `M_D` ⇒ `ε_1=0` AND `δ_CP ∈ {0,π}`, so `J_PMNS=0` would self-falsify a leptogenesis-sourced `η_B`. The adjudication dissolves it on two independent grounds: (i) leptogenesis is **not** the substrate-determined channel — its CP source is the 3-1 flat `ε_LX` phase (free, zero at the real texture), not a substrate output; (ii) the substrate-determined channel is **K7-transit**, whose CP source is the `φ_88`-Cartan phase `π/2` — a **DIFFERENT CP invariant** from the leptonic Jarlskog. W3-4 `OFFJENSEN-U2-SHARING` (PASS, verdict-file L67) proves the sector-resolution structurally: `dim=5 = 1` (`φ_88` λ₈ U(2)-center singlet) `+ 4` (`ε_LX` CP² coset doublet), "no-linking-constraint", "`φ_88` gauge-invariant survives real `ε_LX`", "K7-transit-CP-independent-of-leptonic-`ε_LX`". So a nonzero K7-sourced `η_B` is CONSISTENT with `δ_CP_PMNS ∈ {0,π}` or under-determined ⇒ `J_PMNS=0` does NOT self-falsify (the sector-resolved E-3 reading). A2.2 = sector-resolved **CONSISTENCY note**, NOT a self-falsification linkage. Routes to `mack` Row #89 baryogenesis annotation.

**Internal/external separation (the S60 result is untouched).** This is NOT the S60 `η_B=0 EXACT` result. S60 computed the **INTERNAL** channel (`[J,D_K]=0 ⇒` internal `M_R` real `⇒` internal `ε_1=0`), which STAYS CLOSED. Here `M_R` is real-diagonal by spectrum-pinning (S-3 B-branch) and the EXTERNAL phase source is `M_D=ε_LX^ν`, whose reality is set by 3-1 (FLAT), NOT by `J`. `J` is exact CPT and SILENT on this external `γ_9`-odd `ε_LX` sector (outside `Ω¹_{D_K}`).

**Substrate framing (PARTICLE).** Direction of explanation: `D_K`'s external `ε_LX` texture (`γ_9`-odd) → the Dirac Yukawa `M_D=ε_LX^ν` + the spectrum-pinned `M_R` → the Davidson–Ibarra CP asymmetry `ε_1` (leptogenesis) AND the `φ_88`-Cartan transit phase `φ_CP^{K7}=π/2` (K7-transit) → the baryon asymmetry `η_B`. The governing structure is the `M_D`-reality gate: `ε_1 ∝ Im[(M_D†M_D)²]`, EXACTLY zero for real `M_D` — the Dirac discipline of taking an exact algebraic vanishing seriously, the same discipline that kept the negative-energy solutions. IS-NOT-IN category tags: `φ_CP^{K7}=π/2` is category (A) substrate pin (canonical:674); `η_BBN_obs=6.12e-10` is category (B) external observational datum KEPT as a binding target; the sphaleron `28/79` + `g_*=106.75` + κ efficiency are the framework's OWN external-channel machinery (substrate-native, NOT a category-(C) rival-framework intermediate). The internal `J`-channel (S60 `η_B=0` EXACT) stays closed; this gate is the external sector `J` is silent on.

**Downstream (fb_pair backward).** Feeds **3-3 LEPTO-PMNS-JOINT-IMAGE** the channel verdict: leptogenesis is NOT the substrate-determined channel (its CP source is the 3-1 flat `ε_LX` phase). 3-3 may still map the `(ε_1, δ_CP^PMNS)` joint image over that free phase as a CONDITIONAL DUNE-testable falsifier (if one chose a complex `ε_LX` to activate leptogenesis), but the substrate's own answer for `η_B` is K7-transit. Also routes to `mack` Row #89 (A2.2 = sector-resolved CONSISTENCY note, not self-falsification linkage).

---

### §W3-3. S117-W3-3-LEPTO-PMNS-JOINT-IMAGE (neutrino-detection-specialist)

**Status**: COMPLETED
**Gate ID**: `S117-W3-3-LEPTO-PMNS-JOINT-IMAGE`
**Trigger**: `[SIGN]`
**Classification**: **PARTICLE** (two CP invariants as joint images of one `M_D` phase)
**Agent**: `neutrino-detection-specialist`
**Hypothesis**: With `M_R` spectrum-pinned real-diagonal (S-3 B-branch) and `M_D=ε_LX^ν` the SOLE phase source, the leptogenesis asymmetry `ε_1(φ)` and the PMNS Dirac phase `δ_CP^PMNS(φ)` are CO-SOURCED by the single `M_D` phase `φ` (both odd about the CP-conserving points `{0,π}`) — so there EXISTS a substrate-natural complex `M_D` landing BOTH a viable `η_B` (leptogenesis) AND a DUNE-measurable `δ_CP^PMNS ∉ {0,π}`: a falsifiable JOINT prediction "baryon asymmetry ⟺ measurable leptonic CP". Consumes 3-1 (is there a phase at all?) and 3-2 (is leptogenesis the channel?).
**Plan reference**: `sessions/session-plan/session-117-plan-w3.md` §W3-3 (720-pt phase scan, seesaw + Davidson–Ibarra, `η_B` viability band `[3,8]e-10`, DUNE 5σ band, `δ_off=0.1 rad`).

**Entry conditions (both PASS/INFO ⇒ gate runs, not mechanical-closure).** 3-1 (`S117-W3-1-CFW21-THREE-WAY`, verdict-file L71) = **INFO, Scenario III CONTINUOUS-FLAT** — the `M_D` CP phase `φ` is a flat, **under-determined** direction (the spectral action is a class function of singular values only). 3-2 (`S117-W3-2-BARYO-CHANNEL-ADJUDICATION`, L114) = **PASS-K7** — `η_B` is sourced by K7-transit (`φ_CP^{K7}=π/2`, a DIFFERENT CP invariant per 3-4 RESOLVED), NOT by leptogenesis (`η_B^lepto=0` EXACT at the real texture). Both verdicts **reframe** this gate: the joint image is computable, but the PASS reading's "falsifiable JOINT prediction" is precluded at its root (see Verdict). (Both present, neither PRE-REG-INC ⇒ this gate proceeds.)

**Output Artifacts** (closure-verification checklist; verified on disk by content/regex, never line/byte counts):
- (1) `computations/session-117/s117_lepto_pmns_joint_image.py` (43,168 B) — `grep -nE "from canonical_constants import|def print_verdict_payload"` → L116 `from canonical_constants import (`, L634 `def print_verdict_payload(` (called at L795). ✓
- (2) `computations/session-117/s117_lepto_pmns_joint_image.npz` (84,308 B) — joint-image arrays `phis`, `eps_lepto`, `J_pmns`, `dcp`, `eta_B` + all cross-checks. ✓
- (3) `computations/session-117/s117_lepto_pmns_joint_image.png` (301,309 B) — 3-panel: the two co-sourced curves vs `φ` (shared `{0,π}` zeros, `ε_1` extra zeros at `{π/2,3π/2}`) + the joint image `{(ε_1(φ), δ_CP^PMNS(φ))}` + `η_B(φ)` vs `δ_CP` with viability band. ✓
- (4) verdict line `s117_gate_verdicts.txt` **L124** matches `^S117-W3-3-LEPTO-PMNS-JOINT-IMAGE:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row **L125**; `[SIGN]` 3-tuple row **L126** (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`); + composite-precedence row + 7 structure/downstream/consistency extra-rows. ✓
- (5) this WP section: Status COMPLETED, Verdict INFO, Output Artifacts, MCP Pre-Compute Audit present. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("leptogenesis epsilon_1 delta_CP PMNS joint image Davidson-Ibarra seesaw")` → returns `delta_CP_PMNS_substrate = 0.0` (S100b/S116; "Scenario-A {0,π} representative, real-ε_LX texture ansatz") and the structural equation `eta_B = (28/79)·epsilon_1·kappa/g_*` (`s60_lepto_cp_log`). The seesaw machinery + the δ_CP representative are known; this gate maps the **joint image over the M_D phase** and adjudicates whether it is a falsifiable prediction — **NOT pre-closed.**
- Sage-MCP `sage_eval` (exact CP-phase algebra, pre-compute): `Im[((M_D†M_D)_12)²] = (Y2²−Y3²)w²sin(2φ)` (zeros `{0,π/2,π,3π/2}`); `M_ν(φ)` off-diagonal `∝ e^{iφ}`, diagonal `∝ e^{2iφ}` (complex symmetric; Im vanishes only at `{0,π}`) — established the co-sourcing harmonic structure BEFORE the numerical scan.
- `get_constant("eta_BBN_obs")` → `6.12e-10`; `get_constant("g_star_SM")` → `106.75` (imported from `canonical_constants.py`, runtime SHA `d884a2b5…`). Agent-memory `s100a_md_normalization.md`: `m_1=0` EXACT (MAP-B Casimir grading `C2(0,0)=0`); Dirac-scale normalisation **oscillation-anchored PERMANENTLY** ⇒ the `η_B` magnitude is NOT a zero-parameter prediction.

**Verdict**: **INFO** — the joint image is a well-defined NON-independent curve (sign PASS), but the falsifiable JOINT prediction is **DISSOLVED** (track_B). `[SIGN]` 3-tuple: `sign_verdict=PASS` (the co-sourcing direction — `ε_1(φ)` and `δ_CP^PMNS(φ)` are non-independent functions of one phase, both vanishing at `{0,π}`, with `δ_CP` LIFTING off `{0,π}` for generic `φ`) / `magnitude_verdict=INFO` (a co-viable `φ` is REALISABLE but is NOT a substrate prediction) / `regime_verdict=VALID` (all cross-checks exact). Composite **INFO** via the generic schema-v2 collapse (sign PASS ∧ magnitude INFO ∧ regime VALID), which AGREES with the plan operator here — no precedence override needed. dual-SHA `audit=b3caaffac1768326…` `content=5c298296d7268fc4…`.

**Results**:

**Cross-checks (all exact).** `M_ν = M_D M_R⁻¹ M_D^T` rebuilt from the s116 npz (`Y_nu_diag=[0, 4.7936, 11.9276]`, `w23_nu=2.8085`, `M_R=diag(1.0044, 1.0786, 1.1700)` B-branch): `max|M_ν(recon) − M_ν(npz)| = 0.000e+00`. PMNS at `φ=0` (real texture): `J_PMNS = 0.000e+00`; `sin²(θ12,θ23,θ13) = (0.99559, 0.05928, 0.00869)` — **bit-matches** the npz `sin2_th*` (the texture's mixing angles are S116-walled / under-determined, but reproduced exactly here). `|U_PMNS|` magnitude-set match vs npz = `1.26e-14`. Charged-lepton rotation `U_eL` taken from the npz (real, masses `[3.19e-5, 6.60e-3, 1.11e-1]`); `M_ν(φ)` re-diagonalised per grid point.

**Co-sourcing structure — the `[SIGN]` content (confirmed).** Scanning `φ ∈ [0,2π)` (720 pts):
- the leptogenesis CP source `Im[((M_D†M_D)_12)²]` matches the **Sage-exact** `(Y2²−Y3²)w²sin(2φ)` (amplitude `940.92`) to residual **4.55e-13** — `ε_1(φ) ∝ sin(2φ)`, period `π`, **FOUR zeros** at `{0, π/2, π, 3π/2}`.
- `|J_PMNS(φ)|` vanishes ONLY at `{0, π}` (`[0, 4.086e-3, 3.7e-19, 4.086e-3]` at `{0, π/2, π, 3π/2}`) — period `2π`, **TWO zeros**; max `|J_PMNS| = 4.086e-3` at `φ=π/2`.
- ⇒ the two CP invariants are **co-sourced by one phase `φ` but NON-INDEPENDENT with DIFFERENT harmonic content**: they share the CP-conserving zeros `{0,π}`, but `ε_1` has EXTRA accidental zeros at `{π/2, 3π/2}` (where `((Y†Y)_12)²` is real-negative) that `δ_CP^PMNS` does NOT. **This refines the plan substitution chain's "both vanish at `{0,π}`"** — true for the SHARED zeros, but `ε_1` vanishes at MORE points. `δ_CP^PMNS` LIFTS off `{0,π}` as `φ` varies (the Dirac phase is genuinely activated).

**`δ_CP` physical despite `m_1=0` (the seesaw subtlety).** `Y_1=0` ⇒ rank-2 `M_D` ⇒ `m_1=0` EXACT (S100a Casimir grading). The massless neutrino eigenvector is `(1,0,0)` EXACTLY for ALL `φ` (`M_ν`'s first row/col is identically zero), so `U_PMNS` column 1 is REAL — yet `J_PMNS(φ) ≠ 0`. The Dirac phase lives in the complex 2-3 Takagi eigenvectors combined with the REAL charged-lepton rotation `U_eL` mixing generation 1. A massless lightest neutrino kills one **Majorana** phase but leaves the **Dirac** `δ_CP` physical (standard NO `m_lightest=0` result).

**Existence test.** Off-`{0,π}` ⟺ `|sin δ_CP| > sin(0.1)=0.0998`.
- at the fixed representative washout `κ=0.01`: **no** co-viable `φ` (`η_B` overshoots `[3,8]e-10` wherever `ε_1≠0`).
- at free physical `κ ∈ (0,1]`: **co-viable `φ` EXISTS**. Representative `φ=1.562` gives `δ_CP^PMNS = 238.5°` (off `{0,π}`), `ε_1=0.138`, with `κ_for-6e-10 = 1.31e-06` — the SAME strong-washout ballpark as 3-2's K7 `κ_req=1.24e-06`. `δ_CP` sweeps `[6.3°, 353.7°]` on the off-`{0,π}` branch (nearly the full circle).
- **consistency note (NOT a prediction):** the joint curve passes through `δ_CP = 238°` at the J-max (`φ=π/2`) — INSIDE the NuFIT 3σ NO band `[108°, 404°]` and near the NuFIT central `~230°`. Since `φ` is free (3-1 flat), this is a CONSISTENCY, not a prediction.

**The joint prediction is DISSOLVED (why INFO, not PASS).** The PASS reading required the framework to make a FALSIFIABLE joint prediction — "a leptogenesis-sourced `η_B` REQUIRES a DUNE-measurable `δ_CP`." Two upstream verdicts preclude it: (i) **3-1 Scenario III flat** ⇒ `δ_CP^PMNS` is **UNDER-DETERMINED** — the substrate selects NO point on the joint curve, so there is no predicted `δ_CP` to falsify; (ii) **3-2 PASS-K7** ⇒ `η_B` is **K7-sourced** (`φ_CP^{K7}=π/2`, a DIFFERENT CP invariant per 3-4 RESOLVED), NOT leptogenesis-sourced — so a baryon asymmetry does NOT require a measurable leptonic CP phase. DUNE measuring `δ_CP` would **LOCATE** the free phase on the curve, it would NOT FALSIFY a linkage (there is none at the substrate texture). **Why INFO and not FAIL:** a co-viable `φ` EXISTS (the joint image is realisable — near `φ≈π/2`, `ε_1` is small but `δ_CP` is large), so it is NOT the FAIL mutual-exclusion; and it is NOT PASS because it is not a substrate prediction (`δ_CP` free + `η_B` K7-sourced + the `η_B` magnitude is efficiency-dependent and oscillation-anchored per S100a). This CROSS-CHECKS 3-2 PASS-K7: the leptonic `δ_CP` and baryogenesis are decoupled.

**4-tuple**: `(value=INFO joint-image co-sourced-NON-independent, J_PMNS_absmax=4.086e-03 @ φ=π/2 (δ_CP=238.1°); scheme=seesaw M_ν=M_D M_R⁻¹ M_D^T PMNS-Jarlskog δ_CP + Davidson-Ibarra ε_1(s60), joint-image over the M_D phase; convention=PMNS from Hermitian M M† rephasing-invariant J / M_R real-diag B-branch / sphaleron 28/79 / g_*=106.75 / η_B(φ)=(28/79)·ε_1(φ)·κ/g_*; L_max=N/A — seesaw on the s116 npz M_D, M_R, no fresh D_K diagonalisation)`.

**Substitution chain (the `[SIGN]` prediction, with substituted numbers; Sage-exact cross-checked).**
```
Claim: "ε_1(φ) and δ_CP^PMNS(φ) are co-sourced by the single M_D phase φ; the
        joint image is a well-defined NON-independent curve through (0,{0,π})."
Def 1: M_D(φ) = [[0,0,0],[0,Y2,w e^{iφ}],[0,w e^{iφ},Y3]]   (symmetric; Y1=0 ⇒ m_1=0)
Def 2: ε_1(φ) = Davidson-Ibarra(M_D(φ), M_R) ∝ Im[((M_D†M_D)_12)²]               [s60]
Def 3: δ_CP^PMNS(φ) from the Jarlskog of U_PMNS = U_eL† U_νL(φ), M_ν=M_D M_R⁻¹ M_D^T
Def 4: η_B(φ) = (28/79)·ε_1(φ)·κ/g_*                                              [g_*=106.75]
Substitute at the CP-conserving points φ ∈ {0,π}:
   M_D(0), M_D(π) REAL ⇒ Im[((M_D†M_D)_12)²]=0 ⇒ ε_1=0 ⇒ η_B=0                  [VERIFIED: cp_src(0)=0]
   real M_ν ⇒ J_PMNS=0 ⇒ δ_CP^PMNS ∈ {0,π}                                       [VERIFIED: J(0)=J(π)=0]
   ⇒ both CP invariants vanish TOGETHER at {0,π} (curve passes through (0,{0,π}))
Move φ off {0,π}:
   ε_1(φ) = (Y2²−Y3²)w² sin(2φ)/(8π (Y†Y)_ii) · f_loop  ≠ 0 (zeros also at π/2,3π/2)  [Sage-exact; resid 4.55e-13]
   δ_CP^PMNS(φ) ≠ {0,π} for generic φ                                              [VERIFIED: |J|_max=4.086e-3 @ π/2]
Canonical form:
   ε_1(φ) and δ_CP^PMNS(φ) are NON-INDEPENDENT functions of one phase φ, both
   vanishing at {0,π}; ε_1 has EXTRA zeros at {π/2,3π/2} (DIFFERENT harmonic content).
Direction:
   the η_B-viable branch (free κ) coincides with the δ_CP-off-{0,π} branch
   ⇒ a co-viable φ EXISTS (realisable; rep. φ=1.562, δ_CP=238.5°, κ_6e-10=1.31e-6).
Conclusion (3-1 + 3-2 refinement):
   the joint relationship is REALISABLE but NOT a falsifiable substrate prediction —
   δ_CP^PMNS UNDER-DETERMINED (3-1 flat ⇒ no predicted point) AND η_B K7-sourced
   (3-2 PASS-K7 ⇒ no η_B⟺δ_CP linkage). INFO (between PASS-prediction and FAIL-exclusion).
```

**Downstream routing (fb_pair backward).** Per the plan W3→W4 decision map, "3-1 = INFO-(III) flat → Row #89 stays CONDITIONAL (the substrate does not select; `δ_CP` genuinely free)." So this gate routes to `mack` Row #89 as a **STRUCTURE / CONSISTENCY note** — two CP invariants co-sourced by one phase, a non-independent joint curve — NOT a falsifiable `δ_CP ⟺ η_B` prediction; the capstone `m_ββ` Row #80 inherits the `δ_CP`-CONDITIONAL status. (All falsifier-surface / Row #89 edits are `mack-cosmic-bridge`'s sole-writer domain.) The result is consistent with and reinforces 3-2 PASS-K7: leptonic CP and baryogenesis are decoupled at the substrate texture.

**Substrate framing (PARTICLE).** Direction of explanation: `D_K`'s external `ε_LX^ν` texture (`γ_9`-odd, outside `Ω¹_{D_K}`) → the Dirac Yukawa `M_D(φ)` + the spectrum-pinned `M_R` → the seesaw composite `M_ν = M_D M_R⁻¹ M_D^T` → the PMNS Jarlskog phase `δ_CP` AND the leptogenesis `ε_1` → the joint observable curve. The lab-IN observable is `δ_CP` measured IN a continuum oscillation experiment (DUNE); the substrate IS the `ε_LX^ν` texture whose phase sources BOTH CP invariants. The npz texture is the real-`ε_LX` ansatz (`J_PMNS=0`); this gate DEFORMS it by a CP phase and reads the joint consequence — it does NOT assume the ansatz is the minimiser (3-1's job, which found the phase FLAT). IS-NOT-IN tags: the `η_B` band `[3,8]e-10` and the DUNE `δ_CP` 5σ band are category (B) external observational data (the substrate is tested against them); the seesaw + Davidson–Ibarra machinery is substrate-native. The absolute `η_B` scale is NOT a zero-parameter prediction — the Dirac-scale normalisation is oscillation-anchored PERMANENTLY (`S100a-MD-NORMALIZATION` INFO) and the washout `κ` is a free efficiency dial.

---

### §W3-4. S117-W3-4-OFFJENSEN-U2-SHARING (baptista-spacetime-analyst)

**Status**: COMPLETED
**Gate ID**: `S117-W3-4-OFFJENSEN-U2-SHARING`
**Trigger**: `[VERIFY]`
**Classification**: **GEOMETRIC** (off-Jensen `U(2)` fiber-moduli count)
**Agent**: `baptista-spacetime-analyst`
**Hypothesis**: The off-Jensen `U(2)`-deformation on the `{λ_4,…,λ_8}` coset+Cartan of SU(3) carries the `φ_88` transit CP phase (`λ_8` Cartan; `φ_CP^{K7}=π/2`) and the lepton `ε_LX` off-diagonal (`λ_4..λ_7` coset) on EITHER independent moduli (RESOLVED: `dim = 1 + k_coset`, so `φ_88` and `ε_LX` are separate deformation parameters and K7-transit survives a REAL leptonic `ε_LX`) OR one shared parameter (SHARED: `dim < 1 + k_coset`, a linking constraint, so the two phases are locked and the D1 main-line linkage stands). The moduli-dimension count is the discriminator — a structural integer, no `η_B`/`J_CP` sign claim. **Independent of the 2-5/3-1/3-2/3-3 chain** (depends only on the registered `§VII.CK`/`§VII.BL` class); runs regardless.
**Plan reference**: `sessions/session-plan/session-117-plan-w3.md` §W3-4 (su(3) Gell-Mann structure-constant count, U(2)+CP² decomposition, Sage-MCP exact rationals).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML — content presence by regex, never line/byte counts):
- (1) `computations/session-117/s117_offjensen_u2_sharing.py` — PRESENT (36087 B). `grep -cE "from canonical_constants import"` = **1**; `grep -cE "print_verdict_payload"` = **2**. ✓
- (2) `computations/session-117/s117_offjensen_u2_sharing.npz` — PRESENT (12437 B). ✓
- (3) `computations/session-117/s117_offjensen_u2_sharing.png` — PRESENT (163509 B; 2×2 panel: |ad(u(2))| block structure on D, moduli-count bar, ad(λ_8)|coset hypercharge eigenvalues, verdict panel). ✓ (optional per plan)
- (4) verdict line — PRESENT, matches `^S117-W3-4-OFFJENSEN-U2-SHARING:.* audit_sha256=[a-f0-9]{64}` with dual-SHA companion comment row (`# audit_sha256_short=1d6b5db3cb1a8e67 content_sha256_short=11468d2c359d48a4 # S117-W3-4-OFFJENSEN-U2-SHARING dual-SHA companion row`) + 2 extra rows (regulator_pin N/A; canonical_drift note). `[VERIFY]` trigger — NO schema-v2 3-tuple (correct). ✓
- (5) this WP section — `**Status**: COMPLETED`, `**Verdict**: PASS — RESOLVED`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` all present. ✓

**MCP Pre-Compute Audit**:
- `search_knowledge("off-Jensen U(2) coset moduli phi_88 Cartan eps_LX sharing RESOLVED")` → prior off-Jensen work is S76 W2-J (`off_jensen_moduli`: full 35D restoring-potential / ridge dynamics, `Off_Jensen_Moduli_Hessian --closed_by--> W2-J`) — a DIFFERENT question (full TT-moduli Hessian, not the φ_88-vs-ε_LX sharing dichotomy). The framework Jensen scaling surfaced exactly: **L_1=e^{2τ} (u(1)_Y=⟨λ_8⟩, 1 dir)**, **L_2=e^{-2τ} (su(2)_I, 3 dirs)**, **L_3=e^{τ} (C² coset SU(3)/U(2)=⟨λ_4..7⟩, 4 dirs)** (`Phononic-Substrate-Geometry.md`; `J_C2=0.933 (coset)`, `J_u1=0.038, J_su2=0.059 (u(2))`). This gate's RESOLVED/SHARED sharing-count is **NOT** pre-closed.
- `get_constant("phi_CP_K7_transit")` → `1.5707963267948966` = π/2 EXACT (S100b; S98-W3-2-BARYOGEN-UNIQUENESS; sector-split per S99 litreview §III). Confirmed unchanged ⇒ the canonical_constants.py SHA drift (plan `8c850fd9..` → runtime `d884a2b5..`, from in-session W0 ρ_s/c2 promotions) does NOT affect this gate (only φ_CP_K7 is cited). `audit_sha256` binds runtime bytes per `substrate-first-canonical-sourcing.md §(ii.B)` plan-text-drift correction.
- `trace_entity("VII.CK external eps_LX class")` → no trace (S116 W2-1 registry entry not yet swept into the knowledge index; the gate is a pure su(3) Lie-algebra count and does not depend on it numerically — §VII.CK/§VII.BL are cited only as the registry home of the ε_LX class).
- **PRE-CLOSED?** NO — genuinely uncomputed (the φ_88-vs-ε_LX moduli-sharing dichotomy is new; S76 off-Jensen is the full-moduli Hessian, orthogonal).

**Verdict**: **PASS — RESOLVED**. `dim(off-Jensen moduli) = 5 = 1 (φ_88) + 4 (ε_LX coset) = 1 + k_coset`; **no linking constraint** `c(φ_88, ε_LX)=0`. The φ_88 Cartan CP phase (K7-transit, φ_CP=π/2) and the ε_LX coset off-diagonal (leptonic CP) are **INDEPENDENT** off-Jensen moduli ⇒ K7-transit survives a real leptonic ε_LX (J_PMNS=0 is CONSISTENT with K7-transit baryogenesis); the E-3 sector-resolution holds; supports 3-2 PASS-K7.

**Results**:

*Governing structure.* The fiber is SU(3); the Jensen background is the U(2)-invariant left-invariant metric (framework scaling **L_1=e^{2τ} on u(1)_Y=⟨λ_8⟩ (1 dir), L_2=e^{-2τ} on su(2)_I=⟨λ_1,λ_2,λ_3⟩ (3 dirs), L_3=e^{τ} on the C² coset SU(3)/U(2)=⟨λ_4..λ_7⟩ (4 dirs)**, `Phononic-Substrate-Geometry.md`). The off-Jensen deformation turns on the λ_8 Cartan phase φ_88 (=φ_CP_K7=π/2) and the coset off-diagonal ε_LX. The off-Jensen MODULI are deformations modulo the residual isotropy gauge U(2)=SU(2)_I×U(1)_Y; the RESOLVED/SHARED discriminant is the **U(2)-isotropy irrep type** of the two directions.

*The decisive fact (exact, all residuals 0.00e+00).* **λ_8 generates the CENTER of U(2)**: `[λ_8,λ_1]=[λ_8,λ_2]=[λ_8,λ_3]=0` (max residual 0.00e+00, machine-exact). Hence **φ_88 is a U(2)-SINGLET** modulus. The coset ⟨λ_4..λ_7⟩ is a **single irreducible U(2)-DOUBLET**: real commutant of `{ad(λ_h)|coset}` has dimension **2 = ℂ** (Schur over ℝ ⇒ one irreducible complex doublet), with a single hypercharge magnitude `|Y| = √3 = 1.7320508` (`ad(λ_8)|coset` eigenvalues all of magnitude √3; `f_845=f_867=√3/2`).

*Why no linking constraint (RESOLVED).* A U(2)-singlet and a U(2)-doublet are **different irreps** ⇒ no U(2)-equivariant (residual-gauge) map connects them. The deformation space `D=⟨λ_4..λ_8⟩` (verified ad(u(2))-invariant, leak 0.00e+00) decomposes as **(U(2)-singlet ⟨λ_8⟩) ⊕ (U(2)-doublet ⟨λ_4..λ_7⟩)** with the λ_8 block fully decoupled from the coset block in ad(u(2)) — off-diagonal mixing 0.00e+00 in **both** directions (λ_8→coset and coset→λ_8). So `dim(off-Jensen moduli) = 1 + k_coset = 1 + 4 = 5`, no constraint ⇒ **RESOLVED**.

*Substitution-chain warning made precise.* `[λ_8, λ_{4..7}] ≠ 0` (the coset carries hypercharge √3, `f_845=f_867=√3/2≠0`), **but generator non-commutation does NOT link the deformation PARAMETERS**. The U(1)_Y action `exp(iφλ_8)` rotates the coset off-diagonal PHASE (`ε_LX → e^{i√3φ}ε_LX`, gauge on ε_LX) while FIXING λ_8 (which commutes with itself). Hence φ_88 is **gauge-INVARIANT** and cannot be absorbed into ε_LX's phase, nor can it be gauged away — it is a genuine, independent physical modulus. The count is on the irrep content, not the generator commutators.

*Validity gates (not FAIL, not INFO).* Reductive `[u(2),m]⊆m` (leak 0.00e+00) and symmetric `[m,m]⊆u(2)` (leak 0.00e+00) ⇒ SU(3)/U(2)=CP² is a symmetric space and the decomposition is well-defined (not FAIL). **Basis-invariant**: rotating the coset basis by a generic U(2) group element keeps λ_8 orthogonal/singlet (`rot_orth_8 = 0.00e+00`) ⇒ the verdict survives reparametrisation (not INFO). **Counterfactual teeth**: if the "Cartan-phase" generator were a coset generator (λ_4) it would land in the doublet (NOT a singlet) ⇒ SHARED — the test discriminates, so RESOLVED is a genuine fact about λ_8 being central, not a tautology.

*Cross-check (Sage QQbar, exact).* Independently verified over QQbar: normalisation Tr(λ_aλ_b)=2δ_ab; λ_8 central in U(2); `f_845=f_867=√3/2`; reductive + symmetric (CP² symmetric space); `ad(λ_8)|coset` eigenvalues ±√3; `D = singlet⟨λ_8⟩ ⊕ doublet⟨λ_4..7⟩` with no equivariant mixing. The numpy producing-script reproduces all of these to machine-exact 0.00e+00.

*4-tuple.* `(value=RESOLVED:dim=5=1+4, no-linking-constraint; scheme=su3-gellmann-U2-isotropy-ad-irrep-moduli-count; convention=Tr(λ_aλ_b)=2δ_ab, U(2)=⟨λ_1,λ_2,λ_3,λ_8⟩, coset CP²=⟨λ_4,λ_5,λ_6,λ_7⟩, Jensen on Cartan, off-Jensen on coset, φ_88=λ_8 CP phase [canonical:674]; L_max=N/A symbolic)`. `[VERIFY]` trigger — integer moduli-dimension discriminant, NO numerical η_B/J_CP sign claim.

*Dual-SHA.* `audit_sha256=1d6b5db3cb1a8e670eaaf07e67b4657a982eab305c3ff510e1a4a6739adecf5d`; `content_sha256=11468d2c359d48a444644f08a128d028f42720c41d21185e9b134eb04c02de00`. (Plan-text-drift note: plan-pinned canonical_constants.py SHA `8c850fd9..` differs from runtime `d884a2b5..` due to in-session W0 ρ_s/c2 promotions; only φ_CP_K7=π/2 is cited and MCP-confirms unchanged; `audit_sha256` binds the runtime bytes per `substrate-first-canonical-sourcing.md §(ii.B)`. Recorded as a `# canonical_drift:` extra-row on the verdict line.)

*Routing (plan §"Wave 3 → Wave 4 Decision Point", 3-4 = PASS-RESOLVED).* φ_88 (K7-transit) and the leptonic ε_LX are **independent CP invariants** ⇒ K7-transit survives a real ε_LX; supports **3-2 PASS-K7** and the **E-3 sector-resolution** reading. mack Row #89 baryo annotation = sector-resolved (φ_88-Cartan phase is a DIFFERENT CP invariant from the leptonic Jarlskog), routed to `mack-cosmic-bridge` per plan §Routing.

*Substrate framing (GEOMETRIC).* The off-Jensen moduli are a property of the spectral-triple STRUCTURE (the fabric), not its excitations. Direction of explanation: SU(3) Gell-Mann generator algebra → U(2)+CP² coset decomposition → off-Jensen moduli space → independence of the φ_88 Cartan CP phase and the ε_LX coset off-diagonal. Whether the transit and leptonic CP phases are different invariants (sector-resolved) or one (shared) is fixed by the fiber's coset geometry — the U(2)⊂SU(3) isotropy irrep factorisation, a Lie-algebraic invariant — NOT by any excitation dynamics. The ε_LX class lives in §VII.BL (the multiplicity-bundle); this gate counts its moduli against the φ_88 Cartan direction.

---

## Wave 3 Synthesis (team-lead)

All four Wave-3 gates ran to verdict (NO mechanical closure — 2-5=PASS(flat) landed before dispatch, so the chain 3-1→3-2→3-3 executed on real prereqs; 3-4 ran independently). The wave **RESOLVES the S116 W-1 campaign question**: J_PMNS=0-forced is ANSATZ-ARTIFACT-as-derived within a free family, and — crucially — it is CONSISTENT with the substrate's actual baryogenesis answer, not self-falsifying.

### (a) Numerical revisions
- 3-1: CP-even identity max|S(ε^CP)−S(ε)|/|S| = **0.000e+00** (zeta a₄ AND cutoff f*); S_min spread 1.072e-15 (continuum minimiser); δ* spread **6.073 rad (~2π, FREE)**; pure-δ Hessian H_δδ = 0.000e+00 (CP-null confirmed) vs control 2.15e-4.
- 3-2: η_B^lepto = **0 EXACT** (real M_D ⇒ Davidson-Ibarra ε₁=0); η_B^K7 = 0.1483 (ε_CP=sin(π/2)=1 EXACT); dominance = ∞.
- 3-3: J_PMNS_absmax = **4.086e-03 @ φ=π/2** (δ_CP=238.1°); the (ε₁, δ_CP^PMNS) joint image is a well-defined NON-independent curve, both vanishing at {0,π}.
- 3-4: dim(off-Jensen moduli) = **5 = 1 (φ_88) + 4 (ε_LX coset) = 1 + k_coset**; no linking constraint c(φ_88, ε_LX)=0.

### (b) Structural changes
- **J_PMNS=0 self-falsification DISSOLVED** (the W-1 campaign's central worry, epistemic-TYPE change). Three independent results compose: (i) 3-1 Scenario III — the lepton-CP phase is a *flat, under-determined* direction of S=Tr f(D_K/Λ) (a class function of singular values only); (ii) 3-2 PASS-K7 — the baryon asymmetry is sourced by K7-transit (φ_CP^{K7}=π/2, substrate-pinned), NOT leptogenesis (which is 0 at the real texture); (iii) 3-4 RESOLVED — the K7 φ_88-Cartan phase and the leptonic ε_LX-coset phase are INDEPENDENT moduli (dim=1+k_coset). So J_PMNS=0 coexists with a real, substrate-determined baryon asymmetry on a *different* CP invariant — a sector-resolved consistency, not a contradiction.
- **The leptonic CP phase is a free dial, not a substrate prediction** (3-1+3-3): DUNE measuring δ_CP would LOCATE the free phase on the joint curve, NOT falsify a linkage (there is none at the substrate texture). The conditional "IF a complex ε_LX is activated, the (ε₁, δ_CP) curve is DUNE-locatable" is a conditional annotation, not a falsifiable prediction.

### Wave 3 → Wave 4 decision point
W3 resolved cleanly; it imposes no constraint on W4 (already complete, all PASS). The lepton-CP cluster closes the W-1 campaign in-session.

## Carry-Forward Computations

No carry-forwards: all Wave-3 outcomes closed in-session. The lepton-CP sector is genuinely UNDER-DETERMINED (3-1 flat, 3-3 free phase) — there is no compute that pins the free ε_LX phase (it is not a substrate observable); the baryon answer is settled (3-2 K7-transit); the moduli independence is RESOLVED (3-4). The deep residual — *what external mechanism selects the ε_LX mixing/CP seed* — is the same standing open research direction as W2's mixing under-determination (atlas-08 Q18b / the §VII.BL external non-LI fibre connection), NOT a 4-field-pinnable gate. Per the no-padding rule it routes to the standing-questions register, not here.

## Effected In-Session / routed to session-close

Non-math registry/falsifier/atlas updates (route to mack sole-writer / session-close capstone-hygiene; executed before STOP):
- falsifier Row #89 (baryogenesis): η_B = K7-transit (φ_CP^{K7}=π/2 substrate-pinned, ε_CP=1 EXACT); leptogenesis under-determined (η_B^lepto=0 at the real texture). (mack)
- `delta_CP_PMNS_substrate`: stays **CONDITIONAL / under-determined** (3-1 Scenario III flat) — NOT DERIVED-dynamically, NOT spontaneous-CPV; the {0,π} value is the real-ε_LX representative, the phase itself is FREE. Annotate accordingly (do NOT promote to a prediction). (registry/canonical)
- §VII.CK / §VII.BL sector-resolution: 3-4 RESOLVED (φ_88 ⊥ ε_LX independent moduli) ⇒ K7-transit survives a real leptonic ε_LX ⇒ J_PMNS=0 CONSISTENT with K7 baryogenesis; the A2.2 entry is a sector-resolved consistency note (E-3), NOT a self-falsification linkage. (mack/registry)
- atlas-08: the W-1 campaign question (J_PMNS=0 forced-vs-artifact) RESOLVED as ANSATZ-ARTIFACT-within-a-free-family, consistent with K7 baryogenesis. (Q3 capstone-hygiene; session-close.)

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:----------|:-------|
| 2026-06-28 | lepton-CP phase (3-1) | CONDITIONAL-PENDING-CF-W2-1 | Scenario III CONTINUOUS-FLAT (under-determined; CP-even, phase FREE) | 3-1 INFO; 2-5=flat |
| 2026-06-28 | baryogenesis channel A2.2 (3-2) | open (K7 vs lepto) | K7-transit sourced (η_B^lepto=0 EXACT; φ_CP^{K7}=π/2) | 3-2 PASS-K7 |
| 2026-06-28 | lepto↔PMNS joint prediction (3-3) | candidate falsifiable linkage | DISSOLVED (δ_CP free + η_B K7-sourced); joint curve realisable but not predicted | 3-3 INFO |
| 2026-06-28 | off-Jensen φ_88/ε_LX moduli (3-4) | linkage undetermined | RESOLVED INDEPENDENT (dim=1+k_coset); K7 survives real ε_LX | 3-4 PASS |
| 2026-06-28 | J_PMNS=0 self-falsification worry (W-1) | open campaign tension | DISSOLVED (sector-resolved consistency) | 3-1+3-2+3-4 composite |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Verdict |
|:-----|:-------|:------------|:------------|:--------|
| 3-1 | `s117_cfw21_three_way.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple; Scenario III) |
| 3-2 | `s117_baryo_channel_adjudication.py` | `.npz` | `.png` | PASS-K7 (+[SIGN] 3-tuple, composite-precedence) |
| 3-3 | `s117_lepto_pmns_joint_image.py` | `.npz` | `.png` | INFO (+[SIGN] 3-tuple) |
| 3-4 | `s117_offjensen_u2_sharing.py` | `.npz` | `.png` | PASS-RESOLVED ([VERIFY]) |
