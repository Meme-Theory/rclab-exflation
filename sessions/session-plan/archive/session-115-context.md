# Session 115 — Context (carry-forward scope)

**Built by**: `/rclab-plan --session 115` (2026-06-24), Phase 1b/1c.
**Source**: the S114 per-wave WP `## Carry-Forward Computations` sections (canonical) + the two S114 workshop wrap-ups they mirror.
**Mode**: `--fanout` (default). **Planner default**: gen-physicist (cross-reviewer fallback); per-wave owners below.
**Verdict file (S115 compute gates)**: `computations/session-115/s115_gate_verdicts.txt`.

> **Scope discipline** (Safety rule 7): the items below ARE the scope — lifted verbatim-equivalent from the S114 WP CF blocks, no invented items. The cosmetic topic label never narrows execution; every carry-forward is tested.

---

## Source manifest

| Source file | CF block | Items lifted |
|:--|:--|:--|
| `sessions/session-114/session-114-w3-workingpaper.md` §"Carry-Forward Computations" (L218–258) | §B hygiene-promotion + W-2 workshop mirror | CF-S115-VIICK-STAGE2-VERIFY · CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL · CF-S115-LEPTON-PMNS-FORCED-TEXTURE (+ CF-S115-HK-1 EVOI frontier-row, register-maintenance not compute) |
| `sessions/session-114/session-114-w2-workingpaper.md` §"Carry-Forward Computations" (L222–235) | W-1 workshop mirror | CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM |
| `sessions/session-114/session-114-w4-workingpaper.md` §"Carry-Forward Computations" (L165–183) | OPTIONAL planner-discretion forward objects | CF-S115-AS-NEWAXIS-SELECTOR · CF-S115-B5A-TFD-QES |
| `sessions/session-114/session-114-w1-workingpaper.md` §"Carry-Forward Computations" (L171–173) | — | NONE (both W1 outcomes closed in-session) |
| `sessions/session-114/workshops/w-2-d4-rightreg-su3r-admissibility.md` §"Carry-Forward Computations" (L688–702) | CF-1/CF-2 | (mirrored into the W3 WP above) |
| `sessions/session-114/workshops/w-1-taufold-canonical-value.md` §"Carry-Forward Computations" (L475–482) | — | (mirrored into the W2 WP above) |
| `sessions/session-114/session-114-housekeeping.md` §B | hygiene compute CF | CF-S115-VIICK-STAGE2-VERIFY (mirror confirms §B) |

**Dedup note**: the W-2 workshop CF-1/CF-2 and the W-1 workshop CF were back-filled into the W3/W2 WP CF sections at S114-close (per the no-technical-debt rule). They are the SAME items, counted once.

---

## Deduplicated carry-forward table (6 compute gates)

| # | Gate ID | EVOI tier | Executor(s) | Dep | One-line scope |
|:--|:--|:--|:--|:--|:--|
| 1 | `CF-S115-VIICK-STAGE2-VERIFY` | HIGH (structural-permanent promotion) | 2 blind cross-reviewers (Axis-A NCG/spectral + Axis-B structurally-distinct) | — | §VII.CK D1–D3 closed-class STAGE-1-CANDIDATE → STAGE-3-PERMANENT (D4-open RETAINED) |
| 2 | `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` | HIGH (completes the genus) | Axis-A lizzi/spectral-geometer × Axis-B volovik | #1 (same §VII.CK slot) | D4 external-coupling discharge → STAGE-3-PERMANENT-UNCONDITIONAL |
| 3 | `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` | HIGH-OBSERVATIONAL | neutrino-detection-specialist (+ gen-physicist for the circulant) | B2+W-2 Q3 (landed S114) | test the external crossed-product corridor's forced PMNS texture vs observed J |
| 4 | `CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` | LOW / CONFIRMATORY | transit-dynamics-theorist / gen-physicist | — | confirmatory τ_cross cross-substitution; CANNOT flip the W-1 verdict |
| 5 | `CF-S115-AS-NEWAXIS-SELECTOR` | LOW (OPTIONAL) | transit-dynamics-theorist | — | new-axis A_s functional selector to collapse the 1.259-OOM spread |
| 6 | `CF-S115-B5A-TFD-QES` | LOWEST (OPTIONAL, Tier-3 NON-BLOCKING) | hawking-theorist | — | two-sided island QES extremization of S=Area/4+S_bulk |

> **Optional-gate disposition**: #5 and #6 were flagged "planner MAY drop" in the S114 W4 WP. Per `session-handoffs.md` ("all recommendations go in the plan; everything else in later waves") they are RETAINED in the final low-priority wave (W3), EVOI-ordered last, rather than dropped — carrying a clearly-scoped low-EVOI gate costs little; dropping a recommendation loses it permanently. The user may elect to drop either at the Phase-3b checkpoint.

