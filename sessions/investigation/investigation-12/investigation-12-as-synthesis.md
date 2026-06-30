# Investigation 12 Synthesis: A_s — Three-Route Integrated Status + CF23-Tag Re-Evaluation

**Date**: 2026-06-17
**Agent**: gen-physicist (neutral integrative reviewer, INV12-W4-3)
**Review type**: INTEGRATIVE (not adversarial — the adversarial A_s framing was INV12-W4-1). Unique contribution: integration of the van den Dungen Bismut-Cheeger η-form route (W2-5), which neither prior workshop covered.
**Source Documents**:
- `sessions/investigation/investigation-12/investigation-12-w1-workingpaper.md` §W1-2 (lizzi modular-reference route)
- `sessions/investigation/investigation-12/investigation-12-w2-workingpaper.md` §W2-5 (vdd FWD-C1 Bismut-Cheeger η-form route)
- `sessions/investigation/investigation-12/investigation-12-w3-workingpaper.md` §W3-1/§W3-2/§W3-3/§W3-4/§W3-5 (transit-dynamics chain)
- `sessions/investigation/investigation-12/workshops/as-wall-reading.md` (INV12-W4-1 STRUCTURAL VERDICT)
- `sessions/framework/Atlas/atlas-08-open-questions.md` (CF23 tag)
- `sessions/framework/registry/falsifier-rigor-registry.md` (A_s Row 8)
- `computations/investigation-12/inv12_gate_verdicts.txt` (verdict ledger)

**Verdict-line status**: NONE. This is a `gate_type: review` artifact — it closes by artifact-existence-with-content per `gate-verdicts.md §"Investigation-Track Canonical Path"`. **Advisory only**: per the investigation-track-local boundary, this synthesis does NOT mutate the session-track register (CF23 in `atlas-08-open-questions.md`, the `falsifier-rigor-registry.md` A_s Row 8, or any Atlas doc). It produces the integrated reading a future session-promotion would act on.

---

## I. Session Outcome

**The three structurally-orthogonal A_s attack routes JOINTLY CONFIRM the wall as a substrate-IS physical floor, and JOINTLY RELOCATE every open question OFF that floor onto two distinct scheme-dependent legs.** The A_s floor `A_s ≥ A_s^{BD}` (equivalently `S_IC = |α_k+β_k|² = 1 + 2n_k ≥ 1`) is independently confirmed on three non-overlapping mathematical axes — reference-state (W1-2), families-index/topological (W2-5), and Bogoliubov-relic/dynamical (W3-1/2/3/4/5). No route dissolves the wall; none even lowers A_s toward Planck. The CF23 recommendation is therefore **CONFIRMED for the floor, with a mandatory SCOPE SHARPENING**: the permanent-structural-position content is the *floor in sign*, not the undifferentiated "3.02× wall" the present CF23 prose narrates. The magnitude (1.57× / 2.42× / up to 7.7×) and the upper-edge greybody filter (∫Γ derived 0.036 vs fitted 0.512) are **SCHEME-DEPENDENT and underived — open, not permanently walled.** They are RELOCATED, not dissolved.

The substrate-first reading throughout: A_s is the post-transit GGE-relic acoustic amplitude. The chain is `D_K eigenvalues → transit Bogoliubov coefficients {α_k, β_k} → produced occupation n_k = |β_k|² → squeezing modulus S_IC = 1+2n_k → relic power-spectrum amplitude A_s`. It is never a ΛCDM inflaton normalization; "A_s" names the squeezing modulus of the produced relic state on the curvature-perturbation amplitude.

---

## II. Key Results

### II.1 The substrate-IS floor object — one inequality, three orthogonal confirmations

**Result**: `A_s = A_s^{BD} · S_IC` with `S_IC(k) = |α_k + β_k|² = 1 + 2 n_k ≥ 1`, `n_k = |β_k|² = ⟨a_k† a_k⟩_relic ≥ 0`. **Classification: PHONONIC** (produced GGE-relic squeezing modulus on the acoustic curvature amplitude).

