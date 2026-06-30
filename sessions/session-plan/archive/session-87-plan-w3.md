# Session 87 Plan — Wave 3: Path-H/Path-C + LiteBIRD/LISA Falsifier Suite

**Wave**: W3
**Owner subagent_type**: `gen-physicist`
**Theme**: 5 W-3 gen-physicist gates landing Path-H/Path-C multi-valued classification (CF-20), BK-Array meta-classifier_v2 callable module (CF-21), joint LiteBIRD-LISA 2×2 falsifier suite with δ_speed sub-gate (CF-22 + CF-23 = §W3-3a..§W3-3e), and S88+ Pati-Salam / EE/BB-T / f_NL^equilateral candidate gates (CF-24 = three pre-scoped placeholder stubs).
**Item count**: 5 top-level items (CF-20, CF-21, CF-22 with 5 sub-gates, CF-23 absorbed into CF-22 as §W3-3c, CF-24 with 3 placeholder sub-stubs)
**Effort estimate**: ~3.5-4.5 wave-equivalents combined (CF-20 ~0.5, CF-21 ~1, CF-22+CF-23 ~2, CF-24 ~0.25 stub-only)
**Level**: LEVEL 1 (must-do for S87) for CF-20, CF-21, CF-22, CF-23; LEVEL 5 (S88+ stub-only) for CF-24
**Verdict-file path**: `computations/s87_gate_verdicts.txt` (canonical, per `.claude/rules/gate-verdicts.md`)

---

## §0. Wave W3 Summary

W3 is the **classification-and-falsifier landing wave** of S86 W-3 (r-Dual-Pathway + BK-Array workshop). The W-3 workshop closed at S86 R3 with §VII.AC = "r-Dual-Pathway + BK-Array Joint Classifier + n_T = -r/8 Audit" (S86 W-3 — gen-physicist primary, connes-ncg-theorist + volovik co-signed, 2026-04-27). Two of its sub-rows landed at S86 close as DEFERRED placeholders awaiting S87 carry-forward:

- **§VII.AC.1** — DEFERRED Path-H/Path-C Multi-Valued Classification (a) Landing (gated on S87 CF-1, which the S86 closeout map labelled CF-1 but the consolidated `compute-carryforward.md` re-numbers as CF-20) — **CF-20 lands this row at §VII.AC.1**.
- **§VII.AC.4** — DEFERRED V1+C1 Sequential-Chain Derivation of Classification (a) — **CF-20 also lands this row at §VII.AC.4** as the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor block per `.claude/rules/registry-landing.md`.

W3 also builds the BK-Array meta-classifier_v2 (CF-21) as a callable Python API and pre-registers the joint LiteBIRD-LISA 2×2 falsifier suite (CF-22 + CF-23) as a 5-sub-gate sequence covering both axes of W-3's structural-change finding (block-decomposition axis Path-H/Path-C via LiteBIRD n_T discriminator; regulator-class axis (A)/(C) via LISA Ω_GW). The S88+ candidate sub-stubs (CF-24) are pre-scoped placeholders so the S88 plan-author can fill the 4-field specs without further research.

**Substrate framing**: Path-H/Path-C is NOT "two competing low-energy effective field theories of inflation" — it is a multi-valued substrate observable expressing the regulator-class lattice's two-cell decomposition of the same fiber spectrum at τ_fold. Per `.claude/rules/phononic-framing.md`: the substrate IS the spectrum; Path-H is a regulator-class projection of that spectrum onto one cell of the L1↔L3 atlas; Path-C is the projection onto the other cell. r is a substrate-emergent observable computed from spectral moments; the "dual-pathway" structure is intrinsic to the regulator-class lattice (not an external choice). The LiteBIRD n_T discriminator and LISA Ω_GW (A)/(C) discriminator are two independent regulator-axis falsifiers; their joint outcome decomposes into a 2×2 product detector with rank-2 product structure (per S86 W-3 §VII.AC.3 Rank-2 Product Detector Orthogonality Theorem). δ_speed is the asymmetric-inheritance observable (volovik R3-A) that completes the substrate's predictive content for the joint suite.

---

## §0.5. Wave W3 Decision-Point Prerequisites

W3 has **NO HARD execution-time prerequisites on other S87 waves**. Its prerequisites are S86-LANDED registry slots and canonical-constants pins, all settled at S87 plan-freeze (2026-04-27). Plan-write proceeds in parallel with all other S87 waves; dispatch-time is unblocked from S87 plan-freeze onward.

| Prerequisite | Provider gate / location | Required outcome at S87 plan-freeze | Consumer in W3 |
|:-------------|:--------------------------|:-------------------------------------|:---------------|
| §VII.AC top-level row + §VII.AC.1..AC.4 sub-rows allocated | S86 W-3 R3 closeout (`permanent-results-registry.md` lines 86-90) | LANDED — §VII.AC + §VII.AC.1..AC.4 present; .AC.1 + .AC.4 marked DEFERRED awaiting S87 CF-20 | CF-20 (§W3-1) |
| W14-1..W14-5 META verdicts (4 PASS + 1 FAIL diagnostic) | `computations/s86_gate_verdicts.txt` | LANDED — W14-1 (LiteBIRD n_T), W14-2 (Ω_GW), W14-3 (n_s), W14-4 (f_NL^folded), W14-5 (A_s) verdicts on disk | CF-21 (§W3-2 self-test corpus) |
| canonical_constants.py: `c_sub_baseline`, `r_PathH`, `r_PathC`, `n_T_PathH`, `n_T_PathC`, `Omega_GW_FW_S82_equilateral`, `Omega_GW_FW_S67_folded`, `Omega_GW_FW_S85_W9_3_analytic` | `computations/canonical_constants.py` (S86-close state) | LANDED — pathway-keyed Ω_GW pins per W14-4 / W14-5 precedents (canonical write-order Step 2) | CF-22 sub-gates (§W3-3a..§W3-3e) |
| `falsifier-master-inventory.md` Row #2 (Path-H/Path-C r-dual-pathway) + Row #9 (f_NL^folded 2-observable split landed via CF-28 in W4) | `sessions/framework/registry/falsifier-master-inventory.md` | LANDED at S86 close per CF-54 / CF-22 lineage; mack-cosmic-bridge sole writer | CF-22 §W3-3d / §W3-3e joint-suite null-elimination cross-check |
| `.claude/rules/registry-landing.md` SOURCE-DOUBLE-CITE-CO-PRIMARY rule | rule file (S86 W0a-1 promotion) | LANDED — schema + audit pre-registered | CF-20 (§W3-1) registry-entry text |
| `.claude/rules/inheritance-falsifier-protocol.md` four-gate structure | rule file (S86 W-5 promotion) | LANDED — Gate 1/2/3/4 template registered | CF-22 (§W3-3a..§W3-3e) joint suite |
| `.claude/rules/joint-theorem-promotion.md` 4-stage pathway | rule file (S86 W-9 promotion) | LANDED — Stage 0/1/2/3 schema operational | CF-22 §W3-3d Fisher-discount sub-gate (joint LiteBIRD+LISA = cross-axis) |

**Substitution chain — execution-time dependency closure**:
```
Step 1: W3 = {CF-20, CF-21, CF-22 (5 sub-gates incl. CF-23), CF-24 (3 stubs)}
Step 2: requires(CF-20) = {§VII.AC.1 + .AC.4 placeholder slots, registry-landing.md rule}
        requires(CF-21) = {W14-1..W14-5 verdicts, canonical_constants pathway/pivot pins}
        requires(CF-22) = {canonical pathway-keyed Ω_GW pins, n_T pins, falsifier-inventory rows, inheritance-falsifier-protocol.md, joint-theorem-promotion.md}
        requires(CF-24) = {} (stub-only; placeholder 4-field specs)
Step 3: union(requires) ⊆ S86-LANDED state at plan-freeze 2026-04-27.
Step 4: NO inter-wave dependency on other S87 waves. W3 dispatches at any compute-time slot.
        Direction: dispatch-independent of other S87 wave landings.
Conclusion: W3 enters the compute queue at S87 dispatch-time without conditional gating
on other waves. Internal sub-gate ordering: CF-20 → CF-21 → CF-22 (5 sub-gates in lex
order §W3-3a..§W3-3e) → CF-24 (stub-write only, no compute).
```

---

## §I. Carry-Forward Items Mapping

| W3 Item | Carry-Forward ID | Source synthesis | Effort | Level | Sequencing |
|:--------|:------------------|:------------------|:-------|:-----|:-----------|
| §W3-1 CF-20 `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING` | CF-20 (compute-carryforward.md row 20) | S86 W-3 R3-A Convergence #2 (workshop §R3-A lines 2472-2507; §R3-B lines 2840-2879) | ~0.5 wave | PRIORITY 1 | INDEPENDENT — lands at existing §VII.AC.1 + §VII.AC.4 |
| §W3-2 CF-21 `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2` | CF-21 (compute-carryforward.md row 21) | S86 W-3 §VII.AC.3 Rank-2 Product Detector Orthogonality + §VII.AC W14-1..W14-5 META row | ~1 wave (3-4 sub-gates) | PRIORITY 1 | INDEPENDENT — consumes settled W14-1..W14-5 verdicts |
| §W3-3 CF-22 + CF-23 `S87-N-T-CONSISTENCY-AUDIT-LITEBIRD-PLUS-LISA-(C)-NULL` (5 sub-gates §W3-3a..§W3-3e, with CF-23 = §W3-3c) | CF-22 (compute-carryforward.md row 22) + CF-23 (compute-carryforward.md row 23) | S86 W-3 R2-B Sub-claim §σ-reduction structural form + R3-A volovik δ_speed asymmetric-inheritance observation + §VII.AC.3 rank-2 product structure | ~2 waves total (5 sub-gates) | PRIORITY 1 | INDEPENDENT — consumes canonical pathway-keyed pins |
| §W3-4 CF-24 `S87-S88-PLUS-CANDIDATES` (3 stub-substubs: Pati-Salam embedding + EE/BB-T cross-correlation + f_NL^equilateral non-Gaussianity) | CF-24 (compute-carryforward.md row 24) | S86 W-3 R3-B forward-looking note on non-Gaussianity + EE/BB-T direct c_S probe + Pati-Salam B1/B2 partition preservation | ~0.25 wave (placeholder 4-field specs only; no compute at S87) | LEVEL 5 (S88+) | INDEPENDENT — pre-scope only |

CF-23 `S87-DELTA-SPEED-MELLIN-WINDOW` is structurally absorbed into CF-22 as §W3-3c per the spawn prompt's explicit nesting instruction; both gate IDs remain independently verdict-emitted (one verdict line per sub-gate).

---

## §W3-1. CF-20 — `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`

**1. Gate ID**: `S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING`

**2. Trigger**: `[VERIFY]` — registry-landing gate; PASS predicate is artifact-existence-with-substantive-content (the §VII.AC.1 row plus the §VII.AC.4 SOURCE-DOUBLE-CITE-CO-PRIMARY anchor block must be present in `permanent-results-registry.md` with all required schema fields per `.claude/rules/registry-landing.md`). This is a COMPUTE-class gate (not METHODOLOGY-class) because the PASS predicate combines artifact-existence with a numerical verification of the closure-SHA pin — i.e., the registry text must include a 64-char SHA over the W-3 workshop-closure verdict and the audit script verifies it matches the SHA in `s86_gate_verdicts.txt` for the S86 W-3 closure verdict. The gate emits a numerical verdict line.

**3. Classification**: GEOMETRIC — operates on the regulator-class lattice's decomposition of the substrate's fiber spectrum at τ_fold; the multi-valuedness of the Path-H/Path-C observable is a geometric property of the L1↔L3 atlas, not a particle or phononic excitation. Per `.claude/rules/phononic-framing.md` classification guide: "GEOMETRIC = concerns the spectral triple structure, D_K eigenvalues, Jensen deformation, fiber topology — the fabric itself rather than its excitations." The two-cell decomposition is structural geometry of the regulator-class atlas.

**4. Agent type**: `gen-physicist` — this is the agent who authored the W-3 workshop's Convergence #2 (where SOURCE-DOUBLE-CITE-CO-PRIMARY was adopted at R3-A) and owns CF-20. Registry-landing gates with explicit anchor-pair structure are within gen-physicist's cross-domain scope. Fallback specialist if gen-physicist unavailable: `connes-ncg-theorist` (NCG axiomatic side of C1 anchor — Connes 1996 reconstruction + axioms 3+5+6 + Schur orthogonality is Connes-track expertise). Do NOT delegate to `volovik-superfluid-universe-theorist` for landing — Volovik's R2-A V1-PRIMARY framing was REVOKED at R3-A in favor of CO-PRIMARY; the landing must reflect the post-revocation structure.

