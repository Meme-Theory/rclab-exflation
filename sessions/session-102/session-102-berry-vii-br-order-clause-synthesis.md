# Session 102 Synthesis: §VII.BR Release-condition-R Order-Clause Reconciliation — W7-3 O(ε²) WZ-Holonomy vs the "O(ε) anisotropy" Theorem Text

**Date**: 2026-06-10
**Agent**: berry-geometric-phase-theorist (Berry-Geometric-Phase-Theorist)
**Source Documents**:
- `sessions/session-102/session-102-w7-workingpaper.md` (§W7-3 in full; Wave-7 synthesis)
- `sessions/permanent-results-registry.md` §VII.BR (lines 21290–21361; Release-condition-R at line 21336)
- `.claude/agent-memory/berry-geometric-phase-theorist/MEMORY.md`
- `computations/session-102/s102_w7_b2_eps2_wz_holonomy.npz` (60 keys; audit `f7ba23e1…`)
- `computations/session-101/s101_w5_4_b2_isotropy_breaking.npz` (upstream W5-4; audit `13617ab9…`)
- knowledge MCP: gate `S101-B2-ISOTROPY-BREAKING` (INFO), §VII.BR theorem trace

---

## I. Session Outcome

**Reading (B) wins, sharpened.** The §VII.BR Release-condition-R "O(ε) anisotropy" clause and the W7-3 "O(ε²) closed-loop holonomy" measure **structurally different geometric objects** that cannot share an ε-order, so there is no contradiction — but the clause as currently worded conflates three distinct quantities under one order-label and needs a curated disambiguation patch. The decisive fact, found by re-reading the upstream W5-4 npz: the **band-matrix anisotropy itself** (`b2_split`, the very object the clause names) was **already** measured at **O(ε²), slope 1.99999, with C₁=0 EXACT** in W5-4 — the order-mismatch is NOT introduced by W7-3's holonomy; it lives in the anisotropy measurement the theorem directly describes. Symbolic perturbation theory (Sage, below) proves C₁=0 is **structural, not fine-tuned**: the (λ₄,λ₆) coset directions are **off-block**, off-block operators have no in-band first-order matrix element (P·δH·P ≡ 0), so the leading anisotropy is the second-order Schur-complement term ∝ε². This **refutes Reading (A)** ("non-generic measure-zero vanishing of an O(ε) term"): the vanishing is generic across the entire off-block coset, which is the substrate-natural deformation class the theorem text itself names (the λ₄..λ₇ coset carrying 94.8% of the Level-1 metric content). This is a **clean disambiguation, NOT an adversarial-derivation defect** — no Slot-2 berry-vs-independent workshop is required (escalation criterion NOT met; reasoning in §IV).

**Gate verdicts are authoritative and untouched**: W7-3 PASS-Track-A (`f_WZ=2.889e-6`, frame-invariance residual 1.776e-15) and W5-4 INFO (slope-2 DEGENERATE-FIRST-ORDER) both stand. This synthesis reconciles the registry *theorem text*, not any verdict.

---

## II. Key Results

### II.1 The order-mismatch predates W7-3: W5-4's band-anisotropy is already O(ε²)

**Result**: `b2_split_slope = 1.99999` with C₁=0 EXACT (W5-4 npz); the Release-condition-R clause names *this* object. **GEOMETRIC.**

§VII.BR Release-condition-R (registry line 21336) states verbatim:

> "…for generic δH the band-matrix develops anisotropy at O(ε) **iff** genuine within-band Wilczek–Zee structure exists."

The "band-matrix" is `M_ab|_ran P` (E5, line 21318) — the within-band geometry tensor. Its anisotropy is precisely what W5-4 measured as `b2_split` (the eigenvalue splitting within the exactly-degenerate B2 quadruplet under the (λ₄,λ₆) deformation):

