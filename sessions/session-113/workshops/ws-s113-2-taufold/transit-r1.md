# WS-S113-2 TAUFOLD — Round 1

**Workshop**: WS-S112-2 TAUFOLD (τ_fold dynamical selection vs empirical input), EVOI Tier-2 #4.
**Author**: transit-dynamics-theorist — Round 1, steelman **Reading A** (dynamical selection survives).
**One-line thesis**: The S95 corridors closed only the *equilibrium / variational* selectors of τ_fold; the substrate-IS object that actually fixes τ_fold = 0.190 is a **non-equilibrium van Hove cusp** (S85, PROVEN, `dS/dτ ≠ 0`), and the transit dynamics select it as a *threshold-crossing* condition, not a potential minimum — so τ_fold is structurally selected by a dynamical mechanism-chain, not tuned, but the selection is a **transit-initiation criterion**, not an attractor of the modulus EOM.

---

## 0. What the knowledge base already pins (query-first)

I queried the MCP before building anything. Three results are load-bearing and I cite them as the spine of the case:

1. **S84 open_channel (OPEN, status verbatim)**: *"MECHANISM-CHAIN selects τ_fold (dynamical, non-V.P.) — I-1 + Turing + RPA + WALL + BCS first-order transition criterion. Not a variational principle but a dynamical selection structure. Orthogonal to §W8a-85 FAIL."* This is Reading A, pre-registered by the framework itself two waves before the S95 closures. It was never refuted — it was filed as an open channel and the S95 work went after a *different* (variational) object.

2. **S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM (PROVEN / PERMANENT, atlas-07 §VII.M.W10-3)**: τ_fold = 0.190 is the **unique van Hove cusp** of the eigenvalue density ρ(λ=0; τ) on the Jensen-SU(3) × A_F spectral triple (cubic-BC class Γ₆, mesh a = 12, L_max = 10), with right-neighbourhood convexity (Γ₅′, `d²S/dτ² = +317,862.85 > 0`) and the **transit-identifier predicate** `dS/dτ|_{τ_fold} = +58,672.80 ≠ 0` locking the cusp as **non-stationary** (explicitly distinct from a critical point). The script's own substitution chain (Step 5): "stationarity requires dS/dτ = 0; +58,672.80 ≠ 0 ⇒ τ_fold NOT a critical point of S(τ)."

3. **S95 corridors**: `T-STAR-ONELOOP-ORIGIN` **FAIL** (FIT-72) and `NO-WELL-ONE-LOOP` **PASS** (value = 0, `convention=EFFECTIVE-ACTION-MONOTONICITY-TREE-PLUS-ONELOOP`). Read literally: the tree+one-loop effective action has **no well** at τ_fold — there is no minimum holding the substrate there.

The contrast my opponent will press — "the action closes t = 1/2 EXACT (rank-4b S101) but does NOT close τ_fold" — is real and I concede its premise. My case is that the *type* of closure differs, and the τ_fold closure is dynamical-kinematic, not variational. I build that now.

---

## 1. The structural pole: why the S95 FAILs are a PREDICTION of Reading A, not a refutation

The workshop framing invites the reflex "the variational selector FAILED, therefore τ_fold is unselected." This conflates two distinct questions:

- **Q_eq** (what S95 tested): *Is τ_fold a stationary point — a minimum/well — of an effective potential V(τ) or one-loop effective action Γ(τ)?*
- **Q_kin** (what S85 answered): *Is τ_fold a substrate-intrinsic, parameter-free feature of the D_K spectrum that a dynamical flow is forced to cross?*

These are not the same object, and the answers are **opposite by construction**:

```
NO-WELL-ONE-LOOP: PASS, value = 0   ⇒ dΓ/dτ has no zero (no minimum) at τ_fold
S85 van Hove:     dS/dτ|_fold = +58,672.80 ≠ 0  ⇒ τ_fold is NON-stationary
```

A van Hove singularity in a density of states is, by its definition (Step 2 of the S85 chain), a point where `dρ(λ₀;τ)/dτ` diverges one-sidedly while the spectral action *itself* is sweeping monotonically (`dS/dτ > 0`). **It is categorically impossible for a van Hove cusp to be a potential minimum** — the DOS singularity sits at non-stationarity of the action. So:

