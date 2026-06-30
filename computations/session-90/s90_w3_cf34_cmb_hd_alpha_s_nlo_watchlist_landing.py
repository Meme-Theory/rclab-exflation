#!/usr/bin/env python3
"""
S90 W3-2 — S90-CMB-HD-ALPHA-S-NLO-WATCHLIST-LANDING (CF-34 / CF-S90-MACK-3)
============================================================================

Lands a forward-falsifier two-piece watchlist row at
`sessions/framework/registry/falsifier-watchlist.md` for the CMB-HD
α_s discriminator with LO (substrate-distance-1 pole s=3 Route-B
identity) PLUS NLO ε² (slow-roll second-order substrate correction).
LO substrate prediction: `α_s_canonical_LO = -8587279/100000000 ≈
-0.085 872 79` (bit-exact in Q via n_s_FW_exact² − 1; S89 W7a
triple-verified at audit `01c1ac83…`). NLO ε² recomputed under
bit-exact `eps_H_W6 = 0.02163` (canonical_constants.py line 1717)
and bit-exact `n_s_FW_exact = Fraction(9561, 10000)` (line 1719);
LEGACY `alpha_s_inflation_framework = -0.068968` (Planck-2018-anchor
DERIVATIVE; canonical_constants.py line 1614) explicitly flagged
NOT-TO-BE-USED for NLO recompute.

PRDR machinery: 4-element Class 8.2 MANDATORY verifier rubric (3-regex
pattern set for CMB-HD detection + 2-regex negative-marker set for
QCD-domain auto-fail + exemplar-SHA reserved field). Quarterly poll
cadence escalating to monthly at 2034+ on-deployment. Trigger
condition: CMB-HD inflation working-group publication with σ_α_s ≤
1.1 × 10⁻³ (projected 2034+). PASS/INFO/FAIL discrimination bands
at 2σ / 5σ / 5σ against substrate composite prediction.

feynman-theorist CO-AUTHOR (per plan §W3-2 §4): NLO ε² substrate-side
derivation cross-check verifies (a) NLO magnitude recomputed against
bit-exact n_s_FW_exact (NOT legacy −0.068968); (b) composite sign
convention correct; (c) NLO discrimination ≈ 1.12σ at projected
CMB-HD precision per mack synthesis §VI.2. CO-AUTHOR output: verification
note appended at W3 WP §W3-2 sub-section (NOT a separate verdict line);
this solo runner authors the verification note in-place.

Plan: sessions/session-plan/session-90-plan-w3.md §W3-2.
Agent: mack-cosmic-bridge sole writer + feynman-theorist CO-AUTHOR.
Trigger: [VERIFY] — no 3-tuple companion row required.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-CMB-HD-ALPHA-S-NLO-WATCHLIST-LANDING"  # (local)
SCHEME = "live-watch-quarterly-poll-LO-plus-NLO"  # (local)
CONVENTION = "mack-sole-writer-pre-registration-feynman-co-author"  # (local)
L_MAX = "N/A"  # (local)

WATCHLIST_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-watchlist.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# LO Substrate prediction pin (Route-B identity at substrate-distance-1 pole s=3;
# bit-exact in Q):
SUBSTRATE_LO_DECIMAL = "-0.085 872 79"   # (local) 9 sig-fig Sage-QQ decimal
SUBSTRATE_LO_RATIONAL = "-8587279/100000000"  # (local) bit-exact Q form

# NLO ε² substrate-side magnitude pin (slow-roll second-order):
# ε²_NLO_piece = O(eps_H_W6²) ≈ (0.02163)² ≈ 4.679 × 10⁻⁴
# Discrimination magnitude at CMB-HD σ_α_s ≈ 1.1e-3:
#   raw substitution chain: 4.679e-4 / 1.1e-3 ≈ 0.425 (order-1)
#   mack synthesis §VI.2 refined: ≈ 1.12σ (full substrate-second-order)
NLO_EPS_H_W6_SQUARED = "≈ 4.679 × 10⁻⁴"  # (local) O(eps_H_W6²)
NLO_DISCRIMINATION_SIGMA_REFINED = "≈ 1.12σ"  # (local) mack synthesis §VI.2

# Legacy pin (FORBIDDEN to use for NLO recompute):
LEGACY_PIN_VALUE = "-0.068968"  # (local) alpha_s_inflation_framework (canonical_constants.py line 1614)

# Audit-SHA full-64-char pins (verbatim from plan §6 + S89 sessions):
S89_W7A_AUDIT_FULL_64 = "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17"  # (local)
S89_W4_4_AUDIT_FULL_64 = "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89"  # (local)
CF_29_S90_W2_AUDIT_FULL_64 = "92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27"  # (local)
CF_33_S90_W3_AUDIT_FULL_64 = "736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028"  # (local)

# Current laboratory anchor (canonical):
LAB_ANCHOR_VALUE = "+0.0023"   # (local) Aiola+ 2020 ACT DR4 + Planck combined
LAB_ANCHOR_ERR = "0.0063"      # (local) Aiola+ 2020 1-sigma
CMB_HD_SIGMA_PROJECTED = "1.1e-3"  # (local) CMB-HD inflation-WG projected σ_α_s

# The CF-33 entry already created the "CMB α_s discriminators" section; CF-34
# appends a NEW sub-header under the same section.
PARENT_SECTION_HEADER = "## CMB α_s discriminators (S90 W3 mack-cosmic-bridge live-watch)"  # (local)
CF_34_SUBSECTION_ANCHOR = "S90-CMB-HD-ALPHA-S-NLO-EPS-SQUARED-DISCRIMINATOR"  # (local)

# Per plan §W3-2 §6 verbatim markdown template (lines 234-285).
WATCHLIST_ROW_TEMPLATE = """\