**5. Hypothesis** (one sentence): The Path-H/Path-C multi-valued classification (a) — Path-H/Path-C as multi-valued substrate observable on the L1↔L3 regulator-class lattice — admits a registry-landed entry at §VII.AC.1 + §VII.AC.4 with SOURCE-DOUBLE-CITE-CO-PRIMARY anchor structure citing V1 (3He-B BDI 0D inheritance arrow) and C1 (Connes 1996 reconstruction + NCG axioms 3+5+6 + Schur orthogonality of A_F = C ⊕ H ⊕ M_3(C)) at co-primary weight, and the closure-SHA pin matches the S86 W-3 workshop-closure verdict SHA in `s86_gate_verdicts.txt`.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_path_h_path_c_registry_landing.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Read S86 W-3 workshop closure verdict line from `computations/s86_gate_verdicts.txt`
  (gate ID: locate the W-3 R3-A Convergence #2 closure verdict; SHA pin is in the
  audit_sha256 field of that verdict line — extract full 64-char form)
- Read existing §VII.AC.1 + §VII.AC.4 placeholder rows from
  `sessions/permanent-results-registry.md` (lines 87, 90 per S87 plan-freeze grep)
- Compose the SOURCE-DOUBLE-CITE-CO-PRIMARY anchor block per
  `.claude/rules/registry-landing.md` Schema:

    §VII.AC.1 PATH-H-PATH-C-MULTI-VALUED-CLASSIFICATION-(a)
      ANCHOR-1 (input layer, V1):
        3He-B BDI 0D inheritance arrow (S58 Volovik-partition canonical;
        canonical_constants.py:1243 w0_FW = -0.918; cross-link to
        sessions/framework/registry/branch-iv-canonical.md §3 substrate-natural
        anchor 59.8 · Δ_BCS / K_base)
      ANCHOR-2 (output layer, C1):
        Connes 1996 reconstruction (Connes "Gravity coupled with matter and
        the foundation of non-commutative geometry", Comm. Math. Phys. 182,
        155-176 (1996)) + NCG axioms 3 (orientability) + 5 (finiteness) +
        6 (real structure J) + Schur orthogonality of A_F = C ⊕ H ⊕ M_3(C)
      STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY
      Derivation chain: V1 (BDI 0D inheritance fixes A_F = C ⊕ H ⊕ M_3(C)
        as the spectral-algebra premise) → A_F (Connes-Chamseddine finite-
        dimensional spectral algebra) → C1 (NCG axioms 3+5+6 + Schur orthog.
        on A_F yield uniqueness of Path-H/Path-C two-cell decomposition) →
        conclusion (Path-H/Path-C is multi-valued substrate observable;
        each cell is a regulator-class projection of the same fiber spectrum)
      Closure SHA pin: <full 64-char audit_sha256 of S86 W-3 R3-A Convergence #2
        closure verdict from s86_gate_verdicts.txt>

    §VII.AC.4 V1-C1-SEQUENTIAL-CHAIN-DERIVATION-OF-CLASSIFICATION-(a)
      [Repeats SOURCE-DOUBLE-CITE-CO-PRIMARY block; this row is the
       per-anchor-rationale companion row, retained as DEFERRED placeholder
       at S86 close and now landed alongside .AC.1.]

