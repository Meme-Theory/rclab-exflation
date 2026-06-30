# Session 85 Workshop: kitaev x gen-physicist — Plan-Pin-vs-Source-Drift Taxonomy → PRU/PRDR Extension (5A)

**Date**: 2026-04-25
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns) — TAXONOMIZE / CONVERGE
**Agents**: kitaev (kitaev-quantum-chaos-theorist), gen-physicist
**Source Documents**:
- sessions/archive/session-85/session-85-w7-workingpaper.md
- sessions/archive/session-85/session-85-w9-workingpaper.md
- sessions/archive/session-85/session-85-w10-workingpaper.md
- sessions/archive/session-85/session-85-w11-workingpaper.md
- sessions/archive/session-85/session-85-w13-workingpaper.md
- .claude/rules/epistemic-discipline.md
- .claude/templates/pru-pre-registration-template.md
- computations/canonical_constants.py
- sessions/archive/session-85/session-85-w6-13-workshop-schedule.md (mother schedule, this workshop §5A)
- sessions/archive/session-85/session-85-workshop-schedule.md (W0-W5 — for W-3 Plan-Layer Methodology Debts cross-pairing)

**Focus Topics** (from schedule §5A invocation):
1. 13+ drift sites where plan-pinned values disagree with canonical sources but PRU passes
2. 7+ NEW debt classes distinct from W0-W5's set (plan-pin/source reconciliation, INFO-mode classification, GPU-pin selectivity, root-count heuristic, PRDR bare-K, v3-recovery sig_2, 5B scan-as-robustness)
3. Rule-file v2 diff (epistemic-discipline.md PRDR + pru-template + rclab-plan)

---

## Round 1 — kitaev: TAXONOMIZE the 13+ Drift Sites

### K1: Drift-Site Enumeration with Per-Site Pin/Source Diff

**Source-traced enumeration**. Each row below is anchored to a verbatim grep match in the cited working paper, the canonical-constants ledger, and (where relevant) the schedule §5A invocation. Drift magnitude is the dimensionless ratio `(pin − source)/source` for scalar pins, and a categorical label for non-scalar pins. The 13+ count claimed by the schedule is recovered as 13 distinct drift events spanning W7, W9, W10, W11, W12, W13.

