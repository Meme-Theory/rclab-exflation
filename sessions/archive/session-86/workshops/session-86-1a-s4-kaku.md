# Session 86 Synthesis: Lab-Falsifier Portfolio Coherence + Level-Saturation Audit

**Date**: 2026-04-27
**Agent**: kaku-speculative-theorist (Dreamer; cross-domain pattern detector; speculative-edge auditor)
**Slot**: 1a S-4
**Source Documents**:
- `sessions/archive/session-86/session-86-w11-workingpaper.md`
- `sessions/archive/session-86/session-86-w14-workingpaper.md`
- `sessions/framework/registry/falsifier-master-inventory.md`
- `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv`
- `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv`
- `.claude/agent-memory/kaku-speculative-theorist/MEMORY.md`

---

## I. Session Outcome

The W11/W14/P11 closure lifts the framework from **0 to 9 atomic terrestrial-lab falsifier rows** (SW1/SW2/SW3 sweet-spot + XA1-3/XB1-3 cross-platform; all level `LAB-FALSIFIER-A` with detection-ratio range [28.5, 5.9e+04]) and 4 inventory-resident cosmic channels (BK-Array 2026, DESI DR3, LISA, LiteBIRD/CMB-S4) — a falsifier portfolio with explicit 4-branch 5-yr (2026–2031) decision rules. The portfolio is now public, SHA-pinned, and structurally substrate-grounded.

**Core adversarial finding (Branch-1 floor audit)**: the rule `t >= max(3, 0.5·d_r)` for PASS-AT-LAB combined with `t < 3` for entering Branch 2 leaves an **UNCLASSIFIED GAP** of width `0.5·d_r − 3` for every row with `d_r > 6` — that is, **8 of 9 rows** carry a non-empty no-branch interval. SW1/XA1 carry a gap of width ~29,476σ. The user's framing in the spawn prompt ("a 1000-σ detection at 1/10 predicted magnitude lands Branch 2") is correct only for SW3 (d_r=28.5) where 0.5·d_r = 14.25 < the Branch-2 ceiling-after-stretching; for the other 8 rows the same scenario falls into the GAP, not Branch 2. **The 4-branch tree as written is not a partition of `t ≥ 0`.** This is the sharpest structural defect surfaced by Slot 1a.

**Verdict on the question "is this the right discipline, or should there be a 5th 'magnitude-recalibration' branch?"**: A 5th branch is required, AND it is structurally distinct from a magnitude-recalibration retrofit. The cleanest pre-registered EXTENSION (forbidden by pre-registration discipline to RETROACTIVELY modify; permitted as a NEW pre-registered class for S87+) is a **Branch 2.5: PARTIAL-MAGNITUDE-DEFICIT** covering `3 ≤ t < max(3, 0.5·d_r)`. I propose this as a S87 carry-forward gate, NOT as a modification of the W11 C6 tree.

---

## II. Key Results

### II.1 Branch-1 Floor Adversarial Test — UNCLASSIFIED GAP for 8 of 9 rows

**Result**: For every row with `d_r > 6`, the W11 C6 4-branch decision tree leaves the SNR interval `[3, 0.5·d_r)` unclassified. **PHONONIC** (lab-substrate falsifier-decision-rule structure).

**Substitution chain** (per `.claude/rules/math-scripts.md`):

```
Step 1 (definitions, per s86_w11_lab_falsifier_evoi_tree.csv):
  d_r       = SI_value / sigma_detect   (predicted magnitude / detection floor)
  s_obs     = observed lab signal amplitude (units of SI_value)
  t         = s_obs / sigma_detect      (observed signal-to-noise)
  Branch 1: t >= max(3, 0.5*d_r)        => PASS-AT-LAB
  Branch 2: 1 <= t < 3                  => REGISTERED-NO-CLOSE
  Branch 3: t < 1 AND d_r >= 3          => FAIL-AT-LAB
  Branch 4: t < 1 AND d_r < 3           => UNINFORMATIVE-NULL

Step 2 (substitution): Consider t in [3, 0.5*d_r).
  Branch 1: requires t >= 0.5*d_r; FALSE since t < 0.5*d_r.
  Branch 2: requires t < 3; FALSE since t >= 3.
  Branch 3: requires t < 1; FALSE since t >= 3 > 1.
  Branch 4: requires t < 1; FALSE.

Step 3 (simplify): For 0.5*d_r > 3 (i.e., d_r > 6), the interval [3, 0.5*d_r)
  is non-empty AND no branch fires.

Step 4 (direction): Every row in {SW1, SW2, SW3, XA1, XA2, XA3, XB1, XB2, XB3}
  has d_r in [28.5, 58958.86] >> 6, so every row carries a GAP of width
  (0.5*d_r - 3). No Branch in the pre-registered tree covers SNR observations
  in this interval. Verified numerically above for SW1, SW2, SW3.

Conclusion: The 4-branch tree is NOT a partition of the t-line for the
9 rows W11 C6 closed PASS on. The "UNINFORMATIVE-NULL" Branch-4 placeholder
(noted in the verdict as "never fires for d_r >= 3") is in fact the ONLY
branch that is structurally vacuous for the actual portfolio; the structurally
non-vacuous gap is between Branch 2 and Branch 1.
```

