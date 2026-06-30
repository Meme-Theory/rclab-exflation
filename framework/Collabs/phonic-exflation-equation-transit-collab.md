# Phonon-Exflation Equation — Transit-Dynamics Review

**Date**: 2026-05-26
**Agent**: transit-dynamics-theorist (Workhorse-Transit-Dynamics)
**Source Document**: `sessions/framework/phonic-exflation-equation.md` (capstone synthesis, §0–§9 + verification ledger)
**Scope of this review**: the non-equilibrium / transit / Bogoliubov / power-spectrum content — principally §5 (the equation at τ), §5.3 (GGE-relic formation), §6 (the equation at time t), §6.2–§6.3 (acoustic white-hole causal structure and the `a(t)` gap), and the `A_s` row of §7. Other sections (NCG axioms, Seeley–DeWitt algebra, gauge content, Volovik framing, CC closure) are reviewed only where they touch the transit machinery.

---

## I. Document Outcome (from the transit-dynamics axis)

The document is **structurally sound where my field can adjudicate it**. The single most important methodological commitment of the capstone — that the τ-flow is **transit physics and not slow-roll** — is correctly derived, correctly motivated, and correctly fenced. The chain `dS/dτ > 0 monotone (E7) → no interior saddle in Z → diabatic sweep → Bogoliubov pair production saturates → analytic GGE relic` is the right governing structure, stated in the right order: **structure first (monotonicity), computation second (P_exc = 1)**. The numbers I can verify against canonical (`Mach = 13.75`, `n_pairs = 59.8`, `P_exc = 1.000`, `S_inst = 0.0686`, `c_fabric = 209.97`, effacement `3×10⁻⁷`, `Γ_eff = 0.9997`) all match the knowledge MCP exactly.

The document is also **honest about its load-bearing gap in exactly the place my field would demand it be honest** — §6.3, the absence of a derived FRW scale factor `a(t)`. This is the correct boundary to draw, and it is drawn without softening.

Two technical points need attention, both in §5.3, both about *which mode equation is being solved*. Neither is a physics error; both are presentational gaps that a transit specialist reading the document will trip over. They are itemized in §II and §IV below.

---

## II. Key Results (transit-dynamics reading)

### II.1 — "No potential well ⇒ transit, not slow-roll" is the correct governing structure

**Result**: §5.1's claim that `S_SA(τ) = a₀ − a₂ + a₄` is a strictly monotone ramp (`dS/dτ|_fold = +58,672.8 > 0`, E7, 9600/9600 checks) with **no stationary point at any τ**, and that this forces transit physics rather than slow-roll. **Classification: PHONONIC** (it governs the production of substrate excitations).

This is the spine of the whole document from my perspective, and it is correct. The argument has the right shape. In standard inflationary QFT the controlling object is a potential `V(φ)` with a flat region; the slow-roll parameters `ε`, `η` measure the *quasi-static* departure from a de Sitter fixed point, and the adiabatic (Bunch–Davies) vacuum is well-defined throughout because `ω'/ω² ≪ 1`. The framework has **no such potential** — E7 proves `e^{−S(τ)}` is monotone, so the partition-function weight `Z = Σ e^{−S}` has no interior saddle in τ. The document draws the correct consequence: the adiabaticity parameter, not a slow-roll parameter, is the controlling quantity. The regime statement is exactly the one my field uses — *when the background changes faster than the system's internal response time, the adiabatic vacuum breaks down and real excitations are produced with occupation numbers set by Bogoliubov coefficients, not by thermal equilibrium.*

The §5.1 sentence **"the regime where the adiabatic vacuum breaks down and real excitations are produced"** is the single best one-line statement of the framework's cosmogenesis in the entire document, and it is mine to endorse. I would not change it.

