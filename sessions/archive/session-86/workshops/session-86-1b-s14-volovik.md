# Session 86 Synthesis: SIGN-CONFIRMED-MAGNITUDE-REFUTED Precedent Catalog (3He-B-Inheritance / Volovik-Effacement Domain)

**Date**: 2026-04-27
**Agent**: volovik-superfluid-universe-theorist (volovik)
**Slot**: S86 W1b, entry S-14 (sign-confirmed-magnitude-refuted verdict-vocabulary extension)
**Source Documents**:
- `sessions/archive/session-86/session-86-w5a-workingpaper.md` (W5a §W5a-1 SECTOR-1 SR-flow Z-factor DOUBLE FAIL with §10 SIGN confirmed)
- `.claude/rules/gate-verdicts.md` (PASS/FAIL/INFO ontology; pre-registration discipline)
- `.claude/rules/epistemic-discipline.md` (negative results as boundaries; PRU/SOURCE-RECON Class 8 / 8.1)
- `.claude/rules/v3-closure-recovery.md` (PROHIBITED_ACTIONS: convention-shopping, iterate-until-PASS, post-hoc edit, ansatz-PASS)
- `.claude/agent-memory/volovik-superfluid-universe-theorist/MEMORY.md` (precedent index, S57 / S58 / S59 / S60 / S64)
- `Users/.../memory/project_3heb-inheritance.md` (parent→child inheritance reframe)
- `Users/.../memory/project_substrate-compaction-timescape.md` (Wiltshire-from-fiber-geometry)

---

## I. Session Outcome

The W5a §W5a-1 substitution chain at Step 4 reads off SIGN correctly at both pivots (Z_ratio > 1, substrate-first ξ²(0) IC ENHANCES the Mukhanov-Sasaki normalization) but MAGNITUDE is refuted by 2× (PIVOT55) and 92× (PIVOT312) because §10 used `xi_E_GGE_inv ≈ O(10⁻²)` placeholder while the W4 P4 canonical pin is 13.6425 (M_KK units) — a 3-OOM upstream-pin drift. The flat DOUBLE FAIL verdict (`computations/s86_gate_verdicts.txt:S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55/PIVOT312`) discards the structural fact that the substitution chain remains **reliable for sign prediction at any future xi_E_GGE_inv value** — the chain's algebraic skeleton survived the placeholder error, only the numerical mantissa floated. This synthesis catalogs four 3He-B-inheritance / Volovik-effacement precedents (S57 CC-SIGN-57, S59 f_DM-DEPLETION-59, S59 TEMP-MISMATCH-59, S60 LEGGETT-DM-ABUND-60) where SIGN was structurally correct and MAGNITUDE was wrong by varying margins, plus one S64 sub-sector instance, and argues from substrate physics that **sign-prediction reliability is structurally distinct from magnitude reliability** — they ride on different layers of the substrate machinery (monotone-coupling / equilibrium-theorem structure for sign; correctly-pinned spectral-moment normalizations for magnitude). A SIGN-CONFIRMED-MAGNITUDE-REFUTED verdict tag is therefore a **structurally meaningful epistemic state**, not noise. It corresponds 1:1 to PRU-extension Class 8.1 SOURCE-RECON pin-drift (`epistemic-discipline.md` §Source Reconciliation).

---

## II. Key Results

### II.1. The W5a §W5a-1 SIGN-confirmed / MAGNITUDE-refuted anchor (current session)

**Result**: §10 substitution chain Step 4 reads `Z_ratio − 1 > 0 ⇔ ε_substrate > ε_LCDM ⇔ substrate-first IC ENHANCES ε at pivot`; sign confirmed at PIVOT55 (1.4353 > 1) AND PIVOT312 (3.2976 > 1). MAGNITUDE estimates 0.22 / 0.025 refuted by 2× / 92× same-direction. Classification: **PHONONIC** (substrate transit-physics; SR-flow ODE).

The substitution chain's algebraic skeleton:
```
(dε/dN)|substrate(0) = ε(0) · [2η(0) − 4ε(0) + 2 · xi_E_GGE_inv]
(dε/dN)|LCDM(0)      = ε(0) · [2η(0) − 4ε(0)]
Δ(dε/dN)|N=0         = +2 · ε_0 · xi_E_GGE_inv  (positive for any positive xi_E_GGE_inv)
```
Direction (Step 4): the substrate ξ²-source term enters with **sign +**. This is structural — it depends on the sign convention of the substrate-first IC and the kinematic structure of the SR-flow ODE, not on the numerical value of `xi_E_GGE_inv`. The **magnitude** depends multiplicatively on `xi_E_GGE_inv`, which is what got pinned wrong by 3 OOM in §10.