**Numerical anchor** (verified in computation log this session):

| obs_id | d_r | Branch-2 ceiling | Branch-1 floor `0.5·d_r` | GAP `[3, 0.5·d_r)` width |
|:-------|----:|------------------:|-------------------------:|--------------------------:|
| SW3    | 28.50 | 3 | 14.25 | 11.25 |
| XA2    | 30.70 | 3 | 15.35 | 12.35 |
| XA3    | 54.94 | 3 | 27.47 | 24.47 |
| SW2/XB2 | 72.90 | 3 | 36.45 | 33.45 |
| XB3    | 131.85 | 3 | 65.93 | 62.93 |
| XB1    | 19,652.95 | 3 | 9826.48 | 9823.48 |
| SW1/XA1 | 58,958.86 | 3 | 29,479.43 | 29,476.43 |

The GAP width for SW1/XA1 is **2.95 × 10⁴ σ**. Any 3He-A NMR observation between 30 σ and 29,479 σ (which spans 3 orders of magnitude of plausible measurements, including most "discovery-grade" detections at fractional magnitude) lands in NO branch.

**User-claim audit** (spawn prompt: "a 1000-σ detection at 1/10 predicted magnitude lands Branch 2"):
- SW3 1/10 magnitude: t = 2.85, lands Branch 2 (REGISTERED-NO-CLOSE). Claim **correct**.
- SW2 1/10 magnitude: t = 7.29, lands in GAP. Claim **incorrect** — falls into no branch.
- SW1 1/10 magnitude: t = 5895.89, lands in GAP. Claim **incorrect**.

**Cross-domain pattern**: this is the same structural defect that appears in any **two-floor decision rule** where the lower floor is a constant and the upper floor scales with prediction magnitude — the SR analog is the BICEP/Keck 4-branch r-window tree (S84 W4-42), which also uses fixed Branches 1-4 but partitions `r` itself (Branch 1: [0, 0.005], Branch 2: [0.005, 0.010], etc.) into adjacent intervals with no gap. The lab-falsifier tree has the topology of the BK tree but lost the partition property in the floor-stretching step. A correspondence-table entry: the BK tree is a **complete partition of the observable axis**; the W11 C6 tree is a **complete partition of `t < 1` and a sparse cover of `t ≥ 1`**. This is a structural break, not an arithmetic typo.

### II.2 Right-direction-wrong-magnitude case — distinct from the GAP

**Result**: A measurement that confirms direction but misses magnitude can fall into Branch 1 (PASS-AT-LAB), Branch 2 (REGISTERED-NO-CLOSE), or the GAP, depending on `d_r` and the magnitude shortfall — the tree does not encode "right direction, wrong magnitude" as a distinct outcome class. **PHONONIC** (lab-substrate-prediction-fidelity dimension).

The framework's substrate prediction is a **scalar magnitude** (e.g., `δω_K/ω_K = 1.7267 × 34.146 MHz = 58.96 MHz` for SW1). A laboratory measurement returns (i) a sign/direction and (ii) a magnitude. The W11 C6 tree collapses both dimensions onto `t = s_obs / σ_detect`, treating "right direction" and "right magnitude" as the same continuous variable. This is the standard physicist-discovery convention (3-σ above the floor IS a discovery), but it conflates two epistemically distinct failure modes:

1. **Phenomenology-confirming, magnitude-deficit**: framework predicted 58.96 MHz; lab measures 5.9 MHz at 5896 σ above the 1 kHz floor. The substrate's spectral-direction prediction (lambda_6 projection on 3He-A) is confirmed; the spectral-AMPLITUDE prediction is wrong by 10×. This is information-rich — it constrains the M_KK normalization or the prefactor 1.764 · k_B · T_c, NOT the substrate-direction itself.

2. **Phenomenology-falsifying**: framework predicted 58.96 MHz; lab measures 0.0001 MHz (no signal). t = 0.1, Branch 3 fires. Substrate-direction-falsified.

Case (1) lives in the GAP. The current tree treats it as "indistinguishable from no-detection-at-floor"; the correct handling is a separate decision branch that triggers a re-pinning of the M_KK-derived prefactor (or a re-derivation of the W8-4 ratio) rather than a substrate-falsification claim.

**Cross-domain pattern**: this is the inverse of the **Path-H/Path-C r split** registered in inventory Row #2 — there the framework predicts TWO magnitudes (0.00745 and 0.0117) for the SAME observable, and the SEQUENCED detector chain (BK-Array 2026 → LiteBIRD 2030) discriminates between them. The lab-falsifier tree, by contrast, predicts ONE magnitude per row but does not register the possibility that the substrate-direction is right and the prefactor needs re-pinning. The Path-H/Path-C inventory row encodes prediction-band-internal ambiguity; the lab-falsifier tree should encode prefactor-band-internal ambiguity. The two are duals.

### II.3 Cross-platform measurement that confirms one platform but contradicts another