> The NO-WELL PASS is not evidence that τ_fold is unselected. It is the *expected signature* of a van-Hove-selected (rather than potential-selected) modulus. If S95 had found a well at τ_fold, *that* would have contradicted S85.

This is the steelman's core move and it is substrate-first: the S85 spectral theorem is logically prior; the S95 effective-action result is a downstream consequence that is **consistent** with — not destructive of — the dynamical-selection reading. The two S95 corridors closed Q_eq. They are silent on Q_kin. Reading B's "the action cannot select τ_fold" is true *only* in the variational sense; it does not license "the substrate does not select τ_fold," because the substrate's selection operates through the spectral geometry (the cusp), not through a potential well.

`★` Substrate-first check: the explanation flows `D_K eigenvalue density ρ(λ;τ) → van Hove cusp at τ_fold → supersonic transit crosses it → emergent cosmogenesis`. At no point do I invoke an external potential as fundamental. The "potential" V(τ) that S95 searched for a well in is itself an *emergent* spectral-action object; its flatness (NO-WELL) is downstream of the cusp, not a competing primary. `─`

---

## 2. What the cusp uniqueness buys: 0.190 specifically, not "some fold"

The workshop asks pointedly: "Does it pick out 0.190 specifically, or just 'some fold'?" The S85 theorem answers **0.190 specifically**, and this is the strongest single fact for Reading A:

- The cusp is the **unique** Γ₆ (cubic-BC) intersection at mesh a = 12 on the L_max=10 triple. Uniqueness is the theorem's verb — "ρ(λ=0; τ) has a UNIQUE van Hove cusp at τ_fold = 0.190." There is exactly one such point in the modulus range.
- Its location is fixed by the **D_K spectrum alone** — the Jensen deformation of SU(3) and the A_F finite algebra — with **zero free continuous parameters**. The Jensen deformation has no tunable knob that slides the cusp; the cusp is where the bottom-band eigenvalue λ→0 reorganizes, and that is a property of the SU(3) representation content under the deformation.
- Three independent "gears" co-localize it (the S85 single-gear replacement): Γ₆ cubic-BC corner + Γ₅′ right-convexity + transit-identifier `dS/dτ ≠ 0`. (The pre-S85 framing called this "triple-gear"; S85 sharpened it to a single van-Hove statement, but the over-determination remains: the cusp is pinned from multiple structural directions.)

Contrast this with the M_KK magnitude import that Reading B wants to make τ_fold parallel to. M_KK is a **dimensionful** scale — a single real number with units, with N₃=0 (one dimensional handle), genuinely unfixed by the dimensionless substrate. τ_fold is **dimensionless** (it is the Jensen deformation parameter, a pure number labelling a point in moduli space), and it is fixed *combinatorially* by where the cubic-BC eigenvalue hits the BZ corner. These are not structurally parallel:

| | M_KK | τ_fold |
|:--|:--|:--|
| Type | dimensionful scale | dimensionless modulus coordinate |
| Substrate handle | N₃ = 0 (none — single dimensional import) | Γ₆ ∩ a=12 cubic-BC intersection (combinatorial) |
| Free continuous knob? | yes (the import itself) | **no** — cusp location is spectrum-determined |
| Selection mechanism | external calibration | van Hove cusp (S85 PROVEN) |

So Reading B's "structurally parallel to M_KK" analogy is the weak point of the empirical reading: M_KK has *no* substrate selector and is honestly imported; τ_fold has a **PROVEN substrate selector** (the cusp uniqueness theorem) and merely lacks a *dynamical-attractor* derivation. Those are different deficits.

---

## 3. The dynamical mechanism-chain (the Reading-A name): I-1 → RPA → Turing → WALL → BCS

The S84 open channel names a concrete **non-variational dynamical selection structure**. It is not a fixed-point of a potential; it is a **first-order-transition criterion** assembled from five substrate dynamical conditions (knowledge base, theorem `proven_1459`, "Mechanism chain (I-1 → RPA → Turing → WALL → BCS) unconditional," PROVEN, atlas-04 B7):

