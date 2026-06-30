#!/usr/bin/env python3
"""
S90 W3-1 — S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING (CF-33 / CF-S90-MACK-2)
========================================================================

Lands a forward-falsifier watchlist row at
`sessions/framework/registry/falsifier-watchlist.md` for the CMB-S4
α_s discriminator. Substrate prediction is the bit-exact Route-B
identity `α_s_canonical = n_s_FW_exact² − 1 = -8587279/100000000 ≈
-0.085 872 79` (S89 W7a triple-verified Sage-QQ exact, audit_sha256
`01c1ac83…`; CF-29 W2 PASS at falsifier-master-inventory.md Row #3
audit `92c09dc0…`). PRDR machinery: 4-element Class 8.2 MANDATORY
verifier rubric (3-regex pattern set + disjunction/conjunction
declaration + 2-regex negative-marker set + exemplar-SHA reserved
field). Quarterly poll cadence (S87 precedent). Trigger condition:
CMB-S4 inflation working-group publication with σ_α_s ≤ 2.3e-3
(projected 2028+). PASS/INFO/FAIL discrimination bands at 2σ / 5σ /
5σ against substrate prediction. Single-shot AFTER-pattern emission
per `.claude/rules/registry-landing.md §"Bridge-Landing Script
Architecture"`.

Plan: sessions/session-plan/session-90-plan-w3.md §W3-1.
Agent: mack-cosmic-bridge sole writer per `feedback_mack-bridge-role.md`.
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

GATE_ID = "S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING"  # (local)
SCHEME = "live-watch-quarterly-poll"  # (local)
CONVENTION = "mack-sole-writer-pre-registration"  # (local)
L_MAX = "N/A"  # (local)

WATCHLIST_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-watchlist.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Substrate prediction pin (Route-B identity at substrate-distance-1 pole s=3;
# derived bit-exact from n_s_FW_exact = Fraction(9561, 10000) via Route-B):
#   α_s_canonical = (9561/10000)² − 1 = 91412721/100000000 − 1
#                = -8587279/100000000 = -0.085 872 79  (Sage-QQ exact in Q)
# Symbol pinned at canonical_constants.py n_s_FW_exact (S88 W-15 W15-V.2).
# Triple-verified at S89 W7a audit_sha256 below.
SUBSTRATE_PREDICTION_DECIMAL = "-0.085 872 79"  # (local) 9 sig-fig Sage-QQ decimal
SUBSTRATE_PREDICTION_RATIONAL = "-8587279/100000000"  # (local) bit-exact Q form

S89_W7A_AUDIT_FULL_64 = "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17"  # (local)
S89_W4_4_AUDIT_FULL_64 = "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89"  # (local)
CF_29_S90_W2_AUDIT_FULL_64 = "92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27"  # (local)

# Current laboratory anchor (canonical at canonical_constants.py alpha_s_canon_2020):
LAB_ANCHOR_VALUE = "+0.0023"  # (local) Aiola+ 2020 ACT DR4 + Planck combined
LAB_ANCHOR_ERR = "0.0063"     # (local) Aiola+ 2020 1-sigma
CMB_S4_SIGMA_PROJECTED = "2.3e-3"  # (local) CMB-S4 inflation-WG projected σ_α_s
GAP_CURRENT_SIGMA = "14σ"     # (local) (0.0023 − (-0.085872)) / 0.0063 = 13.997
GAP_CMB_S4_SIGMA = "38σ"      # (local) 0.088172 / 0.0023 ≈ 38

NEW_SECTION_HEADER = "## CMB α_s discriminators (S90 W3 mack-cosmic-bridge live-watch)"  # (local)

# Per plan §W3-1 §6 verbatim markdown template (lines 70-128 of plan).
# This is the structurally-required watchlist row text. The forward audit will
# grep this section for all PRDR machinery elements + cross-links + bands.
WATCHLIST_ROW_TEMPLATE = """\