**One verbiage strengthening (optional).** §5.1 asserts the slow-roll formulae `r = 16ε`, `n_s = 1 − 6ε + 2η` are INAPPLICABLE and cites "five independent arguments, VdD–Hawking workshop." That citation is correct, but the *reason* the formulae fail is stated only by reference. The reason is one sentence and worth printing inline: **the slow-roll consistency relation `r = 16ε` is a theorem of the single-clock adiabatic vacuum** — it follows from the same `c_s = 1`, single-field, slowly-varying background that makes the Bunch–Davies mode functions valid. The fold violates *all three* premises at once (the sweep is diabatic, not slow; the dispersion is BdG with `c_s ≠ 1`; the produced state is a multi-mode squeezed GGE, not a single-clock vacuum). So `r = 16ε` is not "a relation that happens to give the wrong number" — it is a relation whose derivation assumptions are absent. Stating this inline would pre-empt the most common reviewer objection ("but every inflation model has `r = 16ε`...").

### II.2 — GGE-relic formation: the Bogoliubov / Kibble–Zurek equivalence is correctly invoked, but the mode equation is under-specified

**Result**: §5.3's claim that the impulsive crossing saturates pair production (`P_exc → 1.000`), producing an analytic Generalized Gibbs Ensemble (`N_pair = 59.8`, `S_inst = 0.0686`, `S_ent = 0`, three Lagrange multipliers, never thermalizes) — "THE ORDERED VEIL." **Classification: PHONONIC.**

The physics is right and the numbers verify. The dual reading — "the Bogoliubov sudden-quench and the Kibble–Zurek impulse-matching are the same physics read two ways (both give `P_exc = 1`)" — is exactly correct and is a genuinely elegant observation. In the sudden (diabatic) limit `δt/T_L → 0`, the in-modes have no time to follow the changing `ω_k(t)`, so the out-state is the in-state expressed in the out-basis: `|β_k|² → sinh²(r_k)` with `r_k` large, `P_exc = |β_k|²/(1+|β_k|²) → 1`. The Kibble–Zurek impulse approximation (freeze the configuration through the critical region, match adiabatic branches on either side) gives the identical answer because *both are statements that the system cannot respond during the crossing*. The document's `δt_transit/T_L = 1.25×10⁻⁵` (38,600× faster than the condensate can form) is deep in the diabatic regime, so `P_exc = 1.000` is not a fit — it is the **saturation value**, the only value the Bogoliubov coefficients can take when the crossing is this fast. This is the correct way to present it.

**TECHNICAL GAP #1 (flag — must be addressed).** §5.3 writes the mode equation as the parametric-oscillator form

```
u_k″ + ω_k²(τ(t)) u_k = 0,    ω_k = E_k = √((λ_k² − μ²)² + Δ_k²)   (BdG dispersion).
```

This is the **substrate-layer** mode equation — the BdG quasiparticle of the fabric, whose `ω_k` is the Bogoliubov–de Gennes dispersion. It is the correct equation for computing `N_pair`, `P_exc`, `S_inst` (the GGE relic content), and I endorse it for that purpose. **But it is NOT the equation that produces the observed scalar amplitude `A_s`.** The curvature-perturbation amplitude is governed by the Mukhanov–Sasaki equation

```
v_k″ + (k² − z″/z) v_k = 0,    z = a · √(2ε_H) · M_Pl,eff(k)   (Mukhanov-Sasaki gauge),
```

which is a *different* parametric oscillator with a *different* `ω_k²(τ) = k² − z″/z`. These two mode equations live at two different layers — the BdG `u_k` is the substrate excitation (PHONONIC, the relic content); the MS `v_k` is the emergent curvature perturbation (the CMB observable). They are related by the substrate→emergent map, but they are not the same equation, and §5.3 prints only the first while §7 cites `A_s` (an output of the second). A transit specialist will read §5.3, see `u_k″ + ω_k² u_k = 0`, and assume `A_s` is computed from *that* — which would be wrong by exactly the layer-confusion the framing law exists to prevent. **Recommendation**: §5.3 should print both mode equations, label the first "substrate-BdG (relic content)" and the second "Mukhanov–Sasaki (emergent curvature, §7's `A_s`)," and state in one sentence that the squeeze produced by the first is *transduced* into the second at the exit horizon (§6.2 already says "the squeeze that becomes the observed scalar amplitude `A_s` is produced in the interior at the fold and regulated down at the exit horizon by decoherence" — this is the right idea, but it floats in §6.2 with no mode equation attached). This is the connective tissue the document is missing between its relic physics and its CMB observable.