1. **I-1** (instability onset): the τ=0 round-SU(3) configuration is an unstable maximum of S (the "cold big bang" — `project_cold-big-bang-vacuum-floor`: τ=0 unstable maximum, cascade inevitable). The substrate *must* flow to larger τ.
2. **RPA** (collective response): the random-phase-approximation susceptibility of the fiber develops structure as τ increases — the spectral weight begins to reorganize.
3. **Turing** (pattern selection): a Turing-type instability picks the wavelength/mode that goes critical first — this is a *dynamical* mode-selection, the analog of a fastest-growing mode in a quench.
4. **WALL** (first-order barrier): the transition is first-order — there is a spinodal/binodal structure, and the flow does not stop adiabatically; it nucleates and transits.
5. **BCS** (1D theorem, S35, unconditional): the BCS pairing in the 1D sector locks the post-transition condensate.

The selection statement is: **the first-order transition criterion `dS/dτ` crossing the van-Hove cusp at the BCS-pairing onset fixes τ_fold.** This is a *threshold-crossing* selection — the same logic as a quench crossing a critical point — not a minimization. The chain is `UNCONDITIONAL` (theorem `proven_2249`: "Mechanism chain UNCONDITIONAL. Paradigm shift to transit."). The paradigm itself (knowledge base, repeated) is: **transit physics, not equilibrium; instanton gas, not potential well.** Reading A *is* the framework's standing paradigm; Reading B is asking us to abandon it for τ_fold specifically.

`★` The crucial substrate-first reframe of "selection": in an equilibrium theory, a parameter is "selected" by sitting at a potential minimum. In a *non-equilibrium transit* theory, a parameter is "selected" by being the **threshold the dynamical flow is forced to cross** — the critical point of the quench. The S95 NO-WELL result tells us the equilibrium notion does not apply; the S85 cusp + the I-1→BCS chain tell us the *transit* notion does. Demanding that τ_fold be a potential minimum to count as "selected" is importing the equilibrium frame the whole framework rejects. `─`

---

## 4. Kibble-Zurek: a quantitative rate-class anchor (the closest thing to a number)

The transit through the fold is the canonical supersonic Mach-13.75 quench, and Kibble-Zurek physics gives the rate-class structure. The relevant pinned results:

- **v_terminal = 26.545** (canonical, S38 `s38_kz_defects.npz`) — the terminal transit velocity dτ/dt at the fold. This is a *computed* dynamical quantity, not a fit.
- **Mach_max = 13.75** (van Hove fold velocity ratio, canonical) — supersonic, the diabatic/sudden regime where the adiabatic vacuum breaks and real excitations (the GGE relic, 59.8 pairs, P_exc = 1.000) are produced.
- **Fold universality class = Rao v > v_c RANGE-controlled** (my own S100b W5-2 PASS, MEMORY): the GGE-relic content is a **count of modes in the spectral-excursion window** — spectral geometry, with `eps_LZ = 6.84e-4` sitting 6.43× inside the rate-flat boundary `eps_b = 4.39e-3`. The Landau-Zener adiabaticity parameter is *deep in the diabatic regime*, and the transit is **rate-flat** over Mach ∈ [5, 30] — i.e., the produced-relic structure is insensitive to the precise transit rate, controlled instead by the *range* of the spectral excursion (the van Hove window).

The KZ structure thus supplies a genuine dynamical anchor: **the transit is in the diabatic, range-controlled (not rate-controlled) class**, which is *consistent* with a van-Hove-window selection (the window is a spectral-geometric range, the rate is irrelevant). This is the rate-class prediction the workshop asks for — and it is a PASS. The fold is **tricritical-adjacent** (Li diagnostic: ν·z ~ 1 both sides = analytic first-order slope, `d²S` curvature ±2.71·δ), confirming first-order-transit character over a true second-order critical point. KZ does not by itself produce "0.190" — but it certifies that the *dynamical* object crossing τ_fold is in the correct (diabatic, range-controlled) regime for the cusp to be the selected threshold.

---

## 5. The pre-registrable selection gate (the workshop's actionable deliverable)

Reading A must put a gate on the table, not just a narrative. Here is the strongest pre-registrable structure, in two tiers.