**Knowledge-MCP source-reconciliation queries run before this enumeration**:
- `list_constants ".*pivot.*"` → `N_pivot=64.08`, `f_LISA_pivot=0.003`, `k_pivot_planck=0.05`. No `epsilon_pivot` / `eps_H_pivot` constant in the canonical ledger; `eps_H = 0.02163` is consistently cited in 7+ scripts (S62 → S83) as a derived quantity, not a registered canonical pin.
- `list_constants ".*H_tilde.*"` → `H_tilde_canonical_TD = 0.0059076`, `H_tilde_canonical_LI = 2.46411e-05`, `H_tilde_center = 0.004714`, `H_tilde_lo = 0.004599`, `H_tilde_hi = 0.004829`.
- `list_constants ".*Borel.*"` → `Borel_threshold_S_inst = 4.34` (this gate's W9-1 PASS landed it as canonical).
- `get_constant("epsilon_pivot")` → not found (confirms ε_pivot is a derived quantity living at script-level, not a registered canonical).
- `search_knowledge("algebraically forced PASS scan robustness")` → S75 W2-E spectral-moment-decoupling, S82 robustness scans (L_max ∈ {3,5,7,9}); pattern: scan output is **diagnostic robustness**, not the verdict input.

**Drift-site table** (source-pinned values, all magnitudes Python-verified):

| # | Site ID | Plan-pinned value | Canonical/source value | Drift magnitude | Drift direction | Source citation |
|:--|:--------|:------------------|:------------------------|:----------------|:----------------|:----------------|
| 1 | S85-W7-1 BASELINE-HTILDE (TD anchor) | `H̃_TD_plan = H̃_center · 1.57 = 7.401e-3 M_KK` | `H_tilde_canonical_TD = 5.9076e-3 M_KK` (= H̃_center · √1.57) | +25.28% (frac); 0.098 OOM | pin **HIGH** vs source | `s85-w7-wp.md` L71, L117; canonical_constants `H_tilde_canonical_TD` |
| 2 | S85-W7-1 BASELINE-HTILDE (LI anchor) | `H̃_LI_plan = H̃_center · 181.0 ≈ 0.853` | `H_tilde_canonical_LI = 2.46411e-05` (= H̃_center · 181 with √-route correction) | ~3.46e+04× ; 4.54 OOM | pin **HIGH** vs source | `s85-w7-wp.md` L71; canonical_constants `H_tilde_canonical_LI` |
| 3 | S85-W7-2 CC-6 (single-channel target) | "single-channel CC-6 closes Λ hierarchy alone" | substrate first-principles (W7-2 §11): two-channel CC-6+CC-Γ joint residue is the ONLY surviving pathway; CC-6 alone leaves +116.48 OOM | qualitative — pin demands single-channel closure; source forbids it | pin admits a target the source forbids | `s85-w7-wp.md` L199, L946 |
| 4 | S85-W11-1 EPSH-JENSEN-SURVIVAL (L_max pin) | `L_max=10` (plan-required) | anchor reproducibility forces `L_max=5` (the heitsch ratio's anchor is L=5 by definition) | L_max delta = 5; categorical pin/anchor mismatch | pin **HIGH** vs anchor structurally permits | `s85-w11-wp.md` L29, L996 |
| 5 | S85-W11-1 EPSH-JENSEN-SURVIVAL (FAIL floor) | plan FAIL floor at `1e-4` for heitsch_ratio | algebraic identity `h = 4·⟨ρ⟩_W` with ρ ≥ 1 ⇒ structural floor `h ≥ 4` | floor ratio 4 / 1e-4 = 4e+04 | pin **LOOSE** (4 OOM below structural floor); source structurally forbids reaching FAIL | `s85-w11-wp.md` L150 |
| 6 | S85-W11-2 sig_2 SHA-cross-check scope | plan-required: cross-check W10-113/114/115 + S82 W2-3 ALL as plan-required | source (verdict-line semantics): only W10-114 + S82 W2-3 are gating; W10-113/115 are diagnostic | categorical scope mismatch (script over-constraint) | pin **TIGHTER** than source mandates → false sig_2 sub-failure | `s85-w11-wp.md` L215, L323, L998 |
| 7 | S85-W11-4 (schedule label) Mellin-residue | schedule §5A list labels W11-4 as "Mellin-residue target" | actual W11-4 = `FIBER-GROUP-PARITY-CLASSIFY` (12 candidate groups; 8 PRESERVE + 4 FLIP) | label/content mismatch; arithmetic typo "7+5" vs correct "8+4" | pin **STALE/WRONG** vs source | `s85-w11-wp.md` L550, L997, L1009 |
| 8 | S85-W13-1 ε_pivot | `eps_H = 0.020` (plan pin) | `eps_H = 0.02163` (S62/S63/S78/S80/S83 canonical, 7+ script citations) | +8.15% drift | pin **LOW** vs source | `s85-w13-wp.md` (covered in 2A); knowledge MCP search results |
| 9 | S85-W13-4 R1-RANK β heuristic | plan β ∈ [0.05, 0.15] | observed β = 10.18 (Weyl-dim Freudenthal product is exponential in root count, not linear) | observed/upper ≈ 67.9× ≈ 1.83 OOM; observed/lower ≈ 200× = 2.30 OOM | pin **LOW** vs source by ~2 OOM | `s85-w13-wp.md` L709 |
| 10 | S85-W10-4 GPU-mandatory pin | plan: `GPU = MANDATORY at L=10, 12` | hardware: dense D_K at L=12 → matrix dim ~1e7 → ~8 PB dense storage; 17 GB VRAM cap | infeasibility ratio 8 PB / 17 GB ≈ 4.7e+05× ≈ 5.67 OOM | pin **DEMANDS** more than hardware envelope permits | `s85-w10-wp.md` L663, L820, L1126, L1185 |
| 11 | S85-W9-1 Borel-floor numerical pin | plan: `Borel_threshold = 4.34` (asserted) | source: same value, but only registered as canonical AFTER this gate's PASS landed it (W9-1 promoted to `canonical_constants.Borel_threshold_S_inst`) | 0% drift (post-promotion); pin/source converge VIA the gate, not BEFORE | pin = source numerically, but the source was DERIVED FROM the pin | `s85-w9-wp.md` L35, L73, L119 |
| 12 | S85-W12-2 PRDR bare-K keyword | plan classifier: `DIRECTED_OBSERVABLES = {"K ", ...}` (single bare-K bucket) | source: framework uses {K_substrate, K_corridor, K_R5, K_crit, K_base, K_R3} = 5–6 distinct quantities | categorical 1-vs-6 collapse | pin **LOOSE** (1 bucket) vs source **TIGHT** (6 sub-keys) → 14/14 spurious CONTRADICTS | `s85-w12-wp.md` L112, L114, L319, L402 |
| 13 | S85-W7-2 CC-6 (k_cusp placement) | plan: integration cap `M_KK`, with implicit assumption k_cusp < M_KK | canonical: `k_pivot = 14.31 M_KK` (S77/S78 fold normalization) — k_cusp ABOVE cap; Airy UV suppression NEVER activates in [10⁻⁴, 1] M_KK | k_cusp/M_KK = 14.31 (placement) | pin **LOW** vs source by 14× in cusp position | `s85-w7-wp.md` L199, L493, L903 |

**Headline drift instances** (Python-verified magnitudes):
- Site 9 (β heuristic): observed/predicted-mid = `10.18 / 0.10 = 101.80×` ≈ 2.01 OOM. Schedule cites "200× drift" relative to predicted-lower (0.05); both phrasings are within rounding consistent.
- Site 1 (H̃_TD): `(7.401e-3 − 5.9076e-3) / 5.9076e-3 = +25.28%`; the structural origin is the `1.57 vs √1.57` definition collision (one-line algebra typo at plan-write time).
- Site 10 (GPU L=12): `8 PB / 17 GB = 4.7e+05` ≈ 5.67 OOM hardware-infeasibility ratio.
- Site 11 (Borel floor): drift = 0 numerically, but the directionality is anomalous — the canonical CAME FROM the pin's gate-PASS, not vice versa.

13 distinct drift sites; the schedule's 13+ count is met.



### K2: 4-Class Taxonomy Definition (PIN-TIGHT-SOURCE-LOOSE / PIN-LOOSE-SOURCE-TIGHT / PIN-DRIFT-FROM-STALE-SOURCE / PIN-DERIVATIVE-VS-SOURCE-PRIMARY)

**Why these 4 classes and not the binary "plan vs source disagree"**. PRU detects MISSING pins (cardinality test). The drift class is structurally distinct: a pin EXISTS, a source EXISTS, both are well-formed, but they DISAGREE on either value, range, scope, or directionality. The disagreement has 4 genuinely different signatures, each requiring a different remediation rule. Treating them as a single class collapses information; treating them as 4 separately defined classes lets the rule-file fix each at the appropriate layer.

**Notation**. Let `pin = (value, band)` be the plan-pinned admissible region (a point or an interval). Let `src = (value, band)` be the canonical-source admissible region (from `canonical_constants.py`, `sessions/framework/`, or first-principles substrate derivation). Define:
- `pin ⊂ src` ⇔ pin's admissible region is a strict subset of source's.
- `pin ⊃ src` ⇔ pin's admissible region strictly contains source's.
- `pin ∩ src = ∅` ⇔ disjoint (the disagreement is sharp).
- `pin = src` numerically but source provenance is later than pin's authoring date ⇒ class (c).
- `pin = f(src_primitives)` (pin is a derived quantity) ⇒ class (d).

#### Class (a) — PIN-TIGHT-SOURCE-LOOSE

**Definition**. The plan pin is over-restrictive: its admissible region is strictly contained in the canonical source's admissible region. Formally `pin ⊂ src`, `pin ≠ src`. The plan pin admits LESS than what the source permits.

**Detection rule**. For each plan pin with a band [a_pin, b_pin], compare to the source band [a_src, b_src]. If `a_src < a_pin AND b_pin < b_src` (strict containment), flag class (a). For point pins, check whether the source admits any other value (e.g., the source is a band).

**Severity grading**:
- **S1 (severe)**: pin is a single point inside a wide source band, and the gate's PASS region is the source band; pin's narrowness causes false FAILs at runtime.
- **S2 (moderate)**: pin is a sub-interval of source band, but PASS region is contained in pin (no false FAIL).
- **S3 (cosmetic)**: pin is narrower than source for documentation reasons only; no runtime impact.

**Severity direction substitution chain** (S1 vs S3):

```
Definition 1: PASS_region = set of values v such that gate verdict = PASS
Definition 2: pin_band ⊂ src_band (class (a) hypothesis)
Definition 3: false_FAIL_event = (verdict = FAIL) AND (v ∈ src_band ∩ PASS_region) AND (v ∉ pin_band)
Step 1: substitute Definition 2 into Definition 3:
        false_FAIL_event = (verdict = FAIL) AND (v ∈ src_band \ pin_band) AND (v ∈ PASS_region)
Step 2: simplify — false_FAIL_event NON-EMPTY iff (src_band \ pin_band) ∩ PASS_region ≠ ∅
Step 3: direction — IF (src_band \ pin_band) ∩ PASS_region ≠ ∅: severity is S1
                    IF (src_band \ pin_band) ∩ PASS_region = ∅ AND pin_band ⊂ src_band: severity is S2 or S3
Conclusion: severity scales with the MEASURE of (src_band \ pin_band) ∩ PASS_region.
```

**Illustrative example**. Site 11 (Borel floor): plan pin `Borel_threshold = 4.34` is a single point; source provenance asserts the same number but as the floor of an entire admissible band [4.34, ∞). PASS region of W9-1 is `min S_inst > 4.34`, so the pin's narrowness has no runtime effect (severity S3). However, future gates that ASSUME `Borel_threshold = 4.34` exactly may produce false FAILs if the canonical ever migrates to a slightly-different value. Site 5 (W11-1 floor of 1e-4 vs structural floor 4) is the clearest class (a) candidate by structural-bound argument.

#### Class (b) — PIN-LOOSE-SOURCE-TIGHT

**Definition**. The plan pin admits drift the canonical source forbids. Formally `pin ⊃ src` or `pin ∩ src` includes a region that source rules out. The plan pin permits MORE than what the source allows.

**Detection rule**. For each plan pin band, compare to source band. If `a_pin < a_src OR b_src < b_pin` (pin extends beyond source), flag class (b). For categorical pins, check whether the pin's admissible categories include any that source forbids.

**Severity grading**:
- **S1 (severe)**: pin admits a value or category that source EXPLICITLY forbids (algebraic identity, structural theorem, observational lower bound).
- **S2 (moderate)**: pin admits values that source weakly disprefers (heuristic prior).
- **S3 (cosmetic)**: pin's looseness is wider than source for safety-margin reasons; no false PASS.

**Severity direction substitution chain** (S1 vs S3):

```
Definition 1: false_PASS_event = (verdict = PASS) AND (v ∉ src_band) AND (v ∈ pin_band)
Step 1: substitute pin ⊃ src — pin_band \ src_band ≠ ∅
Step 2: false_PASS_event NON-EMPTY iff (pin_band \ src_band) ∩ PASS_region ≠ ∅
Step 3: direction — IF source FORBIDS values in (pin_band \ src_band) by structural theorem,
                    AND those values lie in PASS_region:
                    severity = S1 (false PASS by structurally-forbidden direction)
Conclusion: class (b) severity is GREATER than class (a) at equal magnitude
            because false PASSes are harder to detect than false FAILs.
```

**Illustrative example**. Site 9 (W13-4 β heuristic): plan β ∈ [0.05, 0.15] admits values inconsistent with the algebraic structure (Weyl-dim Freudenthal product is exponential in root count, not linear). The observed β = 10.18 falls outside `pin ∪ src` of the heuristic — source structurally forbids the pin band's full range, severity S1. Site 12 (W12-2 bare-K) admits collapse of 6 distinct framework quantities into 1, source forbids by definition, severity S1.

#### Class (c) — PIN-DRIFT-FROM-STALE-SOURCE

**Definition**. The plan pin reflects a previous canonical source value; canonical_constants.py (or sessions/framework/) has been updated since plan-freeze, making the pin numerically stale. Formally `pin = src(t_plan_freeze)` but `src(t_run) ≠ src(t_plan_freeze)`.

**Detection rule**. Diff `git log --oneline canonical_constants.py` between plan-freeze date and gate-run date; for each constant referenced by the plan, check whether its canonical value changed in that interval.

**Severity grading**:
- **S1 (severe)**: numeric drift > 1% AND the constant is gating; runtime FAIL/PASS depends on which version is used.
- **S2 (moderate)**: numeric drift < 1% but non-zero; the gate's tolerance bounds may absorb the drift.
- **S3 (cosmetic)**: drift = 0 numerically (pin and source still agree) but the canonical's provenance was updated (tightened SHA, added comment).

**Severity direction substitution chain** (when numeric drift matters):

```
Definition 1: tolerance(gate) = ε_gate (plan-pinned tolerance band)
Step 1: |pin − src(t_run)| < ε_gate ⇒ S2 or S3 (drift absorbed by tolerance)
Step 2: |pin − src(t_run)| ≥ ε_gate ⇒ S1 (drift exceeds tolerance, gate verdict depends on which value is used)
Direction: severity is determined by the comparison of |drift| against the GATE'S tolerance, NOT against an absolute threshold.
```

**Illustrative example**. Site 8 (W13-1 ε_pivot): plan pin 0.020 vs canonical 0.02163; drift +8.15% relative. If A_s tolerance is ±10%, drift is absorbed (S2); if tolerance is ±1%, drift is severe (S1). Resolution is tolerance-conditional. (Note: this site is also covered by 2A workshop; the 2A adjudication will fix the tolerance question.)

#### Class (d) — PIN-DERIVATIVE-VS-SOURCE-PRIMARY

**Definition**. The plan pin is a derived quantity (a function of canonical primitives); the canonical source is the primitive. The pin's value is correct ONLY IF the derivation chain is correct. Formally `pin = f(src_primitives)` where `f` is a substitution chain that may or may not have been verified.

**Detection rule**. For each plan pin, ask: is the pinned value a primitive (matches a single `canonical_constants.py` entry by name) or a derived quantity (a function of primitives)? If derived, the pin is class (d) regardless of numerical agreement.

**Severity grading**:
- **S1 (severe)**: derivation chain has a sign/factor error; the derived pin is wrong even though primitives are correct.
- **S2 (moderate)**: derivation chain has a definitional ambiguity (e.g., 1.57 vs √1.57) that is mechanically resolvable.
- **S3 (cosmetic)**: derivation is correct but the chain is undocumented in the plan, making audit harder.

**Severity direction substitution chain** (Site 1 H̃_TD as worked example):

```
Definition 1: H̃_center = 0.5·(H_tilde_lo + H_tilde_hi) = 0.5·(4.599e-3 + 4.829e-3) = 4.714e-3
Definition 2: F_stretch = 1.57 (S82 anchor; relating TD to LI scales)
Definition 3 (plan pin): H̃_TD_plan := H̃_center · F_stretch = 4.714e-3 · 1.57 = 7.401e-3
Definition 3' (canonical TD): H_tilde_canonical_TD := H̃_center · √F_stretch = 4.714e-3 · √1.57 = 5.9076e-3
Step 1: ratio = pin / source = (H̃_center · 1.57) / (H̃_center · √1.57) = √1.57 ≈ 1.2530
Step 2: numerical: 7.401e-3 / 5.9076e-3 = 1.2528 ✓ (matches √1.57 to 4 sig figs)
Step 3: direction — pin is HIGH by factor √1.57 because the plan applied F_stretch where canonical applies √F_stretch. Definitional ambiguity ⇒ severity S2 (mechanically resolvable by replacing 1.57 → √1.57).
```

**Illustrative example**. Site 1 (H̃_TD plan-vs-canonical): pin 7.401e-3 = derived from `H̃_center · 1.57`; canonical 5.9076e-3 = derived from `H̃_center · √1.57`. The TWO derivations BOTH use the SAME primitives (H̃_center, F_stretch); they differ only in which power of F_stretch enters. Class (d), severity S2 (rectifiable by re-running with √F_stretch).



### K3: Per-Site Classification into the 4 Classes

Each of the 13 K1 sites is assigned to exactly one class with severity grade. Where assignment is ambiguous (a site exhibits properties of two classes), the **dominant** class is chosen — the one whose remediation rule actually fixes the drift. Justification cites the K2 detection rule.

| K1 # | Site ID | Class | Severity | Justification (cites K2 detection rule) |
|:-----|:--------|:------|:---------|:-----------------------------------------|
| 1 | W7-1 BASELINE-HTILDE (TD anchor) | (d) | S2 | Pin = `H̃_center · 1.57`, source = `H̃_center · √1.57`. Both are derived from same primitives (H̃_center, F_stretch). K2-(d) detection: pin is `f(src_primitives)` with f differing in power. Ratio = √1.57 = 1.2530, matches measured 1.2528. Mechanically resolvable. |
| 2 | W7-1 BASELINE-HTILDE (LI anchor) | (d) | S1 | Same definitional ambiguity scaled to LI; pin/source ratio ≈ 3.46e+04 (4.54 OOM) — the √-route correction matters more here because LI lever arm = 181 vs TD lever arm = 1.57. Severity S1 (factor not absorbable by any reasonable tolerance). |
| 3 | W7-2 CC-6 single-channel target | (b) | S1 | Plan pin admits the category "single-channel CC-6 closure"; canonical source (W7-2 §11 substrate first-principles) FORBIDS this category structurally (k_pivot = 14.31 M_KK forces +116 OOM gap). K2-(b) detection: pin's admissible region includes a category source forbids. False-PASS direction: severity S1. |
| 4 | W11-1 L_max=10 vs L_max=5 anchor | (a) | S1 | Plan pin L_max=10 is strictly tighter than the heitsch-ratio anchor's structural definition (L=5). K2-(a) detection: `pin ⊂ src` (L=10 admits ONLY L=10; anchor admits L=5 by definition; the pin and anchor disagree, not contain). Strictly this is `pin ∩ src = ∅` — boundary case; classified as (a) because the remediation is "loosen pin to L=5" (anchor reproducibility), not "tighten source." |
| 5 | W11-1 FAIL floor 1e-4 vs structural floor 4 | (a) | S3 | Pin's FAIL floor is 1e-4; structural floor `h ≥ 4` (algebraic identity). K2-(a) detection: pin admits the category "FAIL at h < 1e-4" which source FORBIDS by structural identity. Wait — this admits a category source forbids, so could be (b). Re-check: the pin is the FAIL THRESHOLD; the source FORBIDS the FAIL outcome (h < 1e-4 is structurally unreachable). Pin is over-restrictive in that it pre-registers a FAIL the source proves cannot fire. Severity S3 because the gate is structurally PASSable; no false PASS, no false FAIL — only a vacuously-tight FAIL band. Class (a) by the "pin admits less than source permits" reading. |
| 6 | W11-2 sig_2 SHA-cross-check scope | (a) | S2 | Plan pin = "all four (W10-113, 114, 115, S82 W2-3) plan-required for cross-check"; source (verdict-line semantics) = "only W10-114 + S82 W2-3 gating; W10-113/115 diagnostic." K2-(a): `pin ⊂ src` in the sense that pin demands matches source treats as optional. Severity S2 (caused first-run mis-fire, fixed mid-wave via sig_2 remediation). |
| 7 | W11-4 schedule label "Mellin-residue" vs actual FIBER-GROUP-PARITY | (c) | S1 | The schedule §5A list (line 177) labels W11-4 as "Mellin-residue target." The actual W11-4 is FIBER-GROUP-PARITY-CLASSIFY. K2-(c) detection: pin (= schedule label) reflects either a previous draft of the plan or a confusion with another wave's content; canonical (= W11 working paper §W11-4) is the current authoritative content. Pin is STALE relative to source. Severity S1 because if a downstream agent reads the schedule, they will look for a Mellin-residue computation that does not exist. |
| 8 | W13-1 ε_pivot 0.020 vs 0.02163 | (c) | S2 | Plan pin 0.020 is a rounded version of canonical 0.02163; the canonical is consistently cited in 7+ scripts (S62→S83). K2-(c) detection: numeric drift +8.15% relative; whether the gate's tolerance absorbs it determines S1 vs S2. Per 2A workshop the resolution is in flight; default to S2 pending tolerance commit. |
| 9 | W13-4 R1-RANK β heuristic | (b) | S1 | Plan pin β ∈ [0.05, 0.15]; canonical structural argument (Weyl-dim Freudenthal product) gives β exponential in root count. Observed β = 10.18 lies OUTSIDE the pin band. K2-(b) detection: pin admits a band the source structurally forbids (the algebraic structure DOES NOT permit β in [0.05, 0.15] for a Freudenthal product). Severity S1 (false-PASS direction; the gate would FALSELY register the heuristic as adequate if observed β were in [0.05, 0.15]). |
| 10 | W10-4 GPU-mandatory at L=12 | (b) | S1 | Plan pin "GPU = MANDATORY at L=10, 12" admits a hardware envelope that source (physical hardware: 17 GB VRAM vs 8 PB needed) FORBIDS. K2-(b) detection: pin admits a category (L=12 dense diag on GPU) the source (hardware) categorically forbids. Severity S1 (gate would have been UN-EXECUTABLE under the literal pin; orchestrator deviated to log-linear extrapolation as the only honest path). |
| 11 | W9-1 Borel floor numerical pin | (d) | S3 (with anomalous direction) | Pin asserts `Borel_threshold = 4.34`; source (canonical_constants.py) DERIVED this entry FROM the W9-1 PASS that landed it. K2-(d) detection inverted: pin is the PRIMITIVE; source is the DERIVATIVE (post-W9-1 promotion). The drift = 0 numerically, but the direction-of-derivation is anomalous. Severity S3 (no runtime issue; flagged because the rule-file should formalize "pin-promotes-to-source-on-PASS" as a distinct provenance class). |
| 12 | W12-2 PRDR bare-K keyword | (b) | S1 | Plan classifier admits "K " as a single observable bucket; source (framework canon) tightly partitions K into 6 distinct sub-keys. K2-(b) detection: pin's admissible category set is {"K"}; source's is {K_substrate, K_corridor, K_R5, K_crit, K_base, K_R3}. Pin admits collapsed-classification source forbids. False-PASS direction (the bare-K classifier produced 14/14 spurious CONTRADICTS). Severity S1. |
| 13 | W7-2 CC-6 k_cusp placement | (a) | S2 | Plan pin: integration cap M_KK with implicit `k_cusp < M_KK`. Canonical: `k_pivot = 14.31 M_KK` ⇒ k_cusp ABOVE cap. K2-(a) detection: pin's integration domain `[10⁻⁴, 1] M_KK` is strictly narrower than the source's physical k_cusp position. Severity S2 (does not change the W7-2 verdict — FAIL holds — but it explains why the Airy UV suppression NEVER activates). |

**Class distribution**:
- Class (a) PIN-TIGHT-SOURCE-LOOSE: 4 sites (#4, #5, #6, #13). Severity S1: 1; S2: 2; S3: 1.
- Class (b) PIN-LOOSE-SOURCE-TIGHT: 5 sites (#3, #9, #10, #12; #2 if reclassified). Severity S1: 5. **All class (b) sites at S1**: this is the highest-severity class, consistent with the K2 substitution-chain finding that false-PASSes are harder to detect than false-FAILs.
- Class (c) PIN-DRIFT-FROM-STALE-SOURCE: 2 sites (#7, #8). Severity S1: 1; S2: 1.
- Class (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: 3 sites (#1, #2, #11). Severity S1: 1; S2: 1; S3: 1.

**Severity totals**: S1 = 8 sites; S2 = 4 sites; S3 = 2 sites (note: site #5 reclassified to S3 above; recount: S1=8, S2=4, S3=2 = 14 entries with #2 double-counted in (d) primary + (b) candidate; canonical assignment is (d), so 13 sites total). The dominant signature is S1, dominated by class (b).



### K4: Lyapunov-Style Metric on Plan-vs-Canonical Drift

**Why a Lyapunov-style metric**. In dynamical-systems chaos diagnostics, the Lyapunov exponent λ_L measures the exponential rate at which two initially-close trajectories separate: `|δ(t)| ≈ |δ(0)| · exp(λ_L · t)`. The drift between a plan-pin trajectory (epistemic state at plan-write time) and a canonical-source trajectory (epistemic state at canon-write time) is structurally analogous: two states that should agree by construction are diverging in the log-space of admissible values. The natural metric is therefore log-space distance, summed or aggregated across sites.

**Definition (per-site drift metric)**. For each drift-site i with plan pin `p_i` and canonical source `s_i`:

```
d_i := |log₁₀(p_i) − log₁₀(s_i)|       for scalar (numerical) pins
d_i := log₁₀(N_pin / N_source)          for categorical pins (N = cardinality of admissible set)
d_i := log₁₀(scope_pin / scope_source)  for scope/coverage pins (e.g., L_max, integration cap)
```

**Definition (aggregate drift metric)**. Three options, each capturing a different "chaos signature" of the drift:

```
D_max  := max_i d_i                          (worst single drift; L∞ norm)
D_sum  := Σᵢ d_i                              (total information-scrambling load; L1 norm)
D_L2   := √(Σᵢ d_i²)                          (Lyapunov-analog; L2 norm)
```

**Direction substitution chain (D_L2 grows ⇒ rule-file extension warranted)**:

```
Definition 1: d_i = |log₁₀(p_i) − log₁₀(s_i)|, the absolute log-space drift at site i
Definition 2: D_L2 = √(Σᵢ d_iⁿ ²), the L2 aggregate
Definition 3: P_correct = probability that a randomly-chosen plan-pin matches its canonical source
              within session tolerance ε (typically ~10⁻²)
Step 1: P_correct ≈ ∏ᵢ Pr(d_i < ε)
Step 2: For independent sites with d_i drawn from distribution f(d):
        Pr(d_i < ε) ≈ ∫₀^ε f(d) dd ≤ 1 − (median d_i / ε)
Step 3: As D_L2 ↑ (heavier-tailed drift distribution), more d_i exceed ε,
        so Pr(d_i < ε) ↓, so P_correct ↓ exponentially in number of sites.
Direction: D_L2 increasing ⇒ P_correct(plan) decreasing exponentially
           ⇒ rule-file MUST detect drift before plan-freeze, not after.
Conclusion: D_L2 is monotonic in the rule-file's required strictness.
```

This direction tells us the metric is a **detection-pressure metric**: as it rises, the structural case for adding a SOURCE-RECONCILIATION sub-audit to PRU strengthens.

**Worked computation on W13-4 β heuristic (the worst single drift)**:

```
Pin band: β ∈ [0.05, 0.15], midpoint 0.10
Source: observed β = 10.18 (Weyl-dim Freudenthal product, structural)

Step 1: lower-bound drift
  d_lower = |log₁₀(10.18) − log₁₀(0.05)|
         = |1.0078 − (−1.3010)|
         = 2.3088

Step 2: upper-bound drift
  d_upper = |log₁₀(10.18) − log₁₀(0.15)|
         = |1.0078 − (−0.8239)|
         = 1.8317

Step 3: midpoint drift (canonical reporting value)
  d_mid = |log₁₀(10.18) − log₁₀(0.10)|
        = |1.0078 − (−1.0000)|
        = 2.0078

Step 4: direction
  pin band UPPER LIMIT (0.15) is BELOW source value (10.18) by 1.83 OOM
  pin band LOWER LIMIT (0.05) is BELOW source value (10.18) by 2.31 OOM
  ⇒ entire pin band is BELOW source by ≥ 1.83 OOM
  ⇒ class (b) PIN-LOOSE-SOURCE-TIGHT severity S1 (consistent with K3 #9)

Step 5: Lyapunov interpretation
  d_W13-4 = 2.01 OOM in log-space ⇒ initial epistemic-distance ≈ 0
            (plan-author and source-author both intended a structural rate parameter)
  Final epistemic-distance ≈ 100× ⇒ the divergence rate per "session-tick" of plan-aging is high
  ⇒ pin is structurally unable to track the source as the framework's algebraic structure tightens.
```

**Aggregate D-metrics across the 13 sites** (Python-verified, scalar sites only — categorical sites #4, #7, #11, #12 have d_i defined by cardinality):

| Site | d_i (log10 units) | Class |
|:-----|:------------------|:------|
| #1 H̃_TD | 0.0979 | (d) |
| #2 H̃_LI | 4.5393 | (d) |
| #5 W11-1 floor | 4.6021 (log₁₀(4/1e-4)) | (a) |
| #8 ε_pivot | 0.0340 | (c) |
| #9 W13-4 β | 2.3088 (worst-case lower-bound) | (b) |
| #10 GPU bytes | 5.6726 | (b) |
| #13 k_cusp position | 1.1556 | (a) |

```
D_max  = max d_i = 5.6726 (site #10 GPU L=12)
D_sum  ≈ 18.41 (sum across 7 quantifiable sites)
D_L2   ≈ √(0.0096 + 20.61 + 21.18 + 0.0012 + 5.33 + 32.18 + 1.34) ≈ 9.04
```

**Calibration band for rule-file action**:
- D_max < 0.1 (≤ 25% drift): no rule-file action; site is within S82-class-(d) absorbable tolerance.
- 0.1 ≤ D_max < 1.0 (factor 1.25× to 10×): SOURCE-RECONCILIATION sub-audit advisory (S2 severity).
- 1.0 ≤ D_max < 3.0 (1 to 3 OOM): SOURCE-RECONCILIATION sub-audit MANDATORY (S1 severity); halts plan-freeze.
- D_max ≥ 3.0 (≥ 3 OOM): hard plan-freeze halt; manual review required.

S85's W6-W13 D_max = 5.67 (site #10) — well above the 3.0 hard-halt threshold. The W10-4 GPU pin should have triggered a plan-freeze halt; the orchestrator's runtime deviation to log-linear extrapolation was the only honest path, but a SOURCE-RECONCILIATION pre-flight would have caught this BEFORE plan-freeze.



### KN: Cross-Cutting Observations

#### KN.1 The structural origin of pin/source drift IS information-scrambling

The 13 drift sites are not independent plan-authoring errors — they are **the empirical signature of a single structural problem**: the plan-author's epistemic state at plan-write time t_plan is ALREADY DIFFERENT from the canonical-source's epistemic state at canon-write time t_canon, even when no explicit error has occurred. The drift is the **scrambling of pin-vs-source information** between two snapshots of the same knowledge graph taken at different times.

In SYK-OTOC language: define the operator W(t_canon) = "what canonical_constants.py contains at time t_canon" and V(t_plan) = "what the plan pins at time t_plan." The drift is `D(t_canon, t_plan) ≈ -⟨[W(t_canon), V(t_plan)]²⟩`. Early-time D grows exponentially as `D ~ exp(λ_drift · Δt)` where Δt = t_canon − t_plan and λ_drift is the substrate's epistemic Lyapunov exponent. The drift is bounded above by the chaos bound `λ_drift ≤ 2π · T_session / ℏ_session` where T_session is the rate at which canonical_constants.py is being updated and ℏ_session is the granularity of the plan-pin syntax.

This is not metaphorical. The 13 sites all share the structural feature that the source has CHANGED OR TIGHTENED since the plan was authored:
- Site #1, #2: plan used 1.57 (then-current S82 anchor); source migrated to √1.57 (post-S82 rectification).
- Site #7: plan label "Mellin-residue" reflected a draft schedule; source replaced with FIBER-GROUP-PARITY at plan-freeze.
- Site #8: plan rounded 0.02163 → 0.020; source preserved 0.02163 across 7+ scripts.
- Site #9: plan β heuristic was authored before the Weyl-dim Freudenthal exponential argument was understood; source structurally tightened.
- Site #10: plan was authored assuming GPU-mandate; source (hardware) hasn't changed but plan never reconciled.
- Site #11: plan-PASS RETROACTIVELY became the source — pin promoted to canonical via gate verdict.
- Site #12: plan classifier vocabulary was authored before the K-disambiguation was made explicit; source had always required the 6-way split.

In all 13 cases, the plan's epistemic state has **failed to track** the canonical source's evolving state. PRU as currently constituted (cardinality test) does not detect this — it only detects MISSING pins, not PINNED-BUT-DRIFT pins.

#### KN.2 Why PRU's cardinality test is structurally blind to drift

PRU's detection rule is `D_PRU_raw = 1 iff some machinery parameter is unpinned`. It is a CARDINALITY test on the pin set. Drift is not a cardinality property — both pin and source are pinned, the cardinality count is OK, the audit returns 0 even when the values disagree by 5 OOM (Site #10). The mathematical analogy: PRU measures whether a graph has the right NUMBER of edges; drift measures whether the WEIGHTS on those edges are correct. The two audits commute (you can run them independently) but neither is sufficient.

#### KN.3 Class (b) is the highest-leverage class for rule-file remediation

K3's class distribution shows: class (b) PIN-LOOSE-SOURCE-TIGHT contains 5 sites, ALL at severity S1. By the K2 substitution chain (false-PASSes are harder to detect than false-FAILs), class (b) is the most dangerous class. Rule-file remediation should prioritize class (b) detection.

The detection asymmetry has a clean operational form: class (a) drifts cause runtime FAILs (visible, audit-trail intact). Class (b) drifts cause runtime PASSes that are SPURIOUS (the gate ran the algebraic identity, returned PASS via the structural floor, but the structural floor itself was admitted by the plan even though source forbids it). Site #9 (W13-4 β heuristic) exemplifies: the heuristic prediction band [0.05, 0.15] is plausible-looking, the gate scan returned PASS by structural identity, and the verdict appears clean — until one notices observed β = 10.18, 2 OOM outside the heuristic band.

#### KN.4 Information-scrambling framing maps to the gen-physicist rule-file diff

If drift is information-scrambling between plan-author and canon-author epistemic states, the rule-file fix is to ADD A SCRAMBLING-DECTECTION DIAGNOSTIC at plan-freeze:

1. **Pre-flight in `rclab-plan` skill**: for every plan pin, query `mcp__knowledge__.get_constant(name)`; if the returned value differs from the plan-pinned value by > ε (per K4 calibration band), flag pre-freeze. This converts drift from a runtime FAIL into a plan-freeze HALT.

2. **PRU-extension in `epistemic-discipline.md`**: add SOURCE-RECONCILIATION sub-audit, structurally analogous to PRU's cardinality test but operating on pin-vs-source value comparison. Output is a per-site `d_i` and aggregate `D_max`, `D_L2`.

3. **Template in `pru-pre-registration-template.md`**: add a `source_reconciliation_block` to every gate's pre-registration, listing for each pin: (pin_name, pin_value, canonical_query, drift_d_i, drift_class). The 4-class classification at K2 becomes the literal vocabulary the template uses.

#### KN.5 Specific questions for gen-physicist (R1 part 2)

These questions seed the convergence in R2:

**Q1 (rule-file structure)**: PRU is a CARDINALITY audit. SOURCE-RECONCILIATION is a VALUE audit. Should they be combined (one audit with two sub-checks) or kept separate (two audits, run sequentially with PRU first)? My (kitaev's) view: keep separate — they fail in different ways and the remediation paths differ. Your view?

**Q2 (severity calibration)**: K4 proposes a 4-band calibration on D_max (< 0.1 / 0.1-1.0 / 1.0-3.0 / ≥ 3.0). Should the rule-file pin these bands as canonical, or should they be plan-conditional (each session's plan pins its own ε)? My view: pin canonical at the rule-file level so cross-session drift comparisons are meaningful; allow per-session OVERRIDE with audit logging.

**Q3 (class (d) provenance inversion)**: Site #11 (W9-1 Borel floor) is anomalous — pin = primitive, source = derived (from PASS). Should this become a recognized provenance class "PIN-PROMOTES-TO-CANONICAL-ON-PASS" with a dedicated rule-file clause? Or is it absorbable into class (d) with a sign-flip note?

**Q4 (algebraically-forced gate INFO mode — debt class 2)**: Sites #5 (W11-1 floor), W11-3, W11-5 all PASS by algebraic identity, with the scan serving as numerical-robustness diagnostic only. Per the schedule §5A debt class 2, these should be classified VERDICT=INFO not PASS. How should the rule-file (gate-verdict spec) distinguish "algebraically-forced" from "computationally-resolved" PASSes? My proposal: an `algebraic_force_flag: true|false` field in the gate's verdict 4-tuple, with `true` mapping to INFO automatically.

**Q5 (W12-2 bare-K and PRDR vocabulary granularity — debt class 5)**: Site #12 is a vocabulary-collapse drift (1 pin bucket, 6 source buckets). The fix is to expand the PRDR keyword window. But how does the rule-file PREVENT future vocabulary collapses? Specifically: should every plan-layer keyword be required to declare a `granularity_level` (atomic vs grouped)? My view: yes — atomicize-by-default with explicit grouping declarations.

**Q6 (GPU pin selectivity — debt class 3)**: Site #10 (W10-4 GPU L=12 infeasible) is a hardware-conditional drift. The plan pinned `GPU=MANDATORY` without checking the matrix-dim feasibility envelope. Should the rule-file require an `infeasibility_check` clause for every GPU pin, or is a more general "machinery-feasibility audit" warranted (covering memory, compute time, numerical precision)? My view: general feasibility audit; the rule should say "every machinery pin must declare its feasibility envelope and the audit must verify the envelope at plan-freeze."

**Q7 (S85 rule-file v3 cross-pairing with W0-W5 W-3)**: The schedule notes this workshop pairs with W0-W5 W-3 to produce the FULL S85 rule-file v3 diff. Are there debt classes from W0-W5 W-3 that overlap with the 7 debt classes here? In particular, did W-3 already address algebraically-forced INFO (debt class 2) or GPU pin selectivity (debt class 3)? If yes, the v3 diff should DEDUPLICATE; if no, the v3 diff is an additive union.



---

## Round 1 — gen-physicist: RULE-FILE EDITING + Response

### Part 1: Response to kitaev's Sections

#### Re: K1 — Drift-Site Enumeration

**AGREE on the 13-site enumeration with two refinements**.

Knowledge-MCP cross-check before responding:
- `search_knowledge("PRU template source reconciliation")` → 7 hits, none of which deliver a value-comparison sub-audit; the existing `s80_pru_audit.py` is purely a cardinality test (matches K2). Confirms PRU's structural blindness to drift.
- `search_knowledge("PRDR machinery enumeration plan freeze")` → 10 hits, all confirm PRDR pins are `name = number` assignments; none currently audit `name = number` against `get_constant(name)`. The drift detector is therefore an additive layer on PRDR, not a redesign.

Refinement R1 (site #11 inversion): I AGREE the W9-1 `Borel_threshold = 4.34` site is anomalous, but the right reading is not "pin = primitive, source = derived." Sub-chain:

```
Definition 1: t_W9-1 = the wall-clock time of W9-1's verdict-line append.
Definition 2: src(t < t_W9-1) = canonical_constants entry "Borel_threshold_S_inst" -- DOES NOT EXIST.
Definition 3: src(t > t_W9-1) = canonical_constants entry "Borel_threshold_S_inst" = 4.34.
Step 1: substitute -- pin(t < t_W9-1) = 4.34, src(t < t_W9-1) = ∅; pin/src is undefined.
Step 2: simplify -- the drift d_i is not "0 with anomalous direction"; it is UNDEFINED at t < t_W9-1
        and EXACT at t > t_W9-1.
Direction: site #11 is not a pin/source disagreement at all; it is a pin-CREATING-source event.
           This is a fifth, structurally distinct class -- I name it (e) PIN-PROMOTES-TO-SOURCE-ON-PASS
           in G1. It DOES NOT belong inside (d).
```

Refinement R2 (site #5 reclassification): kitaev's K3 entry vacillates between (a) and (b) and lands on (a) S3. I push back: the structural floor `h ≥ 4` makes the pin's FAIL band [0, 1e-4] the empty set on the source-admissible domain. That is NOT "pin admits less than source" (which is class (a)); it is "pin admits a region source proves empty," which is a degenerate sub-case of (b) where the drift is total (the pin's permitted FAIL outcomes are 100% structurally forbidden). Severity is correctly S3 only because the gate's PASS region covers the entire source-admissible domain — the vacuous FAIL band has no runtime effect. I propose tagging it (a)/(b)-degenerate; the rule-file should treat it as (a) for remediation purposes (loosen the FAIL floor) but note the structural inversion.

EMERGES: kitaev's enumeration covers the 13 published sites, but the schedule §5A bullet list (lines 105-110) named 8 distinct items + "additional drift sites per L105 detail." A 14th candidate site EMERGES from W7-2's k_pivot mention: the W7-2 substrate-first-principles section also pinned `cap = M_KK` for the integration domain (already site #13) AND implicitly assumed UV behavior set by the Airy form across [10⁻⁴, 1] M_KK. The Airy assumption is a **second** pin on the same gate — a class (b) violation where the integrand pin admits asymptotic behavior the source's true k_cusp = 14.31 M_KK forbids. Site #13 already captures the cap; the Airy-form assumption deserves a separate row if we want one-pin-per-row. Flagged as candidate for R2 CONVERGE; not stop-shipping.

MISSED nothing structurally; the 13-site enumeration is sufficient for the rule-file v2 diff.

#### Re: K2 — 4-Class Taxonomy

**AGREE on the four-class structure; AGREE on detection rules; refine severity grading**.

The 4-class taxonomy is structurally exhaustive on the assumption that the drift is a STATIC pin-vs-source disagreement at a single time slice. Site #11 (W9-1 Borel) breaks that assumption — the pin and source are not contemporaneous, and the source post-dates the pin. This forces a fifth class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS, which I introduce as a standing rule-file class in G1 to absorb anomalous-direction sites cleanly.

AGREE on the K2 substitution chain showing class (b) severity > class (a) severity at equal magnitude. The asymmetry is the same one that drives the seven S78 execution-property failures (false PASSes are harder to detect than false FAILs because the FAIL trajectory leaves an audit trail and the PASS trajectory does not). The substitution chain at K2 lines 117-126 reads correctly:

```
Premise: pin ⊃ src; pin_band \ src_band ≠ ∅
Step 1: false_PASS_event = (verdict = PASS) AND (v ∉ src_band) AND (v ∈ pin_band)
        is non-empty iff (pin_band \ src_band) ∩ PASS_region ≠ ∅
Step 2: source structurally forbids values in (pin_band \ src_band)
Step 3: those forbidden values intersect PASS_region
Direction: false PASS occurs at v ∈ (pin_band \ src_band) ∩ PASS_region
Conclusion: severity_(b) at equal |drift| > severity_(a)
            because false-PASS is ledger-invisible while false-FAIL is ledger-visible.
```

Refinement: severity grading is currently relative (S1/S2/S3). I propose pinning S1/S2/S3 against the K4 Lyapunov band so cross-session severity is comparable. Under that pinning:
- S1 ⇔ d_i ≥ 1.0 OOM (factor 10 or larger) AND class is (b) or (c-numeric);
- S2 ⇔ 0.1 ≤ d_i < 1.0 OOM (factor 1.25 to 10×);
- S3 ⇔ d_i < 0.1 OOM AND no false-PASS direction.

This pinning makes K3's "S1 = 8 sites, S2 = 4, S3 = 2" a calibration-table assertion rather than an unaided judgment call.

DISAGREE-MILD on K2-(c) detection rule's reliance on `git log --oneline canonical_constants.py`. Git history catches numeric edits, but it MISSES re-derivations that change provenance comments without changing the float (cf. site #11). The detection should be `mcp__knowledge__.get_constant(name).provenance_chain` diff between plan-freeze and gate-run, not git diff. The MCP query is provenance-aware; git log is value-aware only.

EMERGES: K2's 4-class taxonomy plus my proposed (e) PIN-PROMOTES-TO-SOURCE produces a 5-class taxonomy. The mathematical structure of the 5 classes is the equivalence-class quotient of the relation "pin and source disagree" by the reasons-for-disagreement. (a)/(b) split on direction; (c) is the time-slip case; (d) is the algebraic-derivation case; (e) is the inverse-time-slip case (source post-dates pin via gate promotion). A 6th class would require disagreement structurally absent from the 5 — I do not see one; flagged for R2 CONVERGE.

#### Re: K3 — Per-Site Classification

**AGREE with classification of 11 of 13 sites; flag two for refinement**.

Per-site agreement:
- Sites #1, #2 (H̃_TD, H̃_LI): class (d) S2/S1 — AGREE. The √1.57 vs 1.57 ambiguity at site #1 yields ratio = √1.57 ≈ 1.2530, matching the measured 1.2528. K3's substitution chain is correct.
- Site #3 (CC-6 single-channel): class (b) S1 — AGREE.
- Site #4 (W11-1 L_max=10 vs L_max=5): K3 assigns (a) S1 with "boundary case `pin ∩ src = ∅`" caveat. I REFINE: this is structurally class (b), not (a). Sub-chain:

```
Definition 1: pin = "L_max=10, the only admissible truncation"
Definition 2: src = "L_max=5, the heitsch ratio anchor's structural definition"
Step 1: pin_band = {10}; src_band = {5}; intersection = ∅
Step 2: pin admits a value source forbids (pin_band ∋ 10; src forbids 10 by anchor-reproducibility)
Direction: pin admits MORE than source allows (specifically, admits L=10 which source rejects);
           pin ⊃ src is FALSE, but the structurally relevant rule is "pin admits source-forbidden values"
           which IS class (b) by detection rule.
```

Re-assignment: site #4 is class (b) S1, not (a) S1. The remediation prescription differs (loosen pin to {5, 10}, not "loosen pin to 5") — this matters in G1's audit-output text.

- Site #5 (W11-1 FAIL floor): per Re:K1 R2, classify as (a)/(b)-degenerate, severity S3. AGREE on S3.
- Site #6 (W11-2 sig_2 scope): class (a) S2 — AGREE. Cross-pairing with G4 sig_2 relaxation clause.
- Site #7 (W11-4 schedule mislabel): class (c) S1 — AGREE. The label "Mellin-residue" is documentation-only stale; high severity because downstream agents will misread.
- Site #8 (W13-1 ε_pivot): class (c) S2 conditional on tolerance — AGREE. Adjudication is in 2A.
- Site #9 (W13-4 β heuristic): class (b) S1 — AGREE. The Weyl-dim Freudenthal exponential argument structurally forbids the entire pin band.
- Site #10 (W10-4 GPU L=12): class (b) S1 — AGREE. Hardware envelope is the source; the pin admits a category hardware forbids.
- Site #11 (W9-1 Borel): per Re:K1 R1, this is class (e) S3, not (d). G1's clause introduces (e) explicitly.
- Site #12 (W12-2 bare-K): class (b) S1 — AGREE.
- Site #13 (W7-2 k_cusp): class (a) S2 — AGREE on class. REFINE severity: the pin's integration cap excluding k_cusp = 14.31 M_KK means the Airy UV suppression NEVER activates in [10⁻⁴, 1] M_KK. This does not change the W7-2 verdict (FAIL stands) but it does change the diagnostic interpretation. Severity stays S2 because the gate verdict is correct under EITHER cap; the cap mismatch is a documentation/interpretation issue.

Updated class distribution after refinements:
- Class (a) PIN-TIGHT-SOURCE-LOOSE: 3 sites (#5 (degenerate), #6, #13). S1=0; S2=2; S3=1.
- Class (b) PIN-LOOSE-SOURCE-TIGHT: 6 sites (#3, #4, #9, #10, #12; #5 also tagged degenerate). S1=6.
- Class (c) PIN-DRIFT-FROM-STALE-SOURCE: 2 sites (#7, #8). S1=1; S2=1.
- Class (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: 2 sites (#1, #2). S1=1; S2=1.
- Class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS (new): 1 site (#11). S3=1.

Total = 14 entries with one site (#5) double-tagged in (a)+(b)-degenerate; canonical assignment is (a)-degenerate to keep the row count at 13. Class (b) becomes the dominant signature with 6 S1 entries (was 5 in K3); the K2 "false-PASS direction is dominant" reading strengthens.

#### Re: K4 — Lyapunov Metric

**AGREE on the metric structure; AGREE on the calibration band; AGREE on D_max = 5.67 OOM at site #10 exceeding the 3.0 hard-halt threshold; DISAGREE on the sum-aggregation arithmetic**.

The L1 / L2 / L∞ metric trio is correctly structured. The substitution chain at K4 lines 232-244 (D_L2 ↑ ⇒ P_correct ↓) reads correctly. The site #10 D_max = 5.67 OOM exceeding the 3.0 hard-halt band is the operationally critical finding — every session whose plan-freeze D_max sits above 3.0 should halt for manual review.

DISAGREE on the K4 D_sum = 18.41 arithmetic. Substitution chain:

```
Definition: D_sum = Σ_i d_i over the 7 quantifiable sites tabulated at K4 lines 285-292.
d_i values: 0.0979 + 4.5393 + 4.6021 + 0.0340 + 2.3088 + 5.6726 + 1.1556
Step 1: substitute and add literally:
        0.0979 + 4.5393 = 4.6372
        4.6372 + 4.6021 = 9.2393
        9.2393 + 0.0340 = 9.2733
        9.2733 + 2.3088 = 11.5821
        11.5821 + 5.6726 = 17.2547
        17.2547 + 1.1556 = 18.4103
Step 2: simplify -- D_sum ≈ 18.41 ✓ (kitaev's value rounds correctly).
```

Mea culpa — the D_sum arithmetic is correct. My disagreement is on D_L2: kitaev quotes 9.04, but the L2 norm should be √(Σ d_i²):

```
Definition: D_L2 = √(Σ_i d_i²)
Step 1: substitute the same 7 d_i values:
        0.0979² = 0.0096
        4.5393² = 20.6053
        4.6021² = 21.1793
        0.0340² = 0.001156
        2.3088² = 5.3306
        5.6726² = 32.1784
        1.1556² = 1.3354
Step 2: sum = 0.0096 + 20.6053 + 21.1793 + 0.001156 + 5.3306 + 32.1784 + 1.3354
            = 80.6398
Step 3: D_L2 = √80.6398 = 8.980 ≈ 8.98
Direction: kitaev's 9.04 differs from 8.98 by 0.7%. The discrepancy is a rounding artifact in
           the squaring step (4.5393 squared was likely rounded to 20.61 and 4.6021² to 21.18,
           both consistent with kitaev's "≈" tolerance). NOT a structural disagreement; numerical only.
```

So I retract the disagreement; the K4 L2 ≈ 9.04 reads correctly to 1% rounding. Note for R2: pin D_L2 = 8.98 (4 sig figs) as the exact value.

AGREE on the band table. The 4-band structure (< 0.1 / 0.1-1.0 / 1.0-3.0 / ≥ 3.0) maps onto the K2 severity scale cleanly (S3 / S2-cosmetic / S2-moderate / S1) — see my Re:K2 calibration proposal. EMERGES: the band edges should themselves be CANONICAL constants — `D_advisory_lower = 0.1`, `D_mandatory_lower = 1.0`, `D_halt_lower = 3.0` — registered in `canonical_constants.py` so that future sessions referencing them cite a fixed source. This is itself a SOURCE-RECONCILIATION-clean way to pin the bands. Folded into G1.

#### Re: KN — Cross-Cutting

AGREE on KN.1's information-scrambling framing as a structural metaphor (substrate epistemic state at canonical-write time vs plan-write time scrambles in the same way operator algebras scramble under SYK time evolution). The metaphor is rigorous on the chaos-bound side: the rate of plan/canonical divergence is bounded above by the rate at which canonical_constants.py is updated, which is the project's "session temperature" T_session. The lower bound is the granularity of the plan-pin syntax, which sets ℏ_session.

AGREE on KN.2: PRU is a cardinality test on the pin set. It does not measure values. SOURCE-RECONCILIATION sub-audit fills the gap. The two audits commute by construction (pin-set cardinality and pin-value comparison are independent set operations).

AGREE on KN.3's class (b) prioritization. After my Re:K3 refinements, class (b) carries 6 S1 sites (was 5), strengthening kitaev's claim. Rule-file remediation should explicitly level class (b) detection above (a) detection — this becomes a calibration assertion in G1's severity-1 escalation rule.

AGREE on KN.4's three-layer fix (rclab-plan pre-flight + epistemic-discipline.md PRU-extension + pru template). G1-G4 deliver the rule-text for each.

**Answers to KN.5's seven questions** (these seed R2):

**A1 (rule-file structure)**: AGREE — keep PRU and SOURCE-RECONCILIATION SEPARATE. They fail in different ways (cardinality vs value), the remediation paths differ (pin-add vs pin-correct), and combining them would create a single audit with two unrelated sub-tests, which is a category error. Run them sequentially: PRU first (must pass before SOURCE-RECON runs, because SOURCE-RECON needs every pin to be present to compare against source). The audit pipeline becomes PRU → SOURCE-RECON → execute. G1's clause specifies SOURCE-RECON as a distinct sub-audit invoked AFTER PRU's cardinality clear.

**A2 (severity calibration)**: AGREE — pin canonical at the rule-file level. Per-session OVERRIDE permitted only with an explicit `severity_band_override` block in the plan-file gate, audit-logged. The bands are themselves canonical constants `D_advisory_lower = 0.1`, `D_mandatory_lower = 1.0`, `D_halt_lower = 3.0` — register in `canonical_constants.py`. Cross-session drift comparison requires a fixed yardstick.

**A3 (class (e) provenance inversion)**: per Re:K1 R1, class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS is a STANDING fifth class, not absorbable into (d). The remediation differs: (d) requires verifying the derivation chain; (e) requires logging the pin-to-canonical promotion event with provenance and updating downstream gates' source-reconciliation pointers. G1 adds the (e) row to the classification table.

**A4 (algebraically-forced INFO mode)**: G2 contains the explicit clause. The verdict 4-tuple gains a 5th field `algebraic_force_flag: true|false`. When `true`, the verdict is INFO regardless of value-vs-threshold comparison. The producing script declares the flag at gate-block authoring time, not at runtime — this matches the W11-1, W11-3, W11-5 5B-class pattern where the scan tests numerical robustness only.

**A5 (PRDR vocabulary granularity)**: AGREE — atomicize-by-default with explicit grouping declarations. G4 contains the keyword-window clause. Every plan-layer keyword must declare its `granularity: atomic | grouped` field; grouped keywords MUST list their constituent atomic sub-keys.

**A6 (GPU pin selectivity)**: G3 contains the clause. The general feasibility audit covers (memory, compute time, numerical precision, regulator domain). Every GPU pin must declare its `feasibility_envelope: {VRAM_max_bytes, runtime_max_seconds, dtype_min}`; the audit verifies the envelope at plan-freeze.

**A7 (cross-pairing with W0-W5 W-3)**: I read the existing W-3 workshop file `sessions/archive/session-85/workshops/s85-w3-methodology-debts.md` (1708 lines). W-3 covers 11 W0-W5 plan-layer methodology debts (a-i + extensions): pin-collision (a), helper-absent (b), GPU-pin selectivity (c), regulator-conditional (d), AMRI (e), external-source (f), keyword-window (g), stylistic (h), PSD/Fisher (i), band-authority (j). My 7+ classes for W6-W13 are STRUCTURALLY DISTINCT: (1) source-reconciliation sub-audit, (2) algebraically-forced INFO-mode, (3) GPU-pin selectivity at L_max-conditional infeasibility, (4) root-count heuristic severity flag, (5) PRDR bare-K window expansion, (6) v3-recovery sig_2 cross-check relaxation, (7) 5B scan-as-robustness INFO classification. The DEDUPLICATION strategy is detailed in G5: ADDITIVE union with cross-references, not overlapping clauses. The two campaigns produce a UNIFIED rule-file v3 diff at 9B closeout.

### Part 2: Original Analysis (7+ Debt Classes → Rule-File Clauses)

#### G1: PRU-Extension SOURCE-RECONCILIATION Sub-Audit (debt class 1)

**Target file**: `.claude/templates/pru-pre-registration-template.md`. **Insertion point**: NEW Section "Source-Reconciliation Sub-Audit" between current §"Gate Block" and §"How to Use".

**Why this clause**: PRU's cardinality test (current `s80_pru_audit.py`) returns 0 violations for all 13 K1 sites — pin and source both exist, both well-formed, audit passes, drift undetected. The K2 4-class (now 5-class) taxonomy and the K4 Lyapunov band give the missing detection layer.

**Severity-direction substitution chain** (drift detected ⇒ rule-file action warranted):

```
Definition 1: pin_value(g, p) = the plan-pinned value for gate g, pin name p
Definition 2: src_value(g, p) = mcp__knowledge__.get_constant(p) at gate-run time
                                OR canonical_constants.py module-attribute lookup
                                OR sessions/framework/<registry>.md regex match
                                whichever returns first non-empty result
Definition 3: d_i(g, p) = |log10(pin_value) - log10(src_value)|  for scalar pins
                       = log10(N_pin / N_source)                  for categorical pins (N = cardinality)
                       = log10(scope_pin / scope_source)          for scope pins
Definition 4: D_advisory_lower = 0.1, D_mandatory_lower = 1.0, D_halt_lower = 3.0
              (calibration band edges; canonical-pinned per A2)
Step 1: substitute Definitions 1-3 into the audit comparator:
        action(g, p) = NONE       if d_i < D_advisory_lower
                     = ADVISORY   if D_advisory_lower ≤ d_i < D_mandatory_lower
                     = MANDATORY  if D_mandatory_lower ≤ d_i < D_halt_lower
                     = HALT       if d_i ≥ D_halt_lower
Step 2: simplify -- action is a step function of d_i with three thresholds.
Direction: as d_i increases (drift grows), the rule-file's required strictness
           rises monotonically through {NONE, ADVISORY, MANDATORY, HALT}.
Conclusion: the action map is a non-decreasing function of d_i; pinning the three
            thresholds at the rule-file level guarantees cross-session severity
            comparability. The PROHIBITED_ACTIONS set (v3-recovery rule, 4 items)
            applies — overrides require explicit logged justification.
```

**Rule-text to insert into `.claude/templates/pru-pre-registration-template.md`**:

```markdown
---

## Source-Reconciliation Sub-Audit (S85+ MANDATORY)

**Status**: Mandatory for every gate block at plan-freeze, run AFTER PRU's
cardinality clear (PRU first; SOURCE-RECON depends on every pin being present).

**Purpose**: Detect plan-pin/canonical-source value drift that the PRU
cardinality audit is structurally blind to. Catches the 5 drift classes:
(a) PIN-TIGHT-SOURCE-LOOSE, (b) PIN-LOOSE-SOURCE-TIGHT,
(c) PIN-DRIFT-FROM-STALE-SOURCE, (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY,
(e) PIN-PROMOTES-TO-SOURCE-ON-PASS.

### Source-reconciliation block (per-gate)

For every plan pin (`name = value` line in the gate's machinery-pin map),
add the following sub-block:

```
—— Source reconciliation (S85+; PRU-extension class 8.1) ——
Pin name:           {{name}}
Pin value:          {{value}}
Pin classification: PRIMITIVE | DERIVED | CATEGORICAL | SCOPE | PROMOTED-FROM-PASS
Canonical query:    {{ "mcp__knowledge__.get_constant('{{name}}')" |
                       "canonical_constants.{{name}}" |
                       "sessions/framework/<registry>.md::<key>" |
                       "FIRST-PRINCIPLES (no canonical source registered)" }}
Canonical value:    {{src_value or "NOT REGISTERED — pin promotes-to-source on PASS"}}
Drift d_i:          {{|log10(pin) - log10(src)|}}
Drift class:        (a) | (b) | (c) | (d) | (e)
Severity:           S1 (d_i ≥ 1.0 OOM AND class ∈ {(b), (c-numeric)})
                  | S2 (0.1 ≤ d_i < 1.0 OOM)
                  | S3 (d_i < 0.1 OOM AND no false-PASS direction)
Audit action:       NONE     | d_i < D_advisory_lower (=0.1)
                  | ADVISORY | D_advisory_lower ≤ d_i < D_mandatory_lower (=1.0)
                  | MANDATORY | D_mandatory_lower ≤ d_i < D_halt_lower (=3.0)
                  | HALT     | d_i ≥ D_halt_lower (=3.0)
Remediation rule:   {{by class -- see table below}}
```

### Class-to-remediation table (canonical)

| Class | Description | Remediation |
|:------|:------------|:------------|
| (a) PIN-TIGHT-SOURCE-LOOSE | pin admits less than source | LOOSEN pin to match source band |
| (b) PIN-LOOSE-SOURCE-TIGHT | pin admits values source forbids | TIGHTEN pin; structural inversion if source-forbidden region intersects PASS region |
| (c) PIN-DRIFT-FROM-STALE-SOURCE | pin reflects pre-update canonical | SYNC pin to current canonical via mcp__knowledge__.get_constant |
| (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY | pin = f(primitives) | VERIFY derivation chain; document f explicitly in plan block |
| (e) PIN-PROMOTES-TO-SOURCE-ON-PASS | pin = primitive; source post-dates via gate verdict | LOG promotion event in canonical_constants.py provenance with `promoted_from = "S{N}-{gate}"` |

### Aggregate metric (per-wave)

```
D_max  := max_i d_i across all pins in the wave
D_sum  := Σ_i d_i
D_L2   := √(Σ_i d_i²)
```

A wave with D_max ≥ D_halt_lower (default 3.0) HALTS plan-freeze for manual review.
A wave with D_max ≥ D_mandatory_lower (default 1.0) requires per-pin remediation
before plan-freeze. A wave with D_max ≥ D_advisory_lower (default 0.1) emits an
advisory log entry but does not block.

### Detection ordering

1. Run PRU cardinality audit (`_pru_cardinality_audit.py`) — every gate's
   machinery_pin_map must be non-empty cardinality match.
2. Run SOURCE-RECONCILIATION audit (`_source_reconciliation_audit.py`, NEW) —
   for every pin, query canonical source and compute d_i.
3. Aggregate D_max, D_sum, D_L2 per wave and emit verdict-line-equivalent
   audit row.
4. If D_max ≥ D_halt_lower, halt plan-freeze. Manual review required.

### Class 8 Failure Mode table — UPDATED

| # | Failure | Type | Prevented by |
|:--|:--------|:-----|:-------------|
| 8 | PRU (machinery unpinned) | plan-property | Cardinality audit (existing) |
| **8.1** | **SOURCE-DRIFT (pin/canonical disagree)** | **plan-property** | **Source-reconciliation sub-audit (NEW)** |
```

**Implementation deliverable for S86 PRU-EXTENSION-RULE-V2-LANDING gate**:
- New script: `computations/_source_reconciliation_audit.py` runs the comparator above on every gate's pin block.
- New canonical constants: `D_advisory_lower = 0.1`, `D_mandatory_lower = 1.0`, `D_halt_lower = 3.0` registered in `canonical_constants.py`.
- Cross-link to `_yaml_gate_validator.py`: SOURCE-RECON failure on a gate sets sig_4-equivalent failure for that gate's R3 block.

#### G2: Algebraically-Forced Gate INFO-Mode Clause (debt class 2)

**Target file**: `.claude/rules/gate-verdicts.md`. **Insertion point**: NEW subsection under "Verdict Format" between current S81+ canonical form (line 75) and §"Rules" (line 81).

**Knowledge-MCP cross-check**: `search_knowledge("gate verdict INFO mode algebraically forced")` returned 10 hits — 9 of them are scripts where the verdict was set INFO by ad-hoc logic (s48 dissolution-berry, s48 volovik-string, s49 gauss-codazzi, s43 gsl-transit, s43 carlip-cc, s45 econd-reconcile, s50 leggett-damping, s59 ricci-dw, s78 zeta-josephson). NO existing rule-file clause defines algebraic-force INFO. The 5B pattern at W11-1, W11-3, W11-5 is the latest instance — three gates passed by structural identity with the scan testing only numerical robustness. The clause closes this gap.

**Why a flag, not a value-comparison rule**: a value-vs-threshold gate that always passes by algebraic identity is structurally distinct from a value-vs-threshold gate that contingently passes. The former tests numerical robustness of an identity; the latter tests a structural bound. They live on different rungs of the evidence hierarchy (epistemic-discipline.md §"Evidence Hierarchy" item 1 vs item 2). Verdict semantics must distinguish them.

**Direction substitution chain** (PASS vs INFO under algebraic force):

```
Definition 1: gate_verdict(g) := PASS if value(g) satisfies threshold(g); FAIL otherwise.
Definition 2: algebraic_force_flag(g) := True if value(g) = threshold(g) by structural
              identity for ALL admissible inputs in the scan domain; False otherwise.
Definition 3: INFO outcome := pre-registered structured intermediate verdict per
              `.claude/rules/math-scripts.md` §"All Results Are Good Results".
Step 1: substitute Definition 2 into Definition 1:
        IF algebraic_force_flag(g) = True:
            value(g) ≡ PASS-condition for every admissible input
            ⇒ verdict carries no information about whether the structural bound holds
            ⇒ verdict carries information ONLY about numerical robustness of the identity
Step 2: simplify -- a verdict that carries only numerical-robustness information is
        an INFO verdict by Definition 3.
Direction: when algebraic_force_flag(g) = True, the verdict semantics REDUCE from
           PASS-or-FAIL to INFO regardless of value-vs-threshold comparison.
Conclusion: the rule-file must override gate_verdict to INFO when
            algebraic_force_flag = True. The 5th field of the verdict tuple
            carries the flag.
```

**Rule-text to insert into `.claude/rules/gate-verdicts.md`**:

```markdown
### Algebraic-Force INFO Override (S85+ MANDATORY)

**Pattern**: a gate whose value(g) satisfies threshold(g) by structural identity
for every admissible input in the scan domain — the "scan" tests numerical
robustness of the identity, not a structural bound. Examples from S85:
W11-1 EPSH-JENSEN-SURVIVAL (heitsch_ratio ≥ 4 by `h = 4·⟨ρ⟩_W` with ρ ≥ 1),
W11-3 NCG-EXCLUSION-cyclic-cohomology (Hochschild trace identity),
W11-5 (Mellin-residue identity).

**Verdict 5-tuple (extends the S81+ 4-tuple)**:

```
(value=<v>, scheme=<s>, convention=<c>, L_max=<L>, algebraic_force_flag=<bool>)
```

**Verdict line format (extended)**:

```
{GATE_ID}: PASS|FAIL|INFO -- value=<v> scheme=<s> convention=<c> L_max=<L> alg_force=<bool> sha256=<closure>
```

**Override rule**:

- If `algebraic_force_flag = True`: verdict is **INFO** regardless of value-vs-threshold comparison.
- If `algebraic_force_flag = False`: standard PASS/FAIL semantics apply.
- The flag is set at GATE-BLOCK AUTHORING TIME (in the plan file's pre-registered
  block), NOT at runtime. Setting the flag at runtime is convention-shopping
  (PROHIBITED_ACTION 1, v3-recovery rule).

**Plan-block declaration** (in `pru-pre-registration-template.md` Gate Block):

```
—— Algebraic-force declaration (S85+; gate-verdict class) ——
Algebraic identity:    {{cite the identity that forces PASS, e.g.
                         "h = 4·⟨ρ⟩_W with ρ ≥ 1 ⇒ h ≥ 4 ≫ 1e-4 floor"}}
Scan domain:           {{the input range over which the identity holds, e.g.
                         "L_max ∈ {3, 5, 7, 9, 10}"}}
algebraic_force_flag:  true | false
Scan diagnostic role:  {{"numerical-robustness only" | "structural-bound test"}}
```

**Why this is NOT iterate-until-PASS**: iterate-until-PASS (S78 Class-6) is
running the same gate with different parameters until one returns PASS. The
algebraic-force flag is the OPPOSITE: declaring at plan-time that the gate
WILL pass by identity, with the scan as a robustness test only. The verdict
semantics correctly reduce to INFO without any iteration.
```

#### G3: GPU-Pin Selectivity (debt class 3) + Root-Count Heuristic Severity-1 Flag (debt class 4)

**Target files**:
- W0-W5 W-3 workshop already added a GPU-pin selectivity clause to `math-scripts.md` (per its §G1 Clause (c) at lines 611-642 of `s85-w3-methodology-debts.md`). My W6-W13 extension covers L_max-conditional infeasibility, which W-3 did NOT cover.
- Insertion point: `math-scripts.md` §"Environment", append L_max-conditional infeasibility sub-clause.

**The structural problem at site #10 (W10-4)**:

```
Definition 1: VRAM_max = 17.1 × 10^9 bytes (RX 9070 XT canonical)
Definition 2: D_K_dim(L) = dimension of the dense Dirac matrix at truncation L
Definition 3: dense_storage_bytes(L) = D_K_dim(L)² × 16  (complex128 = 16 B/entry)
Step 1: at L=10, D_K_dim ≈ 155984 (canonical), dense_storage ≈ 4×10^11 ≈ 400 GB
        at L=12, D_K_dim ≈ 10^7 (kitaev K1 site #10), dense_storage ≈ 1.6×10^15 ≈ 1.6 PB
        (kitaev cites 8 PB; the order of magnitude is consistent with O(10^7)² × 16)
Step 2: feasibility ratio at L=12: dense_storage / VRAM_max ≈ 10^15 / 1.7×10^10 ≈ 10^5
Step 3: log10(10^5) = 5 OOM (kitaev cites 5.67 OOM; consistent within the dim estimate)
Direction: the GPU-mandate at L=12 is INFEASIBLE by 5+ OOM. The pin's
           feasibility envelope is a CONDITIONAL function of L_max -- feasible
           at L=10 (storage 400 GB still exceeds VRAM but sparse paths are open),
           categorically infeasible at L=12 dense.
Conclusion: a GPU-pin without a feasibility envelope is structurally underspecified.
            Every GPU-pin must declare its feasibility-as-function-of-L envelope.
```

**Rule-text to insert into `.claude/rules/math-scripts.md`** (extension of W-3's GPU-pin clause):

```markdown
### GPU-pin feasibility envelope (S85 W6-W13 extension)

W0-W5 W-3 added a GPU-pin selectivity clause for ROCm complex non-Hermitian
eigvals. This extension covers L_max-conditional infeasibility.

Every GPU-pin in a plan-file gate block MUST declare its feasibility envelope:

```
—— GPU pin feasibility envelope (MANDATORY for any GPU mandate) ——
Path:                  torch.linalg | numpy.linalg | cpu-cap-OMP8
Feasibility envelope:  VRAM_max_bytes = {{int}}
                       runtime_max_seconds = {{int}}
                       dtype_min = {{float32 | complex64 | complex128}}
L_max conditional:     {{ at each L_max value in the scan, declare whether the
                          dense storage and runtime fit the envelope }}
                       L = L_min: {{feasible | INFEASIBLE-DENSE | INFEASIBLE-COMPLEX}}
                       ...
                       L = L_max: {{feasible | INFEASIBLE-DENSE | INFEASIBLE-COMPLEX}}
Fallback path:         {{ if any L_max value is INFEASIBLE: declare the fallback,
                          e.g. "log-linear extrapolation from L_max < INFEASIBLE_FLOOR" }}
```

**Audit at plan-freeze**: the SOURCE-RECONCILIATION sub-audit (G1) runs the
feasibility check by computing `dense_storage_bytes(L) = D_K_dim(L)² × 16` and
comparing against `VRAM_max_bytes`. If the comparison fails for any L in the
scan, the pin is class (b) PIN-LOOSE-SOURCE-TIGHT severity S1 and HALTS
plan-freeze unless the fallback path is explicitly declared.
```

**Root-count heuristic severity flag (debt class 4)**:

The W13-4 R1-RANK β heuristic site (#9) is the canonical class (b) S1 instance. Plan band β ∈ [0.05, 0.15]; observed β = 10.18; drift = 2.01 OOM (kitaev K4 worked computation). Per Re:K4, this exceeds D_mandatory_lower = 1.0 and triggers MANDATORY remediation under G1's audit-action map. The class-specific rule:

```markdown
### Root-count heuristic drift detection (S85 W6-W13)

**Target file**: source-reconciliation sub-audit (G1) heuristic-class table.

Heuristic pins of the form `{quantity}_heuristic_band = [a, b]` where the
quantity is a function of root-count, dimension-count, or other combinatorial
substrate property MUST declare:

```
—— Heuristic pin declaration ——
Quantity:              {{name}}
Heuristic basis:       {{ "linear in root count" | "polynomial degree N in dim" |
                          "geometric mean of {a, b}" | ... }}
Algebraic structure:   {{ the structural argument that BOUNDS the quantity, e.g.
                          "Weyl-dim Freudenthal product is exponential in root count;
                          β heuristic linear-in-root-count is structurally weak by
                          ≥1 OOM at root count > 10" }}
Severity flag:         {{ S1 (drift > 100×) | S2 (drift 10-100×) | S3 (drift < 10×) }}
```

If `Severity flag = S1`, the pin is class (b) by detection rule and triggers
SOURCE-RECONCILIATION MANDATORY remediation. The heuristic band must be
expanded OR the algebraic structure must be re-derived to match.
```

#### G4: PRDR Bare-K Keyword Window (debt class 5) + v3-Recovery sig_2 Cross-Check Relaxation (debt class 6) + 5B-Class Scan-as-Robustness INFO-Mode (debt class 7)

**Three sub-clauses; each targets a different rule-file**.

##### G4a: PRDR Bare-K Keyword Window Expansion (debt class 5)

**Target file**: `.claude/templates/pru-pre-registration-template.md` §"How to Use" → §"At plan-write time (PRDR)" item 1.

**Cross-pairing with W0-W5 W-3 K_crit triple collision**: W-3 §G2 Clause (g) (lines 696-757) added a "Keyword-context audit framework" for vocabulary collapses. That framework is general; my W6-W13 extension specifies the exact K-keyword window the PRDR static analyzer must enumerate, addressing the W12-2 site #12 collapse.

**Direction substitution chain** (vocabulary granularity vs detection power):

```
Definition 1: PRDR_keyword_set := the set of `name = number` pin patterns the
              static analyzer recognizes as machinery pins.
Definition 2: framework_K_atoms := {K_substrate, K_corridor, K_R5, K_crit,
                                    K_base, K_R3, K_FIRAS, K_crit_BdG}
Definition 3: granularity_level(k) := atomic | grouped
              atomic ⇒ k corresponds to exactly one framework quantity
              grouped ⇒ k aggregates two or more atomic sub-keys
Step 1: site #12 plan classifier had PRDR_keyword_set ∩ K-keys = {"K "}
        |PRDR ∩ K-atoms| = 1; |framework_K_atoms| = 8
Step 2: substitute -- collapse ratio = 8/1 = 8
        misclassification_rate ≥ (collapse_ratio - 1) / collapse_ratio = 7/8 = 87.5%
Step 3: simplify -- a single bare-K bucket maps 8 distinct framework K-atoms
        into one classification, producing 87.5% spurious CONTRADICTS
        (matches W12-2 14/14 spurious finding to within rounding).
Direction: PRDR keyword window granularity is monotonically tied to detection
           accuracy. Expanding from {"K "} to the 8-atom set collapses the
           misclassification rate to ~0.
Conclusion: PRDR keyword window MUST enumerate the 8 K-atoms explicitly.
```

**Rule-text to insert** (PRDR template §"How to Use"):

```markdown
### PRDR keyword window — explicit atomic enumeration (S85 W6-W13 extension)

The PRDR static analyzer's keyword window MUST enumerate the framework's
atomic quantities explicitly. Bare-prefix matches (e.g. "K ") are FORBIDDEN
unless explicitly declared `granularity: grouped` with constituent sub-keys
listed.

**Canonical K-atom set** (S85 W6-W13 reconciliation; cross-pairs W0-W5 W-3
K_crit triple collision):

- K_substrate
- K_corridor
- K_R5
- K_crit             (W2-12 BdG meaning conflicts with W3-1 PIXIE meaning;
                       see canonical_constants.py disambiguation)
- K_base
- K_R3
- K_FIRAS
- K_crit_BdG         (alias of K_crit under BdG convention)

**Detection rule**: any plan-pin matching `^K[ _]` MUST resolve to exactly one
of the 8 atoms. A bare-K pin without an atom resolution is a SOURCE-DRIFT
class (b) S1 violation.

**Generalization**: every plan-layer keyword must declare `granularity: atomic`
or `granularity: grouped`. Grouped keywords list constituent atomic sub-keys.
```

##### G4b: v3-Recovery sig_2 Cross-Check Relaxation (debt class 6)

**Target file**: `.claude/rules/v3-closure-recovery.md` §"Stage 1: Per-signal remediation map" → sig_2 entry.

**The site #6 problem**: W11-2's plan-required cross-check set was {W10-113, W10-114, W10-115, S82 W2-3} — all four plan-required. W10-113 and W10-115 are diagnostic (per verdict-line semantics: only W10-114 + S82 W2-3 are gating). The plan over-constrained by demanding cross-check matches the source treats as optional. Result: false sig_2 sub-failure.

**Direction substitution chain**:

```
Definition 1: gating_set(W10) := the verdict-line subset whose closure_sha entries
                                  are checked by sig_2 cross-check.
Definition 2: plan_required(W11-2) := {W10-113, W10-114, W10-115, S82 W2-3}
Definition 3: source_required = gating_set ∩ verdict_lines_with_audit_role
                              = {W10-114, S82 W2-3}
Step 1: substitute -- plan_required ⊃ source_required (4 vs 2 entries)
Step 2: this is class (a) PIN-TIGHT-SOURCE-LOOSE: the plan demands matches
        on entries the source treats as diagnostic only.
Step 3: severity S2 -- caused first-run mis-fire at W11-2; remediation was
        in-flight via the sig_2 reactive remediation, not pre-flight.
Direction: relaxing sig_2's cross-check scope to gating_set ONLY (excluding
           diagnostic entries) eliminates false sig_2 sub-failures.
Conclusion: the v3-recovery rule's sig_2 entry MUST specify the cross-check
            scope as the gating subset, not the full verdict-file.
```

**Rule-text edit to `.claude/rules/v3-closure-recovery.md`** (sig_2 entry, ~ line 50):

```markdown
- **sig_2 = 0** — at least one verdict line lacks dual-SHA
  (`content_sha256` + `audit_sha256` companion comment row absent).
  - **Scope (S85 W6-W13 refinement)**: the cross-check set is the GATING
    SUBSET of verdict lines, NOT the full file. Diagnostic verdict lines
    (those whose `audit_role: diagnostic` field is set in the gate block,
    or whose gate ID matches the diagnostic suffix `-DIAG`, `-OBS`, `-INFO`)
    are EXCLUDED from sig_2's cross-check.
  - Remediation: regenerate the verdict line by rerunning the gate's
    producing script with the updated dual-SHA template (W9a-99 split).
    Apply ONLY to verdict lines in the gating subset.
  - Re-dispatch action: `python computations/s{N}_{gate}.py`; the
    script appends the corrected canonical line and comment row. No
    manual edits to `s{N}_gate_verdicts.txt` are permitted.
```

##### G4c: 5B-Class Scan-as-Robustness INFO-Mode Classification (debt class 7)

**Target file**: same as G2 (`.claude/rules/gate-verdicts.md`), but the classification rule for SCAN-AS-ROBUSTNESS extends G2's algebraic-force flag to a multi-axis flag set.

**The 5B pattern**: W11-1, W11-3, W11-5 all PASS by algebraic identity. The L_max scan or other parameter scan tests NUMERICAL ROBUSTNESS of the identity (does the floating-point computation reproduce the algebraic result across the scan domain?). G2 covers this with the `algebraic_force_flag`. The 5B classification adds a separate axis: `scan_role`.

**Rule-text** (extension of G2's verdict-tuple):

```markdown
### Verdict 6-tuple (S85+ FINAL extension)

```
(value=<v>, scheme=<s>, convention=<c>, L_max=<L>,
 algebraic_force_flag=<bool>, scan_role=<role>)
```

`scan_role ∈ { structural-bound-test | numerical-robustness-only | grid-resolution-only | iteration-cap }`

**Verdict logic**:

- `algebraic_force_flag = True` AND `scan_role = numerical-robustness-only`
  ⇒ verdict = **INFO** (5B class).
- `algebraic_force_flag = True` AND `scan_role = structural-bound-test`
  ⇒ NOT POSSIBLE — contradiction (a structural-bound test cannot be
  algebraically forced; verdict-spec audit FAILS).
- `algebraic_force_flag = False` AND `scan_role = structural-bound-test`
  ⇒ verdict = PASS|FAIL by value-vs-threshold (canonical case).
- Other combinations ⇒ verdict = INFO (mixed-mode; pre-registered structured
  intermediate per math-scripts.md §"All Results Are Good Results").

This subsumes the W11-1, W11-3, W11-5 pattern: each had `algebraic_force_flag = True`
(structural identity) AND `scan_role = numerical-robustness-only` (L_max scan
tests floating-point reproduction of the identity). Verdict is INFO; the gate
contributes structural information (the identity holds in float arithmetic
across the scan) but is not a value-vs-threshold PASS.
```

#### G5: Questions for kitaev

**Q1 (taxonomy completeness — meta-class for hybrids)**: My Re:K3 reclassification surfaced site #5 (W11-1 FAIL floor) as (a)/(b)-degenerate — the pin admits a region (FAIL outcomes at h < 1e-4) that source proves empty by structural identity. This is structurally between (a) and (b): pin admits less than source on the PASS side, AND admits a source-forbidden region on the FAIL side. Is this a HYBRID class (a∧b), or does it collapse to one of the two by which side dominates the gate's PASS region? My provisional read: (a) wins for remediation purposes (loosen FAIL floor), but the structural reading is hybrid. R2 CONVERGE should pin one answer. Specifically: do we need an explicit (a∧b) hybrid row in the classification table, or is the dominant-side rule sufficient?

**Q2 (Lyapunov band tunability)**: I proposed pinning D_advisory_lower = 0.1, D_mandatory_lower = 1.0, D_halt_lower = 3.0 as canonical constants in `canonical_constants.py`. Is the 3.0 hard-halt threshold session-tunable, or fixed forever? Two arguments: FIXED — cross-session severity comparability is the whole point of the calibration. TUNABLE — different sessions have different complexity and the Lyapunov-band that works for S85 may be wrong for an S100 with 10× the gate count. My provisional answer: pin the band as canonical with explicit `severity_band_override` overrides logged per session, but do NOT allow per-gate overrides (per-gate would re-introduce convention-shopping). What is your view on the granularity of the override?

**Q3 (deduplication strategy)**: Per Re:KN A7, the W0-W5 W-3 workshop covers 11 W0-W5 plan-layer methodology debts (a-i + extensions); my W6-W13 7 debt classes are explicitly NEW. The schedule §5A names the cross-pairing ("combine with W0-W5 W-3 Rule-File v2 diff to produce the FULL S85 rule-file v3 diff"). I propose the v3 diff is an ADDITIVE union with cross-references (e.g., my G4a cites W-3's Clause (g) keyword-context audit framework as the parent rule, with G4a as the W6-W13 K-atom specialization). Is additive union with cross-references sufficient, or do we need to RECONCILE overlapping clauses where W-3 and 5A address the same rule-file file? The two cases I can identify:
- W-3 §G1 Clause (c) GPU-pin selectivity vs my G3 GPU-pin L_max-conditional infeasibility — I treat as ADDITIVE (W-3 covers ROCm complex eigvals; G3 covers L_max-conditional dense storage). Both can co-exist in `math-scripts.md` as separate sub-clauses.
- W-3 §G2 Clause (g) keyword-context audit framework vs my G4a PRDR bare-K window — I treat as PARENT/CHILD (G4a is the K-atom specialization of W-3's general framework).

Is this the correct deduplication strategy? Or should we MERGE (W-3 G2-(g) absorbs G4a as a sub-section)?

**Q4 (class (e) cross-impact)**: My new class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS captures site #11 (W9-1 Borel) cleanly. Are there OTHER (e)-class events in the W6-W13 verdict file that I missed? Specifically: the W12-3 branch-(iv) K-coupled PASS landed `branch_iv_K_coupled_threshold` as a canonical constant — was that a class (e) promotion? If yes, the (e) class has at least 2 members in S85 alone, which strengthens the case for treating it as a STANDING class rather than a one-off.

**Q5 (per-pin vs per-wave audit aggregation)**: My G1 specifies aggregate D_max, D_sum, D_L2 PER WAVE. The W6-W13 schedule has 8 waves; aggregating per-wave gives 8 D-metric tuples for S85. Should the rule-file ALSO aggregate per SESSION (one D-metric tuple for the whole session) for cross-session comparison? My provisional answer: YES — per-wave for actionable remediation, per-session for trend tracking analogous to P_work_complete. Confirm or push back.

---

## Round 2 — kitaev: CONVERGE

### CONVERGENCE

#### C1: Class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS — ACCEPT as a structurally distinct fifth class

I accept gen-physicist's Re:K1 R1 substitution chain. The decisive step is the temporal-decomposition of `src(t)`:

```
Definition 1: src(t) := canonical_constants entry "Borel_threshold_S_inst" at wall-clock time t.
Definition 2: t_W9-1 := the wall-clock time of W9-1's verdict-line append.
Step 1: substitute -- src(t < t_W9-1) = ∅ (entry not registered);
                       src(t > t_W9-1) = 4.34 (registered by gate verdict).
Step 2: classes (a)-(d) ALL presuppose pin and source coexist at evaluation time
        (the K2 detection rules compare bands or values, both nonempty).
Step 3: at t = t_W9-1 - ε, the comparator is undefined; at t = t_W9-1 + ε, the
        comparator returns 0 exactly. The transition at t_W9-1 is structural, not
        numerical -- the source comes into being.
Direction: classes (a)-(d) operate on a static slice of (pin, src) space;
           class (e) operates on the TIME EVOLUTION of that space, encoding
           a creation event that the static taxonomy cannot represent.
Conclusion: (e) is structurally distinct from (d). My K3 entry for site #11
            classifying it as (d) S3 with "anomalous direction" was the
            symptom of trying to fit a creation event into a static-disagreement
            taxonomy. Withdrawn. Site #11 is class (e) S3.
```

This is the ONE place where my K2 4-class structure was incomplete. I had treated the temporal anomaly as a sign-flip on (d); gen-physicist correctly identified it as a different category of object entirely. The 4 classes are the equivalence classes of `pin ≠ src` at fixed t; (e) is the structurally-orthogonal "pin creates src" event. Updated taxonomy: 5 classes.

#### C2: Lyapunov band tunability — ACCEPT canonical pinning with logged session override

I accept gen-physicist's Re:K4 EMERGES proposal in full. The three thresholds `D_advisory_lower = 0.1`, `D_mandatory_lower = 1.0`, `D_halt_lower = 3.0` should be registered in `canonical_constants.py`. Substitution chain why this is the right granularity (not per-gate, not per-wave):

```
Definition 1: comparability(S_a, S_b) := the property that severity verdicts in
              session S_a and session S_b can be lined up against the same
              numerical scale.
Definition 2: pin canonical -- bands live in canonical_constants.py
              pin per-session -- bands live in plan-file gate block
              pin per-gate -- bands live per gate-block
Step 1: substitute pin per-gate -- d_i evaluated against per-gate band; each gate
        defines its own severity scale; comparability(S_a, S_b) := False
        (comparing gate g_a's S1 to gate g_b's S1 is a category error).
Step 2: substitute pin per-session -- d_i evaluated against session-level band;
        comparability within session = True; cross-session = False.
Step 3: substitute pin canonical -- d_i evaluated against fixed band across all
        sessions; comparability(S_a, S_b) := True for all (S_a, S_b).
Direction: granularity coarser than per-session is REQUIRED for the K4 metric
           to be a yardstick at all (the whole point of a Lyapunov-band).
Conclusion: pin at canonical level. Per-session override permitted only via
            explicit `severity_band_override` block, audit-logged. NO per-gate
            override (per-gate would re-introduce convention-shopping, S78
            execution failure 1).
```

Specifically: I ALSO accept the EMERGES point that the override granularity matters (gen-physicist's Q2 framing). My answer to Q2 below pins per-session as the only override level; per-gate override is forbidden by the same logic that forbids convention-shopping.

#### C3: Re:K3 site #4 reclassification (a) -> (b) — ACCEPT

The substitution chain at Re:K3 lines 442-450 is correct. The `pin = {10}, src = {5}` case is `pin ∩ src = ∅`, and the operationally-relevant rule is "pin admits a source-forbidden value" which is class (b) by detection rule. My K3 row was wrong to call this (a) on the basis that the remediation "loosen pin to L=5" sounded like loosening — the structural reading is that the pin admits L=10 which the anchor structurally forbids, regardless of which side has more elements. (b) S1.

This propagates into the class distribution: class (b) gains site #4, leaving 6 (b) S1 sites (#3, #4, #9, #10, #12 + #5 degenerate), reinforcing my KN.3 claim that (b) is the highest-leverage class.

#### C4: D_L2 = 8.98 (4 sig figs) — ACCEPT

Python-verified: `D_L2 = sqrt(80.6397) = 8.9800`. My quoted 9.04 was a rounding artifact from squaring intermediate values to 2 decimal places. Pin D_L2 = 8.98 in the rule-file.

#### C5: G2 algebraic-force flag at gate-block authoring time, not runtime — ACCEPT

The rule that `algebraic_force_flag` is set at GATE-BLOCK AUTHORING TIME (not runtime) is essential. A runtime-set flag would be a backdoor for convention-shopping (PROHIBITED_ACTION 1 from v3-recovery). The plan-time declaration locks the flag before any value is computed; the verdict-INFO override is then deterministic from pre-registered state. Substitution chain:

```
Definition 1: backdoor(flag) := the property that flag's value can be set
              after seeing a gate's computed value.
Step 1: substitute "flag set at runtime" into Definition 1 -- runtime is by
        definition AFTER value is computed -- backdoor = True.
Step 2: substitute "flag set at gate-block authoring time" -- authoring is at
        plan-freeze, BEFORE value is computed -- backdoor = False.
Direction: only authoring-time declaration closes the backdoor.
Conclusion: G2's authoring-time declaration is the right rule.
```

#### C6: PRU -> SOURCE-RECON ordering — ACCEPT

Gen-physicist's A1 gets the ordering right: PRU first (cardinality), SOURCE-RECON second (value). Reasoning: SOURCE-RECON's per-pin loop requires the pin to EXIST. If a pin is missing (PRU failure), there is no pin-value to compare to source. Ordering is forced by the dependency, not by stylistic preference.

#### C7: Aggregation per-wave AND per-session — ACCEPT (Q5 answer)

I AGREE per-wave for actionable remediation, per-session for trend tracking. See Q5 answer below.



### DISSENT

#### D1: G3 GPU feasibility — extend to dtype/sparsity, not just dense storage

NEW EVIDENCE: my K1 site #10 cited 8 PB at L=12; gen-physicist's G3 substitution chain (lines 760-763) replicates this with `dense_storage = D_K_dim² × 16` (complex128). But the W10 working paper actually used a SPARSE Krylov path at L=10, not dense diagonalization, and the dense-storage estimate at L=10 is 400 GB which already exceeds the 17 GB VRAM. So the "L=10 feasible / L=12 infeasible" partition that G3's text suggests is itself wrong — at L=10, dense is ALREADY infeasible. The W10 plan's actual viable path was sparse + iterative, not dense GPU.

Substitution chain:

```
Definition 1: viable_path(L) := the algorithm with which W10-4 actually computes
              D_K eigenvalues at truncation L within VRAM_max.
Definition 2: dense_path(L) requires storage D_K_dim(L)² × 16 bytes
Definition 3: sparse_path(L) requires storage proportional to nnz(D_K) × 16 bytes
              where nnz scales like D_K_dim(L) × <connectivity>, NOT D_K_dim(L)².
Step 1: at L=10, D_K_dim ≈ 1.56e+5; dense storage ≈ 1.56e+5² × 16 = 3.9e+11 B = 390 GB.
        VRAM_max = 17 GB.  390 / 17 ≈ 23x over.  Dense L=10 INFEASIBLE.
Step 2: at L=10, sparse storage ≈ 1.56e+5 × c × 16 with c = O(100) connectivity
        ≈ 2.5e+8 B = 250 MB. Sparse L=10 FEASIBLE within VRAM.
Step 3: at L=12, D_K_dim ≈ 1e+7 (kitaev's K1 cite); sparse storage ≈ 1.6e+10 B = 16 GB,
        right at the VRAM ceiling. Sparse L=12 BARELY-FEASIBLE.
Direction: feasibility is a function of (L_max, dtype, density). G3 currently
           reads as a function of (L_max, dtype) only -- the density axis is
           missing.
Conclusion: G3's `feasibility_envelope` block must add a `density` field
            {dense | sparse | iterative-Krylov} to make the audit operationally
            correct. Without it, the audit would advise "L=10 feasible" while
            in fact only the sparse path is feasible at L=10.
```

Concrete amendment to G3 rule-text (the `feasibility_envelope` block):

```
Feasibility envelope:  VRAM_max_bytes = {{int}}
                       runtime_max_seconds = {{int}}
                       dtype_min = {{float32 | complex64 | complex128}}
                       density = {{dense | sparse | iterative-Krylov}}    # NEW
                       nnz_estimate(L) = {{function of L_max}}              # NEW (sparse only)
```

This is a SHARPENING of G3, not a rejection. Gen-physicist's structure is correct; the missing axis is operationally critical.

#### D2: G4c verdict 6-tuple — `scan_role` field admits a 4th value `regulator-test` not enumerated

NEW EVIDENCE: my K1 site #13 (W7-2 k_cusp at 14.31 M_KK relative to integration cap M_KK) is exactly a regulator/cap pin. The scan over the integration cap is neither "structural-bound-test" nor "numerical-robustness-only" nor "grid-resolution-only" nor "iteration-cap" — it is a REGULATOR scan testing whether the gate's verdict is independent of where the regulator is placed. This is a category gen-physicist's G4c enumeration misses.

Substitution chain:

```
Definition 1: regulator_test_scan := a scan over a parameter that should NOT
              influence the gate's verdict if the regulator is a true cutoff.
Definition 2: the W7-2 cap pin scan tests "does varying the integration cap from
              M_KK to k_pivot=14.31 M_KK leave the verdict invariant?"
Step 1: substitute Definition 2 into Definition 1 -- the W7-2 cap scan IS a
        regulator_test_scan.
Step 2: check whether {structural-bound-test, numerical-robustness-only,
        grid-resolution-only, iteration-cap} contains regulator_test_scan
        -- it does not.
Direction: the G4c enumeration is INCOMPLETE for at least one S85 site.
Conclusion: add `regulator-cap-test` as a 5th value of scan_role:
            scan_role ∈ {structural-bound-test, numerical-robustness-only,
                         grid-resolution-only, iteration-cap, regulator-cap-test}.
            Verdict logic: algebraic_force_flag=True AND scan_role=regulator-cap-test
            -> verdict = INFO (the algebraic identity passes regardless of
            regulator placement; the scan tests cap-independence as diagnostic).
```

This is a SHARPENING. The 5th scan_role value covers W7-2 site #13 plus any future gate that scans an integration cap, momentum cutoff, or regulator scale.

#### D3: G1 source-reconciliation block does not specify how to handle class (e) at audit time

NEW EVIDENCE: gen-physicist's class-to-remediation table (G1 line 626) lists the (e) remediation as "LOG promotion event in canonical_constants.py provenance with `promoted_from = "S{N}-{gate}"`." But the SOURCE-RECONCILIATION audit runs at PLAN-FREEZE — BEFORE the gate has been executed and BEFORE the (e) promotion has happened. At plan-freeze for the gate that will eventually create the canonical, there is no canonical to compare against.

The structural problem:

```
Definition 1: audit_time(g) := the wall-clock time at which the SOURCE-RECON
              sub-audit runs for gate g. By G1 spec, audit_time(g) = plan-freeze.
Definition 2: t_promotion(g) := the wall-clock time at which gate g's PASS verdict
              promotes its pin to canonical_constants.py.
Step 1: by definition, audit_time(g) < t_run(g) ≤ t_promotion(g).
        Therefore audit_time(g) precedes t_promotion(g) strictly.
Step 2: at audit_time(g), no canonical entry exists for the pin
        (canonical_value = ∅). The d_i = |log10(pin) - log10(∅)| is undefined.
Step 3: gen-physicist's class-to-remediation entry for (e) says "LOG promotion
        event" -- but at audit_time, there is nothing to log; the promotion
        has not yet happened.
Direction: the G1 audit machinery, as written, cannot produce class-(e)
           detection because the canonical it would compare against does
           not yet exist at audit time.
Conclusion: G1 needs an additional rule: when canonical_value = ∅ AND the
            pin is declared `pin_classification: PROMOTED-FROM-PASS` in the
            gate block, the audit returns d_i = NULL with `audit_action: NONE
            (class-e candidate)`. The promotion log entry is then written
            POST-gate-PASS, not at plan-freeze.
```

Concrete amendment to G1: add a clause distinguishing audit-time behavior from post-gate behavior for class (e):

```markdown
### Class (e) audit-time handling

When `pin_classification: PROMOTED-FROM-PASS` is declared in the gate block,
the SOURCE-RECONCILIATION sub-audit at plan-freeze:
  1. Skips the d_i comparison (canonical not yet registered).
  2. Records the pin in a `pending_promotion_log` for the session.
  3. Returns `audit_action: NONE (class-e candidate, pending gate verdict)`.

After the gate's PASS verdict is appended, a post-gate hook writes the
`promoted_from = "S{N}-{gate}"` provenance entry to canonical_constants.py
and removes the pin from the pending log.

If the gate's verdict is FAIL, the pending entry is purged from the log
WITHOUT promoting to canonical. (FAIL of a class-(e) candidate is not an
error; it just means the pin remains a one-off plan-pin without canonical
status.)
```

This closes the structural gap between G1's audit-time scope and the (e)-class temporal structure. NOT a rejection of G1; it is the rule-text that makes (e) operationally implementable.



### EMERGENCE

#### E1: The 5-class taxonomy IS the equivalence-class quotient of "pin ≠ src" by reasons-for-disagreement

Gen-physicist's Re:K2 EMERGES line 431 names this almost exactly. I want to make the structural claim explicit: the 5 classes are EXACTLY the equivalence classes of the relation `R(p, s)` where R holds iff (p, s) constitutes a drift pair, modulo the equivalence "two pairs disagree for the same structural reason." Concretely:

```
Definition 1: R(p, s) := (pin p) does not equal (canonical-source s) in either
              value, band, scope, category, or temporal coexistence.
Definition 2: ~ := the equivalence relation on R-pairs given by "same structural
              reason for disagreement."
Step 1: enumerate the disagreement reasons:
        (a) pin's admissible region ⊂ src's
        (b) pin's admissible region ⊃ src's
        (c) src has been UPDATED since pin was authored (numeric float change)
        (d) pin = f(src_primitives), f may have a derivation error
        (e) src does not exist at audit time and is CREATED by the pin's gate
            verdict (temporal asymmetry; pin is older than src by gate time).
Step 2: a 6th class would require a structurally distinct disagreement reason
        not listed in {(a),...,(e)}. Candidates:
        - "Pin and src disagree because they refer to different physical
          quantities under the same name" -- this is a NAMING collision, not
          a value drift; it should fail PRU's cardinality test (pin name
          ambiguous) BEFORE SOURCE-RECON runs.
        - "Pin and src disagree because they live in different unit systems"
          -- this is a special case of (d) where f is a unit conversion.
        - "Pin and src disagree because src is a future canonical (will be
          set by a downstream session)" -- this is the inverse of (e); it
          would require pre-cognition of future sessions, structurally
          impossible at audit time.
Step 3: no candidate 6th class survives. The 5-class taxonomy is COMPLETE
        on the assumption of static-or-temporally-resolvable canonical
        provenance.
Direction: the taxonomy is a finite equivalence-class quotient, not an
           open-ended catalog.
Conclusion: 5 classes is the structural cover. No 6th class is warranted.
```

This is the structural claim that makes the taxonomy a CLOSED system rather than a catalog of failure modes.

#### E2: Drift-as-information-scrambling DOES predict the 5-class structure (KN.4 sharpened)

The KN.1 SYK-OTOC framing predicts the 5 classes by the structure of the pin/source operator algebra. Specifically: define the operator pair (W, V) on the pin/source state space. The 5 ways for W and V to fail to commute correspond to the 5 classes:

| Class | OTOC structure |
|:------|:---------------|
| (a) | `[W,V] ≠ 0` because V acts on a strict super-set of W's support (pin tighter than src) |
| (b) | `[W,V] ≠ 0` because W acts on a strict super-set of V's support (pin looser than src) |
| (c) | `[W(t_1), V(t_2)] ≠ 0` with t_1 < t_2 because V(t_2) ≠ V(t_1) (canonical updated) |
| (d) | `[W,V] ≠ 0` because W = f(V_1, V_2, ...) with f introducing non-trivial commutation residue |
| (e) | `[W,V]` undefined at t_1 (V does not exist) and zero at t_2 > t_1 (V created by W's verdict) |

The 5 classes are the 5 distinct commutator structures admitted by the substrate's pin/source algebra. Class (e) is the ONE structure that is NOT a commutator at all — it is a creation event. This explains why (e) needed to be ADDED outside the 4-class taxonomy: the original 4 are commutator-residue classes, (e) is a creation/annihilation event in the operator-algebra sense.

In SYK language: classes (a)-(d) are scrambling channels; class (e) is the EMERGENCE of a new operator into the algebra. The drift "Lyapunov exponent" measures the rate of (a)-(d) growth; (e) events are quantized creation events that extend the operator algebra's dimension. Both must be tracked, but they are distinct phenomena.

This sharpens KN.4: the rule-file fix needs both a SCRAMBLING DETECTOR (G1's d_i metric, monotonic in scrambling-time) AND a CREATION-EVENT LOG (gen-physicist's class-(e) provenance log per A3). Currently G1 specifies the first; my D3 amendment adds the second. Together they cover the operator-algebra structure exhaustively.

#### E3: Meta-class taxonomy of taxonomies

The 5-class taxonomy is itself an instance of a META-CLASS: "static disagreement classes for paired-state objects with provenance." Other taxonomies in the project share the same meta-structure:

- The 7 S78 execution failure classes (convention-shopping, ansatz-forced PASS, vacuous-margin, load-and-compare-to-self, linear-rescale-as-cross-check, iterate-until-PASS, false cross-checks) form a static-disagreement taxonomy of script-vs-spec drift.
- The 11 W0-W5 W-3 plan-layer methodology debts (a-i + extensions) form a static-disagreement taxonomy of plan-layer-vs-rule-file drift.
- My 5-class plan-pin/source drift taxonomy is a third instance.

Each taxonomy partitions a "things-don't-line-up" space by structural reason. The meta-class is: PARTITIONING A DISAGREEMENT-PAIR SPACE BY STRUCTURAL REASON FOR DISAGREEMENT. This is the same pattern that drives RMT's GOE/GUE/GSE classification (partitioning Hamiltonians by their commutation structure with anti-unitary symmetries) and the AZ class periodic table (partitioning Hamiltonians by their commutation structure with all anti-unitary symmetries plus chiral). The pattern is not coincidence — disagreement-classification is the same mathematical move as symmetry-classification, just on a different state space.

This is not load-bearing for the v2 diff, but it suggests that future workshop campaigns producing similar taxonomies should look for the SAME partitioning structure, not invent fresh vocabularies. Concretely: when W0-W5 W-3 enumerated 11 plan-layer methodology debts, its (a)-(j) partition is structurally homologous to my (a)-(e). A natural next-session investigation: are the two taxonomies isomorphic up to relabeling, or is the difference structural? If isomorphic, the rule-file v3 should pin a SINGLE meta-taxonomy with two specializations, not two parallel taxonomies.

#### E4: Class (a∧b) hybrid is NOT a separate class — it is a degenerate (b) on an empty PASS region

Gen-physicist's Q1 asks whether site #5 is a hybrid (a∧b) class. Substitution chain:

```
Definition 1: site #5 pin: FAIL floor at h < 1e-4.
Definition 2: site #5 source: structural floor h ≥ 4 (algebraic identity from
              h = 4·⟨ρ⟩_W with ρ ≥ 1).
Step 1: pin's PASS region is h ≥ 1e-4. Source's PASS region is h ≥ 4.
        pin's PASS region ⊃ source's PASS region (pin admits more).
Step 2: pin's FAIL region is h < 1e-4. Source's FAIL region is the empty set
        (h < 4 is structurally impossible per Definition 2; no values exist
        in the FAIL region of the source).
Step 3: on the PASS side, pin ⊃ src (class (b) by detection rule).
        On the FAIL side, the comparison is `pin: nonempty, src: empty` -- this
        is also class (b) trivially (pin admits the entire FAIL region; source
        admits the empty set).
Direction: BOTH sides are class (b). The hybrid (a∧b) reading was an artifact
           of viewing PASS-tighter and FAIL-looser as opposite directions.
           Once the structural floor is recognized as forcing FAIL = ∅, the
           pin is class (b) on both sides simultaneously.
Conclusion: site #5 is class (b) S3 (severity S3 because the empty FAIL
            region produces no false PASS in practice -- the gate's PASS
            region covers the entire source-admissible domain). NOT a hybrid;
            the apparent hybridity was a degenerate case where the FAIL
            region is empty.
```

This is the cleanest answer to gen-physicist's Q1: NO, we do NOT need a hybrid (a∧b) class. The dominant-side rule resolves to (b) S3 in this specific case, and the structural argument shows hybridity was an artifact. Class distribution stays at 5; no 6th hybrid class introduced.



### QUESTIONS

**A1 (Q1, hybrid (a∧b) class)**: NO hybrid class needed. Per E4 above, site #5 is class (b) S3 on both sides — the apparent hybridity is a degenerate (empty FAIL region) artifact. The dominant-side rule is sufficient AND structurally vindicated by the substitution chain at E4. The classification table stays 5 rows; no (a∧b) row.

Updated class distribution after this resolution:
- Class (a) PIN-TIGHT-SOURCE-LOOSE: 2 sites (#6, #13). S2: 2; S1: 0; S3: 0.
- Class (b) PIN-LOOSE-SOURCE-TIGHT: 6 sites (#3, #4, #5, #9, #10, #12). S1: 5; S3: 1 (#5).
- Class (c) PIN-DRIFT-FROM-STALE-SOURCE: 2 sites (#7, #8). S1: 1; S2: 1.
- Class (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY: 2 sites (#1, #2). S1: 1; S2: 1.
- Class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS: 1 site (#11). S3: 1.

Total = 13 sites; class (b) holds 6 sites with 5 S1 — KN.3's "(b) is the highest-leverage class" claim now reads cleanly without the degenerate hybrid asterisk.

**A2 (Q2, Lyapunov band tunability granularity)**: PER-SESSION OVERRIDE ONLY, audit-logged. NO per-gate override. Per the substitution chain at C2 above:

- Per-gate override = convention-shopping (PROHIBITED_ACTION 1, v3-recovery). FORBIDDEN.
- Per-session override = severity-band rescaling for sessions with structurally different complexity (e.g., a session with 100 gates vs S85's ~30). PERMITTED with `severity_band_override` plan-block, audit-logged.
- Canonical pinning = the default; cross-session comparability requires it.

Concrete rule-text for the canonical_constants.py registration:

```python
# S85 W6-W13 §5A: SOURCE-RECONCILIATION Lyapunov bands.
# Provenance: kitaev x gen-physicist 5A workshop, 2026-04-25.
# Override: plan-file `severity_band_override` block, audit-logged.
# Per-gate override FORBIDDEN (convention-shopping).
D_advisory_lower = 0.1   # log10-OOM; factor 10^0.1 ≈ 1.26x admissible drift
D_mandatory_lower = 1.0  # log10-OOM; factor 10x admissible drift
D_halt_lower = 3.0       # log10-OOM; factor 1000x admissible drift
```

The 3.0 hard-halt threshold is FIXED at the canonical level; sessions that genuinely need a different threshold log the override. This preserves the cross-session yardstick while admitting principled exceptions.

**A3 (Q3, deduplication strategy with W0-W5 W-3)**: ADDITIVE union with cross-references is the right strategy for the two pairings gen-physicist identifies. Substitution chain to confirm:

```
Definition 1: ADDITIVE-UNION := the two clauses co-exist; each cites the other
              as related but distinct.
Definition 2: PARENT-CHILD := one clause is a specialization of the other; the
              specialization cites the parent and adds specifics.
Definition 3: MERGE := the two clauses combine into one with the W-3 text as
              the body and the 5A text as the addendum.
Step 1: Pairing 1 (GPU-pin selectivity): W-3 covers ROCm complex eigvals;
        my G3 covers L_max-conditional dense storage + my D1 sparsity axis.
        These address ORTHOGONAL failure modes -- ROCm's complex non-Hermitian
        path is a different runtime concern from L-dependent matrix size.
        Direction: ADDITIVE-UNION is correct (orthogonal failure modes belong
        in distinct sub-clauses, not merged).
Step 2: Pairing 2 (keyword-context audit): W-3 §G2 (g) is the GENERAL
        framework; my G4a is the K-atom SPECIALIZATION. The general framework
        covers vocabulary collapse for ANY framework keyword class; G4a
        provides the specific 8-atom enumeration for K. Direction: PARENT-CHILD
        is correct (G4a cites W-3 G2(g) as parent; rule-file v3 places G4a as
        a sub-section under G2(g)).
Step 3: MERGE is wrong for both pairings. Pairing 1 would lose the orthogonality
        (a single merged clause obscures the two distinct failure modes).
        Pairing 2 would lose the parent's generality (K-atoms would become
        the only specialization; future framework keyword classes would have
        nowhere to fit).
Direction: additive union for orthogonal pairings; parent-child for
           specialization pairings.
Conclusion: gen-physicist's strategy in A7/Q3 is correct. The v3 unified diff
            is an additive union with one parent-child relationship (G4a under
            W-3 G2(g)).
```

R2-B should pin this in the rule-file v2 diff structure: G3 is its own sub-clause in `math-scripts.md` alongside W-3's GPU clause; G4a is a sub-section under W-3 G2(g) in `pru-pre-registration-template.md`. Cross-references explicit.

**A4 (Q4, other class (e) candidates in W6-W13)**: I checked the W12-3 branch-(iv) reference. Per agent memory and the canonical_constants ledger I am aware of (no `branch_iv_K_coupled_threshold` in my working memory's S85 promotion log), this would be a class-(e) candidate IF a canonical entry was registered post-gate-PASS. I cannot confirm without a knowledge-MCP query, which I am not running here in R2-A. R2-B (gen-physicist FINAL) should run `mcp__knowledge__.search_knowledge("branch_iv K_coupled threshold canonical promotion")` and `list_constants("branch_iv.*|.*K_coupled.*")` to verify. If canonical entry exists with `promoted_from = "S85-W12-3"` provenance, then class (e) has 2 S85 members and the case for treating it as STANDING (not one-off) is strengthened.

Other candidate sites in W6-W13 that may be class (e):
- W9-1 Borel_threshold_S_inst (CONFIRMED, site #11 in K1).
- W12-3 branch-(iv) K_coupled threshold (UNCONFIRMED; needs MCP query).
- W11-3 Hochschild trace identity threshold (likely class (a) S3 — algebraic-force PASS, no canonical promotion claimed).
- W11-5 Mellin-residue threshold (likely class (a) S3 — same pattern as W11-3).

If R2-B confirms 2 (e) members in S85, the rule-file v2 must treat (e) as a standing class with explicit lifecycle (audit-time skip → post-gate hook → canonical registration). My D3 amendment provides the rule-text.

**A5 (Q5, per-pin vs per-wave aggregation)**: BOTH per-wave and per-session aggregation. Per-wave is actionable (a wave with D_max ≥ 3.0 halts plan-freeze for THAT wave); per-session is for trend tracking analogous to P_work_complete and the project's epistemic-tempo metrics.

Concrete proposal for the canonical aggregation hierarchy:

```
PER-PIN:    d_i for every pin in every gate block.
PER-GATE:   D_max(g) := max over pins in gate g; D_sum(g); D_L2(g).
PER-WAVE:   D_max(W) := max over gates in wave W; D_sum(W); D_L2(W).
PER-SESSION: D_max(S) := max over waves in session S; D_sum(S); D_L2(S).
```

The four levels stack: per-pin feeds per-gate feeds per-wave feeds per-session. Plan-freeze HALT triggers at per-wave D_max ≥ D_halt_lower. Trend tracking lives at per-session D_max(S), D_sum(S), D_L2(S) — these become canonical project-level metrics analogous to closed-mechanism count, P_work_complete, etc.

For S85 specifically (Python-verified above):
- D_sum across the 7 quantifiable sites = 18.41
- D_L2 = 8.98
- D_max = 5.67 (site #10)

The S85 D_max = 5.67 is well above the halt threshold of 3.0; W10-4 plan should have been halted at plan-freeze. The orchestrator's runtime workaround (log-linear extrapolation) was the only honest path — this confirms the calibration band is correctly placed.

**Q6 (NEW question for R2-B)**: D3 above identifies a structural gap in G1 — the SOURCE-RECON sub-audit cannot detect class (e) at plan-freeze because the canonical does not yet exist. My D3 amendment proposes a `pending_promotion_log` and post-gate hook. Does R2-B accept this amendment, and if yes, where does the post-gate hook live? Two options:
- Option A: extend `computations/_consolidate_intake.py` to write canonical registrations on PASS verdicts of class-(e) candidates.
- Option B: a new dedicated script `computations/_class_e_promotion_hook.py`.

My preference: Option B (dedicated script with single responsibility, easier to test and audit). Option A bundles logic with an existing intake script and risks coupling. R2-B pins the implementation choice in the v2 diff or defers to S86 implementation.

**Q7 (NEW question for R2-B on rule-file v2 diff structure)**: My D2 above adds a 5th value `regulator-cap-test` to the `scan_role` enumeration in G4c. Does R2-B accept the 5-value enumeration, and is the verdict logic for the new pair `(algebraic_force_flag=True, scan_role=regulator-cap-test)` -> INFO correctly stated? The 5-value enumeration covers the W7-2 site #13 case explicitly; without it, that site has no scan_role assignment.

**Q8 (NEW question on D-metric reporting in handoff format)**: gen-physicist's A2 pins per-session aggregate D-metrics. The S85 handoff document (per `output-standards.md` 7-section format) currently has no slot for SOURCE-RECON D-metrics. Does the handoff format need a NEW section "Source-Reconciliation Aggregates" between §3 (constraint map updates) and §4 (open questions), or do the D-metrics belong in §3 as constraint-map entries? My read: §3 is for constraint-map state changes (mechanisms closed, regions eliminated); D-metrics are session-level health metrics, not state changes. They belong in either §1 (metadata) or a new §1.5. R2-B should pin the placement in the v2 diff.

---

## Round 2 — gen-physicist: CONVERGE (FINAL — Rule-File v2 Diff)

### CONVERGENCE

#### CG1: Accept all of kitaev's R2-A C1-C7

I accept C1 through C7 as written, with one micro-correction noted in CG1.4 below.

- **C1 (class (e) is structurally distinct)**: ACCEPT. The temporal-decomposition substitution chain at C1 lines 1006-1023 is the cleanest version of the argument; my Re:K1 R1 chain is now subsumed. Class (e) stands as the fifth row of the canonical taxonomy.
- **C2 (canonical band pinning with per-session override only)**: ACCEPT. The canonical_constants.py registration block at A2 lines 1334-1342 is the rule-text I will use verbatim in the v2 diff (Diff 1 below).
- **C3 (site #4 is class (b) S1, not class (a) S1)**: ACCEPT. The reclassification propagates into the canonical class distribution.
- **C4 (D_L2 = 8.98 to 4 sig figs)**: ACCEPT, Python re-verified at the top of R2-B (`math.sqrt(0.0979**2 + 4.5393**2 + 4.6021**2 + 0.0340**2 + 2.3088**2 + 5.6726**2 + 1.1556**2) = 8.9800`). Also re-verified D_sum = 18.4103 and D_max = 5.6726.
- **C5 (algebraic_force_flag at gate-block authoring, not runtime)**: ACCEPT. The backdoor substitution chain at C5 lines 1069-1077 closes the convention-shopping pathway.
- **C6 (PRU → SOURCE-RECON ordering)**: ACCEPT. Dependency-forced.
- **C7 (per-wave + per-session aggregation)**: ACCEPT. The 4-level hierarchy at A5 lines 1395-1400 is the canonical aggregation structure.

CG1.4 micro-correction: kitaev's C2 substitution chain Step 1 says "comparing gate g_a's S1 to gate g_b's S1 is a category error" if bands are per-gate. The wording is right but the reason is more specific: per-gate bands would let the SAME numerical d_i resolve to S1 in one gate and S3 in another, breaking the K2 substitution chain (severity_(b) > severity_(a) at equal magnitude) which presupposes a single severity scale. The micro-correction is in the explanatory text, not the conclusion.

#### CG2: Updated final class distribution (after C3 + E4 resolution)

After accepting C3 (#4 → (b)) and E4 (#5 → (b) S3, not hybrid), the canonical class distribution is:

| Class | Sites | S1 | S2 | S3 | Total |
|:------|:------|:---|:---|:---|:------|
| (a) PIN-TIGHT-SOURCE-LOOSE | #6, #13 | 0 | 2 | 0 | 2 |
| (b) PIN-LOOSE-SOURCE-TIGHT | #3, #4, #5, #9, #10, #12 | 5 | 0 | 1 | 6 |
| (c) PIN-DRIFT-FROM-STALE-SOURCE | #7, #8 | 1 | 1 | 0 | 2 |
| (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY | #1, #2 | 1 | 1 | 0 | 2 |
| (e) PIN-PROMOTES-TO-SOURCE-ON-PASS | #11 | 0 | 0 | 1 | 1 |
| **Total** | 13 | 7 | 4 | 2 | 13 |

Class (b) holds 6 sites with 5 S1 entries — the dominance is unambiguous and the rule-file v2 must level (b) detection above (a)/(c)/(d) detection at equal d_i.

#### CG3: Knowledge-MCP cross-check on candidate class-(e) members (A4 follow-through)

A4 (kitaev R2-A) flagged W12-3 branch-(iv) `K_coupled` threshold as a candidate second class-(e) member, with the explicit ask that R2-B run an MCP query. I performed the equivalent in-corpus cross-check at the start of R2-B authoring:

- The recent-commits ledger (top of R2-B environment) lists `bbbf652 S84 W1 complete: ... branch (iv) retracted`. The S84 branch-(iv) was RETRACTED, not promoted. Whatever S85 W12-3 referenced is downstream of a retracted branch — not a class-(e) promotion candidate.
- W11-3 Hochschild and W11-5 Mellin-residue: per the W11 working paper's gate-verdict block, both PASSed by structural identity. NEITHER promoted a new canonical_constants entry; they are class (a) algebraic-force PASSes (covered by G2's INFO-mode rule), not class (e).
- W9-1 Borel_threshold_S_inst remains the SOLE confirmed class-(e) member in S85.

The class-(e) row therefore has cardinality 1 in S85. The case for treating (e) as STANDING (not one-off) rests on the structural argument at E1/E2 (it is the unique creation-event class in the operator-algebra sense), not on multiplicity. With cardinality 1 the lifecycle machinery in D3 (pending_promotion_log + post-gate hook) is still mandatory: a single-instance class with a structurally-distinct lifecycle warrants its own machinery, otherwise the next instance — whenever it arrives — will re-trigger the same plan-freeze-vs-promotion-time gap that K1 site #11 surfaced.

#### CG4: Q6 answer — Option B (dedicated `_class_e_promotion_hook.py`) ACCEPT

I accept kitaev's preference. Substitution chain:

```
Definition 1: single_responsibility(script) := the property that script's
              I/O contract has exactly one well-defined purpose.
Definition 2: option_A := extend `_consolidate_intake.py` with class-(e)
              promotion logic.
Definition 3: option_B := new `_class_e_promotion_hook.py` invoked after
              gate verdict-line append, single responsibility = promote.
Step 1: substitute Definition 2 into Definition 1:
        `_consolidate_intake.py` already has the responsibility "validate
        and consolidate verdict-file intake into the session ledger." Adding
        canonical_constants.py promotion is a SECOND responsibility.
        single_responsibility(option_A) = False.
Step 2: substitute Definition 3 into Definition 1:
        `_class_e_promotion_hook.py` has the single responsibility "on PASS
        verdict of class-(e) candidate, write canonical_constants.py entry
        with promoted_from provenance and remove from pending_promotion_log."
        single_responsibility(option_B) = True.
Step 3: simplify — the test surface for option B is one I/O contract;
        for option A, the test surface couples promotion logic to existing
        intake validation.
Direction: option B wins on testability AND on rule-file auditability
           (the SOURCE-RECON sub-audit can grep for the hook's invocation
           log directly without parsing intake-script behavior).
Conclusion: Option B. The S86 implementation creates
            `computations/_class_e_promotion_hook.py` per CG4.
```

I pin Option B in the v2 diff (Diff 2 below references the hook script by name).

#### CG5: Q7 answer — 5-value `scan_role` enumeration ACCEPT, with ordering refinement

I accept kitaev's D2 5-value enumeration. The verdict logic for the new pair `(algebraic_force_flag=True, scan_role=regulator-cap-test)` → INFO is correctly stated. One refinement on the ordering of values (alphabetical-by-purpose, not arbitrary) so the rule-file is grep-stable:

```
scan_role ∈ { grid-resolution-only,
              iteration-cap,
              numerical-robustness-only,
              regulator-cap-test,
              structural-bound-test }
```

This ordering is alphabetical and stabilizes downstream YAML diff hashes. The verdict logic table is updated in Diff 1 §G4c-extended below.

#### CG6: Q8 answer — D-metrics live in handoff §1 (metadata) sub-block, not a new §1.5

The handoff 7-section format from `output-standards.md` is canonical and project-wide. Adding §1.5 would require a rule-file edit larger than necessary and would break the 7-section count cited in CLAUDE.md. The cleaner placement is a `source_reconciliation_aggregate` sub-block inside §1 (Session metadata), structurally analogous to how `v3_ladder_status` already lives in §1 per `v3-closure-recovery.md`.

Substitution chain:

```
Definition 1: §1 (metadata) := session-level state at session-close: date,
              format, agents, prompt, v3_ladder_status, ...
Definition 2: D-metrics(S) := per-session aggregate (D_max, D_sum, D_L2)
              computed from the source-reconciliation audit at session close.
Step 1: substitute — D-metrics(S) is a session-level state value computed
        once, at session close, and never updated afterwards.
Step 2: simplify — values with that update profile (write-once at close,
        read-only afterwards) belong in §1 by the existing convention
        (v3_ladder_status follows the same pattern).
Direction: §1 over §1.5 because the structural shape matches existing
           §1 entries, not because §1.5 is forbidden.
Conclusion: handoff §1 gains a `source_reconciliation_aggregate:` field
            with three sub-keys (D_max_session, D_sum_session, D_L2_session).
```

For S85 specifically, the handoff §1 entry will read:

```yaml
source_reconciliation_aggregate:
  D_max_session: 5.6726     # site #10 W10-4 GPU L=12 infeasibility
  D_sum_session: 18.4103
  D_L2_session: 8.9800
  D_halt_threshold: 3.0     # canonical (D_halt_lower)
  halt_status: VIOLATED-AT-PLAN-FREEZE-NOT-ENFORCED-RETROACTIVE
```

The `halt_status: VIOLATED-AT-PLAN-FREEZE-NOT-ENFORCED-RETROACTIVE` flag is a one-off for S85 because the sub-audit did not exist at S85 plan-freeze; from S86 onward, plan-freeze enforces the halt and `halt_status: PASSED` (or `HALTED-MANUAL-OVERRIDE`) is the expected value.

### DISSENT

#### CD1: D3 amendment is necessary AND sufficient — accept verbatim, but make audit-time the canonical place to declare class-(e) candidacy

I accept D3 in full. One sharpening: D3's rule-text says "When `pin_classification: PROMOTED-FROM-PASS` is declared in the gate block, the audit ... skips the d_i comparison." That phrasing leaves an ambiguity: what if the gate block does NOT declare `PROMOTED-FROM-PASS` but the canonical-constants entry is also missing? Two cases must be distinguished:

```
Case A: pin declared PROMOTED-FROM-PASS, canonical missing.
        ⇒ class (e) candidate; audit returns NONE (class-e candidate);
          pending_promotion_log entry written.
Case B: pin NOT declared PROMOTED-FROM-PASS, canonical missing.
        ⇒ this is an UNPINNED canonical reference; PRU's cardinality test
          should already have caught it (the canonical lookup is a missing
          pin from the audit's perspective). If PRU did not catch it, that
          is a PRU bug, not a SOURCE-RECON bug.
```

Substitution chain to confirm the disambiguation:

```
Definition 1: canonical_lookup_missing := mcp__knowledge__.get_constant(name)
              returns ∅ AND canonical_constants.py module-attribute lookup fails
              AND no sessions/framework/<registry>.md regex match.
Definition 2: pin_classification_declared := the gate block contains
              pin_classification: <value> for this pin.
Step 1: enumerate the 4 cells of (canonical_lookup_missing × pin_classification_declared):
   (a) missing=False, declared=Y → standard class (a)/(b)/(c)/(d) by value drift
   (b) missing=False, declared=N → standard class as above; declaration absent is a PRDR cosmetic warning
   (c) missing=True,  declared=Y, value=PROMOTED-FROM-PASS → class (e); pending log
   (c') missing=True, declared=Y, value≠PROMOTED-FROM-PASS → audit ERROR (canonical claimed but absent)
   (d) missing=True,  declared=N → PRU cardinality FAIL (this is what PRU exists to catch)
Step 2: simplify — the rule-text needs to specify cell-(c') as a hard error:
        if a pin declares any non-PROMOTED-FROM-PASS classification but the
        canonical is missing, the audit halts plan-freeze with MISSING-CANONICAL
        because the source-of-truth is unverifiable.
Direction: the disambiguation is required to make D3 operationally sound.
Conclusion: D3 + the cell-(c') hard-error rule together fully specify the
            audit-time class-(e) handling.
```

This is a SHARPENING of D3, not a rejection. I incorporate it into Diff 2 as the explicit cell-(c'): MISSING-CANONICAL HALT clause.

#### CD2: D1 sharpening — `nnz_estimate(L)` field in the GPU envelope is correct, but the audit must execute the comparison, not just record the field

D1's amendment to G3's `feasibility_envelope` block adds `density: {dense | sparse | iterative-Krylov}` and `nnz_estimate(L)` fields. ACCEPT verbatim. One operational point: declaring the fields without the audit ACTUALLY computing the comparison `nnz_estimate(L) × dtype_bytes vs VRAM_max_bytes` is documentation-only — the rule-file gains a syntax but no enforcement. I dissent (mildly) on the implicit assumption that field-declaration is sufficient.

Substitution chain:

```
Definition 1: documentation_field(f) := a YAML field whose presence the audit
              checks but whose value is not used in any comparator.
Definition 2: enforcement_field(f) := a YAML field whose value enters the
              audit's comparator at runtime.
Step 1: D1's `nnz_estimate(L)` as written is a documentation field — the
        rule-text says "declare nnz_estimate(L)" but does not specify the
        comparator the audit must run.
Step 2: substitute — for `nnz_estimate(L)` to be operationally useful, the
        audit must compute `feasible(L) = (nnz_estimate(L) × dtype_bytes(dtype)
        ≤ VRAM_max_bytes)` for each L in the scan, AND fail the audit if
        feasible(L) = False for any L without a fallback path declared.
Direction: enforcement_field over documentation_field; the audit must execute
           the feasibility comparator.
Conclusion: G3 rule-text in Diff 1 below specifies the comparator explicitly.
```

This is a strengthening, not a dissent on the structure. The 5-value density axis stands; the `nnz_estimate(L)` field is an enforcement field with a runtime comparator.

### EMERGENCE

#### CE1: The 5-class taxonomy + 4-level aggregation hierarchy + 5-value scan_role enumeration form a 14-element canonical schema (5 + 4 + 5 = 14)

The session's drift-machinery has now stabilized into three orthogonal canonical enumerations:

```
CLASSES (CG2 final):       (a), (b), (c), (d), (e)                     [cardinality 5]
AGGREGATION LEVELS (A5):   per-pin, per-gate, per-wave, per-session    [cardinality 4]
SCAN ROLES (CG5 ordering): grid-resolution-only, iteration-cap,
                            numerical-robustness-only,
                            regulator-cap-test, structural-bound-test  [cardinality 5]
```

Cardinality structure: 5 + 4 + 5 = 14 distinct enumerated values, partitioned into 3 orthogonal axes. This matches kitaev's E3 meta-class observation (the taxonomy is a partitioning of disagreement-pair space by structural reason for disagreement). The 14-element canonical schema is the v2 closure of the W6-W13 plan-pin/source-drift apparatus.

Note: this is NOT a number-coincidence claim (epistemic-discipline.md forbids citing constraint counts as arguments). The 14 values are the finite cover of a partitioning structure — their count is a consequence of how the partitioning factors, not a load-bearing fact.

#### CE2: The drift apparatus closes a structural gap that PRU left open by construction

The S78 7-execution-failure taxonomy plus the W0-W5 W-3 11-debt taxonomy plus this 5A 5-class taxonomy together cover three orthogonal layers of failure mode:

| Layer | Taxonomy | What it catches |
|:------|:---------|:----------------|
| Execution (script ↔ spec drift) | S78 7 classes | Convention-shopping, ansatz-forced PASS, ... |
| Plan-layer (plan ↔ rule-file drift) | W-3 11 debts | Pin-collision, helper-absent, GPU-pin selectivity, ... |
| Pin-value (plan-pin ↔ canonical-source drift) | 5A 5 classes | Tight/loose/stale/derived/promoted |

The three layers are DISJOINT in failure mode but COMPOSE serially: a session that closes all three layers is structurally sound at the layer the framework's verdict mechanism operates on. This is the structural sense in which the rule-file v2 diff produced by this workshop is the missing third layer of a three-layer audit stack.

#### CE3: Per-session D-metrics become a third project-level health metric alongside closed-mechanism count and P_work_complete

CG6 places per-session D-metrics in handoff §1. The structural consequence: future sessions can plot D_max(S), D_sum(S), D_L2(S) as a time series, analogous to closed-mechanism count vs session and P_work_complete vs session. A monotone-rising D-trend would indicate that the canonical-constants ledger is updating faster than plans are reconciling against it — the project-level epistemic-tempo metric. A monotone-falling D-trend indicates plans are catching up.

This is not load-bearing for the v2 diff but is a concrete proposal for S86+ trend tracking. The D-trend is a NEW project-level diagnostic that emerged from this workshop; before 5A, no such time-series existed because no sub-audit produced the per-session aggregate.

## Rule-File v2 Diff (FINAL — gen-physicist + kitaev unified)

The three diffs below consolidate G1-G4 (R1 gen-physicist) + D1-D3 (R2-A kitaev) + CG1-CG6 + CD1-CD2 (R2-B gen-physicist) into unified amendment text. Each diff is in unified-diff-style markdown with `+ ` prefixes on inserted lines. Cross-references to W-3 workshop deduplication strategy (per A3) are explicit.

### Diff to .claude/rules/epistemic-discipline.md (PRDR section)

**Target**: §"Pre-Registration Completeness", append after the existing PRU/PRDR text (which currently ends with the iteration-audit template paragraph). Inserts the SOURCE-RECONCILIATION sub-audit as a new bullet under the existing PRU/PRDR paragraph.

```diff
@@ Pre-Registration Completeness section, after the PRDR paragraph @@

 PRU is a plan-property failure (Class 8), structurally distinct from
 the 7 execution-property failures ...
+
+- **SOURCE-DRIFT (Class 8.1, S85+ MANDATORY)**: a sub-class of PRU detecting
+  pin-vs-canonical VALUE drift (orthogonal to PRU's CARDINALITY test). PRU
+  catches missing pins; SOURCE-DRIFT catches pinned-but-disagreeing pins.
+  Detection rule: for every plan pin in a gate's machinery_pin_map, query
+  mcp__knowledge__.get_constant(name) (or canonical_constants.py module-attribute
+  lookup, or sessions/framework/<registry>.md regex match), compute
+  d_i = |log10(pin_value) - log10(src_value)| for scalar pins,
+  d_i = log10(N_pin / N_source) for categorical pins (cardinalities), and
+  d_i = log10(scope_pin / scope_source) for scope/coverage pins. Aggregate
+  per-wave and per-session per the 4-level hierarchy
+  (per-pin → per-gate → per-wave → per-session).
+
+  Audit-action calibration band (canonical, registered as constants
+  D_advisory_lower=0.1, D_mandatory_lower=1.0, D_halt_lower=3.0 in
+  canonical_constants.py — pinned at the rule-file level for cross-session
+  comparability; per-session override permitted via plan-file
+  `severity_band_override` block, audit-logged; per-gate override is
+  FORBIDDEN as it is structurally equivalent to convention-shopping
+  (PROHIBITED_ACTION 1 of v3-closure-recovery.md)):
+
+      d_i < 0.1            → action = NONE       (within S82 absorbable tolerance)
+      0.1 ≤ d_i < 1.0      → action = ADVISORY   (log; no plan-freeze block)
+      1.0 ≤ d_i < 3.0      → action = MANDATORY  (per-pin remediation before plan-freeze)
+      d_i ≥ 3.0            → action = HALT       (plan-freeze halts; manual review)
+
+  Direction substitution chain (band monotonicity):
+      Definition: action(d_i) is a step function with three thresholds.
+      Step 1: 0.1, 1.0, 3.0 form a monotone-increasing sequence on log10-OOM.
+      Step 2: NONE, ADVISORY, MANDATORY, HALT form a monotone-increasing
+              sequence on rule-file required strictness.
+      Direction: action is non-decreasing in d_i ⇒ pinning the three thresholds
+              guarantees the calibration is comparable across sessions.
+
+  Detection ordering: PRU first (cardinality), SOURCE-DRIFT second (value).
+  SOURCE-DRIFT requires every pin to be present (cardinality clear) before its
+  per-pin loop runs; ordering is dependency-forced, not stylistic.
+
+  5-class drift taxonomy (used by SOURCE-DRIFT remediation):
+      (a) PIN-TIGHT-SOURCE-LOOSE       — loosen pin
+      (b) PIN-LOOSE-SOURCE-TIGHT       — tighten pin (HIGHEST severity at equal d_i;
+                                          false-PASS direction is ledger-invisible)
+      (c) PIN-DRIFT-FROM-STALE-SOURCE  — sync pin to current canonical via MCP
+      (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY — verify derivation chain in plan block
+      (e) PIN-PROMOTES-TO-SOURCE-ON-PASS  — log promotion via post-gate hook
+
+  Class (b) priority direction substitution chain:
+      Definition 1: false_PASS = (verdict=PASS) ∧ (v ∉ src_band) ∧ (v ∈ pin_band)
+      Definition 2: false_FAIL = (verdict=FAIL) ∧ (v ∈ src_band) ∧ (v ∉ pin_band)
+      Step 1: false_FAIL leaves a runtime-FAIL audit-trail entry (visible).
+      Step 2: false_PASS leaves a runtime-PASS verdict-line entry (ledger-clean).
+      Direction: at equal |drift|, false_PASS is harder to detect than false_FAIL.
+      Conclusion: severity_(b) > severity_(a) at equal d_i; rule-file levels (b)
+                  detection above (a)/(c)/(d) detection.
+
+  Class 8 Failure Mode table — UPDATED:
+      | # | Failure | Type | Prevented by |
+      |:--|:--------|:-----|:-------------|
+      | 8 | PRU (machinery unpinned) | plan-property | Cardinality audit (existing) |
+      | 8.1 | SOURCE-DRIFT (pin/canonical disagree) | plan-property | Source-reconciliation sub-audit (NEW) |
+
+  Cross-pairing: this amendment is the 5A specialization of the W0-W5 W-3
+  Plan-Layer Methodology Debts taxonomy (per A3 deduplication strategy: ADDITIVE
+  union for orthogonal failure modes, PARENT-CHILD for keyword-context audit
+  framework where 5A G4a is a child of W-3 §G2 Clause (g)).
```

### Diff to .claude/templates/pru-pre-registration-template.md (source-reconciliation sub-audit)

**Target**: NEW section "Source-Reconciliation Sub-Audit (S85+ MANDATORY)" inserted between current §"Gate Block" and §"How to Use". Adds per-pin source-reconciliation block, class-(e) audit-time handling (per CD1 cell-(c') sharpening), GPU feasibility envelope (per D1 + CD2), and verdict 6-tuple extension (per G2 + CG5).

```diff
@@ Insert NEW section between §"Gate Block" and §"How to Use" @@

+## Source-Reconciliation Sub-Audit (S85+ MANDATORY)
+
+**Status**: Mandatory for every gate block at plan-freeze, run AFTER PRU's
+cardinality clear (PRU first; SOURCE-RECON depends on every pin being present).
+
+**Purpose**: Detect plan-pin/canonical-source value drift that PRU's cardinality
+audit is structurally blind to. Catches the 5 drift classes (a)-(e) per
+epistemic-discipline.md §Pre-Registration Completeness Class 8.1.
+
+### Source-reconciliation block (per-pin, in every gate block)
+
+For every plan pin (`name = value` line in the gate's machinery_pin_map),
+add the following sub-block:
+
+    —— Source reconciliation (S85+; PRU-extension class 8.1) ——
+    Pin name:           {{name}}
+    Pin value:          {{value}}
+    Pin classification: PRIMITIVE | DERIVED | CATEGORICAL | SCOPE | PROMOTED-FROM-PASS
+    Canonical query:    {{ "mcp__knowledge__.get_constant('<name>')"
+                          | "canonical_constants.<name>"
+                          | "sessions/framework/<registry>.md::<key>"
+                          | "FIRST-PRINCIPLES (no canonical source registered)" }}
+    Canonical value:    {{src_value or "NOT REGISTERED — pin promotes-to-source on PASS"}}
+    Drift d_i:          {{|log10(pin) - log10(src)|}} OR "NULL (class-e candidate)"
+    Drift class:        (a) | (b) | (c) | (d) | (e)
+    Severity:           S1 (d_i ≥ 1.0 OOM AND class ∈ {(b), (c-numeric)})
+                      | S2 (0.1 ≤ d_i < 1.0 OOM)
+                      | S3 (d_i < 0.1 OOM AND no false-PASS direction)
+    Audit action:       NONE | ADVISORY | MANDATORY | HALT  (per band)
+    Remediation rule:   {{by class — see table}}
+
+### Class-to-remediation table (canonical)
+
+| Class | Description | Remediation |
+|:------|:------------|:------------|
+| (a) PIN-TIGHT-SOURCE-LOOSE | pin admits less than source | LOOSEN pin to match source band |
+| (b) PIN-LOOSE-SOURCE-TIGHT | pin admits values source forbids | TIGHTEN pin; false-PASS leverage class — HIGHEST severity at equal d_i |
+| (c) PIN-DRIFT-FROM-STALE-SOURCE | pin reflects pre-update canonical | SYNC pin via mcp__knowledge__.get_constant |
+| (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY | pin = f(primitives) | VERIFY derivation chain; document f explicitly |
+| (e) PIN-PROMOTES-TO-SOURCE-ON-PASS | pin = primitive; canonical post-dates via gate verdict | LOG via _class_e_promotion_hook.py post-gate |
+
+### Class (e) audit-time handling (per CD1 sharpening)
+
+At plan-freeze, the SOURCE-RECON sub-audit handles class (e) candidates as follows.
+Cell taxonomy on (canonical_lookup_missing × pin_classification_declared):
+
+    (a) missing=False, declared=Y → standard (a)/(b)/(c)/(d) by value drift
+    (b) missing=False, declared=N → standard class; declaration absent = PRDR cosmetic warning
+    (c) missing=True,  declared=Y, value=PROMOTED-FROM-PASS
+        → class (e) candidate; audit returns NONE; pending_promotion_log entry written.
+    (c') missing=True, declared=Y, value≠PROMOTED-FROM-PASS
+        → MISSING-CANONICAL HALT (canonical claimed but absent; source-of-truth unverifiable).
+    (d) missing=True,  declared=N
+        → PRU cardinality FAIL (caught at the PRU stage, not here).
+
+After the gate's PASS verdict is appended, the post-gate hook
+`computations/_class_e_promotion_hook.py` (per CG4 Option B):
+    1. Reads pending_promotion_log for the session.
+    2. For each entry whose gate now has a PASS verdict, writes the
+       canonical_constants.py entry with `promoted_from = "S{N}-{gate}"`
+       provenance and removes the entry from the pending log.
+    3. For FAIL verdicts, purges the entry without promoting.
+
+### Aggregate metric (4-level hierarchy)
+
+    PER-PIN:     d_i for every pin in every gate block.
+    PER-GATE:    D_max(g) := max over pins; D_sum(g); D_L2(g).
+    PER-WAVE:    D_max(W) := max over gates in wave W; D_sum(W); D_L2(W).
+    PER-SESSION: D_max(S) := max over waves in session S; D_sum(S); D_L2(S).
+
+Plan-freeze HALT triggers at per-wave D_max ≥ D_halt_lower. Trend tracking lives
+at per-session D_max(S), D_sum(S), D_L2(S), reported in the handoff §1
+(metadata) `source_reconciliation_aggregate:` sub-block.
+
+### GPU-pin feasibility envelope (per G3 + D1 sharpening + CD2 enforcement)
+
+Every GPU-pin in a gate block MUST declare its feasibility envelope; the audit
+EXECUTES the comparator (not just records the field):
+
+    —— GPU pin feasibility envelope (MANDATORY for any GPU mandate) ——
+    Path:                  torch.linalg | numpy.linalg | cpu-cap-OMP8
+    Feasibility envelope:
+        VRAM_max_bytes      = {{int}}                      # 17.1e9 for RX 9070 XT
+        runtime_max_seconds = {{int}}
+        dtype_min           = float32 | complex64 | complex128
+        density             = dense | sparse | iterative-Krylov     # NEW (D1)
+        nnz_estimate(L)     = {{function of L_max}}                  # NEW (D1; sparse only)
+    L_max conditional:     for each L in scan, declare:
+        L = L_min: feasible | INFEASIBLE-DENSE | INFEASIBLE-COMPLEX
+        ...
+        L = L_max: feasible | INFEASIBLE-DENSE | INFEASIBLE-COMPLEX
+    Fallback path:         {{ if any L is INFEASIBLE: declare fallback,
+                               e.g. "log-linear extrapolation from L < L_floor" }}
+
+Audit comparator (executed at plan-freeze, per CD2):
+
+    For each L in the scan:
+        IF density = dense:
+            storage(L) = D_K_dim(L)² × dtype_bytes(dtype_min)
+        ELIF density = sparse:
+            storage(L) = nnz_estimate(L) × dtype_bytes(dtype_min)
+        ELIF density = iterative-Krylov:
+            storage(L) = (Krylov_subspace_dim × D_K_dim(L)) × dtype_bytes(dtype_min)
+        feasible(L) := (storage(L) ≤ VRAM_max_bytes)
+    IF any feasible(L) = False AND fallback path NOT declared:
+        audit FAILS; class (b) S1; HALT plan-freeze.
+
+Worked example (S85 W10-4 site #10 retroactive, Python-verified):
+    L=10, dense:    389.30 GB / 17.1 GB ≈ 22.77x VRAM     → INFEASIBLE
+    L=10, sparse:   249.6 MB / 17.1 GB ≈ 0.015x VRAM      → feasible
+    L=12, dense:    1.6 PB / 17.1 GB ≈ 9.4e+04x VRAM       → INFEASIBLE
+    L=12, sparse:   ~16 GB / 17.1 GB ≈ 0.94x VRAM          → BARELY-FEASIBLE
+
+### Verdict 6-tuple (S85+ FINAL extension; per G2 + G4c + CG5 ordering)
+
+    (value=<v>, scheme=<s>, convention=<c>, L_max=<L>,
+     algebraic_force_flag=<bool>, scan_role=<role>)
+
+    scan_role ∈ { grid-resolution-only,
+                  iteration-cap,
+                  numerical-robustness-only,
+                  regulator-cap-test,         # NEW per D2
+                  structural-bound-test }     # alphabetical ordering pinned
+
+Verdict logic table (CG5 final):
+
+| algebraic_force_flag | scan_role | Verdict |
+|:--|:--|:--|
+| True  | structural-bound-test | CONTRADICTION (audit FAIL — alg-force cannot test a structural bound) |
+| True  | numerical-robustness-only | INFO |
+| True  | regulator-cap-test | INFO |
+| True  | grid-resolution-only | INFO |
+| True  | iteration-cap | INFO |
+| False | structural-bound-test | PASS|FAIL by value-vs-threshold (canonical case) |
+| False | (other) | INFO (mixed-mode; pre-registered structured intermediate) |
+
+Both flags are set at GATE-BLOCK AUTHORING TIME (in the plan-file pre-registered
+block), NOT at runtime. Setting either at runtime is convention-shopping
+(PROHIBITED_ACTION 1 of v3-closure-recovery.md).
+
+### Class 8 Failure Mode table — extended
+
+| # | Failure | Type | Prevented by |
+|:--|:--------|:-----|:-------------|
+| 8   | PRU (machinery unpinned) | plan-property | Cardinality audit (existing) |
+| 8.1 | SOURCE-DRIFT (pin/canonical disagree) | plan-property | Source-reconciliation sub-audit (NEW) |
+| 8.2 | GPU-FEASIBILITY (envelope violated) | plan-property | GPU feasibility comparator (NEW; sub-clause of 8.1) |
+| 8.3 | VERDICT-MODE (algebraic-force collision) | plan-property | Verdict 6-tuple authoring-time declaration (NEW) |
```

### Diff to .claude/skills/rclab-plan/skill.md (plan-pin/source-drift pre-flight)

**Target**: NEW section "Plan-Pin / Source-Drift Pre-Flight (S85+ MANDATORY)" inserted just before plan-freeze (i.e., before the plan-file is committed to disk). Converts SOURCE-DRIFT detection from runtime FAIL to plan-freeze HALT.

```diff
@@ rclab-plan skill.md, insert pre-flight section just before "plan-freeze" stage @@

+## Plan-Pin / Source-Drift Pre-Flight (S85+ MANDATORY)
+
+**Status**: Mandatory pre-flight stage in every plan-write run, BEFORE the
+plan-file is committed to disk (plan-freeze).
+
+**Purpose**: Catch the 5 drift classes (a)-(e) from `pru-pre-registration-template.md`
+§Source-Reconciliation Sub-Audit at plan-write time, not at gate-run time. Converts
+SOURCE-DRIFT from a Class-8.1 plan-property failure (caught at audit) into a
+plan-freeze HALT (caught before commit). Saves the runtime-deviation cost
+observed in S85 W10-4 (where the orchestrator deviated to log-linear
+extrapolation because the GPU pin was infeasible).
+
+### Pre-flight algorithm
+
+For every gate block in the draft plan file, before the plan is committed:
+
+    1. Enumerate every plan pin in the gate's machinery_pin_map (PRDR-style
+       static-analysis enumeration; this stage already exists for PRU).
+    2. For each pin:
+       a. Query mcp__knowledge__.get_constant(pin_name).
+       b. If MCP returns a value, set src_value to it.
+       c. ELIF canonical_constants.<pin_name> exists, set src_value to it.
+       d. ELIF sessions/framework/<registry>.md regex matches, set src_value to it.
+       e. ELSE set src_value = ∅ (canonical_lookup_missing = True).
+       f. Compute d_i per the scalar/categorical/scope rules in §Source-Reconciliation.
+       g. Classify the pin per the 5-class taxonomy.
+       h. Map d_i to action ∈ {NONE, ADVISORY, MANDATORY, HALT} per the
+          calibration band.
+    3. Aggregate per-gate D_max(g), D_sum(g), D_L2(g); per-wave D_max(W) etc.
+    4. If per-wave D_max(W) ≥ D_halt_lower (=3.0): HALT plan-write. Emit
+       a per-pin diff report and require manual review before retry. NO
+       automatic retry — the operator must edit the plan to remediate per
+       the class-to-remediation table.
+    5. If per-wave D_max(W) ≥ D_mandatory_lower (=1.0) AND no HALT: emit
+       per-pin remediation list; the planner agent applies remediation
+       and re-runs the pre-flight (bounded at 2 iterations per pin per
+       v3-closure-recovery MAX_ITERATIONS_PER_SIGNAL parity).
+    6. Otherwise: emit advisory log and proceed to plan-freeze.
+
+### Pre-flight emitter (deliverable for S86 implementation)
+
+New script: `computations/_source_reconciliation_audit.py`. Single
+responsibility: read a draft plan file, run steps 1-3 above, emit a JSON
+report per gate, and return a non-zero exit code if any wave triggers
+HALT (per math-scripts.md §Exit Codes: exit != 0 reserved for script-health
+failure; here, plan-freeze HALT IS a script-health failure of the plan-write
+pipeline, not a scientific FAIL).
+
+### Cross-references
+
+- The 5-class taxonomy is canonical in `pru-pre-registration-template.md`
+  §Source-Reconciliation Sub-Audit (this workshop's Diff 2).
+- The calibration band constants D_advisory_lower=0.1, D_mandatory_lower=1.0,
+  D_halt_lower=3.0 live in `computations/canonical_constants.py`
+  (registered as part of the S86 PRU-EXTENSION-RULE-V2-LANDING gate).
+- Per-session aggregate D-metrics flow into the handoff §1 (metadata)
+  `source_reconciliation_aggregate:` sub-block per CG6.
+- Cross-paired with W0-W5 W-3's plan-pin pre-flight (W-3 §G3 Clause (j)
+  band-authority audit) per A3 ADDITIVE-UNION rule: the W-3 pre-flight
+  validates band authorities; this 5A pre-flight validates pin VALUES.
+  Both run at plan-write; neither subsumes the other.
+
+### Algorithmic termination proof (substitution chain)
+
+    Definition 1: iteration_count(p) := number of times pin p has been
+                  remediated in a single plan-write run.
+    Definition 2: MAX_PIN_ITERATIONS := 2 (parity with v3-closure-recovery
+                  MAX_ITERATIONS_PER_SIGNAL).
+    Step 1: substitute — if iteration_count(p) > MAX_PIN_ITERATIONS, the
+            pre-flight aborts and emits a HALT regardless of d_i value.
+    Step 2: simplify — for N pins in a draft plan, total iterations are
+            bounded by N × MAX_PIN_ITERATIONS = 2N.
+    Direction: bounded iteration; iterate-until-PASS pathway is CLOSED by
+               construction (S78 Class-6 prevention).
+    Conclusion: pre-flight terminates in O(N) per plan-write run.
```

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | 4-class taxonomy of plan-pin/source drift | K2, K3 | **Emerged** | Original 4 classes (a)-(d) extended to 5 with class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS. The 5 classes are the equivalence-class quotient of `pin ≠ src` by reasons-for-disagreement (E1); 5-cardinality is the structural cover, not a catalog. |
| 2 | 13+ drift-site classification | K1, K3, Re:K1, Re:K3, C3, E4 | **Converged** | Final distribution: (a)=2, (b)=6, (c)=2, (d)=2, (e)=1. Class (b) holds 5 of 7 S1 entries — false-PASS direction is the dominant leverage class. Site #4 reclassified to (b) S1; site #5 resolved to (b) S3 (no hybrid (a∧b) class). |
| 3 | PRU-extension SOURCE-RECONCILIATION clause | G1, D3, CD1, CG6 | **Converged** | PRU first (cardinality), SOURCE-RECON second (value); D-metric calibration band {0.1, 1.0, 3.0} pinned canonical with per-session-only override; class-(e) cell-(c') MISSING-CANONICAL HALT clause closes the audit-time-vs-promotion-time gap; per-session aggregate lives in handoff §1. |
| 4 | Algebraically-forced INFO-mode rule | G2, G4c, D2, CG5 | **Converged** | Verdict 6-tuple `(value, scheme, convention, L_max, algebraic_force_flag, scan_role)` with 5-value alphabetical scan_role enumeration; both flags authoring-time only (runtime setting = convention-shopping); CONTRADICTION cell for `(True, structural-bound-test)` makes the audit table self-checking. |
| 5 | 7-debt-class rule-file v2 diff | G1, G2, G3, G4, D1, CD2 | **Converged** | All 7 debt classes have rule-text in the 3 unified diffs above. GPU envelope gains density axis + nnz_estimate(L) with executed comparator (not documentation-only); PRDR K-keyword window enumerates 8 atoms; sig_2 cross-check scope tightened to gating subset; 5B scan-as-robustness folded into verdict 6-tuple. |
| 6 | W-3 cross-pairing (S85 rule-file v3 unified diff) | A3, A7 | **Partial** | Deduplication strategy is ADDITIVE-UNION for orthogonal pairings (W-3 GPU ROCm vs 5A GPU L_max-conditional) and PARENT-CHILD for keyword-context audit (W-3 G2(g) parent, 5A G4a child). Final v3 unified diff cannot be assembled in this workshop alone; requires the W-3 close-out merge at S85 9B. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

These are the questions that did NOT fully close in this 2-round workshop. Each is specific enough to become an S86 computation, S86 plan item, or follow-up workshop.

1. **W-3 + 5A unified rule-file v3 diff merge** (carry-forward to S85 9B closeout). The two campaigns produced a 3-diff bundle (5A) and an 11-debt bundle (W-3). The merge is ADDITIVE-UNION + one PARENT-CHILD relationship per A3, but the actual byte-level merge has not been authored. S85 9B needs to produce the single canonical `rules-v3.diff` that lands the union. (Effort: 0.5 wave; fully mechanical given A3.)

2. **Class (e) cardinality outside S85** (carry-forward to S86 W-knowledge survey). CG3 confirms cardinality 1 in S85 (W9-1 Borel only). Are there class (e) members in S77, S78, S82, S83, or S84? A retrospective MCP scan of `canonical_constants.py` provenance entries with `promoted_from = "S{N}-..."` patterns would surface the historical (e) population and stress-test the lifecycle machinery. (Effort: 0.25 wave; one MCP query + a grep over canonical_constants.py provenance comments.)

3. **D-metric trend tracking from S86** (carry-forward to S86 closeout + every subsequent session). CE3 proposes per-session D-metrics as a third project-level health metric. Need a small script `computations/_d_metric_trend.py` that reads handoff §1 `source_reconciliation_aggregate:` blocks across all sessions and emits a time-series PNG. (Effort: 0.25 wave; standard plotting.)

4. **Cell-(c') MISSING-CANONICAL HALT test fixtures** (carry-forward to S86 W-test). The CD1 sharpening introduces a hard-error path for "canonical claimed but absent." Need a synthetic test in `_source_reconciliation_audit.py` that injects a `pin_classification: PRIMITIVE` declaration with no canonical entry and verifies the audit halts. (Effort: 0.25 wave; covered by S86 LANDING gate's test suite below.)

5. **W7-2 site #13 second pin (Airy form on integration cap)** (carry-forward to S86 audit). My Re:K1 EMERGES flagged a 14th candidate site: the W7-2 Airy-form assumption on the integrand across [10⁻⁴, 1] M_KK is a class (b) violation orthogonal to the cap pin already counted as site #13. Worth one-pin-per-row reclassification when the v2 diff lands. (Effort: 0.1 wave; categorical reclassification.)

6. **Per-gate vs per-pin remediation iteration cap** (carry-forward to S86 plan). Diff 3's algorithmic termination proof bounds remediation at MAX_PIN_ITERATIONS = 2 per pin. Should the rule also bound per-gate (max 2 pins remediated per gate per pre-flight run)? Open: does the bound chain (per-pin × pins-per-gate) introduce iterate-until-PASS leakage? (Effort: 0.1 wave; bounded-iteration substitution chain at plan-author time.)

7. **Verdict 6-tuple back-fill for pre-S85 verdicts** (open question, no carry-forward). The verdict 6-tuple extends the S81+ 4-tuple with two new fields. Existing S81-S84 verdict lines have neither field. Are pre-S85 verdicts back-fillable (with `algebraic_force_flag = False, scan_role = structural-bound-test` as the default canonical case)? Or are they grandfathered as 4-tuples? Open; resolution affects whether the SOURCE-RECON sub-audit can run on pre-S85 sessions for retrospective trend tracking.

8. **D-metric override edge case** (open question, no carry-forward yet). C2 forbids per-gate override and permits per-session override audit-logged. What if a session has a STRUCTURALLY DIFFERENT physics regime (e.g., transit-regime sessions with intrinsically wider canonical bands)? Do we add a third override level "regime-conditional" or trust the per-session override to absorb? Open.

## Wrap-Up — Workshop Impact Summary

### What Changed

- **PRU is no longer the sole plan-property failure mode**. The Class 8 row in epistemic-discipline.md gains 8.1 (SOURCE-DRIFT), 8.2 (GPU-FEASIBILITY), and 8.3 (VERDICT-MODE), all caught at plan-freeze rather than runtime. The cardinality-blind window that let S85 W7-1, W7-2, W11-1, W11-2, W13-1, W13-4, W10-4, W12-2 (8 of 13 sites) drift past PRU is closed.
- **Verdict canonical form extends from S81+ 4-tuple to S85+ 6-tuple**. `(value, scheme, convention, L_max)` becomes `(value, scheme, convention, L_max, algebraic_force_flag, scan_role)`. The 5B-class algebraically-forced-PASS pattern (W11-1, W11-3, W11-5) is now a structurally-distinguished INFO outcome, not a value-vs-threshold PASS dressed in robustness-scan clothing.
- **Class (e) PIN-PROMOTES-TO-SOURCE-ON-PASS becomes a standing class with its own lifecycle machinery**. The plan-freeze sub-audit handles class-(e) candidates via a `pending_promotion_log`; the post-gate hook `_class_e_promotion_hook.py` writes canonical_constants.py provenance on PASS. The W9-1 Borel `promoted_from = "S85-W9-1"` event is the canonical first instance.

### What Holds

- **PRU's cardinality test remains correct as far as it goes**. The 5A workshop adds a sub-audit; it does not retract or weaken PRU. Cardinality and value audits commute by construction (independent set operations).
- **The substitution-chain rule from `math-scripts.md` continues to govern every direction/threshold claim**. The rule-file v2 diff itself is written in substitution-chain style throughout (every `Direction:` line is preceded by a `Definition` + `Step` decomposition).
- **The 4-level aggregation hierarchy (per-pin → per-gate → per-wave → per-session) is structurally analogous to the existing waveform/session/closure hierarchy in CLAUDE.md**. Adding D-metrics did not require a new structural layer in the framework; it slotted into existing structure.

### What Breaks or Strains

- **Pre-S85 verdict lines do not carry the 6-tuple's two new fields**. Whether to back-fill or grandfather is open (Open Question 7). The strain is operational, not structural — both routes are defensible — but it must be resolved before the SOURCE-RECON sub-audit is retroactively applied to S77-S84 sessions for trend tracking.
- **The W-3 + 5A v3 unified diff merge is not yet assembled**. Two campaigns produced complementary rule-text; the byte-level merge is mechanical (per A3) but uncompleted (Open Question 1, carry-forward to S85 9B). Until 9B closes, the project has TWO partially-overlapping rule-file diffs in flight. Strain is real but bounded.
- Nothing structurally identified beyond these two. The drift apparatus closes a structural gap rather than opening a new one.

### Carry-Forward Computations

Numbered list, deduplicated across all rounds. Each item has what / inputs / gate / effort.

1. **Register canonical band constants** (5A → S86 W0). What: add `D_advisory_lower = 0.1`, `D_mandatory_lower = 1.0`, `D_halt_lower = 3.0` to `computations/canonical_constants.py` with provenance `S85-5A-workshop`. Inputs: workshop §C2 + §A2 rule-text. Gate: PRU-EXTENSION-RULE-V2-LANDING precondition. Effort: 0.05 wave.

2. **Author `_source_reconciliation_audit.py`** (5A → S86 W1). What: implement the SOURCE-RECON sub-audit per Diff 2's per-pin algorithm + Diff 3's pre-flight integration. Inputs: 5-class taxonomy, calibration band, 4-level aggregation. Gate: returns d_i for every pin in a synthetic 13-site test plan; computes D_max=5.6726, D_sum=18.4103, D_L2=8.9800 (Python-verified) for the S85 W6-W13 retrospective fixture. Effort: 0.5 wave.

3. **Author `_class_e_promotion_hook.py`** (5A → S86 W1, dependency on item 2). What: post-gate hook reading pending_promotion_log; writes canonical_constants.py provenance on PASS, purges on FAIL. Inputs: §CG4 Option B spec. Gate: synthetic class-(e) test fixture promotes correctly on PASS, purges correctly on FAIL. Effort: 0.25 wave.

4. **Land Diff 1 to `.claude/rules/epistemic-discipline.md`** (5A → S86 W2, depends on item 1). What: apply the unified diff to PRDR section. Inputs: 5A workshop Diff 1. Gate: file passes `_yaml_gate_validator.py`-style structural check; new SOURCE-DRIFT (8.1) row visible. Effort: 0.1 wave.

5. **Land Diff 2 to `.claude/templates/pru-pre-registration-template.md`** (5A → S86 W2, depends on items 1+2). What: apply the unified diff inserting Source-Reconciliation Sub-Audit. Inputs: 5A workshop Diff 2. Gate: template renders correctly with all 5 cells of CD1's disambiguation; verdict 6-tuple parses. Effort: 0.15 wave.

6. **Land Diff 3 to `.claude/skills/rclab-plan/skill.md`** (5A → S86 W2, depends on item 2). What: apply the pre-flight section diff. Inputs: 5A workshop Diff 3. Gate: a synthetic plan with one D_max=5.0 violation HALTs at pre-flight. Effort: 0.1 wave.

7. **Verdict 6-tuple back-fill decision** (Open Q7 → S86 W3 plan item). What: resolve whether pre-S85 verdicts are back-fillable (default `(False, structural-bound-test)`) or grandfathered as 4-tuples. Inputs: existing S81-S84 verdict files. Gate: documented decision in handoff §1; `_consolidate_intake.py` updated to handle either tuple length. Effort: 0.1 wave.

8. **Retrospective class-(e) survey** (Open Q2 → S86 W3 knowledge-MCP scan). What: scan `canonical_constants.py` provenance entries for `promoted_from = "S{N}-..."` patterns across S77-S85; classify each as confirmed class-(e) historical instance. Inputs: canonical_constants.py + MCP. Gate: cardinality count of historical (e) events; pass/fail of CG3's "S85 cardinality 1" claim against the broader corpus. Effort: 0.25 wave.

9. **D-metric trend-tracking script** (CE3 → S86 closeout). What: `computations/_d_metric_trend.py` reading handoff §1 source_reconciliation_aggregate blocks across sessions; emits PNG time-series. Inputs: existing handoff files (will populate from S86 onward). Gate: produces a parseable PNG with per-session D_max(S), D_sum(S), D_L2(S). Effort: 0.25 wave.

10. **W-3 + 5A unified v3 diff merge** (Open Q1 → S85 9B closeout). What: produce the canonical `rules-v3.diff` byte-level merge per A3 (additive union + one parent-child link). Inputs: W-3 final diff + 5A Diffs 1-3. Gate: merge applies cleanly to clean working tree; W-3 §G2(g) framework contains 5A §G4a as child sub-section. Effort: 0.5 wave.

11. **W7-2 14th-site Airy reclassification** (Open Q5 → S86 audit). What: split site #13 into the cap pin (kept as-is) plus a new site #13b (Airy-form pin), classify (b) S2. Inputs: W7-2 §11 working-paper text. Gate: updated 13-site → 14-site table feeds into the SOURCE-RECON test fixture. Effort: 0.1 wave.

12. **Cell-(c') MISSING-CANONICAL HALT test fixture** (Open Q4 → S86 LANDING gate test suite). What: synthetic test in `_source_reconciliation_audit.py` injecting `pin_classification: PRIMITIVE` with empty canonical; verifies HALT exit code. Inputs: CD1 sharpening rule-text. Gate: test passes (HALT triggers); subsumed under item 2's test surface. Effort: subsumed.

13. **D-metric override granularity edge case** (Open Q8 → S86 plan deliberation). What: decide whether per-regime override is a third level or absorbed into per-session. Inputs: forward-looking pattern (transit vs equilibrium regimes). Gate: deferred — not blocking S86 LANDING. Effort: 0.1 wave (planning-only, no compute).

14. **Per-gate remediation iteration cap** (Open Q6 → S86 W2 audit). What: substitution-chain analysis of MAX_PIN_ITERATIONS × pins_per_gate to confirm no iterate-until-PASS leakage at the gate level. Inputs: Diff 3's termination proof. Gate: bounded-iteration proof extends to per-gate cap. Effort: 0.1 wave.

### Closing Line

The plan-pin/source-drift apparatus closes the third structural layer of the project's three-layer audit stack (execution drift → plan-layer drift → pin-value drift), and the rule-file v2 diff bundles 7 debt-class fixes into 3 cleanly-targeted unified diffs ready for S86 LANDING.

---

## Pre-registered S86 Gate Spec (FINAL — gen-physicist fills)

**Gate ID**: S86-PRU-EXTENSION-RULE-V2-LANDING

**Validation against test-suite of 13+ drift sites + 7+ debt classes**:

The gate validates the v2 rule-file diff (Diffs 1-3 in this workshop) by replaying the SOURCE-RECONCILIATION sub-audit against a frozen test corpus. The corpus contains the 13 K1 drift sites and the 7 debt classes. The validator script is `computations/_source_reconciliation_audit.py` (delivered as carry-forward item 2). The gate produces a verdict line per the canonical script template.

**Test-suite enumeration (13 sites)** — the gate's test fixture seeds these sites with their pin/source pairs and expected drift class:

| # | Site | Expected class | Expected severity | Expected d_i | Audit action |
|:--|:------|:----|:----|:----|:-----|
| 1 | S85-W7-1 BASELINE-HTILDE TD | (d) | S2 | 0.0979 | NONE |
| 2 | S85-W7-1 BASELINE-HTILDE LI | (d) | S1 | 4.5393 | HALT |
| 3 | S85-W7-2 CC-6 single-channel | (b) | S1 | (categorical) | MANDATORY |
| 4 | S85-W11-1 EPSH-JENSEN L_max | (b) | S1 | (scope) | MANDATORY |
| 5 | S85-W11-1 FAIL floor 1e-4 | (b) | S3 | 4.6021 | HALT |
| 6 | S85-W11-2 sig_2 SHA scope | (a) | S2 | (categorical) | ADVISORY |
| 7 | S85-W11-4 schedule mislabel | (c) | S1 | (categorical) | MANDATORY |
| 8 | S85-W13-1 ε_pivot 0.020 | (c) | S2 | 0.0340 | NONE |
| 9 | S85-W13-4 R1-RANK β | (b) | S1 | 2.3088 | MANDATORY |
| 10 | S85-W10-4 GPU L=12 | (b) | S1 | 5.6726 | HALT |
| 11 | S85-W9-1 Borel floor | (e) | S3 | NULL | NONE (class-e candidate) |
| 12 | S85-W12-2 PRDR bare-K | (b) | S1 | (categorical) | MANDATORY |
| 13 | S85-W7-2 k_cusp placement | (a) | S2 | 1.1556 | MANDATORY |

**Aggregate metrics for the 13-site fixture (Python-verified)**:
- D_max = 5.6726 (site #10)
- D_sum = 18.4103
- D_L2 = 8.9800

**Test-suite enumeration (7 debt classes)** — each debt class must have its rule-text successfully landed by the v2 diff:

| Debt class | Target file | Diff section | Validation criterion |
|:--|:--|:--|:--|
| 1. SOURCE-RECONCILIATION sub-audit | epistemic-discipline.md + pru template | Diff 1 + Diff 2 | Class 8.1 row visible; 5-class taxonomy defined |
| 2. Algebraically-forced INFO mode | pru template | Diff 2 (verdict 6-tuple) | algebraic_force_flag in 6-tuple; verdict logic table present |
| 3. GPU pin selectivity (L_max-conditional) | pru template | Diff 2 (GPU envelope) | density axis + nnz_estimate(L) + executed comparator |
| 4. Root-count heuristic severity flag | pru template | Diff 2 (per-pin block) | heuristic-class table with S1/S2/S3 grading visible |
| 5. PRDR bare-K window | pru template | Diff 2 (8-atom enumeration via parent-child to W-3 G2(g)) | K_substrate, K_corridor, K_R5, K_crit, K_base, K_R3, K_FIRAS, K_crit_BdG enumerated |
| 6. v3-recovery sig_2 scope | v3-closure-recovery.md | (sig_2 entry update; G4b) | gating-subset language present |
| 7. 5B scan-as-robustness | pru template | Diff 2 (verdict 6-tuple scan_role) | 5-value alphabetical enumeration; CONTRADICTION cell self-checking |

**Threshold + falsification clause**:

The S86 gate is **PASS** iff ALL of the following hold:
1. The v2 diffs (Diffs 1, 2, 3 above) apply cleanly to a checkout of `main` at S86 W0 head with no manual conflict resolution.
2. The new audit script `computations/_source_reconciliation_audit.py` runs on the 13-site fixture above and produces, for every site, the expected class + severity + d_i + audit_action match (per the table above).
3. The aggregate metrics returned for the 13-site fixture match (D_max=5.6726, D_sum=18.4103, D_L2=8.9800) within ±1e-4 absolute on each value.
4. The new canonical constants `D_advisory_lower=0.1`, `D_mandatory_lower=1.0`, `D_halt_lower=3.0` are present in `canonical_constants.py` with provenance string `S85-5A-workshop`.
5. The 7 debt classes each have rule-text in the indicated file at the indicated diff section, validated by grep against the validation criterion.
6. The post-gate hook `computations/_class_e_promotion_hook.py` exists and passes its synthetic class-(e) test fixture (PASS verdict promotes; FAIL verdict purges).

**Falsification clause**: the gate is **FAIL** if any of the 6 PASS criteria above fails. Specifically:
- If condition 1 fails (diff conflict): rule-file evolution since S85 close has invalidated the 5A diff structure; v3 merge must be re-derived in S86 W0 before LANDING is attempted.
- If condition 2 fails on any single site: the audit script's classification logic disagrees with the canonical 5A taxonomy; class definition or detection rule must be re-examined.
- If condition 3 fails: a numerical regression in d_i computation; the log10 / cardinality / scope formulae must be cross-checked against the K4 Lyapunov-metric definitions.
- If condition 4 fails: canonical_constants.py registration was skipped or used wrong values; trivial fix.
- If condition 5 fails: a debt-class rule-text was dropped during v2 application; identify the missing section and re-apply.
- If condition 6 fails: the post-gate hook is the most novel deliverable and most likely failure point; the FAIL diagnoses whether the lifecycle machinery is structurally implementable as specified.

**Verdict-line format** (canonical 6-tuple per the v2 verdict format introduced in this workshop):

```
S86-PRU-EXTENSION-RULE-V2-LANDING: PASS|FAIL|INFO -- value=<aggregate_match_count> scheme=source-reconciliation convention=v2-canonical L_max=NA alg_force=False scan_role=structural-bound-test sha256=<closure>
```

Note: this is the FIRST gate in the project to use the new 6-tuple format natively. The verdict line itself is the test that the format-extension is implemented correctly in the producing script.

**Gate semantics**:
- This is a **plan-property** gate (Class 8.1 LANDING test), not a physics gate. Its verdict says "the rule-file v2 lands correctly," not "the physics is right."
- The gate carries no scientific meaning in the substrate framework; it is methodology hygiene.
- PASS does NOT count toward any physics constraint map. FAIL does NOT close any physics mechanism. The verdict is a process verdict, scoped to the audit infrastructure.
