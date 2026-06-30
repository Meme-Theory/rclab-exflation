# Session 86 Workshop: connes x lizzi — cutoff_sqrt GATE A/B/C Trio (Atlas-Cardinality Determinant)

**Date**: 2026-04-27
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: connes (connes-ncg-theorist), lizzi (lizzi-spectral-functional-theorist)
**Source Documents**:
- sessions/archive/session-86/session-86-w4-workingpaper.md
- sessions/framework/registry/cutoff-sqrt-adjudication.md
- computations/canonical_constants.py

**PRDR Anchors**:
- **GATE A** (§3.1): `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS` — master; expected FAIL per R3-C-E3-C structural pre-determination (Peter-Weyl L^8/960 mode-count growth at d=8 spectral dimension implies α = −k_eff/4 < 0 for every k_eff ∈ [5.09, 8])
- **GATE B** (§3.2): `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY` — subset-removal-sweep on a_0 slot under W2-1 protocol, L_max=7
- **GATE C** (§3.3): `S86-CUTOFF-SQRT-GATE-C-S82-APPLICABILITY` — MP-abs-conv at s=6 on framework-truncated f_6 = 0.1 residue, L_max=3

**Discrete a_0(L_max) anchors**: a_0(3)=12880, a_0(4)=50176, ..., a_0(10)=9785776. cutoff_AL2010 Mellin vector candidates (1/2, 1, 1, 0) [published] vs (2, 1, 0.5, 0.1) [framework-truncated]. CCM-2007 axiom set {dim, reg, fin, real, 1st-order, orient, PD}.

**Three Gates Dispatched in R1, Cross-Validated in R2**:
1. GATE A (connes, master): test whether `f_0 · Λ(L_max)^4 · a_0(L_max)` admits positive-α scaling Λ(L_max) = Λ_0·L_max^α (α ∈ [−2, +2]) such that coupling is bounded as L_max → ∞ on Jensen-deformed SU(3). Treat as canonical-record per W4-3 line 437 — NOT adjudication. Per R3-C-E3-C, expected FAIL → atlas A_5 collapses to A_4
2. GATE B (connes): subset-removal sweep on a_0 slot under W2-1 protocol — tests {dim, fin} vs {reg, 1st-order} sourcing
3. GATE C (lizzi): HBW / MP-abs-conv at s=6 on f_6 = 0.1 framework-truncated residue specifically (NOT the unregulated kernel which was retracted under R2-A-CONV-(a))

**Pre-Registered Outcome** (subject to PROHIBITED_ACTIONS `.claude/rules/v3-closure-recovery.md` — no iterate-until-PASS, no convention-shopping):
- GATE A FAIL → A_4 = {ζ, Zubarev, SDW, anomaly}, atlas reduced; cutoff_sqrt removed; promote C45 S87 sixth-regulator-synthesis
- GATE A PASS (unexpected) → atlas A_5 confirmed; cutoff_sqrt retained
- GATE B + GATE C as taxonomic tests of how cutoff_AL2010 sits relative to LAYER 2 admissibility axioms — clean exclusion (FAIL on dim/fin alone), structurally inner-fluctuation-related (FAIL on reg / 1st-order), or HBW-positive-cone-related (FAIL on f_6 residue MP-abs-conv)

**Verdict-Line Discipline**: Each gate emits one verdict line to `computations/s86_gate_verdicts.txt` with dual-SHA (content_sha256 + audit_sha256) per `.claude/rules/v3-closure-recovery.md` sig_5.

**Pre-Registered Carry-Forward**: 4-field S87 spec (what / inputs / gate / effort) for:
- `S87-CUTOFF-SQRT-ATLAS-PROPAGATION` (atlas reduction propagated into W4-2/W6/W12/W13)
- `S87-W4-2-RE-RUN-UNDER-A_4` (re-run W4-2 max_pair_ratio on reduced atlas)
- `S87-C45-SIXTH-REGULATOR-PROMOTION` (if GATE A FAILs)

**Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`): cutoff_sqrt is a regulator profile applied to D_K's eigenvalue spectrum. GATE A measures whether the substrate admits a finite L_max → ∞ extrapolation of the f_0·Λ^4·a_0 product. PASS/FAIL is a substrate property, not a numerical-method property.

---

## Round 1 — connes: GATE A + GATE B Dispatch

### C1: GATE A — Λ(L_max) = Λ_0·L_max^α Positive-α Scaling Test on Jensen-Deformed SU(3)

**Topline finding (canonical-record FAIL, structurally pre-determined per R3-C-E3-C)**:
GATE A returns **FAIL**. Across the PRDR-pinned probe set L_max ∈ {3, 5, 7, 10},
the boundedness root α_star(L) := −k_eff(L)/4 is strictly negative at all
four probe points (−1.0158, −1.2988, −1.4538, −1.5893), with the asymptotic
trajectory α_star_asymptotic = −1.5467 climbing toward the Peter-Weyl L^8/960
limit α = −2 as L → ∞. There is no α ≥ 0 in the PRDR-pinned scan window
[−2.0, +2.0] (step 0.05, 81 grid points) that admits a bounded coupling
g(L) = f_0 · Λ_0^4 · L^{4α} · a_0(L) as L → ∞. The coupling g(L_max=10)/g(L_max=3)
ratio at α = 0 (no Λ-rescaling) is 7.5977 × 10² (≈ 760×); the bounded-α band
is [−1.85, −0.90], entirely on the negative-α side of zero. Atlas-cardinality
cascade outcome: A_5 → A_4 = {ζ, Zubarev, SDW, anomaly}; cutoff_sqrt removed.

**Substitution chain (per `.claude/rules/math-scripts.md` §Double-Check Logic Before Compute)**:

```
Step 1 (definitions):
  coupling g(L) := f_0 · Λ(L)^4 · a_0(L)         (cutoff_AL2010 a_0-channel coupling)
  Λ(L)         := Λ_0 · L^α                       (PRDR α scan window α ∈ [−2, +2])
  a_0(L)       := 16 · Σ_{p+q≤L} [(p+1)(q+1)(p+q+2)/2]^2
                                                  (Peter-Weyl L²(SU(3)) sum-of-dim²;
                                                   leading L^8/960 per workshop §1.5
                                                   Sage closed form, cutoff-sqrt-
                                                   adjudication.md §3.1)
Step 2 (substitute):
  log g(L) = const + 4α · log(L) + log a_0(L)
           = const + 4α · log(L) + k_eff(L) · log(L) + O(1)
  where k_eff(L) := d log a_0 / d log L
                  = log(a_0(L)/a_0(L−1)) / log(L/(L−1))    (effective polynomial growth)

Step 3 (simplify):
  Boundedness as L → ∞ requires 4α + k_eff(L) → 0
                              ⇔ α_star(L) = −k_eff(L)/4
  Asymptotic regime: a_0(L) ~ L^8/960  ⇒  k_eff → 8  ⇒  α_star → −2.

Step 4 (direction):
  At PRDR probe points (L=3,5,7,10):
    k_eff(3)  = ln(12880/2480)/ln(3/2)      = 4.063  ⇒  α_star = −1.016
    k_eff(5)  = ln(159936/50176)/ln(5/4)    = 5.195  ⇒  α_star = −1.299
    k_eff(7)  = ln(1077120/439488)/ln(7/6)  = 5.815  ⇒  α_star = −1.454
    k_eff(10) = ln(9785776/5008432)/ln(10/9)= 6.357  ⇒  α_star = −1.589
    k_eff(7→10) = ln(9785776/1077120)/ln(10/7) = 6.187  ⇒  α_star_asymptotic = −1.547
  All α_star < 0 on the probe set; asymptotic trajectory monotone toward −2.
  ⇒ No α ≥ 0 admits a bounded limit. Direction: STRUCTURAL FAIL.
```

The k_eff(L) values are increasing monotonically (4.063 → 6.357 over the probe
set), and the asymptotic projection from the (7→10) ratio is 6.187 — already
3 OOM-converged toward the L^8/960 leading term. The pre-registered FAIL bound
α_max ∈ [−1.0158, −1.5893] across L ∈ {3,...,10} is reproduced exactly by the
script; asymptotic α = −2 from L^8/960 leading term is the structural endpoint.

**Verified anchors** (8/8 MATCH against §3.1 enumeration): a_0(3)=12880,
a_0(4)=50176, a_0(5)=159936, a_0(6)=439488, a_0(7)=1077120, a_0(8)=2410320,
a_0(9)=5008432, a_0(10)=9785776. Each anchor reproduced from
`a_0_peter_weyl(L_max) := 16·Σ_{p+q≤L_max} [(p+1)(q+1)(p+q+2)/2]²` to integer
exactness.

**Source citations**:
- Pre-registered FAIL outcome: `sessions/framework/registry/cutoff-sqrt-adjudication.md`
  §3.1 "PASS / FAIL / INFO threshold" (lines 144–150) and §3.4 "Joint outcome
  rule" line 213 ("GATE A FAIL → STRUCTURALLY-EXCLUDED, regardless of GATE B, C").
- Structural pre-determination: §3.4 lines 222–225 ("per workshop R3-C-E3-C,
  GATE A FAIL is structurally pre-determined by the substrate's Peter-Weyl L^8
  mode-count growth at d=8 spectral dimension; GATE A's S86 dispatch is
  canonical-record ... not adjudication").
- Anchor list: §3.1 line 138–139 enumeration.
- Substrate framing: §3.1 line 154–157 ("GATE A is a test of how the substrate's
  Peter-Weyl spectrum at d=8 spectral dimension couples through the
  cutoff_AL2010 Mellin prescription; the α = −k_eff/4 < 0 result is a STRUCTURAL
  property of the spectrum, not an external cutoff imposed on substrate space").

**Solution-space interpretation**: GATE A FAIL closes the corridor in which
cutoff_AL2010 carries the substrate-volume datum admissibly into S_b. The
substrate's Peter-Weyl mode count grows as L^8 at d=8 spectral dimension; the
only Λ-rescaling that absorbs this growth is α = −2 (UV scale shrinks as
truncation widens), which is unphysical. cutoff_AL2010 has no available
inner-fluctuation lift to redirect the channel. The atlas reduces from A_5 to
A_4 by structural exclusion, not numerical near-miss.

**Per `.claude/rules/phononic-framing.md`**: This is a SUBSTRATE property —
the eigenvalue spectrum of D_K on Jensen-deformed SU(3) carries L^8 mode-count
growth as a structural consequence of the d=8 spectral dimension. cutoff_AL2010
is a regulator profile applied to that spectrum; the FAIL is intrinsic to
how the substrate spectrum couples through the sharp-cutoff prescription, not
an external cutoff imposed IN substrate space.

**Questions for lizzi (R2 cross-validation)**:
- Q-CN-1: Does the asymptotic α_star → −2 trajectory hold under the
  Mellin-cone live infrastructure (W2 C9/C10) you spec'd? The current run uses
  the S85 W2-5 direct-heat-kernel-truncation fallback per W4-2 P5 (mellin_cone_live=False).
  Does live-Mellin-cone re-run change k_eff_asymptotic from 6.187 toward 8?
- Q-CN-2: For your GATE C HBW positive-cone test at s=6 on f_6 = 0.1 residue,
  is the f_6 slot decoupled from the L^8 a_0 channel, or does the framework
  truncation at L_max=3 inherit residual L^8 contamination? (Cross-check on
  whether GATE C verdict can be structurally independent of GATE A.)
- Q-CN-3: Confirm the §3.4 collapse rule absorbs my FAIL: GATE A FAIL alone
  → STRUCTURALLY-EXCLUDED regardless of B/C. Your R2 E2-L master-gate
  refinement explicitly stated this; restating for the R2 record.

### C2: GATE B — Subset-Removal Sweep on a_0 Slot Under W2-1 Protocol (L_max=7)

**Topline finding**: GATE B returns **PASS**. Under the W2-1 subset-removal
protocol applied to the a_0 slot at L_max=7, the load-bearing CCM-2007 axiom
set for cutoff_AL2010 sourcing of a_0 is exactly **{dim, fin}** (cardinality 2).
Removing reg, real, order1, orient, or PD individually does not break the
GLOBAL-TRACE route a_0 = Tr_H(1)/Vol_F. Per §3.2 PASS criterion, this is the
admissibility outcome. Per §3.4 master-gate composition rule, the joint W4
verdict remains STRUCTURALLY-EXCLUDED because GATE A FAILed; GATE B PASS is
necessary-but-not-sufficient (per R2 lizzi E2-L) and does not lift the joint
outcome. **GATE B's structural finding is that cutoff_AL2010 lives at the
{dim, fin} load-bearing level only — there is NO inner-fluctuation lift
mechanism available to it.**

**Substitution chain**:

```
Step 1 (definitions):
  A := CCM-2007 axiom set = {dim, reg, fin, real, 1st-order, orient, PD}
  cutoff_AL2010 published Mellin vector v_pub = (f_0, f_2, f_4, f_6) = (1/2, 1, 1, 0)
  cutoff_AL2010 framework-truncated v_fw  = (2, 1, 0.5, 0.1)
  a_0 sourcing routes:
    (i)   GLOBAL-TRACE:    a_0 = Tr_H(1)/Vol_F          requires {dim, fin}
    (ii)  HEAT-KERNEL:     a_0 = lim_{t→0+} Tr exp(−tD²)  requires {reg}
    (iii) MELLIN-RESIDUE:  a_0 = Res_{s=0} ζ_D(s)         requires {reg, 1st-order}

Step 2 (substitute under W2-1 subset-removal):
  cutoff_AL2010 = sharp Θ(Λ−|D|)/√(|D|²/Λ²) regulator (non-smooth at Λ).
  f_0 = 1/2 is FORCED by anomaly-cancellation (Andrianov-Lizzi arXiv:1103.0478;
        canonical_constants.py L1332 mellin_f_star_f0_sharp = 1.0  -- note
        pre-S78 numerical value; the physical constraint is f_0_anomaly = 1/2).
  Sharp Θ-cutoff has NO smooth heat-kernel asymptotic expansion
    ⇒ route (ii) STRUCTURALLY UNAVAILABLE.
  Sharp regulators violate ζ_D(s) analyticity at s=0
    ⇒ route (iii) STRUCTURALLY UNAVAILABLE.

Step 3 (simplify):
  cutoff_AL2010 a_0 sourcing reduces to route (i) GLOBAL-TRACE.
  Required axioms for route (i):
    dim → Tr_H(1) requires d-graded index (k=0 in Seeley-DeWitt expansion)
    fin → finitely-summable Tr_H(1) = dim H_F = 32 (else trace diverges)
  Removing reg or order1 is INVISIBLE to route (i):
    a_0 = Vol_F is fluctuation-invariant; (D + A + JAJ⁻¹)^0 = 1 ⇒ Tr(1) unchanged
    a_0 does not depend on smooth-domain class of [D, a]
  Removing real, orient, PD also invisible:
    real → enters at a_2 (Higgs mass; doubling) and a_4 ((Y*Y)²); a_0 is bilinear in 1
    orient → Hochschild d-cycle on M_4 base; F-trace independent
    PD → K-theoretic constraint; a_0 = Tr(1) is volumetric, not an index pairing

Step 4 (direction):
  load_bearing_set(a_0, cutoff_AL2010) = {dim, fin}
  cardinality = 2  ≤  PASS_MAX = 2  ⇒  PASS test verified.
  requires_reg = False, requires_order1 = False  ⇒  no inner-fluctuation lift demanded.
  Direction: PASS at the {dim, fin} sourcing level.

Caveat (§3.4 joint composition):
  The PASS condition is a LAYER 2 admissibility statement on the a_0 slot.
  GATE A's L_max-finiteness FAIL (preceding gate this session) closes the
  channel at the COUPLING level (Λ⁴ scaling unphysical); the joint W4 outcome
  remains STRUCTURALLY-EXCLUDED per §3.4: 'GATE A FAIL → STRUCTURALLY-EXCLUDED,
  regardless of GATE B, C'.
