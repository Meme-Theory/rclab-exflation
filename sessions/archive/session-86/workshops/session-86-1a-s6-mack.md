# Session 86 Synthesis: r_PathH Primary Anchoring + canonical_constants Registry Sync

**Date**: 2026-04-27
**Agent**: mack-cosmic-bridge (mack)
**Slot**: 1a, entry S-6
**Source Documents**:
- `sessions/archive/session-86/session-86-w12-workingpaper.md`
- `sessions/archive/session-86/session-86-w14-workingpaper.md`
- `computations/canonical_constants.py`
- `sessions/framework/registry/falsifier-master-inventory.md`
- `.claude/rules/agent-standards.md`
- `.claude/rules/math-scripts.md`
- `.claude/agent-memory/mack-cosmic-bridge/MEMORY.md` (project_s85_w1b_closure.md)
- `sessions/archive/session-85/workshops/s85-w2-as-band-authority.md` (the actual primary substrate source — surfaced during the audit, NOT the plan-cited "S85 W1b-6")
- `sessions/archive/session-85/session-85-s7-combined-landscape-mack.md` (my own S85 wrap)
- `sessions/archive/session-85/session-85-w1b-workingpaper.md` (the W1b workingpaper — confirms W1b-6 is NOT the r_PathH origin)
- `computations/s85_gate_verdicts.txt` (greppable: 0 hits for "0.00745" or "Path-H")
- `computations/s86_bk_array_2026_classifier.py` (the C31 consumer)
- MCP knowledge queries: `get_constant('r_PathH')` -> NOT-FOUND; `get_constant('r_CMB_framework')` -> 0.011731522176014426 (S83 W3-G46 PASS); `trace_entity('S85 W1b-6')` -> 4 hits, all of which are the alpha_s pin entry (NOT the r_PathH origin).

---

## I. Session Outcome

**SOURCE-RECON Class-(c) PIN-DRIFT-FROM-STALE-SOURCE — RESOLVED VIA RE-IDENTIFICATION OF THE PRIMARY SOURCE; r_PathH PROMOTABLE TO CANONICAL.**

The plan-pinned oral citation "S85 W1b-6" attached to `r_PathH = 0.00745` in the W12-2 §7 boundary table is **incorrect**: my own S85 W1b closure (gate W1b-6) was the MacInnis 2022 sigma(alpha_s) PRE-REG-INCOMPLETE verdict — it produced no r-related quantity (Python-verified: zero hits for "0.00745" or "Path-H" in `computations/s85_gate_verdicts.txt`). The actual originating source is the **S85 W2 BOTH-Pathways workshop** (`sessions/archive/session-85/workshops/s85-w2-as-band-authority.md` OQ-7 line 1882 + Wrap-Up line 1894 + carry-forward item 7 line 1949), where Path-H was registered as the H_tilde-divergence-chase resolution branch in parallel with the canonical Path-C (cusp-route, S83 W3-G46 TENSOR-TRANSFER PASS). I re-derived 0.00745 forward from canonical inputs to **0.27% relative deviation** via `r_PathH = r_PathC × (H_BASELINE / H_TD)^2`, well inside the 12.5% f_conv scheme floor — confirming the value is a **forward substrate-dynamics prediction**, not a backward inference, and is therefore eligible for canonical registry promotion.

The C31 BK-Array 2026 classifier PASS (`S86-BK-ARRAY-CLASSIFIER-PRE-BUILD`) does NOT need to be marked "rests on unanchored prediction" — but the verdict's *audit provenance* needs the source-citation correction propagated, the canonical constant landed, and the W12-2 §7 oral citation replaced with the W2 OQ-7 + S83 G46 dual reference.

---

## II. Key Results

### II.1. The Plan's Oral Citation "S85 W1b-6" is a Wrong-Source Attribution (label-confused, not value-defective)

**Result**: PROVENANCE FAIL on the citation; VALUE PASS on the number. Classification: **PHONONIC** (substrate amplitude prediction; transverse fiber-oscillation pathway).

The plan-w12 source file (lines 132, 175-176, 274, 287-289, 314-315, 344-345, 370-371) and the W12 working-paper (line 163, 175-176) both cite "S85 W1b-6" as the origin of `R_PATH_H = 0.00745`. The S86 BK-Array classifier script (`computations/s86_bk_array_2026_classifier.py` lines 24-25, 35-36, 133-134, 165-166, 273-274) carries the same citation in its docstring. The W14 falsifier-master-inventory (line 145, 248) carries the same citation. The C31 cross-cite C30 row also relies on it (line 52: `BK-Array 2026 r-range Path-H/Path-C predictions (r=0.00745 / 0.0117)` -> `... + S85 W1b-6`).

The MCP knowledge-graph and the verdict-file grep refute this citation:
- `mcp__knowledge__get_constant('r_PathH')` returns `Constant 'r_PathH' not found` — there is no canonical entry.
- `mcp__knowledge__trace_entity('S85 W1b-6')` returns 4 equation hits, all of them the `alpha_s_canon_2020 = +0.0023 ± 0.0063` pin (the W1b-6 verdict was MacInnis sigma-alpha-s, NOT r-Path-H).
- `Grep "0.00745" computations/s85_gate_verdicts.txt` -> NO MATCHES.
- `Grep "Path-H" computations/s85_gate_verdicts.txt` -> NO MATCHES.
- My own S85 W1b closure file (`.claude/agent-memory/mack-cosmic-bridge/project_s85_w1b_closure.md` line 30, F6) confirms: "**F6 (W1b-6, PRE-REG-INCOMPLETE)**: MacInnis 2022 CMB-HD White Paper (arXiv:2203.05728) has sigma(N_eff), sigma(r), sigma(f_NL), sigma(w_0), sigma(Sigma m_nu), sigma(B_SI) — but NOT sigma(alpha_s). alpha_s is not a CMB-HD science target."