```
eps_scan   = [1.0e-4,   3.16e-4,  1.0e-3,   3.16e-3,  1.0e-2 ]
b2_split   = [1.36e-9,  1.36e-8,  1.36e-7,  1.36e-6,  1.36e-5]
b2_split_slope = 1.99999   (log-log)   ⟹   anisotropy ∝ ε²,  C₁ = 0 EXACTLY
slope_reading  = "DEGENERATE-FIRST-ORDER-C1zero-C2nonzero-slope2-INFO"
```

The clause says the band-matrix anisotropy onsets at **O(ε)**. The substrate realization onsets at **O(ε²)**. This mismatch is **independent of W7-3** — it is already present in the W5-4 anisotropy measurement of the object the clause directly names. W7-3 inherits the same slope (its `slope_angle = 1.99989 ≈ 2`) because the holonomy angle and the band-anisotropy are driven by the same second-order off-block mechanism. The Wave-7 synthesis correctly reconciled **Corollary U** (undecidability on the U(2)-INVARIANT base, registry line 21332) but did **not** address this Release-condition-R order clause; that gap is the focus of this synthesis.

### II.2 Why C₁=0 is STRUCTURAL (off-block), not fine-tuned — Reading (A) refuted

**Result**: P·δH·P ≡ 0 for any off-block δH ⟹ leading in-band anisotropy = 2nd-order Schur complement ∝ ε². **GEOMETRIC.**

