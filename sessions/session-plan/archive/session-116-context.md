# Session 116 — Planner Context (open-question exploration)

**Date**: 2026-06-27
**Mode**: SESSION (session-116 namespace) with **mixed gate types** per wave (workshop + compute), per user directive ("a wave each… in-wave workshops, and computes").
**Scope source**: user-supplied 9-question open-question table (NOT mined WP carry-forwards). The table IS the scope — analog of WP carry-forwards. Each question → one wave. Owner = the domain specialist matched to the question's substrate.
**Gate-type machinery**: each wave carries `gate_type ∈ {workshop, compute}` per gate, per `.claude/templates/plan-investigation.md §"Mixed gate types"`. Verdict path for COMPUTE gates = `computations/session-116/s116_gate_verdicts.txt` (session track, NOT investigation track). WORKSHOP gates close by artifact-existence into `sessions/session-116/workshops/{slug}.md` (no verdict line).
**Planner discipline**: every per-wave planner MUST query the knowledge MCP for its question's entities before writing gate blocks (`search_knowledge` / `trace_entity` / `get_constant`). The grounding below is the ORCHESTRATOR's pre-flight; the planner deep-queries the derivation inputs.

---

## CRITICAL GROUNDING CATCHES (the user's table is staler than the repo on three questions)

These were caught at plan-freeze by knowledge-MCP grounding. Each per-wave planner MUST build on the TRUE prior state, not the table's "never computed" framing — re-deriving settled work is the rediscovery failure mode the query-first rule exists to prevent.

1. **Q3 (Goldstone mass) WAS computed and FAILED** — `INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER` (investigation-5): `enh=0.0231, x_G=0.0012, m_G=0.00319, xi_L=17.115, leg1=NEG, leg2_belowedge=True, frac170=4.036e-05`; scheme=`IMRY-MA-RANDOM-FIELD-GOLDSTONE-MASS`, convention=`DISORDER-LENGTH-FROM-NON-C2-JOSEPHSON-COU`; verdict **FAIL**. The Imry-Ma random-field route reached only 4.04e-05 of the required 170× factor. S116 Q3 = build on this FAIL (alternative disorder mechanism OR structural-closure verdict), NOT a fresh first compute.

2. **Q12 (τ=0 IC) WDW WAS computed and FAILED the e-fold clause** — `INV11-W3-3-WHEELER-DEWITT-PSI-TAU-EFOLD` (investigation-11): `tau_peak=0.0000, N_e_WKB=0.1734, B_WKB=22.2552, gap_to_3.1=2.9266, WKB_defines_time=True, clause_tau=True, clause_efold=False`; scheme=`WDW-minisuperspace`; verdict **FAIL**. The τ-clause PASSED (peak at τ=0); the e-fold clause FAILED (N_e=0.17 vs needed ~3.1). The genuinely-open part is the **boundary condition** (Hartle-Hawking no-boundary vs Vilenkin tunneling), not the WDW operator. Q45 (τ=0 operator canonicity) is OPEN-PENDING-COMPUTE; `S110-CF1-AT-MINISUPERSPACE` returned INFO (`branch=SPLIT; schemes_agree=False`).

3. **Q18b (§VII.CK) shape wall LANDED S114 PASS** — `CF-S114-YUK-SHAPE-WALL-VII-LANDING`: `Tr[g9 D]=0.00e+00, Tr[g9 D3]=0.00e+00, anticomm=0.00e+00, exact=True, slot=VII.CK`; verdict **PASS** (machine-exact). The SHAPE branch is a registered permanent wall ("no G-invariant construction on (A_K,H_K,D_K) supplies a non-monotone sign-changing scalar" — session-112-workshop-schedule). So §VII.CK's leg is a **Stage-2 two-agent cross-axis VERIFY** (per `joint-theorem-promotion.md §"Stage 2"`), NOT a fresh derivation.

---

## Wave assignments (one question per wave)

