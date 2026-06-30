# Session 97 Synthesis: The q_Ω Route-Sensitivity — Gauge Artifact vs Physical Inequivalence, and the Sharpened S98 Route-Reconciliation Pre-Registration

**Date**: 2026-05-31
**Agent**: volovik-superfluid-universe-theorist (Volovik)
**Slot**: Session-97 workshop campaign, Slot-1 solo S-2
**Source Documents**:
- `sessions/archive/session-97/session-97-w1-workingpaper.md`
- `computations/session-97/s97_gate_verdicts.txt`
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md` (agent context)

---

## I. Session Outcome

Gate `S97-W1-QOMEGA-ROUTE-INVARIANCE` closed **INFO** (LIVE non-superseded line `6dcc22f1`, verdict-file line 38; Option-A chain `8756ea30→ecb17c76→970f0105→6dcc22f1`; 3-tuple `sign=PASS / magnitude=FAIL / regime=MARGINAL`): the conformal-transported two-fluid deceleration `q_Ω` is **route-SENSITIVE**, not route-invariant — the three S96 `H(τ)` reconstructions disagree by `max|ΔH_A| = 3.835844 ≫ band_tol 0.356`. This synthesis does **not** re-adjudicate that numerical verdict (it is authoritative). It addresses the **adversarial pre-question** the carry-forward `CF-S98-W1-ROUTE-RECONCILIATION` currently fudges: is the route-disagreement a **GAUGE/FRAME artifact** (reading (i)) or a **PHYSICAL inequivalence** (reading (ii))? My first-principles verdict, argued from the spectral-action origin of the emergent metric and from Volovik's superfluid two-fluid hydrodynamics, is **reading (i) — GAUGE/FRAME**: the AOFT covariant spectral-action route IS the substrate-natural acoustic frame, and the VOL/GFT routes are non-canonical reconstructions whose disagreement is a frame-of-reconstruction artifact, NOT a substrate-physics fact. The consequence is a sharpened S98 pre-registration that I record below as an in-session structural note (per the carry-forward mandate's NON-MATH clause).

---

## II. Key Results

### II.1 — The root cause is pole-free and unambiguous: three different bare expansion histories sharing one Ω

**Result**: `max|ΔH_A| = 3.835844` (AOFT–VOL 3.8358, AOFT–GFT 0.2191, VOL–GFT 3.8171) ≫ `band_tol 0.356`. **PHONONIC** (conformal-transport reading of the order-parameter trajectory's acoustic curvature).

The W1-3 root-cause statement (WP line 184; verdict-line 40) is the load-bearing fact for the gauge-vs-physical adjudication, and it is established **pole-free** so the conclusion does not ride on the removable coordinate pole at `H_A = 0`:

- The three routes' **bare** scale-factor growths over the common support `[0.190, 0.451041]` are **AOFT 1.048× / VOL 1.673× / GFT 1.024×**.
- All three are transported through the **same** conformal factor Ω (which decreases ×0.954, from `Ω(τ_fold)=2.241017` to `Ω(0.6)=2.01956`, gate 1.1 PASS).
- The conformal Hubble rate `H_A = H_bare + d ln Ω/dτ` (Sage-verified identity, WP line 176) therefore lands at three structurally different places: AOFT `H_A ≈ 0` (the bare growth nearly cancels Ω's decrease — acoustic-frame **conformally stationary**), VOL `H_A ∈ [−0.3057, 3.8363]` (bare growth dominates), GFT `H_A ∈ [−0.2192, 0.0220]` (Ω's decrease overtakes the weak growth).

The decisive observation: **conformal transport cannot homogenize routes whose bare expansion histories already disagree by ~1.6×.** A shared Ω is a single multiplicative re-grading applied identically to all three; it shifts each `H_A` by the SAME `d ln Ω/dτ`, so it can never close a pre-existing difference in `H_bare`. The disagreement therefore lives entirely in the **bare `H(τ)` reconstructions** — i.e., in HOW each of the three frameworks reads the effective expansion rate off the same `D_K` spectrum, NOT in the two-fluid EoS being transported (cross-check 4, WP line 222: the leg-i algebraic anchor `q_two_fluid(x(τ),w_n)` is a single route-independent curve `q ∈ [−0.996, −0.983]`, confirming x is one substrate ratio and the disagreement is a property of the conformal TRANSPORT, not the underlying physics).

### II.2 — The decisive discriminator: only AOFT is the spectral-action-derived metric

**Result**: AOFT is the covariant route whose `H(τ)` derives from the `a₂` Seeley–DeWitt coefficient; VOL and GFT are reconstructions through different, non-canonical channels. **GEOMETRIC** (which `H(τ)` is the emergent-metric rate is a fabric property, not an excitation property).

This is the structural fact that breaks the tie between reading (i) and reading (ii). The framework's emergent metric is **not** route-democratic. Per `phononic-framing.md` (the framework's own canonical statement): *"The 4D metric g_M emerges from the a₂ Seeley-DeWitt coefficient. Newton's constant is the second spectral moment. The Yang-Mills action is the fourth spectral moment."* There is exactly **one** emergent metric `g_M`, and it is fixed by `a₂` — the same `a_2^{ζ} = 2776.165389` (regulator-pinned, gate 1.1 and 1.3 both `CLASS=FULL`) that backbones Ω itself.

The three S96 routes are NOT three equally-valid metrics. They are:

- **AOFT** (`S96-W1-AOFT-FRIEDMANN-MAP`, PASS, audit `edfe1f7f`): the **covariant spectral-action** route. Its `H²(τ)` is the FRW-form rate of growth of `a₂`(τ) — i.e., it IS the rate of change of the spectral-action coefficient that GENERATES `g_M`. `H²(τ*) = 7.478844e-03 M_KK²` is its fixed-point value, reproduced bit-for-bit by gate 1.4 (rel 5.46e-8).
- **VOL** (`S96-W1-VOLOVIK-2FLUID`): the Landau–Khalatnikov two-fluid integration. This is a **matter-sector** construction — it tracks `ρ_n/ρ_s` differential dilution (Volovik superfluid two-fluid hydrodynamics, my agent-memory mapping `Two-fluid w=-1 + w=0 → Effacement (vacuum) + GGE (matter)`). It reconstructs `a_norm` from the normal-component redshift, NOT from `a₂`.
- **GFT** (`S96-W1-GFT-FRIEDMANN`, INFO): the group-field-theory condensate effective Friedmann route — a **different effective-dynamics reconstruction** that need not, and does not, agree with the spectral-action `a₂`-rate.

The three are reading the **acoustic image** of the same `D_K` spectrum through three different lenses. Only AOFT's lens is the one that DEFINES `g_M`. This is the crux: there is no symmetry, no gauge orbit, that relates the spectral-action metric to the two-fluid matter-tracking reconstruction or the GFT condensate reconstruction. They are not gauge-equivalent representatives of one geometry; they are **one canonical geometry (AOFT) plus two auxiliary diagnostics that approximate it from the matter and condensate sides**.

### II.3 — First-principles argument: reading (i) GAUGE/FRAME is correct; (ii) PHYSICAL is mis-framed

**Result**: The route-disagreement is a **frame-of-reconstruction artifact**, not a substrate-physics fact. **GEOMETRIC**.

I argue reading (i) from three independent first-principles legs, then show why reading (ii) — "three genuinely distinct effective-Friedmann contents" — mis-locates the disagreement.

**Leg A — Uniqueness of the emergent metric (spectral-triple axiom).** A spectral triple `(A_K, H_K, D_K(τ))` has ONE Dirac operator and ONE heat-kernel expansion. The Seeley–DeWitt coefficients `a₀, a₂, a₄, …` of `D_K²` are unique invariants of that operator at each τ. `g_M` is read off `a₂`; the emergent expansion rate is `H_AOFT(τ) = (1/2) d ln a₂/dτ · (dτ/dt)`-type object (the FRW-form rate of `a₂`-growth). There is no second emergent metric on the same triple. Therefore the question "which `H(τ)` is THE acoustic-frame rate" has a unique answer **by the structure of the spectral triple**: AOFT. VOL and GFT do not produce a metric — they produce matter-sector and condensate-sector RATE ESTIMATES that, if the reconstructions were exact and complete, would have to AGREE with the AOFT rate (since there is only one geometry). Their disagreement is the signature that VOL and GFT are **incomplete reconstructions of the one metric**, not evidence of a second metric.

*Hard anchor for Leg A (MCP-confirmed, not just framing-rule)*: the AOFT gate `S96-W1-AOFT-FRIEDMANN-MAP` (PASS) carries the explicit value-field tokens `S_eff_covariant=True; field_eq_sourced_Geff_munu=8πG_eff·T_relic=True; bianchi_lift_K_to_gM=True; emergent_bianchi_residual=0.000e+00`. That is: AOFT is the route whose generally-covariant effective action `S_eff[g_M]` yields the Einstein field equation `G_eff^{μν}=8πG_eff T_relic^{μν}` with the Bianchi identity lifting from `K` to `g_M` at zero residual. It is the ONLY one of the three routes that is certified to PRODUCE the emergent metric and its field equation. VOL (`S96-W1-VOLOVIK-2FLUID`) and GFT (`S96-W1-GFT-FRIEDMANN`, whose own form `(H_GFT)² = (8πG_eff/3)·ρ_relic·(1−ρ_relic/ρ_crit)` is the Oriti/LQC-bounce condensate-hydrodynamics ansatz, NOT a metric-from-`a₂` construction) carry no such covariance/field-equation certification. This is a stronger statement than "AOFT is conventionally canonical": the registry verifies AOFT alone discharges the generally-covariant `S_eff[g_M]` → Friedmann chain. (The `Emergent General Relativity (a_2 channel)` canonical class confirms the principle: "the Einstein-Hilbert action arises as the second Seeley-DeWitt coefficient a_2 of the spectral action.")

**Leg B — The two-fluid route is a matter-frame, not the acoustic frame (Volovik).** In Volovik's superfluid universe, the two-fluid system has TWO velocity fields (superfluid `v_s` and normal `v_n`), but ONE acoustic metric — the metric quasiparticles propagate IN is set by the superfluid background (the order-parameter texture), and is the SAME object regardless of which fluid component one tracks. The VOL route reconstructs `a(τ)` from the **normal-component dilution** `ρ_n ∝ a^{−3(1+w_n)}` (gate 1.2, `x = ρ_s/ρ_n`). That is a matter-clock reconstruction — it answers "how does the GGE quasiparticle gas redshift?" — NOT "what is the acoustic metric's expansion rate?". In Volovik's framework these need not coincide off-equilibrium: the matter-component dilution and the acoustic-metric expansion are related but distinct, and only the acoustic metric (the superfluid-background metric, the AOFT `a₂`-derived `g_M`) is the frame in which `q_Ω` is the physical deceleration. Reading VOL's `H_A ∈ [−0.31, 3.84]` as a competing "physical" deceleration is exactly the container-thinking error my memory flags (`.claude/rules/phononic-framing.md`): it treats a matter-sector reconstruction as if it were the geometry itself.

**Leg C — The conformal factor was BUILT from `a₂`, so it is self-consistent only with the AOFT route.** Ω(τ) = √(ρ_s/a₂) (gate 1.1, CLAIM B). Its denominator IS `a₂` — the spectral-action coefficient. When Ω is applied to the AOFT bare `a`, the transport `A = Ω·a_bare` is internally consistent: both factors trace to the same `a₂`-spectral content. When the SAME Ω is applied to the VOL `a_norm` (which traces to `ρ_n`-dilution, not `a₂`) or the GFT `a_gft` (which traces to condensate dynamics), the transport **mixes two different spectral channels** — an `a₂`-derived conformal factor riding on a non-`a₂` bare history. The resulting `H_A` for VOL/GFT is a hybrid object with no clean substrate-IS interpretation. The near-cancellation `H_AOFT ≈ 0` is not a pathology — it is the SIGNATURE that AOFT's bare growth and the `a₂`-derived Ω-decrease are two views of the SAME `a₂`-evolution, and they nearly cancel because Ω = √(ρ_s/a₂) with ρ_s ≈ const means `d ln Ω/dτ ≈ −(1/2) d ln a₂/dτ`, which is (minus one-half times) exactly the AOFT bare growth rate. The conformal-stationarity of AOFT is the self-consistency check passing, not failing.

**Why reading (ii) is mis-framed.** Reading (ii) says the three routes "carry genuinely DISTINCT effective-Friedmann content read three inequivalent ways" and asks for "a principled selection with a DERIVED reason." But there is no genuine multiplicity of effective-Friedmann contents on one spectral triple — there is one metric (`a₂`-derived) plus reconstructions. Reading (ii) reifies the reconstructions into physics. The leg-i algebraic cross-check (WP line 222) already shows the underlying two-fluid EoS gives ONE route-independent `q(x)` curve; the disagreement appears ONLY after the three different bare-`H` reconstructions are inserted into the transport. A disagreement that appears only at the reconstruction step, and that the spectral triple's uniqueness forbids at the metric step, is a frame artifact by definition — not a substrate-physics fact. Reading (ii) is not WRONG in the weak sense (the bare growths DO differ), but it mis-attributes the difference: it is a difference in **reconstruction completeness/channel**, not in **physical content**. The correct "derived reason" is Leg A's uniqueness theorem, which selects AOFT — and that is exactly what reading (i) says.

**The honest boundary (what this argument does NOT establish).** Declaring AOFT canonical does NOT prove the AOFT `q_Ω` lands in the SF54 band `[−0.97,0.81]` — that is a separate empirical question the S98 compute must answer. The A-leg's own AOFT entry was `nan` (fully conformally stationary), so the AOFT-frame deceleration is currently UNDETERMINED at the `H_A≈0` points and must be computed via the pole-free `q = −1 − Ḣ_A/H_A²` with the removable pole handled analytically (L'Hôpital at the stationary points) — exactly the method the agent already used as primary. Reading (i) **dissolves the route-disagreement** (it is a frame artifact); it does NOT by itself **deliver the AOFT deceleration value**. Those are two distinct deliverables, and the S98 pre-registration must keep them separate.

### II.4 — Convention translation: this is a frame choice, in the precise GR sense

**Result**: The "route" ambiguity maps exactly onto the GR conformal-frame ambiguity, with AOFT = the Einstein-frame analog. **GEOMETRIC** (convention-translation deliverable).

In the condensed-matter → cosmology dictionary I maintain, the three routes are three **frames** in which to read the same acoustic geometry:

| Volovik / substrate object | Route | Frame analog (GR) |
|:--|:--|:--|
| Acoustic metric of the superfluid background (`a₂`-derived `g_M`) | **AOFT** | **Einstein frame** — the frame in which the metric is the dynamical geometry |
| Normal-component (GGE matter) dilution clock | VOL | A **matter/Jordan-frame-like** reconstruction — physical, but a matter-tracking readout, not the geometry |
| Condensate effective-dynamics reconstruction | GFT | An **alternative-coupling frame** reconstruction |

The deceleration `q` is famously frame-DEPENDENT in GR (conformal transformations change `q`). The route-sensitivity of `q_Ω` is the substrate-IS instance of exactly this: `q` is read differently in differently-reconstructed frames. The resolution in GR is to pick the physical frame (Einstein frame, where the metric is the geometry); the resolution here is identical — pick the frame where the metric is the spectral-action-derived `g_M`, i.e., AOFT. The disagreement is real arithmetic but it is the EXPECTED behavior of a frame-dependent quantity computed in non-canonical frames, not a substrate-physics contradiction. This is the sharpest statement of reading (i): **`q_Ω` route-sensitivity is the substrate's conformal-frame ambiguity, and AOFT is the Einstein-frame analog.**

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S97-W1-QOMEGA-ROUTE-INVARIANCE | INFO (LIVE `6dcc22f1`) | `max|ΔH_A| = 3.835844 ≫ band_tol 0.356`; `frac_in_band=0.1899 < 0.90`; A-fires; `f_used=0.6367` → regime MARGINAL |
| S97-W1-OMEGA-PROFILE (upstream BLOCKER) | PASS | `rel_spread = 6.420002e-02 ≫ 1e-3`; Ω non-constant, `Ω̇<0`, fold rel-dev 1.5e-4 |
| S97-W1-XTODAY (upstream A-window) | PASS | `x_today = [103.22, 117.22] > x_fold=85.7928`; `q(x_today) ∈ [−0.9915, −0.9873]` |
| S97-W1-1-AT-TRAJECTORY (downstream consumer) | INFO | AOFT `H²(τ*)` anchor rel 5.46e-8; shape non-unique (50/50 τ̇ shapes) |
| S97-COOLING-BUDGET-KAPPA-PIN | PASS | κ_implied = κ_nat = 8.86044e-42 (unit-consistency identity, NOT triangulation) |

*The numerical verdicts above are from the source documents and are authoritative. This synthesis adjudicates only the INTERPRETIVE reading (gauge vs physical), which the gate left open as its own pre-registered carry-forward (WP line 225: "either (i)… or (ii)…").*

---

## IV. Structural Implications

**The constraint-map cell that changes.** The W1-3 INFO is correctly recorded as "route-SENSITIVE; C1's a(t) deceleration CONDITIONAL on route choice" (constraint-map update, WP line 432). My adversarial reading SHARPENS this without contradicting it: the deceleration is conditional on route choice **because `q` is a frame-dependent quantity and the three routes are three frames** — and the frame ambiguity is RESOLVABLE (not a genuine physical degeneracy) because the spectral triple has a unique metric. The cell moves from "route-sensitive, resolution-path undetermined (i)-or-(ii)" to "route-sensitive = conformal-frame-dependent; canonical frame = AOFT by spectral-triple uniqueness; resolution path = (i)."

**What this opens.** The S98 compute now has a DERIVED canonical-frame selection criterion (spectral-action / `a₂`-uniqueness), not an ad-hoc one. The PASS criterion for `S98-W1-ROUTE-RECONCILIATION` can be tightened from the current disjunction (WP line 422, "(a) route-invariant OR (b) divergence substrate-physically expected") to a SINGLE pre-registered statement under reading (i): re-test `q_Ω` invariance **in the AOFT canonical frame as reference**, where invariance means VOL/GFT converge to AOFT as their reconstructions are completed — and where the PRIMARY deliverable is the AOFT-frame `q_Ω` value itself (with the `H_A≈0` removable pole handled analytically).

**What this does NOT change.** C1 stays HELD ASSUMED (WP line 397, 431) — declaring AOFT canonical is a frame-selection argument, not new empirical evidence, and does not license up-tagging C1. The κ-pin (gate 1.5) is a unit-consistency identity, not triangulation, and likewise does not promote C1. The capstone-hygiene K-counter does not advance (no over-claim drift to down-tag; WP line 402). My reading is a **pre-registration sharpening**, not a verdict change.

**Cross-link to my agent corpus.** This is structurally the same move as the 3He-B inheritance being a parent→child morphism rather than an analogy (my memory, `project_3heb-inheritance`): the relationship between the three routes is NOT "three analogous Friedmann equations" but "one canonical spectral-action metric (AOFT) + two reconstructions (VOL matter-sector, GFT condensate-sector) that morph INTO it." Treating them as co-equal is the same category error as treating 3He-B as an analogy rather than an inheritance.

---

## V. Carry-Forward Computations

> **NON-MATH item effected in-session (per the Focus carry-forward mandate)**: the sharpened pre-registration recommendation below (V.0) is recorded in THIS synthesis as the authoritative structural note for the S98 planner. It is a recommendation, not a registry write: it touches the `CF-S98-W1-ROUTE-RECONCILIATION` block (the team-lead's wave-synthesis domain) and the `mack-cosmic-bridge` §7-falsifier surface is NOT touched, so per sole-writer conventions I record the recommendation here rather than editing the WP carry-forward block directly. The S98 plan author lifts V.0 into the `S98-W1-ROUTE-RECONCILIATION` gate block at plan-freeze.

### V.0 — SHARPENED PRE-REGISTRATION for `S98-W1-ROUTE-RECONCILIATION` (structural note; NON-MATH; effected in-session as this synthesis record)

The current CF (WP lines 416–424) selects "the canonical τ̇ shape from the 50 admissible and re-tests" and leaves the canonical-frame selection as an open disjunction (i)-or-(ii). The adversarial pre-question is now ADJUDICATED to reading (i). The S98 gate should pin:

- **WHICH path the S98 compute pins**: **Path (i) — GAUGE/FRAME.** Declare the AOFT covariant spectral-action route the canonical acoustic frame. DERIVED reason (not ad-hoc): the spectral triple `(A_K, H_K, D_K(τ))` has a unique emergent metric `g_M` read off `a₂` (`phononic-framing.md`; `a_2^{ζ}=2776.165389`); VOL and GFT do not produce metrics, they produce matter-sector / condensate-sector RATE RECONSTRUCTIONS. By uniqueness there is one acoustic frame; it is AOFT.
- **The canonical-acoustic-frame H(τ) selection criterion under path (i)**: `H_AOFT(τ)` is the FRW-form rate of `a₂`-growth, `H²(τ*) = 7.478844e-03 M_KK²` (S96 canonical, audit `edfe1f7f`, verbatim cross-check already passed at gate 1.4 rel 5.46e-8). The conformal-frame rate is `H_A,AOFT = H_bare,AOFT + d ln Ω/dτ` with Ω = √(ρ_s/a₂) (gate 1.1). The `H_A,AOFT ≈ 0` conformal-stationarity is a self-consistency FEATURE (since `d ln Ω/dτ ≈ −½ d ln a₂/dτ = −H_bare,AOFT`), to be handled analytically, not a degeneracy.
- **What PASS means** (re-test of `q_Ω` route-invariance under the selected canonical frame): the S98 gate is a **two-clause** PASS, kept structurally separate (per `epistemic-discipline.md` layer-decomposition — do not conflate the frame-selection clause with the value-delivery clause):
  - **Clause 1 (frame-resolution, the dissolution of route-sensitivity)**: PASS iff, with AOFT as reference frame, the VOL and GFT reconstructions are shown to be incomplete reconstructions of the AOFT `a₂`-rate (i.e., their disagreement is attributable to the matter-sector / condensate-sector channel difference, NOT to a second metric). Operational test: the VOL/GFT `H_bare` differ from `H_AOFT,bare` by terms identifiable as matter-dilution / condensate-coupling content, with the residual carrying NO independent geometric (`a₂`) content. This is the registry-eligible structural statement.
  - **Clause 2 (AOFT-frame deceleration value, the actual physical `q`)**: COMPUTE `q_Ω` in the AOFT canonical frame via the pole-free `q = −1 − Ḣ_A/H_A²` with the removable pole at the conformal-stationary points handled by L'Hôpital. PASS iff `q_Ω,AOFT ∈ SF54 band [−0.97,0.81]`; INFO if outside band but finite and single-signed; FAIL if non-finite after analytic pole removal. **This clause is the empirical deliverable and is NOT pre-judged by Clause 1** — declaring AOFT canonical dissolves the route-disagreement but does NOT guarantee the band.
  - **Coupled sub-gate (inherited from 1.4 INFO)**: select the canonical τ̇ shape from the 50 admissible `S96-W1-TAUDOT-PROFILE` shapes so the AOFT `a(t)` becomes fully unique (the κ-pin from gate 1.5 fixes the seconds-scaling; the τ̇-shape fixes the trajectory shape). Pin the selection criterion (e.g., the τ̇ shape consistent with the SCENARIO-A cooling-budget `N_e=80.89` AND the AOFT `H²(τ)` profile jointly).
- **Distinctness from the existing CF**: the existing CF (WP V.1 / line 416) selects the τ̇ shape and re-tests invariance with the (i)-or-(ii) disjunction OPEN. THIS note CLOSES the disjunction to (i) with a derived reason and SPLITS the PASS into the frame-resolution clause and the value-delivery clause. Do NOT merge them; the existing CF is the OBJECT, this note is the SHARPENED PRE-QUESTION resolution.

### V.1 — AOFT-frame `q_Ω` value with analytic pole removal (MATH; 4-field spec)

- **What**: Compute `q_Ω,AOFT(τ)` over `[τ_fold, 0.451041]` via `q = −1 − Ḣ_A/H_A²`, `H_A = H_bare,AOFT + d ln Ω/dτ`, with the removable pole at `H_A=0` (conformal-stationary points) resolved by L'Hôpital (`lim_{H_A→0} (−1 − Ḣ_A/H_A²)` via the local expansion of `A(τ)` around `A′=0`). Output: the AOFT-frame deceleration array + its band-membership fraction vs SF54 `[−0.97,0.81]`.
- **Inputs**: `computations/session-96/s96_w1_aoft_friedmann_map.npz` (AOFT `H²(τ)`, `H2_aeff`); `computations/session-97/s97_w1_omega_profile.npz` (Ω, Ω̇, Ω̈; audit `6fee3fdf`); `computations/session-97/s97_w1_qomega_route_invariance.npz` (`HA_aoft`, `dHA_*`; LIVE audit `6dcc22f1`); `canonical_constants.py` (`a_2_FW_zeta=2776.165389`, `tau_fold`, `Omega_BA_fold`, `M_KK_inv_seconds`).
- **Gate**: feeds `S98-W1-ROUTE-RECONCILIATION` Clause 2. PASS iff `q_Ω,AOFT ∈ [−0.97,0.81]` after analytic pole removal; INFO if finite, single-signed, outside band; FAIL if non-finite. S98 planner pins the band-membership-fraction threshold (suggest ≥0.90 of finite points, matching the B-leg `B_thresh`) at plan-freeze.
- **Effort**: ~0.5 wave, 1 agent session (the npz already carries `HA_aoft`; this is the analytic-pole-removal + band test).

### V.2 — VOL/GFT reconstruction-channel decomposition (MATH; 4-field spec)

- **What**: Decompose `H_bare,VOL − H_bare,AOFT` and `H_bare,GFT − H_bare,AOFT` into (a) matter-sector dilution content (VOL: the `ρ_n ∝ a^{−3(1+w_n)}` redshift channel) / condensate-coupling content (GFT), and (b) any residual. Verify the residual carries NO independent `a₂`-geometric content (i.e., the routes differ only in their non-metric reconstruction channel, supporting reading (i)).
- **Inputs**: `computations/session-96/s96_w1_{aoft_friedmann_map,volovik_2fluid,gft_friedmann}.npz`; `computations/session-97/s97_w1_xtoday.npz` (the `x=ρ_s/ρ_n` two-fluid dilution structure, audit `067fe807`); `canonical_constants.py` (`a_2_FW_zeta`, `x_fold=85.7928`, w_n band `[−0.407649, 0.0]`).
- **Gate**: feeds `S98-W1-ROUTE-RECONCILIATION` Clause 1 (frame-resolution). PASS iff the VOL/GFT − AOFT difference is fully attributable to matter/condensate channel content with residual `a₂`-content below a pre-registered floor (suggest `< 1e-2` in `M_KK²` units, matching the gate-1.1 `eps_nonconst` scale). This is the structural / registry-eligible clause.
- **Effort**: ~0.5 wave, 1 agent session.

### V.3 — Canonical τ̇-shape selection from the 50 admissible (MATH; 4-field spec; coupled sub-gate)

- **What**: Select the unique τ̇(τ) shape from the 50 admissible `S96-W1-TAUDOT-PROFILE` shapes by imposing joint consistency with (a) the AOFT `H²(τ)` profile and (b) the SCENARIO-A cooling budget `N_e_exfl=80.89` (gate 1.5). Output: the selected τ̇ shape + the resulting fully-unique AOFT `a(t)` in physical seconds (κ from gate 1.5 = `κ_nat=8.86044e-42` fixes the seconds-scaling).
- **Inputs**: `computations/session-96/s96_w1_taudot_profile.npz` (50 admissible shapes); `computations/session-97/s97_w1_1_at_trajectory.npz` (the 1-parameter band structure, audit `b8507148`); `computations/session-97/s97_cooling_budget_kappa_pin.npz` (κ_nat, N_e=80.89, audit `f451f43d`); `canonical_constants.py` (`M_KK_inv_seconds`, `tau_fold`, `G_DeWitt`).
- **Gate**: feeds `S98-W1-ROUTE-RECONCILIATION` coupled sub-gate (resolves the 1.4 shape-uniqueness INFO). PASS iff a single τ̇ shape satisfies the joint constraint to a pre-registered tolerance (S98 planner pins; suggest the τ̇-band rel-spread collapses from 0.419 to `< 1e-2`). INFO if multiple shapes remain admissible (the constraint is necessary but not sufficient).
- **Effort**: ~0.5 wave, 1 agent session.

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Root cause pole-free: bare growths AOFT 1.048×/VOL 1.673×/GFT 1.024× share one Ω | PHONONIC | Authoritative (WP line 184) | Disagreement lives in `H_bare` reconstructions, not the EoS — a shared Ω cannot close a pre-existing bare difference |
| 2 | Only AOFT is the spectral-action-derived metric (`g_M` from `a₂`) | GEOMETRIC | First-principles (this synthesis) | Breaks the (i)/(ii) tie — there is ONE emergent metric, not three |
| 3 | Adversarial verdict: reading (i) GAUGE/FRAME correct; (ii) PHYSICAL mis-framed | GEOMETRIC | First-principles (this synthesis) | Spectral-triple uniqueness selects AOFT; VOL/GFT are reconstructions, not metrics |
| 4 | `q_Ω` route-sensitivity = substrate conformal-frame ambiguity; AOFT = Einstein-frame analog | GEOMETRIC | Convention-translation | `q` is frame-dependent by construction; resolution = pick the metric-frame (AOFT) |
| 5 | Sharpened S98 pre-registration: path (i), AOFT-canonical, two-clause PASS | NON-PHONONIC (methodology) | Effected in-session (V.0 structural note) | S98 gate splits frame-resolution (Clause 1, structural) from value-delivery (Clause 2, empirical) |
| 6 | Honest boundary: (i) dissolves disagreement, does NOT deliver the AOFT q-value | PHONONIC | First-principles | Clause 2 (band membership) is NOT pre-judged by Clause 1 — separate deliverable |

---

## VII. Source-Fidelity & Scope Notes

- **What the sources SHOW**: the W1-3 gate verdict (route-SENSITIVE, `max|ΔH_A|=3.835844`, INFO Track-B) and the pole-free root cause (three bare growths sharing one Ω). These are authoritative and not re-adjudicated here.
- **What the sources SUGGEST**: the gate's own substrate-IS assessment (WP line 225) names paths (i) and (ii) as the two resolution routes but does NOT choose between them — it defers to the carry-forward. This synthesis makes that choice from first principles.
- **What the sources do NOT address**: the sources do not prove the AOFT-frame `q_Ω` lands in the SF54 band; the A-leg AOFT entry is `nan` (conformally stationary). My reading dissolves the route-disagreement but explicitly leaves the AOFT-frame deceleration VALUE as an open compute (V.1) — these are three distinct epistemic categories and I keep them separate.
- **Canonical anchor for the decisive claim**: "`g_M` emerges from the `a₂` Seeley-DeWitt coefficient" is the framework's own canonical statement (`.claude/rules/phononic-framing.md` §"The Substrate Picture"), cross-consistent with `a_2_FW_zeta=2776.165389` (the same coefficient backboning Ω in gate 1.1). The spectral-triple uniqueness of the emergent metric is the structural fact that selects AOFT.
- **MCP cross-verification (executed; query-first discipline)**: the decisive Leg-A claim was cross-checked against the knowledge graph and STRENGTHENED, not merely assumed. Confirmed: (1) `S96-W1-AOFT-FRIEDMANN-MAP` PASS carries `S_eff_covariant=True; field_eq_sourced_Geff_munu=8πG_eff·T_relic=True; bianchi_lift_K_to_gM=True` — AOFT is registry-certified as the covariant-`S_eff[g_M]`→Friedmann route. (2) The `Emergent General Relativity (a_2 channel)` canonical class: "the Einstein-Hilbert action arises as the second Seeley-DeWitt coefficient a_2." (3) `a_2_FW_zeta = 2776.165389` (S88-A-N-FW-CANONICALIZATION) — the coefficient backboning Ω in gate 1.1. (4) `SCALE-FACTOR-54` PASS, `q: −0.97 → +0.81` Connes-distance proxy — the SF54 band is a state-side (Connes-distance) proxy, consistent with the Clause-2 framing. (5) `S96-W1-GFT-FRIEDMANN` value confirms GFT is the Oriti/LQC-bounce condensate-hydrodynamics reconstruction, NOT a metric-from-`a₂` route. (6) The S96 workshop `sessions/archive/session-96/workshops/w1-q-omega-band-divergence.md` already surfaced this route-disagreement, confirming it is a genuine cross-session frontier. No claim above depends on an unverified external lookup; gate verdicts from the source docs remain authoritative and are not re-adjudicated.