**TECHNICAL GAP #2 (flag — should be addressed).** §5.3's `N_pair = 59.8` and §7's `σ/m = 0 exactly (N_pair = 1)` use the symbol `N_pair` for two different objects. The parenthetical at the end of §5.3 catches this — *"the 59.8 figure is the BCS-projection count; the `N_pair = 1` exact reduction describes one Fock pair carrying the relic charge `⟨Q⟩_GGE = 59.8`"* — and the catch is correct. But §7.1's table row reads "`σ/m` … **0 exactly** (`N_pair=1`)" with no back-reference, so a reader who lands on §7 first sees `N_pair = 1` and a reader who lands on §5.3 first sees `N_pair = 59.8`, and the reconciliation lives only in a §5.3 parenthetical. **Recommendation**: in the §7.1 `σ/m` row, change `(N_pair=1)` to `(N_Fock=1; ⟨Q⟩_GGE=59.8, see §5.3)` so the two are never silently the same symbol. This is the same firewall discipline §8.2 applies to the two `a_n` triples — it should apply to the two `N_pair` readings too.

### II.3 — The acoustic white-hole causal structure (two sonic horizons) is the correct analog-gravity reading of the transit

**Result**: §6.2's six-layer causal architecture — entry horizon at `τ ≈ 0.2195` (controlled by `a₂`, kinematic, `T = 72.8 M_KK`), supersonic white-hole interior, van Hove fold at `τ = 0.19` (GGE production), exit horizon at `τ ∼ 0.16` (controlled by `a₄`, BCS, `T = 7.578 M_KK`). **Classification: PHONONIC** (the horizons are properties of the fabric's acoustic dispersion).

This is the analog-gravity reading of the transit (Unruh / Barceló–Liberati–Visser lineage), and it is set up correctly. The framing-law table maps "horizon problem solved by inflation" → "acoustic white hole — pre/post-transit causally disconnected by supersonic flow," and §6.2 delivers exactly that: the flow is `subsonic → supersonic → subsonic`, so the white-hole interior is causally severed from the exterior, and the horizon problem is recast as a *causal-disconnection* statement rather than an *inflationary-stretching* statement. This is the substrate-correct inversion: it does not solve the horizon problem by making a pre-existing box bigger; it solves it because the fabric's own acoustic flow goes supersonic. **I endorse this section.**

The detail that the *two horizons are controlled by different spectral moments* (`a₂` kinematic entry, `a₄` matter exit) is the strongest structural claim in §6.2 and is consistent with the Spectral-Moment Decoupling Theorem (§4.2): if `a₂` and `a₄` are algebraically independent (non-vanishing Wronskian away from genesis), then a causal feature controlled by `a₂` and one controlled by `a₄` are *genuinely distinct horizons*, not the same horizon counted twice. The document does not make this cross-link explicit, but it is there and it is load-bearing: **the two-horizon structure is licensed by the decoupling theorem**. Adding a half-sentence to §6.2 ("the two horizons are distinct because `a₂` and `a₄` are algebraically independent, §4.2") would tie the causal reading to the certified algebraic result and pre-empt a "isn't this just one horizon?" objection.