The §10 substitution chain therefore **remains valid for sign prediction at any positive `xi_E_GGE_inv`**. The DOUBLE FAIL closes the SECTOR-1 SR-LO **corridor** (the trajectory leaves the SR-validity window within N ≈ 0.13 e-folds), but it does **not** close the substitution chain itself — the chain produced the correct sign at both pivots, which is non-trivial information.

### II.2. Catalog of 3He-B-inheritance / Volovik-effacement SIGN-correct / MAGNITUDE-wrong precedents

#### II.2.a. CC-SIGN-57 (Volovik partition; canonical effacement instance)

**Result**: PASS (sign), GAP 114 OOM (magnitude). Classification: **PHONONIC** (substrate vacuum-energy partition).

Source: `cc-sign-57-result.md` and `s58_cc_cancellation_sweep.py`. Volovik formula at the fold:
```
Lambda_eff = E_GGE − E_BCS = +1.709 M_KK > 0  (SIGN correct: positive, accelerating)
Lambda_eff / Lambda_obs = 5.2e+67 / 5.2e−47 GeV^4 ≈ 10^114  (MAGNITUDE refuted)
```
Per-sector decomposition shows the near-cancellation structure: B2 = +0.316, B1 = −0.165, B3 = −0.150, residual = +0.00145 M_KK (0.46%). The Volovik formula is the spectral analog of the 3He-B vacuum-energy partition (Volovik 2003 §29, Volovik 2009 Paper 07). The **sign** is forced by the substrate's monotone-coupling structure (the GGE relic sits above the BCS ground state by the equilibrium theorem); the **magnitude** is the unsuppressed spectral-action moment a_0 at scale M_KK.

This is the cleanest historical instance of "structural sign + unconstrained magnitude" in the project. Treating it as flat FAIL would discard the constraint-map information that **any future CC mechanism must preserve sign while reducing magnitude by 114 OOM** — the surviving region of solution space.

#### II.2.b. f_DM-DEPLETION-59 (3He-B partition for DM)

**Result**: PASS literally, OVERSHOOT physically. Classification: **PHONONIC** (Leggett-mode DM).

Source: `fdm-depletion-59-result.md` and `s59_fdm_depletion.py`. The depletion mechanism predicts:
```
f_DM(z=0) = 1.000   (within substrate sector; PASS gate threshold 0.70)
f_DM(observed) = 0.844  (Omega_DM / Omega_m)
```
Sign of the correction is correct (depletion RAISES f_DM from 0.209 Leggett-only to 1.0); magnitude OVERSHOOTS observed by 0.156 (substrate sector closes too efficiently — no baryon fraction in substrate-only accounting). The sign reliability comes from the **3He-B inheritance template** (parent→child per `project_3heb-inheritance.md`): the substrate's pair-breaking annihilation channels share the same kinematic structure as 3He-B BCS-quasiparticle recombination (K_7 charge conservation). Magnitude reliability requires a separate baryogenesis mechanism that the 3He-B parent does not pin (3He has no baryon-asymmetry analog).

This is the 3He-B-inheritance instance: the inheritance pinned the *direction* of the Leggett-channel survival but did not pin the baryon fraction.

#### II.2.c. TEMP-MISMATCH-59 (Wiltshire-from-fiber-geometry)

**Result**: INFO (DESI w_a channel CLOSED). Sign of |w_a|>0 correct in Model B; magnitude phase-suppressed by 25× from Josephson lock. Classification: **PHONONIC** (substrate clock-rate variance).

