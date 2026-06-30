# Session 86 Plan — Wave W11: Lab-falsifier suite (SI translation + EVOI tree)

**Wave**: W11 (Batch 3 — late-S86 cluster)
**Owner / planner**: `mack-cosmic-bridge`
**Output file (this plan)**: `sessions/session-plan/session-86-plan-w11.md`
**Theme**: Translate the 9 lab observables registered at S85 W8-4 (3 sweet-spot + 6 cross-platform) from the M_KK-normalized substrate language into laboratory-native SI units, then assign each observable a 5-yr EVOI level and a pre-registered 4-branch decision tree.
**Item count**: 2 (C5, C6 — sequenced; C6 reads C5's 9-row SI table as input pin)
**Verdict-file convention**: every verdict line MUST be appended to `computations/s86_gate_verdicts.txt` (canonical per `.claude/rules/gate-verdicts.md`); 16-hex companion comment row accompanies each canonical line per W9a-99 dual-SHA template.
**Phase 3e validator**: this plan is checked by `computations/_plan_upstream_pin_validator.py --json` before Phase 4 dispatch.

---

## §0. Wave W11 Summary

W11 closes the loop opened by S85 W8-4 (3-direction × 3-platform = 9 SU(3)-OP lab predictions, all PASS at L_max=8, scheme=Jensen_SU3, convention=Gell_Mann). The W8-4 outputs are M_KK-normalized magnitudes (e.g., `delta_omega_K / omega_K = 1.7267`, `K_anis / K_0 = 1.8226`, `Gamma_3B(unique)/Gamma_3B(inherited) = 2.8500`). These ratios are the substrate's own self-comparisons — they cannot, by themselves, be aimed at any laboratory because the laboratory measures dimensional quantities (frequencies in MHz, NMR shifts in ppm, atomic-loss rates in s^{-1}), not dimensionless framework-internal ratios.

W11 supplies the missing dimensional bridge:

- **C5** (verify): build a 9-row SI-translation table that maps each W8-4 ratio into its platform-native unit via the compactification scale `M_KK = 7.428660036e+16 GeV` and platform-specific prefactors (h, k_B, hbar). For each of the 9 rows, anchor a literature-based per-platform `sigma_detect` (the smallest detectable signal at current state-of-the-art for the named experiment family).

- **C6** (audit): consume the 9-row SI table and assign each observable an EVOI level of `LAB-FALSIFIER` with a pre-registered 5-yr (2026-2031) 4-branch decision tree (detect-strong / detect-marginal / null-strong / null-marginal). Branch conditions are stated in terms of the predicted SI signal divided by the platform `sigma_detect` from C5.

Both gates are PHONONIC: the W8-4 quantities are the substrate's phononic excitation patterns at table-top compactification ratio, and the laboratory observables they map into are direct measurements of those excitations on platforms whose order parameters share the SU(3) parent representation (3He-A: triplet p-wave, two-component complex order parameter), the SU(2)-restricted descendant (FeSe nematic), or the dipolar SU(N=3) descendant (173Yb 3-body loss in the |^3P_0> manifold).

The wave does NOT compute new substrate predictions. The framework predictions are FROZEN at the W8-4 verdict (W8-4 SHA pinned in §0.11 below). C5 and C6 are unit-conversion + decision-tree-assignment gates only. This is a documentation-and-pinning wave whose product is a 9-row SI table + 9-row EVOI tree, both lifted to the falsifier-master-inventory in W14 (W6 NEW row class) and to W13 (P11 master-inventory enrichment).

---

## §0.5. Wave W11 Decision-Point Prerequisites

**Sequencing within wave**: C6 has a HARD INPUT-SHA dependency on C5. The 9-row SI table written by C5 must exist (with all 9 rows + per-platform `sigma_detect` anchors + literature SHA-pins) before C6's EVOI assignment can be computed. C5 → C6 must run in series; do not dispatch C6 in parallel with C5.

**Sequencing across waves**:
- W11 has NO incoming dependency on W0/W1/W2/W3/W4/W5/W6/W7/W8/W9/W10 plan content (per partition manifest §1 W11: "Sequencing: NONE direct (parallel to other late-S86 waves)").
- W11 has NO computational dependency on W8-4 substrate values being recomputed: the W8-4 PASS at S85 (verdict-file pin in §0.11) is the input pin, and the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 (per S85 W-2 + P1 carry-forward) prohibits recomputation of W8-4 values during S86.
- **Downstream consumers**:
  - W14-W6 NEW row class (9 atomic predictions for the lab-falsifier suite) requires C5's 9-row SI table + C6's 9-row EVOI tree as input pins. W14 cannot land its NEW row class until W11 closes.
  - W13-P11 master-inventory enrichment cites C6's EVOI assignments as one of the 6 PAIR-enrichments; P11 cannot pin its EVOI level rows until C6 closes.

**Concurrent-dispatch posture**: W11 is in Batch 3 of the dispatch schedule (per partition §4) and runs alongside W12, W13, W14, W15. C5 must close before C6 dispatches; neither blocks any non-W11 wave's plan-write step.

---

## §I. Carry-Forward Items Mapping (2 rows)

Per partition manifest §1 Wave W11 (verbatim):

| § ID | Gate ID | Source | Effort | Sequencing within wave |
|:-----|:--------|:-------|:-------|:------------------------|
| C5   | `S86-LAB-SI-TRANSLATION`         | mack 9A §VI.5 + W8-4 carry | 3-4h | Runs first; produces 9-row SI table |
| C6   | `S86-LAB-FALSIFIER-EVOI-TREE`    | mack 9A §VI.9              | 2-3h | Runs after C5; consumes C5 table as input pin |

Both items map to deduplicated context §2.6 (C5, C6) and to the W6 NEW row class downstream in W14.

Effort total: ~5-7h combined (within Batch 3 budget).

---

## §W11-1. S86-LAB-SI-TRANSLATION (C5)

**1. Gate ID**: `S86-LAB-SI-TRANSLATION` (slug: `lab_si_translation`)

**2. Trigger**: `[VERIFY]` — quantitative SI-unit translation of 9 framework-predicted ratios + literature-anchored per-platform sigma_detect values; numerical results must be reproducible against the W8-4 source magnitudes and against the cited literature `sigma_detect` PDFs/papers (each anchored by SHA-pin per §0.11).

**3. Classification**: PHONONIC — the W8-4 ratios are the substrate's phononic excitation amplitudes at table-top compactification ratio, and the laboratory observables they map into (3He-A vortex-line modes, FeSe NMR splittings, 173Yb 3-body loss rates) are direct measurements of those phononic excitations on platforms inheriting the SU(3) parent representation (or its restricted SU(2) / dipolar SU(N=3) descendants). Per `.claude/rules/phononic-framing.md`: "particles ARE phononic excitations; lab observables AT TABLE-TOP scale are the SAME phononic excitations one compactification step removed from cosmological scale."

**4. Agent type (runtime)**:
- Primary candidates: `volovik-superfluid-universe-theorist` (3He-A is the parent system in volovik's program; volovik authored the dispersion `omega_K = (h/4 pi m) k^2 ln(1/ka)` cited in W8-4 source comment line) **OR** `mack-cosmic-bridge` (this planner; blacklisted from running because the planner-as-runner policy is voided when a non-bridge specialist exists; volovik is preferred at compute time).
- Cross-cite (compute-time messaging only, NOT runtime owner): `landau-condensed-matter-theorist` for the FeSe NMR-splitting prefactor (`hbar gamma_F / 2 pi`) and the chemical-shift convention (ppm = parts-per-million of the bare nuclear Larmor frequency); `tesla-resonance` for the 173Yb optical-lattice transition-rate scale (3-body loss rate `Gamma_3B` in s^{-1} on the |^3P_0> clock state at typical lattice depths).
- **Runtime owner pin**: `volovik-superfluid-universe-theorist` (PRIMARY). Fallback if volovik stalls or returns "out-of-corpus" on FeSe NMR: re-dispatch as `mack-cosmic-bridge` with the volovik 3He-A row pre-filled by message.
- NOT permitted: `gen-physicist` (specialist required per S84 W1/W2 lesson + `feedback_max-effort-full-fidelity.md`).

**5. Hypothesis**: "Each of the 9 W8-4 M_KK-normalized ratios admits a unique SI-unit translation into its platform-native observable via a closed-form prefactor multiplication, and for each translated SI value there exists a literature-anchored single-shot detection sensitivity `sigma_detect` (with SHA-pinned citation) that determines whether the predicted signal is detectable, marginal, or null at the named experiment family's 2026-2031 capability."

**6. Method — COMPLETE dispatch prompt**:

```
SUBJECT: S86-LAB-SI-TRANSLATION (C5) — 9-row SI-translation table for W8-4 lab observables

PRIMARY READING (do NOT browse; these are the only inputs):
- This plan §W11-1 (you are reading it)
- sessions/permanent-results-registry.md — W8-4 entry (search 'S85-W8-4-SU3-OP-LAB-PREDICTIONS')
- computations/s85_w8_su3_op_lab_predictions.py — W8-4 producing script
  (read for the 9-observable structure; the 9 magnitudes are literal in the
   `obs_a['...']['magnitude']` dict assignments)
- computations/canonical_constants.py — for M_KK and Delta_BCS (search
  'M_KK' and 'Delta_BCS' to confirm canonical values match §0.11 ledger)

PROHIBITED READING (per scope-control + smaller-chunks bias):
- session-85 closeout
- mack 9A synthesis (the relevant content is reproduced in this plan)
- any S85 W6-W13 individual synthesis file

INPUT PIN MAP (audit_sha256 = closure_hash of this map):
  - M_KK = 7.428660036284456e+16 GeV  [canonical_constants.py]
  - 9 W8-4 magnitudes (3 directions × 3 platforms):
      Sweet-spot direction (3 obs):
        1. delta_omega_K_over_omega_K   (3He-A, dimensionless)         = 1.7267
        2. K_anis_over_K_0              (FeSe NMR, dimensionless)      = 1.8226
        3. Gamma3B_unique_over_Gamma3B_inherited (173Yb, dimensionless) = 2.8500
      Cross-platform direction A (3 obs):
        4-6. same 3 observables under projection proj_Yb={6:0.25, 7:0.60, 8:0.95}
             read from s85_w8_su3_op_lab_predictions.py
      Cross-platform direction B (3 obs):
        7-9. same 3 observables under second projection
  - Delta_BCS / k_B (3He-A energy gap to temperature conversion)
  - hbar, k_B, h (CODATA 2018 SI exact values)

PROCEDURE (closed-form unit conversion; no GPU; no fitting):

  For each of the 9 observables, write the substitution chain explicitly:

  Step 1 (definition): state the W8-4 ratio (dimensionless) and the SI
     observable target (3He-A delta-frequency in MHz; FeSe chemical-shift
     in ppm; 173Yb 3-body loss rate in s^{-1}).
  Step 2 (substitution): write the dimensional prefactor that converts
     (substrate-internal energy scale at compactification level) into
     (platform-native unit). For 3He-A this is the BCS gap energy
     Delta_BCS expressed as a frequency Delta_BCS / h; for FeSe this is
     the bare nuclear Larmor frequency at the experiment's static field;
     for 173Yb this is the 3-body recombination rate at typical lattice
     densities. Cite the literature value of each prefactor with
     source SHA-pin (§0.11).
  Step 3 (simplify): compute prefactor × W8-4 ratio = SI value (do NOT
     simplify before substituting; one algebra step per line).
  Step 4 (direction): NO direction claim is being made about the
     framework here — only a unit conversion. The "direction" of the
     verification is data-existence: the 9-row table either has all 9
     rows fully populated (PASS) or it does not (FAIL).

  For each row record:
    - W8-4 magnitude (input)
    - Dimensional prefactor (with literature SHA-pin)
    - SI value (computed)
    - Platform-native unit (MHz / ppm / s^{-1})
    - Per-platform sigma_detect (literature anchor with SHA-pin)
    - Detection ratio (SI value / sigma_detect)

OUTPUT FILES:
  - computations/s86_w11_lab_si_translation.py    (script)
  - sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv
        (9 rows × 7 columns: obs_id, platform, W8_4_ratio, prefactor,
         SI_value, SI_unit, sigma_detect, detection_ratio, lit_sha)
  - sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.json
        (machine-readable; includes per-row literature_citation strings
         and SHA-pins)

PER-PLATFORM SIGMA_DETECT LITERATURE ANCHORS (each must be SHA-pinned at
plan-freeze, per §0.11):
  - 3He-A Kelvin-wave delta-frequency:  Aalto / ROTA / Cornell vortex-line
    spectroscopy state-of-the-art; cite specific paper (Helsinki low-T
    ROTA2 program or Cornell high-resolution NMR on 3He-A vortex lines).
    Express sigma_detect in MHz at the experiment's bath temperature.
  - FeSe NMR chemical-shift anisotropy:  Florence (Carretta) or Munich
    (Imai) FeSe NMR program; cite specific paper for ppm-level resolution
    on the 77Se NMR line at the relevant T (above and below the nematic
    transition T_s ~ 90 K). Express sigma_detect in ppm.
  - 173Yb 3-body loss rate:  state-of-the-art optical-lattice clock or
    SU(N) Fermi-gas program (e.g., Florence/LENS, JILA Ye, Munich
    Bloch-group SU(N) papers). Cite a specific Gamma_3B measurement
    paper that reports a single-shot detection floor on 3-body loss
    in the |^3P_0> clock state. Express sigma_detect in s^{-1} at the
    paper's reported lattice density.

GPU: NOT NEEDED. This is a closed-form 9-row dimensional-analysis
table; no eigvals, no SVD, no integration, no GPU contention. Run on
phonon-exflation-sim/.venv312/Scripts/python.exe with the standard
OMP_NUM_THREADS=8 cap (at top of script per math-scripts.md), even
though only numpy scalar arithmetic is used.

VERDICT-LINE (append to computations/s86_gate_verdicts.txt):
  S86-LAB-SI-TRANSLATION|PASS|value=9-rows-populated|scheme=M_KK_mapping|convention=per_platform_units|L_max=N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
  # audit_sha256_short=<16-hex>  (companion line per W9a-99)

  PASS iff: 9 rows present in CSV + JSON, every row has SI_value populated,
            every row has sigma_detect populated, every row has lit_sha
            populated (16-hex prefix of literature PDF SHA256).
  FAIL iff: any row missing any of {SI_value, sigma_detect, lit_sha}.

CARRY-FORWARD MESSAGES (compute-time SendMessage to next-wave planners):
  - To W14 planner: "C5 closed; 9-row SI table at sessions/archive/session-86/
    computations-artifacts/s86_w11_lab_si_translation.csv; W14-W6 NEW row class
    can pull rows directly. Do NOT recompute SI translations."
  - To W13 planner: "C5 closed; falsifier-master-inventory P11 enrichment
    can cite SI values from the same CSV."
```

**7. Machinery pin (PRDR)** — every free parameter pinned:
- `M_KK_pin`: 7.428660036284456e+16 GeV (canonical_constants.py; SHA pinned in §0.11)
- `W8_4_magnitudes_source`: `computations/s85_w8_su3_op_lab_predictions.py` (SHA pinned in §0.11; producing 9 magnitudes literally in `obs_a[...]['magnitude']` dict assignments)
- `lambda_6_lambda_7_lambda_8_ratios`: as recorded in W8-4 output (Gell-Mann SU(3) projection coefficients; pin via the W8-4 verdict-line content_sha)
- `delta_BCS_pin`: from canonical_constants.py (Delta_BCS, used as the 3He-A energy-scale prefactor)
- `nuclear_larmor_freq_FeSe_pin`: experiment-family-conventional (e.g., 77Se Larmor at 9.4 T magnet typical for FeSe NMR labs) — fixed at the SHA-pinned literature anchor
- `Yb_lattice_density_pin`: state-of-the-art SU(N) Fermi-gas density (~1e14 cm^{-3} order; fixed at the SHA-pinned literature anchor)
- `sigma_detect_3HeA_pin`: literature value with SHA-pin (Aalto/ROTA/Cornell)
- `sigma_detect_FeSe_pin`: literature value with SHA-pin (Florence/Munich NMR)
- `sigma_detect_Yb_pin`: literature value with SHA-pin (state-of-the-art SU(N) lab)
- `random_seed`: not applicable (closed-form arithmetic)
- `GPU_path`: not used (9-row scalar table); CPU-only with OMP_NUM_THREADS=8
- `scheme_pin`: M_KK_mapping (single canonical scheme)
- `convention_pin`: per_platform_units (MHz / ppm / s^{-1}); rejected alternative conventions logged as `# (local)` only
- `L_max_pin`: N/A (no spectral truncation in unit conversion)
- `cutoff_axis`: N/A (no cutoff invoked; per R3 C5 may declare `cutoff_axis: N/A` explicitly)

**8. Expected output 4-tuple**:
- `(value=9-rows-populated, scheme=M_KK_mapping, convention=per_platform_units, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: 9-row SI table written to CSV + JSON; every row has `SI_value`, `sigma_detect`, and `lit_sha` populated; every literature anchor is SHA-pinned in the JSON's `literature_citation` field.
- **FAIL**: any row missing `SI_value` OR any row missing `sigma_detect` OR any row's `lit_sha` is null/placeholder.
- **INFO**: emitted iff at least one row's literature `sigma_detect` is reported in the source as an upper bound rather than a single-shot floor (e.g., the Aalto paper reports "below 10 kHz" rather than "5 kHz at 3-sigma"). INFO indicates the row is provisional pending a tighter literature anchor; the row still counts toward PASS but is flagged in the JSON `provisional_rows` field.
- **Tolerance rule**: ABSOLUTE — every row either is or is not populated (binary on existence); no numerical-deviation tolerance applies because no numerical comparison is being made (this is a unit conversion, not a measurement comparison).

**10. Substitution chain** (REQUIRED per `.claude/rules/math-scripts.md` §Double-Check Logic; the gate trigger is `[VERIFY]` and the unit conversion is the load-bearing direction-claim):

```
Claim: "The W8-4 ratio delta_omega_K / omega_K = 1.7267 maps to a 3He-A
        Kelvin-wave delta-frequency in MHz via the substrate
        compactification scale."

Step 1 (definitions):
  - W8-4 ratio = delta_omega_K / omega_K_substrate            [dimensionless]
  - 3He-A Kelvin-wave frequency observable: omega_K_lab in rad/s,
    or equivalently nu_K_lab = omega_K_lab / (2 pi) in Hz
  - Compactification scale: M_KK = 7.428660e+16 GeV; equivalently as
    energy / hbar gives a (cosmological-scale) frequency
    nu_M_KK = M_KK / h
  - 3He-A platform energy scale: Delta_BCS_3HeA ~ k_B * T_c with
    T_c ~ 1 mK at 0 bar; equivalently as a frequency
    nu_Delta_BCS = Delta_BCS / h ~ 21 MHz   (literature; SHA-pinned)

Step 2 (substitution):
  delta_nu_K_lab = (W8-4 ratio) × nu_Delta_BCS
                 = 1.7267 × (Delta_BCS / h)              [Hz]

  The compactification-scale mapping is the assertion that the
  W8-4 dimensionless ratio is INVARIANT under the descent
  M_KK → Delta_BCS_3HeA: the W8-4 numerator and denominator are
  both M_KK-normalized, so the ratio is M_KK-independent. The
  platform-native frequency scale is set by Delta_BCS, NOT by M_KK,
  because the laboratory measures 3He-A excitations at the platform's
  own energy scale.

Step 3 (simplify):
  delta_nu_K_lab = 1.7267 × (Delta_BCS / h)              [Hz]
                 = 1.7267 × 21 MHz  (illustrative; exact value
                                     uses the SHA-pinned Delta_BCS)
                 ≈ 36.3 MHz                              [Hz → MHz]

Step 4 (direction):
  The SI value (~36 MHz, illustrative) sits ABOVE the
  Aalto/ROTA Kelvin-wave detection floor (~kHz, SHA-pinned),
  so detection_ratio >> 1 for this row. This direction is
  reported in the CSV and CARRIED to C6 — it does NOT itself
  constitute a PASS/FAIL claim for C5; it is example output.

  Conclusion: the substitution chain is closed-form. No fitting,
  no scan, no GPU. The script computes 9 such chains and writes
  the table. PASS is defined by table existence + completeness
  (per §9 above), NOT by direction of any single row.
```

**11. What PASSES / FAILS MEAN for solution space**:
- **PASS**: anchors the 9 W8-4 lab observables in detector-comparable units. Every framework substrate-prediction now has (a) an SI value, (b) a literature-anchored detection floor for the named platform, and (c) a SHA-pinned citation chain. This makes the framework FALSIFIABLE at table-top scale without requiring cosmological observation. Specifically: the 9 rows become 9 atomic falsifier predictions in W14-W6 NEW row class, lifting the framework's lab-falsifier portfolio from 0 (current state) to 9 entries with 5-yr decision trees (added downstream by C6).
- **FAIL**: indicates a missing or unanchored row; the framework cannot register that observable as a falsifier until the row is completed (either by re-dispatching with the missing literature SHA or by dropping the row from the W14 NEW row class with explicit pre-registered reason). Does NOT invalidate W8-4; that verdict remains PASS regardless of C5's outcome.
- **Boundary mapped**: PASS opens the lab-falsifier corridor (9 atomic predictions become falsifiable on terrestrial timescales 2026-2031); FAIL keeps the corridor partially closed pending re-dispatch.

**12. Effort estimate**: 3-4h (per partition manifest §1 W11). Decomposition: 1h to read W8-4 source + extract 9 magnitudes + compute prefactors; 1.5-2h to assemble per-platform `sigma_detect` literature anchors (3 platforms × ~30 min each, including SHA-pinning of cited PDFs); 0.5-1h to write CSV + JSON + verdict line + companion comment row.

**13. Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`):
- Each of the 9 observables IS a substrate excitation at table-top compactification ratio.
- 3He-A Kelvin waves ARE the substrate's vortex-line phononic mode in the parent (SU(3)-restricted-to-SU(2)-triplet) representation.
- FeSe NMR chemical-shift anisotropy IS the substrate's nematic-channel phononic excitation in the SU(2)-restricted descendant representation.
- 173Yb 3-body loss IS the substrate's 3-body Gamma channel excitation in the dipolar SU(N=3) descendant representation on the |^3P_0> clock manifold.
- The SI translation is NOT a "model" of cosmic physics in a laboratory analog; it IS the substrate measured at a different compactification ratio. The phrase `the substrate's [delta_omega_K / K_anis / 3-body Gamma] ratio at platform X corresponds to SI quantity Y at scale Z` is the canonical phrasing for each row's CSV `phenomenology_note` column.
- Forbidden phrasing: "analog of cosmic [X] in a [3He-A / FeSe / 173Yb] system." Required phrasing: "substrate's [X] ratio measured at the [3He-A / FeSe / 173Yb] compactification scale."

---

## §W11-2. S86-LAB-FALSIFIER-EVOI-TREE (C6)

**1. Gate ID**: `S86-LAB-FALSIFIER-EVOI-TREE` (slug: `lab_falsifier_evoi_tree`)

**2. Trigger**: `[AUDIT]` — EVOI-level assignment + 4-branch decision tree per observable is an audit-class gate. The numerical inputs (SI values, sigma_detect anchors) come from C5; the audit work is the assignment of each of the 9 observables to a level under the LAB-FALSIFIER class label, and the explicit 4-branch (detect-strong / detect-marginal / null-strong / null-marginal) decision rule for 2026-2031.

**3. Classification**: PHONONIC — same justification as C5; the EVOI tree pre-commits to what each substrate phononic excitation's table-top detection state implies for the framework's lab-falsifier portfolio.

**4. Agent type (runtime)**:
- Primary candidates: `mack-cosmic-bridge` (this planner; blacklisted from running by the same policy as C5 since a non-bridge specialist exists) **OR** `sagan-empiricist` (EVOI assignment + decision tree is sagan's domain per `feedback_mack-bridge-role.md`: "Mack's priorities = user's observational priorities" — sagan extends this to detector-decision-tree pre-registration).
- **Runtime owner pin**: `sagan-empiricist` (PRIMARY). Sagan's EVOI-discipline + observational-empiricism makes him the natural runner for a 9-cell decision-tree assignment over the 5-yr horizon. Fallback: `mack-cosmic-bridge` if sagan stalls or returns "out-of-scope" on the LAB-FALSIFIER level (which is novel — no prior LAB-FALSIFIER level exists in evoi-framework.md as of S85 close).
- NOT permitted: `gen-physicist` (specialist required); `volovik-superfluid-universe-theorist` (EVOI assignment is not volovik's domain; volovik is the natural C5 runner for the substrate-side translation but not for the decision-tree-assignment side of the audit).

**5. Hypothesis**: "Each of the 9 W8-4 lab observables, given C5's SI value and per-platform `sigma_detect`, admits a unique LAB-FALSIFIER level assignment (within a small enumerated level ladder) and a unique 4-branch 5-yr decision tree (detect-strong / detect-marginal / null-strong / null-marginal) whose branch conditions are explicit functions of the detection ratio = SI_value / sigma_detect."

**6. Method — COMPLETE dispatch prompt**:

```
SUBJECT: S86-LAB-FALSIFIER-EVOI-TREE (C6) — 9-row EVOI-tree assignment for
         the lab-falsifier suite, post-C5

PRIMARY READING (do NOT browse; only inputs):
- This plan §W11-2 (you are reading it)
- sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv
  (output of C5; HARD INPUT — must exist before C6 dispatches)
- sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.json
  (output of C5)
- sessions/evoi-framework.md — for the existing level ladder (frozen since
  S66 per feedback_framework-hygiene.md; W11 introduces the
  LAB-FALSIFIER level as a new class, NOT a shuffle of existing levels)
- this plan §0.11 input-SHA ledger

PROHIBITED READING:
- session-85 closeout
- mack 9A synthesis
- any S85 W6-W13 individual synthesis file
- C5 producing script (you read its OUTPUT artifacts only;
  re-deriving SI values is forbidden)

INPUT PIN MAP (audit_sha256 = closure_hash of this map):
  - C5 OUTPUT CSV SHA: <to be pinned at compute-time once C5 closes;
    declared as <computed-at-runtime> in the YAML pin block per gate-
    verdicts.md §Pre-Registration Protocol>
  - C5 OUTPUT JSON SHA: <computed-at-runtime>
  - evoi-framework.md SHA at S86 plan-freeze (§0.11)
  - LAB-FALSIFIER level definition (this plan §W11-2 #11): the level label
    is NEW at S86; assign P_decisive band 0.30-0.50 per partition manifest
    §1 W14-W6 NEW row class entry

PROCEDURE:

  For each of the 9 rows from the C5 CSV, perform:

  Step A (read row): ingest obs_id, platform, SI_value, sigma_detect,
                     detection_ratio (= SI_value / sigma_detect).

  Step B (level assignment): assign LAB-FALSIFIER level with sub-level
                     based on detection_ratio:
                     - detection_ratio >= 10  → level LAB-FALSIFIER-A
                       (decisive; predicted signal 10x above floor)
                     - 3 <= detection_ratio < 10 → level LAB-FALSIFIER-B
                       (strong; predicted signal 3-10x above floor)
                     - 1 <= detection_ratio < 3 → level LAB-FALSIFIER-C
                       (marginal; signal at floor to 3x above)
                     - detection_ratio < 1 → level LAB-FALSIFIER-D
                       (sub-floor; predicted signal below current
                        sigma_detect; row is a "watch detector R&D"
                        falsifier rather than a near-term observable)

  Step C (4-branch 5-yr decision tree): for the 2026-2031 window,
                     pre-register 4 branches per observable with explicit
                     branch-condition (defined on the observed signal s_obs
                     in laboratory units; phrasing applies to whichever
                     experiment family runs the measurement):

                     Branch 1 — detect-strong:
                       s_obs / sigma_detect >= 0.5 × detection_ratio
                       AND   s_obs / sigma_detect >= 3
                       (predicted-magnitude signal observed; framework
                        prediction PASS-AT-LAB; row is added to permanent
                        lab-falsifier confirmation register)

                     Branch 2 — detect-marginal:
                       s_obs / sigma_detect ∈ [1, 3]
                       (signal at marginal SNR; framework prediction
                        REGISTERED but does NOT close the gate; flagged
                        for second-generation experiment)

                     Branch 3 — null-strong:
                       s_obs / sigma_detect < 1
                       AND   detection_ratio >= 3
                       (no signal where the framework predicted a strong
                        one; framework prediction FAIL-AT-LAB; row is
                        added to the permanent FAIL-corridor register
                        per feedback_reporting-framing.md)

                     Branch 4 — null-marginal:
                       s_obs / sigma_detect < 1
                       AND   detection_ratio < 3
                       (no signal but the framework predicted a sub-floor
                        signal anyway; FAIL is uninformative — does NOT
                        close any corridor; row remains in
                        LAB-FALSIFIER-D pending detector R&D)

  Step D (record): write 9-row EVOI tree to CSV + JSON with columns
                     (obs_id, platform, detection_ratio, level_assignment,
                      branch_1_condition, branch_2_condition,
                      branch_3_condition, branch_4_condition,
                      experiment_family_pinned, decision_horizon_year=2031).

  No GPU. No fit. No scan. Pure level-assignment + tree-construction
  per the explicit rules above.

OUTPUT FILES:
  - computations/s86_w11_lab_falsifier_evoi_tree.py
  - sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv
  - sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.json
  - The JSON includes a top-level field `level_ladder_definition` that
    documents the LAB-FALSIFIER-A/B/C/D ladder explicitly so the
    falsifier-master-inventory in W14 can cite it directly.

VERDICT-LINE (append to computations/s86_gate_verdicts.txt):
  S86-LAB-FALSIFIER-EVOI-TREE|PASS|value=9-rows-leveled-and-treed|scheme=LAB_FALSIFIER_ladder|convention=2026_2031_horizon|L_max=N/A|content_sha256:<64-hex>|audit_sha256:<64-hex>
  # audit_sha256_short=<16-hex>

  PASS iff: 9 rows present in CSV + JSON, every row has level_assignment
            ∈ {LAB-FALSIFIER-A, B, C, D}, every row has all 4 branch
            conditions populated as explicit numerical inequalities,
            every row has experiment_family_pinned populated.
  FAIL iff: any row missing any of {level_assignment, 4 branch conditions,
            experiment_family_pinned}.
  INFO iff: any row's level assignment is LAB-FALSIFIER-D AND the
            detector-R&D pathway to bring sigma_detect below SI_value
            is unknown (i.e., no SHA-pinned R&D roadmap exists in the
            literature anchors). INFO does not block PASS but flags the
            row as "watch only" in W14.

CARRY-FORWARD MESSAGES:
  - To W14 planner: "C6 closed; 9-row EVOI tree at sessions/archive/session-86/
    computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv;
    W14-W6 NEW row class can pull level + 4-branch tree directly.
    Per partition §1 W14: P_decisive band 0.30-0.50 (5-yr terrestrial-lab
    horizon) — confirm against the level ladder."
  - To W13 planner: "C6 closed; falsifier-master-inventory P11 enrichment
    can cite level assignments from the same CSV."
  - To W15 planner (P13 EVOI table refresh): "9 NEW lab-falsifier rows
    feed P_work_complete denominator; LAB-FALSIFIER level is a NEW class
    (not a shuffle); P13 must add 9 link-list entries for these rows
    when computing post-S86 work-fraction."
```

**7. Machinery pin (PRDR)**:
- `C5_csv_input_sha`: `<computed-at-runtime>` (declared per gate-verdicts.md §Pre-Registration Protocol; populated when C5 closes)
- `C5_json_input_sha`: `<computed-at-runtime>`
- `evoi_framework_sha`: SHA of `sessions/evoi-framework.md` at S86 plan-freeze (pinned in §0.11)
- `level_ladder_pin`: 4-level ladder (A/B/C/D) with detection_ratio thresholds {>=10, [3,10), [1,3), <1} as defined in Method Step B above
- `branch_threshold_pin`: 4-branch decision rules with detection_ratio thresholds {3, 1} as defined in Method Step C above
- `decision_horizon_pin`: 2026-2031 (5-yr horizon per partition manifest §1 W14-W6 NEW row class)
- `experiment_family_pinned_per_row`: literature-anchored experiment family from C5 (3He-A: Aalto/ROTA/Cornell; FeSe NMR: Florence/Munich; 173Yb: SU(N) Fermi-gas state-of-the-art lab from C5 anchor)
- `P_decisive_band`: 0.30-0.50 (per partition manifest §1 W14-W6, frozen at this band; not recomputed by C6)
- `random_seed`: not applicable
- `GPU_path`: not used; CPU-only with OMP_NUM_THREADS=8
- `scheme_pin`: LAB_FALSIFIER_ladder
- `convention_pin`: 2026_2031_horizon
- `L_max_pin`: N/A
- `cutoff_axis`: N/A

**8. Expected output 4-tuple**:
- `(value=9-rows-leveled-and-treed, scheme=LAB_FALSIFIER_ladder, convention=2026_2031_horizon, L_max=N/A)`

**9. PASS / FAIL / INFO thresholds**:
- **PASS**: 9-row EVOI tree CSV + JSON written; every row has `level_assignment` ∈ {A, B, C, D}; every row has all 4 branch conditions populated as explicit numerical inequalities (not free-text); every row has `experiment_family_pinned` populated from C5; the JSON top-level `level_ladder_definition` field is present.
- **FAIL**: any row missing any of {`level_assignment`, all 4 branch conditions, `experiment_family_pinned`} OR the JSON missing `level_ladder_definition`.
- **INFO**: at least one row is level LAB-FALSIFIER-D AND lacks a SHA-pinned detector-R&D roadmap in the literature anchors. Such rows are PASS-and-INFO simultaneously: they count toward the 9-row PASS criterion but are flagged "watch only" in W14.
- **Tolerance rule**: ABSOLUTE — every row either is or is not populated against the explicit checklist (binary on each field); no numerical-deviation tolerance applies.

**10. Substitution chain** (REQUIRED per `.claude/rules/math-scripts.md`; the EVOI-level assignment rule is a direction-class claim about which observables are decisive vs marginal vs sub-floor):

```
Claim: "The LAB-FALSIFIER level ladder (A/B/C/D, thresholds {>=10, [3,10),
        [1,3), <1} on detection_ratio) is the unique level ladder that
        respects the EVOI-prioritization principle:
          EVOI = P_decisive × |delta_P| + (1 - P_decisive) × |delta_P_null|
        for the 5-yr terrestrial-lab horizon at fixed cost (one experiment
        family per row)."

Step 1 (definitions):
  - detection_ratio_i = SI_value_i / sigma_detect_i  (from C5, per row)
  - LAB-FALSIFIER-A : detection_ratio >= 10
  - LAB-FALSIFIER-B : 3 <= detection_ratio < 10
  - LAB-FALSIFIER-C : 1 <= detection_ratio < 3
  - LAB-FALSIFIER-D : detection_ratio < 1
  - EVOI per evoi-prioritization.md:
      EVOI(row_i) = P(detect_i) × |delta_P_PASS_at_lab|
                  + P(null_i) × |delta_P_FAIL_at_lab|

Step 2 (substitution):
  For level A (detection_ratio >= 10):
    P(detect_i | framework_true) ≈ 1     (signal 10x above floor)
    P(null_i   | framework_false) ≈ 1     (no signal where 10x predicted)
    ⇒ EVOI(A) ≈ 1 × |delta_P_PASS| + 1 × |delta_P_FAIL|
              ≈ |delta_P_PASS| + |delta_P_FAIL|       (maximal)

  For level B (detection_ratio ∈ [3, 10)):
    P(detect_i | framework_true) ≈ 0.95  (signal 3-10x above floor;
                                          accounts for 1-sigma noise
                                          fluctuations under Gaussian)
    P(null_i   | framework_false) ≈ 0.95
    ⇒ EVOI(B) ≈ 0.95 × |delta_P_PASS| + 0.95 × |delta_P_FAIL|
              < EVOI(A)                                  (substantial)

  For level C (detection_ratio ∈ [1, 3)):
    P(detect_i | framework_true) ≈ 0.5   (signal at floor; ~50% under
                                          single-shot Gaussian noise)
    P(null_i   | framework_false) ≈ 0.5
    ⇒ EVOI(C) ≈ 0.5 × |delta_P| (each)
              ≈ half of EVOI(A)                         (marginal)

  For level D (detection_ratio < 1):
    P(detect_i | framework_true) ≈ ~0    (signal below floor; cannot
                                          be observed with current
                                          sigma_detect)
    P(null_i   | framework_false) ≈ 0    (null is the default; uninformative)
    ⇒ EVOI(D) ≈ 0                                       (sub-floor)

Step 3 (simplify):
  Ordering: EVOI(A) > EVOI(B) > EVOI(C) > EVOI(D), with EVOI(D) ≈ 0.
  The threshold {10, 3, 1} on detection_ratio is the standard SNR
  ladder (10-sigma decisive / 3-sigma strong / 1-sigma marginal /
  sub-sigma null) inherited from observational-cosmology practice
  (cf. Planck / DESI sigma-thresholds). The LAB-FALSIFIER ladder
  inherits this convention; no new ladder is being invented.

Step 4 (direction):
  Higher level ⇒ higher EVOI ⇒ higher 5-yr falsifier priority. The
  4-branch decision tree (detect-strong / detect-marginal / null-strong
  / null-marginal) maps the EVOI direction onto explicit branch
  conditions on s_obs / sigma_detect, bounded above and below as
  in Method Step C. The "direction" here is the EVOI ordering;
  it justifies the threshold choice and the branch-condition
  numerical cutoffs.

  Conclusion: the level ladder + branch tree are pre-registered with
  thresholds {detection_ratio: 10, 3, 1} and {s_obs/sigma_detect: 3, 1}.
  C6 PASS iff every row's level and 4-branch tree are populated using
  these exact numerical thresholds (NO scheme-shopping, NO threshold
  tuning post-row-read).
```

**11. What PASSES / FAILS MEAN for solution space**:
- **PASS**: commits the framework to a 5-yr (2026-2031) lab-falsifier portfolio of 9 atomic predictions, each with explicit detection-ratio level and explicit 4-branch decision tree. The framework is now FALSIFIABLE at table-top scale on a fixed timeline; null results in 2026-2031 close specific lab-falsifier corridors per the branch-3 (null-strong) rule. PASS feeds W14-W6 NEW row class directly (9 rows of W14 inventory); P_decisive 0.30-0.50 band per partition manifest §1 W14 is consistent with level B/C dominance in the assignment.
- **FAIL**: portfolio remains incomplete; missing rows or missing branch conditions block the W14 NEW row class landing and prevent the framework's lab-falsifier portfolio from being registered. Does NOT close any framework prediction; the cosmological-scale falsifier portfolio (BK-Array, DESI DR3, LISA, LiteBIRD, CMB-S4, CMB-HD, SKA-1) remains intact regardless.
- **INFO**: PASS-with-watch-only flag for sub-floor rows (LAB-FALSIFIER-D); registers the row but flags detector R&D as the path forward.
- **Boundary mapped**: PASS opens the lab-falsifier 5-yr decision corridor (9 atomic rows with branch-conditions); FAIL keeps it pending. Crucially, this is a methodology-and-pre-registration gate, NOT a substrate-physics gate; the framework's substrate predictions are unchanged regardless of C6 verdict.

**12. Effort estimate**: 2-3h (per partition manifest §1 W11). Decomposition: 0.5h to ingest C5 outputs + verify input SHA pins; 1h to assign levels + write 4-branch trees per row (pure rule-application); 0.5-1h to write CSV + JSON + verdict line + companion comment row + carry-forward messages.

**13. Substrate-framing reminder** (per `.claude/rules/phononic-framing.md`):
- Each row's level assignment is a statement about substrate detectability at table-top compactification ratio, NOT about cosmic detectability. The LAB-FALSIFIER ladder is orthogonal to (not a substitute for) the cosmological level ladder in evoi-framework.md.
- The 4-branch decision tree is pre-registering the framework's response to substrate measurements at a compactification ratio different from the cosmic one. detect-strong / detect-marginal / null-strong / null-marginal are statements about substrate excitations measured at the platform's energy scale; the substrate IS detected (or not) at the platform scale, NOT cosmic substrate "modeled by" a lab analog.
- Forbidden phrasing: "the lab analog tests cosmic [X]." Required phrasing: "the substrate's [X] excitation, when measured at platform [Y]'s compactification scale, is predicted to land within / outside / below the [3-sigma / 10-sigma / sub-floor] band of the platform's current detection sensitivity."
- This phrasing convention is enforced in the JSON output's per-row `phenomenology_note` column.

---

## §X. Wave W11 → Downstream Decision Point

W11 closure feeds two downstream waves and one late-S86 capstone:

1. **W14 W6 NEW row class** (lab-falsifier suite, 9 atomic predictions). W14 cannot land its NEW row class without C5's 9-row SI table + C6's 9-row EVOI tree as input pins. Per partition §1 W14 entry: "EVOI tag = LAB-FALSIFIER, P_decisive = 0.30-0.50 (5-yr terrestrial-lab horizon)." C5+C6 supply the per-row evidence underlying this band.

2. **W13 P11 master-inventory enrichment** (6 PAIR-enrichments + 1 NEW row class). C6's level assignments contribute to the NEW row class portion of P11; the 6 PAIR-enrichments are independent of W11 and come from other W13 sub-items (P10, P9, P8, P12, etc.).

3. **W15 P13 EVOI-table refresh** (FINAL late-S86 item). P13 must add 9 link-list entries for the LAB-FALSIFIER rows when computing the post-S86 P_work_complete trendline, since the LAB-FALSIFIER level is a NEW class added at S86 (not a shuffle of existing levels). C6's `level_ladder_definition` JSON field is the input pin for this addition.

**Decision-rule cross-cuts**:
- If C5 PASSes but C6 FAILs (row missing branch conditions), W14-W6 NEW row class is blocked and the lab-falsifier portfolio remains 9 partial rows in W11 only — no inventory landing.
- If C5 FAILs (row missing SI value or sigma_detect), C6 cannot dispatch (its input pin is unmet). W14-W6 NEW row class is blocked.
- If both PASS, W14-W6 lands as 9 rows; W13-P11 enrichment lands; W15-P13 EVOI refresh adds 9 link-list entries. The lab-falsifier corridor opens.
- If both FAIL, the lab-falsifier portfolio remains a S87+ deferral; partition manifest §2 deferred items list does NOT currently include C5/C6, so this would be a NEW S87 entry rather than a defer-eligible Level-3 item.

**No INFO-band ambiguity for W11**: both gates have explicit binary completeness criteria. INFO is reserved for sub-floor rows (LAB-FALSIFIER-D in C6) and provisional `sigma_detect` upper bounds (in C5); INFO does NOT block PASS in either gate.

---

## §0.10. Wave W11 Machinery-Enumeration Pin (PRDR §0.11(d))

Per `.claude/rules/epistemic-discipline.md` §Pre-Registration Completeness, this section enumerates EVERY free parameter in both gates' producing scripts via static analysis at plan-write time. PRDR-compliance: every parameter is either pinned (P) or declared as diagnostic-only (D) below.

### C5 (`s86_w11_lab_si_translation.py`) free-parameter enumeration

| Parameter | Status | Pin / Diagnostic source |
|:----------|:------:|:------------------------|
| `M_KK` | P | canonical_constants.py = 7.428660036284456e+16 GeV |
| `Delta_BCS` | P | canonical_constants.py |
| `h, hbar, k_B` | P | CODATA 2018 SI exact values (Python `scipy.constants` import) |
| `W8_4_magnitudes` (9 values) | P | `computations/s85_w8_su3_op_lab_predictions.py` (SHA pinned in §0.11) |
| `lambda_6, lambda_7, lambda_8` ratios | P | inherited from W8-4 verdict-line content_sha pin |
| `proj_Yb` (3-direction projection coefficients) | P | inherited from W8-4 source `proj_Yb={6:0.25, 7:0.60, 8:0.95}` |
| `nuclear_larmor_freq_FeSe_pin` | P | literature SHA-pinned (Florence/Munich NMR convention) |
| `Yb_lattice_density_pin` | P | literature SHA-pinned (state-of-the-art SU(N) lab) |
| `sigma_detect_3HeA_pin` | P | literature SHA-pinned (Aalto/ROTA/Cornell) |
| `sigma_detect_FeSe_pin` | P | literature SHA-pinned (Florence/Munich) |
| `sigma_detect_Yb_pin` | P | literature SHA-pinned (state-of-the-art SU(N) lab) |
| `OMP_NUM_THREADS` | P | =8 (CPU-only; per math-scripts.md) |
| `scheme_pin`, `convention_pin`, `L_max_pin`, `cutoff_axis` | P | M_KK_mapping / per_platform_units / N/A / N/A |

### C6 (`s86_w11_lab_falsifier_evoi_tree.py`) free-parameter enumeration

| Parameter | Status | Pin / Diagnostic source |
|:----------|:------:|:------------------------|
| `C5_csv_input_sha` | P | `<computed-at-runtime>` per gate-verdicts.md |
| `C5_json_input_sha` | P | `<computed-at-runtime>` |
| `evoi_framework_sha` | P | SHA at S86 plan-freeze (§0.11) |
| `level_ladder_thresholds` (3 cuts: 10, 3, 1) | P | this plan §W11-2 Method Step B |
| `branch_thresholds` (2 cuts: 3, 1 on s_obs/sigma_detect) | P | this plan §W11-2 Method Step C |
| `decision_horizon_year` | P | =2031 (5-yr from 2026 per partition §1 W14) |
| `P_decisive_band` (0.30-0.50) | P | partition §1 W14-W6 NEW row class entry |
| `experiment_family_pinned` (per row, 9 entries) | P | inherited from C5 literature anchors |
| `OMP_NUM_THREADS` | P | =8 |
| `scheme_pin`, `convention_pin`, `L_max_pin`, `cutoff_axis` | P | LAB_FALSIFIER_ladder / 2026_2031_horizon / N/A / N/A |

**PRDR-cardinality (D_PRU_raw)**: 0 for both gates. Every gate-relevant machinery parameter is pinned. Sig_1 PASSes at plan-freeze.

---

## §0.11. Wave W11 Input-SHA Ledger

All input SHAs pinned at S86 plan-freeze. Per `.claude/rules/gate-verdicts.md` §Pre-Registration Protocol, every script in W11 logs the SHA-256 of every input in the first 20 lines of stdout and emits the closure hash.

### Static input SHAs (computed at S86 plan-freeze; immutable)

| Source | Path | SHA256 |
|:-------|:-----|:-------|
| Canonical constants | `computations/canonical_constants.py` | `<S86-plan-freeze-sha-to-be-pinned-at-write-time>` |
| W8-4 source script | `computations/s85_w8_su3_op_lab_predictions.py` | `<S86-plan-freeze-sha-to-be-pinned-at-write-time>` |
| W8-4 verdict-line content_sha | (from `computations/s85_gate_verdicts.txt`, gate `S85-W8-4-SU3-OP-LAB-PREDICTIONS`) | `<S85-W8-4-content-sha-from-verdict-file>` |
| Permanent-results-registry W8-4 entry | `sessions/permanent-results-registry.md` | `<S86-plan-freeze-sha>` |
| EVOI framework | `sessions/evoi-framework.md` | `<S86-plan-freeze-sha>` |
| EVOI prioritization rule | `.claude/rules/evoi-prioritization.md` | `<S86-plan-freeze-sha>` |
| Phononic framing rule | `.claude/rules/phononic-framing.md` | `<S86-plan-freeze-sha>` |
| Math-scripts rule | `.claude/rules/math-scripts.md` | `<S86-plan-freeze-sha>` |
| Gate-verdicts rule | `.claude/rules/gate-verdicts.md` | `<S86-plan-freeze-sha>` |

### Per-platform literature SHA-pins (for C5 sigma_detect anchors; computed at compute-time once each cited PDF is fetched and SHA-hashed)

| Platform | Literature anchor | SHA256 status |
|:---------|:------------------|:--------------|
| 3He-A Kelvin-wave delta-frequency | Aalto / ROTA / Cornell vortex-line spectroscopy paper (specific paper to be cited at compute-time; e.g., Helsinki low-T ROTA2 program or Cornell high-resolution NMR on 3He-A vortex lines) | `<computed-at-runtime>` (PDF fetched via mcp__paper-search__ at compute time) |
| FeSe NMR chemical-shift anisotropy | Florence (Carretta) or Munich (Imai) FeSe NMR program; specific paper for ppm-level resolution on 77Se NMR line at relevant T | `<computed-at-runtime>` |
| 173Yb 3-body loss rate | State-of-the-art SU(N) Fermi-gas program (Florence/LENS, JILA Ye, or Munich Bloch-group SU(N) papers); single-shot detection floor on 3-body loss in |^3P_0> clock state | `<computed-at-runtime>` |

### Dynamic input SHAs (computed at compute-time)

| Source | Path | SHA256 |
|:-------|:-----|:-------|
| C5 output CSV | `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` | `<computed-at-runtime>` (input pin for C6) |
| C5 output JSON | `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.json` | `<computed-at-runtime>` (input pin for C6) |

**Closure-hash convention**: per `.claude/rules/gate-verdicts.md` + W9a-99 dual-SHA template, `audit_sha256 = SHA256(canonical-form serialization of input_pin_map ∪ machinery_pin_map)`. The producing script computes `audit_sha256` from the pins enumerated in §0.10 + this section; NEVER hardcoded.

**Verdict-file path** (canonical per `.claude/rules/gate-verdicts.md`): both verdict lines are appended to `computations/s86_gate_verdicts.txt`. Variants (`sessions/archive/session-86/...` or `sessions/session-plan/...`) are FORBIDDEN.

---

**End of Wave W11 plan.** Two full gate blocks. C5 → C6 sequenced. Downstream feeds W13 (P11), W14 (W6 NEW row class), W15 (P13 EVOI refresh).