The floor is a produced-side fact: `n_k` is the output of the parametric-oscillator mode equation `u_k'' + ω_k²(τ) u_k = 0` through the van Hove fold, fixed by the transit Bogoliubov coefficients and the matching conditions — NOT by any choice of reference vacuum. Bunch-Davies is merely the `n_k = 0` infimum of the produced ladder. The wall `S_IC ≥ 1` is forced by two unitarity facts that hold in every regularization: number-operator positivity `n_k ≥ 0`, and the symplectic/Bogoliubov constraint `|α_k|² − |β_k|² = 1`.

The integrative point of this synthesis is that THREE independent machineries — none of which shares inputs or method with the others — each return the same floor verdict. That is the structural-confirmation pattern `joint-theorem-promotion.md` and `epistemic-discipline.md` recognize as decisive: not agreement-among-agents (shared context), but agreement-among-orthogonal-derivations on the same structural object.

### II.2 Route 1 — reference-state axis (W1-2): the wall is reference-state-INDEPENDENT

**Result**: `R_wall^{GGE} = 2.4182 ≡ R_wall^{BD}`; `K_sub = S_IC^{GGE}/S_IC^{BD} = 1 + 2n_k ∈ [1.0000205, 1.0038373]`, every reading ≥ 1; `Δ = A_s^{GGE} − A_s^{BD} = +1.04e-13 > 0`. Composite **FAIL** (sign=FAIL, magnitude=INFO, regime=VALID). **Classification: PHONONIC.**

This route dispatched the framework's own highest-leverage attack: replace the Bunch-Davies vacuum reference with the substrate's actual post-transit GGE modular state ω (the faithful normal weight on `A_hor = A_K ⋊_{σ^ω} ℝ`, §VII.BZ, STAGE-3-PERMANENT S105–S106) and ask whether the BD-referenced bound lifts. It does not — it equal-or-amplifies. The W4-1 workshop then closed the one residual the diagonal `1+2n_k` form left open (the off-diagonal anomalous correlator `⟨a_k a_{-k}⟩ = α_k β_k*`) STRUCTURALLY, via the registry theorem that the Type-II semifinite trace is the UNIQUE faithful normal tracial weight fixed by the second moment: A_s is a second-moment functional, the anomalous correlator is an entry of that same trace-fixed second moment (bound to `n_k` by `|α|²−|β|²=1`), and the FROZEN-GGE-NON-KMS lock makes Cauchy-Schwarz strict (`|⟨a_k a_{-k}⟩| < n_k`). No admissible modular weight lowers A_s. **The reference-state-artifact reading is dead in both its diagonal (W1-2 landed) and phase-coherent (W4-1 theorem) forms.**

### II.3 Route 2 — families-index / topological axis (W2-5): the η-form carries ZERO normalization content

**Result**: Bismut-Cheeger η-form of the τ-family `{D_K(τ)}` across `[0, τ_fold]` = **0** (L=8 full trajectory −1.47e-13; L=10/L=12 cache-saturation 0.0 EXACT). Composite **INFO** (sign=FAIL, magnitude=FAIL, regime=VALID); FWD-C1 slot reserved **REGISTRY-INCOMPLETE-PENDING-OPERATIONAL-ALIGNMENT**. **Classification: PHONONIC** (FWD-C1 cross-pillar bridge; Element-3 bridge map = adiabatic-limit η-form, scheme suffix `-Bismut-Cheeger`).

This is the route neither prior workshop covered, and it is the one this synthesis uniquely integrates. The plan hypothesized the η-form would quantitatively MATCH the integrated pair-production (`n_pairs = 59.8`, S38 — note: impulsive-treatment value, no PROVENANCE entry beyond S38). It does not, and the *reason* is the fidelity-critical finding: the families-index of a self-adjoint BDI operator with a ±-symmetric spectrum and a gap that never closes (`sf = 0`, J-protected, S61) splits as `Index = ∫Â (integer) + η-form (non-integer)` with the η-form **identically zero** — a Level-1 cohomology identity, L-independent. The signed spectral-asymmetry transgression is structurally 0 because the BDI ± symmetry cancels it pointwise at every τ.