The crux distinguishing Readings (A) and (B) is whether C₁=0 in the (λ₄,λ₆) coset is a *measure-zero / symmetry-protected* accident (Reading A: theorem's "generic δH" clause excludes it) or a *structural property of the entire off-block coset* (Reading B: the O(ε) term is generically absent for off-block deformations). Degenerate perturbation theory settles this. For a band ran P that is exactly degenerate, the leading in-band effective operator is the first-order projection P·δH·P. The (λ₄,λ₆) directions are **off-block**: they connect the B2 isotypic block to *other* isotypic blocks (this is exactly why they "carry 94.8% of the Level-1 metric content" — they are the C² coset generators, off-diagonal in the Peter-Weyl block structure E1). An off-block operator has **no in-band diagonal matrix element**, so:

```
P · δH_off-block · P  ≡  0      (structural — not fine-tuning)
```

Hence the first-order in-band correction vanishes identically, and the leading band-matrix anisotropy is the **second-order Schur-complement (Löwdin) term**. Sage symbolic verification (3×3 model: two degenerate band states at 0, one remote block at Δ, off-block coupling amplitudes a, b for the two coset directions):

```
H = [[0, 0, ε·a], [0, 0, ε·b], [ε·a, ε·b, Δ]]
H_eff(2nd order, in-band) = −(ε²/Δ) · [[a², a·b], [a·b, b²]]
eigenvalues = [ −(a²+b²)ε²/Δ ,  0 ]
⟹  in-band splitting (anisotropy) = −(a²+b²)·ε²/Δ      [∝ ε², GENERIC in a,b]
```

The splitting is O(ε²) for **generic** off-block amplitudes (a,b) — not measure-zero. The vanishing of the O(ε) term is forced by off-block-ness, a property of the *whole* coset class, which is the substrate-natural deformation family the theorem itself nominates. **Reading (A) is therefore false**: (λ₄,λ₆) is not a non-generic choice the "generic δH" clause excludes; it is a representative of the generic off-block class, and the generic off-block class onsets at O(ε²).

The contrast case confirms the theorem's discriminator content is still correct for the *other* (in-block) deformation class:

```
In-block anisotropic δH (P·δH·P = diag(+1,−1), a genuine within-band non-Schur-scalar):
   in-band eigenvalues = [−ε, +ε]   ⟹   splitting = −2ε   [O(ε), slope 1]
```

So an *in-block* deformation that carries genuine within-band anisotropy (non-Schur-scalar P·δH·P) DOES split the band at O(ε). The theorem's "anisotropy at O(ε) iff WZ structure" is correct **for the in-block linear-response class**. It is the order-label, applied indiscriminately to the off-block class, that is wrong.

### II.3 The closed-loop holonomy is intrinsically O(ε²) by Stokes — a third, distinct object

**Result**: `hol_angle ∝ loop-area ∝ ε²` (W7-3 `slope_angle=1.99989`); abelian-or-non-abelian-independent. **GEOMETRIC.**

W7-3's witness is not the band-matrix anisotropy at all — it is the **Wilczek–Zee link-product holonomy** around the *closed* loop θ∈[0,2π] that rotates the deformation *direction* in the (λ₄,λ₆) plane:

```
H(θ) = H₀ + ε·(cos θ · dH₄ + sin θ · dH₆),   H(2π)=H(0) exactly (closed loop).
U_hol = ∏ₖ (F_{k+1}† Fₖ)  (band frames),   f_WZ = |Tr U_hol − 4|.
```

By Stokes, the holonomy angle is the **curvature flux through the area enclosed by the loop**. The loop is a circle of radius ε in deformation-amplitude space, so its enclosed area ∝ ε². The non-abelian Berry connection A_a is O(ε) (off-block matrix element over the gap, first order), and the curvature flux through an O(ε²) area gives:

```
ang(U_hol) = ∮ A = ∬ F  ~  (curvature) × (loop area ~ π ε²)  ⟹  O(ε²), slope 2.
```

This O(ε²) scaling is a **geometric property of any closed loop of radius ε** — it holds whether the connection is abelian or non-abelian (a U(1) Berry phase around the same loop would also be O(ε²)). The W7-3 numbers confirm: `slope_angle=1.99989≈2` (curvature flux), `slope_wz=3.99972≈4` (the witness f_WZ = ½·angle² is the trace deviation, hence O(ε⁴)). The DISCRIMINATING content of W7-3 is **not** the ε-order (which is geometrically fixed at 2) but the **frame-invariant non-scalar content**: `non_scalar_frac = 1.0000` (the commutator [A₄,A₆] is maximally non-Schur-scalar) and `n_broken = 4/4` (the loop fully breaks U(2)). Those are what certify genuine Wilczek–Zee structure (Track A), independent of the order.

**The three objects, ranked by ε-order:**

| Object | What it is | Class | ε-order | Source |
|:-------|:-----------|:------|:--------|:-------|
| In-block within-band splitting | `P·δH·P` non-Schur-scalar (open linear response) | in-block | **O(ε)** slope 1 | theorem's literal "O(ε) iff WZ" |
| Off-block band-matrix anisotropy | 2nd-order Schur-complement splitting | off-block | **O(ε²)** slope 2 | W5-4 `b2_split`, C₁=0 EXACT |
| Closed-loop WZ holonomy angle | curvature flux through loop area | closed loop | **O(ε²)** slope 2 | W7-3 `hol_angle` slope 1.9999 |

The theorem text names the first; the substrate realizes the second and third. They are different geometric objects, so they need not — and structurally cannot — share an order.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W7-3 `CF-S102-B2-EPS2-WZ-HOLONOMY` | **PASS — Track A** | `f_WZ=2.888785e-06`; frame-invariance residual `1.776e-15`; `slope_angle=1.99989`; `non_scalar_frac=1.0000`; `n_broken=4/4` |
| W5-4 `S101-B2-ISOTROPY-BREAKING` (upstream) | **INFO** (DEGENERATE-FIRST-ORDER) | `b2_split_slope=1.99999`; C₁=0 EXACT; priors UNCHANGED 0.6B/0.4A |
| §VII.BR Schur-Rigidity complex | **STAGE-3-PERMANENT** (T1/T2/P/U/R; not re-adjudicated) | T2 Schur-scalar witness ≈1e-13; Corollary U intact |

These verdicts are authoritative per the source docs and are **not** re-adjudicated here. The reconciliation is of the registry *theorem prose* (Release-condition-R order label), not of any verdict.

---

## IV. Structural Implications

### IV.1 The chosen reading, PINNED

> **PINNED READING (B), sharpened.** §VII.BR Release-condition-R's "band-matrix develops anisotropy at O(ε) iff genuine within-band Wilczek–Zee structure exists" is the correct **in-block linear-response discriminator** (an *in-block* δH with non-Schur-scalar P·δH·P splits the band at O(ε), Sage-confirmed). It is realized at **O(ε²)** by the substrate-natural **off-block** coset directions (λ₄..λ₇), because off-block-ness forces P·δH·P≡0 and pushes the leading anisotropy to the second-order Schur complement (∝ε², generic). The **closed-loop Wilson-loop holonomy** (W7-3) is a **separate** object whose O(ε²) order is fixed by Stokes (curvature flux ∝ loop-area ∝ ε²), independent of abelian/non-abelian character. The theorem and the gate measure **different objects**; no contradiction exists. The clause text needs an explicit **O(ε)-in-block-anisotropy vs O(ε²)-off-block / O(ε²)-closed-loop-holonomy disambiguation** so downstream consumers (CF-S103-B2-ISOBREAK-REGISTRY-LANDING) do not inherit the order-mismatch.

This pin lets CF-S103-B2-ISOBREAK-REGISTRY-LANDING land a *reconciled* "Release-condition-R companion of Corollary U" claim: W7-3 is a **legitimate** discriminator R licenses (it breaks U(2), n_broken=4/4, and exhibits frame-invariant non-scalar holonomy), but it discriminates via the **frame-invariant non-scalar content** (`non_scalar_frac=1`), **not** via an O(ε) anisotropy — because the substrate-natural off-block class has no O(ε) anisotropy to exhibit. The companion entry must state the discriminator is the **closed-loop frame-invariant non-Schur-scalar holonomy at O(ε²)**, not the literal "O(ε) band-matrix anisotropy."

### IV.2 Why this is a disambiguation, NOT an adversarial defect (escalation criterion NOT met)

The escalation clause asks whether the order-mismatch is a genuine STAGE-3-PERMANENT-theorem-text DEFECT requiring a berry-vs-independent ADVERSARIAL derivation. It is **not**, for three reasons:

1. **The perturbation theory is unambiguous and single-valued.** Off-block ⟹ P·δH·P≡0 ⟹ O(ε²) is elementary degenerate PT (Löwdin / Schur complement), confirmed symbolically with no free interpretive choice. There is no competing first-principles derivation that yields O(ε) for an off-block deformation — Reading (A) is not a defensible alternative derivation, it is a misreading of "generic" (it treats off-block C₁=0 as fine-tuned when it is structural). An adversarial workshop adjudicates between *two defensible competing derivations*; here there is one correct derivation and one refuted misreading.

2. **The theorem's discriminator logic is preserved intact.** "Anisotropy iff WZ structure" remains true for the in-block class. The patch does not weaken, strengthen, or invert any clause — it disambiguates which deformation class the O(ε) label applies to. Per `cross-pillar-bridge-anatomy.md` substrate-first framing and `capstone-hygiene-gate.md`, a status/scope clarification that preserves the explanation direction is a curated-doc reviewed edit, not a re-derivation.

3. **No verdict or numerical result changes.** W5-4 INFO and W7-3 PASS-Track-A stand exactly. Only the registry prose's order-label gains a class qualifier. This is the `Investigating-Workshops.md` Q2 marker class (a theorem-text scope edit / curated-doc reviewed patch), explicitly **NOT** a Q1 math/physics adjudication (there is no genuine ledger-dissonance between two competing readings of an observable — one reading is refuted by elementary PT).

**Conclusion: route as a curated §VII.BR theorem-text disambiguation patch (designated sole-writer reviewed edit), NOT a Slot-2 workshop.** The patch recommendation is in §IV.3; it is a recommendation FOR the sole-writer, not a direct edit by this synthesis (per the task rules and `feedback_framework-hygiene.md` no-bulk-append discipline).

### IV.3 Recommended §VII.BR Release-condition-R patch (FOR the sole-writer; reviewed curated edit)

The patch is a **minimal class-qualifier insertion** into the Release-condition-R paragraph (registry line 21336). It does NOT touch T1, T2, P, U, the numerical-witness table, the lineage caveat, or the clause attribution. Recommended replacement of the single sentence

> "…and for generic δH the band-matrix develops anisotropy at O(ε) **iff** genuine within-band Wilczek–Zee structure exists."

with (substrate-first, order-disambiguated):

> "…and the band-matrix develops anisotropy **iff** genuine within-band Wilczek–Zee structure exists; **the onset ORDER in ε is set by the deformation class** — an *in-block* δH carrying a non-Schur-scalar in-band part P·δH·P splits the band at **O(ε)** (open linear response), whereas an *off-block* δH (the substrate-natural C²-coset directions λ₄..λ₇, for which P·δH·P ≡ 0 because off-block operators have no in-band first-order matrix element) develops its anisotropy at **O(ε²)** via the second-order Schur-complement term (generic in the coset amplitudes; C₁=0 is STRUCTURAL, not fine-tuned). The **closed-loop** Wilczek–Zee holonomy ∮A_coset around a coset loop of radius ε is a DISTINCT object whose **O(ε²)** order is fixed by Stokes (curvature flux ∝ enclosed loop-area ∝ ε²), independent of abelian/non-abelian character; its discriminating content for genuine WZ structure is the **frame-invariant non-Schur-scalar trace** (non_scalar_frac → 1), not the ε-order. The substrate's off-block realization (forward gate CF-S101-B2-ISOTROPY-BREAKING → S102 W7-3) therefore confirms genuine WZ structure at O(ε²) on the released base, with no contradiction to the O(ε) in-block statement."

Supporting cross-reference to add to the numerical-witness lineage: W5-4 `b2_split_slope=1.99999` (C₁=0 EXACT) and W7-3 `slope_angle=1.99989`, `f_WZ=2.888785e-06` frame-invariant to `1.776e-15`. This insertion is consistent with the existing "(forward gate CF-S101-B2-ISOTROPY-BREAKING, §V.1)" pointer already in the clause — it simply records the *outcome* of that forward gate and disambiguates the order. Per the `capstone-hygiene-gate.md` 5-question discipline this is a Q3-class prose status reconciliation (a STAGE-3-PERMANENT clause's confidence is unchanged; only its order-scope is sharpened) — route to the §VII.BR designated writer as an in-session reviewed patch, NOT a bulk append. **Note**: §VII.BR carries the MANDATORY lineage caveat (LC-lineage-conditional numbers); the patch text above adds NO new LC-conditional number to the operator-independent clauses — the O(ε)-vs-O(ε²) order distinction is an operator-INDEPENDENT consequence of off-block-ness + degenerate PT (it "transfers as-is under either branch of the τ=0 canonicity adjudication," exactly like T1/T2/P/U/R), so it belongs with the operator-independent body, not the LC-conditional witness table.

### IV.4 Constraint-map effect

| Item | Prior state | New state | Reason |
|:-----|:------------|:----------|:-------|
| §VII.BR Release-condition-R order clause | "O(ε) anisotropy" (un-disambiguated; would be inherited as order-mismatch by CF-S103 landing) | **Reading (B) PINNED, sharpened** — in-block O(ε) / off-block O(ε²) / closed-loop O(ε²); patch recommended to sole-writer | Off-block ⟹ P·δH·P≡0 (Sage-confirmed); W5-4 `b2_split` already O(ε²) with C₁=0 EXACT |
| Reading (A) "non-generic measure-zero O(ε)" | candidate reading | **REFUTED** | C₁=0 is structural (off-block), generic across the coset, not symmetry-protected fine-tuning |
| CF-S103-B2-ISOBREAK-REGISTRY-LANDING companion claim | would land "as Release-condition-R companion" inheriting O(ε) mismatch | **lands reconciled** — discriminator is the O(ε²) frame-invariant non-scalar holonomy, not O(ε) anisotropy | This synthesis pins the reconciled statement |
| Slot-2 berry-vs-independent workshop | possible escalation | **NOT triggered** | unambiguous single-valued PT; disambiguation not adversarial adjudication (§IV.2) |

This sharpens — does not weaken — §VII.BR. The Schur-rigidity no-go complex (T1/T2/P/U) is untouched; Corollary U's undecidability-on-the-invariant-base is intact (the Wave-7 synthesis already reconciled it); Release-condition-R is upgraded from an order-ambiguous discriminator to a class-resolved one. The substrate's (1,1)-fiber B2 band genuinely breaks U(2) isotropy with frame-invariant Wilczek–Zee holonomy once the Schur lock is released — exactly where §VII.BR placed the protection boundary — and the order at which it does so (O(ε²) for the substrate-natural off-block class) is now correctly recorded.

### IV.5 Memory-consistency note (S25 Ω=0)

The W7-3 result is fully consistent with this agent's PERMANENT S25 erratum (`MEMORY.md`: Berry curvature = Im(QGT) = 0 IDENTICALLY on the closed SU(3) structure). W7-3's `abel_phase = 8.9e-16 ≈ 0` (the U(1) det-holonomy is trivial) reproduces Ω=0 exactly. The non-trivial holonomy is **pure SU(4) non-abelian** (Wilczek–Zee), which is NOT the abelian Berry curvature S25 nulls — it lives in the off-diagonal non-abelian connection released only when U(2) is broken (consistent with the S61 "SU(3)→SU(2) phases emerge from C² cross-terms via [A^{C²},A^{C²}]" mechanism: here the C² coset cross-terms [A₄,A₆] carry the holonomy, `non_scalar_frac=1`). No update to the S25 PERMANENT entry is needed; the W7-3 finding extends, not contradicts, it. The MEMORY note "CKH discrimination needs isotropy-BREAKING deformations" (S100b row) is now CONFIRMED with a frame-invariant witness on the broken base.

---

## V. Carry-Forward Computations

V.1. **§VII.BR Release-condition-R disambiguation patch landing (NON-MATH; routed in-session as recommendation)**
   - **What**: the §VII.BR sole-writer applies the reviewed prose patch of §IV.3 (insert the in-block-O(ε) / off-block-O(ε²) / closed-loop-O(ε²) class qualifier into the Release-condition-R sentence at registry line 21336; add the W5-4/W7-3 outcome cross-reference). Curated designated-writer reviewed edit, NOT a bulk append; the patch carries NO new LC-lineage-conditional number (operator-independent order distinction).
   - **Inputs**: this synthesis §IV.3 (verbatim patch text); `sessions/permanent-results-registry.md` §VII.BR (line 21336); W5-4 npz (`b2_split_slope`, audit `13617ab9…`); W7-3 npz (`slope_angle`, `f_WZ`, `frame_resid`, audit `f7ba23e1…`).
   - **Gate**: feeds **CF-S103-B2-ISOBREAK-REGISTRY-LANDING** (housekeeping §B) — the companion entry's "Release-condition-R companion of Corollary U" claim cites the disambiguated clause and states the discriminator as the O(ε²) frame-invariant non-scalar holonomy. PASS = patch present in §VII.BR with the order-class qualifier + the companion landing cites the reconciled clause (artifact-existence + content-marker, METHODOLOGY-class curated-doc edit).
   - **Effort**: 0.25 gate (single reviewed sentence patch by the §VII.BR sole-writer; no compute). Effected as a recommendation here per task rules (this synthesis writes ONLY its own file); the actual registry edit is the sole-writer's in-session action.

V.2. **Second coset-doublet WZ-holonomy probe (MATH; S103 compute)**
   - **What**: repeat the W7-3 frame-invariant Wilson-loop holonomy on the **orthogonal off-block C² coset doublet** (array indices [3,5], the npz `next_pair=[3 5]`), completing the C² coset span (λ₄..λ₇). Measure `f_WZ`, `slope_angle`, `non_scalar_frac`, `frame_resid` on that loop; test whether the second doublet carries the same non-trivial O(ε²) WZ holonomy (would strengthen Track A from one coset plane to the full C² coset).
   - **Inputs**: `computations/session-102/s102_w7_b2_eps2_wz_holonomy.py` (the W7-3 driver; re-parametrize the coset pair to [3,5]); `dirac_spectrum.py` (SHA `dadba674…`); `s101_w5_4_b2_isotropy_breaking.npz` (off-block log-metric directions); `canonical_constants.py` (`tau_fold=0.19`).
   - **Gate**: new `S103-B2-WZ-HOLONOMY-COSET2` — PASS iff `frame_resid < 1e-10` (precondition) AND `f_WZ > eps_WZ=1e-8` (Track-A confirm on the second doublet) AND `slope_angle ∈ [1.8, 2.2]` (O(ε²) consistency); INFO if `f_WZ` converges but `< 1e-8` (second doublet Schur-protected even on broken base); FAIL if `frame_resid ≥ 1e-10` (frame-dependent — rebuild). Companion-strengthens CF-S103-B2-ISOBREAK-REGISTRY-LANDING.
   - **Effort**: 0.5 gate, 1 agent session (re-parametrized re-run of an existing validated driver; no new machinery).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Order-mismatch predates W7-3: W5-4 `b2_split` (the named band-matrix anisotropy) is already O(ε²), C₁=0 EXACT | GEOMETRIC | Established (W5-4 npz) | The clause's "O(ε)" mis-labels the substrate's off-block realization; not a W7-3 artifact |
| 2 | C₁=0 is STRUCTURAL (off-block ⟹ P·δH·P≡0), generic in the coset; Reading (A) "measure-zero" REFUTED | GEOMETRIC | Sage-confirmed | Reading (B) wins; the O(ε) term is generically absent for the substrate-natural off-block class |
| 3 | Three distinct objects: in-block O(ε) / off-block-anisotropy O(ε²) / closed-loop holonomy O(ε²) | GEOMETRIC | Sage-confirmed | Theorem (object 1) and gate (object 3) measure different objects ⟹ no contradiction |
| 4 | Closed-loop WZ holonomy O(ε²) by Stokes (flux ∝ loop-area ∝ ε²), abelian/non-abelian-independent | GEOMETRIC | Sage-confirmed | W7-3's discriminator is `non_scalar_frac=1` + frame-invariance, NOT the ε-order |
| 5 | Disambiguation, NOT adversarial defect — Slot-2 workshop NOT triggered | METHODOLOGY | Pinned (§IV.2) | Route as curated §VII.BR sole-writer reviewed patch (Q2-class), recommended in §IV.3 |
| 6 | Reading (B) PINNED, sharpened; CF-S103 landing inherits reconciled claim | GEOMETRIC | Pinned (§IV.1) | CF-S103-B2-ISOBREAK lands "Release-condition-R companion" with O(ε²) frame-invariant-non-scalar discriminator |
| 7 | W7-3 consistent with PERMANENT S25 Ω=0 (abelian phase ≈0; holonomy pure SU(4) non-abelian) | GEOMETRIC | Confirmed (§IV.5) | No S25 update; extends the S61 C²-cross-term mechanism; CKH-needs-isotropy-breaking now witnessed |

---

**Files written**: this synthesis only (`sessions/session-102/session-102-berry-vii-br-order-clause-synthesis.md`). No registry edit performed by this agent — the §VII.BR patch is a recommendation FOR the sole-writer (§IV.3 + V.1) per the task rules. No new canonical constants minted (no new framework prediction value; the order-class distinction is structural, not a numerical pin).
