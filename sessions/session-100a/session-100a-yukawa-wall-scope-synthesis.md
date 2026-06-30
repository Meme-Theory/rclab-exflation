# Session 100a Synthesis: W5-1 Yukawa-Shape Wall — Corridor-Status Adjudication (Scale Wall vs Shape Corridor)

**Date**: 2026-06-07
**Agent**: connes-ncg-theorist (Workhorse-NCG)
**Source Documents**:
- `sessions/session-100a/session-100a-w5-workingpaper.md` (§W5-1 Results (2)/(4) + Assessment; Wave-5 Synthesis §1)
- `sessions/session-100a/session-100a-w2-workingpaper.md` (§W2-1 through §W2-4 + Wave-2 Synthesis)
- `computations/session-100a/s100a_gate_verdicts.txt` (canonical verdict lines + companion rows)
- `sessions/session-plan/session-100a-plan-w5.md` §W5-1 (dual_prior, INFO_meaning, FAIL_meaning, machinery pin)
- `computations/session-100a/s100a_md_normalization.npz` (data-artifact verification of all load-bearing numbers)
- `sessions/framework/phonic-exflation-equation.md:563` (§7.3 item-(4), S100a W5 update) + §7.2 Row #9
- Agent memory: `.claude/agent-memory/connes-ncg-theorist/s99-generation-blindness-theorem.md` (§VII.BL STAGE-3-PERMANENT)

**GRACEFUL-DEGRADE STATUS (checked on disk, 2026-06-07)**: the W-2 (counting-convention) and W-3 (envelope-carrier) workshop files under `sessions/session-100a/workshops/` exist as scaffolds only — every section reads `[NOT STARTED]`, both Workshop Verdict tables are entirely *pending*. **The not-landed branch fires**: this synthesis proceeds on the W2/W3 WP anchors alone. No pinned counting convention and no carrier reading are consumed; where either would bind, the dependence is declared explicitly (§V.1 machinery pin, conditional-consumption clause).

---

## I. Session Outcome

**Corridor-status verdict: reading (ii) — the wall is two-maps-deep — but with a load-bearing scoped strengthening on one axis.** The W5-1 wall decomposes exactly into a SCALE wall and a SHAPE wall, and the two have different breadths. The **scale wall is shape-independent** within every bottom-triple-anchored normalization (an algebraic factorization, Eq. (3) below: any map with Y₂ anchored to a bottom-triple eigenvalue fails the required absolute Yukawa by a factor ≥ 5.49 regardless of the shape function), so the capstone §7.3 item-(4) language "the Dirac-scale anchor is irreducibly EXTERNAL / S99 caveat PERMANENT" **is licensed on the scale axis** — at the pre-registered track_B-0.9 posterior grade of the plan's own INFO_meaning, with exactly one identified post-hoc escape corner queued for S101 falsification. The **shape wall, by contrast, is licensed only at the tested breadth**: eigenvalue-proportional, √C₂-graded, and (post-hoc) linear-C₂ power-law reductions of the bottom triple — i.e., O(1) low-order gradings. The framework's OWN established charged-lepton mechanism (the W3-9 exponential Casimir envelope, fit residual 2.2e-16; the W2-4 Connes-distance map m = e^{−d/ℓ}; the S99 four-lens modulus) is **not in the excluded class**, and a one-parameter widening exponential closes the required shape 2.4883 exactly while converting the gate's "not even 1-parameter" residual into an exactly-1-parameter constant rescale. The surviving map class and its pre-registered S101 gate spec are in §V.1. Gate verdicts (W5-1 INFO, track_B 0.9) are authoritative and un-touched; what this synthesis adjudicates is the BREADTH of the synthesis-level "confirmed PERMANENT" language (§IV.2).

---

## II. Key Results

### II.1 The W5-1 wall decomposed: the shape wall is the SAME Jensen-fold van-Hove compression that closed the W2 floor corridor

**Result**: shape ladder 1.0444 (MAP-A, deformed floors) < 1.5000 (MAP-B, √C₂ exact) < 2.25 (linear-C₂, post-hoc) < **2.4883 required**; MAP-A's shape is mechanistically the W2-3/W2-4 fold compression. Classification: **PARTICLE** (with GEOMETRIC mechanism content).

The substrate IS the Jensen-deformed SU(3) fiber; the three neutrino-Dirac generations are its three lowest Peter-Weyl towers (0,0) / (1,0)⊕(0,1) / (1,1) with C₂ = (0, 4/3, 3), and the gate's two pre-registered maps read the Dirac Yukawas directly off this bare sector data. The required shape (npz `shape_required`, full float64):

```
Y₃/Y₂ |_required = sqrt(m₃M₃ / m₂M₂) = 2.4882511868     (1)
```

(dimensionless; m_i the S99 light masses [eV], M_i = M_R,i·M_KK [GeV]; the gate publishes 2.4883 at 5 sig figs). Against it: MAP-A gives E₃/E₂ = 0.87297503/0.83589351 = 1.044362; MAP-B gives √(3/(4/3)) = 3/2 exactly; the WP's post-hoc linear-C₂ diagnostic gives 3/(4/3) = 9/4 = 2.25, still 9.6% short.