### Gate A1 (the honest, achievable one) — **Cusp-coincidence selection gate** `[VERIFY]`

**Claim**: the dynamical transit-initiation criterion (the `dS/dτ ≠ 0` van-Hove-cusp crossing at the I-1→BCS first-order-transition onset) selects τ_fold = 0.190 with **zero free continuous parameters**, and is robust to the regulator/mesh.

- **Substrate observable**: the cusp location τ_cusp(L_max, a, BC) = argmax_τ [sharpness of ρ(λ=0; τ)].
- **Pre-registered PASS criterion**: τ_cusp(L_max=12, a=12, Γ₆) = 0.190 ± 0.5% AND the transit-identifier `dS/dτ(τ_cusp) ≠ 0` (sign + non-vanishing) AND robustness across L_max ∈ {8, 10, 12} within the Friedrich-Bär saturation band.
- **Inputs**: the L12 master spectrum cache (`s84_spectrum_cache_L12_tau019.npz`); the `dirac_spectrum.collect_spectrum` rebuild at a τ-grid bracketing 0.190; `dS_fold`, `d2S_fold` canonical anchors.
- **What PASS means for the solution space**: τ_fold is a substrate-IS, regulator-robust, parameter-free spectral feature — **selected by spectral geometry, dynamically crossed by the transit** — closing the "last tuned number" framing. τ_fold moves from "empirical input" to "van-Hove-selected, transit-crossed structural constant" (it already has the PERMANENT S85 theorem; this gate hardens it against the cusp/canonical mismatch in §6 below and against L_max).
- **What FAIL means**: τ_cusp drifts away from 0.190 under L_max or mesh refinement ⇒ the cusp location is regulator-artifactual ⇒ Reading B strengthens (the "selector" was a truncation accident).

**This gate is achievable now** and is the deliverable I will defend. It does NOT claim a potential-well attractor (which S95 closed); it claims a *spectral-cusp + transit-crossing* selection (which S85 already proved at L_max=10, and this gate extends + stress-tests).

### Gate A2 (the ambitious one — honestly flagged as the hard target) — **Modulus-EOM transit-initiation gate** `[SIGN]`

**Claim**: the modulus EOM `τ̈ + 3Hτ̇ + dV_eff/dτ = 0`, launched from the I-1 unstable maximum at τ ≈ 0, has its *first-order-transition / supersonic-crossing event* at τ = 0.190 (the cusp), with the transit velocity matching v_terminal = 26.545 there.

- This re-frames "selection" correctly: τ_fold is **where the flow goes supersonic / crosses the cusp**, NOT where it settles. My S112 CF-FLOQUET3-HPAR-TIGHTEN work integrated exactly this EOM with a physical Volovik-tracking V_eff and found the modulus **launches from τ_fold (v = 26.545), overshoots to τ_max ≈ 1.30, rings down, and settles to τ_final = 0.184** — it does NOT settle at τ_fold. **I flag this as the genuine threat (§6) and the reason Gate A2 is hard.**

---

## 6. HONEST engagement with the strongest threats

I will not strawman Reading B. There are three real threats, and I rate them in descending severity.

### Threat 1 (most severe) — the direction problem: "dynamical selection drives τ → τ_fold" is the WRONG frame.

The modulus does **not** flow *to* τ_fold and stop. The EOM (my S112 integration, and S73B before it) **launches FROM τ_fold** with v_terminal = 26.545, overshoots, and settles at τ_final ≈ 0.184, not 0.190. So if "dynamical selection" means "an attractor of the modulus EOM at 0.190," that reading **fails** — there is no attractor at 0.190; 0.190 is the *initial condition* of the transit.

**My honest response**: this defeats the *attractor* version of Reading A but not the *threshold-crossing* version. τ_fold is selected as **the cusp the supersonic flow is forced to cross**, exactly analogous to how a quench "selects" the critical point T_c — not because the system settles at T_c, but because T_c is the parameter-free location where the order parameter goes critical and defects freeze in. T_c is *selected by the spectrum* (it is a thermodynamic singularity), and the quench *crosses* it; nobody calls T_c "tuned" because the system ends up at T ≠ T_c. **τ_fold = 0.190 is the substrate's T_c.** The S85 van Hove cusp IS that thermodynamic singularity, proven parameter-free. So the correct Reading-A statement is:

