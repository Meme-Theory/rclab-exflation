# Investigation-5 Synthesis: The m_H +5.36% Residual — Three Independent Readings (INV5-W3-3 Review)

**Date**: 2026-06-15
**Agent**: gen-physicist (neutral single-agent synthesizer; NOT a participant in any of the three source gates)
**Gate**: INV5-W3-3 (`gate_type: review`; closes by artifact-existence-with-content; NO verdict line, NO `emit_verdict`)
**Source Documents**:
- `computations/investigation-5/inv5_gate_verdicts.txt` — verdict lines INV5-W1-1-PS-QUADRATIC-FLUCTUATION-HIGGS-QUARTIC, INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY, INV5-W3-1
- `sessions/investigation/investigation-5/investigation-5-w1-workingpaper.md §W1-1` (connes — Pati-Salam quadratic-fluctuation QUARTIC)
- `sessions/investigation/investigation-5/investigation-5-w2-workingpaper.md §W2-3` (landau — Pekker-Varma continuum SELF-ENERGY)
- `sessions/investigation/investigation-5/investigation-5-w3-workingpaper.md §W3-1` (spectral-geometer — a₄ L_max TRUNCATION tail)
- `sessions/investigation/investigation-1/connes-ncg-theorist.md` (G-1, C-1, R-1: the Pati-Salam quartic route)
- `sessions/investigation/investigation-1/landau-condensed-matter-theorist.md` (C-2, B-2, R-4: the amplitude mode + the m_H-residual/effacement decoupling)
- `sessions/investigation/investigation-1/spectral-geometer.md` (C4, R4, LB1: +5.36% as the a₄ truncation tail at L_sat=6)

**Charge** (neutral, per `feedback_review-dispatch-no-orchestrator-angle.md`): synthesize the three independent readings head-to-head along two axes — **SIGN** and **MAGNITUDE** — plus a **TRUNCATION-vs-PHYSICAL** classification. Do the three AGREE or CONFLICT? Characterize the joint picture; do NOT force a single winner. No injected angle; no pre-judged conclusion about which reading is correct.

---

## I. Session Outcome

All three prerequisite gates have landed: **INV5-W1-1 PASS, INV5-W2-3 FAIL, INV5-W3-1 INFO** — a full three-way synthesis (no PARTIAL-PENDING). The headline structural finding is a clean asymmetry: the two readings that attempted to **explain-and-remove** the +5.36% residual (landau's physical continuum self-energy, spectral-geometer's resolvable truncation tail) BOTH **failed on SIGN** — and they failed in opposite functionals for the same structural reason (the carrier mode / the extensive coefficient sits on the wrong side of the relevant scale, so the shift goes UP where DOWN was needed). The one reading that **did not attempt to remove** the residual — connes' Pati-Salam quadratic-fluctuation quartic, which treats +5.36% (vs PDG) as a PROPERTY of the geometric quartic rather than a correction to it — PASSED, landing m_H = 135.01 GeV inside the framework's own eps_H band around 131.8 GeV.

The three therefore **do NOT conflict in the naive truncation-vs-physical sense** (the seed's worry: "truncation says it vanishes while self-energy says it persists"). They cannot conflict that way, because **both** the truncation-vanishes mechanism (W3-1) and the named physical-screening mechanism (W2-3) were **independently falsified**. The residual is, as of these three computes, **neither a resolvable a₄ truncation tail NOR the named Pekker-Varma continuum screening** — its specific +5.36% value remains **UNDERIVED**. What the three jointly establish is a constraint map, not a winner: two corridors closed, one corridor (the residual as an intrinsic property of the substrate's geometric quartic, consistent within eps_H) left occupied but not pinned to the exact number.

---

## II. The Residual Under Test (one number, three functionals)

The object is the **m_H residual** — a derived consequence of the a₄ weight-4 spectral moment of D_K (the a₄-dressed `|S|²` KK-threshold mode). Substrate-first, the arrow is identical across all three readings:

```
D_K eigenvalues → spectral moments (a₄/a₂ → Higgs quartic λ) → emergent m_H → measured residual
```

The residual itself (all three gates pin the SAME number from canonical constants):