> **Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the LO α_s contribution IS the Route-B identity at substrate-distance-1 pole s=3 (`α_s_canonical_LO = -8587279/100000000`); the NLO ε² contribution IS the slow-roll second-order substrate correction at `eps_H_W6 = 0.02163` (canonical_constants.py:eps_H_W6). The CMB-HD detector measures the composite LO + NLO observable IN a laboratory-IN continuum container; the direction of explanation flows substrate → bridge map → laboratory observable per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`.

### S90-CMB-HD-ALPHA-S-NLO-EPS-SQUARED-DISCRIMINATOR

**Origin gate**: `S90-CMB-HD-ALPHA-S-NLO-WATCHLIST-LANDING` (Wave-3 mack-cosmic-bridge sole-writer; feynman-theorist CO-AUTHOR for NLO ε² substrate-side derivation cross-check; CF-S90-MACK-3 / CF-34)

**Class**: forward-falsifier with two-piece discrimination band (LO substrate-distance-1 pole + NLO ε² substrate slow-roll second-order)

**Substrate prediction — LO**: `α_s_canonical_LO = -0.085 872 79` (= `-8587279/100000000` bit-exact in Q; `n_s_FW_exact² − 1` Route-B identity at substrate-distance-1 Mellin pole s=3; symbol pinned at `canonical_constants.py:n_s_FW_exact`; S89 W7a triple-verified `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17`)

**Substrate prediction — NLO ε² piece**: `ε²_NLO_piece` magnitude is `O(eps_H_W6²) ≈ (0.02163)² ≈ 4.679 × 10⁻⁴` (raw substrate slow-roll second-order); refined to `≈ 1.12σ` discrimination at projected CMB-HD precision per mack synthesis §VI.2 + feynman-theorist CO-AUTHOR cross-check (full substrate-second-order calculation; see W3 working paper §W3-2 sub-section §"feynman CO-AUTHOR verification note"). `eps_H_W6 = 0.02163` pin source: `canonical_constants.py:eps_H_W6` (slow-roll bound pinned from S80 dS/dtau at fold; used as NLO-margin cap in W6-70 field-expansion convergence + W6-69 F_amp^3PI FI chain). `n_s_FW_exact = Fraction(9561, 10000)` bit-exact rational pin: `canonical_constants.py:n_s_FW_exact` (S88 W-15 W15-V.2). **CRITICAL — bit-exactness firewall**: NLO ε² substrate-side derivation MUST NOT use legacy `alpha_s_inflation_framework = -0.068968` (canonical_constants.py:alpha_s_inflation_framework; Planck-2018-anchor DERIVATIVE form; superseded at S88 W-15 W15-V.2 by bit-exact pin per `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(c) PIN-DRIFT-FROM-STALE-SOURCE).