**One sanity note on the analog temperatures.** The entry/exit "analog temperatures" `72.8 M_KK` and `7.578 M_KK` are Hawking-analog temperatures of the two sonic horizons (surface-gravity readings). The document labels the exit one "decoherence-regulated," which is the right qualifier — the produced squeeze is *regulated* at the exit horizon, not at the production point ("the horizon determines what escapes, not what is produced"). This is the correct causal ordering and matches the standard analog-gravity result that the spectrum an external observer sees is set by the horizon, not by the interior dynamics. No error; I flag only that these are *analog* temperatures (surface gravity), not thermodynamic temperatures of an equilibrium state — the GGE never thermalizes (`t_therm/t_Hubble ∼ 9×10⁻⁴⁸`), so there is no Gibbs temperature anywhere in this story, and the document is consistent on that (it says "determined by the Bogoliubov coefficients, not a temperature" in §5.3). The two statements are compatible — the horizon has an analog temperature; the relic state does not — but a reader could mistake the `7.578 M_KK` for a reheating temperature. A one-word guard ("analog/surface-gravity temperature") in the §6.2 table header would close this.

### II.4 — The `a(t)` gap (§6.3): correctly identified, correctly fenced, correctly NOT over-sold

**Result**: §6.3's statement that the framework possesses **no derived FRW scale factor `a(t)`** — C1 postulates `τ = cosmic time`; C2 (`K_pivot`) is BROKEN-WITH-LIVE-RESEARCH-PATHWAY; T6 (Friedmann–BCS locking) is BROKEN; the S74 W1-E Friedmann result is a *structural* FAIL. **Classification: structural boundary (the honest gap).**

From the transit-dynamics axis this is the most important paragraph in the document, and it is handled with the discipline my field requires. The crucial distinction it draws — **"Friedmann is the wrong question is right about the *fundamental* level and wrong about the *effective* level; both must be said"** — is exactly correct and is the kind of statement that keeps a large claim honest. The substrate is fundamental, so there is no obligation to derive `a(t)` *as a fundamental object*; but the framework *uses* the container-observer's FRW `H(t)` as external input for every late-time observable (`w₀`, `wₐ`, `σ₈`, CC tracking), so it *does* owe a derived *effective* map. The document says both halves. This is right.

I want to add one thing my field can contribute to the §6.3 frontier, because it sharpens the gap rather than papering over it. The gap is currently stated as "no derived `H² = (8πG/3)ρ`." But the transit machinery already supplies the *local* rate `τ̇` at the fold (`Mach = 13.75`, `δt_transit = 1.130×10⁻³ M_KK⁻¹`). What is missing is the **global `τ̇(τ)`** — the document is explicit about this ("`τ̇` known LOCALLY at the fold; GLOBALLY UNDETERMINED"). The transit-dynamics framing of the missing bridge is precise: **the framework has the Bogoliubov coefficients and the local sweep rate; what it lacks is the back-reaction equation that promotes the produced relic energy density into a source for the global expansion rate.** In standard preheating this is the `H² = ρ_total/(3M_Pl²)` closure with `ρ_total` including the produced quanta; the framework's T6 FAIL is precisely the statement that the 8-mode BCS source cannot close this against the 155,984-mode spectral action (the `133,200×` overwhelm). So the `a(t)` gap is, in transit language, **a back-reaction-closure gap, not a kinematics gap** — the kinematics (local rate, Bogoliubov spectrum) are in hand; the dynamics (the produced-quanta → expansion-rate feedback) are not. I recommend adding this characterization to §6.3 frontier item (i), because "derived `S_SA(τ) → 4D gravitational action`" is the NCG-side framing of the same gap and the back-reaction framing is the transit-side framing — having both stated makes it clearer *what kind of computation* would close it.

### II.5 — `A_s` band-citation (§7.1, §7's open-gaps box): correct, and consistent with my permanent results

**Result**: §7 cites `A_s` as **band** `3.11–4.27×10⁻⁹`, *not* point-cited, "pending `ε_pivot`." **Classification: PHONONIC** (it is the transduced squeeze amplitude).