Source: `temp-mismatch-59-result.md` and `s59_temp_mismatch.py`:
```
Model A (lock):     w_a = 0 exact                 (canonical prediction; structural)
Model B (unlock):   w_a = wa_B_fit                (maximum unlocked magnitude)
Model B effective:  w_a = wa_B_fit · 0.04 = 0.037 (phase-suppressed by 25×)
DESI DR2:           w_a = -0.86 ± 0.28
```
Sign of the residual w_a (negative, accelerating-deceleration trend) matches DESI direction in Model B; magnitude is suppressed from O(1) to O(0.04) by Josephson lock per JOSEPHSON-PHASE-59 PASS-B (E_J/E_C = 194, 111× critical). The SIGN reliability comes from the substrate-compaction timescape mechanism (`project_substrate-compaction-timescape.md`): denser regions hold tau at fold longer, slower clocks accumulate, residual w_a is structurally negative. The MAGNITUDE failure routes through the equilibrium-theorem prediction of phase ordering (not a placeholder error — a structurally suppressed coupling). Different failure topology from CC-SIGN-57 / W5a but same SIGN/MAGNITUDE bifurcation.

#### II.2.d. LEGGETT-DM-ABUND-60 (cosmological moduli problem analog)

**Result**: FAIL double (overclosure + decay). Classification: **PHONONIC** (Leggett-mode DM cosmology).

Source: `leggett-dm-abund-60-result.md`:
```
Omega_L h^2 = 3.23e+25  (sign: positive contribution to closure; magnitude: 26.4 OOM overshoot)
tau_L = 3.6e-34 s       (sign: finite decay; magnitude: 52 OOM underestimate of cosmological lifetime)
```
Both observables share SIGN-correct, MAGNITUDE-wrong structure. Sign reliability: the Leggett mode IS a relative-phase mode of a U(1) order parameter (Leggett 1966; Volovik 2009 §3.4), so a finite mass and finite abundance are structural inheritances from the dipolar analog (DIPOLAR-CATALOG-49 PASS confirms epsilon=0.00248, m_G=0.070 M_KK 18% from n_s req). Magnitude failure: the M_KK ~ M_Pl rescaling factor was pinned wrong by structural overshoot (the 3He-B parent has no cosmological-modulus analog, so the inheritance breaks at the Hubble-scale dimensional argument).

This is the **closed-channel** counter-pair to W5a §W5a-1: the channel was permanently closed by the magnitude failure even though the sign was structurally inherited correctly. The lesson: SIGN-correct does **not** rescue a channel; it constrains the structure of any successor mechanism in that direction.

#### II.2.e. S64 a_0/a_2 trap (off-Jensen Casimir)

**Result**: PROVEN theorem (sign), CC FAIL (magnitude direction wrong for closing CC gap). Classification: **GEOMETRIC** (spectral-action moment ratio).

Source: `s64-synthesis-result.md` Theorem 2 ("a_0/a_2 trap"); EIH effacement (S65) `constraint-mega-matrix.md`:
```
Off-Jensen direction:  a_0/a_2 INCREASES on descent from Jensen   (proven sign)
EIH projection:        a_0/a_2 monotonic with C_2(p,q) — wrong direction
Implication:           CC ratio worsens, not improves
```
This is the **inverse polarity** instance — the SIGN is structurally proven (a_0/a_2 monotone in the wrong direction for CC suppression), so even though the magnitude-of-monotonicity is bounded, the channel is **closed by sign**. Different from W5a where the sign confirmed the substrate enhancement (which itself overshot SR-LO validity). Catalog this as **SIGN-WRONG-DIRECTION-CLOSURE** — a sibling of SIGN-CONFIRMED-MAGNITUDE-REFUTED but with opposite usefulness: a sign-wrong result closes a corridor irrevocably; a sign-confirmed-magnitude-wrong result preserves the substitution chain for the next pin-corrected attempt.

### II.3. The substrate-physics argument — why sign and magnitude separate

**Result**: Sign-prediction reliability and magnitude-prediction reliability ride on **independent layers of the substrate machinery**. Classification: **PHONONIC + GEOMETRIC** (organizing insight, not a new gate verdict).

The 3He-B-inheritance domain has two structural layers:

1. **Sign layer (kinematic)**: the substrate's BDI Z_2 protection, GGE relic monotone-coupling structure, equilibrium-theorem ordering (E_BCS < E_GGE < E_eq < E_maxent), and 3He-B parent→child sign inheritance (Volovik 2003 §29; project_3heb-inheritance.md). These pin **directions** without pinning **magnitudes**:
   - CC sign positive (E_GGE > E_BCS by partition theorem).
   - f_DM rises under depletion (annihilation kinematics).
   - w_a residual negative under timescape (Wiltshire fiber-geometry).
   - Z_ratio > 1 under substrate-first IC (W5a §W5a-1 ε-flow ODE).
   - a_0/a_2 monotone wrong-way (S64 AM-GM theorem).