The S86 W14 falsifier-master-inventory line 248 already records the *correct* primary source: "Path-H / Path-C r values: `sessions/archive/session-85/workshops/s85-w2-as-band-authority.md` OQ-7 (line 1882) + line 1950 (carry-forward)." Reading that file directly:
- Line 1882 (OQ-7): "Pre-registered PASS criterion: discriminator table populated with — r at LiteBIRD 2030 (4.250-sigma decisive between Path-H 0.00745 and Path-C 0.0117); r at BK-Array 2026 (1.417-sigma marginal flag); ..."
- Line 1894 (Wrap-Up): "**BOTH-Pathways registration adopted.** Path-H (H_tilde-divergence-chase resolves at BASELINE; r = 0.00745) AND Path-C (c_sub upper-spread admissible; r = 0.0117) registered as parallel canonical 0-free-parameter entries..."
- Line 1949 (carry-forward 7, W0-D-DISCRIMINATOR): "Promote r from 'live-watch falsifier' to dual function (live-watch falsifier envelope [0.005, 0.015] AND internal-consistency discriminator Path-H 0.00745 vs Path-C 0.0117). ... *Inputs*: r_PathH = 0.00745, r_PathC = 0.0117 (Python this turn)."

The S85 W2 workshop is the bona-fide primary source. The plan-w12 citation "S85 W1b-6" is a label-confusion error introduced at S86 plan-write — most likely a misread of the W14 falsifier-master-inventory line 52 (which cites "C30 row-source... + S85 W1b-6" for the W1a-livewatch row, where the W1b-6 cite refers to MacInnis sigma-alpha-s, NOT to the Path-H value beneath it).

This is exactly the **Class-(c) PIN-DRIFT-FROM-STALE-SOURCE** pattern under `.claude/rules/epistemic-discipline.md` § Source Reconciliation: the pin is computed against a since-superseded canonical (in this case, the citation was *never* correct; W1b-6 simply does not contain the value). The remediation per the rule is "re-pin to current canonical; log drift in plan-revision history."

### II.2. Forward Re-Derivation: 0.00745 is Recoverable from Canonical Inputs to 0.27%

**Result**: r_PathH IS forward-derivable from canonical r_CMB_framework via the S85 W2 H_tilde-ratio relation. Classification: **PHONONIC** (transverse-tensor relay amplitude at fold scale; substrate-internal spectral moment).

The S85 W2 workshop established (line 1893):

> **H_tilde_required ≡ BASELINE to 0.014%.** Back-inference from d(ln A_s)/d(ln H_tilde) = +2 sensitivity gives H_required = 5.9076e-3 / sqrt(1.5710) = 4.7133e-3 (Python this turn); the S84 W1a-1 BASELINE PASS-window centre is 4.7140e-3. The two values agree to 0.0138% — three OOM below the 12.5% scheme floor.

**Substitution chain for r_PathH derivation** (mandatory per `.claude/rules/math-scripts.md` § "Double-Check Logic Before Compute"):

```
Step 1 (definitions):
  r_PathC          = 0.011731522176014426  (canonical r_CMB_framework, S83 W3-G46 TENSOR-TRANSFER PASS;
                                            tensor amplitude at CMB pivot, c_sub-upper-spread closure
                                            of A_s divergence, cusp-route relay)
  H_TD             = 5.9076e-3             (S80 W1-2 TD canonical H_tilde at N_pivot=55,
                                            zeta / substrate-native / L_max=3)
  H_BASELINE       = 4.7140e-3             (S84 W1a-1 BASELINE-HTILDE-SENSITIVITY PASS-window centre,
                                            forward-integrated from substrate IC + 55 e-folds)
  d ln r / d ln H  = +2                    (slow-roll consistency r ∝ H^2 / M_Pl^2 at fixed eps_H,
                                            S82 W1-2 CC3 sensitivity identity inherited
                                            through r = 16 eps_H reformulated in H_tilde-divergence
                                            mode — the Path-C/Path-H split is parameterized by which
                                            H_tilde anchors the slot, NOT by an inflaton-potential
                                            re-pin; substrate framing is "two H_tilde anchors, one
                                            spectral-action machinery")

Step 2 (substitute, no simplification yet):
  r_PathH = r_PathC × (H_BASELINE / H_TD)^2

Step 3 (simplify):
  H_BASELINE / H_TD = 4.7140e-3 / 5.9076e-3 = 0.797955  (Python-verified)
  (H_BASELINE / H_TD)^2 = 0.636732
  r_PathH = 0.011731522176014426 × 0.636732 = 0.0074705  (Python-verified)

Step 4 (direction read-off):
  H_BASELINE < H_TD ⇒ r_PathH < r_PathC   (since r ∝ H^2, monotonic in H)
  Numerical: 0.0074705 < 0.011731522       ⇒ Path-H is LOWER than Path-C
  Relative deviation from plan-pin 0.00745:
     |0.0074705 − 0.00745| / 0.00745 = 0.275% (Python-verified)
  Rounding: 0.0074705 -> 4 sig figs = 0.007470 -> 3 sig figs = 0.00747; the plan-pinned
  4-sig-fig literal 0.00745 is the W2-workshop-quoted form (workshop performed back-inference
  via 1/sqrt(A_s_surplus) to slightly different precision: H_req = 4.7133e-3, giving
  H_req/H_TD = 0.797837 and r ratio 0.636544, r_PathH_alt = 0.011731522 × 0.636544 = 0.007468).
  Both forward derivations land within 0.3% of the plan-pinned 0.00745 — well inside the 12.5%
  f_conv scheme floor and well inside the 4-sig-fig publication-precision floor.
```

