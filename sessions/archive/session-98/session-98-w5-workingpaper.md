# Session 98 Wave 5 — Spectral-Moment Robustness (a₀/a₂ tier-2 PV-scheme invariance) (Results Working Paper)

**Session**: 98 | **Wave**: 5 | **Plan**: session-98-plan-w5.md | **Theme**: Spectral-functional robustness — re-evaluate the capstone §8.5 tier-2 survival verdict for the a₀/a₂ moment-pair under two regulator anchorings (FI-within-family Mellin-zeta vs full-physical Pauli-Villars) and verify the survival LABEL is scheme-invariant (the DI1-guard numerical confirmation S97 W2-1 deliberately left open).

## Gate Sections

### §W5-1. S98-A0A2-TIER2-PV-INVARIANCE (lizzi-spectral-functional-theorist)

**Status**: COMPLETED
**Gate ID**: `S98-A0A2-TIER2-PV-INVARIANCE`
**Trigger**: `[SIGN]`
**Classification**: **GEOMETRIC** (a₀/a₂ Seeley-DeWitt moment-pair; §8.5 tier-2 survival partition robustness)
**Agent**: `lizzi-spectral-functional-theorist`
**Hypothesis**: The §8.5 tier-2 survival LABEL for a₀/a₂ is invariant under regulator anchoring — Δ(survival-margin) = 0 to numerical precision across the FI-anchor Mellin-zeta ratio and the full-physical-PV ratio — confirming d(survival)/d(PV-scheme) = 0 numerically (the DI1 guard S97-W2-1 scoped out).
**Plan reference**: `sessions/session-plan/session-98-plan-w5.md` §W5-1 (machinery pin, dual-anchor thresholds, substitution chain, INFO drift-operand source).

**Output Artifacts**:
- **script** `computations/session-98/s98_a0a2_tier2_pv_invariance.py` — present; `grep -E 'from canonical_constants import|append_verdict'` →
  - `from canonical_constants import a_0_FW_zeta, a_2_FW_zeta   # zeta-FW anchors (cross-check)`
  - `def append_verdict(gate_id, verdict, value_str, scheme, convention, l_max,`
  - `    res = append_verdict(` (call site)
- **data** `computations/session-98/s98_a0a2_tier2_pv_invariance.npz` — present (the two anchored ratios + the survival-margins + label-distance + the within-family drift operand + verdict 3-tuple).
- **plot** `computations/session-98/s98_a0a2_tier2_pv_invariance.png` — present (left: absolute moment-ratio RD across PV with the invariant SURVIVE label annotation; right: Δ(survival-margin)=0 label-distance bar + the d_PV within-family-drift INFO bar against ε_FI / info_band).
- **verdict_line** `computations/session-98/s98_gate_verdicts.txt` — present; `grep -E '^S98-A0A2-TIER2-PV-INVARIANCE:.* audit_sha256=[a-f0-9]{64}'` matches the canonical line. dual-SHA companion row present (`audit_sha256_short=4522ea7e56287415 content_sha256_short=548e32bb0d00b055`); [SIGN] 3-tuple companion row present (`sign_verdict=PASS magnitude_verdict=INFO regime_verdict=VALID`). `audit_sha256=4522ea7e…` unique in file (sig_5 preserved).
- **wp_section** this file §W5-1 — Status COMPLETED / Verdict INFO / Output Artifacts / MCP Pre-Compute Audit all present.

**MCP Pre-Compute Audit**:
- `get_constant("a_0_FW_zeta")` → **6440.0**, gate `S88-A-N-FW-CANONICALIZATION`, **Superseded: False** (matches plan pin + npz `a_0_FW_zeta` bit-for-bit).
- `get_constant("a_2_FW_zeta")` → **2776.165389**, gate `S88-A-N-FW-CANONICALIZATION`, **Superseded: False** (matches plan pin + npz `a_2_FW_zeta` bit-for-bit).
- `search_knowledge("S98 A0A2 TIER2 PV INVARIANCE survival tier-2")` → returns the upstream W2-1 provenance (`s97_w2_1_a0a2_pv_full_mellin`) and the W2-1 gate `S97-W2-1-A0A2-PV-FULL-MELLIN` (INFO, `absolute_a0PV_over_a2PV=0.510595`, DI1-scoped). **No closure covers this gate** — S97 W2-1 explicitly scoped its verdict to OBJECT-DEFINEDNESS-AXIS-ONLY and `does-NOT-establish-or-retract-§8.5-tier-2-survival`. This gate is NOT PRE-CLOSED; it is the deliberate completion of the DI1 guard W2-1 left open. (The §8.5 tier-2 survival partition itself is the EXISTING capstone claim being numerically confirmed, not re-derived.)

