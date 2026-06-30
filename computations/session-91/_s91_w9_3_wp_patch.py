#!/usr/bin/env python3
"""Single-shot Python patcher for session-91-w9-workingpaper.md §W9-3 Results/Verdict.

Replaces the stub Results table + Verdict block + Substrate-framing-runtime-addendum
with populated content per the S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT
gate's actual computed values. One atomic file rewrite; no Edit-tool race.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
WP = ROOT / "sessions" / "session-91" / "session-91-w9-workingpaper.md"

OLD = """### Results (filled at runtime)

| Field | Value |
|:------|:------|
| `bare_n_s_count` | pending |
| `bare_w_0_count` | pending |
| `selected_candidate` | pending |
| `k_advance` | pending |
| `regex_calibration_passes` | pending |
| `scan_roots_sha256` | pending |
| `audit_sha256` | pending |

### Verdict (filled at runtime)

```
S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT: <PASS|FAIL|INFO> -- value=<selected_candidate>+<k_advance> scheme=alpha-s-symbol-overload-K2-advancement-via-second-instance-discovery convention=bare-symbol-citation-without-qualifier-substrate-IS-observable-ambiguity L_max=N/A audit_sha256=<pending> content_sha256=<pending> schema_version=S84+
# audit_sha256_short=<pending> content_sha256_short=<pending> # S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT dual-SHA companion row
# sign_verdict=<pending> magnitude_verdict=<pending> regime_verdict=<pending> # S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT 3-tuple annotation (S87 schema-v2)
```

### Substrate framing (runtime addendum)

(reserved)"""

NEW = """### Results

**Aggregate counts** (regex scan across `sessions/session-{80..90}/**/*.md`; 402 .md files total):

| Field | Value |
|:------|:------|
| `bare_n_s_count` (total) | 2555 |
| `bare_w_0_count` (total) | 1820 |
| `distinct_n_s_sessions` (threshold ≥3) | 11 (S80-S90 all) |
| `distinct_w_0_sessions` (threshold ≥3) | 10 (S81 zero) |
| `selected_candidate` | **BOTH** (Step-5 discriminator: PASS-MANDATORY branch) |
| `k_advance` | K=1 → **K=3 MANDATORY** (direct advancement) |
| `regex_calibration_passes` | 5/5 (T1_bare_ns + T2_ns_canonical + T3_bare_w0 + T4_w0_FW_R842 + T5_separated all PASS) |
| `composite_verdict` | **PASS** |
| `scan_roots_sha256` (manifest of 402 .md files) | `f5ee92550a73b088...` |
| `pinmap_sha256` (sorted SHA-pin map) | `a372a41b2a7a7c0f...` |
| `audit_sha256` (script + sorted pinmap) | `27cf2f992b0f79b5b8da51950cfa2e29d04a4eb28ce16fded2b1d986171fb9a3` |
| `content_sha256` (script bytes only) | `2ea236fe658444904632fae2153299c60dcac682af8c8b0445da0303765ffdaf` |

**Per-session bare-count breakdown** (S80-S90; bare = NOT followed by qualifier within 20-char window):

