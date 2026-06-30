# Session 117 — Plan Context (carry-forward scope)

**Date**: 2026-06-28
**Built by**: `/rclab-plan --session 117` (fanout) from the S116 per-wave WP `## Carry-Forward Computations` blocks + the S116 workshop-schedule campaign synthesis math-CF index.
**Mode**: SESSION, fanout (per-wave plan + per-wave WP).
**Prior**: S116 (9 compute waves / 82 in-session gate verdicts + a 13-deliverable adversarial-review campaign: 7 review solos S-1…S-7 + 5 workshops W-1…W-5 + 1 closeout S-8).

This is the authoritative scope for the per-wave planner swarm. Each planner reads ITS wave's item rows below (+ the named source CF block for campaign-sourced gates) + the rules/templates + Knowledge MCP. Do NOT read `session-116-plan*.md`.

---

## Source manifest (1b gather)

**WP carry-forward blocks (full 4-field specs read by the orchestrator):**
- `sessions/session-116/session-116-w1-workingpaper.md §"Carry-Forward Computations"` — A_s normalization (CF-S117-T-FOLD-EXIT-NORMALIZATION, ROUTE-B-PW-SOCC; + Q2 CF-W1-1/CF-W1-2)
- `…-w2-workingpaper.md` — Yukawa/PMNS (VIICK-UNCONDITIONAL-REVERIFY, LEPTON-SEESAW-R-CHANNEL, SEESAW-RESONANCE-MR-SEARCH, QUARK-CKM-UNDERDETERMINATION-REEXAM, CF-W2-1 UEL-FLAT-DIRECTION; + Q2 CF-W2-2)
- `…-w3-workingpaper.md` — DM (FREESTREAM-AT-ANCHOR, LEGGETT-COLLECTIVE-CEILING; + Q2 CF-W3-1)
- `…-w4-workingpaper.md` — modulus a₄ (MODULUS-A4-GRADIENT)
- `…-w5-workingpaper.md` — A_F ℍ: NO carry-forwards (closed in-session)
- `…-w6-workingpaper.md` — WDW (Q45-TAU0-OPERATOR-CANONICITY **[MOOTED — see below]**, CF-W6-1 J≡0-rigor)
- `…-w7-workingpaper.md` — STATE-PROJ (STATEPROJ-INTER-SUMMAND, STATEPROJ-SC-FROM-SUBSTRATE **[blocked]**, CF-W7-1)
- `…-w8-workingpaper.md` — FWD bridges (FWDC2-LEMP-BULKGAP-PROTECTION, CF-S94-W5-3-FWDC1-ASYMPTOTIC **[feasibility-gated]**; + the W4-refinement note flagging the UV-regulator B(R) span as "the new CF")
- `…-w9-workingpaper.md` — w0/branch-iv (BRANCH-IV-L16, W0-ANCHOR-FIDELITY; + Q2 CF-W9-1)

**Campaign math-CF index + source CF blocks (planner reads the named source block for the spec):**
- `sessions/session-116/session-116-workshop-campaign-synthesis.md §"Carry-Forward Computations (MATH ONLY)"` — the consolidated index (one-liners only; specs live in the source docs below).
- S-1 → `session-116-w1-Nspread-soundness-synthesis.md` · S-2 → `session-116-w1-As-falsifiable-content-synthesis.md` · S-3 → `session-116-w2-MR-structure-synthesis.md` · S-5 → `session-116-w7w8-vanishing-test-synthesis.md` · S-6 → `session-116-w8w9-FB-scope-synthesis.md` · S-7 → `session-116-w9-w0-transport-degree-synthesis.md`
- W-1 → `workshops/s116-jpmns-forced-vs-artifact.md` · W-2 → `workshops/s116-leggett-dm-edge-protection.md` · W-3 → `workshops/s116-efold-binding-vs-container.md` · W-4 → `workshops/s116-lemp-forced-vs-earned.md` · W-5 → `workshops/s116-w0-spectral-derivability.md`

**Housekeeping §B–§E**: empty (no hidden hygiene-compute / parallel-wave / rule-extension / shell items). Genuine math CFs live entirely in the WP + campaign source CF blocks above.

---

## Dedup / re-typing decisions (latest-synthesis-wins; the campaign post-dates the in-session WPs)