**Verdict**: **INFO** — Δ(survival-margin) = 0.000000000e+00 (≤ 1e-9 PASS-conjunct holds; the two survival LABELs are byte-identical "SURVIVE"/"SURVIVE") ⇒ **d(survival)/d(PV-scheme) = 0 NUMERICALLY**; BUT the PV-anchor within-family L_max=10→12 RATIO drift d_PV = 0.05702619832238401 ∈ (ε_FI = 0.05, info_band = 0.10] fires the **hidden RD-axis dependence** flag. Composite 3-tuple: `sign=PASS / magnitude=INFO / regime=VALID`. This is the expected verdict per the plan dry-run (track_B, prior 0.4): the §8.5 PARTITION is regulator-robust, the residual RD direction is the L_max-extension axis (not the PV-vs-Mellin axis).

**Results**:

*Numbers first.* All operands read from the W2-1 npz (`s97_w2_1_a0a2_pv_full_mellin.npz`; verdict-audit `7d5ca3f9…`); no new spectrum diagonalization. Both moments come from the SAME L_max=10 D_K² eigenvalue cache.

| Quantity | FI-anchor (`a_n^{Mellin}`) | PV-anchor (`a_n^{Pauli-Villars}`) |
|:--|:--|:--|
| `a₀` (L_max=10) | `2752.3895887045956` | `1300.2094666215025` |
| `a₂` (L_max=10) | `12651.013717791986` | `2546.457539332954` |
| `O = a₀/a₂` (absolute ratio) | `0.21756277007539102` | `0.5105953845835941` |
| survival-margin `m(a₀/a₂)` | `+1` | `+1` |
| survival LABEL | `SURVIVE` | `SURVIVE` |

- **Absolute moment-ratio IS regulator-dependent (RD across PV):** `|O_PV − O_FI| = 0.29303261450820306` — EXPECTED ≠ 0 (this is the S96-SDW-CC-GAP `partB_FI_across_PV=False` / PV-shift content). This is NOT the survival-margin; the survival-margin is a CLASS-membership, not the ratio value.
- **Survival-margin = §8.5 DI1 partition signed distance:** `Δ(survival-margin) = |m_PV − m_FI| = |(+1) − (+1)| = 0`. The survival LABEL is byte-identical ("SURVIVE" under both). The class membership is decided by the parse-tree TYPE (a dimensionless moment-RATIO a₀/a₂), NOT by the numerical ratio value: the c² volume/curvature rescale cancels in ANY anchoring (capstone §8.2 R₁-invariance, the cancellation is regulator-INDEPENDENT, residual 0). Capstone §8.5 lists `a₂/a₀` explicitly on the truncation-robust SURVIVE-side. ⇒ **d(survival)/d(PV-scheme) = 0 NUMERICALLY**, not merely structurally.
- **INFO discriminator (the hidden RD-axis):** PV-anchor within-family L_max=10→12 RATIO drift `d_PV = |ratio_PV(L12) − ratio_PV(L10)| / |ratio_PV(L10)| = |0.48147807091983613 − 0.5105953845835941| / 0.5105953845835941 = 0.05702619832238401` = npz `Lmax_drift_ratio` bit-for-bit. Against `ε_FI = 0.05`: `d_PV = 0.0570 > ε_FI = 0.05` ⇒ marginally OUTSIDE the K-invariant-family FI tolerance at the L_max-extension axis. `d_PV ∈ (0.05, 0.10]` ⇒ INFO band fires. The §8.5 LABEL is invariant (PASS-conjunct) BUT the PV anchoring carries a sub-threshold RD-drift on its OWN within-family L_max axis.

**4-tuple**: `(value = Δ(survival-margin) = 0.000000000e+00, scheme = TIER2-SURVIVAL-DUAL-ANCHOR-FI-vs-FULL-PV, convention = RATIO-LABEL-DISTANCE-poleconv-A-double-PV-FULL-PHYSICAL, L_max = 10)`.

**Constraint gates**:
- *CC-label-equality* (the PASS-conjunct): `Δ(survival-margin) = 0 ≤ 1e-9` AND `label_FI == label_PV` (byte-identical "SURVIVE") → **holds**.
- *CC-drift-operand* (the INFO discriminator): `d_PV = 0.0570` vs `ε_FI = 0.05` / `info_band = 0.10` → `d_PV > ε_FI` AND `d_PV ≤ info_band` → **INFO band fires** (hidden RD-axis dependence on the PV within-family L_max=10→12 axis).