- Replace the DEFERRED placeholder text at §VII.AC.1 + §VII.AC.4 with the
  composed block above using append-only Python writer pattern (NOT Edit-tool
  round-trip; per `.claude/rules/epistemic-discipline.md` §"Registry-Write
  Hygiene under Parallel-Writer Race"). Open `permanent-results-registry.md`
  in atomic in-place rewrite mode (read full file, splice replacement at the
  two row positions, atomic-rename).
- Verify post-write: re-read the file; grep for DEFERRED markers in
  §VII.AC.1 / §VII.AC.4 — none should remain.
- Compute content_sha256 over the new registry block (the §VII.AC.1 + §VII.AC.4
  row text concatenated).
- Compute audit_sha256 = closure_hash(input_pin_map) where input_pin_map =
  {plan_block_sha256, registry_landing_rule_sha256, s86_workshop_closure_sha256,
   workshop_closure_audit_sha256, gate_id, scheme, convention, L_max} per
  `computations/script-template.py append_verdict()` pattern.

GPU: NOT NEEDED (registry-write gate; no eigenvalue computation).
CPU fallback: cap `OMP_NUM_THREADS = 8` if any numpy ops execute.

Outputs:
- `computations/s87_w3_path_h_path_c_registry_landing.npz`
  (closure_sha records, post-write registry-block byte length, both anchor
  citation strings as np.bytes_ for audit-trail provenance)
- `computations/s87_w3_path_h_path_c_registry_landing.json`
  (verdict 4-tuple + dual-SHA + registry-landing diagnostic — placeholder
  removal confirmed True/False, anchor-block character count, structure-tag
  presence True/False)
- (NO .png — registry-landing gate has no plot)

Verdict line append to `computations/s87_gate_verdicts.txt`:
S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING: <PASS|FAIL|INFO> -- value=<bool_5_criteria_met> scheme=registry-landing convention=SOURCE-DOUBLE-CITE-CO-PRIMARY L_max=N/A audit_sha256=<64-hex> content_sha256=<64-hex> schema_version=S84+

Dual-SHA companion comment row:
# audit_sha256_short=<16-hex> content_sha256_short=<16-hex> # S87-PATH-H-PATH-C-MULTI-VALUED-REGISTRY-LANDING dual-SHA companion row (W9a-99 split)

(NO 3-tuple SIGN/MAGNITUDE/REGIME row — this is a [VERIFY] artifact-existence
gate, not a [SIGN] gate; sign_verdict=N/A.)
```

**7. Machinery pin (PRDR)**:
- `L_max`: N/A (registry-landing gate; no spectral evaluation at L_max axis)
- `scheme`: `registry-landing`
- `convention`: `SOURCE-DOUBLE-CITE-CO-PRIMARY`
- `n_eval`: 5 (5 PASS criteria — see §9 below: placeholder removed; both anchors present; STRUCTURE tag present; closure SHA matches S86 W-3 closure; rule schema match)
- `scan_range`: N/A
- `step_size`: N/A
- `tolerance`: N/A (boolean PASS criteria; no numerical tolerance band)
- `random_seed`: N/A (deterministic file rewrite)
- `GPU path`: NOT USED
- `cutoff_axis`: N/A (registry-landing gate; not a spectral computation)
- `regulator_pin_tag`: N/A (no a_n citations in this gate)
- `verifier_rubric_pre_registration`: REQUIRED — anchor-block must contain literal strings: "ANCHOR-1 (input layer, V1)", "ANCHOR-2 (output layer, C1)", "STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY", "Derivation chain:", "Closure SHA pin:". Disjunction: NONE; ALL 5 strings required (conjunction). Negative-marker set: literal "DEFERRED" string MUST NOT appear in §VII.AC.1 or §VII.AC.4 rows post-write. Calibration corpus pinned by S86 W-3 R3-A Convergence #2 verdict SHA.

**8. Expected output 4-tuple**:
`(value=<bool_all_5_PASS_criteria_met>, scheme=registry-landing, convention=SOURCE-DOUBLE-CITE-CO-PRIMARY, L_max=N/A)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS** (all 5 criteria met):
  (a) §VII.AC.1 + §VII.AC.4 placeholder DEFERRED markers REMOVED post-write
  (b) ANCHOR-1 (V1: 3He-B BDI 0D inheritance arrow) text present in both rows
  (c) ANCHOR-2 (C1: Connes 1996 + NCG axioms 3+5+6 + Schur orthogonality) text present
  (d) STRUCTURE: SOURCE-DOUBLE-CITE-CO-PRIMARY tag present
  (e) Closure SHA pin matches the full 64-char audit_sha256 of the S86 W-3 R3-A Convergence #2 closure verdict in `s86_gate_verdicts.txt`
- **FAIL** (any of (a)-(e) missing): the registry landing is incomplete
- **INFO** (criteria (a)-(d) met but (e) SHA mismatch within first 32 chars only): provisional landing flagged for SHA reconciliation; the §VII.AC entry is text-complete but the audit-trail closure pin needs follow-up reconciliation in S88+
- **Tolerance rule**: THEOREM (boolean PASS predicate; no numerical tolerance band)

**10. Substitution chain** (closure-SHA-match direction):
```
Step 1 (definitions):
  registry_text(post)   = the §VII.AC.1 + §VII.AC.4 block as written by this gate
  pin_SHA               = the audit_sha256 string composed into "Closure SHA pin: <pin_SHA>"
  ws_closure_SHA        = the audit_sha256 of the S86 W-3 R3-A Convergence #2 verdict
                          line in computations/s86_gate_verdicts.txt
  PASS_criterion_(e)    = (pin_SHA == ws_closure_SHA) as 64-char hex strings (case-fold)

Step 2 (substitute):
  PASS_criterion_(e) ⇔ (lowercase_hex(pin_SHA) == lowercase_hex(ws_closure_SHA))
                       AND len(pin_SHA) == 64

Step 3 (simplify; no algebra collapse):
  PASS_criterion_(e) is a boolean string-equality; no arithmetic.

Step 4 (direction):
  IF the gate's input-pin map embeds ws_closure_SHA verbatim (no truncation,
  no copy-paste error), THEN pin_SHA == ws_closure_SHA structurally
  (the gate writes the SHA it reads).
  Direction: PASS if and only if the read-write pipeline preserves the SHA bytes.
  No sign claim; this is a structural identity check.

Conclusion: criterion (e) PASSes by construction provided the script reads
ws_closure_SHA from s86_gate_verdicts.txt with exact-match parsing
(no head-truncation; no \n stripping that drops trailing chars), and writes
it verbatim into the Closure SHA pin field. FAIL on (e) indicates an I/O bug
in the read-write pipeline, not a physics defect.
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: the §VII.AC.1 + §VII.AC.4 sub-rows are LANDED PERMANENTLY in `permanent-results-registry.md`. The Path-H/Path-C multi-valued classification (a) becomes a citable structural result of the framework. Future falsifier-design rows in `falsifier-master-inventory.md` can cite §VII.AC.1 as the registry anchor for the dual-pathway structure rather than the now-superseded W-3 workshop-internal text. The SOURCE-DOUBLE-CITE-CO-PRIMARY anchor pattern is calibrated for use in any future cross-axis sequential-chain landings (per `.claude/rules/registry-landing.md` calibration corpus extension).
- **FAIL**: the landing is incomplete and §VII.AC.1 + §VII.AC.4 stay marked DEFERRED. CF-20 carries forward to S88. Downstream consumers (CF-22 §W3-3, falsifier-master-inventory Row #2) keep citing the W-3 workshop-internal text rather than a registry-anchored row, weakening audit provenance.
- **INFO**: text content lands but closure SHA reconciliation needs follow-up — likely a read-pipeline defect in extracting the W-3 workshop closure SHA from `s86_gate_verdicts.txt`. S88 carry-forward CF-20-FOLLOWUP fixes the read-pipeline and re-emits the verdict line; the §VII.AC.1 + §VII.AC.4 text content remains valid in the interim.

**12. Effort estimate**: ~0.5 wave (~3-5 hours). Light because the registry text is mostly composed from existing W-3 workshop-closure citations + the explicit anchor strings the spawn prompt provides; the only computational work is the closure-SHA match check and the atomic file rewrite. Heavy-side risk: parallel-writer race if mack-cosmic-bridge is concurrently writing to `permanent-results-registry.md` (mitigation: use append-only Python writer pattern + scan-ALL-header-levels rule per `.claude/rules/epistemic-discipline.md` §"Registry-Write Hygiene under Parallel-Writer Race").

**13. Substrate-framing reminder**: The Path-H/Path-C structure is NOT "two competing inflationary models" — it is a multi-valued substrate observable. State the registry-landing as: **"The substrate's regulator-class lattice exhibits a two-cell decomposition (Path-H, Path-C) of the L1↔L3 atlas; the multi-valued classification (a) is a structural property of the substrate's fiber spectrum at τ_fold, derived from the V1 3He-B BDI 0D inheritance arrow (which fixes A_F = C ⊕ H ⊕ M_3(C) as the spectral-algebra premise) followed by the C1 NCG-axiomatic uniqueness theorem (Connes 1996 + axioms 3+5+6 + Schur orthogonality)."** Avoid framing as "two effective theories of inflation" or "two phenomenological choices" — the substrate is logically prior; the dual-pathway is structural geometry of the regulator-class lattice, not a phenomenological alternative.

---

## §W3-2. CF-21 — `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2`

**1. Gate ID**: `S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2`

**2. Trigger**: `[VERIFY]` — callable Python module build with self-test gate. PASS predicate combines (a) module file existence at `computations/_meta_classifier_v2.py` with substantive callable API (`classify_outcome(litebird_n_T, lisa_omega_GW, regulator_class) -> dict`), (b) self-test correctness on the W14-1..W14-5 verdict corpus (all 5 verdicts must classify into the pre-registered 4-outcome decision matrix without raising exceptions), and (c) regression test on a synthetic 4-outcome corpus (4 manufactured input tuples, one per cell of the decision matrix, must round-trip through the classifier with cell-label match).

**3. Classification**: GEOMETRIC — the meta-classifier is a structural decoder of the substrate's regulator-class lattice into the 2×2 product detector (Path-H/Path-C × (A)/(C)) per S86 W-3 §VII.AC.3 Rank-2 Product Detector Orthogonality Theorem. The classifier's outcome cells are geometric labels of the substrate's two-axis regulator-class structure, not particle properties. PARTICLE classification rejected: the classifier consumes substrate-emergent observables (n_T, Ω_GW) but produces a regulator-class label, not a particle/excitation observable.

**4. Agent type**: `gen-physicist` — owner of CF-21 per partition manifest. The classifier-build is cross-domain (Python module engineering + W-3 workshop's classification logic + regulator-class taxonomy) and benefits from cross-domain breadth. Fallback: `connes-ncg-theorist` (the C1 anchor's NCG-axiomatic side reproduces the four-outcome structure if the gen-physicist build hits a domain-specific blocker; Connes-Chamseddine M2-axiom side fixes the regulator-class taxonomy). Do NOT delegate to `mack-cosmic-bridge` — mack is the falsifier-master-inventory writer (per `feedback_mack-bridge-role.md`) and should not own the classifier itself.

**5. Hypothesis** (one sentence): A four-outcome callable Python meta-classifier_v2 with API `classify_outcome(litebird_n_T: float, lisa_omega_GW: float, regulator_class: Literal['(A)','(C)']) -> dict` correctly partitions the W14-1..W14-5 verdict corpus into the pre-registered 4-outcome decision matrix {PASS-PathH-(A), PASS-PathH-(C), PASS-PathC-(A), PASS-PathC-(C)} without raising exceptions, AND a synthetic 4-outcome regression corpus (4 manufactured cell-canonical tuples, one per cell) round-trips through the classifier with cell-label match for all 4.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_bk_array_meta_classifier_v2.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- BUILD STEP: write `computations/_meta_classifier_v2.py` (the callable module)
  exposing:
    def classify_outcome(litebird_n_T: float,
                         lisa_omega_GW: float,
                         regulator_class: str  # '(A)' or '(C)'
                         ) -> dict:
        # Returns: {'cell': <str: PASS-PathH-(A)|PASS-PathH-(C)|PASS-PathC-(A)|PASS-PathC-(C)|FAIL-no-cell-match>,
        #           'block_axis': <str: 'Path-H'|'Path-C'|'undecided'>,
        #           'regulator_axis': <str: '(A)'|'(C)'>,
        #           'block_axis_evidence': <float: log-likelihood ratio>,
        #           'rationale': <str: human-readable per-axis decision trace>}
- Decision matrix (pre-registered 4-outcome):
    Block axis (LiteBIRD n_T discriminator):
      Path-H if n_T ∈ [n_T_PathH - 0.5*sigma_n_T_LiteBIRD, n_T_PathH + 0.5*sigma_n_T_LiteBIRD]
      Path-C if n_T ∈ [n_T_PathC - 0.5*sigma_n_T_LiteBIRD, n_T_PathC + 0.5*sigma_n_T_LiteBIRD]
      undecided otherwise (LLR within 1.5 of zero)
    Regulator axis (LISA Ω_GW × regulator_class label):
      (A) if regulator_class == '(A)' AND Ω_GW within 0.5 OOM of Ω_GW_FW_(A) canonical pin
      (C) if regulator_class == '(C)' AND Ω_GW within 0.5 OOM of Ω_GW_FW_(C) canonical pin
      undecided otherwise
- The four-cell product is the 2×2 product detector per §VII.AC.3.
- Pull canonical pins from canonical_constants.py:
    n_T_PathH, n_T_PathC, sigma_n_T_LiteBIRD,
    Omega_GW_FW_S82_equilateral, Omega_GW_FW_S67_folded,
    Omega_GW_FW_S85_W9_3_analytic_template,
    Omega_GW_C_FW (Sage-exact 8.299e-58 per W13-2.Ω verdict; round-figure 1e-57 FORBIDDEN per regulator-pin-discipline.md §"Sage-Exact Rationals for Ω_GW Regulator-Class Values")
- SELF-TEST 1 (W14 verdict corpus reproduction):
    Read W14-1..W14-5 verdicts from computations/s86_gate_verdicts.txt;
    for each verdict, extract (n_T_value, Ω_GW_value, regulator_class_label) tuple
    where reportable; classify; assert classification does not raise + cell label
    is one of the 5 enum values.
    Record pass count out of 5.
- SELF-TEST 2 (synthetic 4-cell regression):
    Construct 4 cell-canonical tuples (one per cell) using the canonical pins;
    classify each; assert cell label round-trips. Record pass count out of 4.
- AGGREGATE PASS criterion: SELF-TEST 1 = 5/5 AND SELF-TEST 2 = 4/4.

GPU: NOT NEEDED (classifier is pure-Python branching logic; no eigvals/SVD).

Outputs:
- `computations/_meta_classifier_v2.py` (the callable module — must exist
  post-run; size > 2 KB substantive content)
- `computations/s87_w3_bk_array_meta_classifier_v2.npz` (self-test results
  array, 9 outcomes total: 5 W14 + 4 synthetic)
- `computations/s87_w3_bk_array_meta_classifier_v2.json` (verdict 4-tuple
  + per-self-test pass diagnostic)
- (NO .png — classifier-build gate; no plot)

Verdict line:
S87-BK-ARRAY-JOINT-META-CLASSIFIER-V2: <PASS|FAIL|INFO> -- value=<int: aggregate_pass_count_out_of_9> scheme=meta-classifier-v2-build convention=BK-Array-2x2-product-detector L_max=N/A audit_sha256=<64> content_sha256=<64> schema_version=S84+

Dual-SHA companion row + (NO 3-tuple SIGN/MAGNITUDE/REGIME row — [VERIFY] gate).
```

**7. Machinery pin (PRDR)**:
- `L_max`: N/A (classifier-build gate; no spectral evaluation)
- `scheme`: `meta-classifier-v2-build`
- `convention`: `BK-Array-2x2-product-detector` (§VII.AC.3 rank-2 product structure)
- `n_eval`: 9 (5 W14 corpus + 4 synthetic regression)
- `scan_range`: N/A
- `step_size`: N/A
- `tolerance`: 0.5σ for n_T LiteBIRD discriminator band; 0.5 OOM for LISA Ω_GW band; 1.5 LLR for "undecided" zone
- `random_seed`: 42 (for any synthetic-corpus generation; deterministic per seed)
- `GPU path`: NOT USED
- `cutoff_axis`: N/A
- `regulator_pin_tag`: N/A
- `verifier_rubric_pre_registration`: REQUIRED — module file must contain literal strings: `def classify_outcome(`, `'cell':`, `'block_axis':`, `'regulator_axis':`, `'rationale':`, `PASS-PathH-(A)`, `PASS-PathH-(C)`, `PASS-PathC-(A)`, `PASS-PathC-(C)`. Conjunction (ALL 9 required); module is rejected as stub if fewer than 9 are present.
- `module_substantive_content_floor`: 2 KB minimum file size for the classifier module — stub modules fail the M1 artifact-existence-with-substantive-content predicate.

**8. Expected output 4-tuple**:
`(value=<aggregate_pass_count_out_of_9>, scheme=meta-classifier-v2-build, convention=BK-Array-2x2-product-detector, L_max=N/A)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS** (aggregate = 9/9): SELF-TEST 1 returns 5/5 W14 corpus pass AND SELF-TEST 2 returns 4/4 synthetic regression pass
- **FAIL** (aggregate ≤ 6/9 OR module file < 2 KB OR module missing any of the 9 required literal strings): classifier build is structurally incomplete
- **INFO** (aggregate = 7/9 or 8/9): partial success — flag which sub-test cell failed and document for S88 follow-up; the classifier API exists and is structurally complete but a particular cell's threshold may need recalibration
- **Tolerance rule**: THEOREM (boolean per-test PASS; no fractional tolerance)
- **Sub-gate decomposition** (3 sub-gates per spawn prompt's §"3-4 sub-gates" specification):
  - §W3-2a: module file build + import-test (1 PASS criterion)
  - §W3-2b: SELF-TEST 1 W14 corpus reproduction (5 PASS criteria)
  - §W3-2c: SELF-TEST 2 synthetic 4-cell regression (4 PASS criteria)
  - Aggregate of 1 + 5 + 4 = 10 sub-criteria, of which the verdict reports the 9 W14+synthetic outcomes (the import-test is a precondition, not a counted criterion)

**10. Substitution chain** (decision matrix direction):
```
Step 1 (definitions):
  block_axis(n_T)       = Path-H  if |n_T - n_T_PathH| < 0.5 * sigma_n_T_LiteBIRD
                          Path-C  if |n_T - n_T_PathC| < 0.5 * sigma_n_T_LiteBIRD
                          undecided  otherwise
  regulator_axis(Ω,r)   = (A)  if r == '(A)' AND |log10(Ω) - log10(Ω_GW_FW_(A))| < 0.5
                          (C)  if r == '(C)' AND |log10(Ω) - log10(Ω_GW_FW_(C))| < 0.5
                          undecided  otherwise
  cell(n_T, Ω, r)       = PASS-{block_axis(n_T)}-{regulator_axis(Ω,r)} if both decisive
                          FAIL-no-cell-match  otherwise

Step 2 (substitute the synthetic-corpus PASS test):
  For (n_T_PathH, Ω_GW_FW_(A), '(A)'):
    block_axis = Path-H (by construction; |n_T_PathH - n_T_PathH| = 0 < 0.5*σ)
    regulator_axis = (A) (by construction; log-diff = 0 < 0.5 OOM)
    cell = PASS-PathH-(A)  ✓ matches expected
  Similarly for the other 3 cells.

Step 3 (simplify):
  Synthetic round-trip PASS reduces to: each manufactured tuple's expected cell
  label is identical to classify_outcome(...)['cell']. By construction (the
  synthetic corpus is built FROM the canonical pins the classifier reads),
  round-trip is structurally guaranteed if the classifier's branching logic
  is correctly implemented.

Step 4 (direction):
  IF the classifier's branching logic correctly tests both axes (Path-H/Path-C
  via n_T discriminator AND (A)/(C) via Ω_GW discriminator + regulator_class
  label), THEN synthetic round-trip = 4/4. Direction: PASS-by-construction
  conditional on correct branching implementation. FAIL on synthetic indicates
  a logic bug in the classifier (off-by-one band, wrong canonical pin, or wrong
  conjunction order).

Conclusion: synthetic-corpus PASS is structurally guaranteed conditional on
correct implementation; W14-corpus PASS is the empirical test of whether the
S86 W14-1..W14-5 results land cleanly inside the 4-cell decomposition (some
W14 verdicts may carry undecided block-axis or regulator-axis if their
reportable n_T/Ω_GW values do not satisfy the 0.5σ / 0.5 OOM bands).
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS** (9/9): meta-classifier_v2 is a callable Python API ready for downstream consumption by CF-22 §W3-3 sub-gates and any future S88+ joint LiteBIRD-LISA falsifier-design gates. The 4-cell decomposition is empirically demonstrated to span the W14 verdict corpus (5/5) and synthetic regression-corpus round-trip (4/4). The framework's r-Dual-Pathway joint classifier is operational at module level.
- **FAIL** (≤ 6/9): the classifier is structurally incomplete; the 4-cell decomposition does not span the actual S86 W14 outcomes. CF-21 carries forward to S88 with the per-cell-failure diagnostic guiding the next-iteration band recalibration.
- **INFO** (7/9 or 8/9): classifier is mostly operational with one or two cell-band edge cases requiring recalibration. The module is usable for downstream consumers but flagged for S88 cell-band recalibration. CF-22 §W3-3 sub-gates may proceed but should report any classifier-driven decision they consume as "v2-with-band-INFO" until S88 closes the recalibration.

**12. Effort estimate**: ~1 wave (3 sub-gates: §W3-2a module build ~2h, §W3-2b W14 self-test ~3h, §W3-2c synthetic regression ~2h). Heavy-side risk: the W14-1..W14-5 verdict format may not directly expose (n_T, Ω_GW, regulator_class) tuples — extracting them may require reading the W14 .npz files or working-paper sections beyond the verdict line; mitigation is to fall back to placeholder INFO on §W3-2b if the W14 corpus extraction blocks within first attempt and re-emit in S88 once W14 verdict format is regularized.

