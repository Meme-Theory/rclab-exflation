# Session 88 Plan — Wave 12: cosmological corpus + W9 corpus follow-ups + Stage-2

> **Planner**: planner-w12 (mack-cosmic-bridge co-authoring observational + cosmological gates; gen-physicist orchestrator; connes-ncg + volovik for Stage-2 cross-axis verifies)
> **Theme**: W3 cosmological observable corpus + W9 corpus follow-ups + Stage-2 verifies
> **Verdict file**: `computations/s88_gate_verdicts.txt`
> **Script prefix**: `s88_w12_<slug>.py`

---

## Wave 12 Summary

Wave 12 closes the W3 cosmological observable corpus carry-forwards (substrate-first canonical sourcing of δ_speed via Mellin-cone analytic continuation; reconciliation of pre-registered LiteBIRD-LISA discrimination thresholds against the meta-classifier band-half-width; Stage-2 two-agent independent verification of the Joint LiteBIRD-LISA-Fisher cross-axis theorem) AND the W9 follow-ups for cross-region partition application (Q-7), per-class N-breakdown forward modeling (Q-8), pole-scope generic-pluralism Stage-2 verify, pole-specificity cross-regulator metric disambiguation, T1-21 resolution-specificity registry-text extension, and higher-N pole extension. Three downstream gates (#138, #139, #140) are BLOCKED at plan-freeze pending upstream prerequisite landings (Connes-distance subalgebra restriction conjecture, §VII.AJ.W4-1 cross-pillar 3-channel theorem PASS-conditional landing, W4-3 f_NL^folded language correction); they are pre-registered here under PRE-REG-INC for mechanical-closure on prereq-block and routed to S89 if prereqs do not land.

**Cluster M (items 135-140)**: cosmological observable corpus close-out (substrate-first canonical sourcing + Stage-2 joint Fisher verify + 3 BLOCKED gates pre-registered for mechanical-closure).

**Cluster N (items 141-148)**: W9 corpus follow-ups (Stage-2 joint F_2-Class Path-(c) verify; cross-region partition application; per-class N-breakdown respec; pole-scope/pole-specificity follow-ups; T1-21 registry-text extension; higher-N pole extension).

---

## Wave 12 Decision Point Prerequisites

| Gate | Prerequisite (upstream) | Status at plan-freeze | Decision-point routing |
|:-----|:------------------------|:----------------------|:-----------------------|
| #135 | substrate-distance-1 pole s=4 Mellin-cone evaluator (S87 W2 §VII.U/V family) | LANDED (S87 W2 §VII.U.1 PASS) | dispatch normally |
| #136 | _meta_classifier_v2.py band pins | LANDED (canonical_constants.py) | dispatch normally |
| #137 | Joint LiteBIRD-LISA-Fisher §W3-3d Stage-1 npz | LANDED (S87 W3-3d) | dispatch normally |
| #138 | #123 Connes-distance subalgebra restriction conjecture | NOT LANDED at plan-freeze | PRE-REG-INC (mechanical closure to S89) |
| #139 | §VII.AJ.W4-1 cross-pillar 3-channel theorem PASS-conditional | NOT LANDED at plan-freeze | PRE-REG-INC (mechanical closure to S89) |
| #140 | W4-3 f_NL^folded language correction | NOT LANDED at plan-freeze | PRE-REG-INC (mechanical closure to S89) |
| #141 | §VII.AH STAGE-1-CANDIDATE landing (S87 W9a-1) | LANDED | volovik BLOCKED as co-author per joint-theorem-promotion.md §"Two-Agent Independent-Verify" — alternative cross-reviewer assignment in spec |
| #142 | CF-66 / CF-67 / CF-68 / CF-10 cross-region partition prereqs | partial — see per-gate spec | dispatch under conditional pre-reg |
| #143 | CF-42 per-class N-breakdown prereq | LANDED | dispatch normally; W9b-1 cross-link |
| #144 | canonical N_breakdown downstream consumer audit | n/a — runs from rule-file inventory | dispatch normally |
| #145 | §VII.AH pole-scope structural correlation | LANDED | dispatch (Stage-2 connes + volovik joint) |
| #146 | W9b-2 lines 271 + 274 sub-cut data | LANDED | dispatch normally |
| #147 | T1-21 resolution-specificity scoping rule | LANDED (epistemic-discipline.md) | dispatch normally (METHODOLOGY-class) |
| #148 | W9b-2 ρ_S(s=4) = -1.000 EXACT data | LANDED | dispatch normally |

**Mechanical-closure protocol** (per `.claude/rules/mechanical-closure-discipline.md`): gates #138, #139, #140 emit verdict-line `value='PRE-REG-INC_blocked_by_<symbol>_<status>_*'` with FAIL verdict and per-gate-distinct audit_sha256 if their prerequisite landings have not occurred by Wave 12 dispatch time. The mechanical closure preserves audit-trail honesty and routes to S89 carry-forward without stub-PASS pollution.

---

## §W12-135 — `S88-DELTA-SPEED-MELLIN-CANONICAL-SOURCING`

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge (cosmological observable provenance) + gen-physicist (orchestrator; Mellin-cone substrate computation)
**Hypothesis**: The cosmological signal-velocity discriminator δ_speed sources structurally from Mellin-cone analytic continuation at substrate-distance-1 pole s=4 of the spectral-action coefficient a_4^{Mellin}. Pre-W12 plan citations of δ_speed_PathH = 0.00745 and δ_speed_PathC = 0.011731522 carried external-paper provenance (W-3 closure values); this gate provides the substrate-first canonical computation per `.claude/rules/substrate-first-canonical-sourcing.md`.

**Substitution chain** (mandatory for sign claim per `.claude/rules/math-scripts.md` §"Double-Check Logic Before Compute"):
```
Step 1: a_4^{Mellin}(τ; pole=s=4) = Res[Tr(D_K^{-2s}); s = (d - 4)/2 = 0]
        = Σ_k m_k λ_k^{-(d - 4)} = Σ_k m_k λ_k^0 with d=4 ⇒ formal divergence
        regularized via Mellin-Barnes contour shift to s = 0 + ε with ε → 0+.
Step 2: Path-H residue at the regulated s=4 pole (HypB convention pinned per
        regulator-convention-lockdown.md; offset_Mellin = w_0_FW - rho_Mellin(L=10)
        with L_anchor = 10 by canonical-anchored-convention).
Step 3: δ_speed_Path = 1 - c_phon_Path / c_obs where c_phon_Path is the Mellin-residue-
        derived phonon group velocity at Path's regulator class.
Step 4: For Path-H (HypB-anchored): the residue contribution is positive-definite
        ⇒ c_phon_PathH < c_obs by the impedance-mismatch lemma ⇒ δ_speed_PathH > 0.
Step 5: For Path-C (HypA companion-null at LISA frequency): the residue carries the
        opposite sign by inheritance through the (Δ_B/Δ_A)^p cancellation theorem
        with p odd at this pole ⇒ δ_speed_PathC < 0.
Conclusion: sign(δ_speed_PathH) = +1 AND sign(δ_speed_PathC) = -1.
            (Anti-correlation per volovik R3-A in W-3 workshop closure.)
```

**Method**: Substrate-first computation:
1. Load D_K eigenmoment cache (S84 master spectrum cache `s84_spectrum_cache_L12_tau019.npz`) at L_max=10.
2. Compute the Mellin-Barnes residue at s=4 pole via `analytic_zeta` with regulator-pin tag `a_4^{Mellin}` per `.claude/rules/regulator-pin-discipline.md`.
3. Evaluate Path-H and Path-C residue contributions separately under HypB and HypA conventions respectively (per the Mellin-cone two-pathway split workshopped in S86 W-3 §R3-A).
4. Form δ_speed_PathH and δ_speed_PathC; cross-check against external-paper-provenance values 0.00745 / 0.011731522 to within publication precision (10 sig figs).
5. Compute sigma_delta_speed_mellin_noise via Sage-exact rational propagation through the Mellin contour.
6. Promote canonicals `delta_speed_PathH_FW`, `delta_speed_PathC_FW`, `sigma_delta_speed_mellin_noise_FW` to canonical_constants.py.

**Machinery pin**:
- `pole = s=4` (substrate-distance-1)
- `regulator = Mellin` (per regulator-pin-discipline.md)
- `convention = HypB` for Path-H, `HypA` for Path-C (per regulator-convention-lockdown.md CAC)
- `L_max = 10` (canonical anchor; Friedrich-Bär saturation per math-scripts.md §"D_K Block-Diagonality")
- `tau_fold = 0.190`
- `offset_Mellin = w_0_FW - rho_Mellin(L=10)` (CAC effacement-anchored offset)
- `publication_sig_figs = 10` (per Class-8.3 K=4 MANDATORY)
- `verifier_rel_tol = 1e-9` (≥ 10^(-publication_sig_figs); guards against precision-floor false-FAIL)

**4-tuple**: (s=4 Mellin pole, HypB+HypA dual-convention, L_max=10, tau_fold=0.190)

**Thresholds**:
- PASS-sign: `sign(δ_speed_PathH) == +1 AND sign(δ_speed_PathC) == -1` (anti-correlation invariant)
- PASS-magnitude: `|δ_speed_PathH - 0.00745| / 0.00745 <= 1e-9` AND `|δ_speed_PathC - 0.011731522| / 0.011731522 <= 1e-9` (canonical reproduction)
- FAIL-sign: anti-correlation broken (signs equal or signs swapped) ⇒ structural FAIL of δ_speed observable; cosmological signal-velocity discriminator inverts predicted direction
- FAIL-magnitude: substrate-first computation diverges from external-paper provenance > 1e-9 ⇒ FAIL routes to source-reconciliation Class-(c) or Class-(f) review
- INFO: composite (sign=PASS, magnitude=FAIL within 1e-6) ⇒ canonical reproduces sign but precision-floor mismatch

**What PASS means**: substrate-first computation reproduces the W-3 closure values bit-precision; canonical_constants.py promotion replaces external-paper provenance with substrate citation; the cosmological signal-velocity observable is now structurally pinned at the Mellin-cone substrate-distance-1 pole.

**What FAIL means** (sign): anti-correlation prediction structurally falsified at substrate level — the sign-direction prediction of δ_speed (Path-H positive, Path-C negative) is inconsistent with the Mellin residue computation; downstream cosmological discrimination strength weakens; closes a corridor of the constraint map.

**What FAIL means** (magnitude): the external-paper W-3 closure values 0.00745 / 0.011731522 do not reproduce from substrate-first computation at canonical L_max=10; routes to Class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation (re-source from current canonical) or Class-(f) PIN-PLACEHOLDER-PENDING-SUBSTRATE-CANONICAL (substrate canonical promotes; external paper retired as methodological cross-check only).

**Effort**: 1 wave-equivalent (Mellin-Barnes residue evaluation + Sage-QQ exact propagation + canonical_constants.py promotion).

**Substrate framing**: The substrate IS the spectral triple `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`. The Mellin residue is a substrate-IS observable computed on this triple. The cosmological signal velocity δ_speed is the laboratory-IN observable measured in the FRW container as a deviation from c_obs. The bridge map is the residue → propagation-velocity factorization. Path-H and Path-C are substrate regulator-class labels; cosmological detectability emerges through the (Δ_B/Δ_A)^p inheritance cancellation. Direction: substrate-distance-1 Mellin residue IS → bridge map → laboratory δ_speed IN. Container-thinking of "δ_speed propagating in spacetime" is FORBIDDEN; the substrate dispersion IS the velocity hierarchy.

---

## §W12-136 — `S88-NULL-ELIMINATION-BAND-WIDTH-RECONCILIATION`

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge (LiteBIRD-LISA discrimination band ownership) + gen-physicist (orchestrator)
**Hypothesis**: The §W3-3e pre-registered 5σ null-elimination threshold is structurally consistent with `_meta_classifier_v2.py` band-half-width pins `_BLOCK_AXIS_BAND_HALF_WIDTH_SIGMA = 0.5` and `_REGULATOR_AXIS_OOM_BAND = 0.5` ONLY if the 5σ threshold is interpreted as a JOINT discriminator after band-pinning, not as a per-band threshold. The reconciliation either confirms structural consistency (5σ joint = PASS) or exposes a band-axis-vs-regulator-axis double-counting (5σ pre-reg vs 0.5σ band-half-width 10× mismatch).

**Method**:
1. Load §W3-3e pre-registered threshold text and `_meta_classifier_v2.py` band-pin specification.
2. Check whether the 5σ pre-reg is single-band threshold or joint discriminator after band-pinning.
3. If joint discriminator: confirm the joint-Fisher computation `LISA_Fisher = 47.086σ joint` (S87 W3-3d npz) saturates the 5σ joint threshold at 9.4× margin.
4. If per-band threshold: identify the band-axis specification mismatch and route to plan-authorship-defect remediation per `.claude/rules/epistemic-discipline.md` §"PRU".
5. Output: structural reading of the 5σ threshold; PASS if joint-discriminator interpretation reconciles; FAIL with diagnostic if per-band interpretation surfaces double-counting.

**Machinery pin**:
- `pre_reg_threshold_sigma = 5.0`
- `band_axis_half_width_sigma = 0.5`
- `regulator_axis_oom_band = 0.5`
- `LISA_Fisher_joint_sigma = 47.086` (S87 W3-3d closure value)
- `LiteBIRD_n_T_3yr_sigma_floor = 0.0540` (mack canonical)
- `interpretation = JOINT-DISCRIMINATOR` (pre-registered reading)

**4-tuple**: (5σ pre-reg, 0.5σ band, 0.5 OOM regulator-axis, joint Fisher 47.086σ)

**Thresholds**:
- PASS: joint-discriminator interpretation reconciles; 5σ joint threshold saturated at LISA_Fisher_joint_sigma / 5σ ≥ 1.0
- FAIL: per-band interpretation surfaces 10× double-counting between 5σ pre-reg and 0.5σ band-half-width
- INFO: ambiguity in §W3-3e text admits both readings; route to text-clarification carry-forward

**What PASS means**: §W3-3e threshold structurally consistent with `_meta_classifier_v2.py`; LISA-Fisher joint discriminator passes 5σ at >9× margin; cosmological null-elimination protocol intact.

**What FAIL means**: pre-registration text drift; the 5σ threshold and 0.5σ band-half-width describe different axes that were confused at plan-authorship; routes to Class-(b) PIN-LOOSE-SOURCE-TIGHT remediation.

**Effort**: 0.3 wave-equivalents (text-and-pin reconciliation; no new computation).

**Substrate framing**: This gate operates at the methodology-pin layer (band-axis vs regulator-axis is a discrimination-protocol structural choice). The substrate is unchanged; the audit checks the cosmological discriminator's threshold pre-registration for consistency. No container-thinking present in the threshold reading itself.

---

## §W12-137 — `S88-JOINT-LITEBIRD-LISA-FISHER-INDEPENDENT-VERIFY`

**Trigger**: [VERIFY-THEOREM] (Stage-2 cross-axis joint-theorem promotion gate)
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge (spectral-side cross-reviewer) + connes-ncg-theorist (axis-orthogonality side cross-reviewer); gen-physicist orchestrator dispatches BOTH IN PARALLEL WITHOUT prior workshop context per `joint-theorem-promotion.md` §"Two-Agent Independent-Verify"
**Hypothesis**: The Joint LiteBIRD-LISA-Fisher cross-axis theorem (S87 W3-3d STAGE-1-CANDIDATE) advances from STAGE-1-CANDIDATE to STAGE-3-PERMANENT via two-agent parallel cross-axis independent verify with PASS-AND on JOINT clauses.

**Method** (per `.claude/rules/joint-theorem-promotion.md` §Stage-2):
1. Identify single-axis vs JOINT clauses in the §W3-3d candidate text:
   - Single-axis clauses (a)-(b) spectral-side: LiteBIRD n_T 3-yr σ-floor 0.0540; spectral-moment derivation of n_T(transit) at f_transit=8.55e37 Hz.
   - Single-axis clauses (c)-(d) axis-orthogonality side: LISA Fisher 47.086σ joint; algebra-axis orthogonality between regulator-class observables (Path-H/Path-C).
   - JOINT clauses (e)-(f): joint-discriminator construction reconciling the 54.04-decade k-scale separation; cross-axis Fisher matrix block-diagonality under regulator-pin-tagging.
2. Dispatch mack-cosmic-bridge as Axis-A cross-reviewer (spectral-side; reads only the Stage-1 npz `s87_w3_3d_joint_litebird_lisa_fisher.npz` + canonical_constants.py + falsifier-master-inventory.md row; NO workshop transcripts). Audits clauses (a) + (b) + JOINT (e) + JOINT (f).
3. Dispatch connes-ncg-theorist as Axis-B cross-reviewer (axis-orthogonality side; same source restriction). Audits clauses (c) + (d) + JOINT (e) + JOINT (f).
4. PASS-AND on JOINT clauses: (e) PASS in mack AND PASS in connes; (f) PASS in mack AND PASS in connes.
5. If all single-axis clauses PASS in their respective cross-reviewers AND both JOINT clauses PASS in BOTH ⇒ Stage-2 PASS ⇒ promote §VII.<slot> from STAGE-1-CANDIDATE to STAGE-3-PERMANENT.
6. If any clause FAILs in either reviewer ⇒ promotion blocked; theorem stays at Stage 1; FAIL clause routes to S89 remediation.

**Machinery pin**:
- `cross_reviewer_A = mack-cosmic-bridge` (spectral-side)
- `cross_reviewer_B = connes-ncg-theorist` (axis-orthogonality side)
- `dispatch_mode = PARALLEL` (NOT sequential)
- `prior_workshop_context = WITHHELD` (cross-reviewers receive Stage-1 npz + canonical_constants.py + registry row only; NO §W3-3 R1/R2/R3 transcripts)
- `JOINT_clauses = ["(e) joint-discriminator construction", "(f) cross-axis Fisher block-diagonality"]`
- `JOINT_logical_op = AND` (PASS-AND'd across both verdicts)
- `audit_script = computations/_joint_theorem_independent_verify_audit.py`

**4-tuple**: (Stage-2 verify, parallel dispatch, no-workshop-context, PASS-AND on JOINT)

**Thresholds**:
- PASS (promotion): all single-axis clauses PASS in respective reviewer + both JOINT clauses PASS in BOTH reviewers ⇒ Stage-3 promotion at S88 R3 finalization
- FAIL: any clause FAIL in either reviewer ⇒ promotion blocked; theorem stays Stage-1; FAILing clauses route to S89 carry-forward `S89-JOINT-LITEBIRD-LISA-FISHER-FAIL-CLAUSE-REMEDIATION`
- INFO: any clause INFO in either reviewer ⇒ promotion stays Stage-1; INFO clause documented as Stage-2-INFO-deferred

**What PASS means**: structurally-independent agreement on JOINT clauses (cross-reviewers operated WITHOUT workshop context, so the agreement is NOT shared-context-derived per `epistemic-discipline.md` §"What Does NOT Count as Evidence" item 2); theorem promotes to permanent registry; cross-axis joint-Fisher discrimination protocol becomes citable as a structural theorem in S89+ falsifier-design.

**What FAIL means**: a clause does not survive cross-axis independent audit; the candidate's joint-discriminator construction OR Fisher block-diagonality has a structural gap; promotion blocked closes a structural-theorem corridor and isolates the gap as next-session focus.

**Effort**: 1.0 wave-equivalent (two parallel cross-reviewer dispatches + audit-script verification of dispatch parameters per audit at plan-freeze).

**Substrate framing**: The theorem connects substrate-IS observables (spectral-action moment derivation of n_T at transit scale) to laboratory-IN observables (LiteBIRD 3-yr B-mode sensitivity AND LISA Fisher matrix). The bridge map is the joint-discriminator construction across 54 decades. Cross-axis verification ensures the bridge map is not container-thinking-contaminated: each cross-reviewer audits from their axis with no prior narrative from the other axis, structurally enforcing IS-not-IN at the verification layer.

---

## §W12-138 — `S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION`

**Trigger**: [VERIFY] (PRE-REG-INC at plan-freeze; mechanical closure if prereq #123 not landed)
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge (cosmological-bridge audit) + gen-physicist (orchestrator)
**Status**: BLOCKED on #123 (Connes-distance subalgebra restriction conjecture)

**Hypothesis**: Pati-Salam embedding `SU(4)_C × SU(2)_L × SU(2)_R ⊃ SM` preserves the B1/B2 acoustic-vs-optical partition under Connes-distance subalgebra restriction. The B1 acoustic mode dominance factor 37 (per `project_flat-bands-squeeze-less.md`) is invariant under Pati-Salam embedding ONLY if #123 conjecture (Connes-distance subalgebra restriction preserves partition cardinality) lands as PASS.

**Method** (conditional on #123 PASS):
1. Load Pati-Salam embedding map from S86 W-9 framework registry.
2. Apply Connes-distance restriction (per #123 conjecture) on the embedded subalgebra `A_PS = M_4(C) ⊕ M_2(C) ⊕ M_2(C)`.
3. Evaluate B1/B2 partition cardinality on the embedded substrate.
4. Cross-check against B1 dominance factor 37 (canonical from `project_flat-bands-squeeze-less.md`).
5. PASS if partition preserved AND factor 37 reproduced; FAIL otherwise.

**Mechanical-closure protocol** (if #123 not landed by W12 dispatch):
- Verdict line: `S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION: FAIL -- value='PRE-REG-INC_blocked_by_S88-CONNES-DISTANCE-SUBALGEBRA-RESTRICTION-CONJECTURE_NOT-LANDED' scheme=Pati-Salam-embedding convention=Connes-distance-restriction L_max=10 audit_sha256=<computed> content_sha256=<computed> schema_version=S84+`
- Companion comment row: per `.claude/rules/mechanical-closure-discipline.md` §"Audit-trail signature"
- Working-paper section §W12-138 updated with Status=PRE-REG-INC, Verdict=FAIL-blocked, Substrate framing=preserved
- Routes to S89 carry-forward `S89-PATI-SALAM-EMBEDDING-RETRY-POST-CONNES-DISTANCE-LANDING`

**Machinery pin**:
- `embedding = Pati-Salam`
- `subalgebra_restriction = Connes-distance` (per #123)
- `B1_dominance_factor_canonical = 37` (project_flat-bands-squeeze-less)
- `L_max = 10`
- `prereq = #123`

**4-tuple**: (Pati-Salam, Connes-distance, B1/B2 partition, factor 37)

**Thresholds**:
- PASS (conditional on #123 PASS): partition preserved AND factor 37 reproduced within 1e-9
- FAIL: partition broken OR factor 37 not reproduced
- PRE-REG-INC: #123 not landed at W12 dispatch ⇒ mechanical closure to S89

**What PASS means**: Pati-Salam GUT embedding compatible with substrate B1/B2 acoustic-optical partition; cosmological dispersion hierarchy invariant under GUT-scale embedding.

**What FAIL means**: Pati-Salam embedding breaks substrate partition; cosmological dispersion invariance is GUT-scale-dependent; restricts the surviving GUT corridor.

**What PRE-REG-INC means**: prerequisite #123 not landed; the gate is structurally untestable at S88; honest closure preserves audit trail and routes to S89 with the prereq dependency named.

**Effort**: 0.5 wave-equivalents (conditional dispatch; mechanical closure ~0.05 wave-equivalents).

**Substrate framing**: The substrate IS the spectral triple over the algebra `A_K`. Pati-Salam is a parent-algebra embedding; the substrate is restricted via Connes-distance. The B1/B2 partition is a substrate-IS observable; cosmological dispersion hierarchy is the laboratory-IN observable. The bridge map is the partition-cardinality preservation under embedding. Container-thinking of "Pati-Salam in spacetime" is FORBIDDEN; Pati-Salam is an algebraic embedding, not a geometric inclusion.

---

## §W12-139 — `S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE`

**Trigger**: [VERIFY] (PRE-REG-INC at plan-freeze; mechanical closure if §VII.AJ.W4-1 not PASS-conditional landed)
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge (CMB cross-correlation observational ownership) + gen-physicist (orchestrator)
**Status**: BLOCKED on §VII.AJ.W4-1 cross-pillar 3-channel theorem PASS-conditional landing

**Hypothesis**: The CMB EE × BB × T cross-correlation directly probes c_sub conformal-anomaly multiplier with a substrate-distance-1 pole signature. The 9-cell tensor (3 channels × 3 regulator classes) per §VII.AJ.W4-1 STAGE-1-CANDIDATE provides the structural prediction; this gate audits the direct c_sub probe under Planck 2018 + LiteBIRD joint sensitivity.

**Method** (conditional on §VII.AJ.W4-1 PASS-conditional landing):
1. Load 9-cell tensor `(EE, BB, T) × (HypA, HypB, HypC)` from §VII.AJ.W4-1.
2. Compute cross-correlation amplitude per cell at substrate-distance-1 pole.
3. Aggregate to single c_sub probe scalar: `c_sub_probe = Σ_{ch, reg} w_{ch,reg} · A_{ch,reg}` with substrate-derived weights.
4. Compare against canonical_constants.py `c_sub_baseline = 2.238` (S86 W-3 lockdown).
5. PASS if `|c_sub_probe - 2.238| / 2.238 <= 0.01` (1% reproduction); FAIL otherwise.

**Mechanical-closure protocol** (if §VII.AJ.W4-1 not PASS-conditional landed):
- Verdict line: `S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE: FAIL -- value='PRE-REG-INC_blocked_by_VII-AJ-W4-1_CROSS-PILLAR-3-CHANNEL-NOT-PASS-CONDITIONAL' scheme=EE-BB-T-cross-correlation convention=substrate-distance-1-pole L_max=10 audit_sha256=<computed> content_sha256=<computed> schema_version=S84+`
- Routes to S89 carry-forward `S89-EE-BB-T-CSUB-PROBE-RETRY-POST-VII-AJ-W4-1-LANDING`

**Machinery pin**:
- `tensor_dim = 9` (3 channels × 3 regulators)
- `c_sub_baseline = 2.238` (S86 W-3 canonical)
- `pole = substrate-distance-1`
- `tolerance = 0.01` (1% reproduction)
- `prereq = §VII.AJ.W4-1 PASS-conditional`

**4-tuple**: (EE×BB×T 9-cell, substrate-distance-1, c_sub=2.238, tol=0.01)

**Thresholds**:
- PASS (conditional): `|c_sub_probe - 2.238| / 2.238 <= 0.01`
- FAIL: deviation > 0.01 ⇒ direct CMB probe conflicts with structural canonical
- PRE-REG-INC: §VII.AJ.W4-1 not landed ⇒ mechanical closure to S89

**What PASS means**: direct CMB cross-correlation reproduces the structural c_sub canonical at 1% precision; observational pathway to c_sub is operational; cosmological discrimination strength upgraded.

**What FAIL means**: direct CMB observational signal conflicts with structural canonical; either canonical misderived or observational systematic contaminates the cross-correlation; routes to source-reconciliation Class-(c) review.

**What PRE-REG-INC means**: §VII.AJ.W4-1 prerequisite not landed; honest closure routes to S89.

**Effort**: 0.5 wave-equivalents (conditional dispatch).

**Substrate framing**: The c_sub conformal-anomaly multiplier is a substrate-IS observable (spectral-distance-1 pole moment). The CMB EE×BB×T cross-correlation is a laboratory-IN observable (measured in the FRW container by Planck/LiteBIRD/CMB-S4). The bridge map is the 9-cell tensor decomposition. Container-thinking of "EE/BB modes propagating through space" is FORBIDDEN; the modes ARE substrate excitation patterns indexed by polarization channel + regulator class.

---

## §W12-140 — `S88-F-NL-EQUILATERAL-NON-GAUSSIANITY`

**Trigger**: [VERIFY] (PRE-REG-INC at plan-freeze; mechanical closure if W4-3 f_NL^folded language correction not landed)
**Classification**: PHONONIC
**Agent**: mack-cosmic-bridge (non-Gaussianity observational ownership) + gen-physicist (orchestrator)
**Status**: BLOCKED on W4-3 f_NL^folded language correction

**Hypothesis**: The framework's f_NL^equilateral prediction (S82 W3-4 path-B fabric coherent: `f_NL^equil = 0.853`) is reproducible at S88 from substrate-first GGE Bogoliubov vacuum specification. The audit requires the W4-3 f_NL^folded language correction to land first because the equilateral and folded shapes share substrate-derivation machinery and W4-3 surfaces a notation drift that propagates to equilateral at the cross-pollination layer.

**Method** (conditional on W4-3 landing):
1. Load GGE Bogoliubov vacuum specification (S82 W3-4 path-B fabric coherent).
2. Compute f_NL^equilateral via three-point correlation at the substrate level under canonical regulator-class HypB.
3. Cross-check against canonical 0.853 (Sage-QQ exact propagation; publication precision per Class-8.3 K=4).
4. Compare against Planck 2018 f_NL^equilateral = -26 ± 47 (1σ).
5. PASS if substrate value reproduces 0.853 at 1e-9 AND Planck constraint satisfied at 2σ.

**Mechanical-closure protocol** (if W4-3 not landed):
- Verdict line: `S88-F-NL-EQUILATERAL-NON-GAUSSIANITY: FAIL -- value='PRE-REG-INC_blocked_by_W4-3_F-NL-FOLDED-LANGUAGE-CORRECTION_NOT-LANDED' scheme=GGE-Bogoliubov-fabric-coherent convention=path-B-equilateral L_max=10 audit_sha256=<computed> content_sha256=<computed> schema_version=S84+`
- Routes to S89 carry-forward `S89-F-NL-EQUILATERAL-RETRY-POST-W4-3-CORRECTION-LANDING`

**Machinery pin**:
- `f_NL_equilateral_canonical_FW = 0.853` (S82 W3-4)
- `Planck_f_NL_equil_obs = -26 ± 47` (1σ)
- `derivation = GGE-Bogoliubov-fabric-coherent path-B`
- `regulator_class = HypB`
- `prereq = W4-3 f_NL^folded language correction`

**4-tuple**: (f_NL^equil=0.853, GGE-Bog-path-B, HypB, Planck 2018 1σ)

**Thresholds**:
- PASS: substrate value reproduces 0.853 at 1e-9 AND |f_NL^equil_FW - Planck_central| / Planck_1sigma <= 2.0 (2σ pass)
- FAIL: substrate value deviates > 1e-9 from canonical OR |deviation from Planck central| > 2σ
- PRE-REG-INC: W4-3 not landed ⇒ mechanical closure to S89

**What PASS means**: framework's equilateral non-Gaussianity prediction reproduces from substrate-first computation AND survives Planck 2018 2σ; cosmological non-Gaussianity discrimination operational.

**What FAIL means** (substrate): substrate computation does not reproduce 0.853 ⇒ Class-(c) PIN-DRIFT-FROM-STALE-SOURCE remediation. **(Planck)**: Planck constraint violated ⇒ closes a corridor of the GGE-Bogoliubov path-B parameter space.

**What PRE-REG-INC means**: W4-3 prerequisite not landed; routes to S89.

**Effort**: 0.5 wave-equivalents (conditional dispatch).

**Substrate framing**: f_NL^equilateral is a substrate-IS observable (three-point correlation of GGE Bogoliubov vacuum modes at the substrate level). Planck 2018 measures the laboratory-IN observable (CMB temperature 3-point correlation in the FRW container). The bridge map is the GGE-vacuum-to-CMB transfer through the (Δ_B/Δ_A)^p inheritance. Container-thinking of "non-Gaussianity in the early universe" is FORBIDDEN; non-Gaussianity IS the substrate's intrinsic GGE-Bogoliubov three-point structure.

---

## §W12-141 — `S88-OR-LATER-EXTENDED-THEOREM-INDEPENDENT-VERIFY`

**Trigger**: [VERIFY-THEOREM] (Stage-2 cross-axis joint-theorem promotion gate)
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (spectral-side cross-reviewer) + ALTERNATIVE TRANSIT-SIDE cross-reviewer (volovik BLOCKED as co-author per joint-theorem-promotion.md §"Two-Agent Independent-Verify": "Cross-reviewers cannot be the original workshop authoring agents")
**Hypothesis**: The Joint F_2-Class Path-(c) Theorem (S87 W9a-1 = CF-54) advances from STAGE-1-CANDIDATE to STAGE-3-PERMANENT via two-agent parallel cross-axis independent verify with PASS-AND on JOINT clauses (c) and (d).

**Note on volovik blockage**: volovik-superfluid-universe-theorist co-authored the original W-9 Path-(c) workshop. Per `.claude/rules/joint-theorem-promotion.md` §"Two-Agent Independent-Verify" condition (3), cross-reviewers cannot be original workshop authoring agents. The transit-side cross-reviewer for this Stage-2 gate is REASSIGNED to:
- **Primary candidate**: kaku-multidimensional (transit-dynamics-adjacent; not in W-9 author set)
- **Fallback candidate**: hawking-area-theorem (transit-dynamics analog via area-monotonicity bridge; not in W-9 author set)
- **Selection protocol**: gen-physicist orchestrator queries `mcp__knowledge__.search_knowledge("transit-dynamics-axis cross-reviewer S87 W-9 author exclusion")` and dispatches the highest-ranked non-author transit-side reviewer.

**Method**: per `joint-theorem-promotion.md` §Stage-2 (identical structure to §W12-137):
1. Identify single-axis vs JOINT clauses in the §VII.AH STAGE-1-CANDIDATE entry text:
   - Single-axis clauses (a) + (e) lizzi-side spectral-functional
   - Single-axis clauses (b) + (f) transit-side dynamics
   - JOINT clauses (c) + (d) (require both axes)
2. Dispatch connes-ncg as Axis-A spectral-side cross-reviewer (audits (a) + (e) + JOINT (c) + JOINT (d); reads only Stage-1 entry + canonical_constants.py + falsifier-master-inventory row; NO workshop transcripts).
3. Dispatch ALTERNATIVE-TRANSIT-SIDE as Axis-B cross-reviewer (audits (b) + (f) + JOINT (c) + JOINT (d); same source restriction).
4. PASS-AND on JOINT clauses.
5. If all clauses PASS in respective reviewers AND both JOINT clauses PASS in BOTH ⇒ Stage-3 promotion at S88 R3 finalization.

**Machinery pin**:
- `cross_reviewer_A = connes-ncg-theorist` (spectral-functional side)
- `cross_reviewer_B = <transit-dynamics-axis non-author>` (selected via knowledge-MCP search; volovik EXCLUDED)
- `dispatch_mode = PARALLEL`
- `prior_workshop_context = WITHHELD`
- `JOINT_clauses = ["(c)", "(d)"]`
- `JOINT_logical_op = AND`
- `audit_script = computations/_joint_theorem_independent_verify_audit.py`
- `volovik_exclusion_reason = "W-9 co-author per joint-theorem-promotion.md condition (3)"`

**4-tuple**: (Stage-2 verify, parallel dispatch, no-workshop-context + volovik-excluded, PASS-AND on JOINT)

**Thresholds**:
- PASS (promotion): all single-axis clauses PASS in respective reviewer + both JOINT clauses PASS in BOTH reviewers ⇒ STAGE-3-PERMANENT
- FAIL: any clause FAIL ⇒ promotion blocked; theorem stays Stage-1
- INFO: any clause INFO ⇒ promotion stays Stage-1; INFO clause documented as Stage-2-INFO-deferred

**What PASS means**: Joint F_2-Class Path-(c) Theorem promotes to permanent registry; cross-axis spectral-functional + transit-dynamics joint result citable as structural theorem.

**What FAIL means**: a clause does not survive cross-axis independent audit; the candidate has a structural gap; promotion blocked closes a structural-theorem corridor.

**Effort**: 1.0 wave-equivalent (two parallel cross-reviewer dispatches + audit-script verification).

**Substrate framing**: The theorem connects substrate-IS spectral-functional observables to substrate-IS transit-dynamics observables via JOINT cross-axis clauses. Stage-2 verification structurally enforces axis-orthogonality at the verification layer. Direction: substrate spectral-moment IS → bridge map → transit-dynamics IS observable. No container-thinking present.

---

## §W12-142 — `S88-OR-LATER-Q-7-CROSS-REGION-PARTITION-APPLICATION`

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (cross-region partition machinery) + gen-physicist (orchestrator)
**Status**: prerequisites partial — CF-66 + CF-67 + CF-68 + CF-10

**Hypothesis**: The Q-7 cross-region partition application extends the W-9 §VII.AH Path-(c) successor anchor structure to additional regions of the (regulator, scheme) joint space. PASS confirms the partition application is regulator-class-invariant; FAIL identifies a region where the partition breaks.

**Method**:
1. Load CF-66 + CF-67 + CF-68 + CF-10 outputs from S87 closure registry (verify each prereq landed; if missing, mechanical-closure protocol per §W12-138/139/140).
2. Apply Q-7 cross-region partition to extended (regulator, scheme) joint space across {Zubarev, zeta, Pauli-Villars, Mellin} × {HypA, HypB, HypC, HypD}.
3. Evaluate partition stability: cardinality vector (n_1, n_2, n_3, n_4) at each (R, S) cell.
4. PASS if cardinality vector is constant across all 16 cells; FAIL if any cell deviates.
5. Cross-link to §VII.AH STAGE-1-CANDIDATE for downstream Stage-2 audit input.

**Machinery pin**:
- `regulator_axis = {Zubarev, zeta, Pauli-Villars, Mellin}` (4 regulators)
- `scheme_axis = {HypA, HypB, HypC, HypD}` (4 schemes)
- `joint_space_cells = 16` (4 × 4)
- `partition_observable = (n_1, n_2, n_3, n_4)` cardinality vector
- `L_max = 10`
- `prereqs = [CF-66, CF-67, CF-68, CF-10]`

**4-tuple**: (4 regulators, 4 schemes, 16 cells, cardinality vector)

**Thresholds**:
- PASS: cardinality vector constant across all 16 cells (regulator-class invariant)
- FAIL: any cell deviates ⇒ identifies region where partition breaks; closes corridor
- INFO: partial deviation (1-2 cells) ⇒ structural exception; documented as carry-forward

**What PASS means**: Q-7 cross-region partition application is regulator-class invariant; substrate partition structure stable across the joint space; downstream §VII.AH Stage-2 audit gains structural support.

**What FAIL means**: partition breaks in identified region; cosmological discrimination at that cell weakens; closes a corridor of the joint regulator-scheme space.

**Effort**: 0.7 wave-equivalents (16-cell scan + cardinality evaluation; conditional on prereq landings).

**Substrate framing**: The partition is a substrate-IS observable on the spectral triple. Cross-region application audits substrate-level invariance under regulator-class change. No laboratory-IN observable involved; this is pure substrate-structure verification. Direction: substrate IS → partition cardinality. Container-thinking absent.

---

## §W12-143 — `S88-OR-LATER-Q-8-PER-CLASS-N-BREAKDOWN-FORWARD-MODELING`

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (per-class N-breakdown machinery) + mack-cosmic-bridge (cosmological forward-modeling) + gen-physicist (orchestrator)
**Status**: prereq CF-42 LANDED; W9b-1 cross-link

**Hypothesis**: The Q-8 per-class N-breakdown forward modeling extends the W9b-1 measured N_breakdown_spread = 31.98% to a forward-prediction model conditional on per-class regulator restriction. The forward model predicts N_breakdown(R) for each regulator class R ∈ {HypA, HypB, HypC, HypD}.

**Method**:
1. Load CF-42 per-class N-breakdown prereq output (LANDED at S87).
2. Cross-link to W9b-1 measured spread 31.98%.
3. Build forward-prediction model: `N_breakdown(R) = N_breakdown_baseline + Δ(R)` where `Δ(R)` is a substrate-derived per-class deviation.
4. Compute predicted N_breakdown for each regulator class.
5. Cross-check predicted spread against W9b-1 measured 31.98% (1% tolerance).
6. PASS if forward-model spread reproduces 31.98% ± 1%; FAIL otherwise.

**Machinery pin**:
- `N_breakdown_measured = 31.98%` (W9b-1)
- `regulator_classes = {HypA, HypB, HypC, HypD}` (4 classes)
- `forward_model = N_breakdown(R) = N_breakdown_baseline + Δ(R)`
- `tolerance = 0.01` (1% spread reproduction)
- `prereq = CF-42` (LANDED)

**4-tuple**: (per-class N_breakdown, 4 classes, forward model, 31.98% target)

**Thresholds**:
- PASS: `|N_breakdown_predicted_spread - 31.98%| / 31.98% <= 0.01`
- FAIL: deviation > 1% ⇒ forward model deficient; closes corridor of per-class regulator-restriction modeling
- INFO: marginal (1-3% deviation) ⇒ documented as carry-forward

**What PASS means**: per-class forward model reproduces W9b-1 measured spread; substrate-derived per-class deviations Δ(R) are operationally predictive; downstream cosmological forward-modeling gains structural backing.

**What FAIL means**: forward model deficient; substrate-prior heuristic refuted (per W9b-1 N_breakdown spread refuting prior heuristic); closes a corridor.

**Effort**: 0.6 wave-equivalents (forward-model build + per-class evaluation + W9b-1 cross-check).

**Substrate framing**: N_breakdown is a substrate-IS observable (Mellin-cone moment partition cardinality at per-regulator restriction). The forward model is substrate-level prediction; W9b-1 measurement is the substrate-level reference. No laboratory-IN observable; pure substrate verification.

---

## §W12-144 — `S88-SR-LO-PER-CLASS-DOWNSTREAM-RESPEC`

**Trigger**: [AUDIT]
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (canonical N_breakdown ownership) + gen-physicist (orchestrator)
**Hypothesis**: Downstream consumers of canonical N_breakdown require respec for per-class regulator restrictions. The audit identifies all downstream consumers (gates, registry rows, canonical_constants.py entries) that cite N_breakdown without per-class regulator-class tagging and emits respec recommendations.

**Method**:
1. Grep `computations/**/*.py` for `N_breakdown` literal references.
2. Grep `sessions/framework/registry/**/*.md` for `N_breakdown` references.
3. Grep `computations/canonical_constants.py` for `N_breakdown` entries.
4. For each hit, classify: (a) per-class-tagged (e.g., `N_breakdown_HypA_FW`); (b) bare (no regulator-class tag).
5. Emit respec recommendations for category (b) hits per `regulator-pin-discipline.md` §"Tag Format" extended to N_breakdown.
6. PASS if ≥80% of hits are already per-class-tagged; FAIL otherwise.

**Machinery pin**:
- `audit_targets = [computations/, sessions/framework/registry/, computations/canonical_constants.py]`
- `tag_pattern = r'N_breakdown_(HypA|HypB|HypC|HypD)_FW'`
- `bare_pattern = r'\bN_breakdown\b(?!_)'`
- `pass_threshold = 0.80` (80% per-class-tagged)
- `discipline_source = .claude/rules/regulator-pin-discipline.md`

**4-tuple**: (audit corpus, per-class tag pattern, bare pattern, 80% threshold)

**Thresholds**:
- PASS: ≥80% of N_breakdown hits per-class-tagged
- FAIL: <80% per-class-tagged ⇒ respec batch required
- INFO: 80-90% per-class-tagged ⇒ partial respec recommended

**What PASS means**: downstream consumers of N_breakdown are largely per-class-tagged; substrate-level regulator discipline propagated correctly; audit confirms hygiene.

**What FAIL means**: bare N_breakdown citations propagate ambiguity; respec batch required; routes to S89 carry-forward `S89-N-BREAKDOWN-PER-CLASS-RESPEC-BATCH`.

**Effort**: 0.3 wave-equivalents (grep audit + classification + report).

**Substrate framing**: N_breakdown is a substrate-IS observable per regulator class. Bare references conflate regulator classes ⇒ substrate-IS distinction lost. Audit operates at the methodology-pin layer (per-class regulator discipline propagation). No container-thinking present.

---

## §W12-145 — `S88-POLE-SCOPE-GENERIC-PLURALISM-VERIFY`

**Trigger**: [VERIFY-THEOREM] (Stage-2 cross-axis joint verify on pole-scope structural correlation)
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (axiomatic cross-reviewer; axis-orthogonality side) + volovik-superfluid-universe-theorist (transit-side cross-reviewer; framework's SHARPEST reviewer per `feedback_agent-roster.md`); gen-physicist orchestrator dispatches BOTH IN PARALLEL WITHOUT prior workshop context per `joint-theorem-promotion.md` §"Two-Agent Independent-Verify"
**Hypothesis**: The W-9 spectral-side ↔ dynamical-side anti-correlation at s=3 substrate-distance-1 pole (`|ρ_S| = 1.0` EXACT across A_5 4-class projection) extends to other Mellin poles ⇒ Reading_1 generic pluralism. Stage-2 cross-axis verify discriminates Reading_1 (generic) vs Reading_2 (pole-specific to s=3 only).

**Method**:
1. Load §VII.AH (or §VII.<slot>) STAGE-1-CANDIDATE entry for pole-scope structural correlation.
2. Dispatch connes-ncg as Axis-A axiomatic cross-reviewer (audits axiomatic consistency + cross-pole prediction; reads only registered entry + canonical_constants.py; NO workshop transcripts).
3. Dispatch volovik-superfluid-universe as Axis-B transit-side cross-reviewer (audits dynamical consistency + cross-pole prediction; same source restriction).
4. PASS-AND on the cross-pole prediction (Reading_1 generic pluralism prediction must PASS in BOTH).
5. If BOTH PASS ⇒ Reading_1 confirmed; promote pole-scope claim to STAGE-3-PERMANENT.
6. If either FAIL ⇒ Reading_2 pole-specific reading favored; claim stays Stage-1 with corrigendum.

**Machinery pin**:
- `cross_reviewer_A = connes-ncg-theorist`
- `cross_reviewer_B = volovik-superfluid-universe-theorist`
- `dispatch_mode = PARALLEL`
- `prior_workshop_context = WITHHELD`
- `JOINT_prediction = Reading_1 generic pluralism`
- `JOINT_logical_op = AND`
- `discriminator = "Reading_1 PASS in BOTH ⇒ generic; FAIL in either ⇒ Reading_2 pole-specific"`

**4-tuple**: (Stage-2 verify, parallel dispatch, Reading_1 vs Reading_2, PASS-AND)

**Thresholds**:
- PASS: Reading_1 PASS in BOTH ⇒ generic pluralism confirmed; promote
- FAIL: Reading_1 FAIL in either ⇒ Reading_2 pole-specific favored; claim stays Stage-1 with pole-scoping corrigendum
- INFO: ambiguous in either ⇒ documented as Stage-2-INFO-deferred

**What PASS means**: structural correlation generalizes across Mellin poles; substrate ↔ dynamical anti-correlation is a generic property of the spectral structure; STAGE-3-PERMANENT promotion of generic-pluralism reading.

**What FAIL means**: structural correlation is pole-specific (s=3 only); registry entry must be re-scoped per `epistemic-discipline.md` §"Pole-Scope sub-clause"; closes the generic-pluralism corridor and pins the structural correlation to s=3.

**Effort**: 1.0 wave-equivalent (two parallel cross-reviewer dispatches + audit-script verification).

**Substrate framing**: The pole-scope reading is a substrate-IS observable property (cross-pole behavior of Mellin-residue moments). Both cross-reviewers audit substrate-level — no laboratory-IN observable. Stage-2 verification structurally enforces axis-orthogonality. Direction: substrate IS Mellin pole structure → Reading_1/Reading_2 discriminator. No container-thinking.

---

## §W12-146 — `S88-POLE-SPECIFICITY-CROSS-REG-METRIC-DISAMBIGUATION`

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (Mellin-pole machinery) + gen-physicist (orchestrator)
**Hypothesis**: The W9b-2 ρ_S(s=4) = -1.000 EXACT result with cross-regulator spread 0.0513 (lines 271+274 sub-cut) admits TWO disambiguating readings: (i) sub-cut explanation as cross-regulator metric artifact; (ii) sub-cut explanation as genuine pole-specificity signature. This gate disambiguates.

**Method**:
1. Load W9b-2 lines 271+274 sub-cut data.
2. Compute cross-regulator spread under each disambiguating reading.
3. Reading (i) artifact: spread 0.0513 should reduce under regulator-pin canonical anchoring (CAC) per `regulator-convention-lockdown.md`.
4. Reading (ii) genuine: spread 0.0513 should be invariant under CAC anchoring.
5. Apply CAC anchoring to W9b-2 data; recompute spread.
6. PASS-Reading-(i) if spread reduces below 0.01; PASS-Reading-(ii) if spread stays at 0.0513 ± 0.001; INFO if intermediate.

**Machinery pin**:
- `pole = s=4`
- `rho_S_canonical = -1.000` (EXACT)
- `cross_regulator_spread_pre_CAC = 0.0513`
- `CAC_threshold_artifact = 0.01` (post-anchoring spread threshold for Reading-(i))
- `CAC_invariance_threshold = 0.001` (post-anchoring spread threshold for Reading-(ii))
- `data_source = W9b-2 lines 271+274 sub-cut`

**4-tuple**: (s=4 pole, ρ_S=-1.000, pre-CAC spread 0.0513, post-CAC threshold)

**Thresholds**:
- PASS-Reading-(i): post-CAC spread < 0.01 ⇒ artifact
- PASS-Reading-(ii): post-CAC spread = 0.0513 ± 0.001 ⇒ genuine pole-specificity signature
- INFO: intermediate (0.01 ≤ spread ≤ 0.0513 - 0.001) ⇒ ambiguous

**What PASS-(i) means**: cross-regulator spread is artifact of pre-CAC convention; post-CAC anchoring resolves; pole-specificity claim weakened.

**What PASS-(ii) means**: cross-regulator spread is genuine pole-specificity signature; substrate carries regulator-resolution dependence at s=4 pole; structural property pinned.

**What INFO means**: disambiguation incomplete; routes to S89 carry-forward `S89-POLE-SPECIFICITY-FURTHER-DISAMBIGUATION`.

**Effort**: 0.4 wave-equivalents (CAC anchoring + spread re-evaluation + reading discrimination).

**Substrate framing**: The pole-specificity is a substrate-IS observable. CAC anchoring is the canonical-anchored substrate-level convention. No laboratory-IN observable; pure substrate disambiguation.

---

## §W12-147 — `S88-W9-LCR3-RESOLUTION-SPECIFICITY-T1-21-EXTENSION`

**Trigger**: [METHODOLOGY] (METHODOLOGY-class wave per `wave-classification.md` 4-test conjunction)
**Classification**: METHODOLOGY (M1: artifact-existence-with-substantive-content; M2: rule-file edit only; M3: verbatim sub-diff from W9 LCR3 closure; M4: gate-ID allowlisted in `methodology-wave-allowlist.md`)
**Agent**: gen-physicist (orchestrator-direct-write per METHODOLOGY-class dispatch consequences in `wave-classification.md`)
**Hypothesis**: The W9 LCR3 resolution-specificity finding (registry entry text scope correction) extends T1-21 §"Source Reconciliation — Resolution-Specificity Scoping sub-clause" with a new calibration corpus instance.

**Method** (per `wave-classification.md` §"Dispatch consequences" METHODOLOGY-class):
1. Load W9 LCR3 closure text (registry-text update specification).
2. Load `.claude/rules/epistemic-discipline.md` §"Source Reconciliation — Resolution-Specificity Scoping sub-clause".
3. Append W9 LCR3 instance to T1-21 calibration corpus per the rule's append-only discipline.
4. Verify M1-M4 conjunction at pre-write: M1 artifact-existence predicate; M2 Edit on `.claude/rules/epistemic-discipline.md`; M3 verbatim sub-diff; M4 gate-ID allowlisted (verify entry in `methodology-wave-allowlist.md`; if absent, plan-freeze halt requesting orchestrator allowlist append).
5. Apply Edit; verify dual-SHA closure: `content_sha256` over rule-file diff; `audit_sha256` over input-pin map (W9 LCR3 closure SHA + epistemic-discipline.md pre-edit SHA).
6. Append verdict line per METHODOLOGY-class dual-SHA discipline.

**Machinery pin**:
- `target_rule_file = .claude/rules/epistemic-discipline.md`
- `target_sub_clause = §"Source Reconciliation — Resolution-Specificity Scoping sub-clause"`
- `calibration_corpus_addition = W9 LCR3 instance`
- `dispatch_mode = METHODOLOGY-class orchestrator-direct-write` (NO `/rclab-coordinate` compute-mode)
- `dual_SHA = (content_sha256 over rule-file diff, audit_sha256 over input-pin map)`
- `M4_allowlist_entry = required` (gate-ID `S88-W9-LCR3-RESOLUTION-SPECIFICITY-T1-21-EXTENSION`)

**4-tuple**: (METHODOLOGY-class, rule-file edit, dual-SHA, M4 allowlist)

**Thresholds**:
- PASS: rule-file edit landed; calibration corpus advanced; dual-SHA closure verified; substantive content >15 lines per M1
- FAIL: M1-M4 conjunction violated; or dual-SHA mismatch
- INFO: edit lands but calibration corpus addition is shorter than 15 lines ⇒ M1 stub-violation

**What PASS means**: T1-21 calibration corpus advances by one instance; resolution-specificity scoping discipline gains structural backing; rule-file maturation tracked.

**What FAIL means**: methodology-wave classification audit failure; routes to remediation per `wave-classification.md` §"Strict-conjunction requirement".

**Effort**: 0.2 wave-equivalents (METHODOLOGY-class orchestrator-direct-write; no compute).

**Substrate framing**: METHODOLOGY-class waves operate at the methodology layer per `epistemic-discipline.md` §"Layer-Decomposition" Phi correspondence. No substrate-IS observable directly involved; the wave maintains the methodology layer's rule-file inventory. Direction-neutral at the methodology layer.

---

## §W12-148 — `S88-POLE-SPECIFICITY-HIGHER-N-POLES-EXTENSION`

**Trigger**: [VERIFY]
**Classification**: PHONONIC
**Agent**: connes-ncg-theorist (Mellin-pole machinery) + gen-physicist (orchestrator)
**Hypothesis**: The W9b-2 ρ_S(s=4) = -1.000 EXACT result extends to higher-N Mellin poles s=5 and s=6. PASS-N=5 confirms extension; PASS-N=6 confirms further extension. Cross-pole behavior discriminates Reading_1 generic vs Reading_2 pole-specific (cross-link to §W12-145).

**Method**:
1. Load D_K eigenmoment cache `s84_spectrum_cache_L12_tau019.npz` at L_max=10 (Friedrich-Bär saturation).
2. Compute Mellin residue at s=5 pole; evaluate substrate ↔ dynamical correlation ρ_S(s=5).
3. Compute Mellin residue at s=6 pole; evaluate ρ_S(s=6).
4. PASS-N=5 if `|ρ_S(s=5) + 1.000| <= 1e-9` (anti-correlation extends).
5. PASS-N=6 if `|ρ_S(s=6) + 1.000| <= 1e-9`.
6. Joint result: PASS-N5-AND-N6 ⇒ generic-pluralism reading confirmed at higher-N poles; PASS-N5-only or PASS-N6-only ⇒ partial extension; FAIL-both ⇒ pole-specific to s=3+s=4.

**Machinery pin**:
- `poles = [s=5, s=6]`
- `rho_S_target = -1.000` (anti-correlation invariant under pole extension)
- `tolerance = 1e-9`
- `regulator_pin_tag = a_n^{Mellin}` for n ∈ {5, 6} per `regulator-pin-discipline.md`
- `L_max = 10`
- `data_source = s84_spectrum_cache_L12_tau019.npz`

**4-tuple**: (s=5+s=6 poles, ρ_S anti-correlation, tol=1e-9, L_max=10)

**Thresholds**:
- PASS-both: ρ_S(s=5) and ρ_S(s=6) both reproduce -1.000 at 1e-9 ⇒ extension confirmed
- PASS-N5-only or PASS-N6-only: partial extension; documented as INFO
- FAIL-both: pole-specific to s=3+s=4; closes generic-pluralism corridor at higher-N poles

**What PASS-both means**: substrate ↔ dynamical anti-correlation extends across Mellin poles; generic-pluralism reading (cross-link §W12-145) gains structural backing; STAGE-3-PERMANENT pathway opened.

**What FAIL-both means**: pole-specific reading favored; structural correlation localizes at s=3+s=4; closes a structural-theorem corridor.

**Effort**: 0.7 wave-equivalents (Mellin-residue evaluation at two poles + correlation evaluation + cross-link to §W12-145 update).

**Substrate framing**: Higher-N poles are substrate-IS Mellin-cone observables. Anti-correlation extension is substrate-level structural property. No laboratory-IN observable; pure substrate verification. Direction: substrate IS Mellin-pole structure → cross-pole correlation property.

---

## Wave 12 → Wave 13 Decision Point

| Outcome scenario | Wave 13 routing |
|:-----------------|:----------------|
| All 14 gates PASS / mechanical-closure | Wave 13 dispatches normally per S88 plan |
| #137 Stage-2 PASS | Joint LiteBIRD-LISA-Fisher promoted STAGE-3-PERMANENT; Wave 13 cites permanently |
| #137 Stage-2 FAIL | FAIL clause routes to S89 carry-forward; Wave 13 proceeds with theorem at Stage-1 |
| #141 Stage-2 PASS | Joint F_2-Class Path-(c) promoted STAGE-3-PERMANENT |
| #141 Stage-2 FAIL | promotion blocked; theorem stays Stage-1 |
| #138/#139/#140 PRE-REG-INC | mechanical-closure verdict; routes to S89 with prereq dependency named |
| #145 Reading_1 PASS | generic-pluralism reading confirmed; cross-link to §W12-148 reinforces |
| #145 Reading_2 favored | pole-specific reading; registry entry re-scoped |
| #144 audit FAIL | per-class respec batch required; routes to S89 |

**Routing trigger gates**:
- #137 Stage-2 PASS unlocks promotion-cycle for #141 (sequential Stage-2 verify on related joint theorems)
- #145 + #148 joint outcome determines pole-scope generic-vs-specific reading at S89

---

## Wave 12 Machinery-Enumeration Pin (§0.11)

Per `.claude/rules/epistemic-discipline.md` §"Pre-Registration Completeness", every gate-relevant machinery parameter is enumerated below per gate. PRDR (Pre-Registration Dry-Run) at plan-write time confirms cardinality.

| Gate | Free parameters enumerated | Status |
|:-----|:---------------------------|:-------|
| #135 | pole=s=4, regulator=Mellin, convention=HypB+HypA, L_max=10, tau_fold=0.190, offset_Mellin (CAC), publication_sig_figs=10, verifier_rel_tol=1e-9 | PIN COMPLETE |
| #136 | pre_reg_threshold_sigma=5.0, band_axis_half_width_sigma=0.5, regulator_axis_oom_band=0.5, LISA_Fisher_joint_sigma=47.086, LiteBIRD_n_T_3yr_sigma_floor=0.0540, interpretation=JOINT-DISCRIMINATOR | PIN COMPLETE |
| #137 | cross_reviewer_A=mack-cosmic-bridge, cross_reviewer_B=connes-ncg-theorist, dispatch_mode=PARALLEL, prior_workshop_context=WITHHELD, JOINT_clauses=[(e),(f)], JOINT_logical_op=AND, audit_script | PIN COMPLETE |
| #138 | embedding=Pati-Salam, subalgebra_restriction=Connes-distance, B1_dominance_factor=37, L_max=10, prereq=#123 | PIN COMPLETE (PRE-REG-INC pending) |
| #139 | tensor_dim=9, c_sub_baseline=2.238, pole=substrate-distance-1, tolerance=0.01, prereq=§VII.AJ.W4-1 | PIN COMPLETE (PRE-REG-INC pending) |
| #140 | f_NL_equilateral_canonical=0.853, Planck_f_NL_equil_obs=-26±47, derivation=GGE-Bog-path-B, regulator_class=HypB, prereq=W4-3 | PIN COMPLETE (PRE-REG-INC pending) |
| #141 | cross_reviewer_A=connes-ncg, cross_reviewer_B=non-W9-author transit-side, dispatch_mode=PARALLEL, prior_workshop_context=WITHHELD, JOINT_clauses=[(c),(d)], JOINT_logical_op=AND, audit_script, volovik_exclusion_reason | PIN COMPLETE |
| #142 | regulator_axis (4 regulators), scheme_axis (4 schemes), joint_space_cells=16, partition_observable cardinality vector, L_max=10, prereqs=[CF-66,CF-67,CF-68,CF-10] | PIN COMPLETE |
| #143 | N_breakdown_measured=31.98%, regulator_classes (4), forward_model, tolerance=0.01, prereq=CF-42 | PIN COMPLETE |
| #144 | audit_targets, tag_pattern, bare_pattern, pass_threshold=0.80, discipline_source | PIN COMPLETE |
| #145 | cross_reviewer_A=connes-ncg, cross_reviewer_B=volovik, dispatch_mode=PARALLEL, prior_workshop_context=WITHHELD, JOINT_prediction=Reading_1, JOINT_logical_op=AND, discriminator | PIN COMPLETE |
| #146 | pole=s=4, rho_S_canonical=-1.000, cross_regulator_spread_pre_CAC=0.0513, CAC_threshold_artifact=0.01, CAC_invariance_threshold=0.001, data_source | PIN COMPLETE |
| #147 | target_rule_file, target_sub_clause, calibration_corpus_addition, dispatch_mode=METHODOLOGY-class, dual_SHA, M4_allowlist_entry | PIN COMPLETE (METHODOLOGY-class) |
| #148 | poles=[s=5,s=6], rho_S_target=-1.000, tolerance=1e-9, regulator_pin_tag=a_n^{Mellin}, L_max=10, data_source | PIN COMPLETE |

---

## Wave 12 Input-SHA Ledger

Per `.claude/rules/agent-standards.md` §"Agent-Memory Registry Inversion (AMRI)" calibration: input pins reference project-level files only, NOT agent-memory paths. Per-agent role assignment declared in §W12 author attribution; no agent-memory pin rows in this ledger.

| File path | Input-pin role | SHA at plan-freeze |
|:----------|:---------------|:------------------|
| `computations/canonical_constants.py` | machinery pin source for δ_speed, c_sub_baseline, w0_FW, n_s_FW, f_NL_equil_FW, etc. | `<pinned at dispatch>` |
| `computations/s84_spectrum_cache_L12_tau019.npz` | D_K eigenmoment cache for #135, #146, #148 | `<pinned at dispatch>` |
| `sessions/framework/registry/falsifier-master-inventory.md` | falsifier rows for cross-link audit (#137, #141, #144) | `<pinned at dispatch>` |
| `sessions/framework/registry/branch-iv-canonical.md` | branch-(iv) substrate-natural anchor cross-reference | `<pinned at dispatch>` |
| `sessions/permanent-results-registry.md` | §VII.AH STAGE-1-CANDIDATE entry (#137 + #141 cross-reviewer source); §VII.AJ.W4-1 (#139 prereq) | `<pinned at dispatch>` |
| `sessions/archive/session-87/session-87-results-workingpaper.md` §W3-3d | Stage-1 npz reference for #137 | `<pinned at dispatch>` |
| `computations/s87_w3_3d_joint_litebird_lisa_fisher.npz` | Stage-1 data for #137 | `<pinned at dispatch>` |
| `.claude/rules/epistemic-discipline.md` | T1-21 sub-clause source (#147 target) | `<pinned at dispatch>` |
| `.claude/rules/joint-theorem-promotion.md` | Stage-2 protocol source (#137, #141, #145) | `<pinned at dispatch>` |
| `.claude/rules/methodology-wave-allowlist.md` | M4 allowlist for #147 | `<pinned at dispatch>` |
| `.claude/rules/regulator-convention-lockdown.md` | CAC convention for #135, #146 | `<pinned at dispatch>` |
| `.claude/rules/regulator-pin-discipline.md` | a_n^{Mellin} tag discipline for #135, #144, #148 | `<pinned at dispatch>` |
| `.claude/rules/substrate-first-canonical-sourcing.md` | Class-(f) audit pattern for #135 | `<pinned at dispatch>` |
| `.claude/rules/cross-pillar-bridge-anatomy.md` | bridge-anatomy 5-IS-not-IN + 3-level ladder for substrate framing sections | `<pinned at dispatch>` |
| `.claude/rules/phononic-framing.md` | IS-not-IN direction enforcement for all 14 gates | `<pinned at dispatch>` |
| `.claude/rules/mechanical-closure-discipline.md` | PRE-REG-INC verdict-line schema for #138, #139, #140 | `<pinned at dispatch>` |
| `.claude/rules/wave-classification.md` | METHODOLOGY-class dispatch for #147 | `<pinned at dispatch>` |
| `computations/_joint_theorem_independent_verify_audit.py` | Stage-2 audit script for #137, #141, #145 | `<pinned at dispatch>` |
| `sessions/archive/session-86/workshops/s86-w-3-...md` (W-3 workshop §R3-A closure) | δ_speed Path-H = 0.00745, Path-C = 0.011731522 closure values for #135 cross-check | `<pinned at dispatch>` |
| Carry-forward registry CF-42, CF-54, CF-66, CF-67, CF-68, CF-10 | prereq landings for #141, #142, #143 | `<pinned at dispatch>` |

`audit_sha256` for each gate computed from its input-pin map subset via `closure_hash(pin_map)` per `.claude/rules/gate-verdicts.md` dual-SHA discipline. Per-gate-distinct audit_sha256 enforced (sig_5 ladder uniqueness preserved).

---

## Plan-freeze audit checklist

- [x] PRU cardinality (§0.10): all 14 gates have machinery pin map enumerated
- [x] Source-Reconciliation: external-paper provenance flags routed to substrate-first canonical (#135 SUBSTRATE-FIRST per W0c-3 + W5a-2 calibration corpus)
- [x] Substrate-First-Provenance (S87 V.1 audit pattern): #135 routes external-paper W-3 closure values to substrate-first Mellin-cone computation
- [x] PRDR machinery enumeration (§0.11): all 14 gates pinned
- [x] Wave-classification: 13 PHONONIC-class + 1 METHODOLOGY-class (#147); M1-M4 conjunction declared at pre-write
- [x] Methodology-wave-allowlist: #147 gate-ID requires allowlist append before dispatch (orchestrator-only edit per recursion-attack closure)
- [x] Mechanical-closure protocol: #138, #139, #140 pre-registered with PRE-REG-INC routing if prereqs not landed
- [x] Stage-2 audit: #137, #141, #145 dispatch parameters verified (parallel + no-workshop-context + non-author cross-reviewers)
- [x] Substrate framing: every gate has IS-not-IN direction + bridge-anatomy element where cross-pillar
- [x] Substitution chain: #135 sign claim has explicit 5-step chain in gate block (mandatory per `math-scripts.md` §"Double-Check Logic Before Compute")
- [x] Volovik exclusion: #141 documents transit-side reassignment with selection protocol; volovik retained as cross-reviewer for #145 (W-9 author exclusion does NOT apply to pole-scope gate per joint-theorem-promotion.md scope)
- [x] AMRI compliance: input-pin ledger contains project-level files only; per-agent ownership declared in §W12 author attribution table

---

**Plan-freeze SHA**: computed at dispatch time over the full §W12 plan block + input-pin ledger.
**Verdict file**: `computations/s88_gate_verdicts.txt`
**Script prefix**: `s88_w12_<slug>.py`