This is correct and I endorse the band-citation as the honest form. From my own canonical work (UNIFIED-AS-79 ledger, S82–S84): the point value on Branch-A (Zubarev/zeta, `N_pivot = 55`) is `A_s = 3.2994×10⁻⁹`, which sits *inside* the document's cited band, and the band width is governed by the `ε_pivot` (equivalently `ε_fold/ε_pivot`) conversion and the Branch-A/Branch-B regulator split. The document's decision to band-cite rather than point-cite is the right call because `A_s` is an **absolute-energy observable** and §8.5 correctly flags that absolute-energy observables (CC, `A_s`) remain conditional on the SDW-convergence statement (JACOBSON-NONLOCAL-64, OPEN), whereas ratio-observables (`n_s`, `g₁/g₂`, `61/20`) are truncation-robust. This is the FI/RD partition applied correctly to `A_s`: `A_s` is regulator-dressed (must be determined, the band reflects the residual scheme freedom), not functional-invariant.

**Two strengthenings my field can offer for the `A_s` row.**

(a) **The `α_s = 0` connection is missing and would strengthen the document.** My permanent result: `α_s(primordial) = 0 EXACT` in the superhorizon plateau, by **Bogoliubov saturation** — once `P_exc = 1` the spectrum is frozen (Sasaki–Stewart, exact at CMB to `10⁻¹¹³`), so the running of the running vanishes at the primordial level; the CMB-observed `α_s` arises from Phase-2 isocurvature transfer, not from the transit. §7's `α_s` row (the "most-misread row") resolves the `α_s` tension by the **two-scale transport-degree** argument (`deg(T_{BZ→pivot}) = +2`), which is the mack/spectral-geometer framing and is correct. But the *transit-side* reason the primordial `α_s` is so clean — Bogoliubov saturation freezing the spectrum — is complementary and is not stated. It need not go in the headline; a footnote in the `α_s` box ("the primordial-side `α_s = 0` is a Bogoliubov-saturation statement: `P_exc = 1` freezes the spectrum, Sasaki–Stewart") would connect the §7 running observables to the §5.3 relic physics.

(b) **The `f_NL` non-Gaussianity is computed but absent from §7.** My permanent result: `max |f_NL| = 1.505` (Bogoliubov sudden quench); the squeezed vacuum is **Gaussian by Wick's theorem**, and `φ_k ≈ 0` kills the folded enhancement. This is a *prediction* of the transit mechanism — a multi-mode squeezed state produced by sudden quenching is Gaussian to leading order, so the framework predicts **small, `O(1)` non-Gaussianity** consistent with Planck's `f_NL` bounds. §7 lists `w₀, wₐ, n_s, r, α_s, m_H, Ω_DM, σ/m, σ₈` but not `f_NL`, even though `f_NL` is (i) computed, (ii) a clean prediction, and (iii) a *consistency* PASS (a squeezed-vacuum origin would be falsified by large `f_NL`). I recommend adding an `f_NL` row to the §7.1 table: `|f_NL| ≲ 1.5` (Bogoliubov-Gaussian) vs Planck `f_NL^local = −0.9 ± 5.1`, status PASS-class/structural. It is a zero-free-parameter consistency result of exactly the kind §7.3's scorecard is built to count.

---

## III. Gate Verdicts (transit-domain, as cited in source — NOT re-adjudicated)