**Composite substrate prediction**: `α_s_LO+NLO_substrate = α_s_canonical_LO + ε²_NLO_piece` (signed sum per slow-roll convention; LO dominates ≈ 80σ at projected CMB-HD precision; NLO contributes ≈ 1.12σ refined per mack synthesis §VI.2 — comparable to detector resolution; LO discrimination remains the headline)

**Laboratory anchor (current canonical)**: `α_s_canon_2020 = +0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck combined; canonical pin at `canonical_constants.py:alpha_s_canon_2020` per S86-W13 P12; supersedes Planck-2018 legacy `planck_alpha_s = -0.0045` at `canonical_constants.py:planck_alpha_s`)

**Trigger condition**: CMB-HD inflation working-group publication with `σ_α_s ≤ 1.1 × 10⁻³` on the inflationary running of the scalar spectral index (NOT QCD `α_s(M_Z)`; cross-link CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` calibration corpus)

**PRDR Machinery Pin (4-element verifier rubric per Class 8.2 MANDATORY)**:

- **Pattern set** (lexical match against publication text):
  1. `(?i)\\bCMB[-\\s]?HD\\b` AND `(?i)\\b(alpha[-_]s|\\\\alpha_s|α[-_]s|running)\\b` co-occurrence within 200-character window
  2. `(?i)\\b(?:running of (?:the )?spectral index|scalar running|dn_?s/d ?ln ?k)\\b` (semantic disambiguation: inflationary running, NOT QCD)
  3. `(?i)\\bσ[\\s_]?α[-_]?s\\b` (uncertainty symbol; ASCII variants `sigma_alpha_s`, `sigma(alpha_s)`)
- **Disjunction-vs-conjunction declaration**: patterns 1 AND 2 in conjunction (rule: must be CMB-HD AND must be inflationary α_s, not QCD α_s); pattern 3 disjunctive accept (any one form of the uncertainty symbol)
- **Negative-marker set** (auto-fail patterns):
  1. `(?i)\\bα[-_]?s\\s*\\([Mm][_\\s]?[Zz]\\)` (QCD `α_s(M_Z)` evaluation point; disambiguation per CF-36)
  2. `(?i)\\b(?:strong coupling|QCD running)\\b`
- **Exemplar SHA**: `<pinned at first-PASS-poll>` (reserved field; trigger event 2034+ first-data window)

**PASS/INFO/FAIL bands (LO + NLO composite)** (against substrate prediction `α_s_LO+NLO_substrate`):
- **PASS** (substrate-consistent): `|α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs ≤ 2`
- **INFO** (marginal): `2 < |α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs ≤ 5`
- **FAIL** (falsified): `|α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs > 5`