| Session | Files scanned | `bare_n_s` | `bare_w_0` | Notes |
|:--------|:-------------:|:----------:|:----------:|:------|
| S80 | 2 | 9 | 14 | Both symbols present at modest density |
| S81 | 1 | 1 | 0 | n_s only; w_0 absent |
| S82 | 17 | 65 | 93 | First substantial cross-distinct-session presence (workshop schedule + WP) |
| S83 | 25 | 185 | **509** | Peak w_0 density (DR3 R_842 lockdown + branch-(iv) registration) |
| S84 | 34 | 502 | 466 | Both at peak; comparable magnitudes (R_842 binding + n_s convergence) |
| S85 | 63 | **651** | 336 | Peak n_s density (W1c α_s disambiguation patch + W14 META gates) |
| S86 | 86 | 536 | 232 | Sustained high-density wave-13 + W12-4 DR3 L_max-stability activity |
| S87 | 22 | 102 | 4 | n_s dominates (W4-2 / W6-1 / W11-meta methodology landings); w_0 nearly absent |
| S88 | 99 | 295 | 109 | Wave-23 + W7c stage-2 ramp; n_s outpaces w_0 ~3× |
| S89 | 24 | 145 | 46 | Wave-4 + W5-7 SCHEMATIC PARTIAL-POSITIVE landing + heat-kernel sweeps |
| S90 | 29 | 64 | 11 | CF-36 baseline corpus landing (Instance #6); registry maturation; both decline |
| **TOTAL** | **402** | **2555** | **1820** | distinct-with-presence: n_s = 11/11; w_0 = 10/11 |

**Step-5 discriminator outcome** (per plan §W9-3 Field 6 lines 488-498):

```
n_s_pass (distinct ≥ 3) = True   (distinct_n_s = 11)
w_0_pass (distinct ≥ 3) = True   (distinct_w_0 = 10)
  ⇒ BOTH-candidate PASS-MANDATORY branch
  ⇒ selected_candidate = "BOTH"
  ⇒ k_advance = K=1 → K=3 (DIRECT MANDATORY; skips K=2 SUGGESTION rung)
  ⇒ composite = PASS
```

The BOTH-candidate path is the rarest discriminator outcome: both `n_s` AND `w_0` symbol-overload patterns simultaneously cross the distinct-session threshold (≥3) on the same scanning pass. Pre-S91 the K-counter sat at K=1 SUGGESTION (S90 W3 CF-36 baseline corpus instance #6 with the inaugural α_s symbol). The simultaneous landing of TWO new symbol-overload instances (n_s + w_0) advances K-counter K=1 → K=3 DIRECTLY, triggering MANDATORY promotion per `feedback_rules-compensate-missing-structure.md` K=3 threshold. The α_s symbol-overload sub-tracked K-counter now reaches MANDATORY status; bare-symbol citations in framework documentation (post-S91) FORBIDDEN without disambiguating qualifier within 20-character window.

### Verdict

Verdict line appended to `computations/session-91/s91_gate_verdicts.txt` (canonical + dual-SHA + 3-tuple companion rows per `gate-verdicts.md` S87+ schema-v2):

```
S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT: PASS -- value='selected_candidate=BOTH;k_advance=3;distinct_n_s=11;distinct_w_0=10;bare_n_s_total=2555;bare_w_0_total=1820;regex_calibration_passes=5/5;scan_roots_sha256=f5ee92550a73b088;pinmap_sha256=a372a41b2a7a7c0f' scheme=alpha-s-symbol-overload-K2-advancement-via-second-instance-discovery convention=bare-symbol-citation-without-qualifier-substrate-IS-observable-ambiguity L_max=N/A audit_sha256=27cf2f992b0f79b5b8da51950cfa2e29d04a4eb28ce16fded2b1d986171fb9a3 content_sha256=2ea236fe658444904632fae2153299c60dcac682af8c8b0445da0303765ffdaf schema_version=S87+
# audit_sha256_short=27cf2f992b0f79b5 content_sha256_short=2ea236fe65844490 # S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT dual-SHA companion row (W9a-99 split)
# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID # S91-CF-36-ALPHA-S-SYMBOL-OVERLOAD-K2-ADVANCEMENT 3-tuple annotation (S87 schema-v2)
```

3-tuple semantics:
- `sign_verdict = PASS`: K-counter advancement direction (forward; K=1 → K=3) matches the pre-registered substitution-chain Step-3 direction prediction for any candidate that crosses the distinct-session threshold.
- `magnitude_verdict = PASS`: ABSOLUTE integer-count threshold satisfied at the substantively decisive layer (distinct_n_s = 11 ≥ 3 AND distinct_w_0 = 10 ≥ 3, both well above threshold and beyond plausible single-document inflation).
- `regime_verdict = VALID`: regex calibration self-test 5/5 passes; the qualifier-window detection regime operates within its pre-registered scope of validity (per-symbol qualifier set; 20-char qualifier-absence window).

### Substrate framing (runtime addendum)

Direction of explanation (per `phononic-framing.md §"IS Space, Not IN Space"`):

- **Substrate layer**: the substrate IS the spectral triple `(A_K, H_K, D_K)` at τ_fold. `n_s` IS the closed-form `(M_2/M_0)² − 1` Mellin-cone spectral moment at substrate-distance-1 pole s=3 (Cell I per §VII.U.2 4-corner partition; algebra-INVARIANT spectrum-only functional family). `w_0` IS the Volovik-partition canonical at the FW spectral-action a_0 weight per S58 effacement Γ_eff = 0.99970 (canonical pin `canonical_constants.py:w0_FW = -0.918` line 1590); `w_0_FW_R842 = -0.842454` IS the substrate-compaction branch alternative per `branch-iv-canonical.md` (substrate-natural anchor; conditional on DESI DR3 PASS).
- **Methodology layer (F-image)**: under the layer-functor `F: substrate → methodology → audit` per `epistemic-discipline.md §"Layer-Decomposition"`, the methodology-floor citation drops the disambiguating qualifier and renders the substrate-IS distinct observables as a single bare symbol. The 2555 + 1820 bare citations across S80-S90 are the F-image observation of substrate-IS observable-ambiguity.
- **Audit layer (F²-image)**: the regex detector + K-counter advancement is the F²-image of the methodology-floor pathology — a structural commitment at the rule-file layer to halt plan-freeze on bare-symbol citations (post-S91 MANDATORY).

FORBIDDEN container-inversion: "the bare symbol IS the observable" → INVERT: "the bare symbol IS methodology-floor citation drift; the substrate-IS observable IS the parse-tree expansion on the substrate algebra (`n_s = (M_2/M_0)² − 1` at substrate-distance-1 pole s=3; `w_0 = -0.918` at Volovik-partition canonical OR `w_0 = -0.842454` at substrate-compaction R842 branch — these are DISTINCT substrate-IS observables at DISTINCT branches of the substrate's intrinsic structure)".

The structural-orthogonality cross-link to `cross-pillar-bridge-anatomy.md §"Algebra-axis orthogonality K-counter"` MANDATORY-K=3 is relevant for `n_s`: bare-citation collapses Cell I (algebra-INVARIANT spectrum-only functional at substrate-distance-1 pole s=3) and Cell II (hypothetical substrate-distance-2 pole s=4 reassignment analog of α_s Reading-b). Cross-corner co-primary structures are STRUCTURALLY FORBIDDEN under that K=3 MANDATORY rule, so bare-`n_s` in registry text routes to plan-freeze halt as a 4-corner-classification violation in addition to the symbol-overload K-counter-MANDATORY violation. The two MANDATORY rules close orthogonal pathologies on the same observable-naming axis."""

text = WP.read_text(encoding="utf-8")
if OLD in text:
    new_text = text.replace(OLD, NEW, 1)
    WP.write_text(new_text, encoding="utf-8")
    print(f"Patched {WP.relative_to(ROOT)}: replaced {len(OLD.splitlines())}-line "
          f"stub with {len(NEW.splitlines())}-line populated §W9-3 Results/Verdict/SubFrame.")
else:
    print("Step 1 (Results/Verdict/SubFrame block): already populated; skipping")

# Now extend Carry-forward section — anchor against §W9-3 specifically by
# using the §W9-3 Cross-references block as the unique upstream anchor.
ANCHOR = """- `_alpha_s_symbol_overload_audit.py` (R7) — regex detector extension consumer

### Carry-forward computations (filled at runtime)

(reserved)"""
NEW_ANCHOR = """- `_alpha_s_symbol_overload_audit.py` (R7) — regex detector extension consumer
- `sessions/framework/registry/pru-class-corpus.md §"Instance #6 — S90 W3 CF-36 α_s symbol-overload calibration corpus"` — K=1 SUGGESTION baseline (forward-only; STANDS AS RECORDED per directional-asymmetry rule)
- `canonical_constants.py:w0_FW` line 1590 (Volovik-partition canonical -0.918); `canonical_constants.py:n_s_FW_exact` line 1729 (bit-exact Fraction(9561, 10000))
- Compute artifact: `computations/session-91/s91_w9_cf36_alpha_s_symbol_overload_K2.py` (script); `computations/session-91/s91_w9_cf36_alpha_s_symbol_overload_K2.json` (JSON sidecar with full per-test calibration diagnostics + per-session breakdown)

### Carry-forward computations

- **S92+ `_alpha_s_symbol_overload_audit.py` extension landing** (~0.5 we): extend the R7 regex detector pattern set from `α_s`-only to `{α_s, n_s, w_0}` per this gate's MANDATORY K=3 promotion. Wire the detector into `_source_reconciliation_audit.py` plan-freeze validation pipeline as HARD-HALT at first bare-symbol detection. Pre-registered SHA pin: this gate's `audit_sha256=27cf2f992b0f79b5...`.
- **S92+ pre-S91 documentation lazy-retrofit policy** (~0.2 we): post-S91 GRANDFATHER policy applies. Document the retrofit-at-touch convention in `phononic-framing.md` cross-link, plus a one-time `/weave --update` audit run that produces a report of all pre-S91 `n_s` / `w_0` bare-citation sites for opportunistic editing.
- **S92+ third-instance discovery** (~0.3 we): with K=3 MANDATORY now locked, any FOURTH symbol-overload candidate (e.g., `H_0`, `Ω_m`, `r`, `σ_8`, `T_RH`) that crosses the distinct-session threshold becomes K=4 corpus advancement; no further rule-status changes (already MANDATORY), but the calibration corpus continues to accumulate per the forward-only directional-asymmetry rule of `feedback_rules-compensate-missing-structure.md`."""

text2 = WP.read_text(encoding="utf-8")
if ANCHOR in text2:
    text2 = text2.replace(ANCHOR, NEW_ANCHOR, 1)
    WP.write_text(text2, encoding="utf-8")
    print("Cross-references extended + Carry-forward section populated.")
else:
    print(f"ANCHOR block not found verbatim; leaving as-is. (length={len(ANCHOR)})")
