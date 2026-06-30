#!/usr/bin/env python3
"""One-shot Python writer for §W13-5 working-paper section.
Per registry-write hygiene rule (.claude/rules/epistemic-discipline.md
S86 W1c surface): use append-only / one-shot Python writers to avoid
Edit-tool mtime race when other agents are writing to the same file.
"""
from pathlib import Path

WP = Path("sessions/archive/session-86/session-86-w13-workingpaper.md")

OLD = """### §W13-5. S86-ALPHA-S-CANONICAL-UPDATE (mack-cosmic-bridge)

**Status**: NOT STARTED
**Gate ID**: `S86-ALPHA-S-CANONICAL-UPDATE`
**Trigger**: `[VERIFY]` + `[SIGN]`
**Classification**: **PHONONIC** (α_s IS running of GGE-acoustic spectral tilt — second derivative of GGE quasiparticle dispersion at pivot scale)
**Agent**: `mack-cosmic-bridge` (canonical-constants edit + 2 re-emissions; not adjudication of own work)
**Hypothesis**: Updating `canonical_constants.py` from `planck_alpha_s=-0.0045 ± 0.0067` (Planck 2018) to `alpha_s_canon_2020=+0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck) per W1b-8 FAIL produces a self-consistent additive pin AND both re-emissions (S85 W1a-9 7D Fisher + S85 W1b-3 σ_corr/σ_diag) emit non-error verdict lines under the new pin; framework prediction (-0.068968) is UNCHANGED, only canon moves.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-5.

**MCP Pre-Compute Audit**:
*(pending — list the `mcp__knowledge__*` queries executed before writing the script, with one-line salient return each; mark PRE-CLOSED if a closure covers the gate. Per `.claude/rules/knowledge-index-usage.md`.)*

**Verdict**:
*(pending agent execution)*

**Results**:
*(pending — include: alpha_s_canon_2020=+0.0023 pin landed + legacy retained, 4-tuple (scheme=Aiola-2020-ACT-DR4-Planck, convention=additive-edit, L_max=N/A), substitution chain per §10 with substituted numbers (Δ(central)=+0.0068, gap_old=+0.064468, gap_new=+0.071268, n_σ_old=9.622, n_σ_new=11.312, Δ(n_σ)=+1.690), W1a-9 + W1b-3 re-emission verdict lines (`S85-W1a-9-RE-EMIT-S86-W13-P12` + `S85-W1b-3-RE-EMIT-S86-W13-P12`), tension-widening INFO sub-tag, dual-SHA, artifacts `s86_w13_p12_alpha_s_canonical_update.py/.json` + `s86_w13_p12_re_emit_w1a_9.json` + `s86_w13_p12_re_emit_w1b_3.json` + modified `canonical_constants.py`)*"""

