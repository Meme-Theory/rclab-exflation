# WS-S112-2 TAUFOLD — R3 Structural Verdict (open)

**Workshop**: WS-S112-2 TAUFOLD — τ_fold dynamical selection (Reading A) vs irreducible empirical modulus (Reading B). EVOI Tier-2 #4 ("τ_fold = 0.190 is the last tuned number").
**Adjudication question**: Does a substrate-dynamical mechanism-chain select τ_fold = 0.190, or is it an irreducible empirical modulus? If dynamical, what is the pre-registrable selection gate?
**Round files**: `transit-r1.md` (Reading A, threshold-crossing form) · `lizzi-r1.md` (Reading B, monotone-empty-critical-set) · `transit-r2.md` (A rebuttal) · `lizzi-r2.md` (B rebuttal). All four read.
**Author of this verdict**: transit-dynamics-theorist (assigned Reading-A pole), writing the verdict NEUTRALLY per the open-verdict discipline (`epistemic-discipline.md §"Cross-Proxy Adjudication"` item 2). The verdict does **not** favor Reading A; it reports what the four rounds + the verified verdict-file record force.

---

## 1. Each agent's FINAL lean (from R2)

| Pole | Agent | Final lean (R2) | One-line basis |
|:--|:--|:--|:--|
| **A** (dynamical selection survives) | transit-dynamics-theorist | **~0.58 A (corrected, threshold-crossing form) / ~0.42 B for the precise value** — moved down from R1's 0.70 | The van Hove cusp is a real, parameter-free *region*-selector (S85, PROVEN, Sage-confirmed functionally independent of monotonicity); but the *attractor* version is dead (own S112 EOM settles at 0.184, not 0.190), and the precise 0.190-vs-0.221-peak flank-value is unproven at L_max-saturation. |
| **B** (irreducible empirical modulus) | lizzi-spectral-functional-theorist | **~0.82 B / ~0.18 A** — up slightly from R1's 0.80 | The action is strictly monotone in τ (empty critical set, f-independent, 9,600/9,600), so unselectable by *any* spectral functional; the cusp transit cites is a *non-stationarity* theorem (= Reading B's claim) and its *location* is regulator-conditional (0.221 from-scratch L_max=8, FAIL at L_max=5 alt-mesh, frozen-0.190 only verified not derived). |

**Convergence note (the structurally important fact).** The two poles converged to a near-shared structure and **pre-registered the same gate** as the decider, differing only in their *predicted outcome* for it. Both independently killed the gradient/EOM-attractor reading — transit via its own S112 integration (modulus settles at τ_final ≈ 0.184), lizzi via the monotonicity theorem (no interior fixed point of a gradient flow on a monotone S). This is not a stalemate; it is a genuine convergence that localizes the entire remaining disagreement to one computable question.

---

## 2. The crux

> **Lizzi's symbolic claim**: the τ_fold spectral action is strictly monotone with an **EMPTY critical set** (`dS/dτ = +58,673 > 0`, no solution to `dS/dτ = 0`), in contrast to the t-modulus which has an **interior stationary point** (`u′(1/2) = 0`, `u″(1/2) = −2 ≠ 0`, an extremum). So τ_fold is **scheme-robustly unselectable by any spectral functional** (the monotonicity holds for all monotone f, all Λ, all 10 sectors). Does Reading A's dynamical mechanism EVADE this, or CONFIRM it?

**The verdict's answer: Reading A's mechanism EVADES the monotonicity theorem as stated, but does NOT (on current evidence) supply the regulator-independent selector the evasion would need to defeat Reading B. The evasion is structurally valid; the substitute selector is unproven.** Three sub-findings, each grounded:

**(2a) The monotonicity theorem is correct, f-independent, and conceded by BOTH poles.** `dS/dτ = +58,673 > 0` everywhere ⇒ empty critical set ⇒ no action *well* ⇒ the action does not select τ_fold by *extremization*. This is common ground (transit-r2 §0 concession 1; lizzi-r1 §2). It is also exactly the S95 NO-WELL-ONE-LOOP PASS. **Nothing in the workshop contests it.**