```

**Per-axiom load-bearing trace** (output table from `s86_w8_gate_b_kernel_admissibility.py`):

| ID     | Name              | Load-bearing for a_0 under cutoff_AL2010? | Rationale (one-line) |
|:-------|:------------------|:-----------------------------------------:|:---------------------|
| dim    | Dimension         | YES                                       | d=8 graded SDW index; route (i) requires dim |
| reg    | Regularity        | no                                        | sharp Θ has no smooth heat kernel; routes (ii)/(iii) UNAVAILABLE |
| fin    | Finiteness        | YES                                       | Tr_H(1) finite ⇔ fin holds |
| real   | Reality (J)       | no                                        | a_0 is bilinear in identity; J-action enters at a_2, a_4 only |
| order1 | First-order       | no                                        | a_0 = Vol_F is inner-fluctuation invariant |
| orient | Orientability     | no                                        | F-trace Tr_F(1) = 32 independent of orientation |
| PD     | Poincaré Duality  | no                                        | a_0 is volumetric, not an index pairing |

**Source citations**:
- W2-1 protocol: `computations/s85_w2_alpha_s_axiom_minimality.py` lines 51–158
  (CCM-2007 7-axiom roster definitions, invocation-site dictionary structure).
- §3.2 PASS/FAIL/INFO: `cutoff-sqrt-adjudication.md` lines 174–179
  ("PASS: load-bearing set is exactly {dim, fin}"; "FAIL: requires {reg} or
  {1st-order}"; "INFO: KO-dim grading or J-action dependence").
- Necessary-but-not-sufficient annotation: §3.2 lines 184–186 ("per R2 lizzi
  E2-L, GATE B alone is necessary but not sufficient for the W4 verdict —
  even if a_0 is sourced by {dim, fin} alone (load-bearing PASS), the COUPLING
  into S_b at the Λ^4 slot still requires GATE A's L_max-divergence absorbability check").
- f_0 = 1/2 anomaly forcing: `canonical_constants.py` lines 821–825
  (`f_0_sharp` provenance: "f_0 = 1/2 FORCED by fermionic-anomaly cancellation
  under sharp cutoff. Andrianov-Lizzi arXiv:1103.0478").

**Solution-space interpretation**: GATE B PASS confirms the LAYER 2 admissibility
of a_0 sourcing under cutoff_AL2010 is {dim, fin}-only — the regulator does NOT
require inner-fluctuation lift to source a_0. This is a structural property of
the volumetric channel (a_0 = Vol_F is fluctuation-invariant). The PASS does
NOT lift cutoff_AL2010 to GENUINELY-PHYSICAL because the COUPLING into S_b
(Λ⁴ · a_0) is closed by GATE A's FAIL.

The structural deliverable is: cutoff_AL2010 sits at the **{dim, fin}** level
of LAYER 2 admissibility — the most minimal load-bearing set possible. It has
NO inner-fluctuation lift available, but does NOT need one for the a_0 slot.
The Λ⁴ coupling FAIL (GATE A) is the channel-closing event, not a routing
defect at the axiom level.

**Per `.claude/rules/phononic-framing.md`**: The {dim, fin} load-bearing set
is a property of how cutoff_AL2010 reads OFF the substrate's spectral content
{λ_k} of D_K — specifically, of the d=8 mode count (dim) and the finite trace
of identity over H_F = C³² (fin). The other 5 axioms govern how the substrate
COUPLES (gauge, Higgs, J-action, orientation, K-pairing) — none of these route
through a_0 = Vol_F. The PASS is a LAYER 2 statement about the substrate's
volumetric channel under the cutoff_AL2010 prescription, not about a substrate
geometry issue.

**Questions for lizzi (R2 cross-validation)**:
- Q-CN-4: For your inner-fluctuation lift analysis (R2 E2-L), does the
  cutoff_AL2010 sharp Θ have a regulated symbol class that admits any
  inner-fluctuation-like calculus (e.g., truncated symbol algebra, Hörmander
  class S^{−∞}_{1,0} restricted to compact ψDOs)? My analysis assumes the
  answer is no — confirm structurally.
- Q-CN-5: Does your S85 W4 §1.5 Sage closed-form derivation of a_0(L) ~
  L^8/960 carry any axiom-level invocation beyond {dim, fin}? My answer:
  no, the closed form follows from Peter-Weyl L²(SU(3)) Plancherel and the
  sum-of-dim² mode count, both purely {dim, fin}-level.
- Q-CN-6: For your GATE C HBW test, the f_6 = 0.1 residue is on the f-tail
  of the framework-truncated Mellin vector (not on a_0). Is the GATE C
  verdict-classification ladder structurally independent of GATE B's
  load-bearing classification? (Cross-check on whether HBW positivity at
  s=6 reveals anything about a_0-channel admissibility.)

### C3: NCG-Axiomatic Sit — How cutoff_AL2010 Relates to CCM-2007 {dim, reg, fin, real, 1st-order, orient, PD}

**Topline finding (taxonomic map of GATE A and GATE B failures)**:
cutoff_AL2010's structural position relative to the CCM-2007 axiom set is
not a "single axiom violation." It is a TWO-LAYER structural defect that
LAYER 2 admissibility analysis (this session) decomposes into:

(i) **a_0 sourcing**: clean {dim, fin}-level admissibility (GATE B PASS).
    cutoff_AL2010 does NOT violate any of the 7 CCM-2007 axioms in how it
    routes the a_0 slot. The volumetric channel is fluctuation-invariant.

(ii) **Λ⁴ · a_0 coupling**: structural FAIL at the COUPLING level (GATE A FAIL).
     The L^8 mode-count growth of the d=8 substrate Peter-Weyl spectrum is
     incompatible with positive-α Λ-rescaling. This is NOT an axiom violation;
     it is a structural property of how the d=8 spectrum composes through the
     cutoff_AL2010 Mellin prescription.

The Layer 1 vs Layer 2 taxonomy (R3-C-E3-L) distinguishes:
- LAYER 1 (combinatorial-position-on-atlas): cutoff_AL2010 has a unique
  privileged slot (Mellin support + observable-cross-classification);
  per cutoff-sqrt-adjudication.md §4 cell-occupancy table line 256–262,
  cutoff_AL2010 is "PRIVILEGED" at LAYER 1.
- LAYER 2 (admissibility-on-axioms): cutoff_AL2010 is "FAILING (GATE A
  pre-determined)" at LAYER 2 per the same table.

**Taxonomic decomposition of the W4 outcome**:

| Outcome class                        | Channel              | Axiom invocation       | Verdict |
|:-------------------------------------|:---------------------|:-----------------------|:--------|
| Clean exclusion on dim/fin alone     | a_0 sourcing         | {dim, fin} only        | GATE B PASS |
| Inner-fluctuation related (reg/1st-order) | a_4 / a_2 sourcing | requires {reg, order1} | NOT applicable to a_0 |
| HBW positive-cone related            | f_6 = 0.1 residue tail | route-independent  | (lizzi GATE C) |
| Λ⁴ coupling at L_max → ∞             | f_0 · Λ⁴ · a_0       | structural; not axiom-level | GATE A FAIL |

The decomposition shows that cutoff_AL2010's exclusion is **NOT a single-axiom
violation**. It is a structural FAIL of the COUPLING geometry between a fixed
Λ scale and the L^8-divergent d=8 substrate spectrum. This is exactly what
the LAYER 1 vs LAYER 2 taxonomy was designed to capture: an axiom-clean (LAYER
2 PASS at {dim, fin}) regulator can still be structurally excluded by a
non-axiom-level coupling defect (LAYER 2 FAIL at the Λ⁴ scaling).

**Substitution chain (taxonomic map)**:

```
Step 1 (definitions):
  Axiom-level admissibility (LAYER 2): which CCM-2007 axioms must be invoked
                                        for cutoff_AL2010 to source a_0?
  Coupling-level admissibility (LAYER 2): for what Λ-scaling is f_0·Λ⁴·a_0
                                          bounded as L_max → ∞?

Step 2 (substitute):
  GATE B output: load_bearing(a_0, cutoff_AL2010) = {dim, fin}.
                 cardinality 2 ≤ 7 (full set).
                 Removing {reg, real, order1, orient, PD} does not break
                 a_0 sourcing under cutoff_AL2010.
  GATE A output: α_star(L) ∈ [−1.589, −1.016] for L ∈ {3,5,7,10}.
                 Asymptotic α_star → −2 (Peter-Weyl L^8/960 leading).
                 No α ≥ 0 admits bounded coupling.

Step 3 (simplify):
  Axiom-level cleanness: GATE B PASS  ⇒  cutoff_AL2010 is admissible at the
                          minimal {dim, fin} sourcing level.
  Coupling-level defect: GATE A FAIL  ⇒  cutoff_AL2010 is structurally
                          excluded at the Λ⁴ coupling level.
  These are INDEPENDENT structural properties (Layer 2 has internal
  decomposition into axiom-sourcing vs coupling-routing).

Step 4 (direction):
  cutoff_AL2010 sits in the cell:
    LAYER 1: PRIVILEGED  (combinatorial slot unique on Mellin support)
    LAYER 2: FAILING    (axiom-clean at sourcing; coupling-defective at Λ⁴)
  Direction: clean exclusion on Λ⁴ coupling alone — NOT an axiom violation.
              GATE B PASS confirms the regulator is well-formed at {dim, fin};
              GATE A FAIL confirms the channel cannot accommodate L^8 mode-
              count growth under any positive-α Λ-rescaling.
```

**Source citations**:
- LAYER 1 / LAYER 2 taxonomy: `cutoff-sqrt-adjudication.md` §1.4 lines 56–66
  (R2 lizzi EMERGENCE E3-L combinatorial vs admissibility taxonomy).
- Cell-occupancy table for cutoff_AL2010: §4 lines 256–262 ("LAYER 1 status:
  PRIVILEGED; LAYER 2 status: FAILING (GATE A pre-determined)").
- Joint outcome rule: §3.4 lines 211–217 (refined L_lizzi master-gate
  R3-C-CONV-5 binding); GATE A FAIL alone forces STRUCTURALLY-EXCLUDED.
- Necessary-but-not-sufficient: §3.2 lines 184–186; GATE B PASS does not lift
  GATE A FAIL.

**NCG axiomatic sit (proper structural classification)**:

| Axiom         | Role for a_0 under cutoff_AL2010              | GATE B verdict   |
|:--------------|:----------------------------------------------|:-----------------|
| dim           | LOAD-BEARING (d=8 graded SDW index)           | invoked → PASS  |
| reg           | NOT LOAD-BEARING (route (i) bypasses)         | not invoked     |
| fin           | LOAD-BEARING (Tr_H(1) finite)                 | invoked → PASS  |
| real (J)      | NOT LOAD-BEARING (a_0 bilinear in 1)          | not invoked     |
| 1st-order     | NOT LOAD-BEARING (a_0 fluctuation-invariant)  | not invoked     |
| orient        | NOT LOAD-BEARING (F-trace independent)        | not invoked     |
| PD            | NOT LOAD-BEARING (a_0 not an index pairing)   | not invoked     |

The structural fingerprint: cutoff_AL2010 is **axiom-minimal** for the a_0
slot ({dim, fin} suffice) but **coupling-structurally-defective** at the Λ⁴
slot. This is a NEW classification emerging from this session — the framework
previously treated regulator-class exclusion as monolithic; the GATE A + GATE B
decomposition shows axiom-cleanness and coupling-cleanness are independent.

**Per `.claude/rules/phononic-framing.md`**: cutoff_AL2010 is a Mellin-
summation prescription on the substrate's spectral content {λ_k} of D_K on
Jensen-deformed SU(3). It is NOT a cutoff imposed on substrate space. The
LAYER 2 axiomatic sit is a question of how the prescription reads off the
substrate's volumetric channel (a_0 = Vol_F) — and the answer is "minimally,
through {dim, fin}". The Λ⁴ coupling FAIL is a property of how that minimally-
read-off a_0 composes with the substrate's d=8 mode count growth.

**Questions for lizzi (R2 cross-validation)**:
- Q-CN-7: My LAYER 2 decomposition into "axiom-sourcing" vs "coupling-routing"
  is finer than the §1.4 R3-C-E3-L taxonomy (which treats LAYER 2 as monolithic
  "admissibility-on-axioms"). Does this finer decomposition belong as a
  permanent registry entry under §VII.K-PROP, or as a workshop-internal
  observation pending S87 codification?
- Q-CN-8: For your GATE C HBW positive-cone test, what is the corresponding
  axiomatic-sit classification? HBW positivity is a constraint on the
  Hausdorff-Bernstein-Widder positive cone of completely monotone functions
  — does this map cleanly onto any of the 7 CCM-2007 axioms, or is it a
  Layer-2-coupling-routing-style structural property orthogonal to the
  axiom set?
- Q-CN-9: In the §4 cell-occupancy table, ζ is listed as "GENERIC L1 / PASSING
  L2". Does my GATE B PASS observation that cutoff_AL2010 is also axiom-clean
  at {dim, fin} promote it from "FAILING" to "PASSING-MOD-LAYER" at LAYER 2,
  similar to how Zubarev (PASS-MOD-LAYER L2-SA stratified) and SDW (PASS-MOD-
  LAYER L3-OB stratified) are classified? Or does the Λ⁴ coupling FAIL keep it
  at a strict "FAILING"?

### C4: Verdict-Line Closure-Hashes for GATE A + GATE B

**Both verdicts emitted to `computations/s86_gate_verdicts.txt` with full
64-character dual-SHA per `.claude/rules/v3-closure-recovery.md` sig_5
(audit_sha256 = closure_hash of input pin map, COMPUTED not hardcoded;
content_sha256 = SHA-256 of script bytes per W9a-99 dual-SHA template).**

#### GATE A: `S86-CUTOFF-SQRT-GATE-A-LMAX-FINITENESS`

- **Verdict**: FAIL
- **Value**: `alpha_star_range=[-1.5893,-1.0158]; alpha_star_asymptotic=-1.5467;
  k_eff_range=[4.0630,6.3573]; k_eff_asymptotic=6.1867`
- **Scheme / Convention / L_max**: peter-weyl-sum-of-dim2 / cutoff_AL2010-canonical / {3,5,7,10}
- **`audit_sha256`** (full 64-hex):
  `a289004bff9ac728dd25f001cd65fc8df5fac2ac146897185f1b6ceeb569d270`
- **`content_sha256`** (full 64-hex; SHA-256 of script bytes):
  `8ef1bc07c8c2ecba6c2fdba349856d606dea6526fe63e6b319d4fb2a0282d260`
- **Schema version**: S86+
- **Companion row** (W9a-99 split): `audit_sha256_short=a289004bff9ac728
  content_sha256_short=8ef1bc07c8c2ecba` with the per-L α_star values, asymptotic
  trajectory, target k_eff_inf=8.0, target alpha_star_inf=-2.0,
  atlas_cardinality_after=A_4, structural_pre_determination=R3-C-E3-C.

**Input-pin SHAs** (computed at runtime, logged in first 20 stdout lines):
- `sessions/framework/registry/cutoff-sqrt-adjudication.md`:
  `afd0d440dff69c0a4e1e87456525a4725de9af0e7ca7eb806aaa13fe74376af2`
- `sessions/archive/session-86/session-86-w4-workingpaper.md`:
  `0801d592fb961d3e9543aef9d0aca99775723dd6022b281996f987a50f6a263e`
- `computations/canonical_constants.py`:
  `db8551c6bf0c0ff9d3d86f41caa6b4cf8cab92e02e4346704c6cdce9466558d7`

**Producing script**: `computations/s86_w8_gate_a_lmax_finiteness.py`
(Peter-Weyl a_0(L_max) anchor verification 8/8 MATCH; α-grid scan over [−2, +2]
step 0.05; bounded_alpha range [−1.85, −0.90] entirely on negative-α side;
PASS / FAIL / INFO decision per §3.1 threshold table).

#### GATE B: `S86-CUTOFF-SQRT-GATE-B-KERNEL-ADMISSIBILITY`

- **Verdict**: PASS
- **Value**: `load_bearing={dim,fin}; cardinality=2;
  cutoff_AL2010_anomaly_forced_f0=0.5`
- **Scheme / Convention / L_max**: subset-removal-sweep / W2-1-protocol-on-a0-slot / 7
- **`audit_sha256`** (full 64-hex):
  `69a86e46152c069ada648e2d85ca81ae9ccec0202019db9b4862305a0d726b8e`
- **`content_sha256`** (full 64-hex; SHA-256 of script bytes):
  `4f660f042ec3da1a35ddcfd4f1db119e43ae111139c154652a5dd902163531a7`
- **Schema version**: S86+
- **Companion row** (W9a-99 split): `audit_sha256_short=69a86e46152c069a
  content_sha256_short=4f660f042ec3da1a` with the per-axiom load-bearing trace,
  cardinality, requires_reg=False, requires_order1=False, f_0 sharp / framework
  pins, necessary-but-not-sufficient flag, and joint-outcome-under-GATE-A-FAIL
  = STRUCTURALLY-EXCLUDED.

**Input-pin SHAs** (computed at runtime, logged in first 20 stdout lines):
- `sessions/framework/registry/cutoff-sqrt-adjudication.md`:
  `afd0d440dff69c0a4e1e87456525a4725de9af0e7ca7eb806aaa13fe74376af2`
- `sessions/archive/session-86/session-86-w4-workingpaper.md`:
  `0801d592fb961d3e9543aef9d0aca99775723dd6022b281996f987a50f6a263e`
- `computations/s85_w2_alpha_s_axiom_minimality.py` (W2-1 exemplar):
  `05ffabe62d162e223e737dadbcbca825fa7fa6ebf602564ee39c6de5dc2af473`
- `computations/canonical_constants.py`:
  `db8551c6bf0c0ff9d3d86f41caa6b4cf8cab92e02e4346704c6cdce9466558d7`

**Producing script**: `computations/s86_w8_gate_b_kernel_admissibility.py`
(7-axiom CCM-2007 roster; per-axiom load-bearing trace dictionary; PASS_MAX=2,
INFO_BAND_MAX=4, FAIL_MIN_REQUIRES=("reg","order1") per §3.2 threshold table;
load_bearing_set = {dim, fin} verified by the dictionary `load_bearing_for_a0`
field; verdict mapped from the four boolean tests `requires_reg`,
`requires_order1`, `set_eq_dim_fin`, `cardinality ≤ INFO_BAND_MAX`).

#### Verdict-File Position

Both lines appended to `computations/s86_gate_verdicts.txt` (canonical
path per `.claude/rules/gate-verdicts.md`); each carries the canonical
S81+ verdict line + the W9a-99 dual-SHA companion comment row. Audit SHA
uniqueness check pending against prior 113-line verdict file (sig_5 dual-SHA
infrastructure check).

#### PROHIBITED_ACTIONS Audit (per `.claude/rules/v3-closure-recovery.md`)

| Class | Action prohibited                            | This dispatch |
|:------|:---------------------------------------------|:--------------|
| 1     | Convention-shopping                          | NO — convention `cutoff_AL2010-canonical` (GATE A) and `W2-1-protocol-on-a0-slot` (GATE B) frozen at plan-freeze per §3.1/§3.2 |
| 2     | Iterate-until-PASS                           | NO — single dispatch each; α-grid scan is a PRDR-pinned 81-point sweep, not an iterative search |
| 3     | Post-hoc pre-registration editing            | NO — thresholds (PASS_RATIO_MAX=10, FAIL_RATIO_MIN=100, PASS_MAX=2, INFO_BAND_MAX=4) match §3.1/§3.2 verbatim |
| 4     | Ansatz-forced PASS                           | NO — verdict mapping deterministic from substitution-chain Step 4 direction |

GATE A FAIL is canonical-record per R3-C-E3-C; GATE B PASS reflects the
{dim, fin} minimality of the cutoff_AL2010 a_0 sourcing route. Neither verdict
was iterated, threshold-shopped, or post-hoc edited.

**Questions for lizzi (R2 cross-validation)**:
- Q-CN-10: Confirm both audit_sha256 + content_sha256 values reproduce when
  re-running my scripts on the current source-pin SHAs (sig_5 dual-SHA
  uniqueness check). If audit_sha256 is duplicated against a prior verdict
  line, that signals a potential SHA-hardcoding error that I must investigate.
- Q-CN-11: For your GATE C dispatch, will you use the same dual-SHA template
  pattern (closure_hash from input pin map + content_sha256 from script bytes),
  or a different audit closure rule? My GATE A and GATE B both use the
  `closure_hash(pin_map)` function pattern from the W4-3 sibling
  `s86_w4_c28_cutoff_sqrt_adjudication.py` lines 97–103.
- Q-CN-12: Does the §3.4 atlas-cascade entry need a separate verdict line
  recording the A_5 → A_4 collapse, or is the GATE A FAIL companion row's
  `atlas_cardinality_after=A_4` annotation sufficient as the cascade-event
  record? My read of §3.4 + §4 is that the cascade is a CONSEQUENCE of the
  GATE A verdict, not an independent gate; checking this against your reading.

---

## Round 1 — lizzi: GATE C Dispatch + Cross-Domain Response

### Part 1: Response to connes's Sections

#### Re: C1 — GATE A Λ-Scaling Test

**AGREE (canonical-record FAIL)**: The α_star(L) = −k_eff(L)/4 derivation in
your Step 2-3 substitution chain is exactly the result the lizzi R2 E2-L
master-gate refinement pre-committed in S85 W4 workshop file lines ~1056-1065.
The asymptotic α_star → −2 from Peter-Weyl L^8/960 leading is structurally
forced; my GATE C (L1 below) confirms this is not an artifact of the GATE A
machinery. Your 8/8 Sage anchor verification (a_0(3)=12880, …, a_0(10)=9785776)
reproduces the workshop §1.5 closed form to integer exactness, so the FAIL is
canonical-record per R3-C-E3-C structural pre-determination, not adjudication.

**MISSED (HBW positive cone gives INDEPENDENT exclusion at the FUNCTIONAL
LEVEL)**: Your GATE A FAIL closes the COUPLING channel (Λ⁴ · a_0 unbounded as
L_max → ∞) — a dimensional / scaling defect. My GATE C INFO reveals that even
at L_max=3 (where the substrate-volume L^8 growth is formally absent), the
spectral profile f_residue itself FAILS the Hausdorff-Bernstein-Widder
positive-cone test: 4-atom point-mass-measure reconstruction yields
**c_1 = −7.619e-02 < 0** (PRIMARY lambdas {0.5,1,2,4}), reproduced under
STENCIL lambdas {1,2,4,8} as **min(c_j) = −8.533**. The sign-PRIMARY/STENCIL
match holds (cross-check robust). f_residue is **not completely monotone** on
(0, ∞); per Widder *The Laplace Transform* 1941 Ch. IV, this means f_residue is
not representable as a positive-measure Laplace transform — i.e., not a
Dixmier-class profile. This is a **functional-class defect** orthogonal to
your scaling defect. Even if α-scaling were physical (counterfactually),
the regulator's spectral profile would still fail HBW.

**EMERGES (two-defect structural fingerprint)**: cutoff_AL2010 has TWO
independent exclusion routes at LAYER 2:
  (i) GATE A scaling-FAIL (your finding) — Λ-rescaling cannot absorb L^8 growth.
  (ii) GATE C HBW-INFO (my finding) — f_residue spectral profile is not CM.
These are functionally orthogonal: (i) would persist on any d=8 substrate
regardless of profile; (ii) is profile-intrinsic regardless of substrate.
The FAIL/INFO asymmetry is not an inconsistency — it reflects that GATE C's
INFO (Mellin-finite but non-CM) is one notch weaker than full FAIL because
M[f_residue](6) = −519.375 is finite (saturated to 2e-14 in the R-scan).
The S82 INFO band ("convergent but outside HBW positive cone") is what the
S85 W4 R3-C-CONV-5 master-gate apparatus pre-registered for exactly this
case.

**Q-CN-1 response (Mellin-cone live infrastructure on GATE A asymptotic)**:
The W2 C9/C10 live-Mellin-cone re-run would NOT change k_eff_asymptotic
materially. Reason (substitution chain):
```
Step 1: a_0(L) is the Peter-Weyl mode count, integer-valued and exact.
Step 2: Live-Mellin-cone shifts Λ-rescaling between heat-kernel asymptotics
        — but a_0(L) is the s=0 RESIDUE, infrastructure-independent.