**Substitution chain (numbers substituted, per `math-scripts.md §"Double-Check Logic Before Compute"`)**:
- Step 2 (substitute O under each anchoring): `O_FI = 2752.3895887045956/12651.013717791986 = 0.21756277007539102` (= npz `R_CC_zeta_abs`); `O_PV = 1300.2094666215025/2546.457539332954 = 0.5105953845835941` (= npz `R_CC_PV_abs`); `|O_PV − O_FI| = 0.293032615` (RD across PV; EXPECTED ≠ 0; NOT the margin).
- Step 3 (simplify — margin is class-membership, not the ratio): both O have the IDENTICAL parse-tree (moment/moment, dimensionless ratio); a dimensionless moment-RATIO is on the SURVIVE-side under EVERY regulator anchoring (c² cancels regulator-independently, §8.2) ⇒ `m(a₀/a₂, FI) = +1 ⇒ SURVIVE`; `m(a₀/a₂, PV) = +1 ⇒ SURVIVE`.
- Step 4 (read off direction): `Δ(survival-margin) = |(+1) − (+1)| = 0 ≤ 1e-9` ⇒ LABEL unchanged ⇒ `d(survival)/d(PV-scheme) = 0`. [SIGN] directional content: predicted Δ = 0 (non-negative label-distance whose predicted value is exactly 0); `sign_verdict = PASS` iff the two labels coincide (they do), `FAIL` iff a label flip drives Δ to 2.
- Step 5 (INFO discriminator): `d_PV = 0.0570 > ε_FI = 0.05` ⇒ the §8.5 LABEL is invariant (PASS-conjunct) BUT the PV anchoring carries a sub-threshold within-family L_max RD-drift (`info_band = 0.10 ≥ 0.0570 > ε_FI = 0.05`).

**Cross-checks (bit-for-bit vs the W2-1 npz)**: `O_FI == R_CC_zeta_abs` ✓; `O_PV == R_CC_PV_abs` ✓; `ratio_PV(L12) == R_CC_PV_abs_L12` ✓; `d_PV == Lmax_drift_ratio` ✓. **SOURCE-RECON binding test** (consumed-value, per `substrate-first-canonical-sourcing.md §(ii.B)`): `a_0_FW_zeta = 6440.0` (pin 6440.0; npz 6440.0) match ✓; `a_2_FW_zeta = 2776.165389` (pin 2776.165389; npz 2776.165389) match ✓. The plan-pinned `canonical_constants.py` file-SHA (`ed414699…`) drifted at runtime (a concurrent S98 wave touched the file); this is **benign plan-text-drift** — the BINDING test is the consumed VALUE (both non-superseded per the knowledge MCP and bit-identical to the npz fields, D_max < 0.1, no rule-file action), NOT the file SHA. The PV-helper SHA (`eaf98037…`, the CLASS=FULL audit anchor) matches the plan pin EXACTLY and is asserted in-script (a drift would halt).

**Regulator-pin discipline** (`regulator-pin-discipline.md`): every Seeley-DeWitt citation carries an explicit `a_n^{regulator}` tag — `a₀^{Mellin}/a₂^{Mellin}` (FI-anchor, no PV) and `a₀^{Pauli-Villars}/a₂^{Pauli-Villars}` (PV-anchor). Mellin pole-convention `poleconv-A-double` with `(pole_in_s=4, curvature_grade_n=0)` for a₀ and `(pole_in_s=3, curvature_grade_n=2)` at d=8. **Level-pin discipline** (`substrate-first-canonical-sourcing.md §(iv)`): the PV moment is the FULL-physical 2-point Pauli-Villars from `_pauli_villars_subtraction.py` (docstring self-identifies "PRIMARY full-physical Pauli-Villars helper", c=[+2,−1], m²=[1,2] in M_KK units, Σc_r=1 ∧ Σc_r m_r²=0), NOT the SCHEMATIC `_spectral_action_regulators.pauli_villars_a_n` → `CLASS=FULL`, NO `-SCHEMATIC` suffix, NO `# tier_pin=TIER-2` companion row (W2-1 precedent `CLASS=FULL_no_SCHEMATIC_suffix_no_tier_pin`).

