# WS-S113-4 DMMASS — Round 1

**Workshop**: WS-S112-4 DMMASS (Session 113 EVOI-frontier campaign) — adjudicating the 170× DM-mass shortfall (HK-170X-DM).
**Author / pole**: mack-cosmic-bridge — Round 1, steelman **Reading B (the Leggett-DM mass is irreducibly unanchored)**.
**Thesis (one line)**: The Leggett-channel DM mass is an inter-band coherence scale that is *dimensionless in M_KK units* (`M_DM = 11.97·Δ_BCS·M_KK`); its magnitude therefore inherits the just-closed M_KK permanent-external fate, and — decisively — the σ_SI = 1.299e-63 cm² NULL falsifier is *mass-anchor-robust* (survives the full 170× rescaling by ≥26.5 OOM), so "abundance-predicted / mass-unanchored" **sharpens** the falsifier rather than weakening the framework.

---

## 0. What the substrate actually fixes, and what it does not (the structural ledger)

Before steelmanning, I separate three categories the tension tends to blur — *what the substrate fixes*, *what it predicts as a ratio*, and *what it leaves as a dimensionful magnitude*. This is the substrate-IS / laboratory-IN cut (`phononic-framing.md §"IS Space, Not IN Space"`) applied to the DM sector.

| Quantity | Status | Source | Free params |
|:---------|:-------|:-------|:------------|
| **Ω_DM h² = 0.1200** (relic abundance) | **PREDICTED** (0.6% match) | §VII C7 / C11; Leggett-channel partition | **0** |
| **mass RATIO** `M_DM/Δ_BCS = 11.97` | **PREDICTED** (dimensionless) | `Mass_LeggettDM_over_Delta_BCS` (S70, LEGGETT-MOMENT-70) | **0** |
| **σ_SI = 1.299e-63 cm²** (direct-detection NULL) | **PREDICTED** (zero-free-param gravitational floor) | Row #79, `sigma_DM_nucleon_FW` | **0** |
| **mass MAGNITUDE** `M_DM = 4.128e17 GeV` | **rides M_KK** (= 11.97·Δ_BCS·**M_KK**) | Row #79; M_KK = 7.4287e16 GeV (CONST-FREEZE-42) | inherits M_KK's |

The decisive observation is in the bottom two rows: **the substrate-IS content of the DM mass is the dimensionless ratio 11.97**; the *magnitude* `4.128e17 GeV` is that ratio multiplied by `Δ_BCS·M_KK`, and `Δ_BCS` is itself "M_KK units = dimensionless ratio, R-PROTECTED" (`get_constant Delta_BCS` = 0.4642547, R-protected note: "M_KK units = dimensionless ratio"). So:

```
M_DM = 11.97 × 0.4642547 × M_KK = 5.557 × M_KK        [everything before M_KK is dimensionless]
```

**The mass magnitude is a pure dimensionless multiple of M_KK.** This is not an analogy to the M_KK import — it *is* the M_KK import, with a dimensionless prefactor 5.557 the substrate fixes exactly.

---

## 1. The Leggett mass inherits the M_KK permanent-external fate (the core structural argument)

The S112 keystone `CF-S112-MKK-SUBSTRATE-ANCHOR` **FAILed** (the `S111-CF-MKK-RG-INVARIANCE` precedent: M_KK is CODATA/M_Pl-routed, BARE-IMPORT, Δ_rel = 8.193, *not* τ-RG-invariant). The framework's own diagnosis (EVOI §6, the M_KK-DERIVATION standing gap; my memory `[[ws-co-1-compact-object-sterile]]` "M_KK-keystone master diagnosis"): **everything in the substrate is dimensionless in M_KK units; M_KK is the single dimensionful import that the spectral action does not select.** The self-referential-unit-system precedent is exact — you cannot bootstrap a dimensionful scale from a calculus whose every observable is a ratio.

Now apply the layer-functor logic to the DM mass. The mass-anchor question "what fixes `M_DM = 4.128e17 GeV`?" decomposes, via the structural ledger above, into two sub-questions:

- **(a) What fixes the dimensionless prefactor 5.557 = 11.97 × 0.4642?** — *Answer: the substrate already does, at zero free parameters.* `11.97` is the Leggett inter-band coherence ratio on the BdG gap (LEGGETT-MOMENT-70, PROVEN); `0.4642` is the canonical R-protected BCS gap. Both are dimensionless spectral-triple observables. **This part is anchored.**
- **(b) What supplies the dimensionful M_KK the prefactor multiplies?** — *Answer: nothing in the substrate — this is exactly the closed M_KK import.* A "surviving mass-anchor mechanism" that supplied `M_DM` in GeV would have to supply a dimensionful scale, which is *the same thing* as deriving M_KK. The four closed corridors (NSR / Imry-Ma / PBH-from-fold / CFL) are all attempts to supply (b) — and they fail for the same structural reason M_KK derivation fails: **a condensed-matter pairing/gap mechanism produces a dimensionless gap ratio, not a dimensionful magnitude.**

This is the steelman's spine: **the 170× shortfall is not a missing mechanism — it is the missing dimensionful scale, which the framework has independently established is a permanent external import.** The Leggett mass is *unanchored in magnitude for the same reason and to the same degree* that M_KK is. Reading A ("a not-yet-tested pairing mechanism anchors the mass") is structurally asking a closed question in new clothes: any pairing mechanism that anchors the *magnitude* would, by supplying a dimensionful scale absent CODATA/M_Pl, *be* the M_KK derivation — and that is the S112-FAILed keystone.

### 1a. Why the four closed corridors confirm rather than merely fail to refute

The corridors closed this excursion are not a random sample — they are *exactly* the four mechanism-classes that could have supplied a dimensionful mass scale from condensed-matter physics:

- **NSR pseudogap** (Nozières–Schmitt–Rink): phase-rigid; the pseudogap scale `Δ_pg` is a *ratio* to the pairing gap, not a new dimensionful anchor — it inherits the gap's M_KK-units.
- **Imry–Ma weak-disorder**: ~43× too weak (EVOI §6); disorder rounds the gap but cannot supply a 170× *magnitude* enhancement.
- **PBH-from-fold**: 37 OOM below the window — a gravitational-collapse scale set by the fold dynamics, not a coherence-mode mass.
- **CFL** (color-flavor-locked): "soft" — the CFL gap is again a dimensionless ratio on the underlying scale.

Each fails on the *same axis*: it produces a dimensionless ratio, and the ratio is the wrong size (or the right size but still dimensionless). **None can supply the dimensionful magnitude because no condensed-matter calculus on a finite spectral triple can** — the calculus is intrinsically ratio-valued. The pattern is the structural signature of a *closed solution-space corridor* (`epistemic-discipline.md §"How to Assess a Mechanism"`: closed = violates a proven wall), not an incomplete search. The wall is the M_KK self-referential-unit no-go.

---

## 2. The decisive consideration: the σ_SI NULL falsifier is mass-anchor-ROBUST (it SHARPENS)

This is where Reading B does positive work rather than merely conceding a gap. The adjudication question explicitly asks: *does the unanchored reading weaken or sharpen the σ_SI = 1.299e-63 cm² NULL falsifier?* The answer — from the structure of Row #79 — is **sharpen, decisively.**

**The falsifier does not consume the mass as a free input.** Row #79 derives σ_SI as the pure gravitational vertex `α_A = G_N · M_DM · m_Xe` of the (0,0)-sector inter-band coherence mode, where the ONLY inter-sector channel is a₂/gravity (forced by D_K block-diagonality S22b + V(gap,gap)=0 S23a + Trap-1 S34 + CPT-neutral gauge singlet + two-layer architecture S72). The mass enters σ_SI *through the same a₂/G_N unit map* that defines it — there is no independent "mass knob" that a surviving anchor could turn to push σ_SI up toward detectability without simultaneously moving M_KK.

I stress-tested this in Sage (exact, `RealField(200)`), taking the *most detection-favorable* assumptions for Reading A at each step:

**Stress test — does any mass rescaling resurrect a detection?**

| Scenario | σ_SI (cm²) | OOM below LZ-2024 | Verdict |
|:---------|:-----------|:------------------|:--------|
| Pin (M_DM = 4.128e17 GeV) | 1.299e-63 | **30.92** | NULL |
| Mass ÷170 (lighter), σ∝M², excl frozen | 4.49e-68 | **35.38** | NULL (widens) |
| Mass ×170 (heavier — structure-formation direction), σ∝M², excl rises ∝M | 3.75e-59 | **28.69** | NULL |
| Mass ×170, σ∝M², **exclusion FROZEN** (single most detection-favorable assumption) | 3.75e-59 | **26.46** | NULL |