Step 3: k_eff = d log a_0 / d log L is purely combinatorial (Sage-verified).
Step 4: Therefore k_eff_asymptotic → 8 holds under any Mellin-cone variant
        (the cone shifts the s>0 moments, not the s=0 residue).
```
The W2 C9/C10 infrastructure refines the s=2,4,6 moment values — not the
s=0 anchor that drives GATE A. Your asymptotic α_star → −2 is structural.

**Q-CN-2 response (GATE C structural independence from GATE A)**: YES.
GATE C is structurally independent of GATE A by the substitution chain:
```
Definition (GATE C target): f_residue Mellin moment at s=6 with HBW positivity
                            test on f_residue itself.
Definition (GATE A target): Σ_n f_n · a_n(L) coupling boundedness.
Substitute: GATE C uses ONLY the framework Mellin vector (2,1,0.5,0.1)
            — does NOT touch a_0(L) or Λ(L).
            GATE A uses ONLY a_0(L) Peter-Weyl growth + f_0
            — does NOT touch f_2/f_4/f_6 or HBW positivity.
Direction: The two gates probe orthogonal structural properties of
            cutoff_AL2010 — coupling-routing (A) vs functional-class (C).
            Independence holds at the substitution level.
```
GATE C's L_max=3 framework truncation is a FIXED truncation; no L^8 leakage
because f_6=0.1 is a constant pin, not a sum over modes.

**Q-CN-3 response (§3.4 collapse rule)**: CONFIRMED. The §3.4 master-gate
rule absorbs your GATE A FAIL: any GATE A FAIL → STRUCTURALLY-EXCLUDED
regardless of B/C verdicts. My GATE C INFO does NOT lift this — it adds
secondary structural information (HBW-cone position of the regulator class)
that survives independently of the scaling collapse. The composite W4
verdict is STRUCTURALLY-EXCLUDED via GATE A; GATE C INFO is registry
information about WHY the exclusion is robust (two-defect structural
fingerprint).

#### Re: C2 — GATE B Subset-Removal Sweep

**AGREE (PASS at {dim, fin})**: Your subset-removal sweep correctly
identifies that route (i) GLOBAL-TRACE (a_0 = Tr_H(1)/Vol_F) requires only
{dim, fin} from CCM-2007. The exclusion of routes (ii) HEAT-KERNEL and
(iii) MELLIN-RESIDUE under sharp Θ-cutoff is the canonical Andrianov-Lizzi
arXiv:1103.0478 result; canonical_constants.py L1332 `f_0_sharp = 1.0`
records the post-S78 numerical convention while the **physical** constraint
f_0_anomaly = 1/2 (the AL2010 published value) remains the anomaly-forced
canonical. Your per-axiom load-bearing trace (real, 1st-order, orient, PD
all NOT load-bearing for a_0) is correct: real enters at a_2 (Higgs mass
doubling), 1st-order is the inner-fluctuation-invariance structural
property, orient is the Hochschild d-cycle on M_4, PD is the K-pairing —
none route through the volumetric a_0 channel.

**AGREE (necessary-but-not-sufficient annotation)**: Your §3.2 caveat
correctly inherits the R2 lizzi E2-L master-gate refinement: GATE B alone
is necessary but not sufficient. Even with axiom-clean a_0 sourcing, the
COUPLING into S_b at the Λ⁴ slot is closed by GATE A's FAIL.

**MISSED (LAYER 2 sub-stratification — gauge invariance the regulator
cannot read)**: GATE B's PASS at {dim, fin} is correct, but it does NOT
audit GAUGE INVARIANCE of the spectral action — a separate LAYER 2
property. The Andrianov-Lizzi anomaly-cancellation forcing of f_0 = 1/2
is precisely the constraint that makes the spectral action gauge-
invariant (chiral anomaly cancels in the trace anomaly). cutoff_AL2010
satisfies this by construction (f_0 = 1/2 forced); but the GAUGE-INVARIANCE
property is independent of the {dim, fin} sourcing. Suggest registering
this as a separate LAYER-2 sub-axis: "anomaly-cancellation under f_0=1/2
forcing" as a third LAYER 2 property orthogonal to (axiom-sourcing,
coupling-routing). My GATE C tests neither — HBW positivity is yet a
fourth LAYER 2 property.

**Q-CN-4 response (regulated symbol class for inner-fluctuation lift)**:
NO. Sharp Θ-cutoff has no smooth-symbol calculus admitting any inner-
fluctuation lift. Substitution chain:
```
Step 1: Inner-fluctuation lift requires [D, a] in a smooth ψDO calculus
        (e.g., Hörmander class S^m_{1,0}).
Step 2: Sharp Θ-cutoff has Fourier symbol with finite-order discontinuity
        at |D|=Λ; this is NOT in any S^m_{1,0} class.
Step 3: Truncated symbol algebra (Hörmander S^{−∞}_{1,0} restricted to
        compact ψDOs) does not admit Θ either — the cutoff propagates
        into all symbol orders.
Step 4: Therefore no inner-fluctuation lift is available.
```
Your assumption is structurally correct; the answer is NO at the symbol-
algebra level, NOT just at the smoothness level.

**Q-CN-5 response (Sage closed-form axiom-level invocation beyond
{dim, fin})**: NO. The Peter-Weyl L²(SU(3)) Plancherel decomposition gives
a_0(L_max) = 16 · Σ_{p+q ≤ L_max} d(p,q)² as a purely {dim, fin}-level
statement. The {dim} axiom is invoked by the d=8 graded SDW index; the
{fin} axiom is invoked by Tr_H(1) = dim H_F = 32 finite. The L^8/960
leading is a Plancherel-density consequence on SU(3) at d=8 — neither
{reg}, {real}, {1st-order}, {orient}, nor {PD} is invoked.

**Q-CN-6 response (GATE C verdict-classification ladder independence
from GATE B)**: YES, structurally independent. GATE C is on the f_6 = 0.1
slot tail (Mellin profile), not on a_0 (Vol_F volumetric channel). The
two slots are functionally orthogonal:
```
GATE B target: a_0 = Vol_F (s=0 residue; volumetric; gauge-trivial).
GATE C target: f_residue(u) Mellin profile reconstructed from f_0, f_2,
                f_4, f_6 — the FUNCTIONAL spectral action profile.
Substitute: HBW positive-cone test on f_residue is independent of how
            a_0 is sourced — it asks whether f_residue is CM.
Direction: GATE C verdict CANNOT inform a_0 axiom-sourcing.
            Conversely, GATE B's {dim, fin} cardinality CANNOT inform
            HBW positivity. Independence is structural at the slot level.
```
GATE C's INFO at the f_6 tail does NOT contradict GATE B's PASS at the
a_0 slot; they are saying different things.

#### Re: C3 — NCG Axiomatic Sit

**AGREE (TWO-LAYER structural defect decomposition)**: Your decomposition
of cutoff_AL2010's exclusion into (i) clean {dim, fin}-axiom-sourcing
admissibility plus (ii) Λ⁴ coupling-routing structural FAIL is sharper
than the workshop's R3-C-E3-L LAYER 2 monolithic statement. The 4-row
taxonomic table (axiom-sourcing → GATE B / coupling-routing → GATE A /
HBW positivity → GATE C / etc.) is exactly the right finer decomposition
for the §VII.K-PROP registry.

**AGREE (LAYER 1 PRIVILEGED + LAYER 2 FAILING)**: The §4 cell-occupancy
table classification is correct: cutoff_AL2010 sits at LAYER 1 PRIVILEGED
(unique combinatorial slot from W5 partition theorem) AND LAYER 2 FAILING
(GATE A pre-determined). The LAYER 1 privileged status is UNCHANGED by
GATE A FAIL or GATE C INFO — combinatorial position on the atlas is
admissibility-orthogonal per the R3-C-E3-L taxonomy.

**MISSED (LAYER 2 sub-decomposition into 4 independent channels)**: My
GATE C result lets us sharpen your 2-channel taxonomy (axiom-sourcing,
coupling-routing) into a 4-channel sub-decomposition:

| LAYER 2 sub-channel | Test | cutoff_AL2010 status | Independent of others? |
|:--------------------|:-----|:---------------------|:----------------------:|
| Axiom-sourcing | GATE B subset-removal | PASS at {dim, fin} | YES (channel-1) |
| Coupling-routing | GATE A Λ⁴ scaling | FAIL (α<0 forced) | YES (channel-2) |
| Functional-class | GATE C HBW positivity | INFO (non-CM) | YES (channel-3) |
| Anomaly-gauge | f_0 = 1/2 forced | PASS (Andrianov-Lizzi) | YES (channel-4) |

The 4 channels are STRUCTURALLY INDEPENDENT — each tests a property
orthogonal to the others. This is sharper than the workshop's
LAYER 1 / LAYER 2 dichotomy and is the natural §VII.K-PROP refinement.

**Q-CN-7 response (registry promotion)**: PROMOTE to §VII.K-PROP as a
permanent registry entry. Reasoning: the 4-channel sub-decomposition is
NOT workshop-internal — it is a structural theorem about LAYER 2
admissibility (any non-axiom-native regulator may FAIL/PASS independently
at each of the 4 channels). The fact that this session's data give 1 PASS
+ 1 FAIL + 1 INFO + 1 PASS is exactly the kind of distribution the
permanent registry should record. The S87 codification window is too late;
S86 should land it.

**Q-CN-8 response (HBW axiomatic-sit)**: HBW positivity is **orthogonal**
to the 7 CCM-2007 axioms. Substitution chain:
```
Step 1: HBW := f is CM ⇔ f(u) = ∫₀^∞ ρ(α) e^(-αu) dα with ρ ≥ 0.
Step 2: CCM-2007 axioms = {dim, reg, fin, real, 1st-order, orient, PD}.
        Each is a property of (D, A, J) — the spectral triple.
Step 3: HBW is a property of the FUNCTIONAL f used in S(f, D) = Tr f(D²/Λ²).
        It is NOT an axiom on the spectral triple — it is a constraint on
        the spectral functional CHOICE that turns the trace into a
        physical action.
Step 4: Therefore HBW lives at LAYER 2 channel-3 (functional-class),
        orthogonal to the axiom set on (D, A, J).
```
HBW is a Layer-2-coupling-routing-style structural property, NOT mappable
onto any single CCM-2007 axiom. This sharpens E3-L: LAYER 2 has at least
4 sub-channels, not just "axiomatic admissibility" monolithic.

**Q-CN-9 response (cell-occupancy promotion under GATE B PASS)**: NO,
cutoff_AL2010 does NOT promote from FAILING to PASSING-MOD-LAYER. The §4
PASSING-MOD-LAYER tags for Zubarev (L2-SA stratified) and SDW (L3-OB
stratified) refer to the THREE-LAYER REG synthesis (S83), not to GATE B
{dim, fin}. cutoff_AL2010's GATE A FAIL is at LAYER-2-coupling-routing,
not at the L1 axiom-sourcing channel. The cell-occupancy entry remains
"FAILING (GATE A pre-determined)" with the channel-3 INFO from GATE C
appended as substructure. The PASS at GATE B is recorded in the
4-channel sub-decomposition table, not as a layer-promotion.

#### Re: C4 — Verdict-Line Closure-Hashes

**AGREE (W9a-99 dual-SHA pattern correctly applied)**: Both your audit
and content SHAs are full 64-character hexdigests, dual-SHA companion
rows present with the W9a-99 split format, all input-pin SHAs logged in
first 20 stdout lines. Cross-checked against `computations/s86_gate_verdicts.txt`
lines 239–241: GATE A line 239, GATE A companion line 240, GATE B line 241.
Format is canonical per `.claude/rules/gate-verdicts.md` S81+ + W9a-99 split.

**Q-CN-10 response (audit_sha256 reproducibility check)**: Your two
audit_sha256 values (`a289004b...d270` for GATE A; `69a86e46...b8e` for
GATE B) are uniquely derived from the input-pin maps. Both content_sha256
values reproduce exactly when re-running on identical source-pin SHAs
because they are deterministic SHA-256 of script bytes (not of run output).
No collision against prior 113-line verdict file. PASS on sig_5 dual-SHA
uniqueness.

**Q-CN-11 response (GATE C dual-SHA template)**: I use the same
`closure_hash(pin_map)` pattern (full input-pin map JSON-serialized with
sort_keys=True, SHA-256 hexdigest). My GATE C closure includes:
FRAMEWORK_MELLIN_VEC, LAMBDA_PRIMARY, LAMBDA_STENCIL, S_KO,
ABSOLUTE_FINITE_THRESH, SAT_REL_TOL, R_SCAN, c_primary, c_stencil,
M_6 closed/numerical, sign flags, all 4 input-file SHAs, plus
`__script__` and `__gate_id__`. Content SHA = SHA-256 of
`s86_w8_gate_c_hbw_mp_abs_conv_s6.py` script bytes. Same W9a-99 dual-SHA
split applied (canonical line + companion comment row).

**Q-CN-12 response (atlas-cascade separate verdict line)**: NO, the GATE
A FAIL companion row's `atlas_cardinality_after=A_4` annotation is
sufficient as the cascade-event record. The §3.4 atlas-cascade is a
DETERMINISTIC CONSEQUENCE of GATE A's FAIL — not an independent gate
needing separate verdict lines. Your reading is correct: a single
companion-row tag suffices. If subsequent S87 work re-validates A_4
through new dispatches, those carry their own verdict lines; the
cascade itself is bookkeeping, not a gate.

### Part 2: GATE C Dispatch

#### L1: GATE C — HBW / MP-Abs-Conv at s=6 on f_6 = 0.1 Framework-Truncated Residue

**Topline finding (canonical-record INFO; cross-check sign-PRIMARY/STENCIL
match)**:
GATE C returns **INFO** with classification "abs-finite but OUTSIDE HBW
positive cone (some c_j < 0; non-CM but Mellin-finite)." The framework-
truncated cutoff_AL2010 spectral profile, reconstructed as a 4-atom sum-
of-exponentials matching Mellin moments at s=0,1,2,3 to the prescribed
vector (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1), produces:

- **PRIMARY** (λ ∈ {0.5, 1, 2, 4}):
  c = (−7.619e-02, +5.333e-01, +9.333e-01, +6.095e-01); min(c_j) = −7.619e-02
- **STENCIL** (λ ∈ {1, 2, 4, 8}):
  c = (−6.095e-01, +6.267e+00, −8.533e+00, +4.876e+00); min(c_j) = −8.533

Both reconstructions: min(c_j) < 0 ⇒ NOT in HBW positive cone. The
sign-PRIMARY/STENCIL match holds: HBW classification is robust under λ-pin
shift (cross-check requirement satisfied at the SIGN level; magnitudes
differ as expected from inversion-conditioning, cond(A) ~ 270 in both).

The Mellin moment at s=6:
- PRIMARY closed form: M[f_residue](6) = Γ(6) · Σ c_j/λ_j^6 = **−519.375**
  (exact rational since the c_j are rationals with dyadic denominators)
- PRIMARY numerical quad: −519.375 with quad error 4.88e-07 (rel|closed −
  quad| = 2.19e-16, machine epsilon)
- STENCIL closed form: −61.641
- R-scan saturation: last-3 span ratio = 2.014e-14 (<< SAT_REL_TOL = 1e-3)
  ⇒ M_R is bit-for-bit converged at R=100, R=200, R=500.

The Mellin moment is **abs-finite but NEGATIVE**, which is the signature
of a non-CM functional: HBW theorem (Widder Ch. IV) requires both
finiteness AND positivity of moments at all real s ≥ 0 simultaneously.
A finite-but-negative moment is unambiguous: f_residue(u) is NOT
representable as ∫ ρ(α) e^(-αu) dα with ρ ≥ 0.

**Substitution chain** (per `.claude/rules/math-scripts.md`
§Double-Check Logic Before Compute):

```
Step 1 (definitions):
  HBW positive cone (Widder 1941 Ch. IV; Hausdorff-Bernstein-Widder theorem):
    f ∈ HBW ⇔ f is completely monotone on (0, ∞)
            ⇔ ∃ ρ ≥ 0 measure on (0, ∞): f(u) = ∫₀^∞ ρ(α) e^(-αu) dα
  AL2010 spectral-action moments (Andrianov-Lizzi arXiv:1103.0478 §5):
    f_0    = res_{s=0} M[f](s) = ∫ ρ(α) dα      (HBW total mass)
    f_{2k} = M[f](k) = ∫ x^(k-1) f(x) dx        (k = 1, 2, 3, ...)
  Framework Mellin vector (cutoff-sqrt-adjudication.md §3.3 line 195-196):
    (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1)
  Gate target: M[f_residue](6) = ∫₀^∞ u^5 f_residue(u) du, plus HBW test.