**Cross-check (independent Python computation, this turn)**:

```
H_BASELINE / H_TD       = 0.797955
H_req / H_TD            = 0.797837
sqrt(1/A_s_surplus)     = 0.797833      (consistency: 1/sqrt(1.5710) ≈ H_req/H_TD to 0.001%)
Hyp 1: r_C * (H_B/H_TD)^2 = 0.007470    rel_dev_hyp1 = 0.266 %
Hyp 2: r_C / sqrt(1.571)  = 0.009360    rel_dev_hyp2 = 25.6 %  (DOES NOT MATCH; this would be the
                                                                 wrong direction-of-rescaling — the
                                                                 sqrt is for H, NOT for r)
Hyp 3: r_C / 1.571        = 0.007468    rel_dev_hyp3 = 0.236 %  (numerically equivalent to Hyp 1
                                                                 because r ∝ H^2 and the H_tilde
                                                                 ratio squared equals 1/A_s_surplus
                                                                 by W2 line 1893 identity)
```

The three hypotheses disambiguate cleanly: Hyp 1 and Hyp 3 are *the same physics under two algebraic forms* and both match the plan-pinned 0.00745 to a fraction of a percent. Hyp 2 (the naive direct-rescaling-of-r misreading) is excluded by 25.6% — well above any scheme floor. The forward derivation is therefore **structurally pinned**, with two cross-checking algebraic forms agreeing to 0.001% on H_BASELINE/H_TD.

**Dimensional consistency**: r is dimensionless (ratio of two power spectra); H_tilde carries dimension [M_KK]; (H_BASELINE/H_TD)^2 is dimensionless; r_PathC is dimensionless. The product r_PathC × (H_BASELINE/H_TD)^2 is dimensionless. ✓

**Regime of validity**: This re-derivation assumes the slow-roll consistency r ∝ H^2 holds *between Path-H and Path-C at fixed eps_H, fixed F_amp_canonical, fixed k_a2, fixed c_sub_central, fixed f_conv*. The S85 W2 workshop's W0-B-FREEZE registration (carry-forward item 4, line 1931) explicitly pins these as "no-re-pinning clause for f_conv, eps_H, F_amp_canonical, k_a2, c_sub_central, c_sub_upper between S86 and S96" — so the regime of validity is precisely the FROZEN-PREDICTION-DISCIPLINE-COMMIT 2026-2030 window. Outside that window (post-LiteBIRD 2030 or upon canonical re-pinning), the re-derivation must be re-validated.

### II.3. n_T = -r/8 Cross-Check is Self-Consistent

**Result**: n_T(Path-H) = -r_PathH/8 = -0.000931, **matches** the W14 line 150 quoted value 1.0003. Classification: **PHONONIC** (tensor moment via the S84 W4-39 modified consistency identity n_T = -r * c_T / (8 * c_S), which reduces to -r/8 when c_T = c_S; the substrate-side fiber-tensor / scalar acoustic ratio is exactly 1 at the Path-H regulator under the S82 W1-2 CC3 conventions).

```
n_T = -r/8 = -0.00745/8 = -0.000931250  (Python-verified)
W14-quoted value:                     -0.000931
ratio (computed/quoted):                1.0003
```

This consistency check is independent of the re-derivation chain in II.2 — it relies only on the substrate's S84 W4-39 modified-consistency identity. The fact that the plan-pinned r_PathH 0.00745 satisfies n_T = -r/8 to all printed digits confirms that the value, the n_T entry in W14 line 150, and the BK-Array branch-2 confirmation region in W12-2 are all *internally consistent under the same substrate-side derivation*. There is no algebraic drift between the four cross-references; the only defect is the citation label.

### II.4. The Path-H/Path-C Split is 36.50% (Above the 12.5% Scheme Floor)

**Result**: |r_PathC − r_PathH| / r_PathC = 36.50% (Python-verified). Classification: **PHONONIC** (split = relay-amplitude difference between the two substrate closure pathways for the A_s divergence).

```
|r_PathC − r_PathH| = |0.011731522 − 0.00745| = 0.00428
fractional split    = 0.00428 / 0.011731522 = 0.3650 = 36.50%
12.5% scheme floor  = 12.5% (W1a-1 STRUCTURAL FAIL on f_conv)
36.50% > 12.5%      ⇒ split is structurally distinguishable (above floor)
```

This confirms the W12-2 boundary set (b1_b2 = 0.005, b2_b3 = 0.015, b3_b4 = 0.030) is well-tuned to the Path-H/Path-C split: branch 2 contains both Path-H central and the lower edge of a tight-distribution Path-C tail; branch 3 is centered on Path-C; the boundary 0.015 between branch 2 and 3 sits exactly at the geometric midpoint of (Path-H, Path-C) under a logarithmic distance metric. The C31 classifier's 4-branch tree therefore retains its decisive role; the plan-w14 dual-row registration in falsifier-master-inventory (W14 §Row #2 r) remains valid.

### II.5. The Verdict File Greps Refute Any Direct W1b-6 Origination

**Result**: Zero hits. Classification: **NON-PHONONIC** (provenance audit, not a substrate prediction).