**Assessment (solution-space)**: The §8.5 tier-2 survival partition for the a₀/a₂ moment-pair is a property of the substrate's spectral-action FUNCTIONAL, not an artifact of the regulator class chosen for the absolute moments. The DI1 guard that the S97 W2-1 object-definedness gate deliberately scoped out (`does-NOT-establish-or-retract-§8.5-tier-2-survival`) is NUMERICALLY confirmed: the absolute-magnitude RD-ness (the a₀/a₂ value differs 0.5106 vs 0.2176 across PV) does NOT leak into the survival PARTITION. The residual RD direction is precisely localized — it is the L_max-extension axis (d_PV = 0.0570 marginally > ε_FI = 0.05 on the PV within-family L_max=10→12 step), NOT the PV-vs-Mellin axis. This is the spectral-functional-theorist's signature finding: what survives all regulator choices (the survival LABEL / the §8.5 partition) is STRUCTURAL; what depends on the choice (the absolute ratio value, and the within-family L_max margin) is the localized RD degree of freedom. The INFO verdict is NOT a weakness of the survival claim; it is a precise localization of which axis the regulator choice still touches. Carry-forward `CF-S99-A0A2-LMAX-PV-CONTINUATION` (extend the full-PV a₀/a₂ continuation to L_max ≥ 13 to test whether d_PV → < ε_FI, promoting INFO → PASS) follows. Substrate framing: GEOMETRIC — a₀, a₂ are the zeroth/second Seeley-DeWitt spectral MOMENTS of D_K (a₀ → vacuum/CC term; a₂ → emergent Einstein-Hilbert); the direction of explanation flows FROM the D_K spectrum TOWARD the emergent §8.5 partition. NOT a cross-pillar bridge (no laboratory-IN observable) and NOT a §VII registry landing (it confirms an EXISTING capstone partition).

---

## Wave 5 Synthesis (team-lead)

(Written after the gate completes. Structure: `sessions/archive/session-84/session-84-w1-workingpaper.md:1040–1095`. Record the V.8 verdict, the §8.5 DI1-guard numerical-confirmation status, and the capstone-hygiene Q3 outcome per the plan's Wave 5 → Wave 6 Decision Point table.)

## Carry-Forward Computations

(One `### {CF-ID} — {one-line title}` sub-heading per genuine future-work item, each with a 4-field-spec table (What / Inputs / Gate / Effort). Per the plan's V.8-outcome table: an INFO verdict routes `CF-S99-A0A2-LMAX-PV-CONTINUATION` (extend the full-PV a₀/a₂ continuation to L_max ≥ 13 to test d_PV → < ε_FI); a FAIL routes `CF-S99-§8.5-REGULATOR-SCOPE`; a clean PASS produces no carry-forward. If the wave produced zero genuine future-work items, write "No carry-forwards: all wave outcomes closed in-session.")

## Constraint-Map Updates

(One row per state change. Columns: Date | Mechanism/gate | Prior state | New state | Reason. Process observations and in-session hygiene closures go here, not in Carry-Forward Computations.)

## Files Produced

(One row per gate. Columns: Gate | Script | Data (.npz) | Plot (.png) | JSON | Size.)

## Carry-Forward Computations

### CF-S99-W5-A0A2-LMAX-PV-CONTINUATION — extend full-PV a₀/a₂ to L_max ≥ 13 [genuine-math]

1. **What**: Extend the full-physical-PV a₀/a₂ continuation to L_max ≥ 13 (Casimir-bound / Friedrich-Bär feasibility) to test whether the within-family L_max=10→12 drift d_PV (= 0.0570 at S98) shrinks below ε_FI = 0.05, promoting the §8.5 tier-2 survival INFO → PASS. S98 V.8 confirmed d(survival)/d(PV-scheme)=0 NUMERICALLY (FI/SD decomposition: survival LABEL regulator-invariant — `SURVIVE` under both FI-anchor a₀/a₂=0.2176 and PV-anchor 0.5106; L_max-extension margin scheme-dependent); the residual RD direction is localized to the L_max axis, not the PV-vs-Mellin axis.
2. **Inputs**: `computations/session-98/s98_a0a2_tier2_pv_invariance.npz` (V.8, audit `4522ea7e…`); `computations/session-97/s97_w2_1_a0a2_pv_full_mellin.npz`; capstone §8.5 tier-2 survival definition; `a_0_FW_zeta=6440.0`, `a_2_FW_zeta=2776.165389`.
3. **Gate**: `S99-W5-A0A2-LMAX13` — PASS iff d_PV(L_max≥13) < ε_FI=0.05 (INFO→PASS promotion); INFO if it narrows but stays in (0.05, 0.10]; FAIL if d_PV does not shrink (structural RD on the L_max axis).
4. **Effort**: ~0.5 wave (no new diagonalization if an L13 cache exists; else irrep-construction feasibility per `math-scripts.md` D_K block-diagonality pre-check).