NEW = """### §W13-5. S86-ALPHA-S-CANONICAL-UPDATE (mack-cosmic-bridge)

**Status**: **CLOSED**
**Gate ID**: `S86-W13-P12-ALPHA-S-CANONICAL-UPDATE`
**Trigger**: `[VERIFY]` + `[SIGN]`
**Classification**: **PHONONIC** (α_s IS running of GGE-acoustic spectral tilt — second derivative of GGE quasiparticle dispersion at pivot scale; the framework prediction `α_s = n_s^2 - 1 = -0.068968` derives from S50-51 substrate-eigenvalue identity, not data fitting)
**Agent**: `mack-cosmic-bridge` (canonical-constants edit + 2 re-emissions; self-execution permitted because edit is mechanical and re-emission is gate-numerics-preserving — not adjudication of own work)
**Hypothesis**: Updating `canonical_constants.py` from `planck_alpha_s=-0.0045 ± 0.0067` (Planck 2018) to `alpha_s_canon_2020=+0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck) per S85 W1b-8 FAIL produces a self-consistent additive pin AND both re-emissions (S85 W1a-9 7D Fisher + S85 W1b-3 σ_corr/σ_diag) emit non-error verdict lines under the new pin; framework prediction (-0.068968) is UNCHANGED, only canon moves.
**Plan reference**: `sessions/session-plan/session-86-plan-w13.md` §W13-5 (lines 700-911).

**MCP Pre-Compute Audit**:
- `list_constants(pattern="alpha_s")` → 7 matches; confirmed baseline `planck_alpha_s = -0.0045`, `planck_alpha_s_err = 0.0067`, `alpha_s_inflation_framework = -0.068968` (from `n_s_canon**2 - 1`).
- `search_knowledge("alpha_s ACT DR4 Aiola 2020")` → 10 hits; documents W1b-8 recommended pin update `alpha_s_canon_2020 = +0.0023 ± 0.0063` from Aiola+ 2020 Table 5 col 3.
- `trace_entity("S85-W1b-8")`, `trace_entity("S85-W1a-9")`, `trace_entity("S85-W1b-3")` → no traces (gates not yet entity-promoted in knowledge index; identified instead via direct file grep on `s85_gate_verdicts.txt`: baseline lines `S85-W1a-MULTID-FISHER-FRAMEWORK: PASS value=827.9255704800152` and `S85-W1b-ALPHA-S-JOINT-FISHER-CORRELATED: PASS value=1.1297479814965643`).
- No PRE-CLOSED closure covers this gate; the canonical-pin update + re-emission pattern is the registered W1b-8-remediation path per plan §W13-5.5.

**Verdict**: **PASS** (P12 + both re-emissions PASS).

Verdict lines on disk (`computations/session-86/s86_gate_verdicts.txt` lines 211-216 — see also lines 205-210 for the precision-floor first-attempt FAIL retained for audit transparency per S86 W1c-5 all-3-lines-retained discipline):

```
S86-W13-P12-ALPHA-S-CANONICAL-UPDATE: PASS -- value=0.0023 scheme=Aiola-2020-ACT-DR4-Planck convention=additive-edit L_max=N/A audit_sha256=d8b259b33eac2792a32f16b6818dcee03e6541786d374e62a63a81703c83d216 content_sha256=cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497 schema_version=S84+
S85-W1a-9-RE-EMIT-S86-W13-P12: PASS -- value=827.9255704800152 scheme=7D-Fisher convention=block-diagonal-correlation L_max=10 audit_sha256=41da50b65fea7b5a18d9ef1ed622a73a68eeb27876baeb0d051b4d76cdbbfa01 content_sha256=cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497 schema_version=S84+
S85-W1b-3-RE-EMIT-S86-W13-P12: PASS -- value=1.1297479814965643 scheme=Fisher-marg-Gauss convention=block-diag-C L_max=n/a audit_sha256=a670ab3e287c554787162bcc363b3388d3d5272b09458c760b2a830c227107dd content_sha256=cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497 schema_version=S84+
```

**Results**:

**(1) Canonical-constants pin update (additive; legacy retained)**

`computations/_shared/canonical_constants.py` modified additively at lines 1221-1240 (post-edit):

```python
# LEGACY (retained, marked superseded; back-compat preserved):
planck_alpha_s = -0.0045       # LEGACY Planck-2018 pin; superseded by alpha_s_canon_2020 per S86-W13 P12. Use alpha_s_canon_2020 for new computation scripts.
planck_alpha_s_err = 0.0067    # LEGACY Planck-2018 1-sigma on alpha_s.

# NEW (S86 W13 P12; Aiola+ 2020 ACT DR4 + Planck combined):
alpha_s_canon_2020 = +0.0023        # ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin
alpha_s_canon_2020_err = 0.0063     # Aiola+ 2020 1-sigma on alpha_s
alpha_s_canon_2020_source = "Aiola+ 2020 (ACT DR4 + Planck combined)"
alpha_s_canon_2020_session = "S86 W13 P12"
```

Both `from canonical_constants import planck_alpha_s` (legacy) and `from canonical_constants import alpha_s_canon_2020` (new) succeed — back-compat preserved per plan §W13-5.6 ADDITIVE EDIT DISCIPLINE.

Framework prediction `alpha_s_inflation_framework = n_s_canon**2 - 1 = -0.068967990` (full float64) **UNCHANGED** — derives from substrate-eigenvalue identity (S50-51), not from data fitting.

**(2) 4-tuple (P12)**

```
(value=alpha_s_canon_2020=+0.0023, scheme=Aiola-2020-ACT-DR4-Planck, convention=additive-edit, L_max=N/A)
```

**(3) [SIGN] Substitution chain (Python-verified; matches plan §10 exactly)**

```
Step 1 — Definitions:
  α_s^old   = -0.0045    (planck_alpha_s, Planck 2018 central)
  σ^old     =  0.0067    (planck_alpha_s_err, Planck 2018 1-σ)
  α_s^new   = +0.0023    (alpha_s_canon_2020, Aiola 2020 ACT DR4 + Planck central)
  σ^new     =  0.0063    (alpha_s_canon_2020_err, Aiola 2020 1-σ)
  α_s^FW    = -0.068968  (alpha_s_inflation_framework, UNCHANGED across this gate)
  gap(X)    = α_s^X - α_s^FW           (signed; canon central minus framework)
  n_σ(X)    = |gap(X)| / σ^X           (1-D Gaussian-equivalent tension)

Step 2 — Substitute (Python-verified):
  Δ(central)  = α_s^new − α_s^old
              = (+0.0023) − (−0.0045)
              = +0.006800

  gap_old     = α_s^old − α_s^FW
              = (−0.0045) − (−0.068968)
              = +0.064468

  gap_new     = α_s^new − α_s^FW
              = (+0.0023) − (−0.068968)
              = +0.071268

  Δ(gap)      = gap_new − gap_old
              = (+0.071268) − (+0.064468)
              = +0.006800

Step 3 — Simplify:
  n_σ_old    = |gap_old| / σ^old
             = 0.064468 / 0.0067
             = 9.622 σ

  n_σ_new    = |gap_new| / σ^new
             = 0.071268 / 0.0063
             = 11.312 σ

  Δ(n_σ)     = n_σ_new − n_σ_old
             = 11.312 − 9.622
             = +1.690 σ

Step 4 — Direction (each predicate True under Python evaluation):
  Δ(central) > 0   → canon central MOVES toward POSITIVE
  α_s^FW < 0       → framework prediction is NEGATIVE
  Δ(gap) > 0       → gap WIDENS (signed canon − framework, positive direction)
  Δ(n_σ) > 0       → tension INCREASES from 9.622 σ to 11.312 σ (+1.690 σ worse)

Conclusion: Δ(central) = +0.0068 (canon shifts toward POSITIVE); framework
α_s^FW = −0.068968 is NEGATIVE and UNCHANGED; gap WIDENS by 0.0068
(signed canon − framework); n_σ INCREASES from 9.62 σ (Planck-2018) to
11.31 σ (Aiola-2020), Δ(n_σ) = +1.690 σ; tension HARDENS but framework
prediction is UNCHANGED — only the observational reference moved.
```

The script `s86_w13_p12_alpha_s_canonical_update.py` reproduces this chain at runtime (Step 6 `all_match = True`); deltas vs plan §10 expected values are below 1e-6 absolute (delta_central, gap_old, gap_new, delta_gap) and 1e-2 absolute (n_σ_old, n_σ_new, delta_n_σ — published at 3 sig figs in plan).

**(4) W1a-9 re-emission (S85-W1a-9-RE-EMIT-S86-W13-P12: PASS)**

The S85 W1a-9 7D Fisher script (`s85_w1a_multid_fisher.py`) is **numerically invariant under the pin update** because:

(a) Framework prediction vector `p_FW = (w_0, w_a, n_T, r, β_s, α_s_running, f_NL)` is fixed via canonical sources (S58 `w0_FW = -0.918`, S74 `w_a = 0`, S66 `n_T = -3.024e-3`, S83 `r_CMB_framework = 0.011731`, S84 `β_s = -0.1331`, S63 `α_s_running = 0.00117`, S82 `f_NL = 0.0547`).

(b) LCDM reference vector is the inflation-consistency-relation null `(-1, 0, -r/8, 0, 0, 0, 0)` — the α_s LCDM slot is **0.0 by construction** (vanilla LCDM null), NOT the canonical observational central. The pin update (which moves the canonical observational central from -0.0045 to +0.0023) does **not** change the LCDM reference, so the Fisher pull `(α_s_running − 0)/σ_CMB-S4 = 0.00117/2.1e-3 = 0.557` is unchanged.

(c) Detector 1-σ projections (DESI DR3, LiteBIRD, CMB-S4, SKA-1) are pre-registered detector-noise budgets, independent of which canonical-pin convention is in force.

Re-computed value: `log10(BF_FW/LCDM) = +827.9256` (matches S85 baseline `827.9255704800152` to 1e-3 absolute = baseline-S85-match: True). χ²_total = 3812.69; subset-χ² (excl r, β_s) = 14.86 (S84 cross-check expected 13.9 within 20% tolerance: PASS).

**Auxiliary diagnostic** (under the new pin, for the alpha_s-slot-only canon-vs-framework pull using observational σ):
- old (Planck-2018): pull = (-0.0045 − (−0.068968))/0.0067 = +9.622
- new (Aiola-2020):  pull = (+0.0023 − (−0.068968))/0.0063 = +11.312
- widening: +1.690 σ (matches §10 substitution chain Δ(n_σ)).

This diagnostic is informational only; the gate's PASS verdict turns on the 7D joint log10(BF) ≥ 2 threshold (+827.9 ≫ 2: PASS).

**(5) W1b-3 re-emission (S85-W1b-3-RE-EMIT-S86-W13-P12: PASS)**

The S85 W1b-3 widening-ratio script (`s85_w1b_alpha_s_joint_fisher_correlated.py`) is **numerically invariant under the pin update** because:

(a) Detector σ(α_s) values (σ_S4 = 2.1e-3, σ_HD = 1.5e-3, σ_LB = 1.05e-2, σ_DR3 = 1.0e-2, σ_LISA = 1.0e-1) are forecast projections per individual-detector noise budgets, NOT the canonical observational σ.

(b) The 5×5 correlation matrix C with off-diagonals (ρ_S4-HD = 0.30, ρ_S4-LB = 0.15) is plan-pre-registered (S85 W1b-2 §W1b-2.2) and does not depend on the canonical-pin convention.

(c) The Cauchy-Schwarz widening ratio `σ_corr/σ_diag` depends only on (a) detector σ-vector and (b) C; neither moves under the pin update.

Re-computed value: `ratio = σ_corr/σ_diag = 1.1297479814965643` (matches S85 baseline to 1e-6: `baseline-S85-match: True`). σ_corr = 1.3597e-3, σ_diag = 1.2035e-3, det(C) = 0.8875, identity-sanity ratio (C = I) = 1.000000000000 (within 1e-12). PASS_RATIO = 1.25; ratio 1.1297 ≤ 1.25 → PASS.

**(6) Tension-widening INFO sub-tag**

The pin update WIDENS the framework-vs-canonical-observation tension on α_s:

| Era | Canon central | Canon σ | Framework α_s | n_σ |
|:---|:---|:---|:---|:---|
| Planck-2018 (legacy) | −0.0045 | 0.0067 | −0.068968 | **9.622 σ** |
| Aiola-2020 (canonical) | +0.0023 | 0.0063 | −0.068968 | **11.312 σ** |
| Δ(n_σ) | — | — | UNCHANGED | **+1.690 σ** |

The framework's α_s prediction (−0.068968) is FROZEN by the S50-51 substrate-eigenvalue identity. The pin update is OBSERVATIONAL discipline (which external reference is canonical for tension calculations), not a framework adjustment. Reported as INFO sub-tag in the verdict: tension HARDENS but framework prediction is UNCHANGED — only the observational reference moved.

**Solution-space implication**: the framework's α_s prediction is increasingly discriminable from current data; CMB-S4 / CMB-HD / SKA-1 forecast σ values (which depend on the canonical center for noise modeling) shift accordingly. The 11.31 σ tension under Aiola-2020 puts α_s as the framework's currently-largest single-observable tension (was 9.62 σ under Planck-2018). Whether this is a real prediction failure OR indicates the framework's α_s derivation needs revisiting is a DOWNSTREAM question, not a P12 verdict.

**(7) Dual-SHA**

| Verdict line | audit_sha256 | content_sha256 |
|:---|:---|:---|
| `S86-W13-P12-ALPHA-S-CANONICAL-UPDATE` | `d8b259b33eac2792a32f16b6818dcee03e6541786d374e62a63a81703c83d216` | `cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497` |
| `S85-W1a-9-RE-EMIT-S86-W13-P12` | `41da50b65fea7b5a18d9ef1ed622a73a68eeb27876baeb0d051b4d76cdbbfa01` | `cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497` |
| `S85-W1b-3-RE-EMIT-S86-W13-P12` | `a670ab3e287c554787162bcc363b3388d3d5272b09458c760b2a830c227107dd` | `cfd3bed49e36637fef97d43bd2ce1989dfe448b3e32fd947ecd608d15b9cb497` |

Companion comment rows present for all 3 verdicts (gate-verdicts.md S81+ canonical form). Audit SHAs are unique across the 3 lines (no SHA-hardcoding); content SHA shared because the producing script is the same (this is structurally correct — content_sha pins the script bytes).

**Audit-trail note**: lines 205-210 of `s86_gate_verdicts.txt` retain the first-attempt FAIL verdict (precision-floor bug in `canon_check_ok` aggregator: original tolerance `1e-12` against `alpha_s_inflation_framework + 0.068968` mismatched the 6-sig-fig publication precision of `-0.068968` vs the full-float64 `-0.06896799`). Per S86 W1c-5 all-3-lines-retained discipline, both runs persist. The fix loosened the aggregator's tolerance to `1e-5` (one OOM looser than the 6-sig-fig publication precision, per `.claude/rules/epistemic-discipline.md` Publication-Precision Pre-Registration rule, W1c-8 precedent). The gate's actual physics (legacy retained, new added, diagnostic chain match) was always correct; only my pre-flight aggregator had a publication-precision-floor bug. PROHIBITED_ACTIONS Class-1/6 (convention-shopping / iterate-until-PASS) does NOT apply: the threshold for PASS was never modified and the script's underlying numerics were unchanged.

**(8) Substrate-framing assessment** (per `.claude/rules/phononic-framing.md` + plan §13)

α_s IS the substrate's GGE-acoustic spectral tilt's running — the second derivative of the GGE quasiparticle dispersion at the pivot scale. The framework prediction (−0.068968) is FROZEN; it derives from the substrate's S50-51 spectral identity `α_s = n_s² − 1` with `n_s_canon = 0.9649`, NOT from data fitting or convention choice.

The pin update is OBSERVATIONAL discipline (selecting the post-2018 ACT DR4 + Planck combined reference over the legacy Planck-2018-only reference for tension calculations), NOT a framework adjustment. The widening 9.62 σ → 11.31 σ tension is the substrate's PREDICTION facing a hardening external constraint; future detector data (CMB-S4 by 2028, CMB-HD by 2030, SKA-1 Phase-1 by 2028, SKA-2 by 2030+) will resolve whether the substrate-derived value is correct.

This is NOT framed as "the framework is in 11 σ tension and therefore wrong." It IS framed as "the substrate's α_s prediction is increasingly discriminable; future detector data will resolve whether the substrate-derived value is correct." The substrate prediction is FALSIFIABLE — that is its scientific value, not a defect.

**Artifacts on disk**:
- `computations/_shared/canonical_constants.py` (modified; additive entries at lines 1221-1240; back-compat preserved)
- `computations/session-86/s86_w13_p12_alpha_s_canonical_update.py` (producing script, 39 879 bytes)
- `computations/session-86/s86_w13_p12_alpha_s_canonical_update.json` (P12 audit log, 3 463 bytes)
- `computations/session-86/s86_w13_p12_re_emit_w1a_9.json` (W1a-9 re-emit detail, 2 228 bytes)
- `computations/session-86/s86_w13_p12_re_emit_w1b_3.json` (W1b-3 re-emit detail, 1 492 bytes)
- `computations/session-86/s86_gate_verdicts.txt` (verdict lines 205-216: 3 verdicts × 2 runs × 2 rows each = 12 lines including dual-SHA companion rows; first-run FAIL retained for audit transparency, second-run PASS canonical)"""

text = WP.read_text(encoding="utf-8")
if OLD not in text:
    raise RuntimeError("OLD block not found verbatim in WP file")
if NEW.split("\n", 1)[0] in text and "**Status**: **CLOSED**" in text and "**Verdict**: **PASS**" in text:
    print("WP §W13-5 already CLOSED; no-op")
else:
    text2 = text.replace(OLD, NEW, 1)
    WP.write_text(text2, encoding="utf-8")
    new_size = WP.stat().st_size
    print(f"WP §W13-5 updated; new size = {new_size} bytes")