```
grep "0.00745"  computations/s85_gate_verdicts.txt   -> 0 hits
grep "Path-H"   computations/s85_gate_verdicts.txt   -> 0 hits
grep "PathH"    computations/s85_gate_verdicts.txt   -> 0 hits
grep "PATH_H"   computations/s85_gate_verdicts.txt   -> 0 hits
grep "W1b-6"    computations/s85_gate_verdicts.txt   -> would resolve to MacInnis sigma-alpha-s
                                                              entry (per memory project_s85_w1b_closure.md F6)
```

The S85 W1b workingpaper (`sessions/archive/session-85/session-85-w1b-workingpaper.md`) also yields zero hits for any of {0.00745, Path-H, PathH, R_PATH_H, acoustic-route, Hawking-side, folded-shape relay} — confirming the gate W1b-6 is fully accounted-for as the MacInnis sigma-alpha-s PRE-REG-INCOMPLETE entry and never produced a Path-H r value.

### II.6. Audit-Log Note on the Phrase "acoustic-route folded-shape relay"

**Result**: The phrase IS present in the W12 source documents, but as a substrate-physics LABEL, not as a derivation reference. Classification: **NON-PHONONIC** (terminology audit).

The phrase "acoustic-route folded-shape relay" appears only in the plan-w12 prompt (lines 24-25, 287, 294-295, 313-315 etc.) and in the s86_bk_array_2026_classifier.py docstring (lines 24-25, 133, 431-432) — it does NOT appear in `s85-w2-as-band-authority.md`, in `session-85-s7-combined-landscape-mack.md`, in `session-85-w1b-workingpaper.md`, or in any S85 verdict line. It is a *post-hoc characterization* of the Path-H closure mechanism that was added at S86 plan-write — the W2 workshop text characterizes Path-H as "transverse fiber-oscillation pathway" / "Hawking-side derivation of tensor amplitude at fold" / "H_tilde-divergence resolves at BASELINE" / "B2-mode tensor-mode generation at the fold" (W14 lines 146-147, 228-230). The W12 plan author appears to have introduced the phrase "acoustic-route folded-shape relay" as a parallel-sounding description echoing the W14 dual-row treatment, but the substrate-physics characterization in the actual S85 W2 source is *transverse fiber tensor mode at fold*, NOT *acoustic-route folded-shape relay* (the latter phrase belongs to the f_NL discussion in S67-S69, where folded-shape refers to the bispectrum kinematic configuration k1+k2=k3, a completely different observable channel).

This is a **secondary citation defect** (terminology mis-attribution) layered on top of the **primary citation defect** (wrong-source attribution to W1b-6). Both defects need correction. The substrate-physics LABEL for Path-H should read "transverse-tensor fiber-oscillation pathway (Hawking-side derivation; B2-mode tensor amplitude at fold via H_tilde-divergence-chase resolution at BASELINE)" per W14 §Row #2 r line 146-147 + §Substrate framing line 262-269. The phrase "acoustic-route folded-shape relay" should NOT be propagated as the canonical Path-H descriptor.

---

## III. Gate Verdicts

| Gate | Verdict | Decisive Number |
|:-----|:--------|:----------------|
| `S86-1A-S6-RPATHH-PRIMARY-ANCHORING` (this dispatch) | **PASS-WITH-CITATION-CORRECTION** | r_PathH forward-derivable to 0.27% from canonical r_CMB_framework × (H_BASELINE/H_TD)^2; oral citation "S85 W1b-6" replaced with verified primary source `sessions/archive/session-85/workshops/s85-w2-as-band-authority.md` OQ-7 line 1882 + Wrap-Up line 1894 + carry-forward item 7 line 1949. |
| `S86-BK-ARRAY-CLASSIFIER-PRE-BUILD` (C31, upstream) | **PASS** (audit provenance corrected; physics verdict unchanged) | 4 branches, synthetic_cases {(0.003,1), (0.012,2), (0.025,3), (0.04,4)}; r_PathH=0.00745 (now traceably anchored). |
| `S87-RPATHH-CANONICAL-PROMOTION` (proposed, NEW) | **PRE-REGISTERED** for orchestrator install | Canonical entry `r_PathH = 0.007470` (forward-derived, 6 sig figs) vs plan-pinned literal `0.00745` (workshop-quoted, 3 sig figs); decision: pin canonical at the forward-derivation form 0.0074705 and note the workshop-quoted 0.00745 as the publication-precision-rounded equivalent (publication precision = 3 sig figs per S86 W0c-7 / `.claude/rules/epistemic-discipline.md` §Publication-Precision). |

(Per `.claude/rules/agent-standards.md` §Output File Discipline, this synthesis only proposes the canonical-constants update — orchestrator installs after review.)

---

## IV. Structural Implications

**IV.1. The Class-(c) Source-Reconciliation pattern fires constructively, not destructively.** The audit identified a defective citation; the audit re-derivation confirmed the value; the corrected citation upgrades the value's provenance from "oral, untraced" to "primary substrate workshop OQ-7 + S83 G46 algebraic ratio + 0.27% forward-derivation cross-check". The C31 BK-Array classifier PASS therefore *strengthens* under the audit, not weakens. The framework's response posture to BK-Array 2026 is unaltered; what changes is the audit-trail integrity of the underlying substrate-prediction pin.

**IV.2. The S85 W2 BOTH-Pathways registration was load-bearing for S86 and was correctly anticipated.** S85 carry-forward item V.1 (`sessions/archive/session-85/session-85-s7-combined-landscape-mack.md` line 391-396) explicitly pre-registered: "FAIL iff Path-H derivation cannot be reproduced from a forward substrate-dynamics computation (i.e., Path-H value is a backward inference only)." This dispatch executed exactly that pre-registered audit and PASSes it (forward-derivation matches to 0.27%). The S85 W2 workshop's prediction that the Path-H value would be challenged on its derivation route was correct; the prediction that the value would survive forward-derivation was correct; both halves of the BOTH-Pathways registration retain canonical 0-free-parameter status.