| Quantity | Value | Source |
|:---------|:------|:-------|
| `m_H_FW_KK_threshold` | 131.8 GeV | S100a, KK-THRESHOLD-64 |
| `m_H_obs` | 125.1 GeV | ATLAS+CMS Run-1 |
| residual vs PDG | **+6.7 GeV = +5.356% = 67/1251 (Sage-exact) = +38.5σ** | `r_KK` |

Three substrate-IS readings of THIS number, never a container-side correction TO an external m_H. The TRUNCATION-vs-PHYSICAL axis is itself substrate-first: **TRUNCATION** = the residual is an artifact of reading the substrate at finite L_max and vanishes as the substrate's own spectrum resolves toward the continuum; **PHYSICAL** = the residual is a genuine substrate observable (a derived screening or an intrinsic quartic value) that survives the continuum limit.

---

## III. Gate Verdicts

| Gate | Reading | Verdict | Decisive Number |
|:-----|:--------|:--------|:----------------|
| **INV5-W1-1**-PS-QUADRATIC-FLUCTUATION-HIGGS-QUARTIC | connes — Pati-Salam quadratic-fluctuation QUARTIC | **PASS** | m_H^PS = 135.01 GeV; \|135.01 − 131.8\| = 3.21 ≤ 6.7 (eps_H); 3-tuple sign=PASS / mag=PASS / regime=VALID |
| **INV5-W2-3**-PEKKER-VARMA-HIGGS-SELF-ENERGY | landau — Pekker-Varma continuum SELF-ENERGY | **FAIL** | Re Σ(ω_H3=11.465)/m_H = **+0.314%** (POSITIVE), target −5.356%; 3-tuple sign=FAIL / mag=FAIL / regime=VALID |
| **INV5-W3-1** | spectral-geometer — a₄ L_max TRUNCATION tail | **INFO** | tail_fraction = **1.044** (a₄ monotone-INCREASING; Δa₄ all > 0), band [0.0268, 0.0804]; 3-tuple sign=FAIL / mag=INFO / regime=MARGINAL |

(Verdicts read off disk verbatim; NOT re-adjudicated. INV5-W1-1 audit_sha256 `687d9c9d…46`; INV5-W2-3 audit_sha256 `d51071e0…0d`; INV5-W3-1 audit_sha256 `9673cfff…cc`.)

---

## IV. Axis 1 — SIGN

The SIGN axis asks: does each reading predict a shift that is **consistent with the framework sitting ABOVE PDG** (the 131.8 > 125.1 fact), or a NEGATIVE screening that pulls 131.8 back toward 125.1? Two distinct sub-questions are folded in here, and the three gates do not all answer the same one — this is the first structural subtlety.

- **W1-1 (connes) — sign=PASS.** The Pati-Salam quartic reading is NOT a screening; it is a recomputation of the bare geometric quartic with the broken order-one axiom's quadratic fluctuations RETAINED. The quadratic term `A_quad = Σ c_ij[D_K,a_i][D_K,a_j]` is a positive-definite `|[D_K,a]|²` contribution to the a₄ heat-kernel trace ⇒ it ENHANCES λ by δ_quad = (‖A_quad‖/‖A_lin‖)² = (0.1133)² = +1.28% ⇒ pushes m_H UP (134.15 → 135.01). The predicted sign of `m_H − m_H_obs` is **positive** (+9.91 GeV), matching the framework-sits-above-PDG fact. SIGN PASS — but note this is the sign of the *quartic value being positive-and-above-PDG*, NOT the sign of a *removal* of the residual.

- **W2-3 (landau) — sign=FAIL.** The Pekker-Varma reading predicted a NEGATIVE screening: `Re Σ_continuum < 0`, a softening of the `|S|²` mode by decay into the substrate's own B2/B3 two-quasiparticle pair-breaking continuum, which would pull 131.8 down toward 125.1 and DERIVE the residual. The computed `Re Σ(ω_H3=11.465) = +0.03596 M_KK > 0` is **POSITIVE** — the OPPOSITE direction. The substrate's verdict is unambiguous and structural: the `|S|²`-radial m_H carrier ω_H3 = 11.465 sits a full order of magnitude ABOVE its entire continuum (band-top 2Δ_B2 = 1.464), so every continuum state has `(ω_H3 − Ω) > 0`, the principal-value integral is positive everywhere, and a discrete mode far above a continuum is repelled UPWARD. SIGN FAIL: the predicted softening direction is wrong at the m_H carrier. (Notably, the correct softening sign DOES appear at the Higgs-Leggett hybrid ω_H2 = 1.410 sitting AT the continuum edge — `Re Σ = −0.795 < 0` — but that is a different mode of the wrong magnitude.)

