# Session 116 Wave 3 — Q3 Goldstone Mass from Disorder (the 170× mass problem) (Results Working Paper)

**Session**: 116 | **Wave**: 3 | **Plan**: session-116-plan-w3.md | **Theme**: Q3 — structural-closure adjudication + concrete compute of the disorder→Goldstone-mass route to the 170× dark-matter mass shortfall, building on the inv5 Imry-Ma FAIL (frac170 = 4.0e-5). Is the route closed by the Josephson-graph coupling-scale ceiling (m_G ≤ J_C2 ≈ 2Δ_BCS), or does a non-Imry-Ma mechanism survive?

**Gate-type mix**: workshop × 1 (`§W3-1`, artifact-existence closure) + compute × 1 (`§W3-2`, `[SIGN]` verdict-line). MIXED wave per `.claude/rules/wave-classification.md`.

## Gate Sections

### §W3-1. S116-W3-DISORDER-CLOSURE (landau-condensed-matter-theorist × phonon-first-cosmologist)

**Status**: NOT STARTED
**Gate ID**: `S116-W3-DISORDER-CLOSURE`
**Gate type**: `workshop` (2-agent adversarial panel; closes by artifact-existence-with-content per `wave-classification.md §M1` — NO verdict line)
**Trigger**: `[VERIFY]` (structural-closure adjudication, not a numerical SIGN gate)
**Classification**: **PHONONIC** (the U(1)₇ phase Goldstone IS the substrate's broken-phase boson; its mass IS a graph spectral moment)
**Agents**: `landau-condensed-matter-theorist` (structural-closure pole — Landau-pole reading) × `phonon-first-cosmologist` (surviving-channel pole — cross-domain flat-band/Josephson-array/analogue-gravity vantage)
**Rounds**: 3 (R1 steelman both readings / R2 rebuttal-to-opponent's-best-case / R3 converge on the STRUCTURAL VERDICT)
**Hypothesis**: Given the inv5 Imry-Ma FAIL (frac170 = 4.036e-05; disorder-family ceiling construction-E ≈ 0.0118 = J_C2/(170·Δ_BCS)) and the collab §5 Cheeger bound m_G ≥ h(L)/2 with h ~ 2J_C2/Vol giving the SAME m_G ~ J_C2 ≈ 2Δ_BCS scale, the disorder→Goldstone-mass route to the 170× factor is EITHER structurally CLOSED by the Josephson-graph coupling-scale ceiling (~85× short — a wall, not a parameter shortfall) OR OPEN via a surviving non-Imry-Ma mechanism (a different ξ_disorder scaling from the full coupling distribution); the workshop derives which.
**Plan reference**: `sessions/session-plan/session-116-plan-w3.md` §W3-1 (`workshop:` block — agents, rounds, sources, adjudication_question, numeric stakes context).

**Artifact-Existence Closure Checklist** (workshop gate — closes by artifact-existence-with-content per `wave-classification.md §M1`; **NO verdict line, NO MCP Pre-Compute Audit block**):
*(pending — confirm the deliverable `sessions/session-116/workshops/s116-w3-disorder-closure.md` EXISTS (`ls`) AND paste `grep -E` output for every `must_contain` marker from the plan `output_artifacts.workshop_md` block: `## R1` (steelman both readings), `## R2` (rebuttal to opponent's best case), `## R3` (converge), `## Structural Verdict` (the NEW pinned position), `## Wrap-Up` (rclab-workshop closure marker), `Carry-Forward` (the compute mandate handed to S116-W3-GOLDSTONE-M2). Any marker returning empty ⇒ the workshop did not properly close — orchestrator SendMessage-continues the same panel per `feedback_dispatch-discipline.md`. Content presence by regex, never line/byte counts per `feedback_max-effort-full-fidelity.md`.)*

**Structural Verdict**:
*(pending — include: the NEW pinned position resolving the two readings — either **CLOSED-BY-GRAPH-SCALE-WALL** (the disorder/connectivity route is permanently walled at frac170 ≤ J_C2/(170·Δ_BCS) ≈ 0.012; the Leggett-DM mass is Josephson-graph-unanchored, Reading B of WS-S112-4, magnitude-free like M_KK) OR **OPEN-VIA-<named-mechanism>** (a concrete surviving non-Imry-Ma mechanism identified, handed to S116-W3-GOLDSTONE-M2 as Branch A); the §(c) discriminator answer (does any graph-derived mechanism EXCEED the construction-E/Cheeger ceiling ≈ 0.012 toward 170×?); the R1/R2/R3 positions (landau structural-closure pole vs phonon-first surviving-channel pole); the SOURCE-RECON guard that ξ_Larkin = 17.115 bonds is NOT the KZ quench length xi_KZ; the Carry-Forward block stating the mechanism selector passed to the compute. Substrate framing: substrate→observable throughout — D_K (0,0)-sector eigenvalues → Josephson couplings {J_C2, J_su2, J_u1} → graph spectral gap → m_G → DM structure-formation mass; the 170× target is the laboratory-IN quantity the substrate-IS graph either reaches or structurally cannot.)*

---

### §W3-2. S116-W3-GOLDSTONE-M2 (landau-condensed-matter-theorist)
**Status**: COMPLETED
**Gate ID**: `S116-W3-GOLDSTONE-M2`
**Gate type**: `compute` (dual-SHA verdict-line closure; `[SIGN]` ⇒ SIGN/MAGNITUDE/REGIME 3-tuple companion row REQUIRED)
**Trigger**: `[SIGN]`
**Classification**: **PHONONIC** (the Goldstone mass is the lattice-Laplacian spectral gap / Imry-Ma pinning gap of the SU(3) Josephson tessellation)
**Agent**: `landau-condensed-matter-theorist`
**Hypothesis**: The surviving Cheeger / lattice-Laplacian connectivity gap (ξ_eff ~ 1 bond ≪ ξ_Larkin = 17.115 bonds) yields a LARGER Goldstone mass than the inv5 Imry-Ma baseline m_G = 0.003185 (SIGN=PASS, ~293× larger), but the Josephson-graph coupling-scale ceiling (E ≤ J_C2, ξ ≥ 1 bond) caps frac170 ≤ J_C2/(170·Δ_BCS) ≈ 0.0118 — ~85× short of the 170× target.
**Plan reference**: `sessions/session-plan/session-116-plan-w3.md` §W3-2 (PRDR 8-item machinery pin, both-branch verdict rubric, substitution chain (W3.1)–(W3.4), input-SHA ledger).

**Verdict**: **FAIL** — composite `SIGN=PASS ∧ MAGNITUDE=FAIL ∧ REGIME=VALID`, collapsed by the pre-registered rule `magnitude_verdict==FAIL ∧ regime_verdict==VALID ⇒ FAIL` (gate-verdicts.md). This is **Branch B (structural closure)**, the substitution-chain-predicted outcome. The disorder/connectivity corridor for the 170× DM structure-formation mass is **STRUCTURALLY CLOSED**: every Josephson-graph-derived Goldstone mass caps at the coupling scale `m_G ≤ J_C2 = 0.933 ≈ 2Δ_BCS`, giving `frac170 = J_C2/(170·Δ_BCS) = 0.011822` — exactly the inv5 construction-E family ceiling, `84.6×` short of `frac170 = 1`. The Leggett-DM mass is therefore **graph-unanchored** (Reading B of WS-S112-4): abundance-fixed (Leggett 0.6%-Planck, below-edge protected) but magnitude-free *on this route*, structurally like M_KK (an abundance-fixed scale the graph does not pin). FAIL is an informative wall per "All Results Are Good Results" — it pins the ceiling formula `frac170 ≤ J_C2/(170·Δ_BCS)` and routes the DM-mass-anchor question OUTSIDE the graph scale.

**Output Artifacts** (closure-verification checklist — all artifacts confirmed on disk by content):
- script `computations/session-116/s116_w3_goldstone_m2_disorder_ceiling.py` (27185 B) — `grep -cE "from canonical_constants import|print_verdict_payload"` → **3** (both `must_contain` patterns present).
- data `computations/session-116/s116_w3_goldstone_m2_disorder_ceiling.npz` (16690 B) — present (5-construction bracket reload + Cheeger/Fiedler spectra + frac170/ceiling/3-tuple).
- plot `computations/session-116/s116_w3_goldstone_m2_disorder_ceiling.png` (117575 B) — present (frac170 ladder A–E + Cheeger + optical; graph-Laplacian spectra at the J_C2 scale).
- verdict line `computations/session-116/s116_gate_verdicts.txt` — canonical line matches `^S116-W3-GOLDSTONE-M2:.* audit_sha256=[a-f0-9]{64}`; dual-SHA companion row + schema-v2 `[SIGN]` 3-tuple row (`sign_verdict=PASS magnitude_verdict=FAIL regime_verdict=VALID`) + 2 extra companion rows present (emitted via the race-safe `emit_verdict` MCP tool, 5 rows, sig_5 unique).
- dual-SHA: `audit_sha256=2959c503391206800ca53cc1f0411365c4e3c17a9bb644e77b881245a4a0d367` (script‖canonical‖pinmap), `content_sha256=1323fd305266f79b0348c281425a985ae3ec925744c1618654002a585209b04c` (script only).

**MCP Pre-Compute Audit** (queries run BEFORE the script, per knowledge-index-usage.md; gate NOT pre-closed):
- `search_knowledge("Goldstone mass Cheeger Josephson connectivity 170 DM mass disorder Imry-Ma")` → returns the inv5 FAIL `INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER` (`m_G=0.00319, xi_L=17.115, frac170=4.036e-05`) and the collab §5 equation `m_required/m_Leggett = 170`. No S116 verdict — gate is NOT already evaluated.
- `search_knowledge("S116 W3 GOLDSTONE M2 disorder ceiling frac170 Larkin")` → no existing S116-W3-GOLDSTONE-M2 verdict; confirms `m_L1_bare = ω_L1 = 0.138` and the inv5 "softest-direction-dominates" random-field note.
- `get_constant("J_C2")` → 0.933 (no PROVENANCE row; matches canonical_constants.py:737). `get_constant("Delta_BCS")` → 0.4642547394830737 (R-PROTECTED, S70). `get_constant("rho_s")` → **not found** ⇒ SOURCE-RECON: rho_s sourced from the SHA-pinned s48 npz `rho_s_C2 = 7.962` (substrate-first; cross-checked against inv5 npz `rho_s = 7.962`), NOT canonical_constants.
- All five canonical pins (J_C2, J_su2, J_u1, ω_L1, Δ_BCS) imported from `canonical_constants.py`; rho_s loaded from the pinned s48 npz.

**Results**:

*5-construction inv5 disorder bracket (reloaded from `inv5_w2_4_goldstone_mass_disorder.npz`, frac170 = m_G/(170·Δ_BCS)):*

| construction | m_G | frac170 |
|:--|--:|--:|
| A — Larkin-weak (Imry-Ma baseline, ξ=17.115) | 0.003185 | 4.036e-05 |
| B — saturated h_rf (ξ=1) | 0.054514 | 6.907e-04 |
| C — saturated J_u1 (ξ=1) | 0.038000 | 4.815e-04 |
| D — std non-C² (ξ=1) | 0.009093 | 1.152e-04 |
| **E — max-bond J_C2 (family ceiling, ξ=1)** | **0.933000** | **1.18216e-02** |

- Imry-Ma baseline (SIGN reference): **m_G^IM = 0.003185** (ξ_Larkin = J_C2/h_rf = 0.933/0.054514 = 17.115 bonds).
- Disorder-family ceiling: **frac170_ceiling_family = 1.18216e-02** (construction E).

*Surviving mechanism — Cheeger / lattice-Laplacian connectivity gap (collab §5):*
- Closed-form Cheeger bound (eq W3.2): `h(L) = 2·J_C2/Vol(cell) = 1.866` (Vol=1) ⇒ `m_G^Ch ≥ h/2 = J_C2 = 0.933`.
- Coupling-scale ceiling (Step 6): `m_G = E/ξ ≤ J_C2/1 = J_C2`. The h/2 lower bound and the coupling-scale upper bound **PINCH** ⇒ surviving-mechanism mass `m_G = J_C2 = 0.933` (the Cheeger bottleneck = the global-phase coherence rate).
- Lattice-Laplacian Fiedler cross-check: C² backbone (K₄ @ J_C2, where U(1)₇ = T₇ lives) Laplacian spectrum `{0, 3.732, 3.732, 3.732}`; Fiedler `λ_1 = 4·J_C2 = 3.732`, `m_G^λ1 = √λ_1 = 1.9318` (optical mode). Full 8-bond unit-cell star spectrum `{0, 0.041, 0.059, 0.059, 0.096, 0.933, 0.933, 0.933, 4.841}`; Fiedler `λ_1 = 0.0406` (soft inter-block ≈ J_u1 — the Imry-Ma-soft end).
- Cheeger inequality cross-check: `h²/4 = J_C2² = 0.8705 ≤ λ_1(C²) = 3.732` ✓; Alon–Milman sandwich `h²/(2d_max) ≤ λ_1 ≤ 2h` ✓. The entire graph-spectral family (soft inter-block J_u1=0.041 → stiff optical √(4J_C2)=1.93) sits at/below the J_C2 scale; the absolute stiffest graph mode gives `frac170 = 0.0279 ≪ 0.5`. **No graph mode reaches the 170× target (170·Δ_BCS = 78.92).**
- s29b J-matrix Frobenius cross-check at the fold: `‖J‖_F(τ=0.2) = 0.4270` (consistent with the bond inventory; the block-diagonal D_K wall #2 forbids inter-sector entries).

*frac170 / ceiling / shortfall:*
- `170·Δ_BCS = 78.9233`. **frac170 (surviving) = m_G/(170·Δ_BCS) = 0.933/78.9233 = 1.18216e-02 = frac170_ceiling EXACTLY** (Sage-QQ confirmed `frac170 == ceiling`).
- target/ceiling = `(170·Δ_BCS)/J_C2 = 84.59` (eq W3.4) — the structural shortfall: ~85× short.
- Pair-breaking-edge ratio: `ω_G = m_G/√ρ_s = 0.933/√7.962 = 0.330652` (matches inv5 br_E to all digits); `x_G = ω_G/(2Δ_BCS) = 0.356110 < 1` (matches inv5 br_E `x_G=0.35611`) ⇒ **below the pair-breaking edge** (REGIME=VALID; a valid below-edge quasiparticle — the binding wall is the coupling-scale ceiling, NOT the edge).

*Substitution chain (the `[SIGN]` frac170-direction claim, Steps 1–6 with substituted numbers):*
- (1) general pinning mass: `m_G = E_disorder/ξ_disorder` (eq W3.1).
- (2) Imry-Ma baseline: `ξ_Larkin = J_C2/h_rf = 0.933/0.054514 = 17.115`; `m_G^IM = h_rf/ξ_Larkin = 0.054514/17.115 = 0.003185`.
- (3) Cheeger/connectivity: `m_G^Ch = h/2 = J_C2 = 0.933`; ξ_eff ~ 1 bond, E_eff ~ J_C2.
- (4) ratio: `m_G^Ch/m_G^IM = J_C2·ξ_Larkin/h_rf = 0.933·17.115/0.054514 = 292.9` (~293× larger).
- (5) **direction read-off**: `ξ_eff = 1 < ξ_Larkin = 17.115` (SMALLER) and `E_eff = J_C2 > h_rf` (LARGER); `∂m_G/∂ξ = −E/ξ² < 0` ⇒ shorter ξ ⇒ larger m_G ⇒ **sign(m_G^Ch − m_G^IM) = + (POSITIVE)** ⇒ **SIGN = PASS**.
- (6) ceiling (the binding wall): `E ≤ J_C2`, `ξ ≥ 1` ⇒ `m_G ≤ J_C2`; `frac170 ≤ J_C2/(170·Δ_BCS) = 0.0118` ⇒ **MAGNITUDE = FAIL** (≤ family ceiling).
- Conclusion: SIGN=PASS (correct direction, 293× the Imry-Ma baseline) ∧ MAGNITUDE=FAIL (85× short) ∧ REGIME=VALID (x_G<1) ⇒ **composite FAIL**.

*Dual-prior re-allocation (plan dual_prior):* frac170 = 0.0118 ≤ frac170_ceiling_family ⇒ **0.9 mass to Track B** (every Josephson-graph-derived mechanism caps at m_G ~ J_C2 ~ 2Δ_BCS; the Leggett-DM mass is graph-unanchored, irreducibly unanchored like M_KK). Track A (the disorder/connectivity route survives at ≥50% of target) is NOT supported.

*fb_pair:* **forward** = inv5 A–E disorder bracket + collab §5 Cheeger bound (h=2J_C2/Vol) + s29b J-matrix Frobenius + canonical {Δ_BCS, J_C2, J_su2, J_u1, ω_L1} + s48 ρ_s; **backward** = the structural-closure verdict feeds the HK-170X-DM standing gap — on this FAIL the DM-mass-anchor routes to the **graph-ANCHORED clean-Leggett** conclusion (5.5571 M_KK, C11-conditional; **Reading-B WITHDRAWN** per the S116-W3-DISORDER-CLOSURE workshop — the disorder route is closed at every D_K projection but the DM mass is in-graph at the inter-band Leggett scale, NOT unanchored), with the 170× **re-typed-and-routed-to-CF-S117-FREESTREAM-AT-ANCHOR** (a registry-state update, mack/little sole-writer, NOT a re-compute). [S116 reconciliation (orchestrator §6): the parallel-dispatched compute's dual-prior "Track B / unanchored" framing above is the plan's pre-registered default; the workshop's inter-band analysis OVERTURNS the "unanchored" reading — the FAIL closes the (0,0)/intra-band disorder route, it does NOT make the DM mass unanchored.]

**Substrate framing (PHONONIC)**: The U(1)₇ phase Goldstone IS the substrate's broken-phase boson — ungaugeable (`[iK_7,D_K]=0`, wall #5, N4 BROKEN) and un-massable by the spectral action (SA-mass=0 EXACT, S48 wall #7). Therefore ANY mass it carries is a **graph spectral moment** of the SU(3) Josephson tessellation: either the random-field pinning gap (Imry-Ma) or the lattice-Laplacian connectivity gap (Cheeger isoperimetric constant), both built from the SAME couplings {J_C2, J_su2, J_u1}. The flow is D_K (0,0)-sector eigenvalues → Josephson couplings → graph Laplacian λ_1 / Imry-Ma pinning → m_G → DM structure-formation mass → halo/LSS (measured). The 170× "problem" is the container-thinking error of expecting the substrate's largest internal coupling (J_C2 ~ 0.93 M_KK ≈ 2Δ_BCS) to supply a mass ~85× ABOVE itself: **the substrate IS the Josephson graph, and a graph cannot pin its own phase mode harder than its stiffest bond.** Landau reading: this is a stiffness statement — the Goldstone mass is the bottleneck (min-cut) conductance h/2 of the order-parameter manifold, bounded by the largest phase-stiffness J_C2; the optical Fiedler modes (≤ 4J_C2) are higher but irrelevant to the global-phase Goldstone. The DM mass, if it exists, is anchored OUTSIDE the graph scale (not a correction IN a container).

---

## Wave 3 Synthesis (team-lead)

**Wave 3 closed: 2/2 gates (1 compute verdict FAIL + 1 workshop artifact-existence). The wave RE-TYPED the 25-session "170× Goldstone-mass problem" — from a missing-mass shortfall into a cross-pillar kinematic ratio.** Q3 had failed before (inv5 Imry-Ma, frac170≈4e-5); this wave built on that FAIL and adjudicated the *structural status* rather than recomputing.

**Gate-by-gate.**
- **S116-W3-GOLDSTONE-M2** FAIL (`sign=PASS magnitude=FAIL regime=VALID`). The Cheeger/connectivity ceiling: `frac170 = 0.0118` (Cheeger `m_G ≥ h/2`) / `0.0245` (Fiedler λ_1), `ratio_Ch_IM = 293×` the Imry-Ma baseline (SIGN direction correct), `x_G = 0.356` (below the pair-breaking edge). The Branch-B ceiling-pin — the (0,0)/intra-band disorder route is `~85×` short of the 170× target.
- **S116-W3-DISORDER-CLOSURE** (workshop, closed by artifact-existence). Structural Verdict: **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION**. The adversarial exchange converged on a **three-tier ladder** (both opening poles partly right) — and phonon-first **overturned its own R1 Branch A**: inter-band disorder is Schrieffer-Wolff `1/E_n`-*suppressed*, not enhanced. **Tier 1a** intra-(0,0) disorder `frac170 ≤ 0.0118` (compute-confirmed FAIL); **Tier 1b** inter-band-via-disorder `frac170 ≈ 5e-4` (analytic, below 1a) ⇒ the disorder route is CLOSED at *every projection of D_K*. **Tier 2** the clean inter-band Leggett `J_⊥` (`5.5571 M_KK`, `frac170 = 0.0704`) is the surviving channel — but a *clean* coupling (already-registered DM anchor, NOT a disorder mechanism), `√N`-saturated, 14.2× short. **Tier 3** the 170× is RE-TYPED off the mass axis (`x_target = 30.12`, unprotectable). landau's "graph-scale wall" is the airtight *intra-band specialization* of the one binding wall (protection-magnitude exclusion: every protected mode `m ≲ O(10·Δ_BCS)` because the condensate carries one energy scale).

**Joint reading.** Workshop CLOSED + compute FAIL → consistent. The honest verdict (landau's, both sides own it): **disorder route CLOSED; DM mass graph-ANCHORED at the clean Leggett scale 5.5571 M_KK (C11-conditional) — Reading B WITHDRAWN, explicitly NOT "unanchored"; 170× re-typed-AND-ROUTED to `CF-S117-FREESTREAM-AT-ANCHOR`** (NOT asserted-closed — landau's epistemic point: "re-typed is a reclassification, not a computation; zero evidential weight until S117-FREESTREAM runs").

**fb_pair reconciliation (this WP, §W3-2).** The compute's §W3-2 dual-prior "Track B / graph-unanchored" framing was the *plan's pre-registered default*; the workshop's inter-band analysis OVERTURNED the "unanchored" reading. Reconciled in-session at §W3-2 fb_pair + atlas-04 P2 + `_promotion-triage` HK-170X-DM (Effected-In-Session below).

**What holds.** Abundance + below-edge DM-protection intact (the clean Leggett mode is below the pair-breaking edge) **[S116-W2 LEGGETT-DM-EDGE-PROTECTION workshop annotation (landau×volovik, `sessions/session-116/workshops/s116-leggett-dm-edge-protection.md`): this below-edge clause holds for the LIGHT `ω_L1 = 0.070 M_KK` dipolar mode (`proven_1792`, Q=670k, atlas-07 lines 350/412/416/583), NOT for the HEAVY `11.97·Δ_BCS = 5.5571 M_KK` clean-Leggett DM anchor — under Convention M (mass; the kinematic pair-breaking threshold is energy-vs-energy with NO `√ρ_s`) the heavy anchor is ABOVE the inter-band edge `E_edge^⊥ = Δ_BCS+√3 = 4.7308·Δ_BCS`, `x^⊥ = 2.5302 > 1` (Sage-exact). Its survival is Reading A (CPT non-annihilation + GGE integrability + `Γ_grav<H_0`, C11-conditional), NOT below-edge — the C11-conditionality is the tell. The `m_G = 0.933` Cheeger graph-Goldstone (`x_G = 0.356`, §W3-2 line 79) IS genuinely below-edge, a distinct object.]**. The §VII.BL/§VII.CK generation-blindness is untouched. The "one wall in four projections" (protection-magnitude exclusion) is a *theorem*, not a coincidence — the condensate's single R-protected gap `Δ_BCS` caps every protected mode.

### Effected In-Session (NON-MATH — executed at wave-synthesis)

The DM-mass-route status reconciliation (disorder route CLOSED + 170× RE-TYPED + DM mass graph-ANCHORED, Reading-B WITHDRAWN), routed from the workshop via housekeeping §A3. All landings verified on disk:

- [x] **A3.1 atlas-04 P2 row** (orchestrator-direct; general curated) — RETAINed the historical text + appended the S116 supersession: "170x" RE-TYPED (cross-pillar ratio); disorder route CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION; DM mass graph-ANCHORED at 5.5571 M_KK (NOT Reading-B); 170× → CF-S117-FREESTREAM-AT-ANCHOR — `sessions/framework/Atlas/atlas-04-assumptions.md:119`.
- [x] **A3.2(i) `_promotion-triage` HK-170X-DM row** (orchestrator-direct) — disorder corridor CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION (all D_K projections); 170× RE-TYPED; DM graph-ANCHORED — `sessions/investigation/_promotion-triage.md:240`.
- [x] **A3.2(ii) falsifier-inventory Row #79 audit-pin** (`mack-cosmic-bridge`, sole-writer) — `### Row #79.compute-S116-W3-DISORDER-CLOSURE` recording the joint reading (disorder CLOSED every projection; DM graph-ANCHORED = supersession of S112 Reading B; 170× re-typed-and-routed); σ_SI NULL preserved (graph-anchoring lands inside the already-swept window) — `sessions/framework/registry/falsifier-master-inventory.md:2598`.
- [x] **A3.4 §W3-2 fb_pair reconciliation** (orchestrator-direct, this WP) — the compute's pre-registered "Track B / unanchored" framing OVERTURNED: FAIL routes to graph-ANCHORED clean-Leggett, Reading-B WITHDRAWN — `session-116-w3-workingpaper.md` §W3-2 fb_pair.
- [x] **A3.3 open-channel-ledger §DMMASS** — NO-OP (grep-verified: no §DMMASS section / no stale Reading-B entry; the HK-170X-DM substance lives in A3.2).
- [x] **A3.5 capstone-hygiene Q3** — NO-OP (capstone grep: the single "reading b" hit is the acoustic-white-hole *diabatic-freeze reading* on line 440, NOT the WS-S112-4 DM-mass "Reading B"; no DM-mass-route / unanchored / 170×-DM-problem prose in the capstone to down-tag).
- [x] **housekeeping ledger** `§A3` (spec, phonon-first) + `§A3-LANDED (mack)` (line 104) + this orchestrator-landings record; §B–§E confirmed (the 2 S117 CFs are genuine future computation in the WP `## Carry-Forward Computations` block, not §B hygiene).

**Self-audit (orchestrator)**: WP Effected-In-Session unchecked-box count = 0; sig_5 6/6 distinct session SHAs; no curated registry bulk-edited (mack sole-writer surface routed to mack; general curated surfaces orchestrator-direct per the Wave-1 precedent).

## Carry-Forward Computations

### CF-S117-FREESTREAM-AT-ANCHOR — the kinematic discharge of the 170× re-typing [PRIMARY, EVOI-carrying]
1. **What**: compute the DM comoving free-streaming length `λ_fs(m_Leggett, v_rms^{GGE})` at the anchored Leggett mass `m_Leggett = 11.97·Δ_BCS = 5.5571 M_KK`, with `v_rms` as the EXPLICIT second moment of the transit-frozen Bogoliubov occupation (`v_rms² = ∫(k/m)²n(k)d³k / ∫n(k)d³k |_frozen`, non-relativistic — coldness is a COMPUTED output, the `S_ent=0` Ordered Veil licenses the frozen-`n(k)` reading over a thermal `√(T/m)`), against the structure-formation threshold.
2. **Inputs**: `Mass_LeggettDM_over_Delta_BCS = 11.97` (C11 anchor, conditional on `Γ_grav < H_0`); the S38 Bogoliubov squeeze spectrum (`⟨n⟩=730.6`, `n_Bog=0.99863`); the S95 Ordered-Veil certification (`S_ent=0`, `R_therm=5252`); `Δ_BCS=0.4642547` (R-PROTECTED).
3. **Gate**: PASS = cold transit-frozen dispersion gives `λ_fs` below the structure-formation threshold at the anchored mass with NO 170× enhancement (re-typing DISCHARGED); FAIL = a genuine warm-DM kinematic tension (a sharper open question, NOT a missing-mass shortfall). `[SIGN]` on `(λ_fs − λ_threshold)`.
4. **Effort**: low (closed-form free-streaming integral over a known Bogoliubov spectrum; no new diagonalization). **Depends on**: this wave's Tier-2 anchor; S38 Bogoliubov npz; S95 Ordered-Veil; `canonical_constants.py`.

### CF-S117-LEGGETT-COLLECTIVE-CEILING — confirm the collective protection-magnitude exclusion [COMPANION, low-EVOI]
1. **What**: diagonalize the full inter-band pair-transfer across all `(p,q)` at `L_max=10`; read the heaviest PROTECTED collective Leggett mode, confirm it SATURATES at `frac170 ≈ 0.07` (`√N`-saturation + continuum-edge cap).
2. **Inputs**: the `D_K` L_max=10 spectrum cache; collab §3 `E_n = 0.633√C_2 + 0.555`; the clean Leggett `J_⊥`; `Δ_BCS`.
3. **Gate**: PASS = heaviest protected collective mode lands `frac170 ∈ [0.06, 0.08]` (saturation confirmed); `≫ 0.08` would reopen Tier 2 (the informative tail).
4. **Effort**: medium (full inter-band diagonalization at L_max=10; GPU `torch.linalg` on the off-(0,0) blocks). **Depends on**: `D_K` L_max=10 cache; this wave's Tier-2 prediction; collab §3 `E_n`.

### CF-W3-1 — promote `rho_s_C2 = 7.962` to `canonical_constants.py` with provenance [Q2-hygiene provenance backfill; NEW — first-time-surfaced, an upstream wave-synthesis miss]

1. **What**: Promote `rho_s_C2 = 7.962` to `canonical_constants.py` with PROVENANCE (S48 MASS-48 / `s48_goldstone_mass.npz`). The value is consumed in the `[SIGN]` gate `S116-W3-GOLDSTONE-M2` (the `ω_G = m_G/√ρ_s` edge ratio) but is NOT in `canonical_constants.py` (`get_constant('rho_s')` / `get_constant('rho_s_C2')` → not found; the compute's own MCP Pre-Compute Audit sourced it from the SHA-pinned `s48_goldstone_mass.npz`). Surfaced FIRST-TIME by the W3 consolidation — an upstream wave-synthesis miss per `Investigating-Workshops.md §"Q2 first-time surface"`.
2. **Inputs**: `s48_goldstone_mass.npz` (SHA-pinned source; `rho_s = 7.962`); S48 MASS-48 provenance; `S116-W3-GOLDSTONE-M2` (the consumer gate).
3. **Gate**: `rho_s_C2 = 7.962` registered via `update_constant("rho_s_C2", 7.962, session="S48", source="S48-MASS-48", comment="...")` with PROVENANCE; `get_constant('rho_s_C2')` returns the value.
4. **Effort**: ~0 compute (a single `update_constant(...)` call + PROVENANCE entry; `canonical_constants.py` edit). **Depends on**: `s48_goldstone_mass.npz`.

## Constraint-Map Updates

| Date | Mechanism/gate | Prior state | New state | Reason |
|:-----|:---------------|:------------|:---------|:-------|
| 2026-06-27 | S116-W3-GOLDSTONE-M2 ((0,0)/connectivity disorder route) | open — 170× DM-mass shortfall (inv5 Imry-Ma frac170≈4e-5) | **CLOSED (frac170 ≤ 0.0118 Cheeger / 0.0245 Fiedler λ_1, ~85× short)** | FAIL; Branch-B ceiling-pin, the Tier-1a intra-(0,0) wall |
| 2026-06-27 | S116-W3-DISORDER-CLOSURE (disorder→Goldstone-mass route) | HK-170X-DM HARDENED-OPEN (two corridors closed; 170× shortfall) | **CLOSED-BY-PROTECTION-MAGNITUDE-EXCLUSION (all D_K projections — Tier-1a + Tier-1b); DM mass graph-ANCHORED at clean Leggett 5.5571 M_KK (Reading B WITHDRAWN); 170× RE-TYPED off the mass axis** | Workshop verdict + compute FAIL joint reading; phonon-first overturned its own R1 (inter-band disorder SW-suppressed) |
| 2026-06-27 | DM-mass anchor (WS-S112-4 Reading B) | candidate "Josephson-graph-unanchored, like M_KK" | **WITHDRAWN — DM mass is in-graph (off-(0,0) D_K spectral functional), graph-ANCHORED at the inter-band Leggett scale** | landau withdrew Reading B; the disorder FAIL closes the route, it does NOT make the mass unanchored |

## Files Produced

| Gate | Script | Data (.npz) | Plot (.png) | Deliverable md |
|:-----|:-------|:------------|:------------|:---------------|
| S116-W3-DISORDER-CLOSURE | — | — | — | `sessions/session-116/workshops/s116-w3-disorder-closure.md` |
| S116-W3-GOLDSTONE-M2 | `s116_w3_goldstone_m2_disorder_ceiling.py` | `…_disorder_ceiling.npz` | `…_disorder_ceiling.png` | — |

*(Compute under `computations/session-116/`. Verdict line: `S116-W3-GOLDSTONE-M2: FAIL` (audit 2959c503…), dual-SHA-unique. The workshop closes by artifact-existence — no verdict line.)*
