# Session 117 Synthesis: Counting-Class of the §VII.AJ.STATE-PROJ Substrate-First Datum R_summand

**Date**: 2026-06-29
**Agent**: landau-condensed-matter-theorist (Landau)
**Source Documents**:
- `sessions/session-117/session-117-w8-workingpaper.md` (§W8-1)
- `computations/session-117/s117_gate_verdicts.txt` (L152–L158)
- `computations/session-117/s117_w8_stateproj_inter_summand.py`
- `sessions/permanent-results-registry.md` §VII.AJ.STATE-PROJ (L16807–16850)
- `sessions/session-117/session-117-housekeeping.md` §D (L68)
- `.claude/rules/regulator-pin-discipline.md` §"Counting (intensive/extensive)" (4-axis-orthogonality row)

---

## I. Session Outcome

**Verdict: (A) — intensive substrate-FORCED.** The §VII.AJ.STATE-PROJ slot's *defining* functional is `ρ_BCS(P·H)` — a BCS-ground-**state** expectation (registry L16811/L16840: "algebra-DEPENDENT state-pair functional"). A state is normalized (`Tr ρ_BCS = 1`), so its expectation `ρ_BCS(P_g·|w|) = Tr(P_g|w|)/Tr(P_g)` is, *verbatim*, the counting-axis discriminator's intensive **"state evaluation `ρ_g(f(D))`, `ρ_g = P_g/Tr(P_g)`"** mass/position-class form. The counting class is therefore **FORCED intensive from first principles** — `R_summand = +0.9550 > 0` is the substrate-natural STATE-PROJ datum. The plan-pin **value is vindicated**; the plan-pin **reasoning is corrected** (the inheritance justification was non-binding on the counting axis). **No mack sign-fix is warranted; the registered +0.955 stands.** The extensive `−0.9917` is a structurally **different** observable (the total-condensation-energy-budget partition, action-moment-class), not a corrected sign.

This is sign-INDEPENDENT of the slot's substrate-first DISCHARGE, which stands in all outcomes (the `|R|≥1e-3` vanishing test PASSes on both counting axes — confirmed in the W8-1 verdict). **Low leverage, as pre-stated.**

---

## II. Key Results

### II.1 The functional, stated precisely (substrate-first)

**Result**: The §VII.AJ.STATE-PROJ datum IS the substrate's inter-summand BdG edge-condensation **density** asymmetry — not a measurement IN a container. Classification: **PHONONIC**.

Direction of explanation (`phononic-framing.md`):
```
D_K eigenvalues {λ_k}  →  ξ_k = |λ_k|  (μ=0 forced, wall #6)
   →  E_k = √(ξ_k² + Δ_BCS²)
   →  per-mode condensation weight  w_k = |ξ_k| − E_k + Δ_BCS²/(2E_k)   (≤ 0, PH-even, edge-localized)
   →  weighted against the substrate's OWN algebra central projections of A_K = ℂ ⊕ ℍ ⊕ M₃(ℂ)
   →  inter-summand asymmetry  R_summand = (a − b)/(a + b).
```
The two channels are the substrate's color sectors: the color-**singlet** `P_ℍ = (1 − 1_{M₃})` (the electroweak ℂ⊕ℍ content carried by the (0,0) sector, `n_ℍ = Tr P_ℍ = 16`) and the color-**charged** `P_{M₃} = 1_{M₃}` (`n_{M₃} = Tr P_{M₃} = 166{,}880`), via the labeling-independent Peter-Weyl color-sector lift (geometric SU(3) ≡ color SU(3)_c).

Dimensional bookkeeping: `w_k`, `a`, `b` are energies (M_KK); `n_g` is a pure count; `R` is dimensionless. The intensive `a = Tr(P_g|w|)/Tr(P_g)` (M_KK) and the extensive `a_ext = Tr(P_g|w|)` (M_KK, a total) differ by the dimensionless factor `n_g`.

### II.2 The counting axis is the K₀-rank factor — the whole sign flip lives there