**(2b) The evasion is structurally valid: selection-by-cusp-crossing is a DIFFERENT functional than selection-by-action-extremization, and the two are logically independent (Sage-verified).** Transit's R2 §3 proved symbolically that a strictly monotone `S(τ) = Tr f(D_K²/Λ²)` and a van Hove cusp in `ρ(λ; τ) = Σᵢ δ(λ − λᵢ(τ))` coexist: a band-edge eigenvalue `λ₁ = √|τ−τc|` gives `dλ/dτ → ∞` (DOS diverges, cusp) at exactly the τc where `dS_mode/dτ` stays finite and smooth. So lizzi's theorem operates on `S` (a smooth moment-sum); the cusp operates on `ρ` (the density). **"No interior critical point of S" (TRUE) does NOT entail "no substrate feature distinguishes τ_fold" (the cusp is in ρ, not S).** Lizzi conceded the frame's legitimacy in R2 §1 concession 2: "a modulus can be physically distinguished as the threshold the flow is forced to cross even with no well there." So the *equilibrium* premise "selection ≡ action-stationarity" does not bind a *transit* modulus. **The evasion holds: monotonicity of S does not foreclose a cusp-crossing distinction of τ_fold.**

**(2c) BUT the evasion's substitute selector — the cusp *location* — is regulator-CONDITIONAL on current evidence, and a regulator-conditional threshold cannot pin a parameter-free value.** This is lizzi's R2 §3, and the verdict verified each data point against the canonical verdict files:

| Gate (verified, knowledge-MCP) | L_max / convention | Result |
|:--|:--|:--|
| `S85-VAN-HOVE-CUSP-THEOREM` (DOS-cusp from scratch) | L_max=8, Baptista-sign | **0.221, FAIL** |
| `S85-W10-TAU-FOLD-UNIQUENESS-VAN-HOVE-THEOREM` | L_max=10, `convention=canonical_constants-S85-freeze`, `value='promoted'` | PASS — verifies non-stationarity **at a frozen 0.190**, does not derive the location |
| `S84-ALTERNATIVE-TAU-MESH-UNIQUENESS` | L_max=5, `tau_mesh_1e_4_step`, `scheme=triple_gear_AND` | **value=0, FAIL** |
| `S111-CF-TAUCUSP` | refined cusp vs canonical | INFO, `relDev=0.1626`, cusp-excess 0.4695 |

The from-scratch cusp peak is **0.221** (16.3% off the used 0.190); the L_max=10 "uniqueness" PASS *imported* 0.190 (`value='promoted'` is a status string, convention literally `canonical_constants-S85-freeze`) rather than computing it; the L_max=5 alternative mesh **FAILS**. **So the cusp's *existence* (non-stationarity) is robust, but its *location* moves with the regulator on the evidence in hand.** A van Hove singularity whose location is L_max/mesh-dependent is, in functional-pluralism terms, a scheme-dependent feature — the diagnostic that separates the (scheme-dependent) a_0 cosmological constant from the (scheme-robust) ratios and the t=1/2 closure (`u′(1/2)=0` exact, grade-by-grade, f-INDEPENDENT to machine precision).

**Synthesis of the crux**: Reading A correctly evades the *letter* of the monotonicity theorem (the cusp is a different functional, Sage-proven), so τ_fold is **not** "unselectable by any functional" in the strong sense lizzi's headline asserts — the cusp IS a substrate feature S does not see. But Reading A has **not yet** exhibited the regulator-INDEPENDENT cusp-location the threshold-crossing frame requires to pin the *value* 0.190. On current evidence the cusp constrains τ_fold to a ~16%-wide region whose location is regulator-conditional, and the precise 0.190 is frozen on its flank. **The evasion is real; the selection-of-the-value is unproven.**

---

## 3. STRUCTURAL VERDICT

### **SYNTHESIS, resolving to Reading-B-DEFAULT on current evidence, with a single pre-registered compute (Gate A1′) that can flip it to Reading-A.**

The honest landing is neither "A wins" nor "B wins" but a **partition** both poles converged on:

**Settled core (NOT in dispute after R2 — the synthesis):**