The honest direction is the third/fourth rows: the 170× shortfall means structure formation wants a *heavier* particle (`m_required = 170 × m_Leggett`, per inv-5 `r_2scale = Δ_pg/D_s; target = m_required/m_Leggett = 170`), so a surviving anchor that *raised* the mass is the one that threatens the falsifier by pushing σ∝M² up. **Even granting that full 170× rise AND freezing the exclusion curve** (ignoring the flux-floor help that would weaken LZ's reach at higher mass), σ_SI sits **26.5 OOM below LZ-2024.** There is no rescaling within the physically-relevant range — light or heavy, by the full shortfall — that lifts the prediction within 26 orders of magnitude of any current or projected detector.

**First-principles cross-check** (Sage): the gravitational floor `σ ~ (G_N · M_DM · m_Xe)² / π ≈ 1.4e-65 cm²` reproduces the pin (1.30e-63) to ~2 OOM on a back-of-envelope — confirming the floor is real and astronomically tiny *because* G_N in particle units is 6.7e-39 GeV⁻². The smallness is structural, not a tuned coincidence.

**The structural reading**: the σ_SI NULL is a *zero-free-parameter, mass-anchor-independent* prediction. Whether the Leggett mass is anchored at 4.128e17 GeV or sits anywhere across a 170×-wide window, the substrate predicts a direct-detection NULL at every current and projected experiment. **An unanchored mass does not soften the falsifier — it reveals that the falsifier never depended on the anchor.** The prediction "σ_SI = 1.299e-63 cm², NULL at every Xe TPC" stands as a clean inverted falsifier (killed by a detection, corroborated by every deeper null) *regardless of how the mass-anchor question resolves*.

This is the Mack-style point about what observations actually test: the framework's *falsifiable* DM contact (σ_SI) is orthogonal to its *open* DM question (the mass magnitude). Conflating them — treating the open mass anchor as if it weakened the live falsifier — is a category error. The data tests the gravitational-floor NULL; the gravitational-floor NULL is anchor-free.

---

## 3. Engaging the strongest threat honestly (the framing law demands this)

The strongest version of Reading A is **not** "some pairing mechanism will turn up." It is this: *the 170× is not a magnitude question at all — it is a dimensionless **ratio** `m_required/m_Leggett`, and dimensionless ratios are exactly what the substrate CAN fix.* If a surviving condensed-matter mechanism supplies the dimensionless ratio 170 (the way LEGGETT-MOMENT-70 supplies 11.97), then the mass is anchored *without* needing a new dimensionful scale — Reading A wins on the substrate's own home turf.

I take this seriously because it is the one form of Reading A that escapes the M_KK no-go. My honest response, and the residual tension I hand to Round 2:

1. **The ratio target is structure-formation-derived, i.e. laboratory-IN, not substrate-IS.** `m_required` is set by the free-streaming / structure-suppression requirement (a measured cosmological constraint), and `m_Leggett` is substrate-IS. So `m_required/m_Leggett = 170` is a **bridge-map ratio** (substrate-IS denominator, laboratory-IN numerator), not an internal substrate ratio like `11.97` (both BdG-internal). For the substrate to *predict* 170, a mechanism would have to derive `m_required` — the structure-formation scale — from the substrate, which is a *different and harder* derivation than the gap ratio. This is the load-bearing distinction between my pole and Reading A, and it is where the workshop should converge.

2. **But I concede the door Reading A must walk through is real and not yet closed**: if `landau-condensed-matter-theorist` can exhibit a *substrate-internal* dimensionless enhancement of 170 between two BdG scales — a second coherence ratio, analogous to the 11.97, that happens to equal the structure-formation target — then the mass is anchored as a ratio and my "irreducibly unanchored" reading is wrong. The four closed corridors are evidence this is hard (each tried and missed), but "hard" is not "proven impossible." The honest status is **HARDENED-OPEN, leaning unanchored**, not **closed**.

3. **The asymmetry that still favors Reading B**: even if Reading A found a 170 ratio, it would anchor the mass *relative to a structure-formation scale that is itself set by M_KK-rooted cosmology* — so the *magnitude* in GeV would still ride M_KK. Reading A could at best convert "unanchored magnitude" into "anchored ratio, M_KK-rooted magnitude" — which is precisely the M_DM = 5.557·M_KK structure I already have. The ratio-anchoring would be a genuine *strengthening* (it would explain the 170 instead of carrying it as a gap), but it would **not** change the magnitude's M_KK-dependence and — critically — **would not touch the σ_SI NULL**, which is mass-anchor-robust either way.

---

## 4. Pre-registrable structural verdict candidate (what this pole would pin)

If Reading B prevails, the structural verdict is a *pinned scoping statement*, not a new compute gate:

> **The Leggett-DM mass MAGNITUDE is abundance-fixed / ratio-fixed (11.97 at 0 free params) but magnitude-unanchored — it rides the single M_KK dimensionful import (`M_DM = 5.557·M_KK`) and inherits M_KK's permanent-external status (S112 `CF-S112-MKK-SUBSTRATE-ANCHOR` FAIL). The 170× "shortfall" is a bridge-map ratio (structure-formation requirement / substrate coherence scale), not a missing substrate mechanism; the four closed corridors (NSR/Imry-Ma/PBH/CFL) confirm no condensed-matter calculus on a finite spectral triple can supply the dimensionful magnitude. The σ_SI = 1.299e-63 cm² NULL falsifier is MASS-ANCHOR-ROBUST (survives the full 170× rescaling by ≥26.5 OOM, Sage-verified) — the unanchored mass SHARPENS the falsifier by revealing it is a zero-free-parameter gravitational-floor prediction independent of the anchor.**

This would scope the DM falsifier (Row #79 stays a clean inverted NULL regardless of the mass-anchor resolution) and convert HK-170X-DM from "open mechanism gap" to "structural feature parallel to M_KK" — exactly the EVOI §6 framing ("HARDENED-OPEN ... only the MASS anchor is the standing gap"). It is the DM-sector analog of the WS-CO-1 STERILE verdict in my memory `[[ws-co-1-compact-object-sterile]]`: a sign/abundance-built sector whose *falsifiable* content is anchor-free and whose *open* content is the irreducible M_KK magnitude.

The pre-registrable gate this verdict *would* license, if anyone wants one, is the **falsifier-scoping check** (not a mass-anchor gate): pin into Row #79 the explicit statement that σ_SI's mass-derivative `d log σ_SI / d log M_DM` keeps the prediction below every detector horizon across `M_DM ∈ [M_Leggett, 170·M_Leggett]` — making the anchor-independence of the falsifier an audited property rather than a Round-1 Sage observation.

---

## 5. Honest current lean + single most decisive consideration

**(i) Honest current lean**: **Reading B (irreducibly unanchored), at ~65–70%.** The mass *magnitude* is a dimensionless multiple of M_KK (`5.557·M_KK`), so it inherits the S112-FAILed permanent-external fate by construction; the four closed corridors are the structural signature of a closed corridor (each fails on the same ratio-vs-magnitude axis), not an incomplete search. I hold back from a higher confidence because the *ratio* form of Reading A (§3.2 — a substrate-internal 170 enhancement) genuinely escapes the M_KK no-go and is not yet closed; that is the live threat the opponent should press, and it is what keeps this HARDENED-OPEN rather than closed. I will not pre-judge it.

**(ii) Single most decisive consideration**: **The σ_SI = 1.299e-63 cm² NULL falsifier is mass-anchor-robust by ≥26.5 OOM across the entire 170×-wide window (Sage-verified, `RealField(200)`).** This dissolves the premise that "unanchored mass" weakens the framework: the framework's *live, zero-free-parameter, falsifiable* DM prediction (the direct-detection NULL) is *orthogonal* to its *open* DM question (the mass magnitude). The mass being unanchored does not soften the falsifier — it reveals the falsifier never depended on the anchor. Whatever the mass-anchor adjudication, Row #79 stands as a clean inverted NULL: the framework is killed by a DM-nucleon detection above the gravitational floor and corroborated by every deeper null, and *that statement holds at every mass in the window*. The unanchored reading therefore **sharpens** the falsifier — which is the strongest possible outcome for a standing gap, and the reason "abundance-predicted / mass-unanchored" is a structural feature, not a liability.
