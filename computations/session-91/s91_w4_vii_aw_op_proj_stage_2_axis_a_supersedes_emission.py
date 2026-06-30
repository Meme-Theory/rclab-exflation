"""
S91-W2-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A — Option A supersedes-emission

Three prior canonical lines for this gate exist in computations/session-91/s91_gate_verdicts.txt:

  Line 60 (audit_sha256=0279978226f34fb7...): first run, procedural_floor_PASS=False due to
          a false-positive in the substring-match self-check (the script's own forbidden-
          substring search-needles were detected as if they were path references). The
          clause verdicts (a/c/e all PASS) were correct; only the metadata flag was wrong.
  Line 69 (audit_sha256=f83a0ec8c02dcfca...): second run AFTER the procedural-floor check
          was refactored to AST-based file-read-site enumeration, correctly reporting
          procedural_floor_PASS=True. This is the canonical PASS state.
  Line 72 (audit_sha256=f83a0ec8c02dcfca...): third run on the SAME script bytes —
          duplicate of line 69 (sig_5 v3-closure-recovery duplicate audit_sha256
          across two canonical lines for the same gate-ID).

Per .claude/rules/gate-verdicts.md §"Option A — sig_5 remediation pathway under absolute
verdict permanence" (S88 W8-100 user adjudication):
  - Original lines remain on disk (verdict permanence is absolute).
  - This script emits ONE corrective canonical line with a `supersedes=<old_audit_sha>`
    token in its `value=` field, naming BOTH prior audit_sha256 values that should be
    excluded from canonical reading.

Pattern type per the rule's calibration corpus:
  - Line 60: script-bug-corrective (self-check substring false-positive on its own
    search-needles; the AST-based fix at the procedural_floor_check function corrects
    the script bug; substantive verdict unchanged at PASS).
  - Line 72: sig_5-dedup (same audit_sha256 as line 69 because the script bytes
    after the AST fix were identical between runs 2 and 3 — by construction same
    input pins ⇒ same audit_sha256, which is the sig_5 v3-closure failure mode for
    multi-run-of-same-script).

Both are honest in-script corrections; both are excluded from canonical reading via
the explicit supersedes chain emitted here.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO_ROOT / "computations" / "_shared"))

# Canonical-constants import required by math-scripts.md (this script is audit-trail-only;
# the import is for rule compliance and does not consume any framework constant in logic).
from canonical_constants import M_KK  # noqa: F401

GATE_ID = "S91-W2-VII-AW-OP-PROJ-STAGE-2-CROSS-AXIS-INDEPENDENT-VERIFY-AXIS-A"
SCHEME = "stage-2-cross-axis-independent-verify-axis-a-hawking"
CONVENTION = "joint-theorem-promotion-stage-2-pass-and-axis-a-OPTION-A-SUPERSEDES-EMISSION"
L_MAX = 10  # (local) — pin echoed from canonical line per plan §7 PRDR

VERDICT_TXT = REPO_ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"

# Prior audit SHAs being superseded.
SUPERSEDED_PF_FALSE = "0279978226f34fb7801bcb341410eda09f0abeb39be3eb1c29ee805fcd6c9bf5"  # (local) — line 60 PF=False
SUPERSEDED_SIG5_DUP = "f83a0ec8c02dcfca9b506e54c34339b1f0bdb0425d927576de2e3d4e78c110a5"  # (local) — line 72 sig_5 duplicate of line 69

# The CANONICAL substantive state is preserved at line 69 (audit_sha256=f83a0ec8...);
# the corrective emission here EXCLUDES the line-60 PF=False line (script-bug-corrective)
# AND the line-72 duplicate (sig_5 dedup) from canonical reading. After this corrective
# emission, downstream readers see TWO non-superseded canonical lines for this gate:
# (a) line 69 substantive PASS canonical, (b) this corrective supersedes-emission line
# that names lines 60 and 72 as superseded.


def closure_hash(pinmap: dict) -> str:
    items = sorted(pinmap.items())
    payload = "\n".join(f"{k}={v}" for k, v in items)
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main() -> int:
    # Audit pin map for this corrective emission.
    pinmap = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": str(L_MAX),
        "supersedes_pf_false_line_60": SUPERSEDED_PF_FALSE,
        "supersedes_sig5_dup_line_72": SUPERSEDED_SIG5_DUP,
        "canonical_substantive_state_preserved_at_audit_sha":
            "f83a0ec8c02dcfca9b506e54c34339b1f0bdb0425d927576de2e3d4e78c110a5",
        "emission_kind": "OPTION-A-SUPERSEDES-EMISSION",
        "verdict_permanence_preserved": "True",
        "user_adjudication_reference":
            ".claude/rules/gate-verdicts.md_Option_A_S88_W8-100_user_adjudication_2026-05-05",
        "corrective_emission_pattern_types":
            "line_60=script-bug-corrective__line_72=sig_5-dedup",
    }
    audit_sha = closure_hash(pinmap)
    # Content sha = hash over corrective-emission rationale payload.
    content_payload = "|".join(f"{k}={v}" for k, v in sorted(pinmap.items()))
    content_sha = hashlib.sha256(content_payload.encode("utf-8")).hexdigest()

    value_field = (
        f"axis_a=hawking-theorist;option_a_supersedes_emission=True;"
        f"supersedes={SUPERSEDED_PF_FALSE};"
        f"supersedes_sig5_dup={SUPERSEDED_SIG5_DUP};"
        f"canonical_substantive_state_audit_sha=f83a0ec8c02dcfca9b506e54c34339b1f0bdb0425d927576de2e3d4e78c110a5;"
        f"clauses_ace_verdicts=(a:PASS,c:PASS,e:PASS);"
        f"axis_a_composite=PASS;"
        f"verdict_permanence_preserved=True;"
        f"line_60_emission_pattern=script-bug-corrective_pf_check_substring_false_positive_fixed_via_AST_walk;"
        f"line_72_emission_pattern=sig_5_dedup_duplicate_audit_sha_of_line_69_due_to_same_script_bytes_re_run"
    )

    canonical = (
        f"{GATE_ID}: PASS -- "
        f"value='{value_field}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion_dual = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split) "
        f"supersedes={SUPERSEDED_PF_FALSE} "
        f"supersedes_sig5_dup={SUPERSEDED_SIG5_DUP}\n"
    )
    companion_3tuple = (
        f"# sign_verdict=PASS magnitude_verdict=PASS regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; OPTION-A supersedes-emission "
        f"per .claude/rules/gate-verdicts.md §\"Option A — sig_5 remediation pathway "
        f"under absolute verdict permanence\" S88 W8-100 user adjudication 2026-05-05)\n"
    )

    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion_dual)
        fp.write(companion_3tuple)

    print(f"OPTION-A SUPERSEDES-EMISSION for {GATE_ID}")
    print(f"  superseded line-60 audit_sha: {SUPERSEDED_PF_FALSE}")
    print(f"  superseded line-72 audit_sha: {SUPERSEDED_SIG5_DUP}")
    print(f"  canonical-substantive PASS preserved at audit_sha: "
          f"f83a0ec8c02dcfca9b506e54c34339b1f0bdb0425d927576de2e3d4e78c110a5")
    print(f"  this corrective-emission audit_sha: {audit_sha}")
    print(f"  this corrective-emission content_sha: {content_sha}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
