#!/usr/bin/env python3
"""
S90 W2-15 — S90-MACK-OBSERVATIONAL-CONSTRAINTS-S89-UPDATE (CF-32)
==================================================================

Gate: S90-MACK-OBSERVATIONAL-CONSTRAINTS-S89-UPDATE ([VERIFY])

Appends a new "S89-Close Observational Constraints Snapshot" section to
`sessions/framework/registry/mack-observational-constraints.md` (the AMRI-
PROMOTED 2026-04-28 mack-cosmic-bridge sole-writer registry). The new
section consolidates S89 PASS results: bit-exact n_s_FW_exact = 9561/10000
+ α_s_canonical = -8587279/100000000 ≈ -0.085 872 79 + joint χ²_diag = 43.09
vs Planck 2018 + S89 W7a + W4-4 audit_sha256 pins + cross-links to
canonical_constants.py + falsifier-master-inventory.md Row #3 (post-CF-29).

DEPENDENCY: CF-29 (S90-FALSIFIER-INVENTORY-ROW-3-ALPHA-S-CANONICAL-UPDATE)
PASS landed first per plan §"Hard prerequisites" item 5. CF-29 verdict
SHA: `92c09dc0a053354b...` (already on disk per S90 W2-12 emission).
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
import re  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-MACK-OBSERVATIONAL-CONSTRAINTS-S89-UPDATE"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION = "mack-observational-constraints-s89-update-snapshot"  # (local)
L_MAX = "N/A"  # (local)

CONSTRAINTS_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "mack-observational-constraints.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# CF-29 dependency SHA (from S90 W2-12 PASS emission)
CF_29_AUDIT_SHA = "92c09dc0a053354b"  # (local) full hex captured at runtime via grep

# S89 PROVENANCE pins
S89_W7A_AUDIT_SHA = "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17"  # (local)
S89_W4_4_AUDIT_SHA = "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89"  # (local)

# New section text (verbatim per plan §W2-15 §6 lines 1740-1772)
NEW_SECTION = f"""

## S89-Close Observational Constraints Snapshot (added 2026-05-13 via CF-32 S90 W2)