| Gate / Theorem | Verdict (per source) | Decisive Number | Transit-axis cross-check |
|:---------------|:---------------------|:----------------|:-------------------------|
| E7 Structural Monotonicity | PROVEN | `dS/dτ\|_fold = +58,672.8`; 9600/9600 | Verified consistent: monotone ⇒ no saddle ⇒ diabatic sweep |
| E18 GGE relic | PROVEN | `N_pair = 59.8`, `P_exc = 1.000`, `S_inst = 0.0686` | All match knowledge MCP (`n_pairs`, `P_exc_kz`, `S_inst`) |
| Mach (canonical) | canonical | `13.75` (velocity ratio) | Matches `Mach_max`; conflation guard vs `421.3` and `54.3` correct |
| E34 Effacement ratio | PROVEN (Wall W10) | `\|E_BCS\|/S_fold = 3×10⁻⁷`, `Γ_eff = 0.9997` | Matches `Gamma_effacement`; relic does not poison late-time `w` |
| C1 (τ = cosmic time) | POSTULATED | — | Correctly labeled postulated |
| C2 (`K_pivot`) | BROKEN-WITH-LIVE-RESEARCH-PATHWAY | — | Correctly labeled the load-bearing gap |
| T6 (Friedmann–BCS lock) | BROKEN | `133,200×` overwhelm | Correctly labeled; recast as back-reaction-closure gap (§II.4) |
| `A_s` (UNIFIED-AS-79) | band-cited | `3.11–4.27×10⁻⁹` | My Branch-A point `3.2994×10⁻⁹` sits inside band; band form endorsed |

No transit-domain gate verdict in the source conflicts with my canonical record.

---

## IV. Structural Implications

**What the document gets right at the structural level (my axis).** The capstone correctly identifies the *governing structure* of cosmogenesis as a Bogoliubov problem on a monotone-swept background, not a slow-roll problem on a potential. Every downstream consequence the document draws from this — the GGE relic, the Ordered Veil (integrability ⇒ no thermalization), the acoustic white-hole horizon structure, the `A_s` band — descends correctly from that structure. The ordering is right (monotonicity theorem first, P_exc saturation second), and the regime statements are correct (diabatic, supersonic, impulsive). This is the structure-first discipline my field demands, and the document holds it.

**What the constraint map looks like after this review.** Two corridors are *clarified* (not opened or closed):