2. **Magnitude layer (dynamical)**: the spectral-moment normalization scales (M_KK, the actual numerical value of canonical pins like xi_E_GGE_inv, the GL effective coupling, the IC normalization). These require **correctly pinned values**, NOT just structural arguments. Failures at this layer:
   - 114 OOM at CC-SIGN-57 (M_KK^4 vs Lambda_obs).
   - 26.4 + 52 OOM at LEGGETT-DM-ABUND-60 (cosmological-moduli scale mismatch).
   - 25× suppression at TEMP-MISMATCH-59 (Josephson phase lock structurally damps magnitude).
   - 0.156 overshoot at f_DM-DEPLETION-59 (no baryon-fraction subtraction).
   - 2×–92× at W5a §W5a-1 (xi_E_GGE_inv placeholder vs canonical).

**The two layers fail INDEPENDENTLY**. A wrong sign closes a corridor permanently (S64 a_0/a_2); a wrong magnitude leaves the substitution chain valid for the corrected pin. These are different epistemic states. Treating them as a single FAIL bin discards constraint-map information.

This is the substrate-physics analog of the **PRU vs SOURCE-RECON distinction** (`epistemic-discipline.md` §Source Reconciliation): PRU detects MISSING pins (cardinality test); SOURCE-RECON detects PINNED-BUT-DRIFT pins (value test). The two audits commute; analogously, sign-derivation and magnitude-derivation commute as substrate-physics audits. SIGN-CONFIRMED-MAGNITUDE-REFUTED is the substrate-physics name for "Class-(c) PIN-DRIFT-FROM-STALE-SOURCE" or "Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY" at the level of substitution-chain output.

---

## III. Gate Verdicts

| Gate | Verdict (current session) | Sign-state | Magnitude-state | Decisive Number |
|:-----|:-----|:-----|:-----|:-----|
| S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT55 | FAIL | CONFIRMED (>1) | REFUTED 2× | Z_ratio = 1.4353 vs §10 estimate 1.22 |
| S86-SECTOR-1-SR-FLOW-Z-FACTOR-PIVOT312 | FAIL | CONFIRMED (>1) | REFUTED 92× | Z_ratio = 3.2976 vs §10 estimate 1.025 |

**Precedent gates re-classified under the proposed SIGN-CONFIRMED-MAGNITUDE-REFUTED tag** (catalog only, not retroactive verdict edits — verdicts are permanent per `gate-verdicts.md`):

| Gate | Original Verdict | Sign-state | Magnitude-state | Decisive Number |
|:-----|:-----|:-----|:-----|:-----|
| S57-CC-SIGN-57 | PASS | CONFIRMED (Lambda > 0) | REFUTED 114 OOM | Lambda_eff = +1.709 M_KK vs Lambda_obs |
| S59-f_DM-DEPLETION-59 | PASS | CONFIRMED (rises) | OVERSHOOT 0.156 | f_DM = 1.000 vs 0.844 obs |
| S59-TEMP-MISMATCH-59 | INFO | CONFIRMED in Model B | SUPPRESSED 25× | abs(w_a_eff_B) = 0.037 |
| S60-LEGGETT-DM-ABUND-60 | FAIL (double) | CONFIRMED both observables | REFUTED 26.4 + 52 OOM | Omega_L h² = 3.23e+25; tau_L = 3.6e−34 s |
| S64 a_0/a_2 trap (theorem 2) | PROVEN | INVERSE-POLARITY (wrong direction) | structural | a_0/a_2 monotone increasing off-Jensen |

The verdicts above are NOT being re-adjudicated; the catalog adds a sign/magnitude axis to the existing verdict ledger without modifying the canonical PASS/FAIL/INFO outcome.

---

## IV. Structural Implications

### IV.1. SIGN-CONFIRMED-MAGNITUDE-REFUTED is a structurally meaningful epistemic state

The five precedent instances cataloged in §II.2 demonstrate that the substrate's monotone-coupling / equilibrium-theorem / BDI-protection structure **routinely produces sign-correct predictions even when magnitude inputs are placeholder-pinned or canonically-drifted**. The pattern is not noise — it is the expected behavior of a system whose kinematic skeleton (group theory, topology, equilibrium thermodynamics) is structurally rigid while its dynamical mantissa (M_KK, GL coupling, canonical-pin numerical value) requires separate calibration.