1. **`CF-S117-W0-ANCHOR-FIDELITY` ≡ `CF-S117-BRANCH-IV-PROXY-DESIGN`** (CF-W9-1): same compute, two IDs; canonical = the w0-transport/anchor question. The S-7 campaign solo RE-TYPED it: the W9 `→ −1.341` asymptote gap is **PROXY-ARTIFACT-TYPED** (λ_max edge is not an admissible §23 morphism), so the live successor is **`CF-S117-W0-TRANSPORT-DEGREE`** (extract the BZ→pivot morphism degree; deg=0 ⇒ confirm proxy-artifact / deg≠0 ⇒ §23 K=3 candidate). Do NOT plan W0-ANCHOR-FIDELITY separately — it is subsumed.
2. **`CF-S117-Q45-TAU0-OPERATOR-CANONICITY` — MOOTED (drop as a live gate).** S-4 solo: WS-ATFORM (S110 W1) IS Wave-6's pre-registered Stage 1, resolved to s1 ⇒ CF-S117-Q45 MOOTED, Wave-6 → HH-UNCONDITIONAL (double-robust: even granting s2, J≡0 ⇒ HH-parent). Recorded; NOT a Wave gate. `CF-W6-1` (rigorize J≡0 across the full real self-adjoint extension family) survives as an OPTIONAL low-leverage rigorization.
3. **`CF-S117-BRANCH-IV-L16` — DOWNGRADED to a value-neutral L_max diagnostic.** W-5 closed the branch-iv corridor **CLOSED-WITH-RESULT** (w0=−0.918 is a Level-1 closed-form thermodynamic identity, NOT spectral-action-derived; EVOI Tier-2 7c split CLOSED-WITH-RESULT / L_max-diagnostic / DESI-LIVE). L16 stays plannable as an OPTIONAL diagnostic, not a PASS/FAIL gate.
4. **L_emp gate is two orthogonal axes** (W-4 PARTIAL two-axis verdict): the `{APS,CS,BC}` secondary-class axis is **FORCED** (PH-even centered variance `Var(1−|v|²)=Var(|v|²)`, Sage-QQ) → `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION` is a FORCED-PASS confirmation pinned to curvature-grade **n=0**; the `{ζ,PV,Mellin}` UV-regulator axis is **SD-OPEN** (a₀-grade counterterm is additive-in-trace, survives the L_emp log-derivative) → `CF-S117-LEMP-UV-REGULATOR-BR-SPAN` is the GENUINE open gate (the W8 WP refinement note's "the new CF").
5. **`CF-S117-SEESAW-RESONANCE-MR-SEARCH` is anchored on the S-3 closed M_R form** (CF-W2-2): S-3 CLOSED OQ-4 — `M_R = fold-EIGENVALUE-SPECTRUM diag(B₁,B₂,B₃)` (√(B₂/B₁)=1.0363 Sage-exact); the scan covers fiber-spectrum forms ONLY (A_K-built degenerate forms → INFO not PASS; convention-shopping guard).
6. **`CF-S117-GS-1` is a plan-freeze-blocking sub-discriminator for `CF-S117-T-FOLD-EXIT-NORMALIZATION`** (S-1): the 𝒩-spread test alone is INSUFFICIENT (it measures intra-grid Parker-invariance, not the ξ_KZ-vs-H̃ grid SELECTION); GS-1 is the between-grid scale-coincidence test that must be authored alongside the 𝒩 gate.

---

## Wave partition (owner = reviewer-origin / domain specialist)

| Wave | Theme | Owner agent | Gates | Q / EVOI |
|:----:|:------|:------------|:-----:|:---------|
| 0 | Hygiene backfill (provenance + falsifier landing) | gen-physicist | 2 | Q2 backfill |
| 1 | A_s amplitude normalization (the Q23 rate-limiter) | transit-dynamics-theorist | 4 | Q23 — HIGH |
| 2 | Yukawa / seesaw mass-spectrum | neutrino-detection-specialist | 5 | Q18b |
| 3 | Lepton-CP & baryogenesis | dirac-antimatter-theorist | 4 | Q18b-adjacent (W-1) |
| 4 | Leggett DM kinematics | landau-condensed-matter-theorist | 3 | Q3 — FREESTREAM PRIMARY EVOI |
| 5 | Modulus a₄ gradient & WDW geometry | feynman-theorist | 2 | Q8 / Q12 |
| 6 | FWD-C2 L_emp bridge regulator-axes | lizzi-spectral-functional-theorist | 3 | Q30 |
| 7 | w0 transport-degree & categorical-wall | volovik-superfluid-universe-theorist | 3 | Q36 / Tier-2 7c |
| 8 | §VII.AJ STATE-PROJ inter-summand | landau-condensed-matter-theorist | 2 | Q33 |
| 9 | e-fold substrate obligations | mack-cosmic-bridge | 2 | W-3 (replaces retired N_e≥3.1) |

**Total: 30 gates / 10 waves.** EVOI-ordered: hygiene first (W0), then the Q23 A_s rate-limiter (W1) and the actionable-now dashboard order (Q18b, Q3, Q8/Q12, Q30, Q36, Q33), with the e-fold obligations last.

---

## Wave 0 items (gen-physicist) — Hygiene backfill (artifact-existence; ~0 compute)

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 0-1 | `CF-S117-HK-RHOS-C2-PROMOTE` | Promote `rho_s_C2 = 7.962` to `canonical_constants.py` with PROVENANCE (S48 MASS-48 / `s48_goldstone_mass.npz`). Consumed by the S116-W3-GOLDSTONE-M2 `[SIGN]` gate but absent from canonical_constants (`get_constant('rho_s_C2')`→not-found). Gate: `update_constant("rho_s_C2", 7.962, session="S48", source="S48-MASS-48", …)` lands + returns the value. | CF-W3-1 (w3 WP) |
| 0-2 | `CF-S117-HK-ALPHAS-TILT-LANDING` | Land the `α_s(primordial) ≈ 0` corollary (Mode-Independent Occupation; k-flat produced occupation ⇒ magnitude-only ⇒ tilt-flat) as an explicit mack falsifier-inventory sub-row on the A_s leg — a HARD tilt prediction INDEPENDENT of the A_s magnitude `𝒩` fork. mack sole-writer (`feedback_mack-bridge-role.md`). Gate: the tilt sub-row is on the inventory. | CF-W1-1 (w1 WP) |

*Wave-0 note: both are ~0-compute genuine S116-leftover backfills (artifact-existence PASS predicate, NOT a numerical threshold). 0-2 routes to mack (sole writer of the falsifier surface).*

---

## Wave 1 items (transit-dynamics-theorist) — A_s amplitude normalization

| # | Gate ID | Scope (what / key inputs / gate / effort) | Source |
|:--|:--------|:------|:-------|
| 1-1 | `CF-S117-T-FOLD-EXIT-NORMALIZATION` | **What**: propagate the Mukhanov-Sasaki mode eq (Radau; GPU-optional RX 9070 XT) for the produced GGE mode from τ_fold=0.190 across the post-fold subhorizon leg k/aH: 14.7→1, extracting 𝒩 in ζ_k̂(exit)=𝒩·(k̂/aH)^{+2}·\|β_k̂\|(fold); THEN a regime-robustness scan over ≥5 post-fold matching surfaces, measuring the 𝒩 spread. Discipline the grid (produced-relic ξ_KZ grid vs fold-geometry grid; the OOM_naive_extrap=9.37 fold-geometry move is the rejected artifact). **Inputs**: cf_beta2=0.143717 (INV12-W3-1); A_s_FW=1.5367059962762235e-8, ξ_KZ=0.0187601, k̂=53.30475, N_norm=ξ_KZ³=6.6024e-6 (S111 npz); z(τ)+(k/aH)\|_fold=14.7 (S77); deg_T_BZ_pivot=2.0 (canonical_constants:717); H̃=5.9076e-3 (INV12-W3-5); A_s^Planck=2.099e-9 (σ=0.0294e-9). **Gate**: convention-blocked PASS iff 𝒩-spread ≤0.1 OOM AND 𝒩∈{≈1⇒+0.864; =0.2148⇒+0.196}; physics-blocked FAIL iff 𝒩-spread >0.1 OOM (the 410.7σ fork stands). **Effort**: ~1 wave. **Depends on GS-1 (1-2) as a plan-freeze-blocking sub-discriminator.** | w1 WP CF block |
| 1-2 | `CF-S117-GS-1` | **What**: the between-grid scale-coincidence sub-discriminator (ξ_KZ vs acoustic-horizon grid SELECTION) — the test the 𝒩-spread discriminator does NOT make (Parker-invariance trivially forces ≤0.1 OOM for BOTH grids). **Gate-blocking at plan-freeze for 1-1**. Read the spec from the source CF block. **Source CF block**: `session-116-w1-Nspread-soundness-synthesis.md §"Carry-Forward Computations"` (S-1). | S-1 synthesis |
| 1-3 | `CF-S117-ROUTE-B-PW-SOCC` | **What**: recompute Route-B-Peter-Weyl A_s with the OCCUPIED-state spectral functional S_occ=(1+2n_k)·S_fold (NOT vacuum S_fold), CC3-threaded; test reduction to the box-delta/CC3 image vs a distinct third value. **Inputs**: K_sub=(1+2n_k) + locked-relic n̄≈2.736e-4 (INV12-W1-2); S66 AMPLITUDE-NORM-66 Route-B-PW assembly; A_s_FW=1.5367e-8 comparator. **Gate**: PASS-as-image iff within 0.1 OOM of +0.864; INFO-as-third-point iff >0.1 OOM from BOTH +0.864 and +0.196. **Effort**: ~0.5 wave. | w1 WP CF block |
| 1-4 | `CF-S117-ALT-GREYBODY` | **What**: moment-ratio / Connes-distance substrate-IS greybody Γ — the untested filter corridor (CF2 FAILed only on the near-horizon-barrier family; "NOT substrate-derivable" is scoped to that family, NOT to the moment-ratio/Connes-distance Γ). Read the spec from the source CF block. **Source CF block**: `session-116-w1-As-falsifiable-content-synthesis.md §"Carry-Forward Computations"` (S-2). | S-2 synthesis |

*Wave-1 split candidates (if a planner stalls): {1-1,1-2} (the 𝒩/GS-1 fork) | {1-3,1-4} (route-B / greybody filter).*

---

## Wave 2 items (neutrino-detection-specialist) — Yukawa / seesaw mass-spectrum

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 2-1 | `CF-S117-VIICK-UNCONDITIONAL-REVERIFY` | **What**: Stage-2 blind cross-axis re-verify of the W2-1-reconciled §VII.CK D4 mechanism (commutant/Skolem–Noether leg-membership) by a DISJOINT compliant pair — **Axis-A lizzi-spectral-functional-theorist × Axis-B volovik-superfluid-universe-theorist** (orchestrator finalizes per `joint-theorem-promotion.md §Stage-2 Axis-B Selection`). Both read ONLY the registered (corrected) §VII.CK entry — NOT the S112/S114/S115/S116 transcripts, NOT connes, NONE of {connes, paasch, van-den-dungen, baptista, kaluza-klein}. Clean PASS-AND → mack flips §VII.CK STAGE-3-PERMANENT → -UNCONDITIONAL. **Inputs**: corrected §VII.CK entry (post-W2-1 corrigendum); S116-W2-CK-STAGE2-VERIFY PASS (audit 63fc7317…); `computations/session-114/s114_yuk_rightreg_connection.npz`. **Gate**: PASS-AND (both axes independently PASS the joint clause, no workshop context) → UNCONDITIONAL flip; FAIL (either axis) → stays STAGE-3-PERMANENT (D4-open). **Effort**: ~1 wave (2-agent parallel blind verify; registry-read + adjudication, no new compute). **NOTE TO PLANNER**: gate_type is a paired Stage-2 verify — author it as a two-cross-reviewer dispatch per joint-theorem-promotion Stage-2. | w2 WP CF block |
| 2-2 | `CF-S117-LEPTON-SEESAW-R-CHANNEL` | **What**: compute R=Δm²₃₂/Δm²₂₁ from the eigenvalues of the SAME seesaw composite M_ν=M_D M_R⁻¹ M_D^T as W2-3 (mass-pinned M_D; M_R diagonal B-branch [1.0044,1.0786,1.1700]) — the spectrum channel the angle-metric does not touch. **Inputs**: `computations/session-116/s116_lepton_pmns_texture.npz` (M_D,M_R,M_ν); B-branch M_R (S100a); NuFIT 5.2 NO R-floor [17,66]; S96 peak R=6.87. **Gate**: PASS if R∈[17,66] at mass-pinned M_D + diagonal B-branch M_R; FAIL if R<17 (S96 shortfall persists); INFO if R lands only by rescaling M_R off bare B-branch. **Effort**: ~1 agent LOW (eigenvalue-ratio of existing M_ν). | w2 WP CF block |
| 2-3 | `CF-S117-SEESAW-RESONANCE-MR-SEARCH` | **What**: scan substrate-natural M_R candidates for the resonance condition M_D[2,2]/M_D[1,1]≈√(M_R[2]/M_R[1]) firing mix_grp≥3 at the mass-fit seed. **ANCHORED on the S-3 closed M_R form** (CF-W2-2): scan **fiber-spectrum forms ONLY** = M_R=fold-EIGENVALUE-SPECTRUM diag(B₁,B₂,B₃) bowtie (√(B₂/B₁)=1.0363 Sage-exact); A_K-BUILT degenerate forms → INFO not PASS (convention-shopping guard). **Inputs**: dirac_spectrum.py B-branch fold energies across τ; s116 mass-fit M_D; NuFIT 5.2 NO 3σ; the S-3 M_R form (`session-116-w2-MR-structure-synthesis.md §V.1`). **Gate**: PASS if a substrate-natural (S-3-form) M_R fires mix_grp≥3; FAIL if no fiber-spectrum M_R resonates; INFO if resonance fires only off-fold or off-S-3-form. **Effort**: ~1 agent MEDIUM. | w2 WP CF block + S-3 synthesis |
| 2-4 | `CF-S117-QUARK-CKM-UNDERDETERMINATION-REEXAM` | **What**: re-examine the S111 `V_us=0.3107` "prediction" under the under-determination lens — is U_dL free (masses fix singular values not left singular vectors) so V_us spans an interval at fixed quark masses? Quantify the reachable V_us range + minimal ‖ε_LX‖ to reach PDG 0.2243 (the quark analog of the lepton 1.53× soft wall). **Inputs**: S111 quark texture {ρ13^d,ρ23^d,\|w12^d\|,θ_d,Λ_d}+npz; quark mass spectrum; S111 multistart protocol; PDG V_us=0.2243. **Gate**: PASS (under-determination CONFIRMED for quarks) if V_us spans an interval with PDG reachable at non-minimal norm; FAIL (mass-forced) if uniquely pinned to 0.3107 with no free U_dL; INFO if constrained-but-narrow. **Effort**: ~1 agent MEDIUM. | w2 WP CF block |
| 2-5 | `CF-S117-UEL-FLAT-DIRECTION` | **What** (CF-W2-1): test whether the lepton mixing U_eL is a genuine FLAT DIRECTION of the spectral action S=Tr f(D_K/Λ), or whether the action (or the §VII.BL dD_K/dε_LX texture structure) LIFTS it. If lifted ⇒ the mixing is substrate-SELECTED and "under-determination" is an artifact of treating ε_LX as a free orthogonal R. Should precede/accompany 2-4. **Inputs**: `s116_lepton_pmns_texture.npz` (W2-3 ε_LX texture + U_eL-freedom construction); S=Tr f(D_K/Λ); §VII.BL dD_K/dε_LX. **Gate**: flat ⇒ under-determination CONFIRMED; lifted ⇒ mixing substrate-SELECTED (observed PMNS is a prediction at the SA-minimizing U_eL). **Effort**: ~1 agent MEDIUM. **Cross-link**: the W-1 workshop tags lepton-CP CONDITIONAL-PENDING-CF-W2-1 (this gate) — Wave 3 depends on it. | w2 WP CF block (CF-W2-1) |

*Wave-2 split candidates: {2-1} (Stage-2 verify, standalone) | {2-2,2-3} (seesaw spectrum/resonance) | {2-4,2-5} (under-determination: quark + lepton flat-direction).*

---

## Wave 3 items (dirac-antimatter-theorist) — Lepton-CP & baryogenesis

W-1 workshop (`workshops/s116-jpmns-forced-vs-artifact.md`) closed J_PMNS=0-forced as **ANSATZ-ARTIFACT-as-derived / CONDITIONAL-PENDING-CF-W2-1**; the HARD route is doubly-dead ([J,D_K]=0 necessary-not-sufficient; the only HARD route needs KO-dim 0/4, destroying the Majorana sector). These four CFs are its forward computes — **read the spec for each from `workshops/s116-jpmns-forced-vs-artifact.md §"Carry-Forward Computations"`.** The planner should consolidate if the source specs reveal overlap (report the dedup).

| # | Gate ID | Scope (one-liner; full spec in the W-1 source CF block) | Source |
|:--|:--------|:------|:-------|
| 3-1 | `CF-S117-CFW21-THREE-WAY` | lepton-CP three-way adjudication | W-1 workshop |
| 3-2 | `CF-S117-BARYO-CHANNEL-ADJUDICATION` | baryogenesis-channel adjudication | W-1 workshop |
| 3-3 | `CF-S117-LEPTO-PMNS-JOINT-IMAGE` | lepton-CP / PMNS joint-image | W-1 workshop |
| 3-4 | `CF-S117-OFFJENSEN-U2-SHARING` | off-Jensen U(2)-sharing | W-1 workshop |

*Depends on Wave-2 gate 2-5 (`CF-S117-UEL-FLAT-DIRECTION`) — the W-1 lepton-CP verdict is CONDITIONAL-PENDING that flat-direction test. Wave-3 split candidate: {3-1,3-3} (lepton-CP/joint-image) | {3-2,3-4} (baryo-channel / U(2)-sharing).*

---

## Wave 4 items (landau-condensed-matter-theorist) — Leggett DM kinematics

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 4-1 | `CF-S117-FREESTREAM-AT-ANCHOR` | **[PRIMARY, EVOI-carrying; [SIGN]]** **What**: compute the DM comoving free-streaming length λ_fs(m_Leggett, v_rms^GGE) at m_Leggett=11.97·Δ_BCS=5.5571 M_KK, with v_rms the EXPLICIT 2nd moment of the transit-frozen Bogoliubov occupation (v_rms²=∫(k/m)²n(k)d³k/∫n(k)d³k\|_frozen, non-relativistic — coldness is a COMPUTED output, the S_ent=0 Ordered Veil licenses the frozen-n(k) reading over thermal √(T/m)), vs the structure-formation threshold. **Inputs**: Mass_LeggettDM_over_Delta_BCS=11.97 (C11; conditional on Γ_grav<H_0); S38 Bogoliubov squeeze (⟨n⟩=730.6, n_Bog=0.99863); S95 Ordered-Veil (S_ent=0, R_therm=5252); Δ_BCS=0.4642547 (R-PROTECTED). **Gate**: PASS = cold transit-frozen dispersion gives λ_fs below threshold at the anchored mass with NO 170× enhancement (re-typing DISCHARGED); FAIL = a genuine warm-DM kinematic tension. `[SIGN]` on (λ_fs−λ_threshold). **Effort**: low (closed-form integral; no new diagonalization). | w3 WP CF block |
| 4-2 | `CF-S117-LEGGETT-COLLECTIVE-CEILING` | **[COMPANION, low-EVOI]** **What**: diagonalize the full inter-band pair-transfer across all (p,q) at L_max=10; read the heaviest PROTECTED collective Leggett mode, confirm it SATURATES at frac170≈0.07 (√N-saturation + continuum-edge cap). **Inputs**: D_K L_max=10 cache; collab §3 E_n=0.633√C_2+0.555; clean Leggett J_⊥; Δ_BCS. **Gate**: PASS = heaviest protected collective mode lands frac170∈[0.06,0.08]; ≫0.08 reopens Tier 2. **Effort**: medium (full inter-band diagonalization; GPU torch.linalg on off-(0,0) blocks). | w3 WP CF block |
| 4-3 | `CF-S117-LEGGETT-EDGE-AND-STIFFNESS` | **What**: inter-band ρ_s^⊥ / continuum-edge extraction → x_inter-band discriminator (the W-2 workshop CONVERGED-Reading-A theorem re-scoped to a √ρ_s-free SHARP-MODE ceiling E_edge^⊥=4.73·Δ_BCS; eq(15c) exclusion WITHDRAWN); includes the FREESTREAM v_fs^4D refinement. Read the spec from the source CF block. **Source CF block**: `workshops/s116-leggett-dm-edge-protection.md §"Carry-Forward Computations"` (W-2). | W-2 workshop |

*Wave-4 split candidate: {4-1} (free-streaming, PRIMARY) | {4-2,4-3} (collective ceiling + edge/stiffness).*

---

## Wave 5 items (feynman-theorist) — Modulus a₄ gradient & WDW geometry

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 5-1 | `CF-S117-MODULUS-A4-GRADIENT` | **[INFO-class — NOT a question-begging "δ must be small" PASS]** **What**: evaluate Gilkey's a₄ heat-kernel coefficient on M⁴×SU(3) under GCR, SEPARATED BY OPERATOR ORDER — **(B)** the genuine two-derivative δ to G_ττ (R_K(τ)(∂τ)², R_4(∂τ)²; prefactor (f_0/f_2)Λ_eff⁻²), reported AT τ_fold WITH SIGN+magnitude; **(C)** the four-derivative coefficients ((□τ)², (∂τ)⁴, \|R_{μaνb}\|²). Retire the order-mixed K_total≈7.07. Fold the anharmonic G'(τ)τ(∂τ)² vertex δZ on the 35D ridge. **Inputs**: `computations/session-63/s63_kk_reduce_4d.npz` (block data, R_K(τ), S(τ)); Gilkey a₄ (12D GCR invariants); `computations/session-74/s74_lefschetz_gaussian.npz` (35D ridge Hessian→δZ); Λ_eff=M_KK; G_DeWitt=5.0 (cross-check anchor, not input to δ). **Gate**: INFO = order-separated set delivered, δ(τ_fold) reported WITH SIGN at whatever magnitude, four-derivative coeffs separate, K_total≈7.07 retired; regime sub-test pins X=smallest \|τ−τ_fold\| at which ρ_B,ρ_C both <ρ_max≈0.3. FAIL = an O(1) two-derivative shift sourced from the a₂ sector ITSELF. **Effort**: medium (symbolic Gilkey-a₄ + cached-Hessian δZ; no fresh diagonalization). **Agent_type: feynman-theorist.** | w4 WP CF block |
| 5-2 | `CF-S117-WDW-J-RIGOR` (CF-W6-1) | **[OPTIONAL low-leverage rigorization; INFO-class]** **What**: rigorize Eq. H-R3-1 (J≡0) beyond Neumann — τ=0 is a REGULAR endpoint (W(0)=2G(S(0)−E)=0, finite) on the FINITE interval [0,τ_fold], so it is limit-circle and ANY real self-adjoint (Robin) extension gives J(0)=0⇒J≡0; reframe "Vilenkin-fundamental-outgoing" as EXCLUDED as a non-self-adjoint (complex) condition. STRENGTHENS the W6 verdict. **Inputs**: Eq. H-R3-1 (Sage-verified reflecting-τ=0→J≡0); S(τ) on [0,τ_fold]; limit-circle/Robin theory. **Gate**: J≡0 across the whole real self-adjoint family on [0,τ_fold]; INFO-class. **Effort**: ~0.5 agent LOW. **Agent_type: hawking-theorist.** **NOTE**: `CF-S117-Q45-TAU0-OPERATOR-CANONICITY` is MOOTED (S-4 → HH-unconditional) — NOT planned. | w6 WP CF block (CF-W6-1) |

*Wave-5 is mixed-domain (a₄ field-theory + WDW self-adjointness); feynman-theorist plans both but each gate's `agent_type` is per-gate (5-1 feynman, 5-2 hawking). Split candidate: {5-1} | {5-2}.*

---

## Wave 6 items (lizzi-spectral-functional-theorist) — FWD-C2 L_emp bridge regulator-axes

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 6-1 | `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION` | **[FORCED-PASS confirmation-only on the secondary-class axis]** **What**: compute the {APS-1975, Cheeger-Simons, Bismut-Cheeger} secondary-class scheme-spread for FWD-C2 L_emp=−7.046336 (ρ-invariant analog of S93 W9-3), certifying the secondary-class-axis Reading-A independence the W8 workshop FORCED-DEFERRED. Reshaped: verify no s=4 K-window spectral flow (bulk-gap protection). **Pin to curvature-grade n=0** (closes the S90-AQ scope-limit). The 3-scheme compute is FORCED-PASS by construction (degree-0 ∧ the centered-variance PH-evenness Var(1−\|v\|²)=Var(\|v\|²), Sage-QQ 327477/3125000 ⇒ ⟨Var_a,β^odd⟩=0). **Inputs**: `s116_w8_fwdc2_full_bdg_proxy_refinement.npz`; the {APS,CS,BC} machinery (S93 W9-3); L12/L14 BdG caches. **Gate**: scheme-spread Δ_scheme(L_emp)<1e-3 M_KK² across {APS,CS,BC} (FORCED-PASS expected) → §VII.AV.STATE-PROJ secondary-class Reading-A confirmed; FAIL (>1e-3) = surprise re-examining the degree-0∧sign-blind premise. **MUST NOT** be read as UV-regulator robustness (that is gate 6-2). **Effort**: medium. | w8 WP CF block + W-4 refinement note |
| 6-2 | `CF-S117-LEMP-UV-REGULATOR-BR-SPAN` | **[THE GENUINE OPEN L_emp GATE — SD-OPEN]** **What**: compute the B(R) span across the {ζ,PV,Mellin} UV-regulator axis at K_horizon at curvature-grade **n=0** (the a₀-grade cosmological-constant counterterm is ADDITIVE-IN-TRACE ⇒ survives the L_emp log-derivative d²/d(ln K)², Sage-exact L_emp(R)−L_emp(0)=Δ_R·d/du[−κ_0'/κ_0²]≠0 — so the regulator difference is NOT annihilated by the W8-2 multiplicative-normalization cancellation). The real CF-S117 L_emp gate. Read the spec from the source CF block. **Source CF blocks**: `workshops/s116-lemp-forced-vs-earned.md §"Carry-Forward Computations"` (W-4, "B(R) three-regulator span; additive-vs-multiplicative decomposition") + `session-116-w7w8-vanishing-test-synthesis.md §V.1` (S-5, "UV-regulator FI/SD of L_emp"). **Regulator-pin discipline**: tag a_n^{ζ}/a_n^{Pauli-Villars}/a_n^{Mellin} per `regulator-pin-discipline.md`. | W-4 workshop + S-5 synthesis |
| 6-3 | `CF-S117-FB-EDGE-VS-BOTTOM` | **What**: ζ/PV α functional-sensitivity cross-check on the existing L12/L14 caches — the FB edge-vs-bottom decomposition (W8-1's Friedrich-Bär label was MIS-SCOPED at the λ_max edge: s=3≡a₂≡n=2 is a UV/small-σ pole NOT bottom-localized; FB-A (bottom-K exact) vs FB-B (Level-2 convergence) conflated; correct argument = Mellin-cone shell-sum s>d_eff/2 + Casimir-decay). INFO + numbers UNAFFECTED; additive §VII.AU.OP-PROJ annotation. Read the spec from the source CF block. **Source CF block**: `session-116-w8w9-FB-scope-synthesis.md §V.1` (S-6). | S-6 synthesis |

*Wave-6 split candidate: {6-1} (secondary-class FORCED) | {6-2,6-3} (UV-regulator span + FB scope). Note 6-1 and 6-2 are ORTHOGONAL axes (secondary-class vs UV-regulator) — author both; do not conflate.*

---

## Wave 7 items (volovik-superfluid-universe-theorist) — w0 transport-degree & categorical-wall

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 7-1 | `CF-S117-W0-TRANSPORT-DEGREE` | **What** (S-7; subsumes CF-S117-W0-ANCHOR-FIDELITY per dedup #1): extract the w0 BZ→pivot morphism degree. w0 (d_A=0, single-pole s=3) is favored deg=0 T2-VACUOUS scalar ⇒ substrate=pivot=−0.918; the W9 →−1.341 gap is PROXY-ARTIFACT-TYPED (λ_max edge not an admissible §23 morphism). **Gate**: deg=0 ⇒ confirm (no §23 K-advance; the −1.341 is a proxy artifact); deg≠0 ⇒ candidate §23 K=3. (d_A=0 does NOT force deg=0 — A_s is deg=+2 via the square; this is a genuine extraction.) Read the spec from the source CF block. **Source CF block**: `session-116-w9-w0-transport-degree-synthesis.md §"Carry-Forward Computations"` (S-7). **Cross-link**: `cross-pillar-bridge-anatomy.md §"Per-observable transport-degree scale-separation"` (§23). | S-7 synthesis |
| 7-2 | `CF-S117-W0-CATEGORICAL-WALL-GRADE` | **What** (W-5): can the w0∉Tr f(D_K) categorical wall upgrade to theorem-grade via a static-a₀ vs dynamical-EoS-response separation? (W-5 closed branch-iv CLOSED-WITH-RESULT: w0=−0.918 is a Level-1 closed-form thermodynamic identity — Volovik partition + effacement, Gate:None — NOT spectral-action-derived; does NOT join {n_s,m_H,r}.) Read the spec from the source CF block. **Source CF block**: `workshops/s116-w0-spectral-derivability.md §"Carry-Forward Computations"` (W-5). | W-5 workshop |
| 7-3 | `CF-S117-BRANCH-IV-L16` | **[OPTIONAL — value-neutral L_max diagnostic, NOT a PASS/FAIL gate; downgraded per dedup #3]** **What**: extend the branch-(iv) w0 spread_CAC to the sliding window {14,15,16} by building the p+q=16 FB-bounded shell (17 sectors (0,16)…(16,0)); test whether \|d\|~1/λ_max² deceleration continues and the spread keeps narrowing. **Inputs**: `s106_w1_highl_cache_l1416.npz`; `s105_branch_iv_direct_l1314.py` (GT builder + Zubarev); GT-pure (16,0)/(0,16) builder + Casimir-projection for the 15 mixed sectors. **Gate**: spread_CAC{14,15,16} vs the UNCHANGED W5-2 band + decrement-deceleration [SIGN] — but per W-5 this is a value-neutral L_max diagnostic (the corridor is CLOSED-WITH-RESULT), so report as diagnostic, not as a corridor-reopening PASS/FAIL. **Effort**: medium-high (one FB-bounded shell build, ~1.5–2h GPU). **Agent_type: baptista-spacetime-analyst.** | w9 WP CF block (downgraded) |

*Wave-7 split candidate: {7-1,7-2} (transport-degree + categorical wall, the live successors) | {7-3} (optional diagnostic). 7-1 and 7-2 are the live successors of the W9 w0 cluster; 7-3 is optional.*

---

## Wave 8 items (landau-condensed-matter-theorist) — §VII.AJ STATE-PROJ inter-summand

| # | Gate ID | Scope | Source |
|:--|:--------|:------|:-------|
| 8-1 | `CF-S117-STATEPROJ-INTER-SUMMAND` | **[productive Track-A path]** **What**: compute the inter-summand state-pair asymmetry R_summand=(a_ℍ−b_{M₃})/(a_ℍ+b_{M₃}) between the ℍ and M₃(ℂ) algebra summands at the COMMON substrate gap Δ_BCS — sidestepping the no-A-sector obstruction (the asymmetry is between two summands the substrate DOES carry, not A/B phases it does not). Track-A-eligible (no lab SC ratio injected). **Inputs**: `s84_spectrum_cache_L12_tau019.npz`; the A_K=ℂ⊕ℍ⊕M₃(ℂ) sector central projections (from S116-W5-BIMODULE-H); Δ_BCS canonical. **Gate** (composite G1∧G2): G1 = R_summand computed substrate-first (Track A); G2 = R_summand sign+magnitude reported with the inter-summand interpretation (a genuine substrate-IS STATE-PROJ observable even if it does NOT image the 3He A/B asymmetry). **Effort**: medium. **NOTE**: `CF-S117-STATEPROJ-SC-FROM-SUBSTRATE` is HIGH-RISK structurally-blocked (no intrinsic 3He-A sector; single BDI N₃=0) — recorded as a standing gap, NOT planned. | w7 WP CF block |
| 8-2 | `CF-S117-STATEPROJ-OPSTATE-COVARIATION` (CF-W7-1) | **[OPTIONAL low-leverage verification gate]** **What**: quantify the residual OP-PROJ↔STATE-PROJ partial-collapse — the co-variation in the overall-spectrum subspace under {ξ_k}/L_max/τ-moduli deformation (both W7 agents agree BENIGN; quantifying it is a numerical bound, NOT an adjudication). **Inputs**: `s116_w7_stateproj_bcs.npz` (R_STATE, R_BdG, OP-PROJ R_∞); §VII.AJ STATE-PROJ + OP-PROJ observables; {ξ_k}/L_max/τ-moduli family. **Gate**: a numerical bound on the co-variation; PASS if bounded below a pre-registered threshold (benign CONFIRMED); INFO if loose. **Effort**: ~0.5 agent LOW. | w7 WP CF block (CF-W7-1) |

*Wave-8 split candidate: {8-1} (inter-summand, productive) | {8-2} (optional co-variation bound).*

---

## Wave 9 items (mack-cosmic-bridge) — e-fold substrate obligations (replace the retired N_e≥3.1)

W-3 workshop (`workshops/s116-efold-binding-vs-container.md`) DISSOLVED N_e≥3.1 as the e-fold COUNT (category-(C) inflation-mechanism intermediate per `phononic-framing.md` IS-NOT-IN A/B/C) but KEPT the genuinely-binding OBLIGATIONS it proxied. Horizon DISCHARGED (S85). These two are the surviving substrate-native obligations — **read the spec for each from `workshops/s116-efold-binding-vs-container.md §"Carry-Forward Computations"`.**

| # | Gate ID | Scope (one-liner; full spec in the W-3 source CF block) | Source |
|:--|:--------|:------|:-------|
| 9-1 | `CF-S117-A2-OMEGAK-ACOUSTIC-FORM` | flatness obligation: a₂-Ω_k=0 via acoustic-form ∧ uniform conformal factor | W-3 workshop |
| 9-2 | `CF-S117-TRANSIT-PS-67-WINDOW-WIDE` | scale-range obligation: TRANSIT-PS-67 window-wide (OPEN/CRITICAL) | W-3 workshop |

*Wave-9 split candidate: {9-1} (flatness) | {9-2} (scale-range). 9-2 cross-links the A_s/TRANSIT-PS backbone (Wave 1).*

---

## Standing gaps (high-leverage, NO tractable pre-registrable gate this session — leverage ≠ tractability; NOT wave gates)

- **atlas-04 C2 / K_pivot scale mapping** (K=2.0 M_KK tessellation → CMB K*≈0.087 M_KK) — "the single largest observational load-bearing gap"; CLOSED-PERMANENT-external on mag + id legs (S113), ratio open; no mechanism places K at K*. (open-channel-ledger §A1.)
- **τ_fold = 0.190 / moduli selection** — equilibrium one-loop + variational corridors FAILed S95; route is dynamical-relaxation OR accept τ_fold empirical. No pre-registrable selection gate. (atlas-04 A4 / T5.)
- **Born rule (L²-norm measurement weight)** — INPUT no-go (Gleason ⇒ consistency not derivation); GGE geometric-non-locality derivation UNCOMPUTED. (open-channel-ledger §A5.)
- **`CF-S94-W5-3-FWDC1-ASYMPTOTIC`** — FWD-C1 Level-2 asymptotic α at L>14: FEASIBILITY-GATED (blocked on the L>14 irrep-construction wall; super-polynomial at p+q≥13). Re-registered, not dispatchable.
- **`CF-S117-STATEPROJ-SC-FROM-SUBSTRATE`** — substrate-first 3He A/B strong-coupling corrections: HIGH-RISK structurally-blocked (single BDI N₃=0, no intrinsic A-sector). Routed to the inter-summand path (8-1) instead.

---

## Q2 / plan-author-applied reconciliations (no separate gate)

- **CF-W9-1** (dedup #1): treat `W0-ANCHOR-FIDELITY` and `W0-TRANSPORT-DEGREE` as ONE compute — APPLIED (gate 7-1). No double-listing.
- **CF-W1-2**: downstream consumers cite the 2-member 𝒩-gap {+0.196,+0.864} as the live A_s plurality, NOT CF3's "two-cluster axis confirmed" (the adiabatic half is workshop-demoted) — APPLIED in the Wave-1 framing.
- **CF-W2-2** (dedup #5): `SEESAW-RESONANCE-MR-SEARCH` anchored on the S-3 fiber-spectrum M_R form — APPLIED (gate 2-3).