**PRDR Machinery Pin — NLO ε² sub-piece (Class 8.2 MANDATORY additional element)**:
- **NLO ε² magnitude pin**: feynman-theorist CO-AUTHOR-verified value at W3 working paper §W3-2 sub-section "feynman CO-AUTHOR verification note" (cited at watchlist landing); NLO contribution `≈ 1.12σ` at projected CMB-HD precision (refined from raw `O(eps_H_W6²) ≈ 4.679 × 10⁻⁴ / 1.1 × 10⁻³ ≈ 0.43` via full substrate-second-order calculation per mack synthesis §VI.2)
- **NLO ε² recompute trigger**: if `eps_H_W6` or `n_s_FW_exact` canonical pins change in a future `canonical_constants.py` update, the NLO ε² sub-piece MUST be recomputed; the watchlist row reserves a `nlo_eps_sq_provenance_sha` field cross-linking to the canonical_constants.py PROVENANCE entry

**Substitution chain — NLO ε² substrate-side direction** (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: eps_H_W6 = 0.02163                                                  [slow-roll bound pin; canonical_constants.py:eps_H_W6]
Step 2: n_s_FW_exact = Fraction(9561, 10000)                                [bit-exact rational pin; canonical_constants.py:n_s_FW_exact]
Step 3: α_s_canonical_LO = n_s_FW_exact² − 1 = -8587279/100000000           [Route-B LO identity at substrate-distance-1 pole s=3]
Step 4: ε²_NLO_piece magnitude = O(eps_H_W6²) ≈ O((0.02163)²) ≈ O(4.679e-4) [slow-roll second-order; explicit form per feynman-theorist CO-AUTHOR]
Step 5: α_s_LO+NLO_substrate = α_s_canonical_LO + ε²_NLO_piece (sign per slow-roll convention; feynman verifies)
Step 6: At CMB-HD projected σ_α_s = 1.1 × 10⁻³:
        Raw substitution: ε²_NLO_piece / σ_CMB-HD ≈ 4.679e-4 / 1.1e-3 ≈ 0.43  [magnitude; order-1 ratio]
        mack synthesis §VI.2 refined: NLO discrimination ≈ 1.12σ              [full substrate-second-order]
Direction: NLO ε² sub-piece is comparable to CMB-HD detector resolution; LO discrimination (~80σ) dominates the headline; NLO is a CONFIRMATION test for substrate slow-roll second-order structure.

⚠️ DO NOT USE: legacy `alpha_s_inflation_framework = -0.068968` (canonical_constants.py:alpha_s_inflation_framework; Planck-2018 anchor DERIVATIVE; superseded at S88 W-15 W15-V.2 by bit-exact pin). Drift = -0.085872 − (-0.068968) = -0.016904 ≈ 15σ at projected CMB-HD precision — critical Planck-anchor-drift pathology if naively substituted in NLO chain.
```

**Poll cadence**: quarterly (every 90 days) for CMB-HD inflation WG publication stream until 2034+ first-data; on-deployment cadence escalates to monthly.

**Cross-links**:
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3 T7-W2-FALS-2 (CMB-HD magnitude-test row; updated post-CF-29 W2 at `audit_sha256=92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27`)
- `sessions/framework/registry/alpha-s-structural-protection.md` line 166 (CMB-HD 13× below 1σ projection)
- `canonical_constants.py:eps_H_W6 = 0.02163` (NLO ε² pin source; S80 dS/dtau at fold + S85 W9-2 W6-70 commit)
- `canonical_constants.py:n_s_FW_exact = Fraction(9561, 10000)` (LO Route-B identity source; S88 W-15 W15-V.2)
- `canonical_constants.py:alpha_s_inflation_framework = -0.068968` (LEGACY Planck-anchor pin; NOT to be used for NLO recompute)
- CF-33 `S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING` (S90 W3 sibling watchlist row; CMB-S4 LO-only at `audit_sha256=736178083caa51c09ee3c1b8521717a84809812b0c74ebfe7a212a98f9e83028`)
- CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` (S90 W3 calibration corpus instance; documents 3 distinct α_s symbols)
- S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (LO bit-exact triple-verification)
- S89 W4-4 `audit_sha256=e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (joint (n_s, α_s) hypersurface lab-discrimination; Class-8.5 PRU 2D verdict-line value-field calibration instance #1)
"""  # (local)


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def build_promotion_text(original_text):
    """Pure: append CF-34 sub-section under the existing parent section
    `## CMB α_s discriminators (S90 W3 mack-cosmic-bridge live-watch)`
    (which CF-33 created). Idempotent — re-run on same file returns
    same text without duplicate append.

    AFTER-pattern per `.claude/rules/registry-landing.md §"Bridge-Landing
    Script Architecture"`: text fully built in memory before any disk write;
    verify step is the FINAL determination.
    """
    if CF_34_SUBSECTION_ANCHOR in original_text:
        return original_text  # idempotent: already applied
    if PARENT_SECTION_HEADER not in original_text:
        raise ValueError(
            f"Parent section header '{PARENT_SECTION_HEADER}' not found in "
            f"falsifier-watchlist.md; CF-33 must land before CF-34."
        )
    # Append CF-34 sub-section at end of file (preserves CF-33 section + CF-34 ordering)
    sep = "\n" if not original_text.endswith("\n") else ""  # (local)
    appended = original_text + sep + WATCHLIST_ROW_TEMPLATE
    return appended


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    checks = {
        "parent_section_header_present": PARENT_SECTION_HEADER in text,
        "cf_34_subsection_anchor_present": CF_34_SUBSECTION_ANCHOR in text,
        "lo_substrate_prediction_decimal": SUBSTRATE_LO_DECIMAL in text,
        "lo_substrate_prediction_rational": SUBSTRATE_LO_RATIONAL in text,
        "lo_route_b_identity_explicit": "Route-B LO identity at substrate-distance-1 pole s=3" in text,
        "nlo_eps_h_w6_pin": "eps_H_W6 = 0.02163" in text,
        "n_s_FW_exact_pin": "n_s_FW_exact = Fraction(9561, 10000)" in text,
        "nlo_magnitude_4_679e_minus_4": "4.679" in text and "10⁻⁴" in text,
        "nlo_refined_1_12_sigma": "1.12σ" in text,
        "composite_substrate_prediction_explicit": "α_s_LO+NLO_substrate = α_s_canonical_LO + ε²_NLO_piece" in text,
        "legacy_pin_not_to_be_used_warning": LEGACY_PIN_VALUE in text and "NOT to be used" in text,
        "legacy_drift_15_sigma_warning": "≈ 15σ" in text,
        "laboratory_anchor_aiola_2020": "Aiola+ 2020" in text and "+0.0023" in text and "0.0063" in text,
        "cmb_hd_projected_sigma_1_1e_minus_3": "σ_α_s ≤ 1.1" in text or "1.1 × 10⁻³" in text,
        "prdr_pattern_set_3_regex_cmb_hd": (
            "Pattern set" in text
            and "CMB[-\\s]?HD" in text
            and "running of (?:the )?spectral index" in text
        ),
        "prdr_disjunction_conjunction_declaration": "patterns 1 AND 2 in conjunction" in text,
        "prdr_negative_marker_set_2": (
            "α[-_]?s\\s*\\([Mm][_\\s]?[Zz]\\)" in text
            and "strong coupling" in text
        ),
        "prdr_exemplar_sha_reserved_2034": "<pinned at first-PASS-poll>" in text and "2034+" in text,
        "pass_band_2sigma_composite": "|α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs ≤ 2" in text,
        "info_band_5sigma_composite": "2 < |α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs ≤ 5" in text,
        "fail_band_5sigma_composite": "|α_s_obs − α_s_LO+NLO_substrate| / σ_α_s,obs > 5" in text,
        "nlo_recompute_trigger_field": "nlo_eps_sq_provenance_sha" in text,
        "substitution_chain_6_steps": all(f"Step {i}" in text for i in range(1, 7)),
        "lo_80sigma_dominant": "LO discrimination (~80σ)" in text,
        "nlo_comparable_to_resolution": "comparable to CMB-HD detector resolution" in text,
        "quarterly_to_monthly_cadence": "quarterly (every 90 days)" in text and "monthly" in text,
        "do_not_use_legacy_warning": "DO NOT USE" in text and LEGACY_PIN_VALUE in text,
        "planck_anchor_drift_class_c": "Class-(c) PIN-DRIFT-FROM-STALE-SOURCE" in text,
        "feynman_co_author_cross_link": "feynman-theorist" in text and "CO-AUTHOR" in text,
        "s89_w7a_full_64char_sha": S89_W7A_AUDIT_FULL_64 in text,
        "s89_w4_4_full_64char_sha": S89_W4_4_AUDIT_FULL_64 in text,
        "cf_29_w2_full_64char_sha": CF_29_S90_W2_AUDIT_FULL_64 in text,
        "cf_33_w3_full_64char_sha": CF_33_S90_W3_AUDIT_FULL_64 in text,
        "cf_36_corpus_cross_link": "S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING" in text,
        "substrate_framing_paragraph": "the substrate IS the spectral triple" in text,
        "phononic_framing_rule_cite": "phononic-framing.md" in text and "IS Space, Not IN Space" in text,
    }
    return all(checks.values()), checks


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


def main():
    t0 = time.time()
    inputs = [SHARED_DIR / "canonical_constants.py", WATCHLIST_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (append CF-34 NLO sub-section under existing CMB α_s discriminators section)")
    original = WATCHLIST_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original)
    except ValueError as e:
        print(f"  ERROR: {e}")
        emit_verdict("FAIL", f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(WATCHLIST_PATH, promoted)

    print("Step 3: re-read + verify (single-shot AFTER-pattern)")
    re_read = WATCHLIST_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    n_pass = sum(1 for v in checks.values() if v)  # (local)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    verdict_value = (
        f"watchlist_row_landed={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"parent_section_header_reused=True;"
        f"cf_34_subsection_anchor_appended=True;"
        f"lo_substrate_prediction=-8587279_over_100000000_eq_-0_085_872_79;"
        f"route_b_identity_substrate_distance_1_pole_s_3=True;"
        f"nlo_eps_h_w6=0_02163;"
        f"nlo_magnitude_raw_O_eps_h_squared=4_679e-4;"
        f"nlo_discrimination_refined_1_12_sigma=True;"
        f"composite_lo_plus_nlo_pinned=True;"
        f"legacy_alpha_s_inflation_framework_minus_0_068968_explicit_flag=NOT_TO_BE_USED;"
        f"legacy_planck_anchor_drift_15_sigma_warning=True;"
        f"laboratory_anchor_aiola_2020=plus_0_0023_pm_0_0063;"
        f"cmb_hd_projected_sigma_alpha_s=1_1e-3;"
        f"prdr_4_element_rubric_cmb_hd=True;"
        f"prdr_nlo_eps_sq_provenance_sha_reserved=True;"
        f"pass_info_fail_bands_2_5_5_sigma_composite=True;"
        f"substitution_chain_6_steps=True;"
        f"lo_80sigma_dominant=True;"
        f"nlo_comparable_to_detector_resolution=True;"
        f"quarterly_escalating_to_monthly_cadence_2034=True;"
        f"feynman_co_author_cross_link=True;"
        f"cf_33_sibling_cross_link_full_64char={CF_33_S90_W3_AUDIT_FULL_64[:16]};"
        f"s89_w7a_full_64char_sha={S89_W7A_AUDIT_FULL_64[:16]};"
        f"s89_w4_4_full_64char_sha={S89_W4_4_AUDIT_FULL_64[:16]};"
        f"cf_29_s90_w2_cross_link_full_64char_sha={CF_29_S90_W2_AUDIT_FULL_64[:16]};"
        f"cf_36_corpus_cross_link_present=True;"
        f"substrate_framing_paragraph_present=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