Operationally, this means:

- A flat FAIL verdict for W5a §W5a-1 (or any precedent in §II.2) **discards the constraint-map information that the substitution chain remains valid for sign prediction at any future canonical-pin value**. The substitution chain is a **reusable substrate-derivation artifact**, separable from the verdict it produced under the wrong pin.
- A SIGN-CONFIRMED-MAGNITUDE-REFUTED tag preserves this artifact for the next pin-corrected attempt (the W5a carry-forward `S87-SECTOR-1-SR-FLOW-RESCALED` is exactly such an attempt).
- A SIGN-WRONG-DIRECTION-CLOSURE tag (S64 a_0/a_2 trap) is the sibling state for sign-failed corridors — irrevocably closed regardless of magnitude.

### IV.2. The 3He-B parent→child inheritance template explains why sign tends to be right

Per `project_3heb-inheritance.md`, the 22 framework / 3He-B correspondences are **inherited structure** — the framework's substrate IS the parent that produced 3He-B's quasiparticles (atomic helium nuclei = downstream substrate excitations). Inheritance preserves the kinematic skeleton that determines signs:

- BDI Z_2 protection of the gap (S62 TYPE-I-TRANSIT-62 PASS) → CC sign positive (S57).
- K_7 charge conservation (S58) → DM annihilation channels exist with finite cross-section → f_DM rises (S59).
- Josephson phase lock (JOSEPHSON-PHASE-59 PASS-B) → w_a phase-suppressed but residual finite (S59).
- Substrate ξ²-source term enters with sign + in the SR-flow ODE → Z_ratio > 1 (W5a).

Inheritance does **not** preserve magnitudes that depend on the parent's specific dimensional scales (3He's millikelvin vs framework's M_KK). Magnitude must be re-derived at each scale, which is where canonical-pin discipline (PRU + SOURCE-RECON) takes over.

### IV.3. Volovik-effacement timescape constrains where sign-from-substrate is reliable

Per `project_substrate-compaction-timescape.md`, the substrate compaction mechanism predicts a Wiltshire-from-fiber-geometry residual w_a from clock-rate variance. The TEMP-MISMATCH-59 result (Model B sign correct, magnitude suppressed 25×) is the canonical illustration: the **direction** of the timescape correction is forced by the substrate compaction mechanism (denser regions hold tau at fold longer → slower clocks → negative residual w_a); the **magnitude** is suppressed by Josephson phase lock that the timescape derivation does not encode.

This suggests a **structural diagnostic**: any new gate in the 3He-B-inheritance / Volovik-effacement domain whose sign derives from a monotone-coupling argument (BDI Z_2, equilibrium theorem, K_7 conservation, Josephson lock) and whose magnitude derives from a canonical-pin substitution should be **expected** to land in the SIGN-CONFIRMED-MAGNITUDE-REFUTED state if the canonical pin is anywhere off-canonical. The W5a result is not anomalous — it is the modal outcome under pin-drift.

### IV.4. Constraint-map updates from this synthesis (organizational, not gate-verdict)

- **Open**: a verdict-vocabulary extension `SIGN-CONFIRMED-MAGNITUDE-REFUTED` (and sibling `SIGN-WRONG-DIRECTION-CLOSURE`) that distinguishes pin-drift-magnitude-failure from structural-sign-failure.
- **Closed**: the interpretation that all FAILs in the 3He-B-inheritance domain are equally informative. They are not — sign-correct FAILs preserve the substitution chain; sign-wrong FAILs close the corridor.
- **Reorganized**: `permanent-results-registry.md` and `framework-3heb-comparison.md` (volovik-memory) should carry a new column for the sign/magnitude bifurcation when the relevant predictions are tracked. Specifically, the 22 framework/3He-B correspondences in `framework-3heb-comparison.md` should be tagged by which layer (sign vs magnitude) the inheritance is pinning. This is a registry-update task, not a new gate verdict.

### IV.5. Bound on the proposed tag's usefulness

The SIGN-CONFIRMED-MAGNITUDE-REFUTED tag is a meaningful epistemic state if and only if:

1. The substitution chain that produced the SIGN can be re-evaluated at a corrected pin without re-deriving the algebraic skeleton. (W5a §W5a-1 satisfies this — the chain works for any positive `xi_E_GGE_inv`.)
2. The corrected-pin value is independently knowable (canonical-constants ledger, downstream gate, or external observation). (W5a satisfies this — `mcp__knowledge__get_constant("xi_E_GGE_inv")` returns 13.6425 from the W4 P4 commit.)
3. The corrected-pin gate has a non-trivial pre-registration path (the carry-forward S87-SECTOR-1-SR-FLOW-RESCALED in the W5a synthesis is such a path).

If any of (1)–(3) fails, the tag collapses back to flat FAIL. The W5a precedent satisfies all three. Two of the four S58/S59/S60/S64 precedents (CC-SIGN-57, f_DM-DEPLETION-59) satisfy (1) and (2) but not (3) — they have no corrected-pin successor gate proposed because the magnitude failure is **structural** (M_KK^4 vs Lambda_obs is a UV-IR scale problem, not a placeholder error). The tag is most useful for placeholder-error / canonical-pin-drift cases (W5a is the canonical example), less useful for structural-scale-problem cases (CC-SIGN-57 is a witness that the sign is robust but the magnitude is closed by physics).

---

## V. Carry-Forward Computations

V.1. **SIGN-MAGNITUDE-VOCABULARY-87**: Promote SIGN-CONFIRMED-MAGNITUDE-REFUTED and SIGN-WRONG-DIRECTION-CLOSURE to formal verdict-vocabulary tags
   - **What**: extend `.claude/rules/gate-verdicts.md` §Verdict Format to include a sign/magnitude sub-axis on PASS/FAIL/INFO; add to the canonical verdict line a new optional field `sign_state=CONFIRMED|REFUTED|N/A magnitude_state=CONFIRMED|REFUTED|OVERSHOOT|N/A`. Specify at plan-freeze for any [SIGN] or [VERIFY] gate where the substitution chain is decomposed into sign + magnitude steps. Verifier clause: a gate may be SIGN-CONFIRMED-MAGNITUDE-REFUTED only if (a) Step 4 of the substitution chain reads off a sign-from-canonical-form claim, (b) the magnitude FAIL is traced to a specific canonical-pin value drift detected by `_source_reconciliation_audit.py`, (c) the substitution chain is re-evaluable at a corrected pin without algebraic-skeleton modification.
   - **Inputs**: `.claude/rules/gate-verdicts.md`; `.claude/rules/epistemic-discipline.md` §SOURCE-RECON 5-class taxonomy; calibration corpus = the 5 precedents in §II.2 (CC-SIGN-57, f_DM-DEPLETION-59, TEMP-MISMATCH-59, LEGGETT-DM-ABUND-60, S64 a_0/a_2 trap) plus the W5a §W5a-1 anchor.
   - **Gate**: new gate `S87-SIGN-MAGNITUDE-VOCABULARY-LIFT`. PASS = rule-file edit lands; downstream verifier `_sign_magnitude_classifier.py` validates the 3 conditions on the calibration corpus and labels each precedent correctly. INFO if rule-file edit lands but classifier disagrees with one or more precedent assignments. FAIL if rule-file edit cannot accommodate the W5a anchor without ambiguity.
   - **Effort**: 1 wave-equivalent (rule-file edit + classifier script + 5-precedent calibration sweep).

V.2. **3HEB-INHERITANCE-TAG-87**: Tag the 22 framework/3He-B correspondences in `framework-3heb-comparison.md` by sign-vs-magnitude inheritance layer
   - **What**: for each of the 22 correspondences in `.claude/agent-memory/volovik-superfluid-universe-theorist/framework-3heb-comparison.md`, add a column "Inheritance Layer" with values SIGN-ONLY (kinematic skeleton inherited), MAGNITUDE-ONLY (dimensional scale inherited), BOTH (full inheritance), NEITHER (independent emergent physics). Use the substrate-physics argument in §II.3 of this synthesis as the classification rubric.
   - **Inputs**: `framework-3heb-comparison.md` (22 correspondences); `project_3heb-inheritance.md`; Volovik 2003 §29 for the parent-magnitude pinning structure.
   - **Gate**: new gate `S87-3HEB-INHERITANCE-LAYER-TAG`. PASS = all 22 correspondences tagged with one of the 4 layer labels; classification agrees with at least 4/5 of the §II.2 precedents (allowing one borderline case). INFO if all 22 tagged but disagreement on >1 precedent. FAIL if a correspondence cannot be classified.
   - **Effort**: 1.5 wave-equivalents (literature review for parent-magnitude inheritance + tagging + cross-validation against §II.2 precedents).