The cross-cluster identification (new organizational content, not in either WP): the neutrino-Dirac towers 2 and 3 ARE the charged-lepton towers (1,0) and (1,1) of the W2 cluster — the squared floors E₂² = 0.698718, E₃² = 0.762085 are bit-identical to W2-4's ω_{(1,0)}, ω_{(1,1)}. MAP-A's failed shape 1.0444 is therefore not an independent accident: it is the **same Jensen-fold van-Hove floor compression** that W2-3 isolated (chord-slope ratio 6.979380 vs Casimir-linear 1.0) and W2-4 reproduced bit-identically (W_Connes = 12.5629 = (9/5)×6.979). Equivalently: E₂/E₁ = 1.019704 = the S97 R_cross wall reproduced, and E₃/E₂ = 1.0444 is the fold-crowded (1,0)→(1,1) step. The wall ladder is therefore one mechanism seen at three gradings: deformed floors (1.044) < undeformed √Casimir (1.5) < linear Casimir (2.25) < required (2.4883). A deformed-floor EXPONENTIAL map fares worst of all: matching shape on the fold-compressed gap Δω = 0.063367 needs exponent s = ln(2.48825)/0.063367 = 14.39 — the same compression that broke the charged-lepton floor-graded widening makes deformed-floor neutrino envelopes absurdly steep. **Regime**: all statements at τ_fold = 0.19, L_max = 12 cache, exact within-block sums; the required-shape value (1) carries ≈ 0.7–1% from the oscillation-data Δm² convention spread (propagated from the W5-2 diagnostics (d1)/(d2): δS/S = ½(δm₃/m₃ + δm₂/m₂) ≈ ½(1.20% + 0.27%) ≈ 0.73% — my estimate, to be re-pinned at S101 plan-freeze).

### II.2 Scale-shape factorization: the scale wall is shape-independent (the strengthening that licenses the PERMANENT language on the scale axis)

**Result**: r₂ = Y₂^{S99}/Y_ref = 5.8477 for every gen-2-anchored map at Y_ref = E₁, independent of shape; ≥ 5.4911 over ALL bottom-triple anchors. Classification: **PARTICLE** (structural/algebraic).

Write any substrate-forward map in gen-2-anchored form, G an arbitrary positive shape function of any sector data x_i (eigenvalues, Casimirs, floors, block traces — anything):

```
Y_i = Y_ref · G(x_i)/G(x₂),    Y_ref = E₁ (substrate-natural, zero external input)     (2)
```

Then Y₂ = Y_ref identically, and the required gen-2 rescale is an algebraic invariant of the anchoring alone:

```
r₂ = Y₂^{S99}/Y_ref = 4.79356602/0.8197411121 = 5.8477   (= npz pergen_rescale_B[0] exactly)     (3)
```

with min over all three bottom-triple anchor choices r₂ ≥ 4.79356602/0.87297503 = 5.4911. **No shape function whatsoever — power-law, exponential, widening, narrowing, off-diagonal-dressed — can close the absolute-scale wall within a bottom-triple-anchored normalization.** This extends the gate's two-map scale exclusion to full shape breadth within that normalization class, and it is the precise sense in which the capstone's "Dirac-scale anchor irreducibly EXTERNAL" holds beyond the two tested maps. The residual escape is the UNANCHORED reading, where a large shape-function value at gen 2 absorbs scale: that family is enumerated in II.4 and leaves a ≥ 2.8× residual at every structurally-motivated corner except one flagged post-hoc edge. A second exact corollary: once the shape closes (Y₃/Y₂ matched), the per-generation rescales are equal BY CONSTRUCTION (r₃ = S·(1/S)·r₂ = r₂) — so the surviving exponential class **reduces** the gate's "residual freedom is NOT even 1-parameter" finding to "exactly 1 parameter (one constant Dirac scale)". That is a sharpening of track_B, not its removal: the one parameter remaining is precisely the external anchor the verdict names IRREDUCIBLE.

### II.3 The widening-direction derivation: the neutrino-Dirac envelope must run OPPOSITE to the charged-lepton envelope

**Result**: d ln Y^{ν_D}/dC₂ = +0.5469 required vs d ln m^{lep}/dC₂ = −S₀ = −1.6942 measured (W3-9 exact leg); opposite sign, magnitude ratio 3.0975. Classification: **PARTICLE** (discriminating structural fact).

Full substitution chain (required per `math-scripts.md` — this is a direction claim):