---

## Full 4-field specs (verbatim-equivalent from the S114 WP CF blocks)

### 1. CF-S115-VIICK-STAGE2-VERIFY
*(source: `session-114-w3-workingpaper.md` L220–229; housekeeping §B L55–64)*

1. **What**: two-agent blind cross-axis independent-verify of the §VII.CK D1–D3 closed-class "SHAPE-Branch Homogeneity Obstruction" theorem; on PASS-AND, promote STAGE-1-CANDIDATE → STAGE-3-PERMANENT (the D4-open scope qualifier RETAINED — the wall is verified as the closed class, NOT upgraded to unconditional).
2. **Inputs**: the §VII.CK registry entry (`permanent-results-registry.md` body §VII.CK + master-index row 173); W3-3 verdict `audit_sha256=51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f`; the D1 machine-exact reproduction; permanent anchors `{γ₉,D_K}=0` (S34/S56) + multiplicity-leg generation id (`proven_384`).
3. **Gate**: `S115-VIICK-STAGE2-VERIFY` — PASS = both cross-reviewers PASS-AND on D1/D2/D3 (Axis-A NCG/spectral + Axis-B structurally-distinct), BOTH **excluding connes + paasch** (the YUKSHAPE Stage-0 authors) and their downstream-inheritance successors per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`. Reviewers receive ONLY the registered Stage-1 entry, NOT the workshop transcript.
4. **Effort**: ~1 wave (2 parallel verify agents + 1 PASS-AND closeout). **Depends on**: none (independent; shares the §VII.CK slot with #2 — see #2's sequencing note).

### 2. CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL
*(source: `session-114-w3-workingpaper.md` L242–249; `workshops/w-2-d4-rightreg-su3r-admissibility.md` CF-1, L690–695)*

1. **What**: blind two-agent cross-axis independent-verify of the D4-external JOINT clause — "the right-regular `R_{E_α}` SHAPE handle is external-as-a-coupling (admissible only via the canonical crossed product `A_K⋊SU(3)_R` / Kasparov external product, outside `Ω¹_{D_K}(A_K)` by the `t(O)=±1≠0` center-character selection rule), discharging D4 CLOSED-EXTERNAL-AS-A-COUPLING and completing the homogeneity-obstruction genus as a statement about `A_K`-internal couplings." On Stage-2 PASS-AND: §VII.CK re-scoped to the COMPLETE genus; tag STAGE-1-CANDIDATE → STAGE-3-PERMANENT-UNCONDITIONAL.
2. **Inputs**: the registered §VII.CK entry (D1–D3 closed class + the D4 row) + W3-1 residual = 1.000000 EXACT (audit `e392b832483e8f75c6cbd87086c3a10bfb19f3d242ba9f873de3a9434997d49b`) + the `t(O)=±1≠0` center-character selection rule (W-2 Re:V1) + the commutant argument (W-2 Re:V2) + `proven_384` (`t=(p−q) mod 3`). Reviewers receive ONLY the registered entry + these inputs — NOT the W-2 transcript.
3. **Gate**: `S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` — PASS-AND across BOTH axes (logical AND). **Axis-A** (NCG/spectral-functional NON-AUTHOR): `lizzi-spectral-functional-theorist` OR `spectral-geometer` (audits the `Ω¹_{D_K}(A_K)`-membership / selection-rule leg). **Axis-B** (substrate-geometry NON-AUTHOR, §VII.BL-NON-inheriting): `volovik-superfluid-universe-theorist` (audits the isometry-vs-coupling / commutant / crossed-product-image leg). **EXCLUDED**: {connes-ncg-theorist, paasch-mass-quantization-analyst (YUKSHAPE Stage-0)} ∪ {van-den-dungen-bridge-theorist, baptista-spacetime-analyst (W-2 authors)} ∪ {kaluza-klein-theorist (§VII.BL reviewer-of-record + co-author, downstream-inheritance reach)} ∪ any §VII.BL/§VII.CK/WS-C2COSET downstream-inheritance successor.
4. **Effort**: ~1 wave (2 parallel cross-reviewers + 1 PASS-AND closeout). **Depends on**: `CF-S115-VIICK-STAGE2-VERIFY` (#1) — shares the §VII.CK registry slot; SEQUENCING: #1 (closed-class D1–D3 → PERMANENT, D4-open) lands FIRST, THEN #2 (re-scope D4 → CLOSED-UNCONDITIONAL). Register both as distinct gates verifying DIFFERENT clauses; do NOT conflate. INDEPENDENT of #3.

### 3. CF-S115-LEPTON-PMNS-FORCED-TEXTURE
*(source: `session-114-w3-workingpaper.md` L251–258; `workshops/w-2-...md` CF-2, L697–702)*

1. **What**: construct the `A_K⋊SU(3)_R` right-regular circulant on the LEPTON multiplicity sector, impose the `ℂ⊕ℍ` charged-lepton-vs-neutrino sector-asymmetry (right-regular circulant on the neutrino/seesaw structure, coset-diagonal charged-lepton mass basis), compute the physical misalignment `U_mix = U_L^† U_R`, and test the forced tri-maximal `|U_ij|² = 1/3`, `J = 1/(6√3)` against observed PMNS `J ≈ 0.033`, `δ_CP` AFTER the charged-lepton correction. Pre-register: forced-and-surviving ⇒ zero-(mixing)-parameter prediction of the named external corridor; forced-and-washed-out ⇒ down-tag the lepton resonance to a symmetric-limit coincidence.
2. **Inputs**: B2 Sage-exact forced circulant (`|U_ij|² = 1/3`, `J = 1/(6√3)`, `arg(w) = 2π/3`) + the W-2 Q3 sector-misalignment result (two circulants ⇒ `U_mix = identity`; one-circulant-one-coset-diagonal ⇒ tri-maximal, Sage-confirmed) + the `ℂ⊕ℍ` lepton-sector structure of `A_K` + observed PMNS `J`/`δ_CP` (PDG). CONTINGENCY pin: tests the NAMED external crossed-product corridor, NOT a substrate-internal prediction.
3. **Gate**: `S115-LEPTON-PMNS-FORCED-TEXTURE` — `|J_forced − J_PMNS,observed| / J_PMNS,observed` after charged-lepton correction, against a pre-registered band (PASS if the corrected forced texture lands within the PMNS 3σ tri-maximal-deviation window; FAIL/down-tag otherwise). **Negative control**: the same machinery on `M₃(ℂ)`-shared quark chiralities MUST give `U_mix → identity` ≠ CKM (already established structurally, B2/Q3).
4. **Effort**: ~1 wave; routes through `neutrino-detection-specialist` (PMNS owner) and/or `gen-physicist` for the circulant construction. **Depends on**: B2 + W-2 Q3 sector-misalignment Sage result (landed S114); INDEPENDENT of #2 (that gate closes the genus; this one tests the corridor's residue).

### 4. CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM
*(source: `session-114-w2-workingpaper.md` L228–235; `workshops/w-1-taufold-canonical-value.md` L477–482)*

1. **What**: re-run `s101_w3_s0_knob.py` with candidate (iii) routed as `q = 0.191038` (the located crossing) instead of `q = Fraction(19,100)`, AND with the `assert abs(float(tau_f) - tau_fold) < 1e-15` guard relaxed to the substituted value, to mechanically confirm (a) the GRADED selector still selects (iii) and (b) `dev[iii] = 0.00682 ≤ PASS_BAND = 0.01` (gate still PASSes on (iii)); then Sage-confirm `CF(0.191038/0.112)` has no clean small-denominator convergent (large partial quotient 18) so the `S_0 = 95/56` exact-identity has NO analog at the located value.
2. **Inputs**: `computations/session-101/s101_w3_s0_knob.py`; `s101_envelope_carrier_discriminate.npz` (`legC_output_form=GRADED`, `S0_fit=1.694153`); `canonical_constants.py` (`tau_fold`, `T_acoustic`, `tau_cross_van_hove`); Sage `continued_fraction`.
3. **Gate**: `S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` — PASS iff (selector selects (iii) under GRADED) AND (`dev[iii]^{cross} ≤ 0.01`) AND (`CF(0.191038/0.112)` has a partial quotient ≥ 10 within the first 8 terms, certifying no clean small-denom rational). CONFIRMS the analytic W-1 verdict; CANNOT flip it (the exact-rational asymmetry is regulator-free arithmetic).
4. **Effort**: Small (~15 min: one flag-guarded script edit + one Sage CF call). LOW-priority / CONFIRMATORY. **Depends on**: none.

### 5. CF-S115-AS-NEWAXIS-SELECTOR (OPTIONAL, low-priority)
*(source: `session-114-w4-workingpaper.md` L171–176)*

1. **What**: test whether a functional-determination principle NOT already exhausted by the three {impulse-quench, UNIFIED-AS-79, Parker-adiabatic} functionals (e.g. a maximum-entropy / Jaynes selection on the post-transit occupation, or a Connes-distance-canonical normalization of the relic spectral functional) collapses the 1.2590-OOM cross-functional A_s spread to one value.
2. **Inputs**: `s100b_box_delta_bogoliubov.npz` (the impulse-quench β² spectrum); the three functional A_s literals (impulse +0.864 / UNIFIED +0.196 / Parker +1.455 OOM); a candidate substrate-canonical selector spec.
3. **Gate**: `S115-AS-NEWAXIS-SELECTOR` — PASS = selector collapses the spread → A_s becomes a typed one-functional prediction (retires the §EVOI.BF A_s liability); FAIL = no new-axis selector → FUNCTIONAL-PLURALISM-PERMANENT confirmed on a wider axis-basis.
4. **Effort**: ~1 wave. **Low priority**: §EVOI.BF already prices A_s magnitude as a permanent physical d.o.f.; this WIDENS the no-selector evidence, it does NOT change the headline. A genuine new derivation ⇒ a COMPUTE gate. **Depends on**: none.

### 6. CF-S115-B5A-TFD-QES (OPTIONAL, lowest-priority, Tier-3 NON-BLOCKING)
*(source: `session-114-w4-workingpaper.md` L178–183)*

1. **What**: replace the closed-form linear bracket interpolant `R_TFD = R_edge + f·(R_island − R_edge)` with a full two-sided island quantum-extremal-surface (QES) extremization of `S = Area(∂I)/4 + S_bulk-EE(I)` over the island boundary `∂I`, to test whether the A/4 microstate count is reachable by a NON-causal-patch mechanism (the surviving forward object after the causal-patch corridor closed on both single-sided + two-sided routes).
2. **Inputs**: `s111_b5a_island.npz` (L12 GGE bulk-EE profile, `R_edge`, `R_island`, `A_quarter`, `c_conical`); the L12 D_K spectrum cache for the QES variation.
3. **Gate**: `S115-B5A-TFD-QES` — `|R_QES − 1| ≤ 0.10` PASS / `≤ 0.25` INFO / `> 0.25` FAIL (the standard B5A 3-band).
4. **Effort**: ~1–2 waves (QES extremization is heavier than the interpolant). **Tier-3 NON-BLOCKING** — internal-consistency corridor-narrowing, NOT an observational falsifier (no live falsifier row); LOWEST priority. **Depends on**: none.

---

## Phase 1c-REGISTERS — maintain + consume (this plan-freeze)

### MAINTAIN (effected orchestrator-direct, 2026-06-24)
- **`evoi-framework.md`**: §6 S115 re-stamp (S114 fold → §5 narrative + the 6-gate/3-wave S115 queue); §EVOI.BF A_s axis CONFIRMED FUNCTIONAL-PLURALISM-PERMANENT (W4-1 FAIL) + growth axis (Row #71) = SOLE live non-CMB falsifier; **NEW rank-9f row** `D4-RIGHT-ROOT-SU(3)_R-ADMISSIBILITY` (= CF-S115-HK-1, the EVOI frontier-row add); currency S114→S115; staleness audit re-run → **PASS (lag 0)**.
- **`atlas-08-open-questions.md`**: Q18b S114 freshness bullet (SHAPE-branch wall + D4 genus completion) + backing `registry/atlas-08-freshness-S114.md`.
- **`atlas-04-assumptions.md`**: reconciled IN-SESSION at S114 (housekeeping §A5 — A4/C2-ratio/C10 freshness note, 0 status-cell flips); no new down-tag owed at S115.
- **`open-channel-ledger.md`**: per its §F self-disclosure it REPORTS atlas-04 + EVOI §6 (both refreshed above) rather than body-folding post-S106; no edit owed.
- **mack observational surface** (`falsifier-master-inventory.md` / `falsifier-watchlist.md` / atlas-04 §IX / capstone §7): CURRENT as of S114 in-session (Rows #12/#71/#79/#88 + watchlist landed by mack, housekeeping §A1/§A2/§A8); no plan-time mack dispatch owed.

### CONSUME (register-sourced candidate scan)
**NO additional tractable register candidate beyond the 6 WP CFs.** Consistent with the S107–S114 completion-plateau pattern:
- **K8 §VII.AF.1.STATE-PROJ** (open-channel-ledger §C / EVOI structural cohort) — PENDING-VERIFICATION, no dispatch-ready Stage-2 gate (empty companion slot ⇒ needs a Stage-1 derivation, not a verify). NOT admitted.
- **M_KK-DERIVATION · K_pivot/C2 (now structural-external all 3 legs, S114 W2-1) · residual-3% CC (now confirmed standing q-channel limitation, S114 W2-3) · τ_fold-RELAXATION · A_s floor** — high-leverage standing gaps with no pre-registrable gate (leverage ≠ tractability).
- **branch-iv w₀(L)** — capacity-deferred (~2027 DR3 horizon).
- **Q29 BBN-epoch arm** — unchanged-open; no tractable gate.
- The NEW rank-9f D4-admissibility frontier item IS being discharged by the in-queue `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL`.

The register-sourced D4 frontier row (CF-S115-HK-1) and the §EVOI.BF refresh were plan-time MAINTENANCE (above), NOT compute gates — they carry no verdict line.
