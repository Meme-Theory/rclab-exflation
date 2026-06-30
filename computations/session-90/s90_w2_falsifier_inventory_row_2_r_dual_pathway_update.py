#!/usr/bin/env python3
"""
S90 W2-14 — S90-FALSIFIER-INVENTORY-ROW-2-R-DUAL-PATHWAY-UPDATE (CF-31)
========================================================================

Gate: S90-FALSIFIER-INVENTORY-ROW-2-R-DUAL-PATHWAY-UPDATE ([VERIFY])

Appends a NEW audit-pin sub-row (Row #2.audit-CF-31) immediately below
Row #2 (r dual-pathway) of `sessions/framework/registry/falsifier-master-
inventory.md`. The new audit-pin contains:
  - BK-Array 2026 pre-reg full 64-char audit_sha256 = `b1eb9e61ece7b0467...`
    (actual gate: S84-BICEP-KECK-2026-PRE-REGISTER at S84 line 45;
    plan §"Hard prerequisites" referenced this as "S87 W4-42" — actual
    location is S84, plan-pin minor inaccuracy disclosed)
  - LiteBIRD STRUCTURAL-FLOOR full 64-char audit_sha256 = `f5a285d8548129b0...`
    (S85-W1a-LITEBIRD-NT-REGISTRY-LANDING at S85 line 24)
  - S89 W7a/W7b/W4-4 cross-link record-discipline annotations (r not affected;
    cross-link only)
  - Mnemonic-vs-exact ratio K=2 corpus annotation per `math-scripts.md
    §"Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3)"`
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

GATE_ID = "S90-FALSIFIER-INVENTORY-ROW-2-R-DUAL-PATHWAY-UPDATE"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION = "falsifier-inventory-row-2-r-dual-pathway-audit-pin-update"  # (local)
L_MAX = "N/A"  # (local)

INVENTORY_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Full 64-char SHAs verified at runtime via grep prior to script-write
BK_ARRAY_2026_SHA = "b1eb9e61ece7b0467e5fcd0050d671cd897a243b7b9d617f47d3f0755f3af6be"  # (local) S84-BICEP-KECK-2026-PRE-REGISTER at s84:45
LITEBIRD_NT_SHA = "f5a285d8548129b053b0c34d54043f7fd00487ee4549d43cf367fff015f6c8b7"  # (local) S85-W1a-LITEBIRD-NT-REGISTRY-LANDING at s85:24
S89_W7A_SHA = "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17"  # (local) S89 Sage-QQ exact n_s_FW²−1
S89_W7B_SHA = "d7826bcb41f873da15d4c6a54cda6035b611d4091cc68da6cdea5adee6ec546f"  # (local) S89 c_sub_corrected anchor verification
S89_W4_4_SHA = "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89"  # (local) S89 joint (n_s, α_s) hypersurface

# Row #2 anchor (unique closing fragment from line 23)
ANCHOR_ROW_2_END = (
    "PAIR-6 cross-ref §W13-7 (P2 BOTH-Pathways landing — "
    "SEQUENCED detector chain + 36.5% scheme-floor flag)"
)  # (local)

# NEW Row #2.audit-CF-31 sub-row (verbatim per plan §W2-14 §6 line 1634)
ROW_2_AUDIT_CF_31 = (
    "| 2.audit-CF-31 | audit pins (Row #2 r dual-pathway "
    "strengthening citation; CF-31 S90 W2 mack-cosmic-bridge "
    "registry-text landing per `feedback_mack-bridge-role.md`) | "
    "BK-Array 2026 pre-reg + LiteBIRD STRUCTURAL-FLOOR + S86 W-3 "
    "structurally-exact σ-reduction K=2 mnemonic-vs-exact discipline | "
    "source: `computations/session-84/s84_gate_verdicts.txt:45` (BK-Array 2026); "
    "`computations/session-85/s85_gate_verdicts.txt:24` (LiteBIRD STRUCTURAL-FLOOR) "
    "[Note: plan-§Hard-prerequisites referenced 'S87 W4-42' for BK-Array 2026; "
    "actual gate is S84-BICEP-KECK-2026-PRE-REGISTER from S84 line 45 — "
    "plan-pin minor inaccuracy honestly disclosed] | "
    "BK-Array 2026 pre-reg: S84-BICEP-KECK-2026-PRE-REGISTER PASS "
    f"audit_sha256=`{BK_ARRAY_2026_SHA}` (4-branch hard pre-registration; "
    "r_CMB_framework = 0.01173 target; BK-Array σ_r ≈ 0.003; σ-discrimination "
    "band [1.6666σ, 2.7776σ] per S86 W-3 structurally-exact 16577/31705 = "
    "0.5229 σ-reduction ratio). "
    "LiteBIRD STRUCTURAL-FLOOR: S85-W1a-LITEBIRD-NT-REGISTRY-LANDING PASS "
    f"audit_sha256=`{LITEBIRD_NT_SHA}` (n_T B-mode geometric-floor at "
    "transit-scale f_transit=8.55e37 Hz; LB 3-yr σ(n_T)=0.0540; joint "
    "LB+CMB-S4 σ(n_T)=0.0654; 54.04 decades separating transit and CMB "
    "k-scales). "
    f"S89 cross-link (record-discipline; r predictions UNAFFECTED): W7a "
    f"`{S89_W7A_SHA[:16]}…` + W7b `{S89_W7B_SHA[:16]}…` + W4-4 "
    f"`{S89_W4_4_SHA[:16]}…` (full 64-char SHAs in this audit-pin sub-row's "
    "verbatim source pin; r_FW = 0.033 + r_CMB_framework = 0.01173 unchanged). "
    "**Mnemonic-vs-exact ratio K=2 corpus annotation per math-scripts.md "
    "§\"Mnemonic-vs-exact ratio discipline (S86 W-3 RULE-3)\"**: the mnemonic "
    "`1/c_sub = 500/1119 = 0.4468` UNDERSTATES the structurally-exact "
    "σ-reduction ratio `16577/31705 = 0.5229` by 14.54% (Path-H invariant "
    "under HypA/HypB switching; only Path-C shifts; this asymmetry is why "
    "the reduction is bounded below `1/c_sub`). Published σ-bands "
    "[1.6666σ, 2.7776σ] at LiteBIRD use the EXACT form 16577/31705; "
    "downstream consumers MUST NOT use the 1/c_sub mnemonic. | "
    "n/a (audit-pin sub-row, not a live-watch envelope) | "
    "n/a (audit-pin sub-row carries no internal-consistency split; Row #2 "
    "primary cell unchanged — r_FW + r_CMB_framework values preserved) | "
    "n/a (audit-pin sub-row; detector horizon inherited from Row #2 = "
    "BK-Array 2026 + LiteBIRD 2030) | GGE-tensor-scalar-partition (inherited) | "
    "substrate-eigenvalue-partition-B1-B2 (inherited) | 10 (inherited) | "
    "`7ab22995c0ba516e` (inherited from Row #2) | `2ab141dd4cab30d3` "
    "(inherited from Row #2; CF-31 audit pins above are full-64-char "
    "strengthening citations) | "
    "S90 W2 CF-31 audit-pin sub-row (additive citation upgrade per "
    "gate-verdicts.md canonical-form rule; mirrors S86 W14-3 row 7.audit "
    "pattern). Per `feedback_mack-bridge-role.md` mack-cosmic-bridge "
    "sole-writer for falsifier-master-inventory.md per AMRI-PROMOTED "
    "2026-04-28. **K=2 corpus advancement** for mnemonic-vs-exact ratio "
    "discipline (W-3 calibration corpus + this CF-31 inheritance "
    "annotation; K=2 corpus saturated at S86 W-3 close; CF-31 propagates "
    "the structurally-exact form to downstream consumers reading Row #2)."
)  # (local)


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
    """Pure: inventory text → text with Row #2.audit-CF-31 sub-row inserted
    immediately below Row #2 (between line 23 and line 24). Idempotent."""
    if "| 2.audit-CF-31 |" in original_text:
        return original_text  # already inserted
    idx = original_text.find(ANCHOR_ROW_2_END)
    if idx == -1:
        raise ValueError("Row #2 end anchor not found in falsifier-master-inventory.md")
    end_of_row_2_line = original_text.find("\n", idx)
    if end_of_row_2_line == -1:
        raise ValueError("Row #2 line not terminated")
    insertion_point = end_of_row_2_line + 1  # right after Row #2 line
    return original_text[:insertion_point] + ROW_2_AUDIT_CF_31 + "\n" + original_text[insertion_point:]


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    checks = {
        "row_2_audit_cf_31_sub_row_present": "| 2.audit-CF-31 |" in text,
        "bk_array_2026_full_64char_sha_present": BK_ARRAY_2026_SHA in text,
        "litebird_full_64char_sha_present": LITEBIRD_NT_SHA in text,
        "s89_w7a_cross_link_short_sha": S89_W7A_SHA[:16] in text,
        "s89_w7b_cross_link_short_sha": S89_W7B_SHA[:16] in text,
        "s89_w4_4_cross_link_short_sha": S89_W4_4_SHA[:16] in text,
        "mnemonic_vs_exact_K2_corpus_present": (
            "1/c_sub = 500/1119 = 0.4468" in text
            and "16577/31705 = 0.5229" in text
            and "14.54%" in text
        ),
        "sigma_discrimination_band_litebird": "[1.6666σ, 2.7776σ]" in text,
        "plan_pin_minor_inaccuracy_disclosed": (
            "plan-§Hard-prerequisites referenced 'S87 W4-42' for BK-Array 2026" in text
        ),
        "s86_w_3_structurally_exact_reduction_cite": (
            "S86 W-3 structurally-exact" in text
        ),
        "math_scripts_K2_discipline_cite": (
            "math-scripts.md" in text
            and "Mnemonic-vs-exact ratio discipline" in text
        ),
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
    inputs = [SHARED_DIR / "canonical_constants.py", INVENTORY_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (Row #2.audit-CF-31 append)")
    original = INVENTORY_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original)
    except ValueError as e:
        print(f"  ERROR: {e}")
        emit_verdict("FAIL", f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(INVENTORY_PATH, promoted)

    print("Step 3: re-read + verify")
    re_read = INVENTORY_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    n_pass = sum(1 for v in checks.values() if v)
    verdict_value = (
        f"row_2_audit_cf_31_appended={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"bk_array_2026_sha={BK_ARRAY_2026_SHA[:16]};"
        f"litebird_nt_sha={LITEBIRD_NT_SHA[:16]};"
        f"s89_w7a_cross_link={S89_W7A_SHA[:16]};"
        f"s89_w7b_cross_link={S89_W7B_SHA[:16]};"
        f"s89_w4_4_cross_link={S89_W4_4_SHA[:16]};"
        f"mnemonic_vs_exact_K2_annotation=16577_over_31705_eq_0_5229_NOT_1_over_c_sub_0_4468_14_54_pct_understatement;"
        f"sigma_band_litebird=1_6666_to_2_7776_sigma;"
        f"plan_pin_S87_W4_42_actual_S84_BK_pre_reg_disclosed=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