```
Claim: "Extending the charged-lepton exponential Casimir envelope to the neutrino Dirac
        sector requires the OPPOSITE exponent direction: Y INCREASES with C₂ along
        (0,0) → (1,0)⊕(0,1) → (1,1) (a widening), where the charged-lepton sector narrows."

Substitution chain:
  Step 1: Y_i^{req} = sqrt(2 m_i M_i)/v_ew                  [S99 seesaw back-solve; WP §W5-1 CC0]
          m^{lep}_g ∝ exp(−S₀·C₂(g)), S₀ = 1.694153 > 0     [W3-9 shape leg, resid 2.2e-16;
                                                              verdict 78ee1d5677d75dc8]
          charged assignment: τ→C₂=4/3, μ→3, e→6            [W2-2 ∧ W2-4 two-route e=(3,0)]
  Step 2: Y₂^{req} = 4.79356602 at C₂ = 4/3;  Y₃^{req} = 11.92759634 at C₂ = 3   [npz Y_S99]
          ΔY/ΔC₂ = (11.92759634 − 4.79356602)/(3 − 4/3) = 7.13403/1.66667 = +4.2804
  Step 3: d ln Y^{req}/dC₂ = ln(Y₃/Y₂)/ΔC₂ = ln(2.4882512)/(5/3)
                           = 0.9115802 × (3/5) = +0.5469481
          d ln m^{lep}/dC₂ = −S₀ = −1.694153
  Step 4: sign(+0.5469481) = +1 ;  sign(−1.694153) = −1  ⇒  OPPOSITE directions.
          |magnitude ratio| = 1.694153/0.5469481 = 3.0975.
  Conclusion: the neutrino-Dirac envelope WIDENS in C₂ where the charged-lepton envelope
          NARROWS, and at ~1/3 the slope. A single sector-universal Casimir-envelope
          exponent cannot carry both sectors; any common-mechanism extension must carry a
          sector-keyed sign flip AND a sector-keyed magnitude.
```

This is the "discriminating structural fact either way" the dispatch asked for, now quantified: it does NOT kill the exponential ε_LX class (the S99 four-lens synthesis already carries sector-dependent greybody slopes — κ_lepton 1.89 / κ_up 1.29 / κ_down 0.78 — so a fourth, sign-flipped sector value is an extension of an existing pattern, not a new species of assumption), but it DOES preclude the most economical reading in which one substrate exponent serves all Dirac sectors. Either S101 outcome is informative: a substrate-derived s_ν landing on +0.547 (or its form-equivalents below) would make the sign flip a substrate prediction; failure adds the exponential class's substrate-pinned points to the excluded set.

**Can the widening direction produce shape 2.4883 AND the ~10× scale?** Shape: YES, trivially — one free exponent matched to one ratio; the exact solution hypersurface for the family Y_i = A·(C₂,i)^q·exp(s_ν·g(C₂,i)) is

```
ln(2.4882512) = q·ln(9/4) + s_ν·Δg ,   Δg = 5/3 (g = C₂)  or  1/√3 (g = √C₂, exact)     (4)
```

(the (C₂)^q prefactor with q > 0 preserves the MAP-B structural sub-result Y₁ = 0 EXACT from C₂(0,0) = 0 — a constraint the surviving class must keep). Scale: NO at every structurally-motivated corner — the widening absorbs the shape misfit and the rescale non-constancy, but a residual external scale of 2.8–4.0× persists (grid below); the full ~10× (rescale_Yref_A = 10.488, B = 8.638 in Y_ref; equivalently per-generation 5.73–13.66) is NOT produced by any C₂-exponent form at substrate-natural normalization. One corner of the family — the q→0 edge of the √C₂-exponent form — reaches scale closure to within 5.9%; it is flagged post-hoc in II.4.

### II.4 The surviving map class: sector-keyed exponential Casimir envelope (with the enumerated-grid residuals and two flagged post-hoc adjacencies)

**Result**: the exponential ε_LX class closes shape exactly on a 1-parameter hypersurface; absolute-scale residuals over the pre-declared 2×3 form grid: r ∈ {2.820, 3.378, 4.046; 0.944, 1.840, 3.586}. Classification: **PARTICLE**.

The grid below is the FULL set of forms considered (declared here to bound the post-hoc search surface): exponent argument g ∈ {C₂, √C₂} × prefactor power q ∈ {0⁺, 1/2, 1}, absolute normalization Y_i = E₁·(C₂,i)^q·exp(s_ν·g(C₂,i)). For each corner: the shape-exact exponent s_ν from Eq. (4), and the residual scale r = Y₂^{S99}/Y₂^{map}:

| g | q | s_ν (shape-exact) | Y₂^{map} | r = 4.79357/Y₂^{map} | note |
|:--|:--|:--|:--|:--|:--|
| C₂ | 0⁺ | 0.546948 | 1.69977 | **2.820** | pure widening exponential |
| C₂ | 1/2 | 0.303669 | 1.41902 | **3.378** | MAP-B prefactor × widening |
| C₂ | 1 | 0.060390 | 1.18464 | **4.046** | linear-C₂ prefactor |
| √C₂ | 0⁺ | 1.578903 | 5.07533 | **0.944** | ONLY corner crossing 1 (map overshoots +5.9%) |
| √C₂ | 1/2 | 0.876616 | 2.60466 | **1.840** | — |
| √C₂ | 1 | 0.174331 | 1.33671 | **3.586** | — |