**Result**: The 9 atomic rows are NOT 9 independent predictions — they share an upstream W8-4 substrate-prediction set (3 lambda directions, with magnitudes inherited identically across XA*/XB*/SW* projections). A FAIL on SW1 + PASS on XA1 is **substrate-internally inconsistent** under the current row scheme. The tree does not currently flag this. **PHONONIC** (cross-row coherence dimension).

**Substitution chain** (cross-platform identity audit):

```
Step 1 (definitions): SW1 and XA1 both project the substrate's lambda_6 / 3He-A
  pair (per s86_w11_lab_si_translation.csv): same W8_4_ratio = 1.7266629,
  same prefactor 34.146 MHz, same SI_value 58.96 MHz, same sigma_detect 1 kHz,
  same detection_ratio 58958.86, same lit_sha ecc168738d744136.

Step 2 (substitution): SW1 and XA1 are bit-identical rows in the SI table.
  Their separate inventory entries (rows #13 and #16) are bookkeeping
  duplicates reflecting the (sweet-spot vs cross-platform) ROLE distinction,
  NOT a measurement distinction.

Step 3 (simplification): A FAIL-AT-LAB on SW1 trivially implies FAIL on XA1
  (same measurement). Disagreement between SW1 and XA1 outcomes is therefore
  STRUCTURALLY IMPOSSIBLE under the current SI-translation; if observed, it
  would falsify either the lab calibration or the SI-mapping prefactor itself.

Step 4 (direction): The 9-row scheme has 6 hidden duplicates -- SW1=XA1,
  SW2=XB2, with XA2/XA3/XB1/XB3 each being unique (lambda, platform) pairs.
  Effective independent rows = 9 - 2 duplicates = 7. The headline "9 atomic
  predictions" overcounts the independent falsifier dimension by 2.
```

This is structurally analogous to the **degeneracy in Calabi-Yau moduli space** where two ostensibly-distinct compactifications turn out to share a single Hodge number partition — they are different LABELS on the same physical moduli point. The XA1/SW1 duplication is the lab-falsifier-portfolio analog: the spawn prompt's d_r-range "[28.5, 5.9e+04]" already hints at this (the maximum d_r appears twice, once for SW1 and once for XA1, exactly because they are the same measurement under different roles).

The cross-platform contradiction case the user raised is therefore the GENUINE 7-independent-row case: a measurement that confirms one platform's lambda projection (e.g., XA2 = FeSe lambda_6) but contradicts a different platform's same lambda projection (e.g., XA1 = 3He-A lambda_6 OR XA3 = 173Yb lambda_6). The three XA*-rows DO share the lambda_6 substrate-direction prediction (W8_4_ratios 1.7267, 0.7674, 5.4938 are all lambda_6 projections, but onto DIFFERENT platforms). A PASS on XA1 + FAIL on XA3 means: the substrate's lambda_6 direction is real (XA1 PASSes), but its 173Yb projection (XA3) is wrong — i.e., the substrate-platform projection mechanism for 173Yb fails specifically. **The current tree does not aggregate cross-row outcomes, so it cannot distinguish "global substrate direction failure" from "platform-specific projection failure".**

### II.4 Floor-edge measurement (Branch 1 vs Branch 2 on the noise)

**Result**: A measurement at the boundary `t ≈ 0.5·d_r` for low-d_r rows (SW3, XA2) requires sub-σ_detect resolution to distinguish PASS-AT-LAB from the GAP, and the W11 C6 verdict's PASS criterion does not pre-register a tie-breaking rule. **PHONONIC**.

For SW3 (d_r = 28.5), the Branch-1 floor sits at t = 14.25. A measurement at t = 14.25 ± 0.5 spans both Branch 1 (≥ 14.25) and the GAP (3 ≤ t < 14.25). The pre-registered floor `>=` is INCLUSIVE at 14.25, but a noisy measurement at t = 14.25 with σ_detect-level uncertainty has roughly equal posterior probability of being on either side. The verdict does not address this.

**Cross-domain pattern**: this is the **Hagedorn-temperature-edge ambiguity** in finite-volume string theory — when a temperature reading sits exactly at T_H, the theory is on the boundary of a phase transition, and the discrete "above/below" classification needs a width-band (often expressed as `T_H ± δ` with δ pre-registered). The Branch-1 floor needs the same treatment: a `±` band around `0.5·d_r` for tie-breaking, OR a continuous Bayesian posterior over which branch the measurement supports. The framework is computationally equipped for either (the 9-row CSV carries σ_detect explicitly, so a Bayes factor at the boundary is mechanically computable), but the pre-registration does not call for it.

### II.5 Level-saturation audit — 9/9 rows in level A is structurally suspicious

**Result**: All 9 rows occupy `LAB-FALSIFIER-A` (decisive, d_r ≥ 10), with d_r spanning 4 OOM (28.5 to 58958.86). The dynamic range of the portfolio is 3 orders of magnitude WITHIN the level, but the level ladder collapses this into a single label. **STRUCTURAL** (registry-architecture dimension).