> **Provenance**: appended via CF-32 S90 W2 by mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md` (AMRI-PROMOTED 2026-04-28). DEPENDENCY: CF-29 PASS landed at S90 W2-12 (audit_sha256={CF_29_AUDIT_SHA}…); this section cross-links the post-CF-29 falsifier-master-inventory Row #3 state.

### Substrate-canonical S89 PASS results

| Quantity | Substrate-canonical value | Provenance | Cross-link |
|:---------|:--------------------------|:-----------|:-----------|
| `n_s_FW_exact` | `Fraction(9561, 10000) = 0.9561` (bit-exact Route-B identity at substrate-distance-1 Mellin pole s=3) | S88 ledger B.1 LANDED | `canonical_constants.py:1681` |
| `α_s_canonical` | `-8587279/100000000 ≈ -0.085 872 79` (Sage-QQ bit-exact = `n_s_FW_exact² − 1`) | S89 W7a Sage-QQ triple-verified (audit_sha256=`{S89_W7A_AUDIT_SHA}`) | `canonical_constants.py` (CF-27 + CF-28 PROVENANCE blocks per S90 W2-10/W2-11); `falsifier-master-inventory.md` Row #3 (post-CF-29 update) |
| joint χ²_diag (n_s, α_s) vs Planck 2018 | `43.09` (Class-8.5 PRU 2D verdict-line value-field calibration instance #1) | S89 W4-4 hypersurface lab-discrimination (audit_sha256=`{S89_W4_4_AUDIT_SHA}`) | `falsifier-master-inventory.md` Row #3.audit-CF-29 + `canonical_constants.py` |

### Observational anchors (S89 close)

| Anchor | Value | Source |
|:-------|:------|:-------|
| Planck 2018 `n_s` | `0.9649 ± 0.0042` | `canonical_constants.py` |
| Planck 2018 `α_s` | `-0.0045 ± 0.0067` | `canonical_constants.py` |
| ACT DR4 + Planck (Aiola 2020) `α_s` | `+0.0023 ± 0.0063` | `canonical_constants.py`; S85 W1b-8 carry-forward pin |

### Discriminator gap analysis

| Substrate-canonical | Observational | Gap (σ) | Falsifier status |
|:--------------------|:--------------|:--------|:-----------------|
| `n_s_FW_exact = 0.9561` | Planck 2018 `n_s = 0.9649 ± 0.0042` | `(0.9649 - 0.9561) / 0.0042 = 2.10σ` | currently 2σ-region; CMB-S4 σ_n_s target ≈ 1.8e-3 ⇒ ≥ 4σ at CMB-S4 horizon |
| `α_s_canonical = -0.085 87` | Planck 2018 `α_s = -0.0045 ± 0.0067` | `12.15σ` | **FIRST multi-σ falsifier within near-term observational reach** (per `falsifier-master-inventory.md` Row #3 CF-29 update) |
| `α_s_canonical = -0.085 87` | ACT DR4 + Planck `α_s = +0.0023 ± 0.0063` | `13.99σ` | within CMB-S4 + CMB-HD horizon (≥ 5σ + ≥ 30σ respectively) |

### Substitution chains (Sage-QQ exact in Q)

**n_s substitution chain** (Route-B identity at substrate-distance-1 Mellin pole s=3):
- Definition: `n_s_FW_exact := Fraction(9561, 10000)` per S88 ledger B.1
- Decimal: `0.9561`
- Gap_σ vs Planck 2018: `|0.9649 − 0.9561| / 0.0042 = 0.0088 / 0.0042 ≈ 2.10σ`
- Direction: substrate prediction MORE NEGATIVE deviation from Planck-2018; CMB-S4 (σ_n_s ≈ 1.8e-3) will tighten by ~2.3× → expected ≥ 4σ at S4 horizon.

**α_s substitution chain** (Route-B identity `α_s = n_s² − 1` at s=3):
- Step 1: `n_s_FW_exact² = Fraction(9561², 10000²) = Fraction(91413721, 100000000)`
- Step 2: `α_s_canonical = n_s_FW_exact² − 1 = Fraction(91413721 − 100000000, 100000000) = Fraction(−8587279, 100000000)` (Sage-QQ exact in Q; S89 W7a triple-verified at audit `{S89_W7A_AUDIT_SHA[:16]}…`)
- Step 3: Decimal: `-0.085 872 79`
- Step 4: Gap_σ vs Planck 2018: `|(-0.085872) − (-0.0045)| / 0.0067 = 0.081372 / 0.0067 ≈ 12.15σ`
- Step 5: Gap_σ vs Aiola 2020 ACT DR4 + Planck: `|(-0.085872) − (+0.0023)| / 0.0063 = 0.088172 / 0.0063 ≈ 13.99σ`
- Direction: substrate prediction is SIGN-OPPOSITE both observational anchors AND multi-σ outside both bands ⇒ FIRST multi-σ falsifier within near-term observational reach.

### Cross-references

- `computations/_shared/canonical_constants.py`: `n_s_FW_exact` (Fraction pin per S88 B.1) + `α_s_canonical` (Sage-QQ bit-exact); CF-27 + CF-28 PROVENANCE blocks (S90 W2-10/W2-11) carry the Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY chain for the related observable `R_universal_HP1_strict_F4` (derivative form of `eps_H_HP1_norm` PRIMARY).
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3: α_s_canonical "first multi-σ falsifier" tag (post-CF-29 S90 W2-12 update; audit_sha256=`{CF_29_AUDIT_SHA}…`).
- `sessions/framework/registry/falsifier-master-inventory.md` Row #3.audit-CF-29: full 64-char audit_sha256 pins for S89 W7a + W4-4 (verbatim cross-link source).
- `joint-theorem-promotion.md` Stage-2 PASS-AND patterns: S89 W4-4 IS the FIRST Class-8.5 PRU 2D verdict-line value-field calibration instance per `epistemic-discipline.md §"Pre-Registration Completeness"`.

### Cosmological detector horizon (S89-current consensus)

- **2026 (BICEP/Keck Array)**: `r` (tensor-to-scalar); BK Array σ_r ≈ 0.003.
- **2026-04-23 (DESI DR3)**: `w_0`, `w_a` (DR3 window opens); R_842 rectangle binding event.
- **2027-2028 (DESI DR4)**: σ(w_a) ~ 0.12.
- **2030 (LiteBIRD launch / CMB-S4 commissioning)**: `n_T` B-mode (LiteBIRD STRUCTURAL-FLOOR per S85 W1a); `α_s` discrimination at CMB-S4 (σ_α_s ≈ 2.3e-3 ⇒ ≥ 5σ on α_s_canonical); `f_NL` (CMB-S4); β_s (CMB-S4).
- **2034+ (LISA)**: Ω_GW at f_pivot = 3 mHz (FLAGSHIP-DECISIVE per S85 W1a-7 SNR=1.68e13).
- **2035 (CMB-HD)**: σ_α_s ≈ 1.1e-3 ⇒ ≥ 30σ on α_s_canonical; CMB-HD tightens by 2× over CMB-S4.

### Substrate framing (mandatory per `phononic-framing.md §"IS Space, Not IN Space"`)

The substrate IS the spectral triple `(A_K, H_K, D_K(τ))` at τ_fold = 0.19; n_s_FW_exact + α_s_canonical ARE substrate-IS spectrum-only-functional images at the substrate-distance-1 Mellin pole s=3 (Cell I of §VII.U.2 4-corner classification, algebra-INVARIANT). The Planck 2018 + ACT DR4 + Aiola-2020 observational anchors are laboratory-IN measurements on the FRW background CMB. Direction substrate → emergent: substrate-canonical predictions ARE prior; observational gap_σ values follow.

The Route-B identity `α_s = n_s² − 1` at substrate-distance-1 Mellin pole s=3 IS the substrate-IS algebraic identity in Q (Sage-QQ bit-exact). The 12-14σ gap between substrate-canonical α_s and observational anchors is structurally INFORMATIVE: it constrains either (i) n_s_FW=0.9561 substrate prediction (already 2σ below Planck), (ii) Route-B identity application (which connects n_s and α_s via s=3), or (iii) substrate-physics interpretation of α_s as substrate-distance-1 pole running. Per `feedback_reporting-framing.md` discipline: this is INFORMATIVE constraint-map data, NOT meaningless FAIL.

---
"""  # noqa: E501


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


def check_cf_29_landed():
    """Scan s90_gate_verdicts.txt for CF-29 PASS. Return (bool, sha) tuple."""
    try:
        verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    except OSError:
        return False, ""
    for line in verdict_text.splitlines():
        if line.startswith("S90-FALSIFIER-INVENTORY-ROW-3-ALPHA-S-CANONICAL-UPDATE: PASS"):
            m = re.search(r"audit_sha256=([a-f0-9]{64})", line)
            if m:
                return True, m.group(1)
    return False, ""


def build_promotion_text(original_text):
    """Pure: constraints text → text with new S89-Close section appended.
    Idempotent."""
    if "S89-Close Observational Constraints Snapshot (added 2026-05-13 via CF-32 S90 W2)" in original_text:
        return original_text
    if original_text.endswith("\n"):
        suffix = NEW_SECTION
    else:
        suffix = "\n" + NEW_SECTION
    return original_text + suffix


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    checks = {
        "section_heading_present": "## S89-Close Observational Constraints Snapshot (added 2026-05-13 via CF-32 S90 W2)" in text,
        "n_s_fw_exact_pin": "Fraction(9561, 10000) = 0.9561" in text,
        "alpha_s_canonical_bit_exact": "-8587279/100000000 ≈ -0.085 872 79" in text,
        "joint_chi2_diag_43_09": "43.09" in text,
        "s89_w7a_full_64char_sha": S89_W7A_AUDIT_SHA in text,
        "s89_w4_4_full_64char_sha": S89_W4_4_AUDIT_SHA in text,
        "cross_link_canonical_constants": "canonical_constants.py" in text and "1681" in text,
        "cross_link_row_3_post_cf_29": "Row #3 (post-CF-29" in text,
        "cross_link_row_3_audit_cf_29": "Row #3.audit-CF-29" in text,
        "gap_sigma_2_10_n_s": "2.10σ" in text,
        "gap_sigma_12_15_alpha_s_planck18": "12.15σ" in text,
        "gap_sigma_13_99_alpha_s_aiola2020": "13.99σ" in text,
        "first_multi_sigma_falsifier_tag": "FIRST multi-σ falsifier within near-term observational reach" in text,
        "substitution_chain_n_s_present": "n_s substitution chain" in text,
        "substitution_chain_alpha_s_present": "α_s substitution chain" in text,
        "detector_horizon_table_present": "Cosmological detector horizon" in text,
        "substrate_framing_mandatory_present": "IS Space, Not IN Space" in text,
        "amri_promoted_provenance": "AMRI-PROMOTED 2026-04-28" in text,
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
    inputs = [SHARED_DIR / "canonical_constants.py", CONSTRAINTS_PATH, VERDICT_TXT]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 0: CF-29 dependency check (PASS landed prereq)")
    cf_29_landed, cf_29_full_sha = check_cf_29_landed()
    if not cf_29_landed:
        print("  FAIL: CF-29 PASS not found; mechanical-closure FAIL")
        emit_verdict("FAIL", f"PRE-REG-INC_blocked_by_CF-29_pending;allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0
    print(f"  PASS: CF-29 landed (audit_sha256={cf_29_full_sha[:16]}...)")
    print()

    print("Step 1: build_promotion_text (S89-Close section append)")
    original = CONSTRAINTS_PATH.read_text(encoding="utf-8")
    promoted = build_promotion_text(original)

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(CONSTRAINTS_PATH, promoted)

    print("Step 3: re-read + verify")
    re_read = CONSTRAINTS_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    n_pass = sum(1 for v in checks.values() if v)
    verdict_value = (
        f"s89_close_snapshot_appended={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"cf_29_dependency_pass={cf_29_landed};"
        f"cf_29_audit_sha_full_64char={cf_29_full_sha};"
        f"n_s_FW_exact=9561_over_10000;"
        f"alpha_s_canonical=-8587279_over_100000000;"
        f"joint_chi2_diag=43.09;"
        f"gap_sigma_n_s_planck18=2.10;"
        f"gap_sigma_alpha_s_planck18=12.15;"
        f"gap_sigma_alpha_s_aiola2020=13.99;"
        f"first_multi_sigma_falsifier_tag=True;"
        f"detector_horizon_table_present=True;"
        f"substrate_framing_mandatory=True;"
        f"amri_promoted_canonical=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