The consequence for A_s is decisive and orthogonal to Routes 1 and 3: **the η-form carries NO A_s-normalization handle.** A signed-asymmetry families object cannot source a positive-definite amplitude. The pair-production physics that DOES source A_s lives on the *unsigned* mode-mixing of the **non-self-adjoint** Dirac-Schrödinger families object `D + V(τ)` (van den Dungen Paper 09, `ind(D+V) = ⟨[V],[D]⟩`) — `Σ mult·|β_k|² = N_pair_eff = 5.489` from W3-1 — NOT the self-adjoint D_K η-form. This is the topological-axis confirmation of the same floor: the amplitude-bearing content is the unsigned (positive) mode-mixing `|β_k|²`, exactly the `n_k ≥ 0` that forces `S_IC ≥ 1` on the reference-state axis. The signed object that COULD have carried a sign-indefinite (wall-lifting) contribution vanishes by symmetry. Route 2 thus independently closes the same escape hatch Route 1 closed by uniqueness: there is no signed channel to lower the floor.

### II.4 Route 3 — Bogoliubov-relic / dynamical axis (W3): floor real, relic survives, filter fitted

**Result (relic locked, W3-1)**: per-mode `{β_k}` integrator-locked (integrator_agreement 7.76e-5, unitarity residual 4.55e-15); summed `ρ_relic`/`N_pair_eff` carry a truncation band (p+q≤7→≤8). Composite **INFO**. **Classification: PHONONIC.**