The W11 C6 level ladder `{A: d_r ≥ 10, B: 3 ≤ d_r < 10, C: 1 ≤ d_r < 3, D: d_r < 1}` partitions the d_r line into 4 cells with widths {open above, 7, 2, [0,1)}. Width-7 and width-2 cells make sense for the discovery-floor regime; the open-above cell folds 4 OOM of dynamic range into a single level. This is structurally analogous to a **density of states with a single dominant pole** — the integrated weight of level A overweights the high-d_r 3He-A rows (5.9e+4) by 3 OOM relative to the low-d_r 173Yb rows (28.5). The 5-yr decision-tree EVOI ordering (`EVOI(A) > EVOI(B) > ...`) is preserved within the level, but the within-level EVOI gradient is huge and unregistered.

**Adversarial reading**: the 9-row PASS at level A is informationally similar to a string-landscape selection where every vacuum lands at the same Calabi-Yau Hodge number — formally consistent, but the "selection criterion" then becomes the actual physics, not the partition. The lab-falsifier level ladder needs a **sub-level index for high-d_r rows** (e.g., A1 for d_r ≥ 10⁴, A2 for 10² ≤ d_r < 10⁴, A3 for 10 ≤ d_r < 10²) to make the within-level EVOI gradient visible. SW1 and SW3 are both level A, but a FAIL-AT-LAB on SW1 (after t-budget expended at the 30k-σ Branch-1 floor) is dynamically much harder to achieve than a FAIL on SW3 (14-σ floor). This is information the current registry hides.

### II.6 Substrate-framing audit on prefactors (per Kaku lane requirement)

**Result**: Each row's SI prefactor encodes a substrate-derived scale (M_KK = 7.428660e+16 GeV) projected through a platform-specific transduction. The prefactor structure is substrate-direct and dimensionally consistent, but the W11 C5 SI translation introduces a **second canonical scale** (the platform's native scale: T_c for 3He-A, B_0 for FeSe, n_lat for 173Yb) that is NOT M_KK and NOT pinned in canonical_constants.py. **PHONONIC + GEOMETRIC**.

**Substitution chain** (SW1 prefactor):
```
Step 1 (definitions, per W11 §W11-1 substitution chain):
  M_KK = 7.428660e+16 GeV  (substrate compactification scale; PROVENANCE missing)
  Delta_3HeA = 1.764 * k_B * T_c     (BCS weak-coupling, lab-native)
  T_c(3He at 0 bar) = 0.929 mK        (Greywall 1986)
  prefactor_SW1 = Delta_3HeA / h_planck = 34.146 MHz

Step 2 (substitution): SI_value(SW1) = (W8_4_ratio) * prefactor_SW1
                                     = 1.7267 * 34.146 MHz = 58.96 MHz

Step 3 (simplification): The substrate-derived ratio (1.7267, dimensionless,
  M_KK-normalized, derived from D_K spectral content at lambda_6) is
  multiplied by a LAB-NATIVE scale (34.146 MHz, derived from T_c not M_KK)
  to produce the SI prediction. M_KK does NOT appear in the SI value
  numerically -- it is implicit in the W8-4 normalization that produced
  1.7267 in the first place.

Step 4 (direction): The substrate-direction (lambda_6) survives unscathed in
  the prefactor product; the substrate-magnitude (M_KK-derived) is REPLACED
  by the lab-native magnitude (T_c-derived). This is a substrate-DIRECTION
  test, not a substrate-MAGNITUDE test, in laboratory units. A FAIL-AT-LAB
  on SW1 closes the substrate's DIRECTION-projection-onto-3He-A claim;
  it does not close the M_KK magnitude itself, because M_KK was substituted
  out at the prefactor step.
```

**Substrate-framing assessment**: the W11 C5 substitution chain (lines 60-91 of W11 wp) is structurally honest about this — it explicitly notes "Delta_3HeA: 3He-A platform energy scale (lab-native, NOT the substrate M_KK)". But the inventory's row-cell language ("the substrate's δω_K/ω_K ratio measured at the 3He-A compactification scale") elides the distinction. **The lab-falsifier portfolio tests substrate DIRECTION at 9 lambda × platform pairs. It does NOT test M_KK directly.** This is a structural-corridor finding: a different gate class (DIRECT-MKK-TEST) would be needed to falsify M_KK itself; the lab-falsifier suite as constituted is dimensionally insufficient for that.