- **(S1) The gradient/EOM attractor reading is DEAD.** No substrate-natural gradient flow or modulus EOM lands on τ_fold = 0.190 — the modulus launches *from* τ_fold and settles at τ_final ≈ 0.184 (transit's own S112 integration). Both poles agree. *This is the conservative-standard outcome the team-lead pinned*: neither pole **exhibited a zero-parameter substrate dynamical attractor landing on 0.190**, so the attractor-form of Reading A is conceded by both.

- **(S2) The cusp is a real substrate feature, distinct from action-extremization, that M_KK has no analog of.** The van Hove cusp uniqueness theorem (PROVEN/PERMANENT) establishes a parameter-free spectral *region*-selector — Sage-confirmed functionally independent of the monotonicity theorem. M_KK has N₃=0 (no substrate handle at all); τ_fold has a cusp region that localizes it to ~16%. **So τ_fold is NOT "as unconstrained as M_KK"** — lizzi conceded exactly this refinement in R2 §4 ("τ_fold is better-constrained than M_KK... cusp-localized to a region").

- **(S3) The mechanism-chain (I-1→RPA→Turing→WALL→BCS, UNCONDITIONAL) forces a CROSSING, not the VALUE.** Both poles agree the substrate undergoes a first-order transit that crosses *a* cusp, in the diabatic range-controlled Kibble-Zurek class (S100b PASS) — but none of the five chain conditions contains the number 0.190 (lizzi-r2 §5; transit conceded "KZ does not by itself produce 0.190" in transit-r1 §4). The dynamics fix the *crossing*; the *value* is delegated to the cusp location.

**The single open hinge (the only thing the two poles still dispute — a *prediction*, not a fact):**

- **(H) Is the cusp-CROSSING location (the `dS/dτ ≠ 0` flank point where the flow goes supersonic, NOT the DOS-peak) regulator-INDEPENDENT at τ = 0.190 across L_max ∈ {8, 10, 12}?** If yes → τ_fold is a parameter-free, van-Hove-selected, transit-crossed structural constant (Reading A, corrected form). If only the cusp's *existence* is robust while its *location* is scheme-dependent (0.221 from-scratch, mesh-FAIL, 0.190 a frozen flank-point) → the cusp constrains τ_fold to a regulator-dependent region but does not select 0.190, and τ_fold joins M_KK as a (better-constrained) external-dimensional-import (Reading B).

**First-principles reason the verdict defaults to Reading-B on *current* evidence while remaining a synthesis:**

The conservative standard is "EXHIBIT a zero-parameter attractor landing on 0.190, OR concede injection." Neither pole exhibited it; both agree it is dead (S1). The remaining Reading-A route (the threshold-crossing cusp) has a PROVEN *region*-selector (S2) but its *value*-level regulator-independence is **untested at saturation L_max** — and the three data points that DO exist (0.221 from-scratch at L_max=8; FAIL at L_max=5 alt-mesh; verified-at-frozen-0.190 at L_max=10) currently show the cusp *location* moving with the regulator. By the evidence-hierarchy discipline (`epistemic-discipline.md`: computational gates are decisive, structural identities are permanent), the permanent structural facts (S2: cusp exists, parameter-free region) and the decisive gates-on-the-books (location regulator-conditional) together yield: **the substrate selects a cusp region but has not been shown to select the value 0.190 in a regulator-independent way.** That is the Reading-B verdict *for the precise value* — but as a *synthesis*, because it simultaneously affirms (S2) that τ_fold is materially better-constrained than M_KK and (H) names the exact compute that would promote it to Reading-A.

**Why NOT a clean "Reading B" (lizzi's headline) and NOT a clean "Reading A":**
- Against clean Reading B ("τ_fold is the second M_KK, unselectable by any functional"): FALSE in the strong form — the cusp IS a substrate feature the action does not see (Sage-proven), and it localizes τ_fold to a region M_KK has no analog of. Lizzi's own R2 §4 retreated from "as unconstrained as M_KK" to "better-constrained-but-imported." The strong "unselectable by ANY functional" claim conflates the action (S) with the density (ρ).
- Against clean Reading A ("dynamical selection survives, full stop"): FALSE — the attractor is dead (both agree), and the surviving threshold-crossing selector has not been shown regulator-independent at the value level. Transit's own R2 moved to 0.58 and conceded the 16% flank residual is live.

The verdict is therefore a SYNTHESIS whose *current-evidence resolution* is Reading-B-for-the-value / cusp-region-selected-structure, **explicitly conditional on Gate A1′** — the one compute both poles pre-registered as the decider.

---

## 4. Forward artifact

Per the team-lead's instruction, the verdict supplies BOTH the conditional gate (the synthesis's open hinge) AND, because the current-evidence resolution is Reading-B-for-the-value, the pinned-statement skeleton — with the registry/falsifier edit ROUTED to `mack-cosmic-bridge` (not written here, per `feedback_mack-bridge-role.md`).

### 4A. Pre-registrable gate (the synthesis decider) — **Gate A1′: cusp-crossing regulator-independence** `[VERIFY]`

The 4-field spec both poles converged on (transit-r2 §6 Gate A1′; lizzi-r2 §7 endorsement):

1. **What**: compute the van Hove cusp-*crossing* location — the τ at which ρ(λ=0; τ) is non-analytic AND the transit-identifier `dS/dτ ≠ 0` flank-crossing condition holds — **from scratch on a τ-grid bracketing [0.18, 0.23] with NO injected 0.190**, at L_max ∈ {8, 10, 12}, plus the L_max=5 alt-mesh point. Distinguish the cusp-*crossing* point (flank, where the flow goes supersonic) from the DOS-*peak* (0.221) — they are different observables, and the claim is that the *crossing* point, not the peak, is the physical fold. Report the *trend* of the crossing location vs L_max against the Friedrich-Bär saturation band (do NOT tally mixed-L_max PASS/FAIL — the L_max=5 and L_max=8 points are coarse-truncation, where location drift is expected; the decisive question is whether the crossing location *converges* to 0.190 as L_max → saturation).
2. **Inputs**: L12 master spectrum cache `s84_spectrum_cache_L12_tau019.npz`; `dirac_spectrum.collect_spectrum(τ, …, max_pq_sum=L)` rebuild on the bracketing τ-grid at L ∈ {5,8,10,12}; canonical anchors `dS_fold`, `d2S_fold`; the `S84-ALTERNATIVE-TAU-MESH-UNIQUENESS` mesh (`tau_mesh_1e_4_step`) as the mesh-robustness arm. **Zero continuous free parameters** — the grid brackets the region; the cusp-finder + transit-identifier locate the value; 0.190 is NOT supplied to the finder.
3. **Gate (pre-registered PASS/FAIL/INFO)**:
   - **PASS (→ Reading A, corrected form)**: the cusp-crossing location → 0.190 ± 0.5% and is L_max-MONOTONE-CONVERGENT toward 0.190 across {8,10,12} within the Friedrich-Bär band, AND mesh-robust. ⇒ τ_fold is a parameter-free, van-Hove-selected, transit-crossed structural constant; the `EMPIRICAL-τ_fold RETENTION` default-fallback channel is RETIRED; the M_KK parallel is downgraded to "value-selected."
   - **FAIL (→ Reading B, for the value)**: the crossing location does NOT converge to 0.190 (stays at/near 0.221, or remains mesh-dependent, or 0.190 is recoverable only by freezing). ⇒ the cusp selects a regulator-dependent *region*; 0.190 is the imported flank-point; τ_fold joins M_KK in the external-dimensional-import set (better-constrained than M_KK, but value-imported).
   - **INFO**: crossing location L_max-convergent to a value in [0.19, 0.221] but not within ±0.5% of 0.190 at saturation ⇒ the *region* is substrate-selected, the precise canonical 0.190 is a flank-sub-choice within a substrate-pinned window (a HYBRID — strictly stronger than M_KK, weaker than full value-selection).
4. **Effort**: ~1 compute-agent session. Spectrum rebuilds at L ≤ 12 are cached/feasible (the L12 master cache exists; L=5/8 are cheap; the recursive-Casimir-construction ceiling is L≥13, NOT triggered). The cusp-finder + central-FD `dS/dτ` flank-locator is a small script. GPU not required (small per-τ eigensolves). This is the "named dynamical-relaxation selection gate (a forward compute)" the workshop spec lists as the Reading-A outcome — sharpened to the achievable cusp-crossing-robustness form (NOT the S95-closed variational form, NOT the dead EOM-attractor form).

**Depends on**: `s84_spectrum_cache_L12_tau019.npz`; `dirac_spectrum` module; `dS_fold`/`d2S_fold` canonical pins; the `S84-ALTERNATIVE-TAU-MESH-UNIQUENESS` mesh convention. Routes to `/rclab-plan` S114 Wave-1 (compute), agent = transit-dynamics-theorist or spectral-geometer (the cusp/DOS axis).

### 4B. Pinned-statement skeleton (current-evidence resolution) — route to mack-cosmic-bridge

Because the synthesis's current-evidence resolution is Reading-B-for-the-value, the verdict ALSO emits the honest capstone statement, for `mack-cosmic-bridge` to land (sole writer of `falsifier-master-inventory.md` and the §7 falsifier surface per `feedback_mack-bridge-role.md`; the capstone-hygiene Q3 PROSE down-tag routes via the designated writer per `capstone-hygiene-gate.md`):

> **Pinned statement (DRAFT for mack, conditional on Gate A1′):** *τ_fold = 0.190 is, on current evidence, NOT shown to be selected as a parameter-free value: the substrate's spectral action is strictly monotone in τ (empty critical set, f-independent, 9,600/9,600 — atlas-04 S1 DISSOLVED), so τ_fold is not selected by action-extremization; and the van Hove cusp that distinguishes τ_fold as a transit-crossing threshold (S85-W10, PERMANENT) is a region-selector whose computed location is regulator-conditional on current evidence (0.221 from-scratch at L_max=8; FAIL at L_max=5 alt-mesh; verified-not-derived at frozen-0.190 at L_max=10). τ_fold therefore joins M_KK as a member of the framework's external-dimensional-import set — with the structural REFINEMENT that, unlike M_KK (N₃=0, no substrate handle), τ_fold is cusp-region-localized to ~16%. The "empirical input" status is CONDITIONAL on Gate A1′ (S114): a regulator-convergent cusp-crossing at 0.190 ± 0.5% would promote τ_fold from "imported value" to "van-Hove-selected structural constant."*

- **Routing**: atlas-04 **A4** ("τ_fold/moduli selection BROKEN") — refine from bare "BROKEN" to "BROKEN-by-action-extremization / cusp-region-selected / value-conditional-on-A1′". Capstone §6.3-adjacent (the moduli-selection honesty item, parallel to the M_KK external-import narration S112 W1 just landed). Falsifier inventory: NO new live-falsifier row (this is a selection-status statement, not an observable) — it is a capstone honesty item + an EVOI Tier-2 #4 status update.
- **Capstone-hygiene Q3 fires** (PROVEN/CONDITIONAL status change to a capstone claim): the prose tag must read "τ_fold selection CONDITIONAL (pending Gate A1′)", NOT "selected" and NOT "tuned" — reconciled against atlas-04 A4. This is a designated-writer patch, not a bulk append.

---

## 5. Residual dissent + the decisive compute

**Residual dissent (genuine, narrow, and symmetric):** The two poles agree on the entire structure (S1-S3) and on the gate (A1′); they dissent **only on the predicted outcome of A1′**, and they dissent *symmetrically* (each predicts the gate confirms their pole):

- **transit (A)** predicts: the cusp-*crossing* point (flank, where the flow goes supersonic) is the L_max-robust feature and converges to 0.190 as truncation saturates — the 0.221 peak and the L_max=5 FAIL are *coarse-truncation* artifacts (both at L_max ≤ 8, below the Friedrich-Bär saturation regime), and the *trend* will favor 0.190. (transit-r2 §6: "FAIL would land a hybrid... at the ~16% level.")
- **lizzi (B)** predicts: only the cusp's *existence* (non-stationarity) is L_max-robust; the *location* stays regulator-dependent or coincides with 0.221, with 0.190 a frozen flank-choice. (lizzi-r2 §6: "Gate A1 will find the cusp region robust and the precise crossing-point either regulator-dependent or coincident with 0.221.")

Neither dissent can be foreclosed from the existing evidence: the three existing location data points are all at L_max ∈ {5, 8, 10}, and only L_max=10 reaches the canonical truncation — but that one *imported* 0.190 rather than deriving it. **So no existing gate has computed the cusp-crossing location from-scratch at saturation L_max.** That is precisely the gap.

**The decisive compute: Gate A1′ (§4A).** The single computation that resolves the workshop is the from-scratch, no-injected-0.190, L_max-convergence test of the cusp-*crossing* location (distinguished from the DOS-peak) across L_max ∈ {5, 8, 10, 12} with mesh-robustness. Its three pre-registered outcomes (PASS → Reading A / FAIL → Reading B / INFO → hybrid-window) map cleanly onto the synthesis's open hinge (H). Until it runs, the honest status is: **SYNTHESIS — cusp-region-selected, attractor-dead, value-conditional; current-evidence default Reading-B-for-the-value; A1′ is the pre-registered decider.**

**Honest meta-note on the verdict's own neutrality**: I am the assigned Reading-A pole and I am writing a verdict whose current-evidence resolution is Reading-B-for-the-value. I do this because the conservative standard the workshop set — "exhibit a zero-parameter attractor at 0.190 or concede injection" — was NOT met by either pole (the attractor is dead by transit's own computation), and the surviving Reading-A route (cusp-crossing) has a PROVEN region-selector but an UNPROVEN value-selector. The synthesis credits Reading A with exactly what the physics earns (the cusp is real, parameter-free at the region level, functionally independent of the monotonicity theorem, and gives τ_fold a substrate handle M_KK lacks) and credits Reading B with exactly what the physics earns (no functional selects the *value* on current evidence; the precise 0.190 is, today, an imported flank-point). The one compute that would break the symmetry is named and pre-registered.

---

*End of Round 3 structural verdict (transit-dynamics-theorist, written neutrally). Workshop WS-S112-2 TAUFOLD complete. Forward artifacts: Gate A1′ (§4A, → /rclab-plan S114 Wave-1) + pinned-statement skeleton (§4B, → mack-cosmic-bridge for atlas-04 A4 / capstone / EVOI Tier-2 #4 status update).*
