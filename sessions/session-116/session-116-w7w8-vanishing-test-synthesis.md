# Session 116 Synthesis: Does §VII.AV.STATE-PROJ pass the W7 vanishing test? — a functional-sensitivity cross-check

**Date**: 2026-06-28
**Agent**: lizzi-spectral-functional-theorist (Lizzi)
**Source Documents**:
- `sessions/session-116/workshops/s116-w7-algebra-axis.md` (the vanishing test, minted)
- `sessions/session-116/session-116-w7-workingpaper.md` (§VII.AJ.STATE-PROJ, Track-B / INFO)
- `sessions/session-116/session-116-w8-workingpaper.md` (§VII.AV.STATE-PROJ, FWD-C2 PASS / STAGE-3-PERMANENT)
- `computations/session-116/s116_gate_verdicts.txt` (W7-STATEPROJ-BCS INFO; W8-FWDC2-LANDING PASS)

---

## I. Session Outcome

**§VII.AV.STATE-PROJ PASSES the W7 vanishing test.** Its anchor `L_emp = −7.046336 M_KK²` is substrate-committed nonzero on the undifferentiated substrate: NONE of the three flagged legs (the Pauli–Villars multipliers, the Casimir-bound proxy, the s52 8-mode amplitude set) carries a laboratory-IN or canonical-import injection. The PV weight cancels (multiplicative-normalization-cancellation), the Casimir bound was discharged to the FULL physical compute, and the s52 amplitudes are D_K-derived BdG occupations. The two same-session STATE-PROJ instances are therefore **coherently credentialed under ONE consistent gate** (resolution (a)): the vanishing test correctly returns FAIL/Track-B-HELD for §VII.AJ (a lab-injected cross-vacuum A/B contrast) and PASS/Track-A for §VII.AV (a substrate-intrinsic dispersion at common gap). W8's `MULTIPLICATIVE-NORMALIZATION-CANCELLATION` + `SUBSTRATE-NATURAL-BINDING` credential is the §VII.AV-specific *instantiation* of the same substrate-commitment principle the W7 vanishing test executes — the two gates agree, the cross-check confirms it.

**One scope refinement (my axis).** The vanishing test resolves ONLY the substrate-vs-lab axis (substrate-COMMITMENT). It does NOT resolve the regulator/functional axis (FI vs SD). §VII.AV's `−7.046` is a regulator-class-keyed plateau `B(R)` by my own `math-scripts.md` K=3 multiplicative-cancellation rule; the vanishing-PASS certifies the substrate sources it, not that a zeta or Mellin functional would weight the s=4 pole identically. That UV-regulator-class FI/SD determination is the one genuine carry-forward.

---

## II. Key Results

### Result 1 — §VII.AV's substrate-IS observable is a single-vacuum variance, NOT an A/B contrast