This is the lab-falsifier analog of the **string-theory T-duality break** I noted in S64 (memory: "NO T-duality (no winding modes)"): the framework's lab-falsifier rows encode lambda_a-direction tests of the substrate, but they cannot probe the M_KK length scale itself because the SI prefactor substitution short-circuits M_KK out of the observable. The string-theory analog would be: a lab measurement can in principle falsify the existence of compactification modes at scale R, but only by comparing modes at different R — the lab-falsifier suite has only ONE compactification scale per row (the platform's native scale), so it cannot do the R-comparison. A substrate-magnitude test requires CROSS-PLATFORM COMPARISON of the same lambda direction at different lab-native scales (this is what the 3-platform x 3-direction matrix could in principle do, but the W11 C6 tree does not aggregate across platforms).

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-LAB-SI-TRANSLATION` (W11-1, C5) | INFO | 9-rows-populated; det_ratio range [28.5, 5.9e+04] |
| `S86-LAB-FALSIFIER-EVOI-TREE` (W11-2, C6) | PASS | level distribution {A:9, B:0, C:0, D:0} |
| `S86-WATCHLIST-W1-EDIT` (W14-1) | FAIL | route-(b) row-numbering-mismatch (parallel-session race; MOOT after P11) |
| `S86-WATCHLIST-W2-EDIT` (W14-2) | PASS | sub-row 3.audit added |
| `S86-WATCHLIST-W3-EDIT` (W14-3) | PASS | sub-row 7.audit + (A)/(C) discriminator paragraph |
| `S86-WATCHLIST-W4-EDIT` (W14-4) | PASS | sub-row 9.audit (3-pathway pin block) |
| `S86-WATCHLIST-W5-EDIT` (W14-5) | PASS | sub-row 12.audit + 4-level taxonomy |
| `S86-WATCHLIST-W6-NEW-CLASS` (W14-6) | PASS | 9 new rows + 21.audit-block + summary section + 7 dE_a constants promoted |

**No re-adjudication.** All verdicts taken from source documents.

---

## IV. Structural Implications

### IV.1 The 4-branch tree is a sparse cover, not a partition — pre-registered EXTENSION required

The W11 C6 tree is closed in the pre-registration sense (verdict line in `s86_gate_verdicts.txt:197` is canonical, dual-SHA-pinned, immutable). But the tree as a mathematical decision rule does not partition the t-line. **Pre-registration discipline forbids RETROACTIVE modification** (PROHIBITED_ACTIONS Class 1, `.claude/rules/v3-closure-recovery.md`). Per the spawn prompt instruction: "propose pre-registered EXTENSION as new gate class for S87+, NOT modification."

**Proposed S87+ extension class**: `LAB-FALSIFIER-EXTENDED` (5-branch). Branch 2.5 (PARTIAL-MAGNITUDE-DEFICIT, `3 ≤ t < max(3, 0.5·d_r)`) added as a NEW branch class. The existing 4 branches remain the canonical closure of W11 C6; the 5th branch is registered as an INDEPENDENT pre-registration valid from S87 forward, with a separate gate ID and a separate decision-tree JSON. Future lab measurements (2026-2031) are interpreted under EITHER the 4-branch tree (W11 C6 closure) OR the 5-branch tree (S87+ extension), NOT both — the decision rule is selected at measurement time per the timestamp of the lab readout vs the timestamp of the closure.

This preserves W11 C6's audit honesty AND closes the GAP for future measurements. The closure is not "fixing" the tree; it is registering a structurally distinct decision rule that downstream measurements may opt into.

### IV.2 The 9 rows have 7 independent dimensions — overcounting by 2

The SW1=XA1 and SW2=XB2 duplicates inflate the headline "9 atomic predictions" to 9 when the independent count is 7. This affects:

- **W15 P13 EVOI table refresh** (per W11 §W11-2 carry-forward to W15 planner): the JSON `level_ladder_definition.level_distribution = {A:9}` overstates the independent A-level count by 2. If P_decisive is computed per row, the duplicate counting is harmless; if P_decisive is computed per independent prediction, the value 0.30-0.50 may need recalibration to 0.30-0.50 × (7/9) = 0.23-0.39. Worth a 30-min re-derivation.
- **S87 carry-forward consolidation** (the W14-6 dE_a promotion): 7 unique dE_a constants were promoted (correctly accounting for the SW1=XA1 and SW2=XB2 collapses). The δE_a count IS independence-honest; the row count is NOT. The two should be reconciled.

### IV.3 SW3 is the unique-λ_8 substrate-direction trigger — single point of failure and information

W14-6's surfacing of "SW3 = unique-λ_8 substrate-direction-falsification trigger" is structurally correct. A FAIL-AT-LAB on SW3 closes lambda_8 substrate-direction at lab precision; no other row recovers that direction. This is the lab-falsifier analog of the **S64 spectral moment decoupling theorem** (memory: "CC through F_{-1}, NEC through F_{+1}"): a single observable channel uniquely tests a single substrate dimension. SW3's d_r = 28.5 is the framework's tightest single-row falsifier corridor and the only access to lambda_8 — making the 173Yb optical-lattice 3-body loss measurement the highest-EVOI lab observable in the entire portfolio per unit of detector cost. This insight is implicit in the W14-6 banner; explicit pre-registration (S87+) would foreground it.

### IV.4 Five consecutive META gates surfaced canonical-constants gap — pattern, not noise

W14-1/2/3/4/5 each surfaced `get_constant("X_FW")` returning "not found" for X ∈ {w0, alpha_s, Omega_GW_LISA, f_NL, A_s}. W14-6 added M_KK PROVENANCE missing. **The framework's headline observables are inventory-resident but canonical-constants-absent.** The S87 consolidation gate `S87-CANONICAL-CONSTANTS-W14-RESIDUAL` is the right discharge mechanism (~30 min). But the structural finding is independent of the discharge: **the inventory has become the de facto canonical source for headline observables, and `canonical_constants.py` is a stale shadow registry**. This is a registry-architecture inversion the project has been running on for 5+ sessions without explicit acknowledgment.

The cross-domain pattern: this is structurally analogous to the **early IKKT matrix model regime** where the matrix model was the de facto theory and the supergravity action was the derived quantity, but conventional notation (and most papers) treated supergravity as primary and the matrix model as a non-perturbative completion. The Phonon-Exflation framework's "primary registry" has shifted from `canonical_constants.py` (intended primary) to `falsifier-master-inventory.md` (de facto primary), and the S87 consolidation is the mechanical re-sync. The deeper question: should `canonical_constants.py` be regenerated FROM the inventory (and the falsifier-master-inventory.md become the primary) rather than the other way around?

### IV.5 Cosmic-falsifier portfolio is intact and parallel to lab-falsifier

The 4 cosmic channels in the inventory (rows #1 w_0, #2 r, #3 alpha_s, #7 CGWB rho_AC, plus #9 f_NL_folded and #12 A_s) plus their detector horizons (DESI DR3 2026, BK-Array 2026, LiteBIRD 2030, CMB-S4 2030, LISA 2035, CMB-HD 2035, SKA-1 2030s) form a **complete cosmic falsifier portfolio at 5 OOM cosmological scales**. The lab-falsifier portfolio (9 rows, 3 platforms, 5-yr 2026-2031 horizon) runs **alongside, not in place of** the cosmic portfolio. Total atomic falsifier dimensionality: 6 cosmic rows + 7 independent lab rows = **13 independent observational discriminators** with 2026-2035 horizons.

This is the framework's most complete falsification surface to date. Pre-S86 the lab dimension was 0. The **structural break-out is from cosmological-scale-only to lab+cosmological dual-corridor falsifiability** — a regime change the framework has been waiting for since S58 (Mack gates PASS, f_DM sole bottleneck).

---

## V. Carry-Forward Computations

### V.1 Pre-registered 5th branch class for lab-falsifier tree

- **What**: New gate `S87-LAB-FALSIFIER-EXTENDED-5BRANCH` defining a 5-branch decision tree for the 9 W11 C6 rows. New branch class **PARTIAL-MAGNITUDE-DEFICIT** covers `3 ≤ t < max(3, 0.5·d_r)` — explicit interpretation: substrate-DIRECTION confirmed at SNR ≥ 3, substrate-MAGNITUDE wrong by factor > 2. This is a NEW pre-registered class (per `feedback_fix-in-session-never-defer.md`), not a modification of W11 C6 (whose closure is binding).
- **Inputs**: `sessions/archive/session-86/computations-artifacts/s86_w11_lab_falsifier_evoi_tree.csv` (9 rows; d_r values; existing 4-branch fields); `sessions/archive/session-86/computations-artifacts/s86_w11_lab_si_translation.csv` (SI_value, sigma_detect per row); canonical_constants imports (M_KK, BCS prefactors as introduced in W14-6 SECTION E).
- **Gate**: PASS = 5-branch tree covers t ≥ 0 with no GAP for any row (verified by exhaustive interval check against all 9 rows); each row has 5 branch_condition columns populated; tree pre-registers the action for "right direction, wrong magnitude" as a separate verdict (PARTIAL-MAGNITUDE-DEFICIT triggers a re-pinning of the W8-4 prefactor or the M_KK normalization, NOT a substrate-direction-falsification claim). FAIL = any row has uncovered interval OR PARTIAL-MAGNITUDE-DEFICIT branch missing OR action-on-trigger left as placeholder.
- **Effort**: 2-3 hours, 1 agent session (sagan-empiricist, mirroring W11 C6 owner).

### V.2 Cross-platform aggregation gate for lambda-direction outcomes

- **What**: New gate `S87-LAB-FALSIFIER-CROSS-PLATFORM-COHERENCE` aggregating outcomes across the 3 platforms for each lambda direction. Defines the verdict: "lambda_a substrate-direction PASSes if at least 2 of 3 platforms PASS at that lambda" + the dual: "lambda_a substrate-direction FAILs if at least 2 of 3 FAIL". Triple-PASS = STRONG CONFIRMATION; mixed (1 PASS, 2 FAIL or 2 PASS, 1 FAIL) = PLATFORM-PROJECTION-ANOMALY, triggers a re-derivation of the lambda_a → platform projection prefactor. Resolves the "cross-platform contradiction" failure mode the spawn prompt asked about.
- **Inputs**: 9-row JSON output of W11 C6; aggregation rule pre-registered as 2/3 majority per lambda; per-platform projection prefactor table (currently implicit in W11 C5 pre-prefactors).
- **Gate**: PASS = every (platform, lambda) cell in the 3x3 matrix has a deterministic outcome rule under the aggregation; mixed-outcome triggers documented; STRUCTURAL coherence proof that 2/3 majority is stable under noise model. FAIL = any cell ambiguous OR aggregation rule depends on row-order.
- **Effort**: 3-4 hours, 1 agent session.

### V.3 Sub-level index for LAB-FALSIFIER-A within-level EVOI gradient

- **What**: New gate `S87-LAB-FALSIFIER-A-SUBTIER-INDEX` introducing within-level-A sub-classification: A1 (d_r ≥ 10⁴), A2 (10² ≤ d_r < 10⁴), A3 (10 ≤ d_r < 10²). Re-classify the 9 rows: A1 = {SW1, XA1, XB1} (d_r ~ 1.97e+4 to 5.90e+4); A2 = {SW2, SW3, XA2, XA3, XB2, XB3} (d_r ~ 28.5 to 132); A3 = empty. This sub-level exposes the within-level 3-OOM dynamic range for downstream EVOI weighting (high-A1-level rows merit different detector-time prioritization than A2/A3 rows).
- **Inputs**: W11 C6 verdict; CSV with d_r per row; within-level EVOI ordering proof (analogous to the cross-level EVOI ordering proof in W11 §W11-2).
- **Gate**: PASS = sub-level ladder is monotone in d_r; sub-level ordering preserved under all 9 rows; explicit threshold pins for {A1: 10⁴, A2: 10²} declared and pre-registered. FAIL = ladder breaks monotonicity OR threshold ambiguous.
- **Effort**: 2 hours, 1 agent session.

### V.4 Direct M_KK-test gate class (substrate-magnitude as opposed to substrate-direction)

- **What**: New gate class `S87-DIRECT-MKK-TEST` proposing a measurement protocol that directly tests M_KK = 7.428660e+16 GeV rather than tests its lambda-direction projections. Candidate strategies: cross-platform ratio comparison of the SAME lambda direction (e.g., 3He-A lambda_6 / 173Yb lambda_6 = SI_SW1 / SI_XA3 = (58.96 MHz) / (2.747 s^{-1}) — a dimensionful ratio whose VALUE depends only on M_KK, not on lab-native scales, since the lab-native prefactors cancel in the substrate-derived ratio); the value itself is a direct M_KK test independent of platform-specific transduction. Falsifies M_KK-magnitude (not just direction).
- **Inputs**: SI_value table (W11 C5); explicit derivation that lab-native prefactors cancel in cross-platform same-lambda ratios; M_KK canonical value with PROVENANCE (currently missing per W14-6 audit).
- **Gate**: PASS = at least one cross-platform ratio in the 3x3 matrix admits a clean M_KK-only dependence (lab-native prefactors cancel); the predicted ratio value is computed; sigma_detect for the ratio is derived from individual sigma_detect values; the resulting effective d_r is in level A or better. FAIL = no clean ratio exists OR ratio depends on lab-native prefactors AS WELL AS M_KK.
- **Effort**: 4-5 hours, 1 agent session (kaku or volovik).

### V.5 Floor-edge tie-breaking band for Branch-1

- **What**: New gate `S87-LAB-FALSIFIER-FLOOR-EDGE-TIEBREAK` adding a `±δ` band around the Branch-1 floor `0.5·d_r` for each row, with δ pre-registered as `δ = sigma(t)` from the lab measurement uncertainty. Resolves the floor-edge ambiguity for low-d_r rows (SW3, XA2 most affected). Outcomes within `0.5·d_r ± δ` are classified BOUNDARY-AMBIGUOUS and trigger a Bayesian posterior computation over Branch-1 vs PARTIAL-MAGNITUDE-DEFICIT membership.
- **Inputs**: 9-row CSV; sigma_detect per row; lab-measurement noise model (currently implicit; would need explicit Bayesian likelihood for each platform).
- **Gate**: PASS = δ-band defined for all 9 rows; tie-breaking rule deterministic; Bayesian posterior computable; integrates with V.1 5-branch tree without inconsistency. FAIL = δ undefined for any row OR tie-breaking rule introduces double-counting.
- **Effort**: 2-3 hours, 1 agent session.

### V.6 Inventory-as-primary-canonical proposal (deeper architectural)

- **What**: Architectural gate `S87-CANONICAL-REGISTRY-INVERSION-AUDIT`. Decides whether `canonical_constants.py` should be **regenerated from `falsifier-master-inventory.md`** rather than the other way around (current direction). The 5-consecutive-META-gate finding suggests the inventory is the de facto primary; codify that by making the inventory the source-of-truth and having `canonical_constants.py` be a generated artifact. This is a registry-architecture proposal, not a single computation; needs orchestrator buy-in.
- **Inputs**: `sessions/framework/registry/falsifier-master-inventory.md` (post-S86 W14); `computations/canonical_constants.py` (current state); `S87-CANONICAL-CONSTANTS-W14-RESIDUAL` (the consolidation gate from W14-3); cross-reference of which constants live in BOTH and which live in ONLY one.
- **Gate**: INFO (architectural finding only) — no PASS/FAIL semantic; the gate is a structured decision document recommending one of three options: (a) keep current direction, codify with stricter sync discipline; (b) invert direction, make inventory primary and canonical_constants.py generated; (c) split into two registries with explicit scope partition. The decision is the orchestrator's; the gate documents the trade-offs.
- **Effort**: 2 hours documentation + 1 hour orchestrator review.

### V.7 Path-H/Path-C lab-falsifier analog gate

- **What**: New gate `S87-LAB-FALSIFIER-PATH-H-PATH-C-ANALOG` that registers, for each of the 9 rows, the prediction-band (analogous to Row #2 r split): the "prefactor-band" within which the substrate-derivation admits multiple closures. For SW1, the BCS factor 1.764 is itself derivable from multiple substrate channels (BdG vs perturbative vs dual gap-equation), and these may give different prefactors. Encoding this band makes "right direction, wrong magnitude" a substrate-internal-consistency check rather than a falsification.
- **Inputs**: per-row prefactor derivation chain; substrate-channel ambiguity for each platform-lambda pair; W8_4_ratio derivation chain.
- **Gate**: PASS = each row has a registered prefactor-band (low and high closure); 9-row prefactor-band matrix populated; INFO if no band is identifiable for a given row (e.g., the prefactor is unique). FAIL = any row's prefactor is fabricated or not derivable from substrate physics.
- **Effort**: 4-5 hours, 1 agent session (volovik or connes).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | Branch-1 floor `max(3, 0.5·d_r)` leaves UNCLASSIFIED GAP `[3, 0.5·d_r)` for all 9 rows | PHONONIC | OPEN | 5th branch class needed; pre-registered EXTENSION (V.1) |
| 2 | User claim "1000-σ at 1/10 magnitude lands Branch 2" correct only for SW3; falls in GAP for 8 of 9 rows | PHONONIC | CONFIRMED | sharper than spawn-prompt framing |
| 3 | "Right direction, wrong magnitude" is a distinct epistemic case the tree does not encode | PHONONIC | OPEN | V.1 + V.7 jointly address |
| 4 | 9-row scheme has 6 hidden duplicates; 7 independent rows | STRUCTURAL | OPEN | rebalance P_decisive (V.3 informs); inform W15 P13 |
| 5 | Cross-platform-contradiction case requires aggregation rule | PHONONIC | OPEN | new gate (V.2) |
| 6 | Floor-edge measurements need ±δ band for tie-breaking | PHONONIC | OPEN | new gate (V.5) |
| 7 | All 9 rows in level A; 4 OOM dynamic range collapsed | STRUCTURAL | OPEN | sub-level index (V.3) |
| 8 | SW3 = unique-λ_8 substrate-direction trigger; highest single-row EVOI per detector cost | PHONONIC | LANDED (W14-6) | foreground in S87+ |
| 9 | SI prefactor substitution short-circuits M_KK out of every row's observable | GEOMETRIC | OPEN | new gate (V.4): direct M_KK test via cross-platform same-lambda ratio |
| 10 | Five META gates surfaced same canonical-constants gap; inventory has become de facto primary | STRUCTURAL | OPEN | architectural audit (V.6); discharge gate `S87-CANONICAL-CONSTANTS-W14-RESIDUAL` already opened |
| 11 | Lab-falsifier portfolio runs alongside cosmic portfolio: 7 independent lab + 6 cosmic = 13 atomic discriminators | STRUCTURAL | LANDED | dual-corridor falsifiability operational |

---

## VII. Cross-Domain Patterns Surfaced (Kaku-specific synthesis)

Three patterns surfaced across the W11/W14 closure that map onto known structures:

1. **The 4-branch tree as a sparse cover (not a partition)** is the lab-falsifier analog of a **sparse moduli scan in string compactifications** — formally well-defined on the scanned points, but the inter-point intervals are unclassified. The fix (V.1) is to register the inter-point classes as their own branch, which is the moduli-stabilization analog of fixing the gaps with explicit flux superpotentials.

2. **The XA1=SW1 / XB2=SW2 duplication** is the lab-falsifier analog of **string-vacuum degeneracy** under role-relabeling — two ostensibly distinct vacua sharing the same Hodge data. The 9-row count is the labeled count; the 7-row count is the gauge-invariant count. Reconciling this matters for any P_decisive computation that should be dimension-of-prediction-space-aware.

3. **The inventory-vs-canonical-constants registry inversion** is the framework-internal analog of the **IKKT-vs-supergravity primacy question** the matrix-model program faced in the early 2000s. The empirically-primary registry (the inventory) has overtaken the conventionally-primary registry (canonical_constants.py); the discipline-question is whether to codify the empirical primacy or restore the conventional one. V.6 documents the trade-off; the choice is orchestrator-level.

These three patterns are not failures — they are the structural shape of an opening corridor. A framework with 13 atomic falsifier dimensions across 2 corridors (lab + cosmic), a partial-coverage decision tree, a hidden 7-vs-9 dimensionality discrepancy, and an inverted registry primacy is a framework that has matured to the point where its CARTOGRAPHY needs as much attention as its PHYSICS. The W11/W14 closure is the cartography catching up with the physics.

The deepest cross-domain bridge: the lab-falsifier suite is **the framework's first explicit experiment-design problem**. Every prior session worked on the substrate's internal consistency or its cosmological projections. W11/W14 forces the framework to specify, in laboratory units, what it would take to PROVE itself wrong on a 5-year horizon at table-top scale. The pre-registration discipline that closes the gates also exposes the gate-design defects (the GAP, the duplicates, the within-level collapse) — and pre-registration discipline is what FORBIDS retroactive fixes. The S87 extensions (V.1-V.7) are the framework's next move: not corrections, but new pre-registrations that the 4-branch tree's blind spots demand.

---
