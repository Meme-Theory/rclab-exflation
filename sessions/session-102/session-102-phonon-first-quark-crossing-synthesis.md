# Session 102 Synthesis: The Quark Gen-1↔Gen-3 Crossing FAIL — a No-Sign-Changing-Slope-Handle WALL, the Third Fermion-Sector "One Handle Held" Instance

**Date**: 2026-06-10
**Agent**: phonon-first-cosmologist (Phonon-First Cosmologist)
**Source Documents**:
- `sessions/session-102/session-102-w4-workingpaper.md` (read in full)
- `sessions/permanent-results-registry.md` §VII.BL (Generation-Blindness Obstruction, STAGE-3-PERMANENT), §VII.BS (Normalization Non-Universality, rank-1, STAGE-3-PERMANENT), §VII.BM/BN/BO.STATE-PROJ (generation-blindness lineage)
- Knowledge MCP: `search_knowledge`/`trace_entity` (W2-11 triality-preservation, S101-W3-QUARK-COMPONENT-ORIENTATION, no prior no-sign-handle theorem)

---

## I. Session Outcome

The W4-15 gate (`CF-S102-QUARK-PERGEN-KERNEL`, FAIL/FAIL/VALID, audit `77659eb6…cc32c49`) PROVED that the substrate-DERIVED per-generation dressed-block greybody kernel cannot force the joint quark crossing (gen-1 inversion m_u/m_d<1 AND gen-3 upright m_t/m_b>1). I classify the corridor as a **WALL**: a permanent structural wall, not an enumerated gap. The substrate provides NO sign-changing per-generation slope handle, because **every G-invariant scalar available on the single-τ-slice Peter-Weyl spectral triple is a function of the quadratic Casimir C₂ (with triality a Jensen-invariant binary step), hence monotone or binary-step across generations — never the strict gen-2 dip/peak a sign flip requires.** This is the THIRD fermion-sector instance of the same structural genus — "C₂-monotone substrate forces same-signed shapes / one handle held" — after §VII.BL Generation-Blindness Obstruction and §VII.BS rank-1 Normalization-Non-Universality. The W4-15 κ_g-derivation routing therefore does NOT fold into a GAP gate (`CF-S103-QUARK-KAPPA-G-<handle>` does NOT instantiate); it routes to a §VII registry-candidate WALL theorem (recommendation below; the landing is the registry sole-writer's, not mine).

---

## II. Key Results

### II.1 — The crossing requires a sign-changing slope handle the substrate cannot supply

**Result**: κ_g = |w_g|/d_g = +0.07295 / +0.04078 / +0.00384 (gen1/gen2/gen3); slope asymmetry (κ_g^up − κ_g^down) = +0.07295 / +0.04078 / +0.00384, strictly POSITIVE and strictly monotone, `signflip = False`. Classification: **PARTICLE** (per-generation dressed-block kernel) / structurally **GEOMETRIC** (the obstruction lives in the Peter-Weyl invariant content of D_K).

The dressed-block construction is the only substrate-natural per-generation slope structure that S101 W3 produced: physical mass = heavier eigenvalue of `B_g^S = [[d_g^S, w_g^S],[w_g^S*, d_g^S]]`, with `m_g^S = d_g^S + |w_g^S|`, diagonal `d_g^S = √⟨λ²⟩_g^{(comp)}` (bare-ladder RMS), off-diagonal `w_g^S = √Ω^S · exp(−2πC₂(g)τ_fold/κ^S)` (the S101-W3 greybody envelope). Both substrate-derived; no PDG in the kernel. The up/down ratio is `r_g = (d+|w|)_up / (d+|w|)_dn`. The **diagonal floor** is `r_g(|w|=0) = √(Ω^c/Ω^D) = √(1/2) = 0.70711 at EVERY generation` (the bare ⟨λ²⟩ cancels in the ratio; only the Ω-scalar survives, `Ω^D/Ω^c = 2` Sage-exact). Up is intrinsically lighter on the diagonal; the dressing must overpower the floor to flip gen-3.

The substitution chain (W4-15 Step 4–5, authoritative — not re-adjudicated) shows the kernel fails on BOTH binding constraints. Gen-3 upright needs `(w_up,3 − w_dn,3) > (d_dn,3 − d_up,3) = +0.53699`; the substrate supplies `+0.00490` — short by **2 OOM**, because the greybody transmission `exp(−2πC₂τ/κ)` is exponentially smallest exactly at gen-3's LOW C₂ = 1.333. Gen-1 sits at the HIGHEST C₂ = 6.0, where any C₂-monotone up-dressing makes gen-1 the MOST up-heavy — the opposite of inversion. The slope asymmetry is therefore structurally same-signed across all three generations: the greybody is monotone in C₂, so it cannot reverse sign over a monotone C₂ ladder.

### II.2 — Enumerated proof that NO substrate quantity is non-monotone across generations (route-(b) exhaustion is structural, not incidental)

**Result**: Every G-invariant scalar on the single-τ-slice (A_K, H_K, D_K(τ_fold)) Peter-Weyl spectral triple is a function of C₂ or a Jensen-invariant discrete triality step; none is a strict gen-2 dip/peak. Classification: **GEOMETRIC**.

A sign flip in κ_g between g=1 and g=3 requires a non-monotone ω_g(C₂) — a strict dip or peak in the MIDDLE (gen-2) generation. I enumerate every substrate quantity that can enter the per-generation kernel and test each against C₂-monotonicity across {gen3, gen2, gen1} = C₂{1.333, 3.0, 6.0}:

| Candidate substrate ingredient | values across (gen3, gen2, gen1) | monotonicity | non-monotone? |
|:-------------------------------|:---------------------------------|:-------------|:--------------|
| Quadratic Casimir C₂(p,q) | [1.333, 3.0, 6.0] | strictly ↑ | NO |
| Triality t = (p−q) mod 3 | [1, 0, 0] | binary step at gen-3 | NO (not a gen-2 dip) |
| Irrep dimension dim(p,q) | [3, 8, 10] | strictly ↑ | NO |
| Greybody transmission exp(−2πC₂τ/κ) | monotone composite of C₂ | strictly ↓ in g | NO |
| Bare-ladder RMS √⟨λ²⟩ (diagonal d_g) | [1.296/1.833, 1.567/2.217, 1.963/2.776] | strictly ↑ (W3-9) | NO |
| Ω-scalar ratio Ω^c/Ω^D | constant = 1/2 (all g) | constant | NO (no g-dependence at all) |

**The structural root**: for the three sectors carrying the generations — (1,0) gen-3, (1,1) gen-2, (3,0) gen-1 — the SU(3) Peter-Weyl content of D_K is exhausted by two invariants: the quadratic Casimir C₂ (continuous, monotone here) and the triality t (a discrete Z₃ label, a binary step). The cubic Casimir adds no NEW monotonicity freedom (it is fixed by (p,q) alongside C₂ and is itself a polynomial in the same labels — no gen-2 reversal). The greybody and the bare RMS are both monotone *functions* of C₂, so any composition of them inherits monotonicity. There is therefore no algebraic route to a gen-2 dip: a function of a monotone argument, or a binary-step discrete label, cannot have a strict interior extremum at the middle generation. This is why W4-15's `routeb_seed = False` is not an artifact of the particular kernel — it is a theorem about the invariant content available on the slice.

Critically, the **triality step cannot be relocated to gen-2 by deformation**. The knowledge base records W2-11 (PROVEN, 0.00e+00 across 5 τ-points × 2 generators): triality is preserved INTACT under the Jensen TT-deformation (tensor-factor-disjoint commutation of T_s and σ_i). So even allowing the moduli-deformation (Level-2) freedom of the Jensen flow, the t = [1,0,0] step stays at gen-3; it does not become a [0,1,0] gen-2 spike. The discrete handle is frozen by the same symmetry that makes the triality count = 3 generations.

### II.3 — The third instance of the fermion-sector "one handle held" genus

**Result**: W4-15 joins §VII.BL and §VII.BS as the third member of a single structural genus — *the C₂-monotone (left-invariant, homogeneous) substrate forces same-signed / single-handle shapes; the missing degree of freedom is held against substrate-natural extraction.* Classification: **GEOMETRIC** (cross-pillar structural pattern, Pillar III ↔ Pillar VIII).

The three instances share a common skeleton but differ in WHICH handle is held — and the distinction is load-bearing for the S103 register maintenance:

| Instance | Substrate forces | Held handle (the missing DOF) | Fix location |
|:---------|:-----------------|:------------------------------|:-------------|
| §VII.BL Generation-Blindness (STAGE-3-PERMANENT) | every inner/twisted/real-image fluctuation acts SCALAR on each ℂ^{m(p,q)} ⇒ Yukawa hierarchy not deliverable (`R_cross=1.01970`, `n_distinct=2` ∀L_max) | the generation-SPLITTING magnitude | external non-LI `ε_LX` fibre connection OUTSIDE every A_K-module |
| §VII.BS Normalization-Non-Universality (STAGE-3-PERMANENT) | substrate fixes the conformal class + ALL dimensionless shapes; `O = w·Ô` rank-1 covariance | the single dimensional SCALE w = M_KK (the seconds-valued normalization) | externally-calibrated cutoff M_KK (one imported scale) |
| **§VII.BL/BS-genus — W4-15 (this FAIL)** | C₂-monotone greybody/RMS/triality content forces same-signed κ_g at all generations | the **sign-changing per-generation slope handle** (a gen-2 non-monotone DOF) | a substrate ingredient OUTSIDE the single-τ-slice Peter-Weyl invariant set (full-SU(3) σ-model / off-diagonal triality coupling / 2nd modulus) — see §IV |

The genus is the homogeneity obstruction: SU(3) left-invariance makes D_K's representation multiplicity-scalar and its G-invariant scalars Casimir-graded. §VII.BL says homogeneity blinds the SPLITTING; §VII.BS says it blinds the SCALE; W4-15 says it blinds the SIGN-CHANGE. All three are the same wall — the fabric's intrinsic differential calculus is generation-blind / scale-silent / monotone — viewed through three different observables.

### II.4 — The structural payoff that survives: the CKM triality texture

**Result**: gen3↔gen2 and gen3↔gen1 CKM channels are EXACTLY zero (CG-inadmissible, `t(p,q)=(p−q) mod 3`, t=1 vs t=0); gen2↔gen1 (Cabibbo) is the sole admissible channel; triality-masked proxy `M[gen2,gen1]=0.1534`, `M[gen3,*]=0` exactly. Classification: **PARTICLE**.

The same triality binary step that WALLS the crossing is the ENGINE of a genuine substrate prediction. Because the third generation (1,0) sits in a distinct triality class from (1,1)/(3,0), V_ub and V_cb are triality-suppressed relative to the Cabibbo V_us — qualitatively the observed CKM hierarchy. This is a clean intra-pillar triality theorem on the inter-generation channels, independent of the crossing FAIL. It is the structural reason the WALL is informative: the same SU(3) Peter-Weyl orthogonality that protects the proton (W4-18, T17) and forces Cabibbo dominance (here) is what forbids a sign-changing slope handle (W4-15). One symmetry, three consequences — the cross-domain coherence is the framework's signature, not a coincidence.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| W4-15 `CF-S102-QUARK-PERGEN-KERNEL` | **FAIL** (sign/mag/regime = FAIL/FAIL/VALID) | κ_g = +0.07295/+0.04078/+0.00384 (signflip=False, crossing=False); gen-3 up-dressing +0.00490 vs +0.53699 required (2 OOM short) |
| W4-16 `CF-S102-KAPPA-NU-FIRSTPRINCIPLES` | INFO (PASS/FAIL/VALID) | s_ν sign FORCED (+, widening); magnitude ≈+0.0877 vs +0.5469 back-solve (rel 0.84) |
| W4-17 `CF-S102-NU-GRADING-EXTERNAL-EPSLX` | INFO (PASS/—/VALID) | Y₃/Y₂ reconstruct 2.4882512 at rel 5.3e-09; ε_LX HELD (not substrate-motivated) |
| W4-18 `CF-S102-MODELC-PHENO-SCALES` | PASS (set-membership) | τ_p = 6.26e39 yr (T17 tree-zero) > Super-K; S₁ 8.7 OOM above flavor reach |
| W4-19 `CF-S102-M0-TRANSFER-CONVENTION` | PASS (PASS/PASS/VALID) | boundary-RG derived; spread 1.1806% → 0.0000%; residual −0.4612% |
| W4-20 `S102-MH-ROUTE-SELECTION` | PASS (PASS/PASS/VALID) | Route B FORCED, m_H=131.8 GeV; L_sat=6, Aitken overshoot 1.2416× floor |

(W4-15 verdict authoritative per the gate's [SIGN] 3-tuple; not re-adjudicated. Other rows reported for cross-wave context — the FORCED-dimensionless/HELD-dimensional pattern of §IV draws on W4-16/17/20.)

---

## IV. Structural Implications

### IV.1 — WALL classification: the discriminating test and its verdict

The classification rule is the one the Focus pins: WALL iff the substrate provides NO sign-changing per-generation slope handle (a permanent structural wall, registry-candidate theorem); GAP iff a SPECIFIC not-yet-tested substrate ingredient can be named with a pre-registerable forward gate. The discriminator is whether ANY enumerated candidate non-monotone ingredient survives the C₂-monotonicity test of §II.2.

**Every candidate fails the test on the single-τ-slice spectral triple** (the substrate object the dressed-block kernel actually lives on). The verdict is **WALL** at the single-τ-slice level (Level 1 per `phononic-framing.md §"Single-τ-slice vs moduli-deformation"`): the obstruction is regulator-invariant and L_max-independent (it is a statement about which G-invariant scalars exist, not about a truncated numerical value), and it holds at every τ on the Jensen ridge because W2-11 freezes the triality step at gen-3 across the deformation (Level-2 robustness of the binary handle).

The candidate GAP ingredients named in the Focus — non-Casimir-monotone quantity from the full-SU(3) σ-model, off-diagonal triality structure, a second deformation modulus, off-Jensen Schur-rigidity directions — are each tested in §IV.2. The key finding: **none of them is an ingredient of the single-τ-slice Peter-Weyl spectral triple**. They are all UPSTREAM structural extensions (a richer geometry that the framework does not currently possess as a closed object). A handle that requires building a new geometry is not a "not-yet-tested substrate ingredient" in the 4-field-CF sense; it is the absence of the handle. This is exactly the §VII.BL pattern: the Yukawa hierarchy was classified as a PERMANENT obstruction (not an open gap) precisely because the fix (`ε_LX`) lives OUTSIDE every A_K-module — outside the substrate's own differential calculus. The same logic applies here: a sign-changing slope handle lives outside the single-τ-slice invariant set, so the corridor is a WALL.

### IV.2 — Enumerated GAP-candidate ingredients, each tested against C₂-monotonicity

| GAP candidate (Focus-named) | Does it supply a gen-2 non-monotone DOF? | Is it on the single-τ-slice spectral triple? | Verdict |
|:----------------------------|:------------------------------------------|:---------------------------------------------|:--------|
| **non-Casimir-monotone quantity from full-SU(3) σ-model** | POSSIBLY (a σ-model field profile need not be Casimir-graded) | NO — the full SU(3) σ-model is the deferred upstream object (my MEMORY: "Rank-universality 7-count requires upstream full-SU(3) sigma-model (deferred)") | WALL-side: not a current substrate ingredient; building it is a new-geometry program, not a gate |
| **off-diagonal triality structure** (cross-triality coupling) | NO at the current level — W2-11 proves triality is tensor-factor-disjoint and Jensen-invariant; cross-triality terms are forbidden by CG-admissibility (the same selection rule that gives §II.4); an off-diagonal coupling would need to BREAK the triality grading | NO — would require an external non-LI connection (§VII.BL `ε_LX`-class) | WALL-side: forbidden by the triality selection rule that is itself a substrate theorem |
| **second deformation modulus** (beyond τ) | NO for the sign handle — the §VII.BR Schur-rigidity theorem (STAGE-3-PERMANENT) shows the U(2)-invariant TT (τ,μ) surface; a second modulus μ deforms the spectrum but is still G-invariant ⇒ Casimir-graded ⇒ monotone; my MEMORY: "Off-Jensen gradient = 0 by Schur" | PARTIALLY (μ is a Level-2 modulus) but Casimir-graded | WALL-side: a second G-invariant modulus stays monotone; no gen-2 reversal |
| **off-Jensen Schur-rigidity directions** | NO — §VII.BR + my MEMORY "Off-Jensen gradient = 0 by Schur (U(2) invariance, Jensen line is valley attractor)": off-Jensen directions are gradient-zero, the Jensen line is the valley attractor; off-Jensen excursions are not stable substrate states | NO — off-Jensen is off the substrate's stable configuration | WALL-side: Schur rigidity closes this direction |

**Conclusion**: all four named GAP candidates resolve to the WALL side. Each is either (a) not an ingredient of the current substrate object (full-SU(3) σ-model — deferred upstream), (b) forbidden by a substrate selection-rule theorem (off-diagonal triality — CG-inadmissibility + W2-11), or (c) Casimir-graded-and-therefore-monotone (second modulus, off-Jensen — §VII.BR Schur rigidity). **No candidate names a not-yet-tested ingredient OF the substrate that could supply a gen-2 non-monotone DOF.** Therefore `CF-S103-QUARK-KAPPA-G-<handle>` does NOT instantiate as a GAP gate — there is no fillable `<handle>`, hence no fillable What/Inputs fields, hence no 4-field-complete CF (consistent with the W4 team-lead's judgment that the κ_g-derivation routing fails the 4-field test on What/Inputs because "the missing ingredient is not yet identified — no machinery pin is possible").

### IV.3 — The cross-session FORCED-dimensionless / HELD-dimensional pattern: one genus, but W4-15 is a DISTINCT axis

The Focus asks whether the W4-15 FAIL + the W4-16 s_ν (sign-FORCED / value-HELD) + the W4-17 ε_LX (architecture-FORCED / δA-HELD) + the W4-20 m_H (route-FORCED / scale-external) are ONE instance of the single rank-1 normalization gap (§VII.BS), or INDEPENDENT.

**They are the same GENUS but NOT the same theorem — and the distinction matters for the rank-9b/rank-1 register.** The unifying skeleton across all four is: *the substrate FORCES the dimensionless / structural content (a sign-species, a sign of a slope, an architecture, a route) and HOLDS the dimensional / magnitude content (a value, a scale, a connection strength).* This is the surface signature of §VII.BS's `O = w·Ô` factorization: the substrate determines `Ô` (the protected dimensionless kernel) and imports `w` (the externally-calibrated scale). On that reading, W4-16/17/20 are FRW-cousin instances of the rank-1 normalization gap at the particle-sector scale.

But W4-15 is structurally on a DIFFERENT axis, and conflating it would mis-file the register:

- §VII.BS / W4-16 / W4-17 / W4-20 are **scale/magnitude** holds — the missing DOF is a *dimensional number* (a Yukawa magnitude, a Dirac scale, an ε_LX strength, the m_H GeV scale). The structure (`Ô`) is complete; only the multiplicative `w` is imported. The fix is to supply ONE scale at the source.
- W4-15 is a **sign-handle** hold — the missing DOF is a *dimensionless sign-changing degree of freedom* (a gen-2 non-monotone reversal). This is NOT a magnitude that the `O = w·Ô` factorization holds; it is a *qualitative shape feature absent from the protected kernel `Ô` itself*. Supplying a scale `w` does nothing — the slopes are same-signed at every scale.

So W4-15 belongs to the §VII.BL branch of the genus (the homogeneity obstruction on the SPLITTING/SHAPE content) NOT the §VII.BS branch (the homogeneity obstruction on the NORMALIZATION/SCALE content). The genus tree is:

```
Homogeneity obstruction (SU(3) left-invariance ⇒ multiplicity-scalar + Casimir-graded)
├── SHAPE/SPLITTING branch (the dimensionless qualitative content the substrate cannot supply)
│   ├── §VII.BL  Generation-Blindness — cannot supply the SPLITTING magnitude (held: ε_LX)
│   └── §VII.BL/BS-genus W4-15 — cannot supply the SIGN-CHANGE (held: gen-2 non-monotone DOF)  ← NEW
└── SCALE/NORMALIZATION branch (the dimensional content the substrate imports as one cutoff)
    ├── §VII.BS  Normalization-Non-Universality — imports one scale w=M_KK
    ├── W4-16 s_ν magnitude (held: absolute Dirac scale)
    ├── W4-17 ε_LX magnitude (held: δA fibre-connection strength)
    └── W4-20 m_H (route forced; scale-external 67/1251 band-MISS)
```

**Register recommendation for S103 (rank-9b / rank-1 maintenance)**: record W4-15 as a NEW member of the SHAPE/SPLITTING branch of the homogeneity-obstruction genus, a SIBLING of §VII.BL (not §VII.BS). The §VII.BS rank-1 normalization gap remains the SCALE-branch anchor; W4-16/17/20 are its particle-sector cousins. The W4-15 WALL is the SECOND theorem in the SHAPE branch — the genus now has explicit two-branch structure, and the EVOI register should carry the genus as a single "homogeneity obstruction" rank-1-class entry with two sub-branches (shape, scale), NOT four independent open items.

### IV.4 — What opens, closes, shifts

- **CLOSED** (constraint-map, authoritative from W4-15): the quark gen-1↔gen-3 crossing corridor for the dressed-block greybody per-gen kernel. The W2-4 uniform-κ impossibility EXTENDS to the substrate-DERIVED per-gen kernel. Both the uniform handle and the derived handle are now eliminated.
- **PROMOTED to WALL** (this synthesis recommends): the obstruction generalizes from "this kernel fails" to "NO single-τ-slice substrate ingredient can supply a sign-changing per-generation slope handle" — a registry-candidate `no-sign-changing-slope-handle` theorem (§V.1). This is the structural upgrade the Focus asks for: not "the gate FAILed" but "the corridor is walled."
- **SURVIVES** (independent of the FAIL): the CKM triality texture (gen3 channels exactly forbidden, Cabibbo dominant). Routes to its own registry landing (CF-W4-2, already queued).
- **SHIFTED**: the cross-session FORCED/HELD pattern is now resolved into a two-branch genus (§IV.3); W4-15 is the second SHAPE-branch theorem, sibling to §VII.BL, distinct from the §VII.BS scale branch.

The framework is STRENGTHENED by this WALL: it eliminates a wrong corridor (a substrate-derived quark crossing) and sharpens the boundary of what the homogeneous substrate can and cannot supply. The quark mass hierarchy, like the Yukawa hierarchy (§VII.BL), is now established to live in a non-homogeneous deformation OUTSIDE the substrate's intrinsic Casimir-graded calculus — the same structural conclusion, reached through a different observable. Joint coherence across §VII.BL (splitting), W4-15 (sign), §VII.BS (scale) is itself evidence: three independent fermion-sector observables all hit the same homogeneity wall.

---

## V. Carry-Forward Computations

> **Classification consequence**: I classify the corridor as **WALL**, so the κ_g-derivation does NOT become a GAP compute CF (`CF-S103-QUARK-KAPPA-G-<handle>` does not instantiate — no fillable `<handle>` survives the §IV.2 enumeration). The single forward item is a registry-state WRITE (a §VII registry-candidate WALL theorem), which is the registry sole-writer's landing, NOT mine to effect. It is recorded below as a 4-field registry-landing CF (artifact-existence PASS predicate, AFTER-pattern single-shot per `registry-landing.md`), so it propagates to the S103 plan. The §IV.3 register-maintenance item (genus two-branch structure for EVOI rank-9b/rank-1) is a register-maintenance action for `/rclab-plan` Phase 1c-REGISTERS, recorded as V.2.

```
V.1. §VII registry-candidate landing — No-Sign-Changing-Slope-Handle Theorem (quark gen-1↔gen-3 crossing WALL)
   - What: Land a §VII registry-candidate STRUCTURAL theorem (next-free §VII letter slot,
           AFTER-pattern single-shot per registry-landing.md §"Bridge-Landing Script Architecture"):
           "No-Sign-Changing-Slope-Handle Theorem — the single-τ-slice spectral triple (A_K, H_K, D_K(τ_fold))
           provides NO G-invariant scalar that is non-monotone across the three generation sectors
           {(1,0), (1,1), (3,0)} (C₂ = {4/3, 3, 6}); every per-generation slope kernel built from the
           Peter-Weyl invariant content (C₂-graded greybody, bare-ladder RMS, Jensen-invariant triality step)
           is same-signed across generations ⇒ the joint quark crossing (gen-1 inversion ∧ gen-3 upright)
           is NOT deliverable by any single-τ-slice A_K-built kernel."
           Declare: intra-pillar structural theorem (5-anatomy + 3-level N/A-with-reason, precedent §VII.BL/BM/BO);
           Level-1 single-τ-slice; algebra-INVARIANT operator layer; SOURCE-DOUBLE-CITE-CO-PRIMARY Corner-I
           (W4-15 verdict V_input + the route-(b)-exhaustion enumeration C_output); STRUCTURAL-ORTHOGONAL-COMPANION
           to §VII.BL (SHAPE-branch sibling — NOT co-primary, cross-corner co-primary FORBIDDEN); cite W2-11
           triality-preservation (Level-2 robustness of the binary handle) + §VII.BR Schur-rigidity (off-Jensen
           closure) as the two structural pins that make the WALL deformation-stable.
   - Inputs: s102_quark_pergen_kernel.npz (audit 77659eb6809d3d46…, 58 keys — κ_g slope asymmetry, routeb_seed=False,
             Ω^D/Ω^c=2 Sage-exact); §VII.BL Generation-Blindness Obstruction (STAGE-3-PERMANENT, the SHAPE-branch anchor);
             §VII.BR Schur-Rigidity (STAGE-3-PERMANENT); W2-11 triality-preservation (PROVEN); the route-(b)
             enumeration table (§II.2 of this synthesis); SU(3) Peter-Weyl C₂/triality machinery
             (math-scripts.md selection-rule pre-flight section).
   - Gate: S103-NO-SIGN-HANDLE-REGISTRY-LANDING — artifact-existence + content-marker PASS predicate
           (PASS = §VII section body present with the 5 declared structural elements + the route-(b)-exhaustion
           table + the §VII.BL sibling-companion anchor; FAIL = section absent or missing a declared element).
           Sole writer per feedback_mack-bridge-role.md: this is a §VII NCG/geometric structural-theorem landing,
           NOT a §7 falsifier-surface row — mack-cosmic-bridge does NOT apply; landing author = the registry
           §VII sole-writer (gen-physicist precedent for §VII.BL/BM/BS landings).
   - Effort: 1 gate (registry-landing class; ~1 agent-session). No compute — the structural content is the
           W4-15 verdict + the closed-form enumeration; binding-text discipline applies (transcribe, do not re-derive).

V.2. Register-maintenance — homogeneity-obstruction genus two-branch structure (EVOI rank-9b / rank-1)
   - What: Update the EVOI table (sessions/evoi-framework.md) + atlas-08 open-questions to record the
           homogeneity-obstruction genus as ONE rank-1-class entry with TWO explicit sub-branches:
           SHAPE/SPLITTING branch {§VII.BL Generation-Blindness, V.1 No-Sign-Handle} and
           SCALE/NORMALIZATION branch {§VII.BS Normalization-Non-Universality, + particle cousins
           W4-16 s_ν / W4-17 ε_LX / W4-20 m_H scale holds}. This COLLAPSES four apparently-independent
           open items into one genus with two branches (per §IV.3), preventing the register from carrying
           the W4-15/16/17/20 FORCED/HELD instances as four separate rank-9b rows.
   - Inputs: §IV.3 genus tree (this synthesis); §VII.BL / §VII.BS section bodies (registry);
             W4-16/17/20 constraint-map rows (session-102-w4-workingpaper.md); current EVOI rank-9b/rank-1 rows.
   - Gate: register-maintenance action (NOT a compute gate) — consumed by /rclab-plan Phase 1c-REGISTERS at
           S103 plan-freeze; PASS predicate = EVOI table content-currency marker advanced to S103 with the
           two-branch genus entry present.
   - Effort: register-maintenance pass (~0.5 agent-session; folds into the S103 plan-time wrap-up).

V.3. (DEFERRED — not 4-field-complete; recorded for honesty, NOT propagated) full-SU(3) σ-model sign-handle search
   - What: IF the deferred full-SU(3) σ-model is ever built as a closed substrate object, test whether a
           σ-model field profile supplies a gen-2 non-monotone (non-Casimir-graded) DOF that could reopen the crossing.
   - Inputs: the full-SU(3) σ-model (DOES NOT EXIST as a closed object — deferred upstream per agent MEMORY;
             this is the binding Inputs gap).
   - Gate: none pre-registerable — no machinery pin possible until the σ-model is constructed.
   - Effort: UNBOUNDED (a new-geometry construction program, not a gate). This FAILS the 4-field test on
           Inputs/Gate and is therefore NOT a propagating CF — it is the WALL's far-side boundary marker,
           recorded so a future session does not mistake the WALL for an un-attempted GAP.
```

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | κ_g slope asymmetry +0.07295/+0.04078/+0.00384, signflip=False, crossing=False | PARTICLE / GEOMETRIC | W4-15 FAIL (authoritative) | Dressed-block greybody per-gen kernel cannot force the quark crossing |
| 2 | NO substrate quantity non-monotone across generations (C₂↑, triality binary-step, dim↑, greybody↓, RMS↑) | GEOMETRIC | Structural (enumerated, L_max-independent) | Route-(b) exhaustion is a theorem, not an artifact; root = Casimir-graded invariant content |
| 3 | Corridor classified **WALL** — no-sign-changing-slope-handle | GEOMETRIC | Recommended §VII registry-candidate (V.1) | Permanent wall, NOT an enumerated gap; `CF-S103-QUARK-KAPPA-G-<handle>` does NOT instantiate |
| 4 | Third instance of homogeneity-obstruction genus (after §VII.BL, §VII.BS) | GEOMETRIC | Cross-pillar structural pattern | SHAPE-branch sibling of §VII.BL (sign-change); distinct from §VII.BS scale-branch |
| 5 | CKM triality texture (gen3 channels exactly forbidden, Cabibbo dominant) | PARTICLE | Survives independent of FAIL (CF-W4-2 queued) | Same triality step that walls the crossing predicts the CKM hierarchy |
| 6 | FORCED-dimensionless/HELD-dimensional pattern = ONE genus, TWO branches | GEOMETRIC | Register-maintenance (V.2) | W4-15 (shape) ≠ §VII.BS branch (scale); collapses 4 open items to 1 genus/2 branches |

---

*Substrate-first framing preserved throughout (`phononic-framing.md`): the fabric IS the spectral triple (A_K, H_K, D_K) on Jensen-deformed SU(3); generations ARE its Peter-Weyl multiplicity; the per-generation slope content IS the Casimir-graded G-invariant scalar set. Direction of explanation: D_K eigenvalues → Peter-Weyl invariant content (C₂, triality) → per-generation slope asymmetry → quark mass ordering. The WALL is a substrate-IS structural fact: the homogeneous fabric's intrinsic differential calculus is monotone in C₂, so it cannot supply a sign-changing slope handle — the quark crossing, like the Yukawa hierarchy, lives in a non-homogeneous deformation OUTSIDE the substrate's own calculus. FORBIDDEN inversion (container thinking): "the quark masses are values placed on the fabric and the kernel should fit them" → INVERT: "the fabric's Casimir-graded invariant content IS the slope structure; it is same-signed by homogeneity; the crossing requires a handle the homogeneous fabric does not carry."*