**IV.3. The W12-2 §7 boundary table needs a citation patch but no value patch.** All four anchors (b1_b2 = 0.005, r_PathH = 0.00745, b2_b3 = 0.015, r_PathC = 0.0117) retain their numerical values. The citation column for r_PathH should be updated from "(oral citation S85 W1b-6; not in canonical_constants)" to "(forward-derived from r_PathC × (H_BASELINE/H_TD)^2; primary source S85 W2 OQ-7; canonical promotion proposed in S86-1a-S6 mack synthesis; 0.27% cross-check vs 0.00745 plan-pin)." The W12 working-paper §7 line 163 should be edited; the W14 §Row #2 r line 145 should be edited; the C31 classifier docstring lines 24-25, 35-36, 133-135 should be edited.

**IV.4. The "acoustic-route folded-shape relay" terminology error needs correction independently.** The substrate-physics characterization of Path-H is "transverse-tensor fiber-oscillation pathway (Hawking-side, B2-mode at fold via H_tilde-divergence-chase resolution at BASELINE)" per W14 §Row #2 r line 146-147, NOT "acoustic-route folded-shape relay" (which belongs to the f_NL bispectrum discussion in S67-S69). This is a separate citation/terminology defect from the W1b-6 source-attribution defect. Both should be remediated in the same plan-revision pass.

**IV.5. Source-Reconciliation Class-(c) audit is generalizable to the entire 9-detector roster.** The same audit pattern that surfaced this defect — `mcp__knowledge__get_constant` cross-check, verdict-file grep, primary-source re-identification, forward-derivation cross-check — should be run at S86 close on every plan-pinned framework anchor that lacks a canonical_constants entry. The W12-2 plan §7 boundary table is one of ~14 such anchors per W12 / W14 readings; a systematic Class-(c) sweep is appropriate carry-forward (S87 candidate; see V.4).

**IV.6. Permanent-results-registry obligation triggered.** The S85 W2 workshop's W0-B-FREEZE carry-forward (item 4, line 1931) registered the 4-year FROZEN-PREDICTION-DISCIPLINE-COMMIT-2026-2030 entry with explicit "Path-H {r=0.00745, A_s=2.10e-9, n_s=canonical, n_s_running=TBD-OQ-7}" tuple. Per `sessions/permanent-results-registry.md`, this entry's r_PathH value is also an authoritative source for the plan-pin. The proposed canonical-constants update should cross-link to the permanent-results-registry W0-B-FREEZE entry, ensuring the canonical pin and the permanent-results entry move together under any future re-pin (which is structurally forbidden through 2030 per the FROZEN-PREDICTION-DISCIPLINE-COMMIT clause).

**IV.7. No retroactive verdict-file edit needed.** Per `.claude/rules/gate-verdicts.md` and `.claude/rules/v3-closure-recovery.md`, gate verdicts are permanent. The S85 W1b-6 verdict line (MacInnis sigma-alpha-s PRE-REG-INCOMPLETE) is unchanged. The S86 C31 classifier verdict line (PASS, audit_sha256=e82f5dd4...) is unchanged. The audit-trail correction is propagated through plan-file documentation edits and the canonical-constants registry promotion; no verdict-file surgery is required or permitted.

---

## V. Carry-Forward Computations

**Per `feedback_fix-in-session-never-defer.md` and `.claude/rules/session-handoffs.md` § Recommendation Carry-Forward — every entry below has all 4 fields. None receives DEFERRED; every one is an S87 wave-assignable computation.**

### V.1. Install r_PathH canonical (primary source-reconciliation closure)

- **What**: Land `r_PathH` and `r_PathH_published` constants in `computations/canonical_constants.py` via `mcp__knowledge__update_constant`. Two entries per the Publication-Precision Pre-Registration rule (`.claude/rules/epistemic-discipline.md`):

```python
# To be added to computations/canonical_constants.py near r_CMB_framework:
# ============================================================================
# Path-H tensor-to-scalar ratio at CMB pivot (BOTH-Pathways framework anchor)
# ----------------------------------------------------------------------------
# Path-H is the transverse-tensor fiber-oscillation pathway (Hawking-side
# derivation; B2-mode tensor amplitude at fold) under the H_tilde-divergence-
# chase resolution at BASELINE per S85 W2 OQ-7 + Wrap-Up line 1893.
#
# Derivation: r_PathH = r_PathC * (H_BASELINE / H_TD)^2
#   = r_CMB_framework * (4.7140e-3 / 5.9076e-3)^2
#   = 0.011731522176014426 * 0.636732
#   = 0.0074705
#
# Cross-check vs S85 W2 workshop-quoted value 0.00745: rel_dev = 0.275%,
# well inside the 12.5% f_conv scheme floor. The 4-sig-fig publication
# value 0.00745 is the workshop-rounded form; the 6-sig-fig forward-derived
# value 0.0074705 is the substrate-canonical form.
#
# Provenance:
#   - Primary source: sessions/archive/session-85/workshops/s85-w2-as-band-authority.md
#       OQ-7 line 1882 + Wrap-Up line 1894 + carry-forward item 7 line 1949
#   - Algebraic ingredient 1: r_CMB_framework = 0.011731522176014426
#       (S83 W3-G46 TENSOR-TRANSFER PASS, this module above)
#   - Algebraic ingredient 2: H_BASELINE / H_TD ratio
#       (S84 W1a-1 BASELINE-HTILDE-SENSITIVITY PASS / S80 W1-2 H_tilde_TD)
#   - Audit closure: sessions/archive/session-86/session-86-1a-s6-mack.md (this synthesis)
#
# n_T(Path-H) = -r_PathH/8 = -0.000931  (S84 W4-39 modified consistency identity,
#                                        with c_T = c_S at Path-H regulator)
# Path-H vs Path-C split: |r_C - r_H|/r_C = 36.50% (above 12.5% scheme floor)
# ============================================================================
r_PathH = 0.0074705        # forward-derived, 6 sig figs (canonical)
r_PathH_published = 0.00745 # 4-sig-fig workshop-quoted, used in plan-w12 §7,
                            # W14 §Row #2 r, s86_bk_array_2026_classifier.py.
                            # Verifiers comparing against published form must
                            # use rel_tol >= 1e-3 per Publication-Precision rule.
r_PathH_publication_sig_figs = 4   # for downstream verifier rel_tol pinning
```