(All dimensionless; E_i in M_KK units; Y dimensionless; q→0⁺ preserves Y₁ = 0 exactly for any q > 0 while gen-2/3 values approach the pure-exponential limit continuously — the edge is admissible but structurally degenerate, since the prefactor's only surviving role there is the C₂ = 0 zero.) Every corner is DESI-safe: the five undershooting corners give Σ < Σ_mnu_FW trivially, and even the one overshooting corner gives Σ = 0.0582053×(1.0588)² = 0.0652 eV < 0.072 eV.

**Two post-hoc adjacencies (flagged — NOT gate inputs, NOT evidence; pre-registration candidates only):**

- **(P1) k = −2 integer-shifted freeze-in exponent.** The W3 threshold form exp(−(k+S₀)C₂) at integer k = −2 gives exponent −(k+S₀) = 2 − S₀ = 0.305847, vs the (g=C₂, q=1/2) shape-exact requirement 0.303669: dev **0.72%** (shape at the candidate: 2.49730, +0.36% vs required — inside the ≈1% oscillation-precision band on (1)). If it survived a pre-registered test, the neutrino-Dirac shape would be carried by the SAME S₀ as the charged-lepton envelope with a two-unit mode shift — but the scale residual at this corner is 3.378, so it is a shape-only candidate.
- **(P2) s_ν ≈ S₀ on the √C₂ form.** The only scale-closing corner requires s_ν = 1.578903; the charged-lepton S₀ = 1.694153 sits 7.3% above it (and imposing s_ν = S₀ exactly misses shape by +6.9% — several × outside the ≈1% band). Adjacent but presently failing both pre-registerable tolerances; recorded so that S101 kills or revives it cleanly. The bare magnitude ratio S₀/s_ν(C₂, q=0⁺) = 3.0975 (3.25% off 3) is likewise noted and tagged numerology-grade.

**Second surviving structure (CLASS-2): off-diagonal seesaw texture.** The W5-1 seesaw was diagonal-aligned; the W2-2 EXACT off-diagonal — |w| = 1/√6 = 0.408248 at all three Z₃ points, arg(w) = {π, +2π/3, −2π/3} on the BDI (1,0)↔(0,1) s-linear channel — is untested in the neutrino sector. A doublet-split reading (gens 2,3 = the two eigenstates d ± |w| of the (1,0)⊕(0,1) pair) is reality-compatible by the S99 BDI adjudication (J forces d₁ = d₂ on the doublet diagonal, leaves w unconstrained including phase; eigenvalue split depends on |w| only) and CG-safe for rank-deficiency (the s-linear channel cannot connect (0,0) to (0,1): (2,0)⊗(0,0) = (2,0) ≠ (0,1), so m₁ = 0 survives exactly). Required split ratio (d+|w|)/(d−|w|) = 2.48825 needs |w|/d = (S−1)/(S+1) = 0.426650; the substrate-exact 1/√6 = 0.408248 sits **4.5% below** — but the |w|-vs-d unit normalization is NOT pinned (the W2-2 |w| is in unit-normalized kernel units; the diagonal envelope carries different units), so this adjacency is unpinnable until the W-2 counting-convention workshop lands. Caution for hybrid textures: the |s|²-channel element (0,0)↔(1,1) is CG-admissible ((0,2)⊗(2,0) ⊇ (1,1)), and any nonzero value there lifts m₁ = 0 — preserving the rank-deficiency emergence is a mandatory sub-criterion on every CLASS-2 texture.

**Third adjacency (CLASS-3, untested, weakest spec)**: off-diagonal M_R texture on the B-branch fold-energy triple (m_ν = m_D^T M_R^{−1} m_D with non-diagonal M_R^{−1} reshapes the light masses at fixed diagonal m_D; the S60 leptogenesis-CP log carries the M_R texture machinery). Listed as an open adjacency; folded into §V.2's scope rather than given its own gate.

---

## III. Gate Verdicts

Verdicts below are quoted from `computations/session-100a/s100a_gate_verdicts.txt` and the source WPs — authoritative, not re-adjudicated here.

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| S100a-MD-NORMALIZATION (W5-1) | **INFO** (sign=PASS, magnitude=INFO, regime=VALID; track_B 0.9) | uniq_ratio 0.4742 ≫ 0.05; shape required 2.4883 vs maps 1.0444 / 1.5000-exact; per-gen rescale [5.735, 13.663]_A / [5.848, 9.700]_B non-constant; both maps ~100× below 0.0582 eV; Y₁ = 0 EXACT (MAP-B); audit `4f92a5513ad69b07…` |
| S100a-D5-0NUBB-MAJORANA (W5-2, context) | PASS | m_ββ = 3.695 meV ∈ NO funnel [1.5, 4.5]; inherits W5-1 scale caveat in framing only; audit `a2d29b97…` |
| S100a-DUAL-Z3-PHI-POINTS (W2-1) | PASS | c(φ) = {1/9, 1/3, 1/3} exact; lepton-only lever; audit `d23c7e99…` |
| S100a-YUKAWA-OVERLAP-OFFDIAG (W2-2) | INFO | S97 1:1:1 wall BROKEN (spread 1.103 e-folds, e = (3,0)); \|w\| = 1/√6 EXACT, arg(w) Z₃; W = −4.66; audit `871573da729c5972…` |
| S100a-CASIMIR-WIDENING (W2-3) | FAIL | W = −4.663502 outside all bands; floors NOT Casimir-linear at τ_fold (chord-slope ratio 6.979380); audit `67a71781b45ea5d4…` |
| S100a-CONNES-DISTANCE-LADDER (W2-4) | INFO | generation-RESOLVING strict ladder; spread 7.1378 e-folds ∈ [6,10]; W_Connes = 12.5629 = (9/5)×6.979 bit-identical to W2-3; audit `5e24db72e3e5121b…` |
| S100a-FREEZEIN-OVERCONSTRAINED (W3-9) | FAIL (composite; charged-lepton SHAPE leg survived) | ONE S₀ = 1.694153 on C₂ = (4/3, 3, 6), resid_max 2.22e-16; audit `78ee1d5677d75dc8…` |
| S96-MATTER-R-HIERARCHY (anchor, prior session) | FAIL | R_direct = 9.86183067373777 (rank-1 direct-spacing wall; reproduced by W5-1 at reldiff 1.0e-13) |

---

## IV. Structural Implications

### IV.1 Corridor-status verdict: reading (ii), with the (i)-grade sub-claims named exactly

The two readings posed:

- **(i) wall-is-structural**: rank-1 wall + shape wall + non-constant rescale jointly close the substrate-forward corridor at the representation level, licensing PERMANENT language at full breadth beyond the two tested maps.
- **(ii) wall-is-two-maps-deep**: richer D_F structure (off-diagonal Higgs overlap, exponential envelopes, inter-tower mixing) remains untested.

**Adjudication: (ii), scoped.** The decisive observations:

1. **The plan itself separates the two breadths.** The plan's FAIL_meaning reserved "the substrate-forward corridor for a zero-free-parameter Σm_ν is CLOSED" for the FAIL branch (Σ > 0.12 eV overshoot). The landed branch is INFO, whose pre-registered meaning is map NON-uniqueness + irreducible residual scale — NOT corridor closure. Importing FAIL-branch breadth into an INFO-branch verdict would be post-hoc re-scoping of a pre-registered rubric.
2. **The excluded class is exactly the class §VII.BL predicts must fail.** The Generation-Blindness Obstruction (STAGE-3-PERMANENT) reframes the hierarchy as necessarily a threshold/transit/localization effect carried by an external non-left-invariant ε_LX on the multiplicity bundle — NOT a bare-spectrum tree number (consistent with S62 tree-Yukawa-vanishes PROVEN). MAP-A and MAP-B are O(1) power-law readings of bare sector data (deformed floors; √C₂ labels). Their failure is the neutrino-sector image of the S97/S99 reframe — confirmation of the standing theorem's boundary, not a new closure of the ε_LX corridor, which W5-1 never entered.
3. **The framework's own charged-lepton solution lives in the untested class.** The W2/W3 cluster established the charged-lepton envelope as EXPONENTIAL in the Casimir grading (W3-9 shape leg exact at 2.2e-16; W2-4 Connes map m = e^{−d/ℓ}, generation-RESOLVING, regulator-invariant at 1.8e-9 across 3 decades; S99 four-lens modulus exp(−d/ℓ) = Γ·exp(−2πω/κ)). The W5-1 diagnostic's own post-hoc sweep stopped at linear-C₂ ("no LOW-ORDER Casimir grading… reproduces 2.4883" — correct and correctly scoped); the exponential class generates any shape on the 1-parameter hypersurface (4).
4. **But the scale axis is (i)-grade within anchored normalizations.** The factorization (3) extends the scale exclusion to ALL shape functions at bottom-triple-anchored normalization (r₂ ≥ 5.49), and the enumerated unanchored grid leaves ≥ 2.8× at every structurally-motivated corner. The scale wall is therefore effectively structural — short of theorem-grade only because of the single flagged q→0⁺ √C₂ corner (r = 0.944), which is post-hoc and is assigned a falsification duty in §V.1 rather than narrative weight.

**Net corridor statement**: the substrate-forward corridor SPLITS. The **absolute-scale corridor** is closed at track_B-0.9 grade with shape-independent breadth (one queued post-hoc escape). The **shape corridor** through the sector-keyed exponential ε_LX class (and secondarily the off-diagonal texture class) is OPEN and untested — with the new structural cost, derived in II.3, that the neutrino-Dirac exponent must be sign-flipped and ~3.1× shallower than the charged-lepton S₀.

### IV.2 PERMANENT-breadth licensing decision

- **Capstone §7.3 item-(4) (line 563) — LICENSED AS WRITTEN.** Checked verbatim: it asserts NON-uniqueness, not-zero-free-parameter, "Dirac-scale anchor is irreducibly EXTERNAL", caveat PERMANENT at track_B 0.9, and lists the PASS-grade survivors (M_R coincidence 0.0177 < 0.02, seesaw structure, suppression direction, normal ordering, Y₁ = 0 emergence). It does NOT claim representation-level corridor closure. No edit required. Same for §7.2 Row #9 ("absolute Σ NOT-ZFP… S99 caveat PERMANENT") — clean.
- **W5 WP Wave-5 Synthesis §1 — ONE PHRASE NEEDS A SCOPE QUALIFIER.** "confirmed PERMANENT — irreducibly external, **not a refinable approximation**" is licensed for the SCALE (per (3) and the grid), but read as all-maps breadth it would also assert the SHAPE corridor closed, which is FAIL-branch language the INFO verdict does not license. Proposed scoped restatement (routes per capstone-hygiene Q3/Q4 as a designated-writer prose patch, NOT a carry-forward): *"confirmed PERMANENT on the absolute-scale axis — the Dirac scale is irreducibly external at every bottom-triple-anchored normalization, shape-independently; the SHAPE corridor through the W2/W3 sector-keyed exponential ε_LX class remains open and is pre-registered for S101 (S101-NU-DIRAC-ENVELOPE-MAP), with the one identified scale-closing corner (√C₂ q→0⁺ edge, post-hoc) queued for falsification there."*
- The PERMANENT grade itself is the plan's own pre-registered INFO_meaning vocabulary ("STRUCTURALLY IRREDUCIBLE") plus the pre-registered posterior reallocation (INFO → 0.9 track_B). It is a discriminator-weighted claim, not a theorem; the registry-grade phrasing should keep the track_B-0.9 tag attached, as the capstone already does.

### IV.3 Cross-source consistency and conflict flags

- **No numerical conflicts found.** Verdict line, WP §W5-1, npz, capstone §7.3 item-(4), and plan INFO-branch routing agree on every shared number (verified against the npz: shape_required 2.4882511868; pergen_rescale_A [5.73466, 13.66316]; B [5.84766, 9.70030]; rescale_Yref 10.4878/8.6377; R_direct cross-check reldiff 1.0e-13).
- **One near-conflict, resolved by scope**: W5 WP "Carry-Forward Computations: No carry-forwards" vs this synthesis producing §V entries. Not a conflict — the WP statement is scoped to the plan's pre-registered triggers ("the W5-1 FAIL-branch trigger for a distinct-substrate-forward-map CF did not fire"), and its own 2026-06-07 addendum already routes the D_F-texture wall-scope review to the schedule (S-3 = this dispatch). The §V entries below are the OUTPUT of that scheduled review, feeding the EVOI rank-9b texture cluster — not a retroactive edit of the gate's branch routing.
- **Workshop dependence declared**: the W-2 counting-convention adjudication (block-sum vs per-mode vs block-trace ⟨ω⟩_g; μ/τ ordering) and the W-3 carrier reading (same-object vs competing-carrier) condition WHICH exponent form in the II.4 grid is substrate-canonical, and CLASS-2's |w|-vs-d unit pinning. Both workshops are unlanded shells; §V.1/V.2 carry conditional-consumption clauses. The W-2 header's CANONICITY RIDER (LC-lineage s84 cache conditioning by the S100b W-1 τ=0 operator-canonicity workshop) applies transitively to every number here: verdict SHAPES robust, numerical values lineage-conditional.

### IV.4 Constraint-map updates

| Mechanism | Prior state | New state (this synthesis) |
|:--|:--|:--|
| Substrate-forward Σm_ν corridor | CLOSED-INFO as one item (W5 WP) | SPLIT: absolute-scale corridor closed shape-independently at anchored normalization (r₂ ≥ 5.49, Eq. 3), track_B 0.9, one flagged post-hoc escape corner; SHAPE corridor through exponential ε_LX class OPEN, pre-registered §V.1 |
| Neutrino-Dirac envelope direction | unexamined | WIDENS in C₂ (+0.5469/unit-C₂) — OPPOSITE to charged-lepton (−1.6942); sector-universal single-exponent envelope EXCLUDED (II.3 chain) |
| MAP-A shape failure mechanism | "consistent with S96 rank-1 wall" | IDENTIFIED as the W2-3/W2-4 Jensen-fold van-Hove floor compression (shared floors, E₂/E₁ = R_cross = 1.019704; chord-slope 6.979); deformed-floor exponentials excluded as substrate-natural (s = 14.4 unanchored) |
| Residual-freedom dimensionality | "NOT even 1-parameter" (gate, for tested maps) | exponential class with shape-exact s_ν restores EXACTLY-1-parameter constant rescale (r₂ = r₃ algebraically); the 1 parameter remains external — track_B sharpened, not removed |

---

## V. Carry-Forward Computations

Feeds the **EVOI rank-9b fermion-mass texture cluster** (existing row; NOT a new EVOI entry).

**V.1. S101-NU-DIRAC-ENVELOPE-MAP — sector-keyed exponential Casimir envelope on the neutrino-Dirac triple (the surviving map class, pre-registered)**
- **What**: Evaluate the family Y_i = E₁·(C₂,i)^q·exp(s_ν·g(C₂,i)) on the towers (0,0)/(1,0)⊕(0,1)/(1,1), C₂ = (0, 4/3, 3), in BOTH normalizations: (n1) gen-2-anchored (tests shape closure + rescale constancy; r₂ = 5.8477 invariant) and (n2) absolute (tests scale reach from E₁ alone). Compute the shape-solution curve s_ν(q, g) per Eq. (4) for g ∈ {C₂, √C₂}, q ∈ (0, 1]; test the pre-registered substrate-candidate exponents: (a) s_ν = 2 − S₀ = 0.305847 at (g=C₂, q=1/2) [k = −2 shifted freeze-in; predicted shape dev +0.36%]; (b) s_ν = S₀ = 1.694153 at (g=√C₂, q→0⁺) [predicted shape dev +6.9% — expected kill; falsifies the only scale-closing corner if it also misses scale]; (c) the hawking-derived neutrino-sector greybody κ_ν (consume only if landed by S101 plan-freeze; else mark N/A). Verify Y₁ = 0 exact for all q > 0; verify rescale constancy r₂ = r₃ at every shape-exact point; verify DESI safety per corner. Conditional consumption: if the W-2/W-3 workshops land before plan-freeze, pin the adjudicated counting convention (which may replace floor-C₂ data with block-trace ⟨ω⟩_g as the exponent argument) and the carrier reading; otherwise freeze the grid as specified here.
- **Inputs**: `computations/session-100a/s100a_md_normalization.npz` (E_triple, Y_S99, shape_required, M_R; audit `4f92a5513ad69b07…`); `computations/session-100a/s100a_freezein_overconstrained.npz` (S0_fit = 1.694153; audit `78ee1d5677d75dc8…`); `computations/session-84/s84_spectrum_cache_L12_tau019.npz` (SHA `9e6d9cf7…`); canonical: `Sigma_mnu_FW`, `M_KK`, `v_ew`, `tau_fold`, `m_tau_PDG`; workshop pins if landed.
- **Gate**: PASS iff some pre-registered candidate closes shape |Y₃/Y₂ − 2.4882512|/2.4882512 ≤ 0.01 (the ≈1% oscillation-precision band on Eq. (1); re-pin the exact tolerance from the NuFit convention spread at plan-freeze) AND (n2)-scale residual |ln r| ≤ ln(1.05) AND rescale constancy ≤ 1%. INFO iff a candidate closes shape at ≤ 1% but r > 1.05 (shape corridor OPEN, scale wall STANDS — track_B sharpened to exactly-1-parameter; the expected branch, per candidate (a): r = 3.378). FAIL iff no pre-registered candidate closes shape at 1% (the exponential ε_LX class joins the excluded set at its substrate-pinned points; corridor narrows to CLASS-2/CLASS-3).
- **Effort**: ~0.3 wave-equivalents (closed-form algebra on published npz values; no diagonalization).

**V.2. S101-NU-DIRAC-OFFDIAG-TEXTURE — doublet-split off-diagonal seesaw texture (CLASS-2), conditional on W-2 unit pinning**
- **What**: Pin the |w|-vs-diagonal unit normalization per the W-2 counting-convention verdict (BLOCKING prerequisite — without it the 4.5% adjacency |w|/d: 0.408248 vs required 0.426650 is unpinnable); then evaluate the reality-compatible texture m_D ∝ [[d, w],[w*, d]] on the (1,0)⊕(0,1) doublet (gens 2,3 = d ± |w| eigenstates; gen 1 = (0,0), m₁ = 0 CG-protected at s-linear order) through the diagonal-M_R seesaw; report the split-ratio shape vs 2.4882512 and the absolute scale vs Y₂^{S99}; include the mandatory sub-criterion that no |s|²-channel (0,0)↔(1,1) element is introduced (rank-deficiency preservation).
- **Inputs**: W-2 workshop verdict (counting convention + unit pin — prerequisite); `s100a_yukawa_overlap_offdiag.npz` (|w|, arg w, eps_lx_block_phi0; audit `871573da729c5972…`); `s100a_md_normalization.npz` (Y_S99, M_R); S99 BDI reality adjudication (agent memory, §VII.BL file, reusable Sage result).
- **Gate**: PASS iff the unit-pinned split ratio lands in 2.4883 ± 1% AND scale within 5% of substrate-natural; INFO iff shape lands but scale fails (parallel to V.1's INFO); FAIL iff the pinned normalization puts |w|/d outside [0.405, 0.449] (the ±5%-in-shape window around 0.426650). PRE-REG-INC if W-2 has not landed by plan-freeze (prerequisite-block, mechanical closure per `mechanical-closure-discipline.md`).
- **Effort**: ~0.2 wave-equivalents after W-2 lands (2×2 algebra + seesaw substitution).

**V.3. S101-KAPPA-NU-GREYBODY — substrate derivation of the neutrino-sector greybody slope (feeds V.1 candidate (c))**
- **What**: Extend the S99 four-lens sector-κ ladder (lepton 1.89 / up 1.29 / down 0.78) to the Dirac-neutrino channel: derive κ_ν from the horizon/greybody machinery on the (0,0)/(1,0)⊕(0,1)/(1,1) towers and map it to an exponent prediction s_ν^{pred} = f(κ_ν) in the Eq.-(4) variables, including whether the sign flip of II.3 emerges (e.g., as a super-radiant/transmission-enhanced channel) or is excluded.
- **Inputs**: S99 fermion-mass panel deliverables (`sessions/archive/session-99/session-99-fermion-mass-*.md`, hawking sector-κ derivation); `s84` L12 cache floors; `tau_fold`; the II.3 required values (+0.546948 at g=C₂ q=0⁺ form; form-equivalents per Eq. 4).
- **Gate**: PASS iff κ_ν exists with sign and magnitude reproducing a shape-exact s_ν within 5% on any single pre-declared (g, q) corner; FAIL iff the greybody construction forbids the widening sign (which would itself close CLASS-1's candidate-(c) route and leave (a) as the only live substrate pin); INFO for a derivation that lands the sign but not the magnitude.
- **Effort**: ~0.5 wave-equivalents, 1 agent session (hawking-side derivation + cross-check).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Corridor-status verdict: reading (ii), scoped — shape corridor OPEN through the exponential ε_LX class; scale corridor closed shape-independently at anchored normalization | PARTICLE | Adjudicated (this synthesis) | W5-1 INFO ≠ FAIL-branch corridor closure; surviving class pre-registered as S101-NU-DIRAC-ENVELOPE-MAP |
| 2 | Scale-shape factorization: r₂ = Y₂^{S99}/Y_ref = 5.8477 invariant under ALL shape functions (≥ 5.49 over all bottom-triple anchors) | PARTICLE (algebraic) | Derived (exact) | Extends the gate's scale exclusion to full shape breadth within anchored normalizations — the (i)-grade component of the wall |
| 3 | Widening-direction chain: d ln Y^{ν_D}/dC₂ = +0.5469 vs charged-lepton −1.6942 (opposite sign, ratio 3.0975) | PARTICLE | Derived (substitution chain, II.3) | No sector-universal envelope; sector-keyed (sign, magnitude) required — extends the existing four-lens sector-κ pattern |
| 4 | Exponential-grid residual scales r ∈ {2.82, 3.38, 4.05; 0.944, 1.84, 3.59}; shape closes exactly on hypersurface (4); rescale becomes exactly-1-parameter | PARTICLE | Derived (enumerated grid) | Widening closes SHAPE but not SCALE (~3× residual) at every motivated corner; "not even 1-parameter" → "exactly 1 parameter" sharpening of track_B |
| 5 | MAP-A shape 1.0444 = the W2-3/W2-4 Jensen-fold van-Hove floor compression (shared floors; E₂/E₁ = R_cross 1.019704) | GEOMETRIC | Identified (cross-cluster) | One fold mechanism behind both the W2 FAIL and the W5-1 MAP-A shape; deformed-floor exponentials excluded (s = 14.4) |
| 6 | PERMANENT-breadth licensing: capstone §7.3 item-(4) + §7.2 Row #9 LICENSED AS WRITTEN; W5 WP synthesis phrase "not a refinable approximation" needs the IV.2 scope qualifier | NON-PHONONIC (registry hygiene) | Adjudicated; prose patch routed (capstone-hygiene Q3/Q4, designated writer) | PERMANENT = scale-axis, track_B-0.9, pre-registered INFO_meaning vocabulary; not all-maps shape breadth |
| 7 | Post-hoc adjacencies flagged: (P1) s_ν = 2−S₀ (0.72% dev, shape-only); (P2) √C₂ q→0⁺ corner (scale within 5.9%); CLASS-2 \|w\|/d (4.5% dev, unit-unpinned) | PARTICLE | Flagged post-hoc — NOT evidence | Assigned falsification duties in V.1/V.2 pre-registrations; no narrative weight until gated |
| 8 | Y₁ = 0 EXACT from C₂(0,0) = 0 preserved by every (C₂)^q prefactor, q > 0; CG-protected against s-linear (0,0) off-diagonals; threatened only by \|s\|²-channel (0,0)↔(1,1) elements | PARTICLE | Constraint on surviving class | The gate's one positive structural finding (rank-deficiency EMERGES) is carried as a mandatory sub-criterion in V.1/V.2 |
| 9 | Graceful-degrade: W-2/W-3 workshop shells unlanded → WP anchors only; conditional-consumption clauses in V.1/V.2 | NON-PHONONIC (process) | Executed | S101 plan-freeze re-checks workshop landings before pinning the exponent-argument form and CLASS-2 units |