> τ_fold is **dynamically selected as the transit-critical threshold** (the van-Hove cusp the diabatic flow crosses), not as an EOM attractor. The selection is structural (S85 cusp uniqueness) + dynamical-kinematic (the I-1→BCS first-order criterion forces the crossing), and it is parameter-free.

This is weaker than "an attractor drives τ → 0.190" but it is **stronger than "empirical input"**: an empirical input has no substrate selector; τ_fold has a PROVEN one (the cusp). Whether the workshop credits "selected-as-crossed-threshold" as *bona fide* selection or downgrades it to "structurally-pinned initial condition" is the central adjudication, and I think the honest verdict is the former — because the cusp location is *not* a free initial condition, it is forced by the spectrum.

### Threat 2 — "the t-modulus closed variationally (t = 1/2 EXACT) but τ_fold did NOT; same machinery, different outcome ⇒ τ_fold is just unselected."

**Response**: the two moduli are **different kinds of object**, so the asymmetry is expected, not damning. t (the rank-4b t-operator modulus, S101) is an **internal algebraic modulus** of the spectral triple — it sits at a genuine extremum of the spectral action because it parametrizes a symmetry of the finite algebra, and symmetric points ARE stationary points. τ (the Jensen deformation) is a **transit coordinate** — the parameter along which the first-order cosmogenesis transition runs. There is no reason a transit coordinate should sit at an action extremum; on the contrary, S85 *proves* it sits at non-stationarity (`dS/dτ ≠ 0`). So:

- t closes variationally **because it is the kind of modulus that has a well** (an algebraic symmetry point). ✓ action selects it.
- τ_fold does NOT close variationally **because it is the kind of modulus that is a transit threshold** (a van Hove cusp, non-stationary by theorem). ✓ action correctly reports NO-WELL; the *cusp* selects it instead.

"One modulus the action closes, one it does not" is then not "the action is inconsistent" but "the action selects the modulus that is an extremum and (correctly) does not select the one that is a transit cusp — and a *different* substrate structure (the van Hove theorem) selects that one." The framework has **two selection mechanisms for two modulus types**: variational for algebraic moduli, van-Hove-cusp-crossing for the transit modulus. That is more structure, not less.

### Threat 3 — the cusp/canonical numerical mismatch: refined DOS cusp at τ_cusp = 0.221, canonical τ_fold = 0.190.

This is a real, specific tension I carry in my own memory (S111-CF-TAUCUSP) and must disclose. The `S85-VAN-HOVE-CUSP-THEOREM` gate (DOS-cusp, Baptista-sign, L_max=8) returned **value = 0.221 and FAILED**, while the `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` (L_max=10) returned 'promoted' and PASSED. My τ-cusp memory records the resolution: "τ_cusp = 0.221 refined, canonical τ_fold = 0.19 **on the rising flank**; rel_dev = 0.162609 non-stationarity." So the canonical 0.190 sits ~16% below the refined cusp peak, on its rising flank.

**Response**: this is exactly what Gate A1 must resolve, and I do NOT hide it. Two readings:
- (Reading-A-favorable) The cusp is a *region* with a sharp peak at 0.221 and a rising flank through 0.190; the transit-identifier `dS/dτ > 0` is what pins the *crossing point* (0.190) on the flank, where the substrate goes supersonic, distinct from the DOS-peak (0.221). The transit crosses the rising flank at 0.190; the DOS peak at 0.221 is where it would peak if it stopped — but it doesn't stop (NO-WELL). This is *consistent* with the transit picture: the supersonic flow crosses the flank, it doesn't sit at the peak.
- (Reading-B-favorable) The 16% gap between the "selector" (cusp peak 0.221) and the "selected value" (0.190) means the selector does NOT cleanly pick 0.190 — there is a residual tuning of *where on the flank* the canonical value sits.