**Result (Floquet, W3-2)**: `fraction_resonance = 0.0` (0 of 1248 relic modes in resonance bands; max |Tr M| = 1.99999996 < 2; max Re μ = 0). Composite **PASS**. The relic, once frozen by the diabatic transit, is NOT re-pumped by the post-fold modulus ringing — the Ordered Veil survives its own in-band frequency coincidence (the drive amplitude `h_par = 8.3e-4` is ~3 OOM too weak to open a tongue wider than any relic mode's detuning). This certifies that the A_s overproduction is a *genuine surviving amplitude*, not a post-transit re-pumping artifact.

**Result (back-reaction, W3-3)**: `q_eff` direction PASS (a diluting positive-energy relic decelerates, Sage-exact), canonical-dust (w=0) trajectory contained in the lower SCALE-FACTOR-54 band; composite **INFO** (band reproduced as a RANGE, not the monotone-rising deceleration history; the relic-Friedmann q and the s54 Connes-distance-proxy q are DIFFERENT observables). The effective-Friedmann closure is partial; A_s overproduction is real within it.

**Result (greybody, W3-4)**: first-principles BdG greybody `∫Γ_derived = 0.036265` vs fitted `0.511872` (agreement 0.929 ≫ 0.10 tol; band_collapse_ratio 0.247 > 0.10). Composite **FAIL** — honest and informative. The substrate-derived barrier `V_eff = V_0 sech²(κ_eff x_*)` with `κ_eff = κ_exit = 47.6146` has half-transmission `ω_½ = √V_0 = 23.81 M_KK`, sitting **6.40× above** the relic band upper edge (3.72 M_KK) — it reflects ~96% of the band. The fitted 0.512 was placed at the band MIDPOINT by construction (A2 tuning knob exposed). No static substrate scale (`Δ_BCS = 0.464`, `κ_exit = 47.6`, `T_acoustic = 0.112`) lands `ω_½` inside [0.94, 3.72].

**Result (CF21 H̃, W3-5)**: H̃ reconciled to ONE canonical reading (Branch-A TD Mukhanov-Sasaki); composite **PASS** but `structural=False` (a figure-space identification, not a derivation lowering H̃ into its window). The produced-side magnitude 1.57× traces precisely to the H̃ leg sitting factor 1.25 above its own substrate-baseline window, squared via CC3 (`d ln A_s/d ln H̃ = +2`).

Route 3's verdict: floor confirmed on the produced side (upstream of any horizon transmission, so the W3-4 FAIL does not touch it); relic survives (W3-2); the open physics is the *magnitude* (occupation-/regulator-soft, W3-1 band + W3-5 H̃ excess) and the *upper-edge filter* (underived, W3-4 FAIL).

---

## III. Gate Verdicts (integrated across the three routes)

| Route | Gate | Verdict | Decisive Number | Bearing on A_s floor |
|:------|:-----|:--------|:----------------|:---------------------|
| 1 (reference-state) | INV12-W1-2-A-S-GGE-MODULAR-REFERENCE | FAIL | `R_wall^{GGE} = 2.4182 ≡ R_wall^{BD}`; `K_sub ≥ 1` | floor reference-state-INDEPENDENT |
| 1 (reference-state) | INV12-W4-1 workshop verdict | (review, no line) | phase channel theorem-forced `A_s^{ω-full} ≥ A_s^{BD}` | residual closed structurally |
| 2 (families-index) | INV12-W2-5-FWD-C1-BISMUT-CHEEGER-ETA | INFO | η-form = 0 (L8 −1.5e-13; L10/L12 0 EXACT) | signed channel carries 0 normalization → no lift |
| 3 (dynamical) | INV12-W3-1-RELIC-SPECTRUM-ODE-LOCK | INFO | unitarity 4.55e-15; `N_pair_eff = 5.489` (band) | floor source locked; magnitude banded |
| 3 (dynamical) | INV12-W3-2-FLOQUET-ORDERED-VEIL-RESONANCE | PASS | `fraction_resonance = 0.0`; max\|Tr M\| = 1.99999996 | relic survives → amplitude genuine |
| 3 (dynamical) | INV12-W3-3-BACK-REACTION-CLOSURE-HSQ | INFO | `q_eff` sign PASS; dust trajectory lower-band | A_s real in partial closure |
| 3 (dynamical) | INV12-W3-4-GREYBODY-FROM-BDG | FAIL | `∫Γ_derived = 0.036` vs fitted `0.512` | upper-edge filter underived (relocated, open) |
| 3 (dynamical) | INV12-W3-5 CF21 H̃ reconcile | PASS (structural=False) | 1.57× = H̃-window excess² (CC3) | magnitude traces to H̃ leg |

Supporting upstream: INV12-W1-3 (n_s functional COHERENCE PASS — n_s single-valued, so the A_s discussion carries no n_s-band caveat); INV12-W2-1/2/3/4 (the topology/analysis boundary: spectral-action moments are the soft analysis side; K-homology dressing-rigid).

---

## IV. Structural Implications — dissolve / relocate / confirm

**The characterization question (do the routes JOINTLY dissolve, relocate, or confirm the wall?) resolves to: CONFIRM the floor + RELOCATE the open physics. Not dissolve.**

### IV.1 The floor is CONFIRMED — three orthogonal axes, no lift on any

The wall is not dissolved on any axis. Quantitatively, the closest any route comes to "lowering A_s" is Route 1's `Δ = +1.04e-13 > 0` (the GGE reference *raised* A_s, by 0.002%). The three axes are pairwise non-overlapping in machinery:

- **Reference-state axis** (algebra-DEPENDENT state-pair functional): the modular weight ω is a free handle a priori; second-moment uniqueness removes it. Confirms via operator-algebra uniqueness.
- **Families-index axis** (algebra-INVARIANT spectral-asymmetry functional): the η-form is the signed transgression; BDI ± symmetry zeroes it. Confirms via topological vanishing — the *signed* channel that could carry a sign-indefinite lift does not exist.
- **Dynamical axis** (Bogoliubov ODE + Floquet monodromy): the produced occupation `n_k ≥ 0` is the ODE output; Floquet shows it survives the post-fold ringing. Confirms via the produced-side positivity directly.

These three are STRUCTURALLY ORTHOGONAL in the sense of `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` (algebra-INVARIANT vs algebra-DEPENDENT) and the families-index axis adds a third, topological, leg. Their joint confirmation is the strongest structural-confidence signal available: the wall survives every machinery that could in principle have evaded it. **The floor `A_s ≥ A_s^{BD}` is FUNCTIONAL-INDEPENDENT in sign over all Gaussian states, all faithful normal modular weights, AND the families-index η-form.**

### IV.2 The open physics is RELOCATED — two named, distinct, scheme-dependent legs

No route confirms the *magnitude* (3.02× / 2.42× / 1.57× / up to 7.7×) or the *upper-edge filter* as permanent. Both are relocated off the floor onto specific, reconcilable legs:

- **Leg A — the magnitude (occupation-/regulator-soft).** `K_sub − 1` ranges ~2000× across occupation inputs (locked-relic `n̄_mw = 2.74e-4` vs S43-band `n ~ 0.5`); the W3-1 truncation band (p+q≤7→≤8, rel 0.38–0.43) carries the relic content; the W3-5 H̃ leg sits factor 1.25 above its substrate-baseline window, and 1.25² = 1.57 IS the locked produced-side multiple via CC3. This leg is RELOCATED to the H̃-branch / occupation-input question — falsifier-rigor-registry Row 8 correctly tags A_s SCHEME-DEPENDENT (5.078e-9 TD-canonical vs 2.099e-9 Planck, 0.384 OOM) for exactly this reason. It is NOT permanently walled; it is regulator-soft and partially-reconciled (W3-5 picked the canonical branch).

- **Leg B — the upper-edge greybody filter (underived).** W3-4 FAIL exposes the fitted 0.512 as a tuning knob with no substrate-derived barrier scale: the static surface-gravity barrier reflects ~96% of the band. This leg is RELOCATED to the single decisive forward compute (W3-4 carry-forward): scan for a *dynamical* near-horizon resonance set by the finite quench rate `τ̇(τ)` — the one un-scanned candidate. It is NOT permanently walled; it is underived-and-open with positive EVOI.

Route 2 confirms the relocation is correct: the η-form route's honest A_s-route status is that it is **structurally CLOSED for A_s normalization** (η-form ≡ 0), and the live handle migrates to the non-self-adjoint `D + V(τ)` mode-mixing — the same object Routes 1 and 3 identify as the amplitude source. All three routes agree on WHERE the open physics lives (the produced-side `|β_k|²` magnitude and the exit filter), and all three agree it is NOT on the floor.

### IV.3 The floor-vs-edge distinction is the framework's honest A_s status

Integrating the three routes: **A_s is bounded BELOW by a permanent FUNCTIONAL-INDEPENDENT positivity wall (substrate-IS, reference-independent, families-index-confirmed) and bounded ABOVE by a fitted filter whose first-principles value (∫Γ = 0.036) does not reproduce the fit (0.512).** "Bounded, not predicted" — bounded below by a permanent wall, bounded above by a knob that is currently fitted and may or may not be derivable. The lizzi-side "A_s is a BD-artifact dissolvable by the substrate's own modular state" is FALSE on all three axes. The transit-side "A_s bounded to ~1.5–3× by a ledger whose H̃ leg sits outside its own PASS window, with the upper edge fitted" is the HONEST joint status.

---

## V. CF23-Tag Recommendation (ADVISORY for session-promotion)

**Recommendation: CONFIRM with mandatory SCOPE SHARPENING. Not dissolved; not relocated wholesale; the FLOOR is confirmed permanent and the MAGNITUDE/FILTER are relocated to open scheme-dependent legs.**

The present CF23 prose (atlas-08-open-questions.md, S97 freshness bullet) reads: *"the A_s amplitude floor (3.02× Planck) is now a PERMANENT structural-position wall, not remediable at the substrate-IC layer."* This is CORRECT in its load-bearing claim (the floor is permanent) and is now CONFIRMED from two vantages S83 did not have (the modular-weight uniqueness, W1-2 + W4-1; and the families-index η-form vanishing, W2-5). But the prose conflates two epistemically distinct objects under one "3.02× wall" phrase:

- **The FLOOR (sign):** `A_s ≥ A_s^{BD}`. PERMANENT, FUNCTIONAL-INDEPENDENT, confirmed on three orthogonal axes. CF23's "permanent structural-position wall, not remediable at the substrate-IC layer" is exactly right FOR THIS OBJECT. **Confirm.**
- **The MAGNITUDE (3.02× / 2.42× / 1.57×) and the upper-edge FILTER (0.512):** SCHEME-DEPENDENT, occupation-/regulator-soft, and underived. These are NOT permanently walled — they are RELOCATED to open legs (the H̃-branch/occupation question, falsifier-rigor Row 8; and the dynamical greybody scan, W3-4 CF). Attaching "3.02× Planck" to the word "permanent" over-states: the *number* 3.02 floats with the occupation input and the regulator; only the inequality `> 1` is permanent.

**Advisory routing (for a future session-promotion to execute; this synthesis does NOT edit the register):**

1. **atlas-08 CF23 prose** — split the single bullet into (a) FLOOR (`A_s ≥ A_s^{BD}` / `S_IC ≥ 1`): PERMANENT structural-position wall, now CONFIRMED from the modular-weight (W1-2/W4-1) and families-index (W2-5) vantages in addition to the substrate-IC layer (S83); and (b) MAGNITUDE + upper-edge FILTER: SCHEME-DEPENDENT and OPEN — relocated to the W3-4 greybody-scale forward compute and the H̃/occupation-input question. Per `capstone-hygiene-gate.md` this is a Q3 status change (a PROVEN/CONDITIONAL distinction sharpening), routed to the designated register writer, NOT a bulk append.

2. **falsifier-rigor-registry A_s Row 8** — the SCHEME-DEPENDENT tag stays correct for the magnitude; add a CONFIRMATION sub-annotation that the *floor* (sign) is FUNCTIONAL-INDEPENDENT/PERMANENT on three orthogonal axes (the row currently characterizes only the scheme-dependent magnitude). Sole writer is `mack-cosmic-bridge` per `feedback_mack-bridge-role.md`.

3. **Substrate-first framing preserved** (per `capstone-hygiene-gate.md §"Substrate-first framing preservation"`): the scope-sharpening does NOT invert any explanation direction. The arrow `D_K eigenvalues → {α_k, β_k} → n_k = |β_k|² → S_IC = 1+2n_k → A_s` is unchanged; the register tag merely scopes the confidence (floor permanent, magnitude/filter open) without demoting the substrate-IS frame.

**One-line CF23 verdict: CONFIRMED (floor) + SCOPE-SHARPENED (split the permanent floor from the open scheme-dependent magnitude/filter). The wall stands; the "3.02×" number does not deserve the "permanent" qualifier — only `A_s ≥ A_s^{BD}` does.**

---

## VI. Carry-Forward Computations

These are ADVISORY for a session-promotion of investigation-12. The one decisive forward compute (already in the W3 working paper) plus the two register-reconciliation actions:

```
VI.1. A_s upper-edge greybody — dynamical near-horizon resonance scan (THE decisive compute)
   - What: Scan the BdG fluctuation potential at the τ≈0.16 exit horizon for any substrate-derived
     barrier (static OR dynamical-resonance) whose half-transmission ω_½ = √V_0^{sub} lands inside
     the relic band [0.94, 3.72] M_KK and reproduces ∫Γ = 0.512 ± 10% — OR prove no such scale exists.
     Critical un-scanned candidate: a dynamical near-horizon resonance set by the finite quench rate
     τ̇(τ) (finite-rate Bogoliubov / Floquet-WKB correction to the sudden-limit κ_exit), NOT the
     static surface-gravity barrier W3-4 ruled out.
   - Inputs: W3-1 locked {α_k, β_k} + pair_band [0.94, 3.72] (§W3-1); W3-4 V_eff scanner +
     Pöschl-Teller machinery (§W3-4); τ̇(τ) near-exit trajectory (S95-W4-2-HAWKING-ANALOG-T-LEDGER);
     canonical kappa_exit=47.6146, Delta_BCS=0.4642547, T_acoustic=0.112, T_compound=7.578;
     fitted comparator ∫Γ_fitted=0.512.
   - Gate: NEW gate (transit-dynamics). PASS (A_s bounded-and-derived) iff ∃ substrate V_0^{sub} with
     √V_0^{sub} ∈ [0.94, 3.72] AND ∫Γ = 0.512 ± 10%. FAIL (A_s bounded-but-filter-fitted, permanent
     upper-edge knob) iff every substrate scale gives ω_½ outside the band. INFO iff a resonance lands
     in-band but ∫Γ misses 0.512 by >10%. Pre-register tol=10% RATIO + finite-rate WKB regime check
     (regime_verdict per the auto-shortening clause).
   - Effort: ~1 parameter scan + 1 finite-rate transmission computation; ~1 agent-session
     (transit-dynamics-theorist). Single decisive gate, no multi-wave dependency.

VI.2. CF23 prose split (register reconciliation — Q3 capstone-hygiene)
   - What: Split the atlas-08 CF23 bullet into FLOOR (permanent, 3-axis confirmed) vs
     MAGNITUDE+FILTER (scheme-dependent, open). Reconcile the prose tag against the three-route
     integrated reading of this synthesis.
   - Inputs: this synthesis §V; atlas-08-open-questions.md CF23; atlas-04 assumptions; the three
     route verdicts (W1-2, W2-5, W3-4).
   - Gate: capstone-hygiene Q3 status-change reconciliation (designated register writer; reviewed
     patch, NOT bulk append). Closure by artifact-existence (no numerical verdict).
   - Effort: orchestrator-direct register edit at session-promotion; <1 agent-session.

VI.3. falsifier-rigor A_s Row 8 floor-confirmation sub-annotation (register reconciliation)
   - What: Add to Row 8 a CONFIRMATION sub-annotation that the A_s FLOOR (sign) is
     FUNCTIONAL-INDEPENDENT/PERMANENT on three orthogonal axes (reference-state W1-2, families-index
     W2-5, dynamical W3); keep the SCHEME-DEPENDENT tag for the magnitude.
   - Inputs: this synthesis §II–§IV; falsifier-rigor-registry.md A_s Row 8; the three route verdicts.
   - Gate: mack-cosmic-bridge sole-writer append (per feedback_mack-bridge-role.md). Closure by
     artifact-existence.
   - Effort: <1 agent-session at session-promotion.
```

---

## VII. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Floor `A_s ≥ A_s^{BD}`, `S_IC = 1+2n_k ≥ 1` | PHONONIC | CONFIRMED (3 orthogonal axes) | wall is substrate-IS, reference-independent, permanent in sign |
| 2 | Route 1 reference-state: `R_wall^{GGE} ≡ R_wall^{BD}`, `K_sub ≥ 1` | PHONONIC | FAIL (no lift) | modular weight cannot lower A_s (second-moment uniqueness) |
| 3 | Route 2 families-index: η-form ≡ 0 | PHONONIC | INFO (signed channel = 0) | no signed channel to lift; amplitude source is unsigned `\|β_k\|²` |
| 4 | Route 3 relic + Floquet: `N_pair_eff` locked, `fraction_resonance = 0` | PHONONIC | INFO + PASS | relic survives → A_s overproduction genuine, not re-pumping |
| 5 | Magnitude (3.02× / 2.42× / 1.57×) | PHONONIC | SCHEME-DEPENDENT (RELOCATED) | occupation-/regulator-soft + H̃-window excess (W3-5, CC3) |
| 6 | Upper-edge greybody filter (∫Γ 0.036 vs 0.512) | PHONONIC | FAIL → OPEN (RELOCATED) | fitted knob; decisive forward compute = dynamical-resonance scan |
| 7 | CF23 tag | framework-register | CONFIRM + SCOPE-SHARPEN (advisory) | floor permanent; "3.02× permanent" over-states — only `>1` is permanent |