| Wave | Q | Topic | Owner agent | Gate-type mix |
|:----:|:--|:------|:------------|:--------------|
| 1 | Q23 | Transit power spectrum / A_s normalization (THE critical one) | transit-dynamics-theorist | workshop + compute×2–3 |
| 2 | Q18b | Yukawa hierarchy (shape leg + lepton PMNS) | connes-ncg-theorist | workshop + compute (Stage-2 verify + PMNS texture) |
| 3 | Q3 | Goldstone mass from disorder (170× mass problem) | landau-condensed-matter-theorist | workshop + compute |
| 4 | Q8 | 4D modulus effective action | kaluza-klein-theorist | workshop + compute |
| 5 | Q11 | A_F quaternion (H) extraction | connes-ncg-theorist | workshop + compute |
| 6 | Q12 | τ=0 initial conditions (Wheeler-DeWitt) | quantum-foam-theorist | workshop + compute |
| 7 | Q33 | §VII.AJ.STATE-PROJ derivation | volovik-superfluid-universe-theorist | workshop + compute |
| 8 | Q30 | Forward bridges FWD-C1 / FWD-C2 | connes-ncg-theorist | workshop + compute×2 |
| 9 | Q36 | D_K sectors p+q=15 | baptista-spacetime-analyst | workshop + compute |

---

## Wave 1 — Q23: Transit power spectrum / A_s normalization  [owner: transit-dynamics-theorist]

**Status (true)**: α_s→≈0 and n_s done; A_s normalization is the sole open residual. Parent: `TRANSIT-PS-67` (CRITICAL; resolves α_s 5.0σ, A_s norm, n_s(k) simultaneously). Canonical A_s gap = **3.15 OOM** (`AMPLITUDE-NORM-66`, Route B Peter-Weyl, S66 FAIL-marginal; closed-mechanism `AS-ROUTE-B-PW-S66`). Latest amplitude compute `S110-CF-B1-TRANSITPS` (INFO): `deg_T_BZ_pivot=+2 NON-SCALAR 54.04dec; amplitude[inv5_OOM=+0.86, inv6_OOM=+1.455]`.

**n_s scheme split (reconciliation sub-item)**: user cites n_s=0.9590; this is `n_s_FW_sqrt_cutoff = 0.959`. The other framework value is `n_s_framework = 0.9561`. Planck is `n_s_canon = 0.9649`. These are regulator-scheme variants, NOT a contradiction — declare both with their cutoff scheme.