I concede Reading B has a real point here: **the cusp uniqueness theorem pins a cusp region, and the precise 0.190 vs 0.221 requires the transit-identifier to do additional work.** Gate A1's PASS criterion (τ_cusp = 0.190 ± 0.5% AND `dS/dτ ≠ 0`) is therefore the *decisive* test: if the transit-crossing point is genuinely at 0.190 (flank-crossing where the flow goes supersonic) and that is L_max-robust, Reading A wins; if the only L_max-robust feature is the 0.221 peak and 0.190 is a flank-point chosen post-hoc, Reading B wins. **I am pre-registering the gate that could falsify my own pole.** That is the open-verdict discipline.

---

## 7. Where this leaves the adjudication

The two readings are NOT "selected vs unselected." The honest structure is:

- **τ_fold has a PROVEN substrate selector** (S85 van Hove cusp uniqueness, PERMANENT) — this is NOT in dispute and it is what distinguishes τ_fold from the genuinely-unselected M_KK. Reading B's "structurally parallel to M_KK" analogy is **false** at the selector level: M_KK has no selector; τ_fold has one.
- **The selector is a transit threshold, not a potential well** — so the S95 NO-WELL FAIL is a *consistency check that Reading A passes*, not a refutation. The variational selectors S95 closed were searching for the wrong kind of object.
- **The dynamical mechanism-chain (I-1→RPA→Turing→WALL→BCS, UNCONDITIONAL) forces the crossing** — the first-order transit is what carries the substrate through the cusp at the diabatic, range-controlled (rate-flat) Kibble-Zurek class (S100b PASS). This is the "dynamical" content.
- **The genuine residual deficit** is NOT "τ_fold is empirical" but "the *precise* 0.190 (vs the 0.221 DOS-peak) and the *EOM-attractor* status are not yet pinned." Reading A's claim is "transit-threshold selection (parameter-free cusp-crossing), gate-able via A1"; it is NOT "EOM attractor at 0.190" (that fails — the modulus settles at 0.184).

So the structural verdict I will push toward in R2/R3 is a **third position that is closer to A than to B**: τ_fold is **a van-Hove-selected, transit-crossed structural constant** — dynamically selected as the first-order-transition threshold, parameter-free, but NOT a potential-well attractor. The pre-registrable gate is A1 (cusp-coincidence at L_max=12, ±0.5%, with the `dS/dτ ≠ 0` flank-crossing condition). This is a *forward compute*, which is the "named dynamical-relaxation selection gate" outcome the workshop spec lists for Reading A — sharpened to the achievable van-Hove-crossing form rather than the (S95-closed) variational form.

---

## (i) Honest current lean

**Lean ~70% Reading A, but in its corrected (threshold-crossing, not attractor) form** — and I credit Reading B with a real ~30% on the residual that "selected-as-crossed-threshold" may be adjudicated as "structurally-pinned initial condition," and on the unresolved 0.190-vs-0.221 flank mismatch.

The reason I do not go higher: the *attractor* version of dynamical selection genuinely fails (the EOM launches from τ_fold and settles elsewhere — my own S112 integration shows this), so "a dynamical mechanism drives τ → τ_fold and holds it there" is false. The reason I do not go lower: τ_fold demonstrably has a **PROVEN, parameter-free substrate selector** (the S85 van Hove cusp uniqueness theorem, PERMANENT), which is categorically more than the genuinely-unselected M_KK that Reading B wants to equate it to. "Empirical input parallel to M_KK" is the one framing I think the physics clearly **forbids** — M_KK has no selector; τ_fold has a proven one.

## (ii) The single most decisive consideration

**Is the cusp-crossing point genuinely at τ = 0.190 and L_max-robust, or is only the 0.221 DOS-peak robust while 0.190 is a post-hoc flank-point?** This is the one fact that flips the verdict. If Gate A1 returns τ_cusp(transit-crossing) = 0.190 ± 0.5% stable across L_max ∈ {8,10,12} with `dS/dτ ≠ 0`, then τ_fold is a parameter-free van-Hove-selected, transit-crossed constant and Reading A (corrected form) wins decisively. If only the 0.221 peak is L_max-stable and 0.190 is chosen on the flank to match the canonical, then the selector under-determines the value and Reading B's "residual empirical tuning of the flank-point" stands. Everything else (the NO-WELL consistency, the mechanism-chain, the KZ rate-class) is settled in Reading A's favor; this one number is the open hinge.