**Result**: `L_emp := d²ln Var_a(|v_a(K)|²)/d(ln K)²` at substrate-distance-2 pole s=4, on the BdG sub-algebra M_2(ℂ)⊂A_K. Classification: **PHONONIC** (a GGE Bogoliubov occupation-statistics functional of the fabric's own amplitudes).

`Var_a` is the variance, across the 8 s52 Bogoliubov modes {B2×4, B1, B3×3}, of the squared BdG amplitudes `|v_a(K)|²` (W8 WP §W8-2, line 116). The 8 modes are substrate branches distinguished by the D_K spectral structure; the differentiation that makes `Var_a ≠ 0` is the substrate's own mode-to-mode dispersion at the COMMON gap `Δ_BCS = 0.46425 M_KK`. This is structurally distinct from §VII.AJ's `R_STATE = (a−b)/(a+b)` (W7 WP §W7-1, line 49), where the differentiation is the cross-phase gap split `Δ_A = Δ_BCS·SC_A` vs `Δ_B = Δ_BCS·SC_B` — a comparison across the 3He-A (DIII, N_3=2) and 3He-B (BDI, N_3=0) order-parameter manifolds, only ONE of which the fabric realizes. §VII.AJ's differentiator is lab; §VII.AV's is substrate.

Direction of explanation (substrate-first, per `phononic-framing.md`): `D_K eigenvalues → BdG amplitudes v_a(K) at common Δ_BCS → Var_a K-window curvature L_emp → Connes–Karoubi / K-theory-boundary image → 3He-B BdG band edge.` The gap supplies the intrinsic IR scale; the curvature converges without a UV cutoff.

### Result 2 — The three flagged injection candidates are all clean

**Result**: no laboratory-IN or canonical-import leg controls `L_emp`. FUNCTIONAL-INDEPENDENT substrate-commitment.

The vanishing test's diagnostic is "set every laboratory-IN parameter to its symmetric point and read the provenance of the residual; a lab ratio is FAIL, a substrate DOS/occupation ratio is PASS" (W7 Structural Verdict, line 391; volovik R3 §2-3, lines 286-310). Applied to the three legs the dispatch flagged:

1. **Pauli–Villars multipliers** (Connes–Chamseddine 1996: (M_KK, +2), (√2·M_KK, −1); Σc_r = 1, Σc_r M_r² = −4.4e-16): REGULATOR machinery, NOT lab. The `MULTIPLICATIVE-NORMALIZATION-CANCELLATION` (W8 WP line 121) proves the K-independent PV weight `M_PV(s=4)` is annihilated by `d²/d(lnK)²`: `M_PV(L12) = 1321.6 ≠ M_PV(L14) = 1333.3` (ratio 1.0088) yet `L_emp_FULL(L12) = L_emp_FULL(L14) = kernel = −7.046336474` to a 2.96e-10 residual. The PV weight does not enter the value — it cancels. CLEAN.

2. **Casimir-bound proxy**: it WAS the Level-2 envelope placeholder (`REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT`). The FWD-C2 PASS (`audit c79ee0db…`) DISCHARGED it: the FULL physical PV s=4 moment reproduces the proxy to `rel = 7.33e-11` via the same multiplicative cancellation. The bound is no longer load-bearing — the FULL substrate compute lands `−7.046` directly from the bare kernel. The proxy is a representation-theoretic (Peter–Weyl Casimir) SUBSTRATE quantity in any case. CLEAN.

3. **The s52 8-mode amplitude set** (B2×4 + B1 + B3×3): the BdG Bogoliubov amplitudes `|v_a(K)|²` are functionals of the D_K spectrum and the common gap `Δ_BCS` (W8 WP line 111: `D_K eigenvalues → BdG amplitudes v_a(K)`). No Serene–Rainer / Greywall lab input; no cross-vacuum contrast. The variance over these 8 modes is the substrate's intrinsic occupation dispersion. SUBSTRATE. CLEAN.

Contrast with §VII.AJ, where the controlling factors `SC_corr_A = 1.151`, `SC_corr_B = 1.111` are flagged LABORATORY-IN in `canonical_constants.py:721-727` (Greywall 1986 / Serene–Rainer 1983), `substrate_first_SC_ratio_available = False`, and the `+0.03536` reproduction is a bit-tautology (`rel_match = 0.0`, 0 independent substrate bits — W7 WP line 72).

### Result 3 — The vanishing-test verdict, by both readings

**Result**: §VII.AV PASSES — trivially (no lab leg, like OP-PROJ) AND by the deep diagnostic (substrate residual). FUNCTIONAL-INDEPENDENT.

Substitution chain (per `math-scripts.md §"Double-Check Logic Before Compute"`):

```
Claim: L_emp is substrate-committed nonzero on the undifferentiated substrate.
  Step 1: L_emp = d²ln Var_a(|v_a(K)|²)/d(ln K)²  at s=4            [W8 WP line 116]
  Step 2: Var_a = Var over {B2×4,B1,B3×3} of |v_a(K)|²,
          v_a(K) from D_K spectrum + common Δ_BCS                  [substrate; Result 2 leg 3]
  Step 3: vanishing limit = set all laboratory-IN params symmetric.
          §VII.AV has NO laboratory-IN params (Result 2)           ⇒ limit is a no-op
  Step 4: L_emp stays −7.046336 M_KK² ≠ 0, sourced by the substrate spectrum
  Step 5: the M_PV(s=4) weight cancels (mult.-norm.-cancellation); the
          residual = L_emp_kernel = −7.046 = substrate occupation-variance curvature
  Conclusion: residual provenance is a SUBSTRATE quantity ⇒ PASS (substrate-committed).
```

§VII.AV passes the way OP-PROJ passes (`R_∞ = −1.892`, zero lab input — W7 line 247), not the way §VII.AJ fails (`R_BdG → 0` when `SC_A = SC_B`, residual a lab ratio — W7 line 248). The `MULTIPLICATIVE-NORMALIZATION-CANCELLATION` is the structural ANALOG of §VII.AJ's `Δ_BCS`-cancellation: in BOTH a scale-weight cancels (the test "does not care that the gap [weight] cancels — it cancels both times; it reads the provenance of the residual" — W7 line 306). §VII.AJ's residual is the lab `SC_A/SC_B`; §VII.AV's residual is the substrate kernel `Var_a`. Opposite verdicts from identical algebraic skeletons — exactly the W7 diagnostic.

### Result 4 — §VII.AV is the realized genus of the W7 inter-summand reframe

**Result**: §VII.AV instantiates the substrate-intrinsic-dispersion-at-common-gap genus the W7 workshop proposed as the Track-A discharge route (CF-S117-STATEPROJ-INTER-SUMMAND). GEOMETRIC/PHONONIC structural correspondence.

The W7 workshop's discharge proposal: a Track-A STATE-PROJ instance compares two substrate objects at the COMMON `Δ_BCS` (ℍ vs M₃(ℂ) condensation-energy asymmetry), whose residual after `Δ_BCS`-cancellation is `(N_ℍ(0) − N_{M₃}(0))/(N_ℍ(0) + N_{M₃}(0))` — a substrate DOS ratio, no cross-vacuum lab contrast (W7 line 298-303). §VII.AV's `Var_a` over the 8 substrate BdG modes at common `Δ_BCS` is the SAME genus: substrate-intrinsic dispersion, common gap, residual sourced by the substrate's own multiplicity structure. They are not the identical observable (§VII.AV is the Var-curvature at s=4 on M_2(ℂ); the CF-S117 inter-summand is a condensation-energy asymmetry across ℍ/M₃), but they share the structural property the vanishing test rewards. **§VII.AV is thus a worked confirmation that the inter-summand genus is Track-A-eligible** — a sibling slot already past the gate §VII.AJ is held against.

### Result 5 — Coherence of the two credentialing gates is CONFIRMED

**Result**: W7's vanishing test and W8's substrate-natural-binding + multiplicative-cancellation are two operational faces of one substrate-commitment principle; they agree on both instances. No contradiction; the status asymmetry is correct.

| | §VII.AJ.STATE-PROJ (Corner III, s=3) | §VII.AV.STATE-PROJ (Cell IV, s=4) |
|:--|:--|:--|
| Credentialing gate | `S116-W7-STATEPROJ-BCS` (INFO) | `S116-W8-FWDC2-LANDING` (PASS) |
| Differentiator | cross-vacuum gap split `SC_A/SC_B` (LAB) | 8-mode BdG dispersion at common Δ_BCS (SUBSTRATE) |
| Scale-cancellation | Δ_BCS cancels (ratio functional) | M_PV(s=4) cancels (mult.-norm.-cancellation) |
| Residual after cancellation | lab ratio `SC_A/SC_B` | substrate kernel `Var_a` curvature |
| Vanishing test | **FAIL** (`R_BdG → 0` at `SC_A=SC_B`) | **PASS** (no lab leg; substrate residual) |
| Level-3 anchor | Track-B (lab-injected, `rel_match=0.0` tautology) | Track-A (substrate-committed, `−7.046336`) |
| Registry status | `REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION` | `STAGE-3-PERMANENT` |

The two gates do not disagree — they adjudicate two observables of genuinely different substrate-commitment. Applying the vanishing test to BOTH yields exactly the status each already carries. The "different credentials, no cross-check" concern is resolved: this synthesis IS the cross-check, and it returns COHERENT. Note the team-lead's "Corner-III" label for §VII.AV is the algebra-DEPENDENT row shorthand; §VII.AV is precisely **Cell-IV** (DEPENDENT × s=4), §VII.AJ is **Corner-III** (DEPENDENT × s=3). Distinct poles ⇒ cross-pole co-primary FORBIDDEN regardless; the two are correctly credentialed as independent slots in the same algebra-DEPENDENT family.

### Result 6 — The necessary-not-sufficient axis (functional-sensitivity)

**Result**: the vanishing test is a ONE-axis gate (substrate-vs-lab). Track-A registry-PASS requires a SECOND, orthogonal axis (regulator/functional FI vs SD), which the vanishing test does not probe. SCHEME-DEPENDENT magnitude flagged.

The W7 workshop itself recognized this by pairing G1 (vanishing / substrate-commitment) with G2 (gap-localization / regulator-flatness) in its composite CF-S117 gate (W7 line 464-467). For §VII.AV:

- **G1 (substrate-commitment)**: clean PASS (Results 2-3).
- **G2 — L_max leg**: PASS by structural identity. The `MULTIPLICATIVE-NORMALIZATION-CANCELLATION` makes `L_emp` L_max-invariant — but per my own `math-scripts.md` K=3 rule, this is a STRUCTURAL IDENTITY, NOT empirical regulator-class evidence; the discriminating content lives at the plateau VALUE `B(R) = −7.046`, which is regulator-class-keyed.
- **G2 — PV application-layer**: SCHEME-DEPENDENT, but adjudicated. Two FULL-PV F-images of the SAME observable exist: Reading A (s=4 spectral moment, multiplicative weight) → `−7.046`; Reading B (per-mode dispersion `E_a^{(M_j)} = √(ξ²+Δ²+M_j²)`) → `−527.97` (a 75× factor; W8 WP line 123-125). The gate PINS Reading A; the two readings were classified orthogonal F-images at S91 W4 (not a convention-shopping ambiguity — two genuinely different questions). This is settled.
- **G2 — UV-regulator-class leg (PV vs zeta vs Mellin)**: NOT YET PROBED. The existing `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION` covers the {APS-1975, Cheeger–Simons, Bismut–Cheeger} SECONDARY-CLASS axis (degree-0 ∧ sign-blind, FORCED-PASS-expected — W8 WP line 184-187). That is a DIFFERENT axis from the UV-regulator class per the `regulator-pin-discipline.md` 4-axis orthogonality. Whether a zeta-functional or Mellin-functional plateau `B(R)` reproduces `−7.046` is the open FI/SD question (Result in §V).

So §VII.AV's STAGE-3-PERMANENT rests soundly on Level-1 identity + G1 substrate-commitment + Level-2 L_max-binding + the Reading-A/B layer adjudication. The regulator-class FI status of the `−7.046` magnitude is the residual completeness item — a functional-sensitivity flag, not a defect in the landing.

---

## III. Gate Verdicts (cross-check, not re-adjudication — source verdicts authoritative)

| Gate | Verdict (source) | Decisive Number | Vanishing-test status (this cross-check) |
|:-----|:-----------------|:----------------|:-----------------------------------------|
| `S116-W7-STATEPROJ-BCS` | INFO (Track-B) | `R_STATE = +0.0353559` = `R_3HeB_lit` (rel_match 0.0) | FAIL — lab `SC_A/SC_B` residual; HELD, correct |
| `S116-W8-FWDC2-LANDING` | PASS (Track-A) | `L_emp = −7.046336 M_KK²` (rel 7.33e-11) | **PASS** — substrate kernel residual; STAGE-3-PERMANENT, correct |
| W7 algebra-axis workshop | ORTHOGONAL, level-separated (artifact) | — | mints the test; §VII.AV confirms its generality |

---

## IV. Structural Implications

**Resolution: (a)-with-refinement.** The two STATE-PROJ instances ARE coherently credentialed under one consistent gate. The vanishing test is GENERAL across the algebra-DEPENDENT STATE-PROJ family as a *substrate-commitment* (Track-A/B) discriminator; §VII.AV PASSES it, §VII.AJ FAILS it, and W8's machinery agrees with W7's by construction. This is NOT resolution (b) in the strong sense ("the test is A/B-specific and does not generalize") — the test's DEEP content (provenance of the residual after the scale-cancellation) generalizes cleanly. What is A/B-specific is only the canonical OPERATIONAL FORM.

**Scope statement on the vanishing test's generality:**

1. **The deep content is general; the `SC_A = SC_B` operational form is the A/B-coexistence specialization.** The general gate reads: *zero every laboratory-IN / cross-vacuum-contrast parameter; the observable PASSES iff it remains nonzero with the residual sourced by substrate quantities.* For a cross-vacuum A/B observable (§VII.AJ), the lab parameter is the `SC_A/SC_B` split and the limit `SC_A → SC_B` zeroes the observable (FAIL). For a single-vacuum intrinsic-dispersion observable (§VII.AV), there is NO lab-contrast parameter, the limit is a no-op, and the substrate-intrinsic differentiation (the 8-mode variance) is NEVER zeroed (volovik's R3 §3 limit-definition pin: "the vanishing limit sets all laboratory-IN parameters to their symmetric point, never the substrate-intrinsic differentiation" — W7 line 310). PASS trivially.

2. **The test is NECESSARY-not-SUFFICIENT for Track-A registry-PASS; G2 (regulator-flatness) is the orthogonal axis.** Substrate-commitment (the vanishing test, G1) and regulator/functional-invariance (G2, the FI/SD axis) are independent. A vanishing-PASS observable can still carry a SCHEME-DEPENDENT magnitude. The W7 composite gate G1 ∧ G2 already encodes this; the standing form of the Corner-III/IV STATE-PROJ Track-A gate should keep both axes explicit. §VII.AV has G1 (clean) + G2's L_max-leg (structural identity) + G2's PV-layer (adjudicated) + G2's UV-regulator-class leg (open, §V).

**What this opens / closes / shifts:**
- CLOSES the coherence concern: §VII.AJ-vs-§VII.AV is not a same-session inconsistency. The vanishing test is the common gate; the status asymmetry is its correct output.
- OPENS a clean methodology generalization (Q2-class, route to housekeeping, not a compute): register the vanishing test as the standing **G1** axis of the Corner-III/IV STATE-PROJ Track-A gate in `cross-pillar-bridge-anatomy.md`, paired with G2 (regulator-flatness) per the 4-axis `regulator-pin-discipline.md` orthogonality. The two same-session instances are the K=1/K=2 calibration corpus (§VII.AJ = FAIL exemplar; §VII.AV = PASS exemplar).
- SHIFTS §VII.AV's open residual into sharp focus: not its substrate-commitment (settled PASS) but the UV-regulator-class FI/SD status of its `−7.046` plateau.

---

## V. Carry-Forward Computations

### V.1 — UV-regulator-class FI/SD determination of `L_emp = −7.046336 M_KK²`

- **What**: Recompute the FWD-C2 substrate-IS observable `L_emp = d²ln Var_a(|v_a(K)|²)/d(ln K)²` at the s=4 pole under TWO alternative spectral functionals to the pinned Pauli–Villars one — the zeta functional `S_zeta = ζ_D(0) = a_4` weighting, and a sharp-Mellin-cone weighting — and compare each plateau `B(R)` against the PV value `−7.046336`. Classify FUNCTIONAL-INDEPENDENT (all three plateaus agree within rel ≤ 0.05 ⇒ the s=4-spectral-moment weight is multiplicative and cancels in every regulator class, strengthening §VII.AV beyond the vanishing-PASS) vs SCHEME-DEPENDENT (the zeta/Mellin plateau differs ⇒ `−7.046` carries a regulator-class qualifier and the Track-A magnitude must be tagged `a_4^{<class>}`). Per my `math-scripts.md` K=3 rule the EXPECTATION is regulator-class-keyed (SD), so this is an EVOI-positive test, not a foregone confirmation.
- **Inputs**: the 8 s52 Bogoliubov amplitudes `|v_a(K)|²` (B2×4,B1,B3×3) over the K-window [0.95,1.05]K_h; `Var_a` kernel reproduction (`L_emp_kernel = −7.046336474406`, W8 npz); the zeta s=4 spectral-support weight (substrate, no lab input); the Mellin-cone s=4 residue weight (`poleconv-A-double`, `pole_in_s=4`, `curvature_grade_n=0`); `Δ_BCS = 0.46425 M_KK` (canonical); `from canonical_constants import *` incl. `L_emp_VII_AV_STATE_PROJ`.
- **Gate**: new `S117-FWDC2-LEMP-REGULATOR-CLASS-FISD` — PASS(FI) iff `max|B(R_zeta), B(R_Mellin) − (−7.046336)| / 7.046336 ≤ 0.05` AND each alternative weight is verified K-independent (so `d²/d(lnK)²` annihilates it, mirroring the PV multiplicative-cancellation); FAIL(SD) iff any plateau differs by > 0.05 ⇒ re-tag §VII.AV Level-3 anchor with its regulator-class suffix. Closes the UV-regulator-class leg of the W7 G2 gap-localization that `CF-S117-FWDC2-LEMP-BULKGAP-PROTECTION` (secondary-class {APS,CS,BC} axis) does NOT cover — orthogonal axes per `regulator-pin-discipline.md`.
- **Effort**: ~2 hours, 1 agent session (no eigensolve; K-window log-derivatives + two alternative spectral-moment weight sums on the existing caches, the same cost profile as the W8-2 compute).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | §VII.AV is `Var_a` curvature over 8 substrate BdG modes — NOT an A/B contrast | PHONONIC | Confirmed (W8 line 116) | structural basis for the PASS |
| 2 | All 3 flagged legs clean (PV cancels, Casimir discharged, s52 substrate) | GEOMETRIC | FUNCTIONAL-INDEPENDENT | no lab/canonical injection |
| 3 | §VII.AV PASSES the vanishing test (trivial + deep-diagnostic) | PHONONIC | PASS | substrate-committed |
| 4 | §VII.AV realizes the W7 inter-summand-reframe genus | PHONONIC | Structural correspondence | inter-summand Track-A route validated by a sibling slot |
| 5 | W7 vanishing test ≡ W8 substrate-natural-binding (coherence) | — | CONFIRMED | no same-session inconsistency; status asymmetry correct |
| 6 | Vanishing test = G1 only; G2 (regulator FI/SD) orthogonal, `−7.046` is `B(R)` regulator-class-keyed | GEOMETRIC | SCHEME-DEPENDENT (open) | necessary-not-sufficient; UV-regulator leg → CF V.1 |

**Verdict in one line**: §VII.AV.STATE-PROJ PASSES the W7 vanishing test on the substrate-commitment axis — the two STATE-PROJ instances are coherently credentialed under one consistent gate (resolution (a)); the test generalizes via its residual-provenance content (the `SC_A=SC_B` form is the A/B specialization) and is necessary-not-sufficient for Track-A, with the orthogonal regulator-class FI/SD status of `L_emp = −7.046` the one genuine carry-forward.