- **W3-1 (spectral-geometer) — sign=FAIL.** The truncation reading predicted a DECREASING tail: `Δa₄(L) < 0`, the extensive a₄ relaxing downward toward a finite continuum value as L_max grows (so the L_max=3→6 tail would be the resolvable +5.36%). The measured slopes `Δa₄ = {+196, +1597, +4367}` are all strictly POSITIVE — a₄ monotone-INCREASING, the OPPOSITE direction. SIGN FAIL: the un-protected EXTENSIVE coefficient (Weyl exponent α₄ = d+r+4 = 14 > 0) GROWS with L_max; it does not relax to a finite continuum at all (the continuum heat-trace t²-coefficient is UV-divergent — the finite Gilkey value is a *different object*, the curvature integral).

**SIGN summary**: 1 PASS (W1-1, value-positive-above-PDG), 2 FAIL (W2-3, W3-1 — both removal-mechanisms predicted DOWN, both measured UP). The two FAILs share a structural genus: a discrete-mode-above-continuum (W2-3) and an extensive-coefficient-above-its-balanced-partner (W3-1) both shift in the over-counting/repulsion direction, i.e. AWAY from the screening that would close the residual. This is not coincidence — it is the same "wrong side of the scale" pattern in two functionals.

---

## V. Axis 2 — MAGNITUDE

The MAGNITUDE axis asks: does each reading's number match the +5.36% / +6.7 GeV / 38.5σ residual?

- **W1-1 (connes) — magnitude=PASS, but against a DIFFERENT target.** W1-1's magnitude test is m_H^PS vs the framework's OWN 131.8 (NOT vs PDG 125.1): `|135.01 − 131.8| = 3.21 GeV ≤ 6.7 GeV` eps_H band (fractional 0.0243 ≤ 0.0508 tol). So W1-1 PASSES the test "does the PS quadratic route reproduce 131.8 within eps_H." It does NOT derive the −5.36% screening (it never tried to); its residual vs PDG is +9.91 GeV, LARGER than the original 131.8-vs-PDG +6.7 GeV. The PS reading's content: the +5.36% (relative to PDG) is a PROPERTY of the geometric quartic that sits inside the framework's eps_H precision, not a quantity to be removed.

- **W2-3 (landau) — magnitude=FAIL.** Target −5.356%; computed +0.314% at the m_H carrier. `|+0.314% − (−5.356%)| = 5.669 pp ≫ 3 pp` INFO band ⇒ magnitude FAIL. Even setting sign aside, the continuum self-energy at ω_H3 is two orders of magnitude too small (+0.31% vs the 5.36% needed). The effacement factor Γ_eff = 0.99970 it was meant to replace corresponds to (1−Γ_eff) = 0.03% — a DISTINCT quantity from the 5.36% residual; the gate confirmed the self-energy supplies +0.31% of the wrong sign, NOT the 5.36%.

- **W3-1 (spectral-geometer) — magnitude=INFO.** tail_fraction = 1.044 vs target 0.0536; `|1.044 − 0.0536| = 0.990`, ~19.5× the upper band edge. Magnitude INFO (out-of-band but the regime is MARGINAL not BREAKDOWN, so the composite is INFO-physical, not FAIL). The tail is ~23× over L=3→6 — qualitatively in the wrong universe, not a near-miss.

**MAGNITUDE summary**: only W1-1 is in-band, and against 131.8 not PDG. Neither removal-mechanism (W2-3, W3-1) is anywhere near the −5.36% magnitude — W2-3 is ~17× too small, W3-1 is ~19× too large. There is no magnitude agreement to speak of between the three: they are testing different targets (W1-1 vs 131.8; W2-3 and W3-1 vs the 5.36% PDG residual) and the two that test the residual directly both miss by more than an order of magnitude.

---

## VI. Axis 3 — TRUNCATION vs PHYSICAL (per-reading classification)

This is the classification the charge requires explicitly, per reading:

- **W3-1 (spectral-geometer) — TRUNCATION reading: FALSIFIED.** This gate IS the truncation hypothesis ("+5.36% is a resolvable finite-L_max artifact that vanishes as L_max → ∞"). It returned INFO-physical: the un-protected extensive a₄ does the OPPOSITE of vanishing (it diverges, α₄ = 14 > 0, multiset {8,4} ≠ {6,6} so not weight-balanced ⇒ no cancellation). **Verdict on the axis: the residual is NOT truncation.** The corridor "+5.36% disappears as the substrate's spectrum resolves toward the continuum" is ELIMINATED. (The gate also corrected spectral-geometer's survey C4/R4 reading: that survey conflated the τ-axis variation of a₄ — 28.65% across τ ∈ [0,0.5], the S77 R₁ trajectory — with an L_max-axis convergence tail; on the L_max axis at fixed τ_fold a₄ has no finite continuum at all. The two axes are structurally distinct.)

- **W2-3 (landau) — PHYSICAL reading (one specific mechanism): FALSIFIED on sign.** This gate tested ONE candidate physical screening: the Pekker-Varma continuum self-energy. It returned FAIL on sign. **Verdict on the axis: the residual is NOT this physical screening.** The corridor "+5.36% is the `|S|²`-mode self-energy from the B2/B3 continuum" is CLOSED. This does NOT close the PHYSICAL classification in general — it closes the named mechanism. The residual could still be physical via a different substrate observable that survives the continuum (the survey's broader B-2/R-4 framing — convert Γ_eff into a derived screening — is not realized by THIS route).

- **W1-1 (connes) — NEITHER truncation NOR screening: the residual as an intrinsic quartic PROPERTY.** This gate does not classify the residual as truncation or as a screening at all. It computes the bare geometric quartic (with the broken-axiom quadratic fluctuations present) and finds m_H = 135.01 inside the framework's eps_H band around 131.8. The implicit classification: the +5.36% (relative to PDG) is a PHYSICAL property of the geometric quartic — it survives the continuum (W1-1 runs at L_max=12, and the quartic is a ratio a₄/a₂, an R-protected balanced object, NOT the extensive a₄ that W3-1 found divergent) — but it is an intrinsic value, not a derived screening that removes the residual. In the framework's substrate-first frame, 131.8 ± 6.7 (eps_H) IS the prediction; the residual against PDG is the band, not a defect to source.

**Axis summary**: the three classifications do not contradict — they partition cleanly. W3-1 rules OUT truncation. W2-3 rules OUT one specific physical screening (on sign). W1-1 supports the residual being an intrinsic (physical-but-not-screening) property of the quartic, consistent within eps_H. The only way to read these three as a *conflict* would be to claim W3-1 says "vanishes at continuum" while W2-3 says "persists" — but W3-1 did NOT say it vanishes (it FAILED to show vanishing; a₄ diverges), and W2-3 did NOT show it persists as the named screening (it FAILED on sign). The naive conflict the seed flagged does not materialize because both removal hypotheses are falsified.

---

## VII. Structural Implications (the joint picture)

**Do the three AGREE or CONFLICT?** Neither, in the strong senses the charge offered. They are **mutually consistent under the TRUNCATION-vs-PHYSICAL classification** in a specific, non-trivial way:

1. **The residual is NOT a resolvable truncation tail** (W3-1, decisive on its own axis: extensive a₄ diverges with L_max, sign FAIL).
2. **The residual is NOT the named Pekker-Varma continuum self-energy** (W2-3, decisive on its own axis: `Re Σ > 0` at the m_H carrier, sign FAIL).
3. **The residual is consistent with being an intrinsic property of the geometric quartic** that sits inside the framework's own eps_H band (W1-1, PASS vs 131.8) — but its specific +5.36%-vs-PDG value is **NOT DERIVED** by any of the three.

The three readings are testing **different questions about the same number**, and the joint constraint map is sharper than any single gate:

- W1-1 establishes the residual's HOST: it lives in the R-protected balanced ratio a₄/a₂ (the quartic), NOT in the extensive a₄ alone. This is *consistent* with W3-1: W3-1 found the *extensive* a₄ divergent, but the *ratio* a₄/a₂ is exactly the weight-balanced ({8,4} numerator combined with the a₂ {6,6}-class balanced denominator) object that R-protection makes L_max-robust. So W3-1's "extensive a₄ diverges" and W1-1's "the quartic ratio is a stable L_max=12 prediction" are **not in tension** — they are the un-protected-vs-protected partition operating exactly as the R-Protection theorem (S76) predicts. The +5.36% is therefore NOT in the divergent piece.
- W2-3 and W3-1 share a structural genus on the SIGN axis: both removal-mechanisms shift in the over-counting/repulsion direction (UP), away from the screening (DOWN) that would close the residual. The substrate, probed in two independent functionals (a Landau self-energy and a Seeley-DeWitt coefficient), declines to supply a downward correction to 131.8.

**Net**: convergence #1 of the inv-5 seed — "the three vantages agree the +5.36% is the m_H residual" — resolves to: they agree it IS the residual, they agree (W3-1) it is not truncation and (W2-3) it is not the continuum self-energy, and (W1-1) the framework's geometric quartic produces 131.8 ± 6.7 with the +5.36%-vs-PDG sitting inside that band. **The residual's exact origin (why precisely 67/1251, not the eps_H-band's full ±5.08%) remains an OPEN substrate-physics question** — both derivation attempts that targeted the number directly were falsified, on sign, in opposite functionals.

Constraint-map updates:
- **CLOSED corridor**: "+5.36% is a resolvable a₄ extensive truncation tail at L_sat≈6" (W3-1 INFO-physical; the extensive a₄ diverges, contra spectral-geometer survey C4/R4).
- **CLOSED corridor**: "+5.36% is the Pekker-Varma `|S|²`-mode continuum self-energy / converts Γ_eff into a derived screening" (W2-3 FAIL on sign; contra landau survey B-2/R-4).
- **OPEN-and-occupied corridor**: "+5.36% (vs PDG) is an intrinsic property of the substrate's R-protected geometric quartic a₄/a₂, consistent within eps_H" (W1-1 PASS vs 131.8; the residual's exact value is not derived).
- **Effacement note** (cross-track, NOT an investigation edit): the Γ_eff = 0.99970 effacement factor is a 0.03% impedance quantity, structurally DISTINCT from the 5.36% residual (landau C-2/U-2, spectral-geometer C4) — the two should not be conflated. Any m_H prose-status reconciliation ("PROVEN-AT-OBSERVATION" vs the register; landau R-4, spectral-geometer R4) is a capstone-hygiene Q3 / designated-writer item routed to the SESSION track, not an investigation edit.

---

## VIII. Carry-Forward Computations

**These are SESSION-TRACK candidates** (`/rclab-investigate --investigation 5` lifts them into the housekeeping ledger at inv-5 close; this review does NOT itself promote — investigations feed the session pipeline per `gate-verdicts.md §"Track-local boundary"`).

```
VIII.1. Derive the m_H residual's exact value from the R-protected quartic ratio (NOT truncation, NOT continuum self-energy)
   - What: with the truncation (W3-1) and Pekker-Varma (W2-3) corridors closed, compute whether the residual 67/1251 is reproduced by the a₄/a₂ ratio's scheme/convention structure — specifically the RATIO-GILKEY-70 (ratio_gilkey=0.4140, conv B, m_H=131.8) vs cache-moment (a₄z/a₂z=0.4866, m_H=145.4) split, scanned for the convention that lands 131.8 exactly vs the +5.36%-vs-PDG band edge. Test whether the residual is a scheme-fixed property of the protected ratio rather than an additive correction.
   - Inputs: a_4_FW_zeta=1350.7216, a_2_FW_zeta=2776.165389, ratio_gilkey=0.4140, g_3(M_KK)=0.519, v_ew=246.0, m_H_FW_KK_threshold=131.8, m_H_obs=125.1 (=67/1251 exact); INV5-W1-1 npz (m_H^PS, δ_quad)
   - Gate: new gate INV6/Sxxx-MH-RESIDUAL-QUARTIC-SCHEME — PASS iff a single pre-registered (scheme, convention) pin reproduces 131.8 to within publication precision AND the +5.36%-vs-PDG is the eps_H band edge; INFO if the residual is band-width not a derived number; FAIL if no admissible scheme lands 131.8.
   - Effort: 1 agent session (~2-3 hours; a₄/a₂ machinery + canonical_constants on disk; the new work is the scheme scan + the band-edge comparison)

VIII.2. Diagonalize the explicit 169-direction A_quad module (W1-1 Stage-2 refinement)
   - What: replace W1-1's RMS spectral-amplitude bound for ‖A_quad‖ (defect_ratio·sqrt(n·λ_min²/Σλ²)) with a full diagonalization of the 169-direction quadratic inner-fluctuation module (session-46-wave2), recompute δ_quad from the eigenvalue shift directly, and re-evaluate m_H^PS. Tightens the +3.21 GeV vs 131.8 margin.
   - Inputs: A_K_PS summand dims [1,2,2,4] (S97 W5-2), 169 quadratic directions (session-46-wave2), CCS-2013 c_ij machinery (researchers/Connes/23), order-one residual 2.100
   - Gate: feeds a refined INV5-W1-1 successor — PASS iff diagonalized δ_quad keeps m_H^PS within eps_H of 131.8; the explicit eigenvalue shift either confirms or revises the +1.28% λ enhancement.
   - Effort: 2-3 agent sessions (the 169-direction module is on disk; the work is the full diagonalization + heat-kernel a₄-trace re-evaluation)

VIII.3. Independent derivation of Γ_eff = 0.99970 decoupled from m_H (landau R-4)
   - What: derive the Volovik-effacement factor Γ_eff = 0.99970 from impedance-mismatch first principles INDEPENDENTLY of the m_H residual, confirming the 0.03% effacement and the 5.36% residual are structurally separate (W2-3 confirmed they are distinct quantities; this closes the decoupling by deriving Γ_eff on its own footing).
   - Inputs: Gamma_effacement=0.99970, the Volovik partition / DILUTION-CC-66 machinery (ρ_vac/ρ_obs=1.032), impedance-mismatch structure (effacement residual 0.03%)
   - Gate: new gate Sxxx-GAMMA-EFF-INDEPENDENT-DERIVATION — PASS iff Γ_eff is derived to 0.99970 ± publication precision from impedance physics with NO m_H input; this re-tags the m_H claim from "geometric quartic + one fitted screening" to "geometric quartic + one DERIVED screening" (landau R-4) — a capstone-hygiene Q3 routing for the prose status.
   - Effort: 1-2 agent sessions (Volovik machinery on disk; the new work is the impedance-mismatch derivation of Γ_eff)
```

---

## IX. Summary Table

| # | Reading | Gate | Verdict | SIGN | MAGNITUDE | Truncation vs Physical |
|:--|:--------|:-----|:--------|:-----|:----------|:-----------------------|
| 1 | connes — Pati-Salam quadratic-fluctuation QUARTIC | **INV5-W1-1** | PASS | PASS (value +, m_H^PS=135.01 above PDG) | PASS (vs 131.8; +3.21 ≤ 6.7 eps_H) | NEITHER — intrinsic PHYSICAL property of the R-protected quartic (survives continuum at L_max=12); residual NOT removed, NOT derived to exact value |
| 2 | landau — Pekker-Varma continuum SELF-ENERGY | **INV5-W2-3** | FAIL | FAIL (Re Σ=+0.31% at ω_H3, predicted −) | FAIL (+0.31% vs −5.36%; 5.67pp off) | PHYSICAL (one mechanism) — FALSIFIED on sign; named screening ruled OUT |
| 3 | spectral-geometer — a₄ L_max **truncation** tail | **INV5-W3-1** | INFO | FAIL (Δa₄>0 increasing, predicted <0) | INFO (tail_frac=1.044 vs 0.0536; ~19.5× band) | TRUNCATION — FALSIFIED; extensive a₄ diverges (α₄=14>0), residual is NOT a resolvable truncation artifact |

**Joint verdict (NOT a single winner)**: the three are mutually consistent — the residual is NOT truncation (W3-1) and NOT the named continuum self-energy (W2-3); it is consistent with an intrinsic property of the substrate's R-protected geometric quartic within eps_H (W1-1), but its exact +5.36% value is UNDERIVED. Two removal-corridors closed (both failed on SIGN, in opposite functionals, sharing the wrong-side-of-the-scale genus); the intrinsic-quartic corridor is open and occupied. The residual's origin remains a genuine OPEN substrate-physics question routed to the session track.