**Result**: The intensive→extensive sign flip (`+0.9550 → −0.9917`) is *entirely* the topological K₀-rank factor `n_g = Tr(P_g)`. **GEOMETRIC** (it is a property of the spectral triple's channel multiplicities, not of any excitation).

Sage-exact (this synthesis; from the W8-1 published per-mode primitives `a=6.5996e-3`, `b=1.5178e-4`, `n_ℍ=16`, `n_{M₃}=166880`):

| Form | Expression | Value | sign |
|:-----|:-----------|:------|:----:|
| **Intensive** (normalized-state eval) | `ρ_g(\|w\|) = Tr(P_g\|w\|)/Tr(P_g)` | `R_int = +0.955037340514088` | + |
| **Extensive** (weighted trace) | `n_g·ρ_g(\|w\|) = Tr(P_g\|w\|)` | `R_ext = −0.991696866949955` | − |

Per-mode contrast `a/b = 43.5×` (singlet edge wins per mode); total contrast `a_ext/b_ext = 1/239.9` (color tower wins in total) — because `n_{M₃}/n_ℍ = 10{,}430 ≫ 43.5`. The discriminator's own statement that the two classes "differ by the channel's K₀-rank factor `n_g`, topological" is realized exactly: divide out `n_g` → intensive; keep it → extensive.

### II.3 First-principles class determination (the mandatory [SIGN] substitution chain)

**Result**: the slot's defining functional is the discriminator's intensive mass/position-class form *verbatim* ⇒ intensive FORCED ⇒ sign POSITIVE. **PHONONIC**.

**Claim**: "The §VII.AJ.STATE-PROJ datum is intensive-FORCED; substrate-natural sign is POSITIVE, `R_summand = +0.9550 > 0`."

Substitution chain (`math-scripts.md §"Double-Check Logic Before Compute"`):

- **Step 1 — slot definition.** `§VII.AJ.STATE-PROJ datum := ρ_BCS(P_g · |w(D)|)`, the BCS-ground-**state** expectation of the channel-projected condensation operator. [registry L16811 "ρ_BCS(P·H)"; L16840 "algebra-DEPENDENT state-pair functional family", Corner III]
- **Step 2 — state normalization.** `ρ_BCS` is a *state* ⇒ `Tr(ρ_BCS) = 1`. Restricted to channel `g`, the maximally-mixed BCS occupation is the normalized projection `ρ_g = P_g / Tr(P_g)`. [definition of a state: positive, trace-1]
- **Step 3 — the intensive form.** `ρ_BCS(P_g·|w|) = Tr(P_g|w|)/Tr(P_g) = ⟨|w|⟩_g`, the per-mode condensation density. This is the discriminator's intensive class **"state evaluation `ρ_g(f(D))` with `ρ_g = P_g/Tr(P_g)`"** — *the same expression, symbol for symbol*. [regulator-pin-discipline.md §"Counting axis", substrate-analog column]
- **Step 4 — K₀-rank scaling test (FROM FIRST PRINCIPLES, not inheritance).** Apply the discriminator's *defining* criterion (extensive observables scale with `n_g`; intensive do not). Under a degeneracy rescaling `n_g → c·n_g` at fixed per-mode spectrum:
  `⟨|w|⟩_g = Tr(P_g|w|)/Tr(P_g) → (c·Tr(P_g|w|))/(c·Tr(P_g)) = ⟨|w|⟩_g` — **INVARIANT** ⇒ K₀-rank-INVARIANT ⇒ **mass/position-class** ⇒ `RATIO-NORMALIZED-TRACE-MEAN` (intensive).
- **Step 5 — read off the sign.** `sign(R) = sign(a − b) = sign(⟨|w|⟩_singlet − ⟨|w|⟩_color)`. The color-singlet (0,0) is pinned at the spectral floor `|ξ|_min = 0.8197 = 1.766·Δ_BCS` where `|w|` peaks; the color tower spreads to high `|ξ|` where `|w| ∝ |ξ|⁻³` is bulk-diluted ⇒ `⟨|w|⟩_singlet (6.60e-3) > ⟨|w|⟩_color (1.52e-4)` ⇒ `a − b > 0` ⇒ `R > 0`.
- **Conclusion**: intensive-FORCED, `R_summand = +0.9550 > 0`. ✓ (Sage-exact `+0.955037340514088`.)

### II.4 Why NOT (B) extensive-forced

**Result**: B's core fact is TRUE but does not win, because it identifies a *different* observable.

The condensation **energy** is indeed extensive (textbook thermodynamics: it scales with the number of Cooper pairs / modes; the canonical `E_cond = −0.137 M_KK` is a total). The team-lead's read — "a condensation-ENERGY-derived functional is action-moment-class → extensive" — correctly classifies the **total** `Tr(P_g|w|) = n_g·ρ_g(|w|)`: that object IS action-moment-class and IS extensive (`−0.9917`).

But the §VII.AJ.STATE-PROJ slot does **not** name the total energy. Its defining functional (Step 1) is the **normalized-state expectation** `ρ_BCS(P·H)` — a per-mode density, not a sum. The extensive total is the discriminator's "weighted trace" form, structurally distinct: it is `n_g ×` the slot's functional. Adopting B would silently re-define the STATE-PROJ slot as the total-budget observable — a category move, not a sign correction. The extensive value is a real substrate fact ("the substrate's condensate binding lives overwhelmingly in the color tower by total energy, because the color tower has 10,430× more modes"), but it answers the *total-budget* question, not the *per-mode-density* question the slot poses.

Substitution chain for the extensive (showing it is a separate observable):
`R_ext: a_ext = a·n_ℍ = 0.10559; b_ext = b·n_{M₃} = 25.330; R_ext = (a_ext − b_ext)/(a_ext + b_ext) = −0.9917`. Here `n_{M₃}/n_ℍ = 10{,}430 ≫ a/b = 43.5` ⇒ `b_ext ≫ a_ext` ⇒ `R_ext < 0`. The sign is set by mode-count, not by edge-density.

### II.5 Why NOT (C) genuinely dual-class

**Result**: this is NOT a lizzi-signature scheme-dependence; the choice is forced, not free.

The a_0/a_2 CC-ratio is genuinely convention-dependent because the *regularization functional* (zeta / cutoff / anomaly) is a physical degree of freedom with no substrate-forced choice — the functional IS the freedom. Here there is **no regulator d.o.f.**: both the intensive mean and the extensive sum are exactly computable from the cached spectrum, no regularization enters. The intensive/extensive "sign flip" is not two conventions for ONE observable; it is the fingerprint distinguishing **two different observables** (a normalized-state per-mode density vs an un-normalized total). The slot's definition (`ρ_BCS(P·H)`, a state expectation) selects the intensive one. Registering both signs as co-primary on the single §VII.AJ.STATE-PROJ slot would violate the single-observable-per-triple structural filter (`cross-pillar-bridge-anatomy.md`): a `n_g`-factor switch is a discontinuous (integer, topological) structural change, so the two are distinct functionals — distinct functionals get distinct slots, never co-primary on one. C is rejected.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| CF-S117-STATEPROJ-INTER-SUMMAND (W8-1) | **PASS** (FIXED; not re-adjudicated) | `R_summand = +0.955038` (L12), drift 1.41% |
| **Counting-class determination (this synthesis)** | **(A) intensive substrate-FORCED** | `R_int = +0.955037340514088`; class = mass/position |

The W8-1 PASS and the registered `R_summand` value are authoritative and untouched. This synthesis is the **orthogonal** counting-class determination requested in the spawn — it does not re-run the gate; it classifies the already-computed pair `{+0.9550, −0.9917}` and certifies which is the STATE-PROJ datum.

---

## IV. Structural Implications

**1. Plan-pin value vindicated; reasoning upgraded.** The plan reached the correct value (`+0.955`) by the wrong route ("intensive by inheritance to match W7's `bcs_condensation_energy`"). Inheritance is **non-binding on the counting axis**: it transports a *normalization choice* from a prior gate, it does not *derive the class*. The binding justification is first-principles: the slot's defining functional `ρ_BCS(P·H)` **is** the discriminator's intensive mass/position-class form, K₀-rank-invariant under degeneracy rescaling. The constraint-map cell for §VII.AJ.STATE-PROJ tightens from "intensive (plan-pinned)" to "intensive (substrate-FORCED, mass/position-class)".

**2. The counting axis is corner-informed for normalized-state functionals.** A general lesson sharpening the regulator-pin-discipline "Counting axis": when a substrate observable is *defined* as a normalized-state expectation `ρ(O)` (`Tr ρ = 1`) — the canonical Corner-III STATE-PROJ object — its counting class is **intensive by the meaning of "state"**. The extensive partner `n_g·ρ(O)` is the discriminator's weighted-trace (action-moment-class), a distinct observable. This does **not** collapse the declared orthogonality of the counting and algebra-axis pins (you *can* build an extensive total from a state-side quantity — e.g. total occupation `Σ n_k`); it states the narrower, true fact that the *native* normalized-state functional is intensive, and forming its extensive partner produces a different observable.

**3. The extensive value is not orphaned — it is the total-budget partition.** `R_ext = −0.9917` is a legitimate substrate observable: the inter-summand partition of the **total** BCS condensation-energy budget, mode-count-dominated. It shares the negative, count-dominated *character* of the §VII.AJ.OP-PROJ companion `R_∞ ≈ −1.892` (both are "the color tower wins by sheer multiplicity" statements), in contrast to the STATE-PROJ per-mode-density statement. If it ever warrants registry presence, it is a *distinct* slot/sub-row (action-moment-class total-budget), never a co-primary alternative-sign of the STATE-PROJ datum.

**4. No registry sign change.** Outcome A leaves the §VII.AJ.STATE-PROJ Status block's value and DISCHARGE intact. The only recommended registry touch is a non-sign-changing **reasoning annotation** (§V.2), at mack's discretion as sole writer of the §VII surface.

---

## V. Carry-Forward Computations

The class-determination is **structural** — it reads an already-computed pair of values through the discriminator and the slot definition. It surfaces **no load-bearing residual math compute** (per the no-padding discipline, I do not manufacture one). The durable outputs are two **non-math** items (V.2, V.3), specified precisely for S118 plan-freeze, plus one **optional, low-leverage** robustness compute (V.1) offered with a full 4-field spec to honor the §V contract.

```
V.1  [OPTIONAL / LOW-LEVERAGE]  Normalized-state-family invariance of the intensive STATE-PROJ sign
   - What: Confirm sign(R_int) is invariant across the family of admissible normalized BCS states ρ_BCS
           on each channel — uniform ρ_g = P_g/Tr(P_g) (the W7/W8-1 un-PW-weighted form) vs the
           BdG-occupation-weighted ground state ρ_g ∝ Σ_k v_k²|k⟩⟨k| (v_k² = ½(1 − ξ_k/E_k)) vs the
           Peter-Weyl-multiplicity-weighted form (already shown same-sign at R12=+0.9676). Pre-registered
           predicate: every normalized-state member gives R_int > 0 (intensive sign is normalized-state-
           family-invariant), substantiating Step 2→3 of the §II.3 chain numerically.
   - Inputs: computations/session-84/s84_spectrum_cache_L12_tau019.npz (sector_evals);
             canonical_constants.Delta_BCS (R-PROTECTED, =0.4642547394830737);
             w_weight() + color_resolved_R() from s117_w8_stateproj_inter_summand.py (re-use, no rebuild).
   - Gate: NEW CF-S118-STATEPROJ-INTENSIVE-NORMALIZED-FAMILY. PASS = all normalized-state members
           give sign(R_int)=+1 AND |R_int spread| ≤ 0.05; INFO = same sign, spread ∈ (0.05, 0.20];
           FAIL = any member flips sign. [SIGN]. (Does NOT touch the extensive form — that is a
           distinct observable, out of scope.)
   - Effort: ~1 hour, 1 agent session (cache re-read + 3 normalized-state evaluations; no diagonalization).
```

**V.2 — §D counting-axis calibration-corpus strengthening (NON-MATH; methodology; S118 plan-freeze / `/weave --update` reindex).**
The current §D ledger entry (`session-117-housekeeping.md` L68) records only **that** the sign is counting-convention-determined (`+0.955` intensive vs `−0.992` extensive, vanishing-PASS on both; SUGGESTION K=1). It does **not** record **which** class is substrate-forced. Strengthen the `regulator-pin-discipline.md §"Counting axis"` corpus entry to add the determination:

> *S117-W8 (Landau adjudication): for the §VII.AJ.STATE-PROJ datum the counting class is substrate-FORCED **intensive** — the slot's defining functional `ρ_BCS(P·H)` is the discriminator's intensive "state evaluation `ρ_g(f(D))`, `ρ_g = P_g/Tr(P_g)`" mass/position-class form (K₀-rank-INVARIANT per-mode condensation density), NOT an inheritance from W7. Structural calibration: when a substrate observable is **defined** as a normalized-state expectation (the native Corner-III STATE-PROJ object, `Tr ρ = 1`), its counting class is intensive by the meaning of "state"; the extensive partner `n_g·ρ_g(f(D))` is the discriminator's weighted-trace (action-moment-class) — a **distinct** observable (here the total-condensation-energy-budget partition, `−0.9917`, mode-count-dominated, sharing the negative character of the OP-PROJ companion `R_∞≈−1.892`), NOT a corrected sign of the same datum.*

Status stays SUGGESTION K=1 (one instance), but the corpus row now carries a forced-class determination + the corner-informed structural insight, not merely "convention-determined". This is the durable output regardless of A/B/C.

**V.3 — mack §VII.AJ.STATE-PROJ reasoning annotation (NON-MATH; registry; mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`; S118 plan-freeze §A item, NON-sign-changing).**
**No sign-fix** (outcome A, not B). The registered `+0.955` stands. Recommended one-line annotation to the §VII.AJ.STATE-PROJ Status block, replacing the bare "intensive (plan-pinned)" counting note with the first-principles class determination:

> *Counting-axis class (first-principles, S117-W8 Landau adjudication): the slot's defining functional `ρ_BCS(P·H)` is the discriminator's intensive "state evaluation `ρ_g(f(D))`, `ρ_g = P_g/Tr(P_g)`" mass/position-class form (`regulator-pin-discipline.md §"Counting axis"`) — K₀-rank-INVARIANT (per-mode condensation density), substrate-FORCED, not inheritance from W7. ⇒ intensive **+0.9550** is the STATE-PROJ datum. The extensive RATIO-BLOCKSUM **−0.9917** is the action-moment-class weighted trace `n_g·ρ_g(|w|)` — the distinct total-condensation-energy-budget partition (mode-count-dominated; shares the negative count-dominated character of the OP-PROJ companion `R_∞≈−1.892`), NOT the STATE-PROJ datum and NOT a co-primary alternative sign. No sign change.*

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Counting class of R_summand = **intensive substrate-FORCED** (verdict **A**) | PHONONIC | DETERMINED | `+0.955` is the STATE-PROJ datum; plan-pin value vindicated |
| 2 | Sign flip `+0.955→−0.992` = the K₀-rank factor `n_g` (only) | GEOMETRIC | Sage-exact | the two values are two *observables*, not two conventions |
| 3 | Slot functional `ρ_BCS(P·H)` = discriminator's intensive "state eval" form, *verbatim* | PARTICLE | structural | counting class forced by the slot definition, not inheritance |
| 4 | (B) extensive rejected — total-budget partition is a *different* observable | PHONONIC | rejected | condensation energy IS extensive, but the slot names a density |
| 5 | (C) dual-class rejected — no regulator d.o.f.; choice is forced | GEOMETRIC | rejected | not a lizzi a_0/a_2 scheme-dependence; co-primary FORBIDDEN |
| 6 | §D corpus strengthened: which class forced + corner-informed rule | NON-PHONONIC (methodology) | recommended (V.2) | SUGGESTION K=1, now with forced-class determination |
| 7 | mack annotation: reasoning fix, NO sign change | NON-PHONONIC (registry) | recommended (V.3) | registered +0.955 stands; reasoning upgraded |

**Bottom line (substrate-first).** `R_summand` IS the substrate's inter-summand BdG edge-condensation-**density** asymmetry — the per-mode statement that the color-singlet electroweak edge condenses ~43× more densely than the average color-tower mode, pinned by the (0,0) sector sitting at the D_K spectral floor. As a normalized-state expectation it is intensive by construction; `+0.9550` is the §VII.AJ.STATE-PROJ datum, FORCED, not chosen.
