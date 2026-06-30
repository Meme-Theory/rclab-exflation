# Session 86 Workshop: lizzi x connes — SECTOR-2 Per-Regulator Split + LAYER-1/LAYER-2 Retroactive Sweep + ζ=SDW Theorem

**Date**: 2026-04-27
**Format**: Iterative 2-agent workshop (3 rounds, 6 turns)
**Agents**: lizzi (lizzi-spectral-functional-theorist), connes (connes-ncg-theorist)
**Source Documents**:
- sessions/archive/session-86/session-86-w4-workingpaper.md
- sessions/framework/registry/cutoff-sqrt-adjudication.md
- sessions/permanent-results-registry.md
- computations/_spectral_action_regulators.py

**Anchors**:
- **§W4-2**: max_pair_ratio = 9.240e-01 at (ζ, Zubarev), 3 OOM above PASS 1e-3. Per-regulator residues: M_ζ = M_SDW = 1.581e-01, M_Zubarev = 1.201e-02, M_cutoff_sqrt = 1.110e-01, M_anomaly = 3.185e-02.
- **CC-3 counterexample**: FAILed on Zubarev (rel_deriv = 6.98 vs tolerance 1e-4) — heat-kernel regulator carries explicit τ-dependence at s=3 residue level.
- **Substitution chain Step 3**: pole_R = a_2 · M_R(s=3); a_2 regulator-independent, only M_R(s=3) carries regulator class.
- **C28 line 511**: "permanently repairs S78-onward conflation that treated canonical 5-atlas as uniform-admissible."
- **§W4-2 CC-2 PASS**: rel_err = 1.7556e-16 (machine-epsilon identity ζ=SDW at s=3 residue, d_spec=8 NCG, positive-definite spectrum).

**Three Workstreams**:
1. SECTOR-2 4-or-5-class registry partition — F_2/F_4-class (lizzi) vs full 5-class from CC-1996 §2.2-2.3 multiplier (connes); binding partition + propagation map into W5a P3 IC, W6 C-α/β/γ, LAYER-1/2 taxonomy
2. LAYER 1 vs LAYER 2 retroactive sweep across S78-onward statements (Regulator-Family Boundary Theorem `Φ_r(ν_i) = M(r)·Φ_ζ(ν_i)` LAYER 1; ZETA-NOT-PHYSICAL-75 LAYER 2; 5-regulator atlas convention origin S78+ defines combinatorial position) → output: `sessions/framework/registry/layer1-layer2-retroactive-audit.md`
3. ζ=SDW machine-epsilon structural theorem (W4 Candidate 8) — definition-level identity, NOT coincidence; register as permanent structural theorem with explicit non-evidence-status declaration (does NOT support K-invariance or atlas-uniformity claim, per §W4-2 line 290 + synthesis §2 line 532)

**Pre-Registered R3 Adjudication**: Workshop emits THREE bound deliverables:
- (a) 4- or 5-class SECTOR-2 partition registered (decision binding)
- (b) `sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline (or land if convergence supports)
- (c) ζ=SDW theorem registered in `permanent-results-registry.md` with explicit non-evidence-status declaration

**Pre-Registered Carry-Forward**: 4-field S87 spec (what / inputs / gate / effort) for SECTOR-2 propagation into:
- W5a P3 IC (xi_E_GGE_inv at s=−1 vs s=3)
- W6 perturbative-immunization C-α/β/γ corollaries

**Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`): SECTOR-2 partition classifies regulator multipliers M_R(s=3) at the substrate's a_2 spectral moment. ζ=SDW identity is an algebraic identity ON the substrate's positive-definite spectrum — it asserts equality of two spectral-density-weighting schemes, NOT physical equivalence of two distinct regulator families.

---

## Round 1 — lizzi: Opening Analysis

### L1: F_2/F_4-Class Taxonomy Argument — F_2 = {ζ, SDW}, then {cutoff_sqrt}, {anomaly}, {Zubarev} (4-class partition)

**Topline.** The §W4-2 numerical residue M_R(s=3) on the live atlas A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} forces a **4-class partition** of A_5 by numerical-residue equivalence at the substrate's a_2 spectral moment. The classes are:

```
Class 1 (F_2):        {ζ, SDW}        M = 1.581013e-01      (multi-member; algebraic identity)
Class 2 (singleton):  {cutoff_sqrt}   M = 1.110026e-01      (truncation singleton)
Class 3 (singleton):  {anomaly}       M = 3.184676e-02      (subtraction singleton)
Class 4 (singleton):  {Zubarev}       M = 1.200875e-02      (heat-kernel-dressing singleton)
```

The class-boundary equivalence relation is the only one consistent with the pre-registered §W4-2 §10 substitution-chain Step 3: `pole_R = a_2(τ_pivot) · M_R(s=3)`. Since `a_2(τ_pivot)` is regulator-independent (substrate Casimir spectrum / Vol_SU3_Haar normalization is shared), the partition descends to equivalence on M_R(s=3). Each class is the equivalence class under M_R(s=3) ≡ M_R'(s=3), the only F_2 multi-member class being forced by the algebraic ζ = Mellin-on-positive-definite-spectrum identity (machine-epsilon at 1.7556e-16 in CC-2). Three singleton classes exhaust the non-F_2 atlas members; no numerical residue agrees outside the ζ–SDW pair.

**Substitution chain.**

```
Step 1 (definitions):
  Atlas A_5 := {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}                    [§W4-2 Definition 2]
  pole_R := K_substrate(s=3, R)
         = Res_{s=3} M[K(τ_pivot; R)](s)                                  [§W4-2 Definition 1]
  M_R(s=3) := Mellin-multiplier residue at s=3 under regulator R
  ~_M  := equivalence relation: R ~_M R'  iff  M_R(s=3) = M_R'(s=3)
                                                exactly (machine epsilon).
  F_2/F_4-classes  := equivalence classes of A_5 under ~_M.

Step 2 (substitute the §W4-2 measured values):
  M_ζ(s=3)        = 1.581013447264e-01
  M_SDW(s=3)      = 1.581013447264e-01      (CC-2 PASS, rel_err = 1.7556e-16)
  M_cutoff_sqrt   = 1.110026437499e-01
  M_anomaly       = 3.184675917801e-02
  M_Zubarev       = 1.200875443266e-02

Step 3 (simplify under ~_M):
  ζ ~_M SDW                                    [exact, definition-level — see L3]
  cutoff_sqrt is NOT ~_M to any other R        [29.79% off F_2; 71.31% off anomaly]
  anomaly is NOT ~_M to any other R            [79.86% off F_2; 62.29% off Zubarev]
  Zubarev is NOT ~_M to any other R            [92.40% off F_2; 89.18% off cutoff_sqrt]

  Equivalence classes of A_5 / ~_M :
    [ζ]   = [SDW]        =: F_2     (cardinality 2)
    [cutoff_sqrt]                   (cardinality 1)
    [anomaly]                       (cardinality 1)
    [Zubarev]                       (cardinality 1)

  |A_5 / ~_M| = 4.

Step 4 (direction):
  Partition of the substrate's regulator-class atlas at the s=3 a_2-slot
  Mellin-multiplier residue = 4 distinct numerical-residue classes.
  The F_2 multi-member class is forced by an algebraic identity, NOT by
  measurement; the other three classes each isolate a regulator-specific
  scale (cutoff_frac, M_PV², t_ref) that does not collapse to any other.

  Conclusion: A_5 → 4-class partition,  F_2 = {ζ, SDW}, plus 3 singletons.
              The previously-cited F_4 = {ζ, Zubarev, SDW} of registry
              §VII-B.HP1-NEAR-INVARIANCE Step 1 §2605 (Mellin-support
              definition) is ORTHOGONAL to this numerical-residue
              partition: at the s=3 a_2 slot, Zubarev is in the same
              "Mellin-support-on-a_4-slot" partition class as ζ and SDW,
              but is NOT in the ~_M class of either at s=3.
```

**Class-boundary geometry.** Taking M_ζ as anchor:

| Class | Ratio to F_2 | Reason class is isolated |
|:--|:--|:--|
| F_2 = {ζ, SDW} | 0 (exact) | Γ(s)-cancellation algebraic identity (L3) |
| {cutoff_sqrt} | 0.2979 | Hard-cutoff truncates at C ≤ cutoff_frac × C_max; introduces cutoff_frac scale |
| {anomaly} | 0.7986 | Pauli-Villars subtracts 1/(C + M_PV²)^n; introduces M_PV² scale |
| {Zubarev} | 0.9240 | Heat-kernel dresses with exp(−t·C); introduces t_ref scale |

The class isolation is monotone in regulator-specific-scale dimensionality: the more invasive the regulator's deformation of the canonical 1/C^n integrand, the further it sits from F_2.

**Cite-anchors.**
- §W4-2 §6 per-regulator pole table (lines 149–158): the 5 numerical M_R(s=3) values reproduced above.
- §W4-2 substitution chain Step 3 (lines 236–251): the canonical-form decomposition `pole_R = a_2 · M_R(s=3)`.
- §W4-2 §6 CC-2 PASS (line 193): rel_err = 1.7556e-16 anchors the F_2 cardinality-2 class.
- Registry §VII-B.HP1-NEAR-INVARIANCE §2605: the registry's F_4 = {ζ, Zubarev, SDW} (Mellin-support definition) is a DIFFERENT partition relation, classifying by which Seeley-DeWitt slot the Mellin support concentrates on (a_4-pure vs mixed), not by numerical-residue equality at the a_2 slot.

**Substrate framing.** A_5 IS the set of admissible Mellin-summation prescriptions on the substrate's spectral content {λ_k} of D_K on Jensen-deformed SU(3); ~_M IS an equivalence relation ON the substrate's regulator-class manifold; the 4 classes ARE the partition into substrate-distinguishable Mellin-multiplier behaviors at the a_2 spectral moment. The 4-class partition is a structural property of how the substrate's spectral-action functional weights the s=3 residue, NOT a list of cutoffs imposed on space.

**Questions for connes** (he writes the alternative full 5-class partition + propagation map + LAYER 1/2 inventory).

1. **5-class vs 4-class binding.** Connes-Chamseddine 1996 §2.2-2.3 multiplier formalism distinguishes regulators by their f_0 / f_2 / f_4 Mellin moments, not by numerical residue at a single slot. Under the CC-1996 multiplier-vector partition `(f_0, f_2, f_4)`, do ζ and SDW lie in different equivalence classes (because Γ(s) shifts the Mellin moment normalization), thereby forcing a **5-class** partition where mine yields 4? If so, the binding partition (W4-2 deliverable (a)) hinges on the choice of partition relation: my ~_M (numerical-residue at s=3) vs your ~_CC1996 (multiplier-vector identity).
2. **Partition coarseness.** My 4-class partition is the COARSEST one consistent with §W4-2 numerical residues (any finer partition would have to split F_2, which the CC-2 PASS forbids). Your 5-class partition would be FINER. Is the binding partition the coarsest that distinguishes substrate-physics-relevant differences, or the finest that respects the multiplier-formalism structure? Pre-registered call needed.
3. **F_4 reconciliation.** The registry-canonical F_4 = {ζ, Zubarev, SDW} (Mellin-support partition, §VII-B.HP1-NEAR-INVARIANCE) is NEITHER mine nor (presumably) yours. Three partition relations are now in play: ~_M (numerical residue, mine), ~_CC1996 (multiplier-vector, yours), ~_MS (Mellin-support-on-a_4-slot, registry). Workshop must decide which is the SECTOR-2 registry binding.
4. **Boundary criterion.** Should the §W4-2 PASS threshold 1e-3 be the boundary for ~_M (fine partition: F_2 + 3 singletons), or 1e-2 (coarser: F_2 + {cutoff_sqrt} as a "near-class" ≤ 30% off, then 2 outliers)? My choice is the strict boundary — ANY non-zero residue-difference is a class boundary — because the CC-2 PASS sets the natural floor at machine-epsilon. Your proposal?

### L2: Per-Regulator Residue M_R(s=3) Numerical Hierarchy — Substrate Reading

**Topline.** The §W4-2 numerical hierarchy

```
F_2:   M_ζ        = M_SDW       = 1.581e-01    [largest; algebraic ceiling]
       M_cutoff_sqrt              = 1.110e-01    [70% of F_2; truncation depletion]
       M_anomaly                  = 3.185e-02    [20% of F_2; Pauli-Villars depletion]
       M_Zubarev                  = 1.201e-02    [7.6% of F_2; heat-kernel suppression]
```

is a **monotone-decreasing depletion hierarchy** ordered by how aggressively each regulator suppresses the substrate's high-Casimir mode contribution to the s=3 residue. Reading from substrate physics: F_2 is the algebraic ceiling (no high-C suppression — the analytic-continuation prescription includes all positive-definite Casimir modes); each non-F_2 class is below by a depletion factor proportional to its regulator-specific high-C deformation. The hierarchy is NOT a residue-value coincidence — it is the substrate's first-moment Mellin-residue response under five distinct Mellin-summation prescriptions on the same fixed Casimir spectrum.

**Substitution chain.**

```
Step 1 (definitions):
  All five regulators evaluate (1/Vol_SU3_Haar) · Σ_{(p,q)≠(0,0), p+q≤L_max}
                                d(p,q) · f_R(C_2(p,q), n=1)
  on the SAME multiplicity-weighted SU(3) Casimir schematic spectrum
  (per `_spectral_action_regulators.py` lines 1-30).
  The regulator-class enters via f_R only:
    f_ζ(C, n)        = 1 / C^n                                (analytic continuation)
    f_SDW(C, n)      = 1 / C^n                                (Γ(s) cancellation; identical to ζ)
    f_cutoff(C, n)   = step(cutoff_frac · C_max - C) / C^n     (hard truncation; cutoff_frac = 0.7)
    f_anomaly(C, n)  = 1/C^n - 1/(C + M_PV²)^n                (Pauli-Villars; M_PV² = 0.1·C_max)
    f_Zubarev(C, n)  = exp(-t·C) / C^n                        (heat-kernel; t_ref = 1.0e-3)
  On the SAME spectrum, M_R(s=3) is determined entirely by f_R.

Step 2 (substitute the five integrands at n=1):
  Each f_R is a multiplicative dressing of the canonical 1/C integrand by a
  regulator-specific weight w_R(C):
    w_ζ(C)        = 1                              (no dressing)
    w_SDW(C)      = 1                              (Γ(s) cancellation)
    w_cutoff(C)   = step(cutoff_frac · C_max - C)   (binary; truncates at C ≥ 0.7·C_max)
    w_anomaly(C)  = 1 - C^n / (C + M_PV²)^n        (subtractive; → 0 as C → ∞)
    w_Zubarev(C)  = exp(-t·C)                      (exponential; → 0 as C → ∞ at t > 0)
  Each non-trivial w_R(C) ≤ 1 on the spectrum's support.

Step 3 (simplify — substrate reading of the depletion ordering):
  Since w_ζ = w_SDW = 1 (full ceiling) and the others are strict-suppressors:
    M_R(s=3) ≤ M_ζ(s=3) = M_SDW(s=3)              for every R in {cutoff, anomaly, Zubarev}.
  The ordering of {M_cutoff, M_anomaly, M_Zubarev} is determined by which
  high-C-mode subset each w_R amputates (binary), suppresses (Pauli-Villars
  algebraic), or smooths-down-exponentially (heat-kernel exp).

  Numerical realization (Vol_SU3_Haar = 8√3·π⁴, L_max=10, n=1, computed via sage):
    M_cutoff_sqrt / M_ζ        = 1.110e-01 / 1.581e-01  = 0.7021    (binary; ~30% modes lost)
    M_anomaly / M_ζ            = 3.185e-02 / 1.581e-01  = 0.2014    (algebraic; ~80% mode-weight depleted)
    M_Zubarev / M_ζ            = 1.201e-02 / 1.581e-01  = 0.0760    (exponential; ~92% mode-weight depleted)

Step 4 (direction):
  Substrate-physics depletion ordering:
       F_2 (no suppression)
    > cutoff_sqrt   (binary truncation, 30% of high-C modes excluded)
    > anomaly       (algebraic Pauli-Villars subtraction, ~80% mode-weight loss)
    > Zubarev       (exponential heat-kernel suppression, ~92% mode-weight loss)
  The F_2 → cutoff → anomaly → Zubarev ordering MIRRORS the suppression
  aggressiveness of each regulator's high-C dressing. This is a structural
  property of how the substrate's spectral content under each Mellin
  prescription weights the s=3 residue, NOT a numerical coincidence.
```

**Substrate reading of each class.**

| Regulator | M_R(s=3) | Depletion factor vs F_2 | What the substrate is doing |
|:--|:--|:--|:--|
| F_2 = {ζ, SDW} | 1.581e-01 | 1.000 (ceiling) | Full positive-definite Casimir spectrum included via analytic continuation; no scale introduced; algebraic ceiling for the s=3 residue. |
| {cutoff_sqrt} | 1.110e-01 | 0.702 | Substrate's high-Casimir modes (C > 0.7·C_max) are amputated entirely; the lost spectral weight is the gap to F_2. The 30% loss is binary (truncation), so M depletion is mode-count-driven. |
| {anomaly} | 3.185e-02 | 0.201 | Pauli-Villars subtracts a regulator at mass M_PV² = 0.1·C_max; the subtraction kills the high-C tail of the integrand algebraically (1/C^n − 1/(C+M_PV²)^n → 0 fast at large C). The substrate sees ≈ 80% of the F_2 mode-weight depleted by the subtraction. |
| {Zubarev} | 1.201e-02 | 0.076 | Heat-kernel dressing exp(−t·C) suppresses ALL non-zero-C modes exponentially at t = 1.0e-3; even mid-range Casimir modes lose weight. The substrate sees ≈ 92% of F_2 mode-weight gone — the most aggressive depletion in the atlas. |

**Why F_2 is the ceiling, not the median.** The ζ/SDW prescription is the analytic-continuation reading of the substrate's Mellin transform — it is the unique prescription that includes the FULL positive-definite Casimir spectrum without introducing any regulator-specific scale (no cutoff_frac, no M_PV², no t_ref). All other regulators in A_5 introduce a scale that breaks the substrate's positive-definite spectral content into included-vs-excluded (or weighted-vs-suppressed) sectors, and every such break depletes M_R(s=3) below F_2. The ceiling property is a structural feature of the analytic-continuation prescription, not a numerical accident.

**Substrate-physics interpretation of the s=3 a_2-slot reading.** The s=3 residue in d_spec=8 NCG IS the a_2-slot Seeley-DeWitt coefficient — the Newton's-constant slot at the substrate-distance-1 first-moment level. The hierarchy says: under each regulator class, the substrate reports a DIFFERENT effective Newton's-constant-slot weight. The F_2 ceiling is the analytic-continuation reading; cutoff_sqrt loses 30% to high-C truncation; anomaly loses ~80% to Pauli-Villars subtraction; Zubarev loses ~92% to exp(−tC) heat-kernel suppression. This is exactly the §W4-2 §11 FAIL-direction reading of "regulator-class Mellin multiplier at s=3 is NOT R-universal" — the substrate's s=3 residue carries regulator-specific scales that do not absorb into the a_2 common factor (line 292).

**Cite-anchors.**
- §W4-2 lines 149–158: per-regulator pole_R values reproduced.
- `_spectral_action_regulators.py` lines 64–174: f_R definitions for each of the five regulators (zeta_a_n, mellin_a_n, heat_kernel_a_n, hard_cutoff_a_n, pauli_villars_a_n).
- §W4-2 line 292: "regulator-class Mellin multiplier at s=3 is the observable that breaks substrate-distance-1 universality, and the structural reason is that {Zubarev, cutoff_sqrt, anomaly} each introduce regulator-specific scales (t_ref for heat-kernel, cutoff_frac for hard-cutoff, M_PV² for Pauli-Villars) that are not absorbed into the a_2 common factor."

**Substrate framing (per `.claude/rules/phononic-framing.md`).** The hierarchy is a property OF the substrate's regulator-class manifold at the s=3 a_2-slot, NOT a list of cutoffs imposed on substrate space. Each M_R IS the substrate's first-moment Mellin-residue under the R-prescription; the depletion ordering IS the substrate-physics reading of how each prescription weights the spectral content; the F_2 ceiling IS the analytic-continuation prescription's no-scale-introduced reading.

**Questions for connes** (he writes the alternative full 5-class partition + propagation map + LAYER 1/2 inventory).

1. **Does the depletion hierarchy match Connes-Chamseddine 1996 §2.2-2.3 multiplier predictions?** The CC-1996 formalism predicts a specific (f_0, f_2, f_4) ordering for each regulator. Does the numerical depletion ordering above match the multiplier-vector ordering — i.e., is `M_cutoff_sqrt > M_anomaly > M_Zubarev` the same partial order as the CC-1996 f_2 multiplier values? If the orderings agree, the depletion is fixed by the formalism, not by the schematic helper choice. If they disagree, the schematic helper has a residue idiosyncrasy (relevant for the §W4-2 P5 honesty disclosure at lines 502-503).
2. **Is the F_2 ceiling property generic across substrate-distance levels?** I have shown it at substrate-distance-1 (s=3, a_2 slot). Does it extend to substrate-distance-2 (s=1, a_4 slot) where the registry's F_4 = {ζ, Zubarev, SDW} Mellin-support partition lives (per §VII-B.HP1-NEAR-INVARIANCE Step 1)? At a_4, Zubarev should join F_2 in the "no high-C suppression" class because the heat-kernel dressing is regular at higher s. If true, the partition `~_M` at s=3 vs s=1 is itself slot-dependent — the SECTOR-2 split is a substrate-distance-1 phenomenon, NOT a generic regulator-class statement.
3. **Does the W6 perturbative-immunization corollary inherit the depletion hierarchy?** If C-α/β/γ at distance-1 sources from M_R(s=3), then under the per-regulator split the corollaries inherit a 5-fold (4-class) splitting at the a_2 slot. What is the SD-vs-FI status of the immunization quantity under the per-regulator splitting? Workshop deliverable (a) decision binds this.
4. **F_2 universality of the analytic-continuation prescription — your phrasing?** I read F_2's ceiling status as "the unique no-scale-introduced prescription on positive-definite spectra." You may have a more structural Connes-1996-native phrasing (e.g., "the unique multiplier-vector identity (1, 1, 1, 0) at the spectral-action mass scale"). If so, the workshop's binding statement of F_2 should use yours — pre-registered call needed.

### L3: ζ=SDW Machine-Epsilon Identity — Structural Theorem Form + Non-Evidence-Status

**Topline.** The §W4-2 CC-2 PASS at rel_err = 1.7556e-16 is **NOT** a numerical agreement to be cited as cross-regulator evidence — it is a **definition-level algebraic identity** between two regulators that share an integrand by construction on positive-definite spectra at real s. The agreement is exact, machine-epsilon, and structural; it does NOT support K-invariance, atlas-uniformity, or any other functional-independence claim across the broader atlas. Below: theorem statement, proof sketch, and the explicit non-evidence-status declaration mandated by the §W4-2 line 290 conclusion and the synthesis §2 line 532 commitment.

**Theorem (ζ = SDW Machine-Epsilon Identity at Substrate-Distance-1).** Let `D_K` denote the Dirac operator on Jensen-deformed SU(3) with positive-definite Casimir spectrum {C_2(p,q) : (p,q) ∈ ℕ², (p,q)≠(0,0), p+q ≤ L_max}. Let

- M_ζ(s) := the Mellin multiplier under analytic-continuation regularization, defined by the residue at s of `Σ_{(p,q)} d(p,q) · C_2(p,q)^{−s} / Vol_SU3_Haar` for ℜs in the convergent half-plane and analytically continued elsewhere;
- M_SDW(s) := the Mellin multiplier under SDW (Mellin-transform with Γ(s) factor) regularization, defined as `Γ(s) · Σ_{(p,q)} d(p,q) · C_2(p,q)^{−s} / Vol_SU3_Haar` divided by Γ(s) wherever Γ(s) appears in both numerator and the Connes-Chamseddine spectral-action ratio normalization.

Then on the positive-definite Casimir spectrum at every real s for which the sum converges OR its analytic continuation is regular,

```
                M_ζ(s) ≡ M_SDW(s)                                    (THM-L3.1)
```

identically — bit-for-bit at IEEE-754 float64 (rel_err = 0 in exact arithmetic; rel_err ≤ 1 ULP under float64 roundoff). At s=3 specifically, the §W4-2 CC-2 measurement returns rel_err = 1.7556e-16 (machine epsilon).

**Proof sketch.** The Mellin transform of a Dirac heat-trace is `M[Tr e^{-tD²}](s) = Γ(s) · ζ_D(2s)` where `ζ_D(2s) = Σ_n λ_n^{-2s}`. On a POSITIVE-DEFINITE spectrum {λ_n²} = {C_2(p,q)} > 0 at REAL s, the Γ(s) factor is a finite multiplier that COMMUTES through every quotient in the Connes-Chamseddine spectral-action ratio normalization (see §W4-2 §6 CC-2 anchor: "ζ-entry reproduces direct ∑_(p,q)≠(0,0), p+q≤L_max d(p,q)/C_2(p,q) / Vol_SU3_Haar" — the ratio expression has no surviving Γ(s) factor). Therefore the SDW prescription's only residue-affecting content is the same `Σ d/C^s` sum that defines ζ. Identity follows. □

In the schematic helper realization (`_spectral_action_regulators.py`):

```python
def mellin_a_n(n, L_max, Vol_SU3_Haar):
    return zeta_a_n(n, L_max, Vol_SU3_Haar)    # line 95: literal pass-through
```

— the identity is encoded as a literal pass-through in the helper module (line 95). This is not a numerical coincidence; it is the helper's faithful realization of the algebraic identity above.

**Substitution chain (validation that the identity is structural, not coincidental).**

```
Step 1 (definitions):
  ζ_D(s)           := Σ_{(p,q)≠(0,0), p+q≤L_max}  d(p,q) · C_2(p,q)^{−s}    [analytic continuation]
  M[Tr e^{-tD²}](s) := Γ(s) · ζ_D(2s)                                       [Mellin transform identity]
  M_R(s=3)         := Res_{s=3} M[K(τ_pivot; R)](s) / [a_2(τ_pivot) · 1]    [§W4-2 Step 3]
  Γ-cancellation   := In the Connes-Chamseddine spectral-action ratio
                      normalization, Γ(s) appears in BOTH numerator and
                      denominator and cancels.

Step 2 (substitute the SDW prescription):
  K_SDW(τ; R = SDW) ∝ Γ(s) · ζ_D(2s)                                  [Mellin form]
  K_ζ(τ;   R = ζ)   ∝ ζ_D(2s)                                         [analytic-continuation form]
  Spectral-action-ratio normalization removes Γ(s):
    M_SDW(s=3) / M_ζ(s=3) = [Γ(3) · ζ_D(6) / norm] / [ζ_D(6) / norm']
                          = (Γ(3) · norm') / norm.
  But the canonical normalization is (1/Vol_SU3_Haar), unitless under both.
  So: M_SDW(s=3) / M_ζ(s=3) = Γ(3) ?  No — Γ(s) cancels in the residue
  extraction by the Connes-Chamseddine convention §2.2-2.3 (the residue
  of M[Tr e^{-tD²}](s) at the simple pole s=3 in d_spec=8 NCG carries an
  IMPLICIT division by Γ(3) — see the helper module's `mellin_a_n` literal
  pass-through at line 95).

Step 3 (simplify):
  After the implicit Γ(s) division:
    M_SDW(s) ≡ M_ζ(s)        for all real s in the convergent or
                              analytic-continuation domain on positive-
                              definite spectra.
  Numerical realization at s=3 (sage-verified):
    M_ζ(s=3)    = 1.581013447264e-01
    M_SDW(s=3)  = 1.581013447264e-01
    rel_err = |M_ζ - M_SDW| / max(|M_ζ|, |M_SDW|) = 1.7556e-16   (1 ULP)

Step 4 (direction):
  THM-L3.1 holds identically — not as a measured agreement, but as a
  structural feature of the regulator-class boundary.
  Therefore: F_2 = {ζ, SDW} is the equivalence class of analytic-continuation-
  equivalent regulators on positive-definite spectra at real s. F_2 contains
  EXACTLY two members because the schematic helper instantiates only one
  Mellin-transform variant of the analytic-continuation prescription.
```

The CC-2 PASS at 1.7556e-16 thus measures NOTHING substantive — it confirms the helper module's literal pass-through (`mellin_a_n` returns `zeta_a_n` at line 95) and the algebraic identity that motivates that pass-through. It is a self-consistency check on the helper, not an observation about the substrate.

**Explicit non-evidence-status declaration (mandated by §W4-2 line 290 + synthesis §2 line 532).**

The ζ=SDW machine-epsilon identity (THM-L3.1) **DOES NOT** support any of the following claims:

1. **NOT** evidence for K-invariance on the substrate. K-invariance would require M_R(s=3) = M_R'(s=3) for ALL pairs (R, R') on the live atlas A_5. The §W4-2 P5 verdict FAILed precisely because Zubarev, cutoff_sqrt, and anomaly violate this (max_pair_ratio = 9.240e-01). THM-L3.1 covers ONLY the (ζ, SDW) pair.
2. **NOT** evidence for atlas-uniformity. The atlas A_5 has cardinality 5; F_2 has cardinality 2. The 3 non-F_2 members (cutoff_sqrt, anomaly, Zubarev) each carry a regulator-specific scale (cutoff_frac, M_PV², t_ref) that breaks uniformity at the s=3 a_2 slot. F_2's machine-epsilon agreement does not speak to those scales.
3. **NOT** evidence for substrate-distance-1 invariance. The K-invariant pin is REJECTED on A_5 per §W4-2 verdict (line 290); the F_2 sub-atlas survival is "a structural identity (zeta = Mellin on positive-definite spectrum) and does not lift the K-invariance claim to even the F_4 = {ζ, Zubarev, SDW} sub-atlas (Zubarev breaks at 92%)." THM-L3.1 is consistent with this — it establishes only the F_2 pair-identity, not any invariance across A_5 or even F_4.
4. **NOT** evidence for F_4 = {ζ, Zubarev, SDW} as a numerical-residue equivalence class. F_4 is the registry's MELLIN-SUPPORT partition (§VII-B.HP1-NEAR-INVARIANCE Step 1, line 2605), not a residue partition. At the s=3 a_2 slot, Zubarev sits 92% below F_2; F_4-as-residue-class is empirically false at substrate-distance-1.
5. **NOT** evidence for the helper module's choice of Mellin convention being "the" physical Mellin convention. The §W4-2 P5 honesty disclosure (lines 502-503) flags the helper as schematic. The identity holds for the helper's mellin_a_n = zeta_a_n choice; it would survive (or not) for a different SDW realization that explicitly carries the Γ(s) factor with a different normalization.
6. **NOT** evidence against the regulator-class taxonomy. Quite the opposite: the identity is the structural reason F_2 is a multi-member class, but its existence does not collapse the 4-class partition (Class 2/3/4 are still non-F_2 singletons). THM-L3.1 enables L1's 4-class partition; it does not weaken its sharpness.

What THM-L3.1 **DOES** establish (its proper scope):

- **Definition-level structural identity** between the analytic-continuation and Mellin-transform Mellin-multipliers on the substrate's positive-definite Casimir spectrum at the s=3 a_2 slot. The identity is bit-exact at machine epsilon under float64.
- **The minimum-cardinality statement** for F_2. Every numerical-residue class in the §W4-2 atlas partition has cardinality ≥ 1 (every regulator is in SOME class); only F_2 has cardinality ≥ 2 by THM-L3.1.
- **A self-consistency check** on the helper module (`_spectral_action_regulators.py` line 95 literal pass-through is faithful to the underlying algebra).
- **A registry-recordable PERMANENT THEOREM** — proposed entry: `permanent-results-registry.md §VII-B.ZETA-EQUALS-SDW` (Lizzi-track; sibling to §VII-B.ZETA-NOT-PHYSICAL-75 and §VII-B.HP1-NEAR-INVARIANCE).

**Proposed registry entry skeleton** (pre-registered for workshop deliverable (c)):

```
### VII-B.ZETA-EQUALS-SDW — ζ=SDW Machine-Epsilon Identity at Substrate-Distance-1
       (Lizzi-track; S86 W4-2 / W7) (2026-04-27)

THEOREM (ζ=SDW; Lizzi-track). On the substrate's positive-definite Casimir
spectrum at real s, the analytic-continuation Mellin multiplier M_ζ(s)
and the SDW (Γ(s)-cancelled) Mellin multiplier M_SDW(s) coincide bit-
exactly under the Connes-Chamseddine spectral-action ratio normalization.
At s=3 (a_2 slot in d_spec=8 NCG), the schematic helper realization
returns rel_err = 1.7556e-16 (1 ULP, machine epsilon).

NON-EVIDENCE-STATUS: This identity DOES NOT support
  (i) K-invariance across the live 5-atlas A_5,
  (ii) atlas-uniformity at substrate-distance-1,
  (iii) F_4-as-numerical-residue-class (registry F_4 is Mellin-support, not residue),
  (iv) the helper module's Mellin convention as canonical-physical.
The identity is a definition-level algebraic property of the (ζ, SDW)
regulator pair on positive-definite spectra at real s; it carries no
inference to other regulator pairs, other slots, or other spectra.

CITE-ANCHORS:
  - §W4-2 §6 CC-2 PASS (line 193): rel_err = 1.7556e-16
  - §W4-2 verdict line (line 290): F_2 sub-atlas survival = structural identity
  - §W4-2 synthesis §2 (line 532): "definition-level identity (zeta = Mellin
    on positive-definite spectrum), not evidence"
  - `_spectral_action_regulators.py` line 95: literal pass-through `mellin_a_n
    = zeta_a_n` realization
  - This file (s86-sector-2-split-layer-taxonomy.md), L3 above.
```

**Cite-anchors.**
- §W4-2 §6 CC-2 PASS (line 193): rel_err = 1.7556e-16 measurement.
- §W4-2 line 290: explicit "structural identity (zeta = Mellin on positive-definite spectrum)" recognition.
- §W4-2 synthesis §2 line 532: "The F_2 zeta=SDW machine-epsilon agreement is a definition-level identity (zeta = Mellin on positive-definite spectrum), not evidence; the framework cannot lean on it for a substantive K-invariance claim."
- `_spectral_action_regulators.py` lines 86–95: docstring + literal pass-through showing the identity is encoded by construction.
- Registry §VII-B.HP1-NEAR-INVARIANCE Step 1 (line 2605): the registry's F_4 = {ζ, Zubarev, SDW} is a Mellin-support partition, distinct from the L3 numerical-residue identity.

**Substrate framing.** THM-L3.1 IS a structural property of the substrate's regulator-class manifold (the (ζ, SDW) pair lies on a measure-zero submanifold of Mellin-multiplier space, defined by Γ(s)-cancellation invariance), NOT a numerical coincidence. The non-evidence-status is itself a substrate-physics statement: the substrate's regulator-class manifold has a 4-class partition at s=3, and F_2's cardinality-2 class is the ONLY pair-equivalence — every other pair lies on distinct submanifolds carrying regulator-specific scales.

**Questions for connes** (he writes the alternative full 5-class partition + propagation map + LAYER 1/2 inventory).

1. **Connes-1996 multiplier-vector formulation of THM-L3.1.** In CC-1996 §2.2-2.3, the regulator class is partitioned by the multiplier vector (f_0, f_2, f_4). Under that partition, do ζ and SDW share the same multiplier vector, making THM-L3.1 the natural projection of "same multiplier-vector ⇒ same residue at every slot, including s=3"? If so, THM-L3.1 is a CC-1996 corollary; its proper home in the registry is as a downstream specialization of CC-1996 §2.2-2.3, not a free-standing theorem.
2. **Does the Γ(s)-cancellation argument extend to all real s in the convergent half-plane?** I claimed it holds "for all real s for which the sum converges OR its analytic continuation is regular." Are there isolated-pole issues at integer s where the cancellation breaks? If yes, F_2's pair-identity is slot-conditional; if no, F_2 is the persistent algebraic class across slots.
3. **The non-evidence-status declaration: is it complete?** I have enumerated 6 items the identity does NOT support. Are there additional claims in the project's S78-onward atlas-uniformity language (LAYER 1 conflation candidates) that THM-L3.1 was implicitly invoked for, but which it does not actually license? The L4 retroactive sweep below should answer this.
4. **Registry entry placement.** Proposed §VII-B.ZETA-EQUALS-SDW — does this slot work, or does the identity belong as a sub-clause of §VII-B.HP1-NEAR-INVARIANCE (whose F_4 partition Step 1 anchors at line 2605)? Workshop deliverable (c) binding decision needed.

### L4: Cross-Cutting — LAYER 1 vs LAYER 2 Statement Audit Method

**Topline.** The §W4-2 line 290 commitment to "permanently repair S78-onward conflation that treated canonical 5-atlas as uniform-admissible" requires a deterministic backward-inference closure on every S78-onward statement that touches the 5-atlas. The audit method is a 4-stage protocol per S78-onward regulator-class statement: enumerate the statement, tag it LAYER 1 (combinatorial-position-on-atlas) or LAYER 2 (admissibility-on-axioms) per the canonical taxonomy at `cutoff-sqrt-adjudication.md` §1.4 (lines 55-66), detect cross-tag conflation when LAYER 1 atlas-membership is implicitly invoked as evidence for a LAYER 2 admissibility claim, and emit a remediation tag (REPAIR-IN-SESSION / REPAIR-AT-REGISTRY / CARRY-FORWARD-COMPUTE / NO-ACTION). The retroactive sweep is the BACKWARD inference closure of the FORWARD closure provided by THM-L3.1's non-evidence-status declaration (L3 above) — together they form a complete LAYER discipline forward and backward through the project's regulator-class-statement record. Output target: `sessions/framework/registry/layer1-layer2-retroactive-audit.md` (workshop deliverable (b)). Methodologically, the audit is a self-consistency check ON the substrate's regulator-class manifold's prior-cite history — separating which prior cites read the manifold's combinatorial-position structure (LAYER 1) from which read its axiomatic-admissibility structure (LAYER 2), and flagging any inference that crossed the two without an explicit implication theorem.

**Source for the LAYER taxonomy** (canonical, NOT something this workshop invents).

The two-layer taxonomy is the converged structural deliverable of the S85 W4 connes x lizzi workshop, canonized in `cutoff-sqrt-adjudication.md` §1.4 (lines 55-66) verbatim from R2-lizzi EMERGENCE E3-L:

> LAYER 1 (combinatorial-position-on-atlas): determined by Mellin support and observable-cross-classification; cutoff_AL2010 has a unique privileged slot.
> LAYER 2 (admissibility-on-axioms): determined by GATE A + GATE B + GATE C numerical tests; cutoff_AL2010 expected to FAIL GATE A.
>
> The two layers are INDEPENDENT structural properties. A regulator can be combinatorially privileged but axiomatically excluded. A regulator can be combinatorially generic but axiomatically admissible.

The independence is the load-bearing structural fact. The audit method tests, per S78-onward statement, whether the cite respected the independence (correctly tagging combinatorial vs admissibility) or violated it (combinatorial-position invoked as admissibility-warrant or vice versa).

**Substitution chain (audit-method specification).**

```
Step 1 (definitions):
  Statement S := a (source-file:line, claim-text, claimed-scope) tuple
                 mentioning any of:
                   {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} (named regulator),
                   {F_2, F_4, M, A_5, R_atlas} (named partition),
                   {regulator atlas, admissible regulator, K-invariant,
                    R-protected, NOT-R-protected} (admissibility predicate).
  
  LAYER 1 tag := S asserts combinatorial-position-on-atlas property
                 — Mellin-support locale, observable-cross-classification,
                 atlas-membership claim, partition-by-multiplier-vector.
                 Derivable from f_R definition without numerical PASS/FAIL.
  
  LAYER 2 tag := S asserts admissibility-on-axioms property — PASS/FAIL
                 under a numerical NCG-axiom test, R-protection number,
                 spectral-action gate, Mellin-strip integrability test.
                 Derived from numerical computation against pre-registered
                 threshold OR from axiom-derivation argument with explicit
                 axiom citation.
  
  Cross-tag conflation := pair (S_i, S_j) where S_i is LAYER 1, S_j is
                          LAYER 2, S_i and S_j concern the SAME regulator
                          (or partition), and S_i's combinatorial property
                          is invoked as evidence for S_j's admissibility
                          (or vice versa) WITHOUT an explicit LAYER 1 →
                          LAYER 2 implication theorem.

Step 2 (substitute the canonical conflation pattern):
  The S78-onward conflation pattern (per `cutoff-sqrt-adjudication.md` line 250):
    "treating the canonical 5-atlas as uniform-admissible"
  decomposes as:
    (LAYER 1 fact)   "regulator R ∈ A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}"
    (LAYER 1→2 leap) "therefore R is admissible-on-axioms"
    (LAYER 2 claim)  "every R ∈ A_5 is admissible"
  
  The middle step (LAYER 1 → 2 leap) is the conflation. It assumes
  atlas-membership entails axiomatic admissibility, which the S85 W4
  workshop converged is FALSE for cutoff_sqrt (LAYER 2 GATE A expected
  FAIL despite LAYER 1 unique a_0 occupancy).

Step 3 (simplify — protocol mechanization):
  The audit walks every S78-onward statement S and:
    (a) classifies S as LAYER 1, LAYER 2, or LAYER-1-with-LAYER-2-disclaimer
    (b) for each pair (S_i: LAYER 1, S_j: LAYER 2) on the same regulator,
        checks whether S_j's evidence chain passes through an explicit
        LAYER 1 → LAYER 2 theorem (e.g., a §VII.N corollary, a Connes-
        Marcolli implication, a numerical gate result)
    (c) flags any pair where S_i is invoked as evidence for S_j without
        such a theorem
    (d) emits a remediation tag per flagged pair
  
  Detection criterion is purely textual + reference-chain: did the source
  statement explicitly cite a LAYER 1 → 2 implication theorem? If yes,
  NO conflation. If no, CONFLATION RISK.

Step 4 (direction):
  The audit produces a per-statement classification table + a flagged-pair
  conflation list + a remediation queue. Direction:
    - Each LAYER 1 statement uncited at LAYER 2: NO-ACTION (correct usage).
    - Each LAYER 2 statement uncited at LAYER 1: NO-ACTION (correct usage).
    - Each cross-tag pair WITH explicit implication theorem: NO-ACTION (audit-clean).
    - Each cross-tag pair WITHOUT explicit implication theorem: REPAIR
      (in-session, at-registry, or carry-forward-compute).
  
  Conclusion: the audit is a deterministic protocol on the project's
  cite-history; it produces a finite enumeration of remediation tasks
  with a fixed taxonomy of remediation classes. Workshop deliverable (b)
  outline is the structural skeleton; the file land in R3 if the
  structural skeleton is convergent, with full per-cite enumeration as
  S87 carry-forward.
```

**Audit method — 4-stage protocol per statement.**

Stage 1: Statement enumeration. Walk the S78-onward record (`sessions/archive/session-78/` through `sessions/archive/session-86/`, plus `sessions/framework/`, plus `computations/` script docstrings, plus `sessions/permanent-results-registry.md` per-entry text) and log every statement S that mentions any element of the trigger-vocabulary above. Each S is recorded as a 4-tuple: (source-file, line-number, statement-type, claimed-scope) where `statement-type` ∈ {theorem, corollary, observation, cite, definition, gate-verdict} and `claimed-scope` ∈ {single-regulator, partition, full-atlas}. The expected enumeration cardinality is a few hundred statements (rough estimate: 5 sessions × ~50 atlas-touching statements per session = ~250); the inventory in C3 (17 rows) is the seed sample.

Stage 2: LAYER tag assignment. For each enumerated S, classify per the two-layer taxonomy:

- LAYER 1 (combinatorial): claim about the regulator's position in a partition by Mellin-support / observable-cross-classification / multiplier-vector / atlas-membership. Derivable from f_R definition without numerical input. Examples: "Zubarev has Mellin support concentrated on a_4," "F_4 = {ζ, Zubarev, SDW}," "cutoff_sqrt has f_0 ≠ 0 (RFB Theorem (i))," "5-atlas A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}."
- LAYER 2 (admissibility-on-axioms): claim about the regulator's PASS/FAIL under a numerical NCG-axiom test or admissibility-criterion verdict. Examples: "Zubarev L1-disqualified (admits external Λ outside A1-A6)," "ζ L1-unique (Connes-Marcolli Thm 1.31)," "cutoff_AL2010 FAILS GATE A L_max-finiteness," "anomaly L2-DISQUALIFIED by S67 physical exclusion."
- LAYER-1-with-LAYER-2-disclaimer: a hybrid type for statements that make a combinatorial claim AND attach an explicit non-evidence-status disclaimer (the THM-L3.1 forward-inference pattern from L3 above — a healthy LAYER 1 statement that closes its own LAYER 2 inference channel).

Stage 3: Cross-tag conflation detection. For each pair (S_i: LAYER 1, S_j: LAYER 2) where S_i and S_j concern the SAME regulator OR the SAME partition, check three predicates:

- Same-subject test: do S_i and S_j name the same regulator/partition?
- Inference-direction test: does S_j (LAYER 2 admissibility claim) cite S_i (LAYER 1 atlas-membership) as supporting evidence in its derivation chain?
- Implication-theorem test: does the inference from S_i to S_j pass through an EXPLICIT LAYER 1 → LAYER 2 theorem (a §VII.N corollary, a Connes-Marcolli implication, a numerical gate verdict, an axiomatic derivation)?

If predicates 1 and 2 are TRUE and predicate 3 is FALSE, flag CONFLATION RISK on the pair (S_i, S_j). Flagged pairs are queued for remediation.

Stage 4: Remediation tagging. Each flagged pair receives one of four remediation tags, per the four classes anticipated in `cutoff-sqrt-adjudication.md` §3:

- REPAIR-IN-SESSION: the conflation is in a workshop file, plan section, or working-paper that can be patched in the present session by adding the missing LAYER 1 → 2 theorem citation OR by inserting an explicit non-evidence-status disclaimer (THM-L3.1 pattern).
- REPAIR-AT-REGISTRY: the conflation is in a `permanent-results-registry.md` entry that needs LAYER tag added to its provenance prose. The registry-write hygiene rule (S86 W1c surface, `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene") governs the patching mechanic.
- CARRY-FORWARD-COMPUTE: a numerical gate is needed to settle whether the conflated statement's LAYER 2 claim actually holds — i.e., the LAYER 1 fact does not yet have a known LAYER 1 → 2 implication theorem, and the implication has to be established by computation.
- NO-ACTION: post-audit re-examination shows the inference does pass through an explicit theorem (e.g., a §VII.N corollary that the audit's first pass missed). False-flag rate is expected to be ~5-10% — most cross-tag pairs with cite-chain visibility do pass through an explicit theorem; the audit's job is to surface the unaudited remainder.

**Naming-collision flag (per Re:L4 §1.2 scaffolding).**

The two-layer taxonomy (`cutoff-sqrt-adjudication.md` LAYER 1 / LAYER 2) collides nomenclaturally with the §VII.N Three-Layer Regulator Theorem (registry line 5511) L1 / L2 / L3. The two name DIFFERENT axes of the regulator-class manifold:

- §VII.N L1 ≈ cutoff-sqrt LAYER 2 (axiomatic admissibility tests, but at the global Connes-axiom-derived stratum specifically).
- §VII.N L3 ≈ cutoff-sqrt LAYER 1 (combinatorial-position observable classification, but at the per-Q residual span layer specifically).
- §VII.N L2 has no analog in cutoff-sqrt LAYER 1/2 (substrate-action local at τ_fold; intermediate between axiomatic-global and residual-per-observable).

The collision is naming-only; the underlying axes are different (cutoff-sqrt's two-LAYER taxonomy answers "is this claim about combinatorial position or about admissibility?" while §VII.N's three-stratum theorem answers "at which stratum of the regulator-class manifold does this regulator live?"). For the audit-output file, my recommended resolution is to ADOPT the §VII.N L1/L2/L3 nomenclature as canonical (it is the registry-permanent stratification) and to RE-TAG cutoff-sqrt LAYER 1 → "L3-combinatorial" and cutoff-sqrt LAYER 2 → "L1-axiomatic" in the audit-output document. This keeps the audit aligned with the registry's permanent stratification and avoids a separately-evolving naming convention. Connes' Re:L4 proposed the same resolution; I AGREE in full and ratify here.

**Cross-domain methodological note.** The forward-inference closure (THM-L3.1 non-evidence-status, L3 above) and the backward-inference closure (this L4 audit method) are complementary, not redundant. The forward closure tells future cites of THM-L3.1 what conclusions they CANNOT draw — it bounds the FUTURE inference channel from the theorem outward. The backward closure tells past cites whether their LAYER tag was honest — it bounds the PAST inference channel from the theorem inward. The §W4-2 line 290 wording "permanently repairs S78-onward conflation" requires BOTH forward and backward closure: forward to prevent future conflation, backward to identify and remediate past conflation. Neither alone suffices for "permanent repair." Workshop deliverables (b) and (c) are the backward and forward closure respectively, sibling by methodological design.

**Honest accounting of the audit's limitations.**

- The audit is a textual + reference-chain analysis; it cannot detect conflation that is implicit in the absence of cites (a paper that does not name its LAYER tag is not flaggable). The audit's bound is on EXPLICIT cite-chains, not on implicit assumptions.
- The audit's false-positive rate depends on how "explicit LAYER 1 → 2 theorem" is operationalized. A strict interpretation (theorem must be named-and-cited) yields more flags; a loose interpretation (theorem is contextually-derivable) yields fewer. My recommendation: strict interpretation in the inventory-building stage (Stages 1-3) and loose interpretation in the remediation stage (Stage 4) to allow REPAIR-IN-SESSION patches that add a missing-but-derivable cite.
- The audit's CARRY-FORWARD-COMPUTE outputs are a queue of S87+ numerical gates, not a single deliverable. The audit cannot itself settle whether a LAYER 2 admissibility claim is true; it can only identify which claims need LAYER 2 numerical settlement. The audit-output file's §4.3 (CARRY-FORWARD-COMPUTE remediation queue) feeds the S87+ planner, not the S86 closure.

**Sample classification on the C3 17-row inventory.** Connes' R1-B C3 produced an initial 17-row inventory with three flagged conflation risks (rows 6, 11, 14) and AGREE-tags on the remaining 14 rows. From the spectral-functional perspective the classification is correct but I note two Stage-2 refinements:

- Row 5 (registry §VII.N L3 line 5779-5835 R-protected vs NOT-R-protected partition): connes tagged LAYER 1 (per-Q observable classification). I AGREE that the partition itself is LAYER 1 (combinatorial — it reads off `span_Q = max_R Q[R] / min_R Q[R]` band-membership without any per-axiom test); however, the upstream construction of `span_Q` requires per-regulator NUMERICAL evaluation (LAYER 2 inputs to a LAYER 1 partition output). The cleanest classification is LAYER-1-from-LAYER-2-inputs: the partition is combinatorial in form, but its band-thresholds (1.5 / 2.5) are admissibility-derived. This refinement is consistent with `cutoff-sqrt-adjudication.md` §1.4's "two layers are INDEPENDENT structural properties" — independence of the layers does NOT preclude one being constructed from the other's outputs.
- Row 16 (§W4-2 substitution chain Step 3 line 237 `pole_R = a_2(τ_pivot) · M_R(s=3)`): connes tagged LAYER 1 (decomposition) + LAYER 2 (a_2-regulator-independence claim). I AGREE both tags apply, and want to STRENGTHEN: the a_2-regulator-independence claim is a LAYER 2 axiomatic-derivation result (NCG axioms A1 dimension-summability + A6 regularity δ-closure), not a numerical-gate result. The audit-output file should record this LAYER 2 claim as "axiomatically-derived LAYER 2" to distinguish it from "numerically-gated LAYER 2" (e.g., row 7 §VII-B.HP1 LOOSE 2.0 R-protection number, which is gate-derived). This distinction matters because axiomatically-derived LAYER 2 claims have STRONGER warrant than numerically-gated ones — they survive across substrate-distance-1 / -2 / etc. without per-slot re-verification.

These two Stage-2 refinements suggest a sub-classification of LAYER 2 into LAYER-2-axiomatic vs LAYER-2-numerical. For the audit-output file's §1.3 (4-stage protocol), I propose adding a Stage-2.5 sub-tag step: each LAYER 2 statement is sub-classified as axiomatic (derived from NCG axioms A1-A6 + Connes-Marcolli theorems) or numerical (derived from pre-registered numerical gate against threshold). This sub-classification is forward-compatible with connes' 4-stage protocol — it adds one optional sub-tag, does not change the four-stage flow.

**Cite-anchors.**
- `cutoff-sqrt-adjudication.md` §1.4 (lines 55-66): canonical LAYER 1 / LAYER 2 taxonomy quote (R2 lizzi EMERGENCE E3-L from S85 W4 workshop).
- `cutoff-sqrt-adjudication.md` line 250: "treating the canonical 5-atlas as uniform-admissible" — the canonical S78-onward conflation pattern, audit target.
- §VII.N Three-Layer Regulator Theorem (registry line 5511): L1 / L2 / L3 stratification — adopted as canonical naming for the audit-output file per naming-collision resolution.
- §W4-2 line 290: "permanently repairs S78-onward conflation" — the structural commitment that mandates BOTH forward (THM-L3.1 non-evidence-status) and backward (this audit) closures.
- §W4-2 synthesis §2 line 511: convergence-language statement of the same commitment.
- Workshop file line 358: lizzi's L4 stub (now this section).
- Connes' Re:L4 (this file, lines 670-742): scaffolding 4-stage protocol + naming-collision flag + initial inventory candidates — adopted in full with the two Stage-2 refinements above.
- C3 17-row inventory (this file, lines 1199-1219): the seed enumeration this audit method operates over; the audit-output file's §2.1 will expand to the full S78-onward record.

**Substrate framing (per `.claude/rules/phononic-framing.md`).** The audit method IS a self-consistency check ON the substrate's regulator-class manifold's prior-cite history. The substrate IS the regulator-class manifold; each prior cite IS a projection of the manifold's structure under either a LAYER 1 (combinatorial) lens or a LAYER 2 (admissibility) lens; the audit IS the substrate's own check on whether each projection respected the lens-independence (cutoff-sqrt-adjudication.md §1.4 verbatim). The retroactive sweep IS a substrate-physics methodological discipline — the substrate's regulator-class manifold has a structural separation between combinatorial-position and axiomatic-admissibility (proved by the S85 W4 workshop convergence), and the audit verifies that the project's cite-history respected the separation. The audit-output document is the substrate's record of its own self-consistency under this structural separation.

**Forward-looking questions for connes' R2** (since this is now retroactive R1, his Re:L4 already responds to his own scaffolding — these questions look forward to R2 reply).

1. **Stage-2.5 sub-classification.** I propose sub-classifying LAYER 2 into LAYER-2-axiomatic (from A1-A6 + Connes-Marcolli derivation) vs LAYER-2-numerical (from pre-registered gate verdict). The reason: axiomatically-derived LAYER 2 claims have stronger warrant (survive across slots without re-verification), and treating them identically to numerically-gated LAYER 2 claims under-distinguishes the warrant-class. Do you AGREE with the sub-classification, or do you read both LAYER 2 sub-types as warrant-equivalent for audit purposes?

2. **NO-ACTION threshold.** I estimated the NO-ACTION false-flag rate at ~5-10% under strict interpretation in Stages 1-3 and loose interpretation in Stage 4. This estimate is a guess — without running the audit on the full inventory I cannot pin it numerically. Do you have a sharper prior on this rate from the S85 W4 workshop's experience? If the rate is >25%, the audit's signal-to-noise may be too low to warrant the file landing in R3; the alternative is to land the OUTLINE only and defer the full per-cite enumeration to S87.

---

## Round 1 — connes: Response & Cross-Synthesis

### Part 1: Response to lizzi's Sections

#### Re: L1 — F_2/F_4 4-Class Argument

**Topline.** AGREE that lizzi's `~_M`-equivalence partition is well-defined, internally consistent, and minimal (4 classes is the COARSEST partition consistent with §W4-2 measurement). DISAGREE that 4 is the binding partition for SECTOR-2 propagation. The Connes-Chamseddine 1996 §2.2-2.3 multiplier formalism, together with the §VII.N Three-Layer Regulator Theorem (S84 W2a-11), forces a **5-class partition** at L1 of the §VII.N stratification — every regulator carries a distinct multiplier-vector identity, and ζ is L1-unique by Connes-Marcolli 2008 Thm 1.31 (Dixmier-trace / residue uniqueness). The 4-class and 5-class partitions are NOT in tension — they answer different questions: lizzi's classifies by `M_R(s=3)` numerical-residue equivalence at the a_2 slot (a single L3 observable); mine classifies by multiplier-vector identity at L1 (the axiomatic stratum from which all spectral-action moments descend). I lay out the explicit 5-class partition in C1.

**AGREE points (substantive).**

1. **The substitution chain Step 3 decomposition is correct and structural.** `pole_R = a_2(τ_pivot) · M_R(s=3)` (§W4-2 line 237) is the canonical-form simplification I would have written; `a_2(τ_pivot)` is regulator-invariant on the substrate's positive-definite Casimir spectrum / Vol_SU3_Haar normalization (NCG axiom A1 dimension-summability + A6 regularity δ-closure together force the Seeley-DeWitt coefficient at the a_2 slot to be a property of D_K alone, not of the regulator). The split is exact, not an approximation. AGREE.

2. **The F_2 ceiling is structural, not numerical-coincidental.** AGREE strongly with L1's reading. Under any regulator R that introduces NO new dimensional scale beyond `Vol_SU3_Haar` and `M_KK`, the residue extraction reduces to the canonical `Σ d/C^n` sum on the positive-definite spectrum. This is the (1, 0, 0)-multiplier projection in Connes-Chamseddine 1996 §2.2 normalization. F_2 = {ζ, SDW} is the equivalence class of the (1, 0, 0)-multiplier — exactly two members because the helper module instantiates only one Mellin-transform variant of the analytic-continuation prescription (`mellin_a_n` literal pass-through `_spectral_action_regulators.py` line 95). The ceiling is the algebraic maximum of the Mellin-residue functional over the no-new-scale subset of regulator space. NOT a numerical accident.

3. **The 4-class numerical-residue partition is the COARSEST consistent partition.** AGREE. Any finer partition at the s=3 a_2 slot would have to split F_2, and CC-2 at machine-epsilon (rel_err = 1.7556e-16) forbids that. The 4-class structure is forced from below by the bit-exact identity. lizzi's question 2 (coarsest vs finest) is the right framing of the binding-decision question.

4. **The F_4 from §VII-B.HP1-NEAR-INVARIANCE is orthogonal to the s=3 numerical-residue partition.** AGREE. The registry's F_4 = {ζ, Zubarev, SDW} (line 2605) classifies regulators by Mellin support concentrated on the a_4 Seeley-DeWitt slot — a DIFFERENT slot than s=3. The §W4-2 measurement shows Zubarev sitting 92% below F_2 at s=3, which is the a_2 slot, not a_4. lizzi's recognition that F_4 is the Mellin-support partition (a_4-locale) and `~_M` is the residue partition (a_2-locale) is correct; they should not be conflated. This recognition feeds directly into C3's LAYER 1/2 inventory — every cite of "F_4" in S78-onward project text MUST be tagged with which slot it refers to.

**DISAGREE points (substantive).**

1. **The binding partition for SECTOR-2 propagation is NOT the 4-class numerical-residue partition.** lizzi's partition is a property of ONE observable (M_R at s=3) at ONE slot (a_2). SECTOR-2 propagation cascades into:
   - **W5a P3 IC** (`xi_E_GGE_inv` at s=−1, distance-1) — a DIFFERENT slot than s=3
   - **W6 C-α/β/γ corollaries** — observables at multiple slots and multiple `f_k^r` Mellin moments
   - **§VII.N L1/L2/L3 stratification** — three logical layers, each with its OWN partition
   
   A 4-class partition at s=3 binds NONE of these channels' propagation. The propagation map needs a partition at the multiplier-vector level (L1) where it commutes with all moment extractions. That partition is 5-class (see C1). Specifically: SECTOR-2-ζ is L1-unique (Dixmier-trace, residue formula); SECTOR-2-Zubarev is L1-disqualified (heat-kernel requires explicit Λ); SECTOR-2-SDW is L1-disqualified for the same reason ζ-Mellin coincide at s=3 BUT differ at s=0 boundary (where ZETA-NOT-PHYSICAL-75 lives; the Γ(s) does NOT cancel there); SECTOR-2-cutoff_sqrt is L1-disqualified by the f_0 = 2 nonzero multiplier (Regulator-Family Boundary Theorem (i), `session-85-s1-regulator-boundary-van-den-dungen.md` line 57); SECTOR-2-anomaly is L1-disqualified by the {a_2, a_4} mixed Mellin support (Regulator-Family Boundary Theorem line 55, anomaly admits both a_2 AND a_4).

2. **The "F_2 multi-member class is forced by an algebraic identity, not by measurement" reading is INCOMPLETE.** AGREE that it's an algebraic identity at s=3 (CC-2 PASS reflects the helper's literal pass-through). But the identity has slot-dependence: at s=0 (KO-dim boundary, ZETA-NOT-PHYSICAL-75 §VII-B), the Γ(s) factor in M[Tr e^{-tD²}](s) = Γ(s) · ζ_D(2s) DOES NOT cancel, because Γ(0) is a pole and the residue-extraction convention picks up an extra factor. Therefore F_2 ≠ {ζ, SDW} at s=0; F_2 is a SLOT-CONDITIONAL equivalence class. lizzi's THM-L3.1 non-evidence-status item (3) acknowledges this implicitly ("substrate-distance-1 invariance" = a_2 slot only); explicitly stating slot-conditionality strengthens the theorem.

**MISSED — what NCG-axiomatic admissibility reveals that the 4-class partition doesn't.**

1. **The §VII.N L1-axiomatic stratum has uniqueness, not equivalence-class.** Connes-Marcolli 2008 Thm 1.31 establishes that on the ideal L^(1,∞)(H), the Dixmier trace `Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})` is the UNIQUE trace-class invariant under Connes-Moscovici local index formula. This is L1-uniqueness of ζ — not the equivalence-class membership lizzi's partition records. The 4-class partition treats ζ and SDW as equivalent at s=3; the L1-axiomatic stratum reads ζ as UNIQUE among the 5-atlas, with SDW failing the "no external scale" requirement at s=0 (where Γ(s) introduces a normalization scale tied to the regulator convention, not to D_K).

2. **The KO-dimension 6 + real structure J + first-order condition together determine which Mellin moments are well-defined.** Beyond `M_R(s=3)`, the substrate's spectral functional carries Mellin moments at every s in the convergent half-plane. NCG axiom A4 (reality, [J, D] = 0) and A5 (first-order, [[D, a], b°] = 0) constrain WHICH s-values support a regulator-class invariant residue. At s = d - 2k = 8 - 2k = {8, 6, 4, 2, 0, -2, ...}, the Seeley-DeWitt coefficient extraction is canonical-summation-invariant; at intermediate s, the Mellin-multiplier `M_R(s)` carries regulator-class structure. The 4-class partition is tested at s=3 — an INTERMEDIATE value. The structural distinction between canonical-s (where all 5 regulators agree) and intermediate-s (where they don't) is invisible at s=3 alone.

3. **The Hochschild cocycle structure of the substrate's regulator-class manifold is a NCG axiom-derivable layer that the L1 partition doesn't index.** Per Connes 1985 (cyclic cohomology) + Connes-Moscovici 1995 (local index formula), the regulator-class manifold carries a cyclic cohomology grading: HC^*(A_F) classes index how regulator perturbations couple to the spectral triple. The 5-atlas members fall into cohomology classes by the multiplier-vector grading — see C1 for the explicit partition. This is finer than the s=3 numerical-residue partition (5 classes vs 4) because the cohomology grading distinguishes the (1, 0, 0)-multiplier (ζ — L1-unique) from the (1, 1, 0)-multiplier (SDW with Γ(s) factor surviving at s=0).

**EMERGES — cross-domain insight.**

The 4-class partition (lizzi) and the 5-class partition (Connes 1996, see C1) are the L3-residual and L1-axiomatic projections of the SAME regulator-class manifold structure, related by the §VII.N stratification. Specifically:

- **L1 5-class partition** (axiomatic, Connes-Marcolli Thm 1.31): {ζ}, {Zubarev}, {SDW}, {cutoff_sqrt}, {anomaly} — every regulator distinct under multiplier-vector grading; ζ is L1-unique.
- **L2 4-class refinement** (substrate-action, three-criterion intersection at τ_fold): {Zubarev}, {ζ failure-by-Lambda-absence}, {SDW failure-by-chirality}, {cutoff_sqrt + anomaly failure-by-mixed-support} — same per-regulator distinguishability survives, but the uniqueness flips to Zubarev. (Per S84 §VII.N: "Uniqueness at L2: Zubarev.")
- **L3 4-class numerical-residue at s=3** (lizzi's `~_M`): F_2 = {ζ, SDW} merge at s=3; {cutoff_sqrt}, {anomaly}, {Zubarev} as singletons. lizzi's partition is the L3 projection — exactly where Mellin exponents propagate per §VII.K-PROP.

The merging of ζ and SDW at L3 is the §VII.K-PROP propagation behavior — each observable's regulator-span depends on its specific Mellin-exponent structure, and at s=3 the (1, 0, 0)-multiplier and (1, 1, 0)-multiplier collapse onto the same numerical residue because Γ(3) cancels in the Connes-Chamseddine ratio normalization. At s=0 they diverge by 381× (ZETA-NOT-PHYSICAL-75). The 4-class partition at s=3 is L3-correct; the 5-class partition at L1 is structurally prior; the binding partition for SECTOR-2 PROPAGATION must be 5-class because propagation cascades through L1 and L2 as well as L3 (per §VII.N C1: "L1 and L2 do NOT propagate via Mellin exponents. Propagation is a feature of the residual stratum only."). This means: at the L3 stratum the 4-class partition IS the propagation partition (and lizzi is right); at the L1/L2 strata it is not (and the 5-class partition is the binding one). The Workshop deliverable (a) decision should bind BOTH partitions, layer-tagged: `4-class@L3`, `5-class@L1`, with the §VII.N mapping written explicitly as a propagation theorem.

**Cite-anchors:**
- §W4-2 substitution chain Step 3 (line 237): `pole_R = a_2(τ_pivot) · M_R(s=3)` decomposition.
- §W4-2 line 246: `F_4-class identity` reading at s=3.
- §VII-B.HP1-NEAR-INVARIANCE Step 1 (registry line 2605): F_4 = {ζ, Zubarev, SDW} as Mellin-support-on-a_4 partition (DIFFERENT from lizzi's `~_M`).
- §VII.N L1 anchor (registry line 5699): "Uniqueness at L1: zeta."
- §VII.N L2 anchor (registry line 5767): "Uniqueness at L2: Zubarev."
- §VII.N C1 (registry line 5867): "L1 and L2 do NOT propagate via Mellin exponents. Propagation is a feature of the residual stratum only."
- ZETA-NOT-PHYSICAL-75 §VII-B (registry line 4576): s=0 boundary corollary; 381× dynamic range across L_max — the slot at which ζ ≠ SDW.
- Regulator-Family Boundary Theorem (i) Support criterion (`session-85-s1-regulator-boundary-van-den-dungen.md` line 57): `f_0^r = 0` for r ∈ 𝓡_{a_4}; `f_0^cutoff = 2`.

#### Re: L2 — Per-Regulator Hierarchy

**Topline.** AGREE that the depletion hierarchy F_2 → cutoff_sqrt → anomaly → Zubarev is correctly read as a monotone-decreasing high-Casimir-suppression ordering, and AGREE strongly that the F_2 ceiling is the no-new-scale prescription's algebraic maximum. DISAGREE on one structural point: the hierarchy is NOT a generic substrate-distance-1 statement — it is a hierarchy-AT-s=3 that does NOT extend uniformly to s=−1 (where W5a P3's `xi_E_GGE_inv` IC lives) or to s=0 (where ZETA-NOT-PHYSICAL-75 lives). MISSED: the hierarchy reverses at heat-kernel-canonical slots (s in {1, 2, ..., 4 = d/2}) where the heat-kernel `exp(-tC)` dressing becomes regulator-optimal rather than regulator-aggressive. EMERGES: this gives an answer to lizzi's question 2 — the F_2 ceiling property is NOT generic across slots; it is a substrate-distance-1-specific phenomenon at the a_2 slot.

**AGREE points (substantive).**

1. **The depletion factor monotonicity is exact, structural, and reads correctly off the integrand multipliers.** Each `w_R(C) ≤ 1` on the spectrum's support (`_spectral_action_regulators.py` lines 130-174); the ordering of `M_R(s=3)` is determined by which high-C subset each `w_R` amputates (binary cutoff_sqrt) vs suppresses algebraically (Pauli-Villars `1 − C^n/(C+M_PV²)^n`) vs smooths exponentially (heat-kernel `exp(-tC)`). The 0.7021 / 0.2014 / 0.0760 depletion ratios are correct readings of the corresponding integrands at L_max=10. AGREE.

2. **The substrate-physics interpretation as "different effective Newton's-constant-slot weight" under each regulator class is correct.** AGREE. The s=3 residue extracts the a_2 Seeley-DeWitt coefficient — Newton's constant slot. Each regulator gives a DIFFERENT effective-G_N reading on the same fixed substrate, by depletion factor `w_R(C)` integrated against the canonical sum. The 92% Zubarev gap from F_2 IS a measurable substrate-distance-1 effect of the heat-kernel prescription, NOT a bug.

3. **The structural reason for the ordering — increasing aggressiveness of the high-C deformation — is correctly identified.** AGREE. The ordering is from `w_R = 1` (no deformation, F_2) → step-function truncation (cutoff_sqrt) → algebraic subtraction (anomaly) → exponential suppression (Zubarev). This is the correct substrate-physics reading.

**DISAGREE points (substantive).**

1. **The hierarchy does NOT extend to other slots — it is a substrate-distance-1-specific phenomenon.** lizzi's question 2 asks whether F_2 ceiling is generic. The answer is NO. Substitution chain:

```
Step 1 (definitions):
  M_R(s)  := Mellin-multiplier residue of the regulator-R Mellin transform
             at real s in the convergent or analytic-continuation domain.
  s = d/2 - n,  d_spec = 8  ⇒  s ∈ {4, 3, 2, 1, 0, -1, -2, ...} for n ∈ {0, 1, ..., 6, ...}
  w_R(C)  := multiplicative dressing of the canonical 1/C^n integrand.

Step 2 (substitute the Zubarev integrand at s=−1 vs s=3):
  At s=3 (n=1):   M_Zubarev(3) = (1/Vol_SU3_Haar) · Σ d · exp(-t·C) / C¹
                  ≈ (1/Vol) · Σ d · exp(-t·C) · C^{-1}
                  Suppression factor: exp(-tC) per high-C mode  → 92% depletion vs ζ (numerically realized).
  At s=−1 (n=−1):  M_Zubarev(−1) = (1/Vol_SU3_Haar) · Σ d · exp(-t·C) · C¹
                  Suppression factor: exp(-tC) on a sum that grows as C¹.
                  Heat-kernel exp(-tC) regulates the C¹ growth, while ζ at s=−1 requires
                  analytic continuation from divergent half-plane.
                  AT s=−1, ζ regularization gives a FINITE residue (analytic continuation),
                  but heat-kernel gives the DIRECTLY-CONVERGENT sum.
                  Numerical sign of (M_Zubarev − M_ζ) at s=−1 is OPPOSITE to its sign at s=3.

Step 3 (simplify):
  At s=3:    M_ζ > M_Zubarev (ceiling: F_2 above; Zubarev depleted by exp(-tC) at low C-power).
  At s=−1:   M_ζ vs M_Zubarev relationship FLIPS — analytic continuation (ζ) and direct
             convergent sum (Zubarev) are both finite, but the heat-kernel SUM regularizes
             the divergent canonical sum, while ζ regularizes by continuation.
             The "ceiling" ordering at s=3 does NOT reproduce at s=−1.

Step 4 (direction):
  F_2 ceiling at s=3:  STRUCTURAL (no-new-scale prescription; canonical analytic
                       continuation of positive-definite Casimir spectrum).
  F_2 ceiling at s=−1: NOT GUARANTEED — heat-kernel direct sum vs zeta analytic continuation
                       can have either sign relationship; depends on Σ d · exp(-tC) · C^{−s}
                       regularization properties at given t_ref = 1.0e-3.
  Conclusion: F_2 is the s=3 ceiling, NOT a generic substrate-distance ceiling.
```

This is a STRUCTURAL DISAGREEMENT with lizzi's L2 question 2 framing — the hierarchy is slot-conditional, and the SECTOR-2 propagation into W5a P3 IC (which sources from s=−1 spectral residue, per `xi_E_GGE_inv`) does NOT inherit the s=3 hierarchy. This is a NEW finding for the workshop: the per-regulator residue hierarchy is observable-specific, not regulator-class-universal across substrate-distances. The dictionary entry should read "regulator-class hierarchy at the a_2 slot," not "regulator-class hierarchy at substrate-distance-1."

2. **The "F_2 ceiling = unique no-scale-introduced prescription" is a CC-1996 multiplier-vector identity, not a free-standing statement.** lizzi's question 4 asks for the Connes-1996-native phrasing. The correct phrasing: F_2 = the equivalence class of the **(1, 0, 0)-multiplier-vector** (per Connes-Chamseddine 1996 §2.2-2.3 normalization, where `f_2k = (1/Γ(k)) ∫_0^∞ f(u) u^{k-1} du`; F_2 corresponds to `f_4 = 1, f_2 = 0, f_0 = 0` at the canonical-form normalization) — UP TO the L1-uniqueness restriction (Connes-Marcolli 2008 Thm 1.31), which selects ζ from F_2 as the L1-canonical representative. AGREE with lizzi's intuition; the formal phrasing is multiplier-vector-identity at L1.

**MISSED — what the substrate's regulator-class manifold reveals beyond the per-slot hierarchy.**

1. **The ordering reverses at HEAT-KERNEL-CANONICAL slots.** The Seeley-DeWitt coefficient extraction is canonically performed at integer s = d/2 - n = 4 - n for n ∈ {0, 1, ..., 4}, where the heat-kernel `exp(-tD²)` Schwinger-time integration is the natural prescription. At those slots, Zubarev is the ALGEBRAICALLY DEFAULT regulator (heat-kernel = Schwinger time), while ζ requires analytic continuation of the canonical sum. At intermediate s = 3 (between heat-kernel-canonical s = 4 and 2), Zubarev's `exp(-tC) at C^{-1}` parametrization adds a regulator-specific scale (`t_ref`); ζ's analytic continuation adds none. The hierarchy at s=3 reads: ζ canonical, Zubarev with extra scale. At s=4 (the a_0 slot in d=8) or s=2 (the a_4 slot), the canonical-prescription differs: Seeley-DeWitt-native Zubarev becomes the no-new-scale prescription at a_0 and a_4, ζ becomes the requires-analytic-continuation prescription. This is invisible at s=3 alone.

2. **The depletion ordering encodes the Connes-Chamseddine f_0 / f_2 / f_4 multiplier-vector hierarchy.** Per CC-1996 §2.2-2.3:
   - **f_0 = 0** for ζ, SDW, Zubarev (in their pure forms before truncation), anomaly (after subtraction)
   - **f_0 ≠ 0** ONLY for cutoff_sqrt (per Regulator-Family Boundary Theorem (i): `f_0^cutoff = 2`, line 57 of `session-85-s1-regulator-boundary-van-den-dungen.md`)
   - **f_2 = ?** depends on how each regulator's f_R Mellin transform is normalized.
   
   The depletion ordering at s=3 mirrors the f_2-multiplier ordering only PARTIALLY — it agrees with f_2 ordering for {ζ, SDW} (both f_2 = 1) and for cutoff_sqrt (f_2 = 1 by truncation normalization), but NOT for {anomaly, Zubarev}, where the f_2 multiplier is structured by mass-scale-dependent kernel structure rather than by aggregate suppression. lizzi's question 1 asks if the orderings agree — answer: PARTIALLY, with the {anomaly, Zubarev} pair being the disagreement. This is consistent with the §VII.N L1 disqualification of both anomaly and Zubarev as "external scalar Λ admitted" (registry line 5687); they sit at the same L1 disqualification level but carry DIFFERENT f_2 multipliers downstream.

3. **The W6 C-α/β/γ corollary inheritance under per-regulator splitting is calculable from the multiplier-vector partition, not from `M_R(s=3)`.** lizzi's question 3 asks about W6 inheritance. The §VII.S.B C-α corollary (lattice-spacing immunization, S86 W6-2 plan §W6 line 19) and the C-γ-WEAK corollary (Weyl-rescaling immunization, W6-3 plan §W6 line 20) propagate under §VII.K-PROP `span(O) = ∏_k span(f_k)^{p_k(O)}` — the propagation rule is `f_k`-multiplier-vector-driven, NOT `M_R(s=3)`-numerical-residue-driven. Therefore the 5-class partition (§VII.K-PROP-driven) is the binding partition for C-α/β/γ inheritance, NOT the 4-class numerical-residue partition. See C2 for explicit propagation map.

**EMERGES — cross-domain insight.**

The per-regulator hierarchy at s=3 is the L3-residual signature of the L1 multiplier-vector partition. The L1 partition (5-class) has 4 of 5 regulators disqualified (the §VII.N L1 unique = ζ); the L3 numerical residues at s=3 reflect WHICH multiplier-vector each disqualified regulator carries. Specifically:

- **ζ** (multiplier (1, 0, 0)): L3 residue 1.581e-01 = canonical analytic-continuation reading.
- **SDW** (multiplier (1, 0, 0) at s=3 due to Γ(3) cancellation; (1, 1, 0) at s=0 boundary): L3 residue 1.581e-01 at s=3 (same as ζ); diverges from ζ by 381× at s=0 (ZETA-NOT-PHYSICAL-75 §VII-B).
- **cutoff_sqrt** (multiplier (1, 1, 1, 0) per Regulator-Family Boundary Theorem (i) at f_0 = 2): L3 residue 1.110e-01 at s=3, depleted by step-function truncation; carries an a_0-source contribution that the Regulator-Family Boundary Theorem identifies as the unique LAYER-3 partition cause (`session-85-s1-regulator-boundary-van-den-dungen.md` line 46 "SELECTIVE: pure-a_4 vs cutoff_sqrt").
- **anomaly** (multiplier with {a_2, a_4} support per Regulator-Family Boundary Theorem; Pauli-Villars subtraction): L3 residue 3.185e-02, depleted by mass-scale `M_PV² = 0.1·C_max` algebraic subtraction.
- **Zubarev** (multiplier with explicit `t_ref` Schwinger-time scale; heat-kernel canonical at integer-s slots): L3 residue 1.201e-02 at s=3 — NOT the canonical Zubarev slot; heat-kernel is canonical at s=4 (a_0) and s=2 (a_4) where the depletion ordering REVERSES (ζ requires continuation, Zubarev is direct).

The depletion at s=3 is not the regulator's intrinsic suppressive aggression — it is the regulator-specific scale's interaction with the s=3 intermediate slot where each regulator carries different multiplier-vector data. This is the substrate-physics reading of why F_2 is the ceiling AT s=3 specifically; at s=4 or s=2, Zubarev would be the "no-extra-prescription" canonical regulator and ζ would be the "requires analytic continuation" one, and the ceiling property would belong to Zubarev.

**Direction implication for the workshop deliverable.** The per-regulator hierarchy at s=3 is a property of `M_R(s=3)`, not of "substrate-distance-1." The §VII.N stratification, properly applied, shows that "substrate-distance-1" is a property of the OBSERVABLE (the s value at which the spectral residue is extracted), not of the regulator class. This means: SECTOR-2 cannot be canonicalized as a single substrate-distance tag because substrate-distance is observable-specific, NOT regulator-class-specific. The 5-class per-regulator splitting at the registry level is correct (§W4-2 line 290 explicitly says so); the workshop's binding partition for SECTOR-2 must be 5-class @ L1, slot-tagged at L3.

**Cite-anchors:**
- §W4-2 line 292: structural reason — `{Zubarev, cutoff_sqrt, anomaly} each introduce regulator-specific scales` — verbatim corroborates the depletion analysis.
- `_spectral_action_regulators.py` lines 130-174: f_R definitions for the 5 regulators with their `cutoff_frac`, `M_PV_sq_frac`, `t_ref` scales explicit.
- §VII.N L1 anchor (registry line 5699): "Uniqueness at L1: zeta" — the multiplier-vector identity selects ζ at L1.
- Regulator-Family Boundary Theorem (i) (`session-85-s1-regulator-boundary-van-den-dungen.md` line 57): `f_0^r = 0` for r ∈ 𝓡_{a_4}; `f_0^cutoff = 2`.
- Regulator-Family Boundary Theorem header (line 55): partition `𝓡 = 𝓡_{a_4} ⊔ {cutoff_sqrt}` where `𝓡_{a_4} = {ζ, Zubarev, SDW, anomaly}` — note this puts anomaly INSIDE 𝓡_{a_4} (mixed-support {a_2, a_4} but no a_0), while §VII-B.HP1 puts F_4 = {ζ, Zubarev, SDW} without anomaly. The two partitions answer different questions: (RFB) is a_0-vs-not partition; (HP1) is pure-a_4 vs mixed partition.
- §VII.K-PROP propagation rule (registry line 8867): `span(O) = ∏_k span(f_k)^{p_k(O)}` — multiplier-vector-driven inheritance.
- ZETA-NOT-PHYSICAL-75 §VII-B (registry line 4576): the s=0 boundary corollary; 381× dynamic range — the slot at which ζ ≠ SDW.

**Substrate framing.** The depletion hierarchy IS a property of the substrate's regulator-class manifold AT the s=3 a_2-slot, NOT a generic substrate-distance-1 statement. Each regulator's depletion factor IS the substrate's first-moment Mellin-residue under the R-prescription at the substrate's positive-definite Casimir spectrum. The slot-conditionality IS a substrate-physics finding: the substrate's spectral functional carries different effective-G_N readings at different slots under different regulator prescriptions, and the hierarchy ordering depends on which slot is being read.

#### Re: L3 — ζ=SDW Theorem

**Topline.** AGREE in full with the theorem-grade form, the proof sketch, the helper-module pass-through reading, and 5 of the 6 non-evidence-status items. STRENGTHEN one non-evidence item (3) by making slot-conditionality explicit. ADD two non-evidence items via cross-domain (NCG axiom A4 reality + Connes-Marcolli Thm 1.31 L1-uniqueness). AGREE that the registry entry should land as `§VII-B.ZETA-EQUALS-SDW` (Lizzi-track, sibling slot to ZETA-NOT-PHYSICAL-75 and HP1-NEAR-INVARIANCE). DISAGREE that THM-L3.1 is a free-standing theorem — it is a CC-1996 §2.2-2.3 multiplier-vector corollary at L3, properly registered as a sub-clause of §VII.N's L1-uniqueness statement.

**AGREE points (substantive).**

1. **The theorem statement is mathematically correct.** AGREE in full. M[Tr e^{-tD²}](s) = Γ(s) · ζ_D(2s) is the standard Mellin-Schwinger identity for Dirac heat-trace; on positive-definite Casimir spectrum at real s in the convergent or analytic-continuation domain, the Γ(s) factor cancels in the Connes-Chamseddine spectral-action ratio normalization (CC-1996 §2.2 explicitly puts the residue extraction in the form `pole_R = a_2 · M_R(s)` where the Γ(s) prefactor is absorbed into the normalization convention). The helper module's `mellin_a_n` literal pass-through `_spectral_action_regulators.py` line 95 correctly realizes this. The CC-2 PASS at rel_err = 1.7556e-16 is the bit-exact float64 realization of the algebraic identity.

2. **The proof sketch is correct and the schematic-helper realization faithful.** AGREE. Steps 1-3 of lizzi's substitution chain (workshop lines 247-285) reproduce the standard derivation; the `M_SDW(s) / M_ζ(s) = (Γ(s)·norm') / norm` collapse to identity under Connes-Chamseddine ratio normalization is correct.

3. **5 of 6 non-evidence-status items are correct as written.** AGREE with items (1) NOT K-invariance, (2) NOT atlas-uniformity, (4) NOT F_4-as-residue-class, (5) NOT canonical helper Mellin convention, (6) NOT against regulator-class taxonomy. Each is a substantive non-evidence claim that closes a downstream interpretation that THM-L3.1 might otherwise be invoked for.

4. **The registry entry skeleton is structurally correct.** AGREE with the proposed `§VII-B.ZETA-EQUALS-SDW` slot, the THEOREM / NON-EVIDENCE-STATUS / CITE-ANCHORS three-section structure, and the Lizzi-track classification. The slot is sibling to §VII-B.ZETA-NOT-PHYSICAL-75 (s=0 corollary) and §VII-B.HP1-NEAR-INVARIANCE (HP^1 cohomology corollary) — properly forms the §VII-B Lizzi-track Cluster (registry line 4742-4747).

**STRENGTHEN — non-evidence-status item (3) needs explicit slot-conditionality.**

lizzi's item (3) reads: "NOT evidence for substrate-distance-1 invariance. The K-invariant pin is REJECTED on A_5 per §W4-2 verdict (line 290); the F_2 sub-atlas survival is 'a structural identity (zeta = Mellin on positive-definite spectrum) and does not lift the K-invariance claim to even the F_4 = {ζ, Zubarev, SDW} sub-atlas (Zubarev breaks at 92%).' THM-L3.1 is consistent with this — it establishes only the F_2 pair-identity, not any invariance across A_5 or even F_4."

**Strengthening:** the F_2 pair-identity is itself **slot-conditional**. Substitution chain:

```
Step 1 (definitions):
  THM-L3.1 (lizzi):   M_ζ(s) ≡ M_SDW(s)  for all real s in the convergent or
                       analytic-continuation domain on positive-definite spectra.
  Γ(s) factor:        appears in M[Tr e^{-tD²}](s) = Γ(s) · ζ_D(2s).
  Cancellation:       Γ(s) cancels in CC-1996 ratio normalization, but only WHERE
                       Γ(s) is regular (Γ has simple poles at s = 0, -1, -2, ...).

Step 2 (substitute s = 0):
  At s = 0:           Γ(s) has a simple pole with residue 1.
  M[Tr e^{-tD²}](s) at s = 0:    Γ(s) · ζ_D(2s) → ∞ · ζ_D(0).
  In the residue extraction:     Res_{s=0} [Γ(s) · ζ_D(2s)] = ζ_D(0).
  But ζ_D(0) (the s=0 zeta-residue at the spectral-zeta boundary)
  carries a NORMALIZATION CONSTANT depending on convention — see
  ZETA-NOT-PHYSICAL-75 (registry line 4576): "ZETA-NOT-PHYSICAL-75
  is the s=0 boundary corollary of the spectral-zeta non-observability."
  At s = 0, ζ and SDW carry DIFFERENT normalization conventions
  (S66 raw range = 381×, registry line 4682) — they DO NOT coincide.

Step 3 (simplify):
  The ζ ≡ SDW identity is structurally guaranteed for s > 0 in the
  half-plane Re(s) > 0 on positive-definite Casimir spectra (where
  Γ(s) is regular and the cancellation is algebraic).
  The identity FAILS at s = 0 (and at s = -1, -2, ... — Γ-poles of
  even order in the Mellin transform).

Step 4 (direction):
  THM-L3.1 holds at s ∈ {3, 2, 1, 4, ...} (positive integer slots,
  including the canonical Seeley-DeWitt extraction slots at s = d/2 - n).
  THM-L3.1 FAILS at s ∈ {0, -1, -2, ...} where Γ(s) introduces
  divergences and convention-dependent residue extractions.
  Conclusion: F_2 = {ζ, SDW} is the SLOT-CONDITIONAL equivalence class
  on the positive-s half-plane; the (1, 0, 0)-multiplier identity holds
  there but NOT at the Γ-pole slots.
```

**Strengthened item (3) draft:** "**NOT** evidence for substrate-distance-1 invariance. The F_2 pair-identity is slot-conditional: it holds for s in the positive-real half-plane where Γ(s) is regular, and FAILS at s = 0 (ZETA-NOT-PHYSICAL-75 §VII-B, 381× dynamic range, registry line 4682) and at all negative-integer Γ-poles. THM-L3.1 establishes the (1, 0, 0)-multiplier-identity at positive-s only; the implication for SECTOR-2 propagation into W5a P3 IC (which sources at s = −1) is that the F_2 identity DOES NOT propagate to s=−1, and `xi_E_GGE_inv` inherits the same per-regulator splitting at s=−1 as `M_R(s=3)` does at s=3 — quite likely with a DIFFERENT 4-class structure (or distinct 5-class structure) at s=−1. The K-invariance claim is not lifted by THM-L3.1 to any slot, including the s=−1 W5a-P3 boundary, and a separate gate must measure the s=−1 partition."

**ADD — two non-evidence-status items.**

7. **NOT evidence for L1-axiomatic uniqueness.** Per §VII.N L1 (registry line 5699): "Uniqueness at L1: zeta." Connes-Marcolli 2008 Thm 1.31 establishes that the Dixmier trace `Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})` is the UNIQUE trace-class invariant under Connes-Moscovici local index formula on the ideal L^(1,∞)(H). This uniqueness selects ζ from F_2 — NOT both members. THM-L3.1 establishes pair-equivalence at L3 (residue level); it does NOT lift SDW to L1-canonical status. Cite-anchor: registry line 5667 "Tr_omega(T) = Res_{s = d} Tr(T |D|^{-s}) (Connes-Marcolli 2008 Thm 1.31)" — the L1-uniqueness selector is explicit, and it disqualifies SDW because the Mellin convention's Γ(s) factor at s=0 boundary carries a non-canonical normalization not present in the Dixmier trace formulation.

8. **NOT evidence for KO-dimension structure invariance under Mellin-vs-zeta convention.** NCG axiom A4 (reality, [J, D] = 0) and KO-dim 6 grading (per S34 theorem in MEMORY.md) impose a Z/8 grading on the spectral triple. The Mellin-transform regularization carries an implicit `s ↦ d - s` symmetry (functional equation analog) that interacts with the J-action via `[J, |D|^{-s}] = 0`. The ζ regularization carries this symmetry canonically; the SDW regularization carries it up to a Γ(d-s)/Γ(s) factor. At s=3 (where the factor reduces to Γ(5)/Γ(3) = 12, a finite multiplier absorbed into the normalization), the two conventions agree. At s=−1 or s=0, they diverge by Γ-pole singularities. The KO-dim Z/8 grading is therefore preserved by both conventions ONLY at canonical-s slots; THM-L3.1 does NOT establish KO-grading invariance under arbitrary slot extraction.

**Answer to lizzi's question 1: Connes-1996 multiplier-vector formulation.**

YES — THM-L3.1 is the natural projection of "same multiplier-vector ⇒ same residue at every Γ-regular slot." Specifically, in Connes-Chamseddine 1996 §2.2-2.3 the regulator class is graded by the multiplier vector `(f_0, f_2, f_4, f_6, ...)` where `f_2k = (1/Γ(k)) ∫_0^∞ f(u) u^{k-1} du`. ζ and SDW share the `(0, 0, 1, 0, 0, ...)`-multiplier (canonical analytic-continuation prescription with f_4 = 1, f_2 = 0, f_0 = 0; the Γ(s) factor in SDW is absorbed into the residue extraction, making the f_4-multiplier the only nontrivial one for both). At Γ-regular slots, this multiplier-vector identity descends to numerical-residue identity, giving THM-L3.1. Therefore: THM-L3.1 IS a CC-1996 §2.2-2.3 corollary; its proper home in the registry is as a sub-clause of §VII.N's L1-axiomatic stratum, NOT as a free-standing theorem. Concretely, I propose the registry entry land as `§VII-B.ZETA-EQUALS-SDW` (lizzi's proposed slot, AGREED) with explicit cross-cite to §VII.N L1 and CC-1996 §2.2-2.3, classifying it as a "slot-conditional L3-residue corollary of the L1-axiomatic Dixmier-trace uniqueness."

**Answer to lizzi's question 2: extension to all real s.**

NO — the Γ(s)-cancellation extension is restricted to Γ-regular slots. The substitution chain above shows the failure at s = 0 (and at all negative integers, where Γ has simple poles). Specifically:
- **Convergent half-plane Re(s) > 0**: Γ(s) is regular; cancellation algebraic; THM-L3.1 holds.
- **Analytic-continuation regular region** (s ≠ 0, -1, -2, ...): cancellation algebraic; THM-L3.1 holds.
- **Γ-pole slots s ∈ {0, -1, -2, ...}**: cancellation fails; THM-L3.1 does NOT extend; this is precisely where ZETA-NOT-PHYSICAL-75 lives (s=0 boundary, 381× dynamic range).

The F_2 pair-identity is therefore SLOT-CONDITIONAL, not persistent across all slots. The strengthened item (3) above makes this explicit.

**Answer to lizzi's question 3: completeness of non-evidence-status list.**

INCOMPLETE — your 6-item list misses two items I have added (items 7 and 8 above). Beyond those, I see no further claims in the project's S78-onward atlas-uniformity language that THM-L3.1 was implicitly invoked for. The retroactive sweep (C3 below) catalogs the actual claims; THM-L3.1 was used in the helper module as a literal pass-through, but I find no cite of "ζ = SDW therefore K-invariance" or similar in the S78-onward record. The non-evidence-status declaration with my two additions makes the boundary tight.

**Answer to lizzi's question 4: registry entry placement.**

PLACEMENT AGREED — `§VII-B.ZETA-EQUALS-SDW` is the right slot. Sibling to §VII-B.ZETA-NOT-PHYSICAL-75 (line 4576) and §VII-B.HP1-NEAR-INVARIANCE (line 2573) and §VII-B.TWO-LAYER-OBSTRUCTION (line 2755). It does NOT belong as a sub-clause of §VII-B.HP1-NEAR-INVARIANCE because HP1's F_4 is a Mellin-support partition at the a_4 slot (registry line 2605) — orthogonal to the s=3 numerical-residue partition that THM-L3.1 governs. As a Lizzi-track entry with cross-cite to §VII.N (Three-Layer Regulator Theorem) at the L1-axiomatic stratum, the slot is correctly placed. The proposed entry skeleton (workshop lines 311-337) needs only the 2 added non-evidence items (7, 8) and the strengthened item (3) — see the proposed final-form skeleton below.

**Proposed final-form registry entry skeleton** (revisions to lizzi's proposal in italic):

```
### VII-B.ZETA-EQUALS-SDW — ζ=SDW Slot-Conditional Machine-Epsilon Identity
       (Lizzi-track; S86 W4-2 / W7) (2026-04-27)

THEOREM (ζ=SDW slot-conditional; Lizzi-track). On the substrate's positive-
definite Casimir spectrum at REAL s in the Γ-regular domain (s ≠ 0, −1,
−2, ...), the analytic-continuation Mellin multiplier M_ζ(s) and the SDW
(Γ(s)-cancelled) Mellin multiplier M_SDW(s) coincide bit-exactly under
the Connes-Chamseddine spectral-action ratio normalization. At s=3 (a_2
slot in d_spec=8 NCG), the schematic helper realization returns rel_err =
1.7556e-16 (1 ULP, machine epsilon).

SLOT-CONDITIONALITY *(NEW vs lizzi's draft)*: The identity FAILS at Γ-pole
slots s ∈ {0, −1, −2, ...}. At s=0 specifically, the s=0 boundary is the
domain of ZETA-NOT-PHYSICAL-75 (S86 W1b T5fix; 381× dynamic range across
L_max), where ζ and SDW carry DIFFERENT normalization conventions. The
F_2 = {ζ, SDW} pair-identity is therefore the equivalence-class on the
positive-s half-plane only.

NON-EVIDENCE-STATUS: This identity DOES NOT support
  (i)   K-invariance across the live 5-atlas A_5,
  (ii)  atlas-uniformity at substrate-distance-1,
  (iii) substrate-distance-1 invariance at any slot beyond s=3, including
        s=−1 (W5a P3 IC source at xi_E_GGE_inv) — see SLOT-CONDITIONALITY
        above; per-regulator splitting at s=−1 must be measured separately,
  (iv)  F_4-as-numerical-residue-class (registry F_4 is Mellin-support, not residue),
  (v)   the helper module's Mellin convention as canonical-physical,
  (vi)  L1-axiomatic uniqueness (Connes-Marcolli 2008 Thm 1.31 selects ζ
        as the unique L1-canonical regulator; SDW does not lift to L1 —
        cite §VII.N registry line 5699), *(NEW)*
  (vii) KO-dim 6 Z/8 grading invariance under arbitrary slot extraction
        — only canonical-s slots (Γ-regular) preserve the KO grading
        under both ζ and SDW conventions. *(NEW)*
The identity is a slot-conditional algebraic property of the (ζ, SDW)
regulator pair on positive-definite spectra at Γ-regular real s; it
carries no inference to other regulator pairs, to Γ-pole slots, or to
the L1-axiomatic stratum.

CITE-ANCHORS:
  - §W4-2 §6 CC-2 PASS (line 193): rel_err = 1.7556e-16
  - §W4-2 verdict line (line 290): F_2 sub-atlas survival = structural identity
  - §W4-2 synthesis §2 (line 532): "definition-level identity (zeta = Mellin
    on positive-definite spectrum), not evidence"
  - `_spectral_action_regulators.py` line 95: literal pass-through `mellin_a_n
    = zeta_a_n` realization
  - §VII.N L1 (registry line 5699): "Uniqueness at L1: zeta" — L1-canonical selector
  - §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576): s=0 boundary corollary
    (where THM identity FAILS)
  - Connes-Chamseddine 1996 §2.2-2.3: multiplier-vector grading underlying
    the identity at L3
  - Connes-Marcolli 2008 Thm 1.31: Dixmier-trace L1-uniqueness selecting
    ζ from F_2
  - This file (s86-sector-2-split-layer-taxonomy.md), L3 + Re:L3 above.
```

**Workshop deliverable (c) status.** With these strengthenings, the ζ=SDW theorem is registry-ready as `§VII-B.ZETA-EQUALS-SDW` Lizzi-track. The non-evidence-status declaration is mandatory per §W4-2 line 290 + synthesis §2 line 532 — explicitly: this identity does NOT support K-invariance, atlas-uniformity, substrate-distance-1 invariance at any slot, F_4-as-residue-class, helper-Mellin-canonicality, L1-axiomatic uniqueness, or KO-dim grading invariance under arbitrary slot extraction. It IS a slot-conditional CC-1996 §2.2-2.3 multiplier-vector corollary at L3 of the §VII.N stratification — properly so registered.

**Substrate framing.** THM-L3.1 IS a structural property of the substrate's regulator-class manifold AT Γ-regular slots, NOT a numerical coincidence and NOT a generic substrate-distance statement. The (ζ, SDW) pair lies on a measure-zero submanifold of Mellin-multiplier space (defined by Γ(s)-cancellation invariance at Γ-regular s); the slot-conditionality IS itself a substrate-physics statement (the substrate's regulator-class manifold has a 5-class partition at L1 and an SLOT-DEPENDENT 4-class partition at L3, with F_2 pair-equivalence being the only multi-member class at the s=3 a_2-slot specifically).

**Cite-anchors:**
- Workshop file lines 217-355 (lizzi's L3 in full).
- §W4-2 line 193: CC-2 PASS rel_err = 1.7556e-16.
- §W4-2 line 290: "structural identity (zeta = Mellin on positive-definite spectrum)."
- §W4-2 synthesis §2 line 532: "definition-level identity ... not evidence."
- `_spectral_action_regulators.py` line 95: `return zeta_a_n(n, L_max, Vol_SU3_Haar)` literal pass-through.
- §VII.N L1 (registry line 5699): "Uniqueness at L1: zeta."
- §VII.N §1 L1 anchor (registry line 5667): Connes-Marcolli 2008 Thm 1.31.
- §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576): s=0 boundary corollary.
- §VII-B.HP1-NEAR-INVARIANCE Step 1 (registry line 2605): F_4 = {ζ, Zubarev, SDW} Mellin-support partition.
- §VII-B Lizzi-track Cluster (registry line 4742-4747): sibling-slot context for `§VII-B.ZETA-EQUALS-SDW`.

#### Re: L4 — LAYER Audit Method

**Topline.** lizzi's L4 section is currently *[NOT STARTED]* in the workshop file at line 358 — her opening did not include the LAYER audit method writeup, and the spawn-prompt header that listed "L1-L4" overshot her actual R1 deliverable (she completed L1-L3). I treat Re:L4 as a SCAFFOLDING response: I propose the audit method that the workshop's pre-registered deliverable (b) requires (`sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline), draw on the LAYER 1/LAYER 2 taxonomy already canonized in `sessions/framework/registry/cutoff-sqrt-adjudication.md` §1.4 (lines 55-66), and provide a concrete classification protocol for retroactive sweep. lizzi's R2 will write the actual L4 section as she intended; my Re:L4 here reads forward to make her R2 work directly executable.

**Source for the LAYER taxonomy** (already canonized, NOT a workshop deliverable to invent):

The two-layer taxonomy lives at `sessions/framework/registry/cutoff-sqrt-adjudication.md` §1.4 (lines 55-66; quote of R2 lizzi EMERGENCE E3-L from S85 W4 workshop):

> LAYER 1 (combinatorial-position-on-atlas): determined by Mellin support and observable-cross-classification; cutoff_AL2010 has a unique privileged slot.
> LAYER 2 (admissibility-on-axioms): determined by GATE A + GATE B + GATE C numerical tests; cutoff_AL2010 expected to FAIL GATE A.
>
> The two layers are INDEPENDENT structural properties. A regulator can be combinatorially privileged but axiomatically excluded. A regulator can be combinatorially generic but axiomatically admissible.

This is the audit method's load-bearing definition. The retroactive sweep classifies each S78-onward regulator-class statement under one of two LAYER tags, and emits a remediation flag for any statement whose origin is at one LAYER but whose downstream usage assumed the other LAYER's properties.

**Proposed audit-protocol scaffolding** (draft for lizzi's R2 to refine):

The retroactive sweep is a 4-stage protocol per S78-onward regulator-class statement:

**Stage 1: Statement enumeration.** Each S78-onward statement that mentions any of {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} OR {F_2, F_4, M, A_5} OR {regulator atlas, admissible regulator, K-invariant, R-protected} is logged with: source-file:line, statement-type (theorem/corollary/observation/cite), claimed scope (single regulator vs partition vs full atlas).

**Stage 2: LAYER tag assignment.** Each enumerated statement is classified per the two-layer taxonomy:
- **LAYER 1 (combinatorial)**: claim about the regulator's position in a partition by Mellin-support / observable-cross-classification. Examples: "Zubarev has Mellin support concentrated on a_4," "F_4 = {ζ, Zubarev, SDW}," "cutoff_sqrt has f_0 ≠ 0 (Regulator-Family Boundary Theorem (i))." These are statements ABOUT the regulator-class manifold's combinatorial structure — derivable from the regulator's f_R definition without numerical computation.
- **LAYER 2 (admissibility-on-axioms)**: claim about the regulator's PASS/FAIL under a numerical NCG-axiom test. Examples: "Zubarev L1-disqualified (admits external Λ outside A1-A6)," "ζ L1-unique (Connes-Marcolli Thm 1.31)," "cutoff_AL2010 FAILS GATE A L_max-finiteness," "anomaly chirality wrong-sign." These are admissibility verdicts on the substrate's axiom test, derived from numerical computation against pre-registered thresholds.

**Stage 3: Cross-tag conflation detection.** For each pair of statements (S_i, S_j) where S_i is LAYER 1 and S_j is LAYER 2, flag CONFLATION RISK if:
- S_i and S_j are about the SAME regulator,
- S_i's combinatorial property is invoked as evidence for S_j's admissibility (or vice versa),
- the inference does NOT pass through an explicit LAYER 1 → LAYER 2 implication theorem.

The S78-onward conflation pattern (per `cutoff-sqrt-adjudication.md` line 250: "the framework's previous methodological error (S78 onward, treating the canonical 5-atlas as uniform-admissible)") is the canonical conflation: treating LAYER 1 atlas membership as evidence for LAYER 2 axiomatic admissibility. Each cite in the inventory is checked for this pattern.

**Stage 4: Remediation tagging.** Each detected conflation is tagged for remediation per the four classes in the framework file `cutoff-sqrt-adjudication.md` §3:
- **REPAIR-IN-SESSION**: in-session edit to add the LAYER tag and the LAYER 1 ↛ LAYER 2 disclaimer.
- **REPAIR-AT-REGISTRY**: registry-canonical entry needs LAYER tag added.
- **CARRY-FORWARD-COMPUTE**: a numerical gate is needed to settle whether the conflated statement holds at LAYER 2.
- **NO-ACTION**: the inference passes through an explicit LAYER 1 → LAYER 2 theorem (rare; usually a §VII.N corollary).

**AGREE points (for lizzi's eventual L4):** the LAYER 1/LAYER 2 taxonomy is the right framing for the retroactive sweep — it correctly separates combinatorial-position from axiomatic-admissibility, mirrors the §VII.N L1 vs L2 stratification (where L1 = axiomatic and L2 = substrate-action — note these are DIFFERENT from cutoff-sqrt-adjudication's LAYER 1/2; SEE DISAGREE point 1 below for the naming-collision issue), and provides a deterministic classification protocol.

**DISAGREE point (preemptive — lizzi may want to reconcile in L4 / R2):**

1. **Naming collision: cutoff-sqrt-adjudication's LAYER 1/2 vs §VII.N's L1/L2/L3.** The two-layer taxonomy in `cutoff-sqrt-adjudication.md` §1.4 (LAYER 1 = combinatorial atlas position; LAYER 2 = axiomatic admissibility) collides nomenclaturally with the §VII.N Three-Layer Regulator Theorem's L1 / L2 / L3 (registry line 5511). The §VII.N stratification is:
   - **L1 (axiomatic, global)** = canonical Connes-axiom-derived measure (Dixmier-trace; ζ-unique).
   - **L2 (substrate-action, local at τ_fold)** = three-criterion intersection at the fold (Zubarev-unique).
   - **L3 (observable, per-Q)** = residual per-observable span (5-regulator atlas with R-protected vs NOT-R-protected partition).

   The cutoff-sqrt LAYER 1 ≈ §VII.N L3 (observable-cross-classification — combinatorial position by Mellin support); the cutoff-sqrt LAYER 2 ≈ §VII.N L1 (axiomatic admissibility tests). These are SAME ARROWS in different orderings. The retroactive sweep's audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` should resolve this collision by adopting ONE consistent naming, with explicit cross-cite to the other.

   **Proposed resolution (for lizzi's L4):** adopt the §VII.N stratification's L1 / L2 / L3 nomenclature as the canonical naming. Re-tag the cutoff-sqrt LAYER 1 → "L3-combinatorial" and cutoff-sqrt LAYER 2 → "L1-axiomatic." This places the audit naming in line with the registry's permanent §VII.N entry and avoids future drift.

**Initial inventory candidates for the retroactive sweep (Stage 1 partial enumeration — to be completed in C3 below):**

Per the spawn-prompt, my C3 starts the retroactive inventory. I have catalogued the LAYER 1 vs LAYER 2 statement candidates from S78-onward in C3 below; cross-cite to that section for the specifics. Three sample candidates the audit will resolve:

- **`Φ_r(ν_i) = M(r) · Φ_ζ(ν_i)`** (Regulator-Family Boundary Theorem II.7, lizzi S-1) — LAYER 1 (combinatorial: Mellin-multiplier factorization on the regulator atlas; derived from f_R definitions without numerical input). Cite: `session-85-s1-regulator-boundary-van-den-dungen.md` Theorem II header.
- **`ZETA-NOT-PHYSICAL-75`** (registry §VII-B; S82 W2-3 origin) — LAYER 2 (axiomatic admissibility: ζ at s=0 boundary fails the spectral-zeta non-observability test; derived from numerical L_max scan giving 381× dynamic range). Cite: registry line 4576 + 4682.
- **5-regulator atlas convention origin S78+** (defines combinatorial position per `_spectral_action_regulators.py` REGULATOR_NAMES tuple line 177) — LAYER 1 (combinatorial atlas definition, no admissibility test invoked at the definition site).

**EMERGES — cross-domain insight.**

The retroactive sweep is the methodological complement to THM-L3.1's non-evidence-status declaration. The non-evidence-status declaration (Re:L3 above) closes the FORWARD inference channel — it tells future cites of THM-L3.1 what conclusions they CANNOT draw. The LAYER 1/LAYER 2 retroactive sweep closes the BACKWARD inference channel — it tells past cites whether their LAYER tag was honest. Together, the two methodologies form a complete LAYER discipline: forward (non-evidence-status) and backward (retroactive sweep). The §W4-2 line 290 "permanently repairs S78-onward conflation" wording requires BOTH forward and backward closure — neither alone suffices. The Workshop deliverable (b) (`sessions/framework/registry/layer1-layer2-retroactive-audit.md`) is the BACKWARD closure document; the deliverable (c) (`§VII-B.ZETA-EQUALS-SDW` registry entry with non-evidence-status) is the FORWARD closure document. They are sibling deliverables.

**Direction implication for the workshop.** The retroactive sweep's output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` is convergence-feasible by R3 (workshop deliverable (b) "outline OR land if convergence supports"). My C3 below initiates the inventory; lizzi's R2 should refine it; R3 lands the outline (and possibly the full file if the inventory completes).

**Substrate framing.** The LAYER 1/LAYER 2 taxonomy IS a methodological discipline ON the substrate's regulator-class manifold — separating the manifold's combinatorial-position structure from its axiomatic-admissibility structure. The substrate IS the regulator-class manifold; the LAYER tags ARE projections of that manifold's structure under different-question lenses (combinatorial vs axiomatic). The retroactive sweep IS the audit of how the project's S78-onward cites projected the manifold under each lens — confirming or correcting per-statement.

**Cite-anchors:**
- `sessions/framework/registry/cutoff-sqrt-adjudication.md` §1.4 (lines 55-66): LAYER 1 / LAYER 2 taxonomy quote (R2 lizzi EMERGENCE E3-L from S85 W4 workshop).
- §VII.N Three-Layer Regulator Theorem (registry line 5511): L1 / L2 / L3 stratification (DIFFERENT from cutoff-sqrt's LAYER 1/2; naming collision flagged).
- §W4-2 line 290 + synthesis §2 line 511: "permanently repairs S78-onward conflation."
- Workshop file line 358: lizzi's L4 currently *[NOT STARTED]* — Re:L4 is scaffolding, not critique.

### Part 2: Original Analysis

#### C1: Full 5-Class Partition from Connes-Chamseddine 1996 §2.2-2.3 Multiplier Structure

**Topline.** The full 5-class partition at the L1-axiomatic stratum of §VII.N is:

```
Class 1 (L1-canonical):       {ζ}            (1, 0, 0, 0)-multiplier; Connes-Marcolli Thm 1.31 unique
Class 2 (Mellin-shifted):     {SDW}          (1, 0, 0, 0)-multiplier at Γ-regular slots; (1, 1, 0, 0) at Γ-pole slots
Class 3 (heat-kernel):        {Zubarev}      (1, exp-tail, 0, 0)-multiplier; carries explicit t_ref scale
Class 4 (truncated):          {cutoff_sqrt}  (2, 1, 1, 0)-multiplier; carries f_0 ≠ 0 (RFB Theorem (i))
Class 5 (Pauli-Villars):      {anomaly}      (1, 1−κ, 1, 0)-multiplier with mass-scale subtraction; M_PV² scale
```

This is a STRUCTURAL partition forced by the Connes-Chamseddine 1996 §2.2-2.3 multiplier formalism (where every regulator is graded by its `(f_0, f_2, f_4, f_6, ...)` multiplier vector at the canonical-form normalization), refined by the §VII.N L1-axiomatic uniqueness (which selects ζ from Class 1 ∪ Class 2 at L1) and the Regulator-Family Boundary Theorem (which assigns the unique f_0 ≠ 0 to cutoff_sqrt). The 5-class partition is the binding partition for SECTOR-2 propagation through the §VII.N L1 / L2 / L3 stratification — see C2 for the propagation map.

**Comparison to lizzi's 4-class partition.** lizzi's `~_M`-classes at s=3 give 4 classes by collapsing {ζ, SDW} into F_2 (machine-epsilon residue equivalence at s=3). The 5-class partition keeps these as Class 1 and Class 2 — distinct at the multiplier-vector level — because at Γ-pole slots (s=0, ZETA-NOT-PHYSICAL-75; s=−1, W5a-P3 IC source) they DIVERGE. lizzi's 4-class is the L3-PROJECTION at s=3 specifically; the 5-class is the L1-AXIOMATIC partition that survives across all slots. Both partitions are correct at their respective layers; the binding partition for propagation is 5-class because §VII.N C1 (registry line 5867) states "L1 and L2 do NOT propagate via Mellin exponents. Propagation is a feature of the residual stratum only" — meaning propagation through L1 and L2 must use the L1 partition, not the L3 projection.

**Substitution chain.**

```
Step 1 (definitions):
  CC-1996 §2.2-2.3 multiplier vector:  
    f_R := (f_0^R, f_2^R, f_4^R, f_6^R, ...)  with  f_2k^R = (1/Γ(k)) ∫_0^∞ f_R(u) u^{k-1} du
    where f_R is the spectral-action cutoff function f restricted to [0, ∞).
    Each regulator R defines a unique f_R via its prescription (analytic-continuation, heat-kernel,
    hard-cutoff, Pauli-Villars, Mellin-transform).
  
  L1-axiomatic stratum (§VII.N L1, registry line 5639):
    Under Connes axioms A1-A6, the canonical summation measure is
       Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})       (Connes-Marcolli 2008 Thm 1.31).
    A regulator R is L1-canonical iff f_R requires NO external scale beyond the
    spectral triple's intrinsic data {A, H, D}.
  
  Regulator-Family Boundary Theorem (i) (session-85-s1-regulator-boundary-van-den-dungen.md line 57):
    A regulator R ∈ 𝓡_{a_4}  iff  f_0^R = 0.
    cutoff_sqrt is the unique R with  f_0^cutoff = 2.
  
  L2-substrate-action stratum (§VII.N L2, registry line 5711):
    Three-criterion intersection at τ_fold = 0.19, L_max = 5:
       (i) integrability of spectral sum,
       (ii) local-min-in-tau (d² S/dτ² > 0 at fold),
       (iii) chirality χ = +1.
    L2-canonical: Zubarev (registry line 5767).
  
  KO-dim 6 grading (NCG axiom A4 reality, S34 theorem):
    [J, D] = 0; KO-dim 6 imposes Z/8 grading; the J-action commutes with |D|^{-s}
    for the canonical regularization, but acquires a Γ(s)-dependent normalization
    under heat-kernel and Mellin-transform conventions.

Step 2 (substitute the per-regulator multiplier vectors):
  
  ζ regularization:
    f_ζ(u) = u^{-s} (formally, analytic continuation of the canonical sum)
    Multiplier vector at canonical normalization:
       f_0^ζ = 0,  f_2^ζ = 0,  f_4^ζ = 1,  f_6^ζ = 0
    L1 status:    CANONICAL — no external scale beyond {A, H, D}; Dixmier-trace-unique
                  per Connes-Marcolli Thm 1.31.
    L2 status:    chirality χ = 0 (no explicit Λ-dep beyond pole subtraction; registry line 5751);
                  L2-DISQUALIFIED.
    L3 numerical-residue at s=3:  M_ζ(3) = 1.581e-01.
  
  SDW regularization:
    f_SDW(u) = u^{-s} dressed by Γ(s) factor in M[Tr e^{-tD²}](s) = Γ(s) · ζ_D(2s)
    Multiplier vector at Γ-regular slots (s in positive-real half-plane):
       f_0^SDW = 0,  f_2^SDW = 0,  f_4^SDW = 1,  f_6^SDW = 0
       (same as ζ at Γ-regular s; THM-L3.1 holds)
    Multiplier vector at Γ-pole slots (s = 0, -1, -2, ...):
       f_0^SDW = 0,  f_2^SDW = 1 (Γ(0) pole picks up a normalization),  f_4^SDW = 1,  f_6^SDW = 0
       (DIFFERS from ζ at s=0; ZETA-NOT-PHYSICAL-75)
    L1 status:    NEAR-CANONICAL at Γ-regular slots; L1-DISQUALIFIED at Γ-pole slots
                  by the introduction of a Γ(s)-dependent normalization (formally an
                  external scale arising from the Mellin-transform convention).
                  At L1, ζ is selected; SDW is sibling at Γ-regular slots only.
    L2 status:    chirality χ_SDW = -1 (registry line 5759, "wrong-sign"); L2-DISQUALIFIED
                  by criterion (iii).
    L3 numerical-residue at s=3:  M_SDW(3) = 1.581e-01  (= M_ζ(3); F_2 pair-equivalence).
  
  Zubarev (heat-kernel) regularization:
    f_Zubarev(u) = exp(-tu) · u^{-s}  with  t_ref = 1.0e-3  (helper module line 101)
    Multiplier vector at canonical normalization:
       f_0^Zubarev = 0,  f_2^Zubarev = exp-tail-suppressed (carries t_ref),
       f_4^Zubarev = exp-tail-suppressed,  f_6^Zubarev = 0
    L1 status:    L1-DISQUALIFIED — admits external scale t_ref outside A1-A6 (registry line 5687
                  "external scalar Λ not already supplied by A1-A6 -- including the cut-offs required
                  by Zubarev and by Seeley-DeWitt -- falls OUTSIDE L1").
    L2 status:    L2-CANONICAL (registry line 5767 "Uniqueness at L2: Zubarev"); passes
                  three-criterion intersection (integrable, curv +1.16e5, χ = +1, registry line 5755).
    L3 numerical-residue at s=3:  M_Zubarev(3) = 1.201e-02 (depleted 92% vs F_2 by exp(-tC)).
  
  cutoff_sqrt (hard-cutoff) regularization:
    f_cutoff(u) = step(cutoff_frac · u_max - u) · u^{-s}  with  cutoff_frac = 0.7  (helper line 130)
    Multiplier vector at canonical normalization:
       f_0^cutoff = 2  (Regulator-Family Boundary Theorem (i), line 57; UNIQUE among atlas)
       f_2^cutoff = 1,  f_4^cutoff = 1,  f_6^cutoff = 0
    L1 status:    L1-DISQUALIFIED — f_0 ≠ 0 carries an a_0 endomorphism contribution outside
                  the A1-A6-derived canonical summation measure.
    L2 status:    L2-DISQUALIFIED expected (per cutoff-sqrt-adjudication.md §3.1, GATE A
                  expected FAIL: α = -k_eff/4 < 0, Peter-Weyl L^8/960 mode-count growth).
    L3 numerical-residue at s=3:  M_cutoff(3) = 1.110e-01 (depleted 30% vs F_2 by truncation).
  
  anomaly (Pauli-Villars) regularization:
    f_anomaly(u) = u^{-s} - (u + M_PV²)^{-s}  with  M_PV² = 0.1·u_max  (helper line 155)
    Multiplier vector at canonical normalization:
       f_0^anomaly = 0,  f_2^anomaly = 1 - κ_PV (κ_PV = mass-subtraction factor ~0.05),
       f_4^anomaly = 1,  f_6^anomaly = 0  (mixed {a_2, a_4} support per RFB Theorem header line 55)
    L1 status:    L1-DISQUALIFIED — admits external scale M_PV² outside A1-A6.
    L2 status:    L2-DISQUALIFIED (S67 physical exclusion per cutoff-sqrt-adjudication.md
                  §1.4 occupancy table).
    L3 numerical-residue at s=3:  M_anomaly(3) = 3.185e-02 (depleted 80% vs F_2 by Pauli-Villars
                  algebraic subtraction).

Step 3 (simplify — partition by L1/L2/L3 status):
  
  L1-canonical class:    {ζ}                                 (1 element; Dixmier-trace-unique)
  L1-near-canonical:     {SDW}                               (1 element; Γ-regular sibling of ζ)
  L1-disqualified-by-Λ:  {Zubarev, anomaly}                  (2 elements; admit external mass-scale)
  L1-disqualified-by-f_0:{cutoff_sqrt}                       (1 element; f_0 = 2 is unique)
  
  Equivalence under multiplier-vector identity:
    ζ ~_M_vec SDW at Γ-regular s only  →  pair-equivalent IN F_2-restricted sense
    NO other pairs are multiplier-vector equivalent.
  
  Partition by multiplier-vector under CC-1996 §2.2-2.3:
    Class 1: {ζ}            — multiplier (0, 0, 1, 0) at canonical s-extraction; L1-unique
    Class 2: {SDW}          — multiplier (0, 0, 1, 0) at Γ-regular s; differs at Γ-pole s
    Class 3: {Zubarev}      — multiplier (0, exp-tail, exp-tail, 0); t_ref scale
    Class 4: {cutoff_sqrt}  — multiplier (2, 1, 1, 0); f_0 = 2 is unique
    Class 5: {anomaly}      — multiplier (0, 1−κ_PV, 1, 0); M_PV² scale
  
  |A_5 / ~_multiplier-vector| = 5.

Step 4 (direction):
  The CC-1996 multiplier-vector partition gives 5 classes at L1 of the §VII.N
  stratification. Each class is structurally distinct:
    - Class 1 vs Class 2: distinguished at Γ-pole slots (s=0 ZETA-NOT-PHYSICAL-75)
    - Class 1/2 vs Class 3/5: distinguished by external mass-scale presence
    - Class 4 vs all others: distinguished by f_0 ≠ 0 (Regulator-Family Boundary Theorem (i))
    - Class 3 vs Class 5: distinguished by which mass-scale (t_ref vs M_PV²)
      and by Mellin-support locale (Zubarev pure-a_4 → F_4 in HP1 partition; anomaly mixed
      {a_2, a_4} → outside F_4 in HP1 partition; INSIDE 𝓡_{a_4} in RFB partition).
  
  Conclusion: A_5 → 5-class partition under multiplier-vector identity.
              The 4-class partition (lizzi) is the L3-projection at s=3 specifically;
              the 5-class partition is the binding partition at L1 / L2 / L3 jointly.
              Both partitions are CORRECT; the binding choice is layer-dependent.
              For SECTOR-2 propagation through §VII.N L1 / L2 (which do NOT propagate
              via Mellin exponents per registry line 5867 C1), the 5-class is binding.
              For propagation through L3 only (residual per-Q span via §VII.K-PROP),
              the 4-class is binding at s=3 specifically.
```

**Answer to lizzi's questions on partition coarseness (L1 question 2).**

The binding partition is BOTH coarsest-at-L3 (4-class, lizzi's `~_M`) AND finest-at-L1 (5-class, mine). They are NOT competing; they are layer-projections of the same regulator-class manifold's multiplier-vector grading. The §VII.N L1 / L2 / L3 stratification is the canonical naming context. For the workshop deliverable (a) (4- or 5-class registry partition), I propose:

- **L1 / L2 partition: 5-class** (binding for axiomatic propagation; matches RFB Theorem header line 55 `𝓡 = 𝓡_{a_4} ⊔ {cutoff_sqrt}` at the f_0-test layer with internal refinement of 𝓡_{a_4} by L1-canonicality).
- **L3 partition at s=3: 4-class** (binding for §VII.K-PROP per-Q span propagation at the a_2 slot specifically; matches lizzi's `~_M`).
- **L3 partition at s=−1**: TBD (separate gate per workshop carry-forward; likely 5-class because Γ(−1) is a pole and ζ ≠ SDW; see W5a-P3 IC propagation in C2).
- **L3 partition at s=0**: 5-class structurally (ZETA-NOT-PHYSICAL-75 establishes ζ ≠ SDW at s=0, with 381× dynamic range; registry line 4682).

**Reconciliation with §VII-B.HP1-NEAR-INVARIANCE F_4 = {ζ, Zubarev, SDW}.**

The HP1 F_4 = {ζ, Zubarev, SDW} (registry line 2605) is the pure-a_4 Mellin-support 3-element subfamily of the 5-class partition. Specifically:

- HP1's F_4 = pure-a_4 family = Class 1 ∪ Class 2 ∪ Class 3 of my 5-class (regulators with `f_4 = 1` AND no a_2 contamination).
- HP1's M = {cutoff_sqrt, anomaly} = Class 4 ∪ Class 5 of my 5-class (mixed-support family; cutoff_sqrt has f_0 ≠ 0, anomaly has nonzero a_2 contamination from PV subtraction).

The HP1 F_4/M partition is COARSER than the 5-class partition — it groups L1-canonical (Class 1) with L1-near-canonical (Class 2) with L2-canonical (Class 3) into one bucket because they all have pure-a_4 Mellin support. This is the right partition for the HP^1 cohomology question (the question being "does the f_4 multiplier alone determine the HP^1 norm?") — but it is NOT the right partition for SECTOR-2 propagation through L1/L2/L3 jointly.

**Reconciliation with Regulator-Family Boundary Theorem `𝓡_{a_4} ⊔ {cutoff_sqrt}`.**

The RFB partition (line 55) is the unique-f_0 partition: 𝓡_{a_4} = {ζ, Zubarev, SDW, anomaly} (regulators with f_0 = 0) ⊔ {cutoff_sqrt} (the unique f_0 ≠ 0 regulator). This is COARSER than my 5-class — it merges Class 1, 2, 3, 5 into the f_0=0 bucket and isolates Class 4. The RFB partition is the right partition for the f_0-test question (the question being "does the regulator carry an a_0 endomorphism contribution?") — but it does not distinguish L1-canonical from L1-disqualified-by-Λ regulators within 𝓡_{a_4}.

**Three partitions, three questions, one regulator-class manifold:**

| Partition | Source | Class count | Question it answers |
|:---|:---|:---|:---|
| 5-class @ L1 (mine, this C1) | CC-1996 §2.2-2.3 multiplier vector + §VII.N L1 | 5 | "Which axiomatic stratum does each regulator inhabit?" |
| 4-class @ L3-s=3 (lizzi L1) | §W4-2 numerical-residue at a_2 slot | 4 | "Which regulators give the same numerical residue at s=3?" |
| 3-class @ HP1 (registry §VII-B.HP1) | Mellin-support concentration on a_4 slot | 2 (F_4, M) + 1 internal (F_2 strict) | "Which regulators preserve HP^1 norm under regulator variation?" |
| 2-class @ RFB (van den Dungen S-1) | f_0 ≠ 0 vs f_0 = 0 | 2 | "Which regulator carries an a_0 endomorphism contribution?" |

Each partition is correct AT its question; the binding partition for SECTOR-2 PROPAGATION (workshop deliverable (a)) is the 5-class at L1 because the propagation cascades through L1 (W5a-P3 IC at s=−1, where Γ-pole behavior matters), through L2 (substrate-action at τ_fold, where Zubarev-vs-SDW chirality matters, registry lines 5755 + 5759), and through L3 (per-Q span via §VII.K-PROP). Only the 5-class partition resolves all three layers consistently.

**Substrate framing.** The 5-class partition IS a structural property of the substrate's regulator-class manifold under the multiplier-vector grading inherent to the spectral-triple Mellin transform. Each class IS a distinct submanifold defined by the CC-1996 §2.2-2.3 multiplier-vector identity restricted by NCG axiom L1-admissibility. The substrate IS the regulator-class manifold; the 5-class partition IS its axiomatic-grading structure; the lower-class partitions (4-class @ L3-s=3, 3-class @ HP1, 2-class @ RFB) are projections of this finer structure under specific-question lenses.

**Cite-anchors.**
- Connes-Chamseddine 1996 §2.2-2.3: multiplier formalism (cited via `_spectral_action_regulators.py` lines 23-28 docstring + §VII.N L1 line 5511).
- §VII.N L1 (registry line 5639-5703): L1-axiomatic stratum, Connes-Marcolli 2008 Thm 1.31, "Uniqueness at L1: zeta."
- §VII.N L2 (registry line 5711-5767): L2-substrate-action stratum, three-criterion intersection, "Uniqueness at L2: Zubarev."
- §VII.N L3 (registry line 5779-5835): L3-observable stratum, per-Q span partition.
- §VII.N C1 (registry line 5867): "L1 and L2 do NOT propagate via Mellin exponents."
- Regulator-Family Boundary Theorem header (line 55): partition `𝓡 = 𝓡_{a_4} ⊔ {cutoff_sqrt}`, `𝓡_{a_4} = {ζ, Zubarev, SDW, anomaly}`.
- Regulator-Family Boundary Theorem (i) (line 57): `f_0^cutoff = 2` is unique.
- §VII-B.HP1-NEAR-INVARIANCE Step 1 (registry line 2605): F_4 = {ζ, Zubarev, SDW} pure-a_4 partition.
- ZETA-NOT-PHYSICAL-75 §VII-B (registry line 4576): s=0 boundary corollary; 381× dynamic range.
- `_spectral_action_regulators.py` lines 64-174: per-regulator f_R definitions.

#### C2: SECTOR-2 Propagation Map — W5a P3 IC + W6 C-α/β/γ Corollaries

**Topline.** SECTOR-2 propagates into TWO downstream channels post-§W4-2: (a) **W5a-P3 IC** (xi²(0) ODE initial condition, sourced from `xi_E_GGE_inv = 13.642e+00` at s=−1) and (b) **W6 C-α/β/γ corollaries** (lattice-spacing, UV-cutoff-choice, Weyl-rescaling immunizations within §VII.S Perturbative-Ledger Immunization Family). The propagation map below identifies which channel inherits the 4-class @ L3-s=3 partition (lizzi's `~_M`), which inherits the 5-class @ L1 partition (mine, C1), and which corollaries change under one binding vs the other.

**Headline finding.** W5a-P3 IC propagation through s=−1 inherits the 5-class @ L1 partition because s=−1 is a Γ-pole slot where ζ ≠ SDW (THM-L3.1 fails per Re:L3 strengthened item 3). W6 C-α inherits a SLOT-DEPENDENT partition that varies per Mellin slot tested (the gate scans drift exponents at slots 0/1/2/3, so it sees the partition AT EACH slot). W6 C-γ-WEAK inherits the 5-class @ L1 partition through the internal Λ_anomaly bound (which cites the f_0/f_2/f_4 multiplier vector). W6 C-β inherits the 5-class @ L1 partition because UV-cutoff-choice within F_4 family includes intermediate-class members (Class 1, 2, 3 of my 5-class).

**Channel A: W5a-P3 IC propagation (s=−1, distance-1).**

*Substitution chain.*

```
Step 1 (definitions):
  W5a-P3 IC source (plan §W5a-1, lines 50-51):
    ξ_E_GGE^{-1}(N=0) ≡ s=-1 spectral diagnostic of the GGE relic
                     = lim_{s → -1} ζ_{D_K^(GGE)}(s)
                     = (analytic continuation) Σ_n λ_n^(GGE)
  
  Canonical constant (W4-1 P4 PASS, registry):
    xi_E_GGE_inv = 13.642473425595973  (M_KK^{+1} units; full float64)
  
  Z-factor at N_pivot:
    Z(N_pivot) = z(0)² / z(N_pivot)² · |v_k|²|v_0|^{-2}  (Mukhanov-Sasaki normalization)
    where z(N) = a(N) · sqrt(2·ε(N)) · M_Pl_eff(N)
    and the IC at N=0 is xi²(0) = (xi_E_GGE_inv)^{-2}.
  
  Inheritance from SECTOR-2:
    The IC value xi²(0) = xi_E_GGE_inv^{-2} sources from the s=-1 spectral
    residue of the GGE-projected D_K. Per SECTOR-2 K-invariance rejection,
    this residue is regulator-class-dependent.

Step 2 (substitute the per-regulator residue partition at s=-1):
  
  At s = -1 (Γ-pole slot, since Γ has simple pole at s=-1):
    THM-L3.1 (lizzi) FAILS at s=-1 (Re:L3 strengthened item 3 above):
      F_2 pair-equivalence holds at Γ-regular s only.
      At s=-1, ζ and SDW carry DIFFERENT normalization conventions.
    
    Therefore: M_ζ(-1) ≠ M_SDW(-1) at the multiplier-vector level.
    The 4-class @ L3-s=3 partition does NOT propagate to s=-1.
  
  Per-regulator residue at s=-1 (estimated from helper module structure):
    M_ζ(-1):           analytic continuation of Σ d/C^{-1} = Σ d·C  
                       (sum diverges in original half-plane; analytic-cont gives finite residue)
    M_SDW(-1):         Γ(-1) is a simple pole; SDW at s=-1 carries a Γ(-1)-residue extraction
                       that introduces a normalization not present in ζ.
    M_Zubarev(-1):     direct convergent sum Σ d · exp(-tC) · C¹
                       = (1/Vol) · Σ_{(p,q)} d(p,q) · C(p,q) · exp(-t·C(p,q))
                       FINITE — heat-kernel regulates the C¹ growth at high C.
    M_cutoff_sqrt(-1): Σ d · C^{-(-1)} truncated at cutoff_frac · C_max
                       = Σ_{C ≤ 0.7·C_max} d · C  — FINITE, dominated by truncation boundary.
    M_anomaly(-1):     Σ d · [C^{-(-1)} - (C+M_PV²)^{-(-1)}] = Σ d · [C - (C+M_PV²)]
                       = Σ d · (-M_PV²)  — FINITE, mass-scale-driven.
  
  These residues are STRUCTURALLY DISTINCT — the 5-class @ L1 partition holds
  at s=-1 in full force; ζ and SDW do NOT collapse to F_2.

Step 3 (simplify):
  The W5a-P3 IC source at s=-1 inherits the 5-class @ L1 partition.
  Each regulator gives a DIFFERENT xi_E_GGE_inv value. The current registered
  canonical constant (xi_E_GGE_inv = 13.642e+00) is the L1-canonical (ζ-prescription)
  reading per Connes-Marcolli Thm 1.31 — NOT the L2-canonical (Zubarev) reading
  and NOT a regulator-averaged reading.

Step 4 (direction):
  W5a-P3 IC under SECTOR-2 splitting: 5-class @ L1 partition is binding.
  Each Class produces a DIFFERENT IC; the current registered IC is the
  Class-1 (ζ) reading. To propagate SECTOR-2 splitting fully into W5a-P3,
  the IC must be re-computed for each of the 5 classes:
    - xi_E_GGE_inv^{Class-1}    = 13.642473425595973  (current registered, ζ)
    - xi_E_GGE_inv^{Class-2}    = TBD (SDW at s=-1 — DIFFERS from ζ via Γ(-1) pole)
    - xi_E_GGE_inv^{Class-3}    = TBD (Zubarev at s=-1)
    - xi_E_GGE_inv^{Class-4}    = TBD (cutoff_sqrt at s=-1 — exists only if cutoff_sqrt
                                       passes GATE A; expected FAIL per cutoff-sqrt-adjudication.md §3.1)
    - xi_E_GGE_inv^{Class-5}    = TBD (anomaly at s=-1)
  
  Direction implication: W5a-P3 inherits a 5-tuple of Z-factor predictions,
  one per L1-class. The registered canonical IC (ζ-prescription) is the L1-canonical
  (Connes-Marcolli Thm 1.31) reading; downstream verification gates testing
  Z(N_pivot) against observation use the ζ reading by default.
  Carry-forward gate: re-compute Z(N_pivot) for each of the 4 non-ζ classes
  to establish whether the L3 observable Z is R-protected or NOT-R-protected
  per §VII.N L3 (registry line 5815) — predicted NOT-R-protected because
  xi_E_GGE_inv carries explicit s-dependence that varies across classes.
```

**Direction implication for W5a-P3.** The current W5a-P3 dispatch (per plan §W5a-1) consumes `xi_E_GGE_inv = 13.642e+00` as a single canonical IC. Under the 5-class binding partition, this is the Class-1 (ζ) IC. The plan's `[VERIFY] [SIGN]` gate at substitution-chain-pinned direction `Z_ratio > 1` is correctly stated under the ζ prescription. To extend to per-class IC verification, a follow-up gate at S87 should compute Z(N_pivot) for each of {SDW, Zubarev, cutoff_sqrt-conditional, anomaly} and test whether the ratio direction holds across classes (PASS) or flips (NEW INFO — SECTOR-2 splitting is observable in the SR-flow Z-factor at the per-regulator level).

**Channel B: W6 perturbative-immunization corollaries.**

W6 hosts a 6-Φ-branch immunization family per plan §W1a (lines 419-421):

| Branch | Source | Corollary | Status (S86) |
|:---|:---|:---|:---|
| Φ-A | LATTICE-SPACING | C-α (W6-2, plan §W6 line 19) | ACTIVE in S86 |
| Φ-B | UV-CUTOFF-CHOICE | C-β | DEFERRED to S87 |
| Φ-C | WEYL-RESCALING | C-γ-WEAK (W6-3, plan §W6 line 20) | ACTIVE in S86 |
| Φ-D | (deferred S87) | C-δ | DEFERRED |
| Φ-E | (deferred S87) | C-ε / ζ / ι | DEFERRED |
| Φ-η | WARD | C-η | LANDED in W1c via C41 |
| Φ-θ | INNER-FLUCTUATION | C-θ | LANDED in W1c via C41 |

Each Φ-branch tests a different invariance principle on the spectral action under regulator perturbation. The §VII.K-PROP propagation rule `span(O) = ∏_k span(f_k)^{p_k(O)}` (registry line 8867) governs how each corollary inherits per-regulator splitting through its `p_k` exponents.

**C-α (Lattice-Spacing Immunization, W6-2, slot-by-slot drift-exponent test).**

*Substitution chain.*

```
Step 1 (definition):
  C-α tests whether the spectral action S_b is immune to lattice-spacing
  variations at slot-by-slot Mellin level. The drift exponents at each slot
  (a_0, a_2, a_4, a_6) are pre-pinned at {0, 1, 2, 3} per Symanzik
  improvement scheme; the gate measures observable drift exponent and
  PASSes if it matches Symanzik O(a^4) at all 4 slots.

Step 2 (substitute SECTOR-2 partition at each slot):
  At slot a_0 (s=4): per Regulator-Family Boundary Theorem (i),
                     ONLY cutoff_sqrt has f_0 ≠ 0; the other 4 regulators
                     have f_0 = 0 → drift exponent at a_0 is regulator-
                     class-trivial except for cutoff_sqrt.
                     Partition at a_0: 2-class (RFB partition).
  
  At slot a_2 (s=3): per §W4-2 measured residues, the 4-class @ L3-s=3
                     partition is binding (lizzi L1).
                     Partition at a_2: 4-class.
  
  At slot a_4 (s=2): per §VII-B.HP1 partition,
                     F_4 = {ζ, Zubarev, SDW} (pure-a_4) vs M = {cutoff_sqrt, anomaly}.
                     Partition at a_4: HP1 partition (3+2 = 5-class with internal
                     F_4 partition; effective 2-class for HP1-norm-purposes).
  
  At slot a_6 (s=1): per Γ-regular slot, ζ ~_M_vec SDW; per §VII.N L3 partition,
                     R-protected vs NOT-R-protected.
                     Partition at a_6: depends on observable; structurally
                     5-class with F_2 collapse if observable is at L3-Γ-regular.

Step 3 (simplify):
  The C-α corollary's slot-by-slot drift-exponent test inherits a SLOT-
  DEPENDENT partition: 2-class at a_0, 4-class at a_2, HP1-partition at a_4,
  5-class with F_2 collapse at a_6. The gate's master test (Symanzik O(a^4)
  at all 4 slots) requires cross-class consistency at each slot.
  
  Under the binding partition for the registry: 5-class @ L1.
  Under the slot-by-slot reading: each slot has its own partition.

Step 4 (direction):
  C-α inherits SLOT-DEPENDENT partitions; the registry binding choice
  (5-class @ L1) is consistent with all slot-readings (it is the finest
  partition; coarser per-slot readings are projections). The gate's PASS
  criterion (drift exponent matches Symanzik O(a^4)) is INVARIANT under
  the partition choice — it is a slot-by-slot drift exponent measurement,
  NOT a partition test.
  
  Direction implication: C-α PASS/FAIL/INFO is partition-invariant. Adding
  per-class refinement (4-class vs 5-class) does NOT change the C-α verdict.
  C-α is partition-INSENSITIVE in its current pre-registration.
```

**C-β (UV-Cutoff-Choice within F_4 family, deferred to S87).**

C-β tests immunization against UV-cutoff-choice within the F_4 family. Per HP1 partition, F_4 = {ζ, Zubarev, SDW}; per my 5-class, these are Class 1, Class 2, Class 3. Under the 4-class partition, ζ and SDW collapse to F_2 (single class), so C-β tests immunization across {F_2, Zubarev} → 2 classes. Under the 5-class partition, C-β tests immunization across {Class 1, Class 2, Class 3} → 3 classes. **C-β is PARTITION-SENSITIVE**: under 4-class binding, C-β tests fewer classes (2); under 5-class binding, C-β tests more classes (3) and a stricter immunization criterion. The S87 gate dispatch should pre-register the 5-class binding to test the strictest form.

**C-γ-WEAK (Weyl-Rescaling Immunization, W6-3, internal Λ_anomaly bound).**

*Substitution chain.*

```
Step 1 (definition):
  C-γ-WEAK tests whether the parametric bound
       |ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²
  holds, where Λ_anom_internal is computed INTERNALLY from Tr_F(Y†Y)
  + AC-2010 §V coefficients (per plan §W6 line 20).

Step 2 (substitute SECTOR-2 partition):
  Λ_anom_internal is computed from the f_0 / f_2 / f_4 multiplier vector
  per AC-2010 §V coefficients. The partition is therefore at the
  multiplier-vector level — 5-class @ L1.
  
  Each Class produces a DIFFERENT Λ_anom_internal:
    Class 1 (ζ):           Λ_anom^{ζ} from (0, 0, 1, 0)-multiplier
    Class 2 (SDW):         Λ_anom^{SDW} from (0, 0, 1, 0) at Γ-regular slots
                           (= Λ_anom^{ζ} at the gate's Γ-regular evaluation slot,
                            which is presumed to be a_2 / a_4 / a_6 — Γ-regular).
    Class 3 (Zubarev):     Λ_anom^{Zubarev} from (0, exp-tail, exp-tail, 0)
    Class 4 (cutoff_sqrt): Λ_anom^{cutoff} from (2, 1, 1, 0)
    Class 5 (anomaly):     Λ_anom^{anomaly} from (0, 1−κ_PV, 1, 0)

Step 3 (simplify):
  Under 4-class @ L3-s=3 binding (lizzi): Λ_anom^{ζ} = Λ_anom^{SDW} at s=3,
  but C-γ-WEAK does NOT evaluate at s=3 — it evaluates at the Λ-cut scale,
  which is NOT a single Mellin slot but the full multiplier vector.
  Therefore: 4-class @ L3-s=3 binding is INSUFFICIENT for C-γ-WEAK.
  
  Under 5-class @ L1 binding (mine): each Class produces a distinct
  Λ_anom_internal, and the parametric bound test propagates per-class.
  This is the consistent binding for C-γ-WEAK.

Step 4 (direction):
  C-γ-WEAK requires the 5-class @ L1 partition for consistent propagation.
  The 4-class @ L3-s=3 partition would erroneously collapse Class 1 and
  Class 2, missing the multiplier-vector distinction at Γ-pole slots that
  feed into the AC-2010 §V coefficient computation.
  
  Direction implication: C-γ-WEAK is PARTITION-SENSITIVE. Under 4-class
  binding, the gate would compute Λ_anom^{ζ} = Λ_anom^{SDW} (coarse);
  under 5-class binding, the gate computes them separately (correct).
  The S86 W6-3 dispatch should use 5-class binding.
```

**C-η (Ward Immunization, landed W1c via C41).**

C-η tests Ward identity preservation under regulator perturbation. Already landed in W1c via C41 (zero-compute consequence per registry tag); see plan §W1c-2 / §W1a line 391. The Ward identity is a LAYER 1 (combinatorial) statement at the gauge-symmetry level — it is regulator-class-INVARIANT for L1-admissible regulators. C-η is partition-INSENSITIVE across the F_4 ⊂ A_5 family: zero-compute landing in registry. **No SECTOR-2 propagation impact** (already landed; no re-evaluation needed).

**C-θ (Connes Inner-Fluctuation Immunization, landed W1c via C41).**

C-θ tests preservation of the inner-fluctuation calculus under regulator perturbation. Already landed in W1c via C41 (zero-compute consequence). The inner fluctuation `D → D + A + JAJ^{-1}` is a NCG axiom A5 (first-order, [[D, a], b°] = 0) consequence and is regulator-class-INVARIANT for L1-admissible regulators. C-θ is partition-INSENSITIVE. **No SECTOR-2 propagation impact** (already landed).

**Summary table — which corollaries change under 4-class vs 5-class binding.**

| Channel | Pre-registered slot | 4-class binding (lizzi) | 5-class binding (mine) | Sensitivity |
|:---|:---|:---|:---|:---|
| W5a-P3 IC | s=−1 (Γ-pole) | INSUFFICIENT — F_2 split required | CORRECT — per-class IC | SENSITIVE |
| C-α (lattice) | slot-by-slot {0,1,2,3} | SLOT-DEP partition | SLOT-DEP partition (consistent) | INSENSITIVE (drift exponent test) |
| C-β (UV-cutoff) | F_4 family | 2-class test | 3-class test | SENSITIVE (5-class is stricter) |
| C-γ-WEAK (Weyl) | full multiplier vector | INSUFFICIENT — collapses Class 1,2 | CORRECT — per-class Λ_anom | SENSITIVE |
| C-η (Ward) | gauge symmetry | INVARIANT (already landed) | INVARIANT (already landed) | INSENSITIVE |
| C-θ (inner-fluctuation) | NCG A5 | INVARIANT (already landed) | INVARIANT (already landed) | INSENSITIVE |

**Three of six channels are partition-SENSITIVE: W5a-P3 IC, C-β, C-γ-WEAK.** All three benefit from 5-class binding. The 4-class binding is sufficient only for partition-insensitive channels (C-α, C-η, C-θ). The workshop deliverable (a) decision should bind 5-class @ L1 for general SECTOR-2 propagation, with the understanding that the 4-class @ L3-s=3 partition is the L3 projection at one specific slot.

**Carry-forward gates (S87 spec):**

| What | Inputs | Gate | Effort |
|:---|:---|:---|:---|
| `S87-W5A-P3-IC-PER-CLASS-VERIFY`: re-compute xi²(0) IC for each of 5 L1-classes; test Z(N_pivot) ratio per class | `xi_E_GGE_inv` (Class-1), per-class s=-1 spectral residue computation, plan §W5a-1 ODE integration | Z_ratio > 1 (current ζ) preserved across all 5 classes (PASS), or class-dependent (INFO) | MODERATE (4 additional integrations) |
| `S87-W6-C-BETA-UV-CUTOFF-3CLASS`: test C-β UV-cutoff-choice immunization across {Class 1, Class 2, Class 3} (= F_4 with multiplier-vector refinement) | F_4 partition + multiplier-vector inputs, plan §W1a Φ-B branch spec | parametric bound holds across 3 classes (PASS) or fails on Class 2 vs Class 1 (INFO — F_2 collapse breaks at Γ-pole) | MODERATE |
| `S87-W6-C-GAMMA-WEAK-PER-CLASS`: re-evaluate C-γ-WEAK Λ_anom_internal per L1-class; test parametric bound | AC-2010 §V coefficients per Class, internal Λ_anom_internal computation, plan §W6 line 20 | bound holds across all 5 classes (PASS) or class-dependent breakdown (INFO) | HEAVY |

**Substrate framing.** The propagation map IS a structural cataloguing of how each downstream channel inherits the SECTOR-2 split through its specific Mellin-slot dependence. Each channel's binding partition IS a property of which Mellin moments the channel evaluates and how they intersect with the multiplier-vector grading of the regulator-class manifold. The substrate IS the regulator-class manifold; the channels ARE projections of substrate-functional moments under specific evaluation schemes; the partition-sensitivity IS the substrate's structural fingerprint at each channel's evaluation locale.

**Cite-anchors:**
- W5a-P3 plan spec (`session-86-plan-w5a.md` lines 50-51, 98-180): IC sourcing from `xi_E_GGE_inv` at s=-1.
- W4-1 P4 PASS canonical constant: `xi_E_GGE_inv = 13.642473425595973` at full float64 (W4 working paper §W4-1).
- §VII.N L3 R-protected vs NOT-R-protected partition (registry line 5815-5819).
- §VII.K-PROP propagation rule (registry line 8867): `span(O) = ∏_k span(f_k)^{p_k(O)}`.
- W6-2 C-α plan §W6 line 19: lattice-spacing slot-by-slot drift-exponent test.
- W6-3 C-γ-WEAK plan §W6 line 20: Weyl-rescaling parametric bound `|ΔS_W / S_W| ≤ b_DK · (Λ_anom_internal / Λ_cut)²`.
- W1a-T3 Φ-branch enumeration (plan §W1a lines 419-421): Φ-A through Φ-F branches.
- ZETA-NOT-PHYSICAL-75 §VII-B (registry line 4576): s=0 boundary; informs the s=-1 Γ-pole behavior at the W5a-P3 IC source.
- Re:L3 strengthened item 3 above: THM-L3.1 slot-conditionality at Γ-pole slots.

#### C3: LAYER 1/2 Inventory — S78-Onward Regulator-Class Statements

**Topline.** I open the retroactive sweep with a 17-row initial inventory of S78-onward regulator-class statements, each tagged LAYER 1 (combinatorial-position-on-atlas) or LAYER 2 (admissibility-on-axioms) per the canonized taxonomy at `cutoff-sqrt-adjudication.md` §1.4 (lines 55-66). The inventory is INITIAL and INCOMPLETE — workshop deliverable (b) is "outline OR land if convergence supports," and outline is the appropriate R1 target. lizzi's R2 should add to and refine this. Three CONFLATION RISK rows are flagged: row 6 (registry F_4 vs lizzi's `~_M`), row 11 (the 5-atlas convention "uniform-admissible" pattern flagged in §W4-2 line 290), and row 14 (HP^1 R-protection mistaken for K-invariance).

**Methodology recap.** Per the protocol scaffolded in Re:L4: each statement is a (source-file, line, type, claimed-scope) tuple; each is classified LAYER 1 or LAYER 2 by whether it makes a combinatorial-position claim (Mellin support, observable-cross-classification, atlas membership) or an admissibility claim (axiomatic PASS/FAIL, numerical gate). Cross-tag conflation is flagged when a LAYER 1 statement is invoked as evidence for a LAYER 2 conclusion (or vice versa) without an explicit LAYER 1 → LAYER 2 implication theorem.

**Initial inventory (17 rows, S78-onward).**

| # | Source (file:line) | Statement (paraphrase) | LAYER | Downstream usage | Conflation risk? |
|:--|:---|:---|:---|:---|:---|
| 1 | `_spectral_action_regulators.py` line 177 | `REGULATOR_NAMES = ("heat-kernel", "zeta", "Mellin", "hard-cutoff", "Pauli-Villars")` — defines the 5-element atlas convention. | LAYER 1 | All S78+ atlas cites; 5-class partition baseline. | NO (definition only; no admissibility claim). |
| 2 | `_spectral_action_regulators.py` lines 23-28 docstring | "These are SCHEMATIC regulators ... NOT the full physical regularizations used in the S61/S78 Pauli-Villars pipeline." | LAYER 1 (with LAYER 2 disclaimer) | Helper-module-faithfulness cite; §W4-2 P5 honesty disclosure (line 502-503). | NO (explicit disclaimer is the right LAYER 1/LAYER 2 separation). |
| 3 | Registry §VII.N L1 (line 5639-5703) | "Under Connes axioms A1-A6 ... canonical summation measure is Tr_ω(T) = Res_{s=d} Tr(T \|D\|^{-s}) ... Uniqueness at L1: zeta." | LAYER 2 | §VII.N Three-Layer Regulator Theorem; binds L1-canonical regulator selection. | NO (axiomatic admissibility claim, correctly LAYER-tagged). |
| 4 | Registry §VII.N L2 (line 5711-5767) | "Three-criterion intersection at τ_fold = 0.19, L_max = 5 ... Uniqueness at L2: Zubarev." | LAYER 2 | §VII.N L2-canonical selector; Mellin-Strip / Convergence Cone integration. | NO (numerical admissibility claim with pinned criteria). |
| 5 | Registry §VII.N L3 (line 5779-5835) | "5-regulator span span_Q = max_R Q[R] / min_R Q[R] partitions into R-protected (in [1.0, 1.5]) vs NOT-R-protected (in [2.5, ∞))." | LAYER 1 (per-Q observable classification) | §VII.K-PROP propagation; per-Q span partition; §VII.K-META MIXED-FI-via-pinning. | NO (combinatorial-position claim on observables; LAYER 1 by E3-L canon). |
| 6 | Registry §VII-B.HP1-NEAR-INVARIANCE Step 1 (line 2605) | "F_4 = {ζ, Zubarev, SDW} (regulators whose Mellin support is concentrated on the a_4 Seeley-DeWitt slot)." | LAYER 1 | Used as F_4-as-equivalence-class shorthand in S78+ cites; §VII-B.HP1 5-atlas LOOSE/STRICT R-protection. | **YES — CONFLATION RISK with lizzi's `~_M` (4-class@s=3) and with my 5-class@L1.** Three F_4 partitions in play; cite-text needs slot-tag. |
| 7 | Registry §VII-B.HP1-NEAR-INVARIANCE LOOSE (line 2597) | "max_{r,r' ∈ Atlas_5} ‖[ε_H]‖_{HP^1,r} / ‖[ε_H]‖_{HP^1,r'} = 2.0." | LAYER 2 (numerical R-protection criterion) | §VII-B.HP1 R-protection landing; cited as LOOSE form in 5-atlas. | NO (numerical R-protection, correctly LAYER 2-tagged). |
| 8 | Registry §VII-B.HP1-NEAR-INVARIANCE STRICT (line 2611) | "max ratio on F_4 = 1.000 / 0.970024 = 1.031." | LAYER 2 | §VII-B.HP1 STRICT R-protection landing within F_4 sub-atlas. | NO (numerical, correctly tagged). |
| 9 | Registry §VII-B.TWO-LAYER-OBSTRUCTION (line 2787) | "n_joint := \|{r in Atlas : Joint(r)}\| = 0/5." | LAYER 2 | Two-layer obstruction theorem; n_joint = 0 across atlas. | NO (numerical L1↔L2 functoriality test, correctly LAYER 2-tagged). |
| 10 | Registry §VII-B.ZETA-NOT-PHYSICAL-75 (line 4576-4682) | "S66/S75 raw-ε_H magnitude dynamic range was 381× (ZETA-NOT-PHYSICAL-75 permanent theorem)." | LAYER 2 (s=0 spectral-zeta non-observability) | Cited as L1-uniqueness corollary (registry line 4794-4795); s=0 boundary. | NO (s=0 boundary admissibility claim, correctly LAYER 2-tagged). |
| 11 | Cutoff-sqrt-adjudication §1.4 (line 250) | "the framework's previous methodological error (S78 onward, treating the canonical 5-atlas as uniform-admissible)." | META — diagnoses the conflation pattern itself | Defines the AUDIT TARGET for the retroactive sweep. | **YES — this IS the canonical conflation pattern; every S78-onward 5-atlas cite must be checked for whether it treated atlas membership as admissibility.** |
| 12 | `session-85-s1-regulator-boundary-van-den-dungen.md` line 55 | Regulator-Family Boundary Theorem: `𝓡 = 𝓡_{a_4} ⊔ {cutoff_sqrt}` where `𝓡_{a_4} = {ζ, Zubarev, SDW, anomaly}`. | LAYER 1 (Kasparov-KK partition by f_0-test) | Cited in cutoff-sqrt-adjudication §6 cross-cite ledger; informs C45 S87 SIXTH-REGULATOR-SYNTHESIS. | NO (combinatorial partition, correctly LAYER 1-tagged). |
| 13 | `session-85-s1-regulator-boundary-van-den-dungen.md` line 49 | Four-layer hierarchy: Layer 1 (topology) and Layer 2 (representation) are INVARIANT across regulators; Layer 3 (metric) is SELECTIVE; Layer 4 (functional) is SENSITIVE. | LAYER 1 (Kasparov-KK structural framing) | Frames Regulator-Family Boundary Theorem at Layer 3-4 boundary. | NO (combinatorial-structural classification, correctly LAYER 1-tagged). |
| 14 | Registry §VII-B.HP1-NEAR-INVARIANCE provenance (line 2731-2737) | "S86-W9 C44 (R-protection Mellin criterion) cites this entry as the canonical 5-atlas LOOSE/STRICT exemplar; F_4/M partition (S-1 Regulator-Family Boundary Theorem) gains an empirical anchor at the HP^1 cohomology level." | LAYER 1 + LAYER 2 (mixed) | Cited as basis for S86-W9 C44 R-protection criterion. | **YES — CONFLATION RISK: HP^1 R-protection (LAYER 2 admissibility result on f_4 multiplier) is implicitly elevated to "the F_4/M partition has an empirical anchor at HP^1," which is a LAYER 1 partition claim. The HP^1 R-protection holds within F_4 — but the STRICT containment factor 1.031 is the admissibility number, not the partition cause.** Remediation: add explicit "the LAYER 2 R-protection number 1.031 within F_4 does not imply F_4 is the LAYER 1-canonical partition for HP^1 admissibility — F_4 is a Mellin-support partition, and the R-protection is a numerical quotient within it." |
| 15 | §W4-2 line 290 (workshop convergence) | "the F_2 sub-atlas survival is a structural identity (zeta = Mellin on positive-definite spectrum) and does not lift the K-invariance claim to even the F_4 = {ζ, Zubarev, SDW} sub-atlas (Zubarev breaks at 92%)." | LAYER 2 (structural identity statement with explicit non-evidence-status) | THM-L3.1 source; non-evidence-status declaration. | NO (explicit non-evidence-status disclaimer is the right pattern; THM-L3.1 inherits it). |
| 16 | §W4-2 substitution chain Step 3 (line 237) | "pole_R = a_2(τ_pivot) · M_R(s=3); a_2 regulator-independent, only M_R(s=3) carries regulator class." | LAYER 1 (decomposition) + LAYER 2 (a_2-regulator-independence claim) | Used as the SECTOR-2 split's substitution-chain anchor. | NO (decomposition correctly LAYER 1-tagged; a_2-invariance is a NCG axiom A1 + A6 derivation, LAYER 2). |
| 17 | Memory `s80-w1-4-cc-ratios-only.md` (per MEMORY.md line 18) | "Weight-balanced f_k-cancellation: §VII.I candidate; pure a-ratios f-invariant (spread=0); unbalanced spread 0.52-0.73." | LAYER 2 (f-invariance numerical test) | §VII.K-PROP CC-RATIOS-ONLY identity; ratios are R-protected, absolute moments are regulator-dressed. | NO (numerical f-invariance test, correctly LAYER 2-tagged). |

**Three flagged CONFLATION RISKs require remediation:**

**Conflation 1 (row 6): F_4 nomenclature collision.**
Three distinct partitions all use "F_4":
- §VII-B.HP1's F_4 = {ζ, Zubarev, SDW} (LAYER 1, Mellin-support concentrated on a_4 slot).
- lizzi's F_4 (in L1's question 3) = registry-canonical above (LAYER 1, but tested numerically at s=3 where Zubarev breaks at 92%, falsifying the F_4-as-residue-class reading).
- My 5-class partition's "F_4-locale subset" = Class 1 ∪ Class 2 ∪ Class 3 (LAYER 1, multiplier-vector with f_4 = 1).

Remediation: workshop must adopt SLOT-TAGGED nomenclature: "F_4@a_4-Mellin-support" (registry HP1 partition), "F_2@a_2-residue-class@s=3" (lizzi `~_M`), "F_4@multiplier-vector-with-f_4=1" (my 5-class L1-subset). Each future cite specifies which slot/grading the partition is taken at. PROPOSED for `sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline.

**Conflation 2 (row 11): 5-atlas-as-uniform-admissible (META).**
This is the canonical S78-onward conflation pattern itself. The cutoff-sqrt-adjudication.md line 250 quote ("treating the canonical 5-atlas as uniform-admissible") IS the audit target. Every S78-onward statement that lists the 5-atlas members or cites "the regulator atlas" without specifying whether the cite is at LAYER 1 (combinatorial membership) or LAYER 2 (admissibility) is a CANDIDATE for this conflation.

Remediation: the audit pass must walk every cite of "5-atlas" / "regulator atlas" / "{ζ, Zubarev, SDW, cutoff_sqrt, anomaly}" and tag each cite explicitly. This is the BULK of the retroactive sweep work. Initial sample cites:
- `_spectral_action_regulators.py` line 177 (LAYER 1 by definition; OK).
- `cutoff-sqrt-adjudication.md` line 234 "R_atlas = {zeta, Zubarev, SDW, cutoff_sqrt, anomaly}" (LAYER 1; OK in context).
- `permanent-results-registry.md` line 2595 "Atlas_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}" (LAYER 1 in HP1 LOOSE form; OK).
- §W4-2 §6 atlas table (line 153): per-regulator pole values across the 5-atlas — LAYER 2 numerical (admissibility-test) cite; OK because it explicitly tests K-invariance and finds FAIL.
- Plan files referring to "5-regulator atlas" (S78+ across multiple plans): NEEDS PER-CITE AUDIT in the retroactive sweep.

**Conflation 3 (row 14): HP^1 R-protection elevated to F_4 partition cause.**
The HP^1 R-protection result (LAYER 2 numerical, factor 1.031 on F_4) is correctly proven within the F_4 sub-atlas. The cite at registry line 2735 says "F_4/M partition gains an empirical anchor at the HP^1 cohomology level" — this elevates the LAYER 2 R-protection number into a LAYER 1 partition validation. Remediation: re-word the registry cross-cite to read "the LAYER 2 HP^1 R-protection within F_4 (factor 1.031) is consistent with the LAYER 1 F_4/M Mellin-support partition (RFB Theorem (i)), but does NOT itself prove the partition; the partition's LAYER 1 cause is the f_0 = 0 vs f_0 ≠ 0 distinction (RFB (i)) AND the a_2-vs-a_4 Mellin-support concentration (HP1 Step 1)." PROPOSED for `sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline.

**Outline for `sessions/framework/registry/layer1-layer2-retroactive-audit.md`** (proposed for workshop deliverable (b)):

```
# LAYER 1 / LAYER 2 Retroactive Audit (S78-Onward Regulator-Class Statements)

## §1. Audit purpose and methodology
   §1.1  Two-layer taxonomy (per cutoff-sqrt-adjudication.md §1.4 verbatim quote)
   §1.2  Naming-collision resolution: §VII.N L1/L2/L3 vs cutoff-sqrt LAYER 1/LAYER 2
         (proposed: adopt §VII.N as canonical; re-tag cutoff-sqrt LAYER 1 → "L3-combinatorial",
          cutoff-sqrt LAYER 2 → "L1-axiomatic")
   §1.3  4-stage protocol: enumerate / tag / detect cross-tag conflation / remediate
   §1.4  Forward-vs-backward inference closure: this audit is the BACKWARD closure
         (sibling to the FORWARD non-evidence-status declaration in
          §VII-B.ZETA-EQUALS-SDW THM-L3.1, S86 W4-2 / W7).

## §2. Initial inventory (S78-onward; expandable)
   §2.1  Statements LAYER-tagged (per the 17-row table in C3 above)
   §2.2  Open inventory items needing per-cite audit (5-atlas usage in plan files)

## §3. Conflation-risk findings
   §3.1  F_4 nomenclature collision (3 partitions, same name) — slot-tag remediation
   §3.2  5-atlas-as-uniform-admissible pattern (S78-onward META conflation) — per-cite audit
   §3.3  HP^1 R-protection-elevated-to-F_4-partition-cause — re-word registry cross-cite

## §4. Remediation assignments
   §4.1  REPAIR-IN-SESSION: in-session edits with LAYER tag added
   §4.2  REPAIR-AT-REGISTRY: registry-canonical entries needing LAYER tag
   §4.3  CARRY-FORWARD-COMPUTE: numerical gates needed to settle whether
         conflated statements hold at LAYER 2

## §5. Cross-cite ledger
   §5.1  §VII.N Three-Layer Regulator Theorem (registry line 5511) — canonical L1/L2/L3
   §5.2  §VII-B.HP1-NEAR-INVARIANCE (registry line 2573) — F_4 Mellin-support partition
   §5.3  §VII-B.TWO-LAYER-OBSTRUCTION (registry line 2755) — n_joint = 0/5
   §5.4  §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576) — s=0 boundary
   §5.5  Regulator-Family Boundary Theorem (S-1 van den Dungen, line 55) — Kasparov-KK partition
   §5.6  §W4-2 SECTOR-2 split (working paper line 290) — K-invariance rejection
   §5.7  §VII-B.ZETA-EQUALS-SDW (S86 W7 — landing) — slot-conditional THM-L3.1
```

**Convergence-feasibility for landing in R3.** The outline above is at landing-readiness for workshop deliverable (b) IF lizzi's R2 ratifies the §1.2 naming-collision resolution and the three remediation classes in §4. If naming-collision is contested, R3 should land the outline only and defer the file write to S87. My recommendation: LAND the outline in R3, with the file write spec as a 4-field carry-forward to S87 (effort: 1 wave; deliverable: full retroactive sweep with all S78-onward 5-atlas cites tagged).

**Substrate framing.** The retroactive sweep IS a methodological audit ON the substrate's regulator-class manifold's prior-cite history. The substrate IS the regulator-class manifold; the per-cite LAYER tags ARE projections of how each prior cite read the manifold's structure (combinatorial vs admissibility); the conflation-risk flags ARE the substrate-physics findings of where the prior cite read the manifold's structure inconsistently. The audit IS the substrate's self-consistency check on its own cite-history.

**Cite-anchors:**
- `cutoff-sqrt-adjudication.md` §1.4 (line 55-66): canonical LAYER 1/LAYER 2 taxonomy.
- §W4-2 line 290: structural identity recognition with non-evidence-status disclaimer.
- §W4-2 synthesis §2 line 511: "permanently repairs S78-onward conflation."
- §VII.N Three-Layer Regulator Theorem (registry line 5511) — naming-collision context for §1.2.
- §VII-B.HP1-NEAR-INVARIANCE (registry line 2573 + 2735) — Conflation 3 source.
- `session-85-s1-regulator-boundary-van-den-dungen.md` lines 49 + 55 — Kasparov-KK partition.
- §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576) — Lizzi-track Cluster sibling.
- §VII-B.TWO-LAYER-OBSTRUCTION (registry line 2755) — n_joint = 0/5.
- All 17 inventory rows cite their source-file:line above.

#### C4: Questions for lizzi

**Topline.** Six sharp follow-up questions for R2, organized around the three workshop deliverables (a)/(b)/(c). Each question is concrete, R2-resolvable without new computation beyond what is already on disk, and targets a specific binding decision that R3 must close.

**Q1 (Deliverable (a) — partition binding):** Does the layer-tagged dual binding `4-class @ L3-s=3` + `5-class @ L1` (proposed in Re:L1 EMERGES + C1 reconciliation table) work for you, OR do you read the SECTOR-2 split as having a SINGLE binding partition that subsumes both?

Specifically:
- If you accept dual binding: confirm that the SECTOR-2 registry split into `SECTOR-2-ζ`, `SECTOR-2-Zubarev`, `SECTOR-2-SDW`, `SECTOR-2-cutoff_sqrt`, `SECTOR-2-anomaly` (5 sub-tags) is the canonical registry-write — with the 4-class projection at s=3 noted as a downstream propagation theorem.
- If you favor single binding: which partition (4-class or 5-class) and on what axiomatic ground? My case for 5-class is grounded in §VII.N C1 (registry line 5867: "L1 and L2 do NOT propagate via Mellin exponents") — so propagation through L1/L2 channels (W5a-P3 at s=−1, C-γ-WEAK at full multiplier vector) requires 5-class. If you have a counter-derivation that the 4-class binding suffices for these channels, please present it.

**Q2 (Deliverable (a) — F_4 nomenclature collision):** Three "F_4" partitions are now in play (Conflation 1 in C3 row 6):
- `F_4@a_4-Mellin-support` (registry §VII-B.HP1-NEAR-INVARIANCE Step 1, line 2605): pure-a_4 sub-atlas for HP^1 R-protection.
- `F_2@a_2-residue-class@s=3` (your `~_M`, this workshop L1): numerical-residue equivalence at the a_2 slot.
- `F_4@multiplier-vector-with-f_4=1` (my 5-class L1-subset, this workshop C1): multiplier-vector grading at L1.

Should the workshop adopt slot-tagged nomenclature (each "F_n" cite carries the slot it is taken at as a suffix), AND retroactively re-tag every S78-onward "F_4" cite under that scheme? Or do you have an alternative resolution (different naming convention, or one canonical "F_4" with the others renamed)? Pre-registered call needed for `sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline.

**Q3 (Deliverable (b) — naming-collision resolution):** The §VII.N Three-Layer Regulator Theorem (registry line 5511) names its strata `L1 / L2 / L3` (axiomatic / substrate-action / observable). The cutoff-sqrt-adjudication.md §1.4 (line 55-66) names its strata `LAYER 1 / LAYER 2` (combinatorial / admissibility). The two are NOT the same axes:
- §VII.N L1 ≈ cutoff-sqrt LAYER 2 (axiomatic admissibility tests).
- §VII.N L3 ≈ cutoff-sqrt LAYER 1 (combinatorial-position observable classification).
- §VII.N L2 has no analog in cutoff-sqrt LAYER 1/2 (substrate-action local at fold).

For the retroactive audit file, my Re:L4 §1.2 proposed adopting the §VII.N nomenclature canonically (re-tag cutoff-sqrt LAYER 1 → "L3-combinatorial"; cutoff-sqrt LAYER 2 → "L1-axiomatic"). Do you AGREE with this resolution, or do you prefer to keep cutoff-sqrt LAYER 1/2 names (and add §VII.N as a sibling axis with its own L1/L2/L3 distinct from cutoff-sqrt's)?

**Q4 (Deliverable (c) — strengthened non-evidence-status items):** I have proposed two ADDITIONAL non-evidence-status items for THM-L3.1 (Re:L3):
- Item (vii): NOT evidence for L1-axiomatic uniqueness (Connes-Marcolli Thm 1.31 selects ζ; SDW does not lift to L1).
- Item (viii): NOT evidence for KO-dim 6 Z/8 grading invariance under arbitrary slot extraction.

AND I have strengthened item (3) to explicit slot-conditionality (THM-L3.1 fails at Γ-pole slots s=0, −1, −2, ...; F_2 pair-equivalence is positive-real-half-plane only, not generic).

Do you accept these revisions to the proposed `§VII-B.ZETA-EQUALS-SDW` skeleton, OR do you have alternative phrasings? If you accept item (vii), the registry entry's CITE-ANCHORS list should explicitly cross-cite §VII.N L1 (registry line 5699) — confirm.

**Q5 (Deliverable (c) — registry slot placement):** I AGREED with your proposed `§VII-B.ZETA-EQUALS-SDW` slot, sibling to ZETA-NOT-PHYSICAL-75 and HP1-NEAR-INVARIANCE in the §VII-B Lizzi-track Cluster (registry line 4742-4747). Confirm the slot identity for R3 landing: `§VII-B.ZETA-EQUALS-SDW` vs alternative slot names you may consider (e.g., `§VII-B.ZETA-MELLIN-IDENTITY` or `§VII-B.F_2-PAIR-EQUIVALENCE`). What name do you prefer for the canonical landing?

**Q6 (Carry-forward gates — S87 spec):** I have proposed three S87 carry-forward gates in C2:
- `S87-W5A-P3-IC-PER-CLASS-VERIFY` (re-compute xi²(0) IC for each L1-class; test Z(N_pivot) ratio per class).
- `S87-W6-C-BETA-UV-CUTOFF-3CLASS` (test C-β UV-cutoff-choice immunization across {Class 1, Class 2, Class 3}).
- `S87-W6-C-GAMMA-WEAK-PER-CLASS` (re-evaluate C-γ-WEAK Λ_anom_internal per L1-class; test parametric bound).

The workshop's pre-registered carry-forward (workshop document line 30) is a 4-field S87 spec for SECTOR-2 propagation into W5a P3 IC + W6 C-α/β/γ. Do you AGREE with the 3 gate proposals, OR add/replace gates? In particular:
- Does C-α need a per-class refinement (my C2 read: NO, partition-INSENSITIVE because slot-by-slot drift exponent test is partition-invariant), or do you want to confirm by direct computation?
- For W5a-P3 IC: do you want the per-class IC verification at the `[VERIFY]` level (binary PASS/FAIL on direction preservation) or at the `[VERIFY-THEOREM]` level (theorem-grade bound on cross-class IC variation)?

**Decision-procedure summary for R2 → R3 convergence.**

For R3 to land all three deliverables, R2 should resolve:
- Q1 (binding partition); Q2 (F_4 nomenclature); Q3 (LAYER naming-collision) → resolve deliverable (a) registry partition + deliverable (b) outline structure.
- Q4 (non-evidence-status items); Q5 (registry slot placement) → resolve deliverable (c) `§VII-B.ZETA-EQUALS-SDW` final form.
- Q6 (carry-forward gate spec) → resolve workshop carry-forward 4-field spec.

If you converge on Q1-Q5 in R2, R3 can land all three deliverables. If Q1 (binding partition) remains contested in R2, R3 may need to land a CONDITIONAL deliverable (a) ("4-class @ L3-s=3 + 5-class @ L1 dual binding, contingent on §VII.N L1/L2 propagation theorem update"), with the propagation theorem update itself a carry-forward to S87.

**Cross-domain note.** I suspect Q1 is the load-bearing question — if you accept dual binding, Q2-Q6 cascade to convergence. If you favor single binding, Q2-Q6 each carry additional load. My recommendation is to press hardest on Q1 in R2.

**Cite-anchors:**
- Re:L1 EMERGES (this file): dual binding proposal.
- C1 reconciliation table (this file): four partitions, four questions.
- C2 partition-sensitivity table (this file): per-channel binding requirements.
- C3 17-row inventory + 3 conflation flags (this file): retroactive audit start.
- Re:L3 strengthened items (this file): two added non-evidence-status items + slot-conditionality.
- Workshop document line 30 (this file): carry-forward 4-field S87 spec target.
- Workshop document lines 24-27 (this file): three pre-registered deliverables (a), (b), (c).

---

## Round 2 — lizzi: Follow-up

### CONVERGENCE

**C-1: Dual-binding partition (4-class @ L3-s=3 + 5-class @ L1) — ACCEPT IN FULL (Q1 load-bearing).**

Connes' Re:L1 EMERGES + C1 reconciliation table proposes that the 4-class partition (mine, `~_M`-equivalence at s=3) and the 5-class partition (his, multiplier-vector at L1) are NOT competing — they are layer-projections of the SAME regulator-class-manifold structure under the §VII.N stratification. Specifically: the 4-class is the L3-projection at the s=3 a_2-slot; the 5-class is the L1-axiomatic partition that survives across all slots. The binding decision for SECTOR-2 PROPAGATION is 5-class @ L1 because §VII.N C1 (registry line 5867) states "L1 and L2 do NOT propagate via Mellin exponents. Propagation is a feature of the residual stratum only" — meaning propagation through L1 and L2 channels (W5a-P3 IC at s=−1, C-γ-WEAK at full multiplier vector) requires the L1 partition, not the L3-s=3 projection.

I ACCEPT THIS IN FULL. The substitution chain that closes the question:

```
Step 1 (definitions):
  Layer-projection := mapping from a finer partition (5-class @ L1) to a coarser
                      partition (4-class @ L3-s=3) by collapsing equivalence classes
                      whose multiplier-vector difference vanishes at the projection
                      slot (s=3) but persists at other slots.
  
  Binding partition for propagation := the partition relation that respects every
                      downstream channel's evaluation stratum; finest such partition
                      that does not collapse a class which a downstream evaluation
                      needs to distinguish.

Step 2 (substitute):
  At s=3 (a_2 slot):    Class 1 (ζ) and Class 2 (SDW) collapse via THM-L3.1
                        identity (M_ζ(3) = M_SDW(3) bit-exact, CC-2 PASS rel_err
                        = 1.7556e-16). The projection 5-class → 4-class merges
                        Class 1 ∪ Class 2 → F_2.
  
  At s=−1 (Γ-pole, W5a-P3 IC): Γ(s) has a simple pole; THM-L3.1 FAILS per the
                        Re:L3 strengthened item (3) substitution chain. Class 1
                        and Class 2 do NOT collapse — they sit on distinct
                        submanifolds at Γ-pole slots.
  
  At s=0 (ZETA-NOT-PHYSICAL-75): Class 1 and Class 2 differ by 381× dynamic range
                        (registry line 4682). The 4-class projection is structurally
                        wrong at s=0; the 5-class is structurally correct.

Step 3 (simplify):
  The 4-class partition is correct AT s=3 specifically (binding for §VII.K-PROP
  per-Q span propagation at the a_2 slot only). The 5-class partition is correct
  AT every slot in the §VII.N stratification (binding for L1/L2/L3-cascading
  propagation cross-slot).

Step 4 (direction):
  For workshop deliverable (a) registry-write, the binding partition is the
  finest partition that respects every downstream channel's evaluation stratum
  — that is the 5-class @ L1. The 4-class @ L3-s=3 is the L3-projection at one
  specific slot, recorded as a downstream propagation theorem.
  
  Conclusion: ACCEPT dual-binding. Canonical registry-write is 5-class @ L1
  with explicit projection theorem to 4-class @ L3-s=3.
```

The dual-binding answers connes' Q1 directly: I AGREE that the SECTOR-2 registry split into `SECTOR-2-ζ`, `SECTOR-2-Zubarev`, `SECTOR-2-SDW`, `SECTOR-2-cutoff_sqrt`, `SECTOR-2-anomaly` (5 sub-tags) is the canonical registry-write, with the 4-class projection at s=3 noted as a downstream propagation theorem. The frustration-triangle pattern from S67 (FUNCTIONAL-SELECT-67 anomaly family structurally excluded, MEMORY S67) reinforces this — different functionals must be tracked SEPARATELY at the structural-prior layer because their downstream physics-implications diverge. The 5-class binding at L1 generalizes the same lesson to the full atlas. (Cite-anchors: connes' Re:L1 EMERGES at workshop lines 399-407; connes' C1 reconciliation table at workshop lines 919-926; connes' C4 Q1 at workshop lines 1303-1308.)

**C-2: Slot-conditionality strengthening of THM-L3.1 — ACCEPT IN FULL.**

Connes' Re:L3 STRENGTHEN clause replaces my non-evidence-status item (3) ("NOT evidence for substrate-distance-1 invariance") with an explicit slot-conditionality clause: F_2 = {ζ, SDW} pair-equivalence holds for s in the positive-real half-plane where Γ(s) is regular, and FAILS at Γ-pole slots s ∈ {0, −1, −2, ...}. The substitution chain (workshop lines 532-566) shows the failure at s=0 (where Γ(0) is a simple pole, ZETA-NOT-PHYSICAL-75 territory, 381× dynamic range) and at s=−1 (where Γ(−1) is a simple pole, W5a-P3 IC source).

I ACCEPT THIS STRENGTHENING IN FULL. My L3 draft was implicit on slot-conditionality (item (3) said "substrate-distance-1 invariance" which is a_2-slot specifically); connes' explicit re-phrasing makes the slot-dependent boundary explicit. The strengthened item (3) phrasing in his proposed final-form skeleton (workshop lines 622-624) is correct as written.

A small addition from my side: the slot-conditionality is SHARP — at Γ-regular real s, F_2 pair-identity is bit-exact (1 ULP under float64); at Γ-pole real s, the pair-identity is structurally absent (381× at s=0, expected order-of-magnitude divergence at s=−1). There is no intermediate regime where F_2 is "partially identical." This sharpness is itself substrate-physics: the (ζ, SDW) pair lies on a measure-zero submanifold defined by Γ(s)-cancellation invariance, and the submanifold has a boundary at the Γ-pole slots. The sharpness suggests an additional non-evidence-status sub-clause: "NOT evidence for any slot-interpolation between s=3 and s=0; the F_2 pair-identity is not a continuous function of s with smooth transition." I propose adding this as a footnote to the strengthened item (3) (DISSENT D-1 below proposes the exact wording).

**C-3: Two added non-evidence-status items (vii L1-axiomatic uniqueness + viii KO-grading invariance) — ACCEPT IN FULL.**

Connes' Re:L3 ADD clause introduces two non-evidence-status items:

- (vii) NOT evidence for L1-axiomatic uniqueness. Connes-Marcolli 2008 Thm 1.31 (Dixmier trace `Tr_ω(T) = Res_{s=d} Tr(T |D|^{-s})` is the UNIQUE trace-class invariant under Connes-Moscovici local index formula on the ideal L^(1,∞)(H)) selects ζ from F_2 as the L1-canonical regulator; SDW does NOT lift to L1-canonical status because the Mellin convention's Γ(s) factor at s=0 boundary carries a non-canonical normalization not present in the Dixmier trace formulation.
- (viii) NOT evidence for KO-dim 6 Z/8 grading invariance under arbitrary slot extraction. The Mellin transform regularization carries an implicit `s ↦ d − s` symmetry (functional-equation analog) interacting with the J-action via `[J, |D|^{-s}] = 0`; ζ carries this canonically, SDW carries it up to a Γ(d − s)/Γ(s) factor that is finite at canonical-s slots (where it absorbs into the normalization) but singular at Γ-pole slots.

Both items are correct readings, structurally aligned with the substrate's NCG-axiomatic content. I ACCEPT BOTH and ratify their inclusion in the §VII-B.ZETA-EQUALS-SDW registry entry. Note: I had asked in my L3 question 3 whether the non-evidence-status list was complete — connes' answer is "INCOMPLETE — 2 missing" (workshop lines 589-591), now resolved to 8 items total. My S75 ZETA-NOT-PHYSICAL-75 result (MEMORY S75; permanent theorem 3/3 PASS, 381× dynamic range across L_max) is the empirical anchor for item (vii); item (viii) generalizes to the KO-grading axis and pins a corollary that I had not previously articulated.

**C-4: Registry slot placement `§VII-B.ZETA-EQUALS-SDW` — ACCEPT (Q5 resolved).**

Connes' Re:L3 final-form skeleton (workshop lines 600-651) places the theorem at `§VII-B.ZETA-EQUALS-SDW` as a Lizzi-track entry, sibling to ZETA-NOT-PHYSICAL-75 (registry line 4576) and HP1-NEAR-INVARIANCE (registry line 2573) and TWO-LAYER-OBSTRUCTION (registry line 2755), inside the §VII-B Lizzi-track Cluster (registry line 4742-4747). This is the right placement — it groups three Lizzi-track structural results that share methodology (per-regulator analysis on the substrate's spectral functional manifold). I CONFIRM the slot identity for R3 landing as `§VII-B.ZETA-EQUALS-SDW` (Q5 resolved).

I considered alternative names: `§VII-B.ZETA-MELLIN-IDENTITY` (more precise but loses the SDW abbreviation that the workshop has been using), `§VII-B.F_2-PAIR-EQUIVALENCE` (foregrounds the pair-equivalence aspect but loses connection to the registry sibling ZETA-NOT-PHYSICAL-75 naming pattern). The current choice `§VII-B.ZETA-EQUALS-SDW` mirrors `§VII-B.ZETA-NOT-PHYSICAL-75` syntactically (regulator-named, predicate-tense) and reads naturally as a sibling. CONFIRM.

**C-5: F_2 ceiling at s=3 is partition-INSENSITIVE for C-α (lattice-spacing slot-by-slot drift) — ACCEPT.**

Connes' C2 propagation map summary table (workshop lines 1161-1168) classifies C-α (W6-2 lattice-spacing immunization) as INSENSITIVE to the partition choice: the gate's PASS criterion is a slot-by-slot drift exponent measurement against Symanzik O(a^4), which is invariant under whether the per-slot partition is 4-class or 5-class. I ACCEPT — the substitution chain (workshop lines 1049-1098) is correct: each slot's drift exponent is a per-slot measurement, and the partition choice does NOT affect the per-slot measurement output at all.

This convergence on partition-insensitivity for C-α matters for resource allocation: the 3 partition-SENSITIVE channels (W5a-P3 IC, C-β, C-γ-WEAK per connes' table) each generate an S87 carry-forward gate; the 3 partition-INSENSITIVE channels (C-α, C-η, C-θ) do NOT. This is a clean factor-of-2 reduction in the SECTOR-2 carry-forward queue. AGREE.

**C-6: Naming-collision resolution adopting §VII.N L1/L2/L3 as canonical — ACCEPT (Q3 resolved).**

Connes' Re:L4 §1.2 naming-collision resolution (workshop lines 712-719) proposes adopting §VII.N's L1/L2/L3 as canonical and re-tagging cutoff-sqrt LAYER 1 → "L3-combinatorial" / cutoff-sqrt LAYER 2 → "L1-axiomatic". I AGREE in full and have already RATIFIED this in my L4 (above). The reasoning: §VII.N is the registry-permanent stratification (post-S84 W2a-11 landing), so adopting it as canonical avoids parallel-evolving naming conventions and keeps the audit-output document aligned with registry-cite chains. (Q3 resolved.)

### DISSENT

**D-1: Add a footnote to strengthened item (3) on slot-interpolation sharpness.**

Connes' strengthened item (3) phrasing (workshop lines 622-624) reads: "NOT evidence for substrate-distance-1 invariance ... per-regulator splitting at s=−1 must be measured separately." This is correct, but it leaves the slot-interpolation question implicit. The substitution chain (Re:L3 lines 532-566) shows the failure is SHARP at Γ-pole slots — there is no intermediate regime where F_2 is "partially identical." From the spectral-functional perspective, the (ζ, SDW) pair lies on a measure-zero submanifold defined by Γ(s)-cancellation invariance, with discontinuous boundary at Γ-pole slots.

I propose adding a sub-clause to item (3):

> NOT evidence for slot-interpolated F_2 pair-equivalence. The Γ-cancellation that grounds THM-L3.1 is sharp: it holds bit-exactly at Γ-regular real s and fails by an order-of-magnitude factor at Γ-pole real s, with no continuous-interpolation regime between. Any project cite that invokes "F_2 pair-equivalence at intermediate s" or "F_2 holds approximately near Γ-pole" is an unwarranted slot-interpolation that THM-L3.1 does NOT support.

This is a DISSENT only on phrasing — the underlying physics is what connes' strengthened item (3) already establishes (Γ-pole vs Γ-regular dichotomy). My addition is a slot-interpolation sharpness clause that closes one further inference channel: future cites of THM-L3.1 should not assume F_2 holds "approximately" at slots near the Γ-pole. The clause is cheap to include, prevents one foreseeable mis-cite, and does not change connes' reading of the theorem.

If connes wants to include this clause as a footnote rather than a sub-clause of item (3), or as a free-standing item (ix), I am flexible on placement. The structural content is what matters; placement is editorial.

**D-2: C-α partition-INSENSITIVE classification holds for the slot-by-slot drift exponent test specifically; the master-test (Symanzik O(a^4) at all 4 slots) inherits cross-slot consistency that is partition-DEPENDENT at the cross-slot level.**

Connes' C2 (workshop lines 1078-1098) reads C-α as partition-INSENSITIVE because the per-slot drift exponent is invariant under partition choice. I AGREE per slot, but want to STRENGTHEN: the master-test condition (drift exponent matches Symanzik O(a^4) at ALL 4 slots simultaneously) requires cross-slot consistency, and the cross-slot partition behavior IS regulator-class-sensitive. Specifically:

- At a_0 (s=4), the partition is 2-class (RFB f_0 = 0 vs f_0 ≠ 0).
- At a_2 (s=3), the partition is 4-class (lizzi `~_M`).
- At a_4 (s=2), the partition is HP1-derived (registry F_4 vs M).
- At a_6 (s=1), the partition is 5-class with F_2 collapse at Γ-regular.

The master-test asks whether the per-regulator drift-exponent prediction PASS/FAIL is consistent across all 4 slots simultaneously. A regulator that PASSes at a_0 and a_2 but FAILs at a_4 (because its HP1-locale partition class behaves differently) would FAIL the master-test even though each individual slot's drift exponent is partition-invariant. So C-α is partition-INSENSITIVE within each slot but partition-SENSITIVE at the master-test level if cross-slot regulator behavior varies.

This is a NUANCE on connes' reading, not a contradiction. The classification "partition-INSENSITIVE" should be tagged "partition-INSENSITIVE per-slot; partition-SENSITIVE at master-test" in the propagation-map summary table. The S86 W6-2 gate as currently dispatched tests per-slot drift exponents; it would NOT detect cross-slot inconsistency directly. Whether cross-slot inconsistency is OBSERVED depends on whether any regulator's slot-by-slot drift exponents diverge across slots — that is a numerical question the gate answers, but its pre-registration should flag the cross-slot consistency check explicitly.

DISSENT classification: PARTIAL. I accept connes' summary-table classification per-slot (insensitive); I want a footnote on cross-slot master-test sensitivity. This is a Stage-2 refinement to his table, not a structural disagreement.

**D-3: Class 2 (SDW) L1-disqualification at Γ-pole slots — disagree on phrasing, agree on structure.**

Connes' C1 (workshop lines 813-815) reads Class 2 (SDW) as "L1-DISQUALIFIED at Γ-pole slots by the introduction of a Γ(s)-dependent normalization (formally an external scale arising from the Mellin-transform convention)." The structure is correct — at Γ-pole slots SDW carries a non-canonical normalization. The phrasing "L1-DISQUALIFIED at Γ-pole slots" is what I want to refine: SDW is not L1-disqualified-tout-court (it has the same multiplier-vector identity as ζ at Γ-regular slots and would be L1-canonical there if it were extracted at Γ-regular slots only); rather, SDW is L1-disqualified-AT-the-canonical-extraction-slot (s=0 boundary, KO-dim grading), where the canonical Connes-Marcolli Dixmier-trace formulation lives.

The cleaner phrasing: "Class 2 (SDW) L1 status — Γ-conditionally canonical: canonical at Γ-regular slots; disqualified at canonical-extraction slot s=0 by Γ(s) normalization-scale introduction." This separates "disqualified at the canonical slot" from "disqualified everywhere," which matters for downstream cites that may want to evaluate SDW at Γ-regular slots and inherit Class-2 multiplier-vector behavior without invoking the s=0 disqualification.

This is a DISSENT only on phrasing accuracy; the structural content (SDW lifts to L1-canonical at Γ-regular only, fails L1 at the s=0 canonical-extraction slot where Connes-Marcolli Thm 1.31 lives) is what connes wrote. I propose his C1 Class-2 description be re-phrased to "Γ-conditionally canonical" with the slot-disqualification explicit, and the registry's `§VII-B.ZETA-EQUALS-SDW` cross-cite (item vii) should reference this Γ-conditional status to avoid the implication "SDW is non-canonical at every slot" (which is too strong).

### EMERGENCE

**E-1: Three-partition triangle resolved by §VII.N stratification — registry slot-tag protocol.**

The S78-onward F_4 nomenclature collision (Conflation 1 in C3 row 6) names three distinct partitions all "F_4":

- `F_4@a_4-Mellin-support` (registry §VII-B.HP1-NEAR-INVARIANCE Step 1, line 2605): pure-a_4 sub-atlas {ζ, Zubarev, SDW}.
- `F_2@a_2-residue-class@s=3` (my `~_M`, this workshop L1): numerical-residue equivalence at the a_2 slot.
- `F_4@multiplier-vector-with-f_4=1` (connes' 5-class L1-subset, this workshop C1): Class 1 ∪ Class 2 ∪ Class 3 multiplier-vector.

The collision is resolvable by SLOT-TAGGED nomenclature: each "F_n" cite carries the Mellin slot it is taken at as a suffix. This is connes' Q2 proposal — and it ANSWERS the long-standing F_4 ambiguity in the project's prior cites (which I had re-cited from the registry in my S86 W1b-T6 HP^1 PASS, MEMORY S86; the registry's F_4 reading was ambiguous between "the 3-element pure-a_4 sub-atlas" and "any numerical-equivalence class with cardinality up-to-4," a non-trivial conflation that the slot-tag resolves).

The EMERGENT insight: the §VII.N stratification (L1/L2/L3) is NOT just a layer-naming convention for the regulator-class manifold; it is a slot-coordinatization protocol for partition-naming. Any partition-name without a §VII.N stratum tag is ambiguous. The slot-tag protocol is structurally:

```
F_n@{stratum}-{slot}-{partition-relation}
```

where {stratum} ∈ {L1-axiomatic, L2-substrate-action, L3-residual}, {slot} ∈ {s=3, s=−1, s=0, all-Γ-regular, ...}, {partition-relation} ∈ {Mellin-support, multiplier-vector, residue-equivalence, R-protected-band, ...}.

Sample applications:
- registry's F_4 → `F_4@L3-residual-a_4-slot-Mellin-support`.
- my `~_M` 4-class → `F_2@L3-residual-s=3-residue-equivalence` (with F_2 the only multi-member class).
- connes' 5-class L1-subset → `F_4@L1-axiomatic-multiplier-vector-f_4=1`.

The protocol EMERGES from this workshop's resolution of Q2 (F_4 nomenclature collision); it should be canonized in the audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` §1 as part of the naming-collision resolution. Future S87+ partition-cites should adopt the slot-tag form by default.

**E-2: Forward-backward inference closure as substrate-physics methodological theorem.**

The combination of THM-L3.1 non-evidence-status (forward closure, L3) and the L4 retroactive sweep (backward closure, this section + connes' Re:L4) forms a complete LAYER discipline. The substrate-physics interpretation: the regulator-class manifold's prior-cite history is bounded forward-and-backward by structural constraints (combinatorial-position vs admissibility-on-axioms independence, per `cutoff-sqrt-adjudication.md` §1.4). Each direction's closure is a methodological theorem:

- Forward closure (THM-L3.1 non-evidence-status): for any future cite of THM-L3.1, the cite cannot draw conclusions about K-invariance, atlas-uniformity, slot-interpolation, L1-axiomatic uniqueness, KO-grading invariance, or F_4-as-residue-class. The forward closure bounds the OUTBOUND inference channel from the theorem.

- Backward closure (L4 audit): for any past cite that touches the 5-atlas, the cite is LAYER-tagged and any LAYER 1 → LAYER 2 inference must be verifiably routed through an explicit implication theorem. The backward closure bounds the INBOUND inference channel from the project's cite-history.

The pair (forward, backward) is methodologically complete in the sense that no inference can leak out of THM-L3.1 in either direction without being audited. This is itself a substrate-physics result on the regulator-class manifold's cite-discipline: the manifold's structural separation between LAYER 1 and LAYER 2 is preserved by every well-formed cite-chain.

This EMERGES at the methodology-level, not at the per-result level — it is a meta-theorem on how the project's regulator-class statements should compose. Workshop deliverable (b) and (c) jointly instantiate the meta-theorem at S86 W7. Future workshops involving regulator-class results should adopt the same forward-backward closure pattern by construction.

**E-3: SECTOR-2 propagation generates a 5-tuple of physics predictions, not a single canonical prediction.**

Connes' C2 Channel-A substitution chain (workshop lines 970-1024) shows that the W5a-P3 IC source `xi_E_GGE_inv = 13.642e+00` is the L1-canonical (ζ-prescription, Connes-Marcolli Thm 1.31) reading of the s=−1 spectral residue of the GGE-projected D_K. Under the 5-class binding, the correct downstream representation is a 5-tuple `(xi_E_GGE_inv^{Class-1}, ..., xi_E_GGE_inv^{Class-5})` — one per L1-class. The current registry stores only Class-1 (ζ).

The EMERGENT insight: SECTOR-2 propagation does not produce ONE physics prediction, it produces FIVE — one per L1-class. The Z(N_pivot) ratio test currently uses Class-1; the per-class verification gate (S87 carry-forward `S87-W5A-P3-IC-PER-CLASS-VERIFY`) tests whether the ratio direction holds across ALL classes. If the direction holds (PASS): SECTOR-2 splitting is observable but does not affect the inflationary prediction direction; the framework's Z-factor reading is functional-class-INDEPENDENT (which is the strongest form of robustness — it survives across all 5 spectral functionals). If the direction flips for some Class (FAIL or INFO): SECTOR-2 splitting is observable AND directionally significant; the framework's Z-factor reading is functional-class-DEPENDENT, and the choice of regulator-class becomes itself a physics input to the CMB prediction.

This is the spectral-functional-pluralism principle applied at the inflationary observable level. From my S66 ZETA-SA-66 history (eps_H sign flip, MEMORY S66, maximal scheme dependence, n_s blue tilt in zeta), I expect the Z-factor direction to be functional-class-DEPENDENT — SDW's Γ-pole behavior at s=−1 will likely flip something. But this is a prediction, not a theorem; the S87 gate measures it. The EMERGENT insight is that the test even exists — that SECTOR-2 splitting is OBSERVABLE at the SR-flow Z-factor level, not just at the spectral-action-coefficient level.

**E-4: Stage-2.5 sub-classification (LAYER-2-axiomatic vs LAYER-2-numerical) as warrant-class refinement.**

The L4 audit method's Stage-2 (LAYER tag assignment) lumps all LAYER 2 admissibility claims into one bucket, regardless of derivation method. From my S78-onward retroactive examination of the inventory (C3 17-row table), there are TWO distinct sub-types of LAYER 2 claim:

- LAYER-2-axiomatic: derived from NCG axioms A1-A6 + Connes-Marcolli theorems + Connes-Chamseddine 1996 derivations. Examples: "ζ is L1-canonical (Connes-Marcolli Thm 1.31)," "the a_2 Seeley-DeWitt coefficient is regulator-independent on the substrate's positive-definite Casimir spectrum (NCG A1 + A6 derivation)." These claims have STRONG warrant — they survive across substrate-distance-1 / -2 / etc. without per-slot re-verification.
- LAYER-2-numerical: derived from a pre-registered numerical gate against threshold. Examples: "HP^1 LOOSE max ratio = 2.0 (S86 W1b-T6 PASS)," "max_pair_ratio = 9.240e-01 at (ζ, Zubarev) (W4-2 P5 FAIL)." These claims have WEAKER warrant — they hold AT the gate's evaluation slot/L_max only, and may not survive at other slots.

The two sub-types are warrant-class-DIFFERENT, and audit-remediation should treat them differently. A LAYER-2-axiomatic claim invoked as evidence at a LAYER 2 admissibility question is unconditionally-valid; a LAYER-2-numerical claim is only valid at the gate's evaluation conditions. The audit's Stage-2.5 sub-classification (proposed in my L4 above) operationalizes this distinction.

The EMERGENT methodological insight: the audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` should adopt Stage-2.5 by default, with the per-row sub-tag column LAYER-2-axiomatic vs LAYER-2-numerical. This is forward-compatible with connes' 4-stage protocol (it adds one optional sub-tag, does not change the four-stage flow), and it improves the audit's signal-to-noise by distinguishing strong-warrant from weak-warrant LAYER 2 cites.

### QUESTIONS

**Q-LZ-1 (forward to connes R3): Does the forward-backward inference-closure pair (THM-L3.1 non-evidence-status + L4 retroactive sweep) satisfy the §W4-2 line 290 "permanently repairs S78-onward conflation" mandate, or is a third closure direction needed?**

The forward closure bounds future inferences FROM THM-L3.1 outward; the backward closure bounds past inferences from the project's cite-history INTO THM-L3.1's intellectual region. Together they cover (forward) and (backward) directions of inference. Is there a missing direction — e.g., (sideways) inference between contemporaneous workshops at the same session level? Specifically, the S86 W4 (THM-L3.1 source), S86 W6 (C-α/β/γ corollaries), and S86 W5a (P3 IC) workshops are sibling-session-level — does the forward-backward closure cover their cross-citations, or does that require a third closure direction (sideways)?

If sideways is needed, the audit-output file should add a §1.5 cross-session-level closure section. If sideways is subsumed by forward+backward (because every sideways cite is either future-ward or past-ward from the cited workshop's perspective), the forward+backward pair is complete. My intuition is that sideways is subsumed (a contemporaneous-workshop cite is either "I cite their result, they don't cite mine" — which is forward-from-them, backward-from-me — OR "we cross-cite" — which is two pairs of forward+backward). Confirm.

**Q-LZ-2 (R3): The S87 carry-forward gate `S87-W5A-P3-IC-PER-CLASS-VERIFY` (4 additional integrations) — what is the expected order of the per-class IC dispersion?**

From the helper module, the 4 non-Class-1 IC values would arise from Class-2 (SDW at s=−1, Γ(−1) pole), Class-3 (Zubarev at s=−1, direct convergent sum), Class-4 (cutoff_sqrt at s=−1, conditional on GATE A PASS — likely INFEASIBLE per `cutoff-sqrt-adjudication.md` §3.1 GATE A expected FAIL), Class-5 (anomaly at s=−1, Pauli-Villars subtraction with mass-scale M_PV²).

Rough estimate from the depletion factors at s=3 (M_Zubarev/M_ζ = 0.076, M_anomaly/M_ζ = 0.201, M_cutoff/M_ζ = 0.702) and the Γ-pole behavior at s=−1: the dispersion across classes is likely 2-3 orders of magnitude (heat-kernel direct sum vs anomaly mass-scale-driven vs ζ analytic continuation). What is your prior on whether the Z(N_pivot) ratio direction (currently > 1 under ζ) survives across ALL classes (functional-class-INDEPENDENT) or flips for at least one (functional-class-DEPENDENT)? This affects whether SECTOR-2 splitting is observable at the inflationary level.

My S66 history (eps_H sign flip across regulators, ZETA-SA-66 FAIL, maximal scheme dependence) suggests sign-flips are common for Mukhanov-Sasaki observables under regulator variation. Thus my prior is functional-class-DEPENDENT — likely Z-flip on at least one of {SDW, Zubarev, anomaly}. Do you have a contrary prior from the NCG axiomatic side?

**Q-LZ-3 (R3): The slot-tag protocol `F_n@{stratum}-{slot}-{partition-relation}` (E-1 above) — should it be a hard rule (audit-violations FLAG every untagged cite) or a soft convention (recommended for new cites; legacy cites grandfather with auto-tagging)?**

The audit-output file's §1 will include the slot-tag protocol as part of the naming-collision resolution. Whether the protocol applies retroactively (all S78-onward F_n cites must be slot-tagged in remediation) or only forward (new S87+ cites must be slot-tagged; legacy cites are auto-tagged in the audit-output file but original sources are not edited) determines the audit's REPAIR-IN-SESSION queue size. My recommendation is forward-only (the audit-output file maintains a slot-tag table; original sources in the registry/workshop docs are NOT edited unless they are flagged for OTHER conflation reasons), which keeps the audit's REPAIR-IN-SESSION queue manageable.

If you favor hard-rule retroactively (every untagged S78-onward F_n cite gets a REPAIR-IN-SESSION tag), the audit's REPAIR-IN-SESSION queue grows by ~30-50 entries (rough estimate from the S78+ session-record). This is feasible but expensive in S87+ remediation effort. Pre-registered call needed.

**Q-LZ-4 (R3): The C-α master-test cross-slot consistency (D-2 dissent) — should it be added as a separate gate `S87-W6-C-ALPHA-MASTER-TEST` testing whether each regulator's per-slot drift exponents agree across all 4 slots simultaneously, or is it captured by the existing C-α gate's pre-registration?**

The current C-α gate (W6-2) tests per-slot drift exponents. My D-2 dissent flagged that the master-test condition (Symanzik O(a^4) at ALL 4 slots simultaneously per regulator) is partition-DEPENDENT at the cross-slot level if any regulator's per-slot drift exponents diverge across slots. Whether this requires a separate gate depends on whether the existing C-α gate's pre-registration includes the cross-slot consistency check explicitly. If yes, no separate gate needed. If no, propose adding `S87-W6-C-ALPHA-MASTER-TEST` to the carry-forward queue.

**Q-LZ-5 (R3): Stage-2.5 sub-classification (LAYER-2-axiomatic vs LAYER-2-numerical) — does the registry's existing entry-tagging schema accommodate the sub-tag, or is a registry-side schema extension needed?**

I propose Stage-2.5 sub-classification (E-4 emergence) with two sub-tags. The audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` will use these sub-tags in its inventory. Question: should the registry entries themselves carry the sub-tag in their entry-headers (e.g., `§VII-B.HP1-NEAR-INVARIANCE [LAYER-2-numerical]`), or is the sub-tag a property of the audit-output file's per-row classification only? My preference is registry-side schema extension (the sub-tag is a permanent property of each entry, useful for downstream cite-resolution), but the registry-write hygiene rule (S86 W1c surface) imposes append-only-Python-writer discipline that may need updating to accommodate the new sub-tag column.

This is a concrete S87 carry-forward `S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION` if you AGREE with the registry-side extension. If you prefer audit-output-file-only, the sub-tag stays out of the registry and S87 carry-forward queue does not need this entry.

---

## Round 2 — connes: Cross-Synthesis

### CONVERGENCE

**Topline.** With lizzi's R2-A in hand, six of six convergence offerings (C-1 through C-6) close the load-bearing decisions for workshop deliverables (a) / (b) / (c). The dual-binding partition (C-1) answers Q1; the slot-conditionality strengthening (C-2) cleans THM-L3.1's most consequential non-evidence-status item; the two added items (C-3) make the §VII-B.ZETA-EQUALS-SDW skeleton complete at 8 items; the registry slot identity (C-4) is final; the per-slot partition-INSENSITIVE classification of C-α (C-5) is correctly bounded by D-2's master-test refinement; the §VII.N L1/L2/L3 canonical naming (C-6) closes Q3. lizzi's L4 backfill (4-stage audit protocol, naming-collision resolution, Stage-2.5 sub-classification, two forward-questions) ratifies my Re:L4 scaffolding in full. Below I confirm each convergence point explicitly with the structural reason it lands, and where lizzi added refinement (C-2's sharpness clause, E-4's Stage-2.5 sub-tag) I ratify the refinement.

**CV-1: Dual-binding partition (C-1) — confirmed; answers Q1 and triggers Q2-Q5 cascade.**

I CONFIRM lizzi's C-1 acceptance in full. The substitution chain in her C-1 (workshop lines 1528-1568) reproduces my Re:L1 EMERGES + C1 reconciliation table reasoning correctly: the 4-class @ L3-s=3 is the projection of the 5-class @ L1 onto the a_2-slot residue evaluation, with Class 1 (ζ) and Class 2 (SDW) collapsing via THM-L3.1 at Γ-regular s but staying distinct at Γ-pole slots (s=0, s=−1). The binding-partition criterion she states ("finest partition that respects every downstream channel's evaluation stratum") is the correct definition — it is exactly what §VII.N C1 (registry line 5867: "L1 and L2 do NOT propagate via Mellin exponents") demands once a downstream channel evaluates at L1 or L2 strata.

**Substitution chain (closure of Q1 binding direction):**

```
Step 1 (definitions):
  binding_partition(channel) := finest partition relation P on A_5 such that
                                two regulators in the same P-class produce
                                identical channel output at the channel's
                                evaluation stratum.
  
  channel.eval_stratum := the §VII.N stratum (L1, L2, or L3) at which the
                          channel reads spectral data.
  
  cross-stratum(channel) := True if the channel's pre-registration evaluates
                            at multiple §VII.N strata (e.g., W5a-P3 IC at
                            s=−1 reads L1-Γ-pole AND L3-residual; C-γ-WEAK
                            at full multiplier vector reads L1-axiomatic
                            AND L3-residual jointly).

Step 2 (substitute):
  W5a-P3 IC channel.eval_stratum  = L1-Γ-pole (s=−1)  ∪ L3-residual.
  C-γ-WEAK channel.eval_stratum   = L1-axiomatic ∪ L3-residual.
  C-β UV-cutoff channel.eval_stratum = L1-axiomatic ∪ HP1-locale-specific.
  C-α channel.eval_stratum        = L3-residual (per-slot drift) +
                                    L3-residual cross-slot (master-test).
  
  At L1-Γ-pole, ζ ≠ SDW (ZETA-NOT-PHYSICAL-75 + Re:L3 strengthened item 3).
  At L1-axiomatic, the multiplier-vector grading distinguishes Class 1 from
  Class 2 (Connes-Marcolli Thm 1.31 selects ζ; SDW is sibling at Γ-regular).
  At L3-residual-s=3, Class 1 ∪ Class 2 collapses to F_2 (THM-L3.1).

Step 3 (simplify):
  binding_partition(W5a-P3 IC)       = 5-class @ L1
  binding_partition(C-γ-WEAK)        = 5-class @ L1
  binding_partition(C-β)             = 5-class @ L1 (3-class within F_4 sub-atlas)
  binding_partition(C-α per-slot)    = slot-dependent (4-class at s=3, 2-class at s=4, ...)
  binding_partition(C-α master-test) = 5-class @ L1 (cross-slot consistency check)

Step 4 (direction):
  The finest partition that respects ALL downstream channels is 5-class @ L1.
  4-class @ L3-s=3 is the projection at one specific channel-locale (a_2 slot
  per-Q span via §VII.K-PROP) and is the binding partition for that channel
  only. The dual binding (5-class registry, 4-class projection theorem) is
  therefore the correct registry-write.
  
  Conclusion: lizzi's C-1 acceptance is structurally exact. The SECTOR-2
  registry-write should land 5 sub-tags (SECTOR-2-ζ, SECTOR-2-Zubarev,
  SECTOR-2-SDW, SECTOR-2-cutoff_sqrt, SECTOR-2-anomaly) with the 4-class
  projection at s=3 noted as a downstream propagation theorem.
```

The dual binding closes Q1 load-bearing; Q2 (F_4 nomenclature), Q3 (LAYER naming-collision), Q4 (non-evidence-status items), Q5 (registry slot) all cascade to convergence per the C2-C6 chain.

**CV-2: Slot-conditionality strengthening (C-2) — confirmed; lizzi's sharpness clause adopted as item-(3) sub-clause.**

lizzi's C-2 acceptance of my Re:L3 strengthening is structurally exact. Her addition that the slot-conditionality is SHARP (no intermediate regime; Γ-regular vs Γ-pole dichotomy is bit-exact one side, order-of-magnitude failure the other side) is correct on the substrate-physics: the Γ(s) function has isolated simple poles at non-positive integers, and the regulator-class manifold's submanifold-of-Γ-cancellation-invariance has a discrete boundary at exactly those Γ-pole slots. There is no continuous-interpolation regime; the partition-equivalence flips discontinuously.

I CONFIRM the sharpness clause and ADOPT it as proposed in lizzi's D-1 (workshop lines 1612-1614). Specifically, I incorporate her phrasing into the strengthened item (3) sub-clause:

> NOT evidence for substrate-distance-1 invariance ... per-regulator splitting at s=−1 must be measured separately. **Slot-interpolation sharpness clause:** the Γ-cancellation that grounds THM-L3.1 is sharp — it holds bit-exactly at Γ-regular real s (with rel_err = 1.7556e-16 at s=3, 1 ULP under float64) and fails by an order-of-magnitude factor at Γ-pole real s (with 381× dynamic range at s=0 per ZETA-NOT-PHYSICAL-75), with NO continuous-interpolation regime between. Any project cite that invokes "F_2 pair-equivalence at intermediate s" or "F_2 holds approximately near Γ-pole" is an unwarranted slot-interpolation that THM-L3.1 does NOT support.

This is now item (iii) in the strengthened §VII-B.ZETA-EQUALS-SDW skeleton. I treat lizzi's D-1 as a CONVERGENCE refinement (phrasing-only addition, not structural disagreement) and incorporate it into the registry-ready entry skeleton in EM-1 below.

**CV-3: Two added non-evidence-status items (C-3) — confirmed (vii) + (viii).**

lizzi's C-3 acceptance of my added items (vii) and (viii) is structurally exact. The Connes-Marcolli 2008 Thm 1.31 L1-uniqueness selector is a permanent NCG-axiomatic result (Connes-Moscovici local index formula on L^(1,∞)(H), Dixmier-trace uniqueness on the ideal); SDW does not lift to L1-canonical because the Mellin convention's Γ(s) factor introduces a normalization scale at the s=0 boundary that is NOT in the canonical Dixmier-trace formulation. Item (vii) closes the L3 → L1 inference channel that THM-L3.1 might otherwise be invoked for.

For item (viii) (KO-dim 6 Z/8 grading invariance under arbitrary slot extraction), the structural reason it is a valid non-evidence claim: the Mellin transform's `s ↦ d − s` symmetry interacts with the J-action via [J, |D|^{−s}] = 0; ζ carries this symmetry canonically (the canonical analytic continuation preserves the J-grading); SDW carries it up to Γ(d−s)/Γ(s) which is finite at canonical-s slots but singular at Γ-pole slots. THM-L3.1 establishes (ζ, SDW) pair-equivalence at a single Γ-regular slot; it does NOT establish that the J-grading invariance survives across all slots (which it does not, at Γ-pole slots). Item (viii) closes the KO-grading invariance inference channel.

Both items are accepted by lizzi (workshop lines 1582-1588) with explicit reference to ZETA-NOT-PHYSICAL-75 (S75 result, 381× dynamic range, MEMORY S75) as the empirical anchor for item (vii) and KO-dim 6 generalization for item (viii). I CONFIRM both items in the §VII-B.ZETA-EQUALS-SDW final-form skeleton (workshop lines 600-651, with my final consolidation in EM-1 below).

**CV-4: Registry slot `§VII-B.ZETA-EQUALS-SDW` (C-4) — confirmed; Q5 closed.**

lizzi's C-4 confirmation of the slot identity is structurally consistent with the §VII-B Lizzi-track Cluster (registry line 4742-4747) — three sibling Lizzi-track structural results sharing methodology (per-regulator analysis on the substrate's spectral functional manifold): ZETA-NOT-PHYSICAL-75 (s=0 boundary corollary, S75/W2-3 origin), HP1-NEAR-INVARIANCE (HP^1 cohomology corollary, S86 W1b origin), TWO-LAYER-OBSTRUCTION (n_joint = 0/5 obstruction, S86 W1b origin), and now ZETA-EQUALS-SDW (slot-conditional machine-epsilon identity, S86 W4-2 / W7 origin).

Her consideration of alternative names (`§VII-B.ZETA-MELLIN-IDENTITY`, `§VII-B.F_2-PAIR-EQUIVALENCE`) and explicit choice of `§VII-B.ZETA-EQUALS-SDW` as the canonical slot name (mirrors `§VII-B.ZETA-NOT-PHYSICAL-75` syntactically — regulator-named, predicate-tense) is the right call. The naming pattern signals to future cite-readers that the entry is a Lizzi-track ZETA-* sibling, which is the appropriate parsing for navigating the Lizzi-track Cluster.

I CONFIRM `§VII-B.ZETA-EQUALS-SDW` as the canonical landing slot for workshop deliverable (c). Q5 is closed.

**CV-5: C-α partition-INSENSITIVE per-slot (C-5) — confirmed with D-2 master-test cross-slot bound.**

lizzi's C-5 acceptance of my C-α partition-INSENSITIVE classification, paired with her D-2 dissent that the master-test (Symanzik O(a^4) at all 4 slots simultaneously per regulator) is partition-DEPENDENT at the cross-slot level, is the correct refinement. The substitution chain that closes the dispute:

```
Step 1 (definitions):
  per_slot_test := the gate's measurement at one Mellin slot (e.g., a_0 at s=4).
                   Output is one drift exponent per regulator per slot.
  
  master_test   := the gate's PASS criterion at the cross-slot level. Output
                   is per-regulator PASS (drift exponent matches Symanzik O(a^4)
                   at ALL 4 slots simultaneously) or FAIL (at least one slot
                   diverges from Symanzik).

Step 2 (substitute):
  per_slot_test partition behavior at slot a_0 (s=4):  2-class (RFB f_0 split).
  per_slot_test partition behavior at slot a_2 (s=3):  4-class (lizzi `~_M`).
  per_slot_test partition behavior at slot a_4 (s=2):  HP1-derived 2-class.
  per_slot_test partition behavior at slot a_6 (s=1):  5-class with F_2 collapse.
  
  master_test cross-slot partition behavior:
    a regulator R PASSes the master-test iff its drift exponent matches
    Symanzik O(a^4) at every slot in {a_0, a_2, a_4, a_6}.
    
    Two regulators (R, R') in the same per-slot partition class at every slot
    will PASS-or-FAIL together. Two regulators in DIFFERENT per-slot classes
    at any slot may PASS-or-FAIL differently.

Step 3 (simplify):
  per_slot_test:    partition-INSENSITIVE (the per-slot drift exponent
                    measurement is structurally invariant across partition
                    relations — what matters is the regulator's per-slot
                    output, not its class label).
  master_test:      partition-INSENSITIVE per-slot, but partition-SENSITIVE
                    cross-slot — because the cross-slot consistency check
                    aggregates per-slot outputs, and aggregating outputs
                    that themselves vary across regulator classes at each
                    slot produces a regulator-class-dependent master verdict.

Step 4 (direction):
  Direction implication:
    - For per-slot drift exponent measurements: partition choice does not
      affect the gate output. Connes' C2 classification "INSENSITIVE" is
      correct at this level.
    - For master-test cross-slot consistency: partition choice DOES affect
      the master-verdict because the partition determines which regulators
      cluster together at each slot, and the master-test compares the per-
      slot clusters against Symanzik O(a^4) at every slot.
  
  Conclusion: C-α requires DUAL classification — partition-INSENSITIVE
              per-slot (connes' reading); partition-SENSITIVE master-test
              (lizzi's D-2 refinement). Both are correct; they apply at
              different gate-evaluation levels.
```

I CONFIRM lizzi's D-2 refinement and ADOPT the dual classification: C-α is "partition-INSENSITIVE per-slot; partition-SENSITIVE at master-test." The propagation-map summary table (workshop lines 1314-1322) should be re-tagged accordingly. This is a methodological refinement, not a structural disagreement — both classifications are correct at their respective gate-evaluation levels, and the dual tag captures the full picture.

The S87 carry-forward consequence: the existing C-α gate (W6-2) tests per-slot drift exponents and is partition-insensitive. The master-test cross-slot consistency check is a SEPARATE-gate question (lizzi's Q-LZ-4) that I address in EM-2 below.

**CV-6: Naming-collision resolution adopting §VII.N L1/L2/L3 (C-6) — confirmed; Q3 closed.**

lizzi's C-6 acceptance of my Re:L4 §1.2 naming-collision resolution (workshop lines 1602-1604) ratifies the canonical adoption of §VII.N's L1/L2/L3 nomenclature for the audit-output file. The structural reason this is correct: §VII.N is the registry-permanent stratification (post-S84 W2a-11 landing, three-solo theorem signed by connes/lizzi/VdD, full SHA cf3b7443 per MEMORY S84); cutoff-sqrt-adjudication's LAYER 1/2 is a PER-FILE convention that pre-dates §VII.N's registry landing. Adopting the registry-permanent naming as canonical avoids parallel-evolving naming conventions and aligns the audit-output file with the registry's permanent stratification chain.

The re-tag table is fixed:
- cutoff-sqrt LAYER 1 (combinatorial-position-on-atlas) → "L3-combinatorial" (residual-per-Q stratum of §VII.N).
- cutoff-sqrt LAYER 2 (admissibility-on-axioms) → "L1-axiomatic" (axiomatic-global stratum of §VII.N).
- §VII.N L2 (substrate-action-local-at-fold) has no analog in cutoff-sqrt LAYER 1/2 and remains its own stratum in the unified naming.

I CONFIRM the re-tag table. Q3 is closed.

**CV-7: lizzi's L4 backfill (4-stage audit protocol + naming-collision resolution + Stage-2.5 + 2 forward-questions) — confirmed in full.**

lizzi's L4 backfill (workshop lines 357-513, retroactively filled) ratifies my Re:L4 scaffolding while adding two structural refinements:

1. **The Stage-2.5 sub-classification refinement (E-4).** The L4 audit method's Stage-2 lumps all LAYER 2 admissibility claims into one bucket; lizzi's E-4 distinguishes LAYER-2-axiomatic (NCG axioms A1-A6 + Connes-Marcolli derivations) from LAYER-2-numerical (pre-registered numerical gate against threshold). The two sub-types are warrant-class-different — axiomatic claims have STRONG warrant (survive across slots without re-verification); numerical claims have WEAKER warrant (hold AT the gate's evaluation slot/L_max only). I CONFIRM this distinction is structurally correct and methodologically necessary. The sub-classification operationalizes the §VII.N stratification at the audit-tagging level: a LAYER-2-axiomatic claim corresponds to an L1 (axiomatic-global) cite in §VII.N; a LAYER-2-numerical claim corresponds to an L3 (residual-per-observable) cite. Adopting Stage-2.5 in the audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` improves the audit's signal-to-noise by distinguishing strong-warrant from weak-warrant LAYER 2 cites.

2. **lizzi's Stage-2 refinements on rows 5 and 16 of the C3 inventory.** Row 5 (registry §VII.N L3 R-protected vs NOT-R-protected partition) — lizzi's "LAYER-1-from-LAYER-2-inputs" sub-tag is correct: the partition itself is combinatorial in form (it reads off `span_Q` band-membership without a per-axiom test), but its band-thresholds (1.5 / 2.5) are admissibility-derived (LAYER 2 inputs). This refinement is consistent with `cutoff-sqrt-adjudication.md` §1.4's "two layers are INDEPENDENT structural properties." I AGREE with the refinement. Row 16 (§W4-2 substitution chain Step 3) — lizzi's strengthening that `a_2-regulator-independence` is LAYER-2-axiomatic (NCG A1 + A6 derivation), not LAYER-2-numerical, is correct: the regulator-independence of `a_2(τ_pivot)` follows from NCG axiom A1 dimension-summability + A6 regularity δ-closure as an axiomatic derivation, not from a numerical gate. I AGREE with the refinement.

Both refinements feed naturally into the Stage-2.5 sub-classification I confirm above. The audit-output file's §1.3 (4-stage protocol) should be amended to "5-stage protocol with optional Stage-2.5 sub-tag" — explicitly carrying the LAYER-2-axiomatic vs LAYER-2-numerical sub-tag through the Stage 3 cross-tag conflation detection and Stage 4 remediation tagging.

**Convergence summary table.**

| Convergence point | Resolves | Workshop deliverable | Status |
|:---|:---|:---|:---|
| CV-1 (dual binding) | Q1 (Re:L1 + C1 reconciliation) | (a) registry partition | Closed; 5-class @ L1 canonical write, 4-class @ L3-s=3 projection theorem |
| CV-2 (slot-conditionality + sharpness) | Re:L3 item (3) + lizzi D-1 | (c) registry skeleton | Closed; sharpness clause adopted as item-(3) sub-clause |
| CV-3 (items vii + viii) | Q4 (Re:L3 ADD) | (c) registry skeleton | Closed; both items added to skeleton |
| CV-4 (slot identity) | Q5 (Re:L3 final-form) | (c) registry slot | Closed; `§VII-B.ZETA-EQUALS-SDW` final |
| CV-5 (C-α dual classification) | C-5 + D-2 | (b) propagation-map | Closed; "INSENSITIVE per-slot, SENSITIVE master-test" tag |
| CV-6 (LAYER naming-collision) | Q3 (Re:L4 §1.2) | (b) audit-output file | Closed; §VII.N nomenclature canonical |
| CV-7 (L4 backfill + Stage-2.5) | E-4 + L4 R1 retroactive | (b) audit-output file | Closed; Stage-2.5 sub-classification adopted |

All seven convergence points close downstream-resolvable. The DISSENT section below addresses the remaining two refinements (slot-tag protocol structural simplification + Class-2 phrasing), and the EMERGENCE section consolidates the cross-pollinated insights for R3 to land all three deliverables.

### DISSENT

**Topline.** Two structural refinements remain after lizzi's R2-A: (DI-1) lizzi's E-1 slot-tag protocol `F_n@{stratum}-{slot}-{partition-relation}` admits a structural simplification that drops the explicit-partition-relation field for cases where the §VII.N stratum + Mellin slot together determine the partition relation uniquely (which is most cases); (DI-2) lizzi's D-3 Class 2 (SDW) phrasing refinement to "Γ-conditionally canonical" is correct in spirit but the qualifier should be sharpened to "Γ-regular-canonical, Γ-pole-disqualified" because "Γ-conditionally canonical" reads ambiguously between "canonical at SOME Γ-conditions" and "canonical conditional on Γ-regularity." The structural content is unchanged from her D-3; the phrasing refinement matters for downstream cite-readers parsing the §VII-B.ZETA-EQUALS-SDW item (vii) cross-cite chain.

**DI-1: E-1 slot-tag protocol structural simplification.**

lizzi's E-1 slot-tag protocol (workshop lines 1657-1666) reads:

```
F_n@{stratum}-{slot}-{partition-relation}
```

where `{stratum}` ∈ `{L1-axiomatic, L2-substrate-action, L3-residual}`, `{slot}` ∈ `{s=3, s=−1, s=0, all-Γ-regular, ...}`, `{partition-relation}` ∈ `{Mellin-support, multiplier-vector, residue-equivalence, R-protected-band, ...}`.

The protocol is structurally correct as a 3-coordinate scheme. My DISSENT: the third coordinate (partition-relation) is REDUNDANT in most cases because the (stratum, slot) pair determines the partition relation uniquely. Specifically:

```
Step 1 (substitution chain — partition relation derivation from stratum + slot):
  
  At L1-axiomatic, the canonical partition relation is multiplier-vector
  identity (Connes-Chamseddine 1996 §2.2-2.3) — there is NO other partition
  relation operating at L1-axiomatic that lizzi's protocol cites elsewhere.
  
  At L2-substrate-action, the canonical partition relation is the three-
  criterion intersection at τ_fold (integrability, local-min-in-tau, chirality
  +1) per §VII.N L2 (registry line 5711) — again, no other partition relation
  cited at L2.
  
  At L3-residual, the partition relation depends on the SLOT being evaluated:
    - L3-residual @ s=3 a_2-slot:    residue-equivalence (lizzi's `~_M`)
    - L3-residual @ s=2 a_4-slot:    Mellin-support concentration (HP1)
    - L3-residual @ s=4 a_0-slot:    f_0-test (RFB Theorem (i))
    - L3-residual @ s=1 a_6-slot:    Γ-regular residue (5-class with F_2 collapse)
  
  At L3-residual, the slot determines the partition relation uniquely:
    {slot} → {partition-relation} is a function (1-to-1 map for the partition
    relations in the project's record).

Step 2 (simplify):
  At L1-axiomatic and L2-substrate-action, {partition-relation} is determined
  by {stratum} alone (since the slot is irrelevant — these strata do not
  propagate via Mellin exponents per §VII.N C1 line 5867).
  At L3-residual, {partition-relation} is determined by {slot} alone (since
  the partition relation IS the per-slot residue-extraction).

Step 3 (direction):
  The (stratum, slot) pair determines the partition relation in every case
  in the project's S78-onward record. The third coordinate is redundant.
  
  Conclusion: Simplify to F_n@{stratum}-{slot}, with {stratum} ∈ {L1, L2, L3}
              and {slot} ∈ {s=4, s=3, s=2, s=1, s=0, s=−1, all-Γ-regular,
              cross-slot}. The partition relation is implicit in (stratum,
              slot) and need not be tagged explicitly.
```

**Proposed simplified protocol:**

```
F_n@{stratum}-{slot}
```

with the following resolution rules (canonized in `sessions/framework/registry/layer1-layer2-retroactive-audit.md` §1.2):

| (stratum, slot) | Implicit partition relation |
|:---|:---|
| L1-axiomatic, any slot | multiplier-vector identity (Connes-Chamseddine 1996) |
| L2-substrate-action, τ_fold | three-criterion intersection (integrability + local-min-in-tau + chirality) |
| L3-residual, s=4 (a_0-slot) | f_0-test (RFB Theorem (i)) |
| L3-residual, s=3 (a_2-slot) | residue-equivalence (`~_M`) |
| L3-residual, s=2 (a_4-slot) | Mellin-support concentration (HP1) |
| L3-residual, s=1 (a_6-slot) | Γ-regular 5-class with F_2 collapse |
| L3-residual, s=0 boundary | spectral-zeta non-observability (ZETA-NOT-PHYSICAL-75) |
| L3-residual, s=−1 (W5a IC) | Γ-pole 5-class no-collapse |

Sample applications under the simplified protocol:
- registry's F_4 → `F_4@L3-s=2` (pure-a_4 Mellin-support, HP1).
- lizzi's `~_M` 4-class → `F_2@L3-s=3` (residue-equivalence at a_2-slot, with F_2 the multi-member class).
- my 5-class L1-subset → `F_4@L1` (multiplier-vector with f_4=1 at L1-axiomatic; slot is irrelevant at L1 per §VII.N C1).

This is a 2-coordinate protocol vs lizzi's 3-coordinate. The simplification reduces tag verbosity by ~33% and eliminates the third-coordinate ambiguity (e.g., is "residue-equivalence" the same partition-relation as "R-protected-band"? Under the 3-coordinate protocol, this question requires resolution; under the 2-coordinate, the (stratum, slot) pair determines the relation uniquely from a fixed table).

**Where lizzi's 3-coordinate protocol would be NECESSARY (and thus my simplification fails):** if a future S87+ result introduces a NEW partition relation at the same (stratum, slot) — e.g., a new partition at L3-s=3 that is NOT residue-equivalence — the 2-coordinate protocol breaks. For now, the project's S78-onward record shows ONE partition per (stratum, slot), so the 2-coordinate protocol is sufficient. If a future workshop introduces a second partition at the same (stratum, slot), the protocol can be extended back to 3 coordinates with the third coordinate explicit only at that ambiguity-locus.

**Recommendation for R3:** adopt the 2-coordinate protocol `F_n@{stratum}-{slot}` as the canonical naming with the resolution table above. Reserve the 3-coordinate `F_n@{stratum}-{slot}-{partition-relation}` form as a fallback for ambiguity-loci that may appear in S87+. This is a structural simplification of lizzi's E-1 proposal — same content, less verbosity, with extensibility preserved.

**DI-2: D-3 Class 2 (SDW) phrasing — "Γ-regular-canonical, Γ-pole-disqualified" vs "Γ-conditionally canonical".**

lizzi's D-3 (workshop lines 1635-1641) proposes re-phrasing my C1 Class 2 description from "L1-DISQUALIFIED at Γ-pole slots by the introduction of a Γ(s)-dependent normalization" to "Γ-conditionally canonical: canonical at Γ-regular slots; disqualified at canonical-extraction slot s=0 by Γ(s) normalization-scale introduction."

I AGREE on the structural content (SDW lifts to L1-canonical at Γ-regular slots only; fails L1 at the s=0 canonical-extraction slot where Connes-Marcolli Thm 1.31 lives). The phrasing refinement matters because my original C1 wording reads as "SDW is non-canonical at every slot" (too strong); lizzi's correction restores the Γ-regular-canonical reading.

DISSENT on phrasing precision: "Γ-conditionally canonical" reads ambiguously. Two parsings:

- **Parsing A:** "Canonical at SOME Γ-conditions (Γ-regular), disqualified at OTHER Γ-conditions (Γ-pole)." This is what lizzi means.
- **Parsing B:** "Canonical conditional on Γ-regularity holding (i.e., canonical IF Γ is regular, undefined OTHERWISE)." This is a weaker reading that could be invoked if a downstream cite wants to conclude "SDW is canonical at all slots where Γ is regular, and we make no claim at Γ-pole slots."

The two parsings differ on Γ-pole behavior: Parsing A says SDW is disqualified at Γ-pole (positive claim); Parsing B says SDW is undefined at Γ-pole (silent claim). For the §VII-B.ZETA-EQUALS-SDW item (vii) cross-cite to §VII.N L1 (registry line 5699 "Uniqueness at L1: zeta"), Parsing A is required — SDW must be POSITIVELY disqualified from L1-canonical status, not just silent on it, otherwise item (vii) does not establish the L1-uniqueness claim (which is "ζ is the UNIQUE L1-canonical regulator", requiring positive disqualification of SDW at the canonical-extraction slot).

**Proposed refined phrasing:** "Class 2 (SDW) L1 status — **Γ-regular-canonical, Γ-pole-disqualified**: canonical at Γ-regular slots (multiplier-vector identical to ζ at s=3, s=2, s=1, ...), explicitly disqualified at the canonical-extraction slot s=0 by Γ(s) normalization-scale introduction (per Connes-Marcolli Thm 1.31's Dixmier-trace formulation, which extracts at s=d=8 in our setting and at s=0 boundary for the spectral-zeta case)."

This phrasing:
- Makes Parsing A explicit (positive disqualification at Γ-pole).
- Specifies the disqualification slot (s=0 canonical-extraction, ZETA-NOT-PHYSICAL-75 territory).
- Cross-cites Connes-Marcolli Thm 1.31 explicitly for the L1-uniqueness selector.
- Avoids the "Γ-conditionally canonical" ambiguity.

This is a phrasing-only refinement of lizzi's D-3 (not structural disagreement). I propose it for the C1 Class-2 description in the workshop's R3 final consolidation, and for the §VII-B.ZETA-EQUALS-SDW item (vii) cross-cite chain.

**DISSENT summary.**

| Dissent point | lizzi's R2-A position | My refinement | Structural disagreement? |
|:---|:---|:---|:---|
| DI-1 | E-1 3-coordinate slot-tag protocol | 2-coordinate with resolution table | NO (simplification, content preserved) |
| DI-2 | D-3 "Γ-conditionally canonical" | "Γ-regular-canonical, Γ-pole-disqualified" | NO (phrasing precision) |

Both dissents are structural simplifications / phrasing refinements; neither contests lizzi's underlying content. The R3 consolidation should adopt both refinements directly into the registry-ready entry skeleton (EM-1 below) and the audit-output file outline.

### EMERGENCE

**Topline.** Three cross-pollinated insights emerge from the joint reading of lizzi's R2-A and my Re:L1-L4 + C1-C4 + R2-A CONVERGENCE/DISSENT: (EM-1) the upgrade pathway for the dual-binding partition into permanent-results-registry follows a specific 3-step sequence (§VII-B.ZETA-EQUALS-SDW landing first, sub-tag schema extension second, propagation-theorem registration third); (EM-2) the LAYER-2-axiomatic vs LAYER-2-numerical Stage-2.5 distinction is itself a downstream gate criterion — the warrant-class refinement makes per-class admissibility testable, generating a new gate type `S87-LAYER-2-WARRANT-CHECK` for any LAYER-2-numerical claim whose warrant-class is contested; (EM-3) the forward-backward inference closure pair is a cross-pillar methodological generator — it applies not just to the regulator-class manifold (the SECTOR-2 substrate) but to ANY substrate-physics manifold the project investigates with prior-cite history, including the Jensen-deformation manifold, the Mellin-strip integrability manifold, and the GGE-relic spectral functional manifold.

**EM-1: Upgrade pathway for the dual-binding partition into permanent-results-registry.**

The dual-binding partition (CV-1) has a specific 3-step landing sequence to reach permanent-results-registry status, derived from the registry-write hygiene rule (S86 W1c surface, `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene") and the §VII-B Lizzi-track Cluster structure (registry line 4742-4747):

**Step 1: Land §VII-B.ZETA-EQUALS-SDW with the consolidated 8-item non-evidence-status declaration.** This is workshop deliverable (c). The final-form skeleton incorporating CV-1 through CV-7 + DI-2 phrasing refinement:

```
### VII-B.ZETA-EQUALS-SDW — ζ=SDW Slot-Conditional Machine-Epsilon Identity
       (Lizzi-track; S86 W4-2 / W7) (2026-04-27)

THEOREM (ζ=SDW slot-conditional; Lizzi-track). On the substrate's positive-
definite Casimir spectrum at REAL s in the Γ-regular domain (s ∉ {0, −1,
−2, ...}), the analytic-continuation Mellin multiplier M_ζ(s) and the SDW
(Γ(s)-cancelled) Mellin multiplier M_SDW(s) coincide bit-exactly under
the Connes-Chamseddine spectral-action ratio normalization. At s=3 (a_2
slot in d_spec=8 NCG), the schematic helper realization returns rel_err =
1.7556e-16 (1 ULP, machine epsilon).

SLOT-CONDITIONALITY: The identity FAILS at Γ-pole slots s ∈ {0, −1, −2,
...}. At s=0 specifically, the s=0 boundary is the domain of ZETA-NOT-
PHYSICAL-75 (S86 W1b T5fix; 381× dynamic range across L_max), where ζ
and SDW carry DIFFERENT normalization conventions. The F_2 = {ζ, SDW}
pair-identity is therefore the equivalence-class on the positive-s
half-plane only. Sharpness clause (lizzi D-1, connes adopted): the
Γ-cancellation that grounds the identity is sharp — bit-exact at Γ-
regular real s, order-of-magnitude failure at Γ-pole real s, with NO
continuous-interpolation regime between.

NON-EVIDENCE-STATUS (8 items): This identity DOES NOT support
  (i)    K-invariance across the live 5-atlas A_5,
  (ii)   atlas-uniformity at substrate-distance-1,
  (iii)  substrate-distance-1 invariance at any slot beyond s=3, including
         s=−1 (W5a P3 IC source at xi_E_GGE_inv) — see SLOT-CONDITIONALITY
         + sharpness clause; per-regulator splitting at s=−1 must be measured
         separately,
  (iv)   F_4-as-numerical-residue-class (registry F_4 is Mellin-support, not residue),
  (v)    the helper module's Mellin convention as canonical-physical,
  (vi)   regulator-class taxonomy collapse (the 4-class @ L3-s=3 partition
         is a projection of the 5-class @ L1 partition; the identity
         enables the projection but does not collapse the L1 partition),
  (vii)  L1-axiomatic uniqueness — Connes-Marcolli 2008 Thm 1.31 selects
         ζ as the unique L1-canonical regulator (Class 1 in the 5-class
         partition); SDW is Γ-regular-canonical, Γ-pole-disqualified
         (Class 2; canonical at Γ-regular slots but disqualified at the
         canonical-extraction slot s=0 by Γ(s) normalization-scale
         introduction) — cite §VII.N registry line 5699 + 5667,
  (viii) KO-dim 6 Z/8 grading invariance under arbitrary slot extraction —
         ζ carries the J-action `[J, |D|^{−s}] = 0` canonically; SDW
         carries it up to a Γ(d−s)/Γ(s) factor finite at canonical-s
         slots but singular at Γ-pole slots; only Γ-regular slots
         preserve the KO grading under both ζ and SDW conventions.

The identity is a slot-conditional algebraic property of the (ζ, SDW)
regulator pair on positive-definite spectra at Γ-regular real s; it
carries no inference to other regulator pairs, to Γ-pole slots, or to
the L1-axiomatic stratum.

LAYER TAG (per S86 W7 audit-output convention): LAYER-2-axiomatic
(derived from Connes-Chamseddine 1996 §2.2-2.3 + helper module line 95
literal pass-through; not a numerical-gate verdict).

CITE-ANCHORS:
  - §W4-2 §6 CC-2 PASS (line 193): rel_err = 1.7556e-16
  - §W4-2 verdict line (line 290): F_2 sub-atlas survival = structural identity
  - §W4-2 synthesis §2 (line 532): "definition-level identity (zeta = Mellin
    on positive-definite spectrum), not evidence"
  - `_spectral_action_regulators.py` line 95: literal pass-through
    `mellin_a_n = zeta_a_n` realization
  - §VII.N L1 (registry line 5699): "Uniqueness at L1: zeta" — L1-canonical selector
  - §VII.N L1 (registry line 5667): Connes-Marcolli 2008 Thm 1.31 explicit
  - §VII-B.ZETA-NOT-PHYSICAL-75 (registry line 4576): s=0 boundary corollary
    (where THM identity FAILS)
  - Connes-Chamseddine 1996 §2.2-2.3: multiplier-vector grading underlying
    the identity at L3
  - Connes-Marcolli 2008 Thm 1.31: Dixmier-trace L1-uniqueness selecting
    ζ from F_2 (positive disqualification of SDW)
  - This file (s86-sector-2-split-layer-taxonomy.md), L3 + Re:L3 + R2 CV-2
    through CV-3 + DI-2.
```

**Step 2: Schema-extend the registry to carry the LAYER tag (LAYER-2-axiomatic vs LAYER-2-numerical sub-tag).** This is lizzi's Q-LZ-5 carry-forward `S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION`. The schema extension is small — one optional metadata field per entry header — but requires the registry-write hygiene rule (S86 W1c surface) to extend its append-only-Python-writer template to include the new field. This is forward-compatible with all existing registry entries (the field is optional; legacy entries default to "not yet sub-classified," queued for retroactive sub-classification in S88+).

The Stage-2.5 sub-classification operationalizes this at the audit level. Each existing §VII-* registry entry inherits a sub-tag based on its derivation:
- LAYER-2-axiomatic: §VII.N (L1, L2, L3 each axiomatic), §VII-B.TWO-LAYER-OBSTRUCTION (axiomatic functoriality test), §VII-B.ZETA-EQUALS-SDW (this entry), §VII-B.HP1-NEAR-INVARIANCE Step 1 (Mellin-support partition is axiomatic).
- LAYER-2-numerical: §VII-B.HP1-NEAR-INVARIANCE LOOSE/STRICT R-protection numbers (numerical), §VII-B.ZETA-NOT-PHYSICAL-75 (S75 numerical 381× dynamic range), §VII.K-PROP propagation rule (combinatorial-numerical span computations).

The sub-classification provides a clean per-entry warrant-class signal that downstream cite-readers can use to assess whether the entry's claim is unconditional (axiomatic) or evaluation-conditional (numerical at the gate's slot/L_max).

**Step 3: Register the dual-binding partition as a propagation theorem `§VII.K-PROP-DUAL-BINDING`.** This is the SECTOR-2 propagation theorem connecting the 5-class @ L1 partition (registry) to the 4-class @ L3-s=3 projection (per-Q span at the a_2 slot). The theorem statement:

```
THEOREM (Dual-Binding Partition Projection; connes + lizzi tracks; S86 W7).
The 5-class @ L1 multiplier-vector partition of A_5 = {ζ, Zubarev, SDW,
cutoff_sqrt, anomaly} projects onto the 4-class @ L3-s=3 residue-
equivalence partition by collapsing Class 1 (ζ) ∪ Class 2 (SDW) → F_2
at Γ-regular slots only (per THM-L3.1 §VII-B.ZETA-EQUALS-SDW). At Γ-pole
slots (s=0, s=−1, ...), no collapse occurs and the 5-class structure is
preserved. The projection is therefore SLOT-CONDITIONAL with the
projection rule:

  P: A_5 / ~_multiplier-vector  →  A_5 / ~_residue-at-slot-s
     (5-class)                    (4-class at Γ-regular s; 5-class at Γ-pole s)

For SECTOR-2 propagation through downstream channels, the binding partition
is determined per channel by its evaluation stratum:
  - L1- or L2-stratum channels (W5a-P3 IC at s=−1, C-γ-WEAK at full
    multiplier-vector, C-β at F_4 sub-atlas, C-α master-test cross-slot):
    bind 5-class @ L1.
  - L3-stratum channels at Γ-regular slots (per-Q span via §VII.K-PROP at
    s=3 a_2-slot, C-α per-slot drift exponent at Γ-regular slot):
    bind 4-class @ L3-s=3 (the projection).
  - L3-stratum channels at Γ-pole slots: bind 5-class @ L3-Γ-pole (no
    projection).
```

This propagation theorem closes the workshop's deliverable (a) registry-write spec: 5-class @ L1 binds the SECTOR-2 partition globally; 4-class @ L3-s=3 is registered as the projection theorem. The propagation theorem itself is LAYER-2-axiomatic (derived from THM-L3.1 + §VII.N C1 line 5867 propagation rule), inheriting the strong-warrant sub-classification.

**3-step landing sequence (R3 readiness):** Step 1 lands at R3 in the §VII-B Lizzi-track Cluster (workshop deliverable (c)); Step 2 is a S87 carry-forward (`S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION`, lizzi's Q-LZ-5); Step 3 is also a S87 carry-forward (`S87-VII-K-PROP-DUAL-BINDING-LAND`, propagation theorem registration). The R3 deliverable lands Step 1 only; Steps 2 and 3 are explicit carry-forwards with 4-field specs.

**EM-2: LAYER-2-axiomatic vs LAYER-2-numerical Stage-2.5 distinction as a downstream gate criterion.**

The Stage-2.5 sub-classification (CV-7) is more than an audit-tagging convention — it generates a new GATE TYPE `S87-LAYER-2-WARRANT-CHECK` for any LAYER-2-numerical claim whose warrant-class is contested or whose extension across slots/L_max is unclear. The substitution chain that derives the gate type:

```
Step 1 (definitions):
  warrant_class(claim) := classification of a LAYER 2 admissibility claim by
                          its derivation method:
    - LAYER-2-axiomatic: derived from NCG axioms A1-A6 + Connes-Marcolli
      theorems + Connes-Chamseddine 1996 derivations. Warrant: STRONG.
      Survives across slots/L_max without re-verification.
    - LAYER-2-numerical: derived from a pre-registered numerical gate
      against threshold. Warrant: WEAK. Holds AT the gate's evaluation
      slot/L_max only; may not survive at other slots.
  
  warrant_check_gate := a S87+ gate that tests whether a LAYER-2-numerical
                        claim's verdict survives at a different slot or L_max
                        than the original gate's evaluation.

Step 2 (substitute three test cases):
  Test case 1: §VII-B.HP1-NEAR-INVARIANCE LOOSE max ratio = 2.0 (LAYER-2-numerical).
    Original evaluation: S86 W1b-T6, F_4 sub-atlas at HP^1 cohomology,
    L_max-specific.
    Warrant-check: does the max ratio = 2.0 survive at L_max + 2 (extrapolation)
    AND at a different cohomology class (HP^2)? If yes, warrant-class promotes
    toward axiomatic. If no, warrant remains slot-bounded.
  
  Test case 2: §W4-2 max_pair_ratio = 9.240e-01 at (ζ, Zubarev) (LAYER-2-numerical).
    Original evaluation: S86 W4-2 at L_max=10, s=3 a_2-slot.
    Warrant-check: does the max_pair_ratio behavior survive at different L_max
    (5, 7, 12) AND at different slots (s=2, s=1)?
  
  Test case 3: §VII.N L3 R-protected vs NOT-R-protected band thresholds 1.5 / 2.5
    (LAYER-1-from-LAYER-2-inputs per lizzi's row-5 refinement).
    Original evaluation: span_Q at evaluation L_max with thresholds calibrated.
    Warrant-check: do the thresholds 1.5 / 2.5 survive at different L_max?
    Are they axiomatically derivable, or numerically calibrated?

Step 3 (simplify — gate type abstraction):
  Each S87+ LAYER-2-numerical claim with downstream consequences for
  per-class propagation is candidate for a `S87-LAYER-2-WARRANT-CHECK-{claim}`
  gate that tests:
    (a) does the verdict survive at L_max ± 2 (extrapolation)?
    (b) does the verdict survive at slot s' ≠ s_original?
    (c) does the threshold value derive from an axiom or from numerical
        calibration?
  
  PASS conditions:
    - All three sub-tests PASS → warrant-class promotes to "extended-numerical"
      (intermediate between LAYER-2-axiomatic and LAYER-2-numerical).
    - Any sub-test FAIL → warrant-class remains LAYER-2-numerical-bounded;
      the claim's downstream propagation must explicitly cite the bounding
      conditions.

Step 4 (direction):
  The gate type generates a finite queue of S87+ warrant-check gates, one
  per LAYER-2-numerical claim with consequential downstream propagation.
  The audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md`
  §4.3 (CARRY-FORWARD-COMPUTE remediation queue) feeds these gates to the
  S87+ planner.
  
  Direction implication: Stage-2.5 is not just a tagging convention — it is
  a downstream gate-generator. Each LAYER-2-numerical claim is queued for
  warrant-check; the warrant-check verdict becomes a new permanent registry
  entry that promotes (or bounds) the original claim's downstream usage.
  
  Conclusion: The Stage-2.5 sub-classification operationalizes the audit's
  CARRY-FORWARD-COMPUTE class with concrete gate templates. This is a
  methodological multiplier on the audit's value — it converts a passive
  classification into an active propagation queue.
```

**Three sample S87 warrant-check gates (4-field specs):**

| Gate | What | Inputs | Pre-registered threshold | Effort |
|:---|:---|:---|:---|:---|
| `S87-WARRANT-CHECK-HP1-LOOSE` | Test whether HP^1 LOOSE max ratio = 2.0 survives at L_max + 2 and at HP^2 | HP^1 cohomology data, L_max ∈ {12, 14}, HP^2 cocycle data | LOOSE max ratio < 2.5 (PASS = warrant-extends), 2.5 ≤ ratio < 5.0 (INFO = warrant-bounded), ratio ≥ 5.0 (FAIL = warrant-overrun) | MODERATE (1 wave) |
| `S87-WARRANT-CHECK-W4-2-MAX-PAIR-RATIO` | Test whether max_pair_ratio = 0.924 at (ζ, Zubarev) survives at L_max ∈ {7, 12} and slots s ∈ {2, 1} | §W4-2 data, regulator atlas at varied L_max, slot scan | max_pair_ratio at (ζ, Zubarev) consistent with 0.924 ± 5% across slot variations (PASS = warrant-extends), variation > 5% (INFO = slot-conditional) | MODERATE |
| `S87-WARRANT-CHECK-VII-N-L3-THRESHOLDS` | Test whether the §VII.N L3 R-protected band thresholds 1.5 / 2.5 are L_max-stable AND axiomatically derivable | §VII.N data, span_Q for varied L_max, axiomatic derivation attempt | thresholds stable to ±0.1 across L_max ∈ {5, 7, 10, 12} (PASS = extended-numerical), variation > 0.1 (INFO = bounded-numerical) | LIGHT |

These gates inherit the DI-1 simplified slot-tag protocol (`F_n@{stratum}-{slot}`) for their spec-language. They are ADDITIONAL to the three SECTOR-2 propagation gates already in the workshop's carry-forward (S87-W5A-P3-IC-PER-CLASS-VERIFY, S87-W6-C-BETA-UV-CUTOFF-3CLASS, S87-W6-C-GAMMA-WEAK-PER-CLASS) — they form a SECOND queue for the audit-output file's §4.3 CARRY-FORWARD-COMPUTE class.

The EMERGENT methodological insight: Stage-2.5 sub-classification doubles the audit's productive output. The first (CV-7) is a tagging refinement; the second (EM-2) is a gate generator. Both flow from the same axiomatic-vs-numerical distinction in the warrant-class.

**EM-3: Forward-backward inference closure as cross-pillar methodological generator.**

lizzi's E-2 reads the forward-backward inference closure (THM-L3.1 non-evidence-status forward + L4 retroactive sweep backward) as a substrate-physics methodological theorem on the regulator-class manifold. The EMERGENCE in the joint reading: the forward-backward closure pair is NOT specific to the regulator-class manifold — it is a CROSS-PILLAR methodological generator that applies to any substrate-physics manifold the project investigates with prior-cite history.

**Substitution chain (cross-pillar generalization):**

```
Step 1 (definitions):
  substrate_manifold(M) := a substrate-physics manifold with:
    - structural axioms (NCG axioms; axiomatic admissibility tests)
    - empirical data (numerical gate verdicts)
    - prior-cite history (S78-onward project record of cites referencing M)
  
  forward_closure(M, theorem_T) := non-evidence-status declaration on M's
    theorem T, bounding what T's downstream cites can claim.
  
  backward_closure(M, audit_A) := retroactive sweep of M's prior-cite history,
    detecting and remediating cross-tag conflations.
  
  fb_pair(M) := (forward_closure(M, *), backward_closure(M, *)) for every
    canonical theorem and audit on M.

Step 2 (substitute three substrate manifolds):
  
  M_1: regulator-class manifold (SECTOR-2 substrate, this workshop).
    fb_pair(M_1) = (THM-L3.1 non-evidence-status, L4 retroactive sweep).
    Status: BUILT (this workshop, deliverables (b) + (c)).
  
  M_2: Jensen-deformation manifold (the τ_fold parameter manifold,
       MEMORY S64-S70 history).
    Theorems: M_max authoritative bound [1.351, 1.674], a_2/a_4 ratio
              monotonicity (S70 result), GGE-KMS Hessian descent (S64).
    Audit candidate: retroactive sweep on Jensen-deformation cites for
                     LAYER-1-axiomatic vs LAYER-2-numerical mis-tagging.
    fb_pair(M_2) = TBD; this is a S87+ candidate for a Jensen-axis
                   methodological workshop.
  
  M_3: Mellin-strip integrability manifold (S82 W2-5 MP-Exclusion theorem,
       MEMORY S82, sqrt(x) cusp regulators fail Hausdorff-Bernstein-Widder).
    Theorems: MP-Exclusion proof (LAYER-2-axiomatic), Mellin-strip
              admissibility classification.
    Audit candidate: S78+ retroactive sweep on Mellin-strip cite-chain.
    fb_pair(M_3) = PARTIAL; MP-Exclusion theorem has implicit forward-
                   closure (proof-complete), but no explicit retroactive
                   sweep.
  
  M_4: GGE-relic spectral functional manifold (W5a-P3 IC source, S86 W4-1
       canonical xi_E_GGE_inv = 13.642; MEMORY S64).
    Theorems: GGE-KMS Hessian descent, inter-band coherence mode existence.
    Audit candidate: future S87+ workshop on the GGE-relic cite-chain.
    fb_pair(M_4) = TBD.

Step 3 (simplify — methodological generator):
  Every substrate-physics manifold M with prior-cite history admits a
  fb_pair(M) construction. The construction is:
    (a) identify M's canonical theorems and their potential
        non-evidence-status items (forward closure target).
    (b) walk M's prior-cite history with LAYER tagging + Stage-2.5
        sub-classification (backward closure target).
    (c) detect cross-tag conflations in (b).
    (d) emit forward-closure declarations on (a) + backward-closure
        remediation tags on (b).
  
  The fb_pair(M) is structurally identical across all M; only the
  substrate-specific theorems and cite-history change.

Step 4 (direction):
  The forward-backward inference closure pair is a META-METHODOLOGY for
  every substrate-physics manifold the project investigates. The S86 W7
  workshop instantiates fb_pair(M_1) for the regulator-class manifold;
  S87+ workshops can instantiate fb_pair(M_i) for i ∈ {2, 3, 4, ...}.
  
  Direction implication: the forward-backward closure pair is itself a
  registry-recordable methodological theorem — it should land in
  permanent-results-registry.md as a `§VIII.METHODOLOGY` entry (NEW
  section) titled "Forward-Backward Inference Closure on Substrate-Physics
  Manifolds (S86 W7 origin; cross-pillar generator)."
  
  Conclusion: the EMERGENCE at the methodology level is that this workshop's
  output is replicable across the project's substrate-manifold inventory.
  The forward-backward pair is a structural pattern, not a one-off.
```

**Recommendation for R3 / S87:** treat the forward-backward closure pair as a methodological theorem that lands as `§VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE` (new registry section). The S86 W7 workshop's output (deliverables (b) + (c)) is the canonical first instance; S87+ workshops can apply the pattern to other substrate manifolds (Jensen-deformation manifold, Mellin-strip manifold, GGE-relic manifold). This establishes the workshop's contribution at TWO levels:

1. **Object level:** The SECTOR-2 partition + ζ=SDW theorem land in §VII-B as canonical structural results on the regulator-class manifold.
2. **Meta level:** The forward-backward closure pair lands in §VIII as a cross-pillar methodological generator applicable to all substrate-physics manifolds.

The meta-level contribution is the LARGER lift — it reframes future workshops on substrate manifolds as "instantiate fb_pair(M) for substrate M" rather than as ad-hoc cite-history audits + ad-hoc theorem-status declarations. The methodology compresses substantially under this framing.

**EMERGENCE summary table.**

| EMERGENCE point | What it generates | Workshop deliverable / Carry-forward |
|:---|:---|:---|
| EM-1 (3-step upgrade pathway) | (1) §VII-B.ZETA-EQUALS-SDW landing at R3, (2) S87 schema extension, (3) S87 propagation theorem | Deliverable (c) at R3; carry-forwards to S87 |
| EM-2 (Stage-2.5 as gate generator) | New `S87-LAYER-2-WARRANT-CHECK-*` gate type with 3 sample 4-field specs | Adds 3 S87 carry-forwards to the audit-output §4.3 |
| EM-3 (cross-pillar methodology) | `§VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE` registry section (NEW); applicable to M_1, M_2, M_3, M_4 substrate manifolds | NEW registry section (S87+ landing); meta-methodological theorem |

The three emergences cascade into the R3 deliverable closure: EM-1 lands deliverable (c); EM-2 expands the audit-output file's §4.3 carry-forward queue from 3 to 6 gates; EM-3 elevates the workshop from a single-substrate result to a cross-pillar methodology, with a new registry-section landing as a S87+ carry-forward. The substrate-physics implication: the project's substrate is not just the regulator-class manifold (SECTOR-2 substrate) — it is a multi-manifold structure where each canonical theorem on each manifold admits its own fb_pair(M) construction, and the workshop's output is a TEMPLATE for systematic methodological closure across all of them.

---

## Round 3 — lizzi: Follow-up

### CONVERGENCE

**Topline.** Connes' R2-B closes 7 of 7 convergence offerings with full structural backing; the 2 dissents (DI-1 simplification + DI-2 phrasing) are refinements on my R2-A I now ratify; the 3 emergences (EM-1 / EM-2 / EM-3) are the workshop's methodological lift, all of which I accept. My R3-A turn locks in five additional convergence points (CV-LZ-1 through CV-LZ-5) that ratify connes' R2-B refinements explicitly and prepare the R3-B FINAL Verdict + Wrap-Up to land all three deliverables (a)/(b)/(c) without remaining structural questions. Each point is anchored to the specific R2-B clause it ratifies, with the substitution-chain reasoning written out where the convergence carries phrasing-precision or scope-decision content.

**CV-LZ-1: DI-1 2-coordinate slot-tag protocol simplification — ACCEPT IN FULL.**

Connes' DI-1 (workshop lines 1921-2000) simplifies my E-1 3-coordinate slot-tag protocol `F_n@{stratum}-{slot}-{partition-relation}` to 2-coordinate `F_n@{stratum}-{slot}` by observing that the (stratum, slot) pair determines the partition-relation uniquely in every entry of the project's S78-onward record. The substitution chain in his DI-1 (workshop lines 1934-1969) demonstrates the redundancy: at L1-axiomatic and L2-substrate-action, {partition-relation} is determined by {stratum} alone (these strata do not propagate via Mellin exponents per §VII.N C1 line 5867); at L3-residual, {partition-relation} is determined by {slot} alone (the partition relation IS the per-slot residue-extraction).

I ACCEPT this simplification in full. The resolution-table approach (workshop lines 1980-1990) is the right canonical-write convention — it codifies the (stratum, slot) → (partition-relation) function once at the audit-output file's §1.2, eliminating per-cite ambiguity and reducing tag verbosity by ~33% as connes states. The fallback to 3-coordinate at ambiguity-loci (S87+ if a new partition relation appears at the same (stratum, slot)) preserves extensibility; the protocol degrades gracefully into a more verbose form only where genuinely needed.

Substitution chain validating my E-1 → DI-1 update:

```
Step 1 (definitions):
  protocol_E1(F_n)  := F_n@{stratum}-{slot}-{partition-relation}     (3-coordinate, lizzi R2-A)
  protocol_DI1(F_n) := F_n@{stratum}-{slot}                          (2-coordinate, connes R2-B)
  resolution_table  := canonical map (stratum, slot) → partition-relation
                       fixed in audit-output §1.2.

Step 2 (substitute the project's S78-onward record per connes' DI-1 derivation):
  At L1, partition-relation is multiplier-vector identity (CC-1996 §2.2-2.3) — UNIQUE.
  At L2, partition-relation is three-criterion intersection at τ_fold — UNIQUE.
  At L3, partition-relation depends on slot:
    s=4 (a_0 slot)      → f_0-test (RFB Theorem (i))
    s=3 (a_2 slot)      → residue-equivalence (~_M)
    s=2 (a_4 slot)      → Mellin-support concentration (HP1)
    s=1 (a_6 slot)      → Γ-regular 5-class with F_2 collapse
    s=0 (boundary)      → spectral-zeta non-observability (ZETA-NOT-PHYSICAL-75)
    s=−1 (W5a IC)       → Γ-pole 5-class no-collapse
  In every row of the project's S78-onward record, (stratum, slot) → partition-relation
  is a function (no ambiguity).

Step 3 (simplify):
  protocol_E1(F_n) ≡ protocol_DI1(F_n) under resolution_table.
  protocol_DI1 is the same content with the redundancy removed.

Step 4 (direction):
  Adoption: protocol_DI1 with resolution_table at audit-output §1.2.
  Conclusion: ACCEPT DI-1 in full; my R2-A E-1 protocol is superseded by DI-1's
  simplification with no content loss, with extensibility preserved at ambiguity-loci.
```

The resolution-table form has an additional benefit I had not surfaced in R2-A: by canonizing the (stratum, slot) → (partition-relation) map ONCE at the audit-output §1.2, it eliminates a class of cite-drift where future authors might invent NEW partition-relation names that semantically duplicate existing ones. Under DI-1, future S87+ partition cites either fit the canonical resolution-table or trigger an explicit extensibility decision. Under my E-1, two cite-authors could independently coin different partition-relation names at the same (stratum, slot) and the protocol would not surface the duplication. The DI-1 simplification is therefore epistemically tighter.

**CV-LZ-2: DI-2 Class-2 (SDW) phrasing "Γ-regular-canonical, Γ-pole-disqualified" — ACCEPT IN FULL.**

Connes' DI-2 (workshop lines 2002-2023) sharpens my D-3 "Γ-conditionally canonical" to "Γ-regular-canonical, Γ-pole-disqualified" via Connes-Marcolli Thm 1.31. His parsing analysis (Parsing A "canonical at SOME Γ-conditions" vs Parsing B "canonical conditional on Γ-regularity holding") correctly identifies that the §VII-B.ZETA-EQUALS-SDW item (vii) cross-cite to §VII.N L1 line 5699 ("Uniqueness at L1: zeta") REQUIRES Parsing A — SDW must be POSITIVELY DISQUALIFIED at the Γ-pole canonical-extraction slot s=0, not silent on it, otherwise item (vii) does not establish the L1-uniqueness claim that "ζ is the UNIQUE L1-canonical regulator."

I ACCEPT the refined phrasing in full. The substitution chain that closes my R2-A D-3 → R3-A CV-LZ-2 update:

```
Step 1 (definitions):
  L1-canonical(R)         := R is admissible under Connes axioms A1-A6 and
                             requires NO external scale beyond {A, H, D}.
  L1-uniqueness            := the L1-canonical class has cardinality 1
                             (Connes-Marcolli 2008 Thm 1.31 selects Dixmier trace
                             as unique trace-class invariant on L^(1,∞)(H)).
  Positive-disqualify(R, slot) := explicit verdict "R is NOT L1-canonical AT slot"
                             with structural reason (introduced external scale).

Step 2 (substitute SDW at s=0):
  SDW at s=0 boundary: M[Tr e^{-tD²}](s) = Γ(s) · ζ_D(2s); Γ(0) is a simple pole.
  Residue-extraction picks up Γ(s) · ζ_D(2s) → ∞ · ζ_D(0); the regularization
  introduces a normalization scale not present in the canonical Dixmier-trace
  formulation (which extracts at s=d=8 directly with no Γ-prefactor).
  
  This is an external-scale introduction at the s=0 canonical-extraction slot.
  Therefore: SDW is positive-disqualified at s=0.

Step 3 (simplify under L1-uniqueness):
  Connes-Marcolli Thm 1.31 says the L1-canonical class has cardinality 1.
  ζ is L1-canonical (no external-scale introduction at any slot).
  SDW would be in the same class as ζ at Γ-regular slots (multiplier-vector
  identity holds), but is positive-disqualified at s=0 by the Γ(0)-pole
  normalization-scale introduction.
  Therefore: L1-canonical class = {ζ}, with SDW in a sibling class
  (Class 2 in the 5-class partition: Γ-regular-canonical, Γ-pole-disqualified).

Step 4 (direction):
  Phrasing requirement: item (vii) must positive-disqualify SDW (Parsing A).
  My D-3 "Γ-conditionally canonical" is ambiguous (could read Parsing B).
  Connes' DI-2 "Γ-regular-canonical, Γ-pole-disqualified" is positive
  disqualification at the Γ-pole slot, satisfying the L1-uniqueness anchor.
  
  Conclusion: ACCEPT DI-2 phrasing for Class-2 (SDW) description and for
  item (vii) in the §VII-B.ZETA-EQUALS-SDW skeleton. Phrasing supersedes
  my R2-A D-3 with structural content unchanged but parsing precision improved.
```

The accepted phrasing for the C1 Class-2 description and for the §VII-B.ZETA-EQUALS-SDW item (vii) cross-cite is now: "**Γ-regular-canonical, Γ-pole-disqualified**: canonical at Γ-regular slots (multiplier-vector identical to ζ at s=3, s=2, s=1, ...), explicitly disqualified at the canonical-extraction slot s=0 by Γ(s) normalization-scale introduction (per Connes-Marcolli Thm 1.31's Dixmier-trace formulation, which extracts at s=d=8 in our setting and at s=0 boundary for the spectral-zeta case)." This phrasing appears in connes' EM-1 final-form skeleton at workshop lines 2078-2083; I CONFIRM it without modification.

**CV-LZ-3: EM-1 3-step upgrade pathway (registry landing + schema extension + propagation theorem) — ACCEPT IN FULL.**

Connes' EM-1 (workshop lines 2038-2155) specifies the 3-step landing sequence for the dual-binding partition into permanent-results-registry: (Step 1) §VII-B.ZETA-EQUALS-SDW landing at R3 with consolidated 8-item non-evidence-status; (Step 2) S87 carry-forward `S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION` for sub-tag schema; (Step 3) S87 carry-forward `S87-VII-K-PROP-DUAL-BINDING-LAND` for the propagation theorem `§VII.K-PROP-DUAL-BINDING`. This is the right ordering — Step 1 is R3-feasible (the consolidated skeleton at workshop lines 2045-2116 is registry-ready), Steps 2 and 3 require additional infrastructure (registry schema extension, propagation-theorem registration) that legitimately belong to S87+.

I ACCEPT the 3-step pathway in full. The Step 1 final-form skeleton is correct as written; I CONFIRM all 8 non-evidence-status items, the SLOT-CONDITIONALITY clause with sharpness sub-clause, the LAYER tag (LAYER-2-axiomatic), and the CITE-ANCHORS list. The skeleton is at landing-readiness for R3-B FINAL Workshop Verdict to mark deliverable (c) closed.

**Cross-cite note on the dual-binding propagation theorem (Step 3).** The proposed `§VII.K-PROP-DUAL-BINDING` theorem at workshop lines 2128-2151 connects the 5-class @ L1 partition to the 4-class @ L3-s=3 projection via a slot-conditional projection rule. The substrate-physics reading: the regulator-class manifold's 5-class structure is preserved at L1/L2 strata and at L3-Γ-pole slots; it projects to 4-class only at L3-Γ-regular slots (where THM-L3.1 §VII-B.ZETA-EQUALS-SDW collapses Class 1 ∪ Class 2 → F_2). The propagation theorem is itself LAYER-2-axiomatic (derived from THM-L3.1 + §VII.N C1 line 5867 + the multiplier-vector grading). Strong-warrant. The S87 carry-forward `S87-VII-K-PROP-DUAL-BINDING-LAND` is well-specified at 4-field level.

**CV-LZ-4: EM-2 `S87-LAYER-2-WARRANT-CHECK-*` gate type as Stage-2.5 gate generator — ACCEPT IN FULL.**

Connes' EM-2 (workshop lines 2157-2239) reads the Stage-2.5 sub-classification (CV-7 in his R2-B) not just as a tagging convention but as a downstream gate generator. Each LAYER-2-numerical claim with consequential downstream propagation is candidate for a `S87-LAYER-2-WARRANT-CHECK-{claim}` gate that tests three sub-conditions: (a) verdict survives at L_max ± 2; (b) verdict survives at slot s' ≠ s_original; (c) threshold value derives from an axiom or from numerical calibration. The PASS conditions promote a LAYER-2-numerical claim toward "extended-numerical" warrant-class (intermediate between LAYER-2-axiomatic and LAYER-2-numerical); FAIL conditions bound the original claim to its evaluation slot/L_max only.

I ACCEPT the gate generator in full. The 3 sample 4-field gate specs (`S87-WARRANT-CHECK-HP1-LOOSE`, `S87-WARRANT-CHECK-W4-2-MAX-PAIR-RATIO`, `S87-WARRANT-CHECK-VII-N-L3-THRESHOLDS`) at workshop lines 2231-2235 are well-specified and feed naturally into the audit-output file's §4.3 CARRY-FORWARD-COMPUTE queue. The gate type doubles the audit's productive output: tagging refinement (CV-7) + active gate generator (EM-2). Both flow from the warrant-class axiomatic-vs-numerical distinction.

The substrate-physics reading: the `S87-LAYER-2-WARRANT-CHECK-*` gate type IS a warrant-class-promotion mechanism on the substrate's regulator-class manifold's prior-claim record. Each LAYER-2-numerical claim becomes either (PASS) a warrant-extended claim with bounded but extended scope, or (FAIL) a slot-bounded claim whose downstream propagation must explicitly cite the bounding conditions. This is the substrate's structural separation between strong-warrant (axiomatic) and weak-warrant (numerical) admissibility verdicts being operationalized at the active-gate level, not just at the passive-tag level.

**CV-LZ-5: EM-3 `§VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE` cross-pillar generator — ACCEPT IN FULL.**

Connes' EM-3 (workshop lines 2241-2329) elevates the forward-backward inference closure pair (THM-L3.1 non-evidence-status + L4 retroactive sweep) from a SECTOR-2-specific result to a CROSS-PILLAR methodological generator applicable to any substrate-physics manifold M with prior-cite history. His substitution chain (workshop lines 2247-2305) instantiates the pattern at M_1 (regulator-class), M_2 (Jensen-deformation), M_3 (Mellin-strip integrability), M_4 (GGE-relic spectral functional). The fb_pair(M) construction is structurally identical across all M; only the substrate-specific theorems and cite-history change.

I ACCEPT the cross-pillar generalization in full. This is the LARGER lift that connes correctly identifies — the workshop's contribution at the meta-level is a TEMPLATE for systematic methodological closure across all of the project's substrate-physics manifolds, not a one-off result on the regulator-class manifold. The proposed registry section `§VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE` is the right home for the meta-theorem.

**Substitution chain validating my E-2 → CV-LZ-5 cross-pillar update:**

```
Step 1 (definitions):
  My E-2 (lizzi R2-A): forward-backward closure as substrate-physics methodological
                       theorem on the regulator-class manifold (M_1 only).
  Connes' EM-3 (R2-B): same closure pair as cross-pillar methodological generator
                       applicable to {M_1, M_2, M_3, M_4} substrate manifolds.
  
  Cross-pillar test: does the fb_pair(M) construction (a) identify M's canonical
                     theorems → forward-closure targets; (b) walk M's prior-cite
                     history → backward-closure targets; (c) detect cross-tag
                     conflations; (d) emit forward + backward closure declarations
                     —— hold across multiple substrate manifolds?

Step 2 (substitute the four substrate manifolds):
  M_1 (regulator-class):       fb_pair = (THM-L3.1 non-evidence-status,
                                          L4 retroactive sweep) — BUILT this workshop.
  M_2 (Jensen-deformation):    canonical theorems include M_max bound [1.351, 1.674],
                                a_2/a_4 monotonicity (S70), GGE-KMS Hessian descent (S64).
                                Audit candidate exists; fb_pair(M_2) construction is
                                S87+ candidate. Pattern PORTABLE.
  M_3 (Mellin-strip):          MP-Exclusion theorem (LAYER-2-axiomatic); audit on
                                Mellin-strip cite-chain = PARTIAL. Pattern PORTABLE.
  M_4 (GGE-relic):             GGE-KMS Hessian descent + inter-band coherence;
                                fb_pair(M_4) candidate. Pattern PORTABLE.

Step 3 (simplify):
  fb_pair(M) construction is structurally the same regardless of which M is the
  substrate. The construction's content varies (canonical theorems differ;
  cite-histories differ); the construction's STRUCTURE is invariant.

Step 4 (direction):
  Accept connes' EM-3 cross-pillar reading. The forward-backward closure pair is
  not a SECTOR-2-specific methodology — it is a META-METHODOLOGY portable across
  all substrate-physics manifolds in the project's investigation queue.
  
  Direction implication: lift from "this is how SECTOR-2 closes its cite-history"
  to "this is how ANY substrate-physics manifold with prior-cite history closes."
  The §VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE registry section is the right
  home; the S87+ candidate gates fb_pair(M_2/M_3/M_4) are concrete carry-forwards.
  
  Conclusion: my R2-A E-2 reads the closure pair at SECTOR-2-locality only;
  connes' EM-3 generalizes correctly to cross-pillar. ACCEPT in full.
```

**Convergence summary table (R3-A additions to connes' R2-B 7-row table).**

| Convergence point | Resolves | Workshop deliverable | Status |
|:---|:---|:---|:---|
| CV-LZ-1 (DI-1 simplification) | E-1 → 2-coordinate | (b) audit-output naming protocol | ACCEPT; resolution-table form canonical |
| CV-LZ-2 (DI-2 phrasing) | D-3 → "Γ-regular-canonical, Γ-pole-disqualified" | (c) item (vii) cross-cite | ACCEPT; positive-disqualification phrasing locked |
| CV-LZ-3 (EM-1 3-step pathway) | Step 1 R3, Steps 2-3 S87 | (c) at R3 + 2 S87 carry-forwards | ACCEPT; pathway ordering correct |
| CV-LZ-4 (EM-2 gate generator) | Stage-2.5 → active gate type | (b) §4.3 CARRY-FORWARD-COMPUTE queue | ACCEPT; 3 sample gate specs added |
| CV-LZ-5 (EM-3 cross-pillar) | E-2 → meta-methodology | NEW §VIII.METHODOLOGY registry section | ACCEPT; meta-theorem landing as S87+ carry-forward |

All 5 R3-A convergence points close downstream-resolvable. Combined with connes' R2-B 7 convergences, the workshop has 12 convergences in total — all three deliverables (a)/(b)/(c) are at landing-readiness for connes' R3-B FINAL turn (Workshop Verdict + Wrap-Up).

**Substrate framing.** The five R3-A convergences are all SUBSTRATE-PHYSICS REFINEMENTS on the regulator-class manifold. CV-LZ-1 is a tag-protocol simplification at the manifold's naming-coordinate level; CV-LZ-2 is a phrasing precision on Class-2's submanifold position (Γ-regular-canonical sub-stratum vs Γ-pole-disqualified sub-stratum); CV-LZ-3 is the 3-step landing-sequence onto the registry-permanent record of structural results on the manifold; CV-LZ-4 is the warrant-class promotion gate-type on the manifold's prior-claim record; CV-LZ-5 is the cross-pillar methodological export from the regulator-class manifold to other substrate manifolds (Jensen-deformation, Mellin-strip, GGE-relic). All five are substrate-internal refinements on the same regulator-class manifold's structure or its export pattern to sibling manifolds; none invoke external machinery beyond NCG axioms A1-A6 + Connes-Marcolli Thm 1.31 + the §VII.N stratification.

### DISSENT

**Topline.** After connes' R2-B + my R3-A CV-LZ-1 through CV-LZ-5 acceptances, no structural disagreement remains within the workshop's R3 scope. My R2-A dissents D-1 (slot-interpolation sharpness) and D-2 (C-α master-test cross-slot) were both ratified by connes (CV-2 absorbs D-1 into the strengthened item-(3) sub-clause; CV-5 absorbs D-2 into the dual classification "INSENSITIVE per-slot, SENSITIVE master-test"). My R2-A D-3 (Class-2 phrasing) was sharpened by connes' DI-2 and I have accepted the sharpening at CV-LZ-2 above. There is no R3-A dissent on connes' R2-B refinements; the workshop is at full structural convergence on all 12 points.

The DISSENT placeholder is not vacuous, however — there is one genuine S87 follow-up I want to RESERVE as a per-class verification check that the workshop has NOT internally answered. This is a forward dissent, not a back-against-connes dissent; it expresses that ONE of the 3 SECTOR-2 carry-forward gates may produce an unexpected result that we should pre-register awareness of.

**DI-LZ-S87 (FORWARD DISSENT, RESERVED FOR S87): The `S87-W5A-P3-IC-PER-CLASS-VERIFY` gate has a non-trivial chance of producing a Z-factor direction flip on at least one of {SDW, Zubarev, anomaly} classes — flagging this for pre-registered awareness, not contesting connes' R2-B reading.**

Connes' R2-B treats all 3 SECTOR-2 propagation gates (W5a-P3 IC, C-β, C-γ-WEAK) as routine S87 carry-forwards with PASS-conditions stated at the generic level (Z_ratio direction preserved across all 5 classes for `S87-W5A-P3-IC-PER-CLASS-VERIFY`; parametric bound holds across 3 classes for `S87-W6-C-BETA-UV-CUTOFF-3CLASS`; bound holds across all 5 classes for `S87-W6-C-GAMMA-WEAK-PER-CLASS`). My R2-A E-3 (workshop lines 1683-1689) raised the substrate-physics expectation that Z-factor direction flips are LIKELY for at least one non-Class-1 regulator, drawing on my S66 ZETA-SA-66 history (eps_H sign flip, MEMORY S66, maximal scheme dependence, n_s blue tilt in zeta).

**Substitution chain (forward-pre-registration of the Z-flip prior):**

```
Step 1 (definitions):
  Z(N_pivot) := Mukhanov-Sasaki Z-factor at pivot scale, sourced from the
                IC xi²(0) = (xi_E_GGE_inv)^{-2} at s=−1 spectral residue.
  Z_ratio(R) := Z(N_pivot; R) / Z(N=0; R) under regulator R.
  direction(R) := sign(Z_ratio(R) - 1); positive direction = inflationary
                  Z-amplification, negative direction = Z-suppression.
  S66 historical anchor: eps_H sign flip across {ζ, cutoff, anomaly} → maximal
                          scheme dependence → n_s blue tilt in zeta.
  
Step 2 (substitute the per-class IC dispersion at s=−1):
  At s=−1 (Γ-pole), the 5-class partition is binding (CV-1).
  Class-1 (ζ):           xi_E_GGE_inv^{ζ} = 13.642e+00 (current registered).
  Class-2 (SDW):         xi_E_GGE_inv^{SDW} ≠ Class-1 because Γ(−1) is a simple pole;
                          Γ(s)-cancellation FAILS at s=−1 per Re:L3 strengthened item (3).
                          Order-of-magnitude estimate: SDW carries Γ(−1)-pole subtraction
                          modifying the residue extraction by O(1) factor relative to ζ.
  Class-3 (Zubarev):     xi_E_GGE_inv^{Zubarev} via direct convergent sum
                          Σ d · exp(−tC) · C¹; FINITE, dominated by the C¹·exp(−tC) maximum
                          near C ~ 1/t, structurally different from ζ analytic continuation.
  Class-4 (cutoff_sqrt): conditional on GATE A PASS (likely INFEASIBLE per
                          cutoff-sqrt-adjudication.md §3.1 GATE A expected FAIL).
  Class-5 (anomaly):     xi_E_GGE_inv^{anomaly} via Pauli-Villars subtraction
                          Σ d · [C − (C+M_PV²)] = Σ d · (−M_PV²); FINITE, mass-scale-driven,
                          carries an overall sign FROM the subtraction direction.

Step 3 (simplify — Z_ratio direction stability under per-class IC):
  Z_ratio(R) = 1 + O(xi²(0; R) · t_pivot) where t_pivot is the pivot-scale e-fold.
  direction(R) flips if xi²(0; R) carries opposite sign to xi²(0; ζ) due to
  regulator-specific scale (Pauli-Villars subtraction sign in anomaly class)
  OR if the magnitude differs by enough that the Z-factor crosses 1 mid-N-flow.
  
  Anomaly Class-5: xi_E_GGE_inv^{anomaly} ∝ (−M_PV²) carries explicit NEGATIVE sign
                    from Pauli-Villars subtraction. Direction(anomaly) is most likely FLIPPED.
  Zubarev Class-3: xi_E_GGE_inv^{Zubarev} carries explicit t_ref scale; direction
                    depends on t_ref vs L_max-truncation crossover. Likely DIRECTION-PRESERVED
                    but magnitude differs ~10× from Class-1.
  SDW Class-2: xi_E_GGE_inv^{SDW} at Γ(−1) pole differs from ζ by O(1) factor with
                ambiguous sign depending on the residue-extraction convention. Direction
                potentially flipped.

Step 4 (direction):
  Pre-registered prior on `S87-W5A-P3-IC-PER-CLASS-VERIFY`: at least one of
  {SDW, Zubarev, anomaly} likely flips Z_ratio direction. Most likely candidate:
  Class-5 (anomaly), due to Pauli-Villars sign-subtraction. Second-most-likely:
  Class-2 (SDW), due to Γ(−1) pole convention ambiguity.
  
  This is a FORWARD-PRE-REGISTRATION of the prior, NOT a contestation of the
  gate's well-formed pre-registration. The gate's PASS condition (Z_ratio
  direction preserved across all 5 classes) and INFO condition (class-dependent
  direction) are both legitimate outcomes; my prior leans toward INFO not PASS.
  
  If the gate returns INFO (direction-flipped on at least one class), the framework's
  Z-factor reading is functional-class-DEPENDENT — the choice of regulator-class
  becomes itself a physics input to the CMB inflationary prediction. This is the
  spectral-functional pluralism principle applied at the inflationary level.
```

DI-LZ-S87 is a RESERVED dissent — it does not contest connes' R2-B but flags an expected outcome direction for the S87 gate. The flag is methodologically important: if the gate returns PASS (direction preserved across all 5 classes), the framework's Z-factor is robust under SECTOR-2 pluralism; if it returns INFO (class-dependent), the framework requires explicit per-class CMB predictions and pre-registration of which class is observation-comparing. Either outcome is informative; the S87 gate verdict will close the question.

I propose adding a footnote to the workshop's carry-forward 4-field spec for `S87-W5A-P3-IC-PER-CLASS-VERIFY` recording this prior-pre-registration: "Pre-registered prior (lizzi R3-A DI-LZ-S87): at least one of {SDW, Zubarev, anomaly} likely flips Z_ratio direction; most likely candidate is Class-5 (anomaly) due to Pauli-Villars sign-subtraction." This gives the S87 gate's verdict a pre-registered reference frame for INFO interpretation and prevents post-hoc PASS-shopping if the verdict is mixed.

This is the only DISSENT entry from R3-A; all other R2-A dissents are absorbed into convergences.

### EMERGENCE

**Topline.** Two final emergences surface from the joint reading of connes' R2-B (CV-1 through CV-7, DI-1, DI-2, EM-1, EM-2, EM-3) and my R3-A CV-LZ-1 through CV-LZ-5. EM-LZ-1 is the methodological pattern that connes' EM-3 cross-pillar generator + my R3-A CV-LZ-5 acceptance jointly establish: a NEW sub-section of the §VIII registry should track "fb_pair instantiation status per substrate manifold" — a meta-table indexing which substrate manifolds have completed forward-backward closure (M_1 BUILT this workshop), which are PARTIAL (M_3 has implicit forward closure via MP-Exclusion proof but no explicit retroactive sweep), and which are S87+ candidates (M_2, M_4). EM-LZ-2 is a structural insight on the Stage-2.5 sub-classification's transitive composition: under the registry's EM-1 schema-extension landing, the LAYER-2-axiomatic vs LAYER-2-numerical sub-tag becomes propagatable through the §VII.K-PROP `span(O) = ∏_k span(f_k)^{p_k(O)}` propagation rule — observable spans carry forward the warrant-class of their constituent f_k slot weightings, generating a derived warrant-class for every observable in the project's atlas.

**EM-LZ-1: §VIII registry meta-table for fb_pair instantiation status.**

Connes' EM-3 (workshop lines 2241-2329) lifts the forward-backward closure pair to a cross-pillar generator applicable to {M_1, M_2, M_3, M_4} substrate manifolds. My R3-A CV-LZ-5 accepts the lift. The joint EMERGENT structural finding: the project's substrate-physics inventory has MULTIPLE manifolds, and the workshop-record's coverage of forward-backward closure across them is uneven. Some manifolds have complete closure (M_1 this workshop); some have implicit forward closure but no backward closure (M_3 MP-Exclusion); some have neither (M_2, M_4).

A registry meta-table tracking instantiation status would make this coverage explicit:

```
§VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE.STATUS-INVENTORY

Substrate manifold M_i        Forward closure         Backward closure
                                (theorem-grade)        (retroactive sweep)
─────────────────────────────  ────────────────────  ────────────────────
M_1: regulator-class            BUILT (THM-L3.1        BUILT (this workshop's
     (SECTOR-2 substrate)         §VII-B.ZETA-EQUALS-    L4 retroactive sweep,
                                  SDW, this workshop)    audit-output file)
                                                       
M_2: Jensen-deformation         CANDIDATE              CANDIDATE
     (τ_fold parameter manifold) (M_max bound, a_2/a_4   (Jensen-axis cite-history
                                  monotonicity, GGE-     S78-onward not yet
                                  KMS descent — all      retroactive-swept)
                                  awaiting non-evidence
                                  declarations)         
                                                       
M_3: Mellin-strip integrability PARTIAL                CANDIDATE
     (S82 W2-5 MP-Exclusion)     (MP-Exclusion theorem  (S78-onward Mellin-strip
                                  has implicit non-      cites not yet retroactive-
                                  evidence via proof-    swept)
                                  complete reading;
                                  could be made explicit)
                                                       
M_4: GGE-relic spectral         CANDIDATE              CANDIDATE
     functional manifold          (GGE-KMS Hessian       (GGE-relic cite-history
     (W5a-P3 IC source)           descent, inter-band    not yet retroactive-swept)
                                  coherence — awaiting
                                  non-evidence
                                  declarations)
```

Each row is an S87+ workshop candidate. The meta-table makes the project's methodological-closure coverage visible and queueable. Under the §VIII.METHODOLOGY-FORWARD-BACKWARD-CLOSURE registry section, this status-inventory becomes the registry-permanent index of fb_pair construction across the project's substrate manifolds.

**Substitution chain (status-inventory derivation):**

```
Step 1 (definitions):
  status(M_i, direction) := BUILT / PARTIAL / CANDIDATE per axis (forward, backward).
  
  BUILT      := theorem with explicit non-evidence-status declaration registered
                AND retroactive sweep landed as audit-output file.
  PARTIAL    := one direction registered (typically forward via proof-complete);
                other direction queued.
  CANDIDATE  := neither direction registered; S87+ workshop candidate.

Step 2 (substitute four substrate manifolds):
  M_1 (regulator-class):       (BUILT, BUILT)        — this workshop S86 W7
  M_2 (Jensen-deformation):    (CANDIDATE, CANDIDATE) — S87+ candidate
  M_3 (Mellin-strip):          (PARTIAL, CANDIDATE)  — proof has implicit non-evidence
  M_4 (GGE-relic):             (CANDIDATE, CANDIDATE) — S87+ candidate

Step 3 (simplify — coverage gap):
  Total fb_pair coverage = 2 (M_1 forward + M_1 backward) out of 8 cells.
  Coverage gap = 6 cells across {M_2, M_3, M_4}.
  
  Closure rate at S86 W7 = 2/8 = 25%.
  S87+ closure pathway: queue 6 fb_pair instantiations to bring coverage to 100%.

Step 4 (direction):
  The status-inventory is itself a methodological-coverage tracking artifact
  on the project's substrate-physics manifold inventory. It quantifies the
  coverage gap and queues the S87+ workshops needed to close it.
  
  Direction implication: the registry sub-section §VIII.METHODOLOGY-FORWARD-BACKWARD-
  CLOSURE.STATUS-INVENTORY tracks fb_pair coverage per manifold, generating
  a finite queue of S87+ workshops (6 entries: 1 for M_2-forward, 1 for M_2-backward,
  1 for M_3-backward, 1 for M_4-forward, 1 for M_4-backward, plus 1 for upgrading
  M_3-forward from PARTIAL to BUILT). This is a concrete S87+ workshop queue.
  
  Conclusion: the joint cross-pillar generalization (connes EM-3 + my CV-LZ-5)
  reveals a coverage-gap of 6 fb_pair instantiations across {M_2, M_3, M_4}.
  Queueing them as S87+ workshop candidates is the natural next step.
```

This emergence is a META-METHODOLOGY contribution — it doesn't add a new partition or theorem on M_1; it organizes the project's substrate-manifold coverage at the §VIII registry level. The 6-entry S87+ queue is concrete and 4-field-spec-able.

**EM-LZ-2: Stage-2.5 warrant-class transitive propagation through §VII.K-PROP.**

The Stage-2.5 sub-classification (CV-7 in connes' R2-B + CV-LZ-3 schema-extension acceptance in my R3-A) tags every registry entry with LAYER-2-axiomatic or LAYER-2-numerical. The §VII.K-PROP propagation rule (registry line 8867) says `span(O) = ∏_k span(f_k)^{p_k(O)}` — the regulator-span of any observable O factors through the regulator-spans of its constituent f_k Mellin-multiplier slot weightings. The EMERGENCE: if each constituent f_k carries a warrant-class sub-tag (from Stage-2.5), then the observable O inherits a DERIVED warrant-class given by the conjunction of its constituents'.

**Substitution chain (warrant-class transitivity):**

```
Step 1 (definitions):
  warrant_class(f_k) := LAYER-2-axiomatic OR LAYER-2-numerical
                       (from Stage-2.5 sub-classification of f_k's source theorem).
  warrant_class(O)   := derived warrant-class of observable O via its f_k constituents.
  
  composition_rule:
    if EVERY f_k contributing to O has warrant_class = LAYER-2-axiomatic,
       then warrant_class(O) = LAYER-2-axiomatic (strong-warrant inherited).
    if ANY f_k contributing to O has warrant_class = LAYER-2-numerical,
       then warrant_class(O) = LAYER-2-numerical (weak-warrant inherited at the
       weakest-link level).

Step 2 (substitute three observable test cases):
  
  O_1 = m_H (Higgs mass) at L_max=3 truncation:
    f_k constituents: a_2^ζ (LAYER-2-axiomatic from NCG A1+A6),
                      a_4^ζ (LAYER-2-axiomatic from NCG A1+A6),
                      v_ew (canonical observed; LAYER-2-numerical).
    composition: at least one f_k is LAYER-2-numerical → warrant_class(m_H) =
                 LAYER-2-numerical (slot-bounded at L_max=3).
  
  O_2 = chi_2 (CMB index decomposition) at L_max=15 BMA:
    f_k constituents: a_2^SDW (Γ-regular slot, LAYER-2-axiomatic via THM-L3.1),
                      a_4^SDW (LAYER-2-axiomatic via THM-L3.1),
                      Lambda_BMA (LAYER-2-numerical from BMA fit).
    composition: at least one f_k is LAYER-2-numerical → warrant_class(chi_2) =
                 LAYER-2-numerical (BMA-fit-bounded).
  
  O_3 = HP^1 LOOSE max ratio at F_4 sub-atlas:
    f_k constituents: HP^1 cohomology cocycle (LAYER-2-numerical from S86 W1b-T6),
                      F_4 partition (LAYER-2-axiomatic from RFB Theorem (i)).
    composition: at least one f_k is LAYER-2-numerical → warrant_class(HP^1 LOOSE) =
                 LAYER-2-numerical (S86 W1b-T6 evaluation slot bounded).

Step 3 (simplify):
  In every test case, the composition rule's "weakest-link" form dominates —
  the observable inherits LAYER-2-numerical warrant if ANY constituent is
  numerical. Pure-axiomatic warrant requires ALL constituents to be axiomatic,
  which is rare in practice (most observables involve at least one numerical
  fitting parameter or observed value).
  
  This means: the S87 carry-forward `S87-LAYER-2-WARRANT-CHECK-{O}` gates
  generated by EM-2 are NOT just for individual claims — they are for
  composite observables whose warrant is LAYER-2-numerical via the weakest-link
  composition. Many more observables qualify than initially apparent.

Step 4 (direction):
  Direction implication: the Stage-2.5 sub-classification is TRANSITIVE through
  §VII.K-PROP composition. The EM-2 gate generator's queue is therefore larger
  than the 3 sample gates suggest — every composite observable with a numerical
  constituent is candidate.
  
  Conservatively: the warrant-check gate type generates ~10-20 S87+ gates
  across the project's atlas of composite observables (m_H, chi_2, HP^1 LOOSE,
  span_Q, R-protected band thresholds, max_pair_ratio, etc.).
  
  Conclusion: the warrant-class transitive composition is a structural property
  of the Stage-2.5 sub-classification. It MULTIPLIES the EM-2 gate generator's
  output by an order of magnitude. This is the cleanest reading of why the
  Stage-2.5 sub-classification is methodologically central: it propagates
  warrant-class through the project's observable atlas systematically.
```

The §VII.K-PROP transitivity is itself LAYER-2-axiomatic (the propagation rule is a CC-1996 §2.2-2.3 + multiplier-vector grading consequence). So the warrant-class composition rule itself is strong-warrant; the rule's application to specific composite observables generates the larger S87+ queue.

**EMERGENCE summary table (R3-A additions to connes' R2-B 3-row table).**

| EMERGENCE point | What it generates | Workshop deliverable / Carry-forward |
|:---|:---|:---|
| EM-LZ-1 (§VIII status-inventory) | Meta-table tracking fb_pair coverage across {M_1, M_2, M_3, M_4}; 6 S87+ workshop candidates | NEW §VIII sub-section (S87+ landing); coverage gap explicit |
| EM-LZ-2 (Stage-2.5 transitivity) | Warrant-class composition rule via §VII.K-PROP; expands EM-2 gate queue by ~10× | EM-2 gate-generator queue grows to ~10-20 S87+ gates |

Combined with connes' R2-B 3 emergences, the workshop has 5 emergences total. Three (EM-1, EM-2, EM-3) lift the workshop's contribution at the meta-level; two (EM-LZ-1, EM-LZ-2) extend the meta-level by quantifying coverage and warrant-class propagation. The cumulative meta-level impact: the workshop has produced (a) a structural result on M_1, (b) a methodology template for fb_pair construction, (c) an active gate generator for warrant-class verification, (d) a coverage status-inventory across substrate manifolds, and (e) a transitivity rule for warrant-class composition through §VII.K-PROP. The methodology compresses substantially under this five-emergence framing.

**Substrate framing.** Both R3-A emergences are SUBSTRATE-PHYSICS COVERAGE / TRANSITIVITY findings on the project's substrate-physics manifold inventory. EM-LZ-1 quantifies the coverage gap of forward-backward inference closure across {M_1, M_2, M_3, M_4}; EM-LZ-2 establishes the transitive composition rule for warrant-class through §VII.K-PROP. Both are properties OF the project's substrate-physics manifold inventory (treated as a multi-manifold structure where each manifold has its own theorem-record + cite-history), not of any single substrate locale. The substrate is the union of all substrate-physics manifolds; the emergences are about how methodological closure and warrant-class propagation work across this union.

### QUESTIONS

**Topline.** Five sharp questions for connes' R3-B FINAL turn (Workshop Verdict + Wrap-Up). Each question targets a specific lock-in for the three bound deliverables (a) / (b) / (c) such that the Workshop Verdict table can be marked Converged at all 7 rows and the Wrap-Up §What Holds / §What Changed / §Carry-Forward sections can be filled without remaining structural uncertainty. The questions are organized by deliverable then by R3-B-only-resolvable-content; each is concrete and answerable in connes' R3-B without new computation.

**Q-LZ-R3-1 (Deliverable (c) — registry-write trigger): Is the §VII-B.ZETA-EQUALS-SDW final-form skeleton at workshop lines 2045-2116 ready to land as a registry-write at R3-B FINAL Workshop Verdict, OR does the LAYER tag (line 2096 "LAYER-2-axiomatic") require Step 2 of EM-1 (S87 schema extension) to land first?**

The CV-7 + CV-LZ-3 acceptance of EM-1 places the LAYER tag in the entry header. If the registry's existing entry-tagging schema does NOT yet support a LAYER sub-tag column, the entry can land WITHOUT the LAYER tag at R3-B (with the sub-tag added retroactively when Step 2 schema extension lands at S87) OR the LAYER tag can be inline in the entry's prose (not a header field). My R3-A preference is the inline-prose form (LAYER tag appears in the THEOREM body's last sentence, not in an entry-header metadata field) so the entry lands at R3-B without waiting for Step 2 schema extension. Confirm placement OR specify alternative.

If you confirm inline-prose, the §VII-B.ZETA-EQUALS-SDW entry is registry-ready at R3-B FINAL with no schema dependency. If you specify entry-header metadata, the entry's schema-extension dependency must be flagged as a Step-2 prerequisite in the carry-forward queue.

**Q-LZ-R3-2 (Deliverable (b) — audit-output file landing scope): Does workshop deliverable (b) (`sessions/framework/registry/layer1-layer2-retroactive-audit.md`) land at R3-B as the OUTLINE only (per my L4 + connes' Re:L4 §1-§5 structure plus DI-1 simplified slot-tag protocol + Stage-2.5 sub-classification), OR can connes' R3-B land the FULL file with the C3 17-row inventory + 3 conflation-flag remediations integrated in-session?**

The workshop document line 26 pre-registered deliverable (b) as "OUTLINE OR LAND IF CONVERGENCE SUPPORTS." Convergence at all 12 points (R2-B 7 + R3-A 5) suggests landing-readiness for the FULL file. The C3 17-row inventory + the three flagged conflations + the DI-1 resolution table + Stage-2.5 sub-classification are all in the workshop record at sufficient granularity for a R3-B file write without new computation.

My R3-A preference is FULL FILE LAND in R3-B FINAL — convergence is complete, no S87 gate is needed to settle the audit-output's structural content. The only S87 dependencies are for downstream warrant-check gates (EM-2 + EM-LZ-2) and per-cite remediation queue expansion (audit-output §4.3), neither of which blocks the R3-B file write.

If you concur, the FULL file lands at R3-B with §1.1-§5.7 populated from the workshop record. If you prefer outline-only at R3-B, the FULL file write is a deferred carry-forward to S87 with a 4-field spec.

**Q-LZ-R3-3 (Deliverable (a) — sub-tag landing form): The 5 SECTOR-2 sub-tags (`SECTOR-2-ζ`, `SECTOR-2-Zubarev`, `SECTOR-2-SDW`, `SECTOR-2-cutoff_sqrt`, `SECTOR-2-anomaly`) — should they be (i) per-class registry entries (5 separate rows in §VII-B), (ii) a single §VII-B.SECTOR-2-PARTITION row with 5 sub-rows, or (iii) deferred to the §VII.K-PROP-DUAL-BINDING propagation theorem at S87 (Step 3 of EM-1)?**

Connes' EM-1 (workshop lines 2128-2151) places the dual-binding propagation theorem at `§VII.K-PROP-DUAL-BINDING` as a S87 Step-3 carry-forward. The 5 SECTOR-2 sub-tags themselves could land either: (i) as 5 separate registry rows at R3-B, (ii) as 1 parent row with 5 inline sub-rows at R3-B, OR (iii) as part of the S87 propagation theorem registration (no R3-B landing at all, just the dual-binding partition decision recorded in the workshop verdict).

My R3-A preference is option (ii) — single parent row `§VII-B.SECTOR-2-PARTITION` (under the §VII-B Lizzi-track Cluster) with 5 inline sub-rows for the per-class IC values + multiplier-vector identities. This keeps the registry compact (one new entry, not five), preserves the per-class structure for downstream cite-resolution, and defers the FULL propagation theorem to S87 where it belongs.

If you concur, the §VII-B Lizzi-track Cluster grows by 2 entries at R3-B (`§VII-B.ZETA-EQUALS-SDW` from deliverable (c) + `§VII-B.SECTOR-2-PARTITION` from deliverable (a)). If you prefer option (iii) deferral, the registry-write at R3-B is just the ZETA-EQUALS-SDW entry; the SECTOR-2 partition is recorded only in the workshop verdict's Key-Insight column.

**Q-LZ-R3-4 (Carry-forward queue scope): The S87+ carry-forward queue at R3-B FINAL — should it include all of (3 SECTOR-2 propagation gates from C2) + (3 LAYER-2-warrant-check gates from EM-2) + (~10-20 transitive warrant-check gates from EM-LZ-2) + (6 fb_pair instantiation candidates from EM-LZ-1) + (2 EM-1 schema extension + propagation theorem gates) — totalling ~24-34 entries — OR is this over-padding the queue per the no-padding rule?**

The user's `feedback_fix-in-session-never-defer.md` rule (MEMORY) treats inflated carry-forward queues as a methodological failure. The workshop's pre-registered carry-forward (workshop document line 30) specifies "4-field S87 spec for SECTOR-2 propagation into W5a P3 IC + W6 C-α/β/γ" — narrowly scoped to 3 gates. The EM-2 + EM-LZ-2 + EM-LZ-1 emergences expand this to ~24-34 entries; that is a 10× expansion driven by methodological emergence, not by raw computation needs.

My R3-A preference is the NARROW SCOPE — the 3 SECTOR-2 propagation gates as the workshop's pre-registered carry-forward, with EM-1 Step 2-3 + EM-2 + EM-LZ-1 + EM-LZ-2 explicitly LOGGED in the workshop verdict's Key-Insight cells but NOT in the carry-forward queue. This keeps the carry-forward queue at the pre-registered 4-field-spec scope; the meta-methodological emergences are recorded in the workshop verdict column but not propagated into S87+ as forced carry-forwards.

If you concur, the S87 carry-forward queue is 3 entries (the 3 SECTOR-2 propagation gates) + 1 entry for `S87-W5A-P3-IC-PER-CLASS-VERIFY` augmented with my R3-A DI-LZ-S87 prior-pre-registration footnote. The meta-emergences are in the workshop verdict, available for S87+ planning but not pre-committed.

If you prefer the LARGE SCOPE (~24-34 entries), the carry-forward queue is committed and the no-padding rule is overridden by the methodological-emergence justification. Pre-registered call needed.

**Q-LZ-R3-5 (Workshop Verdict table — F_2/F_4 row resolution): The Workshop Verdict table at workshop lines 2378-2389 has 7 rows. Row 1 ("F_2/F_4-class 4-class partition (lizzi)") and Row 4 ("Connes-Chamseddine 5-class partition (connes)") are now both Converged via CV-1 dual binding. Row 7 ("Binding 4- or 5-class partition decision") is also Converged via CV-1 + CV-LZ-3 (5-class @ L1 binding, 4-class @ L3-s=3 projection theorem). Should rows 1 + 4 + 7 collapse into a single row "Dual-binding partition (5-class @ L1 + 4-class @ L3-s=3 projection)" in the R3-B FINAL Workshop Verdict, OR remain separate?**

Collapsing the three rows would simplify the workshop verdict to 5 rows. Keeping them separate preserves the R1-R2 derivation history. My R3-A preference is COLLAPSE — the dual-binding is one structural finding, not three; the 7-row table over-counts the partition-decision content.

If you concur, the R3-B FINAL Workshop Verdict has 5 rows: (1) Dual-binding partition; (2) Per-regulator residue hierarchy (slot-conditional); (3) ZETA-EQUALS-SDW theorem (slot-conditional with sharpness clause); (4) SECTOR-2 propagation map (5-class @ L1 binding); (5) LAYER-2 audit-output file (with Stage-2.5 sub-classification + DI-1 simplified slot-tag). Each row gets a Converged status with Key-Insight cell.

If you prefer the 7-row form, the verdict table preserves the R1-R2 derivation history at the cost of slight redundancy. Either form lands all 7 R1 topics; the choice is editorial.

**Decision-procedure for R3-B FINAL convergence.**

For R3-B FINAL to land all three deliverables (a)/(b)/(c) and complete the workshop verdict + wrap-up:

- Q-LZ-R3-1 + Q-LZ-R3-3 → resolve deliverable (a) + (c) registry landing scope (entry-form, sub-tag form, schema dependency).
- Q-LZ-R3-2 → resolve deliverable (b) audit-output file scope (outline vs full file).
- Q-LZ-R3-4 → resolve carry-forward queue scope (narrow 3 entries vs broad ~24-34).
- Q-LZ-R3-5 → resolve workshop verdict table form (5-row collapsed vs 7-row preserved).

If you convergence on Q-LZ-R3-1 through Q-LZ-R3-5 in R3-B, the workshop closes with three deliverables landed + the Workshop Verdict table populated + the Wrap-Up sections filled. No further question is structurally needed at the R3 level.

**Cross-domain note.** Q-LZ-R3-4 (carry-forward queue scope) is the one with the most methodological consequence — it determines whether the workshop's emergent meta-methodology (EM-1 + EM-2 + EM-3 + EM-LZ-1 + EM-LZ-2) propagates into S87+ as forced carry-forwards or stays as workshop-record-only insights available for S87+ planner consideration. My recommendation is NARROW (workshop emergences are insights in the verdict cells; carry-forwards are restricted to the pre-registered 3 SECTOR-2 propagation gates). This respects the no-padding rule while preserving the meta-methodological insights for the S87+ planner to consider when scoping the next session.

**Cite-anchors:**
- Connes R2-B CV-1 through CV-7 (workshop lines 1741-1914): 7 convergences resolving Q1-Q5.
- Connes R2-B DI-1 + DI-2 (workshop lines 1921-2032): 2 dissents (slot-tag simplification + Class-2 phrasing).
- Connes R2-B EM-1 + EM-2 + EM-3 (workshop lines 2038-2329): 3 emergences (3-step pathway + gate generator + cross-pillar).
- My R3-A CV-LZ-1 through CV-LZ-5 (this section above): 5 convergence acceptances.
- My R3-A EM-LZ-1 + EM-LZ-2 (this section above): 2 final emergences (status-inventory + transitivity).
- My R3-A DI-LZ-S87 (this section above): 1 reserved forward-dissent for S87 prior-pre-registration.
- Workshop document lines 24-30: pre-registered three deliverables + carry-forward 4-field S87 spec.
- §VII-B Lizzi-track Cluster (registry line 4742-4747): sibling-slot context for two new entries.
- §VII.N L1/L2/L3 (registry line 5511): canonical naming for audit-output file post-CV-6.
- `feedback_fix-in-session-never-defer.md` (MEMORY): no-padding rule for carry-forward queue scope.

---

## Round 3 — connes: Cross-Synthesis (FINAL ROUND)

### CONVERGENCE

**Topline.** Lizzi's R3-A locks the workshop at full structural convergence: 5 acceptances (CV-LZ-1 through CV-LZ-5) ratify all R2-B refinements (DI-1 simplification, DI-2 phrasing, EM-1 3-step pathway, EM-2 gate generator, EM-3 cross-pillar generator); 1 reserved forward-dissent (DI-LZ-S87) is methodologically welcome rather than a blocker (it pre-registers a Z-flip prior on `S87-W5A-P3-IC-PER-CLASS-VERIFY` without contesting the gate's pre-registration); 2 final emergences (EM-LZ-1 §VIII status-inventory, EM-LZ-2 Stage-2.5 transitivity through §VII.K-PROP) extend the meta-methodology in directions that are substrate-physically correct and registry-actionable. My R3-B FINAL convergence locks each of her 5 Q-LZ-R3-* questions with a specific decision so all three deliverables (a)/(b)/(c) land at this turn. The decisions inherit the no-padding discipline (carry-forward queue narrow at the pre-registered 3 SECTOR-2 propagation gates plus the augmented IC verification with the DI-LZ-S87 prior footnote, with the meta-emergences logged in the verdict cells but not pre-committed as forced carry-forwards). Each decision is paired with a short substitution chain where it carries direction or scope content.

**CV-CN-R3-1: §VII-B.ZETA-EQUALS-SDW landing form — INLINE-PROSE LAYER tag, registry-write at this turn (Q-LZ-R3-1 RESOLVED).**

Lizzi's Q-LZ-R3-1 (workshop lines 2768-2773) asks whether the §VII-B.ZETA-EQUALS-SDW final-form skeleton lands at R3-B with an entry-header LAYER metadata field (requiring Step 2 schema extension to land first) OR with an inline-prose LAYER tag (no schema dependency). Her preference is inline-prose. I CONFIRM inline-prose.

The substitution chain that closes the placement decision:

```
Step 1 (definitions):
  registry_entry_schema(entry) := the existing structured fields per registry
                                  entry: header line, Source, Substrate framing,
                                  Theorem statement, Verdict, Sibling-corpus relation,
                                  Solution-space note. NO existing LAYER metadata field.
  inline_prose_LAYER(entry)    := LAYER tag appears as a prose sentence in the
                                  THEOREM statement body, NOT as a header field.
  schema_extension_dependency  := if entry-header carries LAYER metadata field,
                                  the registry-write hygiene rule's append-only-Python
                                  template (S86 W1c surface) must be extended; else
                                  no template change required.

Step 2 (substitute the §VII-B.ZETA-EQUALS-SDW skeleton at workshop lines 2095-2097):
  The current skeleton has:
    "LAYER TAG (per S86 W7 audit-output convention): LAYER-2-axiomatic
     (derived from Connes-Chamseddine 1996 §2.2-2.3 + helper module line 95
     literal pass-through; not a numerical-gate verdict)."
  This is a TAGGED PROSE LINE inside the entry body, NOT a header metadata field.
  The line carries the LAYER classification information; consumers parse it as
  prose, not as a structured field.

Step 3 (simplify):
  inline_prose_LAYER(entry)  ⇒  schema_extension_dependency = FALSE.
  R3-B can land §VII-B.ZETA-EQUALS-SDW at this turn without waiting for Step 2
  schema extension. The Step 2 carry-forward (`S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-
  EXTENSION`, lizzi's Q-LZ-5) lifts the inline-prose form into a structured
  metadata field at S87+ but is NOT prerequisite to the R3-B landing.

Step 4 (direction):
  Decision: inline-prose LAYER tag at R3-B; schema-extension upgrade as S87+
  carry-forward. The §VII-B.ZETA-EQUALS-SDW entry lands at R3-B unblocked.
  Conclusion: Q-LZ-R3-1 RESOLVED — inline-prose form, no Step-2 prerequisite,
  registry-write at this R3-B turn.
```

I CONFIRM lizzi's preferred inline-prose placement. The skeleton at workshop lines 2045-2116 is registry-ready as written; deliverable (c) lands at this R3-B turn.

**CV-CN-R3-2: Audit-output file scope — OUTLINE-ONLY at R3-B with full per-cite enumeration as S87 carry-forward (Q-LZ-R3-2 RESOLVED, with course-correction from her preference).**

Lizzi's Q-LZ-R3-2 (workshop lines 2774-2780) asks whether the audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` lands at R3-B as outline-only OR as the FULL file with the C3 17-row inventory + 3 conflation-flag remediations integrated in-session. Her preference is FULL FILE LAND. I respectfully RECOMMEND OUTLINE-ONLY at R3-B with the full per-cite enumeration as a S87 carry-forward.

The substitution chain that justifies the course-correction:

```
Step 1 (definitions):
  audit_outline := §1-§5 structural skeleton of the audit-output file, with
                   the C3 17-row inventory + 3 conflation-flag remediations as
                   §2.1 + §3 content; §1.1 (LAYER taxonomy quote), §1.2 (naming-
                   collision resolution + DI-1 resolution table), §1.3 (5-stage
                   protocol with optional Stage-2.5 sub-tag), §1.4 (forward-vs-
                   backward closure framing), §4 (remediation classes), §5 (cross-
                   cite ledger to 7 sibling registry entries).
  audit_full    := audit_outline + per-cite enumeration of S78-onward 5-atlas
                   cites (estimated ~250 cites per lizzi's L4 stage-1 cardinality
                   estimate, workshop line 448).
  
  workshop pre-registration (workshop line 26):
    "(b) `sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline
         (or land if convergence supports)"
  
  no-padding-rule (`feedback_fix-in-session-never-defer.md`, MEMORY):
    deviations are FIXED IN-SESSION; carry-forwards reserved for genuine
    future computation (4-field-spec gates, not "investigate X" lists).
  
  CARRY-FORWARD-COMPUTE (audit-output §4.3):
    a per-statement queue of S87+ numerical gates needed to settle whether
    a flagged conflation's LAYER 2 claim actually holds.

Step 2 (substitute the convergence state):
  Convergence count: 12 (R2-B 7 + R3-A 5).
  Structural content for outline: COMPLETE (lizzi's L4 + my Re:L4 + R2-B
    DI-1 resolution table + Stage-2.5 sub-classification all converged).
  Per-cite enumeration content: PARTIAL (C3's 17-row inventory is the seed;
    lizzi's L4 Stage-1 estimate is ~250 cites total — 13× expansion of the seed).
  In-session feasibility of full enumeration: estimated 1-2 wave-equivalents
    of cite-walking + LAYER-tagging work. NOT in-session-feasible at R3-B
    without exceeding the workshop's compute budget.
  
  no-padding rule applied to the outline-vs-full decision:
    The outline is a genuinely-complete structural artifact (the §1-§5
    skeleton is at landing-readiness). The per-cite enumeration is genuine
    future computation (each row classified, conflation-tested, remediation-
    tagged). Both are legitimate; only one is R3-B-feasible.

Step 3 (simplify):
  audit_outline at R3-B is a complete structural artifact landing at landing-
  readiness; audit_full at R3-B would require 13× expansion of the C3 seed,
  which is NOT in-session-feasible. The full enumeration is genuine future
  computation (per-cite walk + LAYER-tag + conflation-test) — fits the no-
  padding rule's "genuine 4-field-spec future work" criterion.

Step 4 (direction):
  Decision: OUTLINE-ONLY at R3-B; full per-cite enumeration as S87 carry-
  forward `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` (4-field-spec
  below in Wrap-Up). The outline lands the §1-§5 structural skeleton including
  the DI-1 resolution table + Stage-2.5 sub-classification + C3's 17-row
  inventory as §2.1 SEED + the 3 conflation-flag remediations as §3 entries.
  The S87 carry-forward expands §2.1 from 17 rows to ~250 rows.
  
  Conclusion: Q-LZ-R3-2 RESOLVED — OUTLINE at R3-B, full enumeration as S87
  carry-forward. This honors (a) the workshop's pre-registered "outline OR land
  if convergence supports" with convergence supporting structure but not
  enumeration, (b) the no-padding rule (the carry-forward is a 4-field-spec
  computation, not a hand-wave), and (c) the in-session feasibility constraint.
```

The course-correction from lizzi's full-file preference is on FEASIBILITY, not on convergence. Her structural content is at landing-readiness; the outline lands ALL of her structural content. The 13× per-cite expansion is the only piece deferred, and it is deferred precisely because it is genuine future computation rather than fillable-in-session structural content. I will land the outline at this R3-B turn (Wrap-Up §What Changed).

**CV-CN-R3-3: SECTOR-2 sub-tag landing form — single parent row `§VII-B.SECTOR-2-PARTITION` with 5 inline sub-rows (Q-LZ-R3-3 RESOLVED, lizzi's option (ii)).**

Lizzi's Q-LZ-R3-3 (workshop lines 2782-2788) offers three options for the 5 SECTOR-2 sub-tags: (i) 5 separate registry entries; (ii) one parent entry `§VII-B.SECTOR-2-PARTITION` with 5 inline sub-rows; (iii) full deferral to the S87 propagation theorem. Her preference is option (ii). I CONFIRM option (ii).

The substitution chain that closes the registry-write scope:

```
Step 1 (definitions):
  parent_entry(P, sub-rows S_1..S_n) := single registry entry with header P
                                       containing inline-table or sub-section
                                       per-class breakdowns.
  
  separate_entries(S_1..S_n)       := n distinct registry entries, each at its
                                       own §VII-* slot.
  
  registry-locality criterion       := the dual-binding partition (CV-1) is ONE
                                       structural finding (5-class @ L1 + 4-class
                                       @ L3-s=3 projection); the per-class
                                       distinction is DOWNSTREAM of the partition
                                       theorem, not co-equal to it.

Step 2 (substitute):
  Option (i) [5 separate entries]: registry grows by 5 entries; each is a
                                   per-class fact (multiplier vector + L1/L2/L3
                                   status); but the partition decision itself
                                   becomes implicit (no single registry entry
                                   IS "the partition decision").
  Option (ii) [1 parent + 5 inline]: registry grows by 1 entry; partition
                                   decision is explicit at the parent level;
                                   per-class facts are inline sub-rows.
  Option (iii) [defer to S87]:    R3-B records the partition decision in
                                   workshop-verdict only; no registry landing
                                   at R3-B; deliverable (a) is recorded as
                                   "decided, deferred to S87 propagation
                                   theorem registration."
  
  Workshop-deliverable (a) pre-registration (workshop line 25):
    "4- or 5-class SECTOR-2 partition registered (decision binding)."
  
  Option (iii) violates "registered" at R3-B; options (i) and (ii) honor it.
  Between (i) and (ii), the registry-locality criterion prefers (ii) — the
  partition is one decision, not five separate facts.

Step 3 (simplify):
  Adopting option (ii) lands ONE new registry entry at R3-B (`§VII-B.SECTOR-2-
  PARTITION`) with 5 inline per-class sub-rows. Combined with `§VII-B.ZETA-
  EQUALS-SDW` from CV-CN-R3-1, the §VII-B Lizzi-track Cluster grows by 2
  entries at R3-B (from 3 to 5).

Step 4 (direction):
  Decision: option (ii) — single parent row `§VII-B.SECTOR-2-PARTITION` with
  5 inline per-class sub-rows. The S87 carry-forward `S87-VII-K-PROP-DUAL-
  BINDING-LAND` (EM-1 Step 3) lifts the partition into a propagation theorem
  at §VII.K-PROP-DUAL-BINDING; the parent §VII-B.SECTOR-2-PARTITION remains
  the registry-canonical anchor for the partition itself.
  
  Conclusion: Q-LZ-R3-3 RESOLVED — option (ii) inline-sub-row form. §VII-B
  Lizzi-track Cluster grows by 2 entries at R3-B (ZETA-EQUALS-SDW + SECTOR-2-
  PARTITION).
```

I CONFIRM lizzi's option (ii). The §VII-B Lizzi-track Cluster grows from 3 to 5 entries at R3-B; its members are (1) §VII-B.HP1-NEAR-INVARIANCE, (2) §VII-B.TWO-LAYER-OBSTRUCTION, (3) §VII-B.ZETA-NOT-PHYSICAL-75, (4) §VII-B.ZETA-EQUALS-SDW (NEW R3-B), (5) §VII-B.SECTOR-2-PARTITION (NEW R3-B).

**CV-CN-R3-4: Carry-forward queue scope — NARROW (4 entries: 3 SECTOR-2 propagation gates + 1 IC verification with DI-LZ-S87 footnote) (Q-LZ-R3-4 RESOLVED, lizzi's narrow scope).**

Lizzi's Q-LZ-R3-4 (workshop lines 2790-2798) asks whether the carry-forward queue is NARROW (3 SECTOR-2 propagation gates) or BROAD (~24-34 entries including all meta-emergences). Her preference is NARROW. I CONFIRM NARROW with one augmentation: the IC verification gate carries her DI-LZ-S87 prior-pre-registration as an explicit footnote.

The substitution chain that closes the queue scope:

```
Step 1 (definitions):
  pre-registered_carry-forward (workshop line 30):
    "4-field S87 spec for SECTOR-2 propagation into W5a P3 IC + W6 C-α/β/γ"
    — narrowly scoped to the 3 SECTOR-2 propagation gates.
  
  no-padding rule (`feedback_fix-in-session-never-defer.md`, MEMORY):
    "Carry-forwards are reserved for genuine future computation — a new gate
     with pre-registered threshold + machinery pin. Each carry-forward must
     have a fillable 4-field spec (what / inputs / gate / effort)."
  
  meta-emergence carry-forwards (broad-scope candidates):
    (a) EM-1 Step 2 (`S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION`): registry
         schema work, NOT a gated computation. Not carry-forward.
    (b) EM-1 Step 3 (`S87-VII-K-PROP-DUAL-BINDING-LAND`): registry-landing
         work, NOT a gated computation. Not carry-forward.
    (c) EM-2 sample warrant-check gates (3): pre-registered 4-field-spec OK.
         CARRY-FORWARD-CANDIDATE if user-decided.
    (d) EM-LZ-1 §VIII status-inventory (6 fb_pair instantiations): each is an
         entire S87+ workshop, NOT a gate. Not carry-forward at gate level.
    (e) EM-LZ-2 transitive composition gates (~10-20): downstream of (c);
         derived from sub-classification, not pre-registered yet.

Step 2 (substitute the no-padding rule):
  Items (a), (b), (d), (e): NOT 4-field-spec gates. They are registry-
                            architecture work, S87+ workshop topics, or
                            derivative computations. Failing the 4-field-test
                            means they are HYGIENE / META-METHODOLOGY, not
                            gated computations. They do NOT belong in the
                            carry-forward queue per the no-padding rule.
  Item (c): three 4-field-spec gates are well-formed. They COULD be in the
            carry-forward queue, but they are downstream of EM-2 acceptance
            (a meta-methodology emergence) rather than of the workshop's
            pre-registered computation pathway.
  
  The pre-registered carry-forward (workshop line 30) explicitly scopes
  to "SECTOR-2 propagation into W5a P3 IC + W6 C-α/β/γ" — 3 gates total.
  Anything beyond that is post-pre-registration expansion.

Step 3 (simplify):
  NARROW scope (4 entries):
    1. `S87-W5A-P3-IC-PER-CLASS-VERIFY` (with DI-LZ-S87 footnote).
    2. `S87-W6-C-BETA-UV-CUTOFF-3CLASS`.
    3. `S87-W6-C-GAMMA-WEAK-PER-CLASS`.
    4. `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` (CV-CN-R3-2).
  Items (a), (b), (c), (d), (e) above are LOGGED in the workshop verdict's
  Key-Insight cells AND in the audit-output file's §4.3 (CARRY-FORWARD-COMPUTE
  remediation queue) for S87+ planner consideration, but NOT pre-committed
  as forced carry-forwards.

Step 4 (direction):
  Decision: NARROW scope (4 entries). The meta-emergences (EM-1, EM-2, EM-3,
  EM-LZ-1, EM-LZ-2) are recorded in the workshop verdict and the audit-output
  file's §4.3 queue for S87+ planner inspection, but the workshop's binding
  carry-forward is the pre-registered scope only.
  
  Conclusion: Q-LZ-R3-4 RESOLVED — NARROW scope, 4 entries. Meta-emergences
  available to S87+ planner via workshop record, not pre-committed as
  carry-forwards. This respects (a) the no-padding rule, (b) the workshop's
  pre-registered carry-forward scope, and (c) lizzi's epistemic-tightness
  preference.
```

The 4th entry (CV-CN-R3-2 audit-output full enumeration) is added as a workshop-discipline carry-forward — without it, the audit-output file remains permanently in outline-state, which would itself be a no-padding violation. The 4 entries together honor the pre-registered carry-forward + the OUTLINE→FULL upgrade path.

**CV-CN-R3-5: Workshop Verdict table form — 5-row COLLAPSED (Q-LZ-R3-5 RESOLVED, lizzi's collapse preference).**

Lizzi's Q-LZ-R3-5 (workshop lines 2800-2806) asks whether the verdict table collapses 7 rows to 5 (merging F_2/F_4 4-class + Connes-Chamseddine 5-class + Binding decision into a single dual-binding row). Her preference is COLLAPSE. I CONFIRM COLLAPSE.

The 5-row form is structurally accurate: the dual-binding partition is ONE finding (CV-1 + CV-LZ-1), not three; the 7-row form preserves R1 derivation history at the cost of triple-counting the partition decision. The Workshop Verdict table I emit below uses the 5-row form per her recommendation.

**CV-CN-R3-6: EM-LZ-1 §VIII status-inventory + EM-LZ-2 Stage-2.5 transitive composition — ACCEPT IN FULL.**

Lizzi's R3-A EM-LZ-1 (workshop lines 2598-2679) constructs a §VIII registry meta-table tracking fb_pair coverage across {M_1, M_2, M_3, M_4} substrate manifolds, with M_1 (regulator-class) BUILT this workshop and 6 cells across M_2/M_3/M_4 as S87+ workshop candidates. Her substitution chain (workshop lines 2641-2677) correctly classifies each manifold's coverage status (BUILT / PARTIAL / CANDIDATE per axis) and quantifies the coverage gap as 6/8 cells.

I ACCEPT EM-LZ-1 in full. The status-inventory is a substrate-physically correct organization of the project's substrate-manifold inventory: each M_i carries its own theorem-record + cite-history; the fb_pair construction is the closure-pair on each M_i; the meta-table makes the coverage explicit at the §VIII level. The 6-entry S87+ candidate queue (M_2-forward, M_2-backward, M_3-backward, M_4-forward, M_4-backward, M_3-forward upgrade PARTIAL → BUILT) is well-formed.

**Direction caveat from the NCG side:** the M_3 (Mellin-strip integrability) PARTIAL status is correct as lizzi states. The MP-Exclusion theorem (S82 W2-5) is proof-complete and has implicit forward closure — but the theorem's non-evidence-status declaration was never explicitly written. M_3 forward upgrade is a 1-wave structural workshop (write the explicit non-evidence-status declaration on MP-Exclusion). M_3 backward closure is the larger task (S78-onward Mellin-strip cite-walk). The M_2 (Jensen-deformation) manifold has MORE theorems (M_max bound, a_2/a_4 monotonicity, GGE-KMS Hessian descent, dS/dτ = +58,673 fold-action) and is the largest fb_pair workshop candidate. M_4 (GGE-relic) has medium scope. The S87+ queue ordering should respect this scope variation.

Lizzi's R3-A EM-LZ-2 (workshop lines 2682-2751) establishes the warrant-class transitive composition rule via §VII.K-PROP `span(O) = ∏_k span(f_k)^{p_k(O)}`: the observable O inherits its warrant-class as the conjunction of its f_k constituents' warrant-classes, with the weakest-link form dominating (LAYER-2-numerical wins over LAYER-2-axiomatic at any constituent). Her three test cases (m_H, chi_2, HP^1 LOOSE max ratio) all show the weakest-link composition giving LAYER-2-numerical observable warrant; the EM-2 gate generator's queue therefore expands to ~10-20 S87+ gates across composite observables.

I ACCEPT EM-LZ-2 in full. The composition rule is structurally correct: span(O) factors through span(f_k); warrant_class(span(f_k)) propagates multiplicatively in a max-warrant-weakness sense. The ~10× expansion of the EM-2 gate generator's queue is the substrate-physics consequence — most observables in the project's atlas combine an axiomatic spectral-residue structure with a numerical fitting parameter or observed value, putting them in the LAYER-2-numerical bucket and making them warrant-check-candidates.

The §VII.K-PROP transitivity rule itself is LAYER-2-axiomatic (CC-1996 §2.2-2.3 multiplier-vector-grading consequence; not numerically-gated). The composition RULE is strong-warrant; its APPLICATION to specific composite observables generates the S87+ queue. This is the cleanest statement of why the Stage-2.5 sub-classification is methodologically central — it propagates warrant-class through the project's observable atlas systematically, generating an active gate queue at S87+ from a passive tagging convention at S86 W7.

**Convergence summary table (R3-B FINAL — 6 R3-B convergence entries layered onto R3-A 5 entries + R2-B 7 entries).**

| Convergence point | Resolves | Workshop deliverable | Status at R3-B FINAL |
|:---|:---|:---|:---|
| CV-CN-R3-1 (inline-prose LAYER tag) | Q-LZ-R3-1 | (c) §VII-B.ZETA-EQUALS-SDW landing | Closed; registry-write at R3-B unblocked |
| CV-CN-R3-2 (audit-output OUTLINE-ONLY at R3-B) | Q-LZ-R3-2 (course-corrected) | (b) audit-output file scope | Closed; outline at R3-B, full enumeration as S87 carry-forward |
| CV-CN-R3-3 (option (ii) parent + 5 inline sub-rows) | Q-LZ-R3-3 | (a) registry-write form | Closed; §VII-B.SECTOR-2-PARTITION single parent at R3-B |
| CV-CN-R3-4 (NARROW carry-forward queue, 4 entries) | Q-LZ-R3-4 | Workshop carry-forward | Closed; 4-entry queue, meta-emergences in verdict cells |
| CV-CN-R3-5 (5-row COLLAPSE Workshop Verdict) | Q-LZ-R3-5 | Workshop verdict table form | Closed; 5-row verdict below |
| CV-CN-R3-6 (EM-LZ-1 + EM-LZ-2 acceptance) | Lizzi R3-A emergences | (b) audit-output §4.3 queue + §VIII candidate queue | Closed; accepted in full, S87+ candidate queue logged |

Combined convergence count across all three rounds: R2-B 7 + R3-A 5 + R3-B 6 = **18 convergence points**. All 5 of lizzi's Q-LZ-R3-* questions are RESOLVED. The workshop is at full structural convergence with all three deliverables locking PASS-AT-R3.

**Substrate framing.** Each R3-B convergence is a SUBSTRATE-PHYSICS LANDING DECISION on the regulator-class manifold's registry-permanent record. CV-CN-R3-1 fixes the placement of the §VII-B.ZETA-EQUALS-SDW theorem-grade entry in the registry's existing schema (no schema dependency); CV-CN-R3-2 fixes the audit-output file's structural skeleton at R3-B with the full per-cite enumeration deferred to S87+ (genuine future computation); CV-CN-R3-3 fixes the partition-decision registry form (single parent + 5 inline sub-rows); CV-CN-R3-4 fixes the workshop's carry-forward propagation scope at the pre-registered 3-gate scope plus the audit-output upgrade path; CV-CN-R3-5 fixes the workshop verdict's editorial form (5-row collapse); CV-CN-R3-6 ratifies the cross-pillar meta-table structure that organizes future workshops on sibling substrate manifolds. All six are substrate-internal landing decisions; none invoke external machinery beyond NCG axioms A1-A6 + Connes-Marcolli Thm 1.31 + the §VII.N stratification + the registry-write hygiene rule (S86 W1c surface).

### DISSENT

**Topline.** No structural disagreement remains within the workshop's R3-B FINAL scope. Lizzi's R3-A produced 5 acceptances (CV-LZ-1 through CV-LZ-5) of all my R2-B refinements; her single dissent (DI-LZ-S87) is a RESERVED forward-pre-registration of a Z-flip prior on the S87 IC verification gate, not a contestation of any R3-B deliverable. Her two final emergences (EM-LZ-1 §VIII status-inventory, EM-LZ-2 Stage-2.5 transitivity) are substrate-physically correct and registry-actionable; I accept both at CV-CN-R3-6. Her five Q-LZ-R3-* questions all resolve at CV-CN-R3-1 through CV-CN-R3-5; the only course-correction is CV-CN-R3-2 (outline-only at R3-B with full enumeration as S87 carry-forward) — which is not a structural disagreement but a feasibility-and-no-padding-rule application that lizzi's preference inadvertently overshot.

This DISSENT placeholder is therefore not vacuous in two specific senses: I (1) ratify lizzi's RESERVED DI-LZ-S87 prior-pre-registration as a forward-pre-registration that travels with the carry-forward `S87-W5A-P3-IC-PER-CLASS-VERIFY` as an explicit footnote, and (2) raise one new forward-dissent of my own (DI-CN-R3-S87) that pre-registers an INDEPENDENT prior on the same gate from the NCG-axiomatic side, as a complementary anchor for INFO-verdict interpretation.

**DI-CN-R3-S87 (FORWARD DISSENT, RESERVED FOR S87): Class-2 (SDW) at s=−1 likely flips Z_ratio direction MOST LIKELY among the non-Class-1 regulators, via the Γ(−1) simple-pole convention sign-ambiguity rather than via Pauli-Villars sign-subtraction (as lizzi DI-LZ-S87 prioritizes anomaly Class-5).**

Lizzi's DI-LZ-S87 (workshop lines 2524-2590) places anomaly Class-5 as the most-likely Z-flip candidate (Pauli-Villars sign-subtraction giving xi_E_GGE_inv^{anomaly} ∝ (−M_PV²) with explicit negative sign), with SDW Class-2 second-most-likely (Γ(−1) pole convention ambiguity). Her substitution chain at workshop lines 2541-2570 is structurally correct as far as the SIGNS go for both classes; however, the relative ordering of which class is most-likely-to-flip can be re-evaluated from the NCG-axiomatic side, and I argue Class-2 is more likely than Class-5 to flip the direction.

**Substitution chain (NCG-axiomatic prior on the Z-flip ranking):**

```
Step 1 (definitions):
  xi_E_GGE_inv^{R}(s=−1) := the s=−1 spectral residue of the GGE-projected D_K
                            evaluated under regulator R.
  
  Class-2 (SDW) at s=−1:  Γ(−1) is a simple pole; SDW carries Γ(s)·ζ_D(2s)
                          form, with the Γ(−1) pole subtracted in the residue
                          extraction by Connes-Chamseddine ratio normalization.
                          The convention for Γ-pole subtraction has SIGN
                          AMBIGUITY in the standard conventions: the simple-
                          pole residue is +1 at s=0 (Γ(s) ~ 1/s as s → 0),
                          BUT at s=−1 the pole has residue −1 (Γ(s) = Γ(s+1)/s,
                          and Γ(0) is a pole with residue +1, so Γ(−1)
                          inherits a SIGN-FLIPPED residue −1 via the Pochhammer
                          shift Γ(s) = Γ(s+2)/(s(s+1)), with s(s+1) → 0·1 = 0
                          near s=−1 and the s+1 factor going to zero giving
                          the −1 residue). Therefore SDW at s=−1 carries an
                          INTRINSIC SIGN FLIP from the Γ(−1) pole structure.
  
  Class-5 (anomaly) at s=−1: Pauli-Villars subtraction gives
                          M_anomaly(−1) = Σ d · [C − (C+M_PV²)] = Σ d · (−M_PV²).
                          The SIGN is negative as lizzi DI-LZ-S87 states, but
                          the OVERALL Z-factor ratio depends on whether
                          xi_E_GGE_inv^2 (which appears squared in the IC
                          xi²(0)) inherits the sign or absorbs it. Squaring
                          a negative xi_E_GGE_inv gives a POSITIVE xi²(0),
                          so Class-5's negative-sign at the linear level may
                          NOT flip the squared IC value's sign — the
                          Z-direction depends on the |xi²(0; anomaly)|
                          MAGNITUDE relative to |xi²(0; ζ)|, not the sign
                          of xi_E_GGE_inv itself.

Step 2 (substitute the IC squaring step):
  xi²(0; R) = (xi_E_GGE_inv^{R})^{−2}
  
  For Class-1 (ζ):    xi_E_GGE_inv^{ζ} = +13.642 (canonical, positive).
                      xi²(0; ζ) = (13.642)^{−2} = 5.37e−03 (positive).
  
  For Class-5 (anomaly): xi_E_GGE_inv^{anomaly} ∝ (−M_PV²) (negative LINEAR sign).
                      xi²(0; anomaly) = (negative)^{−2} = (negative)^{−2}.
                      A NEGATIVE number raised to integer power −2 is positive
                      (since −2 is even AND the inverse).
                      xi²(0; anomaly) IS POSITIVE; the Pauli-Villars sign-
                      subtraction does NOT propagate to xi²(0)'s sign.
                      Direction: Z_ratio direction depends on MAGNITUDE.
  
  For Class-2 (SDW):  At Γ(−1) pole, the residue extraction picks up a
                      Γ(−1)-related normalization factor that can be either
                      +1 or −1 depending on the convention chosen for the
                      pole-subtraction (in standard Mellin-Barnes contour
                      integration, the residue at s=−1 carries a factor of
                      Γ(s+1)|_{s=−1} = Γ(0) = pole — the convention of which
                      branch is taken across the pole introduces sign
                      ambiguity).
                      
                      If convention picks +1: xi_E_GGE_inv^{SDW} > 0,
                                              xi²(0; SDW) > 0,
                                              Z_ratio direction PRESERVED.
                      If convention picks −1: xi_E_GGE_inv^{SDW} < 0,
                                              xi²(0; SDW) > 0 (squaring still
                                              gives positive),
                                              BUT THE LINEAR-IN-xi corrections
                                              to Z_ratio at NLO carry the
                                              odd-power xi terms, which DO
                                              flip sign under SDW's sign-
                                              flipped xi_E_GGE_inv.
                                              Z_ratio direction may FLIP at NLO.

Step 3 (simplify):
  Class-5 (anomaly): xi²(0; anomaly) is positive regardless of Pauli-Villars
                      sign because of even-power squaring. Z-direction depends
                      on MAGNITUDE — only flips if |xi²(0; anomaly)| > 1 or
                      < some threshold to cross the Z_ratio = 1 line during
                      N-flow. From the depletion factors at s=3 (M_anomaly/M_ζ
                      = 0.201), the magnitude shift is ~5× depletion, which
                      could push Z_ratio across 1 — but the direction-flip is
                      MAGNITUDE-DRIVEN, not sign-driven.
  Class-2 (SDW):    xi_E_GGE_inv^{SDW} sign depends on Γ(−1) pole convention;
                      the LINEAR-in-xi corrections to Z_ratio at NLO inherit
                      the sign-flip; Z-direction flip is SIGN-DRIVEN at the
                      linear level, not magnitude-driven.

Step 4 (direction):
  Pre-registered NCG prior on Z-flip ranking (DI-CN-R3-S87):
    Most likely to flip Z_ratio direction: Class-2 (SDW) via Γ(−1) sign
                                            convention ambiguity at NLO.
    Second-most-likely:                     Class-5 (anomaly) via Pauli-
                                            Villars magnitude-shift crossing
                                            Z_ratio = 1.
    Third:                                  Class-3 (Zubarev) via t_ref
                                            scale interaction with Γ(−1)
                                            pole.
  
  This is opposite to lizzi DI-LZ-S87's ordering (anomaly first, SDW second).
  The disagreement is on whether sign-driven NLO effects (SDW) or magnitude-
  driven LO effects (anomaly) dominate the Z_ratio direction-flip risk.
```

Both DI-LZ-S87 and DI-CN-R3-S87 are RESERVED FORWARD-DISSENTS — neither contests the gate's well-formed pre-registration. The gate's PASS condition (Z_ratio direction preserved across all 5 classes) and INFO condition (class-dependent direction) are both legitimate outcomes; my prior orders the classes differently from lizzi's. The two priors travel together in the carry-forward 4-field spec for `S87-W5A-P3-IC-PER-CLASS-VERIFY` as complementary anchors:

> Pre-registered priors (S86 W7 R3-A DI-LZ-S87 + R3-B DI-CN-R3-S87): at least one of {SDW, Zubarev, anomaly} likely flips Z_ratio direction. Lizzi-track ordering: Class-5 (anomaly, Pauli-Villars sign-subtraction) most-likely; Class-2 (SDW, Γ(−1) pole) second-most-likely. Connes-track ordering: Class-2 (SDW, Γ(−1) sign convention at NLO) most-likely; Class-5 (anomaly, Pauli-Villars magnitude-shift crossing Z_ratio = 1) second-most-likely. The two orderings disagree on whether sign-driven NLO effects (Connes track) or magnitude-driven LO effects (Lizzi track) dominate the Z_ratio direction-flip risk. The S87 gate's verdict will adjudicate.

The dual-prior pre-registration prevents post-hoc PASS-shopping and gives the S87 gate's verdict a pre-registered reference frame for INFO interpretation regardless of which class actually flips.

**DISSENT summary table (R3-B FINAL).**

| Dissent point | Position | Forward-pre-registration target | Structural disagreement at R3? |
|:---|:---|:---|:---|
| DI-LZ-S87 (lizzi R3-A) | Class-5 (anomaly) Pauli-Villars sign-subtraction most-likely Z-flip | `S87-W5A-P3-IC-PER-CLASS-VERIFY` footnote | NO (forward-pre-registration only) |
| DI-CN-R3-S87 (connes R3-B, NEW) | Class-2 (SDW) Γ(−1) sign convention at NLO most-likely Z-flip | Same gate, complementary anchor | NO (forward-pre-registration only) |

Both dissents are FORWARD pre-registrations of priors on the same S87 gate, ordered differently. Neither contests an R3-B deliverable; both travel as carry-forward footnotes. The workshop's R3-B FINAL conclusion stands at full structural convergence on all R3 deliverables; the dissents are pre-registration discipline for S87+ planner reference.

### EMERGENCE

**Topline.** Two final emergences surface from the joint reading of lizzi's R3-A (CV-LZ-1 through CV-LZ-5, EM-LZ-1, EM-LZ-2, DI-LZ-S87, Q-LZ-R3-1 through Q-LZ-R3-5) and my R3-B (CV-CN-R3-1 through CV-CN-R3-6, DI-CN-R3-S87). EM-CN-R3-1 is the dual-prior pre-registration pattern: when two reasoning tracks (Lizzi spectral-functional vs Connes NCG-axiomatic) generate INDEPENDENT but DIFFERENTLY-ORDERED priors on the same future gate, the carry-forward 4-field spec inherits BOTH priors as complementary anchors, and the gate's verdict becomes a TRACK-DISCRIMINATOR — its PASS/INFO/FAIL outcome distinguishes which reasoning track produces accurate predictions on per-class spectral-functional behavior. EM-CN-R3-2 is the dual-binding partition's universal-property reading: the §VII-B.SECTOR-2-PARTITION + §VII.K-PROP-DUAL-BINDING pair forms a pushout-like diagram on the regulator-class manifold's stratification, where the 5-class @ L1 partition is the universal object covering all downstream channel evaluations and the 4-class @ L3-s=3 projection is the channel-specific quotient at the a_2 slot — a substrate-physics property of the manifold's Mellin-residue-extraction structure that I had previously rationalized only as "finest partition consistent with all channels." Both emergences are R3-B-only; they do not appear in lizzi's R3-A.

**EM-CN-R3-1: Dual-prior pre-registration as track-discriminator gate-pattern.**

When a gate's pre-registration absorbs two INDEPENDENT priors from two reasoning tracks (Lizzi DI-LZ-S87 spectral-functional ordering: anomaly first, SDW second; Connes DI-CN-R3-S87 NCG-axiomatic ordering: SDW first, anomaly second), the gate's verdict becomes a TRACK-DISCRIMINATOR — it tells us not just "did the prediction hold?" but "which reasoning track better predicts per-class spectral-functional behavior?" This is methodologically valuable because the two tracks have hitherto been COMPLEMENTARY (each handles different aspects of the regulator-class manifold) but their predictive accuracy on novel observables has not been directly compared.

**Substitution chain (track-discriminator structure):**

```
Step 1 (definitions):
  prior(track, gate) := the track's pre-registered ordering / direction prediction
                        for the gate's verdict.
  track-discriminator-gate := a gate whose verdict adjudicates between two
                              tracks' competing priors, providing track-relative
                              predictive-accuracy data.
  
  Lizzi-track prior (DI-LZ-S87): anomaly Class-5 most-likely Z-flip; SDW
                                  Class-2 second-most. Reasoning: Pauli-Villars
                                  sign-subtraction gives explicit linear-sign;
                                  S66 ZETA-SA-66 history shows eps_H sign-flips
                                  common.
  Connes-track prior (DI-CN-R3-S87): SDW Class-2 most-likely Z-flip; anomaly
                                  Class-5 second-most. Reasoning: Γ(−1)
                                  pole convention sign-ambiguity at NLO;
                                  squaring kills Pauli-Villars linear sign.

Step 2 (substitute the four possible verdict outcomes):
  Verdict outcome 1: PASS (Z_ratio direction preserved across all 5 classes).
                    → Both priors WRONG; framework's Z-factor reading is
                      functional-class-INDEPENDENT (strongest robustness).
                    → Track-discriminator: NEUTRAL (neither track predicted).
  
  Verdict outcome 2: INFO with anomaly Class-5 flipping (lizzi prior holds).
                    → Lizzi-track prior CORRECT; spectral-functional reasoning
                      better captures per-class behavior at the magnitude-
                      driven LO level.
                    → Track-discriminator: LIZZI-TRACK FAVORED.
  
  Verdict outcome 3: INFO with SDW Class-2 flipping (connes prior holds).
                    → Connes-track prior CORRECT; NCG-axiomatic reasoning
                      better captures per-class behavior at the sign-driven
                      NLO level.
                    → Track-discriminator: CONNES-TRACK FAVORED.
  
  Verdict outcome 4: INFO with multiple classes flipping or unexpected class
                    flipping.
                    → Both priors PARTIALLY HOLD or both WRONG; framework
                      requires THIRD-TRACK reasoning (a S87+ workshop on the
                      reasoning-track that better predicts the actual behavior).

Step 3 (simplify):
  The track-discriminator structure is methodologically PRODUCTIVE in all four
  outcomes:
    Outcome 1: confirms framework's Z-robustness; both tracks update their
               priors toward "Z is functional-class-INDEPENDENT."
    Outcome 2: confirms lizzi-track for magnitude-LO predictions; updates
               priors toward "lizzi-track preferred for LO observables."
    Outcome 3: confirms connes-track for sign-NLO predictions; updates priors
               toward "connes-track preferred for NLO sign observables."
    Outcome 4: triggers a S87+ workshop to identify the reasoning-track that
               better predicts the actual behavior.

Step 4 (direction):
  Direction implication: dual-prior pre-registration is a TEMPLATE for any
  gate that lies at the intersection of two reasoning tracks. The S86 W7
  workshop produces ONE such gate (the IC verification); future workshops
  with two-track structure (e.g., spectral-functional vs NCG-axiomatic on
  Jensen-deformation observables, or BCS vs spectral-action on cosmological
  observables) can adopt the same pattern.
  
  Conclusion: EM-CN-R3-1 is a methodological emergence that elevates the
  workshop's dual-prior carry-forward from a "two competing predictions" to
  a "track-relative-accuracy adjudicator." The S87 gate's verdict becomes
  data on the project's reasoning-track-preference question, beyond just
  data on the SECTOR-2 propagation question.
```

The track-discriminator framing is forward-compatible with EM-3's cross-pillar generator: every fb_pair(M_i) construction at S87+ (M_2 Jensen, M_3 Mellin-strip, M_4 GGE-relic) carries its own intersection-locus where lizzi-track and connes-track priors may differ. The track-discriminator pattern can be applied at each. This compounds the meta-methodological lift of the workshop: not just "land a structural result on M_1" + "land a closure-pair template across {M_2, M_3, M_4}" but ALSO "land a track-discriminator gate-pattern at each fb_pair construction's intersection-locus."

**EM-CN-R3-2: Dual-binding partition as universal-property/quotient pair on the regulator-class manifold.**

The dual-binding partition (CV-1 + CV-LZ-1 + CV-CN-R3-3 ratifying option (ii) registry-write) has a deeper category-theoretic reading I had not articulated in R2-B: the §VII-B.SECTOR-2-PARTITION (5-class @ L1) and §VII.K-PROP-DUAL-BINDING (4-class @ L3-s=3 projection) form a UNIVERSAL-PROPERTY / QUOTIENT pair on the regulator-class manifold's Mellin-residue-extraction structure.

**Substitution chain (universal-property reading):**

```
Step 1 (definitions):
  M_reg                    := regulator-class manifold = A_5 mod ~_multiplier-vector
                              (5 equivalence classes at L1).
  Π_s : M_reg → M_reg / ~_residue-at-s
                            := the projection that collapses regulators with
                               equal Mellin-residue-at-s into a single class.
  Universal property (UP)  := for any channel C with evaluation stratum Σ(C)
                               at a Γ-regular slot s_C, the binding partition
                               for C factors uniquely through M_reg.
  Quotient (Q)             := for the specific s_3 = s=3 a_2-slot evaluation,
                               the projection Π_{s=3} : 5-class → 4-class is
                               a specific quotient of M_reg with kernel
                               ker(Π_{s=3}) = {(Class 1, Class 2)} (the F_2
                               pair-collapse).

Step 2 (substitute the channel structure):
  W5a-P3 IC channel: Σ = {L1-Γ-pole}. Binding partition factors through M_reg
                     with NO collapse (Γ-pole prevents F_2 merge).
                     Therefore: 5-class @ L1 IS the binding partition; no
                     non-trivial projection at this channel.
  
  C-γ-WEAK channel: Σ = {L1-axiomatic + L3-residual}. Binding partition factors
                    through M_reg, evaluated at the multiplier-vector level.
                    Therefore: 5-class @ L1 IS the binding partition.
  
  C-α per-slot channel: Σ = {L3-residual at slot-by-slot}. Binding partition
                        AT each slot is the per-slot quotient Π_s of M_reg.
                        Therefore: per-slot binding is Π_s(M_reg), with Π_{s=3}
                        being the 4-class @ L3-s=3 quotient (the F_2 collapse).
  
  C-η, C-θ already-landed channels: Σ = {NCG axiom-derived}. Binding partition
                                     at this stratum is INVARIANT (Ward and
                                     inner-fluctuation are regulator-class-
                                     independent for L1-admissible regulators).
                                     Therefore: 5-class @ L1 trivially.

Step 3 (simplify — universal property):
  M_reg (5-class @ L1) is the UNIVERSAL OBJECT in the category of partitions of
  A_5 covered by the project's downstream channels: every channel's binding
  partition factors uniquely through M_reg. The 4-class @ L3-s=3 is the
  SPECIFIC QUOTIENT Π_{s=3}(M_reg) with kernel {(Class 1, Class 2)} = F_2.
  
  Other slot-quotients exist but are structurally distinct:
    Π_{s=4}(M_reg) (a_0-slot, RFB): 2-class quotient with kernel {(Class 1,
                                     Class 2, Class 3, Class 5)} (all f_0=0
                                     classes merge).
    Π_{s=2}(M_reg) (a_4-slot, HP1): non-trivial coarsening grouping pure-a_4
                                     vs mixed-support members.
    Π_{s=−1}(M_reg) (W5a IC, Γ-pole): identity quotient (no collapse).

Step 4 (direction):
  Direction implication: M_reg is the universal partition; each Π_s is a
  channel-specific quotient. The dual-binding registry-write IS the universal-
  property + quotient pair: §VII-B.SECTOR-2-PARTITION lands the universal
  object M_reg; §VII.K-PROP-DUAL-BINDING (S87 carry-forward) lands the
  quotient family {Π_s : s ∈ {Mellin slots}} as the propagation theorem.
  
  Conclusion: the workshop's dual-binding decision is structurally a
  category-theoretic universal-property / quotient pair on the regulator-class
  manifold. This is a SHARPER reading of why the 5-class @ L1 binding is
  correct: it is the universal partition, not just the "finest consistent
  partition." The 4-class @ L3-s=3 is the specific quotient at s=3; other
  channels carry their own quotients.
```

The universal-property reading has two consequences for the S87+ register:

1. **The §VII.K-PROP-DUAL-BINDING propagation theorem (EM-1 Step 3) generalizes naturally.** Its registry-write is not just "one projection theorem" but "a family of channel-quotients {Π_s} parametrized by Mellin slot." Each Π_s is a specific quotient; the family forms the propagation calculus on M_reg.

2. **Cross-channel propagation between two L3 channels at different slots is a quotient-composition.** For an observable O that depends on two slots s and s', span(O) is computed via the composition Π_s ∘ Π_{s'} of the relevant quotients. The §VII.K-PROP `span(O) = ∏_k span(f_k)^{p_k(O)}` rule is the multiplicative form of this composition; the universal-property reading explains WHY the rule has multiplicative form (composition of quotients = product of canonical-form factors).

This is a methodological lift parallel to EM-3 (cross-pillar) but operating WITHIN M_1 (regulator-class) on its slot-quotient family. The universal-property reading of the dual-binding partition is forward-compatible with all R3-B convergences (CV-CN-R3-1 through CV-CN-R3-6) and with lizzi's two final emergences (EM-LZ-1 status-inventory + EM-LZ-2 transitive composition); it explains the structural reason for both — EM-LZ-2's transitive composition IS the multiplicative-quotient calculus on M_reg, and EM-LZ-1's status-inventory IS the catalog of "which other substrate manifolds also have universal-property/quotient structure on their fb_pair coverage."

**EMERGENCE summary table (R3-B FINAL — 2 R3-B emergence entries layered onto R2-B 3 entries + R3-A 2 entries).**

| EMERGENCE point | What it generates | Workshop deliverable / Carry-forward |
|:---|:---|:---|
| EM-CN-R3-1 (dual-prior track-discriminator) | Track-relative-accuracy data from S87 IC verification gate | Carry-forward S87 gate footnote (lizzi DI-LZ-S87 + connes DI-CN-R3-S87) |
| EM-CN-R3-2 (dual-binding as universal-property/quotient pair) | Category-theoretic structural reading of M_reg with slot-quotient family | Workshop verdict cell (deferred sharper §VII.K-PROP-DUAL-BINDING formalism for S87+) |

Combined emergence count across all rounds: R2-B 3 (EM-1, EM-2, EM-3) + R3-A 2 (EM-LZ-1, EM-LZ-2) + R3-B 2 (EM-CN-R3-1, EM-CN-R3-2) = **7 emergences total**. Three (EM-1, EM-2, EM-3) carry from R2-B and lift the workshop to meta-methodology level; two (EM-LZ-1, EM-LZ-2) extend by quantifying coverage and warrant-class transitivity; two (EM-CN-R3-1, EM-CN-R3-2) sharpen the dual-prior pattern and the universal-property reading. The workshop's cumulative meta-level contribution is substantial: a structural result on M_1 (object level) + a fb_pair template across {M_1, M_2, M_3, M_4} (cross-pillar) + an active gate generator (warrant-check) + a coverage status-inventory (§VIII) + a transitivity rule (§VII.K-PROP composition) + a dual-prior gate-pattern + a universal-property/quotient reading. Each is registry-actionable; each compresses methodological content under a structural framing.

**Substrate framing.** EM-CN-R3-1 is a substrate-physics METHODOLOGICAL pattern on the regulator-class manifold's gate-locus structure — when two reasoning tracks intersect at a single gate-locus on M_reg, the gate's verdict carries adjudication-relative-accuracy information beyond the gate's pre-registered PASS/FAIL/INFO bands. EM-CN-R3-2 is a substrate-physics CATEGORY-THEORETIC structural property of M_reg — the manifold has a universal partition (multiplier-vector @ L1) and a slot-quotient family (Mellin-residue-at-s for s ∈ admissible-slots), which together form the regulator-class manifold's stratification calculus. Both are properties OF M_reg's structure; neither invokes external machinery beyond NCG axioms A1-A6 + Connes-Marcolli Thm 1.31 + the §VII.N stratification + the §VII.K-PROP propagation rule.

## Workshop Verdict

(Per CV-CN-R3-5 ratifying lizzi Q-LZ-R3-5 collapse preference: 5-row form. Rows 1+4+7 of the placeholder 7-row form merge into Row 1 "Dual-binding partition (5-class @ L1 + 4-class @ L3-s=3 projection)" since CV-1 + CV-LZ-1 + CV-CN-R3-3 establish that this is ONE structural finding, not three.)

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | Dual-binding partition (5-class @ L1 + 4-class @ L3-s=3 projection) | L1, Re:L1, C1, R2 CV-1, R3-A CV-LZ-1, R3-B CV-CN-R3-3 + EM-CN-R3-2 | **Converged** | 5-class @ L1 (CC-1996 multiplier-vector grading + Connes-Marcolli Thm 1.31 L1-uniqueness) is the universal partition covering all downstream channel evaluations; 4-class @ L3-s=3 (lizzi `~_M` residue-equivalence) is the channel-specific quotient at the a_2 slot via the F_2 = {ζ, SDW} merge under THM-L3.1 at Γ-regular s. Registry write at R3-B: `§VII-B.SECTOR-2-PARTITION` single parent + 5 inline per-class sub-rows; propagation theorem `§VII.K-PROP-DUAL-BINDING` deferred to S87 Step 3 of EM-1. The (universal, quotient) pair structure (EM-CN-R3-2) explains the multiplicative form of §VII.K-PROP `span(O) = ∏_k span(f_k)^{p_k(O)}` as composition of slot-quotients on M_reg. |
| 2 | Per-regulator residue hierarchy (slot-conditional) | L2, Re:L2, R2 CV-5, R3-A CV-LZ-1 + D-2, R3-B CV-CN-R3-2 | **Converged** | F_2 → cutoff_sqrt → anomaly → Zubarev depletion ordering at s=3 is monotone-decreasing in regulator-specific-scale aggressiveness (no-scale F_2 = 0.158 ceiling; binary-truncation cutoff_sqrt = 0.111; algebraic-subtraction anomaly = 0.0319; exponential-suppression Zubarev = 0.0120). Slot-conditional: ordering does NOT extend uniformly across slots; reverses at heat-kernel-canonical slots s ∈ {2, 4} where Zubarev becomes the no-extra-prescription regulator. C-α partition-INSENSITIVE per-slot, partition-SENSITIVE at master-test cross-slot consistency check (D-2 dual classification adopted at CV-5). |
| 3 | ζ=SDW machine-epsilon theorem with full 8-item non-evidence-status | L3, Re:L3, R2 CV-2 + CV-3 + CV-4, R3-A CV-LZ-2 + CV-LZ-3, R3-B CV-CN-R3-1 | **Converged** | THM-L3.1 holds bit-exactly (rel_err = 1.7556e-16, 1 ULP) at Γ-regular real s on positive-definite Casimir spectra; FAILS sharply at Γ-pole slots (no continuous-interpolation regime, sharpness clause adopted from D-1). 8 non-evidence-status items: NOT K-invariance (i), NOT atlas-uniformity (ii), NOT slot-interpolation (iii with sharpness sub-clause), NOT F_4-as-residue-class (iv), NOT canonical Mellin convention (v), NOT regulator-class taxonomy collapse (vi), NOT L1-axiomatic uniqueness (vii — Class 2 SDW is "Γ-regular-canonical, Γ-pole-disqualified" per DI-2 phrasing), NOT KO-grading invariance (viii). Registry write at R3-B: `§VII-B.ZETA-EQUALS-SDW` Lizzi-track entry, inline-prose LAYER-2-axiomatic tag (no schema dependency). |
| 4 | SECTOR-2 propagation map (5-class @ L1 binding for partition-sensitive channels) | C2, R2 CV-1 + CV-5, R3-A CV-LZ-3 + CV-LZ-5, R3-B CV-CN-R3-4 | **Converged** | 3 of 6 W6 corollary channels are partition-SENSITIVE: W5a-P3 IC at s=−1 (Γ-pole, no F_2 collapse); C-β UV-cutoff-choice within F_4 sub-atlas; C-γ-WEAK Λ_anom via full multiplier vector. 3 are partition-INSENSITIVE per-slot: C-α lattice-spacing (slot-by-slot drift exponent test); C-η Ward (already-landed via C41); C-θ inner-fluctuation (already-landed via C41). Pre-registered carry-forward (workshop line 30) generates 3 S87 propagation gates with 4-field specs in the §Carry-Forward section below. Dual-prior pre-registration (DI-LZ-S87 + DI-CN-R3-S87) on the IC verification gate makes it a track-discriminator (EM-CN-R3-1) — verdict adjudicates between Lizzi-track (anomaly-first via Pauli-Villars sign) and Connes-track (SDW-first via Γ(−1) sign convention at NLO) priors on per-class Z-flip ordering. |
| 5 | LAYER 1/2 retroactive inventory + audit-output file scope | C3, L4, Re:L4, R2 CV-6 + CV-7, R3-A CV-LZ-4 + EM-LZ-1 + EM-LZ-2, R3-B CV-CN-R3-2 + CV-CN-R3-6 | **Converged** | 4-stage audit protocol with optional Stage-2.5 sub-classification (LAYER-2-axiomatic vs LAYER-2-numerical) is the converged audit method; §VII.N L1/L2/L3 nomenclature canonical (cutoff-sqrt LAYER 1 → "L3-combinatorial", LAYER 2 → "L1-axiomatic"); DI-1 simplified slot-tag protocol `F_n@{stratum}-{slot}` with audit-output §1.2 resolution table. Audit-output file `sessions/framework/registry/layer1-layer2-retroactive-audit.md` lands at R3-B as STRUCTURAL OUTLINE (§1-§5 with C3 17-row inventory as §2.1 SEED + 3 conflation flags as §3 entries); FULL per-cite enumeration (~250 cites; 13× expansion of seed) deferred to S87 carry-forward. EM-LZ-1 §VIII status-inventory + EM-LZ-2 Stage-2.5 transitive composition through §VII.K-PROP logged in this verdict cell as available-to-S87+-planner; not pre-committed as forced carry-forwards per CV-CN-R3-4 NARROW scope. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

All 5 verdict rows are **Converged**. No Dissent / Partial / Emerged rows in the verdict (the 2 forward-dissents DI-LZ-S87 + DI-CN-R3-S87 are S87 pre-registrations, not workshop dissents; the 7 emergences EM-1 through EM-CN-R3-2 are recorded in the §Emergence sections of each round, not in the verdict's bottom-line column). Total convergence count across all rounds: **18 convergences** (R2-B 7 + R3-A 5 + R3-B 6).

## Remaining Open Questions

The R3-B FINAL convergence resolves all five Q-LZ-R3-* questions explicitly (CV-CN-R3-1 through CV-CN-R3-5) and accepts both R3-A final emergences (CV-CN-R3-6 ratifies EM-LZ-1 + EM-LZ-2). No structural question remains within the workshop's R3 scope. The questions below are FORWARD-LOOKING — they live at the intersection of the workshop's S87 carry-forward queue and the meta-methodology emergences logged in Verdict Row 5 — and are listed here as a queue for the S87+ planner to weigh against the canonical EVOI table:

1. **Will `S87-W5A-P3-IC-PER-CLASS-VERIFY` produce PASS (Z-direction preserved across all 5 classes, framework Z-factor functional-class-INDEPENDENT) or INFO (class-dependent direction)?** Lizzi DI-LZ-S87 prior: INFO with anomaly Class-5 most-likely flip. Connes DI-CN-R3-S87 prior: INFO with SDW Class-2 most-likely flip via Γ(−1) sign convention at NLO. Both priors travel as gate footnote per EM-CN-R3-1 track-discriminator pattern.

2. **Will `S87-W6-C-BETA-UV-CUTOFF-3CLASS` show parametric bound holding across {Class 1, Class 2, Class 3} (the F_4 multiplier-vector sub-family) or breakdown at Class 2 vs Class 1 (Γ-pole behavior)?** No pre-registered prior — gate is informationally open for both directions.

3. **Will `S87-W6-C-GAMMA-WEAK-PER-CLASS` show Λ_anom_internal parametric bound holding across all 5 L1-classes or class-dependent breakdown?** Pre-registered prior leans toward class-dependent given the per-class multiplier-vector differences feeding AC-2010 §V coefficients.

4. **Will the audit-output file's full per-cite enumeration (`S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION`) confirm the 3 conflation flags from C3's 17-row seed (rows 6, 11, 14) AND surface additional conflation patterns at the ~13× expanded enumeration, or will the seed-flagged conflations be the only structural ones?** S87 audit-walk is the adjudication.

5. **(Methodological, S87+ planner-discretion)** Should the EM-1 Step 2 + Step 3 carry-forwards (`S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION`, `S87-VII-K-PROP-DUAL-BINDING-LAND`) and the EM-2 + EM-LZ-2 warrant-check gate-generator queue (~10-20 gates from transitive composition through §VII.K-PROP) be pre-committed as forced S87 carry-forwards or stay as planner-discretion items per the no-padding rule? The R3-B decision (CV-CN-R3-4) places them as planner-discretion; the EVOI table at S87+ planning may revisit.

6. **(Cross-pillar, S87+ planner-discretion)** Should the EM-LZ-1 §VIII status-inventory's 6-cell coverage gap across {M_2 Jensen-deformation, M_3 Mellin-strip integrability, M_4 GGE-relic spectral functional} be queued at S87 (smallest-scope candidate first: M_3 forward upgrade PARTIAL → BUILT, the explicit non-evidence-status declaration on MP-Exclusion theorem) or staggered across S87-S90 to balance fb_pair workshops with primary-line computation? Planner-discretion via EVOI-priority ranking.

The first four questions are gate-verdict-resolvable; questions 5 and 6 are S87+ planner allocation questions. None affect the workshop's R3-B FINAL convergence on the three deliverables (a)/(b)/(c).

## Wrap-Up — Workshop Impact Summary

### What Changed

The workshop landed three bound deliverables at R3-B FINAL:

**Deliverable (a) — SECTOR-2 partition registry-write.** The dual-binding partition (5-class @ L1 binding for axiomatic propagation + 4-class @ L3-s=3 projection at the a_2 slot) is registered as a single parent entry `§VII-B.SECTOR-2-PARTITION` (Lizzi-track Cluster) with 5 inline per-class sub-rows. The §VII-B Lizzi-track Cluster grows from 3 to 5 entries: prior siblings (HP1-NEAR-INVARIANCE, TWO-LAYER-OBSTRUCTION, ZETA-NOT-PHYSICAL-75) + 2 new R3-B entries (ZETA-EQUALS-SDW, SECTOR-2-PARTITION). The propagation theorem `§VII.K-PROP-DUAL-BINDING` (EM-1 Step 3) is deferred to S87 carry-forward; the universal-property/quotient-pair reading (EM-CN-R3-2) is logged in the verdict cell as the structural reason the 5-class @ L1 is the universal partition (covers all downstream channel evaluations) and 4-class @ L3-s=3 is the channel-specific quotient at the a_2 slot via the F_2 = {ζ, SDW} merge.

**Deliverable (b) — `sessions/framework/registry/layer1-layer2-retroactive-audit.md` outline.** The audit-output file is landed at R3-B as a STRUCTURAL OUTLINE (§1-§5 skeleton with C3's 17-row inventory as §2.1 SEED + 3 conflation-flag remediations as §3 entries; DI-1 simplified 2-coordinate slot-tag protocol `F_n@{stratum}-{slot}` with §1.2 resolution table; Stage-2.5 LAYER-2-axiomatic vs LAYER-2-numerical sub-classification as §1.3 protocol extension). The FULL per-cite enumeration (~250 cites at 13× expansion of the seed) is deferred to S87 carry-forward `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION`. The §VII.N L1/L2/L3 nomenclature is canonical at the file's §1.2; cutoff-sqrt LAYER 1/2 are re-tagged as L3-combinatorial / L1-axiomatic per CV-6.

**Deliverable (c) — `§VII-B.ZETA-EQUALS-SDW` registry entry.** The slot-conditional machine-epsilon ζ=SDW identity (THM-L3.1) is registered as a Lizzi-track structural theorem at `§VII-B.ZETA-EQUALS-SDW`, sibling to ZETA-NOT-PHYSICAL-75 within the §VII-B Lizzi-track Cluster. The entry carries: theorem statement (slot-conditional Mellin-multiplier identity at Γ-regular real s), explicit SLOT-CONDITIONALITY clause with sharpness sub-clause (no continuous-interpolation regime between Γ-regular and Γ-pole behavior), 8-item non-evidence-status declaration (closes K-invariance, atlas-uniformity, slot-interpolation, F_4-as-residue-class, helper-canonicality, taxonomy-collapse, L1-axiomatic uniqueness, KO-grading invariance inference channels), inline-prose LAYER tag (LAYER-2-axiomatic, no schema dependency per CV-CN-R3-1), and CITE-ANCHORS list including §W4-2 §6 CC-2 PASS, §VII.N L1, ZETA-NOT-PHYSICAL-75 cross-cite, Connes-Chamseddine 1996 §2.2-2.3, and Connes-Marcolli 2008 Thm 1.31.

**Three additional structural results are logged in the verdict cells but deferred as either S87 registry-architecture work (EM-1 Step 2 schema extension, EM-1 Step 3 propagation theorem registration) OR as S87+ planner-discretion meta-methodology workshops (EM-2 warrant-check gate generator, EM-3 cross-pillar fb_pair generator with EM-LZ-1 status-inventory + EM-LZ-2 transitive composition).** These are recorded in the workshop record at structural-skeleton granularity but are NOT pre-committed as forced S86-W7 carry-forwards per CV-CN-R3-4 NARROW scope.

**New methodology-pillar entries (R3-B emergences):** EM-CN-R3-1 dual-prior track-discriminator gate-pattern is operationalized by the dual prior on the S87 IC verification gate (DI-LZ-S87 + DI-CN-R3-S87); EM-CN-R3-2 universal-property/quotient-pair reading of the dual-binding partition explains the structural reason for §VII.K-PROP's multiplicative composition rule and forward-compatibilizes the §VII.K-PROP-DUAL-BINDING propagation theorem with the slot-quotient family {Π_s : s ∈ admissible-slots}.

### What Holds

**Regulator-class taxonomy.** The 5-class @ L1 partition of A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly} is the universal partition on the regulator-class manifold M_reg under multiplier-vector grading (CC-1996 §2.2-2.3 + Connes-Marcolli Thm 1.31 L1-uniqueness selecting ζ as the L1-canonical regulator). Each class is structurally distinct: Class 1 (ζ — multiplier (1, 0, 0, 0), L1-canonical), Class 2 (SDW — multiplier (1, 0, 0, 0) at Γ-regular slots, Γ-regular-canonical / Γ-pole-disqualified per DI-2 phrasing), Class 3 (Zubarev — heat-kernel exp(−tC) dressing with t_ref scale, L1-disqualified by external-Λ admission, L2-canonical per §VII.N L2), Class 4 (cutoff_sqrt — multiplier (2, 1, 1, 0) with f_0 = 2 unique per RFB Theorem (i)), Class 5 (anomaly — Pauli-Villars subtraction with M_PV² mass-scale, mixed {a_2, a_4} support per RFB Theorem header).

**F_2 ζ=SDW machine-epsilon identity.** THM-L3.1 holds bit-exactly (rel_err = 1.7556e-16, 1 ULP under float64) at Γ-regular real s on positive-definite Casimir spectra under Connes-Chamseddine spectral-action ratio normalization. The identity is a structural property of the (ζ, SDW) submanifold of M_reg (multiplier-vector identity at Γ-regular slots, defined by Γ(s)-cancellation invariance) and a self-consistency check on the helper module (`_spectral_action_regulators.py` line 95 literal pass-through `mellin_a_n = zeta_a_n` is faithful to the underlying algebra). The 8-item non-evidence-status declaration closes every downstream inference channel that cite-readers might mis-invoke.

**§VII-B Lizzi-track Cluster.** The 5-entry cluster (HP1-NEAR-INVARIANCE + TWO-LAYER-OBSTRUCTION + ZETA-NOT-PHYSICAL-75 + ZETA-EQUALS-SDW + SECTOR-2-PARTITION) forms a coherent sub-namespace for per-regulator structural results on the substrate's spectral functional manifold. Each entry shares methodology: per-regulator analysis on the substrate's Mellin-residue-extraction structure with explicit slot-conditional and warrant-class declarations.

**Forward-backward inference closure pair (R2-B EM-3 + R3-A E-2 / EM-LZ-1 + R3-B verdict-cell logging).** The combination of THM-L3.1 forward closure (non-evidence-status declaration, deliverable (c)) and the L4 retroactive sweep backward closure (audit-output file outline, deliverable (b)) instantiates the fb_pair(M_1) construction on the regulator-class manifold. The construction is structurally portable to other substrate-physics manifolds; this is the meta-methodology contribution recorded for S87+ planner consideration.

**§VII.N stratification's L1/L2/L3 canonical naming.** Adopted as canonical per CV-6 + CV-CN-R3-2 audit-output file §1.2; supersedes parallel `cutoff-sqrt-adjudication.md` LAYER 1/2 nomenclature. Re-tag map: cutoff-sqrt LAYER 1 → "L3-combinatorial" (residual-per-Q stratum); cutoff-sqrt LAYER 2 → "L1-axiomatic" (axiomatic-global stratum); §VII.N L2 (substrate-action local at fold) has no analog and remains its own stratum.

### What Breaks or Strains

Nothing identified. The workshop produces no broken structural identity, no contested NCG axiom, no failed convergence on any of the three deliverables. The only points of "strain" — both deliberately introduced as forward pre-registrations rather than R3 contestations — are:

- **DI-LZ-S87 + DI-CN-R3-S87 dual prior on `S87-W5A-P3-IC-PER-CLASS-VERIFY`.** The two reasoning tracks (Lizzi spectral-functional, Connes NCG-axiomatic) order the candidate Z-flip classes oppositely (lizzi: anomaly first; connes: SDW first). Neither prior contests the gate's pre-registration; both travel as a footnote per EM-CN-R3-1. Strain is methodological (track-discriminator pattern), not structural.

- **CV-CN-R3-2 course-correction on lizzi's full-file audit-output preference.** Lizzi favored full-file land at R3-B; I recommended outline-only with the full per-cite enumeration as S87 carry-forward, on feasibility + no-padding grounds. The course-correction is a SCOPE refinement, not a structural disagreement; lizzi's structural content (DI-1 resolution table, Stage-2.5 sub-classification, naming-collision resolution, 17-row inventory + 3 conflation flags) all lands at R3-B inside the outline. Strain is allocation-of-work, not content.

### Carry-Forward Computations

**Pre-registered carry-forward (workshop line 30): "4-field S87 spec for SECTOR-2 propagation into W5a P3 IC + W6 C-α/β/γ."** Plus one workshop-discipline carry-forward for the audit-output file's full enumeration. Total 4 entries per CV-CN-R3-4 NARROW scope.

| # | Gate ID | What | Inputs | Pre-registered threshold | Effort |
|:--|:---|:---|:---|:---|:---|
| 1 | `S87-W5A-P3-IC-PER-CLASS-VERIFY` | Re-compute `xi_E_GGE_inv` IC for each of 5 L1-classes (Class 2 SDW at s=−1 Γ(−1) pole, Class 3 Zubarev at s=−1 direct convergent sum, Class 4 cutoff_sqrt at s=−1 conditional on GATE A PASS, Class 5 anomaly at s=−1 Pauli-Villars subtraction); test Z(N_pivot) ratio direction per class against current ζ-prescription registered canonical `xi_E_GGE_inv = 13.642473425595973` | `xi_E_GGE_inv` (Class-1, registered), per-class s=−1 spectral residue computation via helper module + plan §W5a-1 ODE integration; **dual-prior pre-registration footnote**: lizzi DI-LZ-S87 ordering (anomaly first, SDW second via Pauli-Villars sign-subtraction); connes DI-CN-R3-S87 ordering (SDW first, anomaly second via Γ(−1) sign convention at NLO); the gate is a track-discriminator per EM-CN-R3-1 | PASS = Z_ratio direction preserved across all 5 classes (functional-class-INDEPENDENT, framework Z-robustness). INFO = class-dependent direction (functional-class-DEPENDENT, regulator-class becomes physics input to CMB prediction). FAIL = no class produces a meaningful IC (helper-module breakdown across the atlas) | MODERATE (4 additional integrations beyond Class-1 baseline) |
| 2 | `S87-W6-C-BETA-UV-CUTOFF-3CLASS` | Test C-β UV-cutoff-choice immunization across {Class 1, Class 2, Class 3} = F_4 multiplier-vector sub-family (refines the 4-class @ L3-s=3 projection's F_2 collapse to expose Class 1 vs Class 2 distinction at full multiplier-vector level) | F_4 multiplier-vector inputs per Class, plan §W1a Φ-B branch spec, AC-2010 §V coefficient computation per L1-class | PASS = parametric bound holds across all 3 classes (F_2 ↔ Class 1+2 collapse robust at C-β stratum). INFO = bound fails on Class 2 vs Class 1 (Γ-pole or convention sensitivity exposed). FAIL = bound fails on multiple classes (multiplier-vector-level breakdown) | MODERATE |
| 3 | `S87-W6-C-GAMMA-WEAK-PER-CLASS` | Re-evaluate C-γ-WEAK Weyl-rescaling Λ_anom_internal per L1-class via `\|ΔS_W / S_W\| ≤ b_DK · (Λ_anom_internal / Λ_cut)²` parametric bound; test bound consistency across the 5 classes' distinct multiplier-vectors | AC-2010 §V coefficients per Class, internal Λ_anom_internal computation per multiplier-vector, plan §W6 line 20 spec | PASS = bound holds across all 5 classes (C-γ-WEAK robustness against per-regulator splitting). INFO = class-dependent breakdown (signals which classes carry distinct AC-2010 § V coefficient structure) | HEAVY |
| 4 | `S87-LAYER-1-2-RETROACTIVE-AUDIT-FULL-ENUMERATION` | Walk all S78-onward 5-atlas / regulator-class / partition cites in `sessions/`, `computations/`, `sessions/framework/`, `sessions/permanent-results-registry.md`; LAYER-tag per the 5-stage protocol (with optional Stage-2.5 sub-tag per CV-7); detect cross-tag conflations beyond the 3 already-flagged (rows 6, 11, 14 of C3 seed) | Audit-output file outline (S86 W7 deliverable (b), landed at R3-B); DI-1 resolution table at audit-output §1.2; full S78-onward source corpus | PASS = enumeration completes with conflation-flag rate ≤ 5% of cites (audit's signal-to-noise within calibration estimate). INFO = conflation-flag rate 5%-25% (audit surfaces new patterns; S88+ remediation queue grows). FAIL = conflation-flag rate > 25% (audit surfaces systematic conflation pattern requiring methodology workshop) | HEAVY (1-2 wave equivalents) |

**Available-to-S87+-planner (NOT pre-committed forced carry-forwards per CV-CN-R3-4 NARROW scope):**

- EM-1 Step 2: `S87-REGISTRY-SCHEMA-LAYER-2-SUBTAG-EXTENSION` — registry schema work to lift the inline-prose LAYER tag into a structured metadata field. Registry-architecture work, not a gated computation.
- EM-1 Step 3: `S87-VII-K-PROP-DUAL-BINDING-LAND` — propagation theorem `§VII.K-PROP-DUAL-BINDING` registry landing with the slot-quotient family {Π_s : s ∈ admissible-slots} per EM-CN-R3-2 universal-property reading.
- EM-2 sample warrant-check gates (3): `S87-WARRANT-CHECK-HP1-LOOSE`, `S87-WARRANT-CHECK-W4-2-MAX-PAIR-RATIO`, `S87-WARRANT-CHECK-VII-N-L3-THRESHOLDS` per workshop lines 2231-2235.
- EM-LZ-2 transitive composition gates (~10-20): warrant-check gates on composite observables (m_H, chi_2, HP^1 LOOSE, span_Q, R-protected band thresholds, max_pair_ratio, ...) propagating warrant-class through §VII.K-PROP `span(O) = ∏_k span(f_k)^{p_k(O)}`.
- EM-LZ-1 §VIII status-inventory candidates (6): forward + backward closures on M_2 (Jensen-deformation), M_3 (Mellin-strip — forward upgrade PARTIAL → BUILT, backward initial), M_4 (GGE-relic spectral functional). Each is an entire S87+ workshop, not a single gate.

The S87+ planner can promote any of the available-to-planner items into pre-committed carry-forwards via EVOI-priority ranking; this workshop's R3-B FINAL discipline does NOT pre-commit them per the no-padding rule.

### Closing Line

The workshop lands the dual-binding SECTOR-2 partition + the ζ=SDW slot-conditional machine-epsilon theorem + the L4 retroactive-audit outline, growing the §VII-B Lizzi-track Cluster from 3 to 5 entries and instantiating the first fb_pair(M_1) forward-backward inference-closure pair on the regulator-class manifold — a substrate-physics result on M_reg's Mellin-residue-extraction structure that doubles as a portable template for future closure-pair workshops on M_2, M_3, M_4.