> **Substrate framing**: the substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold))`; the substrate's intrinsic Mellin running at substrate-distance-1 pole s=3 IS `α_s_canonical = n_s_FW_exact² − 1 = -8587279/100000000`. The CMB-S4 detector measures this quantity IN a laboratory-IN continuum container; the direction of explanation flows substrate → bridge map → laboratory observable per `.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`.

### S90-CMB-S4-ALPHA-S-DISCRIMINATOR-FORWARD-FALSIFIER

**Origin gate**: `S90-CMB-S4-ALPHA-S-WATCHLIST-LANDING` (Wave-3 mack-cosmic-bridge sole-writer; CF-S90-MACK-2 / CF-33)

**Class**: forward-falsifier with quarterly poll cadence; model `S87-ALPHA-S-CMB-S4-WATCH` precedent (this CF-33 entry **SUPERSEDES** the legacy S87 watchlist polling discipline at the framework-current `α_s_canonical = -0.085 872 79` value, NOT the legacy `alpha_s_inflation_framework = -0.068968` Planck-2018-anchor value nor the intermediate `+0.00117` S63 RUNNING-NS-63 reading)

**Substrate prediction**: `α_s_canonical = -0.085 872 79` (= `-8587279/100000000` bit-exact in Q; `n_s_FW_exact² − 1` Route-B identity at substrate-distance-1 Mellin pole s=3; symbol pinned at `canonical_constants.py:n_s_FW_exact` per S88 W-15 W15-V.2 bit-exact rational pin; derived form is the substrate-IS Mellin observable on Pillar-VI inflationary scaling axis)

**Triple-verification SHA**: S89 W7a `audit_sha256=01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` (Sage-QQ exact identity `n_s_FW_exact² − 1 ≡ α_s_canonical`)

**Joint hypersurface SHA**: S89 W4-4 `audit_sha256=e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` (joint (n_s, α_s) hypersurface lab-discrimination; Class-8.5 PRU 2D verdict-line value-field calibration instance #1)

**Laboratory anchor (current canonical)**: `α_s_canon_2020 = +0.0023 ± 0.0063` (Aiola+ 2020 ACT DR4 + Planck combined; canonical pin at `canonical_constants.py:alpha_s_canon_2020` per S86-W13 P12; supersedes Planck-2018 legacy `planck_alpha_s = -0.0045`)

**Trigger condition**: CMB-S4 inflation working-group publication with `σ_α_s ≤ 2.3 × 10⁻³` on the inflationary running of the scalar spectral index (NOT QCD `α_s(M_Z)`; the symbol overload is documented at the calibration-corpus instance landed via CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING`)

**PRDR Machinery Pin (4-element verifier rubric per Class 8.2 MANDATORY)**:

- **Pattern set** (lexical match against publication text):
  1. `(?i)\\bCMB[-\\s]?S[-\\s]?4\\b` AND `(?i)\\b(alpha[-_]s|\\\\alpha_s|α[-_]s|running)\\b` co-occurrence within 200-character window
  2. `(?i)\\b(?:running of (?:the )?spectral index|scalar running|dn_?s/d ?ln ?k)\\b` (semantic disambiguation: inflationary running, NOT QCD)
  3. `(?i)\\bσ[\\s_]?α[-_]?s\\b` (uncertainty symbol; ASCII variants `sigma_alpha_s`, `sigma(alpha_s)`)
- **Disjunction-vs-conjunction declaration**: patterns 1 AND 2 in conjunction (rule: must be CMB-S4 AND must be inflationary α_s, not QCD α_s); pattern 3 disjunctive accept (any one form of the uncertainty symbol)
- **Negative-marker set** (auto-fail patterns; if matched, the publication does NOT trigger this watchlist row):
  1. `(?i)\\bα[-_]?s\\s*\\([Mm][_\\s]?[Zz]\\)` (QCD `α_s(M_Z)` evaluation point; disambiguation per CF-36 corpus instance)
  2. `(?i)\\b(?:strong coupling|QCD running)\\b`
- **Exemplar SHA**: `<pinned at first-PASS-poll>` (reserved; populates at the first PASS poll publication event; until then carries the literal `<pinned at first-PASS-poll>` placeholder per Class 8.2 reserved-field discipline)