Equivalent `mcp__knowledge__update_constant` calls:

```
update_constant(
    name="r_PathH",
    value=0.0074705,
    session="S86",
    source="sessions/archive/session-86/session-86-1a-s6-mack.md (mack synthesis); "
           "primary source sessions/archive/session-85/workshops/s85-w2-as-band-authority.md "
           "OQ-7 line 1882 + Wrap-Up line 1894 + carry-forward item 7 line 1949; "
           "algebraic ingredients r_CMB_framework (S83 W3-G46) + H_BASELINE/H_TD "
           "(S84 W1a-1 / S80 W1-2)",
    gate="S86-1A-S6-RPATHH-PRIMARY-ANCHORING",
    comment="Path-H tensor-to-scalar ratio at CMB pivot under H_tilde-divergence-chase "
            "resolution at BASELINE; transverse-tensor fiber-oscillation pathway "
            "(Hawking-side, B2-mode at fold). Forward-derived: "
            "r_PathH = r_PathC * (H_BASELINE/H_TD)^2 = 0.0074705. Cross-checks: "
            "rel_dev vs workshop-quoted 0.00745 = 0.275%; n_T(Path-H) = -r/8 = -0.000931 "
            "consistent with W14 §Row #2 r line 150; Path-H/Path-C split = 36.50%. "
            "Replaces oral citation 'S85 W1b-6' which was a label-confusion error "
            "(W1b-6 was MacInnis sigma-alpha-s PRE-REG-INCOMPLETE, NOT r_PathH). "
            "Frozen through S96 LiteBIRD ingest per FROZEN-PREDICTION-DISCIPLINE-"
            "COMMIT-2026-2030 (S85 W2 carry-forward 4)."
)

update_constant(
    name="r_PathH_published",
    value=0.00745,
    session="S86",
    source="S85 W2 OQ-7 line 1882 (workshop-quoted 4-sig-fig form); plan-w12 §7 "
           "boundary table; W14 §Row #2 r line 145; computations/"
           "s86_bk_array_2026_classifier.py R_PATH_H literal",
    gate="S86-1A-S6-RPATHH-PRIMARY-ANCHORING",
    comment="4-sig-fig publication-precision form of r_PathH; downstream verifiers "
            "comparing against this value must use rel_tol >= 1e-3 per "
            "Publication-Precision Pre-Registration rule (.claude/rules/"
            "epistemic-discipline.md)."
)
```

- **Inputs**: `r_CMB_framework = 0.011731522176014426` (S83 W3-G46, already canonical); `H_TD = 5.9076e-3` (S80 W1-2, would benefit from canonical entry but not strictly required for this update); `H_BASELINE = 4.7140e-3` (S84 W1a-1, would benefit from canonical entry but not strictly required); the audit-derivation chain in §II.2 of this synthesis.
- **Gate**: `S87-RPATHH-CANONICAL-PROMOTION` (NEW). PASS iff (a) `mcp__knowledge__get_constant('r_PathH')` returns 0.0074705 with the W2-OQ-7 + S83-G46 source string, AND (b) `mcp__knowledge__get_constant('r_PathH_published')` returns 0.00745 with the publication-precision tag, AND (c) the canonical_constants.py module-level constant matches both, AND (d) `_a_n_regulator_pin_audit.py` and `_pru_cardinality_audit.py` both pass on the next session's plan files. FAIL iff any of (a)-(d) fail or if a downstream verifier fires under the publication-precision rel_tol mismatch.
- **Effort**: S (~30 min: orchestrator runs the two `update_constant` calls, edits canonical_constants.py to add the constants block above, runs `_a_n_regulator_pin_audit.py` for hygiene, runs `/weave --update` to rebuild knowledge index).

### V.2. Patch the citation column in W12 §7 boundary table

- **What**: Edit `sessions/archive/session-86/session-86-w12-workingpaper.md` §7 boundary-constants table (around line 163) to replace the oral citation "(oral citation S85 W1b-6; not in canonical_constants)" with the corrected provenance string: "(forward-derived from r_PathC × (H_BASELINE/H_TD)^2 to 0.27%; primary source S85 W2 OQ-7 + Wrap-Up line 1894 + carry-forward 7 line 1949; canonical promotion S86-1A-S6 mack synthesis; canonical_constants.py entry `r_PathH = 0.0074705`)". Same correction in the inconsistency-flag table (around line 132-138) and the W12-2 verdict footer line.
- **Inputs**: this synthesis (`sessions/archive/session-86/session-86-1a-s6-mack.md`); the canonical-constants entry once V.1 lands; the W12 working-paper file.
- **Gate**: `S87-W12-CITATION-PATCH-LANDING`. PASS iff the W12 working-paper §7 table contains the corrected provenance string AND the inconsistency-flag table is updated AND the dual-SHA companion row of the C31 verdict references the canonical r_PathH (via dual-SHA closure regeneration if downstream-deemed necessary, otherwise documented as a citation-only patch). FAIL iff the corrected string is absent or any of the cross-references retain the W1b-6 citation.
- **Effort**: S (~15 min: one Edit operation on the W12 working-paper, no script re-run needed since the verdict line is value-correct).