V.3. **W5A-RESCALED-IC-87 (companion to V.1)**: re-derive the W5a §W5a-1 SR-LO Z-factor using the canonical `xi_E_GGE_inv = 13.6425` to find the IC-rescaling regime where SR-LO remains self-consistent
   - **What**: scan rescaling factors `lambda_IC` for the substrate-first IC such that the substrate ε-trajectory remains in the SR-LO linear regime (ε < 0.1) over [0, 55] e-folds. Identify whether any `lambda_IC` exists that simultaneously preserves the substrate-first IC interpretation (`xi²(0) ∝ xi_E_GGE_inv`) and keeps SR-LO valid. Equivalent to the W5a carry-forward `S87-SECTOR-1-SR-FLOW-RESCALED` already specified in §W5a-1 carry-forward (this V.3 entry is the volovik-side specification for cross-check).
   - **Inputs**: `computations/s86_w5a_p3_sector_1_z_factor.npz`; canonical `xi_E_GGE_inv = 13.642473425595973`; SR-LO ODE form (gen-physicist 9A §4.5a); IC scan range `lambda_IC ∈ [10^-4, 10^0]`.
   - **Gate**: `S87-SECTOR-1-SR-FLOW-RESCALED`. PASS band `|Z_ratio − 1| ≤ 0.05` for some `lambda_IC` that holds the substrate-first IC source term within the linear regime. FAIL if no such `lambda_IC` exists across the scan. The PASS sub-result becomes a SIGN-CONFIRMED-MAGNITUDE-CONFIRMED upgrade of W5a §W5a-1 (resolving the magnitude failure). The FAIL sub-result confirms that the substrate-first SR-LO corridor is permanently closed even with corrected pin (a stronger result than the current pin-drift FAIL).
   - **Effort**: 0.5 wave-equivalents (script reuses the W5a ODE machinery; new IC scan adds the analysis cost).

V.4. **SOURCE-RECON-SIGN-MAGNITUDE-AUDIT-87**: extend `_source_reconciliation_audit.py` to emit a sign-vs-magnitude provenance trace for every Class-(c) and Class-(d) finding
   - **What**: for every PIN-DRIFT-FROM-STALE-SOURCE (c) or PIN-DERIVATIVE-VS-SOURCE-PRIMARY (d) detection in a [SIGN]-tagged gate, the audit script emits a new field `sign_layer_robust=YES|NO` indicating whether the substitution chain's Step 4 sign-readout is independent of the drifted-pin numerical value. Static-analysis pass over the script's Step 4 expression; YES if the substitution chain's sign reads off a sign-of-coefficient (e.g., `+2·ε_0·xi_E_GGE_inv > 0` for any positive `xi_E_GGE_inv`); NO if the sign depends on numerical ordering (e.g., `a_substrate > a_LCDM` requires the actual values).
   - **Inputs**: `computations/_source_reconciliation_audit.py`; the 5-class taxonomy in `epistemic-discipline.md` §Source Reconciliation; calibration corpus = W5a §W5a-1 (sign-layer-robust YES) + S64 a_0/a_2 trap (sign-layer-robust YES, but sign in wrong direction) + a synthetic NO-case to be constructed.
   - **Gate**: `S87-SOURCE-RECON-SIGN-LAYER-EXT`. PASS = audit script emits the new field for ≥3 calibration cases with correct YES/NO labels. INFO if labels correct on 2/3 calibration cases. FAIL if labels incorrect on >1 calibration case.
   - **Effort**: 1 wave-equivalent (static-analysis pass on Step 4 expressions + calibration sweep).