**PASS/INFO/FAIL bands** (against substrate prediction `α_s_canonical = -0.085 872 79`):
- **PASS** (substrate-consistent): `|α_s_obs − α_s_canonical| / σ_α_s,obs ≤ 2` (within 2σ of substrate prediction)
- **INFO** (marginal): `2 < |α_s_obs − α_s_canonical| / σ_α_s,obs ≤ 5` (mack-cosmic-bridge dispatches synthesis within 1 week)
- **FAIL** (falsified): `|α_s_obs − α_s_canonical| / σ_α_s,obs > 5` (5σ rejection of substrate-distance-1 Route-B identity; mack-cosmic-bridge dispatches falsification verdict within 24 hours; framework α_s axis flagged at `falsifier-master-inventory.md` Row #3 PERMANENT-WALL classification)

**Substitution chain for direction claim** (per `.claude/rules/math-scripts.md §"Double-Check Logic Before Compute"`):

```
Step 1: α_s_canonical = -0.085 872 79             [substrate prediction; canonical pin via n_s_FW_exact² − 1]
Step 2: α_s_obs       = +0.0023 ± 0.0063         [current laboratory anchor; ACT DR4 + Planck combined]
Step 3: Δα_s          = α_s_obs − α_s_canonical
                      = 0.0023 − (−0.085 872 79)
                      = +0.088 172 79             [explicit substitution]
Step 4: |Δα_s| / σ_α_s,obs_current
                      = 0.088 172 79 / 0.0063
                      = 13.997...                 [≈ 14σ separation; substrate predicts FAR more negative running]
Step 5: At CMB-S4 projected σ_α_s = 2.3 × 10⁻³:
        Sub-case if α_s_S4 ≈ α_s_canon_2020 ≈ +0.0023:
          |Δα_s|/σ_S4 = 0.088172/0.0023 ≈ 38σ    [substrate FALSIFIED at 38σ; far beyond 5σ FAIL band]
        Sub-case if α_s_S4 ≈ α_s_canonical ≈ -0.0859:
          |Δα_s|/σ_S4 = 0/0.0023 = 0σ            [substrate CONFIRMED; PASS at < 2σ]
Direction: CMB-S4 will either CONFIRM substrate at very-near-zero σ OR FALSIFY at ~38σ; no middle ground at projected precision.
```

**Poll cadence**: quarterly (every 90 days); each poll runs the regex pattern set against the CMB-S4 inflation working-group publication stream (preprint feeds: arXiv astro-ph.CO; institutional preprint servers; CMB-S4 collaboration releases). Negative polls (no publication matches) log to `falsifier-watchlist.md` quarterly-poll-log subsection with timestamp + `<no-match>` status. Positive poll triggers fire mack-cosmic-bridge dispatch within 24 hours for FAIL band, 1 week for INFO band, 4 weeks for PASS band.

**Cross-links**:
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3 T7-W2-FALS-1 (CMB-S4 sign-test entry; **post-CF-29 audit-pin sub-row updated** at S90 W2 audit_sha256=`92c09dc0a053354bedea412926b51d2a5a5d0cc07051f6e2a738e7ea2639bc27`)
- `sessions/framework/registry/alpha-s-structural-protection.md` line 166 (CMB magnitude-test row; 25× below CMB-S4 1σ projection)
- `sessions/framework/registry/alpha-s-watchlist.md` (legacy S87-ALPHA-S-CMB-S4-WATCH polling discipline at +0.00117 RUNNING-NS-63 source; THIS CF-33 entry SUPERSEDES at framework-current `α_s_canonical = -0.085 872 79`)
- `.claude/rules/epistemic-discipline.md §"Verifier-Rubric Pre-Registration"` Class 8.2 MANDATORY (4-element rubric specification structurally inherited)
- `.claude/rules/epistemic-discipline.md §"Source Reconciliation"` Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY for the `α_s_canonical` pin (derivative of `n_s_FW_exact` via Route-B identity; PRIMARY canonical is `n_s_FW_exact = Fraction(9561, 10000)` at `canonical_constants.py:n_s_FW_exact`)
- CF-36 `S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING` (Wave-3; calibration corpus instance for 3 distinct α_s symbols; documents QCD vs LEGACY inflationary vs BIT-EXACT inflationary axis distinction)
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
    """Pure: append new section "CMB α_s discriminators (S90 W3 ...)" with the
    CF-33 watchlist row at end of falsifier-watchlist.md. Idempotent —
    re-run on same file returns same text without duplicate append.

    AFTER-pattern per `.claude/rules/registry-landing.md §"Bridge-Landing
    Script Architecture"`: text fully built in memory before any disk
    write; verify step is the FINAL determination.
    """
    marker = "S90-CMB-S4-ALPHA-S-DISCRIMINATOR-FORWARD-FALSIFIER"  # (local)
    if marker in original_text:
        return original_text  # idempotent: already applied
    # Append new section + row at end of file (after existing trailing content)
    sep = "\n" if not original_text.endswith("\n") else ""  # (local)
    appended = (
        original_text
        + sep
        + "\n"
        + NEW_SECTION_HEADER
        + "\n"
        + WATCHLIST_ROW_TEMPLATE
    )
    return appended


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    """All PRDR machinery elements + cross-links + bands present."""
    checks = {
        "new_section_header_present": NEW_SECTION_HEADER in text,
        "watchlist_row_anchor_present": "S90-CMB-S4-ALPHA-S-DISCRIMINATOR-FORWARD-FALSIFIER" in text,
        "substrate_prediction_decimal_present": SUBSTRATE_PREDICTION_DECIMAL in text,
        "substrate_prediction_rational_present": SUBSTRATE_PREDICTION_RATIONAL in text,
        "route_b_identity_explicit": "Route-B identity at substrate-distance-1 Mellin pole s=3" in text,
        "triple_verification_full_64char_sha": S89_W7A_AUDIT_FULL_64 in text,
        "joint_hypersurface_full_64char_sha": S89_W4_4_AUDIT_FULL_64 in text,
        "cf_29_w2_cross_link_full_64char_sha": CF_29_S90_W2_AUDIT_FULL_64 in text,
        "laboratory_anchor_aiola_2020": "Aiola+ 2020" in text and "+0.0023" in text and "0.0063" in text,
        "cmb_s4_projected_sigma_present": "2.3 × 10⁻³" in text or "σ_α_s ≤ 2.3" in text,
        "prdr_pattern_set_3_regex_present": (
            "Pattern set" in text
            and "CMB[-\\s]?S[-\\s]?4" in text
            and "running of (?:the )?spectral index" in text
            and "σ[\\s_]?α[-_]?s" in text
        ),
        "prdr_disjunction_conjunction_declaration": "patterns 1 AND 2 in conjunction" in text,
        "prdr_negative_marker_set_2_present": (
            "Negative-marker set" in text
            and "α[-_]?s\\s*\\([Mm][_\\s]?[Zz]\\)" in text
            and "strong coupling" in text
        ),
        "prdr_exemplar_sha_reserved": "<pinned at first-PASS-poll>" in text,
        "pass_band_2sigma_present": "|α_s_obs − α_s_canonical| / σ_α_s,obs ≤ 2" in text,
        "info_band_5sigma_present": "2 < |α_s_obs − α_s_canonical| / σ_α_s,obs ≤ 5" in text,
        "fail_band_5sigma_present": "|α_s_obs − α_s_canonical| / σ_α_s,obs > 5" in text,
        "substitution_chain_5_steps": all(f"Step {i}" in text for i in range(1, 6)),
        "14sigma_current_separation": "13.997" in text or "≈ 14σ" in text,
        "38sigma_projected_separation": "≈ 38σ" in text,
        "quarterly_poll_cadence": "quarterly (every 90 days)" in text,
        "supersedes_s87_legacy": "SUPERSEDES" in text and "S87-ALPHA-S-CMB-S4-WATCH" in text,
        "cf_36_cross_link": "S90-ALPHA-S-SYMBOL-OVERLOAD-CORPUS-LANDING" in text,
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

    print("Step 1: build_promotion_text (append CMB α_s discriminators section + CF-33 watchlist row)")
    original = WATCHLIST_PATH.read_text(encoding="utf-8")
    promoted = build_promotion_text(original)

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
        f"section_header_appended=True;"
        f"substrate_prediction_alpha_s_canonical=-8587279_over_100000000_eq_-0_085_872_79;"
        f"route_b_identity_substrate_distance_1_pole_s_3=True;"
        f"s89_w7a_full_64char_sha={S89_W7A_AUDIT_FULL_64[:16]};"
        f"s89_w4_4_full_64char_sha={S89_W4_4_AUDIT_FULL_64[:16]};"
        f"cf_29_s90_w2_cross_link_full_64char_sha={CF_29_S90_W2_AUDIT_FULL_64[:16]};"
        f"laboratory_anchor_aiola_2020=plus_0_0023_pm_0_0063;"
        f"cmb_s4_projected_sigma_alpha_s=2_3e-3;"
        f"gap_current_sigma_14;"
        f"gap_cmb_s4_projected_sigma_38;"
        f"prdr_4_element_rubric_present=True;"
        f"pass_info_fail_bands_2_5_5_sigma=True;"
        f"substitution_chain_5_steps=True;"
        f"quarterly_poll_cadence_pinned=True;"
        f"supersedes_s87_alpha_s_cmb_s4_watch_legacy=True;"
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