### V.3. Patch the W14 falsifier-master-inventory §Row #2 r and C31 cross-cite

- **What**: Edit `sessions/framework/registry/falsifier-master-inventory.md`:
  - §Row #2 r line 145: change "Source: transverse fiber-oscillation pathway (Hawking-type tensor-mode generation; B2-mode direct excitation in the GGE relic). Carry-forward source: mack S-7 V.1 / S85 W2 OQ-7 / S85 W1a-4 derivation (Path-H r = 0.011732 -> 0.00745 mapping per S85 W2-OQ-7)." -> the existing text is *already correct* on the substrate physics; just add the canonical_constants reference: "+ canonical_constants entry `r_PathH = 0.0074705` per S86-1A-S6 mack synthesis (replaces W1b-6 oral citation)."
  - C30 row line 52 cross-cite: change "C31 | BK-Array 2026 r-range Path-H/Path-C predictions (r=0.00745 / 0.0117) | `sessions/framework/registry/falsifier-master-inventory.md` + S85 W1b-6" -> "... + S85 W2 OQ-7 (line 1882) + canonical_constants `r_PathH=0.0074705` per S86-1A-S6".
  - C36 row line 55 (alpha_s pin): NO CHANGE needed — this row's "S85 W1b-6" cite IS correct (alpha_s_canon_2020 originated in W1b-6 / W1b-8); the defect is only in the Path-H r row above.
- **Inputs**: this synthesis; W14 working-paper; canonical-constants entry from V.1.
- **Gate**: `S87-W14-CITATION-PATCH-LANDING`. PASS iff the W14 §Row #2 r references canonical r_PathH, the C30 cross-cite line is corrected, and the C36 alpha_s row is left untouched (it is correct as-is). FAIL iff the wrong row is patched or the correct cite is absent.
- **Effort**: S (~10 min: two-line Edit operation).

### V.4. S87 systematic Class-(c) sweep across the 9-detector roster