**CF21 contradiction (the user's "2.38 vs 4.56 OOM, line 337")**: `CF21 = TD/LI Mukhanov-Sasaki H̃-branch divergence chase`. S82 W-1 H̃-DIVERGENCE-CHASE workshop opened a **2.38-OOM** gap; the figure **drifted to 4.56-OOM** (atlas-08-freshness-S97: "STILL OPEN, figure drifted → 4.56-OOM; the rate-limiting open question for A_s closure since S84 retracted branch-(iv)"). So three OOM numbers live on adjacent observables: 2.38 (H̃-branch S82), 3.15 (A_s Route B PW S66), 4.56 (drifted figure).

**Items**:
- **WORKSHOP** (`gate_type: workshop`, 2 agents): adjudicate the H̃-branch figure drift. Agents: `transit-dynamics-theorist` (TD/Bogoliubov side) vs `mack-cosmic-bridge` (observational A_s side). Adjudication question: *"On the Mukhanov-Sasaki H̃-branch, is the canonical OOM gap 2.38, 3.15, or 4.56 — and is the 2.38→4.56 drift a real divergence in the H̃-branch or a normalization-convention artifact between Route-B-PW and the H̃ chase?"* Output: a single pinned OOM figure + a verdict on whether A_s closure is convention-blocked or physics-blocked.
- **COMPUTE** (CF-B1 successor): A_s amplitude through the τ-fold at canonical L_max, extending `S110-CF-B1-TRANSITPS`. Pre-register the OOM-gap PASS band. Inputs: `s73b_transit_power_spectrum.py` lineage, S110 npz, `deg_T_BZ_pivot=+2` transport.
- **COMPUTE** (CF-AS-2 / CF-AS-3): the user names CF-AS-2/CF-AS-3 — planner resolves these from the source doc / atlas-08 Q23 materials and pre-registers each as its own amplitude-route gate (e.g., a second regulator route + a cross-route reconciliation against the workshop's pinned figure).

**Effort**: high (THE critical question; multi-route).

---

## Wave 2 — Q18b: Yukawa hierarchy  [owner: connes-ncg-theorist]

**Status (true)**: NUMBER held — rank-1 Yukawa wall confirmed per-generation (`Rank-1 Yukawa` S62: J_12/J_23=19.52 algebraically constant, rank-deficient; anchor `R_S96_matter_hierarchy`). Structural shape wall §VII.CK LANDED S114 PASS (see catch #3). All internal corridors closed; shape leg survives only via an external ε_LX class.

**Next step (user)**: `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` + §VII.CK Stage-2 verify.

**Items**:
- **COMPUTE** (Stage-2 verify of §VII.CK): two-agent cross-axis independent verify per `joint-theorem-promotion.md §"Stage 2"`. NOTE: this is a structured 2-reviewer dispatch — the planner pre-registers it as a compute gate whose PASS = both cross-reviewers PASS the joint clauses without prior workshop context. Axis A = `connes-ncg-theorist` (NCG/spectral), Axis B = a distinct axis (`spectral-geometer` or `transit-dynamics-theorist`). Cross-reviewers read only the registered §VII.CK entry, NOT the S112/S114 workshop transcripts.
- **WORKSHOP** (2 agents): the external-ε_LX rescue question. Agents: `connes-ncg-theorist` vs `neutrino-detection-specialist`. Adjudication question: *"Does the external ε_LX charge-class rescue the LEPTON shape leg (PMNS texture), or is the lepton sector permanently walled like the quark sector by the same §VII.CK no-non-monotone-scalar theorem?"*
- **COMPUTE** (`CF-S115-LEPTON-PMNS-FORCED-TEXTURE`): the forced-texture compute for the lepton sector. Planner resolves the CF-S115 spec from S115 WP carry-forwards (`sessions/session-115/`). Owner-of-math: `neutrino-detection-specialist` (PMNS).

**Effort**: high.

---

## Wave 3 — Q3: Goldstone mass from disorder  [owner: landau-condensed-matter-theorist]

**Status (true)**: see catch #1 — the Imry-Ma random-field route ALREADY FAILED in inv5 (`frac170=4.036e-05`, `xi_L=17.115`, leg1=NEG). The 170× target is `m_required/m_Leggett = 170` (atlas-spectral-geometer-collab §5 Cheeger Constants / Spectral Gaps / Mass Problem). Prior: `s48_goldstone_mass.py` (MASS-48; spectral-action Goldstone mass theorem S48). KZ correlation length `xi_KZ = 0.162075 M_KK^{-1}`.

**Items**:
- **WORKSHOP** (2 agents): structural-closure adjudication. Agents: `landau-condensed-matter-theorist` vs `phonon-first-cosmologist`. Adjudication question: *"Given the inv5 Imry-Ma FAIL (frac170~4e-5), is the disorder→Goldstone-mass route to the 170× factor STRUCTURALLY CLOSED, or does a non-Imry-Ma disorder mechanism (e.g., a different ξ_disorder scaling from the Josephson-coupling distribution) survive?"*
- **COMPUTE**: m² ~ 1/ξ_disorder² from the Josephson couplings under the surviving mechanism (if the workshop identifies one), OR a structural-closure compute that pins the disorder-route ceiling. Build on inv5 npz; pre-register the frac170 PASS band against 170×. Inputs: Josephson-coupling distribution, `xi_KZ`, the inv5 convention.

**Effort**: medium-high.

---

## Wave 4 — Q8: 4D modulus effective action  [owner: kaluza-klein-theorist]

**Status (true)**: the modulus action has been WRITTEN repeatedly but the kinetic normalization is the assumed part. Forms on record: `S[τ]=∫d⁴x[(1/2)G_DeWitt(∂τ)²+V(τ)]` (S74, Gaussian one-loop around fold saddle); `L_eff` anisotropic kinetic term (S64; `G_DeWitt=5`); `S_4D ⊃ ∫(1/2)Z(τ)(∂τ)²−V_eff` (S41; Z(τ) "derivable from the 12D Einstein equations with the SU(3) internal-space ansatz"); `Z_norm` (S96-plan-w1, the τ̇² coefficient); `Z=∫D[τ]exp(−S_eff)` (S36). So a path-integral derivation EXISTS (S74); the gap is first-principles derivation of the kinetic normalization Z(τ) vs assumption.

**Items**:
- **WORKSHOP** (2 agents): kinetic-normalization provenance. Agents: `kaluza-klein-theorist` (KK reduction of 12D Einstein eqs) vs `feynman-theorist` (path-integral / spectral-action route). Adjudication question: *"Is Z(τ) (the modulus kinetic normalization) FIRST-PRINCIPLES-DERIVED from KK reduction of the 12D Einstein equations / spectral action, or is `G_DeWitt=5` an assumed/fitted coefficient? Do the two routes (S74 path-integral vs S41 12D-Einstein) agree on Z(τ)?"*
- **COMPUTE**: path-integral derivation of the kinetic term + potential from first principles (Gaussian one-loop around the fold saddle), pre-registering the PASS as agreement with `G_DeWitt=5` (S64) within a stated tolerance. Inputs: S74 saddle, S96-W1 Z_norm, the spectral action S(τ).

**Effort**: high.

---

## Wave 5 — Q11: A_F quaternion (H) extraction  [owner: connes-ncg-theorist]

**Status (true)**: `N2` (atlas-04, S10): "Order-one condition extracts A_F = C + H + M3(C)" — **CONDITIONAL**: "C + M3(C) extracted (dim 20); H (quaternions) requires bimodule structure; complete A_F extraction via o-map route identified." The o-map route was IDENTIFIED but NEVER EXECUTED. Related results: `A_F SINGLETON` (§W8-87b, S84): A_F=ℂ⊕ℍ⊕M_3(ℂ) is the UNIQUE finite real NC algebra with dim_ℝ≤50 satisfying 6 NCG axioms (Wedderburn-Artin enumeration); `chi_action_on_H = "embedded_M2C_via_quaternion_real_form"` (S88-plan-w4c); "A_F bimodule: LEFT in commutant" (S20c).

**Items**:
- **WORKSHOP** (2 agents): which construction extracts H. Agents: `connes-ncg-theorist` vs `van-den-dungen-bridge-theorist` (bimodule/KK side). Adjudication question: *"Which route actually extracts the quaternion ℍ — the o-map bimodule (S10 conditional), the Wedderburn-singleton uniqueness (S84), or the χ-quaternion-real-form embedding (S88) — and are these the SAME construction or structurally distinct routes to ℍ?"*
- **COMPUTE**: construct the bimodule action yielding ℍ — execute the S10 o-map route. Pre-register PASS = the bimodule yields dim_ℝ(ℍ)=4 with the correct quaternionic real form (machine-exact structural check). Inputs: order-one condition, the H_F=ℂ³² bimodule, χ-map (S88-plan-w4c).

**Effort**: high.

---

## Wave 6 — Q12: τ=0 initial conditions  [owner: quantum-foam-theorist]

**Status (true)**: see catch #2 — WDW Ψ(τ) on minisuperspace ALREADY computed in inv11 (`N_e_WKB=0.17`, e-fold clause FAILED, gap_to_3.1=2.93; τ-clause PASSED). Q45 (τ=0 operator canonicity) OPEN-PENDING-COMPUTE; `S110-CF1-AT-MINISUPERSPACE` INFO (branch=SPLIT, schemes_agree=False). The substrate τ=0 is the unstable maximum (project lore: tau=0 unstable maximum, cascade inevitable; `tau_0=0.035 → tau_f=0.201498, type=maximum` in s53 saddle search).

**Items**:
- **WORKSHOP** (2 agents): THE boundary-condition fork. Agents: `hawking-theorist` (Hartle-Hawking no-boundary) vs `quantum-foam-theorist` (Vilenkin tunneling). Adjudication question: *"Hartle-Hawking no-boundary vs Vilenkin tunneling: which boundary condition on Ψ(τ=0) is canonical for the substrate at the unstable maximum, and does either close the inv11 e-fold gap (N_e=0.17 → ~3.1)?"*
- **COMPUTE**: WDW Ψ(τ) refinement under the workshop-selected BC — re-evaluate the e-fold clause `clause_efold` with the chosen IC. Build on `inv11_w3_3` npz; pre-register PASS = N_e closes to within the pre-registered band of 3.1 OR a structured INFO if the BC is itself SPLIT. Inputs: inv11 WDW operator, the τ=0 maximum from s53.

**Effort**: high.

---

## Wave 7 — Q33: §VII.AJ.STATE-PROJ derivation  [owner: volovik-superfluid-universe-theorist]

**Status (true)**: OPEN (NEEDS-COMPUTATION). `§VII.AJ.STATE-PROJ` (atlas-07): "State-projection: BCS-physics-grounded substrate-IS image of R_3HeB_lit = +0.03536 at polycritical pressure P_pc = 21.22 bar (algebraic shape (a−b)/(a+b); algebra-DEPENDENT)" — S88 W7+W10, landed in atlas-07 but the STATE-PROJ companion slot is NEEDS-COMPUTATION. Companion: `§VII.AJ.OP-PROJ` (STAGE-1-CANDIDATE; volovik-defended universal R_∞ ≈ −1.892; algebra-INVARIANT).

**Items**:
- **COMPUTE**: BCS-grounded substrate-IS image of R_3HeB = +0.03536 at P_pc=21.22 bar (the state-projection companion). Pre-register PASS = the substrate BCS occupation distribution reproduces R = +0.03536 via the (a−b)/(a+b) algebraic shape within the published precision. Inputs: 3He-B BCS gap, P_pc, the OP-PROJ derivation. Owner-of-math: `volovik-superfluid-universe-theorist` (or `nazarewicz-nuclear-structure-theorist` for BCS pairing).
- **WORKSHOP** (2 agents): algebra-axis orthogonality. Agents: `volovik-superfluid-universe-theorist` vs `landau-condensed-matter-theorist`. Adjudication question: *"Is §VII.AJ.STATE-PROJ (R=+0.03536, algebra-DEPENDENT state-pair functional) a genuine substrate-IS observable ORTHOGONAL to §VII.AJ.OP-PROJ (R_∞≈−1.892, algebra-INVARIANT spectrum-only functional), or do the two projection-side readings collapse to one?"* (Per `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` — cross-corner co-primary is FORBIDDEN.)

**Effort**: medium-high.

---

## Wave 8 — Q30: Forward bridges FWD-C1 / FWD-C2  [owner: connes-ncg-theorist]

**Status (true — CORRECTED at plan-freeze; the table's "never dispatched" is ~25 sessions stale, confirmed by MCP forward-trace via planner-w8)**: BOTH bridges already LANDED — re-derivation is the rediscovery failure mode.
- FWD-C1 (Pillar I↔II, n_s ↔ Planck CMB): S88 PRE-REG-INC (c_sub blocker) → S89 FAIL (element-2 OE-form) → **`S90-A24-FWD-C1-PILLAR-I-II-BRIDGE-LANDING-VII-AU-RETRY` PASS** (all 8 booleans, `B6_hybrid_independence_test=True`) → §VII.AU.OP-PROJ. c_sub blocker RESOLVED: `c_sub_baseline = 2.238` (canonical_constants.py:2546; S78 W2-E central pin).
- FWD-C2 re-scoped (S88 W8 CF-62; Pillar II↔V → III/IV↔V): **`S93-W3-VII-AV-STATE-PROJ-STAGE-3-PERMANENT-PROMOTION` PASS** → §VII.AV.STATE-PROJ STAGE-3-PERMANENT (s=4, `Var_a(n_a^GGE) = −7.046336`, Cell IV).

**Genuine residuals (what S116 actually targets)**:
- FWD-C1 → the Level-2 convergence-envelope NUMERICAL-DEFERRED sub-class (CF-S94; expected INFO — marginal-saturation, ~25% intrusion at L=14).
- FWD-C2 → the §VII.U.2 Corner-II Var_a PROXY-REFINEMENT (Casimir-bound → FULL BdG Pauli-Villars vs the −7.046336 proxy).

Full forward-trace: `session-116-plan-w8.md §"GROUNDING RECONCILIATION"`. **SOURCE-RECON advisory (backfilled at plan-freeze)**: `c_sub_baseline=2.238` lacked a structured PROVENANCE-dict entry (inline-comment provenance present; value well-sourced at S78 W2-E).

**Items** (gate-IDs unchanged to avoid collision; scope = residual-targeting):
- **COMPUTE** (S116-W8-FWDC1-LANDING): discharge the FWD-C1 Level-2 NUMERICAL-DEFERRED residual (NOT a re-landing). 5-anatomy + 3-level. Owner-of-math: `connes-ncg-theorist`.
- **COMPUTE** (S116-W8-FWDC2-LANDING): FULL-BdG Pauli-Villars PROXY-REFINEMENT vs the −7.046336 proxy (Corner-II Var_a). Owner-of-math: `volovik-superfluid-universe-theorist` (BdG) / `connes-ncg-theorist` (Mellin).
- **WORKSHOP** (S116-W8-BRIDGEMAP-INDEP, 2 agents): `connes-ncg-theorist` vs `van-den-dungen-bridge-theorist`. Adjudication: FWD-C2 bridge-map class (HKR/Connes-Karoubi/K-theory) + FWD-C1 Hybrid-Independence-Test re-audit (within-pillar-restatement challenge).

**Effort**: high (two residual discharges + independence re-audit).

---

## Wave 9 — Q36: D_K sectors p+q=15  [owner: baptista-spacetime-analyst]

**Status (true)**: `CF-S105-BRANCH-IV-GT-BUILDER` (Gelfand-Tsetlin (p,0) irrep builder + direct construction) advanced S105; p+q=13,14 done. `S104-BRANCH-IV-DIRECT-L1314` was PRE-REG-INC (`blocked_by_irrep_construction_wall_Sym13_Sym14`) — the GT-builder is what unblocked 13,14. p+q=15 untested.

**FEASIBILITY PIN (mandatory)**: per `math-scripts.md §"D_K Block-Diagonality + Recursive-Casimir-Projection Feasibility Pre-Check"` — irrep CONSTRUCTION (not diagonalization) is the cost; recursive Casimir projection at p+q≥13 is super-polynomial and may exceed an agent timeslot. The GT-builder is the feasible route. Planner MUST pin the GT-builder cost envelope at p+q=15 AND the Friedrich-Bär saturation argument (does the new sector even shift the bottom-K observable?).

**Items**:
- **WORKSHOP** (2 agents): observable-relevance vs saturation. Agents: `baptista-spacetime-analyst` vs `spectral-geometer`. Adjudication question: *"Does the p+q=15 sector shift any bottom-K observable / w0_FW, or is the D_K spectrum Friedrich-Bär-saturated at p+q≤14 so that p+q=15 is structurally redundant (the GT-builder extension is a completeness check, not a physics change)?"*
- **COMPUTE**: GT-builder extension to p+q=15 — construct the (15,0)/(0,15) and mixed sectors, diagonalize the block, report whether bottom-K / canonical observables shift. Pre-register PASS = construction completes AND the truncation-consistency flag (`truncation_consistent`) holds vs the L_max=12/14 cache. Inputs: `CF-S105-BRANCH-IV-GT-BUILDER` script, the L_max≤14 spectrum cache, Casimir-bound feasibility.

**Effort**: high (feasibility-bounded; GPU per `math-scripts.md`).

---

## Source manifest

- User-supplied 9-question table (this session's `--extra`).
- Knowledge MCP grounding (this plan-freeze): `INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER`, `INV11-W3-3-WHEELER-DEWITT-PSI-TAU-EFOLD`, `CF-S114-YUK-SHAPE-WALL-VII-LANDING`, `S110-CF-B1-TRANSITPS`, `AMPLITUDE-NORM-66`, `CF21`, `S88-FWD-C1-PILLAR-I-II-N-S-BRIDGE-LANDING`, `§VII.AJ.STATE-PROJ`/`OP-PROJ`, `N2` (atlas-04 A_F), `CF-S105-BRANCH-IV-GT-BUILDER`, constants `n_s_FW_sqrt_cutoff`/`n_s_framework`/`n_s_canon`.
- Per-wave planners deep-query their own question's entities via MCP.

## Disciplines the per-wave planners apply (pointers, not re-stated)

- Mixed gate_type: `.claude/templates/plan-investigation.md` (shape) + `.claude/templates/r3-yaml-gate-block.yaml §gate_type`.
- Compute-gate PRDR / verdict / pins / substrate-framing / a_n-tagging / cross-pillar 5-anatomy: the rule set in the per-wave planner prompt.
- Workshop = EXACTLY 2 agents, genuine adversarial tension (`Investigating-Workshops.md`); closes by artifact-existence (no verdict line).
- Verdict path (compute only): `computations/session-116/s116_gate_verdicts.txt`.