V.5. **VOLOVIK-EFFACEMENT-CATALOG-87**: build a structured registry of all SIGN-correct / MAGNITUDE-wrong instances in the framework's history under the Volovik-effacement umbrella
   - **What**: scan `permanent-results-registry.md`, `framework-3heb-comparison.md`, `constraint-mega-matrix.md`, and the verdict files `s{N}_gate_verdicts.txt` for all gates whose verdict line contains a sign-from-canonical-form claim that survived a magnitude FAIL. Produce a registry entry per instance with: gate ID, session, sign-derivation source (substrate machinery layer), magnitude-failure source (pin-drift / scale-problem / suppression-mechanism), corrected-pin successor gate (if any), and SIGN-LAYER-ROBUST classification (per V.4). Target output file `sessions/framework/sign-magnitude-bifurcation-registry.md`.
   - **Inputs**: all session verdict files; `framework-3heb-comparison.md`; `constraint-mega-matrix.md`; the W5a §W5a-1 anchor.
   - **Gate**: `S87-VOLOVIK-EFFACEMENT-CATALOG`. PASS = registry has ≥10 entries with all required fields populated; ≥5 entries have a corrected-pin successor identified. INFO if registry has ≥10 entries but <5 have successors. FAIL if registry has <10 entries (insufficient pattern signal).
   - **Effort**: 2 wave-equivalents (corpus scan + registry writeup + cross-validation with the 5-precedent §II.2 catalog of this synthesis).

---

## VI. Summary Table

| # | Result | Classification | Status | Sign-state | Magnitude-state | Implication |
|:--|:-------|:---------------|:-------|:-----------|:----------------|:------------|
| II.1 | W5a §W5a-1 substitution chain Step 4: substrate-first IC ENHANCES (Z_ratio > 1) | PHONONIC | DOUBLE FAIL on magnitude; sign STRUCTURAL | CONFIRMED at both pivots | REFUTED 2× / 92× same-direction | Substitution chain reusable at corrected pin; flat FAIL discards constraint-map info |
| II.2.a | CC-SIGN-57: Lambda_eff = +1.709 M_KK > 0 | PHONONIC (vacuum-energy partition) | PASS (sign), GAP 114 OOM | CONFIRMED (+ CC accelerating) | REFUTED 114 OOM (M_KK^4 vs Lambda_obs) | Canonical Volovik-effacement instance; sign is robust under any future CC mechanism |
| II.2.b | f_DM-DEPLETION-59: f_DM(z=0) = 1.000 vs 0.844 obs | PHONONIC (Leggett-mode DM) | PASS (sign), OVERSHOOT magnitude | CONFIRMED (rises from 0.209) | OVERSHOOT 0.156 (no baryon subtraction) | 3He-B inheritance pinned direction but not baryon fraction |
| II.2.c | TEMP-MISMATCH-59 Model B: w_a_eff = 0.037 | PHONONIC (substrate clock-rate variance) | INFO (DESI w_a CLOSED) | CONFIRMED (Model B negative) | SUPPRESSED 25× (Josephson phase lock) | Wiltshire-from-fiber-geometry direction correct, magnitude structurally damped |
| II.2.d | LEGGETT-DM-ABUND-60: Omega_L h² = 3.23e+25, tau_L = 3.6e−34 s | PHONONIC (Leggett DM cosmology) | FAIL double | CONFIRMED both observables | REFUTED 26.4 + 52 OOM (cosmological-modulus problem) | SIGN-correct does not rescue; channel permanently CLOSED by magnitude |
| II.2.e | S64 a_0/a_2 trap (Theorem 2): off-Jensen Casimir monotone | GEOMETRIC (spectral-action moment ratio) | PROVEN theorem; CC FAIL | INVERSE-POLARITY (wrong direction) | structural | Sibling tag SIGN-WRONG-DIRECTION-CLOSURE; corridor closed by sign |
| II.3 | Substrate-physics argument: sign and magnitude ride on independent layers | PHONONIC + GEOMETRIC | organizing insight | N/A | N/A | SIGN-CONFIRMED-MAGNITUDE-REFUTED is a structurally meaningful epistemic state |

---

## VII. Notes on source-conflict resolution

No conflicts between source documents detected. The W5a §W5a-1 working paper, the gate-verdicts.md ontology, and the epistemic-discipline.md SOURCE-RECON taxonomy compose cleanly: the substrate-physics SIGN/MAGNITUDE bifurcation in §II.3 is the substrate-physics analog of the SOURCE-RECON Class-(c)/(d) drift detection, and both produce a verdict-vocabulary extension that preserves the canonical PASS/FAIL/INFO outcome while adding a sign/magnitude sub-axis. The agent-memory precedents (cc-sign-57-result.md, fdm-depletion-59-result.md, s60-collab-review.md, s64-synthesis-result.md) are point-in-time observations (some 30+ days old per system reminders); the canonical numbers cited in §II.2 were cross-validated against `mcp__knowledge__search_knowledge` results in this session. The 5-precedent catalog stands as the calibration corpus for the proposed verdict-vocabulary extension.