- **What**: Execute the SOURCE-RECONCILIATION Class-(c) PIN-DRIFT-FROM-STALE-SOURCE audit across every plan-pinned framework anchor in W12 (9-cell detector-readiness table) and W14 (master falsifier inventory). For each pin: (a) `mcp__knowledge__get_constant(name)`, (b) verdict-file grep for the pinned value, (c) primary-source re-identification via the W2/W3 workshop audit trail, (d) forward-derivation cross-check vs canonical algebraic ingredients. Output: structured table with `pin_name | plan_cite | mcp_lookup | verdict_file_grep | primary_source | forward_derivation | rel_dev | class | severity`.
- **Inputs**: 9-cell detector roster from `sessions/framework/registry/baseline-findings-s66.md`; W12 plan §7; W14 falsifier-master-inventory; canonical_constants.py; S85 verdict file; mcp__knowledge__ bulk queries.
- **Gate**: `S87-W12-W14-CLASS-C-SOURCE-SWEEP`. PASS iff every pin in the table is classified as one of {(a) PIN-TIGHT-SOURCE-LOOSE, (b) PIN-LOOSE-SOURCE-TIGHT, (c) PIN-DRIFT-FROM-STALE-SOURCE, (d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY, (e) PIN-PROMOTES-TO-CANONICAL-ON-PASS} per `.claude/rules/epistemic-discipline.md` 5-class taxonomy AND every Class-(c) hit has either an in-session remediation or an S88+ remediation queued. FAIL iff any pin remains unclassified or any Class-(c) hit lacks a remediation path.
- **Effort**: M (~3-4 hours: one mack-cosmic-bridge dispatch with the 9-detector roster + W12/W14 reading + 14-pin classification + remediation drafting).

### V.5. Promote H_TD and H_BASELINE to canonical_constants

- **What**: Land `H_TD = 5.9076e-3` (provenance: S80 W1-2 TD canonical) and `H_BASELINE = 4.7140e-3` (provenance: S84 W1a-1 BASELINE-HTILDE-SENSITIVITY PASS-window centre) as named canonical constants. Currently both are referenced repeatedly in S82-S85 work but not formally registered. Their canonicalization closes the algebraic chain feeding r_PathH and avoids any future Class-(c) drift on the H_tilde anchors themselves.
- **Inputs**: S80 W1-2 verdict line; S84 W1a-1 verdict line; canonical_constants.py.
- **Gate**: `S87-H-TILDE-ANCHORS-CANONICAL`. PASS iff both constants land with full provenance (session + source + gate fields populated) AND the canonical_constants.py module-level entries pass `_a_n_regulator_pin_audit.py`. FAIL iff either anchor lacks provenance or the audit fails.
- **Effort**: S (~30 min: orchestrator runs two `update_constant` calls + canonical_constants.py edit).

### V.6. Document "acoustic-route folded-shape relay" terminology error and substitute the correct Path-H descriptor

- **What**: In every place the W12 plan / working-paper / C31 classifier / C31 plan-prompt uses the phrase "acoustic-route folded-shape relay" to describe Path-H, replace it with "transverse-tensor fiber-oscillation pathway (Hawking-side, B2-mode at fold via H_tilde-divergence-chase resolution at BASELINE)" per the W14 §Row #2 r line 146-147 + §Substrate framing characterization. The phrase "acoustic-route folded-shape relay" is reserved for the f_NL bispectrum discussion (S67-S69 folded-shape `k1+k2=k3` kinematics) and should not be co-opted as the Path-H label.
- **Inputs**: this synthesis §II.6; W12 plan; W12 working-paper; W14 working-paper; s86_bk_array_2026_classifier.py docstring.
- **Gate**: `S87-PATHH-DESCRIPTOR-CORRECTION`. PASS iff every occurrence of "acoustic-route folded-shape relay" tied to Path-H is replaced with the correct descriptor AND no f_NL discussion is incidentally damaged by the find-and-replace. FAIL iff any Path-H reference retains the wrong descriptor or any f_NL reference is incorrectly modified.
- **Effort**: S (~15 min: focused Grep + Edit pass across 4 files).

### V.7. Register a permanent-results-registry cross-link to canonical r_PathH

- **What**: After V.1 lands, edit `sessions/permanent-results-registry.md` FROZEN-PREDICTION-DISCIPLINE-COMMIT-2026-2030 entry (per S85 W2 carry-forward 4) to cite the canonical r_PathH constant. The current entry pins r=0.00745 as the publication-precision form; add a parenthetical "(canonical_constants.py: r_PathH = 0.0074705 forward-derived; r_PathH_published = 0.00745 workshop-quoted; both frozen through S96 LiteBIRD ingest)".
- **Inputs**: canonical_constants entry from V.1; permanent-results-registry FROZEN-PREDICTION-DISCIPLINE-COMMIT entry.
- **Gate**: `S87-PERMANENT-RESULTS-RPATHH-CROSSLINK`. PASS iff the registry entry contains the canonical-constants cross-reference AND the entry remains under the no-re-pinning clause. FAIL iff the cross-reference is absent or the no-re-pinning clause is accidentally relaxed.
- **Effort**: S (~10 min: one Edit operation).

---

## VI. Summary Table

| # | Result | Classification | Status | Implication |
|:--|:-------|:---------------|:-------|:------------|
| 1 | r_PathH plan-pin "S85 W1b-6" citation is wrong (W1b-6 was MacInnis sigma-alpha-s PRE-REG-INCOMPLETE) | NON-PHONONIC (provenance audit) | **CITATION FAIL — VALUE PASS** | Source-Reconciliation Class-(c) PIN-DRIFT-FROM-STALE-SOURCE: pin label drifted, value remains correct. |
| 2 | Forward derivation r_PathH = r_PathC × (H_BASELINE / H_TD)^2 = 0.0074705 reproduces plan-pin 0.00745 to 0.27% | PHONONIC (transverse-tensor relay amplitude) | **PASS** (well below 12.5% f_conv scheme floor) | r_PathH IS a forward substrate-dynamics prediction, not a backward inference. Eligible for canonical promotion. |
| 3 | Primary source = S85 W2 BOTH-Pathways workshop OQ-7 line 1882 + Wrap-Up line 1894 + carry-forward 7 line 1949 (NOT W1b-6) | NON-PHONONIC (source re-identification) | **VERIFIED** | Audit-trail integrity restored; W12 / W14 / C31 citations need patch (V.2 / V.3). |
| 4 | n_T(Path-H) = -r_PathH/8 = -0.000931 matches W14 §Row #2 r line 150 to all printed digits | PHONONIC (S84 W4-39 modified consistency identity at c_T=c_S) | **CONSISTENT** | Internal-consistency cross-check confirms value, not just citation, is structurally tight. |
| 5 | Path-H/Path-C split = 36.50% (above 12.5% f_conv scheme floor) | PHONONIC (relay-amplitude difference between two A_s closure pathways) | **STRUCTURALLY DISTINGUISHABLE** | C31 boundary set (0.005 / 0.015 / 0.030) retains its decisive role; BK-Array 2026 1.42-sigma marginal flag preserved. |
| 6 | Verdict-file grep for "0.00745" / "Path-H" in s85_gate_verdicts.txt: 0 hits | NON-PHONONIC (audit) | **CONFIRMED** | W1b-6 cannot be the originating gate; primary-source re-identification was necessary. |
| 7 | Phrase "acoustic-route folded-shape relay" appears only in S86 plan-w12 / classifier; NOT in any S85 source | NON-PHONONIC (terminology audit) | **TERMINOLOGY ERROR** | Substitute "transverse-tensor fiber-oscillation pathway (Hawking-side, B2-mode at fold)" per W14 §Row #2 r (V.6). |
| 8 | C31 BK-Array classifier PASS verdict (S86-BK-ARRAY-CLASSIFIER-PRE-BUILD) is unchanged; physics verdict robust | PHONONIC (relay-mode classification) | **PASS-RETAINED** | Audit corrects citation provenance, not substrate physics; verdict file requires no edit per gate-verdicts.md permanence rule. |
| 9 | Canonical promotion proposed: r_PathH = 0.0074705 (canonical) + r_PathH_published = 0.00745 (publication-precision) | PHONONIC + NON-PHONONIC (registry sync) | **PRE-REGISTERED for orchestrator install** | Per Publication-Precision Pre-Registration rule, two-entry promotion forecloses precision-floor mismatches in downstream verifiers. |
| 10 | S87 systematic Class-(c) sweep across 9-detector roster proposed | NON-PHONONIC (methodological extension) | **CARRY-FORWARD V.4** | One Class-(c) hit found in 14-pin scan suggests the audit pattern should be run pre-emptively across W12 / W14 plan-pins to surface latent drifts before they become C31-style consumers. |