**13. Substrate-framing reminder**: The meta-classifier_v2 is a structural decoder of the substrate's regulator-class lattice into a 2×2 product detector — NOT a "phenomenological pipeline that maps inflation-model parameters to observational signatures." State as: **"The classifier reads two substrate-emergent observables (LiteBIRD-measured n_T, LISA-measured Ω_GW) and one regulator-class label, and decodes them into the substrate's regulator-class-lattice cell label per the §VII.AC.3 Rank-2 Product Detector Orthogonality Theorem. The substrate IS the 2×2 product structure; the classifier reads off which cell of the product the substrate's spectral observables land in."** Do not frame as "we predict observations from a model"; the substrate-side IS the spectrum, the lab-side measures, the classifier names which cell of the substrate's regulator-class lattice the lab-measurement places us in.

---

## §W3-3. CF-22 + CF-23 — `S87-N-T-CONSISTENCY-AUDIT-LITEBIRD-PLUS-LISA-(C)-NULL` (5 sub-gates)

**Top-level Gate ID**: `S87-N-T-CONSISTENCY-AUDIT-LITEBIRD-PLUS-LISA-(C)-NULL`

This top-level gate is a **5-sub-gate suite** per `.claude/rules/inheritance-falsifier-protocol.md` four-gate-structure plus the δ_speed sub-gate (CF-23). Each sub-gate gets its own gate ID, its own verdict line, and its own working-paper sub-section. The aggregate verdict at the top-level is the AND-conjunction of the 5 sub-gates.

**Sub-gate decomposition**:

| Sub-gate | Gate ID | Provenance | Effort |
|:---------|:---------|:-----------|:-------|
| §W3-3a (Gate 1, kernel-signature decisive) | `S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR` | inheritance-falsifier-protocol.md Gate 1 + S86 W-3 R3-A LiteBIRD discriminator | ~3h |
| §W3-3b (Gate 1, kernel-signature decisive — second axis) | `S87-W3-3B-LISA-OMEGA-GW-A-C-REGULATOR-CLASS-DISCRIMINATOR` | inheritance-falsifier-protocol.md Gate 1 (second axis) + S86 W-3 R3-A LISA Ω_GW (A)/(C) split | ~3h |
| §W3-3c (CF-23: δ_speed asymmetric inheritance) | `S87-DELTA-SPEED-MELLIN-WINDOW` | volovik R3-A asymmetric-inheritance observation; CF-23 explicit | ~3h |
| §W3-3d (Gate 2, cohomology-asymmetry; joint Fisher-discount) | `S87-W3-3D-JOINT-LITEBIRD-LISA-FISHER-DISCOUNT` | inheritance-falsifier-protocol.md Gate 2 cohomology-asymmetry + joint-theorem-promotion.md cross-axis Fisher | ~4h |
| §W3-3e (Gate 4, slope-discrimination; null-elimination cross-check) | `S87-W3-3E-LITEBIRD-LISA-NULL-ELIMINATION-CROSS-CHECK` | inheritance-falsifier-protocol.md Gate 4 slope-discrimination + S86 W-3 R3-B null-elimination R-row | ~3h |

(Gate 3 in the inheritance-falsifier-protocol.md template — kernel-signature SUPPORTING — is structurally absorbed into §W3-3a + §W3-3b above; the LiteBIRD and LISA axes are both decisive in this 2-axis substrate, so the supporting/decisive split degenerates.)

Per `.claude/rules/agent-standards.md` §"HIGH-DENSITY WORKSHOP TEMPLATE", this top-level gate produces multiple structural outputs (one per sub-gate) and the literal pre-registration is decomposed across 5 OUTPUT slots, not forced into a single PASS/FAIL/INFO at the top level.

---

### §W3-3a. `S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR`

**1. Gate ID**: `S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR`

**2. Trigger**: `[VERIFY]` — pre-registration of LiteBIRD n_T discriminator between Path-H and Path-C predictions; PASS predicate is that the substrate-derived n_T_PathH and n_T_PathC predictions are separated by ≥ 1.0σ at LiteBIRD's projected sensitivity (sigma_n_T_LiteBIRD per canonical_constants.py), with the discriminator margin substituted explicitly per the substitution chain.

**3. Classification**: GEOMETRIC — n_T is a substrate-emergent observable; the discriminator is a structural property of the regulator-class lattice's two-cell decomposition. The LiteBIRD measurement IN the lab is a continuum-image projection of the substrate-IS observable per `.claude/rules/cross-pillar-bridge-anatomy.md` IS-not-IN convention.