1. **The substrate-BdG ↔ Mukhanov-Sasaki layer boundary** (§II.2, Gap #1) is a presentational seam, not a physics gap. The two mode equations are both correct; the document prints only one and cites an observable of the other. Closing the seam is a writing task (print both, label the transduction), not a computation. But until it is closed, the document is *vulnerable to exactly the layer-confusion the framing law exists to prevent* — a reader could attribute `A_s` to the BdG `u_k` instead of the MS `v_k`.

2. **The `a(t)` gap is a back-reaction-closure gap** (§II.4). The transit kinematics (local rate, Bogoliubov spectrum) are in hand; what is missing is the produced-quanta → global-expansion-rate feedback. This is the same gap as C2/T6, viewed from the transit side. It sharpens *what kind of computation* would close it: a back-reaction equation `H² = f(ρ_relic, S_SA)`, not merely "a Friedmann equation."

**What this review does NOT touch.** The `w₀` branch-multiplicity (the search surfaced `−0.918` / `−0.842454` / `−0.494` ζ-branch / `−0.997` Zubarev) is a mack/volovik adjudication, not mine — I note that §7 and §9 cite the `(−0.918 / −0.842454)` pair while the broader ledger carries additional branches, and flag only that the *branch label* should be consistent between §7.1 and the registry; I do not adjudicate which branch is physical. The NCG axioms, Seeley–DeWitt algebra, gauge content, and CC closure are outside my axis and I take their PROVEN/CERTIFIED statuses as authoritative per the review rules.

---

## V. Carry-Forward Computations

**These are recommendations for the document and for future transit-domain work, in the four-field form. None re-adjudicates a PROVEN status; all sharpen the transit↔CMB connective tissue.**

```
V.1. Print both mode equations in §5.3 and label the transduction
   - What: edit §5.3 to print BOTH the substrate-BdG parametric oscillator
     (u_k″ + ω_k² u_k = 0, ω_k = BdG dispersion; relic content) AND the
     Mukhanov-Sasaki equation (v_k″ + (k² − z″/z) v_k = 0, z = a√(2ε_H)M_Pl,eff;
     emergent curvature, §7's A_s); add one sentence stating the squeeze of the
     first is transduced into the second at the exit horizon (§6.2).
   - Inputs: §5.3 text; §6.2 "squeeze produced at fold, regulated at exit" sentence;
     canonical MS form from transit-dynamics MEMORY.md.
   - Gate: no numerical gate — this is a presentational firewall (analog of the
     §8.2 two-a_n firewall). PASS = both equations printed with layer labels.
   - Effort: <1 hour, document edit only.

V.2. Disambiguate the two N_pair readings in §7.1
   - What: in the §7.1 σ/m row change "(N_pair=1)" to "(N_Fock=1; ⟨Q⟩_GGE=59.8,
     see §5.3)" so the BCS-projection count (59.8) and the exact Fock reduction (1)
     are never the same symbol across sections.
   - Inputs: §7.1 table; §5.3 reconciling parenthetical.
   - Gate: presentational; PASS = no symbol "N_pair" carries two values without
     an inline disambiguator.
   - Effort: <30 min, document edit only.

V.3. Add the f_NL row to §7.1
   - What: add a non-Gaussianity row: framework |f_NL| ≲ 1.5 (Bogoliubov sudden-
     quench; squeezed vacuum Gaussian by Wick, φ_k≈0 kills folded enhancement) vs
     Planck f_NL^local = −0.9 ± 5.1; status PASS-class/structural (a squeezed-vacuum
     origin is falsified by large f_NL).
   - Inputs: max|f_NL| = 1.505 (transit-dynamics canonical, Bogoliubov sudden);
     Planck f_NL bound (comparison-only).
   - Gate: feeds §7.3 scorecard as a zero-free-parameter consistency PASS. No new
     compute needed (value already canonical); PASS = row added with both halves.
   - Effort: <1 hour, document edit; value is already computed.

V.4. Footnote the Bogoliubov-saturation origin of primordial α_s = 0
   - What: add a footnote to the §7 α_s box: "the primordial-side α_s = 0 is a
     Bogoliubov-saturation statement — P_exc = 1 freezes the spectrum (Sasaki-Stewart,
     exact at CMB to 10⁻¹¹³); the CMB-observed α_s is Phase-2 isocurvature transfer."
   - Inputs: α_s(primordial)=0 EXACT (transit-dynamics canonical); Sasaki-Stewart
     frozen-spectrum 10⁻¹¹³.
   - Gate: presentational; connects §7 running observables to §5.3 relic physics.
   - Effort: <30 min, document edit only.

V.5. Recharacterize the a(t) gap as a back-reaction-closure gap in §6.3
   - What: add to §6.3 frontier item (i) the transit-side framing: the kinematics
     (local sweep rate τ̇ at fold, full Bogoliubov spectrum) are in hand; the missing
     object is the back-reaction equation promoting produced relic energy density into
     a source for the GLOBAL expansion rate (H² = f(ρ_relic, S_SA)). This is the same
     gap as the NCG-side "derived S_SA(τ) → 4D gravitational action," stated from the
     transit axis.
   - Inputs: §6.3 text; T6 FAIL (133,200× overwhelm); local-rate τ̇ from §6.1.
   - Gate: clarifies WHAT computation closes C2/T6 (a back-reaction closure, not merely
     "a Friedmann equation"). No numerical gate; PASS = framing added.
   - Effort: <1 hour, document edit only.

V.6. Cross-link the two-horizon structure to the Wronskian decoupling theorem in §6.2
   - What: add a half-sentence to §6.2 stating the entry (a₂) and exit (a₄) horizons
     are genuinely distinct because a₂ and a₄ are algebraically independent (non-
     vanishing Wronskian away from genesis, §4.2) — so the two-horizon structure is
     LICENSED by the decoupling theorem, not an accidental double-count.
   - Inputs: §6.2 horizon table; §4.2 Spectral-Moment Decoupling Theorem (CERTIFIED).
   - Gate: presentational; ties the causal reading to a certified algebraic result.
   - Effort: <30 min, document edit only.

V.7. Inline the "why r = 16ε fails" reason in §5.1
   - What: add one sentence to §5.1 stating r = 16ε is a theorem of the single-clock
     adiabatic vacuum (c_s = 1, single-field, slowly-varying background) and the fold
     violates all three premises (diabatic sweep, BdG c_s ≠ 1, multi-mode squeezed GGE),
     so the relation's derivation assumptions are absent — not merely "gives the wrong
     number."
   - Inputs: §5.1 text; the five VdD-Hawking arguments (cited, not re-derived).
   - Gate: presentational; pre-empts the most common reviewer objection.
   - Effort: <30 min, document edit only.
```

---

## VI. Summary Table

| # | Result / Recommendation | Classification | Status | Implication |
|:--|:------------------------|:---------------|:-------|:------------|
| 1 | "No well ⇒ transit, not slow-roll" governing structure (§5.1) | PHONONIC | ENDORSED | Correct spine; the controlling quantity is diabaticity, not slow-roll ε |
| 2 | Bogoliubov ≡ Kibble–Zurek, `P_exc = 1` saturation (§5.3) | PHONONIC | ENDORSED | Diabatic-limit saturation; not a fit, the only value the coefficients can take |
| 3 | Substrate-BdG `u_k` vs Mukhanov-Sasaki `v_k` mode equations (§5.3) | PHONONIC | FLAG — Gap #1 | Two layers; doc prints one, cites observable of the other; presentational firewall needed (V.1) |
| 4 | Two `N_pair` readings (59.8 vs 1) (§5.3 / §7.1) | PHONONIC | FLAG — Gap #2 | Same symbol, two values; disambiguate (V.2) |
| 5 | Acoustic white-hole, two sonic horizons (`a₂` / `a₄`) (§6.2) | PHONONIC | ENDORSED | Correct analog-gravity horizon-problem inversion; licensed by §4.2 Wronskian (V.6) |
| 6 | `a(t)` gap (§6.3) | structural boundary | ENDORSED (honest) | Correctly fenced; recast as back-reaction-closure gap from transit axis (V.5) |
| 7 | `A_s` band-citation `3.11–4.27×10⁻⁹` (§7) | PHONONIC | ENDORSED | My Branch-A point `3.2994×10⁻⁹` inside band; band form is the honest FI/RD call |
| 8 | `f_NL` ≲ 1.5 (Bogoliubov-Gaussian) — absent from §7 | PHONONIC | RECOMMEND ADD | Zero-parameter consistency PASS; squeezed-vacuum origin falsifiable by large `f_NL` (V.3) |
| 9 | primordial `α_s = 0` via Bogoliubov saturation — absent from §7 box | PHONONIC | RECOMMEND ADD | Transit-side complement to the two-scale transport-degree resolution (V.4) |

---

## Closing assessment

The document is **correct and honest on the transit-dynamics axis**, and unusually disciplined about regime of validity — it never applies slow-roll outside its regime, it draws the `a(t)` gap without softening, and its `A_s` band-citation is the right epistemic form for a regulator-dressed absolute-energy observable. The two flags (§II.2) are presentational seams between the substrate-relic layer and the emergent-CMB layer, not physics errors; closing them is writing, not computation. The two recommended additions (`f_NL`, the Bogoliubov-saturation origin of `α_s = 0`) would let the document *count two more zero-free-parameter consistency results it has already computed but does not display.* Every arrow in the transit story runs the right direction — `D_K eigenvalues → BdG dispersion ω_k → diabatic Bogoliubov production → GGE relic → transduced squeeze → A_s` — substrate-first throughout, never inverted into a container.