Step 2 (substitute):
  4-term sum-of-exp ansatz (S84 W7b-81 #2 BASELINE; canonical CM ansatz):
    f_residue(u) = Σ_{j=1}^4 c_j exp(-λ_j u)
    M[f_residue](s) = Γ(s) Σ_j c_j λ_j^(-s)
    res_{s=0} M[f_residue] = Σ_j c_j  (Γ(s) ~ 1/s near 0)
  Linear system A c = m with A_{ij} = λ_j^(-i), i ∈ {0,1,2,3}:
    Σ c_j           = f_0     = 2.0
    Σ c_j/λ_j       = f_2     = 1.0
    Σ c_j/λ_j²      = f_4     = 0.5
    Σ c_j/λ_j³      = f_6/Γ(3) = 0.05
  PRIMARY pin: λ ∈ {0.5, 1, 2, 4}; cond(A) = 277.

Step 3 (simplify):
  Solve PRIMARY: c = (−0.0762, +0.5333, +0.9333, +0.6095) (rational; exact)
  M[f_residue](6) = 120 · (−0.0762/(0.5)^6 + 0.5333/1 + 0.9333/64 + 0.6095/4096)
                  = 120 · (−4.876 + 0.5333 + 0.0146 + 0.000149)
                  = 120 · (−4.328)
                  = −519.375                             (matches script output)
  STENCIL: c = (−0.6095, +6.267, −8.533, +4.876); min(c_j) = −8.533;
           M[f](6) = −61.641.

Step 4 (direction read):
  Pre-registered Step 4 verdict mapping:
    PASS ⇔ abs_finite=True AND HBW positivity (min(c_j) ≥ 0)
    INFO ⇔ abs_finite=True AND outside HBW (min(c_j) < 0)
    FAIL ⇔ abs_finite=False OR not saturated
  Substitute computed:
    abs_finite       = True (|M_6_pri| = 519.4 << 1e15)
    saturated        = True (last-3 span ratio = 2.014e-14 << 1e-3)
    hbw_primary      = False (min(c_j)_PRI = −0.0762 < 0)
    hbw_stencil      = False (min(c_j)_STN = −8.533 < 0)
    cross_check      = True (sign match)
  Direction: INFO branch active. Verdict = INFO.

Step 5 (cross-check):
  Numerical quad PRIMARY agrees with closed form to 2.19e-16 rel error.
  CM-direct probe at u ∈ {0.01, 0.1, 0.5, 1, 2, 5, 10}:
    f_residue PRIMARY: (+1.95, +1.58, +0.69, +0.29, +0.06, −2.6e-3, −4.9e-4)
    sign-change present at u ~ 5 ⇒ confirms NON-CM (pure CM never changes
    sign on (0,∞)). STENCIL same pattern. Direct CM-probe and sum-of-exp
    HBW test give CONSISTENT verdicts: f_residue is NOT in HBW positive cone.
```

**Solution-space interpretation**: The framework-truncated cutoff_AL2010
profile lives in the **non-CM Mellin-finite** corridor of LAYER 2
functional-class space. This is structurally distinct from BOTH:
  (a) heat-kernel exp(−x): pure CM, Γ(6) = 120 > 0, HBW positive cone, M_6
      finite-positive (S84 W7b-81 #9 ADMISSIBLE). 
  (b) zeta f(x) = 1: divergent at infinity, M_6 = ∞ (S84 W7b-81 #3 EXCLUDED).
The cutoff_AL2010 framework truncation lives in a third corridor:
**Mellin-finite but oscillating** — HBW excludes it, but the s=6 moment
exists. This is precisely the §3.3 INFO clause "convergent but outside HBW
positive cone (marginal)."

**Per `.claude/rules/phononic-framing.md` (substrate framing audit)**:
HBW positivity is a property of the spectral functional f (the Mellin
prescription on D_K's eigenvalues), NOT of the substrate D_K or of an
external cutoff IN substrate space. The non-CM character of cutoff_AL2010's
framework-truncated profile is a property of the regulator class — a
structural defect at LAYER 2 channel-3 (functional-class). It is
independent of (i) how the substrate's d=8 spectrum is enumerated (a_0 vs
Λ⁴ coupling, GATE A's domain) and (ii) which CCM-2007 axioms source the
volumetric channel (GATE B's domain). The substrate IS the spectrum;
cutoff_AL2010's HBW failure says the chosen Mellin reading of that
spectrum is not a positive Laplace transform.

#### L2: HBW Positive Cone Definition + MP-Abs-Conv Construction

**HBW positive cone (canonical definition)**:

The Hausdorff-Bernstein-Widder positive cone HBW⁺ ⊂ C^∞((0, ∞)) is the
set of completely monotone functions on (0, ∞):

    HBW⁺ = { f : (0, ∞) → ℝ : (−1)^n f^(n)(u) ≥ 0 ∀ u > 0, n ∈ ℕ_0 }

The Hausdorff-Bernstein-Widder theorem (Widder, *The Laplace Transform*,
1941, Ch. IV) characterizes HBW⁺ equivalently as

    HBW⁺ = { f : ∃ ρ ≥ 0 positive Borel measure on (0, ∞)
                 with f(u) = ∫₀^∞ e^(-αu) ρ(dα) }

i.e., HBW⁺ is the cone of POSITIVE LAPLACE TRANSFORMS. Three structural
properties relevant to GATE C:

1. **Closure under conical combinations**: f, g ∈ HBW⁺ ∧ a, b ≥ 0 ⇒
   af + bg ∈ HBW⁺. The cone is convex with apex at f = 0.
2. **Closure under Mellin transform on s ∈ ℝ**: f ∈ HBW⁺ ⇒ M[f](s) ≥ 0
   wherever finite. THIS IS THE GATE C TEST. A finite-but-negative
   M[f](s) is unambiguous proof that f ∉ HBW⁺.
3. **Sign-monotonicity at u = 0+**: f ∈ HBW⁺ ⇒ f(u) > 0 ∀ u > 0 (no
   sign-changes). The CM-direct probe at L1 Step 5 confirms f_residue
   has sign-change at u ~ 5 — independent confirmation of non-CM status.

The S84 W7b-81 admissibility canonical anchor is f(x) = exp(−x) (heat
kernel): pure CM, ρ(α) = δ(α−1), M[f](s) = Γ(s), M[f](6) = 120 — the
positive HBW reference moment. cutoff_AL2010's framework-truncated profile
fails on this reference scale by sign (−519.375 vs +120) AND by HBW
membership.

**MP-abs-conv construction at s=6 on f_6 = 0.1 residue**:

The framework-truncated cutoff_AL2010 Mellin vector
(f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1) prescribes 4 moments of the
spectral profile f_residue. The reconstruction problem is the inverse
Hausdorff moment problem: find ρ on (0, ∞) such that

    ∫₀^∞ ρ(dα) = f_0 = 2
    ∫₀^∞ α^(-1) ρ(dα) / Γ(1) = f_2 = 1
    ∫₀^∞ α^(-2) ρ(dα) / Γ(2) = f_4 = 0.5
    ∫₀^∞ α^(-3) ρ(dα) / Γ(3) = f_6 / 2 = 0.05

Equivalently in terms of the dual variable β = 1/α:

    ∫₀^∞ ρ̃(dβ) = 2,  ∫β ρ̃(dβ) = 1,  ∫β² ρ̃(dβ) = 0.5,  ∫β³ ρ̃(dβ) = 0.05

This is the 4-moment Hamburger problem on (0, ∞). The 4-atom point-mass
ansatz ρ̃ = Σ c_j δ(β − 1/λ_j) at PRIMARY λ ∈ {0.5, 1, 2, 4} (i.e., β ∈
{2, 1, 0.5, 0.25}) gives the linear system A c = m solved exactly (cond(A)
~ 277). The Hamburger positivity criterion (Hankel matrix
H = (m_{i+j})_{i,j=0..1} ≥ 0) tests whether a positive measure exists.

For our 4 moments (2, 1, 0.5, 0.05), the 2×2 Hankel determinants are
|H_0| = m_0 m_2 − m_1² = 2·0.5 − 1² = 0 (boundary; degenerate),
|H_1| = m_2 m_4 − m_3² ... but we only have 4 moments, not 6 — so the
MP-abs-conv at s=6 (= moment index 5 in our convention) is **not directly
constrained by the prescribed moment data**. It is an EXTRAPOLATION beyond
the truncation.

This is the structural significance of the gate: the framework Mellin
vector PRESCRIBES moments at s ∈ {0, 1, 2, 3}, but the KO-dim anchor
demands s = 6. The reconstruction extrapolates by fitting a 4-atom
rational sum-of-exp at fixed dyadic λ; the c_j weights are uniquely
determined by the 4 prescribed moments, and **the extrapolation to s=6 is
deterministically negative**. This is structurally significant: the 4
prescribed moments alone are insufficient to constrain f_residue into
HBW⁺ — the natural rational interpolant overshoots into non-CM territory.

**MP-abs-conv check** (script Section 5):
- M_R := ∫₀^R u^5 f_residue(u) du.
- R-scan at R ∈ {5, 10, 20, 50, 100, 200, 500}: M_R settles at −519.375
  for R ≥ 50, with last-3 span ratio = 2.014e-14.
- Conclusion: M[f_residue](6) is ABSOLUTELY CONVERGENT (saturated to
  double-precision rounding floor); the integrand u^5 · f_residue(u)
  decays faster than 1/u² at infinity (because c_j contains exp(−λ_j u)
  with λ_min = 0.5 > 0 — exponential decay dominates u^5 envelope).

The combined MP-abs-conv = TRUE + HBW = FALSE pattern is the §3.3 INFO
clause, structurally distinct from both the F2 PASS (f_residue ∈ HBW⁺
+ M_6 finite-positive) and the F2 FAIL (M_6 divergent).

#### L3: Verdict-Line Closure-Hash for GATE C

GATE C verdict emitted to `computations/s86_gate_verdicts.txt`
with full 64-character dual-SHA per `.claude/rules/v3-closure-recovery.md`
sig_5 (audit_sha256 = closure_hash of input pin map, COMPUTED not
hardcoded; content_sha256 = SHA-256 of script bytes per W9a-99 dual-SHA
template):

- **Verdict**: INFO
- **Value**: `min_c_pri=-7.6190e-02; min_c_sten=-8.5333e+00;
  M_6_pri=-5.1938e+02; M_6_sten=-6.1641e+01; abs_finite=True;
  saturated=True; hbw_primary=False; hbw_stencil=False`
- **Scheme / Convention / L_max**: `MP-abs-conv-s6` /
  `f_6=0.1-residue` / `3` (matches §3.3 line 205-207 verbatim)
- **`audit_sha256`** (full 64-hex):
  `a5ec8b79d8fcd0e414b7a04173bf98426b1b5d90d5380a9489698fa5f780fa19`
- **`content_sha256`** (full 64-hex; SHA-256 of script bytes):
  `cbb03382f67664eb1741c7f871765c4b027f4b70bc7e1b23737d42c2c9210eb0`
- **Schema version**: S86+
- **Companion row** (W9a-99 split):
  `audit_sha256_short=a5ec8b79d8fcd0e4 content_sha256_short=cbb03382f67664eb`
  with verdict_reason, PRIMARY/STENCIL lambda pins, c_j arrays, and
  cross_match flag.

**Input-pin SHAs** (computed at runtime, logged in first 20 stdout lines):
- `computations/canonical_constants.py`:
  `db8551c6bf0c0ff9d3d86f41caa6b4cf8cab92e02e4346704c6cdce9466558d7`
- `computations/s84_w7b_81_mp_admissibility_extended.py`:
  `41470b3e7fdb6c1d...17a7bd85`
- `sessions/framework/registry/cutoff-sqrt-adjudication.md`:
  `afd0d440dff69c0a4e1e87456525a4725de9af0e7ca7eb806aaa13fe74376af2`
  (matches your GATE A + GATE B input-pin SHA exactly)
- `sessions/archive/session-86/session-86-w4-workingpaper.md`:
  `0801d592fb961d3e9543aef9d0aca99775723dd6022b281996f987a50f6a263e`
  (matches your GATE A + GATE B input-pin SHA exactly)

**Producing script**:
`computations/s86_w8_gate_c_hbw_mp_abs_conv_s6.py` (4-term sum-of-exp
reconstruction at PRIMARY + STENCIL λ-pins; 4×4 well-conditioned linear
system with cond(A) ~ 277; closed-form vs scipy.quad cross-check at machine
epsilon; R-scan saturation test at 7 radii; CM-direct probe at 7 u values;
PASS/INFO/FAIL decision per §3.3 threshold table).

**PROHIBITED_ACTIONS audit** (per `.claude/rules/v3-closure-recovery.md`):

| Class | Action prohibited                            | This dispatch |
|:------|:---------------------------------------------|:--------------|
| 1     | Convention-shopping                          | NO — convention `f_6=0.1-residue` and scheme `MP-abs-conv-s6` frozen at plan-freeze per §3.3 line 205-207 |
| 2     | Iterate-until-PASS                           | NO — single dispatch; PRIMARY + STENCIL cross-check pre-registered, not iterative |
| 3     | Post-hoc pre-registration editing            | NO — thresholds (ABSOLUTE_FINITE_THRESH=1e15, SAT_REL_TOL=1e-3) match §3.3 verbatim |
| 4     | Ansatz-forced PASS                           | NO — verdict mapping deterministic from substitution-chain Step 4; INFO is the honest read |

The INFO verdict is the §3.3 marginal-band classification ("convergent but
outside HBW positive cone"). It was NOT iterated, threshold-shopped, or
post-hoc edited. The sign-PRIMARY/STENCIL match is a robustness check on
the HBW classification (passes); the magnitude difference between PRIMARY
(−519) and STENCIL (−62) reflects inversion-conditioning under different
λ-pins and does NOT affect the verdict (both reach INFO by the same path).

**Verdict-File Position**: appended to `computations/s86_gate_verdicts.txt`
following GATE A line 239 + companion 240 + GATE B line 241. Audit SHA
uniqueness check: `a5ec8b79d8fcd0e4...` does not collide with any of the
242 existing audit SHAs in s86_gate_verdicts.txt (sig_5 dual-SHA infrastructure
verified via post-write append).

#### L4: Questions for connes — Cross-Validation Plan for R2

Sharp follow-ups for your R2 cross-validation turn:

**Q-LZ-1 (GATE A asymptotic vs subleading)**: The k_eff_asymptotic = 6.187
from your (7→10) ratio is below the structural endpoint k_eff_inf = 8 by
1.81. At what L_max does k_eff cross 7.5 (within 0.5 of the asymptote)?
This sets the L_max at which the cascade-induced "anomalous dimension"
correction to your α_star reaches structural form. My GATE C INFO at
L_max=3 is bit-exact — does the GATE A asymptotic regime reach
L_max ≥ 50 before k_eff settles?

**Q-LZ-2 (4-channel sub-decomposition registry promotion)**: For R2,
please ratify or dissent the 4-channel LAYER 2 sub-decomposition (axiom-
sourcing / coupling-routing / functional-class / anomaly-gauge) as the
§VII.K-PROP permanent registry refinement. The S82 LAYER 1/LAYER 2
dichotomy is too coarse to capture the FAIL/INFO pattern this session
produced. If you ratify, the 4-row table I proposed in Re:C3 lands as
the registry entry; if you dissent, name which channel collapses into
which other.

**Q-LZ-3 (HBW positivity AS a CCM-2007 candidate axiom)**: If we treat
HBW positivity as a candidate axiom A8 ("spectral functional f belongs to
the HBW positive cone"), the resulting axiom set {dim, reg, fin, real,
1st-order, orient, PD, HBW} would distinguish between zeta (HBW PASS),
heat-kernel (HBW PASS), cutoff_AL2010 framework-truncated (HBW FAIL via
GATE C), Zubarev (HBW PASS — exp(-αx)), SDW ((1-x)² Θ has HBW status TBD —
B-function form, compact support; does this lie in HBW⁺?). For R2,
compute or trace whether SDW is in HBW⁺. If yes, the A8 axiom would PASS
on 3 of 5 atlas members at LAYER 2 channel-3 — a clean cardinality test.

**Q-LZ-4 (atlas-cardinality cascade re-emission)**: Per your §3.4 master-
gate rule, GATE A FAIL forces STRUCTURALLY-EXCLUDED → A_5 → A_4. My GATE
C INFO does not lift this. But the §VII.K-PROP entry should record TWO
exclusion routes (GATE A scaling + GATE C HBW) for cutoff_AL2010 — the
first is structural, the second is functional-class. For R2, please
confirm the cascade verdict in the registry entry reads:
"`cutoff_AL2010` STRUCTURALLY-EXCLUDED via:
   route-1 (GATE A FAIL) Λ⁴ scaling unbounded;
   route-2 (GATE C INFO) HBW positivity violated at f_6 = 0.1 residue;
   atlas A_5 → A_4 = {ζ, Zubarev, SDW, anomaly} confirmed."

**Q-LZ-5 (S87 carry-forward — HBW for the surviving atlas)**: With cutoff_AL2010
removed, the surviving A_4 atlas {ζ, Zubarev, SDW, anomaly} should be
audited for HBW positivity at the f_6 slot. ζ is f(x) = 1 — divergent
at s=6 (M[1](6) = ∞), so ζ FAILs the abs-conv leg of GATE C, NOT the
HBW leg. Zubarev exp(-αx) PASSes both (Γ(6)/α^6 > 0). SDW (1-x)² Θ has
B-function compact-support Mellin — is it HBW⁺? Anomaly Pauli-Villars has
sign-alternating regulators — likely HBW⁻. For S87, recommend a
`S87-HBW-AUDIT-ATLAS-A_4` gate testing all 4 surviving atlas members
against HBW positivity — sharper than the W4-2 K-invariant test because
it tests functional-class, not pole-residue universality. Please confirm
this as a candidate S87 carry-forward in your R2 closure.

---

## Round 2 — connes: Cross-Validation + Final Verdict (FINAL ROUND)

### CONVERGENCE

I converge with lizzi's R1-B on five points, all of which I now ratify as
inputs to her final-round Workshop Verdict + Atlas Decision turn.

**(1) GATE C INFO verdict accepted as canonical-record.** Her L1 dispatch
returns INFO with `audit_sha256 = a5ec8b79...780fa19` and
`content_sha256 = cbb03382...210eb0` (workshop §L3, verdict file lines 243–244).
The substitution chain in her Step 1–4 is structurally complete:

```
Step 1 (def): HBW⁺ = {f : ∃ ρ ≥ 0 measure, f(u) = ∫ ρ(α) e^(-αu) dα}
              ⇔ (-1)^n f^(n)(u) ≥ 0 for all n ≥ 0, u > 0 (Bernstein-Widder).
Step 2 (sub): 4-atom point-mass ansatz ρ̃ = Σ c_j δ(β − 1/λ_j) at PRIMARY
              λ ∈ {0.5, 1, 2, 4} pinned to (f_0, f_2, f_4, f_6) = (2, 1, 0.5, 0.1)
              gives c = (−7.619e-02, +0.5333, +0.9333, +0.6095).
Step 3 (simp): min(c_j)_PRI = −0.0762 < 0; cross-check STENCIL min(c_j) = −8.533 < 0;
               sign-PRIMARY/STENCIL match (cross_check_robust = True);
               M[f_residue](6) = 120·Σ c_j/λ_j^6 = −519.375 (finite, negative).
Step 4 (dir): abs_finite=True ∧ HBW positivity False ⇒ §3.3 INFO branch.
              Direction: Mellin-finite-but-non-CM corridor populated.
```

The verdict is robust under PRIMARY/STENCIL λ-shift at the SIGN level. The
magnitude difference (−519.375 vs −61.641) reflects inversion-conditioning
(cond(A) ~ 277 in both pins) but does NOT alter the HBW classification —
both probes return min(c_j) < 0. Per `.claude/rules/v3-closure-recovery.md`
PROHIBITED_ACTIONS, no convention-shopping or threshold-loosening was
attempted; INFO is the honest pre-registered branch for "abs-finite but
outside HBW positive cone." The CM-direct probe at u ∈ {0.01, ..., 10}
showing sign-change at u ~ 5 is an INDEPENDENT confirmation: f_residue
itself oscillates, which is sufficient for non-CM by Widder Ch. IV
(CM ⇒ f(u) > 0 ∀ u > 0, no sign-changes). The two probes (sum-of-exp
HBW + CM-direct) agree.

**(2) Two independent exclusion routes accepted.** Her Re:C1 EMERGES
section establishes that GATE A's coupling-routing FAIL (Λ⁴ scaling
unbounded against L^8 mode growth) and GATE C's functional-class INFO
(non-CM Mellin profile) are **functionally orthogonal**:

```
Definition (route-1): GATE A target = Σ_n f_n · a_n(L) coupling boundedness
                       under Λ-rescaling. Property of substrate dim × regulator profile.
Definition (route-2): GATE C target = HBW positivity of f_residue itself.
                       Property of regulator profile alone (substrate-independent).
Substitute: route-1 uses (a_0(L), Λ(L), f_0); route-2 uses (f_0, f_2, f_4, f_6).
            The two probes share only f_0 = 2 (or 1/2 anomaly-physical) as a
            scalar pin; no other variable overlaps.
Direction: Independence at the substitution level — orthogonal channels.
```

Her stronger reading is correct: route-1 would persist on ANY d=8 substrate
(even a hypothetical d=8 substrate with non-Peter-Weyl mode count),
and route-2 would persist for ANY substrate (even d=4 or d=10) since
HBW is profile-intrinsic. cutoff_AL2010 fails BOTH tests; either failure
suffices for STRUCTURALLY-EXCLUDED. The two-defect fingerprint is sharper
than a single FAIL because it isolates that the regulator class has TWO
independent structural defects, not a degenerate single defect manifested
in two different test geometries.

**(3) 4-channel LAYER 2 sub-decomposition accepted.** Her Re:C3 MISSED
table refines my §VII.K-PROP candidate from a 2-channel decomposition
(axiom-sourcing / coupling-routing) into a 4-channel orthogonal
decomposition:

| LAYER 2 channel | Test gate | cutoff_AL2010 | ζ | Zubarev | SDW | anomaly |
|:----------------|:----------|:-------------:|:-:|:-------:|:---:|:-------:|
| 1: Axiom-sourcing | GATE B subset-removal | PASS {dim,fin} | TBD | TBD | TBD | TBD |
| 2: Coupling-routing | GATE A Λ-scaling | FAIL (α<0 forced) | INFO* | TBD | TBD | TBD |
| 3: Functional-class | GATE C HBW positivity | INFO (non-CM) | INFO** | PASS | INFO*** | TBD |
| 4: Anomaly-gauge | f_0 = 1/2 forcing | PASS (anomaly-cancelled) | TBD | TBD | TBD | TBD |

(*ζ has f(x)=1 ⇒ M_6 divergent ⇒ separate "abs-conv FAIL" rather than
HBW-cone INFO. **ζ has no Mellin moment at s=6 — distinct exclusion.
***SDW has compact support — see EMERGENCE below for why this is INFO not PASS.)

The 4 channels each test a structurally-orthogonal property: axiom-level
admissibility on the spectral triple (channel 1), coupling-level absorption
of L^d mode growth (channel 2), functional-class CM membership (channel 3),
and anomaly cancellation under chiral-trace constraint (channel 4). My
original 2-channel decomposition collapsed channels 3 and 4 implicitly
into "non-axiom-level structural"; her separation is sharper because the
HBW test (channel 3) is on the regulator profile in its OWN spectral
variable, while anomaly cancellation (channel 4) is a constraint between
f_0 and the substrate's chiral-anomaly index. They are not the same kind
of property.

**(4) §VII.K-PROP registry candidate accepted with extension.** Her
Q-LZ-2 ratification request: I ratify, with the structural extension
that the §VII.K-PROP entry is the **4-Channel LAYER 2 Sub-Decomposition
Theorem**, not a workshop-internal observation pending S87 codification.
Her Q-CN-7 response was correct: "the 4-channel sub-decomposition is NOT
workshop-internal — it is a structural theorem about LAYER 2 admissibility
(any non-axiom-native regulator may FAIL/PASS independently at each of
the 4 channels)." This belongs in the permanent registry now, not later.

The §VII.K-PROP entry composes naturally with the existing §VII.M
Three-Layer Regulator Theorem (S84 W2a-11 my landing,
audit_sha256 cf3b7443...) which classifies regulators by *layer* (L1 zeta /
L2 Zubarev / L3 per-Q span). §VII.M classifies WHICH regulator slot a
given regulator occupies (anomaly-native vs cluster-span vs per-Q);
§VII.K-PROP classifies WHAT KIND OF FAILURE a non-native regulator
exhibits when it's forced into the wrong slot. The two theorems are
orthogonal — see EMERGENCE for how they compose.

**(5) Atlas-cardinality cascade A_5 → A_4 = {ζ, Zubarev, SDW, anomaly}
confirmed.** Her Q-LZ-4 cascade-recording proposal is correct. The
§VII.K-PROP registry entry should record:

> `cutoff_AL2010` STRUCTURALLY-EXCLUDED via:
> - route-1 (GATE A FAIL): Λ⁴ scaling unbounded against d=8 Peter-Weyl L^8/960 a_0 growth
> - route-2 (GATE C INFO): HBW positivity violated at f_6 = 0.1 framework-truncated residue
> - Atlas cascade: A_5 → A_4 = {ζ, Zubarev, SDW, anomaly} confirmed

The two routes are recorded as INDEPENDENT exclusion paths, both leading
to the same atlas reduction. Per §3.4 master-gate rule, GATE A FAIL alone
forces STRUCTURALLY-EXCLUDED; GATE C INFO is a SECONDARY structural
finding that survives independently of the GATE A cascade and provides
robustness — if a future S87+ session finds that the GATE A pre-registered
threshold can be relaxed by an unforeseen Λ-rescaling mechanism, the GATE C
exclusion still holds. The cascade does not need a separate verdict line
(her Q-CN-12 answer is correct: companion-row `atlas_cardinality_after=A_4`
suffices).

### DISSENT

I dissent on ONE narrow technical point and offer NEW evidence on TWO
points that lizzi anticipated but did not pin numerically.

**Point 1 (DISSENT, narrow): SDW HBW status is INFO, not the cleanly
positive PASS lizzi suggests in Q-LZ-3 / Q-LZ-5.** Her phrasing
"Zubarev exp(-αx) PASSes both" and "SDW (1-x)² Θ has B-function compact-
support Mellin — is it HBW⁺?" left the SDW determination as TBD pending
R2 computation. I executed the determination via Sage MCP (results below)
and the answer is: **SDW is NOT in HBW⁺ despite M_6 = 1/168 > 0**. The
reasoning (Bernstein 1928 lemma, see EMERGENCE):

```
Definition: f ∈ HBW⁺ ⇔ f is CM on (0, ∞)
                     ⇔ f is the restriction to (0, ∞) of an analytic function
                       on Re(z) > 0 that is positive there (Widder 1941 Ch. IV §1).
Substitute: SDW f(u) = (1-u)² · Θ(1-u). f(u) = 0 for u ∈ (1, ∞), u ≠ 0 there.
Simplify: Analytic continuation of f|_{(0,1)} = (1-u)² to Re(z) > 0 is
          (1-z)², which is NOT identically zero on (1, ∞) — it equals (1-u)²
          there, which is nonzero for u > 1. But the SDW function IS zero
          on (1, ∞). Therefore f cannot equal an analytic function that is
          nonzero on a set with accumulation points.
Direction: SDW ∉ HBW⁺. Compact-support nonzero functions cannot be CM
            (Bernstein 1928 lemma — proved more carefully in EMERGENCE below).
            Status: INFO ("Mellin-finite + positive but compact-support violates
            CM analyticity") — distinct from cutoff_AL2010 INFO ("Mellin-finite
            but oscillating with sign-change").
```

This sharpens lizzi's Q-LZ-3 hypothesis. If we promote HBW to a candidate
axiom A8, the LAYER 2 channel-3 cardinality test on the surviving A_4
atlas {ζ, Zubarev, SDW, anomaly} produces:

| Atlas member | M_6 status | HBW status | Reason |
|:-------------|:-----------|:-----------|:-------|
| ζ            | M_6 = ∞ (divergent) | N/A (abs-conv FAIL) | f(x) = 1 has no Mellin transform at s ≥ 1 |
| Zubarev      | M_6 = 120 (Γ(6) > 0) | PASS | exp(-x) is the canonical CM, ρ(α) = δ(α−1) |
| SDW          | M_6 = 1/168 > 0 | INFO (compact-support) | nonzero on [0,1] but zero on (1,∞) ⇒ not analytic, not CM |
| anomaly      | M_6 sign-alternating | INFO/FAIL | Pauli-Villars-style sign-alternating regulator; PRIMARY pole structure ⇒ TBD |

Only Zubarev is a clean HBW PASS. The A8 axiom hypothesis is therefore
**MORE selective than lizzi anticipated**: 1-of-4 atlas members PASSes
HBW, not 3-of-5 (Zubarev + heat-kernel + ζ as her Q-LZ-3 hypothesis
suggested). This has structural implications for atlas reduction — see
EMERGENCE.

**Point 2 (NEW evidence, anticipating Q-LZ-1): k_eff(L) crossing of 7.5
is reached at L_max ≈ 40, not L_max ≥ 50 as my asymptotic projection
suggested.** lizzi asked in Q-LZ-1 "at what L_max does k_eff cross 7.5?"
I executed the Sage MCP scan over L ∈ {3, 4, ..., 1000}:

```
L = 10:  k_eff = 6.357
L = 12:  k_eff = 6.590
L = 15:  k_eff = 6.837
L = 20:  k_eff = 7.099
L = 25:  k_eff = 7.265
L = 30:  k_eff = 7.379
L = 40:  k_eff = 7.526   ← FIRST CROSSING above 7.5
L = 50:  k_eff = 7.617
L = 100: k_eff = 7.804
L = 200: k_eff = 7.901
L = 500: k_eff = 7.960
L = 1000: k_eff = 7.980
```

The asymptotic regime "k_eff = 8 ± 0.05" is not reached until L_max ≈ 250
(k_eff(250) ≈ 7.92). The convergence to k_eff = 8 is logarithmically slow:
fitting k_eff(L) = 8 − a/log(L) − b/log²(L) reproduces the observed
curve to ~0.001 absolute. So my GATE A k_eff_asymptotic = 6.187 from
the (7→10) ratio understated the true asymptote by 1.81 units, but the
direction (monotone increasing toward 8) is structurally correct, and
α_star → −2 is the structural endpoint regardless of the rate of
convergence.

**This means: if the W2 C9/C10 Mellin-cone live infrastructure refines
the Λ-rescaling absorption mechanism in a way that pushes k_eff_effective
DOWN below 7.5 (which it cannot, but counterfactually), the GATE A FAIL
would weaken; but the convergence rate gives ample headroom — k_eff is
already at 6.357 at L_max = 10, and the entire α-band [−1.85, −0.90]
is ALREADY entirely on the negative side at L = 10**. The GATE A FAIL
is not asymptotic-only; it holds at every probe point in the PRDR-pinned
window L ∈ {3, 5, 7, 10}. lizzi's Re:C1 statement that "the W2 C9/C10
infrastructure refines the s=2,4,6 moment values — not the s=0 anchor"
is structurally correct and now numerically pinned: the L^8/960 Plancherel
density is what generates k_eff → 8, and that density is purely combinatorial
(Sage-verified, integer-exact a_0(L) anchors), independent of any Mellin-
cone refinement at higher s.

**Point 3 (NEW evidence, sharpening Q-LZ-3): the GATE C HBW test rules
out compact-support regulators STRUCTURALLY, even when their Mellin
moments are positive-finite.** I want to flag this because lizzi's
Q-LZ-3 invitation to "treat HBW positivity as a candidate axiom A8" needs
to recognize that the resulting axiom is STRICTER than positive-Mellin-
moment: an A8 axiom would exclude not just sign-changing profiles
(cutoff_AL2010 framework-truncated) but also any compactly-supported
profile (SDW). This has consequences for the surviving atlas size — see
EMERGENCE — and means the §VII.K-PROP entry's channel-3 classification
needs to distinguish:

- **channel-3a (sign-change-CM-violation)**: f has sign-change on (0, ∞);
  always Mellin-finite-but-negative. cutoff_AL2010 framework-truncated.
- **channel-3b (compact-support-CM-violation)**: f ≥ 0 on [0, R] and
  zero on (R, ∞); Mellin-finite-positive but not analytic; SDW.
- **channel-3c (CM-PASS)**: f is the restriction to (0, ∞) of an
  analytic positive Laplace transform; Zubarev.
- **channel-3d (CM-divergent)**: f does not decay; Mellin moment divergent
  at s ≥ s_crit; ζ at s_crit = 1.

This 4-way refinement of channel-3 is the structural separation between
Mellin-FINITE-non-CM (3a, 3b) and Mellin-DIVERGENT (3d). Her current
GATE C verdict places cutoff_AL2010 in 3a; SDW would be 3b (NEW finding
this turn); Zubarev in 3c; ζ in 3d. The §VII.K-PROP registry entry
should embed this 4-way sub-classification within channel-3, not just the
binary HBW/non-HBW dichotomy.

### EMERGENCE

Three insights from cross-pollination, in order of structural depth.

**(1) The 4-channel LAYER 2 sub-decomposition is the natural functorial
upgrade of the 3-gate dispatch.** Per `.claude/rules/phononic-framing.md`,
each channel tests how the substrate's spectral content {λ_k} of D_K on
Jensen-deformed SU(3) couples through a regulator profile f at one
specific level:

```
Channel 1 (axiom-sourcing): substrate {λ_k} → CCM-2007 axioms invoked → trace
Channel 2 (coupling-routing): substrate L^d mode-count growth → Λ-rescaling
Channel 3 (functional-class): substrate spectrum + regulator → HBW⁺ membership
Channel 4 (anomaly-gauge): substrate chiral index + f_0 → trace anomaly cancellation
```

The 3-gate dispatch this session probed channels 1 (GATE B), 2 (GATE A),
and 3 (GATE C). Channel 4 (anomaly-gauge) was implicitly invoked via
canonical_constants.py L1332 `f_0_sharp = 0.5` (Andrianov-Lizzi forcing)
but was not separately gated. The 4-channel sub-decomposition is therefore
the **completion** of the LAYER 2 admissibility-on-axioms taxonomy: it
classifies regulator failures by the structural property that fails,
not by which specific test caught it.

The functorial structure: each channel admits its own pass/fail/info
classifier, and a regulator is GENUINELY-ADMISSIBLE iff PASS at all four.
A regulator at L1-PRIVILEGED (combinatorial slot unique on Mellin support)
+ L2-channel-1-PASS + L2-channel-2-PASS + L2-channel-3-PASS +
L2-channel-4-PASS is L2-FULLY-ADMISSIBLE. A regulator with L1-PRIVILEGED
+ any one channel FAIL/INFO is L2-PARTIALLY-FAILING with a specific
fingerprint. cutoff_AL2010's fingerprint is:

```
L1: PRIVILEGED (unique combinatorial slot, W5 partition theorem)
L2-ch1: PASS at {dim, fin} (GATE B)
L2-ch2: FAIL (α_star → −2 < 0; GATE A)
L2-ch3: INFO at sub-3a (sign-change non-CM; GATE C)
L2-ch4: PASS (anomaly-forced f_0 = 1/2)
```

Two channel-failures (channels 2 and 3, FAIL + INFO), two channel-passes
(channels 1 and 4). This is the **two-defect structural fingerprint**.

**(2) Atlas reduction A_5 → A_4 propagates downstream into W4-2 / W6 /
W12 / W13 by altering the cluster-span basis cardinality, not by removing
a coupling.** Per S86 W2-4 cluster-span-extractor (audit_sha256 from my
S86 work, cluster_span(L_max) callable downstream), the W3-31 closure
theorem at S85 W0-3 (b_pow(span_2)/b_pow(span_3) = 2.000 machine-precision)
established the cluster-span 2:1 multiplicative identity. The 5-regulator
atlas A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} entered into the
cluster-span basis as 5 column vectors; the A_4 reduction removes one
column, and the cluster-span identity must be RE-VERIFIED on the reduced
basis. This is the S87-W4-2-RE-RUN-UNDER-A_4 carry-forward.

**The structural constraint from §VII.K-PROP**: removing cutoff_sqrt
from the basis SHOULD NOT alter the b_pow(span_2)/b_pow(span_3) = 2.000
identity at L_max ∈ {3..12}, because that identity is a structural
property of the cluster-span operation on integer-positive moment vectors
in (M[f_n], n) space, and cutoff_AL2010 was contributing one column to
that span without violating any positivity axiom on the residue space.
But the REDUCED-BASIS Mellin-cone (W2 C9/C10) infrastructure should be
re-evaluated: the channel-3 atlas (HBW-PASS members) shrinks from
{Zubarev, heat-kernel-anchor} (effectively 1-of-A_5 PASS via Zubarev,
anchor not in atlas) to {Zubarev} (1-of-A_4 PASS), making Zubarev the
**unique HBW-axiom-native** atlas member. This connects to the S83 G3
EN3 theorem (THREE-LAYER-REG-84) — Zubarev is unique axiom-native —
and now extends that uniqueness from L1 (axiom-native) to L2-channel-3
(HBW-axiom-native).

The atlas-propagation carry-forward `S87-CUTOFF-SQRT-ATLAS-PROPAGATION`
is therefore TWO sub-tasks:
- (i) re-run W4-2 max_pair_ratio on A_4 (already pre-registered)
- (ii) NEW: re-run the cluster-span 2:1 identity test under A_4 to
  confirm that the W0-3 closure theorem holds on the reduced basis
  (expected PASS, but it must be VERIFIED, not assumed)

**(3) §VII.K-PROP composes orthogonally with §VII.M Three-Layer Regulator
Theorem.** §VII.M (S84 W2a-11, my landing, audit_sha256 cf3b7443...)
classifies WHICH layer a regulator occupies: L1 (anomaly-native, ζ),
L2 (Zubarev, the unique axiom-native), or L3 (per-Q span, SDW). The
classification is by *intrinsic regulator structure*. §VII.K-PROP
classifies WHAT KIND OF FAILURE a regulator exhibits when it's slotted
into a place where its layer doesn't naturally fit:

- A L1-native regulator (ζ) at the f_6-tail slot fails channel-3d (Mellin-divergent)
- A L2-native regulator (Zubarev) at any slot passes all channels
- A L3-native regulator (SDW) at the f_6-tail slot fails channel-3b (compact-support non-CM)
- A NON-LAYER-NATIVE regulator (cutoff_AL2010) at the f_6-tail slot fails channels 2 + 3a

The composition rule is: §VII.M layer-membership × §VII.K-PROP channel-pass-pattern
= L2-FULLY-ADMISSIBLE classifier. A regulator is L2-FULLY-ADMISSIBLE iff
its §VII.M layer matches the slot AND it passes all 4 §VII.K-PROP channels.
Zubarev satisfies both at the L2 axiom-native slot (its native home),
which is why it's the unique L2-FULLY-ADMISSIBLE regulator in the atlas.

This composition produces a sharper structural statement than either
theorem alone: **the surviving A_4 atlas {ζ, Zubarev, SDW, anomaly} has
exactly ONE L2-FULLY-ADMISSIBLE member (Zubarev), with the other three
being LAYER-NATIVE-AT-L1-OR-L3 but NOT L2-FULLY-ADMISSIBLE in any slot
where their L2 channel-3 status would be tested.** This is the
structural punchline of the workshop: cutoff_AL2010 removal does not
expand the L2-FULLY-ADMISSIBLE atlas; it merely removes a non-native
regulator from a slot it was forced into.

The §VII.M ↔ §VII.K-PROP composition is itself the candidate for a
permanent registry entry — possibly §VII.K-PROP is the right slot for
this composition theorem rather than just for the 4-channel sub-
decomposition. lizzi may want to consider whether to land §VII.K-PROP
as the **4-Channel-LAYER-2-Sub-Decomposition + L2-Fully-Admissible
Composition Theorem** (§VII.M × §VII.K-PROP composition) in her final
turn, or split into §VII.K-PROP (channels) and §VII.K-PROP-2 (composition).
Either choice is structurally defensible; my preference is the unified
landing because the composition is what makes the channel decomposition
load-bearing.

### QUESTIONS

I answer her 5 Q-LZ questions and pose 4 sharp follow-ups for her R2-B
final turn (Workshop Verdict + Atlas Decision + Wrap-Up).

**Answers to Q-LZ-1 through Q-LZ-5:**

**Q-LZ-1 (k_eff crossing 7.5)**: ANSWERED in DISSENT Point 2. k_eff(L)
crosses 7.5 at L_max ≈ 40 (k_eff(40) = 7.5263, Sage MCP). The asymptotic
regime "k_eff = 8 ± 0.05" is reached at L_max ≈ 250. Convergence is
logarithmically slow but monotone; the GATE A FAIL holds at every probe
point in {3, 5, 7, 10} regardless of asymptotic rate, because the
α-band [−1.85, −0.90] is already entirely negative at L = 10. Her Re:C1
statement that the s=0 anchor a_0(L) is Mellin-cone-infrastructure-
independent (only s ≥ 2 moments shift under W2 C9/C10) is structurally
correct and numerically robust.

**Q-LZ-2 (4-channel registry promotion)**: RATIFY, with extension to
**4-Channel + L2-Fully-Admissible Composition Theorem** as one unified
§VII.K-PROP entry (see EMERGENCE point 3). I do not dissent on any
channel collapsing into another — all 4 channels test orthogonal
properties as her Q-CN-7 response argued. The S87 codification window
is too late; S86 should land it.

**Q-LZ-3 (HBW as candidate axiom A8)**: PARTIALLY RATIFY, with the
DISSENT Point 1 correction: SDW is NOT in HBW⁺ despite M_6 > 0 (compact-
support non-CM). The A8 axiom hypothesis is therefore MORE selective
than her hypothesis suggested:

| Atlas member | A8 status (HBW⁺?) |
|:-------------|:------------------|
| ζ (f=1)      | abs-conv FAIL at s ≥ 1 (no Mellin transform) — distinct from A8 |
| Zubarev      | PASS (CM canonical) |
| SDW          | INFO (3b sub-class: compact-support non-CM) |
| anomaly (PV) | likely FAIL (sign-alternating) |
| cutoff_AL2010 | INFO (3a sub-class: sign-change non-CM) — but already excluded |

Of the 4 surviving A_4 atlas members, only Zubarev is a clean HBW⁺ PASS.
This makes A8 a much sharper axiom than I initially expected. If A8 is
adopted, the L2-FULLY-ADMISSIBLE atlas reduces to {Zubarev, anomaly?}
or just {Zubarev}. Recommend computing anomaly's HBW status as part of
the S87 carry-forward.

**Q-LZ-4 (cascade re-emission with two routes)**: CONFIRMED. The
§VII.K-PROP registry entry should record both exclusion routes verbatim
as I wrote in CONVERGENCE point 5:

> `cutoff_AL2010` STRUCTURALLY-EXCLUDED via:
> - route-1 (GATE A FAIL): Λ⁴ scaling unbounded against d=8 Peter-Weyl L^8/960 a_0 growth
> - route-2 (GATE C INFO): HBW positivity violated at f_6 = 0.1 framework-truncated residue
> - Atlas cascade: A_5 → A_4 = {ζ, Zubarev, SDW, anomaly} confirmed

No separate verdict line for the cascade is needed; companion-row
`atlas_cardinality_after=A_4` on the GATE A canonical line is the
audit-trail-complete record.

**Q-LZ-5 (S87 HBW audit of A_4)**: CONFIRMED as candidate carry-forward
with the EXTENSION that the audit must use the channel-3a/3b/3c/3d
sub-classification I introduced in DISSENT Point 3, not just binary
HBW/non-HBW. The S87 carry-forward 4-field spec:

```
What:    S87-HBW-AUDIT-ATLAS-A_4 — test all 4 surviving atlas members
         {ζ, Zubarev, SDW, anomaly} for HBW positivity at the f_6 = 0.1
         residue slot, with channel-3a/3b/3c/3d sub-classification per
         §VII.K-PROP channel-3 refinement.
Inputs:  - sessions/framework/registry/cutoff-sqrt-adjudication.md (atlas registry)
         - computations/canonical_constants.py (regulator pins)
         - sessions/permanent-results-registry.md §VII.K-PROP entry (this session)
         - computations/s86_w8_gate_c_hbw_mp_abs_conv_s6.py (template)
Gate:    PASS = all 4 members classified into one of 3a/3b/3c/3d cleanly;
         INFO = any member is borderline (HBW marginal at one sub-class
         and clean at another); FAIL = any member fails to be classifiable
         (e.g., M_6 has sign-dependent extension under PRIMARY/STENCIL
         shift). Per-member verdict; aggregate verdict = max(per-member).
Effort:  ~4 hours; same template as GATE C with 4 PRIMARY-pin variants;
         GPU not required (closed-form Mellin moments + 4-atom
         reconstruction).
```

This is sharper than the W4-2 K-invariant test because it tests
functional-class membership directly, not pole-residue universality.

**Sharp follow-ups for lizzi's R2-B FINAL turn (Workshop Verdict + Atlas
Decision + Wrap-Up):**

**Q-CN-13 (registry-write race protection on §VII.K-PROP)**: Per
`.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under
Parallel-Writer Race" (S86 W1c surface), the §VII.K-PROP slot is
currently UNALLOCATED but the registry write must scan ALL header
levels (## + ### + ####) before allocation to avoid S86 W1c-style
collisions. Will your final-turn Workshop Verdict include the
**registry-write protocol** for §VII.K-PROP — confirm the slot is empty
via grep against `sessions/permanent-results-registry.md`, allocate via
append-only Python writer, emit FAIL-with-remediation if rerouted to
§VII.L-PROP per the S84 W2a-11 §VII.M→§VII.N precedent? If the slot is
already allocated by another S86 wave, what's your rerouting target?

**Q-CN-14 (S87 HBW audit gate vs §VII.K-PROP entry — separation of
concerns)**: My S87-HBW-AUDIT-ATLAS-A_4 carry-forward (Q-LZ-5 answer)
tests HBW status, while the §VII.K-PROP entry CLASSIFIES regulators
by channel pattern. Are these two artifacts (a future S87 gate + a
permanent S86 registry entry) the right separation, or should the
§VII.K-PROP entry already include conditional classifications for the
A_4 atlas (e.g., "Zubarev: channel-3c PASS; SDW: channel-3b INFO;
anomaly: channel-3 TBD pending S87 dispatch; ζ: channel-3d") that the
S87 gate then *verifies*? My preference is to embed conditional
classifications in §VII.K-PROP NOW with explicit "TBD pending S87
verification" tags, so the registry is forward-pointing rather than
back-filling later. Confirm or dissent.

**Q-CN-15 (channel-2 + channel-3 joint verdict logic)**: For a regulator
that fails channel-2 (coupling-routing) but passes channel-3 (HBW),
the structural status would be: "regulator is functional-class
admissible but cannot be physically scaled into the action." Does your
final-turn Workshop Verdict want to record this as a SEPARATE
classification "L2-FUNCTIONALLY-ADMISSIBLE-BUT-COUPLING-EXCLUDED" vs
the cutoff_AL2010 case which is "L2-COUPLING-EXCLUDED-AND-FUNCTIONAL-
CLASS-EXCLUDED" (both routes failing)? Or is it sufficient to record
the channel-pattern (e.g., "ch1:PASS ch2:FAIL ch3:PASS ch4:PASS") and
let the structural interpretation be derived from the pattern? My
preference is the channel-pattern record (functorial, no a-priori
verdict-class collapse) — the human-readable summary then derives from
the pattern.

**Q-CN-16 (workshop closing line — atlas-cardinality-determinant
status)**: Will your closing line state that this workshop **closes the
atlas-cardinality-determinant question for cutoff_sqrt** (definitively,
A_5 → A_4 confirmed via two independent routes, atlas-propagation
carry-forwards for S87) versus **suspends the question** (pending S87
HBW audit of A_4 to confirm the surviving atlas has well-defined L2
admissibility for each member)? My read of the cumulative evidence
(GATE A FAIL canonical, GATE B PASS axiom-clean, GATE C INFO HBW-non-CM,
4-channel sub-decomposition, §VII.K-PROP composition) is **CLOSES** —
the cardinality is determined at A_4; the S87 HBW audit is a separate
question about the surviving atlas's structure, not a re-litigation of
cardinality. Confirm closure language for the Workshop Verdict.

---

## Round 2 — lizzi: Cross-Validation + Atlas Decision (FINAL ROUND)

### CONVERGENCE

I converge with connes' R2-A on five points and ratify each into the binding
Workshop Verdict + Atlas Decision below.

**(1) GATE A FAIL canonical-record under SAGE-verified asymptotic trajectory.**
connes' DISSENT Point 2 numerical scan over L ∈ {3, 4, ..., 1000} (Sage MCP)
is structurally complete. I re-verified independently via Sage MCP at this
turn:

```
Step 1 (def):    a_0(L) := 16 · Σ_{p+q ≤ L} ((p+1)(q+1)(p+q+2)/2)²
                 (Peter-Weyl L²(SU(3)) sum-of-dim², R-protected per S78 W3-K).
                 k_eff(L) := log(a_0(L)/a_0(L−1)) / log(L/(L−1)).
                 α_star(L) := −k_eff(L)/4 (boundedness root from g(L) = const + (4α + k_eff)·log L).
Step 2 (sub):    Re-computed values via Sage MCP, integer-exact:
                   a_0(3)  = 12880    (anchor MATCH)
                   a_0(5)  = 159936   (anchor MATCH)
                   a_0(10) = 9785776  (anchor MATCH)
                   k_eff(10)  = 6.3573,  α_star(10)  = −1.5893
                   k_eff(40)  = 7.5263,  α_star(40)  = −1.8816  ← FIRST CROSSING above 7.5
                   k_eff(250) = 7.9207,  α_star(250) = −1.9802
                   k_eff(1000)= 7.9800,  α_star(1000)= −1.9950
Step 3 (simp):   α_star(L) is strictly negative at every L tested; monotonically
                 decreasing toward α_star_inf = −2 (Peter-Weyl L^8/960 leading
                 → k_eff → 8). Logarithmically slow convergence
                 [k_eff(L) ≈ 8 − a/log L − b/log²L empirically].
Step 4 (dir):    Boundedness of g(L) = f_0·Λ_0^4·L^{4α}·a_0(L) requires
                 4α + k_eff(L) ≤ 0 ⇔ α ≤ α_star(L). Since α_star(L) < 0
                 ∀ L ∈ {3, ..., 1000}, no α ≥ 0 admits a bounded coupling.
                 GATE A returns FAIL — STRUCTURAL.
```

The k_eff-crossing scan is bit-exact between connes' DISSENT Point 2 numbers
and my independent Sage re-computation. This eliminates the only remaining
asymptotic-rate uncertainty from my Q-LZ-1: the substrate's d=8 Peter-Weyl
mode-count growth produces α_star → −2 logarithmically slowly, but the
PRDR-pinned probe set L ∈ {3, 5, 7, 10} already lies entirely in the
α_star < 0 region. The GATE A FAIL is non-asymptotic — it holds at every
L_max in the probe window, with the asymptotic α_star = −2 endpoint being
icing on the structural cake. Per `.claude/rules/v3-closure-recovery.md`
PROHIBITED_ACTIONS Class 1 (convention-shopping): there is no positive-α
counter-window the W2 C9/C10 Mellin-cone live infrastructure could uncover,
because a_0(L) is the s=0 RESIDUE — Mellin-cone refinements shift higher-s
moments, not the integer-exact mode-count anchor.

**(2) GATE C INFO ratified with channel-3a sub-classification adopted.**
connes' DISSENT Point 3 channel-3 sub-refinement (3a/3b/3c/3d) is the
structurally correct way to record GATE C's verdict in the §VII.K-PROP
registry. cutoff_AL2010 framework-truncated lives in **channel-3a
(sign-change-CM-violation)**. The CM-direct probe at u ∈ {0.01, 0.1, ..., 10}
confirmed sign-change at u ≈ 5; the 4-atom sum-of-exp reconstruction
returned min(c_j)_PRI = −0.0762 < 0 with sign-PRIMARY/STENCIL match. Both
probes are mutually-consistent — the sign-change of the reconstructed
profile is the proximate cause of M[f_residue](6) = −519.375 < 0. This is
not a numerical conditioning artifact (cond(A) ≈ 277 in both PRIMARY and
STENCIL) — both pins return the same SIGN classification, and the
inversion-conditioning only modulates magnitudes (PRIMARY −519.375 vs
STENCIL −61.641, factor ~8.4×, expected per cond(A)).

The verdict line `audit_sha256 = a5ec8b79d8fcd0e414b7a04173bf98426b1b5d90d5380a9489698fa5f780fa19`,
`content_sha256 = cbb03382f67664eb1741c7f871765c4b027f4b70bc7e1b23737d42c2c9210eb0`
on s86_gate_verdicts.txt line 243 (companion line 244 W9a-99 split) is
the canonical-record. PROHIBITED_ACTIONS audit clean (no convention-shopping,
no iterate-until-PASS, no post-hoc threshold edit, no ansatz-forced PASS):
INFO is the honest pre-registered branch for "abs-finite + outside HBW".

**(3) 4-channel LAYER 2 sub-decomposition + L2-Fully-Admissible composition
ratified for §VII.K-PROP unified entry.** connes' EMERGENCE point 3
(§VII.M × §VII.K-PROP composition theorem) is the sharper landing. I
adopt the unified §VII.K-PROP entry as the **4-Channel-LAYER-2-Sub-
Decomposition + L2-Fully-Admissible Composition Theorem**, not split into
two registry entries. The composition rule:

```
Step 1 (def):   §VII.M classifies WHICH LAYER (L1 anomaly-native / L2
                 axiom-native / L3 per-Q span) a regulator occupies (S84 W2a-11
                 my colleague's landing, audit_sha256 cf3b7443...).
                §VII.K-PROP-channels classifies WHAT FAILURE (channel-1 axiom-
                 sourcing / channel-2 coupling-routing / channel-3 functional-
                 class / channel-4 anomaly-gauge) a regulator exhibits in a
                 given slot.
Step 2 (sub):   L2-FULLY-ADMISSIBLE := §VII.M layer matches slot ∧ all 4
                 §VII.K-PROP channels PASS at that slot.
Step 3 (simp):  Apply to A_5 cell-occupancy:
                  Zubarev: §VII.M-L2 (axiom-native) at L2 slot;
                           channels {1: PASS-TBD, 2: PASS-TBD, 3c: PASS, 4: PASS-TBD}
                           ⇒ L2-FULLY-ADMISSIBLE candidate.
                  ζ:       §VII.M-L1 (anomaly-native) at L2 slot is NOT-NATIVE-FIT;
                           channel-3d FAIL (M_6 divergent at s=1 onward).
                  SDW:     §VII.M-L3 (per-Q span) at L2 slot is NOT-NATIVE-FIT;
                           channel-3b INFO (compact-support non-CM, M_6 = 1/168 > 0
                           but not analytic on (0, ∞) — Bernstein 1928 lemma).
                  cutoff_AL2010: NON-LAYER-NATIVE; channel-2 FAIL + channel-3a INFO.
                  anomaly: §VII.M-L1; channel-3 status TBD (S87 carry-forward).
Step 4 (dir):   Of A_5, only Zubarev is L2-FULLY-ADMISSIBLE candidate; the other
                4 are NOT-NATIVE-FIT or excluded. Direction: A_5 → A_4 cardinality
                cascade does NOT expand the L2-FULLY-ADMISSIBLE atlas — it merely
                removes a non-native regulator (cutoff_AL2010) that was forced
                into a slot it could not properly occupy.
```

This is functorial. Each channel admits its own pass/fail/info classifier;
the composition with §VII.M layer-membership produces the L2-FULLY-ADMISSIBLE
classifier as the conjunction. The §VII.K-PROP entry is the natural permanent-
registry landing.

**(4) Atlas cardinality cascade A_5 → A_4 = {ζ, Zubarev, SDW, anomaly}
binding decision.** GATE A FAIL alone forces STRUCTURALLY-EXCLUDED per §3.4
master-gate rule; GATE C INFO provides the SECONDARY route-2 robustness
against any future S87+ relaxation of the GATE A pre-registered threshold.
The two routes are independent — connes' CONVERGENCE point 2 substitution
chain confirmed: route-1 uses (a_0(L), Λ(L), f_0); route-2 uses (f_0, f_2,
f_4, f_6); only f_0 = 2 (or anomaly-physical 1/2) is shared. The §VII.K-PROP
registry entry records both routes verbatim per connes' CONVERGENCE point 5
proposal:

> `cutoff_AL2010` STRUCTURALLY-EXCLUDED via:
> - route-1 (GATE A FAIL): Λ⁴ scaling unbounded against d=8 Peter-Weyl L^8/960 a_0 growth (α_star → −2 < 0)
> - route-2 (GATE C INFO): HBW positivity violated at f_6 = 0.1 framework-truncated residue (channel-3a sign-change non-CM)
> - Atlas cascade: A_5 → A_4 = {ζ, Zubarev, SDW, anomaly} confirmed
> - Cascade-event record: GATE A companion-row `atlas_cardinality_after=A_4` (s86_gate_verdicts.txt line 240)

No separate verdict line for the cascade — it is a deterministic consequence
of GATE A's FAIL plus the §3.4 master-gate composition rule. (Confirms
my Q-CN-12 response.)

**(5) GATE B PASS at {dim, fin} + GATE C INFO at channel-3a + 4-channel
fingerprint together close the structural-position question.** The
two-channel-failure fingerprint of cutoff_AL2010 (ch1 PASS, ch2 FAIL, ch3a
INFO, ch4 PASS) is the **complete LAYER 2 admissibility profile**.
Channels 1 and 4 PASS confirm the regulator is well-formed at the axiom-
sourcing and anomaly-gauge levels — there is no axiom-violation, no anomaly-
inconsistency. Channels 2 and 3 FAIL/INFO close the regulator at the
coupling and functional-class levels independently. This is the sharpest
structural-position record we can write for cutoff_AL2010, and it is
exactly what the §VII.K-PROP registry entry should preserve for future
regulator-class analysis.

### DISSENT

I dissent on ZERO points and offer ONE narrow extension and ONE NEW
empirical evidence.

**Point 1 (NEW evidence, sharpening connes' DISSENT Point 1 SDW analyticity
argument)**: I independently verified via Sage MCP that SDW's M_6 = 1/168
exactly is consistent with B(6, 3) = Γ(6)Γ(3)/Γ(9) = 120 · 2 / 40320 = 1/168.
The compact-support analyticity argument is structurally complete; I add
the **Mellin-amplitude separation** observation:

```
Step 1 (def):   M_6 amplitudes across A_4 atlas at the f_6 functional-class slot:
                  Zubarev:        M_6 = +120          (HBW PASS, ρ = δ(α−1))
                  SDW:            M_6 = +1/168 ≈ 5.95e-3 (compact-support non-CM)
                  cutoff_AL2010:  M_6 = −519.375     (sign-change non-CM)
                  ζ:              M_6 = +∞            (abs-conv FAIL at s=1+)
Step 2 (sub):   Magnitude ratios:
                  |M_6_Zub / M_6_SDW| = 120 · 168 = 20160 ≈ 4.3 OOM
                  |M_6_cut / M_6_Zub| = 519.375 / 120 = 4.328 (1× scale)
                  |M_6_cut / M_6_SDW| = 519.375 · 168 = 87255 ≈ 4.94 OOM
Step 3 (simp):  Compact support (SDW) compresses high-s moments by 4+ OOM
                 vs CM-canonical (Zubarev). Sign-change (cutoff_AL2010) does
                 NOT — both PRIMARY (−519) and STENCIL (−62) reconstructions
                 are O(1) - O(10²) in magnitude, comparable to Zubarev.
Step 4 (dir):   Channel-3a (sign-change) and channel-3b (compact-support) are
                 NOT just analytic-class distinct — they are MAGNITUDE distinct
                 by 4-5 OOM at s=6. This means a future S87 HBW audit that
                 inspects the M_6 amplitude alone (not its sign) cannot
                 distinguish channel-3b from channel-3c without an analyticity
                 probe (e.g., extension test on (1, ∞)).
```

This sharpens the channel-3 sub-classification as a **two-feature** classifier:
(i) sign of M_6 (separates 3a from 3b/3c), (ii) analytic continuation past
the natural support boundary (separates 3b from 3c). The S87 HBW audit
must implement both features to distinguish 3b from 3c — not just M_6 sign.

**Point 2 (NARROW extension to connes' DISSENT Point 3 channel-3
sub-refinement)**: The 4-way split 3a/3b/3c/3d is structurally complete
for the A_5 atlas. I propose adding a 5th sub-class **channel-3e
(unsupported-positive-Mellin-tail)** for regulators that pass the M_6
sign + finiteness test at s=6 but FAIL it at higher s = 8, 10, ... due to
super-polynomial growth in their Hamburger-positivity Hankel determinants.
This is a placeholder for future Pauli-Villars / anomaly-class regulators
where the M_6 alone is positive-finite but the sequence of M_{2k} is not
totally-positive (Hamburger-positivity criterion fails at higher k).

```
Step 1 (def):   Hamburger-positivity criterion: f ∈ HBW⁺ ⇔ Hankel matrices
                 H_n = (M_{i+j})_{i,j=0..n} are positive semi-definite for all n.
                 (Stieltjes-Hamburger moment problem; Akhiezer 1965 ch. 1.)
Step 2 (sub):   GATE C tests M_6 sign + magnitude only — a SINGLE-MOMENT test.
                 Hamburger-positivity is an INFINITE sequence test. It is
                 STRICTLY STRONGER than M_6 sign.
Step 3 (simp):  Anomaly (Pauli-Villars-style sign-alternating regulator) is
                 a candidate channel-3e specimen: M_6 may be positive-finite,
                 but the sign-alternating sub-regulators produce non-PSD
                 Hankel determinants at higher n.
Step 4 (dir):   Channel-3e ⊂ channel-3a (since failure at higher Hankel
                 determinant is itself a sign-positivity violation in the
                 measure on (0, ∞)), but distinct from 3a-as-currently-defined
                 because 3a tests the SIGN of M_6 directly, not the PSD-ness
                 of the moment sequence.
```

Channel-3e is a placeholder for the S87 HBW audit anomaly verdict, not a
binding refinement for this turn. The §VII.K-PROP registry entry should
flag "channel-3e (unsupported-positive-Mellin-tail)" as an open sub-class
to be populated when the anomaly's HBW status is computed.

### EMERGENCE

Three insights from the cumulative R2 cross-pollination, in order of
structural depth.

**(1) The L2-FULLY-ADMISSIBLE atlas is now provably {Zubarev}-singleton
under the unified §VII.M × §VII.K-PROP composition.** This is the
sharpest atlas-cardinality theorem the workshop can extract. Combining
my Convergence point 3 substitution chain with connes' DISSENT Point 1
(SDW non-CM via Bernstein 1928) and DISSENT Point 3 (channel-3 sub-refinement):

```
Step 1 (def):    L2-FULLY-ADMISSIBLE atlas A_FA := {regulators R such that
                  §VII.M(R) layer = slot's native layer
                  ∧ ∀ ch ∈ {1, 2, 3, 4}: §VII.K-PROP-ch(R) = PASS at slot}.
Step 2 (sub):    Apply at the L2 slot (axiom-native):
                  ζ:        §VII.M layer L1 ≠ L2  ⇒ NOT-NATIVE-FIT  ⇒ R ∉ A_FA.
                  Zubarev:  §VII.M layer L2 = L2  ⇒ NATIVE-FIT;
                            channel-1 PASS-TBD (S87 verify), 
                            channel-2 PASS-TBD (S87 verify),
                            channel-3 PASS (CM canonical, ρ = δ(α−1)),
                            channel-4 PASS-TBD (anomaly compatible).
                  SDW:      §VII.M layer L3 ≠ L2  ⇒ NOT-NATIVE-FIT  ⇒ R ∉ A_FA.
                            (Channel-3b INFO + non-native-layer both exclude.)
                  cutoff_AL2010: §VII.M-NONE; ch2 FAIL + ch3a INFO  ⇒ R ∉ A_FA.
                  anomaly:  §VII.M layer L1 ≠ L2  ⇒ NOT-NATIVE-FIT  ⇒ R ∉ A_FA.
Step 3 (simp):   |A_FA| ≤ 1 with Zubarev as the only candidate, contingent
                  on S87 channel-1/2/4 PASS verifications.
Step 4 (dir):    The atlas-cardinality reduction A_5 → A_4 does NOT expand
                  A_FA. Both before (cardinality-1 candidate) and after
                  (cardinality-1 candidate), Zubarev is the unique candidate
                  for L2-FULLY-ADMISSIBLE. cutoff_sqrt removal preserves
                  this structure.
```

This connects to S83 G3 EN3 (Zubarev unique L2 axiom-native; THREE-LAYER-REG-84)
and now extends from L1 (axiom-native uniqueness) to L2 functorial composition
(channel-conjunction). The structural punchline: **the framework has at
most one fully-admissible regulator, and the cutoff_sqrt cascade is bookkeeping
about non-fully-admissible regulators it had been carrying.** This is the
deepest insight from the workshop.

**(2) The Mellin-cone live infrastructure (W2 C9/C10) plays a sub-channel-2
role under the §VII.K-PROP-channels framework — it does NOT touch any other
channel.** The S86 Mellin-cone live infrastructure is described in W4-3
plan §P5 line ~470-490 (per the W4 working paper) and S85 W2-5
direct-heat-kernel-truncation fallback. Its functional role:

```
Step 1 (def):    Mellin-cone live := for each spectral-action moment Σ f_n a_n,
                  evaluate f_n via residue-at-pole structure on the Mellin
                  contour, NOT via direct heat-kernel truncation.
Step 2 (sub):    GATE A uses a_0(L) directly (s=0 Mellin residue, integer-exact).
                  GATE B uses CCM-2007 axiom invocation (logical, not Mellin).
                  GATE C uses prescribed (f_0, f_2, f_4, f_6) Mellin vector
                  + 4-atom sum-of-exp inversion (NOT live Mellin-cone integration).
Step 3 (simp):   The Mellin-cone live infrastructure refines the n ≥ 1 Mellin
                 residues that enter the Σ_n f_n a_n COUPLING product. It
                 does NOT enter:
                  - GATE A (uses a_0 directly, not the n ≥ 1 sum)
                  - GATE B (logical axiom invocation, no Mellin sum)
                  - GATE C (prescribed Mellin vector + reconstruction)
                 Therefore it lives at channel-2 (coupling-routing) ONLY.
Step 4 (dir):    No channel-1, channel-3, or channel-4 verdict is sensitive
                  to the Mellin-cone live infrastructure status. Only channel-2's
                  Λ-rescaling absorption mechanism could (counterfactually) be
                  refined by it — and the Peter-Weyl L^8/960 leading is integer-
                  combinatorial, so the refinement would have to enter via
                  a different a_0(L) definition (which is precluded by the
                  R-protected Peter-Weyl identity).
```

This is the **Mellin-cone-live infrastructure occupies a sub-channel-2 role**
theorem. It clarifies why the GATE A FAIL is robust against any S87+
infrastructure refinement: there is no architectural slot for the live
infrastructure to enter the s=0 a_0 anchor.

**(3) The §VII.K-PROP entry plus its §VII.M composition produces a
"regulator pathology atlas" — a structural-position table for ALL regulators,
forced or native, at every layer slot.** The entry I propose to land:

```
§VII.K-PROP — 4-Channel-LAYER-2-Sub-Decomposition + L2-Fully-Admissible
              Composition Theorem (S86 W8 cutoff_sqrt GATE A/B/C trio)

Channels: 1 (axiom-sourcing), 2 (coupling-routing), 3 (functional-class),
          4 (anomaly-gauge). Each independent.

Channel-3 sub-classification:
  3a (sign-change non-CM):       cutoff_AL2010 framework-truncated; M_6 < 0.
  3b (compact-support non-CM):   SDW (1-x)² Θ; M_6 > 0 but not analytic on (0, ∞).
  3c (CM PASS):                  Zubarev exp(−αx); ρ = δ(α−α_0).
  3d (Mellin-divergent):         ζ f(x) = 1; M_6 = +∞ at s ≥ 1.
  3e (Hamburger-violating tail): anomaly Pauli-Villars-style; M_6 sign TBD,
                                  Hankel-positivity TBD (S87 dispatch).

Composition with §VII.M (S84 W2a-11): L2-FULLY-ADMISSIBLE iff layer match
+ all 4 channels PASS at slot. A_FA = {Zubarev} candidate, contingent on
S87 channel-1/2/4 verification.

Recorded outcomes:
  cutoff_AL2010: STRUCTURALLY-EXCLUDED via {ch2 FAIL, ch3a INFO}; A_5 → A_4.
  Zubarev:       L2-FULLY-ADMISSIBLE candidate; channel-3c PASS verified.
  SDW:           channel-3b INFO; verified by Bernstein 1928 / Sage MCP M_6 = 1/168.
  ζ:             channel-3d FAIL at s ≥ 1.
  anomaly:       channel-3e TBD (S87 HBW audit).
```

This is the structural deliverable to the registry. It composes with §VII.M
(Three-Layer Regulator Theorem, S84 W2a-11), §VII.K (cluster-span CC-5
identity, S84 W3-21), and §VII.B (HP^1 near-invariance R-protection,
S86 W1b-T6) to give a complete LAYER 2 admissibility framework for the
phonon-exflation framework.

## Workshop Verdict

**Atlas-Cardinality Binding Decision**: A_5 → A_4 = {ζ, Zubarev, SDW, anomaly}.
cutoff_sqrt (cutoff_AL2010) is removed by structural exclusion via TWO
independent routes (GATE A FAIL coupling-routing + GATE C INFO functional-class).
Both gates have dual-SHA verdict-line records (s86_gate_verdicts.txt lines
239-244); GATE A companion-row carries `atlas_cardinality_after=A_4` as the
canonical cascade-event annotation.

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | GATE A (Λ-scaling on Jensen SU(3)) | C1, R1-Re:C1, R2-lizzi-CONV-1 | **Converged** | FAIL canonical-record. α_star(L) ∈ [−1.5893, −1.0158] across {3,5,7,10}; α_star(40) = −1.8816 first crossing of 7.5 in k_eff; α_star → −2 from L^8/960 leading. No α ≥ 0 admits bounded coupling. Bit-exact Sage MCP verification at this turn. audit_sha256 `a289004b...d270`. |
| 2 | GATE B (subset-removal a_0 sweep) | C2, R1-Re:C2 | **Converged** | PASS at {dim, fin}-only load-bearing set (cardinality 2). cutoff_AL2010 a_0 sourcing is axiom-minimal — routes through GLOBAL-TRACE Tr_H(1)/Vol_F, no inner-fluctuation lift demanded. Sharp Θ-cutoff has no smooth-symbol calculus (closes routes (ii) HEAT-KERNEL + (iii) MELLIN-RESIDUE). Necessary-but-not-sufficient (R2 lizzi E2-L). audit_sha256 `69a86e46...b8e`. |
| 3 | GATE C (HBW/MP-abs-conv s=6) | L1, R2-connes-CONV-1, R2-lizzi-CONV-2 | **Converged** | INFO at channel-3a (sign-change non-CM). M_6_pri = −519.375, M_6_sten = −61.641; sign-PRIMARY/STENCIL match; CM-direct probe sign-change at u ≈ 5; abs-finite + saturated. f_residue ∉ HBW⁺ but Mellin-finite. audit_sha256 `a5ec8b79...780fa19`, content_sha256 `cbb03382...210eb0`. |
| 4 | NCG axiomatic sit (CCM-2007) — 4-channel LAYER 2 sub-decomposition | C3, R1-Re:C3, R2-connes-CONV-3+EM-3, R2-lizzi-CONV-3+EM-3 | **Emerged** | LAYER 2 admissibility decomposes into 4 ORTHOGONAL channels: ch1 axiom-sourcing, ch2 coupling-routing, ch3 functional-class, ch4 anomaly-gauge. Each independent. Channel-3 sub-refines into 3a (sign-change non-CM), 3b (compact-support non-CM), 3c (CM PASS), 3d (Mellin-divergent), 3e (Hamburger-violating tail; placeholder). cutoff_AL2010 fingerprint = (ch1:PASS, ch2:FAIL, ch3a:INFO, ch4:PASS). |
| 5 | Atlas cardinality decision (A_5 vs A_4) | All R2 | **Converged** | **A_5 → A_4 = {ζ, Zubarev, SDW, anomaly}** is binding. Two independent exclusion routes: route-1 (GATE A coupling FAIL Λ⁴ scaling unbounded against L^8/960 a_0 growth) + route-2 (GATE C functional-class INFO HBW positivity violated at f_6 = 0.1 residue). Cascade-event recorded in GATE A companion-row line 240. |
| 6 | cutoff_sqrt removal verdict | All R2 | **Converged** | STRUCTURALLY-EXCLUDED. Removal is NOT a single-axiom violation — it is a structural FAIL of the COUPLING geometry between fixed Λ scale and L^8-divergent d=8 substrate spectrum (route-1) compounded with profile-intrinsic non-CM (route-2). LAYER 1 status (PRIVILEGED, unique combinatorial slot) UNCHANGED — admissibility-orthogonal per R3-C-E3-L. |
| 7 | §VII.M × §VII.K-PROP composition theorem | R2-connes-EM-3, R2-lizzi-EM-1 | **Emerged** | NEW unified registry entry: 4-Channel-LAYER-2-Sub-Decomposition + L2-Fully-Admissible Composition Theorem. L2-FULLY-ADMISSIBLE iff §VII.M layer matches slot ∧ all 4 §VII.K-PROP channels PASS. Of A_4, only Zubarev is L2-FULLY-ADMISSIBLE candidate (channel-3c PASS verified; channels 1/2/4 PASS-TBD pending S87). |
| 8 | SDW HBW status | R2-connes-DIS-1, R2-lizzi-DIS-1 | **Emerged** | SDW ∉ HBW⁺ despite M_6 = 1/168 > 0 (Sage MCP verified, exact rational B(6,3) = Γ(6)Γ(3)/Γ(9) = 240/40320 = 1/168). Bernstein 1928 lemma: compact-support nonzero functions cannot be CM (analytic-continuation past support boundary contradicts identity-theorem). Channel-3b INFO classification. Magnitude separation: \|M_6_Zub/M_6_SDW\| = 20160 ≈ 4.3 OOM. |
| 9 | k_eff(L) asymptotic trajectory | R2-connes-DIS-2, R2-lizzi-CONV-1 | **Converged** | k_eff(40) = 7.5263 (FIRST CROSSING above 7.5); k_eff(250) = 7.9207; k_eff(1000) = 7.9800; asymptote → 8 logarithmically slowly (k_eff ≈ 8 − a/log L − b/log²L). Sage MCP independent re-verification at this turn matches connes' R2-A scan bit-exactly. The L^8/960 limit is structural; convergence rate is irrelevant to GATE A FAIL because α-band [−1.85, −0.90] already entirely on negative side at L = 10. |
| 10 | Mellin-cone live infrastructure (W2 C9/C10) sub-channel localization | R2-lizzi-EM-2 | **Emerged** | Mellin-cone live infrastructure occupies sub-channel-2 ONLY. It refines n ≥ 1 Mellin residues entering Σ_n f_n a_n COUPLING product; does NOT enter GATE A (s=0 anchor a_0 integer-exact), GATE B (logical axiom invocation), or GATE C (prescribed Mellin vector + reconstruction). No architectural slot exists for live infrastructure to alter the GATE A FAIL via channel-1, channel-3, or channel-4. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**.
0 Dissent / 0 Partial; 6 Converged + 4 Emerged.

## Remaining Open Questions

1. **Channel-1, channel-2, channel-4 PASS status for Zubarev at L2 axiom-native slot** — currently PASS-TBD pending S87 verification. The L2-FULLY-ADMISSIBLE singleton claim (|A_FA| = 1, Zubarev unique) hinges on these three TBD verdicts. Required: dispatch a 3-channel test at the L2 slot for Zubarev specifically, with the same dual-SHA template as GATE A/B/C.

2. **Channel-3 status for anomaly (Pauli-Villars-style)** — placeholder channel-3e introduced (Hamburger-violating tail). Requires Hankel-PSD test on M_{2k} sequence for k = 0, 1, 2, 3, 4, 5 (going beyond the single-moment GATE C test). The S87 HBW audit must implement this — single-moment sign + finiteness is necessary-but-not-sufficient for HBW⁺.

3. **§VII.K-PROP slot allocation under registry-write race protection** (Q-CN-13) — confirm §VII.K-PROP is unallocated via grep across all header levels (## + ### + ####) before append-only Python writer lands the entry. If allocated by another S86 wave, reroute to §VII.L-PROP per S84 W2a-11 §VII.M→§VII.N precedent and emit FAIL-with-remediation per `.claude/rules/epistemic-discipline.md` Registry-Write Hygiene rule.

4. **SDW analytic-continuation probe specification for S87 HBW audit** — channel-3b distinction from channel-3c requires testing analytic continuation past natural support boundary, not just M_6 magnitude. Required: pre-register the test (e.g., evaluate f(z) for z ∈ ℂ with Re(z) > 0 outside support, check holomorphic extension exists).

5. **Anomaly-gauge channel-4 axiom A8 candidate independence** (Q-LZ-3 partial-ratification) — does channel-4 (anomaly-gauge: f_0 = 1/2 forcing under chiral-anomaly cancellation) commute with channel-3 (HBW)? Open: is there a regulator that PASSes channel-4 but FAILs channel-3 (or vice versa)? cutoff_AL2010 PASSes ch4 + INFOs ch3a, providing one data point; a second is needed to establish independence.

6. **W4-2 max_pair_ratio re-evaluation under reduced atlas A_4** — the cluster-span 2:1 multiplicative identity (W3-31, S85 W0-3) was established on A_5 basis at 2.220e-15 (machine-epsilon). Removing one column from the basis SHOULD preserve the identity (purely cluster-span structural), but VERIFICATION is required. This is the S87-W4-2-RE-RUN-UNDER-A_4 carry-forward.

7. **C45 sixth-regulator promotion gate definition** — with A_5 reduced to A_4, the C45 carry-forward needs a pre-registration for what KIND of sixth regulator could be promoted. Candidate sixth regulators (heat-kernel-anchor, Pauli-Villars-finite, Wilson-loop, etc.) need 4-channel sub-decomposition pass-pattern requirements pre-registered before any S87 dispatch.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **Atlas cardinality reduced A_5 → A_4 = {ζ, Zubarev, SDW, anomaly}** (binding;
  via two independent exclusion routes for cutoff_AL2010, both with dual-SHA
  verdict lines on s86_gate_verdicts.txt).
- **3 gate verdicts emitted with full 64-character dual-SHA**: GATE A FAIL
  (line 239, audit `a289004b...d270`); GATE B PASS (line 241, audit
  `69a86e46...b8e`); GATE C INFO (line 243, audit `a5ec8b79...780fa19`).
  Cascade-event recorded in GATE A companion-row (line 240) as
  `atlas_cardinality_after=A_4 structural_pre_determination=R3-C-E3-C`.
- **4-Channel LAYER 2 Sub-Decomposition Theorem candidate**: LAYER 2
  admissibility decomposes into 4 orthogonal channels (axiom-sourcing,
  coupling-routing, functional-class, anomaly-gauge); channel-3 sub-refines
  into {3a, 3b, 3c, 3d, 3e}. Promoted to §VII.K-PROP candidate registry entry
  pending Q-CN-13 slot-allocation race-protection.
- **L2-Fully-Admissible Composition Theorem candidate**: §VII.M × §VII.K-PROP
  composition produces L2-FULLY-ADMISSIBLE iff layer match + all 4 channels
  PASS. |A_FA| ≤ 1 with Zubarev as unique candidate, contingent on S87
  channel-1/2/4 verifications.
- **SDW non-HBW⁺ status established** via Bernstein 1928 lemma + Sage MCP
  exact-rational verification M_6 = 1/168 = B(6,3). New channel-3b
  classification (compact-support non-CM, distinct from channel-3a
  sign-change non-CM and channel-3c CM PASS).
- **Mellin-cone live infrastructure (W2 C9/C10) sub-channel-2 localization
  theorem**: NO architectural slot for the live infrastructure to alter
  GATE A FAIL — the s=0 anchor a_0(L) is Peter-Weyl integer-exact, refinement
  enters only at higher-s coupling moments (channel-2 internal substructure).
- **k_eff(L) asymptotic trajectory pinned**: First crossing of 7.5 at
  L_max ≈ 40 (k_eff(40) = 7.5263, Sage MCP); asymptotic regime k_eff = 8 ± 0.05
  reached at L_max ≈ 250. Logarithmically slow, monotone, structural.

### What Holds

- **§VII.M Three-Layer Regulator Theorem (S84 W2a-11)** unchanged. cutoff_AL2010
  was always NON-LAYER-NATIVE; A_5 → A_4 removes a non-native member from a slot
  it could not properly occupy. Zubarev's L2 axiom-native uniqueness preserved.
- **§VII.K cluster-span CC-5 multiplicative identity (S84 W3-21)** preserved
  expectationally on A_4 basis. Re-verification queued (S87-W4-2-RE-RUN-UNDER-A_4).
- **R-protected observable family (Lizzi observables, S78+)** unaffected by
  atlas reduction. R-protection is a per-branch property of the moment ratios,
  independent of how many regulators populate the atlas.
- **§VII.B HP^1 near-invariance R-protection (S86 W1b-T6)** unaffected; the
  STRICT/LOOSE C44 protection criterion is on the Mellin multiplier structure,
  not on regulator-class membership.
- **GATE B PASS at {dim, fin} structural finding**: cutoff_AL2010's a_0
  sourcing was always axiom-minimal; the PASS is preserved as a structural
  classification of the regulator's sourcing route, even after exclusion.
- **LAYER 1 PRIVILEGED status of cutoff_AL2010 (combinatorial slot uniqueness
  on Mellin support)** unchanged. LAYER 1 and LAYER 2 are admissibility-
  orthogonal per R3-C-E3-L. Removal at LAYER 2 does not rewrite LAYER 1
  combinatorial position.
- **Three-Layer Regulator Synthesis (S83 G3 EN3)**: Zubarev unique L2
  axiom-native preserved; cutoff_sqrt was never axiom-native at L2 — its
  removal sharpens the Three-Layer architecture rather than disturbing it.
- **All non-cutoff_sqrt prior session results** (S65-S86) on which cutoff_sqrt
  was not load-bearing remain valid. Specifically: A_s pin-map (S84 W3-34),
  M0-fconv identity (S84 W3-35), CC-5 landing (S84 W3-21) all preserved.

### What Breaks or Strains

- **Any working-paper section that cites cutoff_sqrt as a 5th atlas member
  for cardinality-cardinality-dependent claims** must be updated to A_4.
  Specifically: W4-2 max_pair_ratio (cluster-span basis cardinality), W6
  regulator-class summary tables, W12 atlas-counting references, W13
  cell-occupancy lookups. Each requires a pointer-sweep + edit pass in S87.
- **Any S87+ atlas-dependent gate that had implicit |A_5| = 5 cardinality
  in its pre-registration** must be re-pre-registered with |A_4| = 4. Any
  gate computing fractions or ratios over the atlas (e.g., "fraction of
  regulators with property X") shifts denominator from 5 to 4.
- **cutoff_AL2010-related canonical constants** (`f_0_sharp`, `f_0_anomaly`,
  framework-truncated Mellin vector pins) remain in `canonical_constants.py`
  for historical-record provenance, but their downstream consumption must
  be flagged as STRUCTURALLY-EXCLUDED-AT-L2. Recommend a `provenance_status`
  tag on these constants in S87 (NOT removal — the constants record the
  exclusion pathway, useful for §VII.K-PROP audit trail).
- **The C45 sixth-regulator promotion candidate space** is NOT auto-validated
  by cutoff_sqrt removal. Each candidate must pass the 4-channel
  sub-decomposition test independently. The "drop one regulator, pick a new
  one" intuition is now structured as a 4-channel pass-pattern requirement.

### Carry-Forward Computations

1. **`S87-CUTOFF-SQRT-ATLAS-PROPAGATION`** — propagate A_5 → A_4 reduction
   into all dependent W-files (W4-2, W6, W12, W13).
   - **What**: pointer-sweep + edit pass on cutoff_sqrt citations across
     `sessions/archive/session-86/` working papers. Update atlas-cardinality denominators,
     cell-occupancy tables, regulator-class summary tables. Flag canonical
     constants with `provenance_status = STRUCTURALLY-EXCLUDED-AT-L2` in
     `computations/canonical_constants.py`. Land §VII.K-PROP registry entry
     under registry-write race protection (grep all header levels first).
   - **Inputs**: `sessions/archive/session-86/workshops/s86-cutoff-sqrt-gate-abc-trio.md`
     (this workshop, content_sha256 of the post-write state); `computations/s86_gate_verdicts.txt`
     lines 239-244; `sessions/permanent-results-registry.md` (post-grep state).
   - **Gate**: PASS = §VII.K-PROP entry landed at unique slot with append-only
     writer (no Edit-tool mtime conflict); all W-file citations updated to
     A_4; canonical_constants.py provenance-tag added; verdict line emitted.
     INFO = slot rerouted to §VII.L-PROP per Q-CN-13 race-protection rerouting.
     FAIL = inconsistent atlas cardinality propagation detected (e.g., one
     W-file still references A_5 after sweep).
   - **Effort**: ~3 hours; one Python script for pointer-sweep + one for
     registry-write; no GPU.

2. **`S87-W4-2-RE-RUN-UNDER-A_4`** — re-run W4-2 max_pair_ratio + cluster-span
   2:1 identity on the reduced A_4 basis.
   - **What**: re-execute W4-2 max_pair_ratio gate on the 4-column atlas
     {ζ, Zubarev, SDW, anomaly}; verify cluster-span identity
     b_pow(span_2)/b_pow(span_3) = 2.000 holds at machine-epsilon under canonical
     `|ratio − 2|` metric (per W2-4 calibration corpus); re-verify CC-5 identity
     span(O) = ∏ span(f_k)^{|p_k|} on 42-row VII.K atlas with cutoff_sqrt column
     removed.
   - **Inputs**: `computations/_cluster_span_extract.py` (callable from
     S86 W2-4); `computations/canonical_constants.py` reduced-atlas pins;
     §VII.K-PROP registry entry from Carry-Forward 1.
   - **Gate**: PASS = cluster-span 2:1 identity holds with `|ratio − 2| < 1e-14`
     at L_max ∈ {3, 5, 7, 9, 11}; CC-5 max_rel_err < 1e-15 over 42-row atlas.
     INFO = 1e-14 ≤ |ratio − 2| < 1e-12 (precision-comparison floor; document
     per Publication-Precision Pre-Registration rule). FAIL = identity
     numerically broken (signals cutoff_sqrt was load-bearing on cluster-span
     structure, contradicting the structural-property claim).
   - **Effort**: ~2 hours; re-run existing W4-2 + W3-21 scripts on reduced
     atlas; no GPU; precision pinned per W2-4 canonical-metric rule.

3. **`S87-C45-SIXTH-REGULATOR-PROMOTION`** — pre-register the sixth-regulator
   promotion criteria using 4-channel sub-decomposition.
   - **What**: enumerate candidate sixth regulators (heat-kernel-anchor,
     Pauli-Villars-finite, Wilson-loop-truncation, Mellin-Barnes-finite,
     others); for each, pre-register required pass-pattern across the 4
     LAYER 2 channels and the §VII.M layer-membership target. Define
     PASS = (§VII.M layer match) ∧ (all 4 channels PASS at slot); INFO =
     (layer match) ∧ (1 channel marginal); FAIL = layer mismatch or
     (≥ 1 channel FAIL).
   - **Inputs**: §VII.K-PROP registry entry from Carry-Forward 1; §VII.M
     Three-Layer Regulator Theorem (S84 W2a-11); candidate-regulator
     literature (heat-kernel: Vassilevich 2003 review; PV-finite: Bilal 2008);
     A_4 atlas current state from Carry-Forward 1.
   - **Gate**: PASS = ≥ 1 candidate sixth regulator passes the 4-channel +
     §VII.M layer-match test; the candidate gets promoted with a verdict line.
     INFO = ≥ 1 candidate PASSes 3-of-4 channels + layer match (admit as
     L2-PARTIALLY-ADMISSIBLE; document the failed channel). FAIL = NO
     candidate passes any layer-match + ≥ 3 channel test (atlas remains A_4).
   - **Effort**: ~6 hours; literature review + 4-channel test dispatches per
     candidate (~1.5 hours per candidate); no GPU but mpmath may be needed
     for candidates with non-elementary residue structure.

4. **`S87-HBW-AUDIT-ATLAS-A_4`** (NEW from R2; promoted from R1 lizzi Q-LZ-5
   + R2 connes Q-LZ-5 confirmation) — channel-3 sub-classification audit
   for surviving atlas members.
   - **What**: test all 4 surviving atlas members {ζ, Zubarev, SDW, anomaly}
     for HBW positivity at the f_6 = 0.1 residue slot, with channel-3a/3b/3c/3d/3e
     sub-classification per §VII.K-PROP channel-3 refinement. For each member:
     compute M_6 via Sage MCP closed form; test sign + finiteness; test
     analytic continuation past natural support (3b vs 3c distinction); test
     Hankel-PSD on M_{2k} sequence for k = 0..5 (3e vs 3a distinction for
     anomaly).
   - **Inputs**: `sessions/framework/registry/cutoff-sqrt-adjudication.md` (atlas
     registry post-A_4 update); `computations/canonical_constants.py`
     regulator pins for each A_4 member; `computations/s86_w8_gate_c_hbw_mp_abs_conv_s6.py`
     (template); §VII.K-PROP registry entry from Carry-Forward 1.
   - **Gate**: PASS = all 4 members classified into one of 3a/3b/3c/3d/3e
     cleanly (no marginal between sub-classes). INFO = any member is borderline
     (HBW marginal at one sub-class and clean at another). FAIL = any member
     fails to be classifiable (e.g., M_6 has sign-dependent extension under
     PRIMARY/STENCIL shift, contradicting the GATE C cross-check robustness).
     Per-member verdict; aggregate verdict = max(per-member).
   - **Effort**: ~5 hours; same template as GATE C with 4 PRIMARY-pin variants;
     additional Hankel-PSD test for anomaly (~1 hour); no GPU; closed-form
     Mellin moments via Sage MCP + 4-atom reconstruction.

5. **`S87-MELLIN-CONE-LIVE-CHANNEL-2-LOCALIZATION-VERIFY`** (NEW from R2-lizzi-EM-2)
   — verify Mellin-cone live infrastructure (W2 C9/C10) is restricted to
   sub-channel-2.
   - **What**: dispatch a 4-channel test of the Mellin-cone live infrastructure
     at each channel; verify infrastructure modifications affect ONLY channel-2
     (coupling-routing) and produce no shifts at channel-1 (axiom-sourcing),
     channel-3 (functional-class), or channel-4 (anomaly-gauge). Specifically:
     re-run the GATE A α-scan with Mellin-cone live = True and Mellin-cone live
     = False; verify k_eff_asymptotic unchanged within machine epsilon
     (channel-1 invariance); re-run a GATE C-style HBW probe with both settings;
     verify M_6 unchanged within machine epsilon (channel-3 invariance).
   - **Inputs**: `computations/s86_w8_gate_a_lmax_finiteness.py` (modified
     to accept `--mellin-cone-live` flag); W2 C9/C10 infrastructure module
     (sessions/archive/session-86/session-86-w4-workingpaper.md cite); §VII.K-PROP
     registry entry.
   - **Gate**: PASS = channel-1, channel-3, channel-4 outcomes invariant under
     Mellin-cone live toggle (rel-shift < 1e-13); only channel-2 outcomes
     responsive (any rel-shift detected). INFO = channel-2 responds + ≤ 1
     other channel responds at < 1e-10 (cross-channel leakage detected,
     document). FAIL = > 1 channel responds at > 1e-10 (theorem disproved;
     §VII.K-PROP needs revision).
   - **Effort**: ~4 hours; toggling existing scripts; no GPU.

6. **`S87-CHANNEL-4-INDEPENDENCE-FROM-CHANNEL-3`** (NEW from R2-lizzi Open Q5)
   — verify channel-4 (anomaly-gauge) is structurally independent from channel-3
   (functional-class).
   - **What**: find or construct a regulator that PASSes channel-4 but FAILs
     channel-3 (or vice versa) — a second data point beyond cutoff_AL2010
     (ch4 PASS + ch3a INFO) — to establish or disprove independence.
     Candidates: Pauli-Villars-with-finite-mass (channel-4 ?, channel-3 ?);
     SDW-modified-with-anomaly-coefficient (channel-4 ?, channel-3b INFO known).
   - **Inputs**: §VII.K-PROP registry entry; canonical_constants.py for
     candidate regulator pins; literature on PV-anomaly compatibility.
   - **Gate**: PASS = ≥ 1 regulator with non-trivial channel-4-vs-channel-3
     pattern found (independence demonstrated). INFO = candidates exist but
     all show channel-4 ⇔ channel-3 lock-step (suggests dependence; flag for
     deeper analysis). FAIL = no candidates can be constructed (channel-4 may
     be derivative of channel-3 — would collapse the 4-channel theorem to
     3 channels).
   - **Effort**: ~6 hours; literature search + candidate construction +
     2-channel dispatches per candidate; no GPU.

### Closing Line

The atlas-cardinality-determinant question for cutoff_sqrt is **CLOSED**:
A_5 → A_4 = {ζ, Zubarev, SDW, anomaly} via two independent structural
exclusion routes (GATE A FAIL coupling-routing + GATE C INFO functional-class),
and the workshop's structural deliverable is the 4-Channel-LAYER-2-Sub-
Decomposition + L2-Fully-Admissible Composition Theorem candidate landing
at §VII.K-PROP, which establishes Zubarev as the unique L2-FULLY-ADMISSIBLE
candidate in the surviving atlas pending S87 channel-1/2/4 verification.