**4. Agent type**: `gen-physicist`. Fallback: `mack-cosmic-bridge` (Mack is the framework's observational priorities owner; LiteBIRD is in his portfolio per `feedback_mack-bridge-role.md`). Mack-fallback is operationally clean because §W3-3a's discriminator margin is an n_T pre-registration ahead of LiteBIRD data — exactly Mack's role.

**5. Hypothesis**: The substrate's two-cell decomposition predicts |n_T_PathH − n_T_PathC| ≥ 1.0 · sigma_n_T_LiteBIRD where sigma_n_T_LiteBIRD is the canonical LiteBIRD n_T sensitivity from `canonical_constants.py`.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_3a_litebird_n_T_discriminator.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Pull canonical pins:
    n_T_PathH, n_T_PathC, sigma_n_T_LiteBIRD
- Compute discriminator margin:
    margin_sigma = |n_T_PathH - n_T_PathC| / sigma_n_T_LiteBIRD  # (local)
- PASS criterion: margin_sigma >= 1.0
- INFO band: 0.5 <= margin_sigma < 1.0 (sub-σ separation; LiteBIRD stretched-goal regime)
- FAIL: margin_sigma < 0.5 (axis cannot discriminate)

GPU: NOT NEEDED (scalar arithmetic).

Outputs:
- s87_w3_3a_litebird_n_T_discriminator.npz (margin_sigma, both n_T values, sigma)
- s87_w3_3a_litebird_n_T_discriminator.png (histogram-style bar showing
  n_T_PathH ± sigma vs n_T_PathC ± sigma; shaded LiteBIRD sensitivity band)
- s87_w3_3a_litebird_n_T_discriminator.json (verdict 4-tuple + margin_sigma)

Verdict line:
S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR: <PASS|FAIL|INFO> -- value=<margin_sigma> scheme=LiteBIRD-n_T convention=Path-H-vs-Path-C-block-axis L_max=N/A audit_sha256=<64> content_sha256=<64> schema_version=S84+

S87 schema-v2 3-tuple companion row:
# sign_verdict=<PASS|FAIL|N/A> magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=VALID # S87-W3-3A-LITEBIRD-N-T-PATH-H-PATH-C-DISCRIMINATOR 3-tuple annotation (S87 schema-v2)
```

**7. Machinery pin (PRDR)**:
- `L_max`: N/A
- `scheme`: `LiteBIRD-n_T`
- `convention`: `Path-H-vs-Path-C-block-axis`
- `n_eval`: 1 (single discriminator margin)
- `scan_range`: N/A
- `step_size`: N/A
- `tolerance`: PASS at margin_sigma ≥ 1.0; INFO band [0.5, 1.0); FAIL at margin_sigma < 0.5
- `random_seed`: N/A
- `GPU path`: NOT USED
- `cutoff_axis`: N/A
- `regulator_pin_tag`: N/A
- `publication_precision_pin`: 4 sig figs on margin_sigma per `.claude/rules/epistemic-discipline.md` §"Publication-Precision Pre-Registration"; downstream verifier rel_tol ≥ 1e-4

**8. Expected output 4-tuple**:
`(value=<margin_sigma>, scheme=LiteBIRD-n_T, convention=Path-H-vs-Path-C-block-axis, L_max=N/A)`

**9. PASS/FAIL/INFO thresholds**: PASS at margin_sigma ≥ 1.0; INFO at margin_sigma ∈ [0.5, 1.0); FAIL at margin_sigma < 0.5. Tolerance rule: ABSOLUTE on margin_sigma.

**10. Substitution chain**:
```
Step 1 (definitions):
  n_T_PathH         = canonical pin for tensor spectral index, Path-H regulator-class projection
  n_T_PathC         = canonical pin for tensor spectral index, Path-C regulator-class projection
  sigma_n_T_LB      = canonical pin for LiteBIRD projected n_T sensitivity (1σ width)
  margin_sigma      = |n_T_PathH - n_T_PathC| / sigma_n_T_LB

Step 2 (substitute):
  PASS_a ⇔ |n_T_PathH - n_T_PathC| / sigma_n_T_LB >= 1.0
         ⇔ |n_T_PathH - n_T_PathC| >= sigma_n_T_LB

Step 3 (simplify; canonical form):
  PASS ⇔ "Path-H/Path-C predicted separation in n_T space exceeds 1σ of LiteBIRD's
          projected sensitivity" — direct distance comparison in the n_T axis units
          of LiteBIRD's noise.

Step 4 (direction):
  IF |n_T_PathH - n_T_PathC| > sigma_n_T_LB  THEN axis CAN discriminate (margin > 1σ)
  IF |n_T_PathH - n_T_PathC| < sigma_n_T_LB  THEN axis CANNOT discriminate decisively
                                                  (sub-σ; INFO or FAIL)
  Direction: positive direction = wider Path-H/Path-C separation, more decisive axis.
  Sign of (n_T_PathH - n_T_PathC) is NOT load-bearing here — only |·|.

Conclusion: PASS direction is "absolute n_T separation exceeds LiteBIRD 1σ floor".
The substitution chain is on |n_T_PathH - n_T_PathC|, not on n_T values themselves;
no sign claim on the difference. sign_verdict for the verdict line: N/A
(no signed-direction prediction); magnitude_verdict tracks the PASS/FAIL/INFO band.
```

**11. What PASSES/FAILS MEAN for solution space**: PASS pre-registers LiteBIRD as a decisive axis for Path-H/Path-C discrimination; the lab-side measurement, when delivered, will close the block-axis. FAIL means LiteBIRD lacks resolving power for this axis; the falsifier suite degrades to a 1-axis (regulator-class only) detector; need alternative block-axis discriminator (BICEP/CMB-S4 EE/BB-T cross at higher modes — folded into CF-24 sub-stub). INFO band: the stretched-LiteBIRD-goal regime is informative but conditional on detector performance exceeding nominal; flag for re-evaluation post-LiteBIRD launch.

**12. Effort estimate**: ~3 hours.

**13. Substrate-framing reminder**: n_T is a substrate-emergent observable derived from spectral moments at τ_fold. The "discriminator margin" measures how well the lab-IN measurement (LiteBIRD's projected n_T) can resolve the substrate-IS two-cell decomposition. Direction of explanation flows substrate → bridge map → lab.

---

### §W3-3b. `S87-W3-3B-LISA-OMEGA-GW-A-C-REGULATOR-CLASS-DISCRIMINATOR`

**1. Gate ID**: `S87-W3-3B-LISA-OMEGA-GW-A-C-REGULATOR-CLASS-DISCRIMINATOR`

**2. Trigger**: `[VERIFY]` — second-axis pre-registration of LISA Ω_GW (A)/(C) regulator-class split discriminator. PASS predicate: log10(Ω_GW_FW_(A) / Ω_GW_FW_(C)) ≥ Δ_LISA_OOM_floor where Δ_LISA_OOM_floor = 1.0 (1 OOM separation between (A) and (C) is the LISA-decisive floor; the W-3 workshop established the (A)/(C) split is ~47 OOM Sage-exact, which is overwhelmingly above 1 OOM).

**3. Classification**: GEOMETRIC — Ω_GW is a substrate-emergent observable; the (A)/(C) regulator-class split is structural geometry of the regulator-class atlas.

**4. Agent type**: `gen-physicist`. Fallback: `mack-cosmic-bridge` (LISA is in Mack's observational priorities portfolio).

**5. Hypothesis**: The substrate's regulator-class atlas predicts |log10(Ω_GW_FW_(A) / Ω_GW_FW_(C))| ≥ 1.0 OOM, i.e., LISA's frequency-domain sensitivity discriminates between the (A) and (C) regulator-class sub-cones.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_3b_lisa_omega_gw_a_c_discriminator.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Pull canonical pins (Sage-exact rationals per `.claude/rules/regulator-pin-discipline.md`
  §"Sage-Exact Rationals for Ω_GW Regulator-Class Values"):
    Omega_GW_FW_(A)_canonical, Omega_GW_FW_(C)_canonical (= 8.299e-58 per W13-2.Ω verdict;
    NOT round-figure 1e-57)
- Pull LISA sensitivity canonical: Omega_GW_LISA_floor (LISA design-sensitivity floor at
  pivot frequency from canonical_constants.py)
- Compute split:
    split_OOM = log10(Omega_GW_FW_(A) / Omega_GW_FW_(C))  # (local)
- PASS criterion: |split_OOM| >= 1.0
  (W-3 workshop established ~47 OOM; the floor of 1 OOM is heavily satisfied at PASS-by-
   structural-margin)
- INFO band: 0.5 <= |split_OOM| < 1.0
- FAIL: |split_OOM| < 0.5

GPU: NOT NEEDED (scalar arithmetic; Sage-exact rational division).

Outputs:
- s87_w3_3b_lisa_omega_gw_a_c_discriminator.npz (split_OOM exact + float64 image)
- s87_w3_3b_lisa_omega_gw_a_c_discriminator.png (LISA strain-sensitivity band
  with both Ω_GW_(A) and Ω_GW_(C) overlays; log-y axis)
- s87_w3_3b_lisa_omega_gw_a_c_discriminator.json (verdict 4-tuple)

Verdict line + 3-tuple companion row.
```

**7. Machinery pin (PRDR)**:
- `L_max`: N/A
- `scheme`: `LISA-Ω_GW`
- `convention`: `(A)-vs-(C)-regulator-class-split`
- `n_eval`: 1
- `tolerance`: PASS at |split_OOM| ≥ 1.0; INFO [0.5, 1.0); FAIL < 0.5
- `regulator_pin_tag`: N/A (Ω_GW is substrate-emergent observable, not Seeley-DeWitt coefficient)
- `Omega_GW_sage_exact_required`: TRUE (per regulator-pin-discipline.md extension; round-figure substitution FORBIDDEN)
- `publication_precision_pin`: 4 sig figs on split_OOM; full float64 in .npz

**8. Expected output 4-tuple**: `(value=<split_OOM_abs>, scheme=LISA-Ω_GW, convention=(A)-vs-(C)-regulator-class-split, L_max=N/A)`

**9. PASS/FAIL/INFO thresholds**: PASS at |split_OOM| ≥ 1.0; INFO at [0.5, 1.0); FAIL < 0.5. Tolerance: ABSOLUTE on |split_OOM|.

**10. Substitution chain**:
```
Step 1 (definitions):
  Ω_(A)         = canonical Sage-exact rational, Ω_GW prediction under regulator class (A)
  Ω_(C)         = canonical Sage-exact rational, Ω_GW prediction under regulator class (C)
                  (= 8.299e-58 per W13-2.Ω; round-figure 1e-57 FORBIDDEN)
  split_OOM     = log10(Ω_(A) / Ω_(C))

Step 2 (substitute):
  PASS ⇔ |log10(Ω_(A) / Ω_(C))| >= 1.0
       ⇔ Ω_(A) / Ω_(C) >= 10  OR  Ω_(A) / Ω_(C) <= 1/10

Step 3 (simplify):
  PASS ⇔ at least 1 OOM separation in either direction.

Step 4 (direction):
  W-3 workshop established the (A) >> (C) ordering with split_OOM ≈ +47.
  IF Ω_(A) / Ω_(C) ≈ 10^47 THEN |split_OOM| = 47 >> 1.0; PASS by huge margin.
  Direction: W-3 prediction is split_OOM > 0 (specifically ≈ +47); sign is
  load-bearing for the (A)-larger-than-(C) interpretation.
  Sign verdict: PASS (predicted direction split_OOM > 0 matches Sage-computed direction).

Conclusion: PASS direction is "Ω_(A) exceeds Ω_(C) by ≥ 1 OOM"; the canonical
~47 OOM split satisfies this by 46 OOM of structural margin. sign_verdict = PASS;
magnitude_verdict = PASS (47 >> 1.0 floor); regime_verdict = VALID.
```

**11. What PASSES/FAILS MEAN for solution space**: PASS confirms LISA can discriminate the regulator-class axis decisively (the framework predicts the substrate splits its Ω_GW prediction across 47 OOM, well above LISA's frequency-pivot sensitivity range). FAIL would indicate the (A)/(C) split is illusory or the canonical pins are mis-stated; the regulator-class axis would degrade to 1-axis joint detection. Given the W-3 workshop's Sage-exact establishment of ~47 OOM, PASS is structurally guaranteed; FAIL on this gate would indicate a canonical-constants pipeline defect (Class-(c) PIN-DRIFT-FROM-STALE-SOURCE or Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY).

**12. Effort estimate**: ~3 hours.

**13. Substrate-framing reminder**: Ω_GW is a substrate-emergent observable; (A)/(C) is the regulator-class atlas's two sub-cone partition. The "split_OOM" measures how widely-separated the substrate's two regulator-class sub-cones are in the lab-IN Ω_GW projection. Substrate IS the spectrum; LISA measures its lab-image; the split is structural.

---

### §W3-3c. `S87-DELTA-SPEED-MELLIN-WINDOW` (CF-23)

**1. Gate ID**: `S87-DELTA-SPEED-MELLIN-WINDOW`

**2. Trigger**: `[SIGN]` — δ_speed asymmetric inheritance observation per volovik R3-A; the substrate predicts a specific SIGN for the δ_speed (deviation from c_S = 1) at the τ_fold window, and the gate tests whether the sign matches the volovik substitution-chain prediction. This is the only [SIGN]-trigger gate in W3; all others are [VERIFY].

**3. Classification**: PHONONIC — δ_speed is the deviation of the phonon-mode propagation speed from c_S = 1 within the Mellin-cone window at τ_fold; this is a substrate-excitation observable (the phononic propagation pattern), not pure geometry. Per `.claude/rules/phononic-framing.md`: PHONONIC = "Directly involves substrate excitations, relay patterns, spectral moments, or GGE physics."

**4. Agent type**: `gen-physicist`. Fallback: `volovik-superfluid-universe-theorist` — δ_speed asymmetric inheritance was Volovik's R3-A finding; he is the originator of the observation. Volovik-fallback is mathematically clean because the asymmetric-inheritance computation is in his superfluid-analog tradition.

**5. Hypothesis**: The substrate's δ_speed at τ_fold is sign-positive under the asymmetric-inheritance prediction (Path-H δ_speed > 0; Path-C δ_speed < 0), with the |δ_speed| exceeding the Mellin-window numerical noise floor by ≥ 5σ.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_3c_delta_speed_mellin_window.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Pull canonical pins:
    delta_speed_PathH (substrate prediction at τ_fold for Path-H regulator-class)
    delta_speed_PathC (substrate prediction at τ_fold for Path-C regulator-class)
    sigma_delta_speed_mellin_noise (Mellin-window numerical noise floor at L_max=10)
  If any canonical pin is MISSING from canonical_constants.py at S87 plan-freeze:
    The producing script invokes the substrate-first-canonical-sourcing.md
    Class-(f) remediation: query mcp__knowledge__.search_knowledge("delta_speed
    asymmetric inheritance volovik R3-A") for the substrate-first canonical;
    IF none exists, the gate emits PRE-REG-INCOMPLETE and the canonical
    sourcing is queued as S88 carry-forward (MUST not place placeholder
    O(10⁻ⁿ) value per HARD-HALT band rule).
- Compute δ_speed at τ_fold via Mellin-cone analytic continuation:
    Use C10 analytic_zeta API at s = δ_speed_pole (substrate-distance-1 pole at s=4)
    For each regulator class (Path-H, Path-C), evaluate δ_speed at the τ_fold window
    via Mellin-window integral (L1-class regulator atlas):
      δ_speed_X(τ_fold) = Mellin_residue(integrand_X(s, τ_fold), s=4)  # (local)
- Test (a) sign agreement with prediction:
    sign_PathH_match = (sign(delta_speed_PathH_computed) == +1)  # (local)
    sign_PathC_match = (sign(delta_speed_PathC_computed) == -1)  # (local)
    sign_PASS = sign_PathH_match AND sign_PathC_match
- Test (b) magnitude > 5σ noise floor:
    margin_PathH = |delta_speed_PathH_computed| / sigma_delta_speed_mellin_noise  # (local)
    margin_PathC = |delta_speed_PathC_computed| / sigma_delta_speed_mellin_noise  # (local)
    mag_PASS = (margin_PathH >= 5.0) AND (margin_PathC >= 5.0)
- Aggregate PASS = sign_PASS AND mag_PASS
- regime_verdict = VALID if Mellin-window L_max=10 truncation residual < 1% of |δ_speed|;
                   MARGINAL if residual ∈ [1%, 5%]; BREAKDOWN if > 5%

GPU: USE torch.linalg for any D_K eigvals at L_max=10 (155,984-eigenvalue cache).

Outputs:
- s87_w3_3c_delta_speed_mellin_window.npz (δ_speed both classes, margins, regime diagnostic)
- s87_w3_3c_delta_speed_mellin_window.png (δ_speed vs τ around τ_fold; both classes overlaid)
- s87_w3_3c_delta_speed_mellin_window.json (verdict 4-tuple + sign + magnitude diagnostic)

Verdict line:
S87-DELTA-SPEED-MELLIN-WINDOW: <PASS|FAIL|INFO> -- value=<min(margin_PathH, margin_PathC)> scheme=Mellin-cone-analytic-continuation convention=delta-speed-asymmetric-inheritance-volovik-R3A L_max=10 audit_sha256=<64> content_sha256=<64> schema_version=S84+

S87 schema-v2 3-tuple companion row (REQUIRED for [SIGN] trigger):
# sign_verdict=<PASS|FAIL> magnitude_verdict=<PASS|INFO|FAIL> regime_verdict=<VALID|MARGINAL|BREAKDOWN> # S87-DELTA-SPEED-MELLIN-WINDOW 3-tuple annotation (S87 schema-v2)
```

**7. Machinery pin (PRDR)**:
- `L_max`: 10 (W-3 workshop canonical truncation)
- `scheme`: `Mellin-cone-analytic-continuation`
- `convention`: `delta-speed-asymmetric-inheritance-volovik-R3A`
- `n_eval`: 4 (2 classes × 2 quantities — δ_speed value + Mellin truncation residual)
- `scan_range`: τ ∈ [τ_fold − 0.005, τ_fold + 0.005] (10-point sweep around τ_fold for the .png plot; central value reported)
- `step_size`: dτ = 0.001
- `tolerance`: sign_PASS boolean; mag_PASS at margin ≥ 5.0σ; regime band 1%/5% of |δ_speed|
- `random_seed`: N/A (deterministic Mellin residue)
- `GPU path`: `torch.linalg` (ROCm 7.2 / AMD RX 9070 XT) for D_K eigvals
- `cutoff_axis`: `spectral`
- `regulator_pin_tag`: `a_4^{Mellin}` for Mellin-window evaluation
- `Class_(f)_remediation_active`: TRUE if any canonical pin missing — emits PRE-REG-INCOMPLETE not placeholder

**8. Expected output 4-tuple**: `(value=<min_margin_5sigma_floor_check>, scheme=Mellin-cone-analytic-continuation, convention=delta-speed-asymmetric-inheritance-volovik-R3A, L_max=10)`

**9. PASS/FAIL/INFO thresholds**:
- **PASS**: sign_PASS = True AND mag_PASS = True AND regime_verdict = VALID
- **INFO** (composite collapse): magnitude_verdict = INFO (margin ∈ [3σ, 5σ)) OR regime_verdict = MARGINAL
- **FAIL**: sign_verdict = FAIL OR regime_verdict = BREAKDOWN OR (mag_PASS = False AND regime = VALID)
- **PRE-REG-INCOMPLETE**: any canonical pin missing per Class-(f) remediation
- Tolerance: composite per gate-verdicts.md schema-v2 collapse rule (BREAKDOWN dominates)

**10. Substitution chain** (sign claim — MANDATORY for [SIGN] trigger):
```
Step 1 (definitions):
  c_S            = phonon mode speed at τ_fold (substrate-natural unit; 1 at flat reference)
  δ_speed(τ)     = c_S(τ) - 1 (deviation from flat reference)
  δ_speed_PathH  = δ_speed evaluated under Path-H regulator-class projection
  δ_speed_PathC  = δ_speed evaluated under Path-C regulator-class projection
  Mellin-window  = analytic continuation of substrate spectral moment to s=4 pole at τ_fold

Step 2 (substitute volovik R3-A asymmetric-inheritance prediction):
  Volovik R3-A claim (per S86 W-3 R3-A workshop §"What Changed" and §"Carry-Forward
  Computations"): under asymmetric inheritance, the regulator-class projections give
    δ_speed_PathH ∝ + |inheritance_arrow| > 0
    δ_speed_PathC ∝ - |inheritance_arrow| < 0
  The proportionality is set by the BDI 0D inheritance arrow magnitude (V1 anchor).

Step 3 (simplify):
  Sign of δ_speed_PathH > 0 ⇔ Path-H projection enhances c_S above the flat reference
                              (substrate "speeds up" phonons in the Path-H cell at τ_fold)
  Sign of δ_speed_PathC < 0 ⇔ Path-C projection suppresses c_S below the flat reference
                              (substrate "slows down" phonons in the Path-C cell at τ_fold)
  These are anti-correlated by construction (asymmetric inheritance → cells split symmetrically
  around flat reference, with sign opposite by regulator-class label).

Step 4 (direction):
  Substrate prediction:
    sign(δ_speed_PathH) = +1 (Path-H fastens c_S above flat)
    sign(δ_speed_PathC) = -1 (Path-C slows c_S below flat)
  Computed test:
    sign_PASS ⇔ both signs match prediction
  Direction: PASS if and only if the Mellin-window-computed signs match the volovik R3-A
             prediction. FAIL if either sign reverses.
  sign_verdict = PASS iff sign_PathH_computed == +1 AND sign_PathC_computed == -1.

Conclusion: PASS direction is anti-correlated δ_speed with sign-PathH = +1 / sign-PathC = −1.
Mismatch in either sign indicates the volovik R3-A asymmetric-inheritance prediction is
incorrect for that regulator class. The 5σ magnitude floor + VALID regime are subordinate
to the sign claim per the gate-verdicts.md schema-v2 collapse rule (sign FAIL ⇒ composite
FAIL regardless of magnitude).
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: volovik R3-A asymmetric-inheritance observation is empirically confirmed at the L_max=10 Mellin-window. The substrate's asymmetric inheritance is a structural prediction with directional content (not just magnitude). δ_speed becomes a substrate-derived prediction available for Pillar IV / lab-side cross-check (3He-B vortex-core spectroscopy could probe the analog of δ_speed asymmetry — folded into CF-32's W11-C5 follow-up).
- **FAIL** (sign mismatch): asymmetric inheritance does not reproduce the predicted sign pattern; the volovik R3-A reading needs structural revision. Likely culprit: a different regulator-class assignment (Path-H ↔ Path-C swap; canonical-pins audit needed) OR the Mellin-window's substrate-distance-1 pole at s=4 is not the correct probe (the asymmetry may localize at substrate-distance-2 pole at s=5 instead — folded into S88 follow-up).
- **INFO** (magnitude < 5σ): direction matches but magnitude sub-5σ; a stretched-goal Mellin-window evaluation at L_max=12 may be needed to resolve the asymmetry above noise; flagged for S88 L_max scan.
- **BREAKDOWN regime**: Mellin-window truncation residual > 5% of |δ_speed| — substrate prediction at L_max=10 is not converged; the gate's value is well-defined numerically but its physical interpretation is not what the pre-registration intended. Composite FAIL per schema-v2 collapse rule. Re-run at L_max=12 pre-registered for S88 sub-gate.

**12. Effort estimate**: ~3 hours (covers Mellin-window evaluation at L_max=10 + 10-point τ sweep for plot + Class-(f) remediation check). Heavy-side risk: missing canonical pins force PRE-REG-INCOMPLETE; light-side: if all pins exist and Mellin-window is converged, the computation is straightforward.

**13. Substrate-framing reminder**: δ_speed is a phononic observable — the speed of substrate excitations relative to the flat reference. Asymmetric inheritance is a substrate-side prediction: the regulator-class lattice's two cells inherit BDI 0D anchor with opposite sign of δ_speed. State as: **"The substrate's regulator-class lattice inherits the V1 BDI 0D arrow asymmetrically across its two cells; Path-H accelerates phonon propagation above flat reference, Path-C decelerates below."** Avoid framing as "we predict a phenomenological signal" — δ_speed is structural, not phenomenological.

---

### §W3-3d. `S87-W3-3D-JOINT-LITEBIRD-LISA-FISHER-DISCOUNT`

**1. Gate ID**: `S87-W3-3D-JOINT-LITEBIRD-LISA-FISHER-DISCOUNT`

**2. Trigger**: `[VERIFY]` — joint LiteBIRD + LISA Fisher-information cross-axis discount; PASS predicate is that the joint Fisher information (sum of single-axis Fisher information across LiteBIRD n_T axis + LISA Ω_GW axis) yields a joint discrimination margin ≥ 1.5σ (slightly above the per-axis 1σ thresholds of §W3-3a/b due to cross-axis amplification).

**3. Classification**: GEOMETRIC — Fisher information is a structural property of the joint observable's posterior; the cross-axis discount is a structural property of the §VII.AC.3 rank-2 product detector orthogonality.

**4. Agent type**: `gen-physicist`. Fallback: `mack-cosmic-bridge` (joint LiteBIRD+LISA Fisher analysis is observational falsifier-design — Mack's portfolio).

**5. Hypothesis**: The joint Fisher information across LiteBIRD n_T + LISA Ω_GW axes yields a 2-axis joint discrimination margin ≥ 1.5σ for distinguishing all 4 cells of the §VII.AC.3 rank-2 product structure.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_3d_joint_litebird_lisa_fisher.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Read upstream §W3-3a margin (LiteBIRD margin_sigma_LB) from
  s87_w3_3a_litebird_n_T_discriminator.npz
- Read upstream §W3-3b split (LISA split_OOM) from
  s87_w3_3b_lisa_omega_gw_a_c_discriminator.npz
- Convert LISA OOM split to σ-equivalent at LISA design sensitivity:
    margin_sigma_LISA = abs(split_OOM) / sigma_OOM_LISA  # (local)
    where sigma_OOM_LISA = canonical pin (LISA log-space sensitivity floor in OOM)
- Compute joint Fisher information assuming axis-orthogonality (per §VII.AC.3
  Rank-2 Product Detector Orthogonality Theorem):
    F_joint = F_LB + F_LISA = margin_sigma_LB^2 + margin_sigma_LISA^2  # (local)
  (Information sums; 2σ on each axis = sqrt(8) ≈ 2.83σ joint)
- Joint margin in σ-equivalent:
    joint_margin_sigma = sqrt(F_joint)  # (local)
- PASS criterion: joint_margin_sigma >= 1.5 (per per-axis 1σ + ~50% cross-axis amplification)
- INFO band: 1.0 <= joint_margin_sigma < 1.5
- FAIL: joint_margin_sigma < 1.0

GPU: NOT NEEDED (Fisher arithmetic is scalar).

Outputs:
- s87_w3_3d_joint_litebird_lisa_fisher.npz (per-axis Fisher contributions, joint)
- s87_w3_3d_joint_litebird_lisa_fisher.png (Fisher ellipse on (n_T, log Ω_GW) plane;
  4-cell decomposition shaded; per-axis marginals as side panels)
- s87_w3_3d_joint_litebird_lisa_fisher.json (verdict 4-tuple + Fisher diagnostic)

Verdict line + 3-tuple companion row.
```

**7. Machinery pin (PRDR)**:
- `L_max`: N/A
- `scheme`: `joint-Fisher-information`
- `convention`: `LiteBIRD-+-LISA-axis-orthogonal-per-VII.AC.3`
- `n_eval`: 1 (joint margin)
- `tolerance`: PASS at joint_margin ≥ 1.5σ; INFO at [1.0, 1.5); FAIL < 1.0
- `axis_orthogonality_assumption`: `§VII.AC.3` (Rank-2 Product Detector Orthogonality Theorem; cited as input)
- `joint_theorem_promotion_pathway_stage`: STAGE-1 (per `.claude/rules/joint-theorem-promotion.md`; this gate is a Stage-1 candidate landing for the Joint LiteBIRD-LISA-Fisher cross-axis theorem; Stage-2 two-agent independent verify is queued as S88 carry-forward `S88-JOINT-LITEBIRD-LISA-FISHER-INDEPENDENT-VERIFY`)

**8. Expected output 4-tuple**: `(value=<joint_margin_sigma>, scheme=joint-Fisher-information, convention=LiteBIRD-+-LISA-axis-orthogonal-per-VII.AC.3, L_max=N/A)`

**9. PASS/FAIL/INFO thresholds**: PASS at joint_margin_sigma ≥ 1.5; INFO [1.0, 1.5); FAIL < 1.0. Tolerance: ABSOLUTE on joint_margin_sigma.

**10. Substitution chain**:
```
Step 1 (definitions):
  margin_LB    = LiteBIRD per-axis margin in σ (from §W3-3a)
  margin_LISA  = LISA per-axis margin in σ (from §W3-3b after OOM-to-σ conversion)
  F_LB         = margin_LB^2  (Fisher info per-axis under Gaussian-likelihood approx)
  F_LISA       = margin_LISA^2
  F_joint      = F_LB + F_LISA  (additive under axis-orthogonality per §VII.AC.3)
  joint_margin = sqrt(F_joint) = sqrt(margin_LB^2 + margin_LISA^2)

Step 2 (substitute):
  PASS ⇔ sqrt(margin_LB^2 + margin_LISA^2) >= 1.5

Step 3 (simplify; squared form):
  PASS ⇔ margin_LB^2 + margin_LISA^2 >= 2.25
  Boundary: (margin_LB = margin_LISA = 1.06 ⇒ sum = 2.25; matches (1.06)^2 × 2 = 2.247)
  Cross-axis amplification: per-axis 1σ on each → joint 1.41σ; per-axis 1.5σ on each
    → joint 2.12σ; per-axis 2σ on each → joint 2.83σ. Joint always > max(per-axis).

Step 4 (direction):
  IF margin_LB >= 1.0 AND margin_LISA >= 1.0  THEN joint_margin >= sqrt(2) ≈ 1.41
                                                     (likely INFO, possibly PASS at boundary)
  IF margin_LB >= 1.0 AND margin_LISA >= 47/sigma_OOM_LISA (W-3 prediction)
                                              THEN joint_margin >> 1.5  (heavy PASS by LISA dominance)
  Direction: joint margin is monotone non-decreasing in both per-axis margins; cross-axis
             contribution is amplifying (sqrt(sum) ≥ max).

Conclusion: PASS direction is "joint Fisher exceeds per-axis-Fisher-floor sum of 2.25
σ². Given W-3 prediction of LISA split ≈ 47 OOM, LISA dominates the Fisher; PASS is
structurally guaranteed unless §W3-3b FAILs (unlikely per §W3-3b §11). sign_verdict = PASS
(predicted joint > sum of per-axis); magnitude verdict tracks the joint_margin band.
```

**11. What PASSES/FAILS MEAN for solution space**: PASS confirms the joint LiteBIRD+LISA falsifier suite has sufficient Fisher information to discriminate all 4 cells of §VII.AC.3 at ≥ 1.5σ joint margin. The joint suite is operationally a Stage-1 candidate for the Joint LiteBIRD-LISA-Fisher cross-axis theorem (per `.claude/rules/joint-theorem-promotion.md`); Stage-2 two-agent independent verify is queued as S88 carry-forward. FAIL would indicate axis-orthogonality assumption (§VII.AC.3) breaks down at the joint Fisher level; flagged as Class-8.2 verifier-rubric pre-registration failure for S88 reconciliation.

**12. Effort estimate**: ~4 hours (Fisher computation + 4-cell Fisher ellipse plot + joint-theorem-pathway annotation).

**13. Substrate-framing reminder**: Fisher information is a structural quantification of how strongly the lab-IN observables (n_T from LiteBIRD; Ω_GW from LISA) constrain the substrate-IS regulator-class lattice cells. Joint Fisher at axis-orthogonality is the sum of per-axis Fishers — a structural identity per §VII.AC.3, not a phenomenological assumption.

---

### §W3-3e. `S87-W3-3E-LITEBIRD-LISA-NULL-ELIMINATION-CROSS-CHECK`

**1. Gate ID**: `S87-W3-3E-LITEBIRD-LISA-NULL-ELIMINATION-CROSS-CHECK`

**2. Trigger**: `[VERIFY]` — null-elimination cross-check (Gate 4 of inheritance-falsifier-protocol.md four-gate template; slope-discrimination on cocycle-degenerate rows). PASS predicate: the joint LiteBIRD+LISA suite eliminates the "null" cell (FAIL-no-cell-match in CF-21 §W3-2's classifier output) at ≥ 5σ in cross-check at the τ_fold window — i.e., the substrate prediction is decisively NOT in the FAIL-no-cell-match outcome.

**3. Classification**: GEOMETRIC — null-elimination cross-check is a structural property of the §VII.AC.3 4-cell decomposition (the FAIL-no-cell-match cell is the 5th outcome that the substrate's regulator-class lattice excludes by structure).

**4. Agent type**: `gen-physicist`. Fallback: `connes-ncg-theorist` (the FAIL-no-cell-match exclusion is a Connes-1996 reconstruction consequence; the NCG-axiomatic side rules out the 5th cell via Schur orthogonality).

**5. Hypothesis**: At τ_fold, the substrate's joint LiteBIRD+LISA prediction is decisively in one of the 4 cells (PASS-PathH-(A) or PASS-PathH-(C) or PASS-PathC-(A) or PASS-PathC-(C)) and decisively NOT in the FAIL-no-cell-match cell, with elimination margin ≥ 5σ in joint Fisher distance.

**6. Method** (complete dispatch prompt):

```
Run `computations/s87_w3_3e_null_elimination_cross_check.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head
- Import `classify_outcome` from `_meta_classifier_v2` (CF-21 product)
- Pull substrate-prediction tuple (n_T_substrate_at_tau_fold, Omega_GW_substrate_at_tau_fold,
  regulator_class_substrate_at_tau_fold) from canonical pins (Path-H assignment is the
  W-3 workshop's R3-A canonical reading)
- Classify substrate prediction:
    cell_predicted = classify_outcome(...)['cell']
    assert cell_predicted != 'FAIL-no-cell-match'
- Compute null-elimination Fisher distance:
    For the 4 PASS cells, joint Fisher distance from cell_predicted is structurally
    zero or small (within-cell scatter); for the FAIL-no-cell-match outcome, the
    Fisher distance is the MIN over all (n_T, Ω_GW) tuples that the meta-classifier
    labels FAIL-no-cell-match. If the substrate-prediction tuple lies inside one of
    the 4 PASS cells, the Fisher distance to the FAIL-no-cell-match boundary is
    the orthogonal distance to the nearest band-edge.
    null_elim_sigma = orthogonal_Fisher_distance(cell_predicted, FAIL_boundary)  # (local)
- PASS criterion: null_elim_sigma >= 5.0
- INFO: 3.0 <= null_elim_sigma < 5.0
- FAIL: null_elim_sigma < 3.0

GPU: NOT NEEDED.

Outputs:
- s87_w3_3e_null_elimination_cross_check.npz (cell_predicted, null_elim_sigma,
  per-band-edge orthogonal distances)
- s87_w3_3e_null_elimination_cross_check.png (4-cell + null-cell decomposition;
  substrate-prediction point overlaid; arrows to band edges)
- s87_w3_3e_null_elimination_cross_check.json (verdict 4-tuple + null_elim diagnostic)

Verdict line + 3-tuple companion row.
```

**7. Machinery pin (PRDR)**:
- `L_max`: N/A
- `scheme`: `null-elimination-Fisher-distance`
- `convention`: `cell-predicted-vs-FAIL-no-cell-match-boundary`
- `n_eval`: 1 (orthogonal Fisher distance)
- `tolerance`: PASS at null_elim_sigma ≥ 5.0; INFO [3.0, 5.0); FAIL < 3.0
- `meta_classifier_v2_dependency`: requires CF-21 (`_meta_classifier_v2.py` callable) PASS or INFO
- `inheritance_falsifier_gate_4_position`: structural-confirm; the slope-discrimination form degenerates to orthogonal-distance form because the 4-cell decomposition is rectangular (rather than slope-degenerate)

**8. Expected output 4-tuple**: `(value=<null_elim_sigma>, scheme=null-elimination-Fisher-distance, convention=cell-predicted-vs-FAIL-no-cell-match-boundary, L_max=N/A)`

**9. PASS/FAIL/INFO thresholds**: PASS at null_elim_sigma ≥ 5.0; INFO [3.0, 5.0); FAIL < 3.0. Tolerance: ABSOLUTE on null_elim_sigma.

**10. Substitution chain**:
```
Step 1 (definitions):
  cell_predicted     = classify_outcome(substrate-prediction-tuple)['cell']
                       expected: one of {PASS-PathH-(A), PASS-PathH-(C),
                                          PASS-PathC-(A), PASS-PathC-(C)}
  FAIL_boundary      = the (n_T, log Ω_GW) locus where classify_outcome(...) returns
                       'FAIL-no-cell-match'
  null_elim_sigma    = orthogonal Fisher distance from substrate-prediction tuple to
                       the nearest FAIL_boundary edge

Step 2 (substitute):
  PASS ⇔ orthogonal_Fisher_dist(substrate_pt, FAIL_boundary) >= 5.0
       ⇔ substrate is at least 5σ inside one of the 4 PASS cells

Step 3 (simplify):
  PASS ⇔ substrate prediction is decisively inside a non-FAIL cell (5σ deep in cell
         interior)

Step 4 (direction):
  IF substrate prediction lies in the deep interior of a PASS cell  THEN PASS (5σ deep)
  IF substrate prediction lies near a band-edge between two PASS cells (still non-FAIL)
                                                                      THEN INFO ([3σ, 5σ))
  IF substrate prediction lies near the FAIL-no-cell-match boundary  THEN FAIL (< 3σ)
  Direction: positive-direction = deeper interior of PASS cells = stronger null elimination.

Conclusion: PASS direction is "substrate is decisively inside a PASS cell, away from the
null boundary by 5σ Fisher equivalent". FAIL would indicate the substrate prediction is
at risk of falling into the FAIL-no-cell-match classifier outcome — meaning the W-3
workshop's 4-cell decomposition does not span the substrate's prediction at the τ_fold
window, exposing a structural gap. sign_verdict = PASS by structural construction
(substrate prediction is deep inside Path-H + (A) cell per W-3 R3-A canonical reading).
```

**11. What PASSES/FAILS MEAN for solution space**:
- **PASS**: 4-cell decomposition spans the substrate's τ_fold prediction with 5σ null-elimination margin. The §VII.AC.3 Rank-2 Product Detector Orthogonality Theorem is structurally complete; no 5th cell is needed.
- **INFO** (3σ-5σ band): substrate prediction is on the boundary of two PASS cells; the joint suite cannot decisively discriminate at the τ_fold window — flag for S88 cell-band recalibration.
- **FAIL** (< 3σ): substrate prediction may fall into FAIL-no-cell-match — the 4-cell decomposition has a structural gap. CF-22 carries forward to S88 with the FAIL-cell expansion (potentially a 5-cell decomposition with a "Path-mixed" or "regulator-mixed" intermediate cell — folded into S88 carry-forward).

**12. Effort estimate**: ~3 hours.

**13. Substrate-framing reminder**: null-elimination is a structural property of the substrate's regulator-class lattice — the substrate's prediction at τ_fold MUST land in one of the 4 §VII.AC.3 cells (the lattice has only 4 cells by Schur orthogonality of A_F = C ⊕ H ⊕ M_3(C)); the cross-check confirms the substrate-IS prediction is robustly inside a cell. Lab-IN measurement is the future test; this gate is the substrate-side null-elimination pre-registration.

---

## §W3-4. CF-24 — `S87-S88-PLUS-CANDIDATES` (3 placeholder sub-stubs)

**Top-level Gate ID**: `S87-S88-PLUS-CANDIDATES`

This is a **stub-only pre-scoping gate**: 3 placeholder 4-field specs are written into the working-paper section + a single PRE-REG-INCOMPLETE verdict line is appended. NO compute, NO data, NO plot. The PASS predicate is "S88 plan author can fill the 4-field spec for each sub-stub with no further research at S87 close" per `feedback_fix-in-session-never-defer.md`. The S87-side verdict is INFO with `value='3_substubs_pre_scoped'`.

**Sub-stub decomposition**:

| Sub-stub | Gate ID | Theme | S88 effort estimate |
|:---------|:---------|:------|:--------------------|
| §W3-4a | `S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION` | Pati-Salam GUT embedding preserves B1/B2 block decomposition under §VII.AC.2 | ~1-2 waves (full computation, S88) |
| §W3-4b | `S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE` | EE/BB-T cross-correlation as direct c_S probe (per `feedback_reporting-framing.md` direct-probe-strength) | ~1 wave (S88) |
| §W3-4c | `S88-F-NL-EQUILATERAL-NON-GAUSSIANITY` | f_NL^equilateral non-Gaussianity prediction (W14-4 framework-language extension to equilateral configuration) | ~1-2 waves (S88) |

---

### §W3-4a. `S88-PATI-SALAM-EMBEDDING-PRESERVES-B1-B2-PARTITION` (sub-stub)

**4-field spec** (placeholder per `feedback_fix-in-session-never-defer.md`):

| Field | Specification |
|:------|:--------------|
| **What** | Test whether the Pati-Salam SU(4) × SU(2)_L × SU(2)_R embedding of the substrate's algebra A_F = C ⊕ H ⊕ M_3(C) preserves the B1/B2 block decomposition theorem (§VII.AC.2). PASS iff the Pati-Salam-embedded D_K eigenvalue spectrum admits the same B1/B2 block decomposition with multiplicity-vector match within rel_tol = 1e-6. |
| **Inputs** | (1) Pati-Salam algebra spec (Pati-Salam 1974 PRD; finite-spectral-triple version per CF-12 `S88-CONNES-DISTANCE-FINITE-SPECTRUM-IDENTITY-CONJECTURE` follow-up); (2) `computations/s84_spectrum_cache_L12_tau019.npz` for SM-side reference spectrum; (3) §VII.AC.2 B1/B2 Block Decomposition Uniqueness Theorem (per `permanent-results-registry.md` line 88); (4) canonical_constants.py for any framework-shared pins. |
| **Gate** | PASS iff B1/B2 multiplicity-vector match at rel_tol ≤ 1e-6; FAIL if any block multiplicity differs by > 1; INFO if multiplicities match within ±1 but rel_tol fails. |
| **Effort** | ~1-2 waves S88 (full Pati-Salam algebra construction + D_K eigenvalue cache + block decomposition verification on the larger algebra). Pre-requisites: CF-12 must close to define the finite-spectral-triple version of Pati-Salam. |

S87-side: NO compute. Pre-scoped 4-field spec is written into the working paper §W3-4a section. The S88 plan author fills in canonical pin names + verifier rubric at S88 plan-write time without further research at S87 close.

---

### §W3-4b. `S88-EE-BB-T-CROSS-CORRELATION-DIRECT-CSUB-PROBE` (sub-stub)

**4-field spec** (placeholder):

| Field | Specification |
|:------|:--------------|
| **What** | Compute the substrate's prediction for the EE × BB temperature-mode cross-correlation power spectrum at multipoles ℓ ∈ [30, 1500], as a direct c_S probe (the cross-correlation amplitude is sensitive to the substrate's c_sub conformal-anomaly contribution at the τ_fold window). The cross-correlation is a more direct probe than r alone because its multipole-shape is c_S-dependent rather than c_S-independent. |
| **Inputs** | (1) c_sub_baseline canonical pin (= 2.238 per `canonical_constants.py`); (2) Substrate's polarization power spectrum infrastructure from CF-25 W-4 cross-pillar 3-channel theorem (PASS-conditional); (3) Planck 2018 EE + BB likelihood for the lab-side comparison band; (4) BICEP/Keck EE×BB measurement at high-ℓ. |
| **Gate** | PASS iff substrate-predicted EE×BB cross-correlation amplitude at ℓ_pivot=80 lies within Planck+BICEP joint 1σ band (~direct c_sub measurement); INFO at 1-2σ; FAIL > 2σ. |
| **Effort** | ~1 wave S88 (substrate polarization spectrum + cross-correlation evaluation + lab-side band comparison). |

S87-side: NO compute. Pre-scoped 4-field spec written.

---

### §W3-4c. `S88-F-NL-EQUILATERAL-NON-GAUSSIANITY` (sub-stub)

**4-field spec** (placeholder):

| Field | Specification |
|:------|:--------------|
| **What** | Compute the substrate's prediction for the equilateral-configuration non-Gaussianity bispectrum amplitude f_NL^equilateral (extension of W14-4 framework-language §line 414-422 from f_NL^folded to f_NL^equilateral). The equilateral configuration is structurally distinct from folded — it probes a different residue at the substrate's substrate-distance-1 pole. |
| **Inputs** | (1) f_NL^folded canonical pins (`f_NL_FW_S82_equilateral`, `f_NL_FW_S67_folded`, `f_NL_FW_S85_W9_3_analytic_template` per W14-4 W14-5 precedents — note: re-pin under equilateral configuration); (2) Substrate bispectrum infrastructure (Mellin-cone analytic continuation at pole s=4 with equilateral kinematics weighting); (3) Planck 2018 f_NL^equilateral measurement (= -26 ± 47, 1σ); (4) Bispectrum-extended canonical_constants.py entries for equilateral configuration. |
| **Gate** | PASS iff substrate-predicted f_NL^equilateral lies within Planck 1σ band of -26 ± 47; INFO 1-2σ; FAIL > 2σ. |
| **Effort** | ~1-2 waves S88 (Mellin-cone bispectrum at equilateral kinematics + canonical pin promotion via canonical write-order + lab-side comparison). Pre-requisites: CF-27 W-4 f_NL^folded language correction must be in place to define the equilateral-extension consistently. |

S87-side: NO compute. Pre-scoped 4-field spec written.

---

### CF-24 §W3-4 verdict-line emission (S87-side stub closure):

**Method** (single dispatch, write-only):

```
Run `computations/s87_w3_4_s88_plus_candidates_pre_scope.py` under
`"phonon-exflation-sim/.venv312/Scripts/python.exe"` with:

- `from canonical_constants import *` at script head (no compute; just imports for
  audit-trail completeness)
- Verify the §W3-4a/§W3-4b/§W3-4c 4-field specs above are written into the
  W3 working-paper file section §W3-4a/b/c (read-back check: each section
  contains all 4 fields What/Inputs/Gate/Effort)
- Compute audit_sha256 = closure_hash(input_pin_map) where pin_map = {plan_block_sha256,
  W3-working-paper-section-shas, gate_id, scheme, convention, L_max}

Output:
- s87_w3_4_s88_plus_candidates_pre_scope.json (3-substub pre-scope diagnostic;
  per-substub 4-field-completeness check)
- (NO .npz, NO .png — stub-only gate)

Verdict line:
S87-S88-PLUS-CANDIDATES: INFO -- value='3_substubs_pre_scoped' scheme=stub-only-pre-scope convention=4-field-spec-per-feedback_fix-in-session-never-defer L_max=N/A audit_sha256=<64> content_sha256=<64> schema_version=S84+

Dual-SHA companion row only (no 3-tuple — [VERIFY] artifact-existence stub gate).
```

**PRDR machinery pin**: scheme=`stub-only-pre-scope`, convention=`4-field-spec-per-feedback_fix-in-session-never-defer`, n_eval=3 (3 sub-stubs), tolerance=boolean per-substub 4-field-completeness, all other fields N/A, GPU NOT USED.

**PASS/FAIL/INFO**: INFO at 3/3 sub-stubs pre-scoped; FAIL at < 3 sub-stubs pre-scoped (S87 plan author must complete all 3 4-field specs before terminating).

**Substitution chain** (artifact-existence direction):
```
Step 1: substub_complete_i = (W3-4{a,b,c} working-paper section contains all 4 fields:
        What, Inputs, Gate, Effort) for i ∈ {a, b, c}
Step 2: PASS-precondition ⇔ (substub_complete_a AND substub_complete_b AND substub_complete_c)
Step 3: composite verdict = INFO (per `feedback_fix-in-session-never-defer.md`: pre-scope
        for next-session is INFO, not PASS — there is no compute to PASS)
Step 4: Direction: artifact-existence boolean; no sign claim.
```

**Effort estimate**: ~0.25 wave (~1-2 hours for the 3 sub-stub working-paper sections + the verdict-line append; no compute).

**Substrate-framing reminder**: All three S88+ sub-stubs are substrate-side predictions — Pati-Salam embedding is a regulator-axis extension of the substrate's algebra; EE/BB-T cross-correlation is a substrate-emergent observable derived from spectral moments; f_NL^equilateral is a substrate-bispectrum residue. Direction substrate → bridge → lab in all three.

---

## §II. Wave 3 → Wave 4 Decision Point

W3 has NO downstream-blocking decision points for other S87 waves at the wave level. The 5 sub-gates in §W3-3 (CF-22 + CF-23) collectively decompose the joint LiteBIRD-LISA falsifier suite; their aggregate verdict is recorded as the top-level CF-22 status.

**Internal decision branches** (intra-W3):

- IF §W3-1 (CF-20) FAILs (registry-landing incomplete) → §W3-3a/b (LiteBIRD/LISA single-axis discriminators) STILL DISPATCH (they consume canonical pins, not §VII.AC.1 registry text), but the working-paper text MUST cite the W-3 workshop-internal source for the dual-pathway structure rather than the registry row, with an explicit annotation `(provisional citation; §VII.AC.1 landing pending CF-20 retry in S88)`.
- IF §W3-2 (CF-21) FAILs (meta-classifier_v2 build incomplete) → §W3-3e (null-elimination cross-check) DEFERS to S88 as `S88-W3-3E-NULL-ELIMINATION-RETRY` because §W3-3e directly imports from `_meta_classifier_v2`. §W3-3a/b/c/d still dispatch independently.
- IF any §W3-3a..§W3-3e sub-gate emits BREAKDOWN regime → composite top-level CF-22 verdict is FAIL per gate-verdicts.md schema-v2 collapse rule; sub-gate's individual verdict line preserves the BREAKDOWN diagnostic for S88 follow-up.

**External W3 → other-wave decision branches**:

- §W3-1 (CF-20) PASS → falsifier-master-inventory Row #2 (Path-H/Path-C) gets a citation upgrade from W-3 workshop-internal to §VII.AC.1 registry-row anchor; this is mack-cosmic-bridge's responsibility (per `feedback_mack-bridge-role.md`); not a W3 deliverable but a downstream consequence.
- §W3-3c (CF-23 δ_speed) PASS → δ_speed becomes a substrate-derived prediction citable in Pillar IV / 3He-B vortex-core spectroscopy protocols (CF-32 W11-C5 follow-up); cross-link surfaces in W5/W11/W12 working papers, not in W3 directly.

---

## §III. Wave 3 Machinery-Enumeration Pin (§0.11 PRDR aggregate)

Per `.claude/rules/epistemic-discipline.md` §"PRU (Pre-Registration Underspecification)" + §"PRDR" requirements, the W3 wave's machinery-enumeration pin enumerates the union of all sub-gate machinery pins:

| Machinery dimension | Per-sub-gate pin enumeration | W3 aggregate value |
|:--------------------|:------------------------------|:--------------------|
| `L_max` | §W3-3c: 10; all other gates: N/A | Mixed: `{None: 7, 10: 1}` |
| `scheme` | §W3-1: registry-landing; §W3-2: meta-classifier-v2-build; §W3-3a: LiteBIRD-n_T; §W3-3b: LISA-Ω_GW; §W3-3c: Mellin-cone-analytic-continuation; §W3-3d: joint-Fisher-information; §W3-3e: null-elimination-Fisher-distance; §W3-4: stub-only-pre-scope | 7 distinct schemes; no scheme-shopping |
| `convention` | per-sub-gate (see individual blocks above) | 7 distinct conventions |
| `n_eval` | §W3-1: 5; §W3-2: 9; §W3-3a..e: 1+1+4+1+1; §W3-4: 3 | total = 26 evaluation points |
| `scan_range` | §W3-3c: τ ∈ [τ_fold − 0.005, τ_fold + 0.005], dτ=0.001; all other: N/A | One τ-scan pinned |
| `tolerance` | per-sub-gate (see individual blocks) | 7 distinct tolerance bands |
| `random_seed` | §W3-2: 42 (synthetic regression); all other: N/A | One seed pinned |
| `GPU path` | §W3-3c: torch.linalg ROCm 7.2; all other: NOT USED | One GPU sub-gate |
| `cutoff_axis` | §W3-3c: spectral; all other: N/A | One cutoff_axis pinned |
| `regulator_pin_tag` | §W3-3c: a_4^{Mellin}; all other: N/A | One regulator-pin tag |
| `verifier_rubric_pre_registration` | §W3-1: 5-string conjunction; §W3-2: 9-string conjunction; all other: N/A (numerical comparisons) | 2 verifier rubrics pinned |
| `Omega_GW_sage_exact_required` | §W3-3b: TRUE; all other: N/A | 1 Sage-exact requirement |
| `joint_theorem_promotion_pathway_stage` | §W3-3d: STAGE-1 candidate landing; all other: N/A | 1 joint-theorem stage-1 pin |
| `meta_classifier_v2_dependency` | §W3-3e: REQUIRED CF-21 PASS or INFO; all other: N/A | 1 cross-gate dependency |
| `Class_(f)_remediation_active` | §W3-3c: TRUE if any pin missing; all other: N/A | 1 Class-(f) pre-flight check |

Aggregate: 14 machinery dimensions enumerated; PRU Class-8 cardinality test PASS (no machinery dimension left unpinned at sub-gate level). Verifier-rubric pre-registration extension (S86 W1c-5) MET for §W3-1 (registry-landing literal-string conjunction) + §W3-2 (meta-classifier_v2 module literal-string conjunction).

---

## §IV. Wave 3 Input-SHA Ledger

Per `.claude/rules/gate-verdicts.md` §"Pre-Registration Protocol" item 1, every gate block's input file is pinned by SHA-256. W3 input-SHA pins (computed at runtime from each input file):

| Gate | Input file | SHA pin status at S87 plan-freeze |
|:-----|:-----------|:-----------------------------------|
| §W3-1 (CF-20) | `sessions/permanent-results-registry.md` (read existing §VII.AC.1 + §VII.AC.4 placeholders) | `<computed-at-runtime>` |
| §W3-1 | `computations/s86_gate_verdicts.txt` (read S86 W-3 R3-A Convergence #2 closure SHA) | `<computed-at-runtime>` |
| §W3-1 | `.claude/rules/registry-landing.md` (verify schema availability) | `<computed-at-runtime>` |
| §W3-2 (CF-21) | `computations/s86_gate_verdicts.txt` (W14-1..W14-5 verdict lines) | `<computed-at-runtime>` |
| §W3-2 | `computations/canonical_constants.py` (pathway-keyed Ω_GW pins, n_T pins) | `<computed-at-runtime>` |
| §W3-3a (LiteBIRD) | `computations/canonical_constants.py` (n_T_PathH, n_T_PathC, sigma_n_T_LiteBIRD) | `<computed-at-runtime>` |
| §W3-3b (LISA) | `computations/canonical_constants.py` (Omega_GW_FW_(A), Omega_GW_FW_(C) Sage-exact) | `<computed-at-runtime>` |
| §W3-3c (δ_speed; CF-23) | `computations/canonical_constants.py` (delta_speed_PathH, _PathC, sigma_delta_speed_mellin_noise) | `<computed-at-runtime>` |
| §W3-3c | `computations/s86_w2_mellin_cone_residue_infra.py` output (analytic_zeta API; for s=4 pole evaluation) | `<computed-at-runtime>` |
| §W3-3c | `computations/s84_spectrum_cache_L12_tau019.npz` (D_K eigenvalue cache for Mellin-window) | `<computed-at-runtime>` |
| §W3-3d (joint Fisher) | `computations/s87_w3_3a_litebird_n_T_discriminator.npz` (per-axis margin from §W3-3a) | `<computed-at-runtime>` |
| §W3-3d | `computations/s87_w3_3b_lisa_omega_gw_a_c_discriminator.npz` (per-axis split from §W3-3b) | `<computed-at-runtime>` |
| §W3-3d | `computations/canonical_constants.py` (sigma_OOM_LISA) | `<computed-at-runtime>` |
| §W3-3e (null-elim) | `computations/_meta_classifier_v2.py` (callable from CF-21) | `<computed-at-runtime>` |
| §W3-3e | `computations/canonical_constants.py` (substrate-prediction tuple at τ_fold) | `<computed-at-runtime>` |
| §W3-4 (stubs) | `sessions/archive/session-87/session-87-w3-workingpaper.md` §W3-4a/b/c (4-field-spec readback) | `<computed-at-runtime>` |

All SHA pins computed at runtime per the canonical script template (`computations/script-template.py`); `audit_sha256 = closure_hash(input_pin_map)` derived from the ordered input-pin map.

---

## §V. Plan-Freeze Validation Outputs (Phase 3e expected outputs)

Per `.claude/rules/agent-standards.md` + skill §3e, the orchestrator runs these validators on this plan file at S87 plan-freeze:

1. `python computations/_plan_upstream_pin_validator.py --json sessions/session-plan/session-87-plan-w3.md` → `sessions/session-plan/session-87-plan-w3-validation.json` (upstream-reference pin map)
2. `python computations/_yaml_gate_validator.py sessions/session-plan/session-87-plan-w3.md` → PRDR machinery checklist + `schema_version: R3` per gate
3. `python computations/_source_reconciliation_audit.py sessions/session-plan/session-87-plan-w3.md` → 5+1-class taxonomy report (special attention to Class-(f) PIN-PLACEHOLDER for δ_speed canonical pins)
4. `python computations/_substrate_first_provenance_audit.py sessions/session-plan/session-87-plan-w3.md` (V.1 manual review; production audit pending S87 implementation per CF-79 adjacent)
5. Post-dispatch grep on `computations/s86_gate_verdicts.txt` for collision check on S87 gate IDs (no S87-prefixed entries should pre-exist; if any collision, route to `_recovery_controller.py` Stage-3 user-trigger)

Per-gate YAML metadata (R3 schema):
- `schema_version: R3`
- `verdict_source: computations/s87_gate_verdicts.txt`

---

**End of session-87-plan-w3.md.**
